class Student:
  def __init__(self, pre, mid, fin, name):
    self.__pre = pre
    self.__mid = mid
    self.__fin = fin
    self.__name = name

  def grade(self):
    average = (self.__pre+self.__mid+self.__fin)/3
    print("The Grade of ", self.__name ," is", average)

std1 = Student(90, 91, 98, 'Student 1')
std1.grade()

std2 = Student(72, 74, 82, 'Student 2')
std2.grade()

std3 = Student(70, 85, 94, 'Student 3')
std3.grade()
