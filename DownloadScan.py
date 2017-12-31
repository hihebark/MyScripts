#!/usr/bin/python
# -*- coding: utf-8 -*-

#Copyleft 2017 Hihebark
#This program is free software: you can redistribute it and/or modify
#it under the terms of the GNU General Public License as published by
#the Free Software Foundation, either version 3 of the License, or
#( CopyLeft License ) any later version.

#This program is distributed in the hope that it will be useful,
#but WITHOUT ANY WARRANTY; without even the implied warranty of
#MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#GNU General Public License for more details.

#You should have received a copy of the GNU General Public License
#along with this program.  If not, see <http://www.gnu.org/licenses/>.

import requests
import os
from bs4 import BeautifulSoup
import time

def getImage():
    pass

def downloadSource(URL):
    sourcecode = requests.get(url=URL, timeout=(3,7))
    return sourcecode

def main():

    URL="http://www.mangahere.cc/manga/abara/c001/"
    soup = BeautifulSoup(downloadSource(URL).content, 'html5lib')
    srcImage = soup.find('img', id="image")["src"]
    ##print srcImage
    os.system("cd ~/Scripts/Scan/Abara1/ && wget -c -nv '{:s}'".format(srcImage))
    for i in range(2, 41):
        #print URL+str(i)+".html"
        soup = BeautifulSoup(downloadSource(URL+str(i)+".html").content, 'html5lib')
        srcImage = soup.find('img', id="image")["src"]
        print "cd ~/Scripts/Scan/Abara1/ && wget -c '{:s}'".format(srcImage)
        os.system("cd ~/Scripts/Scan/Abara1/ && wget -c -nv '{:s}'".format(srcImage))


if __name__ == '__main__':
    main()





















