#!/bin/bash
#echo -e '\t\t\e[92m[+]Updating Debian\e[0m\n'

#apt-get update && apt-get upgrade
#sleep .5s
echo -e '\t\t\e[92m[+]Updating gem\e[0m\n'
#sudo gem update
#sleep .5s
echo -e '\t\t\e[92m[+]Updating repository of the script file\e[0m\n'
locate -b '\.git' | sed -e 's/.git//g' > $HOME/listgit.txt
_listgit="$HOME/listgit.txt"
echo "$(tail -n +2 ${_listgit})" > "${_listgit}"
while IFS= read -r _file
	do
	cd ${_file}
	echo -e "\t[I]Updating > \e[92m${PWD##*/}\e[0m"
	git pull origin master
	sleep 1s
done <"${_listgit}"
rm -f ${_listgit}
