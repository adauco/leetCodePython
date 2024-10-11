# Import necessary libraries
from difflib import SequenceMatcher


# Function to identify identical content
def mark_identical_content(text1, text2):
    s = SequenceMatcher(None, text1, text2)
    print(s)

    print('\x1b[6;30;42m' + "Equal" + '\x1b[0m', end='\n')
    print('\x1b[6;30;41m' + "Replace" + '\x1b[0m', end='\n')
    print('\x1b[6;30;43m' + "Delete" + '\x1b[0m', end='\n')
    print('\x1b[6;30;44m' + "Insert" + '\x1b[0m', end='\n')

    print("Text 1")
    print('\x1b[6;30;42m' + text1 + '\x1b[0m', end='')
    print("\nText 2")

    for tag, i1, i2, j1, j2 in s.get_opcodes():
        if tag == 'equal':
            print('\x1b[6;30;42m' + text1[i1:i2] + '\x1b[0m', end='')
        elif tag == 'replace':
            print('\x1b[6;30;41m' + text2[j1:j2] + '\x1b[0m', end='')
        elif tag == 'delete':
            print('\x1b[6;30;43m' + text1[i1:i2] + '\x1b[0m', end='')
        elif tag == 'insert':
            print('\x1b[6;30;44m' + text2[j1:j2] + '\x1b[0m', end='')
        else:
            print(tag)


def highlight_differences_html(s1, s2, match_color='black', change_color='red'):
    # Generate the matching blocks using SequenceMatcher
    matcher = SequenceMatcher(None, s1, s2)
    blocks = matcher.get_matching_blocks()

    # Find and highlight the differences in HTML
    result1 = ''
    result2 = ''
    cursor = 0
    for block in blocks:
        # Add the unchanged text before the current block
        result1 += f'<span style="color: {match_color};">{s1[cursor:block.a]}</span>'
        result2 += f'<span style="color: {match_color};">{s2[cursor:block.b]}</span>'

        # Add the changed text in the current block
        if block.size > 0:
            result1 += f'<span style="color: {change_color};">{s1[block.a:block.a+block.size]}</span>'
            result2 += f'<span style="color: {change_color};">{s2[block.b:block.b+block.size]}</span>'

        cursor = block.a + block.size

    # Add the last unchanged text after the last block
    result1 += f'<span style="color: {match_color};">{s1[cursor:]}</span>'
    result2 += f'<span style="color: {match_color};">{s2[cursor:]}</span>'

    # Return the original strings with differences highlighted in HTML
    return f'<div><p><strong>Text 1:</strong></p><pre>{result1}</pre>' \
           f'<p><strong>Text 2:</strong></p><pre>{result2}</pre></div>'


# Function to compare two texts visually
def main_compare_texts(text1, text2):
    mark_identical_content(text1, text2)
    print("\n" + highlight_differences_html(text1, text2))


text_1 = "word_cloud. A little word cloud generator in Python. Read more about it on the blog post or the website." \
         " Dhe code is tested against Python 3.7, 3.8, 3.9,"
text_2 = ". A little word cloud generator in JAVA. Read more about it on the blog post or the SITIO. " \
         "The code is tested against Python 3.7, 3.8, 3.9, ADAUCO"

# Compare two texts visually
main_compare_texts(text_1, text_2)

