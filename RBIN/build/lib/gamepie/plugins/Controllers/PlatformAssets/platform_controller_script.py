from gamepie import key
# my/ai
class PlatformController:
    def __init__(self, player, camera, objects, speed=0.05, jump_power=10, gravity=0.5,c_key_enabled=True, movement_3_key=("a","d","space")):
        self.player = player
        self.camera = camera
        self.objects = objects
        self._speed = speed
        self._direction_key = None
        self._c_key_enabled = c_key_enabled 
        self._vel_y = 0
        self._gravity = gravity
        self._jump_power = jump_power
        self._movement_key = movement_3_key

        self._can_jump = False 


    def update(self, dt):
        speed = self._speed * dt
        move_x = 0
        collision = not (self._c_key_enabled and key.is_down("c"))

        if key.is_down(self._movement_key[0]):
            move_x -= speed
            self._direction_key = "left"
        if key.is_down(self._movement_key[1]):
            move_x += speed
            self._direction_key = "right"


        if key.is_down(self._movement_key[2]) and self._can_jump:
            self._vel_y = -self._jump_power
            self._direction_key = "jump"
            self._can_jump = False  

        self._vel_y += self._gravity
        self.player.y += self._vel_y

        if collision:
            for obj in self.objects:
                if self.player.collision.rect(obj):
                    if self._vel_y > 0:
                        self.player.y = obj.y - obj.height/2 - self.player.height/2
                        self._vel_y = 0
                        self._can_jump = True 
                    elif self._vel_y < 0:
                        self.player.y = obj.y + obj.height/2 + self.player.height/2
                        self._vel_y = 0


        self.player.x += move_x
        if collision:
            for obj in self.objects:
                if self.player.collision.rect(obj):
                    if move_x > 0: 
                        self.player.x = obj.x - obj.width/2 - self.player.width/2
                    elif move_x < 0: 
                        self.player.x = obj.x + obj.width/2 + self.player.width/2

        self.camera.pos = self.player.pos
