import pygame as pg
import random as rm

def var(n):
    w,q=(800,600),0.30 #q is the life's quantity
    match n:
        case 1:
            return w
        case 2:
            return q

sc,z=pg.display.set_mode(var(1)),(var(1)[0]/5,var(1)[1]/5)
        
A=[[_ for _ in range(int(z[0]))] for _ in range(int(z[1]))]

for i in range(len(A)):
    for j in range(len(A[i])):
        c=rm.random()*4
        if c>var(2) and c<var(2)+1:
            A[i][j]=1
        elif c>var(2)+1 and c<var(2)+2:
            A[i][j]=2
        elif c>var(2)+2 and c<var(2)+3:
            A[i][j]=3
        elif c>var(2)+3 and c<var(2)+4:
            A[i][j]=4
        else:
            A[i][j]=0

def ev(grid):
    Ac=[[0 for _ in range(int(z[0]))] for _ in range(int(z[1]))]
    def neigh(grid,x,y,st):
        s=0
        for a in range(-1,1):
            for b in range(-1,1):
                if a==0 and b==0:
                    continue
                else:
                    ni,nj=(x+a)%int(z[0]),(y+b)%int(z[1])
                s+=grid[nj][ni]
        return s
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            st=grid[i][j]
            n=neigh(grid,i,j,st)
            #rules -> add some rules that can create contacts between the cell's types
            match grid[i][j]:
                case 0:
                    pass
    return Ac

def draw(grid,screen=sc):
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            #rules
            match grid[i][j]:
                case 0: 
                    pg.draw.rect(screen,(0,0,0),pg.Rect(i*5,j*5,5.0,5.0))
                case 1: 
                    pg.draw.rect(screen,(255,255,255),pg.Rect(i*5,j*5,5.0,5.0))
                case 2:
                    pg.draw.rect(screen,(255,50,50),pg.Rect(i*5,j*5,5.0,5.0))
                case 3:
                    pg.draw.rect(screen,(50,255,50),pg.Rect(i*5,j*5,5.0,5.0))
                case 4:
                    pg.draw.rect(screen,(50,50,255),pg.Rect(i*5,j*5,5.0,5.0))