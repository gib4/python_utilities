import os

# Set the directory where your text files are located
directory = "C:/Users/dske/Desktop/Test_Michele_Melbourne/Automate/Run 1/CRASHED/"

# Define the target string to search for
nb1     = "Parameter 'NB1' IS NOT supported"
sig_int = "SIG_INT received."
com     = "[PERL WARNING] -> can't get COMMPROP"

def delete_file(file_path):
    try:
        os.unlink(file_path)
        print(f"Deleted: {file_path}")
    except PermissionError as e:
        print(f"Skipped (File in use): {file_path}")
    except OSError as e:
        print(f"Error deleting {file_path}: {e}")

for root, dirs, files in os.walk(directory):
    for filename in files:
        file_path = os.path.join(root, filename)
        with open(file_path, "r", encoding="latin-1") as file:
            content = file.read()
            file.close()
            if nb1 in content or sig_int in content or com in content:
                delete_file(file_path)
            else:
                print(f"NotDele: {file_path}")