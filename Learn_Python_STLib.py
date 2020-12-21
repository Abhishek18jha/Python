#with operator  that will automaticaly close file for you when you are done processing.
with open("text.txt") as file_handler:
    for line in file_handler:
        print(line)

#CSV File reading Module

import csv

def csv_reader(file_obj):
    """
    Read a csv file
    """
    reader = csv.DictReader(file_obj,delimiter =",")
    for line in reader:
        print(line["variable_name"]+ " : "+ line["dataset"])
    

if __name__ =="__main__":
    csv_path ="TB.csv"
    with open(csv_path) as f_obj:
        csv_reader(f_obj)

# writing a csv file

import csv 
def csv_writer(data,path):

    with open(path,"w",newline='')as csv_file:
        writer = csv.writer(csv_file, delimiter=',')
        for line in data:
            writer writerow(line)
if _name__ == "__main__":
    data =["f_n, l_n,c,".split(",")]
    path