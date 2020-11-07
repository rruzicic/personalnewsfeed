import feedparser
import mysql.connector
from time import sleep
from datetime import datetime

# connection with database
# there is no need to add this to a diferent file because i am running the database and website locally
mydb = mysql.connector.connect( 
  host="localhost",
  user="root",
  password="",
  database="news"
)

# checking the connection with database
if(mydb):
    print("Connection succesful")
else:
    print("Connection unsuccesful")

mycursor = mydb.cursor()

# while loop is set to 1 so the program will keep running indefinitely
while (1):
    mycursor.execute("DELETE FROM articles") # this sql statement deletes the whole table
    mycursor.execute("ALTER TABLE articles AUTO_INCREMENT = 0") # setting the AUTO_INCREMENT value to 0
    rss_url_n1 = "http://rs.n1info.com/rss/249/Naslovna" # link of the first feed
    feed_n1 = feedparser.parse( rss_url_n1 )
    # code below basically goes through every article and saves its publisher, link, title, date, summary, (image column is left blank, that functionality will be added later)
    for post in feed_n1['entries']:
        sql = "INSERT INTO articles (id, agency, title, link, date, summary, image) VALUES (%s, %s, %s, %s, %s, %s, %s)"
        val = (0, "N1", post['title'], post['link'], post['published'], post['summary'], "")
        mycursor.execute(sql, val)
        mydb.commit()

    rss_url_novas = "http://nova.rs/rss"
    feed_novas = feedparser.parse( rss_url_novas )
    for post in feed_novas['entries']:
        sql = "INSERT INTO articles (id, agency, title, link, date, summary, image) VALUES (%s, %s, %s, %s, %s, %s, %s)"
        val = (0, "NovaS", post['title'], post['link'], post['published'][:-5], post['summary'], "")
        mycursor.execute(sql, val)
        mydb.commit()

    rss_url_talas = "http://talas.rs/rss"
    feed_talas = feedparser.parse( rss_url_talas )
    for post in feed_talas['entries']:
        sql = "INSERT INTO articles (id, agency, title, link, date, summary, image) VALUES (%s, %s, %s, %s, %s, %s, %s)"
        val = (0, "Talas", post['title'], post['link'], post['published'][:-5], "", "")
        mycursor.execute(sql, val)
        mydb.commit()
    now = datetime.now()
    current_time = now.strftime("%H:%M:%S")
    print("Last feed fetched: ", current_time)
    sleep(240) # program waits for 240s because there is no need to constantly check for new content 
