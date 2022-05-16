import MySQLdb

def connection():
    conn = MySQLdb.connect(host="localhost",
                    user="root",
                    passwd="root",
                    db="seil_users")
    
    c = conn.cursor()

    return c, conn