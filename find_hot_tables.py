import csv


def find_hot_tables(file_name="log_week_end.csv"):
    debug = False
    write_to_file = False
    target_column = 2
    analyzepattern = "tbl_"

    result = {}

    csvfile = open(file_name)
    reader = csv.reader(csvfile, delimiter=',', quotechar='"')
    n = len(list(reader))
    if debug:
        print(n)
    csvfile = open(file_name)
    reader = csv.reader(csvfile, delimiter=',', quotechar='"')
    step = 0
    for row in reader:
        if debug:
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
    if write_to_file:
        f = open("result.csv", "w")
        for k in result.__reversed__():
            if debug:
                print(k, result[k])
            f.write(str(k) + ", " + str(result[k]) + "\n")
        f.close()
    return list(result.items())


if __name__ == '__main__':
    find_hot_tables()
