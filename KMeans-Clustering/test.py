from sklearn.cluster import KMeans
import pandas as pd
import numpy as np
from sklearn.preprocessing import StandardScaler
from matplotlib import pyplot as plt
df = pd.read_csv('data_nilai_2.csv')
newData = df.drop(['NAMA'],axis=1)
print(newData.to_string())
plt.scatter(newData['PENGETAHUAN'], newData['KETERAMPILAN'])
plt.xlabel('PENGETAHUAN')
plt.ylabel('KETERAMPILAN')
plt.show()
scaler = StandardScaler()
scaler.fit(newData)
df_scaled = scaler.transform(newData)
df_scaled = pd.DataFrame(df_scaled, columns=['PENGETAHUAN','KETERAMPILAN'])
km = KMeans(n_clusters=3)
km
y_predicted = km.fit_predict(df_scaled[['PENGETAHUAN','KETERAMPILAN']])
y_predicted
newData['NAMA'] = df['NAMA']
newData['KATEGORY'] = y_predicted
df1 = newData[newData.KATEGORY==0]
df2 = newData[newData.KATEGORY==1]
df3 = newData[newData.KATEGORY==2]
plt.scatter(df1.PENGETAHUAN,df1['KETERAMPILAN'],color='green')
plt.scatter(df2.PENGETAHUAN,df2['KETERAMPILAN'],color='red')
plt.scatter(df3.PENGETAHUAN,df3['KETERAMPILAN'],color='black')
plt.xlabel('Pengetahuan')
plt.ylabel('Keterampilan')
plt.grid()
plt.show()
conditions = [
    (newData['KATEGORY']==0),
    (newData['KATEGORY']==1),
    (newData['KATEGORY']==2)]
choices = ['Siswa Sedang','Tidak Mampu','Siswa Mampu']
newData['KATEGORY'] = np.select(conditions, choices)
print(newData.to_string())
