N, r, c = map(int, input().split())
result = 0
for i in range(0,N):
    r_quotient, r_reminder = r // (2**(N-i-1)) , r % (2**(N-i-1))
    c_quotient, q_reminder = c // (2**(N-i-1)) , c % (2**(N-i-1))
    result += (((r_quotient * 2) + c_quotient) * 4**(N-i-1))
    r, c = r_reminder, q_reminder
print(result)