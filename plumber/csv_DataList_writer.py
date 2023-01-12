def write_list(data_list, file_name):
    header = data_list[0]
    file = open(file_name, 'a')
    file.write(str(header))

    list_no = -1
    for data_row in data_list:
        list_no = list_no + 1
        if list_no >= 1:
            data_row = data_list[list_no]
            file.write("\n"+data_row)

def csv_to_exel():
    print("LEFT")

def Exel_to_csv():
    print("LEFT")