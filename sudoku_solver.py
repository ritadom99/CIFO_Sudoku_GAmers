from charles.charles import Population, Individual
from data.sudoku_puzzles import easy, medium, hard, expert
from charles.fitness_functions import evaluate, evaluate_robust
from charles.selection import fps, tournament, rank
from charles.mutation import (
    swap_mutation,
    multiple_swap_mutation,
    random_mutation,
    intelligent_random_mutation,
    inversion_mutation,
    partial_inversion_mutation,
)
from charles.crossover import single_point_co, two_point_co, uniform_co
import numpy as np

# Monkey Patching
Individual.evaluate = evaluate
# Individual.evaluate = evaluate_robust

# Populations:
# Easy
pop_easy = Population(
    grid_initial=easy,
    size=1000,
    optim="min",
    sol_size=len(easy),
    valid_set=list(np.arange(1, 10)),
)

# Medium
pop_medium = Population(
    grid_initial=medium,
    size=1000,
    optim="min",
    sol_size=len(medium),
    valid_set=list(np.arange(1, 10)),
)

# Hard
pop_hard = Population(
    grid_initial=hard,
    size=1000,
    optim="min",
    sol_size=len(hard),
    valid_set=list(np.arange(1, 10)),
)

# Expert
pop_expert = Population(
    grid_initial=expert,
    size=1000,
    optim="min",
    sol_size=len(expert),
    valid_set=list(np.arange(1, 10)),
)

# Genetic Algorithm:
pop_easy.evolve(
    gens=75,
    select=tournament,
    crossover=two_point_co,
    mutate=swap_mutation,
    co_p=0.7,
    mu_p=0.9,
    elitism=True,
)
