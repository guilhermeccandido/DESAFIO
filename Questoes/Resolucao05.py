import string
def is_anagram_of_palindrome(input_string):
    char_count = {}
    valid_chars = string.ascii_letters + string.punctuation
    filtered_input = ''.join(char for char in input_string if char in valid_chars)

    for char in filtered_input:
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1
    odd_count = 0
    for count in char_count.values():
        if count % 2 != 0:
            odd_count += 1
    return odd_count <= 1

input_string = input("Digite a string para verificação: ")
is_anagram_palindrome = is_anagram_of_palindrome(input_string)
print(is_anagram_palindrome)