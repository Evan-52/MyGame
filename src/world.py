from panda3d.core import DirectionalLight, AmbientLight, Vec4, Vec3
from direct.showbase.ShowBase import ShowBase

class World:
    def __init__(self, game):
        self.game = game
        
        # Set up basic lighting
        self.setup_lighting()
        
        # Create temporary ground
        self.create_temp_ground()
        
    def setup_lighting(self):
        # Main directional light
        dlight = DirectionalLight('dlight')
        dlight.setColor(Vec4(0.1, 0.1, 0.15, 1))
        dlnp = self.game.render.attachNewNode(dlight)
        dlnp.setHpr(45, -45, 0)
        self.game.render.setLight(dlnp)
        
        # Ambient light
        alight = AmbientLight('alight')
        alight.setColor(Vec4(0.2, 0.2, 0.3, 1))
        alnp = self.game.render.attachNewNode(alight)
        self.game.render.setLight(alnp)
        
    def create_temp_ground(self):
        # Create a simple ground plane for testing
        cm = CardMaker('ground')
        cm.setFrame(-100, 100, -100, 100)
        ground = self.game.render.attachNewNode(cm.generate())
        ground.setPos(0, 0, 0)
        ground.setP(-90)
        ground.setColor(0.2, 0.2, 0.2)
