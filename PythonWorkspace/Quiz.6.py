#def std_weight(height, gender):
#    he = height * 0.01
#    gender = "남자"


#    if(gender == "남자"):
#        print("키 {0}cm 남자의 표준 체중은 {1}kg 입니다.".format(height, round(he * he * 22, 2)))
#    else:
#        print("키 {0}cm 여자의 표준 체중은 {1}kg 입니다.".format(height, round(he * he * 21, 2)))

#std_weight(177, "남자")



def std_weight(height, gender):
    if(gender == "남자"):
        return height * height * 22
    else: 
        return height * height * 21

height = 175
gender = "여자"
weight = round(std_weight(height / 100, gender),2)
print("키 {0}cm {1}의 표준 체중은 {2}kg 입니다.".format(height, gender, weight))