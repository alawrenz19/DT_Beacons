import bsmLib
from bsmLib import RPL
from bsmLib import tcpServer
from bsmLib import vector 

roscore
cd ~/catkin_ws
source devel/setup.bash
ls /dev/ttyACM*
rosrun marvelmind_nav hedge_rcv_bin /dev/ttyACM1

tcpServer(port = '10003')

t = tcpServer()
t.listen()

vec = vector()

def c_read():
    coords = t.recv()

    startx = coords.find( 'X=' )
    midy = coords.find( 'Y=' )
    endz = coords.find( 'Z=' )

    if start != -1 and end != -1:
        result = coords[startx+1:midy+1:endz]

    lat, long, height = result.split

    vec.set(lat, long)
    return vec
