class Heap(object):
    HEAP_SIZE = 10

    def __init__(self):
        self.heap = [0]* Heap.HEAP_SIZE
        self.current_postion = -1