#code
import random
def calc(grade, opencredit, submitcredit, credit, total):
    opencredit += credit
    if grade != 'F':
        submitcredit += credit
    match grade:
        case 'A+':
            total += 4.5*credit
        case 'A':
            total += 4*credit
        case 'B+':
            total += 3.5*credit
        case 'B':
            total += 3*credit
        case 'C+':
            total += 2.5*credit
        case 'C':
            total += 2*credit
        case 'D+':
            total += 1.5*credit
        case 'D':
            total += 1*credit
    return [opencredit, submitcredit, total]
submitcredit = 0
opencredit = 0
total = 0
subjectname = {}
courses = []
while True:
    print("작업을 선택하세요")
    print("1. 입력")
    print("2. 출력")
    print("3. 계산")
    n = int(input())
    if n == 1:
        #input
        print('과목명을 입력하세요:')
        subject = input()
        print('학점을 입력하세요:')
        credit = int(input())
        print('평점을 입력하세요:')
        grade = input()
        print('입력되었습니다.')
        #updating totals
        tmp = calc(grade, opencredit, submitcredit, credit, total)
        opencredit = tmp[0]
        submitcredit = tmp[1]
        total = tmp[2]
        #generating random code 
        k = random.randint(10000, 99999)
        subjectname[k] = subject
        courses.append((str(k), credit, grade))
    elif n == 2:
        for i in range(0, len(courses)):
            print('[%s] %d학점: %s'%(subjectname[int(courses[i][0])], courses[i][1], courses[i][2]))
    else:
        break
submittotal = total/submitcredit
opentotal = total/opencredit
print('제출용: %d학점 (GPA:%.2lf)' %(submitcredit, submittotal))
print('열람용: %d학점 (GPA:%.2lf)' %(opencredit, opentotal))
print('프로그램을 종료합니다.')