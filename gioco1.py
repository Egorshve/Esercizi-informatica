class Entity: 
    def __init__(self, x, y, field):
        self.x = x
        self.y = y
        self.field = field
        self.field.entities.append(self)

    def move(self, direction):
        if direction == "up" and self.y > 0:
            self.y -= 1
        elif direction == "right" and self.x < field.w - 1:
            self.x += 1
        elif direction == "down" and self.y < field.h - 1:
            self.y += 1
        elif direction == "left" and self.x > 0:
            self.x -= 1

class Pokemon(Entity):
    def __init__(self, x, y, name, damage, hp, field):
        super().__init__(x, y, field)
        self.name = name
        self.hp = hp
        self.damage = damage

    def info(self):
        print("sono", self.name, "hp:", self.hp, "e mi trovo a", self.x, ",", self.y)

    def attack(self, enemy):
        if self.hp <= 0:
            print(self.name, "non puoi attaccare da morto")
        else: 
            print(self.name, "attacca", enemy.name)
        if (enemy.hp <= 0):
            print(enemy.name, "e' morto")
        else:
            enemy.hp -= self.damage
      

class Field:
    def __init__(self):
        self.w = 5
        self.h = 5
        self.entities = []
    def draw(self):
        for y in range(self.h):
            for x in range(self.w):
                for e in self.entities:
                    if x == e.x and y == e.y:
                        print("[x]", end = "")
                        break    
                else:
                    print("[ ]", end = "")
            print()

field = Field()
p = Pokemon(4, 4, "Magikarp", 10, 20, field)
p1 = Pokemon(1, 1, "Charizard", 10, 30, field)
field.draw()
input()
p.move("right")
field.draw()
input()
p.move("down")
field.draw()
input()
p.move("left")
field.draw()
input()
p.move("up")
field.draw()
input()


