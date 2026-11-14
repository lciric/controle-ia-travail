"""Écrit demonstrations/pilote_mr2_v73.py depuis pilote_mr2_v72.py : remplacements comptés (décision de la mère sur PO-015,
R-2690 : le bloc gelé nomme les relais par leurs clés, aucun identifiant de modèle)."""
import sys
racine = sys.argv[1]
t = open(f"{racine}/demonstrations/pilote_mr2_v72.py", encoding="utf-8").read()
i = t.index("\nChangements de la v71, gardés")
doc = '''"""Lanceur du pilote d'une génération sur la famille MR-2 — code v73 (fichier neuf, R12 ; `pilote_mr2_v72.py` reste en place,
inchangé ; C-11, C-13, C-14, C-18 ; sonde).

Changement depuis la v72 (décision de la mère sur PO-015, R-2690 : « code v73 dont le bloc gelé nomme les relais par leurs clés,
aucun identifiant de modèle Claude dans les pièces ») : **le bloc gelé ne recopie plus l'identifiant du modèle** de chaque
proposeur ; ses lignes « borne-de-sortie » nomment le proposeur par sa clé de configuration (`fable52`, `opus55`, `argon`,
`astra`) ; une ligne « identite-des-proposeurs » dit que les identifiants sont ceux de la configuration, dont l'empreinte du fichier
est au bloc (l'identité reste donc gelée par l'empreinte) ; marqueurs « empreintes-du-code-pilote-v73 » ; liste des fichiers gelés
avec le lanceur v73. **Sous-commande neuve `sonde-un`** (GO-2026-11-14-02, R-2694) : sonde du seul relais Astra sous une
ligne à part de 2 USD (voir `sonde_un`). Tout le reste est le lanceur v72 (configuration v12, lecture v72, sonde v72).

Changements de la v72, gardés : la configuration v12 (consignes de la sonde écrites pour faire réfléchir), lue par
`pole/proposeurs_pilote_v72.py` ; le module de la sonde v72 (`reflexion_observee`, refus nommé « champ de réflexion absent » pour un
appel abouti, relevé `releve-sonde-pilote-v72.json`).
'''
assert t.startswith('"""Lanceur du pilote')
t = doc + t[i:]
R = [
 ('VERSION = "lanceur-pilote-mr2-v72"\nLANCEUR = "demonstrations/pilote_mr2_v72.py"\n',
  'VERSION = "lanceur-pilote-mr2-v73"\nLANCEUR = "demonstrations/pilote_mr2_v73.py"\n', 1),
 ('"<!-- empreintes-du-code-pilote-v72 : début -->", "<!-- empreintes-du-code-pilote-v72 : fin -->"',
  '"<!-- empreintes-du-code-pilote-v73 : début -->", "<!-- empreintes-du-code-pilote-v73 : fin -->"', 1),
 ('    "demonstrations/pilote_mr2_v72.py", "pole/pilote_mr2_v70.py",', '    "demonstrations/pilote_mr2_v73.py", "pole/pilote_mr2_v70.py",', 1),
 ('        lignes.append(f"borne-de-sortie {nom} {p[\'modele\']} {p[\'borne_sortie_jetons\']} jetons ; plafond de session "',
  '        lignes.append(f"borne-de-sortie {nom} {p[\'borne_sortie_jetons\']} jetons ; plafond de session "', 1),
 ('    lignes.append(f"octets-entree-max {conf[\'octets_entree_max\']}")\n',
  '    lignes.append("identite-des-proposeurs celle de la configuration (clé modele de chaque proposeur), gelée par l\'empreinte du "\n'
  '                  "fichier de configuration ci-dessous ; non recopiée ici (R-2690)")\n'
  '    lignes.append(f"octets-entree-max {conf[\'octets_entree_max\']}")\n', 1),
 ('raise P.Refus("texte scellé : bloc « empreintes-du-code-pilote-v72 » absent")',
  'raise P.Refus("texte scellé : bloc « empreintes-du-code-pilote-v73 » absent")', 1),
]
for a, b, n in R:
    assert t.count(a) == n, (a[:80], t.count(a))
    t = t.replace(a, b)
assert "p['modele']" not in t.split("def bloc_gele", 1)[1].split("def verifier_bloc_du_texte", 1)[0]
sonde_un = open("/home/user/arbre-organisme-co/sources-essais/sonde_un_v73.py.txt", encoding="utf-8").read()
ancre = "\n\ndef mesurer(args):"
assert t.count(ancre) == 1
t = t.replace(ancre, sonde_un.rstrip("\n") + "\n" + ancre)
for a2, b2 in (('    x = s.add_parser("jouer")\n',
                '    x = s.add_parser("sonde-un")\n    x.add_argument("--proposeur", required=True)\n    x.add_argument("--go-sonde", required=True)\n'
                '    x.add_argument("--registre-go", required=True)\n    x.add_argument("--registre-lancements", required=True)\n'
                '    x.add_argument("--sortie", required=True)\n    x.add_argument("--reprise", default=None)\n'
                '    x.add_argument("--registre-decisions", default=None)\n    x = s.add_parser("jouer")\n'),
               ('        elif args.commande == "jouer":\n', '        elif args.commande == "sonde-un":\n            return sonde_un(args)\n        elif args.commande == "jouer":\n'),
               ('  jouer   --mode a_blanc|reel', '  sonde-un --proposeur astra --go-sonde GO --registre-go R --registre-lancements FICHIER (hors dépôt) --sortie DOSSIER\n'
                '          [--reprise R-NNNN --registre-decisions D]   payante : un seul relais, une ligne à part (v73)\n  jouer   --mode a_blanc|reel')):
    assert t.count(a2) == 1, a2
    t = t.replace(a2, b2)
open(f"{racine}/demonstrations/pilote_mr2_v73.py", "x", encoding="utf-8").write(t)
print("écrit")
