for i in range(0, 1001):
    m1 = max(i % 2 != 0)
    m2 = max(i % 3 != 0)
    m3 = max(i % 5 != 0)
    m4 = max(i % 7 != 0)

print(m1, m2, m3, m4)