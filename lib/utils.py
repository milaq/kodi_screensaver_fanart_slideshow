import xbmc
import xbmcaddon

ADDON = xbmcaddon.Addon()
ADDONID = ADDON.getAddonInfo('id')
LANGUAGE = ADDON.getLocalizedString


def log(txt):
    message = '%s: %s' % (ADDONID, txt)
    xbmc.log(msg=message, level=xbmc.LOGDEBUG)
