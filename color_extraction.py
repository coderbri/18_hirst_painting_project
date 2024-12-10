import colorgram

# Extract 30 colors from the image
colors = colorgram.extract('image.jpg', 30)

# Save extracted colors
rgb_colors = []
for color in colors:
    r = color.rgb.r
    g = color.rgb.g
    b = color.rgb.b
    new_color = (r, g, b)
    rgb_colors.append(new_color)
print(rgb_colors)

color_list = [(249, 249, 249), (248, 246, 247), (224, 229, 236), (197, 172, 118), (160, 178, 193), (231, 241, 237), (191, 163, 177), (159, 184, 175), (212, 204, 125), (178, 188, 211), (204, 181, 194), (167, 208, 178), (166, 200, 213), (115, 123, 180), (208, 183, 182), (100, 100, 100), (52, 53, 52), (111, 109, 110), (156, 154, 93), (68, 68, 70)]
