# Pièces de travail du rédacteur des devis de carte du bras A (Claude Opus 5.5) — index v1

Versées le 2026-11-23 sur la demande de la session mère (mot de Lazar, GO-2026-11-23-09 : reprise possible sur un autre compte, sans perte). Ce sont les programmes, brouillons et essais restés dans le bloc-notes de la session ; rien n'y est secret, aucun modèle extérieur n'a été consulté (aucune réponse de modèle à verser). Les devis eux-mêmes sont déjà versés, un fichier par version, dans le dossier parent.

| fichier | ce que c'est |
|---|---|
| `calculs-devis-v3-essai.py` | premier programme de calcul du devis de carte v3, écrit avant la dernière mise au point ; garde une sortie un peu plus riche |
| `calculs-devis-v3.py` | programme recopié à la section 13 du devis v3 (rejoué : sortie identique à celle de la pièce) |
| `calculs-devis-v4.py` | le précédent, corrigé de la remarque m2 de la contre-lecture (retrait de la prise pour le témoin bénin) ; recopié au devis v4 |
| `calculs-moniteurs-v1-essai1.py` | premier programme du devis des moniteurs, avant les réponses du lecteur habilité (lecture commune bornée à 4 h) ; **reconstitué** le 2026-11-23 depuis le journal de la session (sortie vérifiée identique à celle du 22 novembre vers 22:33Z), l'original ayant été écrasé |
| `calculs-moniteurs-v1.py` | programme recopié au devis des moniteurs v1 |
| `calculs-moniteurs-v2.py` | le précédent, corrigé de la remarque M1 (téléchargement retiré du pire cas de la ligne B) ; recopié au devis des moniteurs v2 |
| `faire-v4.py` | applique mot pour mot les corrections de la contre-lecture du devis v3 pour produire le brouillon à marques du devis v4 |
| `remplir-v4.py` | remplit les marques du brouillon v4 et rejoue le programme recopié ; **reconstitué** (le programme original était en ligne de commande) : rejoué, il redonne exactement l'empreinte scellée du devis v4 |
| `faire-v5.py` | passe de la v4 à la v5 (crochet de la correction m4) ; **reconstitué** : rejoué, il redonne exactement l'empreinte scellée du devis v5 |
| `remplir-moniteurs-v1.py` | remplit les marques du devis des moniteurs v1 et rejoue le programme ; **reconstitué** : rejoué sur la v1 remise à marques, il redonne l'empreinte scellée de la v1 |
| `faire-moniteurs-v2.py` | applique mot pour mot les corrections de la contre-lecture du devis des moniteurs v1 pour produire la v2 (programme original, tel que joué) |
| `devis-bras-a-v4-brouillon-a-marques.md` | brouillon du devis v4 avant remplissage des marques (date, heure, confirmation de la mère) |
| `devis-carte-moniteurs-bras-a-v1-brouillon-avant-reponses.md` | premier brouillon du devis des moniteurs, écrit avant les réponses du lecteur habilité (lecture commune bornée à 4 h, décisions différentes) ; non scellé alors, jamais poussé |
| `echec-extraction-sortie-v3-*` | essai raté de contrôle de la sortie du devis v3 (mon extraction comptait mal les clôtures de bloc) ; gardé pour mémoire, la sortie réelle était identique |
| `sortie-*.txt` | sortie de chaque programme ci-dessus, rejoué le 2026-11-23 avec `python3 -I` |

Reconstitués ne veut pas dire inventés : chaque fichier reconstitué est rejoué contre une empreinte ou une sortie déjà consignée, et la vérification est écrite dans la passation.
