"""
hw10.py
"""


def fibonacci(n):
    if n == 1:
        return 1
    elif n == 2:
        return 1
    elif n > 1:
        first = 1
        second = 1
        mylist = [first, second]
        i = 2
        while i < n:
            next_term = first + second
            mylist.append(next_term)
            first = second
            second = next_term
            i = i + 1
        return second
    else:
        return None


def double_investment(principle, rate):
    years = 0
    total = principle
    while total <= principle * 2:
        total = total + total * rate
        years = years + 1
    return years


def syracuse(n):
    total = [n]
    while n != 1:
        if n % 2 == 0:
            even = n / 2
            total.append(even)
            n = even
        else:
            odd = 3 * n + 1
            total.append(odd)
            n = odd
    return total


def goldbach(n):
    if n % 2 != 0:
        return None
    else:
        pass
