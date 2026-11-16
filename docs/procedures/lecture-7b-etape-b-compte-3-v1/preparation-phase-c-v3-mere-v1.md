# Phase C v3 du compte 3 — ce que la commande demande à la mère avant la remise — v1

- **Statut** : brouillon pour la session mère `session_016QhUrtmLyFWJP6Cy7rgfXH`, qui décide, scelle et remet ; rien n'est
  décidé ici. Fichier neuf, scellé, non commité. La commande fait foi :
  `commande-compte-3-phase-c-v3.md` (`9d7889198238c171447a06f56f1a37beb4190572c3a9ceceb18144541c258d2e`).
- **Rédacteur** : sous-agent neuf de la session mère (modèle A), préparateur des préalables de la phase C v3 ; écrit le
  2026-11-16 à partir de 12:13:46Z (`date -u`) ; il n'est ni lecteur ni juge d'aucun verdict ; il n'a ouvert aucune sortie
  de 7a, 7b, T0.7 ou P3-bis, ni aucun texte de T0.7 ou de B bis (noms et empreintes seulement).
- **Pièces produites dans ce dossier** (chacune scellée, compagnon égal) :
  - `calendrier-et-remise-phase-c-v3-v1.md` (`1dd534af0f75ac7a0ba454dc11a87ecf51631f5888a7d1f57d58dc714c2bad21`) : réponse
    aux points 1 à 4 du coordinateur (date, conditions de registre, ce qui manque, voie de remise) ; reprise par R-2971 ;
  - `qui-a-lu-quoi-v3-brouillon1.md` (`c973c8bf5f860264d972b91f002de42ea83a1482a4d74ea24debe67b8688fa6d`) : liste v2
    recopiée à l'octet (lignes 1 à 133) et 32 lignes neuves (134 à 165) ;
  - `essai-attestation-v3-liste-v3-brouillon1-sortie-v1.txt`
    (`47047f9d282b39a27a269aa81d346290950cfe6a40864f6ed1cc2ec05f6d12bf`) : attestation v3 sur ce brouillon, cas sain
    conforme (« lignes de l'hôte admises : 1 »), trois artefacts arrêtés, un témoin fictif conforme ;
  - `ordre_prealables_rv1_v1.py` (`2d63d2d4ee394f2322ab9567ec14300aec5a081a1228b323ecc35141b3ac789b`) et
    `essai-ordre-prealables-rv1-sortie-v1.txt` (`ded05e28ef6a283316bdaa06b89e23c3db52b0ada5854d3658ac30b4cc8a096a`) :
    contrôle d'ordre de R-V1 ; essai sur jouets (sain : tenu ; inversé et incomplet : arrêt) et sur le registre réel
    (arrêt aujourd'hui : `LECTURE-T08-BASE-A` absente).

## Verdict

1. **Neuf préalables restent** : la phase B (course de la pièce « mots et coût » sur 7b) ; les lignes `LECTURE-T08-BASE-A`
   puis `ISSUE-MOTS-ET-COUT-T06` ; le bloc M et la ligne dédiée de BA-L2 ; la consigne du lecteur B ; la liste v3
   versée ; les lignes R-V1, R-V2, R-V4 et R-V5 ; le mot du directeur sur la date ; le message au directeur ; tout
   poussé sur `main`.
2. **Déjà fait** : `CODE-MOTS-ET-COUT-T06`, `AUDIT-FUITES-T07`, `SCELLEMENT-BBIS` (registre propre, absente du registre de
   T0.7) ; R-V3 acceptée (R-2883) ; hôte choisi (GO-2026-11-16-01, point 6) ; pièces de C5 toutes sur `main` ; brouillon 1
   de la liste v3 attesté conforme.
3. **Mots du directeur demandés** : lever la date « mardi 17 » ; coller la commande de la phase B puis celle de la phase
   C ; nommer le modèle C du lecteur B ; sa décision si BA-L2 s'applique et si l'ordre entre l'étape B et B bis bloque.

## 1. Préalables, un par un

Ordre d'exécution conseillé : 1.1 → 1.2 → 1.3, avec 1.4 à 1.6 en parallèle ; puis 1.7 à 1.10. État relevé le 2026-11-16
vers 12:00Z sur `origin/main` (clés et dates seulement).

### 1.1 Phase B : course de la pièce « mots et coût » sur 7b (blocs C0 et C2 ; § 15, bloc M)

- **Source** : C0 exige `LECTURE-T08-BASE-A` et `ISSUE-MOTS-ET-COUT-T06`. Le bloc M se joue « après les lignes
  `LECTURE-T08-BASE-A` puis `ISSUE-MOTS-ET-COUT-T06` ». Le gabarit de la phase B est au § 9 de `commande-compte-3-v1.md`
  (« version 2 requise »).
- **Fait** : code de la pièce scellé (`CODE-MOTS-ET-COUT-T06`, 2026-11-14T14:55:41Z, fichier
  `registres/code-mots-et-cout-t06/CODE-MOTS-ET-COUT-T06-v1.json`, `e418fdaf…`, commit cité `da06bb57…`, R-2778) ;
  préparateur de la commande v2 lancé par la mère à 12:06Z (R-2971).
- **Reste** : commande de la phase B v2 (contre-lue, scellée, poussée) ; remise par le directeur dans la session hôte ;
  course par l'hôte ; vérification des blobs par la mère, sans les ouvrir.
- **Contraintes que la phase B v2 doit tenir pour que la phase C v3 passe telle quelle** (liste pour son préparateur) :
  1. elle fixe la branche des sorties (gabarit : `verdict/t06-mots-et-cout-compte-3-v1`, absente au distant à 12:02Z) :
     c'est la valeur de `<<BRANCHE_PIECE>>` (C2) et de `BRP` (bloc M), sauf si la mère recopie les fichiers dans `main` ;
  2. le fichier que citera `ISSUE-MOTS-ET-COUT-T06` doit avoir un chemin **sans espace** (C2 et C5 le lisent par
     `cut -d'|' -f4 | tr -d ' '`) et son compagnon `.sha256` sur la même branche ; ce chemin ne doit contenir aucun
     fragment de `INTERDITS_NOMS_B` (C5 arrête sinon) ;
  3. le fichier que citera `LECTURE-T08-BASE-A` doit porter la clé `lignes.BA-L2.s_applique`, défaut du bloc M. La pièce
     v3 écrit `"BA-L2": {"s_applique": …}` ; je l'ai relevé par mot-clé seulement, la mère le confirme au bloc M, sinon
     `--cle-json` ;
  4. les exclusions de l'hôte : la ligne de l'hôte de la liste v3 doit porter **exactement** `CELLULE_HOTE` (bloc 2C).
     Si la phase B ajoutait une exclusion à l'hôte, il faudrait l'écrire ailleurs que dans cette cellule, ou passer à une
     version 4 de la phase C. `CELLULE_HOTE` n'exclut que l'écriture et la contre-lecture du code de la pièce, non sa
     course ;
  5. aucun fichier de 7b commité ; un seul appel ; sortie jamais affichée ; seuls `diag/<run>/` et `runs/<run>/` commités,
     scellés ; garde des secrets ; journal provisoire sans issue ni nombre ;
  6. les sorties de la phase B (tirées de 7b) ne vont dans aucun espace de B bis ni du lecteur B, hors du fichier cité par
     `ISSUE-MOTS-ET-COUT-T06`, que C5 remet au lecteur B.
- **Qui, combien** : préparateur et contre-lecture, 2 à 3 heures ; directeur, remise ; hôte, moins de 2 heures (rapport
  v1).

### 1.2 Lignes `LECTURE-T08-BASE-A` puis `ISSUE-MOTS-ET-COUT-T06` (bloc C0)

- **Fait** : rien. Les deux clés sont absentes.
- **Reste** : après la phase B, blobs vérifiés par empreinte sans ouverture, puis les deux lignes, dans cet ordre, par le
  même outil que `CODE-MOTS-ET-COUT-T06` (`t07.registre_v1.ajouter_ligne`, heure du système, R-2778), au format
  `| CLÉ | AAAA-MM-JJTHH:MM:SSZ | chemin relatif | sha256 |`. Aucune ligne de verdict dans `registres/scellements-v1.md`.
- **Qui, combien** : la mère, environ 15 minutes.

### 1.3 Bloc M et ligne dédiée `<<R_BA_L2>>` (§ 15 ; bloc C0)

- **Fait** : programme `lecture_etat_ba_l2_mere_v1.py` (`6d63e9d6e7036310597a7a19711e431910278cf07b48132a376edcf147cf44d0`),
  essai 10 sur 10 (commande, pièces) ; texte du bloc M écrit au § 15 de la commande.
- **Reste** : jouer le bloc M (variable `BRP` = branche de la phase B), écrire la ligne dédiée, effacer le dossier de
  travail par son chemin exact.
- **Brouillon de la ligne** (une seule ligne du registre ; elle doit nommer « BA-L2 » ; aucun mot de la liste
  `INTERDITS_CONTENU_B` de la commande, ni « bbis », ni « b bis », casse comprise ; aucun autre fait ; elle sera recopiée
  telle quelle dans l'extrait du lecteur B) :

  ~~~~text
  | R-<n> | 2026-11-<jj> (<HH:MM> UTC, `date -u`) | **État de BA-L2 avant l'étape B de T0.7** (bloc M de la commande phase C v3, § 15 ; N-C, R-2741 ; T0.7 l. 2183) : `lecture_etat_ba_l2_mere_v1.py` (`6d63e9d6…`) sur le fichier cité par `LECTURE-T08-BASE-A` (branche `<BRP>`) : « ÉTAT BA-L2 : ne s'applique pas » (code 0). Dossier de travail effacé par son chemin exact. | registre ; état |
  ~~~~

  Variante, code 3 (« s'applique ») : même ligne avec « ÉTAT BA-L2 : s'applique », puis, dans la même ligne, le mot de
  Lazar mot pour mot (la commande : « état seul, ou mot de Lazar ») ; aucune étape B avant ce mot. Code 2 (« illisible ») :
  pas de ligne dédiée, nœud, aucune remise.
- **Contrôle avant d'écrire** : `printf '%s' "$LIGNE" | grep -c -i -E 'bbis|b-bis|etape-b-bis|étape b bis|b bis|bras-attaque|mode-tenu'`
  doit rendre 0, et `grep -c 'BA-L2'` doit rendre 1 ou plus (mêmes filtres que C0).
- **Qui, combien** : la mère, environ 10 minutes.

### 1.4 Consigne du lecteur B (§ 0.2 ; blocs 1C, C5 et C6)

- **Fait** : rédacteur lancé par la mère à 12:06Z (R-2971). Je n'ai pas le droit de lire le texte de T0.7 : je ne rédige
  donc pas les critères ; je donne les contraintes que la commande impose.
- **Reste** : rédaction, contre-lecture par un autre modèle, sceau, poussée sur `main` ; l'empreinte devient
  `<<EMPREINTE_CONSIGNE_LECTEUR_B>>`.
- **Contraintes tirées de la commande** (à vérifier par le contre-lecteur) :
  1. chemin sur `main`, avec son compagnon (C5 le copie depuis le dépôt de l'hôte, par `cp --parents`) ; nom sans aucun
     fragment de `INTERDITS_NOMS_B` ; proposition : `docs/procedures/lecture-7b-etape-b-compte-3-v1/consigne-lecteur-b-v1.md` ;
  2. lecteur : sous-agent neuf du modèle C, sans contexte hérité, ni le lecteur A ni un lecteur de B bis (§ 2) ; son
     modèle s'écrit « modèle C » ; « modèle A » est celui des auteurs de T0.7 (message de remise, C6) ;
  3. il recopie d'abord son message dans `<ESPACE>/verdict-ferme/verdict-T0.7-etape-B-v1-message-recu-v1.txt` ; C7 le
     compare au message scellé, sauts de ligne finaux retirés ;
  4. pièces : bordereau `<ESPACE>/bordereau-remise-v2.txt` (scellé, format `sha256sum`), **27 lignes** attendues : les
     13 fichiers et leurs 13 compagnons, plus `extrait-registres-etape-b-v2.md`. Les 13 fichiers : `prereg/T0.7-sondes-v0-v1.md`,
     `prereg/T0.7-sondes-v0-v1-addendum-cache-motifs-v1.md`, `prereg/T0.7-sondes-v0-v1-configuration-t07-v8.json`,
     `prereg/T0.6-organismes-v0-v1.md`, `prereg/T0.8-base-A-mots-et-cout-v1.md`, `prereg/T0.7-consigne-audit-fuites-v1.md`,
     `docs/decisions/decision-N-063-v2.md`, `docs/verdicts/verdict-P3-bis-v1-issue.json`, la consigne elle-même,
     `diag/20261114-001352-t07-lecture-reel/lecture-t07.json`, `runs/20261114-001352-t07-lecture-reel/manifeste.json`,
     `diag/20261114-001352-t07-lecture-reel/audit-fuites-t07.json`, et le fichier cité par `ISSUE-MOTS-ET-COUT-T06`.
     L'extrait porte toutes les lignes de `registres/scellements-v1.md`, les lignes de l'étape B du journal des ouvertures
     et la ligne dédiée `<<R_BA_L2>>` ;
  5. noms permis dans `verdict-ferme/`, motif exact de C7 :
     `^verdict-T0\.7-etape-B-v1(\.md|-issue\.json|-[a-z0-9-]+-v[0-9]+\.(py|txt|json|md))(\.sha256)?$` ; aucun
     sous-dossier ni archive ; le verdict en prose `verdict-T0.7-etape-B-v1.md` est exigé (C7 s'arrête sinon) ; fichier
     d'issue `verdict-T0.7-etape-B-v1-issue.json`, avec la forme que la consigne fixe ; chemin de copie
     `docs/verdicts/verdict-T0.7-etape-B-v1.md` ;
  6. **R-V2** : rapport final fermé de quatre lignes, `STATUT : …`, `FICHIERS : …`, `DÉCLARATIONS : …`, `MESSAGE REÇU :
     sha256 …`, sans aucun nombre, aucune issue, aucune ligne de table, aucune empreinte d'un fichier du run (F-C ne garde
     que les lignes qui commencent par STATUT, FICHIERS, DÉCLARATIONS, MESSAGE) ; liste fermée des codes d'arrêt ;
  7. cloisonnement (§ 0.5) : la consigne est une pièce du lecteur B ; recommandation, à trancher par la mère : n'y nommer
     l'étape B bis que dans les interdits recopiés du message de remise, sans rien de son contenu ; les noms de pièces sont
     déjà filtrés par C5 ;
  8. les critères : recopiés à l'octet du texte scellé de T0.7 et de N-063 v2, par le rédacteur autorisé (le critère 3 de
     G0 n'est jugé qu'aux doses où la base « mots et coût » échoue selon son propre critère, « sans objet » si aucune).
- **Plan de forme proposé** (celui de la consigne A, `b5abfa16…`, adapté) : statut et rédacteur ; 0. rôle et déclarations
  (n'avoir écrit ni T0.7, ni son code, ni cette consigne ; n'être ni le lecteur A, ni un lecteur de B bis, ni l'hôte, ni la
  session-dépôt ; modèle C ; heures par `date -u`) ; 1. interdits (message recopié, puis les règles propres) ; 2. pièces
  et bordereau (27 lignes) ; 3. critères gelés recopiés à l'octet ; 4. où les nombres sont écrits dans `lecture-t07.json`
  (aide non gelée) ; 5. marche à suivre (bordereau, rattachements au manifeste de T0.7 et au registre, état de BA-L2 lu
  dans l'extrait, lecture, comparaison à la ligne mécanique du module) ; 6. calculs permis ; 7. noms permis ; 8. fichier
  d'issue ; 9. message reçu ; 10. verdict en prose ; 11. ce que tu rends.
- **Qui, combien** : rédacteur et contre-lecteur, environ 3 heures.

### 1.5 Liste « qui a lu quoi » v3 (§ 0.2 ; blocs 1C et 2C)

- **Fait** : brouillon 1 (`c973c8bf…`), attesté conforme par l'attestation v3 avec la vraie cellule `CELLULE_HOTE`
  (`47047f9d…`).
- **Reste** (réserve 8 du brouillon) : ajouter le préparateur de la phase B et le rédacteur de la consigne B (R-2971),
  leurs contre-lecteurs, les faits de la phase B dans la colonne « a lu » de la ligne 134 (la cellule « exclu de » restant
  `CELLULE_HOTE`) ; trancher les cas douteux (réserve 5) ; vérification courte par un agent neuf ; versement sous un nom
  de version, par exemple `registres/qui-a-lu-quoi-v3.md` ; sceau ; attestation rejouée sur le fichier versé (cas sain
  et un artefact) ; poussée ; l'empreinte devient `<<EMPREINTE_LISTE>>`.
- **Qui, combien** : la mère et un vérificateur, environ 1 heure après la phase B.

### 1.6 Lignes R-V1, R-V2, R-V4 et R-V5 de la mère (vérification courte, § 6 ; R-2845)

- **R-V1, ordre des préalables** : fait : contrôle `ordre_prealables_rv1_v1.py` (`2d63d2d4…`, essai `ded05e28…`). Reste :
  le jouer après 1.2, puis écrire la ligne. **Cas douteux** : la vérification courte écrit l'ordre « AUDIT < CODE » ; le
  registre a « CODE < AUDIT », ordre voulu par R-2767 et R-2779. Le contrôle proposé tient l'ordre du registre ; à
  trancher par la mère. Brouillon :

  ~~~~text
  | R-<n> | 2026-11-<jj> (<HH:MM> UTC, `date -u`) | **R-V1 levée (ordre des préalables de l'étape B)** : `ordre_prealables_rv1_v1.py` (`2d63d2d4…`, essai `ded05e28…`) sur `origin/main` `<commit>`, code 0 : `CODE-MOTS-ET-COUT-T06` 2026-11-14T14:55:41Z < `AUDIT-FUITES-T07` 2026-11-14T14:57:54Z < `LECTURE-T08-BASE-A` <date> ≤ `ISSUE-MOTS-ET-COUT-T06` <date> ; la ligne dédiée de BA-L2 (R-<n>) vient après. L'ordre « AUDIT < CODE » de la vérification courte (`cb9757d5…`, § 6) est remplacé par celui de R-2767 et R-2779 (coffre de l'audit ouvert après la ligne du code de la pièce) : décision de la mère. | décision ; constat |
  ~~~~

- **R-V2, consignes et recopies** : reste : la règle des quatre lignes dans la consigne B (1.4, point 6), puis la ligne.
  Brouillon :

  ~~~~text
  | R-<n> | 2026-11-<jj> (<HH:MM> UTC, `date -u`) | **R-V2 levée** : la consigne du lecteur B (`<chemin>`, `<empreinte>`, contre-lue `<empreinte>`) interdit tout nombre, toute issue, toute ligne de table et toute empreinte d'un fichier du run dans les lignes STATUT, FICHIERS, DÉCLARATIONS et MESSAGE de son rapport final. La phase C v3, § 15 (2), se lit : « recopie, par programme et sans les ouvrir ni les afficher (N-C : seul l'état BA-L2 est lu), les fichiers du verdict B, rescelle ». | décision |
  ~~~~

- **R-V3, information vers la mère** : fait (R-2883 : acceptée ; code de sortie, durée, nombre de lignes du journal et,
  sur un code 2, la ligne `REFUS-T07` sont consignés comme état d'exécution, non comme résultat).
- **R-V4, section 9 du contrôle à blanc** : reste : la ligne, en remettant. Recommandation : garder `--chaine`, confiance
  0,75 : le module lit ces fichiers de toute façon à l'appel, et retirer `--chaine` changerait le texte du bloc C3 (version
  4, ou écart déclaré). Brouillon :

  ~~~~text
  | R-<n> | 2026-11-<jj> (<HH:MM> UTC, `date -u`) | **R-V4 : la mère accepte**, en remettant la commande phase C v3 (`9d788919…`), la lecture structurelle par programme de la section 9 du contrôle à blanc (§ 0.4 ; `--chaine` gardé au bloc C3) : garde d'ouverture du module sur une copie du registre, puis lectures d'avant les scores (table A, issue de P3-bis, audit, fichier « mots et coût », épisodes, colonnes des mesures), sans rien afficher ; jamais les scores. | décision |
  ~~~~

- **R-V5, références** : reste : (b) le directeur dit « v3 » et donne `9d788919…` à la remise (le bloc 0b-C compare) ;
  (a) et (c) dans une ligne. Brouillon :

  ~~~~text
  | R-<n> | 2026-11-<jj> (<HH:MM> UTC, `date -u`) | **R-V5** : (a) le plan de B bis scellé avant la lecture de l'étape B vient de R-2714 (2) et R-2716 (1), non de R-2740 ; (b) la commande remise est la phase C **v3** (`9d7889198238c171447a06f56f1a37beb4190572c3a9ceceb18144541c258d2e`), non la v2 que nomme la phase A ; (c) réserves du rapport v2 du préparateur ouvertes : module d'étape B jouet seulement en répétition, blocs C1 et C1a non exercés sur le vrai dépôt, voies des scores non éprouvées avant l'appel (code 3 possible), transport local des répétitions. | constat |
  ~~~~

### 1.7 Mot du directeur sur la date (GO-2026-11-16-01, point 6)

- **Reste** : la ligne porte « jouée mardi 17 ». La précision du directeur (relayée le 16 vers 11:50Z) en fait une
  estimation (`calendrier-et-remise-phase-c-v3-v1.md`, § 1). Une ligne de GO ne s'écrit que sur un mot direct : la mère
  inscrit son mot mot pour mot. Brouillon :

  ~~~~text
  | R-<n> | 2026-11-16 (<HH:MM> UTC, `date -u`) | **Mot direct de Lazar**, verbatim : « <mot> ». Lecture : la phase C v3 du compte 3 est remise dès que ses préalables sont prêts, dans la session hôte actuelle (voie (a) en repli) ; « mardi 17 » au point 6 de GO-2026-11-16-01 était l'estimation du chemin critique (rapport v1 du préparateur, l. 15 ; R-2734), non une condition. | mot de Lazar ; décision |
  ~~~~

### 1.8 Valeurs des huit marqueurs du bloc 1C

| marqueur | valeur | état |
|---|---|---|
| `<<LISTE>>` | `registres/qui-a-lu-quoi-v3.md` (proposé) | à verser (1.5) |
| `<<EMPREINTE_LISTE>>` | empreinte du fichier versé | à venir |
| `<<CONSIGNE_LECTEUR_B>>` | `docs/procedures/lecture-7b-etape-b-compte-3-v1/consigne-lecteur-b-v1.md` (proposé) | à écrire (1.4) |
| `<<EMPREINTE_CONSIGNE_LECTEUR_B>>` | empreinte du fichier scellé | à venir |
| `<<REGISTRE_BBIS>>` | `registres/t07-etape-b-bis-v1.md` | connu (R-2762) ; sur `main` |
| `<<CLE_PLAN_BBIS>>` | `SCELLEMENT-BBIS` | connu ; une ligne, 2026-11-14T12:30:30Z ; absente du registre de T0.7 |
| `<<R_BA_L2>>` | numéro de la ligne dédiée (1.3) | après le bloc M |
| `<<BRANCHE_PIECE>>` | branche de la phase B (gabarit `verdict/t06-mots-et-cout-compte-3-v1`), ou `main` si la mère y recopie le fichier « mots et coût » | après la phase B |

### 1.9 Message de la mère au directeur, à coller par lui dans la session hôte (brouillon)

~~~~text
Pour la session hôte du compte 3 (session de la phase A) : commande phase C, version 3,
docs/procedures/lecture-7b-etape-b-compte-3-v1/commande-compte-3-phase-c-v3.md,
sha256 9d7889198238c171447a06f56f1a37beb4190572c3a9ceceb18144541c258d2e (la v3, non la v2).
Hôte : cette session (GO-2026-11-16-01, point 6 ; R-<n> : remise dès que les préalables sont prêts).
Valeurs du bloc 1C : LISTE='<chemin>' ; EMPREINTE_LISTE='<empreinte>' ;
CONSIGNE_LECTEUR_B='<chemin>' ; EMPREINTE_CONSIGNE_LECTEUR_B='<empreinte>' ;
REGISTRE_BBIS='registres/t07-etape-b-bis-v1.md' ; CLE_PLAN_BBIS='SCELLEMENT-BBIS' ;
R_BA_L2='R-<n>' ; BRANCHE_PIECE='<branche ou main>'.
Lecteur B : sous-agent neuf du modèle C ; je te le nomme ici, en conversation : <nom, jamais écrit dans un fichier>.
Rapport final du lecteur : à moi seul ; à la mère, le point 3 de la section 13.
~~~~

### 1.10 Tout poussé sur `main` avant le message (§ 0.2)

- **Reste** : les lignes 1.2, 1.3, 1.6 et 1.7 ; la consigne B et son compagnon ; la liste v3 et son compagnon. Le bloc
  0b-C de l'hôte avance `main` en avance rapide : la commande est lue sur `main` au moment de la remise. Contrôle : le
  bloc C0 de la commande, joué à blanc par la mère en lecture seule sur `origin/main`, avant le message (quatre « ligne …
  : une », la ligne dédiée, le plan de B bis).

## 2. Côté hôte et directeur (à rappeler dans le message)

- Session hôte joignable ; quota sous 80 % avant C4a et C6 ; dossier `$HOME/bac-etape-b-compte-3-v2` absent (sinon le bloc
  1C s'arrête) ; identité git ; 9 Gio libres si l'environnement avec torch doit être créé (C1a) ; réseau vers `pypi.org`
  (horloge) et `github.com` (brief de relance, § 7).
- L'outil d'agent de l'hôte doit pouvoir créer un sous-agent du modèle C, sans repli (§ 2, § 14).
- Codes de l'étape B : 2, refus, et relance seulement par une version nouvelle sur un mot de la mère ; 3, nœud du
  directeur ; borne de 60 minutes dépassée, nœud, le processus continue (§ 14).

## 3. Points qui demandent un mot du directeur

1. **Date** : lever « mardi 17 » du point 6 de GO-2026-11-16-01 (1.7). Recommandation : oui, confiance 0,8.
2. **Phase B** : coller sa commande v2 dans la session hôte (même voie que la phase A) ; confirmer que l'hôte la joue
   (dessein de la commande v1). Recommandation : oui, confiance 0,75.
3. **Modèle du lecteur B** : nommer le modèle C en conversation. Tout autre modèle, par exemple le modèle B redevenu
   disponible (R-2813), serait un écart à la commande (version 4). Recommandation : modèle C tel qu'écrit, confiance 0,8.
4. **BA-L2** : son mot avant l'étape B si le bloc M rend « s'applique » (T0.7 l. 2183, par la commande).
5. **Ordre entre l'étape B et B bis** : R-2971 confie la question au préparateur de la course de B bis. Si B bis exige
   l'absence de l'étape B à son lancement (clé `ABSENCE-B-BBIS`, « relevé de l'étape B » de l'addendum, R-2959), deux
   choix : jouer l'étape B après la course de B bis, ou tenir le journal et le verdict B hors de tout commit que B bis
   fusionnera. Le choix revient au directeur (calendrier du billet, au plus tard dimanche 22).

## 4. Décisions de routine laissées à la mère (cas douteux relevés)

- Ordre de R-V1 (1.6) ; forme de la ligne du lecteur A et exclusions par analogie ; exclusion « lecteur B » des lecteurs
  de B bis au sens large ; lignes 139, 141, 150 et 160, 151 à 153, 154, 156, 162 et 164 de la liste (réserve 5 du
  brouillon) ; incident R-2958 (noms sous `diag` et `runs`), non ajouté.
- R-2778 écrit « la course (phase B, compte 3, après l'étape B) » : la commande v3 (C0, bloc M) et la lecture du module
  (section 9 du contrôle à blanc) veulent la course **avant** l'étape B ; à corriger par une ligne, sans effet sur le
  reste.
- Les fichiers de ce préparateur sont non suivis dans l'arbre de travail commun : à verser par leur nom, jamais par un
  ajout global.

## 5. Après la remise (pour mémoire, § 15 de la commande)

Recopie du seul commit du journal des ouvertures dans `main`, avant toute autre écriture dans ce journal ; recopie des
fichiers du verdict B, par programme et sans les ouvrir (R-V2) ; `lecture-t07.json` laissé sur la branche avec le chemin et
l'empreinte du manifeste de T0.7 ; liste « qui a lu quoi » suivante (hôte : exclusions de la phase C ; lecteur B : pièces
du bordereau) ; verdict soumis au directeur ; rien de la branche de l'étape B dans un espace de B bis avant le verdict
scellé de B bis ; table conjointe B et B bis lue après les deux.

Fin : 2026-11-16T12:15:32Z (`date -u`).
