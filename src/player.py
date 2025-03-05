from direct.showbase.ShowBase import ShowBase
from panda3d.core import Point3, Vec3
import math

class Player:
    def __init__(self, game):
        self.game = game
        
        # Movement settings
        self.move_speed = 5.0
        self.sprint_multiplier = 2.0
        self.mouse_sensitivity = 0.2
        
        # Initial position and rotation
        self.position = Point3(0, 0, 2)
        self.rotation = Vec3(0, 0, 0)
        
        # Set up camera
        self.game.camera.setPos(self.position)
        
        # Movement state
        self.keys = {'w': False, 'a': False, 's': False, 'd': False, 'shift': False}
        
        # Set up input handling
        self.setup_controls()
        
    def setup_controls(self):
        # Keyboard controls
        self.game.accept("w", self.update_key, ['w', True])
        self.game.accept("w-up", self.update_key, ['w', False])
        self.game.accept("a", self.update_key, ['a', True])
        self.game.accept("a-up", self.update_key, ['a', False])
        self.game.accept("s", self.update_key, ['s', True])
        self.game.accept("s-up", self.update_key, ['s', False])
        self.game.accept("d", self.update_key, ['d', True])
        self.game.accept("d-up", self.update_key, ['d', False])
        self.game.accept("shift", self.update_key, ['shift', True])
        self.game.accept("shift-up", self.update_key, ['shift', False])

    def update_key(self, key, value):
        self.keys[key] = value

    def update(self, dt):
        # Mouse look
        if self.game.mouseWatcherNode.hasMouse():
            mouse_x = self.game.mouseWatcherNode.getMouseX()
            mouse_y = self.game.mouseWatcherNode.getMouseY()
            
            # Center mouse
            self.game.win.movePointer(0,
                int(self.game.win.getProperties().getXSize() / 2),
                int(self.game.win.getProperties().getYSize() / 2))
            
            # Update rotation
            self.rotation.x -= mouse_y * self.mouse_sensitivity
            self.rotation.x = max(-85, min(85, self.rotation.x))
            self.rotation.y -= mouse_x * self.mouse_sensitivity
            
            # Apply rotation to camera
            self.game.camera.setHpr(self.rotation)
        
        # Movement
        move_dir = Vec3(0, 0, 0)
        if self.keys['w']: move_dir.y += 1
        if self.keys['s']: move_dir.y -= 1
        if self.keys['a']: move_dir.x -= 1
        if self.keys['d']: move_dir.x += 1
        
        # Normalize movement vector
        if move_dir.length() > 0:
            move_dir.normalize()
        
        # Apply sprint multiplier
        speed = self.move_speed * (self.sprint_multiplier if self.keys['shift'] else 1.0)
        
        # Move relative to camera direction
        heading_rad = math.radians(self.rotation.y)
        final_move = Vec3(
            move_dir.x * math.cos(heading_rad) - move_dir.y * math.sin(heading_rad),
            move_dir.x * math.sin(heading_rad) + move_dir.y * math.cos(heading_rad),
            0
        ) * speed * dt
        
        self.position += final_move
        self.game.camera.setPos(self.position)
