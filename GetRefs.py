#Script to get all labels in TeX project

import glob as glob

def ExtractLabelInfo(lineNum):
    info = {}
    line = allText[lineNum]
    try:
        info['Type'] = line.split('\label{')[1].split(':')[0]
        info['Key'] = line.split('\label{'+info['Type']+':')[1].split('}')[0]
        if (info['Type'] in ['fig','tab']):
            info['Caption'] = line.split('\label{'+info['Type']+':'+info['Key']+'}')[1].split('}')[0]
        elif (info['Type']=='sec'):
            try:
                sectionLine = allText[lineNum-1]
                info['Section'] = sectionLine.split('{')[1].split('}')[0]
                info['Section Type'] = sectionLine.split('\\')[1].split('{')[0]
            except IndexError:
                pass
    except IndexError:
        info = {}
        info['Label'] = line.split('\label{')[1].split('}')[0]
    info['File'] = fileMarkers[keysList[[II for II, key in enumerate(keysList) if key<lineNum][-1]]]
    return info

#Specify directory of project
directory = ''
if (len(directory)==0):
    directory = './'
if not(directory[-1]=='/'):
    directory+='/'
#Search for all .tex files in main directory and subdirectories
texFiles = glob.glob(directory+'**/*.tex',recursive=True)
#Get every line of text into one list with a dictionary marking
# indices of beginnings of files
allText = []
fileMarkers = {}
for texFile in texFiles:
    fileMarkers[len(allText)] = texFile.split(directory)[-1]
    with open(texFile,'r') as f:
        allText.extend(f.readlines())
keysList = list(fileMarkers.keys())
#Find all lines containg \label
labelLines = [II for II, line in enumerate(allText) if '\label' in line and not line[0]=='%']
#Extract label info
labels = [ExtractLabelInfo(labelLine) for labelLine in labelLines]
for label in labels:
    print(label)
    print('\n')
