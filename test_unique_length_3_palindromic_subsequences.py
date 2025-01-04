import unittest
from unique_length_3_palindromic_subsequences import Solution

class TestCountPalindromicSubsequence(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_example_1(self):
        self.assertEqual(self.solution.countPalindromicSubsequence("aabca"), 3)

    def test_example_2(self):
        self.assertEqual(self.solution.countPalindromicSubsequence("adc"), 0)

    def test_example_3(self):
        self.assertEqual(self.solution.countPalindromicSubsequence("bbcbaba"), 4)

    def test_empty_string(self):
        self.assertEqual(self.solution.countPalindromicSubsequence(""), 0)

    def test_no_palindromes(self):
        self.assertEqual(self.solution.countPalindromicSubsequence("abcdef"), 0)

    def test_all_same_characters(self):
        self.assertEqual(self.solution.countPalindromicSubsequence("aaa"), 1)

    def test_ckafnafqo(self):
        self.assertEqual(self.solution.countPalindromicSubsequence("ckafnafqo"), 4)

    def test_long_string(self):
        string = "nhzosdwmwomlebymvkbqbdohzdtpufnllwzhqptyffreebalphgsslryuqryloqxvbehtohdrsynmcbligczvoyzrhbtmqxepqmcjirwishyvoliizknzrokejtqtfoylsdzpgeooczxldvmsnhvzgojxnwwhukynvhhpzmdoiooliesogubtsvkrvzmanpwwlnlskremzisqwwwjistwabqxztlcqwlsxbuhjdnouecwqgxdlggauxrelipqlgvfkmgoozhzrhortbpmxhupjqqrsrvqxqilptchtedoznxvgvmuticzdzwszzujuanlrrpvycgawoxfbvxhkdyhmcxdlrtyktekcmkyajlywcrozjkedwlrqpaugdobtffwidxawddgeraaugiebtntmuncnybuwnlzbmkrmxbcpbhqoiznlpcswqtsflfilkclrjdxbvcctvopoidjrtwszpjpfrfcvjtouvzvpqayvgesiiawokdqatfkijsuocbeqrhrmlhtclhrmrbkpahfdgiatejsnvubwbaxwooskcaiuqvxcvgpnkiiiencnxjsvvgdfptreumttlyoqqwqdblhhbnilbvbwwpnmouxlvqimdbcxisnegllnejhkipuqbcrhsrxwipdjzskpyijuvrvtrnqljjefymfdcvcuvwaitdjevuvelkrglhtlnivmvjyzmhjnzvudgqwocvwhthxdlyfljabngzjayvqudhvsdslacgvosnchhbkulcxpangdlpgkrczbnnzokmqzgauitqutiboveumsqvbulhbfbynzogtejuwi"
        self.assertEqual(self.solution.countPalindromicSubsequence(string), 676)



if __name__ == '__main__':
    unittest.main()