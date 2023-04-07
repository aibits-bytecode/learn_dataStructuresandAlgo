from util import time_it


class BinarySearch:

    @time_it
    def mysearch(self, elements, value):
        min_index = 0
        max_index = len(elements) - 1

        def inner_wrapper(elements, value, min_index, max_index):
            if min_index == max_index and elements[min_index] != value:
                return -1
            else:
                midle_index = (min_index + max_index) // 2
                if elements[midle_index] == value:
                    return midle_index
                elif elements[midle_index] > value:
                    return inner_wrapper(elements, value, min_index, midle_index-1)
                else:
                    return inner_wrapper(elements, value, midle_index + 1, max_index)

        return inner_wrapper(elements,value,min_index,max_index)

    @time_it
    def binary_search(self, elements, value):
        left_index = 0
        right_index = len(elements) - 1

        while left_index <= right_index:
            midle_index = (left_index + right_index) // 2
            if elements[midle_index] == value:
                return midle_index
            elif elements[midle_index] > value:
                right_index = midle_index - 1
            else:
                left_index = midle_index + 1
        return -1


if __name__ == "__main__":
    numbers = [23, 24, 31, 33, 43, 54, 66]
    bs = BinarySearch()
    print(bs.binary_search(numbers, 54))
    print(bs.mysearch(numbers, 54))
