from escape import escape

def test_escape_simple_case():
    assert \
    escape("Nothing to escape") == "Nothing to escape", \
    "Should be 'Nothing to escape'"

def test_escape_single_quote():
    assert \
    escape("Just a ' to escape") == r"Just a \' to escape", \
    r"Should be 'Just a \' to escape'"

def test_escape_single_quotes():
    assert \
    escape("Several ' to 'escape'") == r"Several \' to \'escape\'", \
    r"Should be 'Several \' to \'escape\'"

def test_escape_backslash():
    assert \
    escape(r"Just a \ to escape") == r"Just a \\ to escape", \
    r"Should be 'Just a \\ to escape'"

def test_escape_backslashes():
    assert \
    escape(r"Several \backslashes\ to escape") == r"Several \\backslashes\\ to escape", \
    r"Should be 'Several \\backslashes\\ to escape'"

if __name__ == '__main__':
    test_escape_simple_case()
    test_escape_single_quote()
    test_escape_single_quotes()
    test_escape_backslash()
    test_escape_backslashes()
    print("Everything passed")
