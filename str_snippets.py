# -*- coding: utf-8 -*-

from datetime import datetime
from os.path import splitext

def unistr(ori_str, ignore=True, alt_str=False):
    '''
    Get a string and return an unicode string
    '''
    if isinstance(ori_str, unicode):
        return ori_str

    for encoding in ['utf-8', 'GB18030', 'BIG5']:
        try:
            return ori_str.decode(encoding)
        except:
            pass

    if ignore:
        return ori_str.decode('ascii', 'ignore')
    else:
        return alt_str

def filesize(size):
    '''
    Get an int and return a pretty string like '12 Bytes', '32 KB'
    '''
    for x in ['Bytes', 'KB', 'MB', 'GB']:
        if size < 1024.0 and size > -1024.0:
            return "%3.1f %s" % (size, x)
        size /= 1024.0
    return "%3.1f %s" % (size, 'TB')

def filetype(file_name):
        return splitext(file_name)[1][1:].lower()

def pretty_date(time=False):
    '''
    Get a datetime object or a int() Epoch timestamp and return a
    pretty string like 'an hour ago', 'Yesterday', '3 months ago',
    'just now', etc
    '''
    now = datetime.now()
    if type(time) is int:
        diff = now - datetime.fromtimestamp(time)
    elif isinstance(time, datetime):
        diff = now - time
    elif not time:
        diff = now - now
    second_diff = diff.seconds
    day_diff = diff.days

    if day_diff < 0:
        return ''

    if day_diff == 0:
        if second_diff < 60:
            return 'just now'
        if second_diff < 120:
            return  'a minute ago'
        if second_diff < 3600:
            return str( second_diff / 60 ) + ' minutes ago'
        if second_diff < 7200:
            return 'an hour ago'
        if second_diff < 86400:
            return str( second_diff / 3600 ) + ' hours ago'
    if day_diff == 1:
        return 'Yesterday'
    if day_diff < 7:
        return str(day_diff) + u' days ago'
    if day_diff < 31:
        return str(day_diff/7) + u' weeks ago'
    if day_diff < 365:
        return str(day_diff/30) + u' months ago'
    return str(day_diff/365) + u' years ago'

def age(birthday=False):
    '''
    Get a datetime object or a int() Epoch timestamp and return a
    pretty string like '1 hour', '1 day', '3 months',
    'just now', etc
    '''
    now = datetime.now()
    if type(birthday) is int:
        diff = now - datetime.fromtimestamp(birthday)
    elif isinstance(birthday, datetime):
        diff = now - birthday
    elif not birthday:
        diff = now - now
    second_diff = diff.seconds
    day_diff = diff.days

    if day_diff < 0:
        return ''

    if day_diff == 0:
        if second_diff < 60:
            return 'just now'
        if second_diff < 120:
            return  '1 minute'
        if second_diff < 3600:
            return str( second_diff / 60 ) + ' minutes'
        if second_diff < 7200:
            return '1 hour'
        if second_diff < 86400:
            return str( second_diff / 3600 ) + ' hours'
    if day_diff == 1:
        return '1 day'
    if day_diff < 7:
        return str(day_diff) + ' days'
    if day_diff < 31:
        return str(day_diff/7) + ' weeks'
    if day_diff < 365:
        return str(day_diff/30) + u' months'
    return str(day_diff/365) + u' years'

def nl2br(s, max_line_count=None):
    lines = s.splitlines()
    if max_line_count:
        lines = lines[0:max_line_count]
    return '<br>'.join(lines)

if __name__ == '__main__':
    print unistr(u'1去23里，烟村45家'.encode('gb2312'))
    print filesize(1000 * 1000) 
    print filetype('hello.py') 
    print pretty_date(datetime(2000, 1, 1)) 
    print age(datetime(2000, 1, 1)) 
    print nl2br(u'亭台67座\n8910枝花\n', 2)
