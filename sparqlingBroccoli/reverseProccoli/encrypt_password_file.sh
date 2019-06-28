for a in $(cat $1) ; do printf "$(echo $a | cut -d: -f1):$(openssl passwd -crypt $(echo $a | cut -d: -f2))\n"; done

