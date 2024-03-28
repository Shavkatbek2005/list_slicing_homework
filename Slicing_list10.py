def main(l,n):
    """
    A list of several elements is given. Return all elements in reverse order except n elements from the beginning.
    Args:
        list1(list): parameter
        n(int): parameter
    Returns:
        list: return answer.
    """
    return l[n::-1]
print(main([1,2,3,4,8,5,6,6],6))