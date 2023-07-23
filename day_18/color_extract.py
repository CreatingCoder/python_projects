import colorgram as cg

#creates list of colors used
colors = cg.extract('day_18/image.jpg', 20)

#Color: Rgb(r=234, g=234, b=234), 4.345

rgb_list = []

for i in colors:
    r = i.rgb.r
    g = i.rgb.g
    b = i.rgb.b

    new_color = (r,g,b)
    rgb_list.append(new_color)

print(rgb_list)
    
