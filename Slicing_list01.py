def main(n):
    """
    A list called numbers is given. Return the items in the even index.
    Args:
        numbers(list): parameter
    Returns:
        list: return answer.
    """
    return n[::2]
print(main([1,2,3,4,5,6]))