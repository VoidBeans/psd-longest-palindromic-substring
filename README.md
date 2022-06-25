Extract from [Wikipedia](https://en.wikipedia.org/wiki/Longest_palindromic_substring):

> In computer science, the longest palindromic substring or longest symmetric factor problem is the problem of finding a maximum-length contiguous substring of a given string that is also a palindrome. For example, the longest palindromic substring of "bananas" is "anana". The longest palindromic substring is not guaranteed to be unique; for example, in the string "abracadabra", there is no palindromic substring with length greater than three, but there are two palindromic substrings with length three, namely, "aca" and "ada". In some applications it may be necessary to return all maximal palindromic substrings (that is, all substrings that are themselves palindromes and cannot be extended to larger palindromic substrings) rather than returning only one substring or returning the maximum length of a palindromic substring.

Examples:

**EXAMPLE 1**

```
INPUT:  racecar
OUTPUT: racecar
```

**EXAMPLE 2**

```
INPUT:  banana
OUTPUT: anana
```

**EXAMPLE 3**

```
INPUT:  89561001001001158
OUTPUT: 1001001001
```
