import sys, sqlite3, os.path
from zipfile import ZipFile

if __name__ == '__main__':
    args = sys.argv

def result(query):
    with open('files-part1.txt', 'a') as output:
        res = cur.execute(query)
        for row in res:
            output.write(str(row) + '\n')
    #print (res.description)
directory = args[1]

with ZipFile(directory + '.zip', 'r') as zipObj:
    stufflist = zipObj.namelist()

directories = []
onlyfiles = []
extensions = []
for item in stufflist:
    temp = item.split('/')
    fname = temp[-1]
    check = list(fname)
    ftemp = fname.split('.')
    if fname.startswith('.') or fname.startswith('_'):
        continue
    elif len(ftemp) >= 2:
        ext = ftemp[-1]
    else:
        ext = 'None'
    #print(full, item)
    temp2 = temp[0:len(temp)-1]
    #path = currentdir + '/' + '/'.join(temp2)
    path = '\\'.join(temp2)
    extensions.append(ext)
    onlyfiles.append(fname)
    directories.append(path)
    #print(path)
#print(onlyfiles[-7], 'and ', directories[-7], 'and ', extensions[-7])

if os.path.exists('filesdb'):
    os.remove('filesdb')

conn = sqlite3.connect('filesdb')
cur = conn.cursor()
cur.execute("create table files (ext text, path text, fname text)")
for i in range(len(onlyfiles) - 1):
    statement = "insert into files values(?, ?, ?)"
    cur.execute(statement, (extensions[i], directories[i], onlyfiles[i]))
results = result('select * from files')
conn.commit()
conn.close()