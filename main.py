import os.path

def welcome():
    print("""Welcome to the Caesar Cipher
This program encrypts and decrypts text with the Caesar Cipher.
Developed By Darwin Paudel""")


def enter_message():
    """This Function take Shift value and Mode from user"""
    while True:
        # shift value selection
        global shift
        shift = input("Enter Shift Value (1-25): ")
        if shift.isnumeric() and 0 < int(shift) < 26:
            print("Shift Value", shift, "Confirmed!!")
            break
        else:
            print("Invalid Shift Value")
    while True:
        while True:
            # mode selection
            global mode
            mode = input("Select Mode 'E' for Encrypt and 'D' for Decrypt: ")
            if str.upper(mode) == "E":
                break
            elif str.upper(mode) == "D":
                break
            else:
                print("Invalid Mode!")
                continue
            break
        break


def write_message(data):
    """this function store output to results.txt"""
    with open('results.txt', 'a') as file:
        file.write(data)


def message_or_file():
    """This function gives choice for read mode"""
    global process
    process = input("Would you like to read from a file (f) or the console (c)? ")
    while True:
        if process.upper() == "F" or process.upper() == "C":
            break
        else:
            print("Invalid Read Mode")
            process = input("Would you like to read from a file (f) or the console (c)? ")


def process_file(mod_re, shift):
    """This Fucntion data encrypt of decrypt through file"""
    while True:
        filename = input("Enter a filename: ")
        try:
            with open(filename) as file:
                x = file.readlines()
                for line in x:
                    tem_data =""
                    rem = line.strip().upper()
                    if mod_re.upper() == "E":
                        f = encrypt(rem, int(shift))
                    else:
                        f = decrypt(rem, int(shift))
                    tem_data = tem_data +f
                choice = input("Do you want to store Output? Y/n")
                if choice.upper() == "Y":
                    write_message(tem_data)
            break
        except FileNotFoundError:
            print("Invalid Filename")


def is_file(filename):
    if os.path.exists(filename):
        return 1
    else:
        return 0


def run():
    """This function Run the process"""
    if str.upper(process) == "F":
        process_file(mode, shift)

    elif str.upper(process) == "C":
        print("Process Using Console")
        while True:
            message_text_temp = input("Enter a message to Encrypt or Decrypt: ")
            message_text = message_text_temp.upper()
            if mode.upper() == "E":
                result = encrypt(message_text, int(shift))
            elif mode.upper() == "D":
                result = decrypt(message_text, int(shift))
            else:
                print("Invalid Input!")
                continue
            print("The final Message is", result)
            break


# encrypt function start
def encrypt(prompt, s):
    """This is the fuction to Encrypt"""
    ans = ''
    for i in range(len(prompt)):
        if prompt[i].isalpha():
            value = prompt[i]
            ascii = ord(value)
            ascii +=s
            if ascii >90:
                ascii -= 26
            ans = ans + chr(ascii)
        else:
            ans +=" "
    return ans
# encrypt function end


# decrypt function start
def decrypt(prompt, s):
    """This is the function to decrypt"""
    ans = ''
    for i in range(len(prompt)):
        if prompt[i].isalpha():
            value = prompt[i]
            ascii = ord(value)
            ascii -= s
            if ascii < 65:
                ascii += 26
            ans = ans + chr(ascii)
        else:
            ans += " "
    return ans
# decrypt function end

def redo():
    """This function Help to repeat the program"""
    while True:
        action = input("Would you like to encrypt or decrypt another message? (y/n): ")
        if action.upper() == "Y":
            main()
            continue
        elif action.upper() == "N":
            print("Thanks for using the program, goodbye!")
            break
        else:
            print("Invalid Input Choose (y/n) !")

def main():
    """This is main function"""
    welcome()
    enter_message()
    message_or_file()
    run()
    redo()


main()
