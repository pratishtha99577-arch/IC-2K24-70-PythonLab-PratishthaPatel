def get_integer(prompt):

    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print("Invalid input. Please enter an integer.")


def input_matrix():

    matrix = []

    print("Enter the elements of the 3 x 3 matrix:")

    for row in range(3):
        current_row = []

        for column in range(3):
            value = get_integer(
                f"Enter element [{row + 1}][{column + 1}]: "
            )
            current_row.append(value)

        matrix.append(current_row)

    return matrix


def display_matrix(matrix):

    for row in matrix:
        for element in row:
            print(element, end=" ")
        print()


def sum_of_elements(matrix):

    total = 0

    for row in matrix:
        for element in row:
            total += element

    return total


def diagonal_sum(matrix):

    total = 0

    for i in range(3):
        total += matrix[i][i]

    return total


def find_largest(matrix):

    largest = matrix[0][0]

    for row in matrix:
        for element in row:
            if element > largest:
                largest = element

    return largest


def find_smallest(matrix):

    smallest = matrix[0][0]

    for row in matrix:
        for element in row:
            if element < smallest:
                smallest = element

    return smallest


def transpose_matrix(matrix):

    transpose = []

    for column in range(3):
        new_row = []

        for row in range(3):
            new_row.append(matrix[row][column])

        transpose.append(new_row)

    return transpose


matrix = input_matrix()

print("\nOriginal Matrix:")
display_matrix(matrix)

print("\nSum of all elements:", sum_of_elements(matrix))

print("Sum of main diagonal elements:", diagonal_sum(matrix))

print("Largest element:", find_largest(matrix))
print("Smallest element:", find_smallest(matrix))

print("\nTranspose of the Matrix:")
display_matrix(transpose_matrix(matrix))