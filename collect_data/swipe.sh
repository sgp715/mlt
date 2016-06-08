#!/bin/bash

echo ""
my_pwd="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"/

files="users/*"
for f in $files
do


    echo ""
    echo ""
    # parsing the name to get the user
    IFS='/' read -a path <<< "$f"
    f_name=${path[1]}
    IFS='.' read -a b_name <<< "$f_name"
    u=${b_name[0]}
    echo "*********************"
    echo "user: "$u
    echo "*********************"
    echo ""
    
    identification=$(sed '1q;d' $f)
    user=$(sed '2q;d' $f)
    pass=$(sed '3q;d' $f)

    authentication=$(casperjs $my_pwd'update_token.js' $user $pass)
    
    python $my_pwd'swipe.py' $identification $authentication $my_pwd $u
    
    echo ""
    echo "*********************"
    dt=$(date)
    echo $dt 
    echo "*********************"
    echo ""
    echo ""
    
done
