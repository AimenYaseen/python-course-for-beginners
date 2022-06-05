from unicodedata import name


class Programmer:
    company="Microsoft"
    programmer =[]

    def __init__(self, name="", age=0, skill="", experience="", designation=""):
        # initializing
        self.name = name
        self.age = age
        self.skill = skill
        self.experience = experience
        self.designation = designation

        # Adding to list
        Programmer.programmer.append(self)
    
    def get_info(self):
        print(f"Programmer Name: {self.name}\nAge: {self.age}\n Skill: {self.skill}")
    
    @staticmethod
    def all_programmers():
        if len(Programmer.programmer):
            # print(Programmer.programmer)
            for prog in Programmer.programmer:
                print(prog.name)
        else:
            print("There are no programmers yet")
  
Happy = Programmer("Happy", 35, "hsjd", "sdhs", "gjdg")
Happy.get_info()
Happy.all_programmers()