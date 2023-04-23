#todo: На вход подается предложение из нескольких слов. Слова разделены пробелами.
# Напечатайте самое длинное слово в этом предложении. 


if __name__ == "__main__":
    string = input("Введите предложение из нескольких слов\n")

    string_list = string.split(' ')
    len_list = [len(x) for x in string_list]

    print(string_list[len_list.index(max(len_list))])