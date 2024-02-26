a = 'This is a beautiful nigth on the Atlantic'

index_found = a.find('beautiful')
len_word = len('beautiful')
first = a[:index_found]
second = a[index_found + len_word:]

final_sentence = first + 'terrible' +second

print(final_sentence)