from random import uniform, sample, random
from operator import attrgetter


def fps(population):
    """
    Implementation of Fitness proportionate selection.
    """
    if population.optim == "max":
        # Sum total fitnesses
        total_fitness = sum([i.fitness for i in population])
        # Get a 'position' on the wheel
        spin = uniform(0, total_fitness)
        position = 0
        # Find individual in the position of the spin
        for individual in population:
            position += individual.fitness
            if position > spin:
                return individual
    elif population.optim == "min":
        # Sum total fitnesses
        total_fitness = sum([i.fitness for i in population])
        # Get a 'position' on the wheel using probabilities
        spin = random()
        position = 0
        # Find individual in the position of the spin
        for individual in population:
            # Reversion of the probabilities' order:
            # Division (len(population)-1) made to ensure 0<=probabilities<=1
            position += (1 - individual.fitness / total_fitness) / (len(population) - 1)
            if position > spin:
                return individual

    else:
        raise Exception("No optimization specified (min or max).")


def tournament(population, size=10):
    """
    Implementation of Tournament selection.
    """
    # Select individuals based on tournament size
    tournament = sample(population.individuals, size)
    # Check if the problem is max or min
    if population.optim == "max":
        return max(tournament, key=attrgetter("fitness"))
    elif population.optim == "min":
        return min(tournament, key=attrgetter("fitness"))
    else:
        raise Exception("No optimization specified (min or max).")


def rank(population):
    """
    Implementation of Rank selection.
    """
    # Rank individuals based on optim approach
    if population.optim == "max":
        population.individuals.sort(key=attrgetter("fitness"))
    elif population.optim == "min":
        population.individuals.sort(key=attrgetter("fitness"), reverse=True)
    else:
        raise Exception("No optimization specified (min or max).")

    # Sum all ranks
    total = sum(range(population.size + 1))
    # Get random position
    spin = uniform(0, total)
    position = 0
    # Iterate until spin is found
    for count, individual in enumerate(population):
        position += count + 1
        if position > spin:
            return individual
