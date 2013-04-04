RssRead
=======

    Version 0.3.1
     - Added output format sintax regex
     - Added config file validity check
    Version 0.3
     - Removed DTD
     - External config file for news output
     - Code cleaning and more python syntax
    Version 0.2
     - Refactoring Python Style and more simple API
    Version 0.11
     - Using C implementation of Xml parser
     - Extern DTD for the xml config file
    Version 0.1
     - Initial use of Python class

Repo for RssRead, an experimental API for reading RSS wich offers a good way as a part of a GUI program
or as a base for a personal script. 
[Python modules feedparser and minixsv are *required*.]

It's a module you can use with a 

    import RssRead as feed
    
    
and then use the News property to get the news

    rss = feed.RssRead() 
    
    try:
        rss.loadNewsRss(NAME)
    except feed.SiteError:
        print('Site not present!')
    except (feed.FormatError, KeyError):
        print('Format invalid')


In NAME you can use any of the configured* site.

You can, of course, use multiple RssReader on the same program or you can load more news with the same instance (using each time loadNewsRss())
Use the News object bearing in mind that it's, by default**, in a Xthml Link format.

I also added a class of validity check for the config file. 

    import RssConfValidate as validate

    tst = validate.RssConfValidate()
    print(tst.Valid)
    
The property Valid will be True if the config is valid or False otherwise.

*You can easly add/remove sites using the following syntax

    try:
        rss += 'site', 'url'
    except (TypeError, feed.SiteError):
        print('Already present')
    try:
        rss -= 'site'
    except (TypeError, feed.SiteError):
        print('Not present')
    
**You can also coustomize the way news are outputed in the file changind the standard

    '<a href="%(site)s">%(title)s</a><br />'

Enjoy :)
