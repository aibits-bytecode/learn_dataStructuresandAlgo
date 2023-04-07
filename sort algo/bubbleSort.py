from util import time_it


class BubbleSort:
    @time_it
    def sort(self, elements):
        for i in range(len(elements) - 1):
            swapped = False
            for j in range(len(elements) - i - 1):
                if elements[j] > elements[j + 1]:
                    temp = elements[j]
                    elements[j] = elements[j + 1]
                    elements[j + 1] = temp
                    swapped = True
            if not swapped:
                break
        return elements


if __name__ == "__main__":
    bs = BubbleSort()
    numbers = [12, 10, 23, 11, 3, 5, 50]
    sortnumbers = [10, 20, 30, 40, 50]
    print(bs.sort(sortnumbers))
    print(bs.sort(numbers))
