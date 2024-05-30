#!/bin/bash
cat src/popular-names.txt | sed 's/\t/ /g' | cut -f 2 -d " "