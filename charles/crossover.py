from random import choice, sample, random
import numpy as np
from copy import deepcopy


def uniform_co(p1, p2, prob_co=0.7):
    """
    Implementation of uniform crossover.

    Each gene (number) is selected randomly from one of the corresponding genes of the parent chromosomes.
    The genes are swapped (or not) according to the prob_co probability.
    """
    offspring1 = deepcopy(p1)
    offspring2 = deepcopy(p2)

    for i in range(len(p1)):
        if random() < prob_co:
            offspring1[i] = p2[i]
            offspring2[i] = p1[i]

    return offspring1, offspring2


def single_point_co(p1, p2):
    """
    Implementation of single point crossover.
    """
    # The possible crossover points can only appear between rows
    co_point_list = np.arange(9, 81, 9)

    # Choose one crossover point
    co_point = choice(co_point_list)

    offspring1 = p1[:co_point] + p2[co_point:]
    offspring2 = p2[:co_point] + p1[co_point:]

    return offspring1, offspring2


def two_point_co(p1, p2):
    """
    Implementation of two point crossover.
    """
    # The possible crossover points can only appear between rows
    co_point_list = list(np.arange(9, 81, 9))

    # Choose two crossover points
    co_points = sample(co_point_list, 2)
    co_points.sort()

    offspring1 = (
        p1[: co_points[0]] + p2[co_points[0] : co_points[1]] + p1[co_points[1] :]
    )
    offspring2 = (
        p2[: co_points[0]] + p1[co_points[0] : co_points[1]] + p2[co_points[1] :]
    )

    return offspring1, offspring2
