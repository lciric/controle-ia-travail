"""Banc d'altérations du programme de comparaison du réajustement v4 : chaque garde neuve est retirée ou faussée, une à une, sur une
COPIE du programme (jamais sur le fichier versé) ; une altération est « tuée » si au moins un essai échoue."""
import os
import shutil
import subprocess
import sys
from concurrent.futures import ThreadPoolExecutor
from pathlib import Path

RACINE = Path("/home/user/controle-ia-travail")
SRC = RACINE / "src/controle_ia"
NOM = "comparer_reajustement_v4.py"
ESSAIS = "tests/test_neuron_lens_comparer_reajustement_v4.py"
ICI = Path(__file__).resolve().parent
ORIGINAL = (SRC / "neuron_lens" / NOM).read_text(encoding="utf-8")

A = []  # (nom, garde, ancien, nouveau)


def alt(nom, ancien, nouveau, n=1):
    assert ORIGINAL.count(ancien) == n, (nom, ORIGINAL.count(ancien))
    A.append((nom, ancien, nouveau))


alt("T0 témoin : aucune altération (doit passer)", "PROGRAMME = ", "PROGRAMME = ")
alt("T1 témoin : libellé du premier palier changé (doit être tuée : prouve que la copie est bien celle qu'on essaie)",
    'PALIER_1 = "palier 1 — même', 'PALIER_1 = "palier un — même')
# 1. depot_propre
alt("1a depot_propre non exigé du manifeste neuf", 'm.get("depot_propre") is True, m.get', '(cote == "ref" or m.get("depot_propre") is True), m.get')
alt("1b depot_propre non exigé du manifeste de référence", 'm.get("depot_propre") is True, m.get', '(cote == "neuf" or m.get("depot_propre") is True), m.get')
alt("1c depot_propre : toute valeur « vraie » acceptée (\"true\", 1)", 'm.get("depot_propre") is True, m.get', 'bool(m.get("depot_propre")), m.get')
alt("1d depot_propre : absent accepté", 'm.get("depot_propre") is True, m.get', 'm.get("depot_propre", True) is True, m.get')
# 2. champs du haut
alt("2a table du haut vidée", 'd["haut"] = haut', 'd["haut"] = {}')
alt("2b champ présent d'un seul côté non relevé", "if pr and pn and mref[k] == mneuf[k]:", "if mref.get(k) == mneuf.get(k):")
alt("2c empreinte de la valeur calculée sur le début seulement", "empreinte_octets(json.dumps(v, sort_keys", "empreinte_octets(json.dumps(str(v)[:200], sort_keys")
alt("2d table du haut qui double versions, commit, config", 'HAUT_HORS_TABLE = ("versions", "commit", "config")', "HAUT_HORS_TABLE = ()")
alt("2e table du haut limitée aux champs présents des deux côtés", "for k in sorted((set(mref) | set(mneuf)) - set(HAUT_HORS_TABLE)):", "for k in sorted((set(mref) & set(mneuf)) - set(HAUT_HORS_TABLE)):")
alt("2f un champ du haut oublié (graines)", "for k in sorted((set(mref) | set(mneuf)) - set(HAUT_HORS_TABLE)):", 'for k in sorted((set(mref) | set(mneuf)) - set(HAUT_HORS_TABLE) - {"graines"}):')
# 3. K1
alt("3a préalable K1 commit des résultats retiré", '*releve("commit_resultats"))', 'True, "")')
alt("3b préalable K1 résultat d'ajustement retiré", '*releve_piece("ajustement_neuf"))', 'True, "")')
alt("3c préalable K1 manifeste retiré", '*releve_piece("manifeste_neuf"))', 'True, "")')
alt("3d préalable K1 export retiré", '*releve_piece("export_neuf"))', 'True, "")')
alt("3e relevé tenu sur toute valeur « vraie »", 'return (isinstance(e, dict) and e.get("tenu") is True),', 'return (isinstance(e, dict) and bool(e.get("tenu"))),')
alt("3f relevé absent tenu pour bon", 'return (isinstance(e, dict) and e.get("tenu") is True),', 'return (not isinstance(e, dict) or e.get("tenu") is True),')
alt("3g empreinte au commit non comparée à celle que porte la sortie", 'return tenu and isinstance(porte, str) and e.get("sha256_au_commit") == porte,', "return tenu,")
alt("3h identifiant de commit : toute chaîne acceptée (nom de branche, préfixe)", "if not (isinstance(commit, str) and _COMMIT.fullmatch(commit)):", "if not isinstance(commit, str):")
alt("3i identifiant de commit : préfixe hexadécimal accepté", '_COMMIT = re.compile(r"[0-9a-f]{40}|[0-9a-f]{64}")', '_COMMIT = re.compile(r"[0-9a-f]{7,64}")')
alt("3j identifiant de commit : fin de ligne tolérée à l'essai de forme", "_COMMIT.fullmatch(commit)", "_COMMIT.fullmatch(commit.strip())")
alt("3j bis identifiant de commit : essai de forme non ancré à la fin", "_COMMIT.fullmatch(commit)", "_COMMIT.match(commit)")
alt("3k un arbre accepté comme commit", 'f"{commit}^{{commit}}")', 'f"{commit}")')
alt("3l commit absent du dépôt accepté", "    if r.returncode != 0:\n        return False, f\"commit {commit} illisible", "    if False:\n        return False, f\"commit {commit} illisible")
alt("3m un dossier accepté comme fichier au commit", 'if t.returncode != 0 or t.stdout.strip() != b"blob":', "if t.returncode != 0:")
alt("3n chemin qui n'est pas une chaîne accepté", "    if not isinstance(chemin, str):\n        return None, f\"chemin dans", "    if False:\n        return None, f\"chemin dans")
alt("3o octets au commit non comparés aux octets lus", "egal = b == octets_lus", "egal = True")
alt("3p fichier absent du commit tenu pour rattaché", 'return {"tenu": False, "chemin": chemin, "commit": commit, "sha256_lu": lu, "sha256_au_commit": None, "detail": motif}',
    'return {"tenu": True, "chemin": chemin, "commit": commit, "sha256_lu": lu, "sha256_au_commit": lu, "detail": motif}')
alt("3q comparaison par longueur au lieu des octets", "egal = b == octets_lus", "egal = len(b) == len(octets_lus)")
alt("3r chemin donné en argument ignoré", "    if chemin_donne is not None:\n        return str(chemin_donne), \"donné en argument\"\n", "")
alt("3s chemin déduit depuis le dossier donné et non depuis la racine du dépôt", "relative_to(racine.resolve())", "relative_to(Path(depot).resolve())")
alt("3t fichier hors du dépôt : chemin inventé (nom du fichier)", '        return None, "non donné, et le fichier n\'est pas sous la racine du dépôt : chemin non déductible"', '        return Path(fichier).name, "nom du fichier"')
alt("3u pièces neuves lues au commit du manifeste et non au commit des résultats", "ratt[nom] = dict(rattacher(depot, commit_resultats, chemin, octets)", "ratt[nom] = dict(rattacher(depot, commit_n, chemin, octets)")
alt("3v export neuf non rattaché", '        pieces_neuves.append(("export_neuf", neuf_export, chemin_neuf_export, o_en))\n', "")
alt("3w commit des résultats tenu pour lisible sans lecture", 'ratt["commit_resultats"] = {"tenu": ok,', 'ratt["commit_resultats"] = {"tenu": True,')
alt("3x manifeste neuf rattaché avec les octets du résultat", '("manifeste_neuf", neuf_manifeste, chemin_neuf_manifeste, o_mn)', '("manifeste_neuf", neuf_ajustement, chemin_neuf_ajustement, o_an)')
# 4. K2
alt("4a préalable K2 lanceur retiré", '*releve_piece("lanceur_neuf"))', 'True, "")')
alt("4b préalable K2 commit du manifeste lisible retiré", '*releve(f"commit_manifeste_{cote}"))', 'True, "")')
alt("4c lanceur lu au commit des résultats", 'ratt["lanceur_neuf"] = dict(rattacher(depot, commit_n, chemin_lanceur_neuf, o_ln)', 'ratt["lanceur_neuf"] = dict(rattacher(depot, commit_resultats, chemin_lanceur_neuf, o_ln)')
alt("4d lanceur lu au commit du manifeste de référence", 'ratt["lanceur_neuf"] = dict(rattacher(depot, commit_n, chemin_lanceur_neuf, o_ln)', 'ratt["lanceur_neuf"] = dict(rattacher(depot, commit_r, chemin_lanceur_neuf, o_ln)')
alt("4e commit du manifeste tenu pour lisible sans lecture", 'ratt[f"commit_manifeste_{cote}"] = {"tenu": ok,', 'ratt[f"commit_manifeste_{cote}"] = {"tenu": True,')
alt("4f lanceur rattaché avec les octets du lanceur de référence", "rattacher(depot, commit_n, chemin_lanceur_neuf, o_ln)", "rattacher(depot, commit_n, chemin_lanceur_neuf, o_lr)")
# 5. pièces mal formées
for i, (nom, anc) in enumerate([
        ("enveloppe", 'en dictionnaire ({cote})", isinstance(e, dict), _nom_type(e))'),
        ("résultat", 'en dictionnaire ({cote})", isinstance(r, dict), _nom_type(r))'),
        ("manifeste", 'en dictionnaire ({cote})", isinstance(m, dict), _nom_type(m))'),
        ("config", 'isinstance(_dico(m).get("config"), dict),'),
        ("versions", 'isinstance(_dico(m).get("versions"), dict),'),
        ("correctifs", "_chemins(corr) is not None, str(corr)[:120])"),
        ("enveloppe de l'export", "isinstance(brut, dict), _nom_type(brut), structure_export=True)")]):
    neuf = anc.replace("isinstance(e, dict)", "True").replace("isinstance(r, dict)", "True").replace("isinstance(m, dict)", "True") \
              .replace('isinstance(_dico(m).get("config"), dict)', "True").replace('isinstance(_dico(m).get("versions"), dict)', "True") \
              .replace("_chemins(corr) is not None", "True").replace("isinstance(brut, dict)", "True")
    assert neuf != anc
    alt(f"5{'abcdefg'[i]} préalable de forme retiré : {nom}", anc, neuf)
alt("5h pièce qui n'est pas un dictionnaire laissée telle quelle", "    return x if isinstance(x, dict) else {}", "    return x")
alt("5i liste de correctifs non vérifiée", "    if isinstance(x, list) and x and all(isinstance(v, str) and v for v in x):\n        return x\n    return None", "    return x")
alt("5j liste de correctifs : éléments non vérifiés", "if isinstance(x, list) and x and all(isinstance(v, str) and v for v in x):", "if isinstance(x, list) and x:")
alt("5k liste de correctifs : dictionnaire accepté", "if isinstance(x, list) and x and all(isinstance(v, str) and v for v in x):", "if x and all(isinstance(v, str) and v for v in x):")
alt("5l erreur inattendue de la comparaison non rattrapée", "    except Exception as erreur:  # noqa: BLE001 — aucune exception ne sort", "    except KeyboardInterrupt as erreur:  # noqa: BLE001 — aucune exception ne sort")
alt("5m erreur de lecture des pièces non rattrapée", "    except Exception as erreur:  # noqa: BLE001 — pièce illisible", "    except KeyboardInterrupt as erreur:  # noqa: BLE001 — pièce illisible")
alt("5n arrêt sur erreur : jamais suspendue", "porte_le_18 = bien_formee and (", "porte_le_18 = False and bien_formee and (")
alt("5o arrêt sur erreur : toujours suspendue", "porte_le_18 = bien_formee and (", "porte_le_18 = True or (")
alt("5p arrêt sur erreur : constantes du 18 ignorées", " or sha_neuf in EMPREINTES_FICHIERS_18.values())", ")")
alt("5q arrêt sur erreur : empreinte de la référence lue ignorée", "(sha_neuf == sha_ref or sha_neuf in", "(sha_neuf in")
alt("5r arrêt sur erreur : empreinte mal formée acceptée", "porte_le_18 = bien_formee and (", "porte_le_18 = (")
alt("5s arrêt sur erreur : message d'erreur non versé", '"message": str(erreur),', '"message": "",')
alt("5t arrêt sur erreur : code de sortie nul", "        sys.exit(2)\n", "        pass\n")
alt("5u arrêt sur erreur : sortie non écrite (arrêt avant l'écriture)", "    r[\"ligne_de_commande\"] = sys.argv if argv is None else [PROGRAMME, *argv]\n",
    "    if r[\"arret_sur_erreur\"]:\n        sys.exit(2)\n    r[\"ligne_de_commande\"] = sys.argv if argv is None else [PROGRAMME, *argv]\n")
alt("5v lanceur illisible : exception non rattrapée", "    except (UnicodeDecodeError, SyntaxError, ValueError) as err:", "    except KeyboardInterrupt as err:")
alt("5w lecture de secours : fichier absent non rattrapé", "        except OSError as e:\n            pieces[nom]", "        except KeyboardInterrupt as e:\n            pieces[nom]")
alt("5x lecture de secours : empreinte du résultat neuf non lue", '"sha_neuf": n.get("sha256"),', '"sha_neuf": None,')
alt("5y constante de l'empreinte du 18 fausse (S)", '"S": "aac70eef', '"S": "bac70eef')
alt("5z arrêt sur erreur : marque d'arrêt non posée", '"critere": CRITERE, "arret_sur_erreur": True,', '"critere": CRITERE, "arret_sur_erreur": False,')
alt("5A sortie créée sans le mode exclusif (R12)", 'with open(x.sortie, "x", encoding="utf-8") as f:', 'with open(x.sortie, "w", encoding="utf-8") as f:')
alt("5B correctifs : garde de forme retirée à la lecture", "    if _chemins(chemins) is None:\n        return None\n", "")
alt("5C correctifs : garde de forme retirée dans le préalable", "and bool(er_) and lr_ is not None and ln_ is not None\n", "and bool(er_)\n")
# 6. audit_requis
alt("6a audit_requis posé pour (vi) seulement (comme la v3)", 'out["audit_requis"] = bool(out["declencheurs"])', 'out["audit_requis"] = any(d.startswith("(vi)") for d in out["declencheurs"])')
alt("6b audit_requis toujours vrai", 'out["audit_requis"] = bool(out["declencheurs"])', 'out["audit_requis"] = True')
alt("6c audit_requis non posé à l'arrêt de la lecture", '        r["audit_requis"] = True\n', '        r["audit_requis"] = False\n')
alt("6d audit_requis absent", 'out["audit_requis"] = bool(out["declencheurs"])', "pass")
# 7. mineures
alt("7a etape de l'export non exigée", "ok and e.get(\"etape\") == ETAPE_EXPORT,", "True,")
alt("7b etape de l'export exigée du seul côté de référence", "ok and e.get(\"etape\") == ETAPE_EXPORT,", '(cote == "ref" or (ok and e.get("etape") == ETAPE_EXPORT)),'.replace('cote == "ref"', 'cote == "neuf"'))
alt("7c etape de l'export exigée du seul côté neuf", "ok and e.get(\"etape\") == ETAPE_EXPORT,", '(cote == "ref" or (ok and e.get("etape") == ETAPE_EXPORT)),')
alt("7d valeur attendue de l'etape de l'export fausse", 'ETAPE_EXPORT = "export"', 'ETAPE_EXPORT = "Export"')
alt("7e etape de l'export : absente acceptée", 'e.get("etape") == ETAPE_EXPORT,', 'e.get("etape", ETAPE_EXPORT) == ETAPE_EXPORT,')
alt("7f empreinte du lanceur de référence non versée", '"lanceur_ref": empreinte_octets(o_lr), ', "")
alt("7g empreinte du lanceur de référence : celle du lanceur neuf", '"lanceur_ref": empreinte_octets(o_lr)', '"lanceur_ref": empreinte_octets(o_ln)')
alt("7h étiquette : le critère v3 nommé", "v5 à l'écriture du programme, 50657b89…", "critère v3")
alt("7i nom du programme dans la ligne de commande : v3", 'PROGRAMME = "comparer_reajustement_v4"', 'PROGRAMME = "comparer_reajustement_v3"')
alt("7j etape de l'export manquée : tables de R non rendues", "e.get(\"etape\") if ok else _nom_type(e))", "e.get(\"etape\") if ok else _nom_type(e), structure_export=True)")


def jouer(i):
    nom, ancien, nouveau = A[i]
    d = ICI / "copies" / f"{i:02d}"
    shutil.rmtree(d, ignore_errors=True)
    pk = d / "src/controle_ia"
    (pk / "neuron_lens").mkdir(parents=True)
    for f in SRC.iterdir():
        if f.name not in ("neuron_lens", "__pycache__"):
            os.symlink(f, pk / f.name)
    for f in (SRC / "neuron_lens").iterdir():
        if f.name not in (NOM, "__pycache__"):
            os.symlink(f, pk / "neuron_lens" / f.name)
    (pk / "neuron_lens" / NOM).write_text(ORIGINAL.replace(ancien, nouveau), encoding="utf-8")
    (ICI / "tmp").mkdir(exist_ok=True)
    r = subprocess.run([str(RACINE / ".venv/bin/python"), "-m", "pytest", "-x", "-q", "-p", "no:cacheprovider", "-o", f"pythonpath={d / 'src'} tests",
                        f"--basetemp={ICI / 'tmp' / f'{i:02d}'}", ESSAIS], cwd=RACINE, capture_output=True, text=True,
                       env=dict(os.environ, PYTHONDONTWRITEBYTECODE="1"))
    derniere = r.stdout.strip().splitlines()[-1] if r.stdout.strip() else r.stderr.strip()[-200:]
    premier = next((l for l in r.stdout.splitlines() if l.startswith("FAILED") or l.startswith("ERROR")), "")
    return i, nom, r.returncode, derniere, premier


if __name__ == "__main__":
    with ThreadPoolExecutor(max_workers=int(sys.argv[1]) if len(sys.argv) > 1 else 6) as ex:
        res = sorted(ex.map(jouer, range(len(A))))
    tuees = [x for x in res if x[2] != 0]
    survivent = [x for x in res if x[2] == 0]
    for i, nom, code, derniere, premier in res:
        print(f"{'TUÉE   ' if code else 'SURVIT '} {nom}\n         {derniere}\n         {premier[:230]}")
    print(f"\naltérations : {len(A)} dont 2 témoins ; tuées : {len(tuees)} ; survivent : {len(survivent)}")
    for x in survivent:
        print("  survit :", x[1])
