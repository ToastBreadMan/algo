s = "abcabcbb"


def lengthOfLongestSubstring(s):
    longest_substring = ''
    curr_substring = ''
    value_map = {}
    iterator = 0
    while iterator != len(s):
        if value_map.get(s[iterator]) != None:
            iterator = value_map[s[iterator]]
            value_map = dict()
            curr_substring = ''
        else:
            value_map[s[iterator]] = iterator
            curr_substring += s[iterator]
        if len(curr_substring) > len(longest_substring):
            longest_substring = curr_substring
        iterator += 1
    return len(longest_substring)

print(lengthOfLongestSubstring(s))