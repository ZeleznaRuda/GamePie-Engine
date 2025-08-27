from gamepie import key

class RPGController:
    def __init__(self, player, camera, objects, speed=0.05):
        self.player = player
        self.camera = camera
        self.objects = objects
        self._speed = speed
        self._direction_key = None
        self._c_key_enabled = True 


    @property
    def direction_key(self):
        """Poslední stisknutý směrový klíč (w/s/a/d)"""
        return self._direction_key

    @property
    def c_key_enabled(self):
        """Vrací True, pokud lze použít klávesu C k vypnutí kolizí"""
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

        if key.is_down("w"):
            move_y -= speed
            self._direction_key = "w"
        if key.is_down("s"):
            move_y += speed
            self._direction_key = "s"
        if key.is_down("a"):
            move_x -= speed
            self._direction_key = "a"
            self.player.flip = (False, False)
        if key.is_down("d"):
            move_x += speed
            self._direction_key = "d"
            self.player.flip = (True, False)

        old_x, old_y = self.camera.x, self.camera.y

        self.camera.x += move_x
        self.camera.y += move_y
        self.player.pos = self.camera.pos

   
        if collision:
            for obj in self.objects:
                if self.player.collision.mesh(obj):
                    self.camera.x = old_x
                    self.camera.y = old_y
                    self.player.pos = self.camera.pos
                    break
