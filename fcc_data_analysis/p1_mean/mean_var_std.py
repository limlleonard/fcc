import numpy as np

def calculate(lst1):
    if len(lst1)!=9:
        raise ValueError('List must contain nine numbers.')
    arr1=np.array(lst1)
    arr1=arr1.reshape((3,3))
    dct1={}
    dct1['mean']=[list(np.mean(arr1, axis=0)), list(np.mean(arr1, axis=1)), np.mean(arr1)]
    dct1['variance']=[list(np.var(arr1, axis=0)), list(np.var(arr1, axis=1)), np.var(arr1)]
    dct1['standard deviation']=[list(np.std(arr1, axis=0)), list(np.std(arr1, axis=1)), np.std(arr1)]
    dct1['max']=[list(np.max(arr1, axis=0)), list(np.max(arr1, axis=1)), np.max(arr1)]
    dct1['min']=[list(np.min(arr1, axis=0)), list(np.min(arr1, axis=1)), np.min(arr1)]
    dct1['sum']=[list(np.sum(arr1, axis=0)), list(np.sum(arr1, axis=1)), np.sum(arr1)]
    return dct1

if __name__ == "__main__":
    lst1=[i for i in range(9)]
    print(calculate(lst1))