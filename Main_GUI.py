# -*- coding: utf-8 -*-
"""
Created on Mon Oct 16 16:40:15 2023

@author: pandey
GUI - Application to Generate a Remorable Hindi Word Strong Password
Application Generates the list of strong passwords in a simple click.
IF user doesnt like any of those, or want to see another list it allows to re generate list with new passwords
User then has an option to select and Copy it and save it in Excel File for Records
It is recommended not to use a strong memorable password to open the Excel passwird

"""
import pickle
import PySimpleGUI as sg
from generate_password import generate_passwords
from excel_operations import CreateExcel_try
from excel_operations import read_from_file
from CheckPasswordStrength import check_password_strength
from generate_password import generate_userpass
from encrypt_pass import hash_password, verify_password
import pyperclip
from pathlib import Path


def Run_Ananypass():
    LabelSelfPass = sg.Text("You want Password generator\n"
                            "to consider custom words\n "
                            "provide it here each line")
    label1 = sg.Text("Enter No.of Passwords:")
    input_box_no_of_passwords = sg.InputText(tooltip="# Password",
                                             key="NofPassword",
                                             font=('Calibri', 8),
                                             size=(20, 1))
    gen_button = sg.Button("Generate", key="generate")
    temp = Path('mypickle.pk')
    if temp.exists():
        show_pass = sg.Button("Stored Passwords",key="showpass",disabled=False,size=(10,2))
    else :
        show_pass = sg.Button("Stored Passwords",key="showpass",disabled=True,size=(10,2))
    listbox_pass = sg.Listbox(values="",
                              key="listofpasswords",
                              enable_events=True,
                              size=[20, 13])
    listbox_reads = sg.Listbox(values="",
                               key="listofreads",
                               size=[20, 13])
    inputbox_acount = sg.InputText(tooltip="Save for Account",
                                   key="Account",
                                   font=('Calibri', 8),
                                   size=(15,1))
    save_button = sg.Button("Save Record", key="save")
    copy_button = sg.Button("Copy", key="copy")
    label_account = sg.Text("Save it for Account:")
    label2 = sg.Text("Generate Password and Copy it to use", key="Strength")
    label3 = sg.Text("You can Enter an Account and Store it in Excel", key="Updates")
    label4 = sg.Text("", key="Message")
    sep = sg.VSeparator()
    seph = sg.HSeparator()
    inputbox_multi = sg.Multiline("", enable_events=True, key='multi',
                                  size=(20,15),
                                  justification='left',
                                  background_color="lightblue")
    use_button = sg.Button("Use These", key="user_pass",
                           size=(10,1))
    inputbox_folder = sg.Input(tooltip="Chosen Folder to save the Passwords",
                               key="folder_to_save",
                               size=(33,1))
    button_folder = sg.FolderBrowse("Select Folder",key="Folder")
    Lbl = sg.Text("",key="Success")
    # filler1 = sg.Text("")
    # filler2 = sg.Text("")
    left_column_content = [[LabelSelfPass],
                           [use_button],
                           [inputbox_multi],]

    # Prepare the widgets for the right column
    right_column_content = [[label1,input_box_no_of_passwords,gen_button,show_pass],
                            [listbox_reads,listbox_pass,copy_button],
                            [label2],
                            [label3],
                            [seph],
                            [label4],
                            [inputbox_folder,button_folder],
                            [label_account,inputbox_acount,save_button],
                            [Lbl]]

    left_column = sg.Column(left_column_content)
    right_column = sg.Column(right_column_content)

    LAYOUT = [[left_column, sep, right_column]]

    window = sg.Window(title="Memorable Password Generator",
                       layout=LAYOUT,
                       font=('calibri', 10),
                       size=(670, 430))
    while True:
        event, value = window.read()
        if event == sg.WIN_CLOSED:
            window.close()
            exit()
        if 'location_to_save' not in locals():
            location_to_save = value['folder_to_save']
            
        print(event)
        print(value)

        if event == "generate":
            try:
                Passwords_to_generate = int(value['NofPassword'])
                if Passwords_to_generate >99 :
                    sg.popup("Enter a Smaller Number, You can Regenerate if you need.")
                    window['NofPassword'].update("")
                    continue
                passwords, readables = generate_passwords(Passwords_to_generate)
                window['listofpasswords'].update(values=passwords)
                window['listofreads'].update(values=readables)
                window['folder_to_save'].update(value="")
            except ValueError:
                sg.popup("Enter Correct Number of passwords to Generate", font=('calibri', 12))
        elif event == "copy":
            try:
                to_copy = value['listofpasswords'][0]
                pyperclip.copy(to_copy)
                copied_text = pyperclip.paste()
                if copied_text == to_copy:
                    window['Updates'].update(value="Succesfully Copied to the Clipboard",text_color="navy")
                PasswordStrength = check_password_strength(copied_text)
                Message = f"Your Selected Password is {PasswordStrength[0]}, it will take {PasswordStrength[1]} years to Crack"
                window['Strength'].update(value=Message)
                window['Message'].update(value="Consider Saving it in Records - You only need to select Folder Once")
                window['folder_to_save'].update(value="")
            except IndexError:
                sg.popup("Select a Password First", font=('calibri', 12))

        elif event == "user_pass":
            try:
                list_to_consider = value['multi'].split('\n')
                print(type(list_to_consider))
                print(list_to_consider)
                passwords,readables = generate_userpass(list_to_consider)
                window['listofpasswords'].update(values=passwords)
                window['listofreads'].update(values=readables)
            except IndexError:
                sg.popup("Provide Custom Words, or use Common words in the next section")

        elif event == "Folder":
            pass
        elif event == "save":
            try:
                password_to_save = value['listofpasswords'][0]
                Password_account = value['Account']
                data_to_save = [password_to_save,Password_account]
                location_to_save = value['folder_to_save']
                filename = 'mypickle.pk'
                if Password_account == "":
                    sg.popup("Please Enter Account for which you want to save the password")
                    continue
                if location_to_save == "":
                    with open(filename,'rb') as fi:
                        location_to_save = pickle.load(fi)
                        print(location_to_save)
                else : # Saving location
                    with open(filename,'wb') as fi:
                        pickle.dump(location_to_save, fi)
                        print(location_to_save)
                # Creating and Saving in Excel
                CreateExcel_try(data_to_save,location_to_save)
                window['folder_to_save'].update(value=location_to_save)
                message = f"Success! Your Password Information Stored in mentioned Location"
                window['Success'].update(value=message,text_color="Yellow")
                window['Account'].update(value="")
                window['showpass'].update(disabled=False)
                continue
            except FileNotFoundError:
                sg.popup("You Must Choose the Folder First Time")
            except IndexError:
                sg.popup("Select a password to save.")
        
        elif event == "showpass":
            try:
                if value['folder_to_save'] != '' :
                    xl_path = value['folder_to_save']
                elif 'location_to_save' in locals() :
                    xl_path = location_to_save
                 
                data = read_from_file(xl_path)

                if data == "Not_Found" :
                    sg.popup("Incorrect Location or File Not Found in Given Location")
                else :
                    passwords_to_display = data[0]
                    accounts_to_display = data[1]
                    window['listofpasswords'].update(values=accounts_to_display)
                    window['listofreads'].update(values=passwords_to_display)
            except UnboundLocalError:
                print("Location to save not set")

def main():
    while True :
        loginpass = Path('./user_password.pw')
        if loginpass.exists():
            input_password =  sg.popup_get_text('Password: ', password_char='*')
            with open(loginpass, 'rb') as file:
                stored_hash = file.read()
                print(stored_hash)
                print(type(stored_hash))
                if verify_password(input_password, stored_hash):
                    Run_Ananypass()
                    break
                else:
                    sg.popup_auto_close("Password Incorrect! Please Retry")
                    # print("Password is incorrect.")
        else :
            create_pass_label = sg.Text("Thanks for using Ananypass, Create your password!")
            label1 = sg.Text("Enter a password")
            label2 = sg.Text("Enter same password")
            passwordinput = sg.InputText(key="pass",
                                        size=(20,1),
                                        password_char="*")
            passwordcheck = sg.InputText(key="check",
                                        size=(20,1),
                                        password_char="*")
            sub_button = sg.Button("Submit",key="Submit")
            msg_label = sg.Text("",key="msglabel")
            LAYOUT = [[create_pass_label],
                    [label1,passwordinput],
                    [label2,passwordcheck],
                    [sub_button,msg_label]]
            window = sg.Window(title="Create Password",
                        layout=LAYOUT,
                        font=('calibri', 10))
            while True:
                event, value = window.read()
                if event == sg.WIN_CLOSED:
                    window.close()
                    exit()
                if event == "Submit" :
                    if value['pass'] == value['check'] :
                        password_to_store = value['pass']                    
                        hash_password(password_to_store)
                        sg.popup_timed('Thanks! now Login with password')
                        window.close()
                        break
                    else :
                        window['msglabel'].update(value="Password Does not Match! Retry")
                        window['check'].update(value="")                    
                        window['pass'].update(value="")
                print(event)
                print(value)
                # sg.popup_ok("Incorrect Password")


if __name__ == '__main__':
    main()