#!/usr/bin/python

import MySQLdb

def get_plate(plate):
    # Open database connection
    db = MySQLdb.connect("localhost","root","","pagar" )

    # prepare a cursor object using cursor() method
    cursor = db.cursor()

    sql = "SELECT * FROM info \
            WHERE plat_nomor like '%s'" % ('%' + plate + '%')
    try:
       # Execute the SQL command
       cursor.execute(sql)
       # Fetch all the rows in a list of lists.
       results = cursor.fetchall()
       if(len(results)>0):
           for row in results:
              plat_nomor = row[1]
              # Now print fetched result
              print "Berhasil Masuk.\nPlat Nomor : %s" % \
                     (plat_nomor)
       else:
            print "Gagal Masuk"
    except:
       print "Error: unable to fecth data"

    # disconnect from server
    db.close()
if __name__ == "__main__":
    get_plate('123T')
