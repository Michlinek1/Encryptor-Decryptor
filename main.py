import os
import subprocess
from tkinter import *
from tkinter import filedialog
from cryptography.fernet import Fernet
from rsa import decrypt
from klucz import klucz
window = Tk()
window.title("Encryptor")
window.geometry("500x500")
Label = Label(window, text="", font=("Arial Bold", 10))
        
def encrypt():
    try:
        fileDialog = filedialog.askopenfilename(initialdir="/", title="Wybierz plik", filetypes=(("Pliki tekstowe", "*.txt"), ("Wszystkie pliki", "*.*")))
        Label.config(text=fileDialog)
        with open("C:/Users/Michal/Desktop/zadaniainformatyaa/encryptor/klucz.KLUCZ", "rb") as klucz:
            key = klucz.read()
            klucz.close()
            with open(Label.cget("text"), "rb") as plik:
                data = plik.read()
                plik.close()
                f = Fernet(key)
                encrypted = f.encrypt(data)
                Split = os.path.split(fileDialog)[1]
                with open(Split, "wb") as encrypted_file:
                    encrypted_file.write(encrypted)
                    encrypted_file.close()
                    Label.config(text="Plik został zaszyfrowany")
                    subprocess.call("notepad.exe" + " " + Split, shell=True)
    except FileNotFoundError:
        print("Nie wybrano pliku")            
 
 
def decrypt():
   try:
        fileDialog = filedialog.askopenfilename(initialdir="/", title="Wybierz plik", filetypes=(("Pliki tekstowe", "*.txt"), ("Wszystkie pliki", "*.*")))
        Label.config(text=fileDialog)
        with open("C:/Users/Michal/Desktop/zadaniainformatyaa/encryptor/klucz.KLUCZ", "rb") as klucz:
           key = klucz.read()
           klucz.close()
        with open(Label.cget("text"), "rb") as plik:
            data = plik.read()
            f = Fernet(key)
            decrypted = f.decrypt(data)
            Split = os.path.split(fileDialog)[1]
            with open(Split, "wb") as decrypted_file:
                decrypted_file.write(decrypted)
                decrypted_file.close()
                Label.config(text="Plik został odszyfrowany")
                subprocess.call("notepad.exe" + " " + Split, shell=True)
           
   except Exception as e:
       print(e)      
           


ButtonEncrypt = Button(window, text= "Zaszyfruj", command=encrypt)
ButtonEncrypt.pack()

ButtonDecrypt = Button(window, text= "Rozszyfruj", command=decrypt)
ButtonDecrypt.pack()

Label.pack()
window.mainloop()
    

