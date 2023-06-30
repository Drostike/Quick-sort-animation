class QuickSort:
    def __init__(self, p):
        self.p = p
        self.history = []

    def partition(self, nums, low, high):
        pivot = nums[(low + high) // 2].return_number()
        i = low - 1
        j = high + 1
        while True:
            i += 1
            while nums[i].return_number() < pivot:
                i += 1
            j -= 1
            while nums[j].return_number() > pivot:
                j -= 1
            if i >= j:
                return j
            nums[i], nums[j] = nums[j], nums[i]
            self.history.append(nums.copy())


    def return_history(self):
        return self.history


    def quick_sort(self, nums):
        def _quick_sort(items, low, high):
            if low < high:
                split_index = self.partition(items, low, high)
                _quick_sort(items, low, split_index)
                _quick_sort(items, split_index + 1, high)
        _quick_sort(nums, 0, len(nums) - 1)