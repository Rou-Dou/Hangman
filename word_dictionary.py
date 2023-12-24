import csv


def word_dictionary_create(file_name):

    """ (csv) -> dict

    input word_dictionary csv and output a dictionary of values

    >> word_dictionary_create(word_dictionary.csv)
    {'word' : 'hello', 'name' : ['jerry', 'bob']

    """

    # read csv file to a list of dictionaries
    with open(file_name, 'r', encoding='utf-8-sig') as file:
        csv_reader = csv.DictReader(file)
        data = [row for row in csv_reader]

    # initialize dict_str with open curly bracket
    dict_str = '{'

    # loop through rows removing unneeded characters and header names
    for row in data:

        # if it is not the beginning of the string, append commas
        if dict_str != '{':
            dict_str += ', '
        current_str = str(row)
        new_str = current_str.replace\
        ('{', '').replace\
        ('}', '').replace\
        (':', '').replace\
        ("'Index'", '').replace\
        ("'Word'", '').replace \
        ("'Usage'", '').replace\
        ("'Word Length'", '').strip()

        # create variable i which counts the number of values in each row set
        i = new_str.count(',')

        # create variable comma_value which updates throughout the while to track how many items are left
        comma_value = new_str.count(',')

        # loop through rows and append values to str until all values have been added
        # we kill the loop by searching for commas, each loop a comma is removed,
        # when there are no more commas the loop breaks in the final 'else'
        # the next row is called and the loop repeats.
        while new_str.count(',') >= 0:

            # find the current index in order to split the current value from new_str
            current_index = new_str.find(',')

            # store the sliced value in split_str
            split_str = new_str[:current_index]

            # if it is the first vale, append a colon, this will indicate it is the value in the map
            if comma_value == i:
                dict_str += split_str + ' : '

            # if it is the second value, we add an open bracket to begin the list followed by the str and a comma
            elif comma_value == i - 1:
                dict_str += '[' + split_str + ', '

            # if there are additional values we append the string and then a comma
            elif 0 < comma_value < i:
                dict_str += split_str + ', '

            # for the final value in the str we append the string followed by a closing bracket for the list
            # we break the loop here
            else:
                dict_str += split_str + "']"
                break

            # update the str after appending to dict_str by removing the split str then add a comma in order to prepare
            # the next item in the dictionary
            new_str = new_str.replace(split_str + ', ', '').strip()

            # update the comma count to inform the while condition
            comma_value = new_str.count(',')

    # complete the dictionary with a final closing curly bracket
    dict_str += '}'

    # return the evaluated dictionary to be assigned to a variable
    return eval(dict_str)
