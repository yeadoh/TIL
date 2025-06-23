# # 2.1.1 연습 문제: 입력받은 숫자만큼 반복하기(while)
# # 문제
# # input()으로 사용자로부터 정수를 한 개 입력받아, 그 숫자를 숫자 크기만큼 반복해서
# # 출력하는 파이썬 스크립트를 작성하세요. 이때 출력 앞에 공백을 한 칸 주어서,
# # 입력과 출력이 구분되게 합니다. 단, while 문을 사용하세요.

# num = int(input("정수를 입력해주세요"))
# i = int(0)
# while(num > i):
#     print(num)
#     i += 1

# # 2.1.2 연습 문제: 제곱표(while)
# # 문제
# # 정수를 한 개 입력받아, 1부터 입력받은 수까지 각각에 대해 제곱을 구해 
# # 프린트하는 프로그램을 작성해 보세요.
# # 단, while 문을 사용하세요.1

# num = int(input("정수를 한 개 입력해주세요"))
# i = int(1)
# while(num >= i):
#     j = i * i
#     print(f"{i}의 제곱은 {j}입니다")
#     i += 1

# # 2.1.3 연습 문제: 얌체공
# # 문제
# # 고무공을 100 미터 높이에서 떨어뜨리는데,
# # 이 공은 땅에 닿을 때마다 원래 높이의 3/5 만큼 튀어오릅니다.
# # 공이 열 번 튈 동안, 그때마다 공의 높이를 계산합니다.1

# num = 100
# i = 0 
# while(i < 10):
#     num = round(num * 3 / 5, 4)
#     print(num)
#     i += 1

# 2.2.1 연습 문제: 숫자 읽기(1~3)
# 문제
# input()을 사용해 사용자로부터 입력받은 숫자를 한글로 출력하는 프로그램을 작성하세요.
# 단, 사용자는 1 이상 3 이하의 정수 중 하나를 입력한다고 가정합니다.

# num = input("1 ~ 3 사이의 숫자를 입력해주세요")

# if num == "1":
#     print("일")

# elif num == "2":
#     print("이")

# else: print("삼")

# 2.2.2 연습 문제: 나이에 따른 세대 구분 (1)
# 문제
# input()으로 사용자의 나이를 입력받은 후, 다음 표의 어느 세대에 속하는지 출력하세요.
# 입출력 문구는 자유롭게 지으면 됩니다.

# num = int(input("출생 년도를 입력해주세요"))

# if num <= 1924 :
#     print("The Greatest Generation")
# elif 1925 <= num <= 1945 : 
#     print("The Silent Generation")
# elif 1946 <= num <= 1964 : 
#     print("baby boomer")
# elif 1965 <= num <= 1980 : 
#     print("Generation X")
# elif 1981 <= num <= 1996 : 
#     print("millennial")
# elif 1997 <= num :
#     print("Generation Z")

