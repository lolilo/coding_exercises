from sys import argv
from os.path import exists
import os
dir = os.path.dirname(__file__)

# Takes in Python script and one file as arguments. 
script, input_file = argv
isValid = True

# Check if input_file exists.
if not exists(input_file):
    print "%r does not exist!" % input_file
    isValid = False

def write_1000_ids_to_file(file_count, id_index, num_ids):
    id_counter = 0
    new_file_name = '1000_sets/example.com_user_ids_' + "%03d" % (file_count,)
    new_file_path = os.path.join(dir, new_file_name)
    new_file_handler = open(new_file_path, 'a')
    while id_counter < 1000 and id_index < num_ids:
        new_file_handler.write(ids[id_index])
        id_counter += 1
        id_index += 1
    new_file_handler.close()
    print new_file_name + ' complete. current id_index is', id_index
    return id_index

if isValid:
    ids = open(input_file).readlines()
    id_index = 0
    file_count = 0
    num_ids = len(ids)
    while id_index < num_ids:
        id_index = write_1000_ids_to_file(file_count, id_index, num_ids)
        file_count += 1
