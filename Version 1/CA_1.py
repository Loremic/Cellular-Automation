import CA1_01 as ca
import time as tm

ca.pg.init()

r,t=True,0

while r:
    ca.sc.fill((0,0,0))
    if t==0:
        grid=ca.A
    else:
        grid=ca.ev(grid)
    tm.sleep(0.25)
    ca.draw(grid)
    for e in ca.pg.event.get():
        if e.type==ca.pg.QUIT:
            r=False
    ca.pg.display.update()
    t+=1
            
ca.pg.quit()