def edit(p, reps):
    s = open(p, encoding='utf-8').read()
    for a, b in reps:
        assert s.count(a) == 1, (p, a[:80])
        s = s.replace(a, b)
    open(p, 'w', encoding='utf-8').write(s)


edit('scripts/construire_branche_entree_ligne_1_bras_a_v3.py', [
    ('''"""Construit la branche d'entrée de la machine autonome de la ligne 1 de carte du bras A, version 2 (23 novembre 2026 ;
la version 1, `scripts/construire_branche_entree_ligne_1_bras_a_v1.py`, reste telle quelle, jamais jouée).

Seule différence avec la version 1 : la branche porte aussi **l'amorce complète de la machine**
(`scripts/amorce_ligne_1_bras_a_v2.sh`), prise''', '''"""Construit la branche d'entrée de la machine autonome de la ligne 1 de carte du bras A, version 3 (23 novembre 2026 ;
les versions 1 et 2 restent telles quelles, jamais jouées).

Différences avec la version 2 (contre-lecture de la machine v2) : l'amorce complète portée est la v3
(`scripts/amorce_ligne_1_bras_a_v3.sh`) ; `git fetch origin main` avant de prendre les quatre fichiers du guide à
`origin/main` (m7 ; `--sans-fetch` pour les essais hors réseau).

Différence de la version 2 avec la version 1 : la branche porte aussi **l'amorce complète de la machine**, prise'''),
    ('''Usage : `PYTHONPATH=src python scripts/construire_branche_entree_ligne_1_bras_a_v1.py [--pousser]`''',
     '''Usage : `PYTHONPATH=src python scripts/construire_branche_entree_ligne_1_bras_a_v3.py [--pousser]`'''),
    ('''AMORCE_COMPLETE = "scripts/amorce_ligne_1_bras_a_v2.sh"''', '''AMORCE_COMPLETE = "scripts/amorce_ligne_1_bras_a_v3.sh"'''),
    ('''        pousse = bool(_git_sortie(racine, "branch", "-r", "--contains", commit).strip())
''', '''        pousse = bool(_git_sortie(racine, "branch", "-r", "--contains", commit).strip())
        if not a.sans_fetch and a.reference_du_guide.startswith("origin/"):
            f = _git(racine, "fetch", "-q", "origin", a.reference_du_guide.split("/", 1)[1], capture_output=True)
            if f.returncode != 0:
                raise Refus(f"git fetch de {a.reference_du_guide} en échec (code {f.returncode})")
'''),
    ('''    p.add_argument("--pousser", action="store_true"''', '''    p.add_argument("--sans-fetch", action="store_true", help="essais hors réseau : pas de fetch avant le guide")
    p.add_argument("--pousser", action="store_true"'''),
])
edit('scripts/lanceur_machine_ligne_1_bras_a_v3.py', [
    ('''"""Lanceur de la machine autonome de la ligne 1 de carte du bras A, version 2 (23 novembre 2026 ; la version 1,
`scripts/lanceur_machine_ligne_1_bras_a_v1.py`, reste telle quelle, jamais jouée).''', '''"""Lanceur de la machine autonome de la ligne 1 de carte du bras A, version 3 (23 novembre 2026 ; les versions 1 et 2
restent telles quelles, jamais jouées).

Différences avec la version 2 (contre-lecture de la machine v2) : amorce d'appel v2
(`scripts/amorce_appel_ligne_1_bras_a_v2.sh`) et amorce complète v3 (`scripts/amorce_ligne_1_bras_a_v3.sh`) ; la
commande imprimée porte `${GH_TOKEN:?}` et `${HF_TOKEN:?}` (un secret vide fait échouer la commande chez la mère, au
lieu d'un démarrage perdu), et sa sortie passe par la sous-commande `masquer` de ce programme (m8).

Version 2 :'''),
    ('''`--onstart scripts/amorce_appel_ligne_1_bras_a_v1.sh` (amorce d'appel''', '''`--onstart <amorce d'appel>` (amorce d'appel'''),
    ('''`AMORCE_SHA256` est l'empreinte de l'**amorce complète** `scripts/amorce_ligne_1_bras_a_v2.sh`, portée''',
     '''`AMORCE_SHA256` est l'empreinte de l'**amorce complète**, portée'''),
    ('''  --env "-e GH_TOKEN=$GH_TOKEN -e HF_TOKEN=$HF_TOKEN -e …" --onstart scripts/amorce_ligne_1_bras_a_v1.sh …`) ; les''',
     '''  --env "-e GH_TOKEN=${GH_TOKEN:?} -e HF_TOKEN=${HF_TOKEN:?} -e …" --onstart scripts/amorce_appel_ligne_1_bras_a_v2.sh …
  2>&1 | … masquer`) ; les'''),
    ('''AMORCE = "scripts/amorce_appel_ligne_1_bras_a_v1.sh"
AMORCE_COMPLETE = "scripts/amorce_ligne_1_bras_a_v2.sh"''', '''AMORCE = "scripts/amorce_appel_ligne_1_bras_a_v2.sh"
AMORCE_COMPLETE = "scripts/amorce_ligne_1_bras_a_v3.sh"
CE_PROGRAMME = "scripts/lanceur_machine_ligne_1_bras_a_v3.py"'''),
    ('''    env = " ".join(["-e GH_TOKEN=$GH_TOKEN", "-e HF_TOKEN=$HF_TOKEN",''',
     '''    env = " ".join(["-e GH_TOKEN=${GH_TOKEN:?}", "-e HF_TOKEN=${HF_TOKEN:?}",'''),
    ('''            f"--cancel-unavail --raw --env \\"{env}\\" --onstart {amorce}")''',
     '''            f"--cancel-unavail --raw --env \\"{env}\\" --onstart {amorce} 2>&1 | PYTHONPATH=src .venv/bin/python "
            f"{CE_PROGRAMME} masquer")'''),
    ('''        return {"creation": sous_creation, "etat": sous_etat, "verification": sous_verification}[a.sous](a)''',
     '''        return {"creation": sous_creation, "etat": sous_etat, "verification": sous_verification,
                "masquer": sous_masquer}[a.sous](a)'''),
    ('''def main(argv=None) -> int:''', '''def sous_masquer(a) -> int:
    """Recopie l'entrée standard masquée (sortie de la commande de création du loueur, `--raw`)."""
    for ligne in sys.stdin:
        sys.stdout.write(masquer(ligne))
    return 0


def main(argv=None) -> int:'''),
    ('''    e = s.add_parser("etat")''', '''    s.add_parser("masquer")
    e = s.add_parser("etat")'''),
])
