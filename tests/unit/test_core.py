import textutils.core as c

def test_is_palindrome():
    text = "Level"
    assert c.is_palindrome(text) == True