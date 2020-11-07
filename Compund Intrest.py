"""
A = P(1 + R/100)^t
Compound Interest = A – P
Where,
A is amount
P is principle amount
R is the rate and
T is the time span

"""
def ci(p,r,t):
    # Calculates compound interest
    Amount = p * (pow((1 + r / 100), t))
    CI = Amount - p
    return CI
print(ci(10000, 10.25, 5) )
