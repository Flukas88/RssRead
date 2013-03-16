RssRead
=======

Repo for RssRead, an experimental rss reader. 
[Python module feedparser is required.]

It's a module you can use with a 

    import RssRead as feed

and then use the News peoperty to get the news

    rss = feed.RssRead() 
    rss.loadConf()
    rss.loadNewsRss(NAME)
        for news in rss.News:
            pass
 
In NAME you can use any of the configured site.
You can, of course, use multiple RssReader on the same program.
Use the news object bearing in mind that it's already in a xthml link format.

And you can add/remove sites you con use the following syntax

    rss = feed.RssRead()
    rss.loadConf()
    rss + ['sito', 'url']
    rss - 'sito'


Enjoy :)
