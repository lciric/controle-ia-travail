"""Dérive le lanceur v4 du quatrième pilote descriptif du lanceur v3 (`lancer_pilote4_gemini_v3.sh`, 73d318b9…), par
remplacements exacts, chacun au nombre d'occurrences attendu — sur la contre-lecture 1 du texte du pilote 4
(`prereg/contre-lectures/pilote4-gemini-organisme-v1-cl1.md`) :

- P4C1-02 (option c) : `--temps-max-conception 900` (chaque ronde de conception bornée à 900 s de travail, au lieu des
  2 400 s héritées de `--temps-max` ; la garde du noyau exige au moins 885 s pour 6 recherches et 3 téléchargements) ;
  le temps par ronde du manifeste est recopié dans la vérification après départ du `LANCEMENT.md` ;
- P4C1-02 (option d) : un **minuteur** — à `ECHEANCE_STOP_S` = 5 700 s du départ du lanceur, si la course tourne encore et
  que son manifeste est écrit, il pose `STOP` dans `course/` : le noyau s'arrête avant la ronde ou la génération suivante,
  celle en cours finit, l'archive se ferme comme à la fin d'une course ; il est lancé en fond et arrêté par son PID dès la
  fin du processus de la course (R10) ; l'échéance est fixe en réel (la variable d'essai `ESSAI_ECHEANCE_STOP_S` y est
  refusée) et réglable en simulation seulement ;
- P4C1-14 (b) : en-tête (version, nom du lanceur dans l'usage, texte v2, commentaire du plafond du GO).

Rien d'autre ne change : objets, banque, gardes, environnement, fermeture, liste fermée sont la ligne du lanceur v3.

Usage : python3 -I deriver_lanceur_pilote4_v4.py LANCEUR_V3 SORTIE
Refuse si l'empreinte du lanceur v3 n'est pas 73d318b9…, si une occurrence n'est pas au nombre attendu, si un reste
interdit subsiste, ou si SORTIE existe (R12).
"""
import hashlib, pathlib, sys

SHA_V3 = "73d318b929ca03b98a5d9469271afd4348c4e448fcec1f5ed8aa2edd7c2c72fa"
src, sortie = pathlib.Path(sys.argv[1]), pathlib.Path(sys.argv[2])
if sortie.exists():
    sys.exit(f"refus : {sortie} existe déjà (R12)")
b = src.read_bytes()
if hashlib.sha256(b).hexdigest() != SHA_V3:
    sys.exit("refus : le lanceur source n'est pas la v3 73d318b9…")
t = b.decode("utf-8")

MINUTEUR = '''note "- PID de la course : $PID (arrêt humain par ce PID seulement, R10 ; STOP dans course/ : arrêt avant la ronde ou la génération suivante, celle en cours finit)"
# P4C1-02 : minuteur, lancé en fond et arrêté par son PID dès la fin du processus de la course (R10). À l'échéance, si la
#   course tourne encore et que son manifeste est écrit, il pose STOP dans course/ (le noyau le lit avant chaque ronde et
#   chaque génération, `_doit_arreter`) ; la fermeture qui suit est celle d'une course finie (étape 8a).
minuteur() {
  local fin=$(( DEBUT_LANCEUR_S + ECHEANCE_STOP_S )) s
  trap 'exit 0' TERM
  while kill -0 "$PID" 2>/dev/null; do
    if [ -f "$PILOTE/course/manifeste-run.json" ] && [ "$(date +%s)" -ge "$fin" ]; then
      : > "$PILOTE/course/STOP"
      note "- minuteur : STOP posé dans course/ à $(date -u +%Y-%m-%dT%H:%M:%SZ) ($ECHEANCE_STOP_S s après le départ du lanceur) : la course s'arrête avant la ronde ou la génération suivante"
      exit 0
    fi
    sleep 1 & s=$!
    wait "$s" || true
  done
}
minuteur & MINUTEUR=$!
note "- minuteur : PID $MINUTEUR ; échéance $(date -u -d "@$(( DEBUT_LANCEUR_S + ECHEANCE_STOP_S ))" +%Y-%m-%dT%H:%M:%SZ), $ECHEANCE_STOP_S s après le départ du lanceur ($(date -u -d "@$DEBUT_LANCEUR_S" +%Y-%m-%dT%H:%M:%SZ))"
set +e; wait "$PID"; CODE=$?; set -e
kill "$MINUTEUR" 2>/dev/null || true
wait "$MINUTEUR" 2>/dev/null || true
if [ -f "$PILOTE/course/STOP" ]; then
  note "- minuteur : STOP du minuteur présent dans course/ à la fin de la course (raison d'arrêt : événement « arret » de l'extrait) — liste d'arrêt du texte"
else
  note "- minuteur arrêté par son PID ($MINUTEUR) à la fin de la course : STOP non posé"
fi
'''

ECHEANCE = '''USD_COURSE=60   # par course ; deux courses : 120 USD au plus (GO-2026-10-25-02, étendu par un mot direct de Lazar dans la session de session-depot : 155 USD au plus pour l'ensemble du GO)
# P4C1-02 : minuteur. STOP posé dans course/ à ECHEANCE_STOP_S s du départ du lanceur si la course tourne encore (la
#   commande de fond de session-depot est bornée à 7 200 s) ; fixe en réel ; réglable en simulation (ESSAI_ECHEANCE_STOP_S)
ECHEANCE_STOP_S=5700
if [ "$MODE" = simulation ] && [ -n "${ESSAI_ECHEANCE_STOP_S:-}" ]; then
  case "$ESSAI_ECHEANCE_STOP_S" in *[!0-9]*) refus_tot "ESSAI_ECHEANCE_STOP_S doit être un entier (secondes)";; esac
  ECHEANCE_STOP_S="$ESSAI_ECHEANCE_STOP_S"
fi
'''

remplacements = [
    # en-tête (P4C1-14 b)
    ("# une course par appel (COURSE=v5-3, puis COURSE=v6-1) — v1, dérivée du lanceur v2 du pilote 3\n",
     "# une course par appel (COURSE=v5-3, puis COURSE=v6-1) — v4 : le lanceur v3 (73d318b9…) par `deriver_lanceur_pilote4_v4.py`\n"
     "# (borne de 900 s par ronde de conception ; minuteur qui pose STOP à 5 700 s du départ ; en-tête ; écart consigné dans\n"
     "# `diff-lanceur-pilote4-v3-vers-v4.txt`), le v3 étant lui-même dérivé du lanceur v2 du pilote 3\n", 1),
    ("# Texte : `essaim-m3-refonte-v1/prereg/pilote4-gemini-organisme-v1.md` (ou la version qui le remplace et cite ce\n",
     "# Texte : `essaim-m3-refonte-v1/prereg/pilote4-gemini-organisme-v2.md` (ou la version qui le remplace et cite ce\n", 1),
    ("#       bash lancer_pilote4_gemini_v1.sh\n", "#       bash lancer_pilote4_gemini_v4.sh\n", 1),
    # origine du minuteur
    ("set +x\nrefus_tot() {", "set +x\nDEBUT_LANCEUR_S=\"$(date +%s)\"   # départ du lanceur : origine du minuteur (P4C1-02)\nrefus_tot() {", 1),
    # variable d'essai refusée en réel
    ("ESSAI_PASSERELLE_PY ESSAIM_M3_ESPACE; do", "ESSAI_PASSERELLE_PY ESSAIM_M3_ESPACE ESSAI_ECHEANCE_STOP_S; do", 1),
    # échéance (et commentaire du plafond, P4C1-14 b)
    ("USD_COURSE=60   # par course ; deux courses : 120 USD au plus (GO-2026-10-25-02, mot direct de Lazar dans la session de session-depot)\n",
     ECHEANCE, 1),
    # borne des rondes (P4C1-02 c)
    ("--rondes-conception-max 6 --usd-max-conception 3 --parallele-max 8",
     "--rondes-conception-max 6 --usd-max-conception 3 --temps-max-conception 900 --parallele-max 8", 1),
    ('" ; dépense du noyau " + str(r.get("depense_totale_usd"))',
     '" ; temps par ronde de conception " + str((m.get("budget_conception") or {}).get("temps_max_s")) + " s ; dépense du noyau " + str(r.get("depense_totale_usd"))', 1),
    # minuteur (P4C1-02 d)
    ('note "- PID de la course : $PID (arrêt humain par ce PID seulement, R10 ; STOP dans course/ : arrêt à la fin de la génération)"\n'
     'set +e; wait "$PID"; CODE=$?; set -e\n', MINUTEUR, 1),
]
for ancien, nouveau, n in remplacements:
    k = t.count(ancien)
    if k != n:
        sys.exit(f"refus : {k} occurrence(s) au lieu de {n} pour : {ancien[:90]!r}")
    t = t.replace(ancien, nouveau)
for motif in ("lancer_pilote4_gemini_v1.sh", "pilote4-gemini-organisme-v1.md", "— v1, dérivée", "arrêt à la fin de la génération)\""):
    if motif in t:
        sys.exit(f"refus : motif restant après dérivation : {motif}")
for motif, n in (("--temps-max-conception 900", 1), ("ECHEANCE_STOP_S=5700", 1), ("kill \"$MINUTEUR\"", 1)):
    if t.count(motif) != n:
        sys.exit(f"refus : {motif} présent {t.count(motif)} fois au lieu de {n}")
sortie.write_text(t, encoding="utf-8")
print(f"lanceur écrit : {sortie.name} {hashlib.sha256(sortie.read_bytes()).hexdigest()} ; {len(remplacements)} remplacements")
