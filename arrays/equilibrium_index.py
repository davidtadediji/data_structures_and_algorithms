from typing import List

def equilibrium_index(arr: List[int]) -> int:
    """
       Find the equilibrium index of an array.

       Args:
           arr (list[int]): The input array of integers.

       Returns:
           int: The equilibrium index or -1 if no equilibrium index exists.

       Examples:
           >>> equilibrium_index([1, 1, 1, 1, 1])
           2
       """

    total_sum = sum(arr)
    left_sum = 0

    for  i, value in enumerate(arr):
        total_sum -= value
        if left_sum == total_sum:
            return i

        left_sum += value

    return -1



if __name__ == "__main__":

    import doctest
    doctest.testmod()