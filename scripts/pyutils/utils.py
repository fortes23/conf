# -*- coding: utf-8 -*-

def style(name, element):
    formats = {
        'warning': '\033[92mWARNING: ',
        'error': '\033[1;31mERROR: ',
        'info': '\033[94mINFO: '
    }
    fmt = formats.get(name)
    reset_fmt = '\033[0m'
    return "{}{}{}".format(fmt, element, reset_fmt)
