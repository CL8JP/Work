import random

class Main:
    Names: list[str] | None = None

    def GetRandom(self):
        return random.choice(self.Names)
    
    def __init__(self, Names: list[str]):

        self.Names = Names

        return None
    
class Sub(Main):
    def __init__(self, Names: list[str]):

        self.Names = Names

        return None

New = Sub(["Yes"])

print(Sub.GetRandom())

#New = Main(["Cat", "Cate", "Carter", "Catherine", "Charlie"])
           
#print(New.GetRandom())