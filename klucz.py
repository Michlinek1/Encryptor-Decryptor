from cryptography.fernet import Fernet
def klucz():
    key = Fernet.generate_key();
    with open("klucz.KLUCZ", "wb") as klucz:
        klucz.write(key)
        klucz.close()
        print("Klucz został wygenerowany")