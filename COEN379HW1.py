import math
import random as rand

#Q1
# count = 0
# iterations = int(input("How many iterations would you like to run? "))
# for i in range(0, iterations):
#     x = rand.uniform(0, 2*math.sqrt(2))
#     y = rand.uniform(0, 4)
#     if (x**2 + y**2 - 4)**3 - 108*y**2 <= 0:
#         count+=1
# prob = count/iterations
# print(prob)
# print(4 * prob * 4 * 2*math.sqrt(2))

#Q2
count = 0
n = int(input("Provide a number n representing the amount of possible integers: "))
k = int(input("Provide a number k representing the amount of iterations desired: "))
a = []
for i in range(0, n):
    a.append(0)
for i in range(0, k):
    r = rand.randint(0, n-1)
    a[r] = 1
for i in range(0, n):
    count += a[i]
print("Expected value: " + str(n*(1-((n-1)/n)**k)))
print("Simulation Value: " + str(count))


