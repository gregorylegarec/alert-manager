from palindrome import isPalindrome

def test_isPalindrome_true():
    assert \
    isPalindrome("A man, a plan, a canal, Panama."), \
    "Should be true"

def test_isPalindrome_false():
    assert \
    not isPalindrome("Radom sentence, probably not a palindrome."), \
    "Should be false"

if __name__ == '__main__':
    test_isPalindrome_true()
    test_isPalindrome_false()
    print("Everything passed")
