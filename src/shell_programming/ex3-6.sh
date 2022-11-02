#!/bin/sh

mkdir $1
cd $1

for i in 1 2 3 4 5
do
	touch file$i.txt
done

cd ../
tar cvf $1.tar $1

mkdir new_folder

tar xvf $1.tar -C /home/jxxeongg/바탕화면/opensource/new_folder
