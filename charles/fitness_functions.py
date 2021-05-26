import numpy as np
import math


def evaluate(self):
    """
    This fitness function counts the number of duplicates in the each row, column and box.

    It returns the total number of duplicates, making this a minimization problem.
    """

    def count_duplicates(input_list):
        duplicate_count = 0

        # Count how many numbers of each unique number there is
        count = np.unique(input_list, return_counts=True)[1]

        # Check if there are duplicates
        if len(count[count > 1]) > 0:
            # Check how many duplicates there are in each column
            duplicate_count += sum(count[count > 1]) - len(count[count > 1])

        return duplicate_count

    # Check duplicates on the columns
    duplicate_column = 0
    for i in range(9):
        # Get the numbers in each column
        column = [self.representation[k] for k in np.arange(i, 81, 9)]
        # Count the duplicates in each column
        duplicate_column += count_duplicates(column)

    # Check duplicates on the rows
    duplicate_row = 0
    for i in np.arange(0, 81, 9):
        # Check the numbers in each row
        row = self.representation[i : i + 9]
        # Count the duplicates in each row
        duplicate_row += count_duplicates(row)

    # Get the representation taking into account boxes instead of rows
    list_3_by_3 = []
    initial_box = []
    for i in np.arange(0, 81, 3):
        list_3_by_3.append(self.representation[i : i + 3])  # Create sublists of 3

    for j in range(21):
        x = [j, j + 3, j + 6]  # Get the indexes of the sublists of each box
        initial_box.append([list_3_by_3[k] for k in x])  # Get the sublists of each box

    final_box = np.array(
        initial_box
    ).flatten()  # Collapse the array of the initial_box into 1 dimension

    # Check duplicates on the boxes
    duplicate_box = 0

    for i in np.arange(0, 81, 9):
        # Check the numbers in each box
        box = final_box[i : i + 9]
        # Count the duplicates in each box
        duplicate_box += count_duplicates(box)

    return duplicate_column + duplicate_row + duplicate_box


def evaluate_robust(self):
    """
    This fitness function calculates:
        - the number of duplicates in each row, column and box
        - the absolute value of the subtraction between 45 and the summation for each row, column and box
        - the absolute value of the subtraction between the factorial of 9 and the product for each row, column and box

    It returns a weighted sum of the previous calculations, making this a minimization problem.
    """

    def count_duplicates(input_list):
        duplicate_count = 0

        # Count how many numbers of each unique number there is
        count = np.unique(input_list, return_counts=True)[1]

        # Check if there are duplicates
        if len(count[count > 1]) > 0:
            # Check how many duplicates there are in each column
            duplicate_count += sum(count[count > 1]) - len(count[count > 1])

        return duplicate_count

    def sum_input_list(input_list):
        # The sum of each column, row or box has to be 45 (1+2+3+4+5+6+7+8+9)
        abs_sum = abs(45 - sum(input_list))

        return abs_sum

    def product_input_list(input_list):
        # The product of each column, row or box has to be 9! (9*8*7*6*5*4*3*2*1)
        factorial_9 = math.factorial(9)
        abs_product = abs(factorial_9 - np.prod(input_list))

        return abs_product

    # Check duplicates, absolute value of sum and absolute value of product on the columns
    duplicate_column = 0
    sum_column = 0
    product_column = 0

    for i in range(9):
        # Get the numbers in each column
        column = [self.representation[k] for k in np.arange(i, 81, 9)]

        # Count the duplicates in each column
        duplicate_column += count_duplicates(column)

        # Calculate the substraction of 45 with the summation in each column
        sum_column += sum_input_list(column)

        # Calculate the substraction of factorial of 9 with the product in each column
        product_column += product_input_list(column)

    # Check duplicates, absolute value of sum and absolute value of product on the rows
    duplicate_row = 0
    sum_row = 0
    product_row = 0

    for i in np.arange(0, 81, 9):
        # Check the numbers in each row
        row = self.representation[i : i + 9]

        # Count the duplicates in each row
        duplicate_row += count_duplicates(row)

        # Calculate the substraction of 45 with the summation in each row
        sum_row += sum_input_list(row)

        # Calculate the substraction of factorial of 9 with the product in each row
        product_row += product_input_list(row)

    # Get the representation taking into account boxes instead of rows
    list_3_by_3 = []
    initial_box = []
    for i in np.arange(0, 81, 3):
        list_3_by_3.append(self.representation[i : i + 3])  # Create sublists of 3

    for j in range(21):
        x = [j, j + 3, j + 6]  # Get the indexes of the sublists of each box
        initial_box.append([list_3_by_3[k] for k in x])  # Get the sublists of each box

    final_box = np.array(
        initial_box
    ).flatten()  # Collapse the array of the initial_box into 1 dimension

    # Check duplicates, absolute value of sum and absolute value of product on the boxes
    duplicate_box = 0
    sum_box = 0
    product_box = 0

    for i in np.arange(0, 81, 9):
        # Check the numbers in each box
        box = final_box[i : i + 9]

        # Count the duplicates in each box
        duplicate_box += count_duplicates(box)

        # Calculate the substraction of 45 with the summation in each box
        sum_box += sum_input_list(box)

        # Calculate the substraction of factorial of 9 with the product in each box
        product_box += product_input_list(box)

    fitness_duplicate = 20 * (duplicate_column + duplicate_row + duplicate_box)
    fitness_sum = 10 * (sum_column + sum_row + sum_box)
    fitness_product = round(
        math.sqrt(product_column) + math.sqrt(product_row) + math.sqrt(product_row)
    )

    return fitness_duplicate + fitness_sum + fitness_product
