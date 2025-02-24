def compute_coefficients(vector1, vector2):
    """Computes Jaccard Coefficient and Simple Matching Coefficient for two binary vectors."""
    
    # Compute necessary frequencies
    f11 = sum(v1 & v2 for v1, v2 in zip(vector1, vector2))  # Count where both are 1
    f00 = sum((1 - v1) & (1 - v2) for v1, v2 in zip(vector1, vector2))  # Count where both are 0
    f01 = sum((1 - v1) & v2 for v1, v2 in zip(vector1, vector2))  # Count where v1=0, v2=1
    f10 = sum(v1 & (1 - v2) for v1, v2 in zip(vector1, vector2))  # Count where v1=1, v2=0

    # Calculate Jaccard Coefficient
    jc = f11 / (f01 + f10 + f11) if (f01 + f10 + f11) != 0 else 0

    # Calculate Simple Matching Coefficient
    smc = (f11 + f00) / (f00 + f01 + f10 + f11) if (f00 + f01 + f10 + f11) != 0 else 0

    return jc, smc

def main():
    """Main function to execute the program."""
    
    # Define binary vectors
    vector1 = [1, 0, 1, 1, 0]
    vector2 = [1, 1, 1, 0, 0]

    # Compute coefficients
    jc, smc = compute_coefficients(vector1, vector2)

    # Display results
    print("Jaccard Coefficient:", jc)
    print("Simple Matching Coefficient:", smc)

# Ensure script runs only when executed directly
if __name__ == "__main__":
    main()
