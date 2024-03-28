def main(l):
    """
    A list of several elements is given. Return this list by adding the reverse.
    Args:
        list1(list): parameter
    Returns:
        list: return answer.
    """
    return l[0::]+l[::-1]
print(main([1,2,3,4,5,6]))