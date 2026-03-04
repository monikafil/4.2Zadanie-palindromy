def is_palindrome(word):
    """
    Sprawdzam,czy podany wyraz jest palindromem.

    Przyklad
    test(string)-argument, np. "kajak"

    True-jesli jest palindromem
    False-jesli nie jest
    """

    return word == word[: :-1]