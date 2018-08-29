#!/bin/bash

counter=0
mkdir PhrackIssues
cd PhrackIssues/
while [ $counter -lt 69 ]
do
	echo "\t\tDonwloading phrack >"$counter
   	wget -c http://phrack.org/archives/tgz/phrack$counter.tar.gz
  	$counter++
done
echo -e "\t\tDone!"
