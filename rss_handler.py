import feedparser 

rss_url_n1 = "http://rs.n1info.com/rss/249/Naslovna"
feed_n1 = feedparser.parse( rss_url_n1 )
for post in feed_n1['entries']:
    print( post['title'])
    print( post['link'])
    print( post['published'])
    print( post['summary'])
    print( "-------------------------------")

rss_url_novas = "http://nova.rs/rss"
feed_novas = feedparser.parse( rss_url_novas )
for post in feed_novas['entries']:
    print( post['title'])
    print( post['link'])
    print( post['published'])
    print( post['summary'])
    print( "-------------------------------")

rss_url_talas = "http://talas.rs/rss"
feed_talas = feedparser.parse( rss_url_talas )
for post in feed_talas['entries']:
    print( post['title'])
    print( post['link'])
    print( post['published'])
    print( "-------------------------------")