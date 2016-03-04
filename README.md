RssRead [![Build Status](https://travis-ci.org/Flukas88/RssRead.svg?branch=master)](https://travis-ci.org/Flukas88/RssRead)
=======

    Version 0.3.3
     - Added unit tests
     - Added travis support 
     - Added internal representation as JSON
    Version 0.3.2
     - Added timestamps 
     - Moved to lxml for xml validation
     - Added compatibility for Python 3.4
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

Repo for RssRead, an experimental Python API for reading RSS which offers a good codebase for a GUI program
or as an integration for a personal script. 
[Python modules feedparser and lxml are *required*.]

It's a module you can use with a 

    import RssRead as feed
    
    
and then use the News property to get the news

    
        rss = feed.RssRead()
        rss.load(NAME)
        print(rss.News)

You could also print it as a *JSON* with a simple
    
        rss = feed.RssRead()
        rss.load(NAME)
        print(rss)

In NAME you can use any of the configured* site.

You can, of course, use multiple RssReader on the same program or you can load more news with the same instance (using each time the *load* function)
Use the News object bearing in mind that it's, by default**, in a Xthml Link format.

I also added a class of validity check for the config file. 
You can use *VerifyConf.py* to verify your configuration
    

*You can easly add/remove sites using the following syntax

    rss.addSite('NAME', 'URL')
    rss.removeSite('NAME')

**You can also customize the way news are outputed in the file, changing the standard

    <a href="%(site)s">%(title)s</a><br />
