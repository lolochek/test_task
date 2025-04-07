def jumper(nums):
    """
        Determines whether it's possible to reach the last index of the list,
        starting from the first index, where each element represents the maximum
        jump length at that position.

        Args:
            nums (List[int]): List of non-negative integers representing jump lengths.

        Returns:
            bool: True if the last index is reachable, False otherwise.
    """
    max_position = 0   # the furthest index of list we can currently reach

    for position in range(len(nums)):
        if max_position < position:  # check if our current position is beyond our maximum reachable position
            return False

        max_position=max(max_position, position+nums[position])  # update the furthest reachable position

        if max_position >= len(nums) - 1:  # check if we've reached or surpassed the last index
            return True

    return False

if __name__=='__main__':
    my_input = input('Enter a list of non-negative integers (e.g. 2 3 1 1 4): ').split()
    my_nums = list(map(int, my_input))
    print(jumper(my_nums))
