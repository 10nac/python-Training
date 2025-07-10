##class robot(object):
##    pass
##x = robot()
####y=robot()
####z=y
####print(y == z)
####print(x == y)
##x.brand = "BYD"
##print(x.brand)
###return x.brand
###print(robot.brand)
##print(x.__dict__)
##setattr(x,"brand2","tesla")
##print(getattr(x,"brand2"))
###print(x.brand2)
##x.robot = "robot_Z"
##print(x.robot)

##def intro(arg):
##    print("I am " + arg.one + " here")
##class what:
##    pass
##name = what()
##name.one = "10nac"
##intro(name)

##class init:
##    def __init__(self):
##        print("__init__ has been executed..")
##x = init()
        
##class robot:
##    def __init__(self,name=None):
##        self.name = name
##        
##    def say_hi(self):
##        if self.name:
##            print("we give that robot a name , It's name is " + self.name)
##        else:
##            print("We don't give a name to the robot..")
##    def walk(self,movement=None):
##        self.move = movement
##        if movement:
##            print("The robot is " + self.move)
##        else:
##            print("The robot is not moving at all..")
##        
##robot1 = robot()
##robot1.say_hi()
##
##robot2 = robot("10nac")
##robot2.say_hi()
##
##robot3 = robot("walker")
##robot3.walk("walking")
##robot3.say_hi()

##class robot():
##    def __init__(self):
##        self.name = None
##        self.sing = None
##        self.move = None
##        
##        
##    def voice(self):
##        if self.name :
##            print("Now,I am Exist.I am " + self.name)
##        else:
##            print("I got some Error...")
##            
##    def movement(self):
##        if self.move:
##            print("I am " + self.move)
##        else:
##            print("Some Error's are make stuck..")
##
##    def sing_song(self):
##        if self.sing:
##            print("Now I capable of sing the song " + self.sing)
##        else:
##            print("Again a Error, helps to sculpt my mind..")
##        
##            
##    def set_sing_song(self,sing):
##        self.sing = sing
##        
##    def get_sing_song(self):
##        return self.sing
##    
##    def set_name(self, name):
##        self.name = name
##        
##    def set_movement(self,move):
##        self.move = move
##        
##        
##x = robot()
##x.set_name("10nac")
##y = robot()
##y.set_movement("Running")
##
##x.set_movement(" in little movement")
##y.set_name("Ben10")
##
##x.set_sing_song("seval kodi song")
##y.set_sing_song("vetri vel song")
##
##x.voice()
##y.voice()
##
##x.movement()
##y.movement()
##
##x.sing_song()
##y.sing_song()
##
##print(x.get_sing_song())
##print(y.get_sing_song())

        
##name = ["boeing","hindustan","airindia"]
##str_name = str(name)
####print(name)
####print(str(','.join(name)))
##print(type(str_name))
      
##class A():
##    def __init__(self):
##        self.__priv = "I am Private..."
##        self._prot = "I am in Protected form ."
##        self.pub = "I am in public mood ."
        

from attribute_tests import A
x = A()
print(x.pub)
x.pub = x.pub + "you can freely see me ..."
print(x.pub)

print(x._prot)
x._prot = x._prot + "error found"
print(x._prot)

print(x.__priv)










 














