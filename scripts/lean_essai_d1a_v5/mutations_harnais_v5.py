"""Mutations du harnais Lean v5 sur des copies (CLC4-08 de la contre-lecture machine de la v4 `918662a7…`, R-2323).

Même méthode que la v4 : copie neuve par mutation, remplacement exact présent une seule fois (sinon arrêt), **import tracé**
vers la copie, `pytest -o pythonpath=<copie>/src <copie>/tests` sans `PYTHONPATH` hérité, délai de 180 s ; en plus : aucun
jeton de Hetzner dans l'environnement des enfants, et taille de fichier bornée (100 Mo) pour qu'aucune boucle n'emplisse le
disque. Seuls les essais v5 sont lancés : chaque mutation doit être tuée par eux. Au moins une mutation par correction v5
(CLC4-01, -03, -05, -06, -07, procédure du poste local), et une par mutation de la contre-lecture (n1 à n20), n3, n10 et n18 en
tête ; celles qui portent sur une ligne de la v4 encore utilisée par la v5 (n5, n10, n14 dans `hetzner_v4`, n19 dans
`minuterie_v4`) mutent cette ligne.

Usage : python -I -B mutations_harnais_v5.py RACINE_DE_L_ARBRE DOSSIER_DE_TRAVAIL ; code 0 si toutes les mutations sont tuées.
"""
from __future__ import annotations

import json
import os
import resource
import shutil
import subprocess
import sys
from pathlib import Path

ESSAIS = ["tests/test_lean_essai_minuterie_v5.py"]
M, H, H4, M4 = "minuterie_v5", "hetzner_v5", "hetzner_v4", "minuterie_v4"

MUTATIONS = [
    # -- CLC4-08 : survivantes de la contre-lecture, n3, n10, n18 en tête --------------------------------------------------------
    ("n3", "minuterie non lancée : serveur non détruit", M,
     "        detruire_par_identifiant(client, ident, NOM_MACHINE, journal, dormir, essais_max=essais_max, solder=solder)\n"
     "        raise GardeArret(f\"minuterie non armée", "        raise GardeArret(f\"minuterie non armée"),
    ("n10", "un serveur du même nom existe : contrôle retiré", H4,
     "        if any(n == nom for _, n in self.inventaire()):\n            raise GardeArret(f\"un serveur nommé {nom!r} existe "
     "déjà : un seul serveur par pas\")\n        corps", "        corps"),
    ("n18a", "seconde machine admise (création)", M,
     "    if anterieures:\n        raise GardeArret(f\"seconde machine sous {go_id} refusée sans exception : {anterieures} ; une "
     "seconde machine passe par \"\n                         \"une consigne neuve de la mère\")\n    taux = ",
     "    if False:\n        raise GardeArret(f\"seconde machine sous {go_id} refusée sans exception : {anterieures} ; une "
     "seconde machine passe par \"\n                         \"une consigne neuve de la mère\")\n    taux = "),
    ("n18b", "seconde machine admise (préparation)", M,
     "    if anterieures:\n        raise GardeArret(f\"seconde machine sous {go_id} refusée sans exception : {anterieures} ; une "
     "seconde machine passe par \"\n                         \"une consigne neuve de la mère\")\n    if heure_limite_creation.tzinfo",
     "    if False:\n        raise GardeArret(f\"seconde machine sous {go_id} refusée sans exception : {anterieures} ; une "
     "seconde machine passe par \"\n                         \"une consigne neuve de la mère\")\n    if heure_limite_creation.tzinfo"),
    ("n1", "contrôle du nom avant destruction (tri)", M, "    autres = [(i, n) for i, n in trouves if n != NOM_MACHINE]",
     "    autres = []"),
    ("n5", "statut 500 traité comme refus", H4, "        if 400 <= statut < 500:", "        if 400 <= statut <= 500:"),
    ("n8", "intention non exigée avant l'appel", M, "_ajouter_journal_creations(chemins[\"creations\"], entree, exige=True)",
     "_ajouter_journal_creations(chemins[\"creations\"], entree, exige=False)"),
    ("n9a", "déjà-dépensé passé à la minuterie = 0 (création)", M, "taux=taux, deja=deja[\"retenu\"],",
     "taux=taux, deja=0.0,"),
    ("n9b", "déjà-dépensé perdu dans les arguments", M, "\"--deja-depense-usd\", repr(float(deja)),",
     "\"--deja-depense-usd\", \"0.0\","),
    ("n12", "inventaire de contrôle après detruire --pas", M, "    if restants:\n        raise GardeArret(f\"serveurs {restants} encore",
     "    if False:\n        raise GardeArret(f\"serveurs {restants} encore"),
    ("n14", "pagination des étiquettes fixes", H4,
     "if d.get(\"meta\", {}).get(\"pagination\", {}).get(\"next_page\"):\n            raise GardeArret(\"plus de 50",
     "if False:\n            raise GardeArret(\"plus de 50"),
    ("n15a", "taux passé à la minuterie = 1,0 (création)", M, "echeance_h=echeance_h, taux=taux, deja=",
     "echeance_h=echeance_h, taux=1.0, deja="),
    ("n15b", "taux perdu dans les arguments", M, "\"--taux-usd-eur\", repr(float(taux)),", "\"--taux-usd-eur\", \"1.0\","),
    ("n16", "devis non revérifié au démarrage", M, "            verifier_devis(prix, pas_long, deja)\n", ""),
    ("n17", "recherche par nom retirée de detruire --pas", M, "    trouves = sorted(set(par_etiquettes) | set(par_nom))",
     "    trouves = sorted(set(par_etiquettes))"),
    ("n19", "jeton réutilisé admis", M4, "    if chemin.exists():\n        raise GardeArret(f\"{chemin} existe déjà : jeton réutilisé\")",
     "    pass"),
    ("n20", "plafond sans le déjà-dépensé", M, "    reste = PLAFONDS_MACHINE[pas_long] - deja", "    reste = PLAFONDS_MACHINE[pas_long]"),
    # -- CLC4-01 : démarrage de la minuterie, survie contrôlée ------------------------------------------------------------------
    ("c01a", "forme actuelle `location`", H, "    lieu = _nom(s.get(\"location\"))", "    lieu = None"),
    ("c01b", "repli `datacenter.location`", H, "    lieu = _nom(dc.get(\"location\")) if isinstance(dc, dict) else None",
     "    lieu = None"),
    ("c01c", "repli `--lieu`", M, "            if type_lu and (lieu_lu or lieu):", "            if type_lu and lieu_lu:"),
    ("c01d", "démarrage sous retentatives", M, "        except Exception as e:  # noqa: BLE001 — démarrage retenté",
     "        except ZeroDivisionError as e:  # noqa: BLE001 — démarrage retenté"),
    ("c01e", "échéance passée sans lecture", M, "            if horloge() >= fin:", "            if False:"),
    ("c01f", "survie contrôlée", M, "        if not (survie[\"vivante\"] and survie[\"garder\"]):", "        if False:"),
    ("c01g", "ligne « garder » exigée", M, "        if not (survie[\"vivante\"] and survie[\"garder\"]):",
     "        if not survie[\"vivante\"]:"),
    ("c01h", "attente de la ligne « garder »", M, "        if lignes_garder(minuterie[\"journal\"]):", "        if True:"),
    ("c01i", "contrôle par défaut", M, "controler = controler or (lambda mi, dormir: attendre_minuterie(mi, dormir=dormir))",
     "controler = controler or (lambda mi, dormir: {\"vivante\": True, \"garder\": True, \"motif\": \"\"})"),
    ("c01j", "prix le plus haut", M, "            prix = max(candidats)", "            prix = candidats[0]"),
    ("c01k", "création lue plus tôt que --depuis", M,
     "    depuis_retenu = min(depuis, cree_a) if cree_a is not None else depuis", "    depuis_retenu = depuis"),
    ("c01l", "refus de nom au démarrage", M, "            if s.get(\"name\") != NOM_MACHINE:", "            if False:"),
    ("c01m", "lecture refusée au démarrage bornée", M,
     "            if refus >= refus_max:\n                raise DestructionRefusee(f\"lecture du serveur",
     "            if False:\n                raise DestructionRefusee(f\"lecture du serveur"),
    # -- CLC4-03 : dépôt et contrôle portable -------------------------------------------------------------------------------------
    ("c03a", "racine écrite en dur", M, "    return Path(depot).resolve() if depot else Path(__file__).resolve().parents[3]",
     "    return Path(depot).resolve() if depot else Path(\"/home/user/controle-ia-travail\")"),
    ("c03b", "dépôt exigé", M, "    if exiger and not (c[\"go\"].is_file() and c[\"depenses\"].is_file()):", "    if False:"),
    ("c03c", "kill -0 avant ps", M,
     "        arguments = None if etat == \"absent\" else (ps(pid).split() if etat == \"présent\" else [])",
     "        arguments = ps(pid).split()"),
    ("c03d", "ps -ww", M, "[\"ps\", \"-ww\", \"-p\", str(pid), \"-o\", \"command=\"]", "[\"ps\", \"-p\", str(pid), \"-o\", \"command=\"]"),
    ("c03e", "kill -0 réel", M, "        os.kill(pid, 0)   # signal 0 : contrôle d'existence, rien n'est envoyé", "        pass"),
    ("c03f", "fraîcheur des lignes « garder »", M,
     "        if derniere is None or (horloge() - derniere).total_seconds() > fraicheur_s:", "        if derniere is None:"),
    ("c03g", "identifiant de la minuterie", M,
     "    return any(a == \"--identifiant\" and b == identifiant for a, b in zip(arguments, arguments[1:]))", "    return True"),
    # -- CLC4-05 : refus durable --------------------------------------------------------------------------------------------------
    ("c05a", "refus durable borné (destruction)", M,
     "            if refus >= refus_max:\n                raise DestructionRefusee(\n                    f\"suppression",
     "            if False:\n                raise DestructionRefusee(\n                    f\"suppression"),
    ("c05b", "refus durable borné (lectures)", M,
     "            if refus >= refus_max:\n                raise DestructionRefusee(f\"{quoi} refusée durablement",
     "            if False:\n                raise DestructionRefusee(f\"{quoi} refusée durablement"),
    ("c05c", "401 et 403 durables (requêtes)", H,
     "        if statut in STATUTS_REFUS_DURABLE:\n            raise self._refus(methode, chemin, statut)",
     "        if False:\n            raise self._refus(methode, chemin, statut)"),
    ("c05d", "401 et 403 durables (lecture d'un serveur)", H,
     "        if statut in STATUTS_REFUS_DURABLE:\n            raise self._refus(\"GET\", f\"/servers/{int(ident)}\", statut)",
     "        if False:\n            raise self._refus(\"GET\", f\"/servers/{int(ident)}\", statut)"),
    ("c05e", "code de sortie distinct", M, "        return CODE_DESTRUCTION_REFUSEE", "        return CODE_REFUS"),
    ("c05f", "échecs écrits sans journal", M, "    if journal is not None:\n        _ecrire(journal, entree)\n        return",
     "    if True:\n        _ecrire(journal, entree)\n        return"),
    # -- CLC4-06, CLC4-07 ---------------------------------------------------------------------------------------------------------
    ("c06a", "bon nom d'abord", M, "    bons = [(i, n) for i, n in trouves if n == NOM_MACHINE]",
     "    bons = [] if any(n != NOM_MACHINE for _, n in trouves) else trouves"),
    ("c06b", "autres noms nommés à l'arrêt", M, "    if autres:\n        raise _arret_autres(detruits, autres)\n    return {\"trouves\"",
     "    if False:\n        raise _arret_autres(detruits, autres)\n    return {\"trouves\""),
    ("c07a", "solde après destruction", M,
     "                if solder is not None:\n                    try:\n                        solder(ident, etiquettes)",
     "                if False:\n                    try:\n                        solder(ident, etiquettes)"),
    ("c07b", "solde par les étiquettes du serveur", M,
     "        etiquette, go = jeton or etiquettes.get(ETIQUETTE_CREATION), go_id or etiquettes.get(\"go\")",
     "        etiquette, go = jeton, go_id"),
    ("c07c", "solde par la minuterie", M,
     "solder = fabrique_solder(c[\"creations\"], horloge, a.go, a.etiquette) if (a.go and a.etiquette) else None",
     "solder = None"),
    ("i01", "inventaire : recherche par nom", M, "    serveurs = sorted(set(par_etiquettes) | set(par_nom))",
     "    serveurs = sorted(set(par_etiquettes))"),
    ("i02", "inventaire : adresses non attribuées seulement", H,
     "for x in d.get(\"primary_ips\", []) if x.get(\"assignee_id\") is None]", "for x in d.get(\"primary_ips\", [])]"),
    # -- procédure du poste local -------------------------------------------------------------------------------------------------
    ("p01", "heure limite de création", M, "    if horloge() > prep[\"heure_limite_creation\"]:", "    if False:"),
    ("p02", "fichier de rattrapage poussé", M, "    if not pousse:", "    if False:"),
    ("p03", "échéance bornée par la tâche de la mère", M,
     "    echeance = min(depuis + timedelta(hours=ECHEANCES_H[pas_long]), limite)",
     "    echeance = depuis + timedelta(hours=ECHEANCES_H[pas_long])"),
    ("p04", "au moins une heure avant la tâche", M, "    if (limite - intention).total_seconds() / 3600.0 < ECHEANCE_MIN_H:",
     "    if False:"),
    ("p05", "préparer : heure limite passée", M, "    if heure_limite_creation <= maintenant:", "    if False:"),
    ("p06", "préparer : écart limite-tâche", M,
     "    if heure_tache_mere < heure_limite_creation + timedelta(hours=ECART_LIMITE_TACHE_H):", "    if False:"),
    ("p07", "préparer : 47 heures au plus", M, "    if heure_tache_mere > maintenant + timedelta(hours=TACHE_MERE_MAX_H):",
     "    if False:"),
    ("p08", "nom du fichier et jeton", M,
     "    if chemin.name != f\"rattrapage-machine-{r['pas']}-{jeton[:12]}-v1.json\" or r.get(\"nom\") != NOM_MACHINE:",
     "    if False:"),
    ("p09", "GO du fichier", M, "    if go_id is not None and r.get(\"go\") != go_id:", "    if False:"),
    ("p10", "format du fichier", M, "    if not isinstance(r, dict) or r.get(\"format\") != FORMAT:", "    if not isinstance(r, dict):"),
    ("p11a", "git : suivi", M, "        if git(\"ls-files\", \"--error-unmatch\", \"--\", rel).returncode != 0:", "        if False:"),
    ("p11b", "git : égal à HEAD", M, "        if git(\"diff\", \"--quiet\", \"HEAD\", \"--\", rel).returncode != 0:", "        if False:"),
    ("p11c", "git : poussé", M, "    if not distantes:", "    if False:"),
    ("p12a", "détaché : option retirée de l'enfant", M, "        elif x != \"--detache\" and not x.startswith(\"--sortie=\"):",
     "        elif not x.startswith(\"--sortie=\"):"),
    ("p12b", "détaché : session à lui", M, "stderr=subprocess.STDOUT, start_new_session=True",
     "stderr=subprocess.STDOUT, start_new_session=False"),
    ("p12c", "minuterie : session à elle", M, "stdout=s, stderr=s, start_new_session=True",
     "stdout=s, stderr=s, start_new_session=False"),
    ("p13", "détaché : sortie neuve", M, "    if sortie.exists():", "    if False:"),
    ("p14", "jamais une clé privée", M,
     "    if \"PRIVATE\" in texte.upper() or \"\\n\" in texte or not texte.startswith((\"ssh-\", \"ecdsa-\")):",
     "    if \"\\n\" in texte:"),
    ("p15", "adresse IPv4 du poste", M,
     "        ipaddress.IPv4Address(ip_poste)\n    except ValueError:\n        raise GardeArret(\"adresse du poste : une adresse IPv4 "
     "seule attendue\") from None\n    chemin = _chemin_acces",
     "        pass\n    except ValueError:\n        raise GardeArret(\"adresse du poste : une adresse IPv4 "
     "seule attendue\") from None\n    chemin = _chemin_acces"),
    ("p16", "accès : serveur encore là", M,
     "    if client.chercher_par_etiquette(prep[\"etiquette\"]) or any(n == NOM_MACHINE for _, n in client.inventaire()):",
     "    if False:"),
    ("p17", "accès : nom contrôlé", M, "        if objet.get(\"name\") != acces[\"nom\"]:", "        if False:"),
    ("p18", "accès : fichier neuf", M, "    if chemin.exists():\n        raise GardeArret(f\"{chemin.name} existe déjà (R12)\")",
     "    if False:\n        raise GardeArret(f\"{chemin.name} existe déjà (R12)\")"),
    ("p19", "message de la mère : autre nom", M, "            \"ne jamais toucher un serveur d'un autre nom (le signaler à Lazar) ; \"\n",
     ""),
    ("p20", "seconde tâche à 24 heures", M, "\"heure_tache_mere_2\": heure_tache_mere + timedelta(hours=24),",
     "\"heure_tache_mere_2\": heure_tache_mere,"),
]


def copier(racine: Path, dest: Path) -> None:
    (dest / "src" / "controle_ia").mkdir(parents=True)
    for f in ("__init__.py", "gardes.py"):
        shutil.copy2(racine / "src" / "controle_ia" / f, dest / "src" / "controle_ia" / f)
    shutil.copytree(racine / "src" / "controle_ia" / "lean_essai", dest / "src" / "controle_ia" / "lean_essai",
                    ignore=shutil.ignore_patterns("__pycache__"))
    (dest / "tests").mkdir()
    for f in ["tests/conftest.py"] + ESSAIS:
        shutil.copy2(racine / f, dest / f)
    shutil.copy2(racine / "pyproject.toml", dest / "pyproject.toml")


def env_propre() -> dict:
    retires = ("PYTHONPATH", "PYTHONHOME", "PYTHONSTARTUP", "HCLOUD_TOKEN")
    env = {k: v for k, v in os.environ.items() if k not in retires}
    env["PYTHONDONTWRITEBYTECODE"] = "1"
    return env


def borner_fichiers() -> None:
    resource.setrlimit(resource.RLIMIT_FSIZE, (100 * 2 ** 20, 100 * 2 ** 20))


def tracer_import(copie: Path, module: str) -> str:
    code = ("import sys; sys.path[:0] = [sys.argv[1] + '/src', sys.argv[1] + '/tests']; "
            f"import controle_ia.lean_essai.{module} as m; print(m.__file__)")
    p = subprocess.run([sys.executable, "-I", "-B", "-c", code, str(copie)], capture_output=True, text=True,
                       env=env_propre(), cwd=copie)
    chemin = p.stdout.strip()
    if p.returncode != 0 or not chemin.startswith(str(copie)):
        raise SystemExit(f"import non tracé vers la copie : {chemin!r} {p.stderr[-300:]}")
    return chemin


def lancer_essais(copie: Path) -> tuple[int, str]:
    cmd = [sys.executable, "-B", "-m", "pytest", "-q", "-x", "-p", "no:cacheprovider", "-c", str(copie / "pyproject.toml"),
           "--rootdir", str(copie), "--basetemp", str(copie / "pytest-tmp"),
           "-o", f"pythonpath={copie / 'src'} {copie / 'tests'}"] + [str(copie / e) for e in ESSAIS]
    try:
        p = subprocess.run(cmd, capture_output=True, text=True, env=env_propre(), cwd=copie, timeout=180,
                           preexec_fn=borner_fichiers)
    except subprocess.TimeoutExpired:
        return -9, "délai dépassé (boucle sans fin) : enfant arrêté par son PID"
    lignes = [x for x in p.stdout.splitlines() if x.strip()]
    return p.returncode, (lignes[-1] if lignes else p.stderr[-200:])


def main(argv=None) -> int:
    argv = argv or sys.argv[1:]
    racine, travail = Path(argv[0]).resolve(), Path(argv[1]).resolve()
    travail.mkdir(parents=True, exist_ok=True)
    temoin = travail / "temoin"
    shutil.rmtree(temoin, ignore_errors=True)
    copier(racine, temoin)
    tracer_import(temoin, M)
    code, ligne = lancer_essais(temoin)
    resultats = [{"id": "témoin", "defaut": "aucune mutation", "code": code, "fin": ligne, "tuee": None}]
    if code != 0:
        print(json.dumps(resultats, ensure_ascii=False, indent=1))
        raise SystemExit("la copie témoin ne passe pas : mutations sans objet")
    shutil.rmtree(temoin)
    for ident, defaut, module, ancien, nouveau in MUTATIONS:
        copie = travail / ident
        shutil.rmtree(copie, ignore_errors=True)
        copier(racine, copie)
        fichier = copie / "src" / "controle_ia" / "lean_essai" / f"{module}.py"
        texte = fichier.read_text(encoding="utf-8")
        if texte.count(ancien) != 1:
            raise SystemExit(f"{ident} inapplicable : {texte.count(ancien)} occurrence(s) dans {module}.py")
        fichier.write_text(texte.replace(ancien, nouveau), encoding="utf-8")
        trace = tracer_import(copie, module)
        code, ligne = lancer_essais(copie)
        resultats.append({"id": ident, "defaut": defaut, "module": module, "import": trace.replace(str(travail), "<travail>"),
                          "code": code, "fin": ligne, "tuee": code != 0, "par_delai": code == -9})
        shutil.rmtree(copie)
    survivantes = [r["id"] for r in resultats if r["tuee"] is False]
    print(json.dumps({"mutations": len(MUTATIONS), "tuees": len(MUTATIONS) - len(survivantes), "survivantes": survivantes,
                      "par_delai": [r["id"] for r in resultats if r.get("par_delai")], "detail": resultats},
                     ensure_ascii=False, indent=1))
    return 0 if not survivantes else 1


if __name__ == "__main__":
    sys.exit(main())
