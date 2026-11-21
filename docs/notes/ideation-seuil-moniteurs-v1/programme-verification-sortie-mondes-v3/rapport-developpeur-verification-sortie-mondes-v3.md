# Rapport du développeur — programme de vérification de la sortie de l'auteur des mondes plantés (course « seuil et moniteurs ») — v3

- Auteur : développeur du programme de vérification de la sortie des mondes, modèle O. Écrit le 2026-11-21.
- Version : la v3 complète les rapports v1 (`6c00779d…`) et v2 (`7374460c…`), gardés intacts. Elle ne dit que ce qui change.
- Causes :
  - la vérification du vérificateur S sur la v2, `docs/notes/ideation-seuil-moniteurs-v1/programme-verification-sortie-mondes-v2/verification-v1/verification-programme-verification-sortie-mondes-v2-v1.md` (`9270bcab03c5a7e97c6afb2557c3432042b4b8f77ab0960e000cd00d221c8143`, égale à son compagnon, lue en entier), verdict « À corriger » (D1, D2, D3) ;
  - les mots de la mère de 11:00Z, relayés par le coordinateur (D1, D2 avec sa règle de lecture, D3, tranche voisine), sa précision sur la comparaison des noms sans casse ni accents (règle E1), et ses trois précisions sur la proposition de S (étape (c) parmi les clés laissées par l'étape (a) ; contrôle sous la loi de la tranche associée à T09 ; tolérance de 10⁻³ sur le taux de 3 %), portées dans le code et au § 2.
- Statut : instrument (classe B), **non contre-lu**. Aucun appel, aucune dépense, aucune clé, aucun commit, aucun refus de permission, de classifieur ni de garde.

## 0. Verdict

1. **D1** : plus de 40 témoins, ceux de tête et ceux du bloc à l'écart comptés ensemble, est une faute du point 1 (`P1_TEMOINS_AU_DELA_DU_PLAFOND`) : la sortie est illisible. L'observation de la v2 est retirée.
2. **D2** : la vérification signale par un code propre, `E_DERIVE_SANS_DECALAGE_LISIBLE`, que le décalage de F ne se lit pas dans T09 : F est écartée, la sortie reste lisible. La lecture suit la règle de la mère et compare les noms sans casse ni accents. Le compte rendu de correspondance rend la valeur transmise, le rang de la clé, la tranche associée à T09 et sa loi, et la tolérance du contrôle (10⁻³ sur 3 %), qui appartient au recalcul.
3. **D3** : aucun témoin du monde M n'est converti vers le recalcul (`NC_MONDE_M_SANS_GAMMA`), et c'est rapporté.
4. **Tranche voisine** : la suivante ; pour la dernière, la précédente ; sans boucle.
5. **314 essais, tous passés** (Python 3.13) ; 109 mutations tuées.
6. **Les 39 sorties de S rejouées** : toutes comme attendu. F y est partout écartée, sortie lisible, car leur T09 ne porte aucune clé que la règle reconnaisse.
7. **Correspondance sur la sortie factice** : 37 témoins convertis et 2 non convertis (le monde M). Le programme de vérité accepte les 37 : tous calculés, aucun refus.

## 1. D1 — plafond de témoins en faute du point 1

- Constante inchangée : `TEMOINS_MAX = 40` (l. 73), à un seul endroit.
- Le compte se fait au point 1 (l. 878 à 884) : la longueur de `temoins`, plus celle de chaque liste `temoins` du bloc `a_l_ecart` (témoins dans chaque famille, ou objet à part).
- Essais :
  - `temoins_au_plafond` : 40 témoins, lisible ;
  - `temoins_au_dela_du_plafond` : 41 en tête et à l'écart, illisible ;
  - `plafond_par_le_bloc_a_l_ecart` : 39 + 2 dans le bloc à l'écart, illisible.
- Mutations : par le code ; plafond relevé à 41 ; plafond baissé à 39 ; et `D1_bloc_a_l_ecart_non_compte`, qui ne compte plus le bloc à l'écart.
- L'artefact v2 « trois familles à l'écart » franchissait le plafond avec ses copies. Ses deux copies sont désormais sans témoins : il n'éprouve que le nombre de familles.

## 2. D2 — dérive de F lue dans T09

**Règle E1** (`lire_decalage_de_t09`, l. 939 à 964), sur `valeurs_de_plus` de T09 :
- (a) on écarte les clés dont le nom contient « couverture », « taux » ou « probabilite » ;
- (b) on garde la seule clé laissée par l'étape (a) ;
- (c) à défaut, on garde l'unique clé dont le nom contient « decalage » ou « derive », **cherchée parmi les clés laissées par l'étape (a), et non parmi toutes les clés** (précision de la mère, écrite en commentaire l. 951) ;
- sinon, F est écartée.

Chaque nom de clé est comparé sur sa forme normalisée, par sous-chaîne : minuscules, accents retirés, tirets repliés. « Décalage », « DERIVE » et « Probabilité » sont reconnus.

**Contrôle de cohérence : il appartient au recalcul, pas à ce programme** (précisions de la mère). Il porte sur un seul critère : le décalage lu triple le taux de 1 %, c'est-à-dire porte le taux à **3 %**. Il se fait sous **la loi de la tranche associée à T09**, la tranche de F dont `n_calibration` contient **299**. Sa tolérance est de **10⁻³ sur le taux de 3 %**, comme au point 4 du § 6, et non de 10⁻¹². Ces trois éléments sont des constantes du programme (`N_DE_T09`, `TAUX_VISE_PAR_LA_DERIVE`, `TOLERANCE_DU_CONTROLE_DE_DERIVE`, l. 932 à 934), écrites au compte rendu pour le programme de vérité.

**En vérification** (l. 1037 à 1044) : si F est présente et que la règle ne lit rien, ou si T09 manque, F est écartée avec `E_DERIVE_SANS_DECALAGE_LISIBLE`. La sortie reste lisible, et le point 2 n'est pas manqué pour autant.

**En correspondance** :
- la même règle donne le décalage transmis au recalcul : un décalage de la loi de lecture, en écarts types, pour tous les témoins de F ;
- le compte rendu porte `derive_de_F`. Quand le décalage est lu : `statut` « lue », `rang_de_la_cle`, `valeur_transmise` (texte du nombre), `tranche_associee_a_T09` (`rang`, `n_calibration_contient_299`), `loi_de_la_tranche` (la loi recopiée telle quelle), et `controle` (`par` : le recalcul ; `critere` ; `taux_vise` « 0.03 » ; `tolerance` « 0.001 »). Sinon : `{"statut": "illisible_F_a_ecarter"}`, ou `{"statut": "sans_famille_F"}` ;
- le rang de la clé est compté de 1, dans l'ordre de l'objet ; le nom de la clé n'est pas recopié ;
- si aucune tranche de F ne joue 299, la première tranche est transmise, avec `n_calibration_contient_299` à faux ;
- **ce programme ne fait pas le contrôle** : il dit seulement quelle valeur, quelle tranche et quelle loi il transmet.

**Essais.**
- Écartées :
  - T09 sans `valeurs_de_plus` ;
  - deux clés libres ;
  - deux clés nommées « decalage… » et « derive… » ;
  - une seule clé, exclue (« couverture… ») ;
  - « taux_de_derive » exclue par l'étape (a) et deux clés libres : l'étape (c) ne la reprend pas, F est écartée.
- Lisibles, sans écart :
  - une clé libre restante après exclusion ;
  - « taux… » et « probabilite… » exclues, une restante ;
  - une clé nommée parmi deux restantes ;
  - noms accentués (« Probabilité_y », « Décalage_X ») ;
  - noms en majuscules (« COUVERTURE », « DERIVE »).
- Correspondance :
  - sur la sortie factice v3 : valeur « 0.5 », clé de rang 2, tranche de rang 2 (celle à 299), sa loi, tolérance « 0.001 » sur « 0.03 » ;
  - aucune tranche à 299 : la première, signalée ;
  - « F à écarter » quand la lecture échoue.

**Mutations** :
- par le code ;
- `D2_sans_exclusion_des_noms` ;
- `D2_sans_repli_par_le_nom` ;
- `E1_repli_parmi_toutes_les_cles` ;
- `E1_noms_compares_sans_normalisation` ;
- la tranche de T09 cherchée à 300 au lieu de 299.

**Sortie factice v3.** Son T09 porte `{"couverture_qui_reste": 0.4321, "decalage_en_ecarts_types": 0.5}`, valeurs factices. Sa famille F a trois tranches (`n_calibration` [200, 300, 400], [299], [200, 300, 400]) ; la deuxième, de loi factice distincte, est celle de T09 (`fabriquer_sorties_factices_v3.py`, différentiel joint). La sortie factice v1 aurait vu F écartée par la règle.

## 3. D3 — monde M non converti

- `lois_du_monde_m` (l. 1479) lève `NC_MONDE_M_SANS_GAMMA` pour tout témoin du monde M, quel que soit son signal.
- La conversion de la v2 (populations dans l'ordre, honnête en mélange, refus de `somme`, loi de signal hors forme) est retirée, avec ses deux codes `NC_SIGNAL_SOMME_SANS_LOI` et `NC_LOI_DU_SIGNAL_HORS_FORME`, devenus inatteignables. Elle reste lisible au différentiel v2 → v3, pour le jour où la lettre dira γ.
- Essais : LM1 sur `valeur`, LM2 sur `somme`, tous deux `NC_MONDE_M_SANS_GAMMA`. Mutation par le code.

## 4. Tranche voisine

- L. 1463 : la tranche suivante ; pour la dernière, la précédente ; jamais de retour à la première. Choix déclaré : `CH1B_TRANCHE_VOISINE_SUIVANTE_OU_PRECEDENTE`.
- Essais sur la famille D (tranches à 40, 300 et 400) : n = 40 donne la voisine à 300, n = 300 celle à 400, n = 400 celle à 300.
- Mutation : la voisine circulaire de la v2 donnerait 40 pour la dernière tranche ; l'essai la tue.

## 5. Rejeu des 39 sorties de S

`rejouer_sorties_de_s_v3.py` lit les noms des 39 sorties dans le fichier de résultats v1 de S. Il ouvre chaque sortie par son chemin complet dans `…/verif-verification-sortie-mondes/mes_essais/sorties2/`, sans lister aucun dossier. Il n'écrit que des codes dans `rejeu-sorties-de-s-v3.txt` ; les rapports individuels sont dans `rejeu-sorties-de-s-rapports-v3/`, hors table.

Différences avec les résultats v1 de S, toutes voulues :
- **F écartée** (`E_DERIVE_SANS_DECALAGE_LISIBLE`) dans les 34 sorties où le point 2 est jugé (toutes, sauf les cinq illisibles au point 1 : 04a, 04b, 04d, 06i, 08) : leur T09 ne porte aucune clé que la règle reconnaisse. Ces sorties restent lisibles ou illisibles pour leurs autres raisons ;
- 03f et 03h lisibles, E écartée (C2 de la v2) ;
- 05d prise au point 5 (N2) ;
- 06k porte aussi `P2_IDENTIFIANT_IMPOSE_RESERVE` ;
- plus aucune observation sur le nombre de témoins : ses sorties en comptent 33 au plus, sous le plafond ;
- 08 (taille) reste illisible, au-delà de 52 000 caractères.

Je n'ai lu que les codes, jamais le texte des sorties.

## 6. Correspondance sur la sortie factice

- Sortie factice v3 : 37 témoins convertis. LM1 et LM2 ne le sont pas, par D3.
- Pour F : valeur « 0.5 », clé de rang 2, tranche de rang 2 (à 299), loi normale factice de cette tranche, contrôle au recalcul avec une tolérance de 0.001 sur 0.03.
- Fichiers : `entree-recalcul-factice-saine-v3.json` et son compte rendu.
- Le programme de vérité (`4857343c…`), lancé par `python3 -I -B … --recalculer` sur cette entrée, sort en code 0 : 37 témoins calculés, aucun refus. L'essai ne lit que les statuts et les codes, et efface la sortie.

## 7. Comptes

- **314 essais, tous passés.**
- **Artefacts : 157.**
- **Mutations : 109**, toutes tuées :
  - 72 par code ;
  - 13 par motif de clé ;
  - 14 par correction : C1 deux fois, C2, C3, N2, la borne deux fois, le plafond deux fois, D1, D2 deux fois, E1 deux fois ;
  - 6 par code `NC_…` ;
  - 1 pour la tranche voisine ;
  - 1 pour la tranche de T09 ;
  - 2 pour les gardes de la correspondance.
- **Autres essais : 48.**
- **Mutations de la v2 rejouées** : toutes, sauf deux dont la garde n'existe plus (`NC_SIGNAL_SOMME_SANS_LOI` et `NC_LOI_DU_SIGNAL_HORS_FORME`, code retiré par D3). Le code `O_TEMOINS_AU_DELA_DU_PLAFOND` est devenu `P1_TEMOINS_AU_DELA_DU_PLAFOND` (D1), et sa mutation suit.

## 8. Ce que la lettre ne fixe pas (remarques neuves)

1. **D2, repli** : tranché par la mère. L'unique clé « decalage » ou « derive » se cherche parmi les clés laissées par l'étape (a) ; une clé « taux_de_derive » est donc exclue avant le repli.
2. **D2, rang** : compté de 1, dans l'ordre de l'objet JSON tel qu'écrit.
2 bis. **D2, tranche de T09 absente** : si aucune tranche de F ne joue 299, la première est transmise et c'est dit (`n_calibration_contient_299` à faux). La lettre ne le règle pas ; au recalcul de juger.
3. **D2, F absente** : la règle ne s'applique pas ; le compte rendu dit `sans_famille_F` (l'absence de F est déjà une faute du point 2).
4. **D3** : un monde M sans ses deux témoins reste écarté en vérification, comme en v2 ; le non-convertible ne concerne que la correspondance.
5. **D1** : la lettre du § 6 ne nommait pas ce plafond ; il est rangé au point 1 sur le mot de la mère (11:00Z), comme le recommande S.
6. **Mots de la mère souhaités par S, non tranchés ici** : l'unité des décalages du saboteur (CH5) reste celle de la v2 ; voir son § 6.

## 9. Commandes

`D=/tmp/claude-0/-home-user-controle-ia-travail/16eb2a62-e29a-56e1-a702-f48557a5876c/scratchpad/dev-verification-sortie-mondes-v3`, une commande par appel.

- Essais : `/home/user/controle-ia-travail/.venv/bin/python -B -m pytest -q -p no:cacheprovider --basetemp=$D/essais-tmp $D/test_verifier_sortie_auteur_mondes_v3.py`. Attendu : 314 passés. Effacer ensuite `$D/essais-tmp`, qui contient des chaînes de forme de clé fabriquées à l'exécution.
- Avant l'envoi : `python3 -I -B $D/verifier_sortie_auteur_mondes_v3.py $D/sortie-factice-saine-v3.json RAPPORT_NEUF.json --motifs LISTE_REELLE`. Attendu : code 0, aucune observation, aucun écart.
- À la réception :
  - vérification : la même commande, sur la sortie reçue ;
  - puis, si elle est lisible : `python3 -I -B $D/verifier_sortie_auteur_mondes_v3.py --vers-recalcul SORTIE_RECUE.json ENTREE.json --motifs LISTE_REELLE` ;
  - puis le mode `--recalculer` du programme de vérité sur `ENTREE.json`, et lire `derive_de_F` dans `ENTREE.json.correspondance.json` pour le journal de la session.

## 10. Réserves

1. Programme, essais et rejeu non contre-lus.
2. Le décalage transmis pour F n'est pas contrôlé ici : c'est le recalcul qui dira s'il porte le taux à 3 % à 10⁻³ près, sous la loi de la tranche associée à T09.
3. L'essai d'acceptation fait calculer au programme de vérité des valeurs sous des lois factices. Je ne les lis ni ne les recopie, et l'essai efface sa sortie.
4. Fichiers inchangés : `motifs-noms-refuses-essai-v1.txt` garde son nom et son empreinte v1. La fabrique et la sortie factice changent et passent en v3.

développeur du programme de vérification de la sortie des mondes, modèle O
