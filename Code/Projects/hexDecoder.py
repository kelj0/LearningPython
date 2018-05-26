from PIL import Image

im= Image.open("colors.png")
pix = im.load()
test = Image.open("TEST.png")
Tpix = test.load()
hexFile = open("hex.txt",'w')
hsh = {}
hx = "81ff"
counter = 0
for y in range(1,131,16):
    for x in range(0,255,16):
        hs = hash(pix[x,y])
        hsh[hs] = hex(counter)
        counter+=1

for y in range(0,149):
    for x in range(0,192):
        tmp = hash(Tpix[x,y])
        fileString = """LDA #${0}\nSTA ${1}\n""".format(hsh.get(tmp),hx)
        hx = str(hex(int(hx,16)+1))
        
        hexFile.write(fileString)


hexFile.close()