# print('here')


P = 5 * 10**6
r = 0.05
n = 20
X = (1+r)**n
A = (P*r*X)/(X-1)

print('Month    Instalment    Interest    Principal    Outstanding')

month = 0
outstanding = P

def one_month(month, outstanding):
    # global month
    # global interest
    # global principal
    # global outstanding

    month = month + 1
    interest = outstanding * r
    principal = A - interest
    outstanding = outstanding - principal
    row = '{0:05d}    {1:.2f}    {2:.2f}    {3:.2f}    {4:.2f}'.format(month, A, interest, principal, outstanding)
    print(row)
    return month, outstanding

for w in range(20):
    month, outstanding = one_month(month, outstanding)

