class Solution:
    def reverseVowels(self, s: str) -> str:
        ss = list(s)
        left = 0 
        right = len(ss) - 1
        vowels = {'a' , 'e' ,'o' , 'i' , 'u' , 'A', 'E', 'I', 'O', 'U'}
        while left < right:
            if ss[left] in vowels and ss[right] in vowels:
                ss[left], ss[right] = ss[right], ss[left]
                left += 1
                right -= 1
            elif ss[left] in vowels:
                right -= 1
            else:
                left += 1
        return "".join(ss)
