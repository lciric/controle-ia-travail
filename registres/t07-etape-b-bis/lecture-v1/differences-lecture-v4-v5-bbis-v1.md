# Différences entre la version 4 et la version 5 du module de lecture — apprentissage des sondes sur la tâche (étape B bis de T0.7) — v1

- **Auteur** : développeur du module de lecture (le même sous-agent que pour la version 4), session conductrice de la lecture `session_013QMayjNC5GKdDFTN87oAV5`, modèle Fable 5.2. Il n'a écrit ni le texte scellé, ni ses addenda, ni le complément ; il n'est ni contre-lecteur, ni lecteur-opérateur, ni juge.
- **Mandat** : `registres/t07-etape-b-bis/lecture-v1/mandat-developpeur-lecture-v4-bbis-v1.md` (`970aa7f2383fb220df5875b38c06d30c6ad0140b12b57160b909f00f4c10dfc0`), complété par `registres/t07-etape-b-bis/lecture-v1/complement-mandats-code-lecture-v5-bbis-v1.md` (`9d85d4d7959d1c5c6b839a2cd3f4e6af8a16a51bad329a97d120b8c68f0edb0a`) ; règles communes (`5f303a9c58005808f78a5674860cab7b785c876777287dbe22f998f67d7b7783`). Compagnons vérifiés.
- **Spécification** : complément scellé au quatrième addendum, `prereg/T0.7-etape-B-bis-v1-addendum-ecart-4-complement-v1.md` (`12c908732c329e61b57fe435e430464cb8033d0db708d4432076c62b4c9aa419`, compagnon vérifié), § 6 : septième différence (D7, suite d'un refus de pure mise en place), huitième différence (D8, refus sous variable d'environnement de git), nom du module — et rien d'autre.
- **Fichiers comparés** : `src/controle_ia/t07bbis/lecture_v4.py` (`9bfca6269e34bb2a2ccd9b35c43c2af7b69e67b8bee45eab223cbd0a1c85f7ca`, égale à l'empreinte du complément ; fichier non modifié) et `src/controle_ia/t07bbis/lecture_v5.py` (`dac9f8590784a2bf93d312128b09e89a7a21c04509700f3a3ee8c7a81a28064c`).
- **Comment la version 5 a été produite** : par programme, en appliquant à la version 4 les dix-huit couples « ancien, nouveau, une occurrence exigée » écrits dans `tests/test_lecture_bbis_v5_complement_addendum_4_v1.py` (`COUPLES`) ; l'essai `test_6_…` refait le fichier depuis la version 4 et exige l'égalité exacte. Aucun autre changement n'existe ; de la version 3 à la version 5, il n'y a donc que D1 à D6, D7, D8 et le nom du module.
- **Rien d'exécuté sur des fichiers réels** : le module, sa garde, ses fonctions et le programme de la preuve après coup n'ont été joués que sur des registres, des arbres et des dépôts git jouets, fabriqués dans le dossier temporaire des essais. Aucun fichier de résultat ouvert.

## Blocs changés : seize, chacun fondé

Sortie de `diff -u` ci-dessous : **seize blocs**. Aucun bloc sans fondement. (Dix-huit couples, seize blocs : deux paires de couples voisins tombent dans un même bloc de `diff`, blocs 8 et 10 ; un troisième, bloc 15, réunit le nom du module et D8.)

| bloc | lignes de la version 4 | ce qui change | fondement (§ 6 du complément) |
|---|---|---|---|
| 1 | 16-21 | un paragraphe ajouté au docstring d'en-tête : nomme le complément, son empreinte scellée, D7, D8, le nom du module ; aucune ligne retirée | **nom du module** (« le docstring d'en-tête nomme ce complément et son empreinte scellée ») |
| 2 | 521-526 | classe neuve `RefusMiseEnPlace(RefusLecture)` | **D7 (a)** |
| 3 | 534-539 | fonction neuve `exiger_environnement_git_propre()` : refus, sans nettoyage, noms seulement | **D8** |
| 4 | 605-611 | `lire_lignes` : registre absent → `RefusMiseEnPlace`, même message | **D7 (a)**, motif (M2) |
| 5 | 642-657 | `verifier_lignes` : fichier cité absent, compagnon absent relevés avant `sceau_conforme` → `RefusMiseEnPlace`, mêmes messages que la version 3 ; le refus rassemblé n'est de mise en place que si tous ses motifs le sont | **D7 (a)**, motif (M1) |
| 6 | 665-681 | `preuve_entree_conjointe` : la fabrique de refus reçoit la classe ; code de retour inattendu ou git introuvable → `RefusMiseEnPlace` | **D7 (a)**, motif (M3) |
| 7 | 683-690 | `preuve_entree_conjointe` : commit nommé absent → relevé `git rev-parse --is-shallow-repository` ; dépôt superficiel → `RefusMiseEnPlace`, sinon `RefusLecture` (fond) | **D7 (a)**, motif (M3) |
| 8 | 805-818 | (i) `exiger_ordre_propre` : le refus de la preuve est relevé dans sa classe (`type(e)` au lieu de `RefusLecture`) ; (ii) `_git` : code de retour non nul → `RefusMiseEnPlace`, même message | **D7 (a)** — (i) est la lecture retenue n° 1 ci-dessous ; (ii) motif (M3) |
| 9 | 820-825 | `anteriorite_etape_b` : relevé du dépôt superficiel en tête de la fonction → `RefusMiseEnPlace` | **D7 (a)**, motif (M3) |
| 10 | 1378-1387 | (i) fonction neuve `preuve_aucune_ouverture(racine, garde_entrees, passee) -> dict`, placée juste avant `lire` ; (ii) première instruction de `lire` : `if essai is None: exiger_environnement_git_propre()` | (i) **D7 (b)**, points (O1) à (O3) ; (ii) **D8** |
| 11 | 1396-1401 | `lire` : `garde, passee = None, False` avant le bloc de la garde | **D7 (b)** (ce que la preuve reçoit) |
| 12 | 1417-1422 | `lire` : immédiatement avant le premier appel de `GardeEntrees.exiger`, `passee = True` puis la ligne `BBIS LECTURE ENTREES OUVERTES` imprimée | **D7 (c)** |
| 13 | 1424-1430 | `lire`, branche du refus : `res["garde"]["nature"]` (« mise en place » ou « fond ») ; pour « mise en place », `res["garde"]["aucune_ouverture"]` | **D7 (b)** |
| 14 | 1569-1575 | `commande="python -m controle_ia.t07bbis.lecture_v5"` dans `ecrire_lecture` | **nom du module** |
| 15 | 1592-1602 | docstring de `main` : `lecture_v5` ; première instruction de `main` : la garde des variables de git, rendue `BBIS LECTURE ARRET : …`, code 2 | **nom du module** ; **D8** |
| 16 | 1615-1620 | `main`, après l'écriture du fichier de lecture : nature « mise en place » et preuve conforme → pièce `preuve-aucune-ouverture-bbis` scellée par `manifeste.ecrire_resultat`, aucune ligne au journal, ligne `BBIS LECTURE NON CONSOMMEE …`, code 3 ; sinon la suite de la version 3 | **D7 (d)** |

## Lectures retenues là où le complément ne fixe pas la lettre (à juger par le contre-lecteur du code)

### Module de lecture

1. **La nature du refus traverse la fonction d'ordre (bloc 8, i).** Le § 6 nomme les endroits où `RefusMiseEnPlace` est levée ; `exiger_ordre_propre` n'y figure pas. Or la version 4 y rattrape le refus de la preuve d'entrée conjointe et lève à sa place un `RefusLecture` (refus de la version 3 suivi du motif de la preuve) : sans rien changer, un commit nommé absent d'un dépôt superficiel serait rendu « de fond », contre le cas sain exigé (§ 6, essai 1). Lecture retenue : le refus relevé garde la classe du refus de la preuve (`raise type(e)(…)`), même texte. Le refus d'ordre qui précède dans le message (égalité à la seconde, couverte par l'exception de QA-1) n'est pas compté comme un second motif, de fond. **C'est la seule ligne changée hors des endroits que le § 6 nomme.**
2. **Git introuvable (bloc 6).** Une commande git qui ne peut pas être lancée (`OSError`) est tenue pour « git en échec », motif (M3), comme un code de retour inattendu.
3. **Relevé du dépôt superficiel (blocs 7 et 9).** Par `git rev-parse --is-shallow-repository`. Dans `anteriorite_etape_b`, il est fait en tête, avant tout `git log` : un dépôt superficiel refuse là même si le commit du scellement s'y trouve ; une sortie autre que « true » ou « false » est un refus de mise en place (« sortie inattendue »). Dans la preuve d'entrée conjointe, il n'est fait que si un commit nommé est absent.
4. **Tout code de retour non nul de `_git` (bloc 8, ii)** est un refus de mise en place : `_git` ne sert qu'à `anteriorite_etape_b`, qui n'attend aucun code 1.
5. **`verifier_lignes` (bloc 5).** Les deux motifs de mise en place gardent, mot pour mot, les messages que `sceau_conforme` leur donnait. La nature est jugée par appel : `lire` vérifie les lignes du registre propre, puis celles du registre partagé ; un refus de mise en place sur les premières arrête avant les secondes, comme dans la version 3, sans avoir vu un éventuel motif de fond des secondes (la garde rejouée entière à la relance le verra).
6. **`preuve_aucune_ouverture` (bloc 10, i).** (O3) compte toute ligne du journal qui contient `OUVERTURE-BBIS` (plus large que « dont la clé est ») ; un journal qui n'est ni un fichier ni absent, ou illisible, est non conforme ; la fonction ne lève rien. `passee` est le fait que la ligne du seuil a été imprimée.
7. **Ordre au seuil (bloc 12).** `passee = True` est posé avant l'impression, pour qu'un échec de l'impression ne laisse pas croire qu'aucune entrée n'allait être ouverte ; l'impression vide son tampon. La ligne est imprimée aussi en mode jouet.
8. **Issue de l'épreuve du signal planté autre que « vu ».** Ce n'est pas la branche du refus : `res` ne porte pas `garde`, donc aucune nature ; la suite est celle de la version 3 (ligne au journal, code 0). Un `RefusRegistre` rattrapé par le bloc de la garde est « de fond ».
9. **Pièce écrite par `main` (bloc 16).** Contenu : `motif`, `nature`, `aucune_ouverture` (les trois points et leurs relevés), `fichier_de_lecture`, `fichier_de_lecture_sha256`. Manifeste du run : `runs/<run>/manifeste.json`. L'écriture est dans le bloc `try` de `main` : une garde d'arrêt à ce moment rend le code 2.
10. **Garde des variables de git (blocs 3, 10 ii, 15).** Dans `main`, elle précède tout, importations et lecture de la ligne de commande comprises ; le refus y est rendu par un `try` propre (`BBIS LECTURE ARRET : …`, code 2). Dans `lire`, elle précède les importations et `exiger_processeur`. Le message liste les noms triés.
11. **Docstrings.** Celui de `main` ne change que par le nom du module (il ne décrit ni le code 3 ni les deux lignes neuves) ; celui de `lire` ne change pas : le § 6 ne déclare que le nom.

### Programme de la preuve après coup (`scripts/preuve_aucune_ouverture_apres_coup_bbis_v1.py`)

12. **Interface.** `--racine`, `--run-lecture`, `--run-bbis`, `--numero`, `--sortie-lancement CHEMIN EMPREINTE` (répétable). Codes : 0 pièce écrite et conforme ; 1 pièce écrite, non conforme ; 2 arrêt, rien d'écrit (variable `GIT_*`, argument mal formé, pièce existante). Ligne imprimée : `BBIS PREUVE APRES COUP ECRITE <chemin> <empreinte> conforme=… classement=…`. La pièce est écrite dans l'arbre donné, conforme ou non ; elle porte l'heure du relevé ; son compagnon est écrit par le programme (aucun module du dépôt importé).
13. **Commit des sorties.** Épinglé dans le code (`7322049dbbc10975ec1fa7dd54c10c8bc1ec4cf9`) ; aucune option ne le change. Les essais remplacent la constante du module chargé par le commit du dépôt jouet.
14. **Classement.** « lecture consommée » si une sortie gardée est absente, non scellée, d'une autre empreinte, porte la ligne du seuil, ou si aucune n'est donnée ; sinon « nœud » si un point (A1) à (A3) est non conforme ou non faisable ; sinon « relance permise sur preuve ». La lecture consommée prime sur le nœud.
15. **(A1).** « Aucun commit de l'histoire du journal n'en porte une » : pour chaque commit de `git log --all -- <journal>`, le journal de ce commit est lu et ne doit contenir aucun `OUVERTURE-BBIS`.
16. **(A2).** « Toutes les références » : la tête et la pointe de chaque référence (`git for-each-ref`), non chaque commit de leur histoire. Le disque est parcouru en entier, hors du dossier de git. **Fichiers tolérés** : le complément dit « ceux que citent, par chemin et empreinte, les lignes `PANNE-MISE-EN-PLACE-BBIS-<n>` déjà inscrites », alors que ces lignes citent la déclaration, qui cite les fichiers. Lecture retenue : le registre voisin est lu sur le disque de l'arbre ; un fichier est toléré si son chemin **et** son empreinte recalculée figurent dans le texte d'une ligne de panne ou dans la déclaration qu'elle cite, la déclaration étant à l'empreinte de sa ligne ; une ligne de panne mal formée, ou dont la déclaration est absente ou d'une autre empreinte, rend le point non conforme.
17. **(A3).** La ligne `SCORES-BBIS` est lue au registre propre sur le disque (une seule exigée, chemin `diag/<run de la course>/sondes-bbis.json`). Les noms du disque sont tous les fichiers des trois dossiers, suivis ou non ; un lien symbolique est non conforme. Octets comparés par empreinte, en flux, sans décodage.
18. **Histoire incomplète.** Dans un dépôt superficiel, les trois points sont « non faisables » (nœud).
19. **Sorties gardées.** Chemin relatif à l'arbre (ou absolu) ; la ligne du seuil est cherchée comme sous-chaîne.

## Points ouverts

1. **Dépôt superficiel dont un commit nommé est présent mais le parent coupé.** La preuve d'entrée conjointe y relève « 0 parent, un seul exigé » : selon la lettre du § 6 (« commit nommé absent d'un dépôt superficiel, code de retour inattendu »), ce refus reste **de fond**, donc consomme la lecture, alors que (M3) nomme le dépôt superficiel comme défaut de mise en place. Non ajouté ; à trancher. Geste qui l'évite : la commande de lecture vérifie l'histoire complète avant le lancement.
2. **(M2) et le fichier de la fiche de code.** Comme le dit le § 4, point 4, du complément, le registre absent et la fiche absente arrêtent `main` en code 2 avant toute issue : (M2) n'est éprouvé qu'au niveau de `lire_lignes`. Ces arrêts relèvent de la preuve après coup.
3. **`main` joué en mode jouet par un passeur.** Aucun paramètre de `main` ne fait passer `lire` en mode jouet. Les essais jouent le vrai `main` et remplacent le seul nom `lire` par un passeur qui appelle le vrai `lire` avec `essai=…`. La lecture réelle de `main` (constante de D2, tirages réels) n'est donc éprouvée que jusqu'à la garde des variables de git.
4. **Format des citations d'une ligne de panne** (lecture n° 16) : non fixé par le complément ; à fixer avec la forme de la déclaration.
5. **« Toutes les références »** (lecture n° 16) : pointes des références, non toute l'histoire.
6. **Les essais de la version 4 héritent de l'environnement** (ils ne le fixent pas, et ne sont pas modifiés, § 6, essai 6) ; ils passent sur cette machine avec ses variables `GIT_*`. Les essais neufs fixent le leur.
7. **Nom du fichier d'essais du programme de la preuve après coup** : `tests/test_preuve_aucune_ouverture_apres_coup_bbis_v1.py` (« nom sur le même modèle », hors du motif `test_t07bbis_*`).
8. **Rappel du complément, point ouvert 7** : la lecture de (A3) par le commit des sorties est un nœud de Lazar ; le programme est écrit et éprouvé sur jouets, la voie de l'arrêt avant le seuil n'est pas employée avant son mot.

## Sortie de `diff -u` (version 4 → version 5)

Commande : `diff -u --label lecture_v4.py --label lecture_v5.py src/controle_ia/t07bbis/lecture_v4.py src/controle_ia/t07bbis/lecture_v5.py`.

~~~diff
--- lecture_v4.py
+++ lecture_v5.py
@@ -16,6 +16,17 @@
 a servi est écrite sous `ordre_propre` (lecture réelle : la constante et elle seule) ; (D6) nom du module dans `ecrire_lecture` et
 dans le docstring de `main`. Les v1 à v3 restent (R12).
 
+v5 : la v4, modifiée par le **complément au quatrième addendum d'écart**
+(`prereg/T0.7-etape-B-bis-v1-addendum-ecart-4-complement-v1.md`, empreinte scellée
+`12c908732c329e61b57fe435e430464cb8033d0db708d4432076c62b4c9aa419`, § 6) et par lui seul : (D7) suite d'un refus de la garde né
+d'un pur défaut de mise en place — classe `RefusMiseEnPlace`, levée aux seuls endroits des motifs (M1) à (M3) ; nature du refus
+et preuve d'aucune ouverture (`preuve_aucune_ouverture`, points (O1) à (O3)) écrites par `lire` ; ligne
+`BBIS LECTURE ENTREES OUVERTES` imprimée juste avant la première ouverture d'une entrée ; dans `main`, pièce
+`preuve-aucune-ouverture-bbis` scellée, aucune ligne au journal des ouvertures, ligne `BBIS LECTURE NON CONSOMMEE`, code de
+sortie 3 ; (D8) `exiger_environnement_git_propre` : refus, sans nettoyage, si une variable d'environnement `GIT_*` est posée, en
+première instruction de `main` et de `lire` en lecture réelle ; nom du module dans `ecrire_lecture` et dans les docstrings. Les
+v1 à v4 restent (R12) ; la v4 n'est ni rattachée ni jouée pour la lecture.
+
 Sections : (1) états d'une cellule (table A), issue I0 à I6, suffixe du transfert T0 à T+, libellés du nœud 5 (« lecture dure »,
 retenu ; « lettre de R-2716 », information), qualifications (MU, SC), lignes de (i-a), réserves et audit de symétrie R4 —
 phrases gelées recopiées du texte, crochets remplis par le code ; (2) gardes : refus sur l'instance (variable `BBIS_INSTANCE`,
@@ -521,6 +532,12 @@
     """Refus de la garde d'ouverture : rien n'est lu (I0, motif écrit)."""
 
 
+class RefusMiseEnPlace(RefusLecture):
+    """Refus de la garde d'ouverture né d'un pur défaut de mise en place de l'arbre de lecture (complément au quatrième
+    addendum, motifs (M1) à (M3)) : fichier cité ou compagnon absent du disque, registre absent du disque, dépôt superficiel,
+    commit nommé absent d'un dépôt superficiel, code de retour inattendu d'une commande git. Rendu en I0 comme tout refus."""
+
+
 JAMAIS = ("lecture-sondes-t06.json", "resume.json", "scores-actions-t07.npz", "sondes-t07.json", "notation-t07.json",
           "planchers-figees-t07.npz", "sondes-neuves-t07.npz", "extraire_mesures_epreuve_t06_v1.py")
 MARQUES_JAMAIS = ("bras-attaque", "mode-tenu-a-l-ecart", "etiqueteur", "lecture-b-7a-quarantaine", "anteriorite-bras-informe",
@@ -534,6 +551,16 @@
                          "résumé de score n'est calculé sur l'instance")
 
 
+def exiger_environnement_git_propre() -> None:
+    """Complément au quatrième addendum, D8 : si l'environnement du processus porte une variable dont le nom commence par
+    `GIT_`, refus (jamais un nettoyage : aucune variable n'est retirée ni changée) ; le refus nomme ces variables par leur nom
+    seulement, jamais une valeur."""
+    posees = sorted(k for k in os.environ if k.startswith("GIT_"))
+    if posees:
+        raise GardeArret(f"variable(s) d'environnement de git posée(s) ({', '.join(posees)}) : refus ; la lecture de B bis ne "
+                         "lance aucune commande git sous une variable GIT_* (complément au quatrième addendum, D8)")
+
+
 class GardeEntrees:
     """Liste blanche des entrées (plan, point 1) ; tout chemin hors de la liste, ou de la liste « Jamais », est refusé ; chaque
     chemin ouvert est consigné."""
@@ -605,7 +632,7 @@
     from ..t07 import registre_v1 as rg
     registre = Path(registre)
     if not registre.is_file():
-        raise RefusLecture(f"registre {registre} absent")
+        raise RefusMiseEnPlace(f"registre {registre} absent")
     trouvees, fautes = {k: [] for k in cles}, []
     for l in registre.read_text(encoding="utf-8").splitlines():
         c = [x.strip() for x in l.strip().strip("|").split("|")]
@@ -642,16 +669,22 @@
 def verifier_lignes(racine: Path, lignes: dict, instant: int) -> None:
     """Antériorité stricte à l'ouverture et sceau du fichier cité (fichier et compagnon `.sha256`)."""
     from ..t07 import registre_v1 as rg
-    fautes = []
+    fautes, de_fond = [], False
     for k, x in lignes.items():
         try:
             if not x["instant"] < int(instant):
                 raise RefusLecture(f"ligne {k} datée {x['date']}, pas strictement antérieure à l'ouverture")
-            rg.sceau_conforme(Path(racine) / x["chemin"], x["sha256"])
+            cite = Path(racine) / x["chemin"]
+            if not cite.is_file():                                   # (M1) relevé avant `sceau_conforme` : fichier non extrait
+                raise RefusMiseEnPlace(f"{cite} absent")
+            if not Path(str(cite) + ".sha256").is_file():            # (M1) compagnon non extrait
+                raise RefusMiseEnPlace(f"{cite} : compagnon .sha256 absent")
+            rg.sceau_conforme(cite, x["sha256"])
         except GardeArret as e:
             fautes.append(str(e))
+            de_fond = de_fond or not isinstance(e, RefusMiseEnPlace)
     if fautes:
-        raise RefusLecture(" ; ".join(fautes))
+        raise (RefusLecture if de_fond else RefusMiseEnPlace)(" ; ".join(fautes))
 
 
 def preuve_entree_conjointe(racine: Path, exception: dict) -> dict:
@@ -665,17 +698,17 @@
     import re
     hexa = re.compile(r"[0-9a-f]{40}")
 
-    def refus(point: str, motif: str) -> RefusLecture:
-        return RefusLecture(f"preuve d'entrée conjointe, point ({point}) : {motif}")
+    def refus(point: str, motif: str, classe=RefusLecture) -> RefusLecture:
+        return classe(f"preuve d'entrée conjointe, point ({point}) : {motif}")
 
     def git(point: str, *args, codes=(0,)):
         try:
             r = subprocess.run(["git", "-C", str(racine), *args], capture_output=True)
         except OSError as e:
-            raise refus(point, f"git {' '.join(args[:2])} : échec de git ({e})") from None
+            raise refus(point, f"git {' '.join(args[:2])} : échec de git ({e})", RefusMiseEnPlace) from None
         if r.returncode not in codes:
             raise refus(point, f"git {' '.join(args[:2])} : échec de git (code {r.returncode} ; "
-                               f"{r.stderr.decode('utf-8', 'replace').strip()[:200]})")
+                               f"{r.stderr.decode('utf-8', 'replace').strip()[:200]})", RefusMiseEnPlace)
         return r
 
     def exiger_commit(point: str, c) -> None:
@@ -683,8 +716,10 @@
             raise refus(point, f"identifiant de commit {c!r} : 40 caractères hexadécimaux attendus")
         r = git(point, "cat-file", "-e", f"{c}^{{commit}}", codes=tuple(range(256)))
         if r.returncode != 0:
-            raise refus(point, f"commit {c[:12]} absent du dépôt ou illisible (code {r.returncode} ; "
-                               f"{r.stderr.decode('utf-8', 'replace').strip()[:200]})")
+            superficiel = git(point, "rev-parse", "--is-shallow-repository").stdout.decode("utf-8", "replace").strip() == "true"
+            raise refus(point, f"commit {c[:12]} absent du dépôt{' superficiel' if superficiel else ''} ou illisible (code "
+                               f"{r.returncode} ; {r.stderr.decode('utf-8', 'replace').strip()[:200]})",
+                        RefusMiseEnPlace if superficiel else RefusLecture)
 
     def seul_parent(point: str, c) -> str:
         exiger_commit(point, c)
@@ -805,14 +840,14 @@
             try:
                 preuve = preuve_entree_conjointe(racine, exception)
             except RefusLecture as e:
-                raise RefusLecture(f"{refus} ; preuve d'entrée conjointe du quatrième addendum refusée : {e}") from None
+                raise type(e)(f"{refus} ; preuve d'entrée conjointe du quatrième addendum refusée : {e}") from None
     return {"regle": "stricte"} if preuve is None else {"regle": "quatrième addendum", "preuve": preuve}
 
 
 def _git(racine: Path, *args) -> str:
     r = subprocess.run(["git", "-C", str(racine), *args], capture_output=True, text=True)
     if r.returncode != 0:
-        raise RefusLecture(f"git {' '.join(args[:2])} : échec ({r.stderr.strip()[:200]})")
+        raise RefusMiseEnPlace(f"git {' '.join(args[:2])} : échec ({r.stderr.strip()[:200]})")
     return r.stdout
 
 
@@ -820,6 +855,10 @@
     """Le premier commit (toutes les références locales) qui ajoute `lecture-t07.json` ou `arret-etape-b.json`, s'il existe, est
     postérieur (date de commit strictement plus grande) au commit qui ajoute la ligne `SCELLEMENT-BBIS` au registre propre ;
     sinon refus et nœud (liste d'arrêt, première ligne)."""
+    superficiel = _git(racine, "rev-parse", "--is-shallow-repository").strip()
+    if superficiel != "false":
+        raise RefusMiseEnPlace("dépôt superficiel : histoire git incomplète, antériorité de l'étape B non vérifiable"
+                               if superficiel == "true" else "git rev-parse --is-shallow-repository : sortie inattendue")
     ajout = _git(racine, "log", "--all", "--reverse", "--format=%H %ct", "-S", "| SCELLEMENT-BBIS |", "--",
                  registre_propre_rel).split()
     if len(ajout) < 2:
@@ -1378,10 +1417,40 @@
     return sortie
 
 
+def preuve_aucune_ouverture(racine: Path, garde_entrees, passee: bool) -> dict:
+    """Preuve d'aucune ouverture (complément au quatrième addendum) : (O1) la liste blanche des entrées n'a pas été construite
+    (`garde_entrees` absent) ou sa liste `lus` est vide ; (O2) la ligne `BBIS LECTURE ENTREES OUVERTES` n'a pas été imprimée
+    (`passee` faux) ; (O3) le journal des ouvertures est absent du disque, ou présent sans aucune ligne `OUVERTURE-BBIS` (nombre
+    de lignes et empreinte relevés). Rend `conforme` vrai ou faux avec les relevés ; ne lève rien pour un point en défaut."""
+    import hashlib
+    from .registre_bbis_v1 import REGISTRE_PROPRE
+    rel = REGISTRE_PROPRE + ".ouvertures.md"
+    journal = Path(racine) / rel
+    lus = None if garde_entrees is None else list(garde_entrees.lus)
+    o1 = {"conforme": not lus, "liste_blanche_construite": garde_entrees is not None, "entrees_ouvertes": len(lus or [])}
+    o2 = {"conforme": not passee, "ligne_du_seuil_imprimee": bool(passee)}
+    if journal.is_file():
+        try:
+            octets = journal.read_bytes()
+            lignes = octets.decode("utf-8", "replace").splitlines()
+            n = sum("OUVERTURE-BBIS" in l for l in lignes)
+            o3 = {"conforme": n == 0, "journal": rel, "etat": "présent", "lignes": len(lignes), "lignes_ouverture": n,
+                  "sha256": hashlib.sha256(octets).hexdigest()}
+        except OSError as e:
+            o3 = {"conforme": False, "journal": rel, "etat": f"illisible ({type(e).__name__})"}
+    elif journal.exists() or journal.is_symlink():
+        o3 = {"conforme": False, "journal": rel, "etat": "présent, ni fichier ni absent"}
+    else:
+        o3 = {"conforme": True, "journal": rel, "etat": "absent du disque"}
+    return {"conforme": bool(o1["conforme"] and o2["conforme"] and o3["conforme"]), "O1": o1, "O2": o2, "O3": o3}
+
+
 def lire(racine: Path, run_7b: str, run_bbis: str, instant: int, adaptateur_mc=None, essai: dict | None = None,
          run_7a: str | None = None) -> dict:
     """Lecture complète (plan, point 10, (a) à (e)) ; rend le résultat (sans l'écrire). Un refus de la garde rend I0, motif écrit,
     et rien d'autre n'est lu. `essai` (jouet seulement) : `n_directions`, `n_nul`, `n_tirages` ; jamais en lecture réelle."""
+    if essai is None:
+        exiger_environnement_git_propre()
     from ..harnais.run_harnais_factice import graine_entiere
     from ..manifeste import lire_manifeste
     from ..t06.configuration import conditions_evaluation
@@ -1396,6 +1465,7 @@
     essai = dict(essai or {})
     res = {"texte": TEXTE, "texte_sha256": TEXTE_SHA256, "run_7b": run_7b, "run_bbis": run_bbis,
            "instant_ouverture": rg.date_utc(instant), "essai": not reel, "section_D": SECTION_D}
+    garde, passee = None, False
     try:
         propres = lire_lignes(racine / REGISTRE_PROPRE, CLES_PROPRES, EXIGEES_PROPRES_LECTURE, propre=True,
                               remplacables=REMPLACABLES_PROPRES)
@@ -1417,6 +1487,8 @@
             raise RefusLecture("ligne SCORES-BBIS : chemin autre que diag/<run-bbis>/sondes-bbis.json")
         res["anteriorite"] = anteriorite_etape_b(racine, REGISTRE_PROPRE)
         garde = GardeEntrees(racine, entrees_autorisees(run_7b, run_bbis, partagees, propres), run_7a)
+        passee = True
+        print("BBIS LECTURE ENTREES OUVERTES", flush=True)
         p3 = issue_p3bis(garde.exiger(partagees["VERDICT-P3BIS"]["chemin"]), garde)
         res["p3bis"] = p3
         if p3["P"] != "vu":
@@ -1424,7 +1496,9 @@
             res["entrees_lues"] = sorted(set(garde.lus))
             return res
     except (RefusLecture, rg.RefusRegistre) as e:
-        res["garde"] = {"refus": str(e)}
+        res["garde"] = {"refus": str(e), "nature": "mise en place" if isinstance(e, RefusMiseEnPlace) else "fond"}
+        if res["garde"]["nature"] == "mise en place":
+            res["garde"]["aucune_ouverture"] = preuve_aucune_ouverture(racine, garde, passee)
         res["issue"] = issue_complete({}, {}, None, motif_i0=f"garde refusée ({e})")
         return res
     res["module_gele"] = ad.exiger_module_gele()
@@ -1569,7 +1643,7 @@
               "instant_ouverture": resultat.get("instant_ouverture"), "essai": not reel}
     chemin_m, _ = creer_manifeste(racine, run_lecture, config, cles, entropie=int(entropie), decisif=reel,
                                   prereg=(racine / TEXTE) if reel else None, autoriser_depot_sale=not reel,
-                                  commande="python -m controle_ia.t07bbis.lecture_v4")
+                                  commande="python -m controle_ia.t07bbis.lecture_v5")
     propre = json.loads(json.dumps(resultat, ensure_ascii=False, default=_json))
     return ecrire_resultat(racine, chemin_m, "lecture-bbis", propre)
 
@@ -1592,11 +1666,16 @@
 
 
 def main(argv=None) -> int:
-    """`OMP_NUM_THREADS=1 OPENBLAS_NUM_THREADS=1 MKL_NUM_THREADS=1 PYTHONPATH=src python -m controle_ia.t07bbis.lecture_v4 --racine
+    """`OMP_NUM_THREADS=1 OPENBLAS_NUM_THREADS=1 MKL_NUM_THREADS=1 PYTHONPATH=src python -m controle_ia.t07bbis.lecture_v5 --racine
     R --run-7b RUN --run-bbis RUNB --run-lecture RUNL [--adaptateur-mc module:attribut]` : lit, écrit et scelle
     `diag/<RUNL>/lecture-bbis.json` ; n'imprime que le chemin et l'empreinte (aucune valeur : la lecture humaine suit le scellement
     et la ligne `LECTURE-BBIS`). MC : adaptateur du code de la pièce si la ligne `CODE-MOTS-ET-COUT-T06` est inscrite avant
     l'échéance (`adaptateur_retenu` ; fils de calcul à 1 exigés), sinon implémentation de repli."""
+    try:
+        exiger_environnement_git_propre()
+    except GardeArret as e:
+        print(f"BBIS LECTURE ARRET : {e}")
+        return 2
     import time
     from ..scellement import empreinte
     from .registre_bbis_v1 import REGISTRE_PROPRE, journaliser_ouverture, lire_fiche_code
@@ -1615,6 +1694,17 @@
                               remplacables=REMPLACABLES_PROPRES)
         entropie = lire_fiche_code(racine / propres["CODE-BBIS"]["chemin"])["entropie"]
         chemin = ecrire_lecture(racine, a.run_lecture, r, entropie)
+        refus = r.get("garde") or {}
+        if refus.get("nature") == "mise en place" and (refus.get("aucune_ouverture") or {}).get("conforme") is True:
+            from ..manifeste import ecrire_resultat
+            piece = ecrire_resultat(racine, racine / "runs" / a.run_lecture / "manifeste.json", "preuve-aucune-ouverture-bbis",
+                                    {"motif": refus["refus"], "nature": refus["nature"],
+                                     "aucune_ouverture": refus["aucune_ouverture"],
+                                     "fichier_de_lecture": str(chemin.relative_to(racine)),
+                                     "fichier_de_lecture_sha256": empreinte(chemin)})
+            print(f"BBIS LECTURE NON CONSOMMEE {chemin.relative_to(racine)} {empreinte(chemin)} {piece.relative_to(racine)} "
+                  f"{empreinte(piece)}")
+            return 3
         journaliser_ouverture(racine, f"lecture B bis ({a.run_lecture})", instant, empreinte(chemin))
     except GardeArret as e:
         print(f"BBIS LECTURE ARRET : {e}")
~~~
