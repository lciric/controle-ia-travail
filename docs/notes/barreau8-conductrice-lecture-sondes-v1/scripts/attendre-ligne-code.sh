#!/usr/bin/env bash
cd /home/user/controle-ia-travail
until git fetch -q origin main 2>/dev/null && git show origin/main:registres/sondes-iib-v1.md 2>/dev/null | grep -q '^| CODE-LECTURE-SONDES-IIB |'; do sleep 60; done
echo "LIGNE CODE-LECTURE-SONDES-IIB INSCRITE SUR origin/main à $(date -u +%H:%M:%SZ) :"
git show origin/main:registres/sondes-iib-v1.md | grep '^| CODE-LECTURE-SONDES-IIB |'
