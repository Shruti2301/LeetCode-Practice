import heapq

class MedianFinder:
    def __init__(self):
        # Initialize two heaps:
        # max_heap to store the smaller half of the numbers (negated values)
        # min_heap to store the larger half of the numbers
        self.max_heap = []
        self.min_heap = []

    def addNum(self, num: int) -> None:
        # Add the number to the appropriate heap
        if not self.max_heap or num <= -self.max_heap[0]:
            heapq.heappush(self.max_heap, -num)
        else:
            heapq.heappush(self.min_heap, num)
            
        # Balance the heaps to maintain the size difference at most 1
        if len(self.max_heap) > len(self.min_heap) + 1:
            heapq.heappush(self.min_heap, -heapq.heappop(self.max_heap))
        elif len(self.min_heap) > len(self.max_heap):
            heapq.heappush(self.max_heap, -heapq.heappop(self.min_heap))

    def findMedian(self) -> float:
        # If the number of elements is even, return the average of the two middle elements
        if len(self.max_heap) == len(self.min_heap):
            return (-self.max_heap[0] + self.min_heap[0]) / 2 if self.max_heap else 0
        # If the number of elements is odd, return the middle element from max_heap
        else:
            return -self.max_heap[0] if self.max_heap else 0

# Runtime complexity:
# - addNum: O(log n) where n is the number of elements inserted so far.
# - findMedian: O(1), as it only requires accessing the roots of the heaps.

# Space complexity:
# - O(n) where n is the number of elements inserted so far, as the heaps store all the elements.
