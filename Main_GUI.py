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

import PySimpleGUI as sg
from generate_password import generate_passwords
from excel_operations import CreateExcel
from CheckPasswordStrength import check_password_strength
import pyperclip
def main():
    label1 = sg.Text("Enter No.of Passwords:")
    input_box_no_of_passwords = sg.InputText(tooltip="# Password",
                                             key="NofPassword",
                                             font=('Calibri', 8),
                                             size=(10,1))
    gen_button = sg.Button("Generate",key="generate")
    listbox_pass = sg.Listbox(values = "",
                         key="listofpasswords",
                         enable_events=True,
                         size=[20,15])
    listbox_reads = sg.Listbox(values="",
                               key="listofreads",
                               size=[20,15])
    inputbox_acount = sg.InputText(tooltip="Save for Account",
                                   key="Account",
                                   font=('Calibri', 8))
    save_button = sg.Button("Save Record",key="save")
    copy_button = sg.Button("Copy",key="copy")
    label_account = sg.Text("Save it for Account:")
    label2 = sg.Text("Generate Password and Copy it to use",key="Strength")
    label3 = sg.Text("You can Enter an Account and Store it in Excel",key="Updates")
    label4 = sg.Text("",key="Message")
    sep = sg.HSeparator()
    inputbox_multi = sg.Multiline("", enable_events=True, key='multi',
                                  size=(10,15),
                                  expand_x=True,
                                  expand_y=True,
                                  justification='left')
    use_button = sg.Button("Use These",key="user_pass")
    window = sg.Window(title = "Memorable Password Generator",
                       layout = [[use_button, label1,input_box_no_of_passwords,gen_button],
                                 [inputbox_multi,listbox_reads,listbox_pass,copy_button],
                                 [label_account,inputbox_acount,save_button],
                                 [sep],
                                 [label2],
                                 [label3],
                                 [label4]],
                       font = ('calibri',10),
                       size=(700, 400))

    while True :
        event, value = window.read()
        if event == sg.WIN_CLOSED :
            window.close()
            exit()

        print(event)
        print(value)
    
        if event == "generate" :
            try:
                Passwords_to_generate = int(value['NofPassword'])
                passwords, readables = generate_passwords(Passwords_to_generate)
                window['listofpasswords'].update(values=passwords)
                window['listofreads'].update(values=readables)
            except ValueError:
                sg.popup("Enter Number of passwords to Generate", font=('calibri', 12))
        elif event == "copy" :
            try:
                to_copy = value['listofpasswords'][0]
                pyperclip.copy(to_copy)
                copied_text = pyperclip.paste()
                if copied_text == to_copy :
                    window['Updates'].update(value="Succesfully Copied to the Clipboard")
                PasswordStrength = check_password_strength(copied_text)
                Message = f"Your Selected Password is {PasswordStrength[0]}, it will take {PasswordStrength[1]} years to Crack"
                window['Strength'].update(value=Message)
                window['Message'].update(value="Consider Saving it in Records")
            except IndexError:
                sg.popup("Select a Password First",font=('calibri',12))

        elif event == "save":
            pass
if __name__ == '__main__':
    main()

