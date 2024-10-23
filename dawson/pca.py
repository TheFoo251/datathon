from sklearn import datasets, decomposition
import data

frame = data.get_dataframe()
Y = frame["Injury?"]

pca = decomposition.PCA(n_components=3)
pca.fit(X)
X = pca.transform(X)