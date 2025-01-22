import heapq

nums = [5, 3, 8, 1, 2]

heapq.heapify(nums)

print(nums)

heapq.heappush(nums, 23)

print(nums)

top = heapq.heappop(nums)

print(top)

bottom = heapq.nlargest(1, nums)[0]

print(bottom)
#
# while True:
#     top = heapq.heappop(nums)


# thinking: always replace the weakest one
def find_k_smallest(nums, k):
    # Use a max-heap for k smallest elements, so we negate values
    heap = [-num for num in nums[:k]]  # Take first k elements and negate them
    heapq.heapify(heap)  # Create a max-heap (negated min-heap)

    for num in nums[k:]:
        if -num > heap[0]:  # Compare with the largest element (negated smallest in original)
            heapq.heapreplace(heap, -num)  # Replace the largest with the new smaller value

    return sorted([-x for x in heap])  # Negate values back to original and return sorted list

nums = [10, 2, 14, 4, 7, 6, 3, 1]
k = 3
print(find_k_smallest(nums, k))  # [1, 2, 3](nums, k))  # [1, 2, 3]