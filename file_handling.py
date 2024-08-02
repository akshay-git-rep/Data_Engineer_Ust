"""
f_sample = open("sample.txt")
read_content = f_sample.read();
print(read_content)
f_sample.close()
"""

"""
f_demo = open("demo.txt", "w")
f_demo.write("first line")
f_demo.write("second line")
f_demo.write("third line")
f_demo.write("\nfirst line\n")
f_demo.write("second line\n")
f_demo.write("third line\n")
f_demo.close()
"""
"""
f_demo = open("demo.txt","a")
f_demo.write("*"*60)
f_demo.close()
"""
"""
f_read = open("demo.txt")
read_file = f_read.read()
print(read_file)
"""

import csv

with open("portfolio.csv",mode="w",newline="") as pfile:
    pfile_writer = csv.writer(pfile,delimiter=",",quotechar='"',quoting=csv.QUOTE_MINIMAL)
    #pfile_writer.writerow("akshay, sudhir")
    pfile_writer.writerow(["name","age"])
    pfile_writer.writerow(["akshay","25"])
    pfile_writer.writerow(["sudhir","25"])
    pfile_writer.writerow(["kalavathi","25"])

with open("portfolio.csv",mode="r",) as pfile:
    csv_reader = csv.reader(pfile,delimiter=",")
    line_count = 0
    for row in csv_reader:
        if line_count == 0:
            print(f'{",".join(row)}')
            line_count += 1
        else:
            print(f'{row[0]}\t{row[1]}')
            line_count += 1
    print(f'read {line_count-1} shares from the portfolio')


data = [
        ["name","age","city"],
        ["akshay",25,"bangalore"],
        ["sudhir",28,"bangalore, bihar"]
    ]

with open("output.csv",mode="w",newline="") as file:
    output = csv.writer(file,delimiter=",")
    output.writerows(data)







