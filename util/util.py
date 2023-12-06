# import numpy as np
# import matplotlib
# import matplotlib.pyplot as plt
# from mpl_toolkits.mplot3d import Axes3D, art3d
from itertools import chain, combinations
import copy

FUZZ = 0.001

def getOneVector(p,i):
    pCopy = copy.deepcopy(p)
    pCopy[i] = 1
    return pCopy

def getZeroVector(p,i):
    pCopy = copy.deepcopy(p)
    pCopy[i] = 0
    return pCopy

def sortTwoLists(list1, list2):
    zipped_lists = zip(list1, list2)
    sorted_pairs = sorted(zipped_lists)

    tuples = zip(*sorted_pairs)
    newList1, newList2 = [ list(tuple) for tuple in  tuples]
    return newList1, newList2

# def plot_2var_fns(fns, ub = 1, imgName = 'plot', usetex = False):

#     matplotlib.rcParams['text.usetex'] = usetex
    
#     def matrix_fn(f, X, Y):
#         Z = np.empty([np.shape(X)[0], np.shape(X)[1]])
#         for i in range(np.shape(X)[0]):
#             for j in range(np.shape(X)[1]):
#                 Z[i][j] = f([X[i][j], Y[i,j]])
#         return Z

#     x = np.linspace(0,ub, 50)
#     y = np.linspace(0,ub, 50)

#     X, Y = np.meshgrid(x, y)
#     ZVals = [matrix_fn(f, X, Y) for f in fns]
    
#     fig = plt.figure()
#     fig.set_size_inches(15, 15)

#     ax = plt.axes(projection='3d')
#     ax.set_xlabel('x_1')
#     ax.set_ylabel('x_2')
#     ax.set_zlabel('F(x_1,x_2)')
#     #ax.set_zlim3d(0, 120)
#     index = 0
#     cmaps = ['winter', 'autumn']
#     alphas = [1, 0.5]
#     for Z in ZVals:
#         print(Z)
#         p = ax.plot_surface(X, Y, Z, rstride=1, cstride=1,
#                 cmap= cmaps[index], alpha = alphas[index], edgecolor='none')
#         index += 1
    #fig.colorbar(p)
    
    
    # ax.invert_yaxis()
    # #ax.view_init(15,-30)
    # plt.savefig('' + imgName + '.jpg')
    # plt.show()

def powerset(iterable, min_size):
    s = list(iterable)
    return chain.from_iterable(list(combinations(s, r)) for r in range(min_size,len(s)+1))

def posDictTriple(x):
    return {(i,j,s) : x[i,j,s] for (i,j,s) in x if abs(x[i,j,s]) > 0.001}

def strKeysDict(x, rnd_digits = 1):
    return {str(key) : round(x[key], rnd_digits) for key in x}

def posDict(x):
    return {(i,j) : x[i,j] for (i,j) in x if abs(x[i,j]) > 0.001}

def posDictSet(x, myset):
    return {(i,j) : x[i,j] for (i,j) in myset if abs(x[i,j]) > 0.001}

def posKeysIntersection(x, y):
    return set(posDict(x)).intersection(posDict(y))

def dictMult(a, b, myset):
    return {(i,j) : a[i,j]*b[i,j] for (i,j) in myset}

def keysForNonZeroVals(x):
    return [(i,j) for (i,j) in x if abs(x[i,j]) > 0.001]

def getTupleKeysEqualToValue(x, value):
    return [(i,j) for (i,j) in x if x[i,j] == value]
