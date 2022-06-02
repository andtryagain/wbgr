from PIL import Image
  
def convertImage():
    img = Image.open("./img.png")
    img = img.convert("RGBA")
  
    data = img.getdata()
  
    newData = []
  
    for item in data:
        if item[0] == 255 and item[1] == 255 and item[2] == 255:
            newData.append((255, 255, 255, 0))
        else:
            newData.append(item)
  
    img.putdata(newData)
    img.save("./img_bg_rmvd.png", "PNG")
    print("Successful")
  
convertImage()
