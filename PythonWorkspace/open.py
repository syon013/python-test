#score_file = open("score.txt", "w", encoding = "utf8") # txt 파일 생성
#print("수학 : 0", file = score_file)
#print("영어 : 50", file = score_file)
#score_file.close()

#score_file = open("score.txt", "a", encoding = "utf8") # txt 파일에 추가
#score_file.write("과학 : 80")
#score_file.write("\n코딩 : 100")
#score_file.close()

#score_file = open("score.txt", "r", encoding = "utf8") # txt 파일 읽기
#print(score_file.read())
#score_file.close()

#score_file = open("score.txt", "r", encoding = "utf8") # txt 파일 읽기
#print(score_file.readline(), end="") # 줄별로 읽기, 한 줄 읽고 커서는 다음 줄로 이동
#print(score_file.readline(), end="")
#print(score_file.readline(), end="")
#print(score_file.readline(), end="")
#score_file.close()


#score_file = open("score.txt", "r", encoding = "utf8") # txt 파일 읽기
#while True:
#    line = score_file.readline()
#    if not line: # 라인이 없으면
#        break   # 반복문 탈출
#    print(line, end="")
#score_file.close()


score_file = open("score.txt", "r", encoding = "utf8") # txt 파일 읽기
lines = score_file.readlines() # list 형태로 저장
for line in lines:  # list 형태로 저장된 것을 한 줄씩 출력
    print(line, end="")
score_file.close()