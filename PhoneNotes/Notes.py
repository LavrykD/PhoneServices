import time

class Notes:
    def __init__(self):
        self.notes = {}
        self._notes_count = 0

    def format_date(self, day, month, year):
        return time.strftime("%d-%b-%Y", 
                             time.strptime(f"{day}-{month}-{year}", 
                                           "%d-%m-%Y"))
    
    def add_new_note(self, note_header: str, *note_text):
        current_time = time.strftime("%d-%b-%Y", time.localtime())
        if self.notes.get(current_time):
            self.notes[current_time].update({note_header: note_text})
        else:
            self.notes[current_time] = {note_header: note_text}
        self._notes_count += 1

    def check_all_notes(self):
        for key, value in self.notes.items():
            print(key, end=":\n\n")
            for inkey, invalue in value.items():
                print(inkey, end="\n")
                print(*invalue, sep=" || ", end="\n")
                print("- " * int(len("".join(invalue))//1.5), end="\n\n")

    def check_notes_for_day(self, day, month, year):
        date_to_search = self.format_date(day, month, year)
        if self.notes.get(date_to_search):
            index = 1
            print()
            print(f"Notes for {date_to_search}:")
            for key, value in self.notes[date_to_search].items():
                print(f"{index}. {key:<11}: {value}", end="\n")
                index += 1
        else:
            print("There are no notes for this date.")

    def delete_note(self, all=False):
        if all:
            if input("Are you sure you want to delete all notes? \
                     y/n: ").lower() \
                == "y":
                self.notes.clear()
                self._notes_count = 0
            else:
                "Deletion is canceled."
        else:
            date_of_note = input("Please provide the date for \
                                 which you want to delete the \
                                 note in format dd-mm-yyyy: ")
            formated_date = self.format_date(*date_of_note.split('-'))
            self.check_notes_for_day(*date_of_note.split('-'))
            note_to_delete = int(input("Choose note to delete \
                                       (type it's list number): "))
            index = 1
            for key, value in self.notes[formated_date].items():
                if index == note_to_delete:
                    self.notes[formated_date].pop(key)
                    break
                index += 1
