def digits_to_letters(digits: int):
    """ 将数字转换为字母"""
    return ''.join(chr(int(d) + ord('a')) for d in str(digits))


def letters_to_digits(letters: str):
    """ 将字母转换为数字"""
    return ''.join(str(ord(letter) - ord('a')) for letter in letters)


id = digits_to_letters(3812427104)
sta_date = "content"

end_date = id + "_" + sta_date

print(end_date)

print( letters_to_digits("dibcechbae"))



