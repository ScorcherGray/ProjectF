import sys, sqlite3, os.path
from zipfile import ZipFile

if __name__ == '__main__':
    args = sys.argv
    dbname = args[1]
    extensions = args[2:]
#print(extensions)
conn = sqlite3.connect(dbname)
cur = conn.cursor()

for ext in extensions:
    count = 0
    with ZipFile(ext + '.zip', 'a') as myzip:
        res = cur.execute('select * from files where ext = ?', [ext])
        for row in res:
            count = count + 1
            #print(row[0], row[1], row[2])
            myzip.write(os.path.join(row[1], row[2]))
            #print(row[0])
    print(f"{count} {ext} files gathered")
conn.close()