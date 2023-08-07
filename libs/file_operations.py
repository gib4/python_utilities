import os
import shutil

# USEFUL CONSTANTS
#delete_files_matching()


# my_replace()
#location    = "C:\\Users\\dske\\Desktop\\Test_Michele_Melbourne\\Automate\\Run 2.1 - ipv4\\"
#input_file  = "failed.bat"
#output_file = "failed_run21_trace.bat"

# Set the directory where your text files are located
#directory = "C:/Users/dske/Desktop/Test_Michele_Melbourne/Automate/Run 1/CRASHED/"

# Define the target string to search for
#string1     = "Parameter 'NB1' IS NOT supported"
#string2     = "SIG_INT received."
#string3     = "[PERL WARNING] -> can't get COMMPROP"

# HTML Operations ---------------------------------------------------------
def get_test_time ():
    time_line = "</TD></TR><TR><TD>Duration:</TD><TD>" 0:15:49

def read_html_report(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        return file.read()

# Arguments: report path, delimiter string
# Return: List
def split_into_segments(report, delimiter):
    segments = report.split(delimiter)
    # Remove leading and trailing whitespaces from each segment
    segments = [segment.strip() for segment in segments]
    return segments

#def filter_lines_by_keywords(lines, keywords):
#    filtered_lines = [line.strip() for line in lines if any(keyword in line for keyword in keywords)]
#    return filtered_lines

def filter_lines_by_keywords(lines, keywords):
    #keywords = ["AT TX:", "DUT response is", "Expected response is:"]
    filtered_lines = []
    for line in lines:
        if any(keyword in line for keyword in keywords):
            filtered_lines.append(line.strip())
    return filtered_lines

# Folder Operations -------------------------------------------------------
# Create folder
def create_folder(folder_path):
    try:
        os.mkdir(folder_path)
        print(f"Folder '{folder_path}' created successfully.")
    except FileExistsError:
        print(f"Folder '{folder_path}' already exists.")

# Parse name of files in a folder
def parse_file_names(directory):
    file_names = []
    try:
        for file in os.listdir(directory):
            if os.path.isfile(os.path.join(directory, file)):
                file_names.append(file+"\n")
    except:
        return file_names
    return file_names

# Move file
# Arguments: source file path, destination folder
def move_file(source_file, destination_folder):
    try:
        shutil.move(source_file, destination_folder)
        print(f"File '{source_file}' moved to '{destination_folder}'.")
    except FileNotFoundError:
        print(f"File '{source_file}' not found.")
    except shutil.Error as e:
        print(f"Error occurred while moving the file: {e}")

# Move all files in a Directory containing the strings: string1, string2, string3
def move_files_matching(directory, string1, string2="xoxoxo", string3="xoxoxo"):
    for root, dirs, files in os.walk(directory):
        for filename in files:
            file_path = os.path.join(root, filename)
            with open(file_path, "r", encoding="latin-1") as file:
                content = file.read()
                file.close()
                if string1 in content: 
                    move_file(file_path, os.path.join(root, string1))
                elif string2 in content: 
                    move_file(file_path, os.path.join(root, string2))
                elif string3 in content:
                    move_file(file_path, os.path.join(root, string3))
                else:
                    print(f"NotMove: {file_path}")

# Delete a single file
def delete_file(file_path):
    try:
        os.unlink(file_path)
        print(f"Deleted: {file_path}")
    except PermissionError as e:
        print(f"Skipped (File in use): {file_path}")
    except OSError as e:
        print(f"Error deleting {file_path}: {e}")

# Delete all files in a Directory containing the strings: string1, string2, string3
def delete_files_matching(directory, string1, string2="xoxoxo", string3="xoxoxo"):
    for root, dirs, files in os.walk(directory):
        for filename in files:
            file_path = os.path.join(root, filename)
            with open(file_path, "r", encoding="latin-1") as file:
                content = file.read()
                file.close()
                if string1 in content or string2 in content or string3 in content:
                    delete_file(file_path)
                else:
                    print(f"NotDele: {file_path}")

# TODO create delete Traces script
def delete_files_withextension(directory, extension):
        # for root, dirs, files in os.walk(directory):
        # for filename in files:
        #     file_path = os.path.join(root, filename)
        #     with open(file_path, "r", encoding="latin-1") as file:
        #         content = file.read()
        #         file.close()
        #         if string1 in content or string2 in content or string3 in content:
        #             delete_file(file_path)
        #         else:
        #             print(f"NotDele: {file_path}")
        print('todo')
        
# BATCH OPERATIONS --------------------------------------------------------------
def delete_lines_with_string(file_path, string_to_find):
    # Read the file and store the lines in a list
    with open(file_path, 'r') as file:
        lines = file.readlines()

    # Filter out the lines that contain the specified string
    filtered_lines = [line for line in lines if string_to_find not in line]

    # Write the filtered lines back to the file
    with open(file_path, 'w') as file:
        file.writelines(filtered_lines)

    print(f"Lines containing '{string_to_find}' have been deleted from the file.")

# Append start and kill trace in batch file
def append_trace(script_name, trace_name):
    start_ulogr = "perl StartTrace_Ulogr.pl " + trace_name +".trace\n"
    stop_ulogr  = "perl Kill_trace.pl"
    output = start_ulogr + script_name.strip() + "\n" + stop_ulogr + "\n"                 # perl StartTrace_Ulogr.pl tracename.trace
    return output

def split_in_two():
    print()



# Parse name of files in a folder
# TODO repair function
def list_files_in_directory(directory_path):
    file_list = []
    if os.path.exists(directory_path):
        for root, dirs, files in os.walk(directory_path):
            for file in files:
                file_list.append(os.path.join(root, file))
        return file_list
    else:
        print("Directory not found.")

# Delete the rest of the line after the string
def delete_after(location, input_file, output_file, string):
    modified_lines      = []

    with open(location + input_file, "r") as file:
        lines = file.readlines()

    for line in lines:
        if line.strip():   
            modified_lines.append(line.split(string)[0] + "\n")
    with open(location + output_file, "w") as file:
            file.writelines(modified_lines)

# Create a batch from a list 
def list_to_batch(location, input_file, output_file, word):
    with open(location + input_file, "r") as file:
        lines = file.readlines()
    modified_lines      = []

    for line in lines:
        if line.strip():                                                                                    # Delete empty lines
            modified_line   = line.split(word)[0] + "\n"                                                    # Delete everything after AUS-Telstra in a line
            name_and_params = modified_line.replace("perl ", "")                                            # Remove "perl " from line
            trace_name     = name_and_params.strip().replace(" ","_").replace(".pl","").replace("\n","")    # Save name of test to a variable
            rep_word        = append_trace(modified_line, trace_name)
            if "ipv6" in line:
                modified_lines_ipv6.append(rep_word)
                test_number_ipv6+=1
            else:
                modified_lines.append(rep_word)
                test_number_other+=1
            #print ("**************************************************************************")
            #print ("Rep word :")
            #print (rep_word)
            test_number+=1

    with open(location + output_file.replace(".bat", "ipv6.bat"), "w") as file:
        file.writelines(modified_lines_ipv6)


def my_replace(location, input_file, output_file, word = "AUS-Telstra"):
    test_number         = 0
    test_number_ipv6    = 0
    test_number_other   = 0
    with open(location + input_file, "r") as file:
        lines = file.readlines()

    modified_lines      = []
    modified_lines_ipv6 = []

    for line in lines:
        if line.strip():                                                                                    # Delete empty lines
            modified_line   = line.split(word)[0] + "\n"                                                    # Delete everything after AUS-Telstra in a line
            name_and_params = modified_line.replace("perl ", "")                                            # Remove "perl " from line
            trace_name     = name_and_params.strip().replace(" ","_").replace(".pl","").replace("\n","")    # Save name of test to a variable
            rep_word        = append_trace(modified_line, trace_name)
            if "ipv6" in line:
                modified_lines_ipv6.append(rep_word)
                test_number_ipv6+=1
            else:
                modified_lines.append(rep_word)
                test_number_other+=1
            #print ("**************************************************************************")
            #print ("Rep word :")
            #print (rep_word)
            test_number+=1

    with open(location + output_file.replace(".bat", "ipv6.bat"), "w") as file:
        file.writelines(modified_lines_ipv6)
    with open(location + output_file, "w") as file:
        file.writelines(modified_lines)

    print ("Total test number: \t" + str(test_number))
    print ("IPV6 test number: \t" + str(test_number_ipv6))
    print ("Other test number: \t" + str(test_number_other))
