import pygame
import random
from circleshape import CircleShape
from logger import log_event
from constants import *

class Asteroid(CircleShape):

    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            # print("destroyed")
            return
        else:
            log_event("asteroid_split")
            split_angle = random.uniform(20,50)
            split1 = Asteroid(self.position[0],self.position[1],self.radius - ASTEROID_MIN_RADIUS)
            split1.velocity = self.velocity.rotate(split_angle) * 1.2
            split2 = Asteroid(self.position[0],self.position[1],self.radius - ASTEROID_MIN_RADIUS)
            split2.velocity = self.velocity.rotate(-split_angle) * 1.2


    def draw(self,screen):
        pygame.draw.circle(screen,"white",self.position,self.radius,2)

    def update(self, dt):
        self.position += (self.velocity * dt)

