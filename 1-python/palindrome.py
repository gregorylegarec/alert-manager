#!/usr/bin/env python
import sys

#
# Return true if str is a palindrome
#
def isPalindrome(str):
    lowerAlphaChars = toLowerAlphaChars(str)
    return lowerAlphaChars == reverse(lowerAlphaChars)

#
# Transform a string into a new one, keeping only Lowercased alphabetical
# characters
#
def toLowerAlphaChars(str):
    return ''.join(filter(lambda s: s.isalpha(), str.lower()))

#
# Reverse a string
#
def reverse(str):
    return ''.join(reversed(list(str)))

#
# Main script
#
if __name__ == '__main__':
    if len(sys.argv) < 2:
        print("""Usage: palindrome.py \"STRING\"""")
        sys.exit(0)

    if isPalindrome(sys.argv[1]):
        print('"' + sys.argv[1] + '" is a palindrome')
    else:
        print('"' + sys.argv[1] + '" is not a palindrome')
