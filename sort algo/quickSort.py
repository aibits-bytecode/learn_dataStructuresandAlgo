from util import time_it

class QuickSort:

    def swap(self, a, b, arr):
        if arr[a] != arr[b]:
            arr[a], arr[b] = arr[b], arr[a]
        # tmp = arr[a]
        # arr[a] = arr[b]
        # arr[b] = tmp

    def partition(self, elements, startPosition, endPosition):
        pivot_index = startPosition
        pivot = elements[pivot_index]
        start = pivot_index + 1
        end = endPosition
        while start < end:
            while start < len(elements) and elements[start] < pivot:
                start += 1
            while end > 0 and elements[end] > pivot:
                end -= 1
            if start < end:
                self.swap(start, end, elements)
        self.swap(pivot_index, end, elements)
        return end

    def quickSort(self, elements, start, end):

        if start < end:
            pi = self.partition(elements, start, end)
            self.quickSort(elements, start, pi - 1)
            self.quickSort(elements, pi + 1, end)


if __name__ == "__main__":
    numbers = [11, 9, 29, 7, 2, 15, 28]
    # [7, 9, 2, 11, 29, 33, 15, 28]

    qs = QuickSort()
    qs.quickSort(numbers, 0, len(numbers) - 1)
    print(numbers)
