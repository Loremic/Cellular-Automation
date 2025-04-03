import Ca_0 as ca
import time as tm

ca.pg.init()

r,t=True,0
while r:
    ca.screen.fill((0,0,0))
    if t==0: 
        grid=ca.A
    else:
        grid=ca.ev(grid)
    
    ca.draw(grid)
    tm.sleep(1)
        
    for e in ca.pg.event.get():
        if e.type==ca.pg.QUIT:
            r=False
    ca.pg.display.update()
    t+=1
            
ca.pg.quit()
