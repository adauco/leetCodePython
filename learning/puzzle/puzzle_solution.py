import re
import os

pattern_ = r'\d{3}-\d{3}-\d{4}'
test_string = 'here is a phone number 123-123-3322'
file_ = 'text_file.txt'


def search_func(file, pattern):
    f = open(file, 'r')
    text = f.read()
    print(re.findall(pattern, text))
    if re.search(pattern, text):
        return re.search(pattern, text)
    else:
        return ''


search_func(file_, pattern_)
