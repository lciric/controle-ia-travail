# Contre-lecture de la consigne du lecteur de l'issue du pilote MR-2 (procédure v14), v6 — tour 1 — v1

Contre-lecteur neuf (R2), modèle C ; auteur de la pièce : modèle A. Rapport écrit le 2026-11-16T15:26Z (`date -u`, lu à 15:25Z, juste
avant l'écriture et le scellement).
Pièce lue en entier : `consigne-lecteur-issue-pilote-v14-v6.md`, empreinte `0fcd736cc30e…` (égale à son compagnon ; douze premiers
caractères relus). Empreintes recalculées, toutes égales à leur compagnon : v1 `5189c442`, v2 `0e12acbd`, v3 `f06f46b3`, v4 `de826db5`,
v5 `05f4f325` ; rapports `14725e82`, `8c020f41`, `27269e92`, `98332a74`, `d0019ab6`. Texte scellé (branche
`prep/pilote-mr2-compte-organisme-v1`) : `8aa33014667da569ec934459d7bc1b1f6b54efa5c2145a6e5bdce5f7fa74603e`, égale. Programme de
dépense (`dbe3d24e`) : `9866e611d7997c32eba82cf308dbed1c2ccf184992f106811b2623357dc88643`, égale. Sortie de dépense (`2f7acc1d`) :
`53c72308bb30adcce5602ad18b47f2e7325a22a295264c143ed52ff46f349ce2`, égale à son compagnon ; commits `dbe3d24e` et `2f7acc1d` existent
et sont ancêtres de `lot/compte-organisme-v1`. Le sommet `69275b74` de la branche de sortie n'a pas été relu (branche interdite) : il est
celui que donne R-2981.

## Verdict : corrections

Aucune majeure ; quatre mineures exigées ; six remarques facultatives. La passe v5 → v6 applique fidèlement la correction exigée au tour 3
(m1, trois couples) et les trois décisions de la mère portées au corps (pièce de dépense, sommet final, section « Pour les cribles ») ;
la conception tient. Restent des précisions de lecture (deux chemins de champs, la comparaison des modules, une condition de phrase) et
une question laissée ouverte à la mère dans la pièce, que la décision R-2992 (point 0) permet de fermer.

## A. Différentiel v5 → v6 (`diff`, lu en entier)

Dix zones, toutes déclarées : titre ; ligne 3 (version 6, 15:07:46Z, empreintes des versions précédentes exactes) ; point 2 des pièces
(sommet `69275b74`, R-2981) ; point 4 des pièces (sortie de dépense nommée, `53c72308…`, `2f7acc1d`) ; liste de « Ce qu'il rend »
(renvoi à « Pour les cribles ») ; paragraphe « Pour les cribles » ; puce « Application » du tour 1 de la v3 et du tour 2 de la v3
(couples 1 et 2) ; réponse m1 (couple 3, avec la variante du rapport) ; sous-section « Tour 3 de la v3 » ajoutée en fin. Rien d'autre :
le corps des points 0 à 7 est inchangé à l'octet. Le programme `appliquer-…-v6.py` fait exactement ces remplacements. Les trois couples du
tour 3 sont appliqués mot pour mot ; la puce « Application » du tour 1 (« modèle C ») est volontairement non touchée (voir m3).

## B. Vérifications (1) à (8)

**(1) Fidélité au texte scellé.** Les points 0 à 7 appliquent « Métrique », « Seuil », « Plan d'analyse » (1 empreintes, 2 mesure une
seule fois, 3 issue par la table, 4 coûts, 5 exclusions, 6 phrases), « Critères de lecture gelés » (table, première ligne, « ce qui
suit »), « Audit de symétrie » et « Liste d'arrêt », dans l'ordre. Empreintes citées contre le texte : `676d5f37…` (programme de mesure,
bloc gelé) ; parts 12, 8, 9,36, 9,36, machine 3, lignes π1 20 et π2 21,72 (bloc gelé, `ligne-de-go`) ; taux d'erreur (0,20 ; 0,26 ;
0,22 et 0,21 ; 0,29 et 0,27) égaux à la section « Prédiction chiffrée » ; chaînes de l'audit R4 (« déclenché : x = 0 », « déclenché : x ≥ 3 »,
« non déclenché ») égales à `mesure_pilote_v4.py` (ligne 470) ; champ `audit_R4` est une chaîne. Ajouts de la consigne par rapport au texte,
tous justifiés par la procédure v14 et acceptés aux tours précédents (voir F4) : contrôle des empreintes du secret et de la phrase
contre le registre, états de la machine, codes d'étape. Précisions à faire : m1 et m2 ci-dessous.

**(2) Pièces remises.** Noms et tailles seulement dans `retour/` : présents tous les noms de la consigne : `etat.txt`, `lancements.jsonl`
(une ligne, 158 octets), `engagement-mondes.json`, `secret-sha256.txt`, `phrase-sha256.txt`, les sept `code-*.txt` (06, 07, 08-blanc, 09-reel,
10-mesurer, 10-lire, 11-rapatrier), `journal-09-reel.txt`, `journal-10-mesurer.txt`, `remis-au-sous-agent/sortie-lire-non-ouverte.txt` ;
dans `rapatrie-reel/` : `lecture-pilote-v70.json`, `sortie-mesure-pilote-v70.json`, `mesure-pilote-v70.json`, `manifeste-pilote-v70.json`,
`releve-pilote-v70.json`, `CARTES.json`, `liste-rapatriement-pilote-v70.json`, quatre `journal-relais-*.jsonl`, quatre dossiers
`monde-N` × quatre proposeurs × (réponse brute, corps du relais, témoin d'isolement) soit 16 et 16 et 16, tous avec leur compagnon ;
compagnons présents pour lecture, sortie de mesure, mesure, manifeste, relevé, `CARTES.json`. Pas de `CARTES-partiel.json`. `journal-09-reel-2`
absent (le « ou » de la consigne le prévoit). `rapatrie-blanc/` existe et n'est pas nommé comme remis. Aucun monde, aucun fichier privé,
aucune clé privée dans la liste. Les prix de la configuration ne sont pas nécessaires : le programme de dépense ne lit que
`releve-pilote-v70.json` (`depense_usd`, `appels[].cout_usd`, `proposeur`, `appele`, `etat`) et `journal-relais-<proposeur>.jsonl`
(`cout_usd`, `au_dessus_du_pire_cas`), relu sur le code. Aucune pièce nécessaire ne manque : l'audit du point 7 lit les épisodes servis
dans `corps-relais.json` et les gabarits dans les témoins ; les empreintes du bloc gelé sont dans le texte remis.

**(3) Lecture de l'issue.** `lecture-pilote-v70.json` porte bien `regle` (le code de `lire` écrit `regle`, `issue`, `mode`,
`amont_boucle_locale`, `sortie_mesure_sha256`, `releve_sha256`, `couts`, `a_dire_au_rapport` ; relu sur le différentiel v69 → v70 du code,
non sur la sortie réelle), tandis que la sortie imprimée de `lire` (donc `sortie-lire-non-ouverte.txt`) est plate (`issue`, `texte`, `noeuds`,
`mode`, `ecarts_de_cout`) : la consigne dit juste. `regle` contient `issue`, `classe`, `noeuds_avant_banc`, `texte` ; « P-2 avec réserve » =
`issue` P-2 et `noeuds_avant_banc` non vide : exact (cas R-1 de la répétition). Table et « ce qui suit » : mot pour mot, nœuds appelés.

**(4) Arrêts.** Tout écart d'empreinte, de code, d'état, de compte ou de part arrête avant la lecture de `lecture-pilote-v70.json` et de
`sortie-lire-non-ouverte.txt` ; la sortie de mesure ne s'ouvre avant la fin des points 0 et 1 que pour `hors_corps` et
`corps.mondes_sha256` ; un contrôle impossible est « non fait » avec sa cause et vaut arrêt aux points 0 à 2 (R5), « non fait » sans arrêt
au point 7. Conforme à « Tout arrêt (code 3) après le premier appel » (aucune issue lue, pas même P-0) et à « Dépense d'un fournisseur
atteignant sa part → arrêt » (inégalité stricte, plus sévère que `sous_la_part` du programme, qui est `≤` : écart assumé et écrit).

**(5) Rendu.** Verdict scellé, en français, sans identifiant de modèle ni identifiant servi (R-2731), fichier neuf sur une branche désignée
par la mère, rien d'autre écrit (le compagnon de sceau mis à part, F5). Conforme.

**(6) Dépense : quelle voie.** La consigne fixe la voie « reçue » : le lecteur reçoit la sortie JSON déjà produite et scellée par le
compte organisme (`depense-pilote-v14-v1.json`, `53c72308…`, commit `2f7acc1d`) ; il ne rejoue pas le programme (qui écrit un fichier de
sortie, donc interdit par « aucun programme qui écrit hors de son fichier de verdict », et exige `--machine` et `--autre` qu'il ne peut
vérifier) ; il vérifie l'empreinte du programme et de la sortie, recoupe par lecture les sommes du relevé et des journaux, rapporte les
arguments recopiés (`machine` : prix horaire 0,052222 USD/h, création 11:26:57Z, destruction 13:01:11Z ; `autres` : épreuve des clés
0,001164 et machine de la tentative v13 0,074757, lus pour confirmer que les champs existent), et ne recalcule aucun prix. C'est la voie à
garder. Le programme ne lit que le relevé et les journaux des relais ; il n'ouvre ni la lecture, ni la sortie de mesure, ni
`mesure-pilote-v70.json` (`fichiers_non_ouverts` vide dans la sortie : cohérent). Note : la sortie de dépense est sur
`lot/compte-organisme-v1`, non sur `main` ; la mère doit la remettre (la consigne en donne le chemin et le commit).

**(7) Symétrie R4.** Telle que le texte la gèle : x = 0 (cartes refusées, au-delà de six, non évaluables, trois cartes par appel,
épisodes, témoins) et x ≥ 3 (cartes qui portent, pièces servies, isolement, refusées et non évaluables) ; champ absent pour P-0 ; l'audit
commente, ne change pas l'issue. Les précisions du tirage (graine, générateur, ordre, indices, version de `numpy` rapportée) sont des
précisions déclarées, non un écart. `CARTES.json` liste bien un `appels` (monde, proposeur, état) et des `cartes` à plat (monde, proposeur,
emplacement, état, loi) : « toutes celles que `CARTES.json` lui attribue, dans l'ordre où il les liste » est déterminé.

**(8) Identifiants de modèle.** Aucun dans la pièce : lettres A, B, C ; clés de proposeurs (`fable52`, `opus55`, `argon`, `astra`)
seulement, tolérées par R-2690. Empreintes citées : toutes exactes (voir en tête).

## Corrections exigées (chaque « ancien » figure une seule fois dans la v6)

Aucune majeure. Quatre mineures.

**m1 (chemins des empreintes de mondes dans le manifeste).** Dans le manifeste, `fichier_mondes_sha256` et `mondes_sha256` sont sous
`controles.mondes` (et `mondes_sha256` est indexé par numéro de monde, « 1 » à « 4 »), non à la racine ; `mesure-pilote-v70.json` porte
aussi un `fichier_mondes_sha256` à la racine, d'où un risque de confusion (lu sur la répétition locale et sur le code de `lire`).

Couple 1 :
ancien : `` `fichier_mondes_sha256` du manifeste égal à `H` inscrit ``
→ nouveau : `` `controles.mondes.fichier_mondes_sha256` du manifeste égal à `H` inscrit ``

Couple 2 :
ancien : `` empreintes de mondes égales à `S1` à `S4` (la liste ``
→ nouveau : `` empreintes de mondes (`controles.mondes.mondes_sha256` du manifeste, indexé par numéro de monde : le monde k égal à `Sk`) égales à `S1` à `S4` (la liste ``

**m2 (comparaison de `modules_importes` au bloc gelé, S-c).** La liste `hors_corps.modules_importes` compte 13 couples [chemin relatif à
`orchestrator/mr2_v68/`, empreinte] ; le bloc gelé compte 31 lignes dont exactement 13 sous `orchestrator/mr2_v68/` (le code de `lire`
refuse un écart avec « les 13 fichiers portés »). « Comparée au bloc gelé » ne dit pas laquelle des deux listes contient l'autre ni quel
préfixe ôter ; un lecteur pourrait conclure à tort à un écart (13 contre 31) ou à une égalité.

ancien : `` liste `hors_corps.modules_importes` de la sortie de mesure comparée au bloc ``
→ nouveau : `` liste `hors_corps.modules_importes` de la sortie de mesure (13 couples [chemin relatif à `orchestrator/mr2_v68/`, empreinte]) comparée, comme ensemble, aux 13 lignes `orchestrator/mr2_v68/…` du bloc ``

**m3 (question ouverte à la mère laissée dans la pièce).** La décision R-2992 (point 0, 14:52Z) dit fausses les mentions « rédacteur lettre C »
des rédacteurs de corrections lancés au modèle A et demande de les corriger « dans les versions qui feront foi » ; la v6, écrite après,
laisse la puce du tour 1 (« rédacteur neuf (modèle C), qui n'a écrit ni la v1… ») et une puce « Non touchée » qui renvoie la question à la
mère. Une pièce à sceller ne doit pas porter une question ouverte adressée à la mère ; et « n'a écrit ni la v1 » est faux pour le modèle A,
auteur de la consigne. **Condition : la mère confirme que la passe v1 → v2 a bien été appliquée par un rédacteur lancé au modèle A**
(R-2992 point 0 le dit pour tous les rédacteurs de corrections ; sinon, laisser la puce et supprimer seulement la question, voir point 2 du
rapport). Deux couples.

Couple 1 :
ancien : `` - **Application** : par un rédacteur neuf (modèle C), qui n'a écrit ni la v1, ni le texte scellé, ni le code, par le programme ``
→ nouveau : `` - **Application** : par le rédacteur des corrections (modèle A), qui n'a pas écrit le texte scellé ni le code, par le programme ``

Couple 2 (puce de trois lignes, de `  - Non touchée` à `mère de dire si celle-ci en est une.`) :
ancien :
```
  - Non touchée : la puce « Application » du tour 1 (« rédacteur neuf (modèle C) »), que ni ce rapport ni les décisions
    transmises ne nomment ; R-2992 (point 0) dit fausses les mentions « lettre C » des rédacteurs lancés au modèle A : à la
    mère de dire si celle-ci en est une.
```
→ nouveau :
```
  - Rectifiée : la puce « Application » du tour 1, qui disait « rédacteur neuf (modèle C) », dit désormais « le rédacteur des
    corrections (modèle A) » : R-2992 (point 0) tient fausses les mentions « lettre C » des rédacteurs de corrections lancés au
    modèle A.
```

**m4 (condition de la phrase du point 6).** Le texte scellé écrit « Une issue P-2 favorable ne dit pas que… » (section « Critères de
lecture gelés ») ; la consigne la fait écrire « si l'issue est P-2 », donc aussi pour un P-2 défavorable (x ≥ 3), où la phrase est
sans objet. `regle.classe` vaut « favorable » ou « défavorable » (lu sur la répétition).

ancien : `` et, si l'issue est P-2, la phrase ``
→ nouveau : `` et, si l'issue est P-2 (avec ou sans réserve) et que `regle.classe` vaut « favorable », la phrase ``

## Remarques facultatives (non exigées)

- **F1.** `remis-au-sous-agent/sortie-lire-non-ouverte.txt` est remise mais la consigne ne dit pas à quoi elle sert au lecteur. Proposition :
  au point 3, comparer `issue` et `noeuds` de cette sortie plate à `regle.issue` et `regle.noeuds_avant_banc` de la lecture et à
  `corps.regle` de la sortie de mesure ; tout désaccord est rapporté et vaut arrêt de lecture (« non fait » sinon).
- **F2.** Point 4 : « recoupe lui-même, par lecture, les sommes » et « ne recalcule aucun coût » se lisent bien (additionner les
  `cout_usd` déjà présents, sans prix ni jetons) ; une demi-phrase le dirait.
- **F3.** « Pour les cribles », cas d'arrêt : les `duree_s` du relevé et les `debut_utc`/`fin_utc` du manifeste sont lus alors que le
  point 0 limite le relevé et le manifeste à leurs champs de contrôle ; ils ne portent aucune issue, une demi-phrase lèverait le doute.
- **F4.** Le contrôle des empreintes du secret et de la phrase contre le registre n'est pas dans « Plan d'analyse » ni dans « Liste
  d'arrêt » du texte scellé (il vient de « Dessin » et « Ordre » : empreintes inscrites, et de la procédure v14, section 5) ; accepté
  aux tours précédents, signalé ici pour que la mère sache que c'est un arrêt ajouté.
- **F5.** Le sceau écrit un compagnon `.sha256` à côté du verdict : « rien d'autre n'étant écrit » s'entend hors ce compagnon.
- **F6.** `engagement-mondes.json` porte aussi `texte_sha256` (répétition locale) : l'égaler à `8aa33014…`, et vérifier que `mode` vaut
  `reel` dans le manifeste et la lecture, coûte une ligne et écarte une confusion avec `rapatrie-blanc/`.

## Points pour la mère

1. **R-2992, point 0 et m3 :** confirmer que la passe v1 → v2 a été appliquée par un rédacteur lancé au modèle A ; sinon, ne remplacer que la
   question ouverte, pas la lettre.
2. Aucun écart au texte scellé ; aucune dépense ; aucun mot du directeur nécessaire.
3. Remettre au lecteur la sortie de dépense `depense-pilote-v14-v1.json` (elle est sur `lot/compte-organisme-v1`, non sur `main`), avec son
   compagnon et le programme `depense_pilote_v14_v1.py`, et donner le code de sortie 3 ou 0 du programme si elle le sait (R-2983 chiffre
   π1 et π2 sous leurs lignes) ; donner aussi la version de `numpy` au lecteur (1,25 au moins ; le bloc gelé exige 2.5.3 pour la machine).
4. Une fois les quatre couples appliqués : un contrôle différentiel suffit (aucune majeure en jeu).

## Incidents de ma main

Aucun fichier de `retour/` ni de la branche de sortie ouvert (noms et tailles seulement). Un listage de noms de fichiers de la branche
`prep/pilote-mr2-compte-organisme-v1` (filtre par mots « bundle, rapport, lecture ») a fait défiler des noms de brouillons « P3-bis » :
noms seulement, aucun ouvert, rien lu. Lus pour la vérification, hors zones interdites : pièces de la répétition locale du commit `2d35cafa`
(noms de champs et quelques valeurs de la répétition), différentiel du code v69 → v70 (fonction `lire`), sortie de dépense `53c72308…` (noms
de clés, champs `machine`, `autres`, `fichiers_non_ouverts`). Un `git fetch` avec refspec (deux, pour `prep/…` et `lot/compte-organisme-v1`) ;
aucun clone ; aucune clé ; aucun calcul lourd ; aucun test.
