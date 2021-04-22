import csv
import json


# filter the desire columns, write the header file
def filter(file_name, output_file_name, desired_columns, champion_dictionary, write_headers):
    valid_length = 1150
    input_file = open(file_name, "r")
    output_file = open(output_file_name, "w", newline='')
    champion_dictionary = json.load(open(champion_dictionary, 'r'))
    reader = csv.reader(input_file, delimiter=',')
    writer = csv.writer(output_file, delimiter=',')
    first_row = True
    selected_columns = []
    i = 0
    for row in reader:
        # read first line from csv to obtain the indexes to obtain
        # store the length of the title line
        if first_row:
            selected_columns = get_selected_column_indexes(row, desired_columns)
            print('The selected indexes are:', selected_columns)
            first_row = False
            if write_headers:
                writer.writerow((get_selected_columns(row, selected_columns))) #write headers
            # read each line and write it to a seperate file
            # verify the length of the line is correct, if incorrect then next
        elif len(row) == valid_length:
            selected = get_selected_columns(row, selected_columns)
            cols = convert_to_champion_key(selected, champion_dictionary)
            writer.writerow(cols)
            i += 1
    print('Found and filtered', i, 'valid matches with no missing data')
    input_file.close()
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
    if head == 'Win':
        result.append('1')
    elif head == 'Fail':
        result.append('0')
    return result


def convert_to_champion_key(arr, champion_dictionary):
    res = []
    for i in range(len(arr) - 1):
        el = arr[i]
        res.append(str(champion_dictionary[str(el)]['key']))
    res.append(arr[len(arr) - 1])
    return res
