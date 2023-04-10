class ShellShort:

    def short(self, elements):
        arr_size = len(elements)
        gap = arr_size // 2

        while gap > 0:
            for i in range(gap,arr_size):
                anchor = elements[i]
                j = i
                while j >= gap and elements[j-gap] > anchor:
                    elements[j] = elements[j-gap]
                    j -= gap
                elements[j] = anchor
            gap = gap//2


if __name__ == "__main__":
    numbers = [21, 38, 29, 17, 4, 25, 11, 32, 9]
    ss = ShellShort()
    ss.short(numbers)
    print(numbers)

