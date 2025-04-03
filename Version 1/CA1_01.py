import pygame as pg
import random as rm

dim,w=[620,620],0.80
A,screen=[[1 if rm.random()>w else 0 for _ in range(int(dim[0]/5))] for _ in range(int(dim[1]/5))],pg.display.set_mode(dim)

def ev(grid: list):
    Ac=[[0 for _ in range(int(dim[0]/5))] for _ in range(int(dim[1]/5))]
    def neigh(grid,a,b):
        n=0
        for x in range(-1,2):
            for y in range(-1,2):  
                if x==0 and y==0:
                    continue
                else:
                    ni,nj=(a+x)%int(dim[0]/5),(b+y)%int(dim[1]/5)
                    n+=grid[ni][nj]
        return n
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            N=neigh(grid,i,j)
            match grid[i][j]:
                case 0:
                    if N==3:
                        Ac[i][j]=1
                case 1:
                    if N<2 or N>3:
                        Ac[i][j]=0
                    else:
                        Ac[i][j]=1
    return Ac

def draw(grid):
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if grid[i][j]==1:
                pg.draw.rect(screen,(255,255,255),pg.Rect(i*5,j*5,5.0,5.0))
            else:
                pg.draw.rect(screen,(0,0,0),pg.Rect(i*5,j*5,5.0,5.0))
