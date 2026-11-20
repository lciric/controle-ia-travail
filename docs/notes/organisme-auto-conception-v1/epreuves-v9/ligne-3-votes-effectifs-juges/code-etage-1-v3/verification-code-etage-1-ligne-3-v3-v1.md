# Vérification du code de l'étage 1 de la ligne 3, version 3 (deux ajouts à l'alarme) — v1

Pièce de travail (classe C), 2026-11-20. Vérificateur neuf, modèle S. Rien écrit dans le dépôt, rien sous `/root/.claude/`, aucun calcul décisif, aucun chronométrage, aucune racine autre que 2026111930, aucun refus d'outil.

## Verdict : **Conforme**

## Empreintes
Mandat v4 et additif 1 v2 (`e1c1ee84…`) égaux à leurs compagnons. Code v3 (banc `09bfe0db…`, essais `28ad0e89…`, chronomètre, contrôle `b4078e71…`, programme de comparaison, sa sortie, rapport du développeur) : chacun égal à son compagnon. Mes copies (dossier `code-v3/`) ont les mêmes empreintes. Python 3.13.18.

## 1. Les deux ajouts suivent l'additif
- **Silence 1** (`silence_1_part_et_comptes`, appelée par `cellule_alarme`) : (b) = suites « à effet » détectées / suites portant au moins une alarme à l'un des 11 tests, qu'elles changent ou non, avant ou après le changement ; une suite « à effet » dont toutes les alarmes précèdent le changement est au dénominateur seulement. Dénominateur nul : None. Cinq comptes présents (suites à effet détectées ; suites qui changent détectées ; suites en alarme ; suites sans changement en alarme ; suites). Nom distinct de (a) (`part_des_detections_sur_changement_a_effet`, inchangée). Mention obligatoire (« mélange planté : une suite sur deux change, une sur quatre à effet ») rendue avec (b). Calcul après les tirages, sur `alarmes`, `change`, `effet`, `detecte` déjà construits.
- **Silence 2** (`criteres_alarme_p6`) : par m (10, 20, 40), fausse alarme du bras B atteinte si 100 x > 8 N sur comptes entiers (plus de 80 sur 1 000), lue à chaque m ; détection « à effet » de B contre D, atteinte si B ≤ D, lue à m = 20 et 40, rapportée hors clause à m = 10. Mots « P6 réfutée » / « P6 non réfutée », ou « incomplet » si une cellule manque ou est en double (jamais un repli silencieux). Marqué « aide… jamais le verdict (R13) ». La carte `fcbf4a2dd1a57` reçoit « mesurée, sans mot : aucune règle de mot gelée » ; les deux mots de P6 ne lui sont jamais écrits (essai). Le reste de P6 est dit sans clause.
- **Clé ajoutée `comptes_du_melange_plante`** (par cellule d'alarme : suites qui changent, à effet, sans effet, sans changement ; valeurs tirées des masques plantés, non des tirages) : **acceptable**. L'additif demande « les comptes » par m et la clause de fausse alarme a besoin du nombre de suites sans changement (dénominateur) et du nombre de suites à effet ; sans cette clé il faudrait les coder en dur dans l'aide. Elle est déclarée, comptée parmi les clés neuves du programme de comparaison, essayée (valeurs 200/100/100/200 sur 400 suites). Remarque pour l'additif de code : la nommer dans la liste des ajouts, l'additif 1 ne la nomme pas.

## 2. Différentiels et égalité à l'octet
- J'ai refait `diff -u` v2 → v3 du banc : seuls changent la version, la docstring, les constantes et fonctions ajoutées, trois insertions dans `cellule_alarme` et `executer_etage_1` (une clé de critères), les deux noms de sorties. Aucune ligne de calcul existante, aucun tirage, aucune constante existante. Même contenu que `banc-v2-v3.diff`.
- Chronomètre : version, nom du banc, nom du manifeste seulement. Essais : seules lignes retirées = renommages v2 → v3 (en-tête, chemins, sorties). Contrôle : en-tête, assemblage de la liste, nom du chronomètre, nom du programme.
- Programme de comparaison rejoué par moi (banc v2 d'empreinte `ffc33083…`) : deux configurations, `toutes les sorties existantes égales : True` ; relecture du v2 rend ses octets, 0 clé du v2 absente du v3, clés neuves = ajouts déclarés (14 et 40), seule feuille différente `/version`, v3 réduit égal au v2 à l'octet, dérivations de graines égales, racine 2026111930 seule. Les empreintes de résultats (v2, v3, v3 réduit) sont identiques, une à une, à celles de `comparaison-sorties-v2-v3-ligne-3-v1.json`.

## 3. Essais et contrôle des défauts chez moi
- `python3 -B -m pytest -q -p no:cacheprovider essais_banc_juges_scriptes_ligne_3_v3.py` : **115 passés, 0 échoué** (10,7 s). Les 109 du v2 sont conservés, 6 neufs (essais sain et artefacts des deux ajouts, preuve à l'octet).
- Contrôle des défauts, mode visé : essais visés sains 78 passés ; **93 défauts sur 93 vus** (v1 27, contre-lecture 35, C2R 1, B3S 1, graines 6, silence 1 : 10, silence 2 : 11, égalité : 2) ; `non_vus` vide.
- Mode complet (fichier entier, `-x`) : **93 vus sur 93**, fichier entier sain 115 passés, `tous vus : True`.
- Échoués : aucun.

## 4. Graines
Seule 2026111930 est dérivée : l'essai final (journal et entropies = {2026111930}) passe dans mes 115 essais ; le programme de comparaison rend `racines=[2026111930]` et journaux v2 et v3 égaux à [2026111930]. Aucune racine de 2026111931 à 2026111937.

## 5. `git status --porcelain` du manifeste
La commande est `commit_du_depot` (banc 1689-1700, **inchangée depuis le v2** : absente du différentiel) : `git -C DOSSIER rev-parse HEAD` puis `git -C DOSSIER status --porcelain -- DOSSIER`, avec DOSSIER = dossier du fichier du banc (`Path(__file__).resolve().parent`). Elle est donc bornée deux fois au dossier du code (option `-C` et spécification de chemin `-- DOSSIER`) : git ne lit l'état que des chemins sous ce dossier. Le mot `archives-reponses-modeles` n'apparaît nulle part dans le banc (recherche dans le fichier). Elle ne touche un chemin sous `archives-reponses-modeles/` que si ce dossier se trouvait sous le dossier du code : je ne l'ai pas vérifié (aucune commande de liste) ; ce n'est pas le cas du dossier `code-etage-1-v3/` tel que le texte du mandat le décrit. Pour le lancement décisif, ne pas copier le banc dans un dossier qui contiendrait `archives-reponses-modeles/`. Erreurs et absence de dépôt gérées sans repli silencieux (« inconnu »).

## Défauts vus, corrections
Aucune correction exigée. Remarques : (1) nommer `comptes_du_melange_plante` dans l'additif de code ; (2) la fonction `criteres_alarme_p6` ignore sans bruit une cellule dont m n'est pas 10, 20 ou 40 : sans effet sur la configuration décisive, et un m manquant donne « incomplet ».

Vérificateur, modèle S.
