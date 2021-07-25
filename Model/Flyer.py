from Util import Log
import time
import random

class FlyerClass:
    x = 0
    y = 0
    d = 0
    order=0

    def __init__(self, x, y, d,order=0):
        self.x = x
        self.y = y
        self.d = d
        self.order=order
    
    def disappear(self):
        # result = int(time.time() % 60)%2==0
        result = int(random.randint(0,100))%2==0
        Log.info(0, f'Flyer[{self.order}].disappear() : {result}')
        return result

    def step(self,n):
        Log.info(n, f'Flyer[{self.order}].step({n})')
