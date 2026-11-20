# Vérification des corrections du brouillon 6 de la version 2 du préenregistrement « lecture des sondes de l'étape B bis par lentilles » — v1

- **Vérificateur** : le contre-lecteur des brouillons 4 et 5 (rapports `08a698577a952669dd3cd75fa7d7bcb7447a5b1e795106b322bf0e377792c17b`
  et `04282064d10c6cdd2a4266bf9e5a526c9835463476108dec8a54dfcae2f64328`), sous-agent de la session des lentilles
  (`session_01XJ6Mgr9o68QqLiFTLg3zRW`), modèle **Claude Opus 5.5** (`claude-opus-5-5`) ; le rédacteur du brouillon 6 est sur
  Fable 5.2. Même mandat et même cloisonnement que pour la contre-lecture 4 (`…/mandat-contre-lecteur-texte-lecture-v2-brouillon4-v1.md`,
  `85d3c1bb…`), sur l'ordre de la session des lentilles ; dans les registres de la branche principale, seules les lignes cherchées
  par leur identifiant ont été lues.
- **Heures (UTC, `date -u`)** : 2026-11-20 ; début 05:36:16 ; `git fetch origin main` à 05:36 (tête `97f6a0b9…`, datée 05:34:13Z) ;
  fin relevée au pied.
- **Pièce vérifiée** : `prereg/lecture-sondes-bbis-par-lentilles-v2-brouillon6.md`,
  `f707bced9c7fb1605e99250797cfc52a178f58fe2633772778e72a780a963000` (2 999 lignes ; commit `3aa32083` ; compagnon « OK »).

## Pièces lues, empreintes recalculées (égales à l'ordre reçu et aux compagnons)

| pièce | empreinte | lu |
|---|---|---|
| brouillon 6 | `f707bced9c7f…` | par la sortie des couples (tous les textes changés), puis par passages et recherches |
| brouillon 5 | `88a2011a8b9e…` | par programme |
| mandat du rédacteur du brouillon 6, `…/mandats/mandat-redacteur-texte-lecture-v2-brouillon6-v1.md` | `7cc8a455f3a2…` | section « Texte du mandat », tâches |
| `couples-brouillon5-vers-brouillon6-v1.py` | `259191df8782…` | rejoué ; lu par sa sortie |
| `sortie-couples-brouillon5-vers-brouillon6-v1.txt` | `6bc4cd360067…` | en entier (rejouée) |
| `diff-brouillon5-vers-brouillon6-v1.txt` | `05dbfabbe881…` | recalculé, égal à l'octet |
| note du mot de Lazar sur N12 et N17, `docs/notes/neuron-lens-v1/mot-lazar-noeuds-n12-n17-et-brouillon6-2026-11-20-v1.md` | `cd02b0fb85e0…` | en entier |
| ma vérification du brouillon 5 | `04282064d10c…` | relue pour les corrections |
| `origin/main:registres/go.md` | — | lignes GO-2026-11-20-17 et GO-2026-11-20-18, cherchées par leur identifiant |
| `origin/main:registres/decisions.md` | — | ligne R-4104, cherchée par son identifiant |
| critère d'identité v8 | `541bb86b1508…` | phrases du § 5, par programme |
| v1 scellée | `ca5066d757df…` | par programme seul |
| validateur `src/controle_ia/prereg.py` | `3b2e3ee56463…` | relancé |

Non lu : le brouillon 6 en entier ; la note `f28f18ae…` (relevée par l'index des empreintes). Vu sans ouvrir : aucun fichier
cloisonné. **Refus d'outil : aucun.**

## Exposition (R4)
Aucune ligne de V (verdict de la tranche) ouverte ici. Dans les registres, les trois seules lignes cherchées par leur identifiant
(GO-2026-11-20-17, GO-2026-11-20-18, R-4104) : toutes de cette chaîne, noms, heures et événements. Aucune ligne d'une autre
chaîne n'a été vue. Rien de la chaîne des sondes.

## Conclusion

**Scellable après corrections** : **une seule correction exigée, R1, le remplacement du marqueur
`LIGNE_D_ACCORD_DES_NOEUDS_N12_ET_N17` par la citation de GO-2026-11-20-18**, texte exact ci-dessous ; **la session principale
peut la porter elle-même au scellement, comme simple remplacement de marqueur** : le texte proposé fixe aussi l'heure que la
pièce de `GO-LENTILLES-BBIS-V2` doit recopier, ce que le brouillon 6 laissait ouvert. Une correction recommandée, R2 (citation de
GO-2026-11-20-17 pour M6), hors d'un marqueur : couple exact que la session principale peut porter par programme, avec un
contrôle du différentiel ; laissée telle quelle, la phrase reste vraie à sa date. **Aucun brouillon de plus n'est nécessaire.**
C1 et M1 à M6 sont faites ; N12 et N17 sont écrits tranchés partout ; le bloc séparable est égal à l'octet ; le script rejoué
redonne le brouillon 6 à l'octet.

## Verdict par point

### 1. C1 et M1 à M6

| objet | verdict | lieux (brouillon 6) |
|---|---|---|
| C1 issue de N12 et N17 avant le scellement | **corrigée, adaptée à des nœuds tranchés** : issue fixée par le texte ; la pièce ne fait que recopier ; arrêt nommé sur une autre issue, une ligne d'accord non strictement antérieure à `SCELLEMENT-LENTILLES-BBIS-V2`, ou une autre forme ; essais | « Lignes de registre », l. 2409-2425 ; « Liste d'arrêt », l. 2243 ; essais, l. 2620-2631 ; « Entrées » ; « Nœuds », l. 2700-2712 |
| M1 couples pour le lecteur désigné | **corrigée** : L16 à L19, et L12 et L15 pour information | bloc « Brouillon 5 », « Reste à faire » ; « Contre-lecture », entrée 4 |
| M2 formes de la phrase du déclencheur (vi) | **corrigée** : « séries … inchangées » et les deux faits joints par « et », dans les deux ordres ; arrêt et essais accordés | fiche ; « Liste d'arrêt » ; essais |
| M3 passe encore en cours ; tables sans entrées | **corrigée**, dans mes mots ; ligne d'arrêt et essai ajoutés | plan, point 11 ; « Liste d'arrêt » ; essais |
| M4 lentille des logits | **corrigée** | « Métrique », point 6 |
| M5 description de `GO-LENTILLES-BBIS-V2` | **corrigée** aux deux lieux | plan, point 1 (i), l. 1798 ; « Lignes de registre », l. 2397 |
| M6 mot de départ du rédacteur du brouillon 5 | **corrigée à sa date** (mot rapporté, aucune ligne au commit `8ba3c932…`) ; **dépassée depuis** : GO-2026-11-20-17 le consigne → R2 | bloc « Brouillon 5 », « Auteur », l. 181-186 |

### 2. N12 et N17 tranchés — **formes conditionnelles retirées partout ; clé retirée sans trou ; aucune marge après coup**
- Recherche de « option (b) », « option (c) », « si (b) », « sous l'option », « défaut échu », « laissé ouvert », « reste à
  trancher », « N17, ouvert », « addendum de recopie », `ADDENDUM-RECOPIE-IDENTITE-LENTILLES-BBIS-V2` : hors du bloc de tête du
  brouillon 6 qui les énumère, elles ne restent que (i) dans les blocs « Brouillon 4 » et « Brouillon 5 » et dans des lignes
  d'histoire que le bloc de tête dit laissées et remplacées (l. 272, 294, 304, 313, 429, 774), (ii) dans le texte des nœuds
  « tel qu'il a été posé, gardé pour mémoire » (l. 2715-2735), suivi chaque fois de l'issue retenue, et (iii) pour dire qu'elles
  sont retirées (l. 1486-1490, 2424-2425, 2630-2631, 2738-2741, 2788). Aucune règle conditionnelle ne reste.
- La phrase « Si Lazar ou la session principale lit CI comme exigeant un texte écrit **après** le verdict d'identité, c'est une
  version neuve (nœud N17, ouvert) » est retirée avec le reste (couple P11) : juste, N17 (a) l'écarte.
- La clé retirée laisse : la condition de lecture et son motif, le cas d'arrêt, la clé conditionnelle, ses essais, la ligne 28
  des changements (dite remplacée) ; l'essai neuf vérifie qu'aucun code ne l'exige. Aucun renvoi vers elle ne reste ouvert.
- **Marge restante** : aucune. Le seul mot de Lazar encore attendu, sous N12 (a), ouvre ou non la lecture d'une lentille déjà
  écrite ; il ne choisit aucune branche, et le texte le dit (l. 1448-1459). C'est l'option que Lazar a retenue, conforme au
  critère v8 (§ 5).

### 3. Fabrication — **saine**
Rejeu : code 0 ; brouillon 6 égal à l'octet ; sortie égale hors les deux lignes de chemin ; `diff` égal à l'octet. 32 couples,
chaque « avant » unique. La différence mot à mot de chaque couple ne retire rien hors des lieux que le bloc de tête liste (lieux
des brouillons 1 à 5 réécrits, un à un). Commits cités : `2cdb7b28` (05:22:01Z), `d05179e3` (05:22:20Z), `b5486e67` (05:28:09Z),
`8ba3c932` (05:31:23Z, ancêtre de la branche principale) : exacts. Empreintes des lignes neuves : 4 entières et 10 préfixes,
toutes sur la pièce nommée, hors ces commits.

### 4. Les neuf choix du rédacteur

| choix | jugement |
|---|---|
| (1) pièce muette qui n'arrête pas, phrase fixée en tête | **tenable** : l'issue est celle du texte, la phrase le dit |
| (2) forme de la ligne recopiée, heure à la seconde, arrêt si non strictement antérieure | **tenable, à préciser** : la ligne GO-2026-11-20-18 ne porte qu'une date ; l'heure d'inscription est celle de R-4104 (05:34:13Z), l'heure du mot relu 05:20:51Z. Le remplacement du marqueur (R1) dit laquelle est recopiée |
| (3) le code ne lit aucune option | **tenable**, c'est ce que C1 demandait |
| (4) marqueur entre doubles chevrons, une fois | **tenable** ; il se remplit maintenant (R1) |
| (5) M2 dans les deux ordres | **tenable** ; essais présents (« la même forme deux fois », « autre mot que « et » » : arrêt) |
| (6) M3 sans réécrire la phrase de tête | **tenable** ; réserve de lettre : pour une passe en cours, la phrase écrite en tête dit « avant le nœud de la v1 », alors qu'il n'y en a pas ; le plan, point 11, le précise ; un brouillon de plus pour cela ne se justifie pas |
| (7) clé retirée, ni exigée ni lue | **tenable** |
| (8) histoire des blocs des brouillons 2, 4 et 5 laissée et dite remplacée | **tenable** : le bloc de tête la liste et dit qu'elle ne vaut plus |
| (9) registre de la ligne d'accord non nommé | **tenable** ; la ligne est dans `registres/go.md`, R1 le nomme |

### 5. Bloc séparable — **égal à l'octet à celui du brouillon 5**
De la ligne de début à la ligne de fin comprises (l. 1189 à 1238), égal à l'octet ; une occurrence de chaque borne. Aucun couple
du brouillon 6 n'y touche ; rien de neuf pour le lecteur désigné, qui reçoit les couples du brouillon 5 (L16 à L19, L12 et L15).

### 6. Validateur
`PYTHONPATH=src .venv/bin/python -c "from controle_ia import prereg; print(prereg.problemes('prereg/lecture-sondes-bbis-par-lentilles-v2-brouillon6.md'))"` :
`['contre-lecture 4 sans ses deux empreintes (brouillon relu et rapport)', 'marqueurs de gabarit restants : <<CONTRE_LECTURE_4>>, <<CONTRE_LECTURE_ET_SCELLEMENT_DU_CRITERE>>, <<DECISION_DATEE_DE_LA_RETENUE>>, <<DECLARATION_DE_LAZAR_SUR_LE_VERDICT>>, <<DECLARATION_DE_LA_SESSION_DES_LENTILLES>>, <<DECLARATION_DE_LA_SESSION_PRINCIPALE>>, <<DIFFERENCES_DU_BROUILLON_2_A_LA_VERSION>>, <<ETAT_DE_LA_PREMIERE_PASSE_AU_SCELLEMENT>>, <<ETAT_DU_REGISTRE_PROPRE_A_L_ANCRE>>, <<LIGNE_D_ACCORD_DES_NOEUDS_N12_ET_N17>>']`
Dix marqueurs, ceux attendus ; aucune section absente ou vide.

### Autres contrôles
Phrases permises égales au critère v8 (cinq formes ; « S seule » égale à sa construction). Lignes de la v1 : `791 0 23 1098`,
mêmes 13 réécrites et 10 prolongées, 813 lignes : conforme au pied.

## Corrections

### R1 — remplacement du marqueur de la ligne d'accord (exigée ; la session principale peut la porter seule)
Lignes de la branche principale, lues par leur identifiant : GO-2026-11-20-18 (`registres/go.md`, l. 548) ; R-4104
(`registres/decisions.md`, 2026-11-20T05:34:13Z).
- **Ligne 2706.** Avant : « principale : <<LIGNE_D_ACCORD_DES_NOEUDS_N12_ET_N17>> (cherchée par le rédacteur du brouillon 6 dans
  `registres/go.md` et »
  Après : « principale : ligne **GO-2026-11-20-18** de `registres/go.md` (branche principale), dont l'objet est « Lentilles,
  texte de lecture v2 : nœuds N12 et N17 tranchés selon les recommandations, et départ du rédacteur du brouillon 6. N12 (a) : mot
  de Lazar postérieur à l'avertissement de l'écart mesuré (ligne NOEUD-PALIER-2-AJUSTEMENT-SEUL-LENTILLES-BBIS). N17 (a), aux deux
  paliers : ce texte vaut le texte de lecture neuf exigé par le critère d'identité, sans addendum de recopie. » ; mot relu à la
  source par la session principale (événement `3961f2f8-7eb1-48a4-974a-94796f174168`, 2026-11-20T05:20:51Z) ; inscrite par la
  ligne R-4104 de `registres/decisions.md` le **2026-11-20 à 05:34:13Z**, heure que recopie la pièce de `GO-LENTILLES-BBIS-V2`
  (« Lignes de registre » : « ligne d'accord GO-2026-11-20-18, 2026-11-20T05:34:13Z ») (cherchée par le rédacteur du brouillon 6 dans
  `registres/go.md` et »
  La suite de la parenthèse (« … au commit `8ba3c932…` : non trouvée ; marqueur porté par la session principale, avant le
  scellement) ») reste : elle dit ce qui était vrai à l'écriture du brouillon 6.
- **Cela suffit** : l'identifiant et l'heure sont fixés dans le texte ; « Lignes de registre » (l. 2412-2415) dit déjà que la pièce
  recopie « l'identifiant et l'heure […] de la ligne par laquelle la session principale inscrit l'accord », que le remplacement
  ci-dessus nomme ; l'arrêt de « Liste d'arrêt » (l. 2243) et l'essai (l. 2620-2626) s'appliquent tels quels. La table des
  marqueurs (l. 650 et 663) se met à jour comme pour les neuf autres marqueurs que la session principale porte au scellement.

### R2 — citation de GO-2026-11-20-17 pour M6 (recommandée ; hors d'un marqueur)
- **Lignes 184-186** (« avant » trouvé une fois, sauts de ligne compris). Avant : « il est donc consigné ici comme **mot rapporté** par la session des lentilles et sa note, citée
  seule ; il ouvrait un travail sans dépense ; la session principale peut le consigner, comme elle l'a fait à la ligne R-3994 pour
  le mot du brouillon 4 ; vérification des corrections du brouillon 5, M6) »
  Après : « il était donc consigné ici comme mot rapporté ; **il a été consigné depuis** par la session principale, qui l'a relu à
  la source (événement `a8e8cd06-decf-403f-911c-0664833286ff`, 2026-11-19T23:46:53Z) : ligne **GO-2026-11-20-17** de
  `registres/go.md`, « départ du rédacteur Fable du brouillon 5 sans attendre les défauts de N12 et N17 », inscrite par la ligne
  R-4104 de `registres/decisions.md` (2026-11-20T05:34:13Z) ; vérification des corrections du brouillon 5, M6) »
- **Qui la porte** : ce n'est pas un marqueur ; la session principale peut l'appliquer au scellement comme couple exact, par
  programme (« avant » trouvé une fois), avec un contrôle de son différentiel, comme pour l'addendum de concentration. Laissée,
  la phrase reste vraie à sa date (« au commit `8ba3c932…` ») et ne touche aucune règle : ce n'est pas un motif de brouillon de plus.

## Nœuds pour Lazar
Aucun. N12 (a) et N17 (a) aux deux paliers sont tranchés et inscrits (GO-2026-11-20-18) ; N18 tranché, N19 clos. Pour
information au scellement, inchangé : la règle sur une première passe lancée et non achevée ; et, sous N12 (a), un mot de Lazar
sera à demander après l'avertissement si une de nos lentilles sort au deuxième palier sans mesure propre.

## Annexe — programmes (bloc-notes de la session des lentilles, dossier `contre-lecteur-brouillon4/`)
Rejeu du script : `b6/` (copie du script, `b6.md`, `sortie.txt`, `diff.txt`). Rejoués sur le brouillon 6 :
`outils/phrases_v1.py`, `outils/controle_v1_annexe_b.py`, `outils/empreintes_v1.py` (index hors chemins cloisonnés),
`outils/mots_couples_v1.py` ; égalité du bloc séparable par un programme court. Aucune écriture dans le dépôt hors ce rapport.

## Refus d'outil
Aucun.

Rien de cloisonné n'a été ouvert : ni la liste « Jamais ouverts » de la v1, ni aucune sortie, score, table, lecture ou verdict de
l'apprentissage des sondes sur la tâche, ni table ou sortie de la lentille publique, ni branche `donnees/*` ou `calcul/*`, ni
`diag/`, `runs/`, `docs/verdicts/`, fichier « consigne-privee » ou « conception-ii-b », ni `brouillons/ii-b-saboteur-budget-v1/`, ni
P3, P3-bis, T0.6, T0.7 hors ce texte, l'étape B, le bras d'attaque ou le saboteur à budget. Aucun commit, aucun push, aucune
machine, aucune dépense, aucun modèle chargé ; réseau : `git fetch origin main` seul.

Pied : vérification achevée le 2026-11-20 à 05:41:36 UTC (`date -u`).
