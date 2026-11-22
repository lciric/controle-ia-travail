# Note du correctif 0013 : coupure propre de l'étalonnage relevée de 12 à 16 USD — v1

Écrite le 2026-11-22 par le développeur du correctif 0011 (Claude Opus 5.5, côté saboteur), sous le même mandat
(`registres/iib-reconception/mandat-developpeur-correctif-0011-environnement-machine-v1.md`, abfe45aa9d28…). Préparé sans rien lancer
d'autre que des essais. **À n'appliquer qu'au mot de Lazar** (relèvement porté par la mère, sous le plafond de 17 USD de l'étape 1
au devis scellé et sous GO-2026-11-21-70). Aucune sortie de l'étalonnage en cours n'a été lue.

## Commit
- Correctif 0013 : commit 530240333699579912fb8610dc12ace3e85e221a, arbre a08acfe667f4496d65793e76d6c93ee0fddf65ec, parent
  887561b759ded1bcadb450cedead3f29e946dda7 (correctif 0012) ; branche locale `correctif-0011-local`, jamais poussée.
- `0013-Organisme-retenu-du-saboteur-budget-code-en-version-.patch` (8538c203b4bc39cf01b5cb4cd987b4688427975456ab254bde06811d0f76e907) ;
  appliqué sur 887561b7 dans un index temporaire, il redonne l'arbre a08acfe6.

## Ce qui change, et seulement cela
- `src/controle_ia/iib/session_v5.py` : `COUPURE_ETALONNAGE_USD = 16.0` ; les deux phrases de documentation qui disaient 12.
- `scripts/lancer_iib_v3.sh`, ligne 402 : « seuil 16 USD » dans la ligne écrite au départ de la surveillance.
- Essais de la règle, mêmes formes : l'essai de la règle dans le processus (cas sain à 15,99 USD, artefact à 16,00, prix réel lu,
  début non relevé et second démarrage à 16,56, autre phase au-delà de 16) ; les trois essais de la surveillance (11 h, 15,18 USD :
  rien ; 12 h, 16,56 USD : coupure ; autre phase et fin du run à 12 h) ; la règle sous python3 sans numpy (15,18 : rien ; 16,56 :
  arrêt). Deux essais de la surveillance portaient « 12 » dans leur nom : renommés `…_sous_16_rien` et `…_a_16_coupure_…`.
  La liste du rejeu des huit essais arrêtés sur la machine suit ces deux noms (mêmes essais) : c'est le seul autre essai touché.
- Inchangés : amorce, minuterie, configuration, liste figée. **275 essais attendus**, nombre inchangé.

## D'où la surveillance lit la règle
Du dépôt extrait du côté de la session, jamais de la machine. `lancer_iib_v3.sh` fixe à la ligne 79
`DEPOT="${IIB_DEPOT:-<arbre qui porte le lanceur>}"`. La ligne 88 pose `SESSION=… sys.path.insert(0, '$DEPOT/src'); from
controle_ia.iib import session_v5 …`, et la ligne 427 joue, à chaque relevé, un python3 neuf
(`python3 -I -B -c "$SESSION" coupure-etalonnage …`), qui relit `session_v5.py` sur le disque de la session. L'amorce, sur la
machine, n'appelle jamais la règle (aucune « coupure » dans `amorce_instance_iib_v5.sh`). Un commit neuf, extrait du côté de la
session, suffit donc ; rien ne change sur la machine. Précisions :
1. C'est l'arbre `$DEPOT` qui doit porter le commit : `IIB_DEPOT` s'il est posé, sinon l'arbre du lanceur.
2. La surveillance déjà lancée prend 16 USD dès le relevé qui suit l'extraction, sans redémarrer. La ligne de départ déjà écrite
   dans `surveillance.txt` (« seuil 12 USD ») reste telle quelle jusqu'à un redémarrage ; la décision, elle, suit la constante.
3. Le lanceur ne vérifie pas `session_v5.py` par une empreinte (seul `location_v1.py` l'est) : c'est le fichier présent dans
   `$DEPOT/src` à chaque relevé qui fait foi. L'extraction doit donc porter le commit entier, pas une édition partielle.
4. La boucle de surveillance en cours est déjà lue par bash : le cas `surveillance` appartient à une seule commande
   `case … esac` (lignes 203 à 524). Le `lancer_iib_v3.sh` remplacé n'est pas relu par cette boucle.

## Essais rejoués sur le commit 53024033
- Fichiers touchés (`tests/test_iib_lanceur_v5.py`, `tests/test_iib_environnement_machine_v5.py`) :
  `sortie-essais-fichiers-touches-correctif-0013.txt` (949301c5…), « 24 passed ».
- Liste figée (`scripts/tests-cibles-iib-v5-v5.txt`, 24 fichiers) : `sortie-liste-figee-correctif-0013.txt` (f207a452…),
  « 275 passed in 598.98s ».
