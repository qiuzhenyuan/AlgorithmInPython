import sys
import random
reload(sys)
sys.setdefaultencoding('utf-8')


def MAX_Heapify(heap, HeapSize, root):

    left = 2*root + 1
    right = left + 1
    larger = root
    # if the child bigger than the parent, exchange it
    if left < HeapSize and heap[larger] < heap[left]:
        larger = left
    if right < HeapSize and heap[larger] < heap[right]:
        larger = right
    if larger != root:
        heap[larger], heap[root] = heap[root], heap[larger]
        MAX_Heapify(heap, HeapSize, larger)

def Build_MAX_Heap(heap):
    HeapSize = len(heap)
    for i in xrange((HeapSize - 2)//2, -1, -1):
        MAX_Heapify(heap, HeapSize, i)

def HeapSort(heap):
    Build_MAX_Heap(heap)
    # from last item to first item
    for i in range(len(heap)-1, -1, -1):
        heap[0], heap[i] = heap[i], heap[0]     #put the item to the first place
        MAX_Heapify(heap, i, 0)                 #sink the item
    return heap

if __name__ == '__main__':
    a = [30, 50, 57, 77, 62, 78, 94, 80, 84]
    print a
    HeapSort(a)
    print a
    # b = [random.randint(1,1000) for i in range(1000)]
    # print b
    # HeapSort(b)
    # print b