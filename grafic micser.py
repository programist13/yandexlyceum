from PIL import Image


def twist_image(input_ﬁle_name, output_ﬁle_name):
    image: Image.Image = Image.open(input_ﬁle_name)
    pixels = image.load()
    width, height = image.size
    left = Image.new('RGB', (width // 2, height))
    l_p = left.load()
    right = Image.new('RGB', (width // 2, height))
    r_p = right.load()
    for x in range(width):
        for y in range(height):
            pixel = pixels[x, y]
            if x < width // 2:
                l_p[x, y] = pixel
            else:
                r_p[x - width // 2, y] = pixel
    image.paste(right, (0, 0))
    image.paste(left, (width // 2, 0))

    image.save(output_ﬁle_name)
