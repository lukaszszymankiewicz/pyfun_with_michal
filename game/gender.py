class Gender:
    def __init__(self):
        self.sex = None

    def gender_setter(self):
        val = input()
        self.sex = val

g = Gender()
print(g.sex)
