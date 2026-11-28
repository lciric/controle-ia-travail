"""Aides de la construction du commit d'essai des bancs de la chaîne de P3, brouillon 3 : candidat d'essai (le candidat 1
de la session, plus les formes exactes des décisions 1 à 3 de la relecture courte), journal synthétique de la répétition
jouet, épingles de la copie versée des contrôles. Chaque remplacement doit trouver son motif exactement une fois.
Usage : aides_essai_b3.py candidat|journal|controles ARGS…"""
import sys
from pathlib import Path


def remplacer(texte: str, avant: str, apres: str) -> str:
    n = texte.count(avant)
    if n != 1:
        raise SystemExit(f"motif trouvé {n} fois (une attendue) : {avant[:80]!r}")
    return texte.replace(avant, apres)


def candidat(src, dst):
    t = Path(src).read_text(encoding="utf-8")
    t = remplacer(t, "\n\n- Auteur : ", "\n\n- Candidat d'essai des bancs de la chaîne de P3 (brouillon 3), fabriqué dans un dépôt jetable du "
                  "bloc-notes à partir du candidat 1 : jamais versé au dépôt de travail, jamais scellé comme texte de P3 ; seules "
                  "changent les formes exactes de la révocation de R-192, de l'accord de Lazar et la borne de stockage "
                  "(relecture courte, décisions 1 à 3 de la session).\n- Auteur : ")
    t = remplacer(t, "consigné au registre\n    des décisions par une ligne datée du jour qui contient « accord de Lazar », « P3 » et « lancement » ;",
                  "consigné au registre\n    des décisions par une ligne datée du jour dont la cellule de décision commence exactement par\n"
                  "    « **Accord de Lazar pour le lancement de P3** » ;")
    t = remplacer(t, "Révocation de R-192\n    (CH-09) : une ligne de type « révocation » du registre des GO qui nomme R-192 sans nommer d'autre GO, ou une ligne R-… du\n"
                     "    registre des décisions qui « révoque », « retire » ou « annule » R-192 ; l'une ou l'autre présente, la chaîne refuse de\n    lancer.",
                  "Révocation de R-192\n    (CH-09, RCh-01) : une ligne du registre des GO de type « révocation » dont le périmètre nomme R-192 ou\n"
                  "    GO-2026-10-04-08, ou une ligne du registre des décisions dont la cellule de décision commence exactement par\n"
                  "    « **Révocation de R-192** » ; rien d'autre ; l'une ou l'autre présente, la chaîne refuse de lancer.")
    t = remplacer(t, "`registres/depenses.md` l. 26 au commit `03cb538`) ; l'offre conforme la moins chère est prise à la création",
                  "`registres/depenses.md` l. 26 au commit `03cb538`), stockage au plus 0,03 USD de l'heure\n"
                  "   (`storage_total_cost`, RCh-04) ; l'offre conforme la moins chère est prise à la création")
    t = remplacer(t, "   - crédit exigé à la création : 6,5 heures × (prix de l'offre + prix des autres projets en marche) + 1,2 USD ;",
                  "   - crédit exigé à la création : 6,5 heures × (prix de l'offre + prix des autres projets en marche) + 1,2 USD (le disque\n"
                  "     de l'instance arrêtée repose sur la recharge automatique du compte) ;")
    Path(dst).write_text(t, encoding="utf-8")


def journal(dst, k, nom_c, sha_c, nom_k, sha_k, sha_recup, sha_rep):
    artefacts = (("artefact-scores-manquants", "4c"), ("artefact-donnee-orpheline", "4c"),
                 ("artefact-ajout-hors-perimetre", "1c"), ("artefact-scores-alteres", "2b"),
                 ("artefact-sceau-des-scores-faux", "2b"), ("artefact-resultat-autre-manifeste", "2b"),
                 ("artefact-scores-hors-plan", "4d"), ("artefact-textes-incomplets", "4e"),
                 ("artefact-texte-hors-du-fichier-des-textes", "4f"), ("artefact-texte-echappe-dans-un-resultat", "4f"),
                 ("artefact-sondes-figees-incompletes", "5"),
                 ("artefact-figees-apres-episodes", "6d"), ("artefact-figees-apres-premier-episode", "6e"),
                 ("artefact-lot-manquant", "6f"), ("artefact-jeton-dans-une-trace", "7"),
                 ("artefact-copie-non-versee", "0"), ("artefact-versions-autres", "3f"), ("artefact-carte-autre", "6b"))
    L = [f"commit du code répété : {k}", f"candidat répété : {nom_c} {sha_c}", f"consignes répétées : {nom_k} {sha_k}",
         f"script répété : recuperation_p3_v1.sh {sha_recup}", f"script répété : repetition_jouet_p3_v1.sh {sha_rep}",
         "JOURNAL SYNTHÉTIQUE D'ESSAI (bancs de la chaîne de P3, brouillon 3) : aucune répétition jouée ; lignes écrites "
         "aux formes exigées par le module commun, pour les bancs des contrôles et du scellement seulement",
         "passage 1-sain : code 0 ; durée totale 0 s (synthétique)",
         "passage 2-artefact-branche-presente : code 2 ; durée totale 0 s (synthétique)",
         "passage 3-manque : code 1 ; durée totale 0 s (synthétique)",
         "récupération (passage-1-sain) : code 0 ; RÉCUPÉRATION : TOUS CONFORMES",
         "récupération (passage-3-traces-seules) : code 4 ; RÉCUPÉRATION DES TRACES SEULES (AUCUN RUN) : TOUS CONFORMES",
         "récupération (arret-synthetique-episodes) : code 0 ; RÉCUPÉRATION : TOUS CONFORMES",
         "    --  4d aucun résultat d'épisodes vérifié (synthétique)",
         "récupération (gardes-reelles) : code 0 ; RÉCUPÉRATION : TOUS CONFORMES",
         "récupération (texte-degenere-repete) : code 0 ; RÉCUPÉRATION : TOUS CONFORMES"]
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


if __name__ == "__main__":
    action, args = sys.argv[1], sys.argv[2:]
    {"candidat": candidat, "journal": journal, "controles": controles}[action](*args)
