class SelectionSort:

    def sort(self, elements):
        for i in range(len(elements)):
            min_index = i
            for j in range(i + 1, len(elements)):
                if elements[j] < elements[min_index]:
                    min_index = j
            if min_index != i:
                elements[i], elements[min_index] = elements[min_index], elements[i]


if __name__ == "__main__":
    numbers = [13, 2, 32, 22, 11, 1]

    sort = SelectionSort()
    sort.sort(numbers)
    print(numbers)
