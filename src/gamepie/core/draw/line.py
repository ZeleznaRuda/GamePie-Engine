from ..rect import Rect
from .draw import line
from ..constants import camera
from ..color import _Color
class Line:
    def __init__(self, surface, positions=((100, 100), (200, 200)), width=3, color=(255,255,255),anti_aliasing=False,blend=False, enable=True, visible=True):
            self.surface = surface
            self._color = color
            self.__destroyed = False
            self._width = width
            self._spos, self._epos = positions
            self._visible = visible
            self._anti_aliasing = anti_aliasing
            self._blend = blend
            self._enable = enable
            self.color = color
    def _set_poss(self, poss):
        self._spos, self._epos = poss
    
    def draw(self):
        if not self._visible:
            return
        if not self._enable:
            return
        line(surface=self.surface,color=self._color,width=self._width, start_pos=self._spos, end_pos=self._epos,anti_aliasing=self._anti_aliasing, blend=self._blend)


    @property
    def positions(self): 
        return self._spos, self._epos

    @positions.setter
    def positions(self, value): 
        self._set_poss(value)
        
    @property
    def start_pos(self): 
        return self._spos

    @start_pos.setter
    def start_pos(self, value): 
        self._set_poss((value, self._epos))

    @property
    def end_pos(self): 
        return self._epos

    @end_pos.setter
    def end_pos(self, value): 
        self._set_poss((self._spos, value))

    @property
    def width(self): return self._width

    @width.setter
    def width(self, value): self._width = value


    @property
    def visible(self): return self._visible

    @visible.setter
    def visible(self, value): self.visible = value

    @property
    def enable(self): return self._enable

    @enable.setter
    def enable(self, value): 
        self._enable = value


    @property
    def color(self): return self._color

    @color.setter
    def color(self, value): 
        self._color = _Color(value)()

    def copy(self):
        return self
