from sklearn.metrics.pairwise import cosine_similarity

vec1 = [1, 2, 3]
vec2 = [4, 5, 6]

cos_sim = cosine_similarity([vec1], [vec2])

print("Cosine Similarity:", cos_sim[0][0])
