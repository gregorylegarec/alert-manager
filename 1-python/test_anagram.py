from anagram import areAnagram

def test_isAnagram_true():
    assert areAnagram("Debit card", "Bad credit"), "Should be true"

def test_isAnagram_false():
    assert not areAnagram("Debit card", "Great concert"), "Should be false"

if __name__ == '__main__':
    test_isAnagram_true()
    test_isAnagram_false()
    print("Everything passed")
