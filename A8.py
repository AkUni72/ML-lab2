vector1 = [1, 0, 1, 1, 0]
vector2 = [1, 1, 1, 0, 0]

f11 = sum(v1 & v2 for v1, v2 in zip(vector1, vector2))
f00 = sum((1 - v1) & (1 - v2) for v1, v2 in zip(vector1, vector2))
f01 = sum((1 - v1) & v2 for v1, v2 in zip(vector1, vector2))
f10 = sum(v1 & (1 - v2) for v1, v2 in zip(vector1, vector2))

jc = f11 / (f01 + f10 + f11)
smc = (f11 + f00) / (f00 + f01 + f10 + f11)

print("Jaccard Coefficient: ",jc)
print("Simple Matching Coefficient: ",smc)
