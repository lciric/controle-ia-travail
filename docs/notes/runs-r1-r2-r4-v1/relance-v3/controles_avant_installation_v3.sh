#!/usr/bin/env bash
# Contrôles d'avant l'installation du script d'instance v3 et gardes de citation du module, rejoués sur une copie (hors
# réseau, processeur, jetons factices) : dépôt jetable tiré du commit du code (git archive de src, scripts, tests), plus
# l'addendum v3 tel qu'il est dans l'arbre, la configuration v5, la table v3 et le parent, scellés **dans la copie
# seulement** ; dépôt nu local servant de « dépôt distant ». Le vrai script, en mode réel et avec son préenregistrement
# par défaut, passe ses contrôles d'avant l'installation et sa poussée initiale, puis s'arrête à `nvidia-smi` absent (cas
# sain, code 127) ; six artefacts doivent l'arrêter avant l'installation (code 2). Puis, dans l'arbre lui-même, les gardes
# de citation de `rejeu_activations_v3.executer` (configuration, parent, entropie, commit du code), le chargement de la
# table par le module, le compte de chaque libellé et `prereg.problemes`.
#
#   bash controles_avant_installation_v3.sh <arbre de la branche prep/r1-relance-v3> <dossier temporaire neuf>
set -u
ARBRE=$(cd "$1" && pwd); W=$2
CODE=f921fcec10539f1565fab410624a926efdfec12e
PY=/home/user/controle-ia-travail/.venv/bin/python
TEXTE=prereg/R1-addendum-relance-v3.md
mkdir "$W" || exit 1
export GIT_TERMINAL_PROMPT=0 GIT_AUTHOR_NAME=essai GIT_AUTHOR_EMAIL=essai@example.invalid GIT_COMMITTER_NAME=essai \
       GIT_COMMITTER_EMAIL=essai@example.invalid
echo "addendum v3 lu dans l'arbre : sha256 $(sha256sum "$ARBRE/$TEXTE" | cut -c1-64)"
echo "commit du code : $CODE ; arbre : HEAD $(git -C "$ARBRE" rev-parse HEAD)"
S="$W/source"; mkdir -p "$S/prereg"
git -C "$ARBRE" -c http.proxy=http://127.0.0.1:9 archive "$CODE" src scripts tests pyproject.toml .gitignore | tar -x -C "$S"
for f in "$TEXTE" prereg/R1-rejeu-config-v5.json prereg/R1-table-tokenisation-v3.json \
         prereg/R1-table-tokenisation-v3.json.sha256 prereg/R1-R2-rejeu-p3-v1.md prereg/R1-R2-rejeu-p3-v1.md.sha256 \
         prereg/R1-rejeu-config-v4.json prereg/R1-table-tokenisation-v2.json prereg/R1-table-tokenisation-v2.json.sha256; do
    cp "$ARBRE/$f" "$S/$f"
done
sceller() { (cd "$S" && PYTHONDONTWRITEBYTECODE=1 PYTHONPATH=src "$PY" -m controle_ia.scellement sceller "$@" >/dev/null); }
sceller "$TEXTE" prereg/R1-rejeu-config-v5.json prereg/R1-rejeu-config-v4.json
git -C "$S" init -q -b main && git -C "$S" add -A && git -C "$S" commit -q -m "copie : code $CODE, addendum v3 et configuration v5 scellés dans la copie"
SAIN=$(git -C "$S" rev-parse HEAD)
# artefacts : chacun sur une branche de la copie, à partir du cas sain
artefact() {   # nom, puis commande qui modifie la copie
    local nom=$1; shift
    git -C "$S" checkout -q -b "a-$nom" "$SAIN"
    (cd "$S" && eval "$*")
    git -C "$S" add -A && git -C "$S" commit -q -m "artefact $nom"
    git -C "$S" rev-parse HEAD > "$W/commit-$nom"
}
artefact texte-non-scelle 'rm prereg/R1-addendum-relance-v3.md.sha256'
artefact tests-attendus-deux-fois "printf -- '- Tests attendus : \`1\`\n' >> $TEXTE && rm $TEXTE.sha256 && PYTHONPATH=src $PY -m controle_ia.scellement sceller $TEXTE >/dev/null"
artefact configuration-v4-citee "sed -i 's#^- Chemin de la configuration du rejeu : .*#- Chemin de la configuration du rejeu : \`prereg/R1-rejeu-config-v4.json\`#' $TEXTE && rm $TEXTE.sha256 && PYTHONPATH=src $PY -m controle_ia.scellement sceller $TEXTE >/dev/null"
artefact table-v2-citee "sed -i 's#^- Chemin de la configuration du rejeu : .*#- Chemin de la configuration du rejeu : \`prereg/R1-rejeu-config-v4.json\`#; s#^- Chemin de la table de tokenisation : .*#- Chemin de la table de tokenisation : \`prereg/R1-table-tokenisation-v2.json\`#' $TEXTE && rm $TEXTE.sha256 && PYTHONPATH=src $PY -m controle_ia.scellement sceller $TEXTE >/dev/null"
artefact empreinte-de-table-fausse "$PY -c \"import json; p='prereg/R1-rejeu-config-v5.json'; c=json.load(open(p)); c['table_tokenisation_sha256']='0'*64; open(p,'w').write(json.dumps(c, sort_keys=True, indent=1))\" && rm prereg/R1-rejeu-config-v5.json.sha256 && PYTHONPATH=src $PY -m controle_ia.scellement sceller prereg/R1-rejeu-config-v5.json >/dev/null"
artefact sceau-de-table-faux "printf '%064d  R1-table-tokenisation-v3.json\n' 0 > prereg/R1-table-tokenisation-v3.json.sha256"
git -C "$S" checkout -q main
git clone -q --bare "$S" "$W/depot.git"
for b in $(git -C "$S" for-each-ref --format='%(refname:short)' refs/heads/ | grep '^a-'); do git -C "$S" push -q "$W/depot.git" "$b"; done
jouer() {   # nom, commit
    local nom=$1 commit=$2 code
    env -i PATH="$PATH" HOME="$W" LANG=C.UTF-8 GIT_TERMINAL_PROMPT=0 MODE=reel COMMIT="$commit" HF_TOKEN=jouet \
        GH_TOKEN=jouet DEPOT_URL="file://$W/depot.git" TRAVAIL="$W/inst-$nom" BRANCHE="calcul/essai-avant-$nom" \
        bash "$S/scripts/r1_relance_instance_v3.sh" > "$W/$nom.log" 2>&1
    code=$?
    echo "== $nom : code $code"
    grep -E "addendum lu|sceau|introuvable|non conforme|absent|poussée avant|ARRÊT|sortie imprévue" "$W/inst-$nom/journal.txt" \
        | sed -E 's/^[0-9T:-]+Z //' | head -4
}
jouer sain "$SAIN"
for n in texte-non-scelle tests-attendus-deux-fois configuration-v4-citee table-v2-citee empreinte-de-table-fausse \
         sceau-de-table-faux; do
    jouer "$n" "$(cat "$W/commit-$n")"
done
echo "== gardes de citation du module et chargement de la table, dans l'arbre"
(cd "$ARBRE" && HTTPS_PROXY=http://127.0.0.1:9 https_proxy=http://127.0.0.1:9 PYTHONDONTWRITEBYTECODE=1 PYTHONPATH=src \
    "$PY" - "$TEXTE" <<'PY'
import json, re, sys
from pathlib import Path
from controle_ia.harnais.validation_reelle import COMMIT_CITE, ENTROPIE_CITEE, exiger_code_cite
from controle_ia.prereg import problemes
from controle_ia.runs_nuit import rejeu_activations_v3 as rc
from controle_ia.scellement import verifier
texte_p = sys.argv[1]
t = Path(texte_p).read_text(encoding="utf-8")
c = json.loads(Path("prereg/R1-rejeu-config-v5.json").read_text(encoding="utf-8"))
rc.exiger_config(c)
canon = rc.empreinte_config(c)
print("configuration v5 : empreinte canonique", canon, "; citée :", rc.CONFIG_CITEE.format(canon) in t,
      "; occurrences du libellé :", t.count("Configuration du rejeu (empreinte canonique) : `"))
print("parent : sceau", verifier(c["chemin_prereg_parent"]) == c["prereg_parent_sha256"], "; empreinte citée :",
      c["prereg_parent_sha256"] in t)
e = ENTROPIE_CITEE.findall(t)
print("entropie citée :", e)
print("commit du code cité :", COMMIT_CITE.findall(t), "; arbre gelé = commit cité :", exiger_code_cite(Path("."), Path(texte_p)))
for lib in ("Tests attendus", "Chemin de la configuration du rejeu", "Chemin de la table de tokenisation",
            "Chemin du préenregistrement parent"):
    lignes = [x for x in t.splitlines() if (lib + " : `") in x]
    print(f"libellé « {lib} » : {len(lignes)} ligne(s) ; valeur", re.sub(r".*" + re.escape(lib) + r" : `([^`]*)`.*", r"\1", lignes[0]) if lignes else None)
tab = rc.charger_table(c["chemin_table_tokenisation"], c["table_tokenisation_sha256"])
print("table chargée par rejeu_activations_v3.charger_table : version", tab["version"], ";", len(tab["episodes"]), "entrées ;",
      "non_resolu :", tab["comptes"]["non_resolu"])
print("prereg.problemes :", problemes(texte_p))
PY
) 2>&1
