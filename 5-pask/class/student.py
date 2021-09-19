from human import Human


class Student(Human):
    """initialiaze Student object"""
    def __init__(self, name, age, height, graduation_year):
        super().__init__(name, age, height)
        self.graduation_year = graduation_year


    # def __init__(self, graduation_year, avg_grade, extra_class, debil_yes_no):
    #     self.graduation_year = graduation_year
    #     self.avg_grade = avg_grade
    #     self.extra_class = extra_class
    #     self.debil = debil_yes_no


    def get_student_info(self):
        print(f"Name:\t\t{self.name}")
        print(f"age:\t\t{self.age}")
        print(f"height:\t\t{self.height}")
        print(f"Graduation_year:\t\t{self.graduation_year}")
