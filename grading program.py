student_scores={
    "Harry:":81,
    "Ron":78,
    "Hermione":99,
    "Draco":74,
    "Neville":62,
    }

student_scores["Alin"]="100"


for item in student_scores:
    print(item)
    a=int((student_scores[item]))
    if (a>=91)and(a<=100):
           b="Outstanding"
    if (a>=81)and(a<=90):
           b="Exceeds Expectations"
    if (a>=71)and(a<=80):
           b="Acceptable"
    if (a<=70):
           b="Fail"
    print(b)  
    

     