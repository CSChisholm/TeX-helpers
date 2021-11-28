#Script to initialise a Git repository with a suitable .gitignore (Linux only)

import subprocess
import os as os
import glob as glob
import sys

try:
    directory = sys.argv[1] #The target directory can be parsed from the command line
except IndexError:
    directory = '' #A default directory can be specified here
if (len(directory)==0):
    directory = './' #Allow working in directory where this script is saved
if not(directory[-1]=='/'):
    directory+='/'
subprocess.run(['mkdir',directory]) #Make directory if it doesn't exist already
os.chdir(directory) #Change to specified directory

if not(os.path.exists('.git')):
    subprocess.run(['git','init'])
    #Create readme
    with open('ReadMe.md','w') as f:
        f.write('# '+directory.split('/')[-2])
        f.flush()
    #Write .gitignore
    gitignore = """
*.aux
*.out
*.log
*.synctex.gz
*.bbl
*.toc
*.blg
*.bib.bak
*.bib.sav
.~lock*
*.db
"""
    with open('.gitignore','w') as f:
        f.write(gitignore)
        f.flush()
    subprocess.run(['git','add','.gitignore','ReadMe.md'])
    subprocess.run(['git','commit','-m','Initial commit'])
    #Check if there are already .tex or .bib files here
    files = glob.glob('**/*.tex',recursive=True)+glob.glob(directory+'**/*.bib',recursive=True)
    if (len(files)>0):
        adder = ['git','add']
        adder.extend(files)
        subprocess.run(adder)
        subprocess.run(['git','commit','-m','Added exisitng .tex and .bib files'])
    #Add .pdf files with same name as .tex files to .gitignore
    addToGitignore = [file.replace('.tex','.pdf') for file in files if '.tex' in file]
    with open('.gitignore','a') as f:
        f.writelines(addToGitignore)
        f.flush()
else:
    #Don't do anything because there is already a git repository here
    print('Git repository already exists')
