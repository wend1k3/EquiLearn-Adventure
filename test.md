## model
### people
#### entity
- walkspeed
- pos
- walk dir

```python 
class Entity:
    def __init__(self,x,y,width,height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
```

#### player
inherit from entity
- bag