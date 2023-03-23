# Latest Code
import tkinter
from tkinter import filedialog
import numpy as np
from tkinter import *


def encrypt_word(word):
    key = np.array([[3, 15], [4, 5]])  # key matrix
    l1 = []

    for x in word:  # storing ascii values of word in list
        x = x.lower()
        if x == "z":
            val = 0
        else:
            val = ord(x) - ord("`")

        l1.append(val)

    l3 = []

    if (len(l1) % 2) != 0:  # adding last letter if odd number of letters
        a = l1[-1]
        l1.append(a)

    while (len(l1) != 0):  # encrypt pairs in list
        col_mat = np.array([[l1[0]], [l1[1]]])
        col_mat = np.dot(key, col_mat)
        col_mat = np.mod(col_mat, 26)
        l3.append(col_mat[0][0])  # add encrypted values to list
        l3.append(col_mat[1][0])

        l1.pop(0)
        l1.pop(0)

    l4 = []

    for x in l3:  # convert values into letters
        y = chr(x + 96)
        l4.append(y)

    word = ("".join(l4))  # merge list to form word
    return word  # return encrypted word

##########################################

def decrypt_word(word):
    list1 = []
    key_inverse = [[23, 9], [18, 19]]

    for x in word:  # storing ascii values of word in list
        x = x.lower()
        if x == "z":
            val = 0
        else:
            val = ord(x) - ord("`")

        list1.append(val)

    list2 = []

    if (len(list1) % 2) != 0:  # adding last letter if odd number of letters
        a = list1[-1]
        list1.append(a)

    while (len(list1) != 0):  # decrypt pairs in list
        col_mat = np.array([[list1[0]], [list1[1]]])
        col_mat = np.dot(key_inverse, col_mat)
        col_mat = np.mod(col_mat, 26)
        list2.append(col_mat[0][0])  # add decrypted values to list
        list2.append(col_mat[1][0])

        list1.pop(0)
        list1.pop(0)

    list3 = []

    for x in list2:  # convert values into letters
        y = chr(x + 96)
        list3.append(y)
    word = ("".join(list3))  # merge list to form word
    return word  # return decrypted word

##########################################

def encrypt_string(string):
    list1=string.split(" ")

    for i in range(len(list1)):
        if ('.' or ','or '!') in list1[i]:
            char=list1[i][-1]
            x = list1[i][:-1]
            x = encrypt_word(x)
            list1[i] = x +char
        else:
            list1[i] = encrypt_word(list1[i])

    string=" ".join(list1)
    return(string)

##########################################

def decrypt_string(string):
    list1 = string.split(" ")

    for i in range(len(list1)):
        if ('.' or ',' or '!') in list1[i]:
            char = list1[i][-1]
            x = list1[i][:-1]
            x = decrypt_word(x)
            list1[i] = x + char
        else:
            list1[i] = decrypt_word(list1[i])

    for i in range(len(list1)):
        x=list1[i][-2:]
        if x[0]==x[-1]:
            list1[i] = list1[i][:-1]


    string = " ".join(list1)
    return (string)

##########################################

def raise_frame(frame, f_prev):
    frame.pack(fill='both', expand=True)
    f_prev.forget()

##########################################

def encrypt_file():
    file_name = filedialog.askopenfilename()
    file = open(file_name, "r")
    list1 = []
    list2 = []

    for u in file:
        list1.append(u)

    for u in list1:
        u = u.split(' ')
        list2.append(u)

    for i in range(len(list2)):
        if '\n' in list2[i][-1]:
            list2[i][-1] = list2[i][-1][:-1]

    for i in range(len(list2)):
        for ind in range(len(list2[i])):
            if ('.' or ',' or '!') in list2[i][ind]:
                char = list2[i][ind][-1]
                x = list2[i][ind][:-1]
                x = encrypt_word(x)
                list2[i][ind] = x + char
            else:
                list2[i][ind] = encrypt_word(list2[i][ind])

    for i in range(len(list2)):
        list2[i][-1] = list2[i][-1] + "\n"

    for i in range(len(list2)):
        list2[i] = " ".join(list2[i])

    if '.' in file_name:
        index = file_name.index('.')
        file_name = file_name[:index]

    with open(file_name + "_encrypted.txt", "w") as f:
        for z in range(len(list2)):
            f.write(list2[z])

##########################################

def decrypt_file():
    file_name = filedialog.askopenfilename()
    file = open(file_name, "r")
    list1 = []
    list2 = []

    for u in file:
        list1.append(u)

    for u in list1:
        u = u.split(' ')
        list2.append(u)

    for i in range(len(list2)):
        if '\n' in list2[i][-1]:
            list2[i][-1] = list2[i][-1][:-1]

    for i in range(len(list2)):
        for ind in range(len(list2[i])):
            if ('.' or ',' or '!') in list2[i][ind]:
                char = list2[i][ind][-1]
                x = list2[i][ind][:-1]
                x = decrypt_word(x)
                list2[i][ind] = x + char
            else:
                list2[i][ind] = decrypt_word(list2[i][ind])

    for i in range(len(list2)):
        for ind in range(len(list2[i])):
            x = list2[i][ind][-2:]
            if len(x)>1:
                if x[0] == x[-1]:
                    list2[i][ind] = list2[i][ind][:-1]

    for i in range(len(list2)):
        list2[i][-1] = list2[i][-1] + "\n"

    for i in range(len(list2)):
        list2[i] = " ".join(list2[i])

    if '.' in file_name:
        index = file_name.index('.')
        file_name = file_name[:index]

    with open(file_name + "_decrypted.txt", "w") as f:
        for z in range(len(list2)):
            f.write(list2[z])

##########################################

def main_frame():
    f = Frame(root, bg="misty rose", height=750, width=900)

    f.pack(fill="both", expand=True)
    string_op = Button(f, text="Enter a String", height=2, width=25, bd=5, bg="white",
                       font=('Lucida Bright', 20, 'bold'), command=lambda: raise_frame(string_frame(), f))

    file_op = Button(f, text="Select a file", height=2, width=25, bd=5, bg="white",
                     font=('Lucida Bright', 20, 'bold'), command=lambda: raise_frame(file_frame(), f))

    title1 = Label(f, text="CRYPTOGRAPHY", font=('Snap ITC', 40), bg="aquamarine1")
    title1.place(relx=100, rely=100, anchor="center")

    string_op.grid(row=3, column=2, padx=200, pady=55)
    file_op.grid(row=4, column=2, padx=200, pady=50)
    title1.grid(row=0, column=2, padx=200, pady=30)
    return f

##########################################

def string_frame():
    frame_string_op = Frame(root, height=1000, width=1000, bg="AntiqueWhite1")

    text_ = StringVar()
    textBox = Entry(frame_string_op, textvariable=text_, bg="white", bd=5, font=('Lucida Bright', 30, 'bold'))

    EncryptButton = Button(frame_string_op, text="ENCRYPT", width=18, height=2, bd=5, bg="green3",
                           font=('Lucida Bright', 18, 'bold'),
                           command=lambda: encrypt_label())
    DecryptButton = Button(frame_string_op, text="DECRYPT", width=18, height=2, bd=5, bg="green3",
                           font=('Century Schoolbook', 18, 'bold'),
                           command=lambda: decrypt_label())
    ExitButton = Button(frame_string_op, text="EXIT", bg="red", height=2, width=10, bd=5,
                        font=('Century Schoolbook', 18, 'bold'),
                        command=lambda: raise_frame(main_frame(), frame_string_op))

    msg1 = Label(frame_string_op, text="Enter a string :", font=('Lucida Bright', 25, 'bold'), bg="AntiqueWhite1")

    msg1.grid(row=0, column=0, padx=5, pady=10)
    EncryptButton.grid(row=2, column=0, padx=30, pady=30)
    DecryptButton.grid(row=2, column=1, padx=10, pady=30)
    ExitButton.grid(row=6, column=1, padx=100, pady=50)
    textBox.grid(row=0, column=1, padx=20, pady=50)

    def encrypt_label():
        inputText = text_.get()
        text_encrypt = encrypt_string(inputText)
        text = Text(frame_string_op, height=1, width=18, bg="white", bd=5, font=("Lucida Bright", 30, 'bold'),
                    wrap=WORD)
        msg2 = Label(frame_string_op, text="Encrypted String :", font=('Lucida Bright', 25, 'bold'), bg="AntiqueWhite1")

        text.insert(INSERT, text_encrypt)
        text.grid(row=1, column=1, padx=20, pady=30, ipadx=10, ipady=2)
        msg2.grid(row=1, column=0, padx=5, pady=10)

    def decrypt_label():
        inputText = text_.get()
        text_decrypt = decrypt_string(inputText)
        text = Text(frame_string_op, height=1, width=18, bg="white", bd=5, font=("Lucida Bright", 30, 'bold'),
                    wrap=WORD)
        msg2 = Label(frame_string_op, text="Decrypted String :", font=("Lucida Bright", 25, 'bold'), bg="AntiqueWhite1")
        text.insert(INSERT, text_decrypt)
        text.grid(row=1, column=1, padx=20, pady=30, ipadx=10, ipady=2)
        msg2.grid(row=1, column=0, padx=5, pady=10)

    return frame_string_op

##########################################

def file_frame():
    frame_file_op = Frame(root, bg="peach puff", height=500, width=500)
    button_encrypt = Button(frame_file_op, text="ENCRYPT", bg="white", height=2, width=20, bd=5,
                            font=('Lucida Bright', 20, 'bold'),
                            command=lambda: encrypt_file())  # command = lambda:encrypt_file())
    button_decrypt = Button(frame_file_op, text="DECRYPT", bg="white", height=2, width=25, bd=5,
                            font=('Lucida Bright', 20, 'bold'),
                            command=lambda: decrypt_file())  # command = lambda:decrypt_file())
    butt_exit = Button(frame_file_op, text="EXIT", bg="lightcoral", height=2, width=15, bd=5,
                       font=('Lucida Bright', 20, 'bold'),
                       command=lambda: raise_frame(main_frame(), frame_file_op))
    title2 = Label(frame_file_op, text="Select a file to :", font=('Lucida Bright  ', 30, 'bold'), bg="peach puff")
    title2.place(relx=100, rely=100, anchor="center")

    button_encrypt.grid(row=3, column=2, padx=200, pady=40)
    button_decrypt.grid(row=4, column=2, padx=200, pady=40)
    butt_exit.grid(row=5, column=2, padx=200, pady=40)
    title2.grid(row=0, column=2, padx=300, pady=30)
    return frame_file_op

##########################################


root = tkinter.Tk()
root.title("Cryptography")
root.geometry("900x700")
root.resizable(False, False)
main_frame()
root.mainloop()






