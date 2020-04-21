import sys, sqlite3, os.path
from os import listdir, walk
from os.path import isfile, join
from zipfile import ZipFile

if __name__ == '__main__':
    args = sys.argv

def result(query):
    with open('files-part1.txt', 'a') as output:
        res = cur.execute(query)
        # for fieldinfo in res.description:
        #     output.write(fieldinfo[0])
        for row in res:
            output.write(str(row) + '\n')
    #print (res.description)
directory = args[1]
print(directory)
#directory = f"ProjectF\Stuff"

with ZipFile(str(directory) + '.zip', 'r') as zipObj:
    stufflist = zipObj.namelist()

directories = []
onlyfiles = []
extensions = []
cwd = os.getcwd()
tempdir = cwd.split('\\')
currentdir = '/'.join(tempdir)
for item in stufflist:
    temp = item.split('/')
    fname = temp[-1]
    ftemp = fname.split('.')
    if len(ftemp) >= 2:
        ext = ftemp[-1]
    else:
        ext = 'None'
    #print(full, item)
    temp2 = temp[0:len(temp)-1]
    path = currentdir + '/' + '/'.join(temp2)
    extensions.append(ext)
    onlyfiles.append(fname)
    directories.append(path)
    #print(path)
#print(onlyfiles[-7], 'and ', directories[-7], 'and ', extensions[-7])

if os.path.exists('filesdb'):
    os.remove('filesdb')

conn = sqlite3.connect('filesdb')
cur = conn.cursor()
cur.execute("create table files (ext, path, fname)")
for i in range(len(onlyfiles) - 1):
    statement = "insert into files values(?, ?, ?)"
    cur.execute(statement, (extensions[i], directories[i], onlyfiles[i]))
results = result('select * from files')