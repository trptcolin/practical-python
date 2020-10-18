# bounce.py
#
# Exercise 1.5


def count_bounces(n):
    bounce_count = 0
    height = 100
    while bounce_count < n:
        height *= 0.6
        bounce_count += 1
        print(bounce_count, round(height, ndigits=4))


count_bounces(10)
