def main(l,n):
    """
    A list of several elements is given. Return all items from the beginning in n steps.
    Args:
        list1(list): parameter
        n(int): parameter
    Returns:
        list: return answer.
    """
    return l[::n]
print(main([1,2,3,4,5,6,67,7],3))