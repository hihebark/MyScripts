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
import argparse
from bs4 import BeautifulSoup
import time

def getImage():
    pass

def downloadSource(URL):
    sourcecode = requests.get(url=URL)
    return sourcecode

def main():

    parser  = argparse.ArgumentParser(description="DownloadScan - download scan from http://www.mangahere.cc/")
    parser.add_argument('-link', '-l', help="Link to the scan", required=True)
    parser.add_argument('-nos', '-n', help="number of page", required=True)
    args        = parser.parse_args()
    link        = args.link
    numberpage  = int(args.nos)+1
    #URL="http://www.mangahere.cc/manga/abara/c001/"
    soup = BeautifulSoup(downloadSource(link).content, 'html5lib')
    srcimage = soup.find('img', id="image")["src"]
    ##print srcImage
    os.system("cd ~/Path/to/Scan/ && wget -c -nv '{0:s}' -O {1:s}.jpg".format(srcimage, '1'))
    for i in range(2, numberpage):
        #print URL+str(i)+".html"
        soup = BeautifulSoup(downloadSource(link+str(i)+".html").content, 'html5lib')
        srcimage = soup.find('img', id="image")["src"]
        os.system("cd ~/Path/to/Scan/ && wget -c -nv '{0:s}' -O {1:s}.jpg".format(srcimage, str(i)))


if __name__ == '__main__':
    main()





















