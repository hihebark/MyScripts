#!/bin/bash

################################################################################
#                   Download all the torrent on website                        #
################################################################################
echo '~|~       _ ,_|-~|~|_ _ ,_  /|||'
echo ' | ()|`|`(/_|||_ | ||(/_|||/-|||'
echo
while getopts u: option; do
    case "${option}" in
        u) URL=${OPTARG};;
    esac
done

shift $((OPTIND -1))
BASENAME=$(echo $URL | cut -d'/' -f3,2,1)

function DownloadTorrent(){
    wget -c $1 -O $2 -q
}

function getLink(){
    curl -s $1 | grep "<td><i" | grep -Po '(?<=href=")[^"]*'
}

function getTorrent(){
    curl -s $1 | grep "Télécharger le Torrent" | grep -Po '(?<=href=")[^"]*'
}
if [ -z ${URL} ]
then 
    echo -e "[?] USAGE: ${0} -u URL"
    exit 0
fi
L=$(getLink $URL)
LINKS=(`echo $L | sed 's/\n/ /g'`)

for LINK in "${LINKS[@]}"; do
    FILENAME=$(basename $LINK)
    echo -e "[#] Downloading file from: ${FILENAME}"
    LINKTORRENT=$(getTorrent ${LINK})
    TORRENTFILE="$BASENAME$LINKTORRENT"
    DownloadTorrent $TORRENTFILE $FILENAME
done;
