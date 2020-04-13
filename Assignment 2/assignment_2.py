# Author: Max Grier
# Date: 4/11/2020
# Description: CS261 - Assignment 2


import numpy as np


# class Dynamic_Array:
#     def __init__(self):
#         # creates an empty array of length 4, change the [4] to another value to make an
#         # array of different length.
#         self._list = np.empty([4], np.int16)
#         self._capacity = 4
#         self._size = 0

# StudentList class is our implementation of Python's List
class StudentList:
    def __init__(self):
        # creates an empty array of length 4, change the [4] to another value to make an
        # array of different length.
        self._list = np.empty([4], np.int16)
        self._capacity = 4
        self._size = 0

    def get_array(self):
        print(self._list)

    def get_index(self, index):
        print(self._list[index])

    def pop(self, index=-1):
        """
        Deletes a value at a specific index.  If no index is given, deletes the last value.
        :param index: Value to delete at that index.
        :return: Deleted value.
        """
        print("before", self._list)
        popped_value = self._list[index]

        copy = self._list
        print("copy", copy)

        self._list = np.empty([4], np.int16)
        print("new self.list", self._list)

        if index == -1:
            new_array = np.empty([4], np.int16)
            print("new array", new_array)
            for index in range(self._size - 1):
                new_array[index] = self._list[index]
                index += 1
            self._list = new_array
            self._size = index
        print(self._list)
        return popped_value

        while index < self._size:
            self._list[index] = self._list[index + 1]
            index += 1
        print("after ",self._list)
        return popped_value

    def add(self, value):
        self._list[self._size] = value
        self._size += 1

    def remove(self, index):
        np.delete(self._list, index)
        print(self._list)


my_list = StudentList()
print(my_list)
#
# another_list = Dynamic_Array()
# print(another_list)
#
# my_list.get_array()
# my_list.get_index(3)
# my_list.add(0)
# my_list.add(1)
# my_list.add(2)
# my_list.add(3)

# my_list.remove(0)

# my_list.pop()
# my_list.get_index(3)

# lst = [0,1,2,3,4]
# print(lst[-1])