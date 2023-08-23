m, n = int(input()), int(input())
m_nechet = m%2+m-1
for i in range(m_nechet, n-1, -2):
    print(i)
