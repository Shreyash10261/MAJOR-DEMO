from src.string_utils import reverse_string

def test_reverse_string():
    # This will fail because the function returns 'ehllo' instead of 'olleh'
    assert reverse_string("hello") == "olleh"
