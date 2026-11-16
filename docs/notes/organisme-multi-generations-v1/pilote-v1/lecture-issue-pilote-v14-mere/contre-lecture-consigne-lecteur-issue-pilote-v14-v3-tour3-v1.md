# Contre-lecture de la consigne du lecteur de l'issue du pilote MR-2 (procédure v14), v5 — tour 3 de la v3 — v1

Contre-lecteur neuf (R2), modèle C ; auteur de la pièce : modèle A. Rapport écrit le 2026-11-16T14:44Z (`date -u`).
Pièce lue en entier : `consigne-lecteur-issue-pilote-v14-v5.md`, empreinte
`05f4f32598e62aaad4cd81f5697c5d0a3eaea43eeb39e387208cbc2fe28e6fbd` (égale à son compagnon). Version précédente : v4,
`de826db5953ec86123ffca204c5b0c488098043298d5b15bc39563025781f8e4` (recalculée, égale). Rapport du tour 2 recalculé :
`98332a7459f6d0ada90441fc57d07b76d3a5051c579de356aa58a556fea177c2`, égal. v3, v2, v1 : préfixes `f06f46b3`, `0e12acbd`, `5189c442` recalculés, égaux.

## Verdict : corrections

Aucune majeure ; une seule correction mineure. Le différentiel v4 → v5 ne contient que ce qui est déclaré, mais la correction demandée au tour 2
n'a pas été appliquée : elle a été remplacée par une formule qui laisse une question ouverte dans la pièce, et la nouvelle puce du tour 2 répète
une affirmation probablement fausse.

## A. Différentiel v4 → v5 (`diff`, lu en entier)

Quatre zones : titre (v4 → v5) ; ligne 3 (version 5, heure `14:38:53Z` antérieure à ce rapport ; v4, v3, v2, v1 citées avec leurs préfixes exacts) ;
puce « Application » du tour 1 de la v3 (une ligne) ; sous-section « Tour 2 de la v3 » ajoutée en fin de pièce. Rien d'autre : le corps de la
consigne (points 0 à 7, « Ce qu'il rend ») est inchangé à l'octet. Le programme `appliquer-…-v5.py` (empreinte égale à son compagnon) fait
exactement ces quatre remplacements, vérifie les empreintes de la v4 et du rapport, l'unicité de chaque « ancien », et refuse d'écraser.
Empreinte citée du rapport du tour 2 exacte.

Correction demandée au tour 2 (m1) : remplacer, dans la puce du tour 1 de la v3, « modèle C » par « modèle A » ou, si la mère confirme A, par la
formule « le rédacteur des corrections (modèle A) » ; « aucune correction » si la mère confirmait C et neuf. **Appliquée avec une adaptation
déclarée** (la mère n'ayant rien confirmé) : « modèle à confirmer par la mère ». Ce n'est ni l'une ni l'autre des deux issues du rapport, et la
pièce scellée porterait alors une question ouverte (« à confirmer par la mère ») sur son indépendance, deux fois. Or la mère sait maintenant : sa
tâche dit que les corrections sont écrites par le modèle A. La question se tranche avant le scellement, elle n'a pas à rester dans la pièce.

## B. Vérifications (1) à (8) rejouées

(1) Points 0 à 7 inchangés ; empreinte du texte scellé recalculée sur la branche `prep/pilote-mr2-compte-organisme-v1` : `8aa33014…03e`, égale ;
empreinte du programme de mesure `676d5f37…` et de dépense `9866e611…` inchangées par le différentiel. (2) Noms vérifiés dans
`/home/user/pilote-mr2-v74-envoi-v14/retour` (noms et tailles) : présents `etat.txt`, `lancements.jsonl`, `engagement-mondes.json`, `secret-sha256.txt`,
`phrase-sha256.txt`, les sept `code-*.txt` nommés, `journal-09-reel.txt`, `journal-10-mesurer.txt`, `remis-au-sous-agent/sortie-lire-non-ouverte.txt`,
et dans `rapatrie-reel/` : `CARTES.json`, `lecture-pilote-v70.json`, `mesure-pilote-v70.json`, `sortie-mesure-pilote-v70.json`, `manifeste-pilote-v70.json`,
`releve-pilote-v70.json`, `liste-rapatriement-pilote-v70.json`, quatre journaux de relais, dossiers `monde-N` ; compagnons présents pour ceux qui en
ont ; rien ouvert. (3) à (7) : inchangés, conformes au tour précédent. (8) Aucun identifiant de modèle dans la pièce (lettres seulement).

## Correction exigée (chaque « ancien » figure une seule fois dans la v5)

### Mineure

**m1 (provenance du rédacteur, deux puces « Application »).** Remplacer le doute par la lettre connue de la mère. Le rédacteur de la v4 → v5 est
du modèle A d'après la tâche de la mère ; pour la v3 → v4, la mère dit qui (si c'était A, couples ci-dessous ; si c'était C et neuf, laisser
la puce du tour 1 de la v3 avec « modèle C » seulement, supprimer le doute). Dans les deux cas, « n'a écrit ni la consigne » est faux pour A,
auteur de la consigne : la formule du rapport précédent évite cette fausseté.

Couple 1 (puce du tour 1 de la v3, une seule ligne) :
ancien : `par un rédacteur neuf (modèle à confirmer par la mère : « modèle C » écrit ici par ce rédacteur, « modèle A » selon le contre-lecteur du tour 2 de la v3), qui n'a écrit ni la consigne, ni le texte scellé, ni le code, par le programme`
→ nouveau : `par le rédacteur des corrections (modèle A), qui n'a pas écrit le texte scellé ni le code, par le programme`

Couple 2 (puce du tour 2 de la v3, deux lignes consécutives, la seconde indentée de deux espaces) :
ancien : `- **Application** : par un rédacteur neuf (modèle à confirmer par la mère : sa tâche le dit « modèle C » et dit aussi que`
suivi de la ligne `  les corrections sont écrites par le modèle A), qui n'a écrit ni la consigne, ni le texte scellé, ni le code, par le programme`
→ nouveau : `- **Application** : par le rédacteur des corrections (modèle A), qui n'a pas écrit le texte scellé ni le code, par le programme`
(les deux lignes anciennes deviennent une seule ligne).

Couple 3 (puce « Réponse » m1, cinq lignes, de `  - m1 (puce « Application » du tour 1 de la v3, modèle du rédacteur) : appliquée **avec une adaptation**.` à `seule : la puce dit les deux lectures et renvoie à la mère (point 1 du rapport). Le reste de la puce est inchangé.`) :
→ nouveau : `  - m1 (puce « Application » du tour 1 de la v3, modèle du rédacteur) : appliquée avec la variante du rapport (« le rédacteur des corrections (modèle A) »), la mère ayant confirmé que les corrections sont écrites par le modèle A ; le reste de la puce est inchangé.`

## Remarques facultatives

- F1 à F3 des tours précédents restent applicables, non exigées.
- Si la mère préfère garder l'aveu de doute dans la pièce, elle l'écrit comme un écart assumé : le verdict reste « corrections » car la
  pièce ne peut être scellée avec une question ouverte adressée à la mère.

## Points pour la mère

1. Confirmer qui a appliqué la v3 → v4 (A ou C) ; cette tâche dit A pour la v4 → v5. Aucune correction si C et neuf.
2. Aucun écart au texte scellé, aucune dépense, aucun mot du directeur nécessaire.
3. Inchangés : tolérance des clés de proposeurs `fable52`/`opus55` dans les noms de fichiers ; donner au lecteur la version de `numpy` (au moins 1.25) ;
   produire et sceller la sortie du programme de dépense (`--machine`, `--autre`) avant remise, code 3 dit.

## Incidents de ma main

Un premier jet de ce rapport, scellé avec une heure erronée (14:46Z au lieu de 14:43Z), a été supprimé par moi (fichier et compagnon, tous deux de ma main) puis réécrit à l'identique avec l'heure lue. Un `git fetch` avec refspec ; noms et tailles seulement dans `retour/` ; aucune pièce de la copie ni de la branche de sortie ouverte ; aucune clé ; aucun calcul lourd.
