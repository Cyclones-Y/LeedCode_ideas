"""
给定一个字符串 s ，请你找出其中不含有重复字符的 最长 子串的长度。
"""

"""
滑动窗口---双指针
"""
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        char_index = {}
        left = 0
        max_length = 0

        for right in range(len(s)):
            word = s[right]
            # 遍历到的字符在字典中，并且在字典中出现的该字符串的索引大于等于left
            # 如果遍历的字符在窗口内的话，就向右滑动窗口，将之前出现在字典中的字符移出窗口中
            if word in char_index and char_index[word] >= left:
                left = char_index[word] + 1
            char_index[word] = right
            max_length = max(max_length, right - left + 1)
        return max_length





if __name__ == '__main__':
    s = "abcbabcbb"
    result = Solution()
    results = result.lengthOfLongestSubstring(s)
    print(results)

