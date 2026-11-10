import os
from PIL import Image, ImageDraw
os.makedirs("resources",exist_ok=True)
def grad(s):
    im=Image.new("RGB",(s,s));p=im.load()
    for y in range(s):
        for x in range(s):
            t=(x+y)/(2*s);p[x,y]=(int(26+(120-26)*t),int(16+(40-16)*t),int(48+(200-48)*t))
    return im
def figure(s):
    im=Image.new("RGBA",(s,s),(0,0,0,0));d=ImageDraw.Draw(im);c=s/2
    def E(w,h,fill,dy=0):
        d.ellipse([c-w,c-h+dy,c+w,c+h+dy],fill=fill)
    E(s*.36,s*.24,(255,255,255,255))
    E(s*.32,s*.20,(198,255,61,255))
    for sx in(-1,1):
        d.ellipse([c+sx*s*.14-s*.035,c-s*.07-s*.06,c+sx*s*.14+s*.035,c-s*.07+s*.06],fill=(26,16,48,255))
    d.arc([c-s*.16,c-s*.06,c+s*.16,c+s*.12],20,160,fill=(26,16,48,255),width=int(s*.025))
    for sx in(-1,1):
        x=c+sx*s*.40;y=c
        d.polygon([(x+sx*s*.07,y),(x-sx*s*.01,y-s*.07),(x-sx*s*.01,y+s*.07)],fill=(255,79,163,255))
    return im
S=1024
fg=figure(S);bg=grad(S)
full=bg.convert("RGBA");full.alpha_composite(fg);full.save("resources/icon-only.png")
fg.save("resources/icon-foreground.png");bg.save("resources/icon-background.png")
sp=grad(2732).convert("RGBA");f=figure(1100);sp.alpha_composite(f,((2732-1100)//2,(2732-1100)//2))
sp.save("resources/splash.png");sp.save("resources/splash-dark.png")
