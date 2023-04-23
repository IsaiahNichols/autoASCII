from PIL import Image
import math

shades = {
    
}
    
chars = "$@B%8&WM#*oahkbdpqwmZO0QLCJUYXzcvunxrjft/\\|()1{}[]?-_+~<>i!lI;:,\"^`'."
chars = chars[::-1]

image = Image.open("assets/image.png").convert("RGBA") # Change this path for custom image
px = image.load()

# You might need to change skip size to view image in terminal
# comfortably. Larger values shrink the image.
skip = 50
for i in range(image.size[1]):
    if i % skip == 0:
        for j in range(image.size[0]):
            if j % skip == 0:
                val = 0
                for k in range(len(px[j, i])):
                    val += (px[j, i][k])/255
                
                val /= len(px[j, i])
                val = 1-val
                val = round(val, 2)

                print(chars[math.floor(val*(len(chars)-1))], end="")
    
        print()