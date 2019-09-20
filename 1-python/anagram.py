#!/usr/bin/env python
import sys

#
# Return true if str1 and str2 are anagrams of each others
#
def areAnagram(str1, str2):
    # Transform both strings in a way we can easily compare them
    return toSortedString(str1) == toSortedString(str2)

#
# Transform the given string to a string representing the existing characters
# in the original string, lowercase and sorted alphabetically.
# Duplicates are preserved. Punctuation is removed.
#
# Example : "Debit Card" becomes "abcddeirt"
#
def toSortedString(str):
    # First lowercase as sorted() sort capital letters before non capital ones.
    # Only keep alphabetical characters.
    return ''.join(filter(lambda s: s.isalpha(), sorted(str.lower())))

#
# Main script
#
if __name__ == '__main__':
    if len(sys.argv) < 3:
        print("""Usage: anagram.py \"STRING A\" \"STRING B\"""")
        sys.exit(0)

    if areAnagram(sys.argv[1], sys.argv[2]):
        print('"' + sys.argv[1] + '" and "' + sys.argv[2] + '" are anagrams of each other')
    else:
        print('"' + sys.argv[1] + '" and "' + sys.argv[2] + '" are not anagrams of each other')
