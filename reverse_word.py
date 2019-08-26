def spin_words(sentence):
    word_list = [(lambda i: i[::-1] if len(i) >=5 else i)(i) for i in sentence.split(" ")]
    return " ".join(word_list)

print(spin_words("Welcome"))#, "emocleW")
print(spin_words("Hi my honey i love you Welcome to me"))