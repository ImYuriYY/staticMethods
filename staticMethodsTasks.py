# TASK "Robot"

# class Robot:
#     MAX_COORD = 100
#     MIN_COORD = 0

#     def __init__(self, x=0, y=0):
#         self.x = self.y = 0
#         if Robot.validate(x) and Robot.validate(y):
#             self.x = x
#             self.y = y
#             self.countOfCall = 0

#     def path(self):
#         if(self.countOfCall == 0):
#             print(list(self.x, self.y))
#         else:
#             print(self.arrayOfLastMove)
        
#     def move(self, coords):
#         self.countOfCall +=1
#         self.arrayOfLastMove = []
#         for i in range(len(coords)):
#             if(coords[i] == "N"):
#                 if(self.y != 100):
#                     self.y += 1
#                 else:
#                     print("N - Дальше двигать некуда!")
#                     self.arrayOfLastMove.insert(0, self.x)
#                     self.arrayOfLastMove.insert(0, self.y)
#                     self.path()
#                     break
#             elif(coords[i] == "S"):
#                 if(self.y != 0):
#                     self.y -= 1
#                 else:
#                     print("S - Дальше двигать некуда!")
#                     self.arrayOfLastMove.insert(0, self.x)
#                     self.arrayOfLastMove.insert(0, self.y)
#                     self.path()
#                     break
#             elif(coords[i] == "E"):
#                 if(self.x != 100):
#                     self.x += 1
#                 else:
#                     print("E - Дальше двигать некуда!")
#                     self.arrayOfLastMove.insert(0, self.x)
#                     self.arrayOfLastMove.insert(0, self.y)
#                     self.path()
#                     break
#             elif(coords[i] == "W"):
#                 if(self.x != 0):
#                     self.x -= 1
#                 else:
#                     print("W - Дальше двигать некуда!")
#                     self.arrayOfLastMove.insert(0, self.x)
#                     self.arrayOfLastMove.insert(0, self.y)
#                     self.path()
#                     break
#             if (i + 1 == len(coords)):
#                 self.arrayOfLastMove.insert(0, self.x)
#                 self.arrayOfLastMove.insert(0, self.y)
#                 break

#     @classmethod
#     def validate(cls, arg):
#         return cls.MIN_COORD <= arg <= cls.MAX_COORD



# myRobot = Robot(0,0)
# myRobot.move("NNEESNNWW")
# myRobot.path()
        










# TASK Talking

# class Talking:
#     def __init__(self, name):
#         self.name = name
#         self.answerCount = 0
#         self.yesAnswers = 0
#         self.noAnswers = 0
    
#     def to_answer(self):
#         self.answerCount += 1
#         if (self.answerCount % 2 != 0):
#             self.yesAnswers += 1
#             return("moore-moore")
#         else:
#             self.noAnswers += 1
#             return("meow-meow")
        
#     def number_yes(self):
#         return self.yesAnswers
    
#     def number_no(self):
#         return self.noAnswers

    


# myCat = Talking("Badili")
# print(myCat.to_answer())
# print(myCat.to_answer())
# print(myCat.to_answer())

# print(f'{myCat.name} сказал "Да" {myCat.number_yes()} раз, "Нет" {myCat.number_no()}.')
