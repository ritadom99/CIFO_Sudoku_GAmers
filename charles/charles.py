from random import choice, random
from operator import attrgetter
import numpy as np
import pandas as pd
from copy import deepcopy
import csv
import time
from statistics import mean


class Individual:
    def __init__(
        self,
        representation=None,
        grid_initial=None,
        size=None,
        valid_set=None,
    ):

        if grid_initial is None:
            raise Exception(
                "You need to provide the initial Sudoku puzzle to the class."
            )

        if len(grid_initial) != 81:
            raise Exception(
                "You need to provide a Sudoku puzzle with a 9x9 grid (length of 81)."
            )

        # Check if there is any null in grid_initial
        if any(pd.isnull(grid_initial)):
            # Swap None, NaN and Null in the grid by zero
            def standard_grid(initial_grid):
                standard_grid_list = []

                for i in range(len(initial_grid)):
                    if (initial_grid[i] is None) or (initial_grid[i] is np.nan):
                        standard_grid_list.append(0)
                    else:
                        standard_grid_list.append(initial_grid[i])

                return standard_grid_list

            grid_initial = standard_grid(grid_initial)

        # Check if the grid provided has 17 or more known numbers
        if np.count_nonzero(grid_initial) < 17:
            raise Exception(
                "You need to provide a Sudoku puzzle with at least 17 known numbers."
            )

        # If a representation is not given (we generate a possible Sudoku solution)
        if representation == None:
            new_grid = grid_initial.copy()
            # For each row
            for i in np.arange(0, 81, 9):
                number_missing = valid_set.copy()
                # Check which numbers are missing in this row
                for pos in range(i, i + 9):
                    if grid_initial[pos] in number_missing:
                        number_missing.remove(grid_initial[pos])

                # Choose a random number from the number_missing list for each position == 0
                for pos1 in range(i, i + 9):
                    if grid_initial[pos1] == 0:
                        new_grid[pos1] = choice(number_missing)

                        # Remove the previously selected number from the number_missing list
                        number_missing.remove(new_grid[pos1])

            self.representation = new_grid.copy()

        # If a representation is given
        else:
            self.representation = representation

        self.fitness = self.evaluate()

    def evaluate(self):
        raise Exception("You need to monkey patch the fitness path.")

    def index(self, value):
        return self.representation.index(value)

    def __len__(self):
        return len(self.representation)

    def __getitem__(self, position):
        return self.representation[position]

    def __setitem__(self, position, value):
        self.representation[position] = value

    def __repr__(self):
        return f"Fitness: {self.fitness}"


class Population:
    def __init__(self, grid_initial, size, optim, file_name=int(time.time()), **kwargs):
        self.individuals = []
        self.size = size
        self.optim = optim
        self.grid_initial = grid_initial
        self.gen = 1
        self.file_name = file_name

        for _ in range(size):
            self.individuals.append(
                Individual(
                    grid_initial=grid_initial,
                    size=kwargs["sol_size"],
                    valid_set=kwargs["valid_set"],
                )
            )

    def evolve(self, gens, select, crossover, mutate, co_p, mu_p, elitism, alpha=1):
        for gen in range(gens):
            new_pop = []

            if elitism == True:
                if self.optim == "max":
                    elite = deepcopy(max(self.individuals, key=attrgetter("fitness")))
                elif self.optim == "min":
                    elite = deepcopy(min(self.individuals, key=attrgetter("fitness")))

            while len(new_pop) < self.size:
                parent1, parent2 = select(self), select(self)
                # Crossover
                if random() < co_p:
                    offspring1, offspring2 = crossover(
                        parent1.representation, parent2.representation
                    )
                else:
                    offspring1, offspring2 = (
                        parent1.representation,
                        parent2.representation,
                    )
                # Mutation
                if random() < mu_p:
                    offspring1 = mutate(offspring1, self.grid_initial)
                if random() < mu_p:
                    offspring2 = mutate(offspring2, self.grid_initial)

                new_pop.append(
                    Individual(
                        representation=offspring1, grid_initial=self.grid_initial
                    )
                )
                if len(new_pop) < self.size:
                    new_pop.append(
                        Individual(
                            representation=offspring2, grid_initial=self.grid_initial
                        )
                    )

            if elitism == True:
                if self.optim == "max":
                    least = min(new_pop, key=attrgetter("fitness"))
                elif self.optim == "min":
                    least = max(new_pop, key=attrgetter("fitness"))
                new_pop.pop(new_pop.index(least))
                new_pop.append(elite)

            if self.optim == "max":
                print(
                    f'Gen: {gen+1} / Best Individual: {max(self, key=attrgetter("fitness"))} / Worst Individual: {min(self, key=attrgetter("fitness"))}'
                )
            elif self.optim == "min":
                print(
                    f'Gen: {gen+1} / Best Individual: {min(self, key=attrgetter("fitness"))} / Worst Individual: {max(self, key=attrgetter("fitness"))}'
                )

            self.log()
            self.individuals = new_pop
            # Change crossover rate in each generation if alpha != 1
            co_p *= alpha
            self.gen += 1

        # At the end of the run, print the incomplete Sudoku puzzle and the best individual found
        if self.optim == "max":
            pass
        elif self.optim == "min":
            print("Initial grid: \n", np.array(self.grid_initial).reshape((9, 9)))

            for i in range(self.size):
                if self.individuals[i].fitness == (
                    min(self, key=attrgetter("fitness")).fitness
                ):
                    print(
                        "Final solution: \n",
                        np.array(self.individuals[i].representation).reshape((9, 9)),
                    )
                    break

    def log(self):
        with open(f"{self.file_name}.csv", "a", newline="") as file:
            writer = csv.writer(file)
            all_fitness = []
            for i in self:
                all_fitness.append(i.fitness)

                if i.fitness == (min(self, key=attrgetter("fitness")).fitness):
                    best = i

                elif i.fitness == (max(self, key=attrgetter("fitness")).fitness):
                    worst = i

            writer.writerow(
                [
                    self.gen,
                    best.representation,
                    best.fitness,
                    worst.representation,
                    worst.fitness,
                    mean(all_fitness),
                ]
            )

    def __len__(self):
        return len(self.individuals)

    def __getitem__(self, position):
        return self.individuals[position]

    def __repr__(self):
        return f"Population(size={len(self.individuals)}, individual_size={len(self.individuals[0])})"
