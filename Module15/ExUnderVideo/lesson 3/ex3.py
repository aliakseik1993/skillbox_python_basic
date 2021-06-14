count = [0,0,0]
words = []
for i in range(3):
    print(f"Введите слово №{i + 1}: ", end = "")
    word = input()
    words.append(word)
text_user = input("Слово из текста: ")
while text_user != "end":
    for index in range(3):
        if words[index] == text_user:
            count[index] += 1
    text_user = input("Слово из текста: ")

for i in range(3):
    print(words[i], ":", count[i])