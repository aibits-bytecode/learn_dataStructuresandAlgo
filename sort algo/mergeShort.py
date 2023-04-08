class MergeShort:
    def merge_sort(self, elements):
        if len(elements) <= 1:
            return elements
        mid = len(elements)//2
        left = elements[:mid]
        right = elements[mid:]

        self.merge_sort(left)
        self.merge_sort(right)
        self.merge_short_lists(left, right, elements)

    def merge_short_lists(self, arr1, arr2, elements):
       # sort_arr = []
        i = j = k = 0
        while i < len(arr1) and j < len(arr2):
            if arr1[i] > arr2[j]:
                elements[k] = arr2[j]
                #sort_arr.append(arr2[j])
                j += 1

            else:
                elements[k] = arr1[i]
                #sort_arr.append(arr1[i])
                i += 1
            k += 1
        while i < len(arr1):
            elements[k] = arr1[i]
            #sort_arr.append(arr1[i])
            i += 1
            k += 1

        while j < len(arr2):
            elements[k] = arr2[j]
            #sort_arr.append(arr2[j])
            j += 1
            k += 1




if __name__ == "__main__":
    arr = [12, 2, 32, 23, 33, 43, 45, 54, 56]

    ms = MergeShort()
    #ms.merge_short_lists(a, b)
    ms.merge_sort(arr)
    print(arr)