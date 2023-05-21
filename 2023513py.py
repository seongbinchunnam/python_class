import sys

class Contact:
    def __init__(self, name, phone, address):
        self.name = name
        self.phone = phone
        self.address = address


    def __str__(self):
        return f"{self.name}, ({self.phone}), {self.address}"

class AddressBook:
    def __init__(self):
        self.contacts = []

    def add_contact(self):
        name = input("이름을 입력하세요: ")
        phone = input("전화번호를 입력하세요: ")
        address= input("주소를 입력하세요: ")
        self.contacts.append(Contact(name, phone,address))

    def get_contact(self, name, address):
        for contact in self.contacts:
            if contact.name == name:
                return contact
            return None
        
    def list_contacts(self):
        return self.contacts   

    def save(self):
        with open("contacts.txt", "w") as f:
            for contact in self.contacts:
                f.write(str(contact) + "\m")

    def load(self):
        with open("contacts.txt", "r") as f:
            for line in f: 
                if(len(line) > 0):
                    contact = Contact(*line.split(","))
                self.contacts.append(contact)

address_book = AddressBook()

while True:
    print("1. 연락처 추가")
    print("2. 연락처 확인")
    print("3. 연락처 목록")
    print("4.load")
    print("5.save")
    print("0. 종료")

    choice = input("  선택하아래에서 고르세요: ")

    if choice == "1":
        address_book.add_contact()
        
    elif choice == "2":
        name = input("검색할 연락처 이름을 입력하세요: ")
        contact = address_book.get_contact(name)
        if contact:
            print(contact)
        else:
            print("입력하신 이름의 연락처가 없습니다.")
    elif choice == "3":
        for contact in address_book.contacts:
            print(contact)
    elif choice == "4":
        address_book.load()
    elif choice == "5":
        address_book.save()
    elif choice == "0":
        sys.exit()
    else:
        print("잘못된 입력입니다.")
