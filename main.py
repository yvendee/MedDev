# main_script.py
import subprocess
import os
import time
import sys

def check_string(input_string):
    if "Clicked row" in input_string:
        return True
    else:
        return False

def main():

    mode = 0
    rtn_str = ""

    # mode = 1
    # rtn_str = "button_1 clicked"

    # Get the directory of main.py
    script_dir = os.path.dirname(os.path.abspath(__file__))

    while True:

        if(mode == 0):

            login_path = os.path.join(script_dir, "Log In", "build", "log.py")

            login_process = subprocess.Popen(["python", login_path], stdout=subprocess.PIPE, universal_newlines=True)

            rtn_str = ""
            for line in login_process.stdout:                            
                print("Stdout from log.py:", line.strip())
                if line.strip():  # If stdout is not empty
                    rtn_str = line.strip()
                    login_process.terminate()
                    mode = 1
                    break  # Exit loop

        if(mode == 1):
 
            if rtn_str == "button_2 clicked":

                signin_path = os.path.join(script_dir, "Sign In", "build", "sign.py")
                signin_process = subprocess.Popen(["python", signin_path], stdout=subprocess.PIPE, universal_newlines=True) ## 

                rtn_str = ""
                for line in signin_process.stdout:                            
                    print("Stdout from sign.py:", line.strip())
                    if line.strip():  # If stdout is not empty
                        rtn_str = line.strip()
                        mode = 0
                        signin_process.terminate()
                        break  # Exit loop

        if(mode == 1):

            if rtn_str == "button_1 clicked":

                mainFrame_path = os.path.join(script_dir, "Main Frame", "build", "mainFrame.py")
                mainFrame_process = subprocess.Popen(["python", mainFrame_path], stdout=subprocess.PIPE, universal_newlines=True) ## 

                rtn_str = ""
                for line in mainFrame_process.stdout:                            
                    print("Stdout from mainFrame.py:", line.strip())
                    if line.strip():  # If stdout is not empty
                        rtn_str = line.strip()
                        mode = 2
                        break  # Exit loop

        if(mode == 2):

            if rtn_str == "button_1 clicked":

                if mainFrame_process.poll() is None:
                    # If it's running, terminate it
                    mainFrame_process.terminate()
                    print("mainFrame_process terminated")
                else:
                    print("mainFrame_process is not running")

                ListofPatient_path = os.path.join(script_dir, "List of Patient", "build", "ListofPatient.py")
                ListofPatient_process = subprocess.Popen(["python", ListofPatient_path], stdout=subprocess.PIPE, universal_newlines=True) ## 

                rtn_str = ""
                for line in ListofPatient_process.stdout:                            
                    print("Stdout from ListofPatient.py:", line.strip())
                    if line.strip():  # If stdout is not empty
                        rtn_str = line.strip()
                        mode = 3
                        break  # Exit loop

        if(mode == 2):

            if rtn_str == "button_2 clicked":

                if mainFrame_process.poll() is None:
                    # If it's running, terminate it
                    mainFrame_process.terminate()
                    print("mainFrame_process terminated")
                else:
                    print("mainFrame_process is not running")
    

                editTherapistDetails_path = os.path.join(script_dir, "Edit Therapist Details", "build", "editTherapistDetails.py")
                editTherapistDetails_process = subprocess.Popen(["python", editTherapistDetails_path], stdout=subprocess.PIPE, universal_newlines=True) ## 

                rtn_str = ""
                for line in editTherapistDetails_process.stdout:                            
                    print("Stdout from editTherapistDetails.py:", line.strip())
                    if line.strip():  # If stdout is not empty
                        rtn_str = line.strip()
                        mode = 4
                        break  # Exit loop

        if(mode == 2):

            if rtn_str == "button_3 clicked":

                if mainFrame_process.poll() is None:
                    # If it's running, terminate it
                    mainFrame_process.terminate()
                    print("mainFrame_process terminated")
                else:
                    print("mainFrame_process is not running")


                mode  = 0
                rtn_str = ""


        if(mode == 3):

            if rtn_str == "button_2 clicked":
                ListofPatient_process.terminate()

                AddPatientDetails_path = os.path.join(script_dir, "Add Patient Details", "build", "AddPatientDetails.py")
                AddPatientDetails_process = subprocess.Popen(["python", AddPatientDetails_path], stdout=subprocess.PIPE, universal_newlines=True) ## 

                rtn_str = ""
                for line in AddPatientDetails_process.stdout:                            
                    print("Stdout from AddPatientDetails.py:", line.strip())
                    if line.strip():  # If stdout is not empty
                        rtn_str = line.strip()
                        mode = 5
                        break  # Exit loop

        if(mode == 3):

            ## cwhen user click "search"
            if rtn_str == "button_1 clicked":
                ListofPatient_process.terminate() 
                mode = 0
                rtn_str = ""

                # AddPatientDetails_path = os.path.join(script_dir, "Add Patient Details", "build", "AddPatientDetails.py")
                # AddPatientDetails_process = subprocess.Popen(["python", AddPatientDetails_path], stdout=subprocess.PIPE, universal_newlines=True) ## 

                # rtn_str = ""
                # for line in AddPatientDetails_process.stdout:                            
                #     print("Stdout from AddPatientDetails.py:", line.strip())
                #     if line.strip():  # If stdout is not empty
                #         rtn_str = line.strip()
                #         mode = 0
                #         break  # Exit loop

        if(mode == 3):

            ## cwhen user click "search"
            if rtn_str == "button_3 clicked":
                ListofPatient_process.terminate()
                rtn_str = "button_1 clicked"
                mode = 1


        if(mode == 3):

            if(check_string(rtn_str)):
                if ListofPatient_process.poll() is None:
                    # If it's running, terminate it
                    ListofPatient_process.terminate()
                    print("ListofPatient_process terminated")
                else:
                    print("ListofPatient_process is not running")


                PatientData_path = os.path.join(script_dir, "Patient Data", "build", "PatientData.py")
                PatientData_process = subprocess.Popen(["python", PatientData_path], stdout=subprocess.PIPE, universal_newlines=True) ## 
                
                rtn_str = ""
                for line in PatientData_process.stdout:                            
                    print("Stdout from PatientData.py:", line.strip())
                    if line.strip():  # If stdout is not empty
                        rtn_str = line.strip()
                        mode = 6
                        break  # Exit loop


        if(mode == 4):

            if rtn_str == "button_2 clicked":
                editTherapistDetails_process.terminate()
                mode = 1
                rtn_str = "button_1 clicked"

        if(mode == 4):

            if rtn_str == "button_1 clicked":
                editTherapistDetails_process.terminate()
                mode = 1


        if(mode == 5):
            if rtn_str == "button_2 clicked":
                if AddPatientDetails_process.poll() is None:
                    # If it's running, terminate it
                    AddPatientDetails_process.terminate()
                    print("AddPatientDetails_process terminated")
                else:
                    print("AddPatientDetails_process is not running")
                mode = 1
                rtn_str = "button_1 clicked"

        if(mode == 5):

            if rtn_str == "button_1 clicked":

                if AddPatientDetails_process.poll() is None:
                    # If it's running, terminate it
                    AddPatientDetails_process.terminate()
                    print("AddPatientDetails_process terminated")
                else:
                    print("AddPatientDetails_process is not running")


                ListofPatient_path = os.path.join(script_dir, "List of Patient", "build", "ListofPatient.py")
                ListofPatient_process = subprocess.Popen(["python", ListofPatient_path], stdout=subprocess.PIPE, universal_newlines=True) ## 

                rtn_str = ""
                for line in ListofPatient_process.stdout:                            
                    print("Stdout from ListofPatient.py:", line.strip())
                    if line.strip():  # If stdout is not empty
                        rtn_str = line.strip()
                        mode = 3
                        break  # Exit loop

        if(mode == 6):

            if rtn_str == "button_6 clicked":
                # print("archive")

                if PatientData_process.poll() is None:
                    # If it's running, terminate it
                    PatientData_process.terminate()
                    print("PatientData_process terminated")
                else:
                    print("PatientData_process is not running")


                ArchivedSession_path = os.path.join(script_dir, "Archived Session", "build", "ArchivedSession.py")
                ArchivedSession_process = subprocess.Popen(["python", ArchivedSession_path], stdout=subprocess.PIPE, universal_newlines=True) ## 

                rtn_str = ""
                for line in ArchivedSession_process.stdout:                            
                    print("Stdout from ArchivedSession.py:", line.strip())
                    if line.strip():  # If stdout is not empty
                        rtn_str = line.strip()
                        mode = 8
                        break  # Exit loop

        if(mode == 6):


            if rtn_str == "button_4 clicked":
                # print("left view")
                if PatientData_process.poll() is None:
                    # If it's running, terminate it
                    PatientData_process.terminate()
                    print("PatientData_process terminated")
                else:
                    print("PatientData_process is not running")


                ViewSession_path = os.path.join(script_dir, "View Session", "build", "gui.py")
                ViewSession_process = subprocess.Popen(["python", ViewSession_path], stdout=subprocess.PIPE, universal_newlines=True) ## 

                rtn_str = ""
                for line in ViewSession_process.stdout:                            
                    print("Stdout from ViewSession_process(gui).py:", line.strip())
                    if line.strip():  # If stdout is not empty
                        rtn_str = line.strip()
                        mode = 1
                        break  # Exit loop
        
        if(mode == 6):
            if rtn_str == "button_5 clicked":
                # print("right view")
                if PatientData_process.poll() is None:
                    # If it's running, terminate it
                    PatientData_process.terminate()
                    print("PatientData_process terminated")
                else:
                    print("PatientData_process is not running")


                ViewSession_path = os.path.join(script_dir, "View Session", "build", "gui.py")
                ViewSession_process = subprocess.Popen(["python", ViewSession_path], stdout=subprocess.PIPE, universal_newlines=True) ## 

                rtn_str = ""
                for line in ViewSession_process.stdout:                            
                    print("Stdout from ViewSession_process(gui).py:", line.strip())
                    if line.strip():  # If stdout is not empty
                        rtn_str = line.strip()
                        mode = 1
                        break  # Exit loop
        
        if(mode == 6):
            if rtn_str == "button_3 clicked":
                # print("backlist")
                mode = 2
                rtn_str = "button_1 clicked"
        if(mode == 6):
            if rtn_str == "button_2 clicked":
                # print("edit details")
                if PatientData_process.poll() is None:
                    # If it's running, terminate it
                    PatientData_process.terminate()
                    print("PatientData_process terminated")
                else:
                    print("PatientData_process is not running")


                EditPatient_path = os.path.join(script_dir, "Edit Patient Details", "build", "EditPatient.py")
                EditPatient_process = subprocess.Popen(["python", EditPatient_path], stdout=subprocess.PIPE, universal_newlines=True) ## 
                rtn_str = ""
                for line in EditPatient_process.stdout:                            
                    print("Stdout from EditPatient.py:", line.strip())
                    if line.strip():  # If stdout is not empty
                        rtn_str = line.strip()
                        if rtn_str == "button_1 clicked":
                            mode = 3
                            rtn_str = "Clicked row"
                        if rtn_str == "button_2 clicked":
                            mode = 1
                            rtn_str = "button_1 clicked"

                        break  # Exit loop



        if(mode == 6):
            if rtn_str == "button_1 clicked":
                # print("get data")
                if PatientData_process.poll() is None:
                    # If it's running, terminate it
                    PatientData_process.terminate()
                    print("PatientData_process terminated")
                else:
                    print("PatientData_process is not running")


                GetData_path = os.path.join(script_dir, "Get Data", "build", "GetData.py")
                GetData_process = subprocess.Popen(["python", GetData_path], stdout=subprocess.PIPE, universal_newlines=True) ## 
                rtn_str = ""
                for line in GetData_process.stdout:                            
                    print("Stdout from GetData.py:", line.strip())
                    if line.strip():  # If stdout is not empty
                        rtn_str = line.strip()

                        
                        if rtn_str == "button_8 clicked":
                            mode = 3
                            rtn_str = "Clicked row"
                        if rtn_str == "button_9 clicked":
                            # rtn_str = "button_1 clicked"
                            # mode = 0
                            mode = 7
                            
                        break  # Exit loop


        if(mode == 7):
            mode = 3
            rtn_str = "Clicked row"

        if(mode == 8):
            if(check_string(rtn_str)):
                if ArchivedSession_process.poll() is None:
                    # If it's running, terminate it
                    ArchivedSession_process.terminate()
                    print("ArchivedSession_process terminated")
                else:
                    print("ArchivedSession_process is not running")


                PatientData_path = os.path.join(script_dir, "Patient Data", "build", "PatientData.py")
                PatientData_process = subprocess.Popen(["python", PatientData_path], stdout=subprocess.PIPE, universal_newlines=True) ## 
                
                rtn_str = ""
                for line in PatientData_process.stdout:                            
                    print("Stdout from PatientData.py:", line.strip())
                    if line.strip():  # If stdout is not empty
                        rtn_str = line.strip()
                        mode = 6
                        break  # Exit loop



        if(mode == 9):
            sys.exit()







        


        


if __name__ == "__main__":
    main()
