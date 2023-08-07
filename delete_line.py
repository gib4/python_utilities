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

# Usage example
file_path = 'C:\\Users\\dske\\Desktop\\Test_Michele_Melbourne\\all\\failed_corrected_copy.bat'  # Replace with the path to your file
string_to_delete = 'ipv64i'

delete_lines_with_string(file_path, string_to_delete)