import numpy as np
arr=[np.random.uniform(1,20) for i in range(15)]
print(arr)
amatrix=np.reshape(np.ravel(arr),(3,5))
print(np.shape(amatrix))
max_ind = np.argmax(amatrix, axis=1)
row_ind = np.arange(amatrix.shape[0])
multi_ind = np.array([row_ind, max_ind])
linear_ind = np.ravel_multi_index(multi_ind, amatrix.shape)
amatrix.reshape((-1))[linear_ind] = 0
print(amatrix)
