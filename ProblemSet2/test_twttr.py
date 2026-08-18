from twtrr import shorten

def test_shorten_standard():
    assert shorten("Rafael") == "Rfl"
    assert shorten("Twitter") == "Twttr"
    assert shorten("2 sad tigers") == "2 sd tgrs"
    assert shorten("Hello, what is your name?") == "Hll, wht s yr nm?"

def test_shorten_vowels_lower():
    assert shorten("a") == ""
    assert shorten ("e") == ""
    assert shorten ("i") == ""
    assert shorten ("o") == ""
    assert shorten ("u") == ""
def test_shorten_vowels_upper():
    assert shorten("A") == ""
    assert shorten ("E") == ""
    assert shorten ("I") == ""
    assert shorten ("O") == ""
    assert shorten ("U") == ""
def test_shorten_numbers():
    assert shorten("1") == "1"
    assert shorten("2") == "2"
    assert shorten("3") == "3"
    assert shorten("4") == "4"
    assert shorten("5") == "5"
    assert shorten("1 2 3") == "1 2 3"
    assert shorten ("1,2,3") == "1,2,3"