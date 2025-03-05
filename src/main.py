from direct.showbase.ShowBase import ShowBase
from direct.task import Task
from panda3d.core import WindowProperties, Point3
from player import Player
from world import World

class Game(ShowBase):
    def __init__(self):
        ShowBase.__init__(self)

        # Window setup
        props = WindowProperties()
        props.setTitle("Space Horror")
        props.setSize(1280, 720)
        self.win.requestProperties(props)

        # Disable default mouse control
        self.disableMouse()

        # Create player
        self.player = Player(self)
        
        # Create world
        self.world = World(self)

        # Add update task
        self.taskMgr.add(self.update, "update")

    def update(self, task):
        dt = globalClock.getDt()
        self.player.update(dt)
        return Task.cont

if __name__ == "__main__":
    game = Game()
    game.run()
