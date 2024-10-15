import sys

# Iterative, bottom-up DP approach


def even_fibonacci(max_value: int):
    ans = 0
    ans_arr = []

    if (max_value == 0):
        return 0
    a = 0
    b = 1
    c = 0

    while (c < max_value):
        c = a + b
        a = b
        b = c

        if (c % 2 == 0):
            ans += c
            ans_arr.append(c)

    print(ans_arr)
    return ans


def main():
    n = 4000000
    print(
        f"Sum of the even fibonacci values under {n} is: {even_fibonacci(n)}")


if __name__ == "__main__":
    main()
