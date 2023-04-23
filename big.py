from PIL import Image
import math

shades = {
    
}
    
chars = "$@B%8&WM#*oahkbdpqwmZO0QLCJUYXzcvunxrjft/\\|()1{}[]?-_+~<>i!lI;:,\"^`'."
chars = chars[::-1]

path = input("Enter image path (e.g image.png): assets/")
im_type = "RGBA"
image = Image.open(f"assets/{path}").convert(f"{im_type}")
px = image.load()

# You might need to change skip size to view image in terminal
# comfortably. Larger values shrink the image.
res = ""
while res != "no":
    skip = int(input("Enter shrink value (int): "))
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