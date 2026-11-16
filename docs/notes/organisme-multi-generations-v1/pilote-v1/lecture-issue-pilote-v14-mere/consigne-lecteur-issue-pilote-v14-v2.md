# Consigne du lecteur de l'issue du pilote MR-2 (procédure v14) — v2

Version 2, 2026-11-16T13:36:53Z (`date -u`, au scellement) : corrections du tour 1 de sa contre-lecture appliquées (section « Contre-lecture », en fin de pièce) ; la v1 (`5189c442…`) reste intacte dans ce dossier.

Préparée par le compte organisme (modèle A), **auteur du texte scellé et du code : il ne lit pas l'issue**. À remettre telle quelle,
avec les seules pièces nommées ci-dessous, à **un sous-agent neuf** qui n'a écrit ni le texte scellé, ni le code, ni la conception v4
(texte scellé, « Plan d'analyse », point 3 ; R13). Le lecteur est choisi et lancé par la mère, après l'état `fini` de la machine et la
récupération de la branche de sortie (procédure v14, section 9). Le compte organisme n'ouvre aucune des pièces d'issue.

## Ce que le lecteur reçoit, et rien d'autre

1. **Le texte scellé** : `docs/notes/organisme-multi-generations-v1/pilote-v1/preenregistrement-pilote-conditionnelles-v1-candidat6-compte-organisme.md`
   (branche `prep/pilote-mr2-compte-organisme-v1`), `8aa33014667da569ec934459d7bc1b1f6b54efa5c2145a6e5bdce5f7fa74603e` ; il en
   applique les sections « Métrique », « Seuil », « Plan d'analyse », « Critères de lecture gelés », « Audit de symétrie (R4) » et
   « Liste d'arrêt », et rien d'autre.
2. **La copie de la branche de sortie** `calcul/pilote-mr2-v74-sortie-v14` faite par la session mère (`$OUTIL recuperer`), à son sommet
   final (`etape=fini` dans `etat.txt`) ; en particulier :
   - `rapatrie-reel/lecture-pilote-v70.json` et son compagnon (sortie de `lire --ecrire` : l'issue, champ `regle`) ;
   - `remis-au-sous-agent/sortie-lire-non-ouverte.txt` (sortie de `lire`, jamais ouverte par la session qui lance) ;
   - `rapatrie-reel/sortie-mesure-pilote-v70.json`, `rapatrie-reel/mesure-pilote-v70.json` (pièce de liaison), le manifeste
     `rapatrie-reel/manifeste-pilote-v70.json`, le relevé `rapatrie-reel/releve-pilote-v70.json`, `rapatrie-reel/CARTES.json`, avec
     leurs compagnons ; `journal-10-mesurer.txt`, `code-10-mesurer.txt`, `code-10-lire.txt`, `journal-09-reel.txt` (ou `…-reel-2`),
     `engagement-mondes.json`, `etat.txt`, `lancements.jsonl`, `code-06-generer.txt`, `code-07-preparer.txt`, `code-08-blanc.txt`, `code-09-reel.txt`, `code-11-rapatrier.txt`, `secret-sha256.txt`, `phrase-sha256.txt`, `rapatrie-reel/liste-rapatriement-pilote-v70.json`, `rapatrie-reel/journal-relais-fable52.jsonl`, `…-opus55.jsonl`, `…-argon.jsonl`, `…-astra.jsonl` (point 4 du plan), et les dossiers `rapatrie-reel/monde-N/PROPOSEUR/` (réponses brutes, corps des relais, témoins d'isolement : lus pour leurs empreintes, leur présence et l'audit du point 7, jamais recopiés). Les journaux, les `code-*.txt` et `etat.txt` sont à la racine de la copie. `rapatrie-blanc/` (essai à blanc, proposeurs factices) ne sert pas à l'issue et n'est jamais confondu avec `rapatrie-reel/`.
3. **Le registre des inscriptions** sur `main` (`registres/pilote-mr2-v74-v14-inscriptions-v1.md`, au commit le plus récent) : empreintes
   du secret, de la phrase, des mondes `H` et `S1` à `S4`.
4. **La dépense**, calculée par le compte organisme avec `depense_pilote_v14_v1.py` (empreinte `9866e611d7997c32eba82cf308dbed1c2ccf184992f106811b2623357dc88643`, dossier `…/lecture-depense-pilote-v14-compte-organisme/` de la branche `lot/compte-organisme-v1`, copié par la mère avec la copie de sortie) : le programme ne lit que `releve-pilote-v70.json` et `journal-relais-*.jsonl`. Le lecteur reçoit sa **sortie JSON scellée** (nom donné par la mère) et les arguments `--machine` (prix horaire, heures de création et de destruction) et `--autre` tels que la mère les a donnés ; il les rapporte sans pouvoir les vérifier. Il vérifie l'empreinte du programme et recoupe lui-même, par lecture, les sommes du relevé et des journaux. Les prix de la configuration ne sont pas remis (le programme ne les lit pas) ; il ne recalcule aucun coût.

Les mondes, le secret et la phrase ne sont pas sur la branche et ne lui sont jamais donnés.

## Ce qu'il fait (plan d'analyse du texte scellé, dans l'ordre)

0. **Arrêts (« Liste d'arrêt »), avant toute ouverture de `lecture-pilote-v70.json` et de `remis-au-sous-agent/sortie-lire-non-ouverte.txt`**
   (ces deux pièces s'ouvrent en dernier, après les points 0 et 1). Il lit à la racine de la copie : `etat.txt` (`etape=fini`, aucun
   `arret (A)`, `noeud, machine gardee` ni `sortie inattendue` ; fichiers exclus au balayage : aucun nécessaire) ; `code-06-generer.txt`,
   `code-07-preparer.txt`, `code-08-blanc.txt`, `code-09-reel.txt`, `code-10-mesurer.txt`, `code-10-lire.txt`, `code-11-rapatrier.txt` : tous
   à 0 (un code 3 vaut arrêt) ; `lancements.jsonl` : une seule ligne ; `rapatrie-reel/liste-rapatriement-pilote-v70.json` : `"aucun_monde": true`
   et pas de `CARTES-partiel.json` ; relevé et manifeste complets (non partiels) ; les 16 appels ont une réponse brute et un témoin
   d'isolement scellés ; dans la dépense remise (point 4 des pièces) : aucun appel au-dessus de son pire cas, aucune part atteinte. Tout
   écart ou tout contrôle impossible : arrêt, rapport, **aucune issue lue, pas même P-0** (texte scellé, « Liste d'arrêt ») ; un contrôle qu'il
   ne peut faire est écrit « non fait » avec sa cause, jamais sauté en silence (R5).

1. **Empreintes** : chaque pièce qui a un compagnon égale à son compagnon (les journaux, `etat.txt`, `lancements.jsonl` et `remis-au-sous-agent/` n'en ont pas) ; le texte scellé lu égal à `8aa33014…` ; `secret-sha256.txt`, `phrase-sha256.txt` et `engagement-mondes.json` égaux aux empreintes du secret, de la phrase, de `H` et de `S1` à `S4` du registre (A dit si `phrase-sha256.txt` est de même nature que l'empreinte inscrite) ; `fichier_mondes_sha256` du manifeste égal à `H` inscrit, et les quatre
   empreintes de mondes égales à `S1` à `S4` (la liste `mondes_sha256` de la sortie de mesure est triée : comparer comme ensemble) ; `programme_sha256` de `mesure-pilote-v70.json` et `hors_corps.script_sha256` de la sortie de mesure égaux à `676d5f37f21cf5d512f92d2029991fa8795a77076c285ea9bd83c43841748365` ;
   `cartes_sha256` de la pièce de liaison égal à l'empreinte de `CARTES.json` ; liste `hors_corps.modules_importes` de la sortie de mesure comparée au bloc
   gelé du texte (S-c). Tout écart : arrêt, rapport, aucune issue lue.
2. **Mesure** : faite une seule fois sur la machine (code 0 attendu : `code-10-mesurer.txt`, `journal-10-mesurer.txt`) ; il ne la refait pas ; code non nul, exception ou refus nommé : arrêt (« Liste d'arrêt », erreur du programme de la mesure), aucune issue lue.
3. **Issue** : lue au champ `regle` de `lecture-pilote-v70.json` (`regle.issue` vaut `P-0`, `P-1` ou `P-2` ; « P-2 avec réserve » est `P-2` dont `regle.noeuds_avant_banc` n'est pas vide, chaque nœud nommé ; « P-2 » sans réserve a cette liste vide) ; il **applique la table « Critères de lecture gelés »** (la première ligne
   qui s'applique : P-0, P-1, P-2 avec réserve, P-2), en vérifiant que le champ `regle` et les comptes de la sortie mènent bien à cette
   ligne ; il rapporte l'issue, les nœuds qu'elle appelle et « ce qui suit », mot pour mot.
4. **Coûts** : rapprochement par fournisseur (`depense_usd` et coûts des appels du relevé, somme des `cout_usd` des journaux des relais, parts de 12, 8, 9,36 et 9,36 USD ; π1 contre 20 USD, π2 contre 21,72 USD ; un code 3 du programme ou une part dépassée est déjà un arrêt du point 0) ; écarts rapportés ; la console fait
   foi pour les montants facturés (R-2803).
5. Aucune autre exclusion que celles de « Métrique » ; aucune analyse en sous-groupe ne décide.
6. Le rapport dit : « P_VUE = 0,25 supposée, non mesurée » ; « p_c ne vaut que pour ce gabarit » ; les taux d'erreur du texte (section « Prédiction chiffrée et signe attendu » : course refusée à tort 0,20 si p vaut 0,02 ; permise à tort 0,26 si p vaut 0,051 ; à 12 et 14 appels répondus, refusée à tort 0,22 et 0,21, permise à tort 0,29 et 0,27) et, si l'issue est P-2, la phrase « Une issue P-2 favorable ne dit pas que les proposeurs « ne voient pas » les conditionnelles ».
7. **Audit de symétrie (R4)**, tel que le texte le gèle : il lit `audit_R4` de la sortie de la mesure. « déclenché : x = 0 » : il relit toutes
   les cartes refusées au gardien, au-delà de six ou non évaluables, et 3 cartes par appel tirées au hasard (graine : `SeedSequence` de
   l'entier des 16 premiers octets, gros-boutiste, de sha256 de `CARTES.json` ; tirage sans remise, toutes les cartes si l'appel en a au plus 3),
   vérifie que les épisodes servis contiennent les traits et que les témoins disent le gabarit servi. « déclenché : x ≥ 3 » : il relit les cartes
   qui portent, vérifie qu'aucune pièce servie ne décrit la famille ou une condition et l'isolement (témoins), relit aussi les cartes refusées et
   non évaluables. « non déclenché » : aucun audit. L'audit ne change pas l'issue, il la commente (réserve écrite) ; un contrôle qui exige une
   pièce non remise est écrit « non fait ».

## Ce qu'il rend

Un verdict écrit, **scellé** (`python -m controle_ia.scellement sceller`), en français, sans identifiant de modèle Claude ni identifiant
servi (« modèle A », « modèle B » si besoin ; R-2731), sur une branche de travail désignée par la mère, dans un fichier neuf au nom donné par elle (R12), rien d'autre n'étant écrit : issue (P-0, P-1, P-2 avec
réserve, P-2), ligne appliquée, comptes, empreintes vérifiées, écarts, dépense rapprochée, contrôles d'arrêt, audit R4 (déclenché ou non, fait ou non fait), les trois phrases du point 6, nœuds de Lazar appelés. Le verdict est soumis à Lazar par la
mère (R13). Le lecteur ne lance ni la mesure, ni le pilote, ni aucun programme qui écrit hors de son fichier de verdict (il lit et additionne les pièces remises), ne dépense rien, n'ouvre aucun chemin interdit (brief, section 6), ne recopie aucune réponse
brute.

## Contre-lecture

- **Rapport** : `contre-lecture-consigne-lecteur-issue-pilote-v14-tour1-v1.md` (même dossier), empreinte
  `14725e82ff9e8d6a7dc0f11457dcb6131c45a69d69d2085965c3fad430e2c8ea` ; verdict « corrections » (cinq majeures, sept mineures).
- **Application** : par un rédacteur neuf (modèle C), qui n'a écrit ni la v1, ni le texte scellé, ni le code, par le programme
  `appliquer-corrections-consigne-lecteur-issue-pilote-v14-v2.py` (même dossier) : empreinte de la v1 vérifiée, chaque « ancien »
  présent une seule fois, cible jamais écrasée. Noms des pièces citées vérifiés présents dans la copie de sortie (noms et tailles
  seulement, aucune pièce ouverte : 16 réponses brutes, 16 témoins d'isolement, quatre dossiers `monde-N`, aucun `CARTES-partiel.json`).
- **Réponse point par point** :
  - C1 (arrêts, nouveau point 0) : appliquée mot pour mot.
  - C2 (P-2 contre P-2 avec réserve) : appliquée mot pour mot ; `regle.issue` et `regle.noeuds_avant_banc` relus sur
    `mesure_pilote_v4.py` (`676d5f37…`).
  - C3 (pièces manquantes) : appliquée mot pour mot ; la note du rapport « à adapter si un de ces noms change » est hors du nouveau
    texte et n'est pas recopiée ; tous les noms existent aujourd'hui.
  - C4 (audit de symétrie) : appliquée mot pour mot. **Point ouvert, à lever par l'auteur avant la remise** : la formule de la graine
    est une proposition du contre-lecteur ; le texte scellé dit seulement « graine dérivée de l'empreinte de `CARTES.json` » ; l'auteur la
    confirme ou la remplace (R9).
  - C5 (dépense, deux couples) : appliquée mot pour mot ; parts et lignes (12, 8, 9,36, 9,36 ; 20 ; 21,72 USD) relues égales à celles du
    programme `9866e611…`.
  - C6, C8 : appliquées mot pour mot ; `hors_corps.script_sha256`, `hors_corps.modules_importes` et le tri de `mondes_sha256` relus sur
    `mesure_pilote_v4.py`.
  - C7 (compagnons, texte, secret, phrase) : appliquée mot pour mot. **Point ouvert, à lever par l'auteur avant la remise** : la
    parenthèse sur la nature de `phrase-sha256.txt` s'adresse à l'auteur, non au lecteur ; le rédacteur ne peut la trancher sans ouvrir
    la pièce. La procédure v14 (section 5, point 5) dit que la machine pousse `phrase-sha256.txt` après avoir vérifié l'empreinte du
    fichier déchiffré égale à celle du feu, qui est celle que le registre inscrit (« empreinte du fichier de la phrase (retour à la ligne
    final compris) ») ; l'auteur le confirme et retire la parenthèse.
  - C9 : supprimée par le contre-lecteur, intégrée à C3 ; sans objet.
  - C10, C11, C13 : appliquées mot pour mot.
  - C12 (taux d'erreur) : appliquée **avec une correction de chiffres**. Le nouveau proposé disait « mêmes taux à 12 et 14 appels
    répondus » ; le texte scellé (« Prédiction chiffrée et signe attendu ») donne d'autres taux à 12 et 14 appels répondus : refus à
    0,02 de 0,22 et 0,21, acceptation à 0,051 de 0,29 et 0,27. Ces chiffres remplacent « mêmes taux » ; le reste du couple est mot pour
    mot.
  - Remarques facultatives R1 à R4 : non appliquées (non exigées), laissées à l'auteur ; R1 (« brief, section 6 », document que le
    lecteur ne reçoit pas) mérite d'être tranchée avant la remise.
