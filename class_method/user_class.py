# in a class you must to use __init__ function as a first function of the class
# self.names are variables of an inheritance
class Biodata:
    def __init__(self, name, birth_date, age, hobbies, phone_number):
        self.names = name
        self.births = birth_date
        self.ages = age
        self.hobbies = hobbies
        self.phones = phone_number
    
    def bio_info(self):
        print(f"- Name : {self.names}\n- Birth Date : {self.births}\n- Age : {self.ages}\n- Hobbies : {self.hobbies}\n- Phone : {self.phones}")
