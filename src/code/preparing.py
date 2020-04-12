import os


text_path = ''


def find_path():
    global text_path
    text_path = os.getcwd()


def change_to_text_dir():
    os.chdir(path=text_path+'/src/text')


def change_to_code_dir():
    os.chdir(path=text_path+'/src/code')


def change_to_res_dir():
    os.chdir(path=text_path+'/res')


def get_path():
    return text_path


def get_files():
    path = os.getcwd()
    files = os.listdir(path=path + '/src/text')
    return files


def preparing(filename):
    change_to_text_dir()
    f = open(filename, 'r')
    p = open('tmp_prepared.txt', 'w')

    line = f.readline()
    while line:
        line = f.readline()
        if line != '\n':
            line = line.replace('.', '\n')
            line = line.replace(';', '\n')
            line = line.replace('!', '\n')
            line = line.replace('?', '\n')
            # print(line)
            p.write(line)

    f.close()
    p.close()
