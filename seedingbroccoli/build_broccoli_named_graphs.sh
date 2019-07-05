
source secret.txt

node code_broccoli_put.js \
    http://icedbroccoli.5th.ch/broccoli#code

python succotash_broccoli_put.py \
    http://icedbroccoli.5th.ch/broccoli#succotash \
    https://raw.githubusercontent.com/koma5/succotash/master/data.ttl

python koma5_broccoli_put.py \
    http://icedbroccoli.5th.ch/broccoli#koma5

python dbpedia_broccoli_put.py \
    http://icedbroccoli.5th.ch/broccoli#dbpedia \
    http://icedbroccoli.5th.ch/broccoli/sparql
