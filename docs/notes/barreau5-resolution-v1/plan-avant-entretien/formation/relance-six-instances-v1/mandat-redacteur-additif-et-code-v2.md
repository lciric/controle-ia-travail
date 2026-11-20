# Mandat : additif « relance des six instances » et code de formation v2 (barreau 5)

Écrit le 2026-11-20 vers 12:45Z par la session de formation du barreau 5, sur le mot de Lazar GO-2026-11-20-51 relayé par la mère. Pièce de travail.

## Contexte
- Un texte scellé fixe la formation de familles d'adaptateurs : `prereg/barreau5-sabotage-ou-empreinte-adaptateurs-tenus-a-l-ecart-v1.md` (sha256 bdff244f…).
- **Tu ne lis du texte que les extraits fournis** : `$S/relance/extraits-texte-scelle.md`. Ce sont le point 14 du plan d'analyse (graines), la liste d'arrêt, « Données gardées », « Calcul et dépense », « Calendrier et chemin critique » (dont la règle et la borne de la relance), « Lignes de registre » et « Code neuf ». N'ouvre jamais le fichier du texte lui-même.
- Le code de formation est figé au commit pointé par la ligne `CODE-FORMATION-B5F` du registre propre. Le commit de course 31fca83b0c26cd035fe9e660d123e690a41b6271 = ce code + le registre. Ton arbre de travail est `$S/relance/code` (branche locale `formation-b5f/code-relance-v2`, à ce commit). Fichiers utiles :
  - `src/controle_ia/barreau5_familles/formation_v1.py` ;
  - `scripts/lancer_b5f_formation_v1.sh` ;
  - `scripts/amorce_b5f_formation_v1.sh` ;
  - `registres/barreau5-familles-jumelles-v1.md` ;
  - `tests/test_barreau5_familles_*.py`.
- Ce qui s'est passé le 20 novembre :
  - l'instance 6 a fini, versement prouvé ;
  - les instances 1, 2, 3, 4, 5 et 7 ont été créées vers 10:43Z, puis arrêtées à 12:12Z faute de crédit chez le loueur (mot de Lazar), sans aucune famille formée ; leurs branches de sortie existent.
- Mot de Lazar, GO-2026-11-20-51 (registre des accords, sur `main`) : « relance les instances ». Les six marches tombées sont relancées par des instances neuves, dans l'ordre du texte, avant la fin des créations (2026-11-21T07:30:16Z), sous l'accord de calcul GO-2026-11-19-86 et son plafond commun de 200 USD. L'écart à la règle de relance (au plus deux instances, GO-2026-11-19-87) est accordé.

## Ce qui bloque, dans le code figé
1. `RELANCES_MAX = 2` et `ENVELOPPE_RELANCE_USD = 56.0` (l. 111-112), contrôlés à la lecture du registre (l. 1053-1059). Les six coupures font 26 × 5 + 17 = 147 USD (trois membres d'apprentissage).
2. Le registre refuse toute clé en double et toute ligne « -B5F » inconnue ; les lignes ne sont jamais réécrites. Or `CODE-FORMATION-B5F` épingle le commit du code v1 et l'entropie (128 bits) dont dérivent les graines. Le code v2 a donc besoin d'une manière admise d'épingler son propre commit (par exemple une clé neuve que le code v2 connaît), sans changer l'entropie, et sans invalider les premières marches déjà versées.
3. La garde de calcul du dépôt (`.claude/hooks/garde_calcul.py`) n'admet en `GO_ID` qu'un accord de type « calcul ». GO-2026-11-20-51 est de type « décision ». Le code exige que le `GO_ID` d'une relance égale l'accord écrit dans la ligne `GO-RELANCE-FORMATION-B5F` (l. 1086). La ligne de relance doit donc citer GO-2026-11-19-86, et GO-2026-11-20-51 dans sa colonne de référence.
4. Le texte met la relance hors du plafond commun ; GO-2026-11-20-51 la met sous le plafond commun de 200 USD (dépense à ce jour ≈ 18,5 USD). À trancher dans l'additif, et à tenir par le code ou par une règle de la session, au plus simple.

## Ce que tu produis
1. **L'additif** au texte scellé : `$S/relance/additif-1-relance-six-instances-v1.md`, court, en français, sans acronyme non développé. Il dit :
   - ce qui change (nombre d'instances relançables, enveloppe, compteur commun, clé du code v2, ligne de relance exacte) et pourquoi (GO-2026-11-20-51) ;
   - ce qui ne change pas : familles, graines par la même entropie avec suffixe `-x1`, lecture de la seule copie `-x1`, échéances H + 30 h et H + 54 h, coupures par instance, tout le reste du texte ;
   - l'ordre des lignes au registre.
   L'additif ne touche à rien hors de la relance.
2. **Le code v2**, minimal : rien d'autre ne change que ce que l'additif exige. Ajoute les essais : cas sain et artefact pour chaque garde changée (R5), et une épreuve par retrait qui montre que chaque essai neuf échoue sur le code v1. Tous les essais `tests/test_barreau5_familles_*.py` doivent passer :
   `cd $S/relance/code && PYTHONPATH=src $S/venv-b5f/bin/python -m pytest -q -p no:cacheprovider tests/test_barreau5_familles_*.py --basetemp=$S/relance/essais`.
   Fais un seul commit local sur la branche `formation-b5f/code-relance-v2` (jamais de poussée).
3. **Le rapport du développeur** : `$S/relance/rapport-developpeur-code-relance-v2.md`, avec le diff commenté, le compte des essais, l'épreuve par retrait, les lignes de registre à inscrire (clé, contenu exact, ordre) et la commande de relance que jouera la session.

## Interdits
- Aucune lecture hors des fichiers cités. Rien de `diag/`, aucun score, aucun résultat (7a, 7b, T0.6, étape B, étape B bis, P3-bis), aucun fichier dont le nom contient « consigne-privee » ou « conception-ii-b », rien sous `/root/.claude/`. Le texte scellé, seulement par les extraits.
- Aucune commande du loueur, aucune dépense, aucune poussée, aucune écriture hors de `$S/relance/`. Aucune clé affichée.
- Tu ne lis aucune branche `donnees/…`.

`$S` = `/tmp/claude-0/-home-user-controle-ia-travail/2e5ab823-f39e-5eb7-8014-a7e033a3a8e4/scratchpad`.
