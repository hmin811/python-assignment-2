#code
import random
class GradeSystem:
    def __init__(self):
        self.subjectnames = {}
        self.courses = []
        self.opencredit = 0
        self.submitcredit = 0
        self.total = 0

    def calc(self, grade, credit):
        self.opencredit += credit
        if grade != 'F':
            self.submitcredit += credit
        match grade:
            case 'A+':
                self.total += 4.5*credit
            case 'A':
                self.total += 4*credit
            case 'B+':
                self.total += 3.5*credit
            case 'B':
                self.total += 3*credit
            case 'C+':
                self.total += 2.5*credit
            case 'C':
                self.total += 2*credit
            case 'D+':
                self.total += 1.5*credit
            case 'D':
                self.total += 1*credit

    def RandomNumber(self, grade, credit):
        self.k = random.randint(10000, 99999)
        self.subjectnames[str(self.k)] = subject
        self.courses.append((str(self.k), credit, grade))

    def output(self):
        for i in range(0, len(self.courses)):
            print('[%s] %d학점: %s'%(self.subjectnames[self.courses[i][0]], self.courses[i][1], self.courses[i][2]))

    def call(self, callsubject):
        self.list = list(self.subjectnames.items())
        for i in range (0, len(self.list)):
            if self.list[i][1] == callsubject:
                key = self.list[i][0]
                for j in range (0, len(self.courses)):
                    if self.courses[j][0] == key:
                        print('[%s] %d학점: %s'%(self.subjectnames[self.courses[j][0]], self.courses[j][1], self.courses[j][2]))
    
    def final(self):
        #final
        self.submittotal = self.total/self.submitcredit
        self.opentotal = self.total/self.opencredit
        print('제출용: %d학점 (GPA:%.2lf)' %(self.submitcredit, self.submittotal))
        print('열람용: %d학점 (GPA:%.2lf)' %(self.opencredit, self.opentotal))

gradesystem = GradeSystem()

while True:
    print("작업을 선택하세요")
    print("1. 입력")
    print("2. 출력")
    print("3. 조회")
    print("4. 계산")
    print("5. 종료")

    UserInput = int(input())

    match UserInput:
        case 1:
            #input
            inputs = input('과목명과 학점, 평점을 입력하세요:').split(", ")
            subject = inputs[0]
            credit = int(inputs[1])
            grade = inputs[2]
            print('입력되었습니다.')

            gradesystem.calc(grade, credit)
            gradesystem.RandomNumber(grade, credit)

        case 2:
            #output
            gradesystem.output()

        case 3:
            #call
            callsubject = input('과목명을 입력하세요:')
            gradesystem.call(callsubject)

        case 4:
            #calculation
            gradesystem.final()

        case 5:
            #end
            print('프로그램을 종료합니다.')
            break
