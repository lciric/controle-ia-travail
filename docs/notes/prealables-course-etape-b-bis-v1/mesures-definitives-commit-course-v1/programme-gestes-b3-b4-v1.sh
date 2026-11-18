#!/usr/bin/env bash
# Gestes B.4 et B.3 (partie hors loueur) de l'arbitrage 688abea5…, au commit de la course exactement.
# Lecture seule du dépôt : aucune écriture dans le dépôt, aucun réseau, aucune clé.
# Usage : bash gestes_b3_b4.sh RACINE DOSSIER_SORTIE
set -u
R="$1"; O="$2"
C=438a9c5257bdc4fa65f25c42cc89753a049b4586
F=05cd22aa
cd "$R" || exit 9
for v in $(compgen -v | grep -E '^GIT_'); do unset "$v"; done
entete() { printf '# %s\n# commit de la course : %s\n# heure (UTC) : %s\n# commande :\n%s\n# sortie :\n' "$1" "$C" "$(date -u +%FT%TZ)" "$2"; }

# 1. git diff --quiet du code hors de la fiche
f="$O/geste-b4-1-git-diff-quiet-code-hors-fiche.txt"
cmd="git diff --quiet $F $C -- src requirements-gpu.txt pyproject.toml tests/conftest.py 'tests/test_t07bbis_*' 'tests/aide_t07bbis_*'"
{ entete "Geste B.4, point 1 : code hors de la fiche inchangé depuis le commit de la fiche" "$cmd"
  git diff --quiet "$F" "$C" -- src requirements-gpu.txt pyproject.toml tests/conftest.py 'tests/test_t07bbis_*' 'tests/aide_t07bbis_*' 2>&1; c=$?
  printf '(aucune sortie attendue)\n# code de retour : %s (attendu 0)\n' "$c"
  printf '# contrôle complémentaire (même chemins, liste des fichiers différents) :\n'
  git diff --name-only "$F" "$C" -- src requirements-gpu.txt pyproject.toml tests/conftest.py 'tests/test_t07bbis_*' 'tests/aide_t07bbis_*' 2>&1
  printf '# fin de la liste (vide attendue)\n'
} > "$f"

# 2. empreintes des fichiers réutilisés de la l. 19 du texte scellé, au commit de la course
f="$O/geste-b4-2-empreintes-l19-texte-scelle.txt"
{ entete "Geste B.4, point 2 : fichiers réutilisés (l. 19 du texte scellé prereg/T0.7-etape-B-bis-v1.md) comparés au commit de la course" "git show $C:prereg/T0.7-etape-B-bis-v1.md | sed -n 19p ; puis, pour chaque fichier, git show $C:<chemin> | sha256sum comparé à l'empreinte de la l. 19"
  printf 'texte scellé au commit : %s (attendu 0ae6210f954917fecff647f45a129961c0676517381becbffe1fd5ac7b90d9eb)\n' "$(git show "$C:prereg/T0.7-etape-B-bis-v1.md" | sha256sum | cut -d' ' -f1)"
  L19=$(git show "$C:prereg/T0.7-etape-B-bis-v1.md" | sed -n 19p)
  printf 'l. 19 : %s\n' "$L19"
  n=0; ko=0
  while read -r chemin attendu; do
    n=$((n+1))
    obtenu=$(git show "$C:$chemin" 2>/dev/null | sha256sum | cut -d' ' -f1)
    a05=$(git show "$F:$chemin" 2>/dev/null | sha256sum | cut -d' ' -f1)
    if [ "$obtenu" = "$attendu" ]; then e=conforme; else e=ECART; ko=$((ko+1)); fi
    printf '%s | l. 19 : %s | au commit de la course : %s | au commit de la fiche %s : %s | %s\n' "$chemin" "$attendu" "$obtenu" "$F" "$a05" "$e"
  done <<'LISTE'
src/controle_ia/sondes/familles.py 6758b651fdcbc6d0108a03263b79ffb1e7c5d0a8be57b0f10502c1645d2b457e
src/controle_ia/sondes/evaluation.py 1040674cb321766a0e2a7fa1e0c610384df6c4fac4109dd50c42dfbb03181ed3
src/controle_ia/sondes/temoins.py 3b051b6fc2d78eeb4a44aab8a385bbce65095998e944b80e5f2a66e21b57faf7
src/controle_ia/t07/repli_recalcul_v1.py 9ceabbcb56cacde0cad6e849a36884139b0175bdf20af5e34cf4514d9da3fe1d
src/controle_ia/t07/repli_v1.py 7ae5862da1c867d99cbbdfa0c2350a238920c314a8924254abaf368dd335223a
src/controle_ia/t07/plancher_v2.py a0f80e6826b77279dfb807863af106655c2515f69d6d415657b7b121598ee796
src/controle_ia/t07/plancher_v3.py c25a8822dc4a59d6d3a98b70f8b7aa92c45bbfdb571e482abf2a1a55ba440cd8
src/controle_ia/t06/test_croise.py 0a627df9ecb82c518d06c0c7ca8df4afab48a5a0da34b785c31c0da4ab41a29c
src/controle_ia/organismes/lora.py 5e4ee21ef2b43a921f8080027d5b5547c02c98bab44a1bc3d52a9dfb562c1ae7
src/controle_ia/t07/lecture_v4.py 42f60780e6944568e81880887a1ad87c57a520e8c7d54083b36a43c097a06d06
src/controle_ia/t07/criteres_v1.py 12b999fecce093372a29fb70d8c11eb7fe965f34c8746a31b399baaecc5ae8c5
LISTE
  # contrôle que la liste ci-dessus reprend bien toutes les empreintes de la l. 19 (et elles seules)
  nl19=$(printf '%s' "$L19" | grep -oE '[0-9a-f]{64}' | sort -u | wc -l)
  printf '# fichiers comparés : %s ; écarts : %s ; empreintes de 64 caractères sur la l. 19 : %s\n' "$n" "$ko" "$nl19"
  printf '# chaque empreinte de la liste figure-t-elle sur la l. 19 : '
  manq=0; for h in 6758b651fdcbc6d0108a03263b79ffb1e7c5d0a8be57b0f10502c1645d2b457e 1040674cb321766a0e2a7fa1e0c610384df6c4fac4109dd50c42dfbb03181ed3 3b051b6fc2d78eeb4a44aab8a385bbce65095998e944b80e5f2a66e21b57faf7 9ceabbcb56cacde0cad6e849a36884139b0175bdf20af5e34cf4514d9da3fe1d 7ae5862da1c867d99cbbdfa0c2350a238920c314a8924254abaf368dd335223a a0f80e6826b77279dfb807863af106655c2515f69d6d415657b7b121598ee796 c25a8822dc4a59d6d3a98b70f8b7aa92c45bbfdb571e482abf2a1a55ba440cd8 0a627df9ecb82c518d06c0c7ca8df4afab48a5a0da34b785c31c0da4ab41a29c 5e4ee21ef2b43a921f8080027d5b5547c02c98bab44a1bc3d52a9dfb562c1ae7 42f60780e6944568e81880887a1ad87c57a520e8c7d54083b36a43c097a06d06 12b999fecce093372a29fb70d8c11eb7fe965f34c8746a31b399baaecc5ae8c5; do
    printf '%s' "$L19" | grep -q "$h" || manq=$((manq+1)); done
  printf '%s manquante(s)\n' "$manq"
  printf '# verdict : %s\n' "$([ "$ko" = 0 ] && [ "$n" = 11 ] && [ "$nl19" = 11 ] && [ "$manq" = 0 ] && echo 'conforme (11 sur 11)' || echo ECART)"
} > "$f"

# 3. git ls-tree --name-only de la racine aux deux commits
f="$O/geste-b4-3-ls-tree-racine-05cd22aa-et-commit-course.txt"
{ entete "Geste B.4, point 3 : entrées de la racine au commit de la fiche ($F) et au commit de la course" "git ls-tree --name-only $F ; git ls-tree --name-only $C ; diff des deux listes"
  git ls-tree --name-only "$F" > "$O/.lt-a"; git ls-tree --name-only "$C" > "$O/.lt-b"
  printf '## %s (%s entrées)\n' "$F" "$(grep -c '' "$O/.lt-a")"; cat "$O/.lt-a"
  printf '## %s (%s entrées)\n' "$C" "$(grep -c '' "$O/.lt-b")"; cat "$O/.lt-b"
  printf '## diff (vide attendu)\n'; diff "$O/.lt-a" "$O/.lt-b"; c=$?
  printf '# code du diff : %s (0 : listes égales)\n' "$c"
  printf '## fichiers (blobs) de la racine, extraits par le motif /* : empreinte des objets aux deux commits\n'
  git ls-tree "$F" | awk '$2=="blob"' > "$O/.lb-a"; git ls-tree "$C" | awk '$2=="blob"' > "$O/.lb-b"
  printf '### %s\n' "$F"; cat "$O/.lb-a"; printf '### %s\n' "$C"; cat "$O/.lb-b"
  printf '### diff des fichiers de la racine (objets) :\n'; diff "$O/.lb-a" "$O/.lb-b"; c2=$?
  printf '# code du diff des fichiers de la racine : %s (0 : contenu égal)\n' "$c2"
  rm -f "$O/.lt-a" "$O/.lt-b" "$O/.lb-a" "$O/.lb-b"
} > "$f"

# 4. empreintes de l'amorce et du lanceur au commit, comparées en entier au § 6 de l'addendum scellé
f="$O/geste-b3-1-empreintes-chaine-v6-au-commit.txt"
{ entete "Geste B.3, partie hors loueur, point 1 : amorce et lanceur v6 au commit de la course, comparés en entier (64 caractères) au § 6 de l'addendum scellé" "git show $C:scripts/amorce_bbis_v6.sh | sha256sum ; git show $C:scripts/lancer_bbis_v6.sh | sha256sum ; empreintes du § 6 lues dans git show $C:prereg/T0.7-etape-B-bis-v1-addendum-ecart-3-v1.md"
  ADD=$(git show "$C:prereg/T0.7-etape-B-bis-v1-addendum-ecart-3-v1.md")
  ko=0
  for p in scripts/amorce_bbis_v6.sh scripts/lancer_bbis_v6.sh tests/test_chaine_bbis_v6_v1.py; do
    obtenu=$(git show "$C:$p" | sha256sum | cut -d' ' -f1)
    lignes=$(printf '%s\n' "$ADD" | grep -c "^| \`$p\`")
    attendu=$(printf '%s\n' "$ADD" | grep "^| \`$p\`" | grep -oE '[0-9a-f]{64}')
    comp=$(git show "$C:$p.sha256" 2>/dev/null | cut -d' ' -f1)
    if [ "$lignes" = 1 ] && [ "$obtenu" = "$attendu" ]; then e=conforme; else e=ECART; ko=$((ko+1)); fi
    printf '%s\n  au commit (sha256sum)  : %s\n  addendum § 6 (%s ligne) : %s\n  compagnon .sha256 au commit : %s\n  %s\n' "$p" "$obtenu" "$lignes" "$attendu" "$comp" "$e"
  done
  printf '# écarts : %s (la troisième ligne, les essais, est donnée en plus ; le geste exige les deux scripts)\n' "$ko"
} > "$f"

# 5. ligne ADDENDUM-ECART-3-BBIS au registre voisin, au commit
f="$O/geste-b3-2-ligne-addendum-ecart-3-registre-voisin.txt"
{ entete "Geste B.3, partie hors loueur, point 2 : ligne ADDENDUM-ECART-3-BBIS au registre voisin, au commit de la course" "git show $C:registres/t07-etape-b-bis-v1-addenda-v1.md | grep -n 'ADDENDUM-ECART-3-BBIS' ; comptes"
  REG=$(git show "$C:registres/t07-etape-b-bis-v1-addenda-v1.md")
  printf '%s\n' "$REG" | grep -n 'ADDENDUM-ECART-3-BBIS'
  n_tout=$(printf '%s\n' "$REG" | grep -c 'ADDENDUM-ECART-3-BBIS')
  n_cle=$(printf '%s\n' "$REG" | grep -c '^| ADDENDUM-ECART-3-BBIS |')
  n_bonne=$(printf '%s\n' "$REG" | grep '^| ADDENDUM-ECART-3-BBIS |' | grep -c '| prereg/T0.7-etape-B-bis-v1-addendum-ecart-3-v1.md | e5604cbdce509958e1f3e3bc3a36c8d17a78c8900b5f93a2102fff9b51d07872 |')
  printf '# occurrences de la clé dans le registre : %s ; lignes à cette clé : %s ; dont chemin et empreinte e5604cbd… complets : %s\n' "$n_tout" "$n_cle" "$n_bonne"
  printf '# verdict : %s\n' "$([ "$n_tout" = 1 ] && [ "$n_cle" = 1 ] && [ "$n_bonne" = 1 ] && echo 'présente une fois, conforme' || echo ECART)"
} > "$f"

# 6. fichier de l'addendum conforme à son compagnon, au commit
f="$O/geste-b3-3-addendum-conforme-a-son-compagnon.txt"
{ entete "Geste B.3, partie hors loueur, point 3 : fichier de l'addendum conforme à son compagnon, au commit de la course" "git show $C:prereg/T0.7-etape-B-bis-v1-addendum-ecart-3-v1.md | sha256sum ; git show $C:prereg/T0.7-etape-B-bis-v1-addendum-ecart-3-v1.md.sha256"
  a=$(git show "$C:prereg/T0.7-etape-B-bis-v1-addendum-ecart-3-v1.md" | sha256sum | cut -d' ' -f1)
  b=$(git show "$C:prereg/T0.7-etape-B-bis-v1-addendum-ecart-3-v1.md.sha256")
  printf 'fichier au commit  : %s\ncompagnon au commit : %s\n' "$a" "$b"
  printf '# verdict : %s\n' "$([ "$a" = "$(printf '%s' "$b" | cut -d' ' -f1)" ] && [ "$a" = e5604cbdce509958e1f3e3bc3a36c8d17a78c8900b5f93a2102fff9b51d07872 ] && echo 'conforme (e5604cbd…, égal au registre voisin et à R-3191)' || echo ECART)"
} > "$f"
