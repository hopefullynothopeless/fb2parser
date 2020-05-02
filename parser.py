from lxml import etree
import re, json

data = {

}

def get_tree(bookName):
    return etree.parse(bookName)

tree = get_tree('book.fb2')

text = tree.xpath('descendant-or-self::text()')

for sentence in text:
    if re.search("[a-z|A-Z|0-9]+", sentence):
        text.remove(sentence)

def remove_empty_strings(arr):
    text = [sentence.rstrip() for sentence in arr]
    return [sentence for sentence in text if len(sentence) >= 1]

text_new = remove_empty_strings(text)

def split_elements(arr):
    # words_array = [re.split(r' ', sentence) for sentence in arr]
    words_array = []
    for sentence in arr:
        words = re.split(r' ', sentence)
        words_array.extend(words)

    return words_array
    # return words_array.copy()

words = split_elements(text_new)

for word in words:
    repeats = words.count(word)
    data.update({word : repeats})

max_values = {}
max = 0
for key, value in data.items():
    if value > max:
        if len(str(key)) >= 3:
            max = value
            max_values[key] = value

for pair in max_values.items():
    print(pair)

# print(str(type(tree)) + '  ' + str(sys.getsizeof(tree)))
# [\w]+_?
