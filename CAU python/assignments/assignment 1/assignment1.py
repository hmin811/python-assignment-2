print('직업을 선택하세요.')
print('1. 입력')
print('2. 계산')

n = int(input())
submitcredit = 0
opencredit = 0
total = 0
while n == 1:
    print('학점을 입력하세요:')
    credit = int(input())
    print('평점을 입력하세요:')
    grade = input()
    print('입력되었습니다')
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
    print('직업을 선택하세요.')
    print('1. 입력')
    print('2. 계산')
    n = int(input())
submittotal = total/submitcredit
opentotal = total/opencredit
print('제출용: %d학점 (GPA:%.2lf)' %(submitcredit, submittotal))
print('열람용: %d학점 (GPA:%.2lf)' %(opencredit, opentotal))
print('프로그램을 종료합니다.')
