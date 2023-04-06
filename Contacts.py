class PhoneDictionary:
    def __init__(self):
        self.dictionary = {}
        self._contacts_count = 0

    def add_new_contact(self, name: str, surname: str, phone_number: str):
        if self.dictionary.get(f"{phone_number}") == None:
          self._contacts_count += 1
        self.dictionary.update({f"{phone_number}": f"{name} {surname}"})

    def get_all_contacts(self) -> dict:
        return self.dictionary

    def find_contact_by_number(self, phone_number: str) -> str:
        return f"{phone_number}: {self.dictionary[f'{phone_number}']}"

    def find_contact_by_name(self, full_name: str) -> str:
        results = []
        for key, value in self.dictionary.items():
          if value == " ".join(
              list(map(lambda word: word.capitalize(), "olha aloshina".split()))):
              results.append((key, value))
        print(*results if len(results) > 0 else "Nothing Found", sep="\n")

    def delete_contact(self, all=False) -> str:
        if not all:
            phone_number = input("Type number to delete: ")
            if self.dictionary.get(phone_number):
                self.dictionary.pop(phone_number)
                self._contacts_count -= 1
                print(f"Phone number {phone_number} deleted from Contacts.")
            else:
                print(f"Phone number {phone_number} was not find in Contacts.")
        elif input("Are you sure you want to delete all contacts? Y/N: ").lower() \
        == 'y':
            self.dictionary.clear()
            self._contacts_count = 0
            print("All contacts were deleted.")
        else:
            print("Contacts will not be deleted.")
