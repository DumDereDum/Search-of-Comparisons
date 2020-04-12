from .preparing import *


def find_comparison_with_prepositions(filename):
    # comparison_words = [' как будто ', ' чем ', ' будто ', ' точно ', ' как ',  ' словно ']
    # comparison_upper_words = [' КАК БУДТО ', ' ЧЕМ ', ' БУДТО ', ' ТОЧНО ', ' КАК ',  ' СЛОВНО ']

    comparison_words = [' как будто ', ' чем ', ' будто ', ' точно ', ' словно ']
    comparison_upper_words = [' КАК БУДТО ', ' ЧЕМ ', ' БУДТО ', ' ТОЧНО ', ' СЛОВНО ']

    count = 0

    change_to_text_dir()
    f = open('tmp_prepared.txt', 'r')
    text = f.read()
    f.close()
    os.remove('tmp_prepared.txt')

    splited_text = text.splitlines()

    change_to_res_dir()
    f = open(filename[:-4]+'_comparison.txt', 'w')
    for sentence in splited_text:
        sentence = ' ' + sentence
        for word in comparison_words:
            if word in sentence.lower():
                count += 1
                i = comparison_words.index(word)
                # sentence = sentence.replace(word, comparison_upper_words[i])
                sentence = sentence.lower().replace(word, comparison_upper_words[i])
                # print(sentence)
                f.write(sentence + '\n')
                break
    f.close()

    print('\nВ файле ' + filename + ' найдено: ' + str(count) + ' сравнений с предлогом')
