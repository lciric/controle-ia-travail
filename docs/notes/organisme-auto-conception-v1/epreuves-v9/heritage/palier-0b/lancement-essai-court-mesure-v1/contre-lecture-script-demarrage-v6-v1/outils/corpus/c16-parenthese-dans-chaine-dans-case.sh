#!/bin/bash
y=a
x=$(case $y in
a) echo ')' ;;
esac
# vrai commentaire
)
printf '%s|' "$x"
