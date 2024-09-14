def is_palindrome(string):
    return string == string[::-1]


def count_palindrome(string):
    count = 0
    for i in range(len(string)):
        for j in range(i+1, len(string) + 1):
            if is_palindrome(string[i:j]):
                count += 1
    return count


string = "abcba"
count = count_palindrome(string)
print(count)
