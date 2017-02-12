import sys
import xbmcaddon
import xbmcgui
import xmbcplugin
 
addon       = xbmcaddon.Addon()
addonname   = addon.getAddonInfo('name')
 
#line1 = "Hello World!"
#line2 = "We can write anything we want here"
#line3 = "Using Python"
 
#xbmcgui.Dialog().ok(addonname, line1, line2, line3)

addon_handle = int(sys.argv[1])

xmbcplugin.setContent(addon_handle, 'tv')

url = 'blob:http://www.trt.net.tr/e5daf217-13db-044c-9caf-3692b33e4336'
li = xbmcgui.ListItem('TRT 1 HD', 'DefaultVidao.png')
xmbcplugin.addDirectoryItem(handle=addon_handle, url=url, listitem=li)
xmbcplugin.endOfDirectory(addon_handle)