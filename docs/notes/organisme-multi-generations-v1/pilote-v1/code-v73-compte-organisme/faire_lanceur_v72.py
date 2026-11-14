"""Écrit demonstrations/pilote_mr2_v72.py depuis pilote_mr2_v71.py : remplacements comptés, rien d'autre."""
import sys
racine = sys.argv[1]
t = open(f"{racine}/demonstrations/pilote_mr2_v71.py", encoding="utf-8").read()
i = t.index("\nTexte : `preenregistrement")
doc = '''"""Lanceur du pilote d'une génération sur la famille MR-2 — code v72 (fichier neuf, R12 ; `pilote_mr2_v71.py` reste en place,
inchangé ; C-11, C-13, C-14, C-18 ; sonde).

Changements depuis la v71 (R-2620, R-2621 : la sonde v71, jouée une fois, rend Argon « indéterminé », champ
`thoughtsTokenCount` absent aux deux appels ; le relevé ne confirme pas la configuration v11) : la **configuration v12**
(`exemples/pilote-mr2-v70/configuration-pilote-mr2-v12.json` : seules les deux consignes de la sonde changent, écrites pour faire
réfléchir), lue par `pole/proposeurs_pilote_v72.py` (la lecture de la v70 recopiée, version exigée v12) ; le **module de la sonde
v72** (`pole/sonde_pilote_v72.py` : conclusion `reflexion_observee` exigée pour Argon et Astra, refus nommé « champ de réflexion
absent », relevé `releve-sonde-pilote-v72.json`) ; les noms (version, marqueurs du bloc gelé « empreintes-du-code-pilote-v72 »,
liste des fichiers gelés : lanceur v72, lecture v72, sonde v71 et v72, configuration v12). Tout le reste est le lanceur v71 ; les
noms des pièces du pilote restent ceux de la v70 (ceux que l'audit v70, inchangé, rapatrie).

Changements de la v71, gardés (contre-lecture du différentiel v69 → v70, `f6bc1b00…` ; mot de Lazar R-2604) : le module de la
sonde v71 (A-1, A-2, a-1, a-2, a-3) ; la sous-commande `sonde` exige un registre des lancements hors dépôt (a-1 : un second
lancement sous les mêmes lignes est refusé avant tout dossier, sauf `--reprise R-NNNN` écrite au registre des décisions) ; les
faits de chaque appel sont tirés de ses pièces, et un appel parti puis arrêté sans être porté par l'arrêt est porté au relevé
(a-3) ; le relevé est lu sous la configuration et le code de l'arbre, ses faits relus de ses pièces (a-2), au bloc et au mode réel.
'''
assert t.startswith('"""Lanceur du pilote')
t = doc + t[i:]
R = [
 ('from pole import proposeurs_pilote_v70 as PR  # noqa: E402\nfrom pole import sonde_pilote_v71 as S  # noqa: E402\n',
  'from pole import proposeurs_pilote_v70 as PR  # noqa: E402\nfrom pole import proposeurs_pilote_v72 as PC  # noqa: E402\n'
  'from pole import sonde_pilote_v72 as S  # noqa: E402\n', 1),
 ('VERSION = "lanceur-pilote-mr2-v71"\nLANCEUR = "demonstrations/pilote_mr2_v71.py"\n',
  'VERSION = "lanceur-pilote-mr2-v72"\nLANCEUR = "demonstrations/pilote_mr2_v72.py"\n', 1),
 ('DEBUT_BLOC, FIN_BLOC = "<!-- empreintes-du-code-pilote-v71 : début -->", "<!-- empreintes-du-code-pilote-v71 : fin -->"',
  'DEBUT_BLOC, FIN_BLOC = "<!-- empreintes-du-code-pilote-v72 : début -->", "<!-- empreintes-du-code-pilote-v72 : fin -->"', 1),
 ('    "demonstrations/pilote_mr2_v71.py", "pole/pilote_mr2_v70.py", "pole/proposeurs_pilote_v70.py", "pole/audit_pilote_v70.py",\n'
  '    "pole/sonde_pilote_v71.py",\n',
  '    "demonstrations/pilote_mr2_v72.py", "pole/pilote_mr2_v70.py", "pole/proposeurs_pilote_v70.py", "pole/audit_pilote_v70.py",\n'
  '    "pole/proposeurs_pilote_v72.py", "pole/sonde_pilote_v71.py", "pole/sonde_pilote_v72.py",\n', 1),
 ('    "exemples/pilote-mr2-v70/configuration-pilote-mr2-v11.json",\n',
  '    "exemples/pilote-mr2-v70/configuration-pilote-mr2-v12.json",\n', 1),
 ('CONFIGURATION = os.path.join(RACINE, "exemples", "pilote-mr2-v70", "configuration-pilote-mr2-v11.json")',
  'CONFIGURATION = os.path.join(RACINE, "exemples", "pilote-mr2-v70", "configuration-pilote-mr2-v12.json")', 1),
 ('    conf, _ = PR.lire_configuration(os.path.join(racine, "exemples", "pilote-mr2-v70", "configuration-pilote-mr2-v11.json"))',
  '    conf, _ = PC.lire_configuration(os.path.join(racine, "exemples", "pilote-mr2-v70", "configuration-pilote-mr2-v12.json"))', 1),
 ('raise P.Refus("texte scellé : bloc « empreintes-du-code-pilote-v71 » absent")',
  'raise P.Refus("texte scellé : bloc « empreintes-du-code-pilote-v72 » absent")', 1),
 ('    conf, _ = PR.lire_configuration(args.configuration)\n', '    conf, _ = PC.lire_configuration(args.configuration)\n', 1),
 ('    conf, _ = PR.lire_configuration(CONFIGURATION)\n', '    conf, _ = PC.lire_configuration(CONFIGURATION)\n', 1),
]
for a, b, n in R:
    assert t.count(a) == n, (a[:80], t.count(a))
    t = t.replace(a, b)
assert "v71" not in t.split('"""', 2)[2].replace("sonde_pilote_v71.py", ""), [l for l in t.splitlines() if "v71" in l]
assert "lire_configuration" not in t.replace("PC.lire_configuration", "")
open(f"{racine}/demonstrations/pilote_mr2_v72.py", "x", encoding="utf-8").write(t)
print("écrit")
