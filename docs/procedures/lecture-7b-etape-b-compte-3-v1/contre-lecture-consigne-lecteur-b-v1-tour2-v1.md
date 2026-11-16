# Contre-lecture de la consigne du lecteur B (brouillon 4) — tour 2 — v1

- **Pièce contre-lue** : `docs/procedures/lecture-7b-etape-b-compte-3-v1/consigne-lecteur-b-v1-brouillon4.md`
  (`ce397083f351d21fbf72a72b7b1c14a1e5acc6744ac1de762e38f5eb9fe313ab`, 1 076 lignes, égale à son compagnon), par différentiel
  contre `consigne-lecteur-b-v1-brouillon3.md` (`12881d63…`), puis relecture des passages touchés et des passages que les
  corrections ont pu déranger.
- **Contre-lecteur** : sous-agent neuf (modèle C), règle R2 ; je n'ai écrit aucune pièce de la liste ni aucun brouillon de la
  consigne ; je ne serai ni le lecteur B ni un lecteur d'une autre étape. Heures (`date -u`) : début 2026-11-16T14:18:36Z ;
  fin 2026-11-16T14:23:29Z (lue juste avant l'écriture de ce fichier).
- **Verdict : corrections** (1 majeure, 3 mineures ; remarques facultatives à part). Les 22 corrections K1 à K22 du tour 1 sont
  appliquées fidèlement, et le différentiel ne contient rien d'autre que trois ajouts déclarés (titre et puce « État du fichier »,
  section « Contre-lecture » finale). Mais la correction K5, telle que le tour 1 l'a écrite, a introduit une contradiction interne
  sur l'arrêt d'une clé du registre (C1) ; trois précisions mineures (C2 à C4) évitent un écart entre deux lecteurs.

## 1. Fidélité des corrections K1 à K22 (par `diff`)

`diff` brouillon 3 / brouillon 4 : les hunks sont exactement ceux-ci, et chacun est égal, caractère pour caractère, au « nouveau »
du rapport du tour 1 (§ 5) : l. 90 (K9), 132 (K4), 152 (K8), 544 (K14), 553 (K10), 570-573 (K7), 583-587 (K5, K6), 606-607 (K12),
621-622 (K20), 633 (K21), 639-640 (K11), 669-670 (K13), 821-831 (K17 à K19, K16), 840-842 (K1), 855-858 (K15), 861 (K22),
1002 (K2), 1029-1031 (K3). Chaque « ancien » du rapport a disparu, chaque « nouveau » est présent une seule fois. Les options O1
et O2 et les remarques facultatives du tour 1 ne sont pas appliquées (déclaré, tableau final de la pièce : exact).
Éléments du différentiel hors K1 à K22, tous déclarés par l'en-tête du programme de couples : (a) titre « brouillon 4 » ; (b) puce
« État du fichier » réécrite ; (c) section « Contre-lecture » ajoutée en fin de pièce (l. 1036-1076). Aucun ne porte de règle ni de
critère (la section dit elle-même qu'elle n'ajoute rien) ; voir remarques R-a et R-b.
Contrôle des renvois : `verification_renvois_consigne_b_v2.py` rejoué par moi sur la pièce : 194 citations, 194 renvois, 7
empreintes, 12 noms conformes, 29 lignes, 14 fichiers du bloc C5 égaux, aucune pièce de la table dans « Jamais remis » :
**code 0** (sortie de ma main, non écrite au dépôt). Filtre `INTERDITS_CONTENU_B` : aucune ligne ; aucun identifiant de modèle
(motif passé en argument) ; aucun marqueur à chevrons doubles.

## 2. Passages relus et ce que les corrections ont pu déranger

- **K1 (6.10)** : l'en-tête du verdict (section 12, point 2) porte bien « heures de début et de fin » ; la lecture de `date -u`
  juste avant la version achevée ne contredit ni la section 10 (issue écrite après le verdict achevé), ni R12 ; aucune autre
  mention d'heure de fin dans la pièce. Conforme.
- **K2 (13)** : la clause de jugement est retirée ; reste « si la ligne en dépend » (jugement léger, déjà présent dans 6.7 point 9
  et 6.8) ; sans repli silencieux (l'écriture « non vérifiable depuis mes pièces » est faite). Remarque seulement.
- **K3 (14)** : la ligne `STATUT` porte le code seul ; les quatre lignes ne contiennent aucun nombre, issue, ligne de table,
  empreinte d'un fichier du run (la seule empreinte permise est celle du message reçu) ; R-V2 satisfaite. Conforme.
- **K4** : § 2.1 de la consigne d'audit va de l. 122 à 191 (le § 2.2 commence l. 192) : exact.
- **K6, K14** : les trois sections de l'extrait sont écrites par `grep -n` aux lignes 398, 399 et 400 du bloc C5 de la commande v4 :
  préfixe `<n>:` exact pour les trois ; la clé d'une ligne (premier champ entre barres) est bien lisible après ce préfixe.
- **K7** : voir C4 (bordereau).
- **K11** : `resultat.entrees.I`, `.II` et `doses.etat_ii_par_dose_jugee`, `doses.ecart_a_la_base` sont bien relus en 6.6 (l. 719-720)
  et 6.7 (point 4, l. 757), donc rien n'est perdu ; accord avec le code (clés).
- **K12, K13, K20, K21** : cohérents avec 6.5 point 6 et avec la section 5.
- **K15** : confronté à `lectures_t07_v1.reserves` (commit `c2fab6cc…`) : le module balaie, pour « aire hors de [0,05 ; 0,95] » et
  « quantile 0,95 > 0,70 », les lectures décisives, les jeux hors jugement et T7-P3, T7-P4, T7-P6, T7-P9, T7-P15, T7-P18 (profondeur
  quelconque) ; `couples_figes_descriptif` et `planchers_p3_descriptif` n'y sont pas. K15 est exact. K22 aussi : le module ne juge
  « trop beau » que sur les jeux décisifs, et « tous les jeux lus au-dessus » entraîne « tous les décisifs au-dessus ».
- **K16 à K19 (6.9)** : voir C2, C3 et le point 1 pour la mère.

## 3. Corrections exigées (« ancien → nouveau » ; chaque « ancien » figure une seule fois dans la pièce, vérifié par programme)

**C1 (majeure ; 6.3, point 2 : contradiction introduite par K5)** — le point 2 dit « une ligne exactement pour chacune des clés
`SCELLEMENT-T07`, … Absente ou en double : arrêt `piece-non-conforme` », et K5 y a ajouté que `SCELLEMENT-T07` « est permise, non
exigée, à l'étape B ». Un lecteur ne sait pas s'il s'arrête quand elle manque ; les points 3 (égalité avec la pièce 4) et 5 (R054 :
`VERDICT-P3BIS` après `SCELLEMENT-T07` ; la clé compte parmi « les dix clés ») la supposent présente. Texte scellé (T0.7, l. 2174-2178) :
neuf clés exigées à l'étape B ; `SCELLEMENT-T07` permise, une fois au plus ; l. 1725 : « si `SCELLEMENT-T07` manque, G1 refuse déjà ».
Lecture proposée, prudente (une garde de plus pour le lecteur, aucune ligne ni issue ne change) : l'exiger ici, en le disant.
- ancien : ````SCELLEMENT-T07` est permise, non exigée, à l'étape B),```
- nouveau : ```neuf sont exigées par le texte (R109) ; `SCELLEMENT-T07`, que le texte permet à l'étape B sans l'y exiger, est exigée ici parce que les points 3 et 5 la comparent et que G1 refuse déjà sans elle (T0.7 l. 1725) : choix de cette consigne),```
(La parenthèse ouverte avant « ces dix clés » se referme comme avant.)

**C2 (mineure ; 12, point 3)** — K16 fait recopier la phrase « Lecture prudente » « à la section « Verdict » », mais la liste du point 3
de la section 12 (contenu de cette section) ne la nomme pas : un lecteur qui suit la liste l'omettra.
- ancien : ```l'état de BA-L2 (section 6.9) ; la phrase de R019.```
- nouveau : ```l'état de BA-L2 et la phrase « Lecture prudente » (section 6.9) ; la phrase de R019.```

**C3 (mineure ; 6.9, K16)** — « la phrase « Lecture prudente » de T08A l. 139 » n'est pas bornée : la ligne 139 porte un intitulé en gras
puis deux membres de phrase après « : ». « À l'octet » exige un empan exact ; le texte dit « à écrire telle quelle ». Prendre la ligne entière.
- ancien : ```la phrase « Lecture prudente » de T08A l. 139 (R143), à```
- nouveau : ```la ligne 139 de T08A (R143) entière, intitulé en gras compris, à```

**C4 (mineure ; 6.1, K7)** — « (1) les noms sous `<ESPACE>/pieces/`, comparés aux chemins du bordereau … sans ouvrir aucun fichier » :
pour comparer aux chemins, le lecteur ouvre le bordereau, dont l'empreinte n'est vérifiée qu'en (2) ; la section 2 dit « avant de lire
un fichier, tu recalcules son empreinte ». Poser l'exception.
- ancien : ```Ordre : (1) les noms sous `<ESPACE>/pieces/`, comparés aux chemins du bordereau et à la liste fermée, sans ouvrir aucun```
- nouveau : ```Ordre : (1) l'empreinte du bordereau et de son compagnon, puis les noms sous `<ESPACE>/pieces/`, comparés aux chemins du bordereau et à la liste fermée, sans ouvrir aucun autre```
(la ligne suivante, « fichier ; (2) seulement ensuite, les empreintes. », reste.)

Essai : les quatre couples appliqués à une copie jetable de la pièce (une occurrence chacun), puis le contrôle des renvois : code 0.

## 4. Remarques facultatives (aucune exigée)

- **R-a** : puce « État du fichier » : « heure du scellement » est inexact (le fichier n'est pas scellé) ; elle est réécrite au
  scellement, comme elle le dit. La lettre du rédacteur (« modèle C ») est à confronter au rédacteur réel (point 4 pour la mère).
- **R-b** : la section « Contre-lecture » est de l'historique pour la session mère, au milieu de la consigne que le lecteur reçoit ; elle
  nomme des fichiers qu'il n'a pas, mais dit que seules les sections 0 à 14 font foi, et le contrôle des noms (« Jamais remis ») passe.
  À garder ou à retirer au scellement, au choix de la mère ; je ne l'exige pas.
- **R-c** : `contradiction-consigne-texte` (« sur un point qui touche la ligne ») reste un jugement ; `critere-inapplicable` garde
  « si la ligne en dépend » : repris tels quels ; aucun repli silencieux.
- **R-d** : rejouer le contrôle des renvois après la réécriture de la puce et le remplacement du jeton `EMPREINTE-COMMANDE-V4-A-REMPLIR`.

## 5. Lecture à blanc : points non retenus au tour 1, jugés de nouveau

- **B2** (verdict assemblé par programme, O1 et O2) : toujours un risque réel de faute de recopie (nombres, cellules « à l'octet ») ;
  pas un écart à un texte scellé ; option de la mère, non exigée ici.
- **m5, m6** (copie du message par un script ; ordre du premier geste) : non retenus, facultatifs ; **m14, m15, m17** : non retenus.
- **m16** (aucun filtre sur le contenu de `verdict-ferme/`) : non retenu comme correction ; point pour la mère (point 5).
- **m10, partie « trois domaines à ajouter en 6.5.4 »** : non retenu : le texte range tout défaut de forme en Q « illisible » et le module
  en porte le motif ; la consigne dit déjà de ne pas refaire la validation du domaine.
- Les autres points (B1, B3, m1 à m4, m7 à m9, m11 à m13) sont corrigés par K1 à K22, vérifiés ci-dessus.

## 6. Les sept ambiguïtés A1 à A7

A1 : lecture fidèle et prudente (double marque admise, rien ne change : R112) ; A2 : fidèle ; A3 : bornée par K15 et K22, exacte ;
A4 : fidèle à T0.7 l. 1924 ; A5 : fidèle et prudente ; A6 : maintenant recopiée (K16 ; C2, C3 la précisent) ; A7 : mécanique, fidèle.
Aucune n'est un écart à un texte scellé qui demande le mot de Lazar.

## 7. Points pour la session mère

1. **Ligne dédiée de BA-L2** : la lecture par chaînes fixes (K17 à K19) n'est sûre que si la ligne est écrite pour que les chaînes soient
   exclusives : jamais « sans mot de Lazar » ni « s'applique ; pas de mot de Lazar requis » (la chaîne « mot de Lazar » y figure) ; même
   apostrophe que « ne s'applique pas » de la consigne (droite). À écrire ainsi, ou à ajuster avant le sceau.
2. **C1** : la lecture « SCELLEMENT-T07 exigée ici » est un choix de la consigne, prudent (arrêt de plus, aucune ligne changée) ; l'autre
   option est de la traiter comme permise : alors écrire « absente » et ne pas juger les points 3 et 5 pour elle. À trancher si tu préfères.
3. **Au sceau** : réécrire la puce « État du fichier » et la puce « Rédacteur », remplacer le jeton, rejouer les renvois (code 0), garder
   ou retirer la section « Contre-lecture ».
4. **Rédacteur de ce brouillon** : la puce dit « troisième rédacteur … (modèle C) » ; la demande de ce tour annonçait le modèle A pour
   les corrections. À faire concorder avec la réalité avant le sceau.
5. **Aucune garde de contenu** sur `verdict-ferme/` au bloc C7 (noms seulement) : un identifiant de modèle venu d'un manifeste recopié ne
   serait vu par personne ; à vérifier à la lecture du verdict.
6. **Option B2** : toujours à décider.
7. **Exclusion** : j'ai lu le texte scellé de T0.7 ; je suis exclu des lecteurs de P3-bis, de l'étape B et de B bis.

## 8. Déclaration et incidents de ma main

- Jamais ouverts : aucun fichier sous `diag/`, `runs/`, `donnees/` (ni `sondes-t07.json`, `lecture-t07.json`, `audit-fuites-t07.json`, ni scores,
  ni manifeste de run) ; aucun fichier de `docs/verdicts/` ; rien de l'étape B bis, du bras d'attaque ni du mode tenu à l'écart ;
  `registres/decisions.md` non ouvert. Code lu par `git show` au commit `c2fab6cc…` (module `lectures_t07_v1`, `lectures_t07_v2` : en-tête).
- Incidents : (1) une recherche de motif sur l'arbre du commit a listé des noms de fichiers de `brouillons/` et de `docs/notes/` (noms
  seulement, rien ouvert). (2) Ma sortie de contrôle des renvois a affiché les noms de chemins de la liste (dont ceux de `diag/…`) : noms
  seulement. (3) Un fichier jetable (`essai.md`, copie corrigée) est sous mon dossier de travail du scratchpad, jamais au dépôt. (4) Aucun commit,
  aucune poussée, aucun réseau, aucune dépense ; la pièce n'est pas modifiée.
