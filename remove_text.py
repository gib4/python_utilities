location    = "C:\\Users\\dske\\Desktop\\Test_Michele_Melbourne\\Automate\\Run 2.1 - ipv4\\"
input_file  = "failed.bat"
output_file = "failed_run21_trace.bat"

word        = "AUS-Telstra"
rep_word    = ""

def append_trace(trace_name, script_name):
    start_ulogr = "perl StartTrace_Ulogr.pl " + trace_name +".trace\n"
    stop_ulogr  = "perl Kill_trace.pl"
    output = start_ulogr + script_name.strip() + "\n" + stop_ulogr + "\n"                 # perl StartTrace_Ulogr.pl tracename.trace
    return output

def my_replace():
    test_number = 0
    test_number_ipv6 = 0
    test_number_other = 0
    with open(location + input_file, "r") as file:
        lines = file.readlines()

    modified_lines      = []
    modified_lines_ipv6 = []

    for line in lines:
        if line.strip():                                                                                    # Delete empty lines
            modified_line   = line.split(word)[0] + "\n"                                                    # Delete everything after AUS-Telstra in a line
            name_and_params = modified_line.replace("perl ", "")                                            # Remove "perl " from line
            trace_name     = name_and_params.strip().replace(" ","_").replace(".pl","").replace("\n","")    # Save name of test to a variable
            rep_word        = append_trace(trace_name, modified_line)
            if "ipv6" in line:
                modified_lines_ipv6.append(rep_word)
                test_number_ipv6+=1
            else:
                modified_lines.append(rep_word)
                test_number_other+=1
            print ("**************************************************************************")
            print ("Rep word :")
            print (rep_word)
            test_number+=1

    with open(location + output_file.replace(".bat", "ipv6.bat"), "w") as file:
        file.writelines(modified_lines_ipv6)
    with open(location + output_file, "w") as file:
        file.writelines(modified_lines)

    print ("Total test number: \t" + str(test_number))
    print ("IPV6 test number: \t" + str(test_number_ipv6))
    print ("Other test number: \t" + str(test_number_other))

my_replace()

print("Text after "+ word + " deleted and saved to", output_file)