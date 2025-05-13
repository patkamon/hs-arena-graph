def find_median(numbers):
    """
    Calculates the median of a list of numbers.

    Args:
      numbers: A list of numbers.

    Returns:
      The median of the numbers, or None if the list is empty.
    """
    sorted_numbers = sorted(numbers)
    length = len(sorted_numbers)

    if length == 0:
        return None
    elif length % 2 == 1:
        # Odd length: median is the middle element
        middle_index = (length - 1) // 2
        return sorted_numbers[middle_index]
    else:
        # Even length: median is the average of the two middle elements
        middle_index_1 = length // 2 - 1
        middle_index_2 = length // 2
        return (sorted_numbers[middle_index_1] + sorted_numbers[middle_index_2]) / 2