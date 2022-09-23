import csv

target_column = 2
analyzepattern = "tbl_"

result = {}

csvfile = open("log_week_end.csv")
reader = csv.reader(csvfile, delimiter=',', quotechar='"')
n = len(list(reader))
print(n)
csvfile = open("log_week_end.csv")
reader = csv.reader(csvfile, delimiter=',', quotechar='"')
step = 0
for row in reader:
    print(str(reader.line_num) + "/" + str(n))
    # print(row)
    for word in row[target_column].replace(",", " ").split(" "):
        if word.__contains__(analyzepattern):
            if word in result:
                result[word] += 1
            else:
                result[word] = 1
    step += 1

result = {k: v for k, v in sorted(result.items(), key=lambda item: item[1])}

f = open("result.csv", "w")
for k in result.__reversed__():
    print(k, result[k])
    f.write(str(k) + ", " + str(result[k]) + "\n")
f.close()
