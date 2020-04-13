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

    def __str__(self):
        return str(self._list[:self._size])

    # You may want an internal function that handles resizing the array.
    # Don't modify get_list or get_capacity, they are for testing

    def re_size(self):
        # This should double the capacity of the numpy array and copy over the old array, but is incomplete
        new_data = np.empty([self._capacity * 2], np.int16)
        i = 0
        for value in self._list:
            new_data[i] = value
            i += 1
        self._list = new_data
        self._capacity *= 2
        self._size = i

    def get_list(self):
        # Given
        return self._list[:self._size]

    def get_capacity(self):
        return self._capacity

    def append(self, val):
        # Given
        # Needs to check if there is room and call _upsize if there isn't
        if self._size < self._capacity:
            self._list[self._size] = val
            self._size = self._size + 1
        else:
            self.re_size()
            self._list[self._size] = val
            self._size = self._size + 1

    def pop(self, index=None):
        # Given  neeeeeeeed to fix for only the last element
        """
        Deletes a value at a specific index.  If no index is given, deletes the last value.
        :param index: Value to delete at that index.
        :return: Deleted value.
        """
        if index is None:
            new = np.empty([self._capacity], np.int16)
            i = 0
            for value in self._list:
                if value != self._list[self._size-1]:
                    new[i] = value
                    i += 1
                elif value == self._list[self._size-1]:
                    self._list = new
                    # return self._list
        self._size -= 1

    def insert(self, index, value):
        # Given
        last = self._list[self._size-1]
        if self._size == self._capacity:
            self.re_size()
        if index >= self._size:
            self._list[index] = value
        else:
            self._list[self._size] = self._list[self._size - 1]
            for i in range(self._size, index, -1):
                self._list[i] = self._list[i-1]
            self._list[index] = value
        self._size += 1

    def remove(self, remove_value):
        # Given
        """
        Removes the first instance of the given value.
        :param remove_value: Value to be removed.
        :return: Nothing
        """
        if remove_value not in self._list:
            raise ValueError('list.remove(x): x not in list')
        index = 0
        remove_index = None
        for list_value in self._list:
            if list_value == remove_value:
                remove_index = index
                break
            index += 1
        for index2 in range(remove_index, self._size):
            self._list[index2] = self._list[index2 + 1]
        self._size -= 1

    def clear(self):
        # Given
        """
        Empties the current array, then downsizes it to the original starting size.
        :return: Nothing.
        """
        self._list = np.empty([4], np.int16)
        self._size = 0

    def count(self, count_value):
        # Given
        count_value_occurrence = 0
        for value in self._list:
            if value == count_value:
                count_value_occurrence += 1
        return count_value_occurrence

    def get(self, index):
        # Given
        return self._list[index]









        # print("before", self._list)
        # popped_value = self._list[index]
        #
        # copy = self._list
        # print("copy", copy)
        #
        # self._list = np.empty([4], np.int16)
        # print("new self.list", self._list)
        #
        # if index is None:
        #     new_array = np.empty([4], np.int16)
        #     print("new array", new_array)
        #     for index in range(self._size - 1):
        #         new_array[index] = self._list[index]
        #         index += 1
        #     self._list = new_array
        #     self._size = index
        # print(self._list)
        # return popped_value
        #
        # while index < self._size:
        #     self._list[index] = self._list[index + 1]
        #     index += 1
        # print("after ",self._list)
        # return popped_value



my_list = StudentList()
print("My empty numpy", my_list)
for i in range(10):
    my_list.append(i)
my_list.append(5)
print("numpy with values", my_list)


print(my_list.get(10))



# start2 = time.time()
# my_list = [x for x in range(100)]
# print(my_list)
# end2 = time.time()
# print("Total time2: ", end2 - start2)
#
# start2 = time.time()
# my_list = []
# for x in range(100):
#     my_list.append(x)
# print(my_list)
# end2 = time.time()
# print("Total time2: ", end2 - start2)

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
#         new_data = np.empty([self._capacity], np.int16)
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
# my_list = Dynamic_Array()
#
# # To begin with this will throw an index out of bounds error until you properly handle the capacity
# # doubling.
# start = time.time()
# for i in range(100):
#     my_list.append(i)
# print(my_list)
# end = time.time()
# print("Total time: ", end - start)
