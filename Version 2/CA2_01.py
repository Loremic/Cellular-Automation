import pygame as pg
import random as rm

dim,w=[620,620],0.80
A,screen=[[rm.randint(0,4) for _ in range(int(dim[0]/5))] for _ in range(int(dim[1]/5))],pg.display.set_mode(dim)

w0=0.30
for i in range(int(dim[0]/5)):
    for j in range(int(dim[1]/5)):
        if rm.random()>=w0-0.075 and rm.random()<=w0+0.075:
            A[i][j]=0


#to modify for v2.1        
def ev(grid: list):
    Ac=[[0 for _ in range(int(dim[0]/5))] for _ in range(int(dim[1]/5))]
    def neigh(grid,a,b):
        n,s=[0 for _ in range(5)],0
        for x in range(-1,2):
            for y in range(-1,2):  
                if x==0 and y==0:
                    continue
                else:
                    ni,nj=(a+x)%int(dim[0]/5),(b+y)%int(dim[1]/5)
                    match grid[ni][nj]:
                        case 0:
                            n[grid[ni][nj]]+=1
                        case 1:
                            n[grid[ni][nj]]+=1
                        case 2:
                            n[grid[ni][nj]]+=1
                        case 3:
                            n[grid[ni][nj]]+=1
                        case 4:
                            n[grid[ni][nj]]+=1
        m=0
        for i in range(len(n)):
            if n[i]>n[m]:
                m=i
        return m
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            N=neigh(grid,i,j)
            
    return Ac

def draw(grid):
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if grid[i][j]==0:
                pg.draw.rect(screen,(0,0,0),pg.Rect(i*5,j*5,5.0,5.0))
            elif grid[i][j]==1:
                pg.draw.rect(screen,(0,255,255),pg.Rect(i*5,j*5,5.0,5.0))
            elif grid[i][j]==2:
                pg.draw.rect(screen,(255,0,255),pg.Rect(i*5,j*5,5.0,5.0))
            elif grid[i][j]==3:
                pg.draw.rect(screen,(255,255,0),pg.Rect(i*5,j*5,5.0,5.0))
            elif grid[i][j]==4:
                pg.draw.rect(screen,(255,255,255),pg.Rect(i*5,j*5,5.0,5.0))
