# student_list.py
# ===================================================
# Reimplementation of Pythons List
# ===================================================

import numpy as np


# StudentList class is our implementation of Python's List
class StudentList:
    def __init__(self):
        # creates an empty array of length 4, change the [4] to another value to make an
        # array of different length.
        self._list = np.empty([4], np.int16)
        self._capacity = 4
        self._size = 0

    def pop(self, index=self._list):
        """
        Deletes a value at a specific index.  If no index is given, deletes the last value.
        :param index: Value to delete at that index.
        :return: Deleted value.
        """
        print("before", self._list)
        popped_value = self._list[index]

        while index < self._size:
            self._list[index] = self._list[index + 1]
            index += 1
        print("after ",self._list)
        return popped_value

    def __str__(self):
        return str(self._list[:self._size])

    # You may want an internal function that handles resizing the array.
    # Dont modify get_list or get_capacity, they are for testing

    def resize(self):
        """
        Doubles the size of the numpy array,
        then copies the old array into the new array.
        """
        new_array = np.empty([self._capacity * 2], np.int16)
        index = 0
        for value in self._list:
            new_array[index] = value
            index += 1
        self._list = new_array
        self._capacity *= 2
        self._size = index

    def get_list(self):
        return self._list[:self._size]

    def get_capacity(self):
        return self._capacity

    def append(self, val):
        # FIXME: You will write this function

    # def pop(self, index=self._size):
    #     """
    #     Deletes a value at a specific index.  If no index is given, deletes the last value.
    #     :param index: Value to delete at that index.
    #     :return: Deleted value.
    #     """
    #     print("before", self._list)
    #     popped_value = self._list[index]
    #
    #     while index < self._size:
    #         self._list[index] = self._list[index + 1]
    #         index += 1
    #     print("after ",self._list)
    #     return popped_value


	# def insert(self, index, val):
    #     # FIXME: You will write this function
    #
	# def remove(self, val):
    #     # FIXME: You will write this function
    #
	# def clear(self):
    #     # FIXME: You will write this function
    #
	# def count(self):
    #     # FIXME: You will write this function
    #
	# def get(self, index):
    #     # FIXME: You will write this function



my_list = StudentList()
my_list.pop()




        # import time
        #
        # import numpy as np
        #
        # class Dynamic_Array:
        #     def __init__(self):
        #         # creates an empty array of length 4, change the [4] to another value to make an
        #         # array of different length.
        #         self._list = np.empty([4], np.int16)
        #         self._capacity = 4
        #         self._size = 0
        #
        #     def __str__(self):
        #         return str(self._list[:self._size])
        #
        #     def _upsize(self):
        #         # This should double the capacity of the numpy array and copy over the old array, but is incomplete
        #         new_data = np.empty([self._capacity * 2], np.int16)
        #         i = 0
        #         for value in self._list:
        #             new_data[i] = value
        #             i += 1
        #         self._list = new_data
        #         self._capacity *= 2
        #         self._size = i
        #
        #     def append(self, val):
        #         # Needs to check if there is room and call _upsize if there isn't
        #         if self._size < self._capacity:
        #             self._list[self._size] = val
        #             self._size = self._size + 1
        #         else:
        #             self._upsize()
        #             self._list[self._size] = val
        #             self._size = self._size + 1
        #
        #     def remove(self, index):
        #         print("size:", self._size)
        #         print(self._list[self._capacity - 1])
        #         self._list[index] = self._list[self._capacity - 1]
        #         print(self._capacity)
        #
        # my_list = Dynamic_Array()
        #
        # # To begin with this will throw an index out of bounds error until you properly handle the capacity
        # # doubling.
        # start = time.time()
        # for i in range(100):
        #     my_list.append(i)
        # print(my_list)
        # print(my_list._capacity)
        # end = time.time()
        # print("Total time: ", end - start)
        #
        # my_list.remove(0)
        # print(my_list)
        # my_list.remove(79)
        # print(my_list)
        #
        # # start2 = time.time()
        # # my_list = [x for x in range(100)]
        # # print(my_list)
        # # end2 = time.time()
        # # print("Total time2: ", end2 - start2)
        # #
        # # start2 = time.time()
        # # my_list = []
        # # for x in range(100):
        # #     my_list.append(x)
        # # print(my_list)
        # # end2 = time.time()
        # # print("Total time2: ", end2 - start2)
        #
        # # import time
        # #
        # # import numpy as np
        # #
        # # class Dynamic_Array:
        # #     def __init__(self):
        # #         # creates an empty array of length 4, change the [4] to another value to make an
        # #         # array of different length.
        # #         self._list = np.empty([4], np.int16)
        # #         self._capacity = 4
        # #         self._size = 0
        # #
        # #     def __str__(self):
        # #         return str(self._list[:self._size])
        # #
        # #     def _upsize(self):
        # #         # This should double the capacity of the numpy array and copy over the old array, but is incomplete
        # #         new_data = np.empty([self._capacity], np.int16)
        # #         i = 0
        # #         for value in self._list:
        # #             new_data[i] = value
        # #             i += 1
        # #         self._list = new_data
        # #         self._capacity *= 2
        # #         self._size = i
        # #
        # #     def append(self, val):
        # #         # Needs to check if there is room and call _upsize if there isn't
        # #         if self._size < self._capacity:
        # #             self._list[self._size] = val
        # #             self._size = self._size + 1
        # #         else:
        # #             self._upsize()
        # #             self._list[self._size] = val
        # #             self._size = self._size + 1
        # #
        # # my_list = Dynamic_Array()
        # #
        # # # To begin with this will throw an index out of bounds error until you properly handle the capacity
        # # # doubling.
        # # start = time.time()
        # # for i in range(100):
        # #     my_list.append(i)
        # # print(my_list)
        # # end = time.time()
        # # print("Total time: ", end - start)
