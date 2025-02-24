import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
from sklearn.metrics.pairwise import cosine_similarity
from sklearn.preprocessing import MinMaxScaler

def load_data(file_name, sheet_name):
    """Loads the dataset from an Excel file."""
    data = pd.ExcelFile(file_name)
    return data.parse(sheet_name)

def normalize_data(data):
    """Normalizes numeric columns using Min-Max Scaling."""
    scaler = MinMaxScaler()  # Initialize the Min-Max Scaler
    
    # Select only numeric columns for normalization
    numeric_data = data.select_dtypes(include='number')
    
    # Apply Min-Max Scaling and create a new DataFrame with the same column names
    normalized_data = pd.DataFrame(scaler.fit_transform(numeric_data), columns=numeric_data.columns)
    
    return normalized_data

def compute_cosine_similarity(data, num_samples=20):
    """Computes the Cosine Similarity matrix for the first 'num_samples' rows."""
    sample_vectors = data.iloc[:num_samples].values  # Extract sample vectors
    return cosine_similarity(sample_vectors)  # Compute cosine similarity

def plot_heatmap(similarity_matrix):
    """Plots a heatmap of the Cosine Similarity matrix."""
    plt.figure(figsize=(10, 8))  # Set figure size
    sns.heatmap(similarity_matrix, annot=True, cmap="coolwarm")  # Create heatmap
    plt.title('Heatmap of Cosine Similarities')  # Set title
    plt.show()  # Display heatmap

def main():
    """Main function to execute the program."""
    file_name = 'Lab Session Data.xlsx'  # Excel file name
    sheet_name = 'thyroid0387_UCI'  # Sheet name

    # Load dataset
    thyroid_data = load_data(file_name, sheet_name)

    # Normalize numeric data
    thyroid_data_normalized = normalize_data(thyroid_data)

    # Compute Cosine Similarity matrix
    cos_sim_matrix = compute_cosine_similarity(thyroid_data_normalized, num_samples=20)

    # Plot heatmap
    plot_heatmap(cos_sim_matrix)

# Ensure script runs only when executed directly
if __name__ == "__main__":
    main()
