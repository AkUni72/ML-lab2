import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
from sklearn.metrics.pairwise import cosine_similarity
from sklearn.preprocessing import MinMaxScaler

data = pd.ExcelFile('Lab Session Data.xlsx')
thyroid_data = data.parse('thyroid0387_UCI')

scaler = MinMaxScaler()
thyroid_data_normalized = pd.DataFrame(scaler.fit_transform(thyroid_data.select_dtypes(include='number')),
    columns=thyroid_data.select_dtypes(include='number').columns)

sample_vectors = thyroid_data_normalized.iloc[:20].values
cos_sim_matrix = cosine_similarity(sample_vectors)

sns.heatmap(cos_sim_matrix, annot=True, cmap="coolwarm")
plt.title('Heatmap of Cosine Similarities')
plt.show()
