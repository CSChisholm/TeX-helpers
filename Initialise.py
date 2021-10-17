#Script to initialise a Git repository with a suitable .gitignore (Linux only)

import subprocess
import os as os
import glob as glob

directory = ''

if not(os.path.exists(directory+'.git')):
    subprocess.run(['mkdir',directory])
    os.chdir(directory)
    subprocess.run(['git','init'])
    with open(directory+'ReadMe.md','w') as f:
        f.write('# '+directory.split('/')[-2])
        f.flush()
    gitignore = """
    *.aux
    *.out
    *.log
    *.synctex.gz
    *.pdf
    *.bbl
    *.toc
    *.blg
    *.bib.bak
    *.bib.sav
    .~lock*
    *.db
    """
    with open(directory+'/.gitignore','w') as f:
        f.write(gitignore)
        f.flush()
    #subprocess.run(['mv',directory+'gitignore.txt','.gitignore'])
    subprocess.run(['git','add','.gitignore','ReadMe.md'])
    subprocess.run(['git','commit','-m','Initial commit'])
    #Check if there are already .tex or .bib files here
    files = glob.glob(directory+'*.tex')+glob.glob(directory+'*.bib')
    if (len(files)>0):
        adder = ['git','add']
        adder.extend(files)
        subprocess.run(adder)
        subprocess.run(['git','commit','-m','Added exisitng .tex and .bib files'])
else:
    print('Git repository already exists')
