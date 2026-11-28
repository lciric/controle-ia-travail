#!/bin/sh
case "$1" in
  *Username*|*username*) printf "%s\n" "x-access-token" ;;
  *) printf "%s\n" "$_MEM_GH_TOK" ;;
esac
