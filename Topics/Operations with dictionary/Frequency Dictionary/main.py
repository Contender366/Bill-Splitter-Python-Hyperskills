sentence = input().lower().split()
for word in set(sentence):
    print(word, sentence.count(word))

