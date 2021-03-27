import csv
import json

def filter_champions(file_name, output_file_name, desired_columns, champion_dictionary):
    valid_length = 1150
    output_file = open(output_file_name, "w")
    champion_dictionary = json.load(open(champion_dictionary, 'r'))
    with open(file_name, "r") as input_file:
        reader = csv.reader(input_file, delimiter = ',')
        first_row = True
        selected_columns = []
        i = 0
        for row in reader:
            #read first line from csv to obtain the indexes to obtain
            #store the length of the title line
            if first_row:
                selected_columns = get_selected_column_indexes(row, desired_columns)
                print('The selected indexes are:', selected_columns)
                first_row = False
                output_file.write(','.join(get_selected_columns(row,selected_columns)))
            #read each line and write it to a seperate file
            #verify the length of the line is correct, if incorrect then next
            elif len(row) == valid_length:
                cols = get_selected_columns(row,selected_columns)
                cols = convert_to_champion_key(cols, champion_dictionary)
                output_file.write('\n')
                output_file.write(','.join(cols))
                i += 1
        print('Found and filtered', i, 'valid matches with no missing data')
    output_file.close()
    print('Done filtering data.')

def filter_champions_no_header(file_name, output_file_name, desired_columns, champion_dictionary):
    valid_length = 1150
    output_file = open(output_file_name, "w")
    champion_dictionary = json.load(open(champion_dictionary, 'r'))
    with open(file_name, "r") as input_file:
        reader = csv.reader(input_file, delimiter = ',')
        first_row = True
        selected_columns = []
        i = 0
        for row in reader:
            #read first line from csv to obtain the indexes to obtain
            #store the length of the title line
            if first_row:
                selected_columns = get_selected_column_indexes(row, desired_columns)
                print('The selected indexes are:', selected_columns)
                first_row = False
            #read each line and write it to a seperate file
            #verify the length of the line is correct, if incorrect then next
            elif len(row) == valid_length:
                cols = get_selected_columns(row,selected_columns)
                cols = convert_to_champion_key(cols, champion_dictionary)
                output_file.write(','.join(cols))
                output_file.write('\n')
                i += 1
        print('Found and filtered', i, 'valid matches with no missing data')
    output_file.close()
    print('Done filtering data.')
       
def get_selected_column_indexes(row, desired_columns):
    selected_columns = []
    for i in range(len(row)):
        col = row[i]
        if col in desired_columns:
            selected_columns.append(i)
    return selected_columns

def get_selected_columns(row, selected_columns, champion_dictionary=None):
    result = []
    for i in range(len(row)):
        if i in selected_columns:
            if champion_dictionary is not None:
                result.append(champion_dictionary[str(row[i])]['key'])
            else:
                result.append(row[i])
    head = result.pop(0)
    if(head == 'Win'):
        result.append('1')
    elif(head == 'Fail'):
        result.append('0')
    return result

def convert_to_champion_key(arr, champion_dictionary):
    res = []
    for i in range(len(arr) - 1):
        el = arr[i]
        res.append(str(champion_dictionary[str(el)]['key']))
    res.append(arr[len(arr) - 1])
    return res
