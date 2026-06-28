# ============================================================
# TESTING FRAMEWORK
# ============================================================

def run_tests(tests):
    passed = 0
    for description, run_case, expected in tests:
        try:
            actual = run_case()
        except Exception as error:
            print(f"FAIL: {description}")
            print(f"      crashed with: {error}")
            continue
        if actual == expected:
            print(f"PASS: {description}")
            passed += 1
        else:
            print(f"FAIL: {description}")
            print(f"      {'expected:':<10}{expected!r}")
            print(f"      {'got:':<10}{actual!r}")
    print(f"\n{passed}/{len(tests)} tests passed")


# ============================================================
# TEST CASES
# ============================================================

shift_letter_tests = [
    ("'a' shifted by 1 should give 'b'",               lambda: shift_letter('a', 1),  'b'),
    ("'B' shifted by 1 should give 'C' (case kept)",   lambda: shift_letter('B', 1),  'C'),
    ("'z' shifted by 1 should wrap to 'a'",             lambda: shift_letter('z', 1),  'a'),
    ("'a' shifted by -1 should wrap to 'z'",            lambda: shift_letter('a', -1), 'z'),
    ("'Z' shifted by 1 should wrap to 'A' (case kept)", lambda: shift_letter('Z', 1),  'A'),
    ("'a' shifted by 0 should stay 'a'",                lambda: shift_letter('a', 0),  'a'),
    ("'a' shifted by 26 should return to 'a'",          lambda: shift_letter('a', 26), 'a'),
    ("'a' shifted by 27 should behave like shift 1",    lambda: shift_letter('a', 27), 'b'),
]

is_letter_tests = [
    ("lowercase letter",        lambda: is_letter("a"), True),
    ("uppercase letter",        lambda: is_letter("A"), True),
    ("last lowercase letter",   lambda: is_letter("z"), True),
    ("last uppercase letter",   lambda: is_letter("Z"), True),
    ("digit",                   lambda: is_letter("5"), False),
    ("space",                   lambda: is_letter(" "), False),
    ("punctuation",             lambda: is_letter("!"), False),
]

shift_string_tests = [
    ("lowercase word shifts correctly",       lambda: shift_string("abc", 1),        "bcd"),
    ("uppercase is preserved",                lambda: shift_string("ABC", 1),        "BCD"),
    ("wraps at the end of the alphabet",      lambda: shift_string("xyz", 1),        "yza"),
    ("non-letters are left unchanged",        lambda: shift_string("Hi, World!", 0), "Hi, World!"),
    ("spaces pass through untouched",         lambda: shift_string("ab cd", 1),      "bc de"),
    ("negative shift moves backwards",        lambda: shift_string("bcd", -1),       "abc"),
    ("empty string stays empty",              lambda: shift_string("", 5),           ""),
    ("mixed case, punctuation, and wrapping", lambda: shift_string("Yikes, zoo!", 1), "Zjlft, app!"),
]

encrypt_tests = [
    ("encrypt shifts forward by the given amount", lambda: encrypt("abc", 1),    "bcd"),
    ("encrypt wraps correctly",                    lambda: encrypt("xyz", 2),    "zab"),
    ("encrypt with a negative shift",              lambda: encrypt("bcd", -1),   "abc"),
    ("encrypting by 0 leaves text unchanged",      lambda: encrypt("hello", 0),  "hello"),
]

decrypt_tests = [
    ("decrypt shifts backwards by the given amount",   lambda: decrypt("bcd", 1),                      "abc"),
    ("decrypt wraps backwards past 'a'",               lambda: decrypt("ab", 3),                       "xy"),
    ("decrypt with a negative shift",                  lambda: decrypt("abc", -1),                     "bcd"),
    ("decrypt undoes a matching encrypt (round trip)", lambda: decrypt(encrypt("hello world", 7), 7),  "hello world"),
    ("decrypting by 0 leaves text unchanged",          lambda: decrypt("hello", 0),                    "hello"),
]


# ============================================================
# SUBPROGRAMS
# ============================================================

def shift_letter(letter, shift):
    """
    Procedure:
        shift_letter
    Parameters:
        letter, a string
        shift, an integer
    Purpose:
        Perform a Caesar shift on a letter.
    Product:
        shifted_letter, a string
    Preconditions:
        letter is a string of length 1
        letter is in the range [a-z] or [A-Z]
    Postconditions:
        shifted_letter has length 1
        shifted_letter is in the range [a-z] or [A-Z]
        shifted_letter has the same case as letter
        shifted_letter is shift letters ahead of letter in the alphabet,
            treating the alphabet as circular (so the letter after z is a,
            and the letter before a is z), within the same case
    """
    # TODO: implement this.
    #
    # Hints:
    #   - ord(letter) gives you the character's numeric code; chr(number)
    #     converts a number back into a character.
    #   - ord('a') and ord('A') are useful reference points for working
    #     out a letter's position in the alphabet (0-25), regardless of
    #     case.
    #   - Python's % operator already wraps negative numbers around
    #     correctly, e.g. -1 % 26 gives 25, not -1. You shouldn't need
    #     any special handling for negative shifts beyond using %.
    pass

def is_letter(character):
    """
    Procedure:
        is_letter
    Parameters:
        character, a string
    Purpose:
        Determine if a given character is a letter or not
    Product:
        result, a Boolean
    Preconditions:
        character is a string of length 1
    Postconditions:
        if character in [a-z] or character in [A-Z]:
            result = True
        else:
            result = False
    """
    pass
    # TODO: implement this
    #
    # Hint: Python strings have a built-in method that checks
    # whether all characters in a string are alphabetic.
    # Can you find it? (Try: help(str) in the Python shell)

def shift_string(text, shift):
    """
    Procedure:
        shift_string
    Parameters:
        text, a string
        shift, an integer
    Purpose:
        # TODO: describe what this function does, in your own words.
    Product:
        shifted_text, a string
    Preconditions:
        # TODO: what must be true about `text` and `shift`? Think about
        #       what shift_letter needs
    Postconditions:
        # TODO: what must be true about `shifted_text`, in terms of
        #       `text` and `shift`?
    """
    # TODO: implement this.
    #
    # Hint: build up the result one character at a time. For each
    # character in text, if it's a letter, shift it using
    # shift_letter; otherwise, leave it exactly as it is.
    # You should use is_letter()!
    pass

def encrypt(text, shift):
    """
    Procedure:
        encrypt
    Parameters:
        text, a string
        shift, an integer
    Purpose:
        # TODO
    Product:
        ciphertext, a string
    Preconditions:
        # TODO
    Postconditions:
        # TODO
    """
    # TODO: implement this using shift_string.
    pass


def decrypt(ciphertext, shift):
    """
    Procedure:
        decrypt
    Parameters:
        ciphertext, a string
        shift, an integer — the same shift originally used to encrypt it
    Purpose:
        # TODO
    Product:
        text, a string
    Preconditions:
        # TODO
    Postconditions:
        # TODO — what should be true about decrypt(encrypt(text, shift), shift)?
    """
    # TODO: implement this using shift_string.
    pass

def main():
    """
    Procedure:
        # TODO
    Parameters:
        # TODO
    Purpose:
        # TODO
    Product:
        # TODO
    Preconditions:
        # TODO
    Postconditions:
        # TODO
    """
    print("Caesar Cipher")
    print("1. Encrypt")
    print("2. Decrypt")
    choice = input("Choose an option (1 or 2): ")
    text = input("Enter your message: ")
    shift = int(input("Enter the shift amount: "))

    # TODO: call encrypt or decrypt based on choice, and print the result
    pass

# ============================================================
# MAIN PROGRAM
# ============================================================

# run_tests(shift_letter_tests)
# run_tests(is_letter_tests)
# run_tests(shift_string_tests)
# run_tests(encrypt_tests)
# run_tests(decrypt_tests)
# main()
