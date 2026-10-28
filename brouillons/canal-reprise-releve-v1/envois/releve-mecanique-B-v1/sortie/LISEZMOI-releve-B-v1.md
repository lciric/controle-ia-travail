# Relevé mécanique (B) du pilote 4 — LISEZMOI du script v1

Écrit le 2026-10-26T07:07:49Z (heure lue sur `date -u` dans la commande qui écrit ce fichier) par un sous-agent neuf de la lignée
conv-audit. Tout ce qui suit est établi sur les pièces de **simulation** des séries v13 et v14 ; aucune pièce d'une course
réelle n'a été ouverte. Ce document ne porte aucune valeur de score.

Font foi : la spécification v2 (`701b5270…`, qui remplace la v1 `3ed32fe8…`), le brief v1 (`a047c89f…`), les deux
décisions de conv-audit du 26 octobre 2026 (`releve.course`, `identite.lignee`) et ses deux précisions issues du constat
CLB4-06 (ligne de réponse).

## 1. Pièces (`sortie/`)

| pièce | empreinte sha256 |
|---|---|
| `releve_mecanique_pilote4_v1.py` | `b51699c77b5e0d6d5132bb58fa5b7ab48ff8f736677bb5fcacc3ffe28204bfac` |
| `table-correspondance-releve-B-v1.json` | `5cfafe33e8b4a2a2525f53b6b642ea8ad59d427f75d5e6560eb419bd8719f95a` |
| `essais_releve_mecanique_pilote4_v1.py` | `4c16a35db4888105b15634c86fd854c7b10c1cb548bc7858639e833b40c93445` |
| `journal-essais-releve-B-v1.log` | `35c55aa280aaea278288f53c0000ff28dca2cde248f4d8371b021bd6ad57b673` |

Chaque pièce a son compagnon `.sha256` (« empreinte, deux espaces, nom nu »). Le script porte l'empreinte de la table et
refuse toute autre table ; avant de rien lire, il vérifie aussi son propre compagnon, posé à côté de lui.

## 2. Ce qui a changé pour moi (spécification v2, décisions et précisions de conv-audit)

J'avais commencé sur la v1 et le brief ; je me suis recalé sur la v2 dès son arrivée, puis sur les décisions et les
précisions. Changements :

- **Identité lue au seul `LANCEMENT.md`**, par des motifs exacts qui couvrent la ligne entière (lignes « - course »,
  « - dépôt », « - lanceur », « - préenregistrement », « - organisme », « - code », écrites d'après le code des lanceurs
  v10 et v11). Mon premier brouillon croisait le commit, l'arbre, la graine et la question avec le manifeste recopié
  dans l'extrait : retiré.
- **`identite.graine`** (exigée, ligne « - préenregistrement ») et **`identite.graine_manifeste`** (facultative, lue
  dans l'extrait sous `manifeste.entropie_seed_sequence`, recopiée sans comparaison : les deux sont dans le relevé).
- **`identite.noyau` et `identite.banque_empreinte`** lues sur la ligne « - code : identique à … ; banque … ». Mon
  brouillon prenait la banque du manifeste : en simulation, les deux empreintes diffèrent (le noyau simulé charge une
  autre banque que celle du dépôt).
- **Lignes d'identité lues dans toutes les sections** (segments et essais refusés compris) : deux valeurs différentes
  d'un même champ font refuser, avec le nom du champ.
- **`unite.g001.question_servie`** : lue sur la ligne qui commence par « - réponse à la question : », reconnue par ce
  seul début (précision 1 de CLB4-06) : `oui` sans les mots « aucune pièce archivée » ; `absent` avec eux ou sans ligne ;
  jamais `non` ; jamais un champ de l'extrait. Mon brouillon lisait `question_ouverte.posee` dans l'extrait, avec une
  exception à la liste noire pour ce conteneur : exception retirée, plus aucun champ de l'extrait dont un composant
  contient « question » n'est lu.
- **Aucune chaîne « reponse-question »** ni dans le script ni dans sa table (précision 2 de CLB4-06) ; la preuve est
  double : par construction (essai A04d) et par la trace des ouvertures de fichiers (essais A04a à A04c).
- **`releve.course`** (décision 1) : dernier élément du chemin de la ligne « - course : <clé> ; dossier du pilote :
  <chemin> (0700, à root) », privé d'un suffixe `-tentative<N>`, qui doit être le nom que la table close écrite dans le
  script donne à la clé (`v6-2` → `pilote4-gemini-v6-2-v1` ; `v6-2-s` → `pilote4-gemini-v6-2-s-v1`) ; sinon refus.
  Mon brouillon prenait le titre « # Lancement du pilote <nom> ».
- **`identite.lignee`** (décision 2) : l'extrait porte la lignée hors de la liste noire (clés de `rapport.lignees` et de
  `manifeste.organismes_imposes`, champ `generations[].lignee`) ; le relevé la recopie et le script vérifie qu'elle est
  unique et égale à celle de la table close (`gemini-organisme-v6-2`, `gemini-organisme-v6-2-s`), sinon refus. Sans
  extrait (artefact 5), elle est **déduite de la clé de course**. Conséquence : l'artefact 5 donne de nouveau un relevé
  écrit, comme le veut la spécification.
- **Empreinte de question inconnue** : refus avec le motif `identite.question` (v2, artefact 12).
- **Cas v13 v5.3** : sa clé de course `v5-3` n'est pas dans la table close ; il est donc refusé (`releve.course`), ce qui
  s'écarte du cas sain 1 de la v2 (« un relevé écrit par cas ») ; ses comptes sont essayés par les fonctions du script
  lui-même (essai S3b). Voir § 8.
- Essais ajoutés pour la v2 (n° 11 à 14), pour les décisions (A17, A18), pour CLB4-06 (A04d, A25 à A25c) et pour les
  vérifications demandées (P4, P5, S6).

## 3. Usage

```sh
python3 -I releve_mecanique_pilote4_v1.py DOSSIER_DE_COURSE DOSSIER_DE_SORTIE
```

- Écrit `DOSSIER_DE_SORTIE/releve-mecanique-<dossier>-v1.txt` et son compagnon, en création exclusive ; `<dossier>` est
  le nom exact du dossier de course donné en argument. Un relevé déjà présent sous ce nom : refus (R12). Un dossier de
  sortie égal au dossier de course ou placé dedans : code 2.
- Sortie standard : une seule ligne, `relevé écrit : <fichier> <empreinte>`. Codes : 0 écrit ; 2 usage ; 3 refus (sortie
  d'erreur : `REFUS : <nom de champ>`, jamais une valeur) ; 4 erreur interne (`ERREUR INTERNE : <type> ligne <n>`).
- Lit le contenu de : `EMPREINTES-pilote-v1.txt` et son compagnon, `LANCEMENT.md`, `A-POUSSER-v1.txt`,
  `extrait-mecanique-v1.json`, `journal-appels-<unité>.jsonl`, chacun seulement s'il est dans la liste fermée et conforme.
  Hache, sans en rien lire d'autre, tous les autres fichiers de la liste fermée (dont `ferme.tar.gz`, `question.md`,
  `reponse-question-g001.md` et ses compagnons, `organisme/…`), comme le brief le demande pour vérifier la liste comme
  `sha256sum -c`. Parcourt les noms de l'arbre (sans ouvrir de fichier) pour refuser tout lien symbolique ou fichier
  spécial. Ne décompresse rien, ne suit aucun lien, n'exécute rien, n'utilise pas le réseau ; bibliothèque standard seule.
- Éprouvé sous Python 3.11.17, 3.12.3 et 3.13.17 (`/usr/bin/python3.11`, `python3.12`, `python3.13`), et sous la langue
  système C.

## 4. Commandes de session-depot (courses réelles)

Depuis la racine du dépôt de travail. `RELEVE` est le dossier où session-depot a posé une copie des pièces de `sortie/`
(script, table et leurs compagnons) ; `SORTIE` est un dossier à part, hors de tout dossier de course.

```sh
RELEVE=<dossier des pièces du relevé>
SORTIE=essaim-m3-refonte-v1/pilotes/releves-mecaniques-B-v1
( cd "$RELEVE" && sha256sum -c releve_mecanique_pilote4_v1.py.sha256 table-correspondance-releve-B-v1.json.sha256 \
  && test "$(cut -d' ' -f1 releve_mecanique_pilote4_v1.py.sha256)" = b51699c77b5e0d6d5132bb58fa5b7ab48ff8f736677bb5fcacc3ffe28204bfac ) \
  || echo "pièces du relevé non conformes : arrêt"
mkdir -p "$SORTIE"

# Course M (finie), lanceur v10 :
python3 -I "$RELEVE/releve_mecanique_pilote4_v1.py" essaim-m3-refonte-v1/pilotes/pilote4-gemini-v6-2-v1-tentative2 "$SORTIE" \
  > "$SORTIE/sortie-releve-pilote4-gemini-v6-2-v1-tentative2-v1.txt" \
  2> "$SORTIE/erreur-releve-pilote4-gemini-v6-2-v1-tentative2-v1.txt"; echo "code $?"

# Course S, lanceur v11, seulement une fois fermée (liste fermée écrite, ligne « - archive fermée » au LANCEMENT.md) :
python3 -I "$RELEVE/releve_mecanique_pilote4_v1.py" essaim-m3-refonte-v1/pilotes/pilote4-gemini-v6-2-s-v1 "$SORTIE" \
  > "$SORTIE/sortie-releve-pilote4-gemini-v6-2-s-v1-v1.txt" \
  2> "$SORTIE/erreur-releve-pilote4-gemini-v6-2-s-v1-v1.txt"; echo "code $?"
```

- Seul le code de retour s'affiche. Le relevé, son compagnon et les deux fichiers de sortie sont poussés **sans être
  lus** (retenue : le relevé porte des bits sur les scores de `test`). Relevés attendus :
  `releve-mecanique-pilote4-gemini-v6-2-v1-tentative2-v1.txt` et `releve-mecanique-pilote4-gemini-v6-2-s-v1-v1.txt`.
- Code 3 : le fichier d'erreur ne porte qu'un nom de champ, que conv-audit peut lire sans lever la retenue.
- Sur `$PILOTE` plutôt que sur la copie poussée : même commande, tant que le dossier porte le même nom.
- Pour mémoire, l'identité attendue que l'assemblage comparera (le script ne la compare pas) : commit du segment 1 de M
  `d1af7a21d614d03d0e3c1eb5a63578f8a611840c`, de S `067b41da1af79384b29770b3824af2cf01c15b59`.

## 5. Réponses aux questions du § 8 de la spécification

**Champs de l'extrait mécanique** (`extrait-mecanique-v1.json`, `extrait_version = 2`, même structure dans les sept cas
des séries v13 et v14). Racine : `course`, `evenements`, `extrait_version`, `generations`, `manifeste`, `quand_utc`,
`rapport`, `totaux_hors_importees`.
- `generations[]` : une entrée par unité, `chemin = "<lignée>/<unité>"` (`c001`, `g000` à `g003`) ; lus : `statut`,
  `cout_usd` (4 décimales), `execution.duree_s` (2 décimales), `execution.delai_depasse`, `n_recherches`,
  `n_telechargements`, `services.recherches.<source>.<statut>` (sources `arxiv`, `openalex`, `semanticscholar`,
  `simulation`, `web`), `successeur`, `problemes_successeur`, `refus_noyau`, `importee`, `lignee`,
  `organisme.n_castes_recrutees`. Jamais lus : `question_ouverte`, `organisme.bilan_spectral` (décimaux sans unité),
  `organisme.n_taches_test*`, `appels.max_tokens_demandes`, `appels.usage_par_espece`, `fichiers_travail`, etc.
- `evenements[]`, selon `etape` : `amorcage`, `graine`, `ronde_conception`, `conception`, `fin_conception`
  (`declaration.critere`, `declaration.ronde_conception`, `declaration.n_exemplaires_isvd` lus ;
  `declaration.exactitude_moyenne_sonde`, de la liste noire, jamais lu), `arret_conception`, `ronde`, `generation`,
  `question_ouverte`, `arret` (`raison` lue : `fichier STOP` ou `aucune lignée active`), `reprise` (segment, état,
  `n_appels_relus`, `depense_relue_usd` : jamais recopiés).
- `rapport` : `depense_totale_usd` (lu), `lignees.<lignée>.fin` (lu : `générations maximales`), `n_appels_total`,
  `rondes_conception`, `fin_utc`.
- `manifeste` : la copie du manifeste de la course (voir plus bas).

**Champs du journal d'appels** (`journal-appels-<unité>.jsonl`, une ligne JSON par appel, un fichier par unité) : `id`
(`organisme-0001`, …, unique dans l'unité, recommence à chaque unité), `role`, `statut` (lus) ; `cout_usd`,
`cumul_usd`, `debut_utc`, `fin_utc`, `espece`, `famille`, `etape`, `fin`, `modele_demande`, `modele_servi`,
`max_tokens`, `usage.entree`, `usage.sortie`, `caracteres`, `sha256_prompt`, `sha256_texte`, `types_blocs`, `angle`,
`categorie`, `echec`, `go_id`, `reel` (jamais lus, comptés dans `sources.champs_ignores`). Le journal ne porte ni la
source des recherches ni le segment.

**Ce que le noyau consigne hors de l'archive** (dans l'extrait) : la déclaration de fin de conception (ronde, critère,
exemplaires) ; le successeur produit (`successeur`) et ses problèmes (`problemes_successeur`) ; les refus du noyau
(`refus_noyau`, vides dans toutes les pièces de simulation : forme des motifs inconnue) ; le nombre de castes recrutées
et leurs rôles ; les tailles des fichiers de travail (`fichiers_travail[].octets`, dont trois `memoire_isvd.json` : à la
racine, sous `organisme/` et sous `successeur/organisme/`). Ne sont consignées nulle part hors de l'archive : la taille
de la mémoire sous un nom de mémoire, sa restauration, la mitose, l'exécution du successeur à l'unité suivante,
l'empreinte de `politique_endogene.py` (tailles seulement), des motifs de refus de l'architecte autres que `refus_noyau`.

**Nom du manifeste et clé de la graine** : aucun fichier de manifeste de course dans le dossier poussé
(`organisme/manifeste.json` est celui de l'organisme, jamais ouvert) ; l'extrait recopie le manifeste de la course sous
la clé `manifeste`, et la graine y est `entropie_seed_sequence` (entier de 19 ou 20 chiffres). `sources.manifeste` vaut
donc `absent`, et `identite.graine_manifeste` se lit par l'extrait.

**Règle de dédoublonnage** : les journaux sont par unité, non par segment ; une unité ne s'étend jamais sur deux
segments (STOP n'agit qu'entre deux unités) ; les appels « relus » à la reprise n'apparaissent que dans les événements
`reprise` de l'extrait (« 7 appels relus », puis « 130 »), jamais dans les journaux. Le script dédoublonne par (unité,
`id`), sinon par (unité, rang de la ligne) ; un doublon de même rôle et même statut compte une fois ; un doublon de rôle ou
de statut différent fait refuser (`unite.<u>.appels`). Éprouvé : les cas en deux et trois segments donnent exactement les
comptes du cas continu (c001 7, g000 123, g001 129, g002 123, g003 124), sans double compte ; essais A19a et A19b.

**Unité qui sert la question** : `g001` (`manifeste.question_ouverte.cibles = ["g001"]` dans les sept cas ; ligne
« - réponse à la question : » du lanceur). Le relevé ne le lit que sur cette ligne (§ 2 ci-dessus).

**Source de `releve.course` et de `identite.lignee`** : tranchée par conv-audit (§ 2 ci-dessus) ; la lignée est copiée
de l'extrait et contrôlée contre la table close ; sans extrait, elle est déduite de la clé de course.

**Empreintes de question des cas sains** (vérifiées, essai P4) : les quatre cas v13 et les cas v14 de forme M
(`cas-sain-v6-2`, `cas-seg-segment1`) portent l'empreinte de M (`8b1c7511…`) ; le cas v14 S porte celle de S
(`a54da93e…`). Aucun cas sain n'est refusé par la règle de `identite.question`.

**Lignes d'identité en mode simulation** (vérifié, essai P5) : dans les sept cas, la section du segment 1 porte une ligne
et une seule de chacun des motifs exacts « - course », « - dépôt » (forme du segment 1), « - lanceur »,
« - préenregistrement », « - organisme », « - code ». La ligne « - préenregistrement » (bloc conditionnel du lanceur,
v10 l. 512, v11 l. 529) est bien écrite en simulation ; dans les deux cas en segments, elle manque aux essais 3 à 5 du
segment 2, refusés (état de reprise non conforme) avant de l'atteindre, ce qui est sans effet sur l'identité.

## 6. Champs qui porteront `absent` en pratique, et fiches qui en deviennent non observables

| champ | pourquoi | fiche (spécification v2, § 9) |
|---|---|---|
| `memoire.<g>.taille`, `memoire.<g>.restauration` | non consignés hors de l'archive | HC-P4-05 : indécidable (non observable) |
| `castes.<g>.mitose` | non consigné | HC-P4-06 : en partie (nombre de castes et rôles des appels observables) |
| `mutation.<u>.successeur_a_tourne` | l'extrait ne relie pas un successeur à l'organisme de l'unité suivante | HC-P4-03 et fait rapporté de HC-P4-04 : en partie |
| `fichier.<u>.politique_endogene` | tailles seulement, aucune empreinte | HC-P4-03, HC-P4-04 : en partie |
| `unite.<u>.telechargements.<source>` | jamais émis : téléchargements indexés par statut, sans source | HC-P4-09 : en partie (recherches par source observables ; `course.telechargements_total` observable) |
| `fin.recherche_cles_faite` | aucune source du dossier de course | fin de course : information manquante, sans effet sur la garde G1 |
| `unite.<u>.question_servie` hors de `g001` | par construction | § 0.9 du registre : sans effet |
| `unite.g001.question_servie` | `absent` si « aucune pièce archivée » | § 0.9 du registre : non observable dans ce cas |
| `sources.manifeste` | aucun fichier de manifeste poussé | aucune |
| `mutation.<u>.refus.<motif>` | observable seulement si les motifs sont des identifiants simples (aucun en simulation) | HC-P4-03 : à confirmer sur la course réelle |
| `mutation.<u>.successeur_valide` | lu comme « successeur vrai et `problemes_successeur` vide » : lecture à confirmer par conv-audit | HC-P4-03 |

La demande d'instrumentation de la ronde est la liste des lignes de ce tableau. À l'inverse, **HC-P4-01 est décidable** :
la déclaration de fin de conception (ronde, critère, exemplaires) est consignée hors de l'archive, dans l'extrait.
HC-P4-07 (durées, coûts, statuts, événements, totaux) et HC-P4-08 (appels par statut) sont observables.

## 7. Point de la spécification → traitement

| point (spécification v2) | traitement |
|---|---|
| § 1 nom, compagnon, création exclusive | `releve-mecanique-<dossier>-v1.txt` dans un dossier de sortie à part ; lien en dur d'un fichier temporaire (jamais de relevé partiel) ; refus si le nom existe (A08) |
| § 1 ne porte jamais de score ni de texte | liste blanche de 26 champs de l'extrait et 3 du journal ; liste noire sur chaque composant du chemin ; grammaire fermée vérifiée avant l'écriture (A01, A02, A16, A33) |
| § 1 retenue | commandes du § 4 : relevé poussé sans être lu ; aucune valeur sur les sorties |
| § 2.1 liste fermée | compagnon, puis chaque ligne (mal formée, nom absolu ou remontant, doublon, liste vide, fichier absent ou altéré, lien) ; balayage de l'arbre (A06a à A06l, A10a à A10c) |
| § 2.2 extrait | JSON strict, décimaux exacts, `extrait_version = 2` exigé (A26, A29, A30) |
| § 2.3 journaux | `journal-appels-<unité>.jsonl`, rôle et statut en identifiants stricts, dédoublonnage (A19a, A19b) |
| § 2.4 lignes du LANCEMENT.md | motifs exacts de la table ; égalité d'un segment à l'autre (A13a à A13c) ; porte (A14) ; réponse par son début (A25 à A25c) ; rien de M dans S (S6) |
| § 2.5 manifeste | lu dans l'extrait (`manifeste`), `sources.manifeste = absent` |
| § 2 n'ouvre jamais | hachage seul des fichiers hors liste blanche ; trace des ouvertures (A04a à A04c) ; aucune chaîne « reponse-question » dans le script ni la table (A04d) |
| § 3 grammaire | formes de la table, vérifiées sur chaque ligne ; décimal sans unité refusé (A03a, A03b) ; décimal sur un entier refusé (A03c) ; jamais d'arrondi (A03d) ; forme « graine » ajoutée (§ 8) |
| § 3 normalisation | identifiants stricts (minuscules, accents ôtés ; espace, point ou plus de 48 caractères : refus) ; vocabulaire fermé pour `fin.lignee` (§ 8) |
| § 4.1 et § 4.2 | champs exigés, dans l'ordre de la v2 : un manquant fait refuser avec son nom (A11, A15, A15b, A15c) ; empreinte inconnue : `identite.question` (A12) ; table close (A17a, A17b, A18a, A18b) |
| § 4.3 segments et fin | issues lues dans le LANCEMENT.md (`stop_repris`, `stop_clos`, `stop_reprise_attendue`, `clore`, `reprise_refusee`, `refus_lanceur`, `fermeture`, `echec`, `aucune_course_partie`) ; `fin.reprise_attendue = oui` sauf fermeture ou clôture (A07, garde G1 figurée) |
| § 4.4 unités | statut, durée, coût de l'extrait ; appels du journal ; recherches par source ; question servie (§ 2) |
| § 4.5 conception | rondes tournées (journaux c… non vides) ; déclaration de l'événement `fin_conception` (plus d'une : refus) |
| § 4.6 mutation | appels du rôle `architecte_mutation_endogene` ; successeur produit et valide ; refus du noyau (A20, A20b) |
| § 4.7 mémoire, castes | castes recrutées ; le reste `absent` (§ 6) |
| § 4.8 événements, totaux | délais dépassés, statuts « plafond », arrêts sur STOP ; coût de la course recopié ; durée, recherches et téléchargements sommés exactement (A05c, A20) |
| § 5 liste blanche, noire, comptage | `sources.champs_ignores` = feuilles JSON hors liste blanche ou noires (A02, A16, A33) |
| § 6 essais | journal : 275 essais, 275 réussis, trois interpréteurs (§ 9) |
| § 7 exécution | codes 0, 2, 3, 4 (A22 à A24) ; une ligne de sortie standard, sans `[0-9][.,][0-9]` (chaque exécution) |
| § 8 | § 5 ci-dessus |
| § 9 | § 6 ci-dessus |

## 8. Écarts déclarés et réserves

1. **Forme « graine »** (`[0-9]{1,40}`) pour `identite.graine` et `identite.graine_manifeste` : la forme « entier » de
   la spécification (12 chiffres au plus) ne peut pas porter une graine de 19 ou 20 chiffres (graine S simulée :
   20 chiffres), et la v2 exige `identite.graine`. La grammaire de l'assemblage doit admettre cette forme.
2. **Normalisation du § 3** (contradiction entre « espaces remplacés par `_`, tronqués » et « avec un espace : refus ») :
   identifiants stricts, sans remplacement d'espace ni troncature (refus), sauf `fin.lignee`, lu dans un vocabulaire
   fermé de trois codes du noyau (`générations maximales`, `sans successeur valide`, `aucune lignée active`), toute
   autre valeur faisant refuser. Risque sur une course réelle : un code de fin inconnu, un statut ou un rôle avec un
   espace font refuser le relevé (code 3, nom du champ) ; il faudrait alors une v2.
3. **Cas v13 v5.3 refusé** par la table close (décision 1), contre le cas sain 1 de la v2 ; comptes essayés par les
   fonctions du script (S3b).
4. **`absent` admis par la règle générale du § 3** là où la liste du § 4 ne l'écrit pas, quand la source manque :
   `fin.liste_fermee_poussee` (sans `A-POUSSER-v1.txt`), `conception.rondes_tournees` et `evenements.plafond_refus`
   (sans journal), `evenements.delai_depasse` et `evenements.stop` (sans extrait).
5. **Lectures choisies** : `identite.lanceur` sans le suffixe `.sh` (forme « identifiant ») ; `unite.<u>.appels.total`
   compté dans le journal dédoublonné (non `n_appels` de l'extrait) ; `course.duree_totale` = somme exacte des durées
   d'exécution des unités (non l'heure de fin moins l'heure de début), `absent` si une unité n'en porte pas ;
   `fin.liste_fermee_poussee` = `A-POUSSER-v1.txt` nomme la liste fermée et son compagnon.
6. **Refus ajoutés**, tous pour éviter un repli silencieux : clé JSON en double, `NaN` ; `extrait_version` autre que 2 ;
   unité importée ; identifiant d'unité hors forme ; deux lignées ; deux déclarations de fin de conception ; doublon
   d'appel contradictoire ; refus du noyau sous une forme non simple ; nom de source inconnu (`extrait-mecanique*.json`
   autre que v1, `journal-appels*.jsonl` hors forme) ; source présente sur le disque mais hors de la liste fermée ;
   en-têtes de segment hors d'ordre ; durée à plus de 3 décimales, coût à plus de 4 (jamais arrondis) ; compagnon du
   script ou empreinte de la table non conformes.
7. **« Jamais ouvert » (artefact 4) prouvé comme « jamais lu »** : le brief demande de hacher tous les fichiers de la
   liste fermée ; la trace des ouvertures montre que la réponse, la question, l'organisme et l'archive ne sont ouverts
   que par la fonction de hachage, et qu'une réponse plantée hors de la liste fermée n'est jamais ouverte.
8. **Risque sur les segments réels** : si le HEAD du dépôt a bougé entre deux segments, la ligne « - dépôt » des
   segments suivants porte un autre commit et le relevé est refusé (`identite.commit`), comme le veut la v2 ; à savoir
   avant de lancer le script sur une course en segments.
9. **Reconstitution v13** : les quatre cas v13 sont remis en dossiers de course par le harnais (pièces fournies remises
   à leur nom réel d'après `A-POUSSER`, octets contrôlés contre `EMPREINTES-fournis-v1.txt`, compagnons et liste fermée
   fabriqués) ; ces dossiers n'ont ni archive, ni organisme, ni réponse. Les copies de travail des cas v14 lient en dur
   les fichiers hors liste blanche (aucune lecture) et ne les remplacent jamais en place ; les pièces fournies sont
   vérifiées intactes après les essais (X2).

## 9. Essais

`essais_releve_mecanique_pilote4_v1.py`, lancé par `python3 -I -B essais_releve_mecanique_pilote4_v1.py` depuis
`sortie/`, a écrit `journal-essais-releve-B-v1.log` : **275 essais, 275 réussis, 0 échec**, sous Python 3.11, 3.12 et
3.13 ; copies de travail effacées.

- Préparation : pièces et compagnons conformes ; pièces fournies et spécification v2 vérifiées ; reconstitution v13 ;
  empreintes de question (P4) ; lignes d'identité en simulation (P5) ; comptes de la v5.3 (S3b).
- Cas sains : v13 v6.2 en un, deux et trois segments (comptes égaux à `releve-serie-v13-v1.txt`, sans double compte,
  `identite.question = m`, `identite.porte_m_precedente = absent`) ; v13 v5.3 refusé par la table close ; v14 M, S et
  segments tels quels (S : `identite.question = s`, `unite.g001.question_servie = oui`,
  `identite.porte_m_precedente = oui`, aucune des 20 valeurs de M ni de la référence du second pilote dans le relevé) ;
  deux exécutions identiques hors `releve.heure` ; mêmes relevés d'un interpréteur à l'autre.
- Artefacts : les dix de la spécification (A01 à A10, avec variantes), ceux de la v2 (A11 à A14), ceux du brief (A15,
  A16), les décisions (A17, A18) et les gardes du script (A19 à A33).
- Contre-essais de mutation, hors journal (R4, résultat trop propre) : neuf versions du script, chacune avec une garde
  désactivée, passées sous Python 3.13. Les sept mutants qui affaiblissent réellement le script sont tous attrapés :
  - dédoublonnage par rang : A19a et A19b ;
  - liste noire désactivée : A33 ;
  - hachage des fichiers hors liste blanche supprimé : A04a, A04c, A06k et A06l ;
  - égalité d'un segment à l'autre supprimée : A13a à A13c ;
  - ligne de réponse ignorée : S1, S4 et A25b ;
  - balayage de l'arbre supprimé : A10a et A10c ;
  - contrôle des champs exigés supprimé : A15, les autres refus restant tenus par la grammaire finale.

  Deux mutants n'ôtaient qu'une garde doublée :
  - le refus des liens au balayage, que la branche « fichier spécial » refuse aussi : aucun essai ne l'a attrapé, et
    le comportement est inchangé ;
  - le test de doublon, la clé du dictionnaire dédoublonnant déjà : A19b l'a attrapé quand même.
