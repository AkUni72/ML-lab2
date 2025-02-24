from sklearn.metrics.pairwise import cosine_similarity

def compute_cosine_similarity(vec1, vec2):
    """Computes the Cosine Similarity between two vectors."""
    cos_sim = cosine_similarity([vec1], [vec2])  # Compute similarity
    return cos_sim[0][0]  # Extract scalar value

def main():
    """Main function to execute the program."""
    
    # Define vectors
    vec1 = [1, 2, 3]
    vec2 = [4, 5, 6]

    # Compute cosine similarity
    similarity = compute_cosine_similarity(vec1, vec2)

    # Display result
    print("Cosine Similarity:", similarity)

# Ensure script runs only when executed directly
if __name__ == "__main__":
    main()
