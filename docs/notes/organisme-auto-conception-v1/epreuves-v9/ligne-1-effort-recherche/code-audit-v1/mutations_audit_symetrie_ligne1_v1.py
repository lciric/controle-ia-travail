"""Contrôle « trop beau » (R4) du programme de l'audit de symétrie de la ligne 1 : défauts réintroduits un par un dans une
copie du dossier `code/` de la copie de travail, puis l'essai visé est lancé, **avec le contrôle final des racines**
(`test_zz_aucune_racine_interdite_derivee`) dans la même passe. « vu » : l'essai visé échoue et le contrôle des racines
passe. Aucune racine du préenregistrement autre que celle des essais n'est employée par une mutation (la mutation de racine
emploie 2026111999, disjointe).

Usage : python3 -B mutations_audit_symetrie_ligne1_v1.py <dossier code/ de la copie de travail> <organisme> <sortie.txt>
"""

import os
import shutil
import subprocess
import sys
import tempfile

PROG = "audit_symetrie_ligne1_v1.py"
ESSAIS = "essais/test_audit_symetrie_ligne1_v1.py"
ZZ = "test_zz_aucune_racine_interdite_derivee"
# essai court qui dérive la racine des essais, joint à chaque passe pour que le contrôle des racines ait de quoi lire même
# quand l'essai visé ne dérive aucune graine (ni la porte ni ce compte ne lisent son issue)
DERIVE = "test_complement_cas_sain_aires_connues_cas_ecrit_a_la_main"

MUTATIONS = [
    ("m01", "complément : indéterminée comptée vraie",
     'effet_complement = None if et is None else (1 if et == "vraie" else 0)',
     'effet_complement = None if et is None else (1 if et in ("vraie", "indeterminee") else 0)',
     "test_complement_cas_sain_aires_et_intervalles_connus"),
    ("m02", "complément : indéterminée hors des aires (convention de la porte)",
     'effet_complement = None if et is None else (1 if et == "vraie" else 0)',
     "effet_complement = effet_porte",
     "test_complement_artefact_indeterminee_deplacee"),
    ("m03", "complément : carte non jugée comptée non vraie",
     'effet_complement = None if et is None else (1 if et == "vraie" else 0)',
     'effet_complement = 0 if et is None else (1 if et == "vraie" else 0)',
     "test_complement_artefacts_etiquettes_et_non_jugees"),
    ("m04", "complément : autre tâche de rééchantillonnage (classe renommée)",
     'comp = E.audit_generateur(cartes[k]["complement"], courses, config, racine_r, k)',
     'comp = E.audit_generateur(cartes[k]["complement"], courses, config, racine_r, k + "-complement")',
     "test_complement_memes_reechantillons_que_la_porte"),
    ("m05", "complément : autre racine (2026111999, disjointe)",
     'comp = E.audit_generateur(cartes[k]["complement"], courses, config, racine_r, k)',
     'comp = E.audit_generateur(cartes[k]["complement"], courses, config, 2026111999, k)',
     "test_complement_memes_reechantillons_que_la_porte"),
    ("m06", "complément : courses dans un autre ordre",
     "    courses = list(range(n))\n",
     "    courses = list(range(n))[::-1]\n",
     "test_complement_cas_sain_aires_et_intervalles_connus"),
    ("m07", "recalcul de la porte : comparaison à la sortie scellée retirée",
     "if scelle is None or JL.canonique(porte) != JL.canonique(scelle):",
     "if False:",
     "test_recalcul_de_la_porte_cas_sain_et_artefact"),
    ("m08", "complément : intervalle hors plage jamais nommé",
     'v["intervalle_tout_entier_hors_plage"] = v["borne_haute"] < plage[0] or v["borne_basse"] > plage[1]',
     'v["intervalle_tout_entier_hors_plage"] = False',
     "test_complement_intervalle_hors_plage_nomme_sans_arret"),
    ("m09", "recoupement : mot du bras toujours « concordant »",
     'return {"lectures": valeurs, "mot": MOT_DESACCORD if detail else MOT_CONCORDANT, "detail": detail}',
     'return {"lectures": valeurs, "mot": MOT_CONCORDANT, "detail": detail}',
     "test_recoupement_artefact_promotion_changee_dans_la_sortie_brute"),
    ("m10", "recoupement : comparaison des (V, R) retirée (M1-nul seul)",
     '    if len({(v["V"], v["R"]) for v in presentes.values()}) > 1:\n',
     '    if False:\n',
     "test_recoupement_artefact_promotion_changee_dans_la_sortie_brute"),
    ("m11", "recoupement : lecture « promotion » remplacée par la lecture « arrêt »",
     '"journal_decisions_de_promotion": journal_promotion.get(nom)',
     '"journal_decisions_de_promotion": journal_arret.get(nom)',
     "test_recoupement_promotions_contre_arrets_seuls"),
    ("m12", "recoupement : calcul direct de la sortie avec l'effet inversé",
     'sans = {x["l"] for x in sortie["lignees"] if not x["a_effet"]}',
     'sans = {x["l"] for x in sortie["lignees"] if x["a_effet"]}',
     "test_recoupement_cas_sain_concordant"),
    ("m13", "empreinte contre le manifeste non vérifiée",
     "    if reel != attendue:\n",
     "    if False:\n",
     "test_refus_empreinte_fausse"),
    ("m14", "compagnon `.sha256` non vérifié",
     "    if not B.verifier_scelle_fichier(chemin):\n        raise EmpreinteDifferente",
     "    if False:\n        raise EmpreinteDifferente",
     "test_refus_empreinte_fausse"),
    ("m15", "empreinte du manifeste donnée en argument ignorée",
     'verifier_fichier(chemin_manifeste, manifeste_sha256, "manifeste décisif")',
     'verifier_fichier(chemin_manifeste, B.sha256_fichier(chemin_manifeste), "manifeste décisif")',
     "test_refus_empreinte_fausse"),
    ("m16", "cohérence : sortie de l'étalonnage contre le manifeste retirée",
     'if (manifeste.get("etalonnage") or {}).get("sha256") != sha_etal:',
     "if False:",
     "test_verifier_coherence_cas_sain_et_artefacts"),
    ("m17", "sorties d'étalonnage non vérifiées contre la sortie scellée de l'étalonnage",
     'lus[nom] = verifier_fichier(chemin, fichiers_attendus[nom], "sortie d\'étalonnage")',
     "lus[nom] = B.sha256_fichier(chemin)",
     "test_refus_empreinte_fausse"),
    ("m18", "mode essai : toute racine admise",
     "        if racine_r != RACINE_ESSAIS or racine_r in RACINES_DU_PREENREGISTREMENT_HORS_ESSAIS:\n",
     "        if False:\n",
     "test_verifier_mode_cas_sains_et_artefacts"),
    ("m19", "mode réel : empreinte de la configuration non vérifiée",
     "        if sha_config != CONFIGURATION_SHA256:\n",
     "        if False:\n",
     "test_verifier_mode_cas_sains_et_artefacts"),
    ("m20", "contrôle des racines dérivées pendant le run retiré",
     'if mode == "essai" and set(racines_derivees) - {RACINE_ESSAIS}:',
     "if False:",
     "test_refus_racine_derivee_hors_du_mode"),
    ("m21", "lecteur : course ou classe de la sortie non contrôlée",
     '            if (s.get("course"), s.get("classe")) != (course, k):\n',
     "            if False:\n",
     "test_lecteur_artefacts_nom_absent_et_course_deplacee"),
    ("m22", "organisme non chargé admis",
     "    if not B.ORGANISME:\n",
     "    if False:\n",
     "test_refus_organisme_non_charge"),
    ("m23", "journal : chaîne rompue tolérée (journal relu sans contrôle de chaîne)",
     "        entete, objets, decisions = JL.lire(os.path.join(dossier_courses, nj))\n",
     "        entete, objets, decisions = _lire_sans_chaine(os.path.join(dossier_courses, nj))\n",
     "test_refus_journal_rompu"),
    ("m24", "recoupement : promotions du bras c jamais comptées depuis le journal",
     'promues = [choisie.get(nom)] if d["sortie"]["promue"] else []',
     "promues = []",
     "test_recoupement_cas_sain_concordant"),
    ("m25", "commande : run lancé en mode essai au lieu du mode réel",
     'chemin_cr, chemin_m = executer("reel", config, sha',
     'chemin_cr, chemin_m = executer("essai", config, sha',
     "test_main_mode_reel_refuse_avant_toute_derivation"),
]

# m23 : lecteur sans contrôle de chaîne, ajouté en fin de la copie mutée
LECTEUR_SANS_CHAINE = '''

def _lire_sans_chaine(chemin):
    import json as _j
    import lzma as _l
    entete, objets, decisions = None, {}, []
    with _l.open(chemin, "rb") as f:
        for i, brut in enumerate(f):
            ligne = _j.loads(brut)
            if i == 0:
                entete = ligne
            elif ligne.get("sorte") == "objet":
                objets[ligne["cle"]] = ligne["valeur"]
            elif ligne.get("sorte") == "decision":
                decisions.append(ligne)
    return entete, objets, decisions
'''


LIGNE = "docs/notes/organisme-auto-conception-v1/epreuves-v9/ligne-1-effort-recherche"
PREREG = "preenregistrement-ligne-1-effort-recherche-v5.md"


def preparer_copie(code, tmp):
    """Copie du dossier `code/` dans un dépôt git neuf, à la même place relative, avec la copie à l'octet du
    préenregistrement (lue par `verifier_preenregistrement` quand le chemin scellé et le commit de scellement manquent)."""
    depot = os.path.join(tmp, "depot")
    copie = os.path.join(depot, LIGNE, "code")
    shutil.copytree(code, copie)
    shutil.copy2(os.path.join(os.path.dirname(code), PREREG), os.path.join(depot, LIGNE, PREREG))
    subprocess.run(["git", "init", "-q", depot], check=True)
    return copie


def lancer(copie, tmp, organisme, essais):
    env = dict(os.environ, BANC_L1_ORGANISME=organisme, PYTHONDONTWRITEBYTECODE="1")
    return subprocess.run([sys.executable, "-B", "-m", "pytest", "-q", "-p", "no:cacheprovider", "--basetemp",
                           os.path.join(tmp, "pytest"), *essais, "-rA"], cwd=copie, env=env, capture_output=True, text=True)


def main():
    code, organisme, sortie = sys.argv[1], sys.argv[2], sys.argv[3]
    with open(os.path.join(code, PROG), encoding="utf-8") as f:
        source = f.read()
    lignes = [f"Contrôle par défauts réintroduits du programme {PROG} (R4) — copie de {code}", ""]
    # témoin : la copie sans défaut passe tous les essais (sinon un « vu » ne voudrait rien dire)
    tmp = tempfile.mkdtemp(prefix="mutation-temoin-", dir=os.environ.get("TMPDIR"))
    r = lancer(preparer_copie(code, tmp), tmp, organisme, [ESSAIS])
    derniere = [x for x in r.stdout.strip().splitlines() if x.strip()][-1]
    lignes.append(f"témoin (aucun défaut, suite entière) | code de retour {r.returncode} | {derniere}")
    shutil.rmtree(tmp)
    vus = 0
    for ident, quoi, ancien, neuf, essai in MUTATIONS:
        n = source.count(ancien)
        if n != 1:
            lignes.append(f"{ident} | {quoi} | texte ancien trouvé {n} fois : mutation non appliquée")
            continue
        tmp = tempfile.mkdtemp(prefix=f"mutation-{ident}-", dir=os.environ.get("TMPDIR"))
        copie = preparer_copie(code, tmp)
        mute = source.replace(ancien, neuf) + (LECTEUR_SANS_CHAINE if ident == "m23" else "")
        with open(os.path.join(copie, PROG), "w", encoding="utf-8") as f:
            f.write(mute)
        r = lancer(copie, tmp, organisme, [f"{ESSAIS}::{essai}", f"{ESSAIS}::{DERIVE}", f"{ESSAIS}::{ZZ}"])
        texte = r.stdout
        echoue = f"FAILED {ESSAIS}::{essai}" in texte
        zz_passe = f"PASSED {ESSAIS}::{ZZ}" in texte
        mot = "vu" if (echoue and zz_passe) else ("NON VU" if zz_passe else "contrôle des racines non passé")
        vus += mot == "vu"
        derniere = [x for x in texte.strip().splitlines() if x.strip()][-1] if texte.strip() else "(aucune sortie)"
        lignes.append(f"{ident} | {quoi} | essai visé : {essai} | {mot} | {derniere}")
        shutil.rmtree(tmp)
    lignes += ["", f"vus : {vus} sur {len(MUTATIONS)}"]
    with open(sortie, "w", encoding="utf-8") as f:
        f.write("\n".join(lignes) + "\n")
    print("\n".join(lignes))


if __name__ == "__main__":
    main()
