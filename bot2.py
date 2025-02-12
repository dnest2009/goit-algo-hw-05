import re
from datetime import datetime

welcome = '''  
___       __   _______   ___       ________  ________  _____ ______   _______          
|\  \     |\  \|\  ___ \ |\  \     |\   ____\|\   __  \|\   _ \  _   \|\  ___ \         
\ \  \    \ \  \ \   __/|\ \  \    \ \  \___|\ \  \|\  \ \  \\\__\ \  \ \   __/|        
 \ \  \  __\ \  \ \  \_|/_\ \  \    \ \  \    \ \  \\\  \ \  \\|__| \  \ \  \_|/__      
  \ \  \|\__\_\  \ \  \_|\ \ \  \____\ \  \____\ \  \\\  \ \  \    \ \  \ \  \_|\ \     
   \ \____________\ \_______\ \_______\ \_______\ \_______\ \__\    \ \__\ \_______\    
    \|____________|\|_______|\|_______|\|_______|\|_______|\|__|     \|__|\|_______|    
                                                                                    '''
comands = """
Create new user enter: add username phone
Change phone number enter: change username phone
View phone number of user: phone username
View all contacts: all
To exit: close or exit
"""
# ДЕКОРАТОРИ ДЛЯ ОБРОБКИ ПОМИЛОК:
def input_error(func):
    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except ValueError:
            return "Enter the argument for the command"
    return inner

def input_error_index(func):
    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except IndexError:
            return "Enter the argument for the command"
    return inner

def input_error_key(func):
    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except KeyError:
            return "Enter the argument for the command"
    return inner

def parse_input(user_input):         #парсер команд
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    return cmd, *args

@input_error
def add_contact(args, contacts):   # функція додавання контакту
    name, phone = args
    if validation_phone_number(phone):
        contacts[name] = phone
        #contacts[] = datetime.strftime(datetime.now(),"%Y-%m-%d %H:%M")
        return "Contact added."
    else:
        return "Enter the argument for the command"
    
@input_error
def change_number(args,contacts): # функція зміни контакту 
    name, phone = args
    if validation_phone_number(phone):
        contacts[name] = phone
        return "Contact changed"
    else:
          return "Enter the argument for the command"
    
@input_error_key
@input_error
@input_error_index      
def view_number(args,contacts): # функція перегляду номеру телефону конкретного користувача
    name = args[0]              # і'мя йде першим у списку argv, потім телефон
    number = contacts[name]     # номер телефону виводимо за ключем "ім'я"
    return number

def view_all_contacts(contacts):     #виводимо контакти
    return contacts

def validation_phone_number(phone):  # перевірка номеру телефону на правильність вводу
    phone_pattern1 = r'^\+?(\d{1,3})?[-\s]?\(?\d{1,4}\)?[-\s]?\d{1,4}[-\s]?\d{1,4}[-\s]?\d{1,4}$'#Шаблон для міжнародного формату телефону (наприклад, +380123456789)
    phone_pattern2 = r'^(?:\+38|0)?(0\d{9})$'#телефонні номери у форматі +380123456789 або 0800123456
    phone_pattern3= r'^(0\d{9})$' #Для українських телефонів без коду країни в форматі 0501234567
    phone_pattern4 = r'^\d{3}[-\s]?\d{3}[-\s]?\d{4}$' #Простий шаблон для номера телефону в форматі 123-456-7890
    if re.match(phone_pattern1, phone) or re.match(phone_pattern2,phone) or re.match(phone_pattern3,phone) or re.match(phone_pattern4,phone):
        print("Номер телефону коректний")
        return True 
    else:
        print("Номер телефону некоректний")
        return False
    
# def save_contacts(contacts,name):     функція зберігання контактів у файл
#     with open ("contacts.txt","w") as file:
#             file.write(f"{contacts[name]}")

def main():     # основна функція циклу
    print(welcome)  #виведення привітання
    print(comands)   # виведення команд
    contacts = {}
    while True:
       # try:
            user_input = input("Enter a command: ")
            command, *args = parse_input(user_input)
            if command in ["close", "exit"]:
                print("Good bye!")
                break
            elif command == "hello":
                print("How can I help you?")
            elif command == "add":
                print(add_contact(args, contacts))
                #save_contacts(contacts)
            elif command == "change":
                print(change_number(args, contacts))
                #save_contacts(contacts)
            elif command == "phone":
                print(view_number(args,contacts))
            elif command == 'all':
                print(view_all_contacts(contacts))
            #else:
                #print("Invalid command.")
       # except:
          #  print("Invalid command.")

if __name__ == "__main__":
    main()