# name1, fam1, surname1, phone1
# name2, fam2, surname2, phone2
# name3, fam3, surname3, phone3


def read_contacts(filename):
    contacts = []
    with open(filename, 'r') as file:
        for line in file:
            name, surname, patronymic, phone = line.strip().split(',')
            contact = {
                'name': name,
                'surname': surname,
                'patronymic': patronymic,
                'phone': phone
            }
            contacts.append(contact)
    return contacts

filename = r'D:\Люба\Обучение\Пайтон\2-ой блок\Пайтон\puthon2\data_1.txt'
contact = read_contacts(filename)
print(f'{contact}')

def change_contact():
    filename = 'D:\Люба\Обучение\Пайтон\2-ой блок\Пайтон\puthon2\data_2.txt'
    contact_data = []
    with open(filename, 'r') as phone_book:
        for line in phone_book:
            contact_data.append(line.strip())

    serhc_info = input('Какой контакт: ')

    for contact_ind in range(len(contact_data)):
        if contact_data[contact_ind] in contact:
            new_info = input('Введите изменения: ')
            contact_data[contact_ind] = new_info
            break
    
    with open(filename, 'w') as phone_book:
        for contact in contact_data[:-1]:
            phone_book.write(contact + '\n')
        phone_book.write(contact_data[:-1])