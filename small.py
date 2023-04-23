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

path = input("Enter image path (e.g image.png): assets/")
im_type = "RGBA"
image = Image.open(f"assets/{path}").convert(f"{im_type}")
px = image.load()

# You might need to change skip size to view image in terminal
# comfortably.
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
                    val = round(val, 1)

                    if val < 0.4:
                        val = 0.4
                    elif val > 1:
                        val = 1

                    print(shades[val], end="")
        
            print()
    
    res = input("Rescale output (yes/no)? ").lower()