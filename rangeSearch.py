import sqlite3 as sql
import uuid
import scipy.spatial

def hwRNG():
    i = 0
    while True:
        yield i, uuid.uuid4().int
        i = i + 1


# Initialise database
conn = sql.connect('RANGEsearch.db')
curs = conn.cursor()

# Create table if not already exists
sql = 'CREATE TABLE IF NOT EXISTS "tblPosition" (\
    "intNr"	INTEGER, \
	"fltLon"	REAL, \
	"fltLat"	REAL \
)'
curs.execute(sql)

# Truncate table
sql ='DELETE FROM tblPosition'
curs.execute(sql)
conn.commit()

nMax = 10_000_000
i = 0

# Datenbank fuellen
while i < nMax:
    lon = (uuid.uuid4().int / 2**128 * 360)
    lat = (uuid.uuid4().int / 2**128 * 360)
    sql = 'INSERT INTO tblPosition VALUES ' + str((i, lon, lat))
    curs.execute(sql)
    i = i + 1

conn.commit()
conn.close()

print('database closed')

i = 0
nMax = 10_000_000
data = []
kern = []
while i < nMax:
    lon = (uuid.uuid4().int / 2 ** 128 * 360)
    lat = (uuid.uuid4().int / 2 ** 128 * 360)
    data.append((i,lon,lat))
    kern.append((lon,lat))
    i = i +1


kTree = scipy.spatial.KDTree(kern)
sel = kTree.query_ball_point((0,0),1)

result = [data[_] for _ in sel]
