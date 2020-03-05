from PIL import Image, ImageDraw


def visualize(matrix, releases):
    print("Visualizing matrix")

    WIDTH = 5000
    HEIGHT = 5000

    im = Image.new('RGB', (WIDTH, HEIGHT), (255, 255, 255))
    draw = ImageDraw.Draw(im)

    curLine = 0
    for release in reversed(releases):
        release['startLine'] = curLine
        curLine += getNLOC(release)
        release['endLine'] = curLine

    drawGrid(draw, releases, matrix, 500, 500, min(WIDTH, HEIGHT) - 1000)

    # draw.ellipse((100, 100, 150, 200), fill=(255, 0, 0), outline=(0, 0, 0))
    # draw.rectangle((200, 100, 300, 200), fill=(0, 192, 192), outline=(255, 255, 255))
    # draw.line((350, 200, 450, 100), fill=(255, 255, 0), width=10)

    # draw.text((10, 10), "Sample text", (255, 255, 255))

    im.save('matrix.jpg', quality=95)


def drawGrid(draw, releases, matrix, sx, sy, size):
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
                sx + release1['startLine'] * scale,
                sy + size - release2['startLine'] * scale,
                sx + release1['endLine'] * scale,
                sy + size - release2['endLine'] * scale
            ), fill=color)

    # Draw the gridlines
    draw.line((sx, sy, sx, sy + size), fill=(0, 0, 0), width=1)
    draw.line((sx, sy + size, sx + size, sy + size), fill=(0, 0, 0), width=1)
    for release in releases:
        x = sx + (release['endLine'] * scale)
        draw.line((x, sy, x, sy + size), fill=(0, 0, 0), width=1)
        y = sy + size - (release['endLine'] * scale)
        draw.line((sx, y, sx + size, y), fill=(0, 0, 0), width=1)


def getColor(similarity):
    return (int(255 * (1 - similarity)), 0, int(similarity * 255))


def getNLOC(release):
    return release['cloc']['header']['n_lines']
