#!bin/bash
# cat ./out/result45.txt | sort | uniq -c | sort -nr
cat ./out/result45.txt | grep '行う' | sort | uniq -c | sort -nr