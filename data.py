import numpy as np
a = np.load("D:\\Documents\\下载\\phi_369.npy")
a = a.reshape([20,20,20])
print(a.mean())