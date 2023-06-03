class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        x=y=0
        flowerbe=[0]+flowerbed+[0]+[1
        for i in flowerbe:
            if i==0:
                x=x+1
            elif x>=2 and x%2==0:
                y=y+(x//2)-1
                x=0
            elif x>=3 and x%2!=0:
                y=y+(x//2)
                x=0
            else:
                x=0
        if y>=n:
            return True
        return False
