import numpy as np
import matplotlib.pyplot as plt
from sklearn.datasets import make_blobs

X, _ = make_blobs(n_samples=100,centers=5)
plt.scatter(X[:,0],X[:,1])
plt.show()

k=5
colors=['pink','blue','green','red','orange']
clustors={}

for ix in range(k):
    center=10.0*(2*np.random.random((X.shape[0],)) -1)
    points=[]

    clustor={
        'center':center,
        'point':points,
        'color':colors[ix]
    }

    clustors[ix]=clustor
print(clustors)