# 3223. Minimum Length of String After Operations
# Medium

# Topics
# Companies

# Hint
# You are given a string s.

# You can perform the following process on s any number of times:

# Choose an index i in the string such that there is at least one character to the left of index i that is equal to s[i], and at least one character to the right that is also equal to s[i].
# Delete the closest character to the left of index i that is equal to s[i].
# Delete the closest character to the right of index i that is equal to s[i].
# Return the minimum length of the final string s that you can achieve.
class Solution:
    def minimumLength(self, s: str) -> int:
        # abaacbcbb
        # aaacbcb
        # acbcb

        # 문자별 카운팅을 하는데 3개 이상인 문자를 선택
        # 3개 이상인 문자는 결과적으로 1개가 되지 않나. 
        # 나머지는 그냥 그 개수 그대로이고 
        strs = {}
        for v in s:
            if v not in strs:
                strs[v] = 1
            else:
                strs[v] = strs[v] + 1

        sum = 0
        for i in strs:
            if strs[i] > 2:
                if strs[i] % 2 == 0:
                    strs[i] = 2
                else :
                    strs[i] = 1
            sum = sum + strs[i]

        return sum