from random import randint, sample, choice, random
import numpy as np
from copy import deepcopy


def swap_mutation(individual, grid_initial):
    """
    Implementation of swap mutation.

    This randomly chooses one row or column to perform the mutation.
    """
    # Check the possible mutation points (the empty spaces in the initial grid)
    mut_points_list = [i for i in range(len(grid_initial)) if grid_initial[i] == 0]

    # Choose the column or row to perform mutation
    mut_where_list = list(range(9))
    mut_where = choice(mut_where_list)

    # Choose if the mutation will be on the columns or rows
    mut_what = choice([0, 1])

    if mut_what == 0:  # column
        # Get the indexes in the column
        indexes = [k for k in np.arange(mut_where, 81, 9)]

    elif mut_what == 1:  # row
        # Get the indexes in the row
        indexes = list(range(mut_where * 9, mut_where * 9 + 9))

    # Check if each index is in the possible mutation points; if it's not, remove it
    final_indexes = []
    for i in indexes:
        if i in mut_points_list:
            final_indexes.append(i)

    if len(final_indexes) < 2:
        pass  # There needs to be at least 2 indexes to do a swap mutation

    else:
        # Get two mutation points
        mut_points = sample(final_indexes, 2)

        # Swap
        individual[mut_points[0]], individual[mut_points[1]] = (
            individual[mut_points[1]],
            individual[mut_points[0]],
        )

    return individual


def multiple_swap_mutation(individual, grid_initial, prob_mut_each=0.9):
    """
    Implementation of multiple swap mutation.

    This randomly, according to prob_mut_each, chooses which columns or rows to mutate.
    """
    # Check the possible mutation points (the empty spaces in the initial grid)
    mut_points_list = [i for i in range(len(grid_initial)) if grid_initial[i] == 0]

    # Choose the columns or rows to perform mutation
    mut_where_list = []
    for i in range(9):
        if random() < prob_mut_each:
            mut_where_list.append(i)

    # Choose if the mutation will be on the columns or rows
    mut_what = choice([0, 1])

    for each in mut_where_list:
        if mut_what == 0:  # column
            # Get the indexes in the column
            indexes = [k for k in np.arange(each, 81, 9)]

        elif mut_what == 1:  # row
            # Get the indexes in the row
            indexes = list(range(each * 9, each * 9 + 9))

        # Check if each index is in the possible mutation points; if it's not, remove it
        final_indexes = []
        for i in indexes:
            if i in mut_points_list:
                final_indexes.append(i)

        if len(final_indexes) < 2:
            pass  # There needs to be at least 2 indexes to do a swap mutation

        else:
            # Get two mutation points
            mut_points = sample(final_indexes, 2)

            # Swap
            individual[mut_points[0]], individual[mut_points[1]] = (
                individual[mut_points[1]],
                individual[mut_points[0]],
            )

    return individual


def random_mutation(individual, grid_initial, prob_mut_each=0.5):
    """
    Implementation of random mutation.

    This randomly, according to prob_mut_each, chooses which columns or rows to mutate.
    Then, for each column or row, it chooses two random genes (numbers) to mutate.
    For each one of these genes (numbers), mutate it to a random value between 1 and 9.
    """
    # Check the possible mutation points (the empty spaces in the initial grid)
    mut_points_list = [i for i in range(len(grid_initial)) if grid_initial[i] == 0]

    # Choose the columns or rows to perform mutation
    mut_where_list = []
    for i in range(9):
        if random() < prob_mut_each:
            mut_where_list.append(i)

    # Choose if the mutation will be on the columns or rows
    mut_what = choice([0, 1])

    # List of possible numbers
    possible_numbers = list(range(1, 10))

    for each in mut_where_list:
        if mut_what == 0:  # column
            # Get the indexes in the column
            indexes = [k for k in np.arange(each, 81, 9)]

        elif mut_what == 1:  # row
            # Get the indexes in the row
            indexes = list(range(each * 9, each * 9 + 9))

        # Check if each index is in the possible mutation points; if it's not, remove it
        final_indexes = []
        for i in indexes:
            if i in mut_points_list:
                final_indexes.append(i)

        if len(final_indexes) < 2:
            pass  # There needs to be at least 2 indexes

        else:
            # Get two mutation points
            mut_points = sample(final_indexes, 2)

            individual[mut_points[0]] = choice(possible_numbers)
            individual[mut_points[1]] = choice(possible_numbers)

    return individual


def intelligent_random_mutation(individual, grid_initial, prob_mut_each=0.5):
    """
    Implementation of intelligent random mutation.

    This randomly, according to prob_mut_each, chooses which columns or rows to mutate.
    Then, for each column or row, it chooses two random genes (numbers) to mutate.
    For each one of these genes (numbers), mutate it to a random value excluding the grid_inital's values from the row/column that was selected.
    """
    # Check the possible mutation points (the empty spaces in the initial grid)
    mut_points_list = [i for i in range(len(grid_initial)) if grid_initial[i] == 0]

    # Choose the columns or rows to perform mutation
    mut_where_list = []
    for i in range(9):
        if random() < prob_mut_each:
            mut_where_list.append(i)

    # Choose if the mutation will be on the columns or rows
    mut_what = choice([0, 1])

    for each in mut_where_list:
        if mut_what == 0:  # column
            # Get the indexes in the column
            indexes = [k for k in np.arange(each, 81, 9)]

        elif mut_what == 1:  # row
            # Get the indexes in the row
            indexes = list(range(each * 9, each * 9 + 9))

        # Check if each index is in the possible mutation points; if it's not, remove it
        final_indexes = []
        possible_numbers = list(range(1, 10))
        for i in indexes:
            if i in mut_points_list:
                final_indexes.append(i)
            else:
                possible_numbers.remove(grid_initial[i])

        if len(final_indexes) < 2:
            pass  # There needs to be at least 2 indexes to do a swap mutation

        else:
            # Get two mutation points
            mut_points = sample(final_indexes, 2)

            individual[mut_points[0]] = choice(possible_numbers)
            possible_numbers.remove(individual[mut_points[0]])
            individual[mut_points[1]] = choice(possible_numbers)

    return individual


def inversion_mutation(individual, grid_initial, prob_mut_each=0.5):
    """
    Implementation of inversion mutation.

    This randomly, according to prob_mut_each, chooses which columns or rows to mutate.
    """
    individual_mut = deepcopy(individual)

    # Check the possible mutation points (the empty spaces in the initial grid)
    mut_points_list = [i for i in range(len(grid_initial)) if grid_initial[i] == 0]

    # Choose the columns or rows to perform mutation
    mut_where_list = []
    for i in range(9):
        if random() < prob_mut_each:
            mut_where_list.append(i)

    # Choose if the mutation will be on the columns or rows
    mut_what = choice([0, 1])

    for each in mut_where_list:
        if mut_what == 0:  # column
            # Get the indexes in the column
            indexes = [k for k in np.arange(each, 81, 9)]

        elif mut_what == 1:  # row
            # Get the indexes in the row
            indexes = list(range(each * 9, each * 9 + 9))

        # Check if each index is in the possible mutation points; if it's not, remove it
        final_indexes = []
        for i in indexes:
            if i in mut_points_list:
                final_indexes.append(i)

        if len(final_indexes) < 2:
            pass  # There needs to be at least 2 indexes

        else:
            final_indexes.sort()

            for i in range(len(final_indexes)):
                individual_mut[final_indexes[-i - 1]] = individual[final_indexes[i]]

    return individual_mut


def partial_inversion_mutation(individual, grid_initial, prob_mut_each=0.5):
    """
    Implementation of partial inversion mutation.

    This randomly, according to prob_mut_each, chooses which columns or rows to mutate.
    Instead of inverting the entire column or row, it only inverts a part of it, which is randomly selected.
    """
    individual_mut = deepcopy(individual)

    # Check the possible mutation points (the empty spaces in the initial grid)
    mut_points_list = [i for i in range(len(grid_initial)) if grid_initial[i] == 0]

    # Choose the columns or rows to perform mutation
    mut_where_list = []
    for i in range(9):
        if random() < prob_mut_each:
            mut_where_list.append(i)

    # Choose if the mutation will be on the columns or rows
    mut_what = choice([0, 1])

    for each in mut_where_list:
        if mut_what == 0:  # column
            # Get the indexes in the column
            indexes = [k for k in np.arange(each, 81, 9)]

        elif mut_what == 1:  # row
            # Get the indexes in the row
            indexes = list(range(each * 9, each * 9 + 9))

        # Check if each index is in the possible mutation points; if it's not, remove it
        final_indexes = []
        for i in indexes:
            if i in mut_points_list:
                final_indexes.append(i)

        if len(final_indexes) < 2:
            pass  # There needs to be at least 2 indexes

        else:
            # Choose how many indexes to invert, with uniform probability, between 2 and the length of final_indexes
            number_indexes = randint(2, len(final_indexes))

            # Choose which indexes to invert
            inversion_final_indexes = sample(final_indexes, number_indexes)
            inversion_final_indexes.sort()

            for i in range(len(inversion_final_indexes)):
                individual_mut[inversion_final_indexes[-i - 1]] = individual[
                    inversion_final_indexes[i]
                ]

    return individual_mut
