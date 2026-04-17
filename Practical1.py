import math

def binomial_probability(n,k,p):
    combination = math.comb(n,k)
    probability = combination*(p**k)*((1-p)**(n-k))
    return probability

n = 25
p = 0.3

#case 1
k1 = int(input("Exactly How much students Pass: "))
prob = binomial_probability(n,k1,p)
print(f"Probabilit that exactly {k1} Student Pass is : {prob}")
