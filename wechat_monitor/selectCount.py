import mysql.connector

def statistics():
    print 'start select...loding...'
    coon=mysql.connector.connect(
        user='root',
        password='root',
        database='musicget')
    cursor=coon.cursor()
    cursor.execute('select count(*) from song')
    value=cursor.fetchone()
    cursor.close()
    coon.close()
    print value
    return value