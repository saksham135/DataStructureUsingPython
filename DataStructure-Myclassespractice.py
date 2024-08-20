# part1-
# class youtube:
#     def __init__(self,uname,subscriber=0,subscriptions=0):
#         self.uname = uname
#         self.subscriber = subscriber
#         self.subscriptions = subscriptions
#
#     def subs(self,user):
#         user.subscriber+=1
#         self.subscriptions+=1
#
#
# user1 = youtube("Elshad")
# user2 = youtube("renad")
# user1.subs(user2)
# print(user1.subscriber)
# print(user1.subscriptions)
# print(user2.subscriber)
# print(user2.subscriptions)

class star_cookie:
    milk = 0.8

    def __init__(self,color,weight):
        self.color = color
        self.weight = weight

star_cookie1 = star_cookie('Red',20)
print(star_cookie1)
print(star_cookie1.color)
print(star_cookie1.weight)