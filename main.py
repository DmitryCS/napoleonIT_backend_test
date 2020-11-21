class Solution:
    def __init__(self):
        self.romanToIntDict = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}

    def romanToInt(self, s: str) -> int:
        romanToIntList = [self.romanToIntDict[x] for x in s]
        ans, lastElement = 0, 1000
        for x in romanToIntList:
            ans = ans + x - 2 * lastElement if x > lastElement else ans + x
            lastElement = x
        return ans


if __name__ == "__main__":
    romanNumber = input("Введите римское число: ")
    solution = Solution()
    print(solution.romanToInt(romanNumber))