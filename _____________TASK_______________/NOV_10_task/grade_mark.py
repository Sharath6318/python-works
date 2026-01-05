def grade(mark):

    grade_1 = "A"
    grade_2 = "B"
    grade_3 = "C"
    grade_4 = "F"

    if(mark >= 90):

        return grade_1
    
    elif(mark >= 75):

        return grade_2
    
    elif(mark >= 50):

        return grade_3
    
    else:

        return grade_4
    
print(grade(90))