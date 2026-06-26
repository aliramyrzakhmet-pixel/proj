from mcpi.minecraft import Minecraft 
import collections
collections.Iterable = collections.abc.Iterable
mc = minecraft.create()

teleport_points = {
    "home": [23, 56, 113],
    "mine": [45, 5, 120],
}

teleport_points = {
    "home": {
        "x": 23,
        "y": 56,
        "z": 113,
    }, 
    "mine": {
        "x": 45,
        "y": 5,
        "z": 120,
    }
}

teleport_points["home"]["x"]
teleport_points["home"]["y"]
teleport_points["home"]["z"]

teleport_points = {}

def add_point(name_point):
    """Добавление к новой точке"""
    global teleport_points
    x, y, z = mc.plaeyer.getTitlePos()
    y += 1 
    teleport_points[name_point] = {
        "x": x,
        "y": y,
        "z": z,
    }
    mc.postToChat(f"{name_point} - add to list points")

def add_point(name_point):
    ...
    x, y, z, = mc.player.getTitlePos()
    teleport_points[name_point] = {"x": x, "y": y, "z": z}

def del_point(name_point) :
    global teleport_points
    if name_point in teleport_points:
        del teleport_points[name_point]

def list_points():
    if keys:
        mc.postToChat("LIST OF TELEPORT POINTS")
        for key in keys:
            mc.postToChat(f"- {key}")
    else:
        mc.postToChat("listis my empty")
        mc.postToChat("use command set/add NAME_POINT")

def teleport_to_point(name_point):
    if name_point in teleport_points:
        x = teleport_points[name_point]["x"]
        y = teleport_points[name_point]["y"]      
        z = teleport_points[name_point]["z"]
    else:
        mc.plaer.setPost(x, y, z)
        mc.postToChat (f"Point {name_point} not found")
        list_points()
    
loop = True
if __name__ == "__main__":
    while loop:
        chatik = mc.events.pollChatPosts()
        for message in chatik:
            msg = message.message.lower()

string = "Привет, мир" .split()
print(string)

msg = "set home".split()
print(msg)
msg = "tp 100 150 100".split()
print(msg)