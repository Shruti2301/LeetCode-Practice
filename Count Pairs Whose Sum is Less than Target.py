#July 7,2024 : Count Pairs Whose Sum is Less than Target                

class Solution:
    def countPairs(self, numbers: List[int], target_sum : int) -> int:
        # Step 1: Sort the array
        sorted_nums = sorted(numbers)
        
        # Initialize pointers
        start = 0
        end = len(sorted_nums) - 1
        
        # Initialize count for valid pairs
        pair_count = 0
        
        # Step 2 and 3: Use two pointers to count pairs
        while start < end:
            # Calculate the sum of the current pair
            current_sum = sorted_nums[start] + sorted_nums[end]
            
            # If the sum of the current pair is less than the target
            if current_sum < target_sum:
                # All pairs between start and end (inclusive) are valid
                pair_count += end - start
                # Move the start pointer to the right to check the next potential pair
                start += 1
            else:
                # If the sum is not less than the target, move the end pointer to the left
                end -= 1
        
        return pair_count


# Time Complexity:
# Sorting the array: O(n log n)
# Two-pointer traversal: O(n)
# Overall time complexity: O(n log n)

# Space Complexity:
# Sorting the array requires O(n) extra space for the sorted copy
# Pointers and variables: O(1)
# Overall space complexity: O(n)
