from longest_palindromic_substring import *

import unittest

class LongestPalindromicSubstringTest(unittest.TestCase):
    def test_findLongestPalindromicSubstring_1(self):
        longestPalindromicSubstring = findLongestPalindromicSubstring("")

        assert longestPalindromicSubstring == ""

    def test_findLongestPalindromicSubstring_2(self):
        longestPalindromicSubstring = findLongestPalindromicSubstring("a")

        assert longestPalindromicSubstring == "a"

    def test_findLongestPalindromicSubstring_3(self):
        longestPalindromicSubstring = findLongestPalindromicSubstring("racecar")

        assert longestPalindromicSubstring == "racecar"

    def test_findLongestPalindromicSubstring_4(self):
        longestPalindromicSubstring = findLongestPalindromicSubstring("Piles and piles and piles of dirty laundry.")
        
        assert longestPalindromicSubstring == "P"

    def test_findLongestPalindromicSubstring_5(self):
        longestPalindromicSubstring = findLongestPalindromicSubstring("arbozozoaozooooozopopoppopqwerty")

        assert longestPalindromicSubstring == "ozooooozo"

    def test_findLongestPalindromicSubstring_6(self):
        longestPalindromicSubstring = findLongestPalindromicSubstring("banana")

        assert longestPalindromicSubstring == "anana"

    def test_findLongestPalindromicSubstring_7(self):
        longestPalindromicSubstring = findLongestPalindromicSubstring("abracadabra")

        assert longestPalindromicSubstring == "aca"
    