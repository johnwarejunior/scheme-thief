from colorthief import ColorThief
import matplotlib.pyplot as plt
import colorsys
import webcolors

# Extract color palette with ColorThief
ss = ColorThief("images/testimg.png")
palette = ss.get_palette(color_count=5)

for color in palette:

  def closest_color(rgb):
    differences = {}
    for color_hex, color_name in webcolors.CSS3_HEX_TO_NAMES.items():
      r, g, b = webcolors.hex_to_rgb(color_hex)
      differences[sum([(r - rgb[0])**2, (g - rgb[1])**2,
                       (b - rgb[2])**2])] = color_name

    return differences[min(differences.keys())]

  try:
    cname = webcolors.rgb_to_name(color)
    print(f"Color Name: {cname}")
  except ValueError:
    cname = closest_color(color)
    print(f"Closest Color: {cname}")

  print(f"RGB: {color}")
  print(f"Hexcode: #{color[0]:02x}{color[1]:02x}{color[2]:02x}")
  print(f"HSV: {colorsys.rgb_to_hsv(*color)}")
  print(f"HLS: {colorsys.rgb_to_hls(*color)}")
  print(f" ")

plt.imshow([[palette[i] for i in range(5)]])
plt.show()
