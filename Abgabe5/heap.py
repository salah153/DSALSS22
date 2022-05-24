class Heap:

    @staticmethod
    def _swap(array: list, a: int, b: int):

        array[a], array[b] = array[b], array[a]
        print(array, "swapped", array[b], "and", array[a])


    def _heapify(self, heap, i: int, length: int):

        largest = i

        left = i * 2 + 1

        right = i * 2 + 2


        if left < length and heap[left] > heap[largest]:

            largest = left

        if right < length and heap[right] > heap[largest]:

            largest = right


        if largest != i:

            self._swap(heap, i, largest)

            self._heapify(heap, largest, length)


    def create_max_heap(self, array: list):

        length = len(array)

        start = length // 2 - 1

        for i in range(start, -1, -1):

            self._heapify(array, i, length)

        return array


    def heap_sort(self, heap):

        end = len(heap) - 1

        for i in range(end, 0, -1):

            self._swap(heap, 0, i)

            self._heapify(heap, 0, i)

        return heap

heap = Heap()
array = [7, 3, 6, 4, 5, 1, 8, 9, 2]
print("array:", array)
print("----------------------------------------")
print(array)
heapified_array = (heap.create_max_heap(array))
print("heap:", heapified_array)
print("----------------------------------------")
print(heapified_array)
sorted_array = heap.heap_sort(heapified_array)
print("sorted array:",sorted_array)
print("----------------------------------------")