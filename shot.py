import pygame


from circleshape import CircleShape


class Shot(CircleShape):
    SHOT_RADIUS = 5
    def __init__(self, x, y):
        super().__init__(x, y, Shot.SHOT_RADIUS)

    def draw(self,screen):
        pygame.draw.circle(screen,(255,255,255),self.position,width=2 ,radius=self.SHOT_RADIUS)
    
    def update(self, dt):
        self.position += (self.velocity * dt)