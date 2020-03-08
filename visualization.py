from PIL import Image, ImageDraw, ImageOps, ImageFont

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)


def visualize(matrix, releases):
    print("Visualizing matrix")

    WIDTH = 2000
    HEIGHT = 2000

    im = Image.new('RGB', (WIDTH, HEIGHT), WHITE)

    curLine = 0
    for release in reversed(releases):
        release['startLine'] = curLine
        curLine += getNLOC(release)
        release['endLine'] = curLine

    drawGrid(im, releases, matrix, 500, 500, min(WIDTH, HEIGHT) - 1000)

    drawLegend(im, WIDTH - 400, 500, 70, min(WIDTH, HEIGHT) - 1000)

    # draw.ellipse((100, 100, 150, 200), fill=(255, 0, 0), outline=(0, 0, 0))
    # draw.rectangle((200, 100, 300, 200), fill=(0, 192, 192), outline=(255, 255, 255))
    # draw.line((350, 200, 450, 100), fill=(255, 255, 0), width=10)

    # draw.text((10, 10), "Sample text", (255, 255, 255))

    im.save('matrix.jpg', quality=95)


def drawGrid(image, releases, matrix, sx, sy, size):
    assert isinstance(image, Image.Image)  # For IDE autocomplete
    draw = ImageDraw.Draw(image)
    totalLines = sum(getNLOC(release) for release in releases)
    scale = size / totalLines

    # Draw the colored squares
    for r1 in matrix.keys():
        for r2 in matrix[r1].keys():
            similarity = matrix[r1][r2]
            release1 = releases[r1]
            release2 = releases[r2]

            color = getColor(similarity)
            draw.rectangle((
                sx + release2['startLine'] * scale,
                sy + release1['startLine'] * scale,
                sx + release2['endLine'] * scale,
                sy + release1['endLine'] * scale
            ), fill=color)

    # Draw the labels
    for release in releases:
        tag = release['tag']
        pos = int((release['startLine'] + release['endLine']) / 2.0 * scale)
        drawText(image, (sx + pos, sy + size + 10), tag, 90)
        drawText(image, (sx - 40, sy + pos), tag, 0)

    # Draw the grid-lines
    draw.line((sx, sy, sx, sy + size), fill=BLACK, width=1)
    draw.line((sx, sy + size, sx + size, sy + size), fill=BLACK, width=1)
    for release in releases:
        x = sx + (release['endLine'] * scale)
        draw.line((x, sy, x, sy + size), fill=BLACK, width=1)
        y = sy + release['endLine'] * scale
        draw.line((sx, y, sx + size, y), fill=BLACK, width=1)


def drawLegend(image, sx, sy, width, height):
    draw = ImageDraw.Draw(image)
    draw.rectangle((sx, sy, sx + width, sy + height), outline=BLACK, width=1)
    for i in range(height):
        y = sy + height - i
        draw.rectangle((sx, y, sx + width, y - 1), fill=getColor(i / height))
    TEXTDIST = 10
    drawText(image, (sx + width + TEXTDIST, sy), "1.0", 0)
    drawText(image, (sx + width + TEXTDIST, int(sy + height / 2)), "0.5", 0)
    drawText(image, (sx + width + TEXTDIST, sy + height), "0.0", 0)


def drawText(image, pos, text, angle):
    assert isinstance(image, Image.Image)
    font = ImageFont.load_default()
    textImage = Image.new('L', font.getsize(text), color=255)
    textDraw = ImageDraw.Draw(textImage)
    textDraw.text((0, 0), text, font=font, fill=0)
    textImage = textImage.rotate(angle, expand=1)
    image.paste(textImage, pos)


def getColor(similarity):
    one = (255, 0, 0)
    half = (255, 255, 0)
    zero = (0, 255, 255)
    if similarity > 0.5:
        return interpolate(half, one, (similarity - 0.5) * 2)
    else:
        return interpolate(zero, half, similarity * 2)
    # return (int(255 * (1 - similarity)), 0, int(similarity * 255))


def interpolate(a, b, perc):
    return (
        int(b[0] * perc + a[0] * (1 - perc)),
        int(b[1] * perc + a[1] * (1 - perc)),
        int(b[2] * perc + a[2] * (1 - perc)),
    )


def getNLOC(release):
    return release['cloc']['header']['n_lines']
