import numpy as np
import pickle
from matplotlib import pyplot as plt

print("This program displays first 10 images from pickled data.\nRequires the file to be in the same folder as this program.\n")

name = input("Enter file name (don't forget .pkl): ")
start_index = int(input("Starting range: "))
end_index = int(input("Finito range: "))

def x():
    data  = pickle.load(open(str(name),'rb'))
    return np.unpackbits(data).astype(int).reshape(-1, 2500)

x = x()

for i in range(start_index, end_index):
    #y = i*1000-1
    #print(y)
    X = x[i].reshape(50,50)
    plt.imshow(X)
    plt.show()
    #plt.savefig(.png)
    #plt.close()
    #plt.clf()
