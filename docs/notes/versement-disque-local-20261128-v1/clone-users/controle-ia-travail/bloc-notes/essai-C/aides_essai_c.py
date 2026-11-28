"""Aides de la construction du commit d'essai C (bancs de la chaîne de P3, brouillon 2) : candidat d'essai, journal
synthétique de la répétition jouet, épingles de la copie versée des contrôles, borne d'essai du lanceur, correctifs
d'essai des scripts de l'instance. Chaque remplacement doit trouver son motif exactement une fois.
Usage : aides_essai_c.py candidat|journal|controles|lanceur|instance ARGS…"""
import sys
from pathlib import Path


def remplacer(texte: str, avant: str, apres: str) -> str:
    n = texte.count(avant)
    if n != 1:
        raise SystemExit(f"motif trouvé {n} fois (une attendue) : {avant[:80]!r}")
    return texte.replace(avant, apres)


def candidat(src, dst, k, sha_a, sha_i, n_tests, tel):
    t = Path(src).read_text(encoding="utf-8")
    t = remplacer(t, "\n\n- Auteur : ", "\n\n- Candidat d'essai du banc de la chaîne de P3 (brouillon 2), fabriqué dans un dépôt jetable du "
                  "bloc-notes : jamais versé au dépôt de travail, jamais scellé comme texte de P3 ; champs « [au candidat] » "
                  "nécessaires aux gardes remplis de valeurs d'essai.\n- Auteur : ")
    t = remplacer(t, "- Commit du code d'analyse : `[au candidat]`", f"- Commit du code d'analyse : `{k}`")
    t = remplacer(t, "`scripts/amorce_instance_p3.sh` (`[au candidat]`, sha256)", f"`scripts/amorce_instance_p3.sh` (`{sha_a}`, sha256)")
    t = remplacer(t, "`scripts/p3_instance.sh` (`[au candidat]`, sha256)", f"`scripts/p3_instance.sh` (`{sha_i}`, sha256)")
    t = remplacer(t, "- Tests attendus : `[au candidat]`", f"- Tests attendus : `{n_tests}`")
    t = remplacer(t, "plus `[au candidat, borne de inet_down_cost]` (CH-04, CH-10)",
                  f"plus {tel} USD par Go (valeur d'essai du banc ; CH-04, CH-10)")
    t = remplacer(t, "(`[au candidat]`) + disque arrêté 72 heures au plus (`[au candidat]`)",
                  f"(au plus {tel} USD par Go, valeur d'essai) + disque arrêté 72 heures au plus (valeur d'essai)")
    Path(dst).write_text(t, encoding="utf-8")


def journal(dst, k, nom_c, sha_c, nom_k, sha_k, sha_recup, sha_rep):
    artefacts = (("artefact-scores-manquants", "4c"), ("artefact-donnee-orpheline", "4c"),
                 ("artefact-ajout-hors-perimetre", "1c"), ("artefact-scores-alteres", "2b"),
                 ("artefact-sceau-des-scores-faux", "2b"), ("artefact-resultat-autre-manifeste", "2b"),
                 ("artefact-scores-hors-plan", "4d"), ("artefact-textes-incomplets", "4e"),
                 ("artefact-texte-hors-du-fichier-des-textes", "4f"), ("artefact-sondes-figees-incompletes", "5"),
                 ("artefact-figees-apres-episodes", "6d"), ("artefact-figees-apres-premier-episode", "6e"),
                 ("artefact-lot-manquant", "6f"), ("artefact-jeton-dans-une-trace", "7"),
                 ("artefact-copie-non-versee", "0"), ("artefact-versions-autres", "3f"), ("artefact-carte-autre", "6b"))
    L = [f"commit du code répété : {k}", f"candidat répété : {nom_c} {sha_c}", f"consignes répétées : {nom_k} {sha_k}",
         f"script répété : recuperation_p3_v1.sh {sha_recup}", f"script répété : repetition_jouet_p3_v1.sh {sha_rep}",
         "JOURNAL SYNTHÉTIQUE D'ESSAI (bancs de la chaîne de P3, brouillon 2) : aucune répétition jouée ; lignes écrites "
         "aux formes exigées par le module commun, pour les bancs des contrôles et du scellement seulement",
         "passage 1-sain : code 0 ; durée totale 0 s (synthétique)",
         "passage 2-artefact-branche-presente : code 2 ; durée totale 0 s (synthétique)",
         "passage 3-manque : code 1 ; durée totale 0 s (synthétique)",
         "récupération (passage-1-sain) : code 0 ; RÉCUPÉRATION : TOUS CONFORMES",
         "récupération (passage-3-traces-seules) : code 4 ; RÉCUPÉRATION DES TRACES SEULES (AUCUN RUN) : TOUS CONFORMES",
         "récupération (arret-synthetique-episodes) : code 0 ; RÉCUPÉRATION : TOUS CONFORMES",
         "    --  4d aucun résultat d'épisodes vérifié (synthétique)",
         "récupération (gardes-reelles) : code 0 ; RÉCUPÉRATION : TOUS CONFORMES"]
    for nom, prefixe in artefacts:
        L.append(f"récupération ({nom}) : code 1 ; RÉCUPÉRATION : 1 CONTRÔLE(S) EN ÉCHEC")
        L.append(f"    KO  {prefixe} contrôle en échec (synthétique)")
    L.append("FIN DE LA RÉPÉTITION")
    Path(dst).write_text("\n".join(L) + "\n", encoding="utf-8")


def controles(chemin, sha_c, sha_cfg, sha_k, rapports, k, sha_j, h_ancien, h_nouveau):
    t = Path(chemin).read_text(encoding="utf-8")
    t = remplacer(t, "\nCANDIDAT_RELU=A_EPINGLER ", f"\nCANDIDAT_RELU={sha_c} ")
    t = remplacer(t, "\nCONFIG_RELUE=A_EPINGLER ", f"\nCONFIG_RELUE={sha_cfg} ")
    t = remplacer(t, "\nCONSIGNES_RELUES=A_EPINGLER ", f"\nCONSIGNES_RELUES={sha_k} ")
    t = remplacer(t, '\nRAPPORTS_ATTENDUS="A_EPINGLER" ', f'\nRAPPORTS_ATTENDUS="{rapports}" ')
    t = remplacer(t, "\nCODE_RELU=A_EPINGLER ", f"\nCODE_RELU={k} ")
    t = remplacer(t, "\nREPETITION_JOUET=A_EPINGLER ", f"\nREPETITION_JOUET={sha_j} ")
    t = remplacer(t, f"\nH={h_ancien}\n", f"\nH={h_nouveau}\n")
    Path(chemin).write_text(t, encoding="utf-8")


def lanceur(chemin, tel):
    t = Path(chemin).read_text(encoding="utf-8")
    t = remplacer(t, "\nTELECHARGEMENT_MAX=A_FIXER ", f"\nTELECHARGEMENT_MAX={tel} ")
    Path(chemin).write_text(t, encoding="utf-8")


def instance(inst, amorce):
    t = Path(inst).read_text(encoding="utf-8")
    t = remplacer(t, "DELAI=(timeout --signal=TERM --kill-after=5m 270m)", "DELAI=(timeout --signal=TERM --kill-after=5m 300m)")
    t = remplacer(t, "donnees/*/scores-p3.npz.sha256 donnees/*/sondes-figees.npz.sha256; do",
                  "donnees/*/scores-p3.npz.sha256 donnees/*/sondes-figees.npz.sha256 donnees/*/jetons-principales-p3.npz \\\n"
                  "             donnees/*/jetons-principales-p3.npz.sha256 donnees/*/textes-actions-p3.jsonl \\\n"
                  "             donnees/*/textes-actions-p3.jsonl.sha256; do")
    Path(inst).write_text(t, encoding="utf-8")
    a = Path(amorce).read_text(encoding="utf-8")
    a = remplacer(a, "timeout --signal=TERM --kill-after=5m 330m ", "timeout --signal=TERM --kill-after=5m 360m ")
    a = remplacer(a, "donnees/*/scores-p3.npz.sha256 donnees/*/sondes-figees.npz.sha256; do [ -f \"$f\" ] && git add -f \"$f\"; done",
                  "donnees/*/scores-p3.npz.sha256 donnees/*/sondes-figees.npz.sha256 donnees/*/jetons-principales-p3.npz \\\n"
                  "                 donnees/*/jetons-principales-p3.npz.sha256 donnees/*/textes-actions-p3.jsonl \\\n"
                  "                 donnees/*/textes-actions-p3.jsonl.sha256; do [ -f \"$f\" ] && git add -f \"$f\"; done")
    Path(amorce).write_text(a, encoding="utf-8")


if __name__ == "__main__":
    action, args = sys.argv[1], sys.argv[2:]
    {"candidat": candidat, "journal": journal, "controles": controles, "lanceur": lanceur, "instance": instance}[action](*args)
