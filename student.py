class Student:
    def getname(self):
        while True:
            self.sname = input("Enter your student name: ").strip()
            self.name=self.sname.split()
            if len(self.name) == 0:
                print("Student name should not be empty! try-again.")
            else:
                res=True
                for self.names in self.name:
                    if (not self.names.isalpha()):
                        res=False
                        break
                if (not res):
                    print("{} is invalid name try-again".format(self.sname))
                else:
                    print("Student is valid Nmae {}".format(self.sname))
                    break
                
          


class Marks(Student):
    def getmarks(self):
        while True:
            try:
                self.sub1 = int(input('Enter marks for python: '))
                if self.sub1 not in range(0, 101):
                    print('Marks must be range 0 and 100. Try again.')
                else:
                    print('Python marks is: {}'.format(self.sub1))
                    break
            except ValueError:
                print("Don't enter strings, alnum and special symbols.")

        while True:
            try:
                self.sub2 = int(input('Enter marks for Django: '))
                if self.sub2 not in range(0, 101):
                    print('Marks must be between 0 and 100. Try again.')
                else:
                    print('Django marks: {}'.format(self.sub2))
                    break
            except ValueError:
                print("Don't enter strings, alnum and special symbols.")

        while True:
            try:
                self.sub3 = int(input('Enter marks for RestAPI: '))
                if self.sub3 not in range(0, 101):
                    print('Marks must be range 0 and 100. Try again.')
                else:
                    print('RestAPI marks: {}'.format(self.sub3))
                    break
            except ValueError:
                print("Don't enter strings, alnum,and special symbols.")


class Grade_avg(Marks):
    def getgrade_avg(self):
        self.total_marks = self.sub1 + self.sub2 + self.sub3
        self.percent = (self.total_marks / 300) * 100

        # Grade logic
        if self.sub1 < 40 or self.sub2 < 40 or self.sub3 < 40:
            self.grade = "Fail"
        else:
            if self.total_marks in range(250, 301):
                self.grade = 'DISTINCTION'
            elif self.total_marks in range(200, 250):
                self.grade = 'FIRST DIVISION'
            elif self.total_marks in range(150, 200):
                self.grade = 'SECOND DIVISION'
            elif self.total_marks in range(120, 150):
                self.grade = 'THIRD DIVISION'

        # Output
        print("*" * 40)
        print("Student Name: {}".format(self.sname))
        print('Student marks Python: {}'.format(self.sub1))
        print('Student marks Django: {}'.format(self.sub2))
        print('Student marks RestAPI: {}'.format(self.sub3))
        print('Total student marks: {}'.format(self.total_marks))
        print('Percentage: {}'.format(round(self.percent, 2)))
        print('Final grade: {}'.format(self.grade))
        print("*"*40)


# Create object and call methods 
obj = Grade_avg()
obj.getname()
obj.getmarks()
obj.getgrade_avg()


