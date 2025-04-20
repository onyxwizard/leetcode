# The class `Solution` contains a method `backspaceCompare` that attempts to compare two strings after
# processing backspace characters, but the implementation has a logical error in handling backspace
# characters.
class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        left,right = len(s)-1,len(t)-1
        def valid_char(string,loop_range):
                backspace = 0
                while loop_range>=0:
                    if string[loop_range] == "#":
                        backspace+=1
                    elif backspace>0:
                        backspace-=1
                    else:
                        return loop_range
                    loop_range-=1
                return loop_range
                
        while left>=0 and right>=0:
            left = valid_char(s,left)
            right = valid_char(t,right)
            
            if left == right:
                return True
            if s[left]!= t[right]:
                return False

            if left!= right:
                return False

if __name__ == "__main__":
    string = Solution()
    s,t = "bc#","b"
    print(string.backspaceCompare(s,t))