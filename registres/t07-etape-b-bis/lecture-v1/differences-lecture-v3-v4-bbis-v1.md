# Différences entre la version 3 et la version 4 du module de lecture — apprentissage des sondes sur la tâche (étape B bis de T0.7) — v1

- **Auteur** : développeur neuf du module de lecture `lecture_v4`, sous-agent de la session conductrice de la lecture (`session_013QMayjNC5GKdDFTN87oAV5`), modèle Fable 5.2. Il n'a écrit ni le texte scellé, ni ses addenda, ni aucun autre code de l'étape B bis ; il n'est ni contre-lecteur, ni lecteur-opérateur, ni juge.
- **Mandat** : `registres/t07-etape-b-bis/lecture-v1/mandat-developpeur-lecture-v4-bbis-v1.md` (`970aa7f2383fb220df5875b38c06d30c6ad0140b12b57160b909f00f4c10dfc0`) et règles communes `registres/t07-etape-b-bis/lecture-v1/regles-communes-agents-lecture-bbis-v1.md` (`5f303a9c58005808f78a5674860cab7b785c876777287dbe22f998f67d7b7783`), compagnons vérifiés.
- **Spécification** : quatrième addendum d'écart scellé, `prereg/T0.7-etape-B-bis-v1-addendum-ecart-4-v1.md` (`5ef929eae8b070bc7f9d1934d487066ded34896df00dc8a9c70c91b44f0b30c4`, compagnon vérifié), § 6.1 (différences D1 à D6) ; note n4 de la contre-lecture du brouillon 1 suivie (la preuve lève le refus de lecture, `RefusLecture`, non l'arrêt de garde).
- **Fichiers comparés** : `src/controle_ia/t07bbis/lecture_v3.py` (`c9a478437f32465418dfafdadbd7823f88853a9c17f77a0e59cc4ccb5ccff6ec`, égale à l'empreinte que le mandat et l'addendum citent ; fichier non modifié) et `src/controle_ia/t07bbis/lecture_v4.py` (`9bfca6269e34bb2a2ccd9b35c43c2af7b69e67b8bee45eab223cbd0a1c85f7ca`).
- **Comment la version 4 a été produite** : par programme, en appliquant à la version 3 les six couples « ancien, nouveau, une occurrence exigée » écrits dans `tests/test_lecture_bbis_v4_addendum_4_v1.py` (`COUPLES`) ; l'essai `test_1_…` refait le fichier depuis la version 3 et exige l'égalité exacte. Aucun autre changement n'existe.
- **Rien d'exécuté sur des fichiers réels** : le module, sa garde et ses fonctions n'ont été joués que sur des registres et des dépôts git jouets, fabriqués dans le dossier temporaire des essais. Aucun fichier de résultat ouvert.

## Blocs changés : six, chacun fondé

Sortie de `diff -u` ci-dessous : **six blocs**. Aucun bloc sans fondement.

| bloc | lignes de la version 3 → lignes de la version 4 | ce qui change | différence du § 6.1 qui le fonde |
|---|---|---|---|
| 1 | 7-12 → 7-21 | un paragraphe ajouté au docstring d'en-tête : nomme le quatrième addendum, son empreinte scellée, et la liste D2 à D6 ; aucune ligne retirée | **D1** — en-tête |
| 2 | 573-578 → 582-599 | constante `EXCEPTION_ORDRE_ADDENDUM_4` ajoutée après `REMPLACABLES_PROPRES` : les trois lignes de F1 (date, chemin, empreinte), les trois commits de QA-1, le chemin du registre propre ; valeurs recopiées de l'addendum, aucune lue dans un fichier ; aucune ligne retirée | **D2** — constante |
| 3 | 633-648 → 654-812 | fonction neuve `preuve_entree_conjointe(racine, exception)`, placée juste avant la fonction d'ordre ; puis `exiger_ordre_propre(lignes, racine=None, exception=None) -> dict` à la place de `exiger_ordre_propre(lignes) -> None` | **D3** — preuve (P1) à (P5) par commandes git en lecture ; **D4** — fonction d'ordre (les deux fonctions se suivent : un seul bloc de `diff`) |
| 4 | 1243-1249 → 1407-1414 | dans `lire`, à la place de l'appel de la l. 1246, même position dans le bloc de la garde : `res["ordre_propre"] = exiger_ordre_propre(propres, racine, EXCEPTION_ORDRE_ADDENDUM_4 if reel else essai.get("exception_ordre"))` | **D5** — appel dans `lire` |
| 5 | 1404-1410 → 1569-1575 | `commande="python -m controle_ia.t07bbis.lecture_v4"` dans `ecrire_lecture` | **D6** — nom du module |
| 6 | 1427-1433 → 1592-1598 | `python -m controle_ia.t07bbis.lecture_v4` dans le docstring de `main` | **D6** — nom du module |

## Lectures retenues là où le § 6.1 ne fixe pas la lettre (à juger par le contre-lecteur du code)

Chacune reste à l'intérieur d'une différence déclarée ; aucune n'ajoute un comportement que le § 6.1 ne nomme pas. Elles sont dites ici pour que rien ne soit caché.

1. **Forme de la constante (D2).** Le § 6.1 fixe son contenu, non ses clés. Clés retenues : `registre_propre`, `code_bbis_remplace`, `code_bbis`, `go_bbis` (chacune : `date`, `chemin`, `sha256`), `commit_entree_conjointe`, `commit_remise_premiere_fiche`, `commit_course`. C'est un dictionnaire ordinaire (non gelé) : aucun code du module ne le modifie.
2. **Importations (D3).** `hashlib` (empreintes des contenus lus par `git show`) et `re` (forme d'un identifiant de commit) sont importés **dans** la fonction neuve, pour ne pas toucher le bloc d'importations du module.
3. **Refus avant toute commande git (D3).** Un identifiant de commit qui n'est pas fait de 40 caractères hexadécimaux, un chemin de l'exception absolu, vide, commençant par un tiret ou portant « .. », une exception sans une de ses clés : `RefusLecture` (« point en défaut »), sans appeler git.
4. **`ls-tree --full-tree` (D3).** L'option rend les chemins relatifs à la racine du dépôt, comme `git show <commit>:<chemin>` ; sans elle, une racine de lecture qui ne serait pas la racine du dépôt rendrait « absent » un fichier présent, et (P3) y verrait à tort la fiche remplaçante absente de l'arbre du parent.
5. **« À l'octet » (P2, P4).** La ligne attendue est reconstruite `| clé | date | chemin | empreinte |` et comptée parmi les lignes du registre découpé sur le seul saut de ligne ; une ligne suivie d'un retour chariot ou d'une espace ne compte pas. « Aucune ligne de clé `CODE-BBIS` ni `GO-BBIS` » au parent : même découpe de la clé que `lire_lignes`. « Aucune ligne qui cite » la première fiche au parent de la remise : aucune ligne du registre ne contient le chemin de la fiche.
6. **Registre absent d'un commit ou de son parent (P2, P4).** `git show` échoue : refus (« objet absent »), jamais « aucune ligne ».
7. **Tête de l'arbre de lecture (P5).** Relevée par `rev-list --parents -n 1 HEAD` (commande de la liste du § 6.1) ; `merge-base --is-ancestor` rend 0 quand la tête est le commit de la course.
8. **Texte du refus quand la preuve a été tentée (D4).** « <refus de la v3, mot pour mot> ; preuve d'entrée conjointe du quatrième addendum refusée : preuve d'entrée conjointe, point (Pn) : <motif> ».
9. **Exception mal formée passée à la fonction d'ordre (D4).** Tenue pour « triplets autres que ceux de l'exception » : refus de la v3, mot pour mot, la preuve n'est pas tentée.
10. **Clé `ordre_propre` (D5).** Écrite quand la fonction d'ordre a rendu ; sur un refus de la garde, la clé est absente et le motif est sous `garde`, comme dans la version 3.

## Points ouverts

1. **Nom du fichier d'essais — le mandat et l'addendum scellé se contredisent.** Le mandat du développeur (et celui du contre-lecteur du code) nomme `tests/test_t07bbis_lecture_v4.py` ; le § 6.2 de l'addendum scellé nomme `tests/test_lecture_bbis_v4_addendum_4_v1.py` et dit pourquoi (« nom hors du motif `test_t07bbis_*`, que la fiche de code et la chaîne de la course comptaient »). Le texte scellé prime : le fichier est déposé sous le nom **de l'addendum**. À trancher par la conductrice ; un renommage ne change pas un octet du contenu (le fichier ne cite pas son propre nom).
2. **Sortie des essais « versée et scellée » (§ 6.2, dernière ligne ; § 6.3, fiche de rattachement).** Le mandat du développeur ne lui fait déposer que trois fichiers. La sortie (noms et comptes, aucun fichier réel touché) est laissée hors du dépôt, dans le dossier temporaire de la session, à verser par la conductrice si elle la retient.
3. **Docstring de `lire`.** Il continue de nommer les seules clés d'essai `n_directions`, `n_nul`, `n_tirages` ; la clé d'essai `exception_ordre` (D5) n'y est pas ajoutée : le § 6.1 ne déclare aucun changement de ce docstring.
4. **Variables d'environnement de git.** Les commandes git de la preuve, comme celles de `anteriorite_etape_b` dans la version 3, héritent de l'environnement du processus (`GIT_DIR` et voisines) ; le § 6.1 ne déclare aucune garde là-dessus, la version 4 n'en ajoute pas. À tenir par la commande de lecture.
5. **Le § 6.2, point 1, dit le différentiel « forme de `tests/aide_t07bbis_differentiels_v4.py` ».** Les couples sont écrits dans le fichier d'essais lui-même, non dans un fichier d'aide à part, pour s'en tenir aux trois fichiers du mandat.

## Sortie de `diff -u` (version 3 → version 4)

Commande : `diff -u --label lecture_v3.py --label lecture_v4.py src/controle_ia/t07bbis/lecture_v3.py src/controle_ia/t07bbis/lecture_v4.py`.

~~~diff
--- lecture_v3.py
+++ lecture_v4.py
@@ -7,6 +7,15 @@
 chaque famille, information à 300 époques de la linéaire, phrase du discriminant) ; ligne `CODE-BBIS` remplacée une seule fois
 lue au registre propre (`lire_lignes`, `exiger_ordre_propre`) ; les v1 et v2 restent (R12).
 
+v4 : la v3, modifiée par le **quatrième addendum d'écart** (`prereg/T0.7-etape-B-bis-v1-addendum-ecart-4-v1.md`, empreinte scellée
+`5ef929eae8b070bc7f9d1934d487066ded34896df00dc8a9c70c91b44f0b30c4`, § 6.1) et par lui seul : (D2) constante
+`EXCEPTION_ORDRE_ADDENDUM_4` (les trois lignes du registre propre, les trois commits et le chemin du registre que la preuve
+épingle) ; (D3) fonction neuve `preuve_entree_conjointe` (points (P1) à (P5) de QA-1, commandes git en lecture) ; (D4)
+`exiger_ordre_propre(lignes, racine=None, exception=None)` : pour le seul couple (`GO-BBIS`, `CODE-BBIS` qui fait foi), l'égalité à
+la seconde ne vaut pas refus si les trois lignes sont celles de l'exception et si la preuve passe ; (D5) dans `lire`, la règle qui
+a servi est écrite sous `ordre_propre` (lecture réelle : la constante et elle seule) ; (D6) nom du module dans `ecrire_lecture` et
+dans le docstring de `main`. Les v1 à v3 restent (R12).
+
 Sections : (1) états d'une cellule (table A), issue I0 à I6, suffixe du transfert T0 à T+, libellés du nœud 5 (« lecture dure »,
 retenu ; « lettre de R-2716 », information), qualifications (MU, SC), lignes de (i-a), réserves et audit de symétrie R4 —
 phrases gelées recopiées du texte, crochets remplis par le code ; (2) gardes : refus sur l'instance (variable `BBIS_INSTANCE`,
@@ -573,6 +582,18 @@
 PERMISES_PARTAGEES = ("CODE-MOTS-ET-COUT-T06", "ISSUE-MOTS-ET-COUT-T06", "AUDIT-FUITES-T07")
 ORDRE_PROPRE = ("SCELLEMENT-BBIS", "CODE-BBIS", "GO-BBIS", "SCORES-BBIS")
 REMPLACABLES_PROPRES = ("CODE-BBIS",)
+EXCEPTION_ORDRE_ADDENDUM_4 = {
+    "registre_propre": "registres/t07-etape-b-bis-v1.md",
+    "code_bbis_remplace": {"date": "2026-11-16T12:57:27Z", "chemin": "registres/t07-etape-b-bis/code-bbis-v1.json",
+                           "sha256": "ee362bb70c5051097dab90c7978eb550d192f8c90f313317812635884b04e469"},
+    "code_bbis": {"date": "2026-11-17T11:05:29Z", "chemin": "registres/t07-etape-b-bis/code-bbis-v2.json",
+                  "sha256": "4b28535c17fe450ff1c1ecc9164d91c4c8d03354e4f4137e324f2b04390be5bb"},
+    "go_bbis": {"date": "2026-11-17T11:05:29Z", "chemin": "registres/t07-etape-b-bis/go-bbis-v2.txt",
+                "sha256": "33f38e675ca2114674b6f7dd96727b222fae613ecb53b57ef16240b74aca8e62"},
+    "commit_entree_conjointe": "c098fb512d999e1dbf7cef5fba6430ff8b1a8fb5",
+    "commit_remise_premiere_fiche": "06c8832819af344d01c184222833c5a42e8ac901",
+    "commit_course": "438a9c5257bdc4fa65f25c42cc89753a049b4586",
+}
 
 
 def lire_lignes(registre: Path, cles, exigees, propre: bool, remplacables=()) -> dict:
@@ -633,16 +654,159 @@
         raise RefusLecture(" ; ".join(fautes))
 
 
-def exiger_ordre_propre(lignes: dict) -> None:
+def preuve_entree_conjointe(racine: Path, exception: dict) -> dict:
+    """Preuve d'entrée conjointe du quatrième addendum (QA-1, points (P1) à (P5)), relevée dans le dépôt de `racine` par des
+    commandes git en lecture (`cat-file -e`, `rev-list --parents -n 1`, `show <commit>:<chemin>`, `ls-tree`, `merge-base
+    --is-ancestor`) ; les empreintes des contenus lus par `git show` sont recalculées. Rend, pour chaque point, « conforme » avec
+    les identifiants relevés. Un point en défaut, un objet absent, un code de retour inattendu : `RefusLecture` avec le point et
+    le motif ; aucun repli (R5). `merge-base --is-ancestor` : code 0, ancêtre ; code 1, refus « non ancêtre » ; tout autre code,
+    refus « échec de git »."""
+    import hashlib
+    import re
+    hexa = re.compile(r"[0-9a-f]{40}")
+
+    def refus(point: str, motif: str) -> RefusLecture:
+        return RefusLecture(f"preuve d'entrée conjointe, point ({point}) : {motif}")
+
+    def git(point: str, *args, codes=(0,)):
+        try:
+            r = subprocess.run(["git", "-C", str(racine), *args], capture_output=True)
+        except OSError as e:
+            raise refus(point, f"git {' '.join(args[:2])} : échec de git ({e})") from None
+        if r.returncode not in codes:
+            raise refus(point, f"git {' '.join(args[:2])} : échec de git (code {r.returncode} ; "
+                               f"{r.stderr.decode('utf-8', 'replace').strip()[:200]})")
+        return r
+
+    def exiger_commit(point: str, c) -> None:
+        if not isinstance(c, str) or not hexa.fullmatch(c):
+            raise refus(point, f"identifiant de commit {c!r} : 40 caractères hexadécimaux attendus")
+        r = git(point, "cat-file", "-e", f"{c}^{{commit}}", codes=tuple(range(256)))
+        if r.returncode != 0:
+            raise refus(point, f"commit {c[:12]} absent du dépôt ou illisible (code {r.returncode} ; "
+                               f"{r.stderr.decode('utf-8', 'replace').strip()[:200]})")
+
+    def seul_parent(point: str, c) -> str:
+        exiger_commit(point, c)
+        x = git(point, "rev-list", "--parents", "-n", "1", c).stdout.decode("utf-8", "replace").split()
+        if len(x) != 2 or x[0] != c or not hexa.fullmatch(x[1]):
+            raise refus(point, f"commit {c[:12]} : {max(len(x) - 1, 0)} parent(s) relevé(s), un seul exigé")
+        return x[1]
+
+    def texte(point: str, c: str, chemin: str) -> str:
+        try:
+            return git(point, "show", f"{c}:{chemin}").stdout.decode("utf-8")
+        except UnicodeDecodeError:
+            raise refus(point, f"{chemin} au commit {c[:12]} : contenu illisible") from None
+
+    def present(point: str, c: str, chemin: str) -> bool:
+        s = git(point, "ls-tree", "--full-tree", c, "--", chemin).stdout.decode("utf-8", "replace").splitlines()
+        if not s:
+            return False
+        if len(s) != 1 or s[0].split()[1:2] != ["blob"]:
+            raise refus(point, f"{chemin} dans l'arbre du commit {c[:12]} : un fichier, et un seul, attendu")
+        return True
+
+    def empreinte_lue(point: str, c: str, chemin: str) -> str:
+        return hashlib.sha256(git(point, "show", f"{c}:{chemin}").stdout).hexdigest()
+
+    def exiger_ancetre(point: str, a: str, b: str, quoi: str) -> None:
+        if git(point, "merge-base", "--is-ancestor", a, b, codes=(0, 1)).returncode == 1:
+            raise refus(point, f"{quoi} : non ancêtre")
+
+    cle = lambda l: [x.strip() for x in l.strip().strip("|").split("|")][0]
+    try:
+        registre = exception["registre_propre"]
+        code, go, premiere = (exception[k] for k in ("code_bbis", "go_bbis", "code_bbis_remplace"))
+        c_conj, c_remise, c_course = (exception[k] for k in ("commit_entree_conjointe", "commit_remise_premiere_fiche",
+                                                             "commit_course"))
+        l_code, l_go, l_premiere = (f"| {k} | {x['date']} | {x['chemin']} | {x['sha256']} |"
+                                    for k, x in (("CODE-BBIS", code), ("GO-BBIS", go), ("CODE-BBIS", premiere)))
+        chemins = [registre, code["chemin"], go["chemin"], premiere["chemin"]]
+    except (KeyError, TypeError) as e:
+        raise RefusLecture(f"preuve d'entrée conjointe : exception mal formée ({e!r})") from None
+    if any(not isinstance(x, str) or not x or x.startswith(("/", "-")) or ".." in Path(x).parts for x in chemins):
+        raise RefusLecture("preuve d'entrée conjointe : exception mal formée (chemin)")
+    # (P1) le commit de l'entrée conjointe existe et a un seul parent
+    parent = seul_parent("P1", c_conj)
+    # (P2) au commit, les deux lignes, une fois chacune et à l'octet ; au parent, aucune ligne de clé CODE-BBIS ni GO-BBIS
+    au_commit = texte("P2", c_conj, registre).split("\n")
+    for nom, l in (("CODE-BBIS", l_code), ("GO-BBIS", l_go)):
+        if au_commit.count(l) != 1:
+            raise refus("P2", f"au commit {c_conj[:12]}, le registre propre porte {au_commit.count(l)} fois la ligne {nom} de "
+                              "l'exception, une fois exigée")
+    deja = sorted({cle(l) for l in texte("P2", parent, registre).splitlines()} & {"CODE-BBIS", "GO-BBIS"})
+    if deja:
+        raise refus("P2", f"au parent {parent[:12]}, le registre propre porte déjà une ligne de clé {deja}")
+    # (P3) le fichier de l'accord est dans l'arbre du parent, à l'empreinte de sa ligne ; la fiche remplaçante n'y est pas ;
+    # elle est dans l'arbre du commit, à l'empreinte de sa ligne
+    if not present("P3", parent, go["chemin"]):
+        raise refus("P3", f"{go['chemin']} absent de l'arbre du parent {parent[:12]}")
+    if empreinte_lue("P3", parent, go["chemin"]) != go["sha256"]:
+        raise refus("P3", f"{go['chemin']} au parent {parent[:12]} : empreinte autre que celle de la ligne GO-BBIS")
+    if present("P3", parent, code["chemin"]):
+        raise refus("P3", f"{code['chemin']} déjà présent dans l'arbre du parent {parent[:12]}")
+    if not present("P3", c_conj, code["chemin"]):
+        raise refus("P3", f"{code['chemin']} absent de l'arbre du commit {c_conj[:12]}")
+    if empreinte_lue("P3", c_conj, code["chemin"]) != code["sha256"]:
+        raise refus("P3", f"{code['chemin']} au commit {c_conj[:12]} : empreinte autre que celle de la ligne CODE-BBIS")
+    # (P4) le commit de la remise de la première fiche existe, a un seul parent, descend de l'entrée conjointe ; il porte une
+    # fois, à l'octet, la ligne de la première fiche ; à son parent, aucune ligne ne cite la première fiche
+    parent_remise = seul_parent("P4", c_remise)
+    exiger_ancetre("P4", c_conj, c_remise, f"commit de l'entrée conjointe {c_conj[:12]} et commit de la remise {c_remise[:12]}")
+    a_la_remise = texte("P4", c_remise, registre).split("\n")
+    if a_la_remise.count(l_premiere) != 1:
+        raise refus("P4", f"au commit {c_remise[:12]}, le registre propre porte {a_la_remise.count(l_premiere)} fois la ligne de "
+                          "la première fiche de l'exception, une fois exigée")
+    if any(premiere["chemin"] in l for l in texte("P4", parent_remise, registre).splitlines()):
+        raise refus("P4", f"au parent {parent_remise[:12]}, le registre propre cite déjà {premiere['chemin']}")
+    # (P5) la remise précède le commit de la course, qui est un ancêtre de la tête de l'arbre de lecture (ou cette tête)
+    exiger_commit("P5", c_course)
+    exiger_ancetre("P5", c_remise, c_course, f"commit de la remise {c_remise[:12]} et commit de la course {c_course[:12]}")
+    tete = git("P5", "rev-list", "--parents", "-n", "1", "HEAD").stdout.decode("utf-8", "replace").split()[:1]
+    if len(tete) != 1 or not hexa.fullmatch(tete[0]):
+        raise refus("P5", "tête de l'arbre de lecture illisible")
+    exiger_ancetre("P5", c_course, tete[0], f"commit de la course {c_course[:12]} et tête {tete[0][:12]}")
+    return {"P1": {"etat": "conforme", "commit": c_conj, "parent": parent},
+            "P2": {"etat": "conforme", "commit": c_conj, "parent": parent, "registre": registre},
+            "P3": {"etat": "conforme", "commit": c_conj, "parent": parent, "accord": go["chemin"], "accord_sha256": go["sha256"],
+                   "fiche": code["chemin"], "fiche_sha256": code["sha256"]},
+            "P4": {"etat": "conforme", "commit": c_remise, "parent": parent_remise, "descend_de": c_conj},
+            "P5": {"etat": "conforme", "commit_remise": c_remise, "commit_course": c_course, "tete": tete[0]}}
+
+
+def exiger_ordre_propre(lignes: dict, racine: Path | None = None, exception: dict | None = None) -> dict:
     """Ordre du plan, point 2 ; second addendum : une ligne `CODE-BBIS` remplacée se lit SCELLEMENT-BBIS < CODE-BBIS (première)
-    < GO-BBIS < CODE-BBIS (remplacement) < SCORES-BBIS."""
+    < GO-BBIS < CODE-BBIS (remplacement) < SCORES-BBIS. Quatrième addendum (QA-1) : pour le seul couple (`GO-BBIS`, `CODE-BBIS`
+    qui fait foi), quand la comparaison stricte échoue, si `racine` et `exception` sont donnés, si les deux dates écrites sont
+    égales et si les triplets (date, chemin, empreinte) de `GO-BBIS`, de `CODE-BBIS` et de la ligne remplacée sont ceux de
+    `exception`, la preuve d'entrée conjointe est jouée ; si elle passe, ce couple est tenu pour ordonné et la boucle continue.
+    Rend `{"regle": "stricte"}`, ou `{"regle": "quatrième addendum", "preuve": …}`. Tout autre échec : refus de la v3, mot pour
+    mot, suivi, quand la preuve a été tentée, de son motif. Sans `racine` ni `exception`, la fonction est la v3."""
     lignes, chaine = dict(lignes), list(ORDRE_PROPRE)
     if "CODE-BBIS" in lignes and "remplace" in lignes["CODE-BBIS"]:
         lignes["CODE-BBIS (première)"] = lignes["CODE-BBIS"]["remplace"]
         chaine = ["SCELLEMENT-BBIS", "CODE-BBIS (première)", "GO-BBIS", "CODE-BBIS", "SCORES-BBIS"]
+    preuve = None
     for a, b in zip(chaine, chaine[1:]):
         if a in lignes and b in lignes and not lignes[a]["instant"] < lignes[b]["instant"]:
-            raise RefusLecture(f"ligne {a} ({lignes[a]['date']}) pas strictement antérieure à {b} ({lignes[b]['date']})")
+            refus = f"ligne {a} ({lignes[a]['date']}) pas strictement antérieure à {b} ({lignes[b]['date']})"
+            triplet = lambda x: (x["date"], x["chemin"], x["sha256"])
+            try:
+                ouverte = ((a, b) == ("GO-BBIS", "CODE-BBIS") and racine is not None and exception is not None
+                           and lignes[a]["date"] == lignes[b]["date"] and lignes[a]["instant"] == lignes[b]["instant"]
+                           and all(triplet(lignes[k]) == triplet(exception[e]) for k, e in
+                                   (("GO-BBIS", "go_bbis"), ("CODE-BBIS", "code_bbis"),
+                                    ("CODE-BBIS (première)", "code_bbis_remplace"))))
+            except (KeyError, TypeError):
+                ouverte = False
+            if not ouverte:
+                raise RefusLecture(refus)
+            try:
+                preuve = preuve_entree_conjointe(racine, exception)
+            except RefusLecture as e:
+                raise RefusLecture(f"{refus} ; preuve d'entrée conjointe du quatrième addendum refusée : {e}") from None
+    return {"regle": "stricte"} if preuve is None else {"regle": "quatrième addendum", "preuve": preuve}
 
 
 def _git(racine: Path, *args) -> str:
@@ -1243,7 +1407,8 @@
                                 propre=False)
         verifier_lignes(racine, propres, instant)
         verifier_lignes(racine, partagees, instant)
-        exiger_ordre_propre(propres)
+        res["ordre_propre"] = exiger_ordre_propre(propres, racine,
+                                                  EXCEPTION_ORDRE_ADDENDUM_4 if reel else essai.get("exception_ordre"))
         if (propres["SCELLEMENT-BBIS"]["chemin"], propres["SCELLEMENT-BBIS"]["sha256"]) != (TEXTE, TEXTE_SHA256):
             raise RefusLecture("ligne SCELLEMENT-BBIS : chemin ou empreinte autre que le texte scellé de B bis")
         if partagees["RUN-CONFIRMATION-T06"]["chemin"] != f"runs/{run_7b}/manifeste.json":
@@ -1404,7 +1569,7 @@
               "instant_ouverture": resultat.get("instant_ouverture"), "essai": not reel}
     chemin_m, _ = creer_manifeste(racine, run_lecture, config, cles, entropie=int(entropie), decisif=reel,
                                   prereg=(racine / TEXTE) if reel else None, autoriser_depot_sale=not reel,
-                                  commande="python -m controle_ia.t07bbis.lecture_v3")
+                                  commande="python -m controle_ia.t07bbis.lecture_v4")
     propre = json.loads(json.dumps(resultat, ensure_ascii=False, default=_json))
     return ecrire_resultat(racine, chemin_m, "lecture-bbis", propre)
 
@@ -1427,7 +1592,7 @@
 
 
 def main(argv=None) -> int:
-    """`OMP_NUM_THREADS=1 OPENBLAS_NUM_THREADS=1 MKL_NUM_THREADS=1 PYTHONPATH=src python -m controle_ia.t07bbis.lecture_v3 --racine
+    """`OMP_NUM_THREADS=1 OPENBLAS_NUM_THREADS=1 MKL_NUM_THREADS=1 PYTHONPATH=src python -m controle_ia.t07bbis.lecture_v4 --racine
     R --run-7b RUN --run-bbis RUNB --run-lecture RUNL [--adaptateur-mc module:attribut]` : lit, écrit et scelle
     `diag/<RUNL>/lecture-bbis.json` ; n'imprime que le chemin et l'empreinte (aucune valeur : la lecture humaine suit le scellement
     et la ligne `LECTURE-BBIS`). MC : adaptateur du code de la pièce si la ligne `CODE-MOTS-ET-COUT-T06` est inscrite avant
~~~
