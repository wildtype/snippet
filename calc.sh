#!/bin/sh
echo $* | bc -l -q | xmessage -file -

