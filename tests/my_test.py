def test_my_input():
    phrase = input("Set a phrase: ")
    assert len(phrase) < 15, f"Phrase '{phrase}' is too long"