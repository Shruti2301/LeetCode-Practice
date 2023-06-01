
class Solution:
    def compress(self, chars: List[str]) -> int:
        chars.append("pavan")
        str_ = ""
        x = 0
        count = 1
        while x <len(chars)-1:
            if chars[x] == chars[x+1]:
                count +=1
            elif chars[x] != chars[x+1]:
                str_ += chars[x]
                if count == 1:
                    pass
                else:
                    str_ += str(count)
                    count = 1

            x+=1

        chars.clear()
        for x in str_:
            chars.append(x)

        return len(chars)
