"""Mutations du harnais Lean v7 sur des copies (R-2415). Copie de `mutations_harnais_v6.py` (inchangé, R12) ; changements :
le pilote visé est `piloter_poste_v7.sh` (c04 porte sur `installer_chaine_v2.sh`) ; les essais lancés sont ceux de la v6 et
`tests/test_lean_essai_installer_v2.py` ; la copie emporte aussi les scripts v7 et `installer_chaine_v2.sh` (avec la v1, que
l'essai compare) ; cinq mutations de la garde de lisibilité (l01 à l05) s'ajoutent, l05 n'étant tuée qu'en root (essai
runuser) ; deux mutations du pilote v7 (l06 : scp sans enregistrement de la clé d'hôte ; l07 : cache du résolveur non vidé).
Usage v7 : python -I -B mutations_harnais_v7.py RACINE_DE_L_ARBRE DOSSIER_DE_TRAVAIL ; code 0 si toutes les mutations sont tuées.

Texte de la v6 :
Mutations du harnais Lean v6 sur des copies (contre-lecture machine de la v5 `897b7438…`, R-2333).

Même méthode que la v5 : copie neuve par mutation, remplacement exact présent une seule fois (sinon arrêt), **import tracé**
vers la copie, `pytest -o pythonpath=<copie>/src <copie>/tests` sans `PYTHONPATH` hérité, délai de 240 s, aucun jeton de
Hetzner dans l'environnement des enfants, taille de fichier bornée (100 Mio). Seuls les essais v6 sont lancés. Une mutation
peut porter sur un module Python ou sur le pilote (chemin relatif à la racine de l'arbre).

Couverture : CLC5-01 (r01 à r04), CLC5-03 (t01 à t03), CLC5-06 (les 16 mutations de la contre-lecture, m01 à m16, rejouées
sur la v6), CLC5-07 (g01 à g13), notes (c01 à c05, e01 à e10), et les mutations v5 encore pertinentes (n, c, p, i).

Usage : python -I -B mutations_harnais_v6.py RACINE_DE_L_ARBRE DOSSIER_DE_TRAVAIL ; code 0 si toutes les mutations sont tuées.
"""
from __future__ import annotations

import json
import os
import resource
import shutil
import subprocess
import sys
from pathlib import Path

ESSAIS = ["tests/test_lean_essai_minuterie_v6.py", "tests/test_lean_essai_installer_v2.py"]
LE = "src/controle_ia/lean_essai/"
M, H, H4, M4 = LE + "minuterie_v6.py", LE + "hetzner_v5.py", LE + "hetzner_v4.py", LE + "minuterie_v4.py"
P = "scripts/lean_essai_d1a_v7/piloter_poste_v7.sh"
I = "scripts/lean_essai_d1a_v2/installer_chaine_v2.sh"

MUTATIONS = [
    # -- CLC5-01 : survie sans course ----------------------------------------------------------------------------------------------
    ("r01", "« morte » sur la première lecture négative (v5)", M,
     "            if not vivante:\n                negatives += 1\n                motif = etat[\"motif\"]",
     "            if not vivante:\n                return {\"vivante\": False, \"garder\": False, \"motif\": etat[\"motif\"], "
     "\"lectures_negatives\": 1}"),
    ("r02", "poll() ignoré", M, "            code = processus.poll()\n            if code is not None:",
     "            code = None\n            if code is not None:"),
    ("r03", "contrôle par défaut sans l'objet du processus", M,
     "attendre_minuterie(mi, dormir=dormir, processus=mi.get(\"_processus\"))", "attendre_minuterie(mi, dormir=dormir)"),
    ("r04", "objet du processus non rendu", M, "            \"_processus\": p}", "            \"_processus\": None}"),
    # -- CLC5-03 ----------------------------------------------------------------------------------------------------------------
    ("t01", "seconde préparation admise", M, "    if autres:\n        raise GardeArret(f\"une préparation existe déjà",
     "    if False:\n        raise GardeArret(f\"une préparation existe déjà"),
    ("t02", "autre rattrapage admis à la création", M,
     "    if autres:\n        raise GardeArret(f\"autre préparation dans le dossier versé",
     "    if False:\n        raise GardeArret(f\"autre préparation dans le dossier versé"),
    ("t03", "le fichier passé compté comme un autre", M, "                    if p.name != rattrapage.name)",
     "                    if True)"),
    # -- CLC5-06 : les 16 mutations de la contre-lecture, sur la v6 ---------------------------------------------------------------
    ("m01", "lectures : 4 refus durables au lieu de 3", M,
     "            if refus >= refus_max:\n                raise DestructionRefusee(f\"{quoi}",
     "            if refus > refus_max:\n                raise DestructionRefusee(f\"{quoi}"),
    ("m02", "suppression : 4 refus durables au lieu de 3", M,
     "            if refus >= refus_max:\n                raise DestructionRefusee(\n",
     "            if refus > refus_max:\n                raise DestructionRefusee(\n"),
    ("m03", "message de la mère sans la clause 401/403", M,
     "            \"si une suppression rend 401 ou 403 : s'arrêter et demander à Lazar de détruire à la main par l'identifiant \"\n"
     "            \"(console de Hetzner) ; \"\n", ""),
    ("m04", "message de la mère : mauvais sélecteur", M, "label_selector=essai%3Dlean%2Cpas%3D{pas}",
     "label_selector=essai%3Dlean%2Cpas%3Dd1x"),
    ("m05", "message de la mère sans « ne jamais recréer »", M, " Ne jamais recréer de serveur.\")", "\")"),
    ("m06", "minuterie détachée sans --go ni --etiquette", M,
     "            \"--go\", go_id, \"--etiquette\", jeton, \"--journal\"", "            \"--journal\""),
    ("m07", "inventaire : adresses libres jamais rendues", M,
     "    return {\"serveurs_de_l_essai\": serveurs, \"ips_primaires_non_attribuees\": ips,",
     "    return {\"serveurs_de_l_essai\": serveurs, \"ips_primaires_non_attribuees\": [],"),
    ("m08", "acces-couper : règles posées sur un autre objet", M, "    client.poser_regles(ident, regles)",
     "    client.poser_regles(int(acces[\"cle_ssh\"][\"id\"]), regles)"),
    ("m09", "survie : aucune attente de la ligne « garder »", M, "DELAI_SURVIE_S = 120.0", "DELAI_SURVIE_S = 0.0"),
    ("m10", "veiller : absence sur une seule lecture", M, "        try:\n            if client.absence_confirmee(m.identifiant):",
     "        try:\n            if client.serveur(m.identifiant) is None:"),
    ("m11", "macOS : sortie de ps ignorée", M, "existe=_existe, ps=_ps,", "existe=_existe, ps=lambda pid: \"\","),
    ("m12", "verifier-minuterie : fraîcheur jamais contrôlée", M, "    if journal_minuterie is not None and res[\"vivante\"]:",
     "    if False:"),
    ("m13", "préparer : tâche de la mère jusqu'à 77 h", M,
     "    if heure_tache_mere > maintenant + timedelta(hours=TACHE_MERE_MAX_H):",
     "    if heure_tache_mere > maintenant + timedelta(hours=TACHE_MERE_MAX_H + 30):"),
    ("m14", "veiller : aucune ligne « garder » écrite", M,
     "        _ecrire(journal, {\"identifiant\": m.identifiant, \"detruire\": detruire, \"motif\": motif})\n        if detruire:",
     "        if detruire:"),
    ("m15", "client : 403 en lecture d'un serveur lu comme « absent »", H,
     "        if statut == 404:\n            return None\n        if statut in STATUTS_REFUS_DURABLE:\n"
     "            raise self._refus(\"GET\", f\"/servers/",
     "        if statut in (404, 403):\n            return None\n        if statut in STATUTS_REFUS_DURABLE:\n"
     "            raise self._refus(\"GET\", f\"/servers/"),
    ("m16", "creer-et-armer : heure limite ignorée", M, "    if horloge() > prep[\"heure_limite_creation\"]:", "    if False:"),
    # -- CLC5-07 : aucune donnée du poste ----------------------------------------------------------------------------------------
    ("g01", "adresse du poste au fichier d'accès", M,
     "              \"pare_feu\": pare_feu, \"etiquettes\": etiquettes, \"heure\": horloge().isoformat()}",
     "              \"pare_feu\": pare_feu, \"etiquettes\": etiquettes, \"heure\": horloge().isoformat(), \"ip_poste\": ip_poste}"),
    ("g02", "commentaire de la clé envoyé", M, "cle = client.creer_cle_ssh_etiquetee(nom, \" \".join(morceaux[:2]), etiquettes)",
     "cle = client.creer_cle_ssh_etiquetee(nom, texte, etiquettes)"),
    ("g03", "règles rendues par acces-couper", M, "    return {\"pare_feu\": ident, \"regles_posees\": len(regles),",
     "    return {\"pare_feu\": ident, \"regles_posees\": len(regles), \"regles\": regles,"),
    ("g04", "verifier-coupure non masqué", M,
     "            res[\"regles\"] = masquer_regles(res.get(\"regles\"))   # CLC5-07 : aucune adresse du poste au journal\n", ""),
    ("g05", "masque sans effet", M,
     "                r[cle] = [x if x == ADRESSE_DOCUMENTATION else \"<adresse masquée>\" for x in (r[cle] or [])]",
     "                r[cle] = list(r[cle] or [])"),
    ("g06", "chemins absolus rendus par la création", M,
     "    public.update({k: _relatif(minuterie[k], chemins[\"racine\"]) for k in (\"fichier_pid\", \"journal\", \"sortie\")",
     "    public.update({k: minuterie[k] for k in (\"fichier_pid\", \"journal\", \"sortie\")"),
    ("g07", "trace inattendue non masquée", M,
     "\"ERREUR INATTENDUE (code 1) :\\n\" + masquer_texte(traceback.format_exc(), racine)",
     "\"ERREUR INATTENDUE (code 1) :\\n\" + traceback.format_exc()"),
    ("g08", "chemin du clone dans le message du dépôt", M,
     "        raise GardeArret(\"dépôt introuvable (registres/go.md",
     "        raise GardeArret(f\"dépôt introuvable sous {racine} (registres/go.md"),
    ("g09", "garde-poste sans l'adresse", M,
     "    motifs = {\"adresse IPv4 du poste\": re.compile(r\"(?<![\\d.])\" + re.escape(ip_poste) + r\"(?![\\d])\")}",
     "    motifs = {}"),
    ("g10", "garde-poste sans les chemins", M,
     "    for nature, brut in ((\"dossier personnel\", str(Path.home())), (\"chemin du clone\", str(Path(racine).resolve()))):",
     "    for nature, brut in ():"),
    ("g11", "garde-poste toujours conforme", M, "        return 0 if not trouves else 1", "        return 0"),
    ("g12", "chemin absolu rendu par --detache", M, "    return {\"pid\": p.pid, \"sortie\": _relatif(sortie, racine),",
     "    return {\"pid\": p.pid, \"sortie\": str(sortie),"),
    ("g13", "adresse sans bornes de mot", M,
     "re.compile(r\"(?<![\\d.])\" + re.escape(ip_poste) + r\"(?![\\d])\")", "re.compile(re.escape(ip_poste))"),
    # -- notes : nom du pare-feu, branche distante, pilote ----------------------------------------------------------------------
    ("c01", "acces-couper sans relire le nom", M, "    if lu.get(\"name\") != acces[\"nom\"]:", "    if False:"),
    ("c02", "commit non comparé à la tête distante", M,
     "        if git(\"merge-base\", \"--is-ancestor\", commit, tete).returncode != 0:", "        if False:"),
    ("c03", "branche sans amont admise", M, "        if not commit or \"/\" not in amont:", "        if False:"),
    ("c04", "pilote : installation sans borne", P, "\"${S[@]}\" timeout 5400 bash /root/installer_chaine_v2.sh",
     "\"${S[@]}\" bash /root/installer_chaine_v2.sh"),
    ("c05", "pilote : connexion sans borne", P,
     "O=(-o BatchMode=yes -o ConnectTimeout=30 -o ServerAliveInterval=30 -o ServerAliveCountMax=4)", "O=(-o BatchMode=yes)"),
    ("c06", "branche distante absente non vue", M, "        if not tete:\n            return False, f\"branche {branche} absente",
     "        if False:\n            return False, f\"branche {branche} absente"),
    # -- empreinte de la mère, accès, adresse du serveur, commandes bornées, tâches -----------------------------------------------
    ("e01", "empreinte de la mère ignorée", M, "    if str(empreinte_mere).strip().lower() != empreinte:", "    if False:"),
    ("e02", "objets d'accès non liés au fichier poussé", M,
     "cles_ssh, pare_feux = [int(acces[\"cle_ssh\"][\"id\"])], [int(acces[\"pare_feu\"][\"id\"])]", "cles_ssh, pare_feux = [1], [2]"),
    ("e03", "fichier d'accès non exigé poussé", M, "    for fichier in (rattrapage, _chemin_acces(prep, chemins[\"verse\"])):",
     "    for fichier in (rattrapage,):"),
    ("e04", "adresse-serveur sans contrôle du nom", M,
     "    if s.get(\"name\") != NOM_MACHINE:\n        raise GardeArret(f\"serveur {ident} nommé {s.get('name')!r} : seul",
     "    if False:\n        raise GardeArret(f\"serveur {ident} nommé {s.get('name')!r} : seul"),
    ("e05", "detruire sans borne de temps", M, "            borne = dormir_borne(dormir, a.duree_max_s)", "            borne = dormir"),
    ("e06", "borne de temps sans effet", M, "        if cumul[0] + s > duree_max_s:", "        if False:"),
    ("e07", "code 5 confondu", M, "        return CODE_PANNE", "        return CODE_REFUS"),
    ("e08", "inventaire sans borne de temps", M,
     "            res = inventaire_essai(client, a.pas, j, dormir_borne(dormir, a.duree_max_s))",
     "            res = inventaire_essai(client, a.pas, j, dormir)"),
    ("e09", "deux tâches à la même heure", M, "DECALAGES_TACHES_H = (0.0, 0.5, 24.0)", "DECALAGES_TACHES_H = (0.0, 0.0, 24.0)"),
    ("e10", "session neuve non dite", M,
     "            2: \"tâche 2 sur 3, en session neuve : tu n'as pas d'autre mémoire que ce message\",",
     "            2: \"tâche 2 sur 3\","),
    ("e11", "message sans borne de temps de curl", M, "| curl -sS --max-time 30 ", "| curl -sS "),
    ("e12", "message sans conduite sur erreur passagère", M,
     "            \"(4) erreur passagère (délai, 429, 5xx) : réessayer trois fois en 15 minutes, puis prévenir Lazar ; \"\n",
     "            \"(4) \"\n"),
    ("e13", "ligne d'état sans rappel de Lazar", M, "<identifiants des trois tâches>. Rappel de Lazar : \"",
     "<identifiants des trois tâches>. \""),
    ("e14", "rappel de Lazar à H", M, "RAPPEL_LAZAR_H = 1.0", "RAPPEL_LAZAR_H = 0.0"),
    # -- mutations v5 encore pertinentes, sur la v6 --------------------------------------------------------------------------------
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
    ("n1", "autres noms non séparés", M, "    autres = [(i, n) for i, n in trouves if n != NOM_MACHINE]", "    autres = []"),
    ("n5", "statut 500 traité comme refus", H4, "        if 400 <= statut < 500:", "        if 400 <= statut <= 500:"),
    ("n8", "intention non exigée", M, "_ajouter_journal_creations(chemins[\"creations\"], entree, exige=True)",
     "_ajouter_journal_creations(chemins[\"creations\"], entree, exige=False)"),
    ("n9a", "déjà-dépensé = 0 (création)", M, "taux=taux, deja=deja[\"retenu\"],", "taux=taux, deja=0.0,"),
    ("n9b", "déjà-dépensé perdu (arguments)", M, "\"--deja-depense-usd\", repr(float(deja)),", "\"--deja-depense-usd\", \"0.0\","),
    ("n12", "inventaire de contrôle", M, "    if restants:\n        raise GardeArret(f\"serveurs {restants} encore",
     "    if False:\n        raise GardeArret(f\"serveurs {restants} encore"),
    ("n14", "pagination des étiquettes fixes", H4,
     "if d.get(\"meta\", {}).get(\"pagination\", {}).get(\"next_page\"):\n            raise GardeArret(\"plus de 50",
     "if False:\n            raise GardeArret(\"plus de 50"),
    ("n15a", "taux = 1,0 (création)", M, "echeance_h=echeance_h, taux=taux, deja=", "echeance_h=echeance_h, taux=1.0, deja="),
    ("n15b", "taux perdu (arguments)", M, "\"--taux-usd-eur\", repr(float(taux)),", "\"--taux-usd-eur\", \"1.0\","),
    ("n16", "devis non revérifié au démarrage", M, "            verifier_devis(prix, pas_long, deja)\n", ""),
    ("n17", "recherche par nom retirée", M, "    trouves = sorted(set(par_etiquettes) | set(par_nom))",
     "    trouves = sorted(set(par_etiquettes))"),
    ("n19", "jeton réutilisé admis", M4, "    if chemin.exists():\n        raise GardeArret(f\"{chemin} existe déjà : jeton réutilisé\")",
     "    pass"),
    ("n20", "plafond sans le déjà-dépensé", M, "    reste = PLAFONDS_MACHINE[pas_long] - deja", "    reste = PLAFONDS_MACHINE[pas_long]"),
    ("c01a", "forme `location`", H, "    lieu = _nom(s.get(\"location\"))", "    lieu = None"),
    ("c01b", "repli `datacenter.location`", H, "    lieu = _nom(dc.get(\"location\")) if isinstance(dc, dict) else None",
     "    lieu = None"),
    ("c01c", "repli `--lieu`", M, "            if type_lu and (lieu_lu or lieu):", "            if type_lu and lieu_lu:"),
    ("c01d", "démarrage sous retentatives", M, "        except Exception as e:  # noqa: BLE001 — démarrage retenté",
     "        except ZeroDivisionError as e:  # noqa: BLE001 — démarrage retenté"),
    ("c01e", "échéance passée sans lecture", M, "            if horloge() >= fin:", "            if False:"),
    ("c01f", "survie contrôlée", M, "        if not (survie[\"vivante\"] and survie[\"garder\"]):", "        if False:"),
    ("c01g", "ligne « garder » exigée", M, "        if not (survie[\"vivante\"] and survie[\"garder\"]):",
     "        if not survie[\"vivante\"]:"),
    ("c01h", "attente de la ligne « garder »", M, "        if vivante and lignes_garder(minuterie[\"journal\"]):",
     "        if vivante:"),
    ("c01j", "prix le plus haut", M, "            prix = max(candidats)", "            prix = candidats[0]"),
    ("c01k", "création lue plus tôt que --depuis", M,
     "    depuis_retenu = min(depuis, cree_a) if cree_a is not None else depuis", "    depuis_retenu = depuis"),
    ("c01l", "refus de nom au démarrage", M, "            if s.get(\"name\") != NOM_MACHINE:\n                _signaler",
     "            if False:\n                _signaler"),
    ("c01m", "lecture refusée au démarrage bornée", M,
     "            if refus >= refus_max:\n                raise DestructionRefusee(f\"lecture du serveur",
     "            if False:\n                raise DestructionRefusee(f\"lecture du serveur"),
    ("c03a", "racine écrite en dur", M, "    return Path(depot).resolve() if depot else Path(__file__).resolve().parents[3]",
     "    return Path(depot).resolve() if depot else Path(\"/home/user/controle-ia-travail\")"),
    ("c03b", "dépôt exigé", M, "    if exiger and not (c[\"go\"].is_file() and c[\"depenses\"].is_file()):", "    if False:"),
    ("c03c", "kill -0 avant ps", M,
     "        arguments = None if etat == \"absent\" else (ps(pid).split() if etat == \"présent\" else [])",
     "        arguments = ps(pid).split()"),
    ("c03d", "ps -ww", M, "[\"ps\", \"-ww\", \"-p\", str(pid), \"-o\", \"command=\"]", "[\"ps\", \"-p\", str(pid), \"-o\", \"command=\"]"),
    ("c03e", "kill -0 réel", M, "        os.kill(pid, 0)   # signal 0 : contrôle d'existence, rien n'est envoyé", "        pass"),
    ("c03f", "fraîcheur", M, "        if derniere is None or (horloge() - derniere).total_seconds() > fraicheur_s:",
     "        if derniere is None:"),
    ("c03g", "identifiant de la minuterie", M,
     "    return any(a == \"--identifiant\" and b == identifiant for a, b in zip(arguments, arguments[1:]))", "    return True"),
    ("c05c", "401 et 403 durables (requêtes)", H,
     "        if statut in STATUTS_REFUS_DURABLE:\n            raise self._refus(methode, chemin, statut)",
     "        if False:\n            raise self._refus(methode, chemin, statut)"),
    ("c05e", "code de sortie 3", M, "        return CODE_DESTRUCTION_REFUSEE", "        return CODE_REFUS"),
    ("c05f", "échecs écrits sans journal", M, "    if journal is not None:\n        _ecrire(journal, entree)\n        return",
     "    if True:\n        _ecrire(journal, entree)\n        return"),
    ("c06a", "bon nom d'abord", M, "    bons = [(i, n) for i, n in trouves if n == NOM_MACHINE]",
     "    bons = [] if any(n != NOM_MACHINE for _, n in trouves) else trouves"),
    ("c06b", "autres noms nommés à l'arrêt", M, "    if autres:\n        raise _arret_autres(detruits, autres)\n    return {\"trouves\"",
     "    if False:\n        raise _arret_autres(detruits, autres)\n    return {\"trouves\""),
    ("c07a", "solde après destruction", M, "                if solder is not None:\n                    try:\n                        solder(ident",
     "                if False:\n                    try:\n                        solder(ident"),
    ("c07c", "solde par la minuterie", M,
     "solder = fabrique_solder(c[\"creations\"], horloge, a.go, a.etiquette) if (a.go and a.etiquette) else None",
     "solder = None"),
    ("i02", "inventaire : adresses non attribuées seulement", H,
     "for x in d.get(\"primary_ips\", []) if x.get(\"assignee_id\") is None]", "for x in d.get(\"primary_ips\", [])]"),
    ("p02", "fichier de rattrapage poussé", M, "        if not pousse:", "        if False:"),
    ("p03", "échéance bornée par la tâche de la mère", M,
     "    echeance = min(depuis + timedelta(hours=ECHEANCES_H[pas_long]), limite)",
     "    echeance = depuis + timedelta(hours=ECHEANCES_H[pas_long])"),
    ("p04", "au moins une heure avant la tâche", M, "    if (limite - intention).total_seconds() / 3600.0 < ECHEANCE_MIN_H:",
     "    if False:"),
    ("p05", "préparer : heure limite passée", M, "    if heure_limite_creation <= maintenant:", "    if False:"),
    ("p06", "préparer : écart limite-tâche", M,
     "    if heure_tache_mere < heure_limite_creation + timedelta(hours=ECART_LIMITE_TACHE_H):", "    if False:"),
    ("p08", "nom du fichier et jeton", M,
     "    if chemin.name != f\"rattrapage-machine-{r['pas']}-{jeton[:12]}-v1.json\" or r.get(\"nom\") != NOM_MACHINE:",
     "    if False:"),
    ("p09", "GO du fichier", M, "    if go_id is not None and r.get(\"go\") != go_id:", "    if False:"),
    ("p10", "format du fichier", M, "    if not isinstance(r, dict) or r.get(\"format\") != FORMAT:", "    if not isinstance(r, dict):"),
    ("p11a", "git : suivi", M, "        if git(\"ls-files\", \"--error-unmatch\", \"--\", rel).returncode != 0:", "        if False:"),
    ("p11b", "git : égal à HEAD", M, "        if git(\"diff\", \"--quiet\", \"HEAD\", \"--\", rel).returncode != 0:", "        if False:"),
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
    ("p19", "message de la mère : autre nom", M,
     "            \"ne jamais toucher un serveur d'un autre nom (le signaler à Lazar) ; \"\n", ""),
    # -- R-2415 : lecture de la chaîne et de Mathlib par bac (installateur v2, pilote v7) ----------------------------------------
    ("l01", "garde de lisibilité toujours conforme (artefact 0600 admis)", I, "  [ -z \"$fautifs\" ] && return 0\n",
     "  return 0\n"),
    ("l02", "garde de lisibilité toujours en échec (cas sain refusé)", I, "  [ -z \"$fautifs\" ] && return 0\n",
     "  fautifs=${fautifs:-artefact}\n"),
    ("l03", "installateur : lecture pour tous retirée", I, "chmod -R a+rX /opt/elan /opt/mathlib /opt/pybac\n", ""),
    ("l04", "pilote : installateur v1 de nouveau", P, "timeout 5400 bash /root/installer_chaine_v2.sh",
     "timeout 5400 bash /root/installer_chaine_v1.sh"),
    ("l05", "lecture par l'utilisateur jamais refusée", I,
     "    runuser -u \"$u\" -- test -r \"$c\" || { echo \"$c : non lisible par $u\"; return 1; }\n", ""),
    ("l06", "pilote : scp sans enregistrement de la clé d'hôte", P,
     "C=(scp -i \"$CLE\" -o StrictHostKeyChecking=accept-new \"${O[@]}\")", "C=(scp -i \"$CLE\" \"${O[@]}\")"),
    ("l07", "pilote : cache du résolveur non vidé avant la sonde", P, "  \"${S[@]}\" timeout 60 resolvectl flush-caches\n", ""),
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
    shutil.copytree(racine / "scripts" / "lean_essai_d1a_v6", dest / "scripts" / "lean_essai_d1a_v6")
    shutil.copytree(racine / "scripts" / "lean_essai_d1a_v7", dest / "scripts" / "lean_essai_d1a_v7",
                    ignore=shutil.ignore_patterns("__pycache__"))
    for f in ("lean_essai_d1a_v1/installer_chaine_v1.sh", "lean_essai_d1a_v2/installer_chaine_v2.sh"):
        (dest / "scripts" / f).parent.mkdir(parents=True, exist_ok=True)
        shutil.copy2(racine / "scripts" / f, dest / "scripts" / f)


def env_propre() -> dict:
    retires = ("PYTHONPATH", "PYTHONHOME", "PYTHONSTARTUP", "HCLOUD_TOKEN")
    env = {k: v for k, v in os.environ.items() if k not in retires}
    env["PYTHONDONTWRITEBYTECODE"] = "1"
    return env


def borner_fichiers() -> None:
    resource.setrlimit(resource.RLIMIT_FSIZE, (100 * 2 ** 20, 100 * 2 ** 20))


def tracer_import(copie: Path) -> str:
    code = ("import sys; sys.path[:0] = [sys.argv[1] + '/src', sys.argv[1] + '/tests']; "
            "import controle_ia.lean_essai.minuterie_v6 as m, controle_ia.lean_essai.hetzner_v5 as h; "
            "print(m.__file__); print(h.__file__)")
    p = subprocess.run([sys.executable, "-I", "-B", "-c", code, str(copie)], capture_output=True, text=True,
                       env=env_propre(), cwd=copie, timeout=60)
    chemins = p.stdout.split()
    if p.returncode != 0 or len(chemins) != 2 or not all(c.startswith(str(copie)) for c in chemins):
        raise SystemExit(f"import non tracé vers la copie : {chemins!r} {p.stderr[-300:]}")
    return chemins[0]


def lancer_essais(copie: Path) -> tuple[int, str]:
    cmd = [sys.executable, "-B", "-m", "pytest", "-q", "-x", "-p", "no:cacheprovider", "-c", str(copie / "pyproject.toml"),
           "--rootdir", str(copie), "--basetemp", str(copie / "pytest-tmp"),
           "-o", f"pythonpath={copie / 'src'} {copie / 'tests'}"] + [str(copie / e) for e in ESSAIS]
    try:
        p = subprocess.run(cmd, capture_output=True, text=True, env=env_propre(), cwd=copie, timeout=240,
                           preexec_fn=borner_fichiers)
    except subprocess.TimeoutExpired:
        return -9, "délai dépassé (boucle sans fin) : enfant arrêté par son PID"
    lignes = [x for x in p.stdout.splitlines() if x.strip()]
    return p.returncode, (lignes[-1] if lignes else p.stderr[-200:])


def main(argv=None) -> int:
    argv = argv or sys.argv[1:]
    racine, travail = Path(argv[0]).resolve(), Path(argv[1]).resolve()
    ids = [m[0] for m in MUTATIONS]
    if len(ids) != len(set(ids)):
        raise SystemExit("identifiants de mutation en double")
    for ident, _d, fichier, ancien, _n in MUTATIONS:   # toutes applicables avant de commencer
        n = (racine / fichier).read_text(encoding="utf-8").count(ancien)
        if n != 1:
            raise SystemExit(f"{ident} inapplicable : {n} occurrence(s) dans {fichier}")
    travail.mkdir(parents=True, exist_ok=True)
    temoin = travail / "temoin"
    shutil.rmtree(temoin, ignore_errors=True)
    copier(racine, temoin)
    tracer_import(temoin)
    code, ligne = lancer_essais(temoin)
    resultats = [{"id": "témoin", "defaut": "aucune mutation", "code": code, "fin": ligne, "tuee": None}]
    if code != 0:
        print(json.dumps(resultats, ensure_ascii=False, indent=1))
        raise SystemExit("la copie témoin ne passe pas : mutations sans objet")
    shutil.rmtree(temoin)
    for ident, defaut, fichier, ancien, nouveau in MUTATIONS:
        copie = travail / ident
        shutil.rmtree(copie, ignore_errors=True)
        copier(racine, copie)
        cible = copie / fichier
        cible.write_text(cible.read_text(encoding="utf-8").replace(ancien, nouveau), encoding="utf-8")
        trace = tracer_import(copie)
        code, ligne = lancer_essais(copie)
        resultats.append({"id": ident, "defaut": defaut, "fichier": fichier, "import": trace.replace(str(travail), "<travail>"),
                          "code": code, "fin": ligne, "tuee": code != 0, "par_delai": code == -9})
        shutil.rmtree(copie)
    survivantes = [r["id"] for r in resultats if r["tuee"] is False]
    print(json.dumps({"mutations": len(MUTATIONS), "tuees": len(MUTATIONS) - len(survivantes), "survivantes": survivantes,
                      "par_delai": [r["id"] for r in resultats if r.get("par_delai")], "detail": resultats},
                     ensure_ascii=False, indent=1))
    return 0 if not survivantes else 1


if __name__ == "__main__":
    sys.exit(main())
