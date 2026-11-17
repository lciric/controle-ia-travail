"""Banc de mutations du crible (iii) — v1 (pièce qui fera foi, section « Étapes », point 0 : « toutes tuées pour la raison attendue »).

Chaque mutation est un couple « ancien → nouveau » appliqué à une copie du module dans un dossier jetable (l'ancien doit figurer
une seule fois) ; les essais du niveau A (`essais_crible_iii_v1.py`) sont rejoués sur la copie, dans un processus neuf
(`python3 -I -B`). Une mutation est **tuée** si les essais échouent **et** si l'essai attendu est parmi les échecs ; une mutation
qui survit, ou tuée par un autre essai seulement, est un défaut du banc. Le code original est rejoué d'abord : 0 échec exigé.

Usage : python3 -I -B mutations_crible_iii_v1.py      (code 0 si toutes les mutations sont tuées pour la raison attendue)
"""
from __future__ import annotations

import os
import shutil
import subprocess
import sys
import tempfile

ICI = os.path.dirname(os.path.abspath(__file__))
MODULES = ("crible_iii_v1.py", "mesure_crible_iii_v1.py", "lire_crible_iii_v1.py", "essais_crible_iii_v1.py")

# (nom, fichier, ancien, nouveau, motif de l'essai attendu parmi les échecs)
MUTATIONS = [
    ("le filtre lit le monde ou l'oracle (garde des entrées retirée)", "crible_iii_v1.py",
     "    exiger_entrees_du_filtre(valides, traits_archive)\n    vus, uniques",
     "    vus, uniques", "le filtre reçoit autre chose"),
    ("égalités rompues par l'ordre du proposeur", "crible_iii_v1.py",
     "    restants.sort()\n", "", "égalités par l'ordre des noms"),
    ("égalités rompues au hasard", "crible_iii_v1.py",
     "        meilleur = min(e for e in restants if abs(dist[e] - m) <= 1e-12)",
     "        import random\n        meilleur = random.choice([e for e in restants if abs(dist[e] - m) <= 1e-12])",
     "filtre : "),
    ("ensemble de l'archive gardé", "crible_iii_v1.py",
     "    restants = [e for e in uniques if not any(set(e) <= a for a in arch)]", "    restants = list(uniques)",
     "ensemble de l'archive retiré"),
    ("distance de Jaccard minimax au lieu de maximin", "crible_iii_v1.py",
     "        m = max(dist.values())", "        m = min(dist.values())", "distance de Jaccard"),
    ("H tiré d'une graine qui ne dépend pas de la racine (hasard du système)", "crible_iii_v1.py",
     "    rng = np.random.default_rng(graine_h(racine, r))", "    rng = np.random.default_rng()", "ensembles de H"),
    ("H tiré du secret (garde de la graine retirée)", "crible_iii_v1.py",
     "    if not isinstance(racine, int) or isinstance(racine, bool) or racine < 0:\n        raise Refus(",
     "    if False:\n        raise Refus(", "ensembles de H"),
    ("B servi d'autres ensembles que D", "crible_iii_v1.py",
     "                tb = texte_g2(s[\"g0\"], f[\"retenus\"])", "                tb = texte_g2(s[\"g0\"], f[\"retenus\"][::-1])",
     "crible sain"),
    ("garde du texte de B retirée", "crible_iii_v1.py",
     "    if not (isinstance(texte_b, str) and texte_b.encode(\"utf-8\") == texte_d.encode(\"utf-8\")):",
     "    if False:", "texte servi de B différent"),
    ("réponse brute de la passe 1 servie à la passe 2", "crible_iii_v1.py",
     "                td = texte_g2(s[\"g0\"], f[\"retenus\"])\n                tb = texte_g2(s[\"g0\"], f[\"retenus\"])",
     "                td = texte_g2(s[\"g0\"], f[\"retenus\"]) + (p1.get(\"texte\") or \"\")\n                tb = td",
     "crible sain"),
    ("garde du texte de passe 2 retirée", "crible_iii_v1.py",
     "    if texte != texte_g2(texte_g0, ensembles):\n        raise Arret(", "    if False:\n        raise Arret(",
     "texte servi d'une passe 2"),
    ("D et B lancés après une passe 1 tronquée", "crible_iii_v1.py",
     "        if p1 is not None and p1.get(\"etat\") == \"complet\":", "        if p1 is not None and p1.get(\"etat\") != \"echec\":",
     "passe 1 sans ensemble valide"),
    ("plus de vingt ensembles gardés", "crible_iii_v1.py",
     "        elif len(valides) < ENSEMBLES_DEMANDES:", "        elif len(valides) < 30:", "au-delà de vingt ignorés"),
    ("borne de 53 000 octets relâchée", "crible_iii_v1.py", "OCTETS_MAX_G12 = 53000", "OCTETS_MAX_G12 = 60000", "53 000 octets"),
    ("garde de départ retirée", "crible_iii_v1.py",
     "    if echeance_s - maintenant() < garde_de_depart(bornes):\n        raise Refus(",
     "    if False:\n        raise Refus(", "garde de départ"),
    ("minuterie au départ d'un monde retirée", "crible_iii_v1.py",
     "    return echeance_s - t >= garde_d_un_monde(bornes)", "    return True", "minuterie au départ d'un monde"),
    ("borne par appel ignorée", "crible_iii_v1.py",
     "        delai = min(bornes[\"appel_s\"], reste)", "        delai = 10 ** 6", "borne par appel"),
    ("ligne du minimum retirée", "crible_iii_v1.py",
     "            if n_c + n_e + n_n < MINIMUM_COMPLETS and c.arret is None:", "            if False:", "(minimum)"),
    ("limite de débit à 50 % au lieu de 5 %", "crible_iii_v1.py", "TAUX_LIMITE_DEBIT = 0.05", "TAUX_LIMITE_DEBIT = 0.5",
     "limite de débit"),
    ("part d'un relais non gardée", "crible_iii_v1.py",
     "            if c.regle[p] + c.reserve[p] + c.plafonds[p] > c.parts[p] + EPS:", "            if False:", "atteignant sa part"),
    ("témoin absent sans arrêt", "crible_iii_v1.py",
     "            arret, r_appel = e, (e.appel or {\"etat\": \"echec\", \"cout_usd\": c.plafonds[p], \"cause\": e.motif})",
     "            arret, r_appel = None, (e.appel or {\"etat\": \"echec\", \"cout_usd\": c.plafonds[p], \"cause\": e.motif})",
     "témoin d'isolement absent"),
    ("affectation des mondes aux files décalée", "crible_iii_v1.py", "    return r % FILES", "    return (r - 1) % FILES",
     "files : le monde r"),
    ("bornes réduites admises en mode réel", "crible_iii_v1.py",
     "    if mode == \"reel\" and bornes != BORNES_GELEES:", "    if False:", "bornes réduites en mode réel"),
    ("ligne de GO sans l'enveloppe GO-2026-11-15-06", "crible_iii_v1.py",
     "    if GO_ENVELOPPE not in g[\"ref\"] and GO_ENVELOPPE not in g[\"perimetre\"]:", "    if False:",
     "ligne « calcul » citant GO-2026-11-15-06"),
    ("passe 1 comptée hors de $_D", "mesure_crible_iii_v1.py",
     "    dollars = {\"S\": cout[\"S\"], \"D\": cout[\"P1\"] + cout[\"D\"],", "    dollars = {\"S\": cout[\"S\"], \"D\": cout[\"D\"],",
     "dollars de D et de B"),
    ("passe 1 comptée hors de $_B", "mesure_crible_iii_v1.py",
     "\"B\": cout[\"P1\"] + cout[\"B\"]}", "\"B\": cout[\"B\"]}", "dollars de D et de B"),
    ("carte refusée comptée", "mesure_crible_iii_v1.py",
     "        if c[\"etat\"] != \"admise\" or not (1 <= c[\"emplacement\"] <= EMPLACEMENTS):",
     "        if not (1 <= c[\"emplacement\"] <= EMPLACEMENTS):", "carte refusée, tronquée"),
    ("carte au-delà de six admise sans défaut", "mesure_crible_iii_v1.py",
     "        if c[\"etat\"] == \"admise\" and not (isinstance(c.get(\"emplacement\"), int) and 1 <= c[\"emplacement\"] <= EMPLACEMENTS):",
     "        if False:", "carte refusée, tronquée"),
    ("carte d'un appel tronqué comptée", "mesure_crible_iii_v1.py",
     "    if appel is None or appel.get(\"etat\") != \"complet\":\n        return []", "    if appel is None:\n        return []",
     "carte refusée, tronquée"),
    ("effet de K1 compté (intersection avec les composantes comptées retirée)", "mesure_crible_iii_v1.py",
     "    return {b: set().union(*[c[\"porte\"][indice] for c in rec[\"bras\"][b][\"valides\"]]) & comptees if",
     "    return {b: set().union(*[c[\"porte\"][indice] for c in rec[\"bras\"][b][\"valides\"]]) if", "effet de K1"),
    ("intervalles à 95 % au lieu de 97,5 % pour les principales", "mesure_crible_iii_v1.py",
     "NIVEAU_PRINCIPAL = 0.975", "NIVEAU_PRINCIPAL = 0.95", "97,5 %"),
    ("seconde mesure admise", "mesure_crible_iii_v1.py",
     "        if os.path.exists(sortie) or os.path.exists(sortie + \".sha256\"):\n            raise Refus(",
     "        if False:\n            raise Refus(", "mesure lancée deux fois"),
    ("lecture : minimum à 15 mondes complets", "lire_crible_iii_v1.py", "MIN_COMPLETS, FORMAT_MIN, ZONE_MIN = 16, 14, 10",
     "MIN_COMPLETS, FORMAT_MIN, ZONE_MIN = 15, 14, 10", "étage 1"),
    ("lecture : « perte établie » permise sous « B tronqué »", "lire_crible_iii_v1.py",
     "    if \"B tronqué\" in reserves and v[\"5\"].startswith(\"perte établie\"):", "    if False:", "B tronqué"),
    ("lecture : ligne d'arrêt lue comme une issue", "lire_crible_iii_v1.py",
     "    if arret is not None and arret.get(\"ligne\") != \"minimum\":", "    if False:", "étage 0"),
]


def jouer_essais(dossier):
    r = subprocess.run([sys.executable, "-I", "-B", os.path.join(dossier, "essais_crible_iii_v1.py")], capture_output=True,
                       text=True, encoding="utf-8", timeout=600)
    echecs = [l for l in r.stdout.splitlines() if l.startswith("ESSAI ÉCHEC")]
    return r.returncode, echecs, r.stdout + r.stderr[-2000:]


def main():
    lignes, defauts = [], 0
    with tempfile.TemporaryDirectory() as d:
        for m in MODULES:
            shutil.copy2(os.path.join(ICI, m), os.path.join(d, m))
        code, echecs, _ = jouer_essais(d)
        lignes.append(f"ORIGINAL : code {code}, {len(echecs)} échec(s)")
        if code != 0 or echecs:
            defauts += 1
        for nom, fichier, ancien, nouveau, attendu in MUTATIONS:
            with tempfile.TemporaryDirectory() as dm:
                for m in MODULES:
                    shutil.copy2(os.path.join(ICI, m), os.path.join(dm, m))
                with open(os.path.join(dm, fichier), encoding="utf-8") as f:
                    t = f.read()
                if t.count(ancien) != 1:
                    lignes.append(f"MUTATION NON APPLICABLE | {nom} | « ancien » trouvé {t.count(ancien)} fois")
                    defauts += 1
                    continue
                with open(os.path.join(dm, fichier), "w", encoding="utf-8") as f:
                    f.write(t.replace(ancien, nouveau))
                code, echecs, sortie = jouer_essais(dm)
                tuee = code != 0 and (any(attendu in e for e in echecs) or (not echecs and "Traceback" in sortie and False))
                raison = "; ".join(e.split(" | ")[1] for e in echecs[:3]) if echecs else (sortie.strip().splitlines() or [""])[-1][:160]
                lignes.append(f"MUTATION {'TUÉE' if tuee else 'SURVIVANTE'} | {nom} | {fichier} | code {code} | attendu « {attendu} » "
                              f"| échecs : {raison}")
                defauts += 0 if tuee else 1
    for l in lignes:
        print(l)
    print(f"MUTATIONS : {len(MUTATIONS)}, tuées pour la raison attendue {sum(1 for l in lignes if l.startswith('MUTATION TUÉE'))}, "
          f"défauts {defauts}")
    return 0 if defauts == 0 else 1


if __name__ == "__main__":
    raise SystemExit(main())
