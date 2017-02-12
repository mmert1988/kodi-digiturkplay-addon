import sys
#import xbmcaddon
import xbmcgui
import xmbcplugin
 
#addon       = xbmcaddon.Addon()
#addonname   = addon.getAddonInfo('name')
 
#line1 = "Hello World!"
#line2 = "We can write anything we want here"
#line3 = "Using Python"
 
#xbmcgui.Dialog().ok(addonname, line1, line2, line3)

addon_handle = int(sys.argv[1])

xmbcplugin.setContent(addon_handle, 'movies')

url = 'http://www.vidsplay.com/vids/traffic_arrows.mp4'
li = xbmcgui.ListItem(label='Traffic arrows', iconImage='DefaultVidao.png')
xmbcplugin.addDirectoryItem(handle=addon_handle, url=url, listitem=li)
xmbcplugin.endOfDirectory(addon_handle)