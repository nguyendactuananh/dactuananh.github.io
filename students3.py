class Students:
    def __init__(self):
        self.id = input("nhap id cua hoc sinh: ")
        self.name = input("nhap ten cua hoc sinh: ")
        self.grades = {}
        self.gpa = 0  
    
    def print_infor(self):
        print (f"student's id: {self.id} ")
        print (f"student's name: {self.name}")
        for subjects in (self.grades):
            print(f"{subjects}: {self.grades[subjects]}")
        print(f"student's GPA: {self.gpa}")
    
    def calculate_GPA (self):
        total_of_subject = 0
        for subjects in self.grades: 
            total_of_subject += self.grades[subjects]
        self.gpa = total_of_subject/len(self.grades)
    
    def add_new_subject(self):
        amount_of_new_subject = int(input("nhap so mon muon nhap: "))
        for i in range (amount_of_new_subject):
            new_subject = input(f"nhap ten mon ban muon nhap: ")
            self.grades[new_subject] = float(input(f"nhap diem vao mon {new_subject}: "))
    def dieu_kien_tot_nghiep (self):
        if int(self.gpa)/10*4 >=2.5:
            print("du dieu kien tot nghiep")
        else:
            print("khong du dieu kien tot nghiep")
student1 = Students()
student1.add_new_subject()
student1.calculate_GPA()
student1.print_infor()
student1. dieu_kien_tot_nghiep()
        