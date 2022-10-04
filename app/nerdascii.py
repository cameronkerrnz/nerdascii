import rembg
import cv2 as cv
import sys

def remove_background(input_filename, output_filename):
    with open(input_filename, 'rb') as i:
        with open(output_filename, 'wb') as o:
            input = i.read()
            output = rembg.remove(input)
            o.write(output)

def render_cells(rgba, hsv, gray, palette, method):
    # First entry in pallette is for the transparency (background)
    for y in range(rgba.shape[0]):
        for x in range(rgba.shape[1]):
            if rgba[y][x][3] == 0:
                yield(palette[0])
            else:
                if method == 'hue':
                    yield(palette[1 + hsv[y][x][0] // (256 // len(palette[1:]))])
                elif method == 'brightness':
                    yield(palette[gray[y][x] // (256 // len(palette[1:]))])
                else:
                    raise(f'Invalid method {method}')
        yield('\n')         

def render(rgba, hsv, gray, palette=[' ', '-', '+', '*', '#'], method='hue'):
    return ''.join(list(render_cells(rgba, hsv, gray, palette, method)))

palettes = {
    'ascii-few': [' ', '-', '+', '*', '#'],
    'ascii-several': list(" .,-!+?%$#"),
    'unicode-shade': list(" \u2591\u2592\u2593"),
    'unicode-colored-dots': ['⚫️', '🟡', '🟢', '🟣'],
    'unicode-chess': list(" ♗♟"),
    'debug': list(" 1234567890abcdefghijklmnopqrstuvwxyz"),
}

if __name__ == "__main__":
    input_filename = sys.argv[1]
    output_filename = sys.argv[2]
    palette_names = sys.argv[3:]

    bgremoved_filename = '/tmp/bgremoved.png'

    remove_background(input_filename, bgremoved_filename)

    bgremoved = cv.imread(bgremoved_filename, -1)

    target_x = 80
    target_y = 40

    small_image = cv.resize(bgremoved, (target_x, target_y))

    small_image_hsv = cv.cvtColor(small_image, cv.COLOR_BGR2HSV)
    small_image_gray = cv.cvtColor(small_image, cv.COLOR_BGR2GRAY)

    # cv.imwrite(input_filename + '.small.jpg', small_image)
    # cv.imwrite(input_filename + '.small-hsv.jpg', small_image_hsv)

    for spec in palette_names:
        (palette_name, method) = spec.split(':')
        rendered = render(small_image, small_image_hsv, small_image_gray,
            palette=palettes[palette_name], method=method)
        # print(rendered)

        with open(output_filename.replace('{palette}', palette_name).replace('{method}', method),
                'wt', encoding='UTF-8') as o:
            o.write(rendered)
    
