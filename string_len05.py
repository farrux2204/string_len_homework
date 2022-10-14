def main(s1,s2):
    """
    Given two strings, s1 and s2. Find their total length.
    Args:
        s1: string
        s2: string
    Returns:
        total length of strings
    """
    s=len(s1)
    a=len(s2)
    y=f'{s}+{a}={s+a}'
    return y
print(main("hi","ki"))