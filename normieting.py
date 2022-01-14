class Creatures():
    def __init__(self, kind, abilities, look_alike ):
        self.kind = kind
        self.abilities = abilities
        self.look_alike = look_alike
        if self.kind == "god":
            self.look_alike = 0
            self.abilities = {"creating without any hard-work and even better options", "creates the other creature","controlling the other creatures"}
        elif self.kind == "human":
            self.look_alike = 7900000000
            self.abilities = {"tring to survive with their limited powers and abilities see !!", "can't control  the god creature *mind blowing noise*", "they do can kinda control other belows like animals"}
        elif self.kind == "animal":
            self.look_alike = 7770000	
            self.abilities = {"idiots"}
        elif self.kind == "angel":
            self.look_alike = 4	
            self.abilities = {"only follow orders from god", "have no freedom"}
        elif self.kind == "satan":
            self.look_alike = 1	
            self.abilities = {"idiot"}
    def __repr__ (self):
        return self.kind




a = Creatures("satan", None, None)

print(a.look_alike)