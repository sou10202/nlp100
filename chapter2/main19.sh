#!/bin/bash
cut -f 1 src/popular-names.txt | sort | uniq -c| sort -n