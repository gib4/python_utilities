import os
from openpyxl import Workbook
import numpy as np
from datetime import datetime, timedelta # Used to get the button press time
import libs.file_operations as fo

# time for button press / release
button_press_time          = 0
button_release_time        = 0
time_difference_seconds    = 0

location    = "C:\\Users\\dske\\Desktop\\Test_Michele_Melbourne\\Automate\\"
input_file  = "MissingTests.bat"
output_file = "test_list.xlsx"
outcomes    = ["NOT RUN","CRASHED", "FAILED", "WARNED", "PASSED"]


word        = "AUS-Telstra"
rep_word    = ""

# Reads a batch file and returns the list of tests
def read_batch(location, input_file):
    test_number = 0
    test_list   = []
    with open(location + input_file, "r") as file:
        lines = file.readlines()
    print ("Reading batch...")
    for line in lines:
        if line.strip():                                                                                    # Delete empty lines
            name_and_params = line.replace("perl ", "")                                                     # Remove "perl " from line
            test_name     = name_and_params.strip().replace(" ","_").replace(".pl","").replace("\n","")     # Save name of test to a variable
            test_list.append(test_name)
            print ("Test name : " + test_name)
            test_number+=1
    return test_list

# Working just fine
def get_folders(directory):
    folders = []
    for item in os.listdir(directory):
        if os.path.isdir(os.path.join(directory, item)):
            folders.append(item)
    return folders

# Working just fine
def write_to_excel(matrix, filename):
    print ("Writing to excel file...")
    workbook = Workbook()
    sheet = workbook.active
    for row in matrix:
        sheet.append(row)

    workbook.save(filename)

def check_string(string, outcome):
    substrings = ["FAIL", "WARN", "PASS"]
    if outcome != "CRASHED":
        for substring in substrings:
            if substring in string:
                return substrings.index(substring)+2
    #else:
        #with open(location + input_file, "r") as file:
        #    lines = file.readlines()
    #    return 1
    return 0

# Working just fine
def parse_file_names(directory):
    file_names = []
    try:
        for file in os.listdir(directory):
            if os.path.isfile(os.path.join(directory, file)):
                file_names.append(file)
    except:
        return file_names
        #print ("Error in parsing files, folder not found.")
    return file_names

def parse_docs(test_list, folder_location):
    print ("Parsing folders...")
    
    many_zeros = np.zeros(len(test_list), dtype=int)
    many_zeros = many_zeros.tolist()
    test_matrix = [test_list, many_zeros]
    folder_list = get_folders(folder_location)
    print (folder_list)
    for test in test_list:                                          # For each test in the list
        test_runs_counter = 0
        print ("Finding test outcome: " + test)
        for folder in folder_list:                                  # For each run (RUN 1, RUN 2, ...)
            for outcome in outcomes[1:5]:                                # For each outcome ("CRASHED", "FAILED", "PASSED")
                current_folder = folder_location + folder + "\\" + outcome
                files = parse_file_names(current_folder)
                for file in files:                                  # For each file in the outcome folder (TC-IS-TCP-USORD-Closure, ...)
                    if test in file:                                # Has been run
                        test_runs_counter +=1                       # Count the times the test has been run
                        #test_matrix [2][test_list.index(test)] = test_runs_counter
                        result = check_string(file,outcome)
                        if test_matrix [1][test_list.index(test)] < result:
                            test_matrix [1][test_list.index(test)] = result     # Update the result only if lower than PASS, see the hierarchy
                    #else:
                    #    test_matrix [1][test_list.index(test)] = 0 # NOT RUN


    transposed_matrix = np.array(list(zip(*test_matrix))) 

    test_total = np.array([0]*len(test_matrix[1])*2).reshape(len(test_matrix[1]),2)
    test_total = test_total.tolist()
    
    i = 0
    while (i <=4):
        test_total [i][0] = outcomes[i];
        test_total [i][1] = "=COUNTIF(B:B,"+str(i)+")";
        i+=1;


    # Concatenate the matrices side by side
    result = np.c_[transposed_matrix, test_total];
    return result.tolist()


print ("**************************************************************************")
button_press_time          = datetime.now()
test_list           = read_batch(location, input_file)
test_result_matrix  = parse_docs(test_list, location)
write_to_excel (list(test_result_matrix), location+output_file)
button_release_time        = datetime.now()

time_difference = button_release_time - button_press_time
time_difference_seconds = time_difference.total_seconds()
print("Operation ended in: ", time_difference_seconds)