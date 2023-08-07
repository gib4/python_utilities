import libs.file_operations as fo

folder  = "C:/Users/dske/Desktop/Test_Michele_Melbourne/Automate"
nb1     = "Parameter 'NB1' IS NOT supported"
sig_int = "SIG_INT received."
com     = "[PERL WARNING] -> can't get COMMPROP"

fo.delete_files_matching(nb1,sig_int,com)