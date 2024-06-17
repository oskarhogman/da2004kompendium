def is_string_palindrome(s):
    """
    Checks if string is a palindrome
    """
    return s == s[::-1]

def palindrome_rows(filename):
    with open(filename, 'r') as fp:
        for row in fp:
            yield is_string_palindrome(row.strip('\n'))

p_rows = palindrome_rows('palindrome.txt')
i=1
for p in p_rows:
    print("Row", i, "palindrome?", p)
    i += 1
