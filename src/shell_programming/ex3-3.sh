#!/bin/sh

INT=$(($1))
INT=$(($2))
a=$(($2 * $2))
BMI=$(($1 / $a))

if [ $BMI -gt 23  ]
then
	echo "과체중입니다"
elif [ $BMI -lt 18 ] 
then
	echo "저체중입니다"
else
	echo "정상체중입니다"
fi
