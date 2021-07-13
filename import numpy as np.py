""" import numpy as np



def set_array(L, rows, cols):
    return L.reshape(rows,cols)

sample_array = np.arange(15)
print("Original array:")
print(sample_array)

print("after setting:")
array_set = set_array(sample_array, 3, 5)
print(array_set) """

import os

path = os.path.dirname(os.path.abspath(__file__))
source_name = path + '/' + 'motto.txt'

file = open(source_name, 'w')

file.write("Fiat Lux")
file.close()

file = open(source_name, 'r')

print(file.readline())

file = open(source_name)
file1 = open(source_name, 'a')

file1.write("Let there be light!")
file1.close()

file1 = open(source_name,'r')

print(file1.readline())


"""try:
    path = os.path.dirname(os.path.abspath(__file__))
    source_file = open(path+'/'+source_name, 'w Fiat Lux')

    for line in source_file:
        if 'ETF' in line:
            print(line)
            source_file.write(line)
except IOError:
    print('IO Error! Please check valid file names and paths')
    exit
finally:
    source_file.close()"""



