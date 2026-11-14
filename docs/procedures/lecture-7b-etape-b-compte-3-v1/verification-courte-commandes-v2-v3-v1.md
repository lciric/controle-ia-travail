# Vérification courte des commandes du compte 3 — phase A v2 et phase C v3 — v1

- **Vérificateur** : sous-agent neuf, « modèle C » (aucun identifiant de modèle écrit) ; je n'ai écrit aucune des pièces lues ; lecteur d'aucun verdict.
- **Heures** (`date -u`) : début 2026-11-14T13:12:46Z ; fin 2026-11-14T13:15:30Z (avant écriture de cette ligne de rendu).
- **Lu** : `commande-compte-3-phase-a-v2.md` (`25635d99…`, empreinte recalculée : égale), `commande-compte-3-phase-c-v3.md` (`9d788919…`, égale),
  `rapport-preparateur-v2.md` (`bdb81265…`, égale), `contre-lecture-commande-compte-3-v1.md` (tableau des 21 constats, corrections proposées),
  lignes R-2739, R-2740, R-2741, R-2746, R-2758 de `registres/decisions.md` (une à une, par `grep -n '^| R-27NN '`), sorties
  `repetition-phase-a-jouet-sortie-v2.txt` (21 sur 21), `repetition-phase-c-jouet-sortie-v3.txt` (53 sur 53), `controle-a-blanc-v2-etat-actuel-sortie-v1.txt`,
  sortie de l'essai de l'attestation v3 (17 sur 17), script du contrôle à blanc v2 (sections 4 et 8 seulement) ; deux lignes de
  `registres/t07-etape-b-bis-v1.md` (clés `SCELLEMENT-BBIS`, `ABSENCE-B-BBIS` : format seulement) et la présence des quatre clés de préalables dans
  `registres/scellements-v1.md` (noms de clés seulement).
- **Non ouvert** : aucun `diag/`, `runs/`, `donnees/` de 7a ou 7b ; aucune sortie de T0.7 ; ni `/root/bac-audit-fuites-t07-v1/`, ni les fichiers non versés de
  `docs/notes/g0-deux-semaines-v1/audit-fuites-t07-v1/`, ni `donnees/bras-attaque*`, `donnees/mode-tenu-a-l-ecart*`, `docs/notes/bras-attaque/` ; aucune valeur de clé.
  Rien n'a été exécuté (les blocs ne sont pas rejoués : je lis les sorties de répétition archivées). Aucun fichier existant modifié ; aucun commit.

## Verdict

**REMISSIBLE**, les deux commandes, avec **cinq réserves non bloquantes** (R-V1 à R-V5, ci-dessous) que la mère ou Lazar lèvent au remplissage ou à la remise ; aucune
correction de texte n'est nécessaire pour remettre. Les couples de correction ne sont donnés que pour les réserves qui pourraient être fermées par un texte (v3 de la
phase A seulement si Lazar le veut : la phase A est scellée, R12).

## 1. Les 21 constats : traités là où le rapport le dit

Pour chacun j'ai rouvert le texte de la contre-lecture (constat et correction proposée), puis l'endroit cité de la commande.

| constat | traité là où le rapport le dit ? | note |
|---|---|---|
| CL3-01 (majeur) | oui : phase A § 0.1, § 2, § 15 (2 à 3), F-A (P3A-005) ; phase C C0 exige `CODE-MOTS-ET-COUT-T06` | verdict A hors de `main` ; journal provisoire limité à STATUT, FICHIERS, DÉCLARATIONS, MESSAGE ; répétition : « aucune ligne ISSUE » |
| CL3-02 (majeur) | oui : phase A § 1 (NARCBench, papiers B et C, code de la pièce « mots et coût », aucune tâche du lot) ; phase C `CELLULE_HOTE` exigée par `--admettre-hote` | essai attestation v3 : H1 à H5 conformes (cellule autre : arrêt) ; répétition C : cellule autre → 2C arrête |
| CL3-03 (majeur) | oui : A3 sans R-2704, filtre de contenu (`INTERDITS_CONTENU`) ; C0 (ligne dédiée, sans B bis, nomme BA-L2) ; C5 (filtre de contenu et de noms) | trois artefacts de C0 et deux de C5 dans la répétition C |
| CL3-04 (majeur) | oui : C4a (marqueur posé avant l'appel), C4-attente, C4b relançable seul ; F-C relançable | répétition : C4a relancé → arrêt ; poussée refusée → reprise |
| CL3-05 (majeur) | oui : appel `setsid nohup`, borne 60 min → nœud, jamais d'arrêt de processus ; durée mesurée (fichier versé) | la mesure est une extrapolation par comparaison (le rapport le dit) |
| CL3-06 (majeur) | oui : section 9 du contrôle à blanc (`--chaine`, bloc C3) ; acceptation par la mère écrite en § 0.4 de la phase C | voir R-V4 |
| CL3-07 (bloquant) | oui : deux répétitions de bout en bout versées et scellées, avec artefacts | réserve du rapport gardée : module d'étape B jouet (vraie garde et vraie écriture) |
| CL3-08 | oui : C1, approfondissement avant la recherche de C7 | non exercé : réserve écrite au rapport |
| CL3-09 | oui : C1a, versions exactes, 9 Gio | installation non exercée : réserve écrite au rapport |
| CL3-10 | oui : `place` admet un fichier suivi ou non s'il égale le blob ; scores admis s'ils égalent `SCORES-T07` | répétition : C2 relancé |
| CL3-11 | oui : marqueur retiré ; arrêt et nœud à défaut du modèle C (A § 2, C § 2) | texte |
| CL3-12 | oui : A2, noms exacts (10 + 3 noms, 9 + 2 fichiers listés par les deux `empreintes.sha256` = 11) | répétition A : « 11 traces » |
| CL3-13 | oui : A § 2 (un seul agent lit et prononce ; mot de Lazar R-2741) | |
| CL3-14 | oui : essai du contrôle à blanc v2 (19 sur 19) ; essai v1 rejoué (28 sur 28) | |
| CL3-15 | oui : sorties versées et scellées (listées au rapport) | |
| CL3-16 | oui : attestation v2 (identifiant entier ou tronqué) ; nouveauté (aucune branche `lot/compte-3-v1`, aucun `registres-provisoires/compte-3-*`) ; citation de R-2704 corrigée au rapport | |
| CL3-17 | oui : blocs 0b et 0b-C (récupération par refspec, avance rapide) ; « tout poussé avant l'ouverture » (A § 4, C § 0.2) | |
| CL3-18 | oui : motif exact des noms, sans archive (A5, C7) | répétition : archive → arrêt (A : X5 ; C : artefact C7) |
| CL3-19 | oui : C7 joué et S7 déclaré (C § 0.3) ; chemin et empreinte du manifeste de T0.7 gardés par la mère (C § 15 (3)) | |
| CL3-20 | oui : le contrôle à blanc n'imprime pas le chemin du plan de B bis (seulement « ligne … datée … ; fichier cité : sceau conforme ») ; C4-attente n'imprime que noms et nombres | |
| CL3-21 | oui : message reçu recopié par le lecteur, comparé au message scellé (A4-A5, C6-C7) | répétition : message autre → arrêt |

Le tableau du rapport v2 est fidèle à la contre-lecture sur les 21 lignes ; aucun constat sans traitement ni raison écrite. Écart du préparateur (phase C v2 modifiée
après scellement, remise à son texte, changements portés en v3) : déclaré au rapport, conforme à R12.

## 2. Les mots de Lazar : portés sans glissement (R-2740, R-2741)

- **N-A (a)** (extracteur non lancé, le lecteur lit lui-même les fichiers de service) : phase A, en-tête et § 0.3 ; l'extracteur est dans les interdits. Fidèle.
- **N-B (a)** (un seul agent lit la table A puis prononce) : phase A § 2, « un seul … décision de Lazar R-2741, N-B (a) ». Fidèle.
- **N-C** (la mère lit, par programme, le seul état BA-L2 ; rien d'autre de 7b n'est lu par la mère ; programme qui n'affiche que l'état) : phase C § 15, bloc M, essayé
  (« ÉTAT BA-L2 : ne s'applique pas », arrêt sur branche absente, arrêt sur registre sans `LECTURE-T08-BASE-A`, aucune autre valeur affichée). Fidèle ; la
  restriction « rien d'autre de 7b » n'est cependant écrite qu'à l'en-tête, pas au point des recopies (voir R-V2).
- **N-D** (le lot NARCBench continue en parallèle, rien de T0.7, 7a, 7b ouvert avant les verdicts) : phase A en-tête, phase C en-tête ; l'hôte est distinct de toute session du lot (A § 1). Fidèle.
- **N-E** (7b et l'étape B sans attendre la grille de G0) : portée aux deux en-têtes (« v9 » non répété : sans effet). Fidèle.
- **R-2740, nœud 2** (même hôte que l'étape B, lecteurs distincts) : phase C § 0 (5), § 1, § 2 ; l'hôte n'est jamais lecteur de B bis. Fidèle.
- **R-2740, GO-2026-11-14-09, 40 USD** : écrit hors de la phase C, qui ne dépense rien. Fidèle.
- **Attribution inexacte, sans effet** : les deux commandes et le rapport mettent « plan de B bis scellé avant toute lecture de l'étape B » sous la référence R-2740 ; la
  lettre de R-2740 (nœud 5) ne parle que de la « lecture dure » retenue avant toute lecture de B bis ; la règle du plan scellé avant la lecture de B vient de R-2714 (2) et
  R-2716 (1). Le contenu est juste ; la source est mal numérotée (R-V5).

## 3. L'ordre des préalables : écrit, et gardé en partie

**Écrit** : R-2758 et « Bloc M et ordre de la remise » du rapport v2 donnent la suite (1) audit des fuites (`AUDIT-FUITES-T07`), (2) `CODE-MOTS-ET-COUT-T06` (alors seulement
le verdict A entre dans `main`), (3) `LECTURE-T08-BASE-A` puis `ISSUE-MOTS-ET-COUT-T06`, (4) bloc M puis ligne dédiée, (5) plan de B bis scellé, (6) consigne du lecteur B,
liste v3, marqueurs, (7) remise de la phase C v3. Dans les commandes : phase A § 0.1 et § 15 (CODE-MOTS avant l'entrée du verdict dans `main`) ; phase C § 0 (2) (liste des
préalables) et § 15 (bloc M « après `LECTURE-T08-BASE-A` puis `ISSUE-MOTS-ET-COUT-T06` »). La suite numérotée complète ne figure que dans R-2758 et le rapport, pas dans les commandes.

**Gardé par des contrôles** (par présence et par antériorité à l'instant de l'appel) :
- bloc C0 : une ligne exactement pour chacune des quatre clés `AUDIT-FUITES-T07`, `ISSUE-MOTS-ET-COUT-T06`, `LECTURE-T08-BASE-A`, `CODE-MOTS-ET-COUT-T06` sur `main` ;
  ligne `<<R_BA_L2>>` présente, sans mot de B bis, nommant BA-L2 ; ligne du plan de B bis présente dans son registre propre et absente du registre de T0.7 ;
- contrôle à blanc (C3, puis juste avant l'appel dans C4a) : section 3 (lignes à date strictement antérieure à l'instant, fichier cité, empreinte), section 4 (`CONSIGNE-AUDIT-FUITES-T07`
  < `AUDIT-FUITES-T07`), section 8 (plan de B bis daté strictement avant l'instant, fichier cité à son empreinte) ; consigne du lecteur B : empreinte vérifiée en C5 ;
  consigne du lecteur A : empreinte et compagnon en A1 ; marqueurs restants : arrêt en 1 / 1C.

**Non gardé par un contrôle** (R-V1) : aucun contrôle ne compare les dates entre `AUDIT-FUITES-T07`, `CODE-MOTS-ET-COUT-T06`, `LECTURE-T08-BASE-A`, `ISSUE-MOTS-ET-COUT-T06`,
la ligne `<<R_BA_L2>>` et le plan de B bis. Ils sont tous « présents et antérieurs à l'instant », donc l'ordre entre eux dépend de la mère à l'écriture. Ce qui protège la règle d'ignorance
de T0.6 (code avant tout résultat) est donc la discipline de la mère, non une garde. Constat de calendrier : le plan de B bis est déjà scellé (`SCELLEMENT-BBIS`, 12:30:30Z), donc antérieur à
tout ce qui reste à écrire ; la suite (5) de R-2758 est de fait satisfaite d'avance ; sans conséquence pour la condition de la section 8.

## 4. Marqueurs restants et qui les remplit

**Phase A** (`commande-compte-3-phase-a-v2.md`) : la mère remplit `<<LISTE>>`, `<<EMPREINTE_LISTE>>` (liste « qui a lu quoi » v2), `<<CONSIGNE_LECTEUR_A>>`,
`<<EMPREINTE_CONSIGNE_LECTEUR_A>>` (bloc 1) ; l'hôte, par programme au bloc A4, remplit `<<ESPACE>>`, `<<EMPREINTE_BORDEREAU>>`, `<<PY>>`, `<<NOTE_MODELE>>`, `<<CONSIGNE>>`,
`<<EMPREINTE_CONSIGNE>>` (arrêt s'il en reste un) ; l'hôte remplit à la main, au bloc F-A, `<rapport final du lecteur A …>`, `<bloquée | passée>`, `<modèle A | modèle C>` (arrêt s'il en reste un) ;
Lazar donne en conversation le chemin et l'empreinte de la version remise (bloc 0b) et nomme le modèle C du lecteur.

**Phase C** (`commande-compte-3-phase-c-v3.md`) : la mère remplit `<<LISTE>>`, `<<EMPREINTE_LISTE>>` (liste v3, ligne de l'hôte à `CELLULE_HOTE`), `<<CONSIGNE_LECTEUR_B>>`,
`<<EMPREINTE_CONSIGNE_LECTEUR_B>>`, `<<REGISTRE_BBIS>>`, `<<CLE_PLAN_BBIS>>`, `<<R_BA_L2>>`, `<<BRANCHE_PIECE>>` (bloc 1C ; arrêt s'il en reste un) ; la mère remplit aussi, dans son propre bloc M (§ 15),
`<branche qui porte base-a-t08.json>` ; l'hôte remplit `<<ESPACE>>`, `<<EMPREINTE_BORDEREAU>>`, `<<PY>>`, `<<NOTE_MODELE>>`, `<<CONSIGNE>>`, `<<EMPREINTE_CONSIGNE>>` (bloc C6, par programme) et, à la main, les trois variables de tête de F-C.
Pièces encore à écrire par la mère (rapport v2) : consignes des lecteurs A et B, listes v2 et v3, lignes de N-B et de CL3-01 ; `base-a-t08.json` doit porter `lignes.BA-L2.s_applique`.

**Correspondance des noms réels de B bis (R-2746)** : le préparateur proposait `registres/etape-b-bis-v1.md` et `SCELLEMENT-PLAN-BBIS` (c'est ce que porte la sortie scellée du contrôle à blanc
sur l'état actuel, cellule 8). **Le registre propre réel est `registres/t07-etape-b-bis-v1.md`, clé `SCELLEMENT-BBIS`** (R-2746 ; je n'ai lu que la ligne, de format
`| SCELLEMENT-BBIS | 2026-11-14T12:30:30Z | prereg/T0.7-etape-B-bis-v1.md | <sha256> |`, quatre cellules ; la clé n'est pas dans `registres/scellements-v1.md`).
**Réponse : oui, la commande accepte ces noms réels sans modification de texte.** La phase C ne cite aucun des deux noms proposés (recherche faite : aucune occurrence de `PLAN-BBIS`,
`etape-b-bis-v1` ni `SCELLEMENT-BBIS` dans les deux commandes) ; elle n'a que les marqueurs génériques `<<REGISTRE_BBIS>>` (chemin relatif à la racine du dépôt) et `<<CLE_PLAN_BBIS>>`. Valeurs à remplir :
`REGISTRE_BBIS='registres/t07-etape-b-bis-v1.md'`, `CLE_BBIS='SCELLEMENT-BBIS'`. Contrôles faits sur le texte : C0 cherche `^| SCELLEMENT-BBIS |` dans `origin/main:registres/t07-etape-b-bis-v1.md`
(donc ce fichier doit être sur `main` : « tout poussé avant ce message ») ; le contrôle à blanc exige la forme de clé `[A-Z0-9]+(-[A-Z0-9]+)+` (satisfaite), une ligne unique à quatre cellules (satisfaite), un registre
distinct de ceux que lit T0.7 (satisfait), la clé absente de `scellements-v1.md` (satisfait : 0 occurrence). La ligne réelle `ABSENCE-B-BBIS` du même registre n'est pas lue par la commande (sans effet). Deux pièces scellées parlent des
noms proposés : le rapport v2 (cité ci-dessus) et la sortie du contrôle à blanc sur l'état actuel ; elles restent telles quelles (R12) ; la mère consigne la correspondance (R-2758 la porte déjà).

## 5. Voies d'ouverture des données de 7b et d'information vers la mère

- **Rôles prévus uniquement** : la phase A fait extraire les 26 fichiers de 7b au seul profit du lecteur A (exception de R-2711 (2)), par liste positive, avec arrêt sur tout nom fermé
  (`lecture-sondes`, `resume.json`, activations, adaptateurs) ; l'hôte n'ouvre aucun résultat (copie, empreintes, noms). La phase C place les scores et les mesures dans la racine de l'hôte pour que le
  module de C7 les lise (rôle prévu), jamais commités (le commit ne prend que le journal, la sortie du module, le verdict, le journal provisoire, avec garde sur l'index) ; l'extrait et le bordereau du lecteur B
  excluent les scores par nom (`scores-actions`, `sondes-neuves`) ; le nettoyage de F-C retire les données placées. Aucune voie vers les scores ou les données de 7b pour la mère, le lecteur de B bis, ni le lot NARCBench.
- **Vers la session mère** : phase A, la sortie « RENDU » (tête, empreinte du journal provisoire), les commits et les empreintes ; phase C, en plus, le code de sortie de l'étape B et sa durée (§ 13 (1)), le nombre de lignes
  ajoutées au journal, et, sur un code 2 seulement, la ligne `REFUS-T07` (motif de refus du module, écrite par lui). Ce ne sont ni scores, ni issues, ni nombres de verdict ; mais ce n'est pas « rien », et le code
  3 / 2 est un état d'exécution de l'étape B (R-V3). Le rapport final des lecteurs va à Lazar en conversation ; la mère ne le recopie pas (A § 13 (2)). Le journal provisoire (lignes STATUT, FICHIERS, DÉCLARATIONS, MESSAGE) est sur la branche : son contenu
  dépend des consignes des lecteurs, non écrites (R-V2). L'état de BA-L2 est la seule lecture de 7b par la mère (bloc M), et passe de sa ligne dédiée à l'extrait du lecteur B, comme le texte de T0.7 le veut.

## 6. Réserves non bloquantes (qui lève, comment)

- **R-V1 (ordre non comparé par programme)** : voir § 3. La mère lève : avant la remise, comparer les dates des lignes `AUDIT-FUITES-T07` < `CODE-MOTS-ET-COUT-T06` < `LECTURE-T08-BASE-A` ≤ `ISSUE-MOTS-ET-COUT-T06` dans
  `registres/scellements-v1.md` et le jour de la ligne `<<R_BA_L2>>` après elles, et inscrire le constat à `registres/decisions.md`. Couple optionnel, pour une v4 de la phase C (non exigé) : ancien : aucune comparaison en C0 ;
  nouveau : en C0, après les quatre `grep -c`, comparer les champs 3 (date, forme `AAAA-MM-JJTHH:MM:SSZ`, comparable lexicalement) des quatre lignes dans l'ordre ci-dessus et `arret "ordre des préalables"` sinon.
- **R-V2 (consignes des lecteurs non écrites ; recopies de la mère)** : le contenu de STATUT, FICHIERS, DÉCLARATIONS, MESSAGE du journal provisoire est fixé par la consigne du lecteur ; elle doit interdire toute issue et tout nombre dans ces lignes
  (A et C : « aucun nombre ni aucune issue hors des fichiers scellés du verdict », écrit au message de remise mais non éprouvé). La mère lève en le mettant dans les consignes, qu'un contre-lecteur lit. De plus,
  la phase C § 15 (1 à 4) (recopie du journal et du verdict B, rescellé, « verdict soumis à Lazar ») ne dit pas, comme la phase A § 15 (1), « sans lire ni afficher » : couple, à porter dans la ligne de décision de la mère ou dans une v4 :
  ancien : « (2) recopie les fichiers du verdict B, rescelle » ; nouveau : « (2) recopie, par programme et sans les ouvrir ni les afficher (N-C : seul l'état BA-L2 est lu), les fichiers du verdict B, rescelle ».
- **R-V3 (information vers la mère au-delà de BA-L2)** : code de sortie et durée de l'étape B, nombre de lignes du journal, ligne `REFUS-T07` sur un code 2. Nécessaires à l'action de la mère (nouvelle version de la commande sur un code 2, nœud sur un code 3) ; à confirmer par
  Lazar d'un mot, ou à consigner par la mère comme état d'exécution, non résultat (la lettre de N-C vise ce que la mère « lit » de 7b).
- **R-V4 (section 9 du contrôle à blanc)** : la lecture par programme, par l'hôte, de la table A, de l'issue de P3-bis, de l'audit, de l'issue « mots et coût », des épisodes et des colonnes des mesures, sans rien afficher, est acceptée par la mère « en remettant »
  (C § 0.4) : c'est un choix de la mère, non un mot de Lazar ; ces fichiers sont ceux que le module lira de toute façon à l'appel. La mère l'inscrit à `registres/decisions.md` en remettant, ou retire `--chaine` du bloc C3 et déclare le risque de refus évitable.
- **R-V5 (références)** : (a) l'attribution du plan scellé à R-2740 (R-2714 (2) et R-2716 (1) en sont la source) ; (b) la phase A scellée nomme `commande-compte-3-phase-c-v2.md` comme commande à part, alors que la phase C à remettre est la v3 : Lazar dit « v3 » et
  son empreinte `9d788919…` à la remise (le bloc 0b-C compare) et ne colle pas la v2 ; (c) les réserves du rapport restent ouvertes (module d'étape B jouet ; C1 et C1a non exercés ; voies de scores non éprouvées avant l'appel, code 3 possible ; transport local des répétitions).
  Aucune ne demande de nouveau texte.

## Fin

Verdict : **remissible** (phase A v2 seule, puis phase C v3 après les préalables, dans l'ordre de R-2758). Aucune condition de remise ne manque dans le texte ; les cinq réserves sont des actions de la mère ou de Lazar, hors des commandes.
