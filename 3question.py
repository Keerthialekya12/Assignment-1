import numpy as np
from numpy import linalg as la
arr=np.array([[3,-2],[1,0]])
w,v=la.eig(arr)
print("eign values:",w)
print("eign vectors:",v)
