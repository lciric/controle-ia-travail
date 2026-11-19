#!/bin/bash
# § 1.4 — module, textes scellés, fiches, registre voisin
# Commande de lecture de l'apprentissage des sondes sur la tâche (étape B bis de T0.7), version 4 ; porte, pour la forme
# seulement, le bloc « § 1.4 » de la version 3 (195207cf…). Ne supprime rien, ne réécrit aucun fichier existant.
# Lancement, ligne unique : bash /home/user/controle-ia-travail/scripts/lecture-bbis-v4/1-4-code-et-textes.sh
. "$(dirname "$0")/commun.sh"
R="$T/releve-code-et-textes.txt"; neuf "$R"
{
cd "$ARBRE" || exit 1
dire "== 1.4 module, textes, fiches, registre voisin, $(date -u +%Y-%m-%dT%H:%M:%SZ)"
while read -r s p; do
  egal "empreinte entière de $p" "$s" "$(sha256sum "$p" 2>/dev/null | cut -d' ' -f1)"
done <<'EOF'
dac9f8590784a2bf93d312128b09e89a7a21c04509700f3a3ee8c7a81a28064c src/controle_ia/t07bbis/lecture_v5.py
cd14195d396a779da954619c9a3405741fe11e2f98bf4aae3767cb87a5036ca0 registres/t07-etape-b-bis/rattachement-lecture-v5-bbis-v1.json
0ae6210f954917fecff647f45a129961c0676517381becbffe1fd5ac7b90d9eb prereg/T0.7-etape-B-bis-v1.md
f00eda8a9fb74516289a085350425d128bf5b1cf1dbc50eee32d8bbe749c78d7 prereg/T0.7-etape-B-bis-v1-addendum-ecart-v1.md
18baeac32d26ebf174c62d7a36caedeee1d5b80648c6743c21dc30d2747afd26 prereg/T0.7-etape-B-bis-v1-addendum-ecart-2-v1.md
e5604cbdce509958e1f3e3bc3a36c8d17a78c8900b5f93a2102fff9b51d07872 prereg/T0.7-etape-B-bis-v1-addendum-ecart-3-v1.md
5ef929eae8b070bc7f9d1934d487066ded34896df00dc8a9c70c91b44f0b30c4 prereg/T0.7-etape-B-bis-v1-addendum-ecart-4-v1.md
12c908732c329e61b57fe435e430464cb8033d0db708d4432076c62b4c9aa419 prereg/T0.7-etape-B-bis-v1-addendum-ecart-4-complement-v1.md
4b28535c17fe450ff1c1ecc9164d91c4c8d03354e4f4137e324f2b04390be5bb registres/t07-etape-b-bis/code-bbis-v2.json
ee362bb70c5051097dab90c7978eb550d192f8c90f313317812635884b04e469 registres/t07-etape-b-bis/code-bbis-v1.json
0a627df9ecb82c518d06c0c7ca8df4afab48a5a0da34b785c31c0da4ab41a29c src/controle_ia/t06/test_croise.py
6758b651fdcbc6d0108a03263b79ffb1e7c5d0a8be57b0f10502c1645d2b457e src/controle_ia/sondes/familles.py
1040674cb321766a0e2a7fa1e0c610384df6c4fac4109dd50c42dfbb03181ed3 src/controle_ia/sondes/evaluation.py
9dbcc55ca47b21674636f5d6c9126af15244d5ee63a9df8dee274df126c4e674 scripts/mots_et_cout_t06_v3.py
bcfe56832a1bf0c9af78b94232aedb44f179446a3871f45c27f1e3348efa7173 src/controle_ia/t06/cout.py
a3dde5509712a7a2fe072dbdec7be616d8bc9190fa1a57e649f90bfce9f05bc3 src/controle_ia/t06/lanceur.py
43a244315573eac5cc07cf90089f057ce94878851c01085e0ad64b7ef782849c src/controle_ia/harnais/run_harnais_factice.py
5d97b223206c6378295946a769c378ccfe0bd6a12372d3b25bcecb5240ab31ae src/controle_ia/environnements/propositions.py
1a5c7464523e224ca29d62ab70d83f9e7043d9bde3000ef1a4adc9ed74c8188d src/controle_ia/manifeste.py
93beeb1c8aae75463afc98e76ffb330b1e4f26be9c08ae8fee539a2df6a94ef2 src/controle_ia/scellement.py
a83c48ceba4877a2e226c3fd43669b464152f18169bb082e9b1c48ed92179439 src/controle_ia/gardes.py
EOF
egal "la fiche de rattachement nomme le module à cette empreinte" 1 "$(grep -c 'dac9f8590784a2bf93d312128b09e89a7a21c04509700f3a3ee8c7a81a28064c' registres/t07-etape-b-bis/rattachement-lecture-v5-bbis-v1.json)"
for k in ADDENDUM-ECART-1-BBIS ADDENDUM-ECART-2-BBIS ADDENDUM-ECART-3-BBIS ADDENDUM-ECART-4-BBIS ADDENDUM-ECART-4-COMPLEMENT-BBIS RATTACHEMENT-LECTURE-V5-BBIS; do
  egal "registre voisin : ligne $k, une fois" 1 "$(grep -c "^| $k |" "$VOISIN")"
  egal "registre voisin au commit de main : ligne $k, une fois" 1 "$(git show "$MAIN_INSCRIPTIONS:$VOISIN" | grep -c "^| $k |")"
done
egal "ligne du quatrième addendum à son empreinte" 1 "$(grep -c '^| ADDENDUM-ECART-4-BBIS | .*| prereg/T0.7-etape-B-bis-v1-addendum-ecart-4-v1.md | 5ef929eae8b070bc7f9d1934d487066ded34896df00dc8a9c70c91b44f0b30c4 |' "$VOISIN")"
egal "ligne du complément à son empreinte" 1 "$(grep -c '^| ADDENDUM-ECART-4-COMPLEMENT-BBIS | .*| prereg/T0.7-etape-B-bis-v1-addendum-ecart-4-complement-v1.md | 12c908732c329e61b57fe435e430464cb8033d0db708d4432076c62b4c9aa419 |' "$VOISIN")"
egal "ligne de rattachement à l'empreinte de la fiche" 1 "$(grep -c '^| RATTACHEMENT-LECTURE-V5-BBIS | .*| registres/t07-etape-b-bis/rattachement-lecture-v5-bbis-v1.json | cd14195d396a779da954619c9a3405741fe11e2f98bf4aae3767cb87a5036ca0 |' "$VOISIN")"
# les 63 fichiers de la fiche de code, par programme (la fiche est un fichier de code, non de résultat)
egal "fichiers de la fiche de code d'empreinte autre, ou absents" "63 0" "$("$PY" -c '
import hashlib, json, pathlib
f = json.load(open("registres/t07-etape-b-bis/code-bbis-v2.json"))["fichiers"]
print(len(f), sum(1 for p, s in f.items() if not pathlib.Path(p).is_file() or hashlib.sha256(pathlib.Path(p).read_bytes()).hexdigest() != s))')"
egal "fichiers sous src ou pièce « mots et coût » modifiés ou retirés depuis le commit de la fiche" 0 "$(git diff --name-status "$C_FICHE" HEAD -- src scripts/mots_et_cout_t06_v3.py | grep -c -v '^A')"
for v in numpy==2.4.6 scipy==1.17.1 torch==2.14.1; do egal "version figée $v dans requirements-cpu.txt" 1 "$(grep -c -x "$v" requirements-cpu.txt)"; done
conclure
} 2>&1 | tee "$R"
