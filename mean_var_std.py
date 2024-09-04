"""    freecodecamp data analysis project1    """

"""Create a function named calculate() in mean_var_std.py that uses Numpy to output the mean, 
variance, standard deviation, max, min, and sum of the rows, columns, and elements in a 3 x 3 matrix.
The input of the function should be a list containing 9 digits. The function should convert the list 
into a 3 x 3 Numpy array, and then return a dictionary containing the mean, variance, standard deviation, 
max, min, and sum along both axes and for the flattened matrix."""

import numpy as np

def calculate(x):
    if len(x) != 9:
        raise ValueError("List must contain nine numbers.")
    x = np.array(x)
    print(x)
    x.shape = (3,3)
    mean1,mean2,mean3 = np.mean(x,axis=0),np.mean(x,axis=1),np.mean(x)
    var1,var2,var3 = np.var(x,axis=0),np.var(x,axis=1),np.var(x)
    std1,std2,std3 = np.std(x,axis=0),np.std(x,axis=1),np.std(x)
    max1,max2,max3 = np.max(x,axis=0),np.max(x,axis=1),np.max(x)
    min1,min2,min3 = np.min(x,axis=0),np.min(x,axis=1),np.min(x)
    sum1,sum2,sum3 = np.sum(x,axis=0),np.sum(x,axis=1),np.sum(x)
    calculations = {'mean': [mean1.tolist(), mean2.tolist(), float(mean3)],
     'variance': [var1.tolist(),var2.tolist(),float(var3)],
     'standard deviation': [std1.tolist(),std2.tolist(),float(std3)],
     'max': [max1.tolist(),max2.tolist(),int(max3)],
     'min': [min1.tolist(),min2.tolist(),int(min3)],
     'sum': [sum1.tolist(),sum2.tolist(),int(sum3)]
    }
    return calculations