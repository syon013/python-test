#for week in range(1, 51): # 1 ~ 50주차까지
#    report_file = open(str(week) + "주차 보고서.txt", "w", encoding = "utf8") # txt 파일 생성
#    print("- {0} 주차 주간보고 -".format(week), file = report_file)
#    print("부서 : 코딩", file = report_file)
#    print("이름 : 요진", file = report_file)
#    print("업무 요약 : ", file = report_file)
#    report_file.close()

for week in range(1, 51):
    with open(str(week) + "주차 보고서.txt", "w", encoding = "utf8") as report_file:
        report_file.write("- {0} 주차 주간보고 -\n".format(week))
        report_file.write("부서 : \n")
        report_file.write("이름 : \n")
        report_file.write("업무 요약 : \n")
