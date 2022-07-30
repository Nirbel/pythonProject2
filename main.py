
from os import listdir
from os.path import isfile, join
from prettytable import *




path = ".\Log"
words = ['debug','info' ,'error','fatal']


#return the num of word events
def key_sorted(a):
    return a[2]

def main_function(path: str, words: list):  ## The function get path and words and create html page with the relevant details.
    data = dict()
    log_files = []
    onlyfiles = [f for f in listdir(path) if
                 isfile(join(path, f))] # add all the files in the directory to the onlyfiles list
    for f in onlyfiles:
        file = f.split(".")
        if file[-1] == "log":
            log_files.append(f) #add all the log files to the log file_list

    for file in log_files:
        data[file] = dict()
        with open(path+ "\\" +file) as f:
            lines = f.readlines()
            for word in words:
                for line in lines:
                    while line.find(word) != -1:# find return -1 when search is fail
                        try:
                            data[file][word] += 1 #if there a value already so update plus one
                        except:
                            data[file][word] = 1 #this to sitouation when its first time that write value
                        line = line[line.find(word) + len(word):] #to cut the line from the last word that found
    res_list = []#result list
    for file in data.keys():
        for key in data[file].keys():
            res_list.append((file, key, data[file][key]))

    res_list = sorted(res_list, key=key_sorted, reverse=True)#resrve = True is the Descending sort by num of repetition


    myTable= PrettyTable()
    myTable.field_names =["File Name" ,"String","Count (number of instances)"]#add headlines  to the table
    myTable.add_rows(res_list) #add data from the result list

    f = open('report.html', 'w')#create blank html page for write
    f.write(myTable.get_html_string())#write my data to the html page
    f.close()#close the doc

main_function(path, words)
with open("report.html", "r") as fp:#Return results report to the terminal as a table
    html = fp.read()

x = from_html_one(html)
print(x)

