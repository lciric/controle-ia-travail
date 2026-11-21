MODULE = "reproduction_v1.py"
ESSAIS = ["test_lentilles_sondes_bbis_seconde_passe_phrases_reproduction_v1.py"]
ALTERATIONS = [
 ("tables ouvertes sans vérifier l'empreinte", "    if _sha(octets) != ligne.sha256:\n        raise Arret(\"tables", "    if False:\n        raise Arret(\"tables"),
 ("tables ouvertes avant le scellement de la v2", "    nl.exiger_ouverture_permise_des_tables(registre_propre)\n", ""),
 ("E-1 non comparée entre les passes", 'if entrees.get("e1_sha256") != sha256_e1 or entrees.get("e2_sha256") != sha256_e2:', 'if entrees.get("e2_sha256") != sha256_e2:'),
 ("libellé différent non vu", "libelle, jetons = lib1 != lib2, set(ids1) != set(ids2)", "libelle, jetons = False, set(ids1) != set(ids2)"),
 ("jetons différents non vus", "libelle, jetons = lib1 != lib2, set(ids1) != set(ids2)", "libelle, jetons = lib1 != lib2, False"),
 ("non achevée traitée comme jamais lancée", "    if premiere_passe == nl.PREMIERE_PASSE_NON_ACHEVEE:\n        return {\"etat\": ETAT_NON_FAITE, \"phrases_de_la_lentille_publique_et_des_logits_ecrites\": False,", "    if premiere_passe == nl.PREMIERE_PASSE_NON_ACHEVEE:\n        return {\"etat\": ETAT_REMPLACEE, \"phrases_de_la_lentille_publique_et_des_logits_ecrites\": True,"),
 ("archive de lectures non vérifiée", "if not chemin.is_file() or _sha(chemin.read_bytes()) != morceau[\"sha256\"]:", "if not chemin.is_file():"),
 ("libellé public différent non signalé", "if libelle and cle[2] == K.LENTILLE_PUBLIQUE:", "if False:"),
]
