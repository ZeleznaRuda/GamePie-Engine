from gamepie import key
class RPGController:
    def __init__(self, player, camera, objects, speed=0.05,c_key_enabled=False,movement_4_key=("w","s","a","d")):
        self.player = player
        self.camera = camera
        self.objects = objects
        self._speed = speed
        self._direction_key = None
        self._c_key_enabled = c_key_enabled 
        self._movement_key = movement_4_key


    @property
    def direction_key(self):
        return self._direction_key

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


    def update(self, dt):
        move_x = 0
        move_y = 0
        speed = self._speed * dt

        collision = True
        if self._c_key_enabled:
            collision = not key.is_down("c")

        if key.is_down(self._movement_key[0]):
            move_y -= speed
            self._direction_key = "up"
        if key.is_down(self._movement_key[1]):
            move_y += speed
            self._direction_key = "down"
        if key.is_down(self._movement_key[2]):
            move_x -= speed
            self._direction_key = "left"
        if key.is_down(self._movement_key[3]):
            move_x += speed
            self._direction_key = "right"

        old_x, old_y = self.camera.x, self.camera.y

        self.camera.x += move_x
        self.camera.y += move_y
        self.player.pos = self.camera.pos

   
        for obj in self.objects:
            if self.player.collision.mesh(obj) and collision:
                        self.camera.x = old_x
                        self.camera.y = old_y
                        self.player.pos = self.camera.pos
                        break

