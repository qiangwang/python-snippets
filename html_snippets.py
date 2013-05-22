# -*- coding: utf-8 -*-

from HTMLParser import HTMLParser

import bleach

def strip_tags(html):
    '''
    Get an html string and return a text string without html tags
    '''

    class MLStripper(HTMLParser):
        def __init__(self):
            self.reset()
            self.fed = []
    
        def handle_data(self, d):
            self.fed.append(d)
        
        def get_data(self):
            return ''.join(self.fed)

    s = MLStripper()
    s.feed(html)
    return s.get_data()

def extract_img_src(html):
    '''
    Get an html string and return a list of img src attr
    '''

    class IMGExtractor(HTMLParser):
        def __init__(self):
            self.reset()
            self.fed = []
    
        def handle_starttag(self, tag, attrs):
            if tag == 'img':
                for attr in attrs:
                    if attr[0] == 'src' and attr[1]:
                        self.fed.append(attr[1])
                        break
    
        def get_data(self):
            return self.fed

    e = IMGExtractor()
    e.feed(html)
    return e.get_data()

def secure_html(html):
    '''
    Get an html string and return an html string without unallowed tags and attrs
    '''
    tags = ['strong', 'em', 'b', 'i', 'u', 'span', 'br', 'p', 'div', 'ul', 'ol', 'li', 'h1', 'h2', 'h3', 'blockquote', 'img', 'a']
    attributes = {
            'a': ['href', 'class'],
            'img': ['src', 'alt', 'width', 'height']
            }
    html = bleach.clean(html, tags=tags, attributes=attributes)

    html = bleach.linkify(html, callbacks=[bleach.callbacks.nofollow, bleach.callbacks.target_blank])

    return html

if __name__ == '__main__':
    print strip_tags('<div>no tags</div>')
    print extract_img_src('<img src="/about" href="#"><img src="" href="#">')
    print secure_html('<script>alert("hacker")</script><a>hello</a>')
