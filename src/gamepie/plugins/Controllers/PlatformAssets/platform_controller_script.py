from gamepie import key

# my/ai
class PlatformController:
    def __init__(self, player, camera, objects,camera_offset=(0,0), speed=0.05, jump_power=10, gravity=0.5, c_key_enabled=True, movement_3_key=("a","d","space")):
        self.player = player
        self.camera = camera
        self.objects = objects
        self._speed = speed
        self._status = None
        self._c_key_enabled = c_key_enabled 
        self._vel_y = 0
        self._gravity = gravity
        self._jump_power = jump_power
        self._movement_key = movement_3_key

        self._can_jump = False
        self._falling = False  # přidána proměnná pro kontrolu pádu
        self.camera_offset = camera_offset
    @property
    def status(self):
        return self._status

    @property
    def c_key_enabled(self):
        return self._c_key_enabled

    @c_key_enabled.setter
    def c_key_enabled(self, value: bool):
        self._c_key_enabled = bool(value)

    @property
    def speed(self):
        return self._speed

    @speed.setter
    def speed(self, value: float):
        if value < 0:
            value = 0
        self._speed = value

    @property
    def falling(self):
        return self._falling

    def update(self, dt):
        speed = self._speed * dt
        move_x = 0
        if self._can_jump and not self._falling:
            self._status = "stand"
        if self._falling and not self._can_jump:
            self._status = "falling"
        collision = not (self._c_key_enabled and key.is_down("c"))

        if key.is_down(self._movement_key[0]):
            move_x -= speed
            if self._can_jump:
                self._status = "left"
        if key.is_down(self._movement_key[1]):
            move_x += speed
            if self._can_jump:
                self._status = "right"

        if key.is_down(self._movement_key[2]) and self._can_jump:
            self._vel_y = -self._jump_power
            self._status = "jump"
            self._can_jump = False  

        self._vel_y += self._gravity
        self.player.y += self._vel_y

        self._falling = self._vel_y > 0

        if collision:
            for obj in self.objects:
                if self.player.collision.rect(obj):
                    if self._vel_y > 0:
                        self.player.y = obj.y - obj.height/2 - self.player.height/2
                        self._vel_y = 0
                        self._can_jump = True 
                        self._falling = False  
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

        # Nastavení kamery s offsetem
        self.camera.pos = (
            self.player.x + self.camera_offset[0],
            self.player.y + self.camera_offset[1]
        )
