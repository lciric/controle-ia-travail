import re, sys, pathlib

F = pathlib.Path("/tmp/claude-0/-home-user-controle-ia-travail/325f961c-9943-5b73-9387-393664866547/scratchpad/prereg-etape1-v6/etape-1-v7.md")
t = F.read_text(encoding="utf-8")

edits = []  # (label, pattern, repl, flags)

# E1 — titre
edits.append(("E1-titre",
  r": sondes apprises par gradient — v6 « économe »",
  ": sondes apprises par gradient — v7 « économe »", 0))

# E2 — paragraphe de version (span complet)
E2_new = (
"Version 7, écrite par la lignée « session-depot » sur la v6 (`ce78d5e5…`, jamais scellée), relue par la contre-lecture R2\n"
"n° 6 (« non scellable » : 1 bloquante, 1 majeure, 1 mineure, 2 de forme, CL6-01 à CL6-05). Elle traite ces remarques sur\n"
"un code nouveau (`bef2c2f`) et le lanceur v4 (inchangé), sans changer aucune hypothèse, prédiction, métrique\n"
"principale, seuil ni table de lecture ; la bloquante CL6-01 (le script de scellement cherchait, à l'entrée\n"
"« Contre-lecture 6 », le libellé « lanceur v3 corrigé » que le texte v6 ne portait plus — il disait « lanceur v4 » — et\n"
"refusait de sceller) et la majeure CL6-02 (un dossier inscriptible par tous imbriqué sous un dossier temporaire déjà\n"
"rendu privé faisait échouer l'exécution isolée, sur l'un et l'autre bras) sont fermées. La v6, écrite sur la v5\n"
"(`d7cf7746…`, jamais scellée), relue par la contre-lecture R2 n° 5 (« non scellable » : 1 bloquante, 2 majeures,\n"
"7 mineures, 2 de forme, CL5-01 à CL5-12), traitait ces remarques sur un code (`224de13`) et le lanceur v4, sans changer\n"
"non plus les énoncés ; la bloquante CL5-01 (le test final était lisible par l'organisme sur l'hôte) et CL5-02 (une voie\n"
"commune entre bras) étaient fermées côté noyau.")
edits.append(("E2-version",
  r"Version 6, écrite par la lignée.*?CL5-02 \(une voie commune entre bras\) sont fermées côté noyau\.",
  E2_new, re.DOTALL))

# E3 — bloc commit
E3_new = (
"commit `bef2c2f9f9c684f414aa36c2f08e04e0ed90e6fa`\n"
"  (depuis `224de13` : CL6-02 — un dossier inscriptible par tous imbriqué sous un temporaire déjà rendu privé ne fait\n"
"  plus échouer l'exécution isolée, essai `test_cl6_02` ; `224de13` : corrections de la contre-lecture n° 5 — isolation\n"
"  du dépôt et du code CL5-01, voie\n"
"  commune CL5-02, lecture gelée CL5-04, essais CL5-05, classement des échecs CL5-07 ; `44cd936` : indice de")
edits.append(("E3-commit",
  r"commit `224de13f88e5931dd47729c6b461033ea955d14b`\n"
  r"  \(depuis `44cd936`, cité par la v5 : corrections de la contre-lecture n° 5 — isolation du dépôt et du code CL5-01, voie\n"
  r"  commune CL5-02, lecture gelée CL5-04, essais CL5-05, classement des échecs CL5-07, `224de13` ; `44cd936` : indice de",
  E3_new, 0))

# E4 — compte essais
edits.append(("E4-essais", r"\*\*132 essais passent\*\*", "**133 essais passent**", 0))

# E5 — phrase mutations
E5_new = (
"dix-sept corrections éprouvées par mutation (douze de la v5,\n"
"  pièce `mutations-rv-v2.txt` ; quatre de la contre-lecture n° 5, pièce `sortie-mutations-cl5-v1.txt` ; une de la\n"
"  contre-lecture n° 6 (CL6-02), pièce `sortie-mutations-cl6-v1.txt` : chacune retirée d'une copie fait échouer son\n"
"  essai, copie non mutée verte).")
edits.append(("E5-mutations",
  r"seize corrections éprouvées par mutation \(douze de la v5,\n"
  r"  pièce `mutations-rv-v2.txt` ; quatre de la contre-lecture n° 5, pièce `mutations-cl5-v1.txt` : chacune retirée d'une\n"
  r"  copie fait échouer son essai, copie non mutée verte\)\.",
  E5_new, re.DOTALL))

# E6 — empreinte bac_a_sable
edits.append(("E6-bac",
  r"8f52ec8864a96f406cbf1c5052a572d689086c2136133a1c17bf4f4ff81c46f5",
  "a84279e536b348def1eff2d61526e1fa0b55a240f311a2a81060df04b316b287", 0))

# E7 — empreinte arbre du noyau
edits.append(("E7-arbre",
  r"f43946a3bd4256719ed44d1de993afe4290f120bad33832f03f324c853bb6d59",
  "062eebccf2cb026c0e57e8b734bc07ebd4144d76453db95f7a430f2bc6cafb56", 0))

# E8a/E8b — pieces v6 -> v7 (l.60, l.61)
edits.append(("E8a-essais-piece",
  r"`prereg/pieces-gradient-etape1-v6/sortie-essais-lanceur-v4.txt`",
  "`prereg/pieces-gradient-etape1-v7/sortie-essais-lanceur-v4.txt`", 0))
edits.append(("E8b-analyseur-piece",
  r"`prereg/pieces-gradient-etape1-v6/sortie-options-analyseur-v4.txt`",
  "`prereg/pieces-gradient-etape1-v7/sortie-options-analyseur-v4.txt`", 0))

# E10 — contradiction Brave (CL6-03)
E10_new = (
"son nom est défini dans la session « session-depot » au scellement (voir « État au scellement » plus bas) : la source\n"
"   `web` n'est servie que si la clé est présente au lancement, et à la même présence dans les deux bras (parité tenue par\n"
"   le lanceur) ; si Brave est présente au lancement, la règle des pannes a cinq comparaisons par paire au lieu de quatre (Seuil).")
edits.append(("E10-brave",
  r"elle ne l'est pas dans la session « session-depot » au scellement : la source\n"
  r"   `web` n'est servie que si la clé est présente au lancement, et à la même présence dans les deux bras \(parité tenue par\n"
  r"   le lanceur\) ; la règle des pannes a alors cinq comparaisons par paire au lieu de quatre \(Seuil\)\.",
  E10_new, re.DOTALL))

# E11 — ligne CL5-11 (nom des pièces de mutation)
E11_new = ("| CL5-11 chiffres et renvois | accepté : noms des pièces de mutation justes "
  "(`mutations-rv-v2.txt`, douze de la v5, scellée en l'état, R12 ; `sortie-mutations-cl5-v1.txt`, quatre de la "
  "contre-lecture n° 5 ; CL6-05) ; coupure à tort à effectifs inégaux dite (0,76 %) ; durées au pire avec l'attente ; "
  "point 12 corrigé (l'amorçage n'est pas dans l'extrait) ; ligne procédurale ajoutée dite |")
edits.append(("E11-cl511",
  r"\| CL5-11 chiffres et renvois \| accepté : pièce `sortie-mutations-v2.txt` nommée juste ; coupure à tort à effectifs inégaux dite \(0,76 %\) ; durées au pire avec l'attente ; point 12 corrigé \(l'amorçage n'est pas dans l'extrait\) ; ligne procédurale ajoutée dite \|",
  E11_new, 0))

# E12 — ligne CL5-12 (script v7, docstring CL6-04)
E12_new = ("| CL5-12 script de scellement | accepté : `prereg/pieces-gradient-etape1-v7/sceller_etape1_v7.py` "
  "(docstring juste, CL6-04) ; `vivier_message` exigé avec les comptes et l'empreinte (Documents) |")
edits.append(("E12-cl512",
  r"\| CL5-12 script de scellement \| accepté : `prereg/pieces-gradient-etape1-v6/sceller_etape1_v6.py` \(docstring juste\) ; `vivier_message` exigé avec les comptes et l'empreinte \(Documents\) \|",
  E12_new, 0))

# E14 — CE3-16 (la 7 dans cette v7)
edits.append(("E14-ce316", r"\(la 6 dans cette v6\)", "(la 7 dans cette v7)", 0))

# E15 — en-tête traitement CL5 (texte de la v6)
edits.append(("E15-cl5head", r"texte de cette v6\) :", "texte de la v6) :", 0))

# E13 — entrée Contre-lecture 6 remplie + nouvelle Contre-lecture 7
CL7_PLACEHOLDER = (
"- **Contre-lecture 7** — sous-agent neuf, revérification limitée aux corrections CL6-01 à CL6-05 (texte v7, diff du code de\n"
"  `224de13` à `bef2c2f`, lanceur v4) ; son rapport, l'entropie E (Plan d'analyse, point 5) et les graines sont\n"
"  inscrits ici au scellement.")
E13_new = (
"- **Contre-lecture 6** — sous-agent neuf, le 25 octobre 2026 de 02:53 à 03:21 UTC, revérification limitée aux corrections\n"
"  CL5-01 à CL5-12 (texte v6, diff du code de `44cd936` à `224de13`, lanceur v4). Texte relu :\n"
"  `gradient-etape1-sondes-v6.md` (marqueurs de scellement non remplis)\n"
"  `ce78d5e59e3ae8e29b998f272d10a65c42765e32d45b6c9c3dc5180dd5b45c4e`. Rapport :\n"
"  `contre-lecture-preenregistrement-gradient-etape1-v6.md` `8e503e3ebdc313460eba1f60353762cc3010800cfd25fb1426cf835d3056d372`.\n"
"  Verdict : **non scellable** ; 1 bloquante, 1 majeure (bloquante pour l'exécution), 1 mineure, 2 de forme. Le fond des\n"
"  corrections CL5-01 à CL5-12 est jugé juste et éprouvé (8 traitées, 4 en partie, les parts non faites étant les cinq\n"
"  remarques ci-dessous). Traitement (code `224de13` → `bef2c2f`, lanceur v4 inchangé ; texte de cette v7) :\n"
"\n"
"| remarque | traitement |\n"
"|---|---|\n"
"| CL6-01 (bloquante) le script de scellement refuse de sceller le texte : il cherche l'entrée « Contre-lecture 6 » au libellé « lanceur v3 corrigé », que le texte v6 ne porte plus (il dit « lanceur v4 ») | accepté, texte et script : le libellé « lanceur v4 » est partout (version, Documents, entrées de contre-lecture) ; le script de scellement de cette v7 (`sceller_etape1_v7.py`) cherche et inscrit l'entrée « Contre-lecture 7 » au libellé « lanceur v4 » ; scellement à blanc rejoué |\n"
"| CL6-02 (majeure, bloquante pour l'exécution) la boucle `prives` abandonne sur un dossier inscriptible par tous imbriqué sous un temporaire déjà rendu privé ; aucun organisme ne tourne | accepté, code (`bef2c2f`) : la boucle `prives` de `ABAISSER_SOURCE` absorbe errno 2 (parent déjà couvert), comme la boucle `caches` ; essai sain et artefact `test_cl6_02_dossier_inscriptible_imbrique_sous_un_temporaire` ; mutation `cl6-02` (retrait du saut errno 2 → l'essai échoue) ; arbre du noyau et empreinte de `bac_a_sable.py` nouveaux |\n"
"| CL6-03 (mineure) contradiction interne sur la présence de Brave au scellement (une clause disait l'inverse de « État au scellement ») | accepté, texte : la clause est réécrite pour concorder — nom de Brave défini au scellement ; cinq comparaisons par paire si Brave est présente au lancement, sous réserve de cette présence |\n"
"| CL6-04 (forme) la docstring du script de scellement n'était pas « juste » (« contre-lecture n° 4 », « `sceller_etape1_v4.py` ») | accepté, script : docstring de `sceller_etape1_v7.py` juste (contre-lecture n° 7, décliné de `sceller_etape1_v6.py`) |\n"
"| CL6-05 (forme) le nom de la pièce de mutations n'était pas corrigé (l. 37 citait « mutations-rv-v2.txt » et « mutations-cl5-v1.txt ») | accepté, texte : les noms cités sont ceux des pièces réellement versées — `mutations-rv-v2.txt` (douze de la v5, scellée en v5, R12) et `sortie-mutations-cl5-v1.txt` (quatre de la contre-lecture n° 5), plus `sortie-mutations-cl6-v1.txt` (CL6-02) ; revendication CL5-11 alignée |\n"
"\n"
+ CL7_PLACEHOLDER)
edits.append(("E13-cl6-cl7",
  r"- \*\*Contre-lecture 6\*\* — sous-agent neuf, revérification limitée aux corrections CL5-01 à CL5-12 \(texte v6, diff du code de\n"
  r"  `44cd936` à `224de13`, lanceur v4\) ; son rapport, l'entropie E \(Plan d'analyse, point 5\) et les graines sont\n"
  r"  inscrits ici au scellement\.",
  E13_new, re.DOTALL))

for label, pat, repl, flags in edits:
    new, n = re.subn(pat, lambda m: repl, t, flags=flags)
    if n != 1:
        print(f"ÉCHEC {label} : {n} remplacement(s) (attendu 1)")
        sys.exit(1)
    t = new
    print(f"OK {label}")

F.write_text(t, encoding="utf-8")
# sauver le gabarit de l'entrée n°7 pour le script de scellement
pathlib.Path("/tmp/claude-0/-home-user-controle-ia-travail/325f961c-9943-5b73-9387-393664866547/scratchpad/prereg-etape1-v6/cl7_placeholder.txt").write_text(CL7_PLACEHOLDER, encoding="utf-8")
print("--- écrit ; longueur", len(t))
