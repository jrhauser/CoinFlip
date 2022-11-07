import random
#helper method
def factorial(n):
    if n == 1:
        return 1
    else:
        return n * factorial(n-1)

def combinations(n, k):
    if n > k:
        return factorial(n) / (factorial(k) * factorial(n - k))
    else: 
        return 1

#Experiment function

def experiment(n, m, k):
    try:
        1 <= m <= k <= n
    except:
        ValueError
    successes = 0
    givens = 0
    for x in range(0, 10**6):
        results = [None]*n
        for i in range(0, n):
            results[i] = random.randrange(0, 2)
        heads = 0
        for result in results:
            if result == 0:
                heads += 1
        if heads >= m:
            givens += 1
        else:
            continue
        if heads == k:
            successes += 1
    return (successes / givens)

#Calculator function 

def calculator(n, m, k):
    try:
        1 <= m <= k <= n
    except:
        ValueError
    denominator = 0
    for r in range(m, n+1):
        denominator += combinations(n, r)
    return combinations(n, k) / denominator


# Top level code
n  = int(input("Coins flipped (n): "))
m = int(input("How many heads are given? (m): "))
k = int(input("How many heads to succeed (k): "))

while not (1 <= m <= k <= n):
    print("Try again")
    n  = int(input("Coins flipped (n): "))
    m = int(input("How many heads are given? (m): "))
    k = int(input("How many heads to succeed (k): "))

experimentResult = experiment(n, m, k)
print(experimentResult)

calculatorResult = calculator(n, m, k)
print(calculatorResult)

if (abs(calculatorResult - experimentResult) < .001):
    print("The two are approximately equal :)")
else:
    print("They are not approximately equal :(")