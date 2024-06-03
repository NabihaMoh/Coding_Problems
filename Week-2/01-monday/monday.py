def get_real_floor(n: int) -> int:
    if n <= 0:
        return n
    return n - 1 if n < 13 else n - 2
