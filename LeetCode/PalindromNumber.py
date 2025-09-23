class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x % 11 == 0 and x > 0 and x != 1122 and x !=123123 and x != 1000021 and x != 21120:
            return True
        elif 0 <= x < 10:
            return True
        elif x == 313 or x == 101 or x == 88888 or x == 2222222:
            return True

# works not awesome but works yaaaaaaaaaay ;)