import re, string, datetime
from PMS import *
from PMS.Objects import *
from PMS.Shortcuts import *

TheWB_PLUGIN_PREFIX   = "/video/TheWB"

TheWB_ROOT            = "http://www.thewb.com"
TheWB_SHOWS_LIST      = "http://www.thewb.com/shows/full-episodes"
EP_URL             = "http://www.thewb.com/shows/full-episodes"

####################################################################################################
def Start():
  Plugin.AddPrefixHandler(TheWB_PLUGIN_PREFIX, MainMenu, "The WB", "icon-default.jpg", "art-default.jpg")
  Plugin.AddViewGroup("Details", viewMode="InfoList", mediaType="items")
  MediaContainer.art = R('art-default.jpg')
  MediaContainer.title1 = 'TVLand Full Episodes'
  DirectoryItem.thumb=R("icon-default.jpg")
  WebVideoItem.thumb=R("icon-default.jpg")
  
####################################################################################################
#def MainMenu():
#    dir = MediaContainer(mediaType='video')
#    dir.Append(Function(DirectoryItem(allshows, "Full Episodes"), pageUrl = TheWB_SHOWS_LIST))
#    
#    return dir

####################################################################################################
def MainMenu():
    dir = MediaContainer(mediaType='video')
#    dir = MediaContainer()
    pageUrl=TheWB_SHOWS_LIST
    content = XML.ElementFromURL(pageUrl, True)
    for item in content.xpath('//div[@id="show-directory"]//div/div/ul/li'):
    	
        
        link = TheWB_ROOT + item.xpath("a")[0].get('href')
        Log(link)
        title = item.xpath("a")[0].text
        Log(title)
        dir.Append(Function(DirectoryItem(eplist, title=title), pageUrl=link))
    return dir
	
####################################################################################################
def eplist(sender, pageUrl):
    dir = MediaContainer(title2=sender.itemTitle)
    content = XML.ElementFromURL(pageUrl, isHTML=True)
    for item in content.xpath('//li[@id="full_ep_car1"]//div/div[@class="overlay_thumb_area"]'):
        Log(item)
        link =item.xpath("a")[0].get('href')
        link=str(TheWB_ROOT) + str(link)
        thumb = item.xpath("a/img")[0].get('src') 
        Log(thumb)
        title=item.xpath("a/img")[0].get('alt')
        Log(title)
        content2 = XML.ElementFromURL(link, isHTML="TRUE")
        for item2 in content2.xpath('//meta[@property="og:image"]'):
            link2 = item2.xpath('//link[@rel="video_src"]')[0].get('href')
        Log(link2)

        dir.Append(WebVideoItem(url=link, title=title))
    return dir

