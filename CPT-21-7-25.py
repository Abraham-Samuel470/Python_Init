# '''code to calc area and circumference of a circle by using a class rectangle, 
# create  a constructor and spearate functions for area of circle and delete construcotr,
# import math pi value'''

# class rect():
    
#     from math import pi
#     def __init__(self,radius):
#         self.radius=radius
#     def area(self):
#         return self.pi*self.radius**2
#     def circum(self):
#         return  2*self.pi*self.radius
#     def __del__(self):
#         print("Rectangle contrucotr deleted...")

# c=rect(10)
# print("Area of Circle is ", c.area())
# print("Circumference of Circle is ", c.circum())
# del c 
# '''
# __lt__(),__le__(),
# __eq__(),__ne__(),
# __gt__(),__ge__(),

# '''

'''
math evaluation on get item set-item
code to add the sum of rows in a 2-D list
'''

class RowSum():
    def __init__(self,matrix):
        self.matrix=matrix
    def __getitem__(self,row):
        return sum(self.matrix[row])
    def __setitem__(self,row,new_row):
        self.matrix[row]=new_row



m=RowSum([[1,2],[3,4],[5,6]])
# sum of 0 index row values = 3
# sum of 2 index row values = 11
print("Sum of row 0 is " , m[0])
print("Sum of row 2 is " , m[2])
# m[1]=[10,20]
# 1,2 m[0]
# 3,4 m[1]
# 5,6 m[2]
# sum of 1 index row values, which are new =30
print("New sum of row 1 is ", m[1])