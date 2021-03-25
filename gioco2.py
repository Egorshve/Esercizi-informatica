class Entity: 
    def __init__(self, x, y, field):
        self.x = x
        self.y = y
        self.field = field
        self.field.entities.append(self)
    
    def check_collision(self, next_x, next_y):
        for e in self.field.entities:
            if e.x == self.x+(next_x) and e.y == self.y+(next_y):
                return e.name
            else:
                return None

    
    def move(self, direction):
        if direction == "up" and self.y > 0 and self.check_collision(0,-1) == None:
            self.y -= 1
        elif direction == "right" and self.x < field.w - 1 and self.check_collision(1,0) == None :
            self.x += 1
        elif direction == "down" and self.y < field.h - 1 and self.check_collision(0,1) == None:
            self.y += 1
        elif direction == "left" and self.x > 0 and self.check_collision(-1,0) == None:
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
p = Pokemon(3, 3, "Magikarp", 10, 20, field)
p1 = Pokemon(4, 3, "Charizard", 10, 30, field)
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

