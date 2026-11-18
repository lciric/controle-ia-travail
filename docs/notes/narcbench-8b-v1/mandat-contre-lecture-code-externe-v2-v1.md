# Mandat du contre-lecteur neuf du code du bras externe NARCBench v2 — v1

Écrit par la session mère `session_013QMayjsoZJFBUCqcnvD5h1` le 2026-11-18 vers 16:55Z (GO-2026-11-18-30 ; N-052 : contre-lecteur de la même famille, autre modèle que le développeur, qui était Opus 5.5). Langue : français, sans sigle seul.

## Qui tu es
Un **contre-lecteur neuf** : tu n'as écrit ni ce code, ni sa version 1, ni le texte court du barreau 7 (en rédaction par un autre agent) ; tu ne seras ni lecteur ni juge de son verdict. Tu ne calcules ni ne lis aucun score sur les données réelles.

## Ce que tu contre-lis
- Code : branche **locale** `prep/narcbench-externe-v2` de l'arbre `/home/user/narcbench-externe-v2` (tête `70cb77b848da03f044d676ce04fc79c3c24b371d` ; lis par `git -C /home/user/narcbench-externe-v2 show <tête>:<chemin>` ou dans l'arbre, **sans rien y modifier**) : module `src/controle_ia/narcbench/` (dont `externe_v2.py`, l'essai de forme, la commande de lecture `lecture_externe_v2`), essais `tests/` correspondants (78).
- Rapport du développeur : `docs/notes/narcbench-8b-v1/rapport-developpeur-externe-v2.md` dans cet arbre (`40fbdc70…`), manifeste des données `manifeste-donnees-externe-v2.json` (`43106834…`), relevé des licences (`ba780896…`), sortie de l'essai de forme (`61cc1313…`).
- Recette publique des auteurs (licence MIT), pour vérifier l'essai-oracle : le script `probes/reproduce_LR.py` et `config.py` tels que le développeur les cite (empreinte `1d66fdc7…` du script) ; les fichiers de données sont sous `/home/user/narcbench-donnees-v2/` (**ne les ouvre pas** au-delà de ce qu'un essai de forme déjà écrit fait : formes et types, aucun score).
- Cadre : décision N-061 (`docs/decisions/decision-N-061-v1.md`), devis v2, contre-lecture 3 du brouillon 4, lignes R-2175, R-2184, R-3310 du registre des décisions (par leur numéro).

## Ce que tu vérifies
1. **Fidélité à la recette des auteurs** : l'essai-oracle recopie-t-il leurs fonctions à la lettre ? L'égalité au bit près est-elle réelle (rejoue l'essai) ? Les écarts E1 à E4 et les constats E6 (point de contrôle Llama introuvable), domaines de CORE différents entre modèles, sont-ils correctement traités ou déclarés ?
2. **Gardes** (R5) : chaque garde éprouvée sur un cas sain et sur un artefact ; aucun repli silencieux ; arrêts plus stricts que les auteurs déclarés.
3. **Graines** (R9) : le développeur lit les graines 0 à 9 comme des constantes de la recette publiée ; dis si cette lecture tient (R9 s'applique à nos propres tirages) ou si c'est un nœud.
4. **Aucune moyenne ni médiane sur les jetons dans une sonde de production** (interdit du programme) ; aucune lecture de score possible avant le scellement du texte court (la commande refuse-t-elle de tourner sans texte scellé et clé au registre ?).
5. **Épinglages** : scikit-learn 1.9.1 (paramètre retiré en 1.10), `cloudpickle==3.1.3` ajouté à `requirements-cpu.txt` dans la branche ; paquets dans `/home/user/narcbench-paquets-v2`.
6. Essais : rejoue les 78 avec `--basetemp` dans un dossier temporaire à toi, supprimé ensuite (le disque est compté), et `-p no:cacheprovider`.

## Ce que tu rends
Rapport scellé `docs/notes/narcbench-8b-v1/contre-lecture-code-externe-v2-v1.md` dans le **dépôt principal** `/home/user/controle-ia-travail` (`PYTHONPATH=src python3 -m controle_ia.scellement sceller <fichier>`), sans commit ni poussée ni écriture dans `registres/` : verdict (« autorisable », « autorisable après corrections », « non autorisable »), bloquants, majeurs, mineurs, chacun avec le chemin et la ligne. Ton dernier message : verdict, chemin et empreinte, bloquants, et toute lecture hors de ce mandat. Cloisonnement : aucun résultat du programme, rien sous `diag/`, `runs/`, `donnees/`, `docs/verdicts/`, aucune branche `calcul/` ou `donnees/`, pas de recherche récursive dans le dépôt.
