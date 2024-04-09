# main_script.py
import subprocess
import os
import time

def main():
    # Get the directory of main.py
    script_dir = os.path.dirname(os.path.abspath(__file__))

    # Specify the full path to script1.py
    script1_path = os.path.join(script_dir, "Add Patient Details", "build", "AddPatientDetails.py")


    # Start AddPatientDetails.py and capture its stdout
    process1 = subprocess.Popen(["python", script1_path], stdout=subprocess.PIPE, universal_newlines=True) ## 

    # Capture and print the stdout of AddPatientDetails.py  ## command=lambda: [print("button_2 clicked"), window.destroy()],
    for line in process1.stdout:                            
        print("Stdout from AddPatientDetails.py:", line.strip())
        if line.strip():  # If stdout is not empty
            break  # Exit loop
    # Terminate the process after printing the first non-empty line of output
    process1.terminate()
        

    # Specify the full path to script1.py
    script2_path = os.path.join(script_dir, "Log In", "build", "log.py")

    # Start script2.py
    process2 = subprocess.Popen(["python", script2_path], stdout=subprocess.PIPE, universal_newlines=True)

    for line in process2.stdout:                            
        print("Stdout from log.py:", line.strip())
        if line.strip():  # If stdout is not empty
            break  # Exit loop
    # Terminate the process after printing the first non-empty line of output
    process2.terminate()
        


if __name__ == "__main__":
    main()
