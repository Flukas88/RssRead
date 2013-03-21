RssRead
=======

    Version 0.2
     - Refactoring Python Style and more simple API
    Version 0.11
     - Using C implementation of Xml parser
     - Extern DTD for the xml config file
    Version 0.1
     - Initial use of Python class

Repo for RssRead, an experimental API for reading RSS( and Atom) . 
[Python module feedparser is required.]

It's a module you can use with a 

    import RssRead as feed

and then use the News property to get the news

    rss = feed.RssRead() 
    
    try:
        rss.loadNewsRss(NAME)
    except feed.SiteError:
        print 'Site not present!'
        
    for news in rss.News:
        pass
 
In NAME you can use any of the configured* site.
You can, of course, use multiple RssReader on the same program.
Or you can load more news with the same istance (using each time loadNewsRss())
Use the News object bearing in mind that it's, by default**, in a Xthml Link format.



*You can add/remove sites you con use the following syntax

    try:
        rss += 'site', 'url'
    except (TypeError, feed.SiteError):
        print 'Already present'

    try:
        rss -= 'site'
    except (TypeError, feed.SiteError):
        print 'Not present'

**You can also coustomize the way news are outputed in the file changind the standard

    '<a href="%(site)s">%(title)s</a><br />'


Enjoy :)
