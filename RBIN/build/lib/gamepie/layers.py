
class Layers:
    def __init__(self,*items):
        self._items = items
    
    def draw(self):
        for item in self._items:
            item.draw()
