import pygame
import os

class Texture:
    def __init__(self,texturedir,colorKey=(255,255,255)):
        self.tex=pygame.image.load(texturedir).convert()
        self.tex.set_colorkey(colorKey)
        self.flipX=False
        self.flipY=False
        self.sTex=self.tex


    def SetFlip(self,flipX=False,flipY=False):
        self.tex=pygame.transform.flip(self.sTex,flipX,flipY)

class Animation:
    def __init__(self,frames,FrameTime):
        self.frames=frames
        self.frameTime=FrameTime
        self.frameIndex=0
        self.frameTimer=0

    #returns the texture that Should be shown
    def Play(self):
        self.frameTimer+=1
        if self.frameTimer>=self.frameTime:
            self.frameIndex+=1
            self.frameTimer=0
        if self.frameIndex>=len(self.frames):
            self.frameIndex=0
        return self.frames[self.frameIndex]

class AnimatonController:
    def __init__(self,animationDic,StartState="Null"):#animationDic is a dictionary of animations with their state names example ["Run":RunAnim,"Idle":IdlenAnim]
        self.animatons=animationDic
        self.state=StartState
    def flipAnims(self,flipX,flipY):
        for anim in self.animatons.values():
            for t in anim.frames:
                t.SetFlip(flipX,flipY)
    def setState(self,state):
        self.state=state
    def Run(self):
        return self.animatons[self.state].Play()

def loadAnimationFromFolder(folderDir,frameTime=8,colorKey=(255,255,255),imageType="png"):
    files=os.listdir(folderDir)
    ImageDirs=[]
    Images=[]
    for f in files:
        if f.split(".")[1]==imageType:
            ImageDirs.append(f)
    for dr in ImageDirs:
        img=Texture(folderDir+"/"+dr)
        Images.append(img)
    return Animation(Images,frameTime)
