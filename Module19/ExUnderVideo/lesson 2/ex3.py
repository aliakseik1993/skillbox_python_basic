def histogramma(text):
    text_dict = dict()
    for sym in text:
        if sym in text_dict:
            text_dict[sym] += 1
        else:
            text_dict[sym] = 1
    return text_dict

text_input = input("Введите текст: ")
result = histogramma(text_input)

for i_result in sorted(result):
    print("{0} : {1}".format(i_result, result[i_result]))

print("Максимальная частота:", max(result.values()))