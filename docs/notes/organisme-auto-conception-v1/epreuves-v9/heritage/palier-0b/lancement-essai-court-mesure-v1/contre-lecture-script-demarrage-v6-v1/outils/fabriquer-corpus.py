"""Fabrique le corpus de scripts inoffensifs (echo seulement) pour comparer sortie de l'original et du texte reduit.
Usage : python -I fabriquer-corpus.py DOSSIER"""
import os, sys
d = sys.argv[1]
C = {
"c01-chaine-simple": "#!/bin/bash\nx='a\n# dans la chaine\n\nb'\nprintf '%s|' \"$x\"\n",
"c02-chaine-double": "#!/bin/bash\nx=\"a\n# dans la chaine\n\nb\"\nprintf '%s|' \"$x\"\n",
"c03-heredoc": "#!/bin/bash\ncat <<'EOF'\n# dans le document\n\nfin\nEOF\n# vrai commentaire\necho ok\n",
"c04-heredoc-tab": "#!/bin/bash\nif true; then\n\tcat <<-EOF\n\t# dans le document\n\n\tfin\n\tEOF\nfi\n",
"c05-continuation": "#!/bin/bash\necho a \\\n# c\necho b\n",
"c06-continuation-vide": "#!/bin/bash\necho a \\\n\necho b\n",
"c07-case-dans-substitution-chaine": "#!/bin/bash\ny=a\nx=\"$(case $y in\na) echo \"q\n# pas un commentaire\nr\";; esac)\"\nprintf '%s|' \"$x\"\n",
"c08-case-dans-substitution-simple": "#!/bin/bash\ny=a\nx=$(case $y in\na) echo 'q\n# pas un commentaire\nr';; esac)\nprintf '%s|' \"$x\"\n",
"c09-ansi-c": "#!/bin/bash\nx=$'a\\'\n# dans la chaine ?\nb'\nprintf '%s|' \"$x\"\n",
"c10-decalage-arith": "#!/bin/bash\necho $((1<<2))\n# commentaire\necho fin\n",
"c11-hash-param": "#!/bin/bash\nv=abc\necho ${#v} ${v#a} $#\n# c\necho fin\n",
"c12-backtick-multi": "#!/bin/bash\nx=`echo 'a\n# dans la chaine\nb'`\nprintf '%s|' \"$x\"\n",
"c13-case-simple-parenthese": "#!/bin/bash\ny=a\nx=$(case $y in\n(a) echo 'q\n# pas un commentaire\nr';; esac)\nprintf '%s|' \"$x\"\n",
"c14-chaine-dans-expansion": "#!/bin/bash\nv=\nx=${v:-'a\n# dans la chaine\nb'}\nprintf '%s|' \"$x\"\n",
"c15-heredoc-dans-substitution": "#!/bin/bash\nx=$(cat <<EOF\n# dans le document\n\nz\nEOF\n)\nprintf '%s|' \"$x\"\n",
"c16-parenthese-dans-chaine-dans-case": "#!/bin/bash\ny=a\nx=$(case $y in\na) echo ')' ;;\nesac\n# vrai commentaire\n)\nprintf '%s|' \"$x\"\n",
"c17-case-dans-double-quote-parenthese-fermante": "#!/bin/bash\ny=a\nx=\"$(case $y in\na) echo hi;; esac\n# vrai commentaire\n)\"\necho \"$x\"\n",
"c18-sain": "#!/bin/bash\n# commentaire\n\necho un # fin de ligne\n\n# autre\necho deux\n",
"c19-chaine-puis-case-bis": "#!/bin/bash\ny=a\nx=\"$(case $y in\na) echo \"q\";; esac\necho 'r\n# dans la chaine\ns')\"\nprintf '%s|' \"$x\"\n",
}
for k, v in C.items():
    with open(os.path.join(d, k + ".sh"), "x", newline="") as f:
        f.write(v)
