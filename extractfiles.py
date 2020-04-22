from zipfile import ZipFile
import re, sys, os
os.chdir('D:\My Documents\School\CS 3270\ProjectF')
if __name__ == '__main__':
    args = sys.argv
    zipFile = args[1]
    regex = args[2]
# zipFile = 'cpp.zip'
# regex = '[Cs].*'
#probably use re.findall(regex, )

directories = []
onlyfiles = []
extensions = []

with ZipFile(zipFile, 'r') as myzip:
    stufflist = myzip.namelist()
    for item in stufflist:
        temp = item.split('/')
        fname = temp[-1]
        check = list(fname)
        ftemp = fname.split('.')
        ext = ftemp[-1]
        temp2 = temp[0:len(temp)-1]
        path = '/'.join(temp2)
        extensions.append(ext)
        onlyfiles.append(fname)
        directories.append(path)
    pattern = re.compile(regex)
    indexes = []
    #print(onlyfiles)
    for i in range(len(onlyfiles)):
        m = re.match(regex, onlyfiles[i])
        if m:
            #print(m.group())
            indexes.append(i)
    count = 0
    for index in indexes:
        count = count + 1
        myzip.extract(directories[index] + '/' + onlyfiles[index], 'test/')
print(f"{count} files extracted")