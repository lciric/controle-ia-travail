P = [("""cat "$R/passage-6.out"
git -C "$R/distant.git" branch -a | grep -F "calcul/p4-jouet-s-v1" | sed 's/^/branche distante : /'
""", """cat "$R/passage-6.out"
""")]
