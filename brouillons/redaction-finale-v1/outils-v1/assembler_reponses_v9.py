"""v9 : assemblage v8, versions corrigées après les vérificateurs neufs. v8 (4 novembre 2026, nuit, instance fusionnée conv-audit et session-depot) : assemblage v7 pour Lazar, après son collage du formulaire
de 00:49 UTC (`reponses-pivotal-collees-par-lazar-2026-11-04-0049.txt`). Pour chaque question : la dernière version au dépôt, ce que Lazar
a collé (identique, autre version, ou ancienne réponse du formulaire de 12:09 UTC), le compte par blancs et au pire cas (`\\w+`), l'état de
vérification. Heimersheim Q1 : texte de Lazar tel quel (aucune phrase anglaise du directeur). Corps = texte au-dessus du premier trait.
Usage : assembler_reponses_v8.py SORTIE HEURE_UTC FICHIER_ETATS_JSON"""
import hashlib, json, os, re, sys
D = '/home/claude/controle-ia-travail/brouillons/redaction-finale-v1/'
def sha(p): return hashlib.sha256(open(D + p, 'rb').read()).hexdigest()
def corps(p, entier=False):
    t = open(D + p).read()
    return t.strip() if entier else t.split('\n---\n')[0].strip()
sortie, heure, etats = sys.argv[1:4]
E = json.load(open(etats))
L = ["# Réponses finales pour Pivotal — assemblage v8 (après les vérificateurs de la nuit du 4 novembre)", "",
     f"4 novembre 2026, {heure} UTC (`date -u`), instance fusionnée (conv-audit et session-depot). Remplace les assemblages v6 et v7 (la v7, intermédiaire, n'a pas été envoyée). "
     "Dans l'ordre du formulaire. **Ne colle que le texte entre les deux filets de chaque réponse.** "
     "« Collé à 00:49 » = ce que tu m'as envoyé à 00:49 UTC (`reponses-pivotal-collees-par-lazar-2026-11-04-0049.txt`).", ""]
for q in E['questions']:
    f = q['fichier']; c = corps(f, q.get('entier', False))
    blancs = len(c.split()); pire = len(re.findall(r'\w+', c))
    L += [f"## {q['titre']}", "", f"**Question** : « {q['question']} »", "",
          f"Fichier `{f}` (sha256 `{sha(f)[:16]}…`) ; **{blancs} mots** par blancs, {pire} au pire cas ; {q['limite']}", "",
          f"**Collé à 00:49** : {q['colle']}", "", f"**État** : {q['etat']}", "",
          "━━━━━━━━━━━━━━━━━━━━", "", c, "", "━━━━━━━━━━━━━━━━━━━━", ""]
assert not os.path.exists(sortie)
open(sortie, 'w').write('\n'.join(L) + '\n')
print(sortie, hashlib.sha256(open(sortie, 'rb').read()).hexdigest())
