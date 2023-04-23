from PIL import Image

shades = {
    0.4 : "-",
    0.5 : "~",
    0.6 : "/",
    0.7 : "+",
    0.8 : "#",
    0.9 : "@",
    1: "&"
}

image = Image.open("assets/image.png") # Change this path for custom image
px = image.load()

skip = 25

for i in range(image.size[1]):
    if i % skip == 0:
        for j in range(image.size[0]):
            if j % skip == 0:
                val = 0
                for k in range(len(px[i, j])):
                    val += (px[i, j][k])/255
                
                val /= len(px[i, j])
                val = 1-val
                val = round(val, 1)

                if val < 0.4:
                    val = 0.4
                elif val > 1:
                    val = 1

                print(shades[val], end="")
    
        print()