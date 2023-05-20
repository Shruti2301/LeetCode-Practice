class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        first, last = min(strs), max(strs)
        prefix = ''
        for ind in range(min(len(first), len(last))):
            if first[ind] != last[ind]:
                break
            prefix += first[ind]

        return prefix
