class MoveCharacter:
    def move_fwd(self):
        print("Move Fwd")
    def move_bwd(self):
        print("Move Bwd")

class JumpCharacter(MoveCharacter):
    def jump_1level(self):
        print("Jump 1 Level")
    def jump_2level(self):
        print("Jump 2 Level")

class Pokemon(JumpCharacter):
    def moving(self):
        print("Pokemon is Moving")

p = Pokemon()
p.move_fwd()
p.move_bwd()
p.jump_1level()
p.jump_2level()
p.moving()
print(Pokemon.mro()) #method resolution order: first it checks in the current class, then in the parent class, and order of checking is depth first search, from left to right.