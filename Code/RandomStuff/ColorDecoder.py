from PIL import Image

im= Image.open("colors.png")
pix = im.load()
colorFile = open("colorsT.txt",'w')
counter = 0
for y in range(1,129,16):
    for x in range(0,255,16):
        colorFile.write("""case {0}:
            pixels[i] = {1};    //r
            pixels[i+1] = {2};   //g
            pixels[i+2] = {3};   //b
            pixels[i+3] = {4};   //a
            break;
            """.format(str(counter),str(pix[x,y][0]),str(pix[x,y][1]),str(pix[x,y][2]),str(pix[x,y][3])))
        counter+=1
    colorFile.write("\n ")
    

colorFile.close()
