try:
    fr = open("P3_AS2_Grade.txt","w",encoding="utf-8")
    '''
    fw = open("P3_AS2_Score.txt","w",encoding="utf-8")
    while True:
            studentid = input("ป้อนข้อมูลคะแนนนักเรียน: ")
            if studentid == "exit":
                break
            score = input("ป้อนคะแนน: ")
            fw.writelines(studentid+"\t"+score+"\n")
    fw.close()
    '''
    fr2 = open("P3_AS2_Score.txt","r",encoding="utf-8")
    grade = None
    for line in fr2.readlines():
        score=line[-4:].strip()
        studentid = line[:-4].strip()
        score = int(score)
        if score>= 80:
            grade = "A"
        elif score >=70 and score <80:
            grade = "B"
        elif score >=50 and score <69:
            grade = "C"
        else:
            grade = "Failed"
        fr.writelines(studentid+"\t"+str(score)+"\t"+grade+"\n")
    fr.close()
    fr2.close()    
except Exception as e:
    print(e)