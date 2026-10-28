# Brief — gardes de la boucle extérieure du pilote 4 et script d'assemblage — v1

De : conv-audit, le 2026-10-26 à 06:49:23 UTC (heure lue sur `date -u` dans la commande qui écrit cette ligne).
À : un sous-agent neuf de la lignée conv-audit. Tu n'as écrit ni le protocole, ni l'objet, ni les cartes.

## 1. Le but

La boucle extérieure du pilote 4 fait lire à des agents neufs, par course, un **dossier de lecture** assemblé par
conv-audit, puis peut proposer une correction de l'objet (la v6.2.1). Des **gardes** (scripts) protègent cette boucle :
pas de lecture pendant une course ni sous la retenue, aucun mélange des deux courses, aucune valeur de `test_final`
recopiée, une correction limitée à un facteur hors des zones interdites, rien de la lecture dans l'arbre d'un organisme.
Tu écris ces scripts et leurs essais (R5 : chacun sur un cas sain et sur au moins un artefact), sur des données
synthétiques et des pièces de simulation seulement.

## 2. Pièces

Dans `fournis/`, à vérifier contre `../EMPREINTES-fournis-v1.txt` (chemins relatifs à `fournis/`) :

- `protocole-boucle-exterieure-pilote4-v3.md` : **§ 3** (dossiers de lecture), **§ 5** (journal et entrées de lancement),
  **§ 6** (un facteur à la fois, liste d'accompagnement), **§ 11** (les gardes : cas sains et artefacts), **§ 14** (ce que
  le correcteur n'écrit jamais). Le reste pour le contexte.
- `LISEZMOI-brief-v5.md` : les décisions E1 à E8 de conv-audit qui corrigent ce protocole (une v4 du protocole est en
  écriture) ; te concernent : E3 (ce qu'un fichier « holm-quatre » ne porte pas), E7 (d) (G6 cherche des mots entiers),
  E8 (G5 lit la carte au niveau des colonnes, par segments ; `VERSION`, `principal.py` l. 27, entre dans la liste
  d'accompagnement).
- `brief-agents-fin-de-course-v3.md` : la forme des pièces que rendent les agents (verdicts, parties A et B, périmètre,
  correction).
- `specification-releve-mecanique-B-v2.md` : le relevé (B), dont G1 lit des champs.
- `LISEZMOI-brief-script-v3.md` : noms et contenus des fichiers de lecture du script v3 (G8 bis, G12). Correction depuis :
  les libellés d'un test (iii) sont « changement au-delà du bruit des tâches » ou « dans le bruit des tâches », la
  correction de multiplicité dans un champ à part.
- `carte-v1/` : la carte des facteurs et les zones interdites v1 (Markdown et JSON, LISEZMOI), que G5 lit ; une
  contre-lecture est en cours, G5 doit lire n'importe quelle version de même forme.
- `objet-v6-2-1/organisme/` : le code de l'objet (26 fichiers), base des essais de G4 et G5.
- `serie-v14/cas-sain-v6-2-s/` : une course simulée saine (lanceur v11), avec sa liste fermée, base des essais de G1.

L'empreinte d'arbre d'un dossier est celle du noyau (`essaim_m3/noyau/boucle.py`), à reproduire à l'identique :

```python
def empreinte_arbre(dossier: pathlib.Path) -> str:
    h = hashlib.sha256()
    for f in sorted(p for p in pathlib.Path(dossier).rglob("*")
                    if p.is_file() and p.suffix != ".pyc" and "__pycache__" not in p.relative_to(dossier).parts):
        h.update(str(f.relative_to(dossier)).encode("utf-8") + b"\0")
        h.update(hashlib.sha256(f.read_bytes()).hexdigest().encode("ascii") + b"\n")
    return h.hexdigest()
```

Sur `fournis/objet-v6-2-1/organisme`, elle doit rendre `4f13647a7070b3941b660d60c428620df6b4e0e31cea1d2c63d71b8606e6214d`.

## 3. À écrire, sous `sortie/`

1. `assembler_dossier_lecture_v1.py` : deux modes, `course` et `finale` (protocole, § 3). Il copie des fichiers nommés
   (chemins en arguments) dans un dossier neuf, vérifie leurs compagnons, sans jamais ouvrir le contenu d'un fichier de
   lecture `test_final` ; écrit `MANIFESTE-DOSSIER-v1.txt` (ou `-FINAL-v1`) avec sa ligne de commentaire de version ;
   recopie `objet/` et écrit `objet-EMPREINTE-ARBRE.txt` à côté ; applique **G1**, **G2** (forme du fichier d'ouverture ;
   la référence elle-même est contrôlée par conv-audit), **G8 bis (b)** et **G12**, et refuse (code non nul, motif sur la
   sortie d'erreur, rien de laissé à moitié écrit) au premier échec.
2. `garde_g4_arbre_organisme_v1.py`, `garde_g5_perimetre_v1.py`, `garde_g6_courses_v1.py`,
   `garde_g8_valeurs_v1.py`, `garde_g9_entree_lancement_v1.py` : chacune telle que le § 11 la décrit, avec ses
   artefacts (G5 : les six, (a) à (f), au niveau des colonnes, dont les lignes partagées l. 997, 2103 et 2104 et les
   segments interdits l. 1009, 1011, 1039 de la carte ; G8 : une liste de valeurs donnée en argument, marqueurs d'un
   dossier d'audit ou valeurs finales à la fin du compteur, jamais lues dans un fichier `test_final` réel avant la fin
   du compteur).
3. `essais_gardes_v1.py` et `journal-essais-gardes-v1.log` (heures lues sur `date -u`) : chaque garde sur son cas sain et
   ses artefacts ; tout essai consigné ; aucun repli silencieux.
4. `LISEZMOI-gardes-v1.md` : les commandes exactes ; qui exécute quoi (protocole, fin du § 11) ; ce que chaque garde ne
   couvre pas ; une table « garde du § 11 → script → essais ».
5. Le compagnon `.sha256` de chacun (« empreinte, deux espaces, nom nu »).

Bibliothèque standard seule ; `python3 -I` ; sous Python 3.11, 3.12 et 3.13 présents sur la machine.

Hors de ta tâche : G3, G7 et G10 (essais d'agents, à part), G8 bis (a) (essai du script de lecture), G11 (essais du
relevé).

## 4. Ce que tu n'écris jamais

Aucun critère ni aucune stratégie de classement des tâches ; aucun contenu interdit du § 14 dans une pièce durable. Pour
l'artefact (e) de G5 (contenu interdit), choisis un contenu de forme interdite mais sans valeur (par exemple une liste de
mots inventés), gardé dans `travail/`, effacé à la fin, jamais recopié dans `sortie/` ni dans le journal (le journal dit
seulement « contenu interdit planté : refusé »). Aucun texte d'appel ni aucune consigne de l'objet recopiés. Aucun score,
aucun fait de course.

## 5. Interdits

Rien hors de ce dossier ; aucun `git`, réseau, sous-agent ni clé ; n'exécute pas le code de l'objet. Dans
`serie-v14/`, tu n'ouvres que `LANCEMENT.md`, `EMPREINTES-pilote-v1.txt`, `A-POUSSER-v1.txt` et leurs compagnons ; tu
hashes les autres fichiers sans les ouvrir ; jamais `reponse-question*`, `question.md`, `organisme/`, ni l'intérieur de
`ferme.tar.gz`. Écrire seulement sous `/var/tmp/gardes-boucle-pilote4-v1/` (`sortie/`, et `travail/` vidé à la fin).
Heures lues sur `date -u` dans la commande qui les écrit.

## 6. Fin

Réponse finale en quelques lignes : ce qui est fait, ce qui reste, écarts déclarés, empreintes des pièces.
