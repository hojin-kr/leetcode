# 1930. Unique Length-3 Palindromic Subsequences
# Medium

# Topics
# Companies

# Hint
# Given a string s, return the number of unique palindromes of length three that are a subsequence of s.

# Note that even if there are multiple ways to obtain the same subsequence, it is still only counted once.

# A palindrome is a string that reads the same forwards and backwards.

# A subsequence of a string is a new string generated from the original string with some characters (can be none) deleted without changing the relative order of the remaining characters.

# For example, "ace" is a subsequence of "abcde".

class Solution:
    def countPalindromicSubsequence(self, s: str) -> int:
        if len(s) < 3:
            return 0

        first = {}
        last = {}
        for i, c in enumerate(s):
            if c not in first:
                first[c] = i
            last[c] = i

        unique_palindromes = set()
        for c in first:
            if first[c] < last[c] - 1:
                middle_chars = set(s[first[c] + 1:last[c]])
                for mc in middle_chars:
                    unique_palindromes.add(c + mc + c)

        return len(unique_palindromes)


# Solution

# 클래스의 countPalindromicSubsequence 메서드는 주어진 문자열 s에서 길이가 3인 고유한 회문 부분 수열의 개수를 세기 위해 설계되었습니다. 회문 부분 수열은 앞뒤로 읽었을 때 동일한 문자열을 의미합니다. 이 메서드는 먼저 문자열의 길이가 3보다 작은 경우, 길이가 3인 회문 부분 수열을 가질 수 없으므로 0을 반환합니다.

# 그 다음, first와 last라는 두 개의 딕셔너리를 초기화합니다. 이 딕셔너리들은 각각 문자열에서 각 문자의 첫 번째와 마지막 발생 인덱스를 저장합니다. enumerate 함수를 사용하여 문자열을 순회하면서 각 문자의 인덱스와 문자를 가져옵니다. 각 문자에 대해, 만약 해당 문자가 first 딕셔너리에 없다면, 현재 인덱스를 첫 번째 발생 인덱스로 기록합니다. 그리고 last 딕셔너리에는 현재 인덱스를 마지막 발생 인덱스로 업데이트합니다.

# 그 다음, 고유한 회문 부분 수열을 저장할 빈 집합 unique_palindromes를 초기화합니다. first 딕셔너리의 문자를 순회하면서, 각 문자에 대해 첫 번째 발생 인덱스가 마지막 발생 인덱스보다 1 작은 경우를 확인합니다. 이 조건은 첫 번째와 마지막 발생 사이에 적어도 하나의 문자가 있어야 함을 보장합니다. 조건이 충족되면, 첫 번째와 마지막 발생 사이에 있는 문자들의 집합을 추출합니다. 이 중간 문자들 각각에 대해, 해당 문자와 중간 문자, 그리고 다시 해당 문자를 연결하여 회문 부분 수열을 만들고, 이를 unique_palindromes 집합에 추가합니다.

# 마지막으로, unique_palindromes 집합의 길이를 반환하여 문자열에서 찾은 길이가 3인 고유한 회문 부분 수열의 개수를 반환합니다.