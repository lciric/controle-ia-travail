# Consigne : session fille « relance de P3-bis sous l'écart 2 » — préparation, lancement et course (GO-2026-11-10-02) — v1

Écrite par la session mère `session_01XJ6Mgn4MZR4nxqK44C8Ea3` le 2026-11-12 à 21:57 UTC (heure relevée par `date -u`). Destinataire : une **session fille neuve** de ce compte (la fille précédente, `session_013QMayo3Je79e17xB1yHiDw`, est injoignable d'ici). **Mot de Lazar** : R-2450 (« Recommandation : (1), confiance 0,75. : go ») ; addendum 2 scellé (R-2457). **Dépense** : **GO-2026-11-10-02** seulement (plafond 80 USD ; création au plus tard le 18 novembre 2026).

## Textes qui font foi (empreintes à vérifier avant tout geste)
- `prereg/P3-bis-temoin-positif-v1.md` (`76ab66ce967796b9…`, texte scellé ; « Liste d'arrêt », plan, points 6 et 11) ;
- `prereg/P3-bis-addendum-1-garde-credit-v1.md` (`4e188814b52736ed…`) ;
- **`prereg/P3-bis-addendum-2-telechargement-controle-v1.md` (`c23b2eb0beb5de34db4359b9b97624df09c9b076d5ebe3d20c5b74e257ec9444`)** : ses sections « Préalables du lancement », « Conditions d'emploi » et « Engagement » priment sur cette consigne en cas de doute ; chaque script se lit d'abord par son en-tête.

## Règles (sans exception)
Interdits communs v2 (`docs/notes/g0-deux-semaines-v1/consignes-mere-2026-11-10-0500-v1/interdits-communs-v2.md`, `1ee3b370…`), à lire en entier, plus : **aucun fichier de T0.7 ouvert** ; jamais `docs/notes/bras-attaque/` (ni lu, ni listé), `donnees/bras-attaque*`, `donnees/mode-tenu-a-l-ecart*`, `registres/index-bras-attaque*`, `anteriorite-bras-informe*`, la branche `claude/compassionate-meitner-d4ryyk`, `donnees/lecture-b-7a-quarantaine-v1`, `donnees/mesure-unanime-v15-sortie-v1`, `essai/t06-explo-v3`, `prep/etiqueteur-v2-lecture-interrompue-reprise-v1`, aucun `diag/` ni `runs/` de 7a ou de 7b, jamais `scripts/extraire_mesures_epreuve_t06_v1.py` ; extraction **partielle** qui exclut ces chemins ; clés par leur nom seulement (`VAST_API_KEY`, `HF_TOKEN`, `CONTROLE_IA_GITHUB_TOKEN_2`), jamais `env`, `printenv`, `set` sans argument, `export -p`, `/proc/*/environ` ; garde des secrets à 0 avant tout commit ; `git fetch` seulement avec refspec ; heures par `date -u` ; **arrêt sur tout refus** d'un contrôle de permissions ou d'un classifieur : ni contournement, ni reformulation, ni transfert à une autre session ; R10 : arrêts et destructions **par identifiant ou PID seulement**. **Instances** : 58936096, 58936099, 58936100 (arrêtées) **intouchables** ; **60370121** (`p3bis-v1`, arrêtée) : **tu ne la touches pas** (sa destruction a été refusée à la mère par le classifieur et revient à Lazar) ; toute instance ou serveur d'une autre session (témoin Bailey, etc.) : jamais touché.

## E1. Préparation (tout de suite, aucune dépense)
1. Outil de location `vastai` **1.8.3** seul (`python3 -m pip install vastai==1.8.3`, sinon environnement neuf dans ton bac et son `bin` en tête de `PATH`) ; `vastai --version` = 1.8.3, sinon arrêt.
2. Inventaire filtré (identifiant, étiquette, état ; jamais `--raw` sans filtre).
3. Extraction partielle de la branche `prep/p3bis-ecart2-v1` au commit `444645bbde329e05a5738e9a40a8ad48c8c28eb4` (récupérée par refspec) dans un dossier neuf de ton bac ; vérifie : addendum 2 `c23b2eb0…`, `enchaineur_p3bis_v5.sh` `34131eaf…`, `lancer_p3bis_v2_ecart1_v2.sh` `2e294e5a…`, `verifications_p3bis_v2_ecart2_v1.py` `ba6deb68…`, `surveiller_p3bis_v2_ecart2_v1.sh` `555ee522…`, `controle_cinq_minutes_p3bis_v2_ecart2_v1.sh` `6aa165e5…` ; scripts d'origine égaux à S (`8f8df8b2`, branche `scellement/p3bis-v2`).
4. Place disque : le pic des contrôles avant dépense est ≈ 11,6 Go (R-2409) ; efface chaque dossier `pytest-N` de tes propres passages par chemin exact.
5. Rapport E1 à la mère, puis **attends son mot** « préalables 2 à 4 faits ».

## E2. Mot de la mère (préalables 2 à 4)
La mère te dira : frais de bande passante de 60370121 relevés (ou non lisibles) ; **60370121 détruite** (par Lazar), absence relue ; **dépense antérieure** (montant exact à passer en cinquième argument, arrondi au centime supérieur, inscrit au registre des dépenses). Rien avant ce mot. Relis toi-même l'absence de 60370121 dans l'inventaire.

## E3. Lancement
Juste avant : inventaire, `EN_MARCHE` (`ID:GO-…` des instances d'autres sessions en marche, sinon `-`), crédit présent > 0, date ≤ 18 novembre, numéro de tentative et branche de calcul selon le texte (point 11 : « une relance exige la branche de la tentative précédente » ; `calcul/p3bis-reel-v1` est absente du distant à la tentative de 15:00 : lis le texte et le lanceur, et rapporte ton choix **avant** de lancer s'il y a un doute). Depuis le dossier de la chaîne de l'extraction, `HF_TOKEN` exporté comme pour le lanceur, détaché par `setsid nohup` :
`bash docs/procedures/P3-bis-temoin-positif-v1/enchaineur_p3bis_v5.sh <S> <dossier neuf> <EN_MARCHE> <N> <DEPENSE_ANTERIEURE_USD>` ; PID noté.

## E4. Course
Selon l'addendum 2, « Conditions d'emploi » 1 à 5 : contrôle d'écart (attente bornée jusqu'à création + 900 s), surveillance d'écart ; code 4 du lanceur, traces illisibles, empreinte autre : inventaire, surveillance à la main ou arrêt par l'identifiant ; contrôle bloqué (aucune ligne neuve de `cinq-minutes/releves.txt` pendant cinq minutes) : arrêt par PID, puis surveillance ou arrêt par l'identifiant. **Fin normale** : `recuperation_p3bis_v2.sh` (tu n'ouvres aucun paquet, tu ne lis aucun résultat), puis `detruire_p3bis_v2.sh` sur **ta** nouvelle instance ; absence relue. **Fin anormale** : liste d'arrêt du texte ; aucune relance sans mot de Lazar. Reste active jusqu'à la destruction vérifiée.

## Rapports à la mère
Par `send_message` vers `session_01XJ6Mgn4MZR4nxqK44C8Ea3` à chaque jalon (E1 ; lancement ; création : identifiant, carte, prix, heure ; contrôle ; fin ou arrêt ; récupération : branche, commit, empreintes ; destruction : heure, coût ; lignes proposées pour `registres/depenses.md` et `registres/arrets.md`). Si `send_message` est refusé : note poussée `etat-p3bis-fille-v2.md` sur la branche neuve `etat/p3bis-fille-v2` (refspec explicite), mise à jour à chaque jalon. Tu n'écris rien dans `registres/` : la mère inscrit.
