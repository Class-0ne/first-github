# # 02-2 문자열 자료형

# # 문자열 자료형을 나타내는 방법
# #     큰따옴표
# #     작은 따옴표
# #     따옴표 3개씩
# #     변수에 문자열을 저장할때 따옴표가 포함되는 경우에 해결

# # 역슬래시
# # 이스케이프 코드
# # 따옴표 3개

# # 문자열 더하기
# head = 'Python'
# tail = ' is fun!'
# print(head+tail)

# # # 문자열 곱하기
# c = 'python'
# print(c * 2)

# # # 문자열 곱하기 응용
# print("=" * 50) 
# print("My Program") 
# print("=" * 50)

# # # 문자열 길이 구하기
# print(len(head))

# # # 문자열 인덱싱
# a = "Life is too short, You need Python"
# print(a[3])

# # 문자열 인덱싱 활용하기
# print(a[-1])
# print(a[12])

# # 문자열 슬라이싱
#     # 단어 하나를 뽑아내기 위한 방법
#     # 아래 코드에서는 0부터 3까지 뽑아냄
#     # 마지막 숫자는 포함하지 않는다.
# print(a[0:4])

# # 슬라이싱으로 문자열 나누기
# a = "20230331Rainy"
# year = a[:4]
# date = a[4:8]
# weather = a[8:]
# print(year)
# print(date)
# print(weather)

# # 문자열 포매팅
#     # 문자열 안에 특정한 값을 바꿔야 할 경우에 사용함

# # 숫자 바로 대입
# print("I eat %d apple" %3)

# # 문자열 바로 대입
# print("I eat %s apple" % "five")

# # 숫자 값을 나타내는 변수로 대입
# number = 3
# print("I eat %d apple." %number)

# # 2개 이상의 값 넣기
#     # 2개 이상의 값을 넣으려면 % 다음 괄호에 (,)로 구분하여 넣기
# number = 10
# day = "three"
# print("I ate %d apples. so I was sick for %s days." % (number, day))

# # 문자열 포맷 코드
#     # %s - 문자열 %d - 정수 %f - 부동소수
#     # %s에는 어떤 형태의 값이든 변환해서 넣을 수 있다.

# # %s 예
# print("I have %s apples." % 3.124)


# # 포맷코드와 숫자 함께 사용하기
# # 1. 정렬과 공백
# print("%10s" % "hi") # 전체 길이 10에 hi를 오른쪽 정렬
# print("%-10s" % "hi") # 왼쪽 정렬

# # 2. 소수점 표현하기
# print("%0.4f" % 3.14159256) # 소수점 4개까지 표현
# print("%10.4f" % 3.14159256) # 10개의 문자열 공간에 소수점 4개까지 표현

# # format 함수를 사용한 포매팅
#     # 조금 더 발전된 스타일의 문자열 포맷

# # 숫자 바로 대입하기
# print("I eat {0} apples".format(3))

# # 문자열 바로 대입하기
# print("I eat {0} apples".format("five"))

# # 숫자 값을 가진 변수로 대입하기
# number = 6
# print("I eat {0} apples".format(number))

# # 2개 이상의 값 넣기
# day = "three"
# print("I ate {0} apples. so I was sick for {1} days.".format(number, day))

# # 이름으로 넣기
# print("I ate {number} apples. so I was sick for {day} days.".format(number=10, day ="five"))
# # {name} 형태로 하는 방법에서는 format 함수 안에 name = value 형태의 입력값이 필수

# # 인덱스와 이름 혼용해서 넣기
# print("I ate {0} apples. so I was sick for {day} days.".format(10, day=3))

# # 왼쪽 정렬
# print("'{0:<10}'".format("hi")) # :<10 표현으로 치환되는 문자열을 왼쪽 정렬하고 자릿수를 10으로 맞추기

# # 오른쪽 정렬
# print("'{0:>10}'".format("hi")) # 화살표의 방향으로 정렬한다고 생각하기

# # 가운데 정렬
# print("'{0:^10}'".format("hi")) # :^로 가운데 정렬

# # 공백 채우기
# print("'{0:!>10}'".format("hi")) # :> 사이에 문자 값을 넣어 그 문자로 빈 공간 채우기

# # 소수점 표현하기
# y = 3.141523523
# print("{0:0.4f}".format(y))

# # { } 문자 표현하기
# print("{{ and }}".format()) # format 함수에서 중괄호를 표현하는 방법

# # f 문자열 포매팅
# name = '홍길동'
# age = 30
# print(f'나의 이름은 {name}입니다. 나이는 {age}입니다.')

# # 딕셔너리 02-5에서 자세히 설명
# d = {"name":'홍길동', 'age':30}
# print(f'나의 이름은 {d["name"]}입니다. 나이는 {d["age"]}입니다.') # 딕셔너리는 key와 value라는 것을 한쌍으로 가지는 자료형

# # 정렬
# print(f'{"hi":>10}')
# # 공백 채우기
# print(f'{"hi":!^10}')
# # 소수점
# y = 3.42134234
# print(f'{y:10.4f}') # y를 4자리 까지 표현하고 자리수를 10으로 맞춤
# print(f'{y:0.4f}') # y를 소수점 4자리까지 표현
# # { } 표시
# print(f'{{ and }}')

# # 문자열 관련 함수들
# a = 'hobby'
# print(a.count('b')) # hobby에서 b의 갯수를 리턴

# 위치 알려주기 find
a = "Python is the best choice"
print(a.find('x'))

# 위치 알려주기 index
print(a.index('b'))

# 문자열 삽입 join
print(", ".join('abcd'))