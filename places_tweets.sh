#!/bin/bash


function tweets {
    for month in 03 04 05
		do zless /net/corpora/twitter2/Tweets/2021/$month/*.out.gz | \
        /net/corpora/twitter2/tools/tweet2tab -i place text | \
		egrep -v '^\s+'
    done
}


tweets > place_tweets_2021.txt
echo done
