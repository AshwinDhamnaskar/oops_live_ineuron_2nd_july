class Person :

    def __init__(sudh, name, surname, emailid, year_of_birth):
        sudh.name1 = name
        sudh.surname = surname
        sudh.emailid = emailid
        sudh.year_of_birth = year_of_birth

    def __init__(sudh, name, surname):
        sudh.name1 = name
        sudh.surname = surname


    def age(sudh, current_year):
        return current_year



anuj_var = Person("anuj", "bhandardi")
sudh=Person("sudhanshu",'kumar')
gargi=Person("gargi","xyz")
print(anuj_var.age(2022))


