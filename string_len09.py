def main(num1, num2):
    """
    Given two non-negative integers, num1 and num2 represented as string.
    Return the sum of num1 and num2 as a string.

    Args:
        num1: str
        num2: str
    Returns:
        str: answer
    """
    num1=int(num1)
    num2=int(num2)
    answer=num1+num2
    int(answer)==answer
    return str(answer)
print(main("19","22"))
