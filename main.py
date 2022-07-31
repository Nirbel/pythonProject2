from os import listdir
from os.path import isfile, join
from prettytable import *


path = ".\Log"
words = ['debug','info' ,'error','fatal']

def is_log_file(file_name):
    return file_name.endsWith('.log')


    my_Table= PrettyTable()
    my_Table.field_names =["File Name" ,"String","Count (number of instances)"]    #add headlines  to the table
    my_Table.add_rows(result_list)    #add data from the result list

    f = open('report.html', 'w')     #create blank html page for write
    f.write(my_Table.get_html_string(attributes={'border': 1, 'style': 'text-align: center; '}))    #write my data to the html page and desing the table
    f.close()    #close the doc

# is_log_file(path, words)
with open("report.html", "r") as fp:      #Return results report to the terminal as a table
    html = fp.read()

x = from_html_one(html)
print(x)

