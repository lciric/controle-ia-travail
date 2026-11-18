# Contrôle neuf de la différence, avant scellement, du texte court du barreau 7 (bras externe NARCBench) — v1

- **Contrôleur** : sous-agent neuf, Claude Sonnet 5.5 (`claude-sonnet-5-5`) ; je n'ai écrit ni le texte, ni le code du bras externe, ni leurs contre-lectures ; je ne serai ni lecteur ni juge du verdict. Travail du 2026-11-18, après 19:50 UTC.
- **Mandat** : `docs/notes/narcbench-8b-v1/mandat-controle-difference-texte-court-v1.md` (`26c880141f25a0bfe4d997692e1d06a5ee87b8ea48df665830be429df8d1f6cf`, vérifié par la commande du dépôt : conforme).
- **Texte candidat contrôlé** : `prereg/narcbench-bras-externe-v1.md`, `f9d4732467d6bf1324c621e2c080e51eafa2204623431184ef4a4f9ccc64598e` (empreinte recalculée : égale). Brouillon 3 `fae8a96c…`, contre-lecture 3 `f8ca72e2…`, fichier des différences `43d352a0…` : empreintes recalculées, égales aux attendues. Code à la tête `fe9d799641ed3cc5d3388026e6f6143f92fc7d5c`, lu par `git archive` dans un dossier temporaire à moi.
- **Aucune donnée réelle, aucun résultat du programme.** Rien lu sous `/home/user/narcbench-donnees-v2/`, `diag/`, `runs/`, `donnees/`, `docs/verdicts/`, `registres/`. Aucun fichier existant modifié, pas de commit, pas de poussée, aucun modèle chargé, aucun téléchargement, aucune dépense. Dossier temporaire supprimé.

## Verdict

**À sceller tel quel, entropie écrite.** Aucun couple à appliquer. Une seule inscription reste à faire : l'entier de la ligne `Entropie :` (311), au moins 2³² = 4 294 967 296.

## 1. Rejeu du `diff -u`

- `diff -u` rejoué entre le brouillon 3 et le texte candidat : 380 lignes ; le bloc `diff` du fichier des différences en compte 380 ; **identiques** (hors les deux lignes d'en-tête avec dates, qui portent les mêmes dates).
- Vingt-deux blocs de changement. Chacun se rattache à une famille permise :
  - **Couples de la contre-lecture 3** : C1 (Puissance ; frontière n° 8 ; ligne M3 du tableau de la contre-lecture 2) ; C2 (liste d'arrêt n° 1) ; C3 (gabarits des lignes R1 et R2, et sa mention dans le paragraphe des phrases gelées) ; C4 (« Ordre » de la liste d'arrêt ; plan n° 2) ; C5 (`run-id`).
  - **Suggestions retenues** : « environ trente fois sous la tolérance de 0,03 » ; « à 10⁻⁹ près » dans les conditions des lignes C2 et C3 de la table ; raison de l'absence de réserve sur R2 (section « Seuil »). Suggestion non retenue (réserve sur F1) : raison écrite dans le texte, aucun mot de phrase gelée touché.
  - **Points de forme demandés par la mère** : statut ; heure du rédacteur ; mandat ; tête finale `fe9d7996…` ; documents qui font foi (heure du recalcul, dépôt principal, brouillon 3 et contre-lecture 3 ajoutés) ; fusion avant le scellement (documents, plan n° 0 et n° 2) ; plan n° 1 ; relevé de la mémoire (liste d'arrêt n° 11, tableau m6) remplacé par la mesure du jouet ; code (base, « Écarts entre ce texte et la tête finale ») ; expositions (d), (h), (i) et rédacteur ; tableau de la contre-lecture 2, ligne m-D6 ; entrée « Contre-lecture 3 ».
- **Aucun changement hors de ces familles.** La phrase du mandat sur R-3310 est remise en lignes sans mot changé (vérifié mot à mot). Les trente-trois changements numérotés du fichier des différences recouvrent exactement les blocs.

## 2. Couples appliqués à la lettre

- **C1** : les trois passages sont ceux de la contre-lecture 3 : « 33 à 61 fois sur cent (deux modèles indépendants ; au plus 57 à 78 fois sur cent sinon) ; les autres issues (« en partie », « non tranché à cette puissance ») se partagent le reste, que la simulation ne répartit pas » ; frontière n° 8 ; ligne M3 « adoptée avec correction de la contre-lecture 3 … ». 0,573 et 0,783 sont dans la sortie scellée `sortie-puissance-regle-v1.txt` (`0c1e9d7a…`, publié 1,00, aires 0,99 et 0,995).
- **C2** : texte identique au couple (« … `EMPREINTES_PUBLIEES` → arrêt avant toute lecture (R11) ; la révision du jeu (`REVISION_JEU`) est consignée au manifeste, non comparée : les empreintes des huit fichiers la fixent »).
- **C3** : gabarits identiques au couple, aux deux lignes R1 et R2.
- **C4** : « Ordre » et plan n° 2 portent l'ajout, avec « dossier `runs/` ou résultat sous `diag/` » au n° 4.
- **C5** : texte identique au couple.
- **Valeur corrigée par le rédacteur (0,004 et non 0,001)** : correcte. La pièce scellée `sortie-puissance-marge-ecart-v1.txt` (`4f51889f…`) donne, à l'écart à sa marge (aire vraie 0,96, publié 0,99) : reproduit 0,160, **non reproduit 0,004**, non tranché 0,836. Le 0,001 du rapport est la valeur de la grille à 0,97 (publié 0,99), non à la marge de l'écart. Le 0,002 « au pic » est la valeur de la grille à 0,97 (publié 1,00, marge du pic 0,97) : exact. « Environ trente fois sous la tolérance » : 0,03 / 0,001 = 30, exact.
- Écart à une suggestion : un seul (cette valeur), déclaré par le rédacteur et justifié.

## 3. Phrases gelées

- Script du développeur `phrases_gelees_brouillon3_v1.py` (copie à moi, seule ligne changée : l'empreinte attendue, remplacée par celle du texte candidat), code de la tête finale, sur la copie du texte candidat : **39 phrases gelées comparées, 0 écart**, code de sortie 0.
- Contrôle de garde : sur une copie dont la phrase R1 est abîmée (« 3 fois » devenu « 4 fois »), le même script rend 1 écart et code 1 (le contrôle détecte un artefact).
- Valeur « sans plancher » : appel de `reponse` du code avec un plancher « sans plancher » ; les phrases R1 et R2 produites (« … plancher apparié : A : au-dessus ; B : pas au-dessus ; C : sans plancher … ») sont permises mot pour mot par le gabarit élargi (« au-dessus, pas au-dessus ou sans plancher »), et le script, rejoué avec cette entrée, rend 0 écart.
- Aucun mot fixe de phrase gelée n'a changé entre le brouillon 3 et le texte candidat (seul le gabarit entre `<…>` de R1 et R2 change).

## 4. Échappatoires et chiffres ajoutés

- Aucune échappatoire neuve (R3) : aucun seuil, aucune condition de règle, aucune issue ni aucun ordre de règle changé ; les ajouts restreignent ou précisent (probabilité de « oui » bornée ; garde d'ordre précisée ; révision du jeu consignée, les empreintes la fixent).
- Chiffres ajoutés, sourcés : tête finale et sujets de ses trois commits (`git log` : `950e5d3c`, `b46c678d`, `fe9d7996`) ; seul `src/controle_ia/narcbench/cellules_externe_v2.py` change dans `src/` depuis `cde3b990` (`git diff --stat` : 1 fichier, 7 ajouts, 2 retraits), empreinte `0461739c…` exacte ; pièce du jouet `e21ac32a2ad8c451c2d008facbf07598f25637643959f47318356117aea3b58d` exacte, qui dit 4 cœurs et 16 Go, 14,8 minutes, pointe 3 748 Mo, 1 054 et 1 320 lignes ; dépôt principal à `9e90e525`, ancêtre du dépôt actuel. « 168 essais » et « 39 phrases » sont attribués au développeur dans le texte ; je n'ai pas lancé la suite d'essais ; les 39 phrases sont rejouées ci-dessus.
- Remarque, non bloquante, sans couple : la formule « les autres issues (« en partie », « non tranché ») se partagent le reste » omet « non », dont la probabilité est négligeable aux aires 0,99 à 0,995 (0,000 dans la sortie scellée) ; c'est la lettre du couple C1 de la contre-lecture 3, appliquée telle quelle.

## 5. Validateur, `verifier-texte`, scellement

- `controle_ia.prereg.problemes` sur le texte candidat : **une seule remarque**, « marqueurs de gabarit restants : `<<ENTROPIE_NARC_EXT>>` ». Sur une copie où ce marqueur vaut 5049312917428823951 : liste vide.
- `verifier-texte` du code de la tête finale : copie à entropie d'essai (≥ 2³²) : **code 0**, configuration lue (augmentation `papier`, couches 26 à 30 et 32 à 37, forme du `run-id`, registre, texte, entropie). Texte lui-même : code 2, seul refus l'entropie. Entropie 123456 : code 2. Entropie 4 294 967 296 : code 0 (borne incluse).
- `sceller_prereg` (lue, non exécutée) : appelle `problemes` puis `sceller` ; `sceller` refuse seulement un fichier absent, une empreinte écrasée ou une empreinte prise pour fichier. Aucun compagnon n'existe pour le texte candidat. Avec l'entropie écrite, `problemes` rend une liste vide : le fichier serait accepté.

## Lectures hors du mandat

- Contrôle de l'existence et de l'ancêtre du commit `9e90e525` ; `git status --short` et `git log --oneline` du dépôt principal (lecture seule) ; empreinte courte du mandat de la contre-lecture 3 (`097a9e21`, égale à celle qu'elle cite). Rien d'autre.
