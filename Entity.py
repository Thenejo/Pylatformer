import pygame
class entity:
    def __init__(self,x,y,texture,id=0):
        self.id=id
        self.pos=[x,y]
        self.scale=[1,1]
        self.sprite=texture
        self.rect=pygame.Rect(x,y,self.sprite.tex.get_size()[0],self.sprite.tex.get_size()[1])

    def move(self, motion, tiles):
        self.pos[0] += motion[0]
        self.rect.x=self.pos[0]
        temp_rect = self.rect
        directions = {k : False for k in ['top', 'left', 'right', 'bottom']}
        for tile in tiles:
            if temp_rect.colliderect(tile.rect):
                if motion[0] > 0:
                    temp_rect.right = tile.rect.left
                    self.pos[0] = temp_rect.x
                    directions['right'] = True
                elif motion[0] < 0:
                    temp_rect.left = tile.rect.right
                    self.pos[0] = temp_rect.x
                    directions['left'] = True


        self.pos[1] += motion[1]
        self.rect.y=self.pos[1]
        temp_rect = self.rect
        for tile in tiles:
            if temp_rect.colliderect(tile.rect):
                if motion[1] > 0:
                    temp_rect.bottom = tile.rect.top
                    self.pos[1] = temp_rect.y
                    directions['bottom'] = True
                elif motion[1] < 0:
                    temp_rect.top = tile.rect.bottom
                    self.pos[1] = temp_rect.y
                    directions['top'] = True


        return directions

    def render(self,window):
       window.blit(self.sprite.tex,self.pos)
