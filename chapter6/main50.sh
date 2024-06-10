cat src/train.txt | cut -f 5 | sort | uniq -c | sort -nr
cat src/valid.txt | cut -f 5 | sort | uniq -c | sort -nr
cat src/test.txt | cut -f 5 | sort | uniq -c | sort -nr