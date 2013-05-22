# -*- coding: utf-8 -*-

import random
import Image, ImageDraw, ImageFont, ImageFilter  
 
def create_captcha(
        size=(120, 30),
        length=4,
        allowed_chars='0123456789',
        mode='RGB',
        bg_color=(255, 255, 255),
        color=(255, 0, 0),
        font_size=18,
        font_type='Monaco.ttf',
        has_points=True,
        point_chance=5):
    ''''' 
    size: captcha picture size, (width, height)
    length: num of chars in captcha
    allowed_chars: allowed chars in captcha
    mode: captcha picture mode 
    bg_color: background color of captcha
    color: color of captcha chars
    font_size: font size
    font_type: font type
    has_points: whether to draw points 
    point_chance: probability of occurrence of points ，range in [0, 50] 
    ''' 
 
    width, height = size
    img = Image.new(mode, size, bg_color)
    draw = ImageDraw.Draw(img)
 
    def draw_points():
        chance = min(50, max(0, point_chance))
        for w in xrange(width):  
            for h in xrange(height):  
                if random.randint(1, 100) <= chance:
                    draw.point((w, h), fill=(0, 0, 0))  
 
    def draw_chars():
        chars = ''.join(random.sample(allowed_chars, length))
 
        font = ImageFont.truetype(font_type, font_size)
        font_width, font_height = font.getsize(chars)  
 
        draw.text(((width - font_width) / 3, (height - font_height) / 4), chars, font=font, fill=color)  
 
        return chars
 
    if has_points:
        draw_points()

    chars = draw_chars()
 
    params = [
            1 - float(random.randint(1, 2)) / 100,  
            0,  
            0,  
            0,  
            1 - float(random.randint(1, 10)) / 100,  
            float(random.randint(1, 2)) / 500,  
            0.001,  
            float(random.randint(1, 2)) / 500
            ]  
    img = img.transform(size, Image.PERSPECTIVE, params).filter(ImageFilter.EDGE_ENHANCE_MORE)
 
    return chars, img

if __name__ == '__main__':  
    chars, img = create_captcha()
    img.save('/tmp/captcha.png', 'png', quality=70)  
    print chars
