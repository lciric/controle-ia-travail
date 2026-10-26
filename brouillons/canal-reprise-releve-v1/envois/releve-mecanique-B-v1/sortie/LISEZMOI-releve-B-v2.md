# Relevé mécanique (B) du pilote 4 — LISEZMOI du script v2

Écrit le 2026-10-26T09:28:22Z (heure lue sur `date -u` dans la commande qui écrit ce fichier) par un sous-agent neuf de la lignée
conv-audit. Tout ce qui suit est établi sur les pièces de **simulation** des séries v13 et v14 ; aucune pièce d'une course
réelle n'a été ouverte. Ce document ne porte aucune valeur de score.

Font foi : la spécification v3 (`d6ac5d3f…`, qui remplace la v2 `701b5270…` et la v1 `3ed32fe8…`), le brief v1
(`a047c89f…`) et les précisions de conv-audit reçues ensuite par message : CLB4-06 (ligne de réponse), CLB5-01 (quatre
lignes portent la clé de course ; la v5.3 est l'artefact 17 ; rédaction de l'artefact 4) et l'interface avec la garde G1.

## 1. Pièces (`sortie/`)

| pièce v2 (à utiliser) | empreinte sha256 |
|---|---|
| `releve_mecanique_pilote4_v2.py` | `b4e6373bb76f68bf98b083778dde97743262472bd5aa00e16f3bcca6249b4e50` |
| `table-correspondance-releve-B-v2.json` | `4ad8b371b1a64348175c79c743ee33664b38382905b3a84ef3168290fc394c71` |
| `essais_releve_mecanique_pilote4_v2.py` | `0797ed46f35a4ef2e87f8d185c06e9c644e49db44f17f07228e798a9b8cc2dfc` |
| `journal-essais-releve-B-v2.log` | `40724404f440841831fcd540053d88a979f1fed324885010c5e4c42f27d44a07` |

Chaque pièce a son compagnon `.sha256` (« empreinte, deux espaces, nom nu »). Le script porte l'empreinte de sa table et
refuse toute autre table ; avant de rien lire, il vérifie aussi son propre compagnon, posé à côté de lui.

Les pièces v1 (`releve_mecanique_pilote4_v1.py` `b51699c7…`, `table-correspondance-releve-B-v1.json` `5cfafe33…`,
`essais_releve_mecanique_pilote4_v1.py` `4c16a35d…`, `journal-essais-releve-B-v1.log` `35c55aa2…`,
`LISEZMOI-releve-B-v1.md` `2d8fa115…`) restent dans `sortie/` telles quelles (R12). Elles sont **remplacées** : écrites
sur la spécification v2, elles ne portent pas `identite.lignee_source` et ne contrôlent la clé de course que sur trois
lignes. Elles ne doivent pas servir.

## 2. Ce qui a changé de la v1 à la v2, et où je suis la v3 ou les messages

- **`identite.lignee_source`** (v3), toujours écrit : `extrait` quand la lignée vient du champ de l'extrait que nomme la
  table, `deduite_de_la_cle_controle_non_independant` quand elle vient de la table close. La décision transmise par
  message disait seulement d'écrire « déduite de la clé de course » dans le LISEZMOI : je suis la v3.
- **Champ de lignée nommé par la table** : `generations[].lignee` (hors liste noire). Ses autres mentions dans l'extrait
  (clés de `rapport.lignees` et de `manifeste.organismes_imposes`, préfixe `<lignée>/` de `generations[].chemin`) ne
  sont que des contrôles de cohérence : toutes doivent égaler la lignée de la table, sinon refus (`identite.lignee`).
  Le script v1 lisait la lignée dans ces quatre endroits à la fois.
- **Clé de course contrôlée sur quatre lignes** (CLB5-01, postérieur à la v3, qui en compte trois) :
  - « - course : <clé> ; dossier du pilote : <chemin> (0700, à root) » (v10 l. 250 ; v11 l. 264) ;
  - « - préenregistrement : … graine <graine> de la course <clé> … » (v10 l. 512 ; v11 l. 529) ;
  - « - organisme : … ; question (<clé>) : sha256 … » (v10 l. 528 ; v11 l. 545) ;
  - « - registre : une ligne <go> de type calcul portant l'empreinte de la question (<clé>), … » (v10 l. 557 ;
    v11 l. 574).

  Une clé différente sur l'une d'elles, dans n'importe quelle section (segments et essais), fait refuser avec le motif
  `releve.course`, comme le veut la v3. Le script v1 refusait avec `identite.graine` ou `identite.question_empreinte`.
- **`unite.<u>.question_servie`** : forme `oui|absent` (v3) ; la règle (ligne reconnue par son seul début, sans les mots
  « aucune pièce archivée ») était déjà celle de la v1 depuis CLB4-06.
- **Jeu v13 v5.3** : il n'est plus un cas sain. Il est l'artefact 17 (CLB5-01, postérieur à la v3, dont le § 6 le
  compte encore parmi les cas sains) : refus attendu, code 3, motif `releve.course`, obtenu.
- **Artefacts renumérotés** selon la v3 (1 à 19) ; les autres essais suivent (A20 et au-delà).
- **Nom du relevé** : `releve-mecanique-<dossier>-v2.txt`, puisque la v3 (§ 1) veut qu'« une version nouvelle du script
  écri[ve] `-v2` ». `releve.version` reste `1`, comme l'écrit la liste close du § 4.1 ; la version du script se lit dans
  `releve.script_empreinte`.

## 3. Usage

```sh
python3 -I releve_mecanique_pilote4_v2.py DOSSIER_DE_COURSE DOSSIER_DE_SORTIE
```

- Écrit `DOSSIER_DE_SORTIE/releve-mecanique-<dossier>-v2.txt` et son compagnon, en création exclusive ; `<dossier>` est
  le nom exact du dossier de course donné en argument. Un relevé déjà présent sous ce nom : refus (R12). Un dossier de
  sortie égal au dossier de course ou placé dedans : code 2 (le relevé n'ajoute jamais de fichier au dossier de course).
- Sortie standard : une seule ligne, `relevé écrit : <fichier> <empreinte>`. Codes : 0 écrit ; 2 usage ; 3 refus (sortie
  d'erreur : `REFUS : <nom de champ>`, jamais une valeur) ; 4 erreur interne (`ERREUR INTERNE : <type> ligne <n>`).
- Lit le contenu de : `EMPREINTES-pilote-v1.txt` et son compagnon, `LANCEMENT.md`, `A-POUSSER-v1.txt`,
  `extrait-mecanique-v1.json`, `journal-appels-<unité>.jsonl`, chacun seulement s'il est dans la liste fermée et conforme.
  Tous les autres fichiers de la liste fermée (dont `ferme.tar.gz`, `question.md`, le fichier de réponse à la question
  et ses compagnons, `organisme/…`) sont **jamais ouverts pour être lus : seulement hachés par la vérification de la
  liste fermée** (preuve par construction et par la trace des ouvertures, § 9). Le script parcourt les noms de l'arbre
  (sans ouvrir de fichier) pour refuser tout lien symbolique ou fichier spécial ; il ne décompresse rien, ne suit aucun
  lien, n'exécute rien, n'utilise pas le réseau ; bibliothèque standard seule.
- Éprouvé sous Python 3.11.17, 3.12.3 et 3.13.17 (`/usr/bin/python3.11`, `python3.12`, `python3.13`), et sous la langue
  système C.

## 4. Commandes de session-depot (courses réelles)

Depuis la racine du dépôt de travail. `RELEVE` est le dossier où session-depot a posé une copie des pièces v2 (script,
table et leurs compagnons) ; `SORTIE` est un dossier à part, hors de tout dossier de course.

```sh
RELEVE=<dossier des pièces du relevé>
SORTIE=essaim-m3-refonte-v1/pilotes/releves-mecaniques-B-v2
( cd "$RELEVE" && sha256sum -c releve_mecanique_pilote4_v2.py.sha256 table-correspondance-releve-B-v2.json.sha256 \
  && test "$(cut -d' ' -f1 releve_mecanique_pilote4_v2.py.sha256)" = b4e6373bb76f68bf98b083778dde97743262472bd5aa00e16f3bcca6249b4e50 ) \
  || echo "pièces du relevé non conformes : arrêt"
mkdir -p "$SORTIE"

# Course M (finie), lanceur v10 :
python3 -I "$RELEVE/releve_mecanique_pilote4_v2.py" essaim-m3-refonte-v1/pilotes/pilote4-gemini-v6-2-v1-tentative2 "$SORTIE" \
  > "$SORTIE/sortie-releve-pilote4-gemini-v6-2-v1-tentative2-v2.txt" \
  2> "$SORTIE/erreur-releve-pilote4-gemini-v6-2-v1-tentative2-v2.txt"; echo "code $?"

# Course S, lanceur v11, seulement une fois fermée (liste fermée écrite, ligne « - archive fermée » au LANCEMENT.md) :
python3 -I "$RELEVE/releve_mecanique_pilote4_v2.py" essaim-m3-refonte-v1/pilotes/pilote4-gemini-v6-2-s-v1 "$SORTIE" \
  > "$SORTIE/sortie-releve-pilote4-gemini-v6-2-s-v1-v2.txt" \
  2> "$SORTIE/erreur-releve-pilote4-gemini-v6-2-s-v1-v2.txt"; echo "code $?"
```

- Seul le code de retour s'affiche. Le relevé, son compagnon et les deux fichiers de sortie sont poussés **sans être
  lus** (retenue : le relevé porte des bits sur les scores de `test`). Relevés attendus :
  `releve-mecanique-pilote4-gemini-v6-2-v1-tentative2-v2.txt` et `releve-mecanique-pilote4-gemini-v6-2-s-v1-v2.txt`.
- Code 3 : le fichier d'erreur ne porte qu'un nom de champ, que conv-audit peut lire sans lever la retenue.
- Sur `$PILOTE` plutôt que sur la copie poussée : même commande, tant que le dossier porte le même nom.
- Pour mémoire, l'identité attendue que l'assemblage comparera (le script ne la compare pas) : commit du segment 1 de M
  `d1af7a21d614d03d0e3c1eb5a63578f8a611840c`, de S `067b41da1af79384b29770b3824af2cf01c15b59`.

## 5. Interface avec la garde G1

- **`sources.liste_fermee`** est l'empreinte sha256 du fichier `EMPREINTES-pilote-v1.txt` **lui-même**, jamais celle de
  son compagnon. Le script la calcule sur les octets qu'il vient de vérifier contre le compagnon. Contrôlé sur chaque cas
  sain (S1, S3 : égale à l'empreinte du fichier sur le disque).
- **Fichiers d'un dossier poussé hors de sa liste fermée, par construction** (vu sur les trois cas de la série v14,
  essai P6) : `EMPREINTES-pilote-v1.txt` et `EMPREINTES-pilote-v1.txt.sha256`, **et eux seuls**.
  - `A-POUSSER-v1.txt` et son compagnon sont **dans** la liste fermée (le lanceur écrit la liste après eux).
  - Les fichiers sur le disque sont exactement ceux de `A-POUSSER-v1.txt` : 66 pour M et S, 80 pour le cas en segments
    (dont les pièces des essais `segment-2-t1/`, `-t2/`, `-t8/` et `-t9/`).
  - Le cas en segments porte en plus cinq dossiers vides (`segment-2-t3/` à `segment-2-t7/`, essais refusés sans
    pièce) : ce sont des dossiers, non des fichiers, et git ne les pousse pas.
  - Hors du dossier de course, à côté de lui, le lanceur laisse `.partis/`, `.verrou-…` et ses `sortie.txt` et
    `erreur.txt`, qui ne sont pas dans le dossier de course.
  - Le relevé s'écrit toujours hors du dossier de course (code 2 sinon).

## 6. Réponses aux questions du § 8 de la spécification

**Champs de l'extrait mécanique** (`extrait-mecanique-v1.json`, `extrait_version = 2`, même structure dans les sept jeux
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

**Lignée dans l'extrait** (question du § 8 de la v3) : oui, sous le champ `generations[].lignee` (une valeur par unité,
hors liste noire), que la table nomme (`extrait.lignee_champ`) ; dans les sept jeux, il porte la lignée attendue
(`gemini-organisme-v6-2`, `gemini-organisme-v6-2-s`) et `identite.lignee_source = extrait`. Elle n'est
`deduite_de_la_cle_controle_non_independant` que si ce champ manque (artefact 18c) ou si l'extrait manque (artefact 5).

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
comptes du cas continu (c001 7, g000 123, g001 129, g002 123, g003 124), sans double compte ; essais A22a et A22b.

**Unité qui sert la question** : `g001` (`manifeste.question_ouverte.cibles = ["g001"]` dans les sept jeux ; ligne
« - réponse à la question : » du lanceur). Le relevé ne le lit que sur cette ligne, reconnue par son seul début.

**Lignes des champs exigés, écrites en simulation** (essai P5, motifs exacts de la table) : dans les six cas sains et le
jeu v5.3, la section du segment 1 porte une ligne et une seule de chacun des motifs « - course », « - dépôt » (forme du
segment 1), « - lanceur », « - préenregistrement », « - organisme », « - registre » et « - code ». La ligne
« - préenregistrement » (bloc conditionnel du lanceur, v10 l. 512, v11 l. 529) est donc bien écrite en simulation ; dans
les deux cas en segments, elle manque aux essais 3 à 5 du segment 2, refusés (état de reprise non conforme) avant de
l'atteindre, sans effet sur l'identité. Les valeurs simulées passent les règles du § 4.2 :
- une seule clé sur les quatre lignes, dans toutes les sections ;
- clé `v6-2` (cinq cas) ou `v6-2-s` (cas S), présente dans la table close ;
- dernier élément du chemin du pilote égal au nom de la table (`pilote4-gemini-v6-2-v1`, `pilote4-gemini-v6-2-s-v1`) ;
- le jeu v5.3 porte la clé `v5-3`, hors de la table close : artefact 17.

**Empreintes de question des cas sains** (essai P4) : les jeux v13 (dont la v5.3) et les cas v14 de forme M
(`cas-sain-v6-2`, `cas-seg-segment1`) portent l'empreinte de M (`8b1c7511…`) ; le cas v14 S porte celle de S
(`a54da93e…`).

## 7. Champs qui porteront `absent` en pratique, et fiches qui en deviennent non observables

| champ | pourquoi | fiche (spécification v3, § 9) |
|---|---|---|
| `memoire.<g>.taille`, `memoire.<g>.restauration` | non consignés hors de l'archive | HC-P4-05 : indécidable (non observable) |
| `castes.<g>.mitose` | non consigné | HC-P4-06 : en partie (nombre de castes et rôles des appels observables) |
| `mutation.<u>.successeur_a_tourne` | l'extrait ne relie pas un successeur à l'organisme de l'unité suivante | HC-P4-03 et fait rapporté de HC-P4-04 : en partie |
| `fichier.<u>.politique_endogene` | tailles seulement, aucune empreinte | HC-P4-03, HC-P4-04 : en partie |
| `unite.<u>.telechargements.<source>` | jamais émis : téléchargements indexés par statut, sans source | HC-P4-09 : en partie (recherches par source observables ; `course.telechargements_total` observable) |
| `fin.recherche_cles_faite` | aucune source du dossier de course | fin de course : information manquante, sans effet sur la garde G1 |
| `unite.<u>.question_servie` hors de `g001` | par construction | § 0.9 du registre : sans effet |
| `unite.g001.question_servie` | `absent` si « aucune pièce archivée » ou sans la ligne | § 0.9 du registre : non observable dans ce cas |
| `sources.manifeste` | aucun fichier de manifeste poussé | aucune |
| `mutation.<u>.refus.<motif>` | observable seulement si les motifs sont des identifiants simples (aucun en simulation) | HC-P4-03 : à confirmer sur la course réelle |
| `mutation.<u>.successeur_valide` | lu comme « successeur vrai et `problemes_successeur` vide » : lecture à confirmer par conv-audit | HC-P4-03 |

La demande d'instrumentation de la ronde est la liste des lignes de ce tableau. À l'inverse, **HC-P4-01 est décidable**
pour M et S : la déclaration de fin de conception (ronde, critère, exemplaires) est consignée hors de l'archive, dans
l'extrait. HC-P4-07 (durées, coûts, statuts, événements, totaux) et HC-P4-08 (appels par statut) sont observables.

## 8. Point de la spécification v3 → traitement

| point | traitement |
|---|---|
| § 1 nom, compagnon, création exclusive | `releve-mecanique-<dossier>-v2.txt` dans un dossier de sortie à part ; lien en dur d'un fichier temporaire (jamais de relevé partiel) ; refus si le nom existe (A08) |
| § 1 ne porte jamais de score ni de texte | liste blanche de 26 champs de l'extrait et 3 du journal ; liste noire sur chaque composant du chemin ; grammaire fermée vérifiée avant l'écriture (A01, A02, A21, A35) |
| § 1 retenue | commandes du § 4 : relevé poussé sans être lu ; aucune valeur sur les sorties |
| § 2.1 liste fermée | compagnon, puis chaque ligne (mal formée, nom absolu ou remontant, doublon, liste vide, fichier absent ou altéré, lien) ; balayage de l'arbre (A06a à A06l, A10a à A10c) |
| § 2.2 extrait | JSON strict, décimaux exacts, `extrait_version = 2` exigé (A28, A31, A32) |
| § 2.3 journaux | `journal-appels-<unité>.jsonl`, rôle et statut en identifiants stricts, dédoublonnage (A22a, A22b) |
| § 2.4 lignes du LANCEMENT.md | motifs exacts de la table ; égalité d'un segment à l'autre (A13a à A13c) ; clé sur quatre lignes (A15a à A15e) ; porte (A14) ; réponse par son seul début (A19a à A19c) ; rien de M dans S (S5) |
| § 2.5 manifeste | lu dans l'extrait (`manifeste`), `sources.manifeste = absent` |
| § 2 n'ouvre jamais | les fichiers hors liste blanche ne sont jamais ouverts pour être lus, seulement hachés par la vérification de la liste fermée ; trace des ouvertures (A04a à A04c) ; ni le nom du fichier de réponse ni son préfixe dans le script ou la table (A04d) |
| § 3 grammaire | formes de la table, vérifiées sur chaque ligne ; décimal sans unité refusé (A03a, A03b) ; décimal sur un entier refusé (A03c) ; jamais d'arrondi (A03d) ; forme « graine » ajoutée (§ 9) |
| § 3 normalisation | identifiants stricts (minuscules, accents ôtés ; espace, point ou plus de 48 caractères : refus) ; vocabulaire fermé pour `fin.lignee` (§ 9) |
| § 4.1, § 4.2 champs exigés | un manquant fait refuser avec son nom (A11, A20a à A20c) ; empreinte inconnue : `identite.question` (A12) |
| § 4.2 table close, `releve.course` | clé sur les quatre lignes (A15a à A15e), nom tiré du chemin (A16a, A16b), clé hors table (A17a : jeu v5.3 ; A17b) |
| § 4.2 `identite.lignee`, `identite.lignee_source` | champ `generations[].lignee` (A18a à A18c), cohérence des autres mentions (A18d, A18e), déduite sans extrait (A05a) |
| § 4.3 segments et fin | issues lues dans le LANCEMENT.md (`stop_repris`, `stop_clos`, `stop_reprise_attendue`, `clore`, `reprise_refusee`, `refus_lanceur`, `fermeture`, `echec`, `aucune_course_partie`) ; `fin.reprise_attendue = oui` sauf fermeture ou clôture (A07, garde G1 figurée) |
| § 4.4 unités | statut, durée, coût de l'extrait ; appels du journal ; recherches par source ; `question_servie` à `oui` ou `absent` (A19) |
| § 4.5 conception | rondes tournées (journaux c… non vides) ; déclaration de l'événement `fin_conception` (plus d'une : refus) |
| § 4.6 mutation | appels du rôle `architecte_mutation_endogene` ; successeur produit et valide ; refus du noyau (A23a, A23b) |
| § 4.7 mémoire, castes | castes recrutées ; le reste `absent` (§ 7) |
| § 4.8 événements, totaux | délais dépassés, statuts « plafond », arrêts sur STOP ; coût de la course recopié ; durée, recherches et téléchargements sommés exactement (A05c, A23a) |
| § 5 liste blanche, noire, comptage | `sources.champs_ignores` = feuilles JSON hors liste blanche ou noires (A02, A21, A35) |
| § 6 essais | journal : 317 essais, 317 réussis, trois interpréteurs (§ 10) |
| § 7 exécution | codes 0, 2, 3, 4 (A25 à A27) ; une ligne de sortie standard, sans `[0-9][.,][0-9]` (chaque exécution) |
| § 8 | § 6 ci-dessus |
| § 9 | § 7 ci-dessus |

## 9. Écarts déclarés et réserves

1. **Forme « graine »** (`[0-9]{1,40}`) pour `identite.graine` et `identite.graine_manifeste` : la forme « entier » de
   la spécification (12 chiffres au plus) ne peut pas porter une graine de 19 ou 20 chiffres (graine S simulée :
   20 chiffres), et la v3 exige `identite.graine`. La grammaire de l'assemblage doit admettre cette forme.
2. **Normalisation du § 3** (contradiction entre « espaces remplacés par `_`, tronqués » et « avec un espace : refus ») :
   identifiants stricts, sans remplacement d'espace ni troncature (refus), sauf `fin.lignee`, lu dans un vocabulaire
   fermé de trois codes du noyau (`générations maximales`, `sans successeur valide`, `aucune lignée active`), toute
   autre valeur faisant refuser. Risque sur une course réelle : un code de fin inconnu, un statut ou un rôle avec un
   espace font refuser le relevé (code 3, nom du champ) ; il faudrait alors une version nouvelle.
3. **`absent` admis par la règle générale du § 3** là où la liste du § 4 ne l'écrit pas, quand la source manque :
   `fin.liste_fermee_poussee` (sans `A-POUSSER-v1.txt`), `conception.rondes_tournees` et `evenements.plafond_refus`
   (sans journal), `evenements.delai_depasse` et `evenements.stop` (sans extrait).
4. **Lectures choisies** : `identite.lanceur` sans le suffixe `.sh` (forme « identifiant ») ; `unite.<u>.appels.total`
   compté dans le journal dédoublonné (non `n_appels` de l'extrait) ; `course.duree_totale` = somme exacte des durées
   d'exécution des unités (non l'heure de fin moins l'heure de début), `absent` si une unité n'en porte pas ;
   `fin.liste_fermee_poussee` = `A-POUSSER-v1.txt` nomme la liste fermée et son compagnon ; un seul champ source pour la
   lignée (`generations[].lignee`), les autres mentions servant au contrôle.
5. **Refus ajoutés**, tous pour éviter un repli silencieux : clé JSON en double, `NaN` ; `extrait_version` autre que 2 ;
   unité importée ; identifiant d'unité hors forme ; mention de lignée discordante ; deux déclarations de fin de
   conception ; doublon d'appel contradictoire ; refus du noyau sous une forme non simple ; nom de source inconnu
   (`extrait-mecanique*.json` autre que v1, `journal-appels*.jsonl` hors forme) ; source présente sur le disque mais
   hors de la liste fermée ; en-têtes de segment hors d'ordre ; durée à plus de 3 décimales, coût à plus de 4 (jamais
   arrondis) ; compagnon du script ou empreinte de la table non conformes.
6. **Artefact 4** : la réponse, comme tout fichier de la liste fermée hors liste blanche, n'est **jamais ouverte pour
   être lue : seulement hachée par la vérification de la liste fermée** (trace des ouvertures : la seule fonction qui
   l'ouvre est celle du hachage ; une réponse plantée hors de la liste fermée n'est jamais ouverte du tout).
7. **Risque sur les segments réels** : si le HEAD du dépôt a bougé entre deux segments, la ligne « - dépôt » des
   segments suivants porte un autre commit et le relevé est refusé (`identite.commit`), comme le veut la v3 ; à savoir
   avant de lancer le script sur une course en segments.
8. **Reconstitution v13** : les quatre jeux v13 sont remis en dossiers de course par le harnais (pièces fournies remises
   à leur nom réel d'après `A-POUSSER`, octets contrôlés contre `EMPREINTES-fournis-v1.txt`, compagnons et liste fermée
   fabriqués) ; ces dossiers n'ont ni archive, ni organisme, ni réponse. Les copies de travail des cas v14 lient en dur
   les fichiers hors liste blanche (aucune lecture) et ne les remplacent jamais en place ; les pièces fournies sont
   vérifiées intactes après les essais (X2).

## 10. Essais

`essais_releve_mecanique_pilote4_v2.py`, lancé par `python3 -I -B essais_releve_mecanique_pilote4_v2.py` depuis
`sortie/`, a écrit `journal-essais-releve-B-v2.log` : **317 essais, 317 réussis, 0 échec**, sous Python 3.11, 3.12 et
3.13 ; copies de travail effacées.

- **Préparation** :
  - pièces et compagnons conformes ; pièces fournies et spécification v3 vérifiées ;
  - reconstitution v13 ;
  - empreintes de question (P4) ;
  - lignes d'identité et clé de course en simulation (P5) ;
  - interface G1 (P6) ;
  - comptes du jeu v5.3 par les fonctions du script (P7).
- **Cas sains** :
  - v13 v6.2 en un, deux et trois segments : comptes égaux à `releve-serie-v13-v1.txt`, sans double compte ;
    `identite.question = m` ; `identite.porte_m_precedente = absent` ; `releve.course`, `identite.lignee` de la table ;
    `identite.lignee_source = extrait` ;
  - v14 M, S et segments, tels quels. Pour S : `identite.question = s`, `unite.g001.question_servie = oui`,
    `identite.porte_m_precedente = oui`, et aucune des 20 valeurs de M ni de la référence du second pilote n'est dans
    le relevé ;
  - deux exécutions identiques hors `releve.heure` ; mêmes relevés d'un interpréteur à l'autre.
- **Artefacts** : les dix-neuf de la v3 (A01 à A19, avec variantes ; A17a est le jeu v5.3), ceux du brief (A20, A21) et
  les gardes du script (A22 à A35).
- **Contre-essais de mutation**, hors journal (R4, résultat trop propre) : chaque mutant est une version du script avec
  une garde désactivée, passée sous Python 3.13.
  - Sur la v1, neuf mutants. Les sept qui affaiblissent réellement le script sont tous attrapés : dédoublonnage,
    liste noire, hachage des fichiers hors liste blanche, égalité d'un segment à l'autre, ligne de réponse, balayage de
    l'arbre, champs exigés. Les deux autres n'ôtaient qu'une garde doublée.
  - Sur la v2, trois mutants pour les gardes nouvelles, tous attrapés :
    - clé de la ligne « registre » ignorée : A15d ;
    - contrôle du champ de lignée supprimé : A18a et A18d ;
    - contrôle des autres mentions de lignée supprimé : A18e.
