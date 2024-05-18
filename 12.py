class Abiturient:
    """
    Клас для опису інформації про абітурієнта.

    Атрибути:
      id: Унікальний ідентифікатор абітурієнта.
      прізвище: Прізвище абітурієнта.
      ім'я: Ім'я абітурієнта.
      по_батькові: По-батькові абітурієнта.
      адреса: Адреса проживання абітурієнта.
      телефон: Номер телефону абітурієнта.
      оцінки: Список оцінок абітурієнта.
    """
    def __init__(self, id, прізвище, ім_я, по_батькові, адреса, телефон, оцінки):
        self.id = id
        self.прізвище = прізвище
        self.ім_я = ім_я
        self.по_батькові = по_батькові
        self.адреса = адреса
        self.телефон = телефон
        self.оцінки = оцінки

    def __str__(self):
        return f"{self.прізвище} {self.ім_я} {self.по_батькові}"

    def get_sum_of_scores(self):
        return sum(self.оцінки)


class EducationalProgram:
    """
    Клас для опису освітньої програми.

    Атрибути:
      name: Назва освітньої програми.
      limit: Ліміт кількості абітурієнтів, які можуть бути зараховані.
    """
    def __init__(self, name, limit):
        self.name = name
        self.limit = limit
        self.applications = []

    def add_application(self, application):
        if len(self.applications) < self.limit:
            self.applications.append(application)
            return True
        else:
            return False

    def process_applications(self):
        self.applications.sort(key=lambda app: app.abiturient.get_sum_of_scores(), reverse=True)
        return self.applications[:self.limit]


class AdmissionApplication:
    """
    Клас для опису заявки на вступ.

    Атрибути:
      абітурієнт: Абітурієнт, який подав заявку.
      програма: Освітня програма, на яку подається заявка.
    """
    def __init__(self, абітурієнт, програма):
        self.abiturіent = абітурієнт
        self.program = програма

    def __str__(self):
        return f"{self.abiturіent} - {self.program.name}"


class University:
    """
    Клас для опису університету.

    Атрибути:
      name: Назва університету.
      programs: Список освітніх програм університету.
    """
    def __init__(self, name):
        self.name = name
        self.programs = []

    def add_program(self, program):
        self.programs.append(program)

    def process_admissions(self):
        admission_orders = {}
        for program in self.programs:
            admission_orders[program.name] = program.process_applications()
        return admission_orders


# Приклад використання

if name == "__main__":
    # Створити університет
    university = University("Національний Університет")

    # Додати освітні програми
    program1 = EducationalProgram("Комп'ютерні науки", 3)
    program2 = EducationalProgram("Інженерія", 2)
    university.add_program(program1)
    university.add_program(program2)

    # Створити абітурієнтів
    abiturient1 = Abiturient(1, "Сидоренко", "Сидір", "Петрович", "вул. Героїв Дніпра, 25", "+380997654321", [3, 3, 4, 5, 4])
    abiturient2 = Abiturient(2, "Киселева", "Марія", "Олександрівна", "вул. Франка, 10", "+380957654321", [4, 5, 4, 5, 4])
    abiturient3 = Abiturient(3, "Мартинова", "Ольга", "Сергіївна", "вул. Леніна, 30", "+380931234567", [5, 5, 5, 5, 5])
    abiturient4 = Abiturient(4, "Волошенюк", "Ігор", "Миколайович", "вул. Козацька, 20", "+380991234567", [4, 4, 4, 4, 4])

    # Подати заявки на освітні програми
    application1 = AdmissionApplication(abiturient1, program1)
    application2 = AdmissionApplication(abiturient2, program1)
    application3 = AdmissionApplication(abiturient3, program1)
    application4 = AdmissionApplication(abiturient4, program2)

    # Додати заявки в освітні програми
    program1.add_application(application1)
    program1.add_application(application2)
    program1.add_application(application3)
    program2.add_application(application4)

    # Обробити заявки та сформувати накази на зарахування
    admission_orders = university.process_admissions() 
    # Вивести накази на зарахування
    print("Накази на зарахування:")
    for program_name, applications in admission_orders.items():
        print(f"\nОсвітня програма: {program_name}")
        for application in applications:
            print(application)