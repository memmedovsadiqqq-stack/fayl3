exam_score = int(input())
school_score = int(input())
age = int(input())

if age < 16 :
    print("Rejected")
elif school_score > 700 or exam_score > 100 :
    print("Please, input the information correctly")
elif exam_score >= 600:
    print("Scholarship")
elif exam_score >= 450 :
    print("Accepted")
elif exam_score >= 300 and school_score >= 80 :
    print("Accepted")
else :
    print("Rejected")