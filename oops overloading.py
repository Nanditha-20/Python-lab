class Student:
    def _init_(self, name, marks):
        self.name = name
        self.marks = marks
    def display(self):
        print(self.name,self.marks)
    def _add_(self, S):
        Temp = Student(S.name, [])
        for i in range (len(self.marks)):
            Temp.marks.append(self.marks[i] + S.marks[i])
        return Temp
S1 = Student("amar",[99,98,97])
S2 = Student("amar",[96,95,94])
S1.display()
S2.display()
S3 = Student(" ", [])
S3 = S1 + S2
S3.display()
