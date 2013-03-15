RssRead
=======

Repo for RssRead, an experimental rss reader. 
It's a module you can use with a 

    import RssRead as feed

and then

    rss = feed.RssRead() 
    rss.loadConf()
    rss.loadNewsRss(NAME)
        for news in rss.getNews(NAME):
            pass
 
In NAME you can use any of the configured site.
Use the news object bearing in mind that it's already in a xthml link format.

And you can add/remove sites with the addSite()/removeSite() methods


Enjoy :)
