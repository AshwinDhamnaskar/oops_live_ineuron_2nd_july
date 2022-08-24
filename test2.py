class Person :

    def __init__(sudh, name, surname, emailid, year_of_birth):
        sudh.name1 = name
        sudh.surname = surname
        sudh.emailid = emailid
        sudh.year_of_birth = year_of_birth

    def age(sudh, current_year):
        return current_year - sudh.year_of_birth



anuj_var = Person("anuj", "bhandardi", "anuj@gmail.com", 1994)
sudh=Person("sudhanshu",'kumar',"sudhanshu@gmail.com",23424)
gargi=Person("gargi","xyz","gargi@gmail.com",234242)
print(sudh.age(2022))
print(anuj_var.age(2022))

print(sudh.name1+sudh.surname)
print(anuj_var.name1)
print(sudh.name1)
print(gargi.name1)
print(type(sudh))

s="sudhanshu"
s1="kumar"
print(s+s1)

s="sudh"
s.upper()
