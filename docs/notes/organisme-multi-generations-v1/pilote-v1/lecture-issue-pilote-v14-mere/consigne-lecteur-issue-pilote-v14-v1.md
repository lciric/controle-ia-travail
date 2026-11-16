# Consigne du lecteur de l'issue du pilote MR-2 (procédure v14) — v1

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
     `engagement-mondes.json`.
3. **Le registre des inscriptions** sur `main` (`registres/pilote-mr2-v74-v14-inscriptions-v1.md`, au commit le plus récent) : empreintes
   du secret, de la phrase, des mondes `H` et `S1` à `S4`.
4. **La dépense** calculée par `depense_pilote_v14_v1.py` (même dossier), pour le point 4 du plan.

Les mondes, le secret et la phrase ne sont pas sur la branche et ne lui sont jamais donnés.

## Ce qu'il fait (plan d'analyse du texte scellé, dans l'ordre)

1. **Empreintes** : chaque pièce égale à son compagnon ; `fichier_mondes_sha256` du manifeste égal à `H` inscrit, et les quatre
   empreintes de mondes égales à `S1` à `S4` ; `programme_sha256` de `mesure-pilote-v70.json` égal à `676d5f37f21cf5d512f92d2029991fa8795a77076c285ea9bd83c43841748365` ;
   `cartes_sha256` de la pièce de liaison égal à l'empreinte de `CARTES.json` ; liste `modules_importes` de la sortie comparée au bloc
   gelé du texte (S-c). Tout écart : arrêt, rapport, aucune issue lue.
2. **Mesure** : faite une seule fois sur la machine (code 0 attendu) ; il ne la refait pas.
3. **Issue** : lue au champ `regle` de `lecture-pilote-v70.json` ; il **applique la table « Critères de lecture gelés »** (la première ligne
   qui s'applique : P-0, P-1, P-2 avec réserve, P-2), en vérifiant que le champ `regle` et les comptes de la sortie mènent bien à cette
   ligne ; il rapporte l'issue, les nœuds qu'elle appelle et « ce qui suit », mot pour mot.
4. **Coûts** : rapprochement par fournisseur (relevé, journaux des relais, prix de la configuration) ; écarts rapportés ; la console fait
   foi pour les montants facturés (R-2803).
5. Aucune autre exclusion que celles de « Métrique » ; aucune analyse en sous-groupe ne décide.
6. Le rapport dit : « P_VUE = 0,25 supposée, non mesurée » ; « p_c ne vaut que pour ce gabarit » ; les taux d'erreur du texte.
7. **Audit de symétrie (R4)** : un résultat trop propre, dans un sens ou dans l'autre, reçoit le même audit et une réserve.

## Ce qu'il rend

Un verdict écrit, **scellé** (`python -m controle_ia.scellement sceller`), en français, sans identifiant de modèle Claude ni identifiant
servi (« modèle A », « modèle B » si besoin ; R-2731), sur une branche de travail désignée par la mère : issue (P-0, P-1, P-2 avec
réserve, P-2), ligne appliquée, comptes, empreintes vérifiées, écarts, nœuds de Lazar appelés. Le verdict est soumis à Lazar par la
mère (R13). Le lecteur ne lance rien, ne dépense rien, n'ouvre aucun chemin interdit (brief, section 6), ne recopie aucune réponse
brute.
