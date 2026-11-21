#!/bin/bash
# Plante un .git VIDE (init seul, tete non nee) dans la racine du cas : ESSAI_DEMARRAGE_BASE/racine
R=$ESSAI_DEMARRAGE_BASE/racine
/usr/bin/git init -q "$R" && echo "plante : .git vide dans $R"
