class Person :

    def __init__(self, name, surname, emailid, year_of_birth):
        self.name = name
        self.surname = surname
        self.emailid = emailid
        self.year_of_birth = year_of_birth


anuj_var = Person("anuj", "bhandardi", "anuj@gmail.com", 1994)
sudh=Person("sudhanshu",'kumar',"sudhanshu@gmail.com",23424)
gargi=Person("gargi","xyz","gargi@gmail.com",234242)
print(anuj_var.name)
print(sudh.name)
print(gargi.name)
print(type(sudh))





