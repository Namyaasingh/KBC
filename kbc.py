question_list=["how many contineents are there ?" ],["what is the capital of india"],["In ng which course learning"]
option_list=["Four","Nine","Seven","Eight"],["Chandigarh","Bhopal","Chennai","Delhi"],["software engineering","counselling tourism","Agriculture"]
solution_list=[3,4,1]
print("welcome to kbc game")
print("good morning to all audience")
print("now our question showing on screen")
question=0
while question<len(question_list):
    print(question+1,question_list[question])
    option=0
    while option<len(option_list[question]):
        print(option+1,option_list[question][option])
        option=option+1
    answer=int(input("enter solution"))
    if answer==solution_list[question]:
        print("congrats")
    else:
        print("quit")
        break
    question=question+1