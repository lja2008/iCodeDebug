
import builtins
from Util import Log

from Model.Dev import DevClass
from Model.Spaceship import SpaceshipClass
from Model.Item import ItemClass
from Model.Flyer import FlyerClass

#################### 此区域用于初始化 ####################
builtins.step = 0

def wait():
    Log.info(0, f'wait()')

Dev = DevClass(0,0,0)
Spaceship = SpaceshipClass(0,0,0)

Flyer = []
for i in range(20):
    Flyer.append(FlyerClass(0,0,0,i))

Item = []
for i in range(20):
    Item.append(ItemClass(0,0,0,i))


#########################################################

#################### 此区域用于实际代码 ###################
for i in range(4):
    for o in range(3):
        Dev.step(2)
        Dev.turnLeft()
    Dev.step(6)
    while Flyer[i].disappear():wait()
    Dev.step(2)

# for i in range(4):Flyer[i].step(i+1)
# for i in range(4):Flyer[i+4].step(i+1)
# for i in range(4):Flyer[i+8].step(i+1)
# for i in range(3):
#     for j in range(4):
#         Dev.turnLeft()
#         Dev.step(1+i if j>0 and j<3 else 5+i*2)
# for i in range(2):
#     Dev.turnRight()
#     Dev.step(14 if i==0 else 11)


#########################################################
