import xbmc
import xbmcaddon

ADDON = xbmcaddon.Addon()
ADDONID = ADDON.getAddonInfo('id')
CWD = ADDON.getAddonInfo('path')
ADDONVERSION = ADDON.getAddonInfo('version')

if __name__ == '__main__':
    xbmc.log("%s: Addon version %s started" % (ADDONID, ADDONVERSION), level=xbmc.LOGDEBUG)
    from lib import gui
    screensaver_gui = gui.Screensaver('script-python-slideshow.xml', CWD, 'default')
    screensaver_gui.doModal()
    del screensaver_gui
xbmc.log("%s: Addon stopped" % ADDONID, level=xbmc.LOGDEBUG)
