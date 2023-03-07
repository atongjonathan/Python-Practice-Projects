import string
def is_pangram(s):
    punc = '''!()-[]{};:'"\,<>./?@#$%^&*_~ '''
    for letter in s:
        if letter in punc:
            s = s.replace(letter, '').lower()
    alphabet = string.ascii_lowercase
    for word in s:
        alphabet = alphabet.replace(word, '')
    return (len(alphabet))==0
        

print(is_pangram("The quick brown ,,fox jumps over the la)(zy dog"))