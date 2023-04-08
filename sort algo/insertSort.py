class InsertSort:

    def swap(self, a, b, arr):
        arr[a], arr[b] = arr[b], arr[a]

    def sort(self, elements):
        for i in range(1, len(elements)):
            for j in range(i):
                if elements[i] < elements[j]:
                    self.swap(i, j, elements)


if __name__ == "__main__":
    numbers = [21, 38, 29, 17, 4, 25, 11, 32, 9]

    s = InsertSort()
    s.sort(numbers)
    print(numbers)
