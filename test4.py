class Person:

    def age(self,cuurent_year,year_of_birth):
        return current_year - year_of_birth

    def email_id_input(self,email_id):
        print("take and mail id from a person and print it",email_id)

    def ask_name(self):
        name=input("tell me your name")
        return name

    def ask_dob(self):
        dob=input("tell me your date of birth")
        return dob

sudh=Person()
anuj=Person()
gargi=Person()
krish=Person()
hitesh=Person()

sudh.email_id_input("sudhanshu@ineuron.ai")
print(sudh.ask_name())

print(hitesh.ask_dob())

