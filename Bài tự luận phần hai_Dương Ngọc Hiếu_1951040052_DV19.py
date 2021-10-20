import random

class STUDENT():
    def __init__(self,  id=None, score=None, credit=None):
        if score is not None:
            self._score = score
        else:
            self._score = round((random.uniform(0, 4)),1)
        
        if credit is not None:
            self._credit = credit
        else:
            self._credit = random.randint(0, 250)
        
        if id is not None:
            self._id = id
        else:
            self._id = "SV_{}".format(random.randint(0, 9999))
    
    def result(self):
        
        if self._score >= 3.8 and self._score <= 4.0:
            return "A+"
        elif self._score >= 3.3 and self._score <= 3.7:
            return "A"
        elif self._score >= 3 and self._score <= 3.2:
            return "B+"
        elif self._score >= 2.6 and self._score <= 2.9:
            return "B"
        elif self._score >= 1.8 and self._score <= 2.5:
            return "C"
        elif self._score < 1.8:
            return "D"
    
    def graduate(self): 
        if self.result != "D"  and self._credit <= 250 and self._score >= 1.8:
            return True
        else: return False

def sort(x: STUDENT):
    return x._score

def DS_SV():
    n = input(" Nhập n sinh viên muốn tạo danh sách: ")
    list_graduate = []
    list_student = []
    for i in range(int(n)):
        s = STUDENT()
        list_student.append(s)
        if s.graduate():
            list_graduate.append(s)
    count = 0
    list_student.sort( key=sort, reverse=True )
    for student in list_student:
        if student.graduate() == True:
            count = count + 1
        print(f'{student._id}: {student._score}, result: {student.result()}, credit: {student._credit}, graduate: {student.graduate()}')
    print(f'Tổng số sinh viên tốt nghiệp (graduated=True) : {count}')
    print(f'Mã số sinh viên có điểm cao nhất là {list_student[0]._id} với số điểm là {list_student[0]._score}')
    
DS_SV() 

import pytest



