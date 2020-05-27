import sys, os
import xbmc, xbmcaddon

ADDON    = sys.modules[ '__main__' ].ADDON
ADDONID  = sys.modules[ '__main__' ].ADDONID
LANGUAGE = sys.modules[ '__main__' ].LANGUAGE


def log(txt):
    if isinstance (txt,str):
        txt = txt.decode('utf-8')
    message = u'%s: %s' % (ADDONID, txt)
    xbmc.log(msg=message.encode('utf-8'), level=xbmc.LOGDEBUG)
