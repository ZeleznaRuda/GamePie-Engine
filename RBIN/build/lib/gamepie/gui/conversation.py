from ..input.event import key,mouse
from ..time import wait
from ..rect import Rect
from ..draw.text import Text

class Conversation:
    def __init__(self, surface, messages: list, position=(200, 200), size=(190, 90),
                 background_color=(150,150,150), text_color=(0,0,0), anchor="topleft",
                 alpha=255, font = None, key="space", visible=True):
        
        self.surface = surface
        self._messages = messages
        self._index = 0
        self._key = key
        self._visible = visible

        self._font = font
        self._alpha = alpha
        self._anchor = anchor
        self._bg_color = background_color
        self._text_color = text_color
        self._position = position
        self._size = size

        self._message = self._messages[self._index] if self._messages else ""

        self.background = Rect(
            surface,
            position=position,
            size=size,
            color=background_color,
            alpha=alpha
        ).border_radius(5, 5, 5, 5)

        self.message = Text(
            surface,
            text=self._message,
            font=font,
            position=position,
            size=size,
            color=text_color,
            alpha=alpha
        )

    def _update(self):
        if not self._visible or not self._messages:
            return
        if self.background.collidepoint(mouse.pos):
            if key.is_down(self._key):
                if wait(500, f"__Gamepie.Conversation.{id(self)}"):
                    self._index += 1
                    if self._index >= len(self._messages):
                        self._index = 0
                    self._message = self._messages[self._index]
                    self.message.text = self._message

    def draw(self):
        if not self._visible:
            return
        self._update()
        self.background.draw()
        self.message.draw()

    @property
    def type(self): return "gui"
