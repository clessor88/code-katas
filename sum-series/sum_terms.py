def series_sum(n):
    sum = 0.00
    if n < 1:
        return '0.00'
    for i in range(1, n + 1):
        sum += 1.0 / (3 * i - 2)
        if i == n:
            return '{:.2f}'.format(sum)
