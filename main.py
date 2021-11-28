sentence = input()
def sort_sentence(sentence):
    probel = " "
    izn_sentence = sentence + probel
    count = 0
    word = 0
    len_word = 0
    result = []
    tek_world = ''
    while count < len(izn_sentence):
        if (izn_sentence[count] == ' '):
            word = word + 1
            count = count + 1
            len_word = 0
            result.append(tek_world.lower())
            tek_world = ''
        else:
            len_word = len_word + 1
            count = count + 1
            tek_world = tek_world + izn_sentence[count - 1]

    sorted_list = list(sorted(result, key = len))
    str_result = ' '.join(sorted_list )
    first_word = str_result[0].upper()
    last_result = str_result[0].upper() + str_result[1:]
    print(last_result)
    return(last_result)

sort_sentence(sentence)
