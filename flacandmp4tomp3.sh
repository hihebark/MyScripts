  
#!/bin/bash
clear

printf "(f)lac or (m)4a\n"
read formato

if ( [ $formato == 'f' ] || [ $formato == 'F' ] ); then
    for a in ./*.flac; do
        echo "Convirtiendo $a..."
        ffmpeg -i "$a" -qscale:a 0 "${a[@]/%flac/mp3}"
    done
elif ( [ $formato == 'm' ] || [ $formato == 'M' ] ); then
    for a in ./*.m4a; do
        ffmpeg -i "$a" -acodec libmp3lame -ab 320k "${a%.*}.mp3"
    done
else
    echo "Error"
fi
 
