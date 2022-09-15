import numpy as np

def calculate(list):
    
    if len(list) != 9 :
        raise ValueError('List must contain nine numbers.')

    arr = np.array(list).reshape(3, 3)

    calculations = {
        'mean': [ np.mean(arr, axis=0), np.mean(arr, axis=1), np.mean(arr, ) ],
        'variance': [ np.var(arr, axis=0), np.var(arr, axis=1), np.var(arr) ],
        'standard deviation' : [ arr.std(axis=0), arr.std(axis=1), arr.std() ],
        'min': [ arr.min(axis=0), arr.min(axis=1), arr.min() ],
        'max': [ arr.max(axis=0), arr.max(axis=1), arr.max() ],
        'sum': [ arr.sum(axis=0), arr.sum(axis=1), arr.sum() ]
    }

    return calculations