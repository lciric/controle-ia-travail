# Contre-lecture des outils de la fusion (étape 3) — v1

- **Nature** : contre-lecture de pièce d'instrument (classe B), par un lecteur neuf (Claude Sonnet 5.5), le 22 novembre 2026. Rien n'a été modifié ; essais faits dans des dépôts git jetables sous `/tmp/cl/` (hors dépôt).
- **Lu** : la spécification (§ 1 à 5), `verifier_citations_v6.py`, `recherche_autorisee_v2.py`, les cinq fichiers à contre-lire, trois lignes du journal et le § 3 du mandat v2. Rien d'autre. Les 71 essais fournis passent (`71 passed`).
- **Non vérifié** : le schéma réel des manifestes de `runs/` (interdit de lecture) ; le contenu de `docs/notes/bras-a-moniteurs-v1/reponses-sans-interne-demandes-18-19-24a-v1.md` (idem).

## Verdict : conforme sous corrections

Un défaut bloquant (fuite par préfixe voisin, fermée en une ligne), onze à corriger, huit remarques. Le coeur voulu par la spécification tient : `registres/veille-de-cap/` hors `commune/` est refusé à la bibliothécaire (casse, `./`, `//`, `..`, barre oblique inverse, espaces, `.sha256`) ; `prereg/`, `runs/`, `diag/` ne s'ouvrent pas pour la boucle (« noms seuls » vérifié en ligne de commande) ; fiche née mère, source hors liste, extrait faux, fiche marquée, commit introuvable, ordre « essai avant naissance », seconde naissance mère : tous donnent « mère ». Les défauts ci-dessous sont les écarts constatés.

## Bloquant

### B1 — `registres/veille*` reste ouvert par préfixe : les dossiers et fichiers voisins de `veille-de-cap/` sont lisibles par la bibliothécaire
- `listes_lecture_v1.py` l. 65 et 76 ; origine : `verifier_citations_v6.py` l. 92, `AUTORISES_PREFIXES` contient `"registres/veille"`, appliqué par `c.startswith(p)`.
- La v4 ne ferme que `registres/veille-de-cap/` (avec la barre finale). La spécification (§ 1.1) dit : « `registres/veille.md` reste autorisé ; `registres/veille-de-cap/` est exclu ». Le code autorise tout le reste de `registres/veille*`.
- Scénario (sortie réelle, `autorise_stricte`) : `registres/veille-de-cap-v1/journal.jsonl` → `True` ; `registres/veille-de-cap.jsonl` → `True` ; `registres/veille-de-capx/a` → `True` ; `registres/veille/x` → `True` ; `registres/veilleur/x` → `True`. Par l'outil : dépôt jetable avec `registres/veille-de-cap-v1/j.jsonl`, `python recherche_bornee_v3.py chercher 'fuite' --bras memo …` rend `registres/veille-de-cap-v1/j.jsonl:1: fuite` et `lire` l'ouvre (journalisé). Le même fichier est refusé au bras boucle (« hors périmètre ») : la bibliothécaire lit ce que la boucle ne lit pas.
- Même effet sur la partition : une source `registres/veille-de-cap-v1/…` serait jugée « autorisée » et la ligne passerait « commune ».
- Correction : ne pas hériter du préfixe. Dans `autorise_stricte`, avant `vc6.chemin_autorise`, refuser tout chemin dont le premier segment sous `registres/` commence par `veille` sauf l'égalité exacte à `registres/veille.md` (et son `.sha256`), ou retirer `"registres/veille"` de la liste et ajouter les deux chemins exacts. Ajouter les cinq chemins ci-dessus aux essais « artefacts » (aujourd'hui seul `registres/veille-de-cap/…` y est).

## À corriger

### C1 — Une source qui est un dossier : l'extrait « retrouvé » dans une liste de noms, exclus compris
- `partition_journal_v1.py` l. 64 (`lire_au_commit`) ; la v6 avait la garde (12) `git cat-file -t` = `blob` (`verifier_citations_v6.py` l. 177-179), absente ici.
- `git show SHA:docs/notes/memoire-conception-v1` rend la liste du dossier. Scénario : événement de naissance avec `source.chemin = "docs/notes/memoire-conception-v1"`, `extrait = "epreuve-banque-ne-pas-lire-bibliothecaire-v1"` → partition « commune » ; sortie : `"extrait": "epreuve-banque-ne-pas-lire-bibliothecaire-v1"`. Le nom exclu entre dans l'extrait commun ; ni `nom` ni `mots` ne le portent, donc la garde du champ libre ne le voit pas.
- Correction : exiger `cat-file -t` = `blob` (et mode 100644/100755, pas 120000 lien ni 160000 sous-module) avant de lire ; essai artefact ; passer aussi l'extrait (et `repere`) au contrôle des noms exclus.

### C2 — La garde « nom exclu dans `nom` ou `mots` » se contourne par le type de `mots`
- `partition_journal_v1.py` l. 75-78.
- `" ".join(str(m) for m in (ev.get("mots") or []))` : si `mots` est une chaîne, on itère sur ses lettres (« c o n s i g n e - … » ne contient plus le mot) ; si c'est un dictionnaire, on n'itère que les clés. Scénario : `mots="consigne-privee x"` → commune ; `mots={"a":"consigne-privee"}` → commune ; `nom={"x":"consigne-privee"}` est, lui, refusé (str du dict). Sortie des essais : lignes « commune ».
- Correction : `mots` doit être une liste de chaînes (sinon « mère », comme pour une ligne illisible), `nom` une chaîne ; vérifier `json.dumps(valeur)` plutôt que `str`.

### C3 — La garde des noms exclus est plus étroite que le § 2.1 de la spécification
- `partition_journal_v1.py` l. 35 (`MOTS_INTERDITS` = mots de la v3 + `ne-pas-lire` + `transcription`).
- La spécification (§ 3, « Garde du champ libre ») : « refuse toute ligne dont `nom` ou `mots` contient un nom exclu (§ 2.1) ». Le § 2.1 compte aussi les dossiers (`quarantaine`, `matiere-premiere`, `archives-reponses-modeles`), les branches (`lot/compte-4-v1`, `matiere-premiere/`, `prep/quarantaine-`, `sauvegarde/`), les motifs de notes de résultats, la demande/réponse 24. Scénarios, tous « commune » : `nom="voir quarantaine/x"`, `nom="matiere-premiere/modes"`, `nom="archives-reponses-modeles"`, `nom="lot/compte-4-v1 sauvegarde/x"`, `nom="epreuve banque ne pas lire"`.
- Correction : ajouter dossiers et préfixes de branches (ceux de `vc6.EXCLUS_DOSSIERS`, `EXCLUS_SOUS_CHAINES`, branches du § 2.1) ; ou déclarer l'écart. Rappel : « rendu » et « scores » refuseront aussi des mots français courants (sûr, mais à savoir).

### C4 — Une ligne mal formée fait planter tout le programme (déni de service) ; aucune garde par événement
- `partition_journal_v1.py` l. 41-46 et 59-62.
- Scénario : `source.commit = ["a"]` → `TypeError: unhashable type: 'list'` (cache par commit) ; aucun extrait n'est écrit. Idem tout champ de type inattendu non anticipé. Fermé en sûreté (rien ne fuit) mais une seule ligne bloque tout l'extrait.
- Correction : enrouler le jugement d'un événement dans `try/except Exception` → « mère », motif « ligne non jugeable », compté.

### C5 — Valeurs non fermées : seuls les noms de champs sont fermés ; chemin brut, `sert`, `repere`, `etat`, etc. sortent tels quels
- `partition_journal_v1.py` l. 81-87 (`reduire`).
- La spécification ferme la liste des champs ; les valeurs de `repere`, `sert`, `issue`, `reveil`, `etat`, `evenement`, `quand` ne sont ni typées ni bornées, et `source.chemin` est recopié **brut** alors que c'est la forme normalisée qui a été jugée. Scénarios (sortie réelle) : `source.chemin = "registres/ceci est un secret/../decisions.md"` → commune, recopié tel quel (normpath le ramène à `registres/decisions.md`, donc jugé autorisé) ; `sert = {"origine": "2026", "autre": "z"}` → recopié, dictionnaire imbriqué ; `repere = "consigne-privee: seuil"` → recopié. Un cycle à lecture large peut y glisser ce qu'il veut (la spécification s'en remet à la relecture de la mère pour `nom` et `mots`, mais pas pour ces champs).
- Correction : écrire `chemin` normalisé ; exiger que `etat`, `evenement` appartiennent aux listes fermées du mandat v2 § 3, `quand`/`reveil` à un motif de date, `issue` aux quatre issues, `sert`, `repere` des chaînes courtes (longueur bornée) ; sinon « mère » ; appliquer la garde des noms exclus à `repere`, `sert`, `extrait`.

### C6 — Fiche marquée « mère » : comparaison sans normalisation
- `partition_journal_v1.py` l. 114 et 145 (`l.strip()` côté marques, rien côté fiche).
- Scénarios : fiche `"F1 "` ou `"f1"` avec marque `F1` → reste « commune » (essais : `commune: [('F1 ', 'naissance')]`, `[('f1', 'naissance')]`). Une marque est un moyen de retrait que la mère veut sûr.
- Correction : comparer sur `fiche.strip().lower()` (et refuser comme « mère » toute fiche qui ne suit pas `[A-Z]-\d{4}`).

### C7 — Le commit cité peut être sur une branche exclue
- `partition_journal_v1.py` l. 59-62 (`resoudre`) ; `recherche_bornee_v3.py` (`--commit`).
- Le § 2.1 exclut les branches `lot/compte-4-v1`, `matiere-premiere/*`, `prep/quarantaine-*`, `sauvegarde/*`. Le code accepte tout commit résolu ; un chemin autorisé à un commit d'une branche exclue peut porter un contenu que `main` n'a pas, et l'extrait y serait « retrouvé ».
- Correction : exiger que le commit soit ancêtre de `main` (`git merge-base --is-ancestor`) ou d'une liste de références permises ; même garde dans l'outil borné.

### C8 — `commune/` : tout fichier est lisible ; liens symboliques non refusés
- `listes_lecture_v1.py` l. 73-75 ; `recherche_bornee_v3.py` (aucun contrôle du mode git).
- Scénario : `registres/veille-de-cap/commune/notes-libres.md`, `commune/sous/x.md`, `journal-commun-x.jsonl.bak` → `True` ; un lien symbolique `commune/lien.md` → cible `../../docs/notes/veille-de-cap-v1/reg.md` est listé et lisible par le bras memo (il montre le texte de la cible, pas le fichier ; mais un agent qui suivrait le lien sur le disque, hors outil, ouvrirait la partition mère). La spécification parle d'extraits `journal-commun-AAAA-MM-JJTHHMMZ.jsonl` écrits par programme.
- Correction : n'autoriser sous `commune/` que `journal-commun-\d{8}T\d{4}Z\.jsonl(\.sha256)?` (motif plat, sans sous-dossier) ; dans l'outil, ne lire que les blobs de mode 100644/100755.

### C9 — Noms accentués : fichiers illisibles et invisibles (échec fermé, mais fonctionnel)
- `recherche_bornee_v3.py` ≈ l. 36 (`ls-tree -r --name-only` sans `-z`).
- Avec `core.quotepath` par défaut, git imprime `"docs/notes/memoire-conception-v1/caf\303\251.md"` (entre guillemets, octal). Scénario : `lire "docs/notes/memoire-conception-v1/café.md"` → `REFUS : hors périmètre, ou absent au commit` pour les bras memo et boucle ; `lister` ne montre rien. Aucun fichier du dépôt n'a aujourd'hui de nom accentué, mais les règles « accents retirés » le prévoient. Les noms exclus accentués restent refusés (le guillemet initial fait échouer tout préfixe) : pas de fuite.
- Correction : `ls-tree -r -z --name-only` et séparation sur `\0`.

### C10 — Manifestes de fin : champs plus larges que la spécification, valeurs non typées, liens suivis
- `manifestes_fin_v1.py` l. 22 (`CHAMPS`), 27-34 (`lire`), 41 (`isdir`).
- La spécification (§ 2.3) : dates de départ et de fin, code de sortie, présence des produits. Le code sort aussi `run_id`, `decisif`, `depot_propre`, `commit`, `id`. Et `SCALAIRES` accepte n'importe quelle chaîne : scénario, `manifeste.json` avec `"decisif": "SECRET SEUIL 0.37 config"` et `manifeste-lanceur-fin.json` avec `"code": "résultat: perdu 0.2"` → recopiés dans la sortie. Un lien symbolique `manifeste.json` → autre fichier JSON est lu (sortie : `run_id: r1` d'un fichier hors de la course) ; un dossier de course lien symbolique est parcouru.
- Correction : types par champ (dates : motif ISO ; `code` : entier ; `sortie_existe` : booléen ; sinon « non conforme ») ; retirer `decisif`, `depot_propre`, `commit` sauf accord (la mère a accordé « champs fermés », pas ceux-là) ; refuser `os.path.islink`. Je n'ai pas pu lire le schéma réel (interdit) : à confronter par la mère.

### C11 — Listes : écarts entre la spécification et les motifs de noms
- `listes_lecture_v1.py` l. 33-38 et 41-46.
- (a) D-1 est appliqué par quatre motifs de nom ; `versement-journal-22-novembre-v1/*` n'attrape pas un `-v2/` (essai : `…-v2/x` → autorisé). Des dérivés possibles ne sont pas visés par les motifs : `reecriture-v3/fiches-reecrites-lot-*`, `contre-lecture-google-v1/fiches-et-sources-echantillon-v1.md`, `etat-bibliothecaire-…`, `veille-bibliothecaire-v1.md`, `questions-fond-v1/` : à trancher par la mère (je ne les ai pas lus). `liste-exhaustive-hypotheses-exploration-v2.md` (sans « allumage ») est autorisé. Casse : `Liste-exhaustive…` autorisé (git est sensible à la casse ; remarque).
- (b) § 2.1 « la demande 24 et la réponse 24 » : le code ne couvre que `docs/notes/demandes-fable-api-2026-11-22-v1/*24*`. Autre fichier de `docs/notes/` à « 24a » dans le nom, plein pour la boucle : `docs/notes/bras-a-moniteurs-v1/reponses-sans-interne-demandes-18-19-24a-v1.md` (à vérifier par la mère ; je ne l'ai pas ouvert). « Toute pièce dont l'objet est la conception d'un mode de sabotage » n'est pas détectable par nom : à la charge de la mère.
- (c) `registres/canaux-sessions-*` : la spécification dit « la dernière version » ; le code fixe `v5` (oubli à la v6). Les passations de `registres/passations/` entrent toutes en plein (comme voulu).
- (d) § 2.2.5 (historique git) : aucun outil de journal git dans les cinq pièces. À rappeler dans la liste des étapes restantes.

## Remarques

1. Le bras est un argument en ligne de commande : une bibliothécaire peut écrire `--bras boucle` et lire la liste large. La réserve de la spécification (« rien n'empêche un agent de lire hors de l'outil ») le couvre en partie, mais ici c'est l'outil lui-même qui le permet ; le journal consigne le bras, donc la porte de l'étape 4 le verra après coup. Proposition : deux points d'entrée, ou un bras fixé par variable d'environnement posée par la mère.
2. `PARTITION_SORTIE_LIBRE` (l. 140) : contournement non déclaré de « la sortie doit être sous `commune/` » (sert aux essais). À déclarer dans la spécification ou à retirer.
3. Le nom du fichier de sortie n'est pas contraint (`journal-commun-AAAA-MM-JJTHHMMZ.jsonl`) ; la bibliothécaire lit « le dernier extrait » mais rien ne le désigne. La sortie et son compagnon ne sont pas atomiques (plantage entre les deux : extrait sans empreinte).
4. `comptes["motifs"]` n'inclut pas les lignes retirées après coup (fiche à seconde naissance mère) ; `commune` + `mere` = `lignes` reste juste, mais la somme des motifs ne l'est pas.
5. Extrait de 10 signes au plus petit, sans frontière de mot (la v6 exige 6 mots, 30 signes, frontières) : `« cision numero un dit que le prog »` est « retrouvé ». Le contrôle n'est qu'un contrôle d'authenticité, mais l'extrait recopié peut être un fragment trompeur.
6. Une fiche née commune dont un événement ultérieur est « mère » voit sa dernière ligne manquer : la bibliothécaire peut lire un état périmé (« en préparation » alors que la mère sait « abandonnée »). Pas une fuite ; à signaler dans l'en-tête de l'extrait.
7. Sous-module ou lien (mode 160000/120000) : `contenu()` rend `None` ou le texte de la cible ; `empreinte` plante sur `hashlib.sha256(None)` (`recherche_bornee_v3.py` ≈ l. 116). L'ordre des journaux en argument compte (une naissance lue après ses événements les perd ; échec fermé).
8. `docs/sources/` est « plein » pour la boucle, PDF compris : `lire` affichera des octets décodés ; la spécification dit « les PDF ne s'ouvrent pas ». Ajouter `.pdf` à « noms ». `chercher` journalise seulement les fichiers avec correspondance (comme la v2) : un fichier lu sans correspondance n'est pas consigné, sans effet sur la fuite.

## Essais manquants (à ajouter au fichier d'essais)
- Stricte : `registres/veille-de-cap-v1/…`, `registres/veille-de-cap.jsonl`, `registres/veille-de-capx/a`, `registres/veille/x`, `registres/veilleur/x` (B1) ; `commune/notes-libres.md`, `commune/sous/x.md` (C8) ; `…-v2/` du versement (C11a).
- Partition : source dossier (C1) ; `mots` chaîne et dictionnaire (C2) ; `nom` portant `quarantaine`, `matiere-premiere`, branche exclue (C3) ; commit non hachable (C4) ; chemin brut non normalisé, `sert` imbriqué (C5) ; fiche marquée avec espace ou casse (C6) ; commit d'une branche exclue (C7) ; lien symbolique dans `commune/` ; journal avec BOM (essai fait : ligne 1 « illisible », fermé) ; deux journaux dans l'ordre inverse.
- Outil borné : nom accentué (C9) ; `--bras boucle` demandé par un agent de réponse (remarque 1) ; sous-module.
- Manifestes : valeur chaîne dans un champ de date ou de code (C10), lien symbolique.

## Scripts de reproduction
Les sorties citées viennent de `/tmp/cl/p1.py` (règles de chemin), `/tmp/cl/p2.py` (partition, dépôt jetable `/tmp/cl/r`), de la ligne de commande de `recherche_bornee_v3.py` sur ce dépôt et de `manifestes_fin_v1.py` sur `/tmp/cl/m/runs/`. Schéma commun : un dépôt `git init` avec `registres/decisions.md` (« La decision numero un dit que le programme avance prudemment… »), un événement de naissance dont `source` pointe sur ce fichier et dont on change un champ à la fois.
