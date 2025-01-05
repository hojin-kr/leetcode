# You are given a string s of lowercase English letters and a 2D integer array shifts where shifts[i] = [starti, endi, directioni]. For every i, shift the characters in s from the index starti to the index endi (inclusive) forward if directioni = 1, or shift the characters backward if directioni = 0.

# Shifting a character forward means replacing it with the next letter in the alphabet (wrapping around so that 'z' becomes 'a'). Similarly, shifting a character backward means replacing it with the previous letter in the alphabet (wrapping around so that 'a' becomes 'z').

# Return the final string after all such shifts to s are applied.
from typing import List

class Solution:
    def shiftingLetters(self, s: str, shifts: List[List[int]]) -> str:
        n = len(s)
        shift_effect = [0] * (n + 1)  # 누적합 배열
        print(shift_effect)
        
        # 누적합 배열에 각 shift의 영향을 기록
        for start, end, direction in shifts:
            if direction == 1:
                shift_effect[start] += 1
                shift_effect[end + 1] -= 1
            else:
                shift_effect[start] -= 1
                shift_effect[end + 1] += 1
        print(shift_effect)
        # 누적합 계산
        for i in range(1, n):
            shift_effect[i] += shift_effect[i - 1]
        
        # 결과 문자열 생성
        result = []
        for i in range(n):
            shift = shift_effect[i]
            # 알파벳 wrapping
            new_char = chr((ord(s[i]) - ord('a') + shift) % 26 + ord('a'))
            result.append(new_char)
        
        return ''.join(result)

# 이동할 만큼을 미리 계산 한 후 적용