# K-Means Clustering

# Importing the libraries

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

#Importing the mall dataset with pandas

#dataset = pd.read_csv('Mall_Customers.csv')
dataset = pd.read_csv('data_nilai_1.csv')
#X = dataset.iloc[:,[3,4]].values
X = dataset.iloc[:,[1,2]].values
plt.scatter(dataset['PENGETAHUAN'], dataset['KETERAMPILAN'])
plt.xlabel('Nilai Pengetahuan')
plt.ylabel('Nilai Keterampilan')
#plt.show()
# Using the elbow method to find the optimal number of clusters

from sklearn.cluster import KMeans
wcss =[]
for i in range (1,11):
    kmeans = KMeans(n_clusters = i, init = 'k-means++', max_iter =300, n_init = 10, random_state = 0)
    kmeans.fit(X)
    wcss.append(kmeans.inertia_)

# Plot the graph to visualize the Elbow Method to find the optimal number of cluster  
plt.plot(range(1,11),wcss)
plt.title('The Elbow Method')
plt.xlabel('Number of clusters')
plt.ylabel('WCSS')
plt.show()
# Applying KMeans to the dataset with the optimal number of cluster
kmeans=KMeans(n_clusters= 5, init = 'k-means++', max_iter = 300, n_init = 10, random_state = 0)
Y_Kmeans = kmeans.fit_predict(X)
dataset['KATEGORY'] = Y_Kmeans
# Visualising the clusters
plt.scatter(X[Y_Kmeans == 0, 0], X[Y_Kmeans == 0,1],s = 100, c='red', label = 'Cluster 1')
plt.scatter(X[Y_Kmeans == 1, 0], X[Y_Kmeans == 1,1],s = 100, c='blue', label = 'Cluster 2')
plt.scatter(X[Y_Kmeans == 2, 0], X[Y_Kmeans == 2,1],s = 100, c='green', label = 'Cluster 3')
plt.scatter(X[Y_Kmeans == 3, 0], X[Y_Kmeans == 3,1],s = 100, c='cyan', label = 'Cluster 4')
plt.scatter(X[Y_Kmeans == 4, 0], X[Y_Kmeans == 4,1],s = 100, c='magenta', label = 'Cluster 5')
plt.scatter(kmeans.cluster_centers_[:,0], kmeans.cluster_centers_[:,1], s = 300, c = 'yellow', label = 'Centroids')    
plt.title('Clusters of Siswa')
plt.xlabel('Nilai Pengetahuan')
plt.ylabel('Nilai Keterampilan')
plt.legend()
plt.show()
conditions = [
    (dataset['KATEGORY']==0),
    (dataset['KATEGORY']==1),
    (dataset['KATEGORY']==2),
    ]
choices = ['Siswa Pintar','Siswa Sedang','Kurang Pintar']
dataset['KATEGORY'] = np.select(conditions, choices)
print(dataset.to_string())


