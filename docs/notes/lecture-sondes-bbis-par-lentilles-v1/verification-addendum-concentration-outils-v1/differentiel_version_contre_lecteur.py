"""Contre-lecteur Opus 5.5 : applique au brouillon 1 de l'addendum les huit couples du § 9 de la contre-lecture (715ddfa7…), extraits
par programme, puis compare le résultat à la version corrigée. Tout ce qui reste au différentiel est hors des couples.
Usage : python -B differentiel_version_contre_lecteur.py RAPPORT_CONTRE_LECTURE BROUILLON1 VERSION SORTIE_DIFF"""
import difflib
import re
import sys

rapport, b1, v = (open(p, encoding='utf-8').read() for p in sys.argv[1:4])
sec = rapport.split('## 9. Couples exacts')[1].split('## 10.')[0]
parts = re.split(r'\n\*\*([CF]\d)\*\* ', sec)
couples = {parts[i]: re.findall(r'```\n(.*?)\n```', parts[i + 1], flags=re.S) for i in range(1, len(parts), 2)}
t = b1
for nom, (avant, apres) in couples.items():
    assert t.count(avant) == 1, nom
    t = t.replace(avant, apres)
    print(f"{nom} : avant trouvé une fois dans le brouillon 1 ; après présent {v.count(apres)} fois dans la version")
d = list(difflib.unified_diff(t.splitlines(), v.splitlines(), 'brouillon1 + couples', 'version', n=0, lineterm=''))
open(sys.argv[4], 'w', encoding='utf-8').write('\n'.join(d) + '\n')
print(f"différentiel restant : {len(d)} lignes ; blocs : " + " ".join(l for l in d if l.startswith('@@')))
