class Solution:
    def isPalindrome(self, s: str) -> bool:
        left = 0
        right = len(s)-1
        my_word = s.lower()

        while left<right:
            if not my_word[left].isalnum():
                while not my_word[left].isalnum() and left<right:
                    left+=1

        
            if not my_word[right].isalnum() and left<right:
                while not my_word[right].isalnum():
                    right-=1


            if my_word[left] != my_word[right]:
                return False
            
            left+=1
            right-=1

        return True

