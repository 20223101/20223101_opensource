#!/bin/sh

case "$2" in
	+)
		echo $1 $2 $3
		echo `expr $1 + $3`;;
	-)
		echo $1 $2 $3
		echo `expr $1 - $3`;;
esac

exit 0
