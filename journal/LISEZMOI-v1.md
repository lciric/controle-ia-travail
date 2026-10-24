# Journal commun du programme — protocole v1 (24 octobre 2026)

Demande de Lazar (24 octobre, 20:11, heure de Paris) : « tenir absolument un journal détaillé exhaustif et un autre
synthétique de toutes les idées et étapes du travail et ce qui a été tranché en détail, hypothèses en cours,
validées, conclusions, hypothèses rejetées ; toi et Claude cloud doivent pouvoir le voir et écrire dessus ».

## Deux journaux, une branche

- Branche `journal/commun-v1`, écrite par les deux lignées (« conv-audit », conversation claude.ai ; « session-depot »,
  session Claude Code en nuage). `main` reste à un seul écrivain (« session-depot »), qui y verse cette branche à
  chaque passation. Lazar lit la branche ou `main`.
- **Journal détaillé** : `journal/detaille/AAAA-MM-JJ-<lignée>.md`, un fichier par jour (UTC) et par lignée — donc
  jamais deux écrivains sur un même fichier. Entrées horodatées (UTC), ajoutées en fin de fichier, **jamais
  réécrites** : une correction est une nouvelle entrée qui cite l'entrée corrigée. Chaque entrée dit : ce qui a été
  fait ou pensé ; les options vues ; ce qui a été tranché, par qui, avec la pièce (chemin, empreinte, commit, message
  du canal) ; les hypothèses posées, testées, retenues, rejetées, et pourquoi ; ce qui reste ouvert. Le fichier du jour
  est scellé (`.sha256`) à la passation ; une entrée ajoutée après descelle et rescelle (nouvelle empreinte consignée
  dans l'entrée suivante).
- **Journal synthétique** : `journal/synthese-vN.md`, un seul fichier à sections fixes (état des hypothèses :
  en cours / validées / réfutées / retirées ; conclusions acquises ; décisions tranchées, avec date, options, choix,
  pièce ; idées ouvertes et idées écartées ; prochaines étapes). Un seul écrivain à la fois : « conv-audit » le tient ;
  « session-depot » le contre-lit et ajoute, s'il n'est pas d'accord, une section « Divergences » signée et datée.
  Nouvelle version = nouveau nom (`synthese-v2.md`, …) ; l'ancienne reste.

## Règles

- Rien ici n'est opposable (R7) : chaque chiffre renvoie à une pièce empreintée ; un chiffre sans pièce est marqué
  « sans pièce ».
- Aucune clé, aucun jeton, aucune valeur secrète, jamais ; les archives de septembre 2026 ne sont pas nommées.
- Avant d'écrire : `git pull --rebase origin journal/commun-v1` ; chaque lignée ne touche qu'à ses fichiers du jour
  (détaillé) ou au fichier de synthèse si elle en est l'écrivain.
- Les registres (`registres/`) restent la source du GO, des dépenses, des décisions numérotées ; le journal les cite,
  il ne les remplace pas.
