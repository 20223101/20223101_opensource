#!/bin/sh

mkdir $1
cd $1

for i in 1 2 3 4 5
do
	mkdir file$i
	touch file$i.txt
	ln -s /home/jxxeongg/바탕화면/opensource/$1/file$i.txt /home/jxxeongg/바탕화면/opensource/$1/file$i/
done
