import unittest

def bubble_sort(arr):
    if not isinstance(arr, list):
        raise TypeError("Input must be a list")
    for item in arr:
        if not isinstance(item, (int, float)):
            raise ValueError("List elements must be numbers")
    
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr

class TestBubbleSort(unittest.TestCase):
    def test_positive_case(self):
        self.assertEqual(bubble_sort([3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]), [1, 1, 2, 3, 3, 4, 5, 5, 5, 6, 9])
        self.assertEqual(bubble_sort([10, 2, 8, 6, 7, 5, 3, 1]), [1, 2, 3, 5, 6, 7, 8, 10])

    def test_negative_case(self):
        with self.assertRaises(TypeError):
            bubble_sort("not a list")
        with self.assertRaises(ValueError):
            bubble_sort([1, 2, "three", 4])
        with self.assertRaises(ValueError):
            bubble_sort([1, 2, None, 4])

    def test_performance_case(self):
        small_array = [3, 1, 4, 1, 5]
        large_array = list(range(1000, 0, -1))
        self.assertEqual(bubble_sort(small_array), sorted(small_array))
        self.assertEqual(bubble_sort(large_array), list(range(1, 1001)))
        
    def test_boundary_case(self):
        self.assertEqual(bubble_sort([]), [])
        self.assertEqual(bubble_sort([1]), [1])
        self.assertEqual(bubble_sort([1, 2, 2, 3, 3, 3]), [1, 2, 2, 3, 3, 3])
        self.assertEqual(bubble_sort([1, 2, 3, 4, 5]), [1, 2, 3, 4, 5]) 
        self.assertEqual(bubble_sort([5, 4, 3, 2, 1]), [1, 2, 3, 4, 5])

    def test_idempotency_case(self):
        arr = [3, 1, 4, 1, 5, 9]
        sorted_once = bubble_sort(arr[:])
        sorted_twice = bubble_sort(sorted_once)
        self.assertEqual(sorted_once, sorted_twice)
    
if __name__ == "__main__":
    unittest.main()