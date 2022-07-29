
from os import listdir
from os.path import isfile, join
import pandas as pd
from prettytable import PrettyTable




path = r"C:\Users\Alpha\PycharmProjects\pythonProject2\Log"
with open("Log/A.log") as file1, open("Log/B.Log") as file2, open("Log/C.log") as file3:
    line1 = file1.read()
    line2 = file2.read()
    line3 = file3.read()
    print(line1,line2,line3)
words = ['debug','info' ,'error','fatal','warning']



def key_sorted(a):
    return a[2]

def main_function(path: str, words: list):
    data = dict()
    log_files = []
    onlyfiles = [f for f in listdir(path) if
                 isfile(join(path, f))]
    for f in onlyfiles:
        file = f.split(".")
        if file[-1] == "log":
            log_files.append(f)

    for file in log_files:
        data[file] = dict()
        with open(path+ "\\" +file) as f:
            lines = f.readlines()
            for word in words:
                for line in lines:
                    while line.find(word) != -1:
                        try:
                            data[file][word] += 1
                        except:
                            data[file][word] = 1
                        line = line[line.find(word) + len(word):]
    res_list = []
    for file in data.keys():
        for key in data[file].keys():
            res_list.append((file, key, data[file][key]))

    res_list = sorted(res_list, key=key_sorted, reverse=True)

    A = PrettyTable()
    A.field_names =["File Name" ,"String","Count (number of instances)"]
    A.add_rows(res_list)

    f = open('report.html', 'w')
    f.write(A.get_html_string())
    f.close()

main_function(path, words)
from prettytable import from_html_one

with open("report.html", "r") as fp:
    html = fp.read()

x = from_html_one(html)
print(x)

