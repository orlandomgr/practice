class Solution:
    def maxFreqSum(self, s: str) -> int:
        vowels = ["a", "e", "i", "o", "u"]
        frequencies = {}

        for c in s:
            count = 1
            if c in frequencies:
                count = frequencies[c] + 1
            frequencies[c] = count

        sorted_items = sorted(frequencies.items(), key=lambda item: item[1], reverse=True)
        sorted_dict = dict(sorted_items)

        vowelCount = 0
        consonantCount = 0
        for key, value in sorted_dict.items():
            if key in vowels:
                if vowelCount == 0:
                    vowelCount = value
            else: 
                if consonantCount == 0:
                    consonantCount = value
            if vowelCount > 0 and consonantCount > 0:
                break
        return vowelCount + consonantCount


obj = Solution()
print(obj.maxFreqSum("successes"))  # 6
print(obj.maxFreqSum("aeiaeia"))  # 3
