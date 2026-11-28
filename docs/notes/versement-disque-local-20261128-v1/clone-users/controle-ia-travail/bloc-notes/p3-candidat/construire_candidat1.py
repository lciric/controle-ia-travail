"""Candidat 1 du préenregistrement de P3, tiré du brouillon 4 : champs « [au candidat] » remplis, nœud T4 tranché (R-203),
parties restantes du traitement de la chaîne tranchées (R-215). Chaque remplacement doit trouver son motif une seule fois.
Usage : python3 -I construire_candidat1.py BROUILLON4 SORTIE TESTS_ATTENDUS"""
import sys
from pathlib import Path

C1 = "03cb53804e0b98fe671b62ebf5ef2d819741e282"
SHA_AMORCE = "0bfaeaa64a0c355ba04bf84c9afc76ea31034a837e44cd588becf88f3aa5dae0"
SHA_INSTANCE = "2bfc6939efe8b68d17b921e0ea8b91e2809b04e5c37006c18364dc4776dc3663"
SHA_GARDES = "cf4ab7b841a5599a23b01255a32d8e378200751c2472176892a7e02a5df956b3"
SHA_TRAITEMENT_CH = "ad1d88d27dca0d4acfdbaed3238b179ea923574dd4abcf0811c5c025cb0e12ca"


def remplacer(t: str, avant: str, apres: str) -> str:
    n = t.count(avant)
    if n != 1:
        raise SystemExit(f"motif trouvé {n} fois (une attendue) : {avant[:90]!r}")
    return t.replace(avant, apres)


def main(src: str, dst: str, tests: str) -> None:
    assert tests.isdigit()
    t = Path(src).read_text(encoding="utf-8")
    t = remplacer(
        t,
        "- Auteur : la session de mise en œuvre du programme de Lazar (session 15, Claude). Brouillon 4 du 2026-10-17, à relire (relecture\n"
        "  courte du traitement par un sous-agent neuf, R2) : il remplace le brouillon 3 (`brouillons/P3-premier-test-i-a-v1-brouillon3.md`,\n"
        "  `a9e85fabd5b23c0eff6da726c4f16f6adf3d722e21e8827719e756671bf67cac`, gardé tel quel, R12) et traite ses deux contre-lectures R2\n"
        "  (section « Contre-lecture ») et les décisions de Lazar du 17 octobre (R-202). Les champs marqués « [au candidat] » se remplissent\n"
        "  au candidat relu, avant le scellement (le texte scellé sera la copie, octet pour octet, du candidat relu).",
        "- Auteur : la session de mise en œuvre du programme de Lazar (Claude ; brouillons 1 à 4 par la session 15, candidat 1 par la\n"
        "  session 14). Candidat 1 du 2026-10-19, tiré du brouillon 4 (`brouillons/P3-premier-test-i-a-v1-brouillon4.md`,\n"
        "  `94e5ff12b45437760638309fe88031b181d7e49d0a49810b8525e12eebc7383b`, gardé tel quel, R12), qui remplaçait le brouillon 3\n"
        "  (`brouillons/P3-premier-test-i-a-v1-brouillon3.md`, `a9e85fabd5b23c0eff6da726c4f16f6adf3d722e21e8827719e756671bf67cac`) :\n"
        "  il traite les deux contre-lectures R2 du brouillon 3 (section « Contre-lecture ») et les décisions de Lazar du 17 octobre\n"
        "  (R-202, R-203), et remplit les champs que le brouillon 4 laissait « au candidat » (changements : ci-dessous). Le texte scellé\n"
        "  sera la copie, octet pour octet, du candidat relu.")
    t = remplacer(t, "- Commit du code d'analyse : `[au candidat]`", f"- Commit du code d'analyse : `{C1}`")
    t = remplacer(t, "`scripts/amorce_instance_p3.sh` (`[au candidat]`, sha256)", f"`scripts/amorce_instance_p3.sh` (`{SHA_AMORCE}`, sha256)")
    t = remplacer(t, "`scripts/p3_instance.sh` (`[au candidat]`, sha256)", f"`scripts/p3_instance.sh` (`{SHA_INSTANCE}`, sha256)")
    t = remplacer(t, "- Tests attendus : `[au candidat]`", f"- Tests attendus : `{tests}`")
    t = remplacer(
        t,
        "l'identifiant de cette ligne et la relit (CH-11) ; le seul GO accepté est GO-2026-10-04-08 (CH-02).",
        "l'identifiant de cette ligne et la relit (CH-11) ; le seul GO accepté est GO-2026-10-04-08 (CH-02). Révocation de R-192\n"
        "    (CH-09) : une ligne de type « révocation » du registre des GO qui nomme R-192 sans nommer d'autre GO, ou une ligne R-… du\n"
        "    registre des décisions qui « révoque », « retire » ou « annule » R-192 ; l'une ou l'autre présente, la chaîne refuse de\n"
        "    lancer.")
    t = remplacer(
        t,
        "Lazar le 17 octobre : T4 retenu ou retiré\n    au candidat]**.",
        "Lazar le 17 octobre et retenu (R-203)**.")
    t = remplacer(
        t,
        "écrite dans les résultats. Aucun autre fichier poussé ne porte de texte d'action.",
        "écrite dans les résultats. Aucun autre fichier poussé ne porte de texte d'action ; la récupération le contrôle (CH-18) :\n"
        "  chaînes de 200 caractères au plus dans les résultats, le manifeste et `run.json` (1 000 pour le motif d'un arrêt, affiché\n"
        "  borné à 200), et textes d'action de 64 caractères ou plus cherchés (48 caractères de leur milieu) dans tous les autres\n"
        "  fichiers ajoutés.")
    t = remplacer(
        t,
        "téléchargement au\n   plus `[au candidat, borne de inet_down_cost]` (CH-04, CH-10) ;",
        "téléchargement au\n   plus 0,05 USD par Go (CH-04, CH-10 ; relevés : 0,026 USD par Go à l'offre du pilote,\n"
        "   `traces/t05-pilote-v1-20261012-1035/offre.json`, `4f1eee6457818f4a5019aba35a9b3eb10f42e9d9173cc629623ee4b84083acc0` ;\n"
        "   0,039 USD par Go à l'offre 29019328, `registres/depenses.md` l. 26 au commit `03cb538`) ;")
    t = remplacer(
        t,
        "+ téléchargement\n     (`[au candidat]`) + disque arrêté 72 heures au plus (`[au candidat]`), sous GO-2026-10-04-08 ;",
        "+ téléchargement\n     (≈ 20 Go relevés à l'offre 29019328, même registre, même ligne : au plus ≈ 1,00 USD à la borne) + disque arrêté\n"
        "     72 heures au plus (stockage à 0,022 et 0,027 USD de l'heure aux deux offres relevées : au plus ≈ 1,94 USD à ce prix ; prix\n"
        "     de stockage de l'offre retenue consigné à la création), soit au plus ≈ 11,2 USD, sous GO-2026-10-04-08 ; l'instance arrêtée\n"
        "     est détruite par son identifiant (R10), au plus 72 heures après son arrêt, une fois la récupération faite ;\n"
        "   - instances au lancement (CH-13, CH-17) : aucune instance du programme sur le compte (les quatre de la liste fermée du\n"
        "     lanceur, 55292763, 55458787, 55538944 et 56438435, sont détruites : R-212, R-214) ; seules sont tolérées les instances\n"
        "     d'autres projets de Lazar, d'étiquette « rr- », comptées dans le crédit exigé ;")
    t = remplacer(
        t,
        "Scripts de session, brouillon 2 (`brouillons/P3-chaine-v1-brouillon2/`, `[au candidat]`), versés sous",
        "Scripts de session, brouillon 2 (`brouillons/P3-chaine-v1-brouillon2/`, quatorze fichiers scellés au commit `03cb538`), versés sous")
    t = remplacer(t, "contrôle à cinq minutes `[au candidat]` (CH-23)", "contrôle à cinq minutes `controle_cinq_minutes_p3_v1.sh` (CH-23)")
    t = remplacer(
        t,
        "`repetition_jouet_p3_v1.sh`, répétition finale `repetition_finale_p3_v1.sh`, et les bancs (cas sain et artefacts, R5). Ordre :",
        "`repetition_jouet_p3_v1.sh`, répétition finale `repetition_finale_p3_v1.sh`, et les bancs (cas sain et artefacts, R5). Les copies\n"
        "versées ne diffèrent du brouillon 2 que par les épingles des contrôles (candidat, configuration et consignes relus, rapports,\n"
        "code relu, journal de la répétition jouet) et leur ligne H, la borne de téléchargement du lanceur (0.05) et la ligne de session\n"
        "du message de commit du scellement. Ordre :")
    t = remplacer(
        t,
        "  - TC-11 : `[au candidat : tests des gardes listées, fichier et compte]` ;",
        f"  - TC-11 : `tests/test_premier_test_ia_gardes_v1.py` (`{SHA_GARDES}`), 20 tests, un par\n"
        "    garde listée (cas sain et artefact, R5), au commit du code ;")
    t = remplacer(t, "(d) `[au candidat]` ;", "(d) docstring du paquet corrigée au commit du code ;")
    t = remplacer(
        t,
        "- **Traitement des constats de la chaîne** : `[au candidat : tableau CH-01 à CH-24, chaîne brouillon 2]`.",
        f"- **Traitement des constats de la chaîne** : `brouillons/P3-chaine-v1-brouillon2/traitement-CH-v1.md` (`{SHA_TRAITEMENT_CH}`),\n"
        "  écrit par un sous-agent neuf, rédacteur de la chaîne : 19 corrigés, 4 corrigés en partie (CH-09, CH-10, CH-17, CH-18),\n"
        "  0 non corrigé, CH-24 sans objet. Les quatre parties restantes sont tranchées par ce texte (R-215) : forme d'une révocation\n"
        "  de R-192 (CH-09, en-tête) ; borne de téléchargement et montants de l'étape (CH-10, Plan d'analyse, point 4) ; instances au\n"
        "  lancement (CH-17, même point) ; contrôle des textes d'action (CH-18, Métrique). Défauts hors de la chaîne relevés par le\n"
        "  rédacteur, corrigés au commit du code : délais des scripts de l'instance (300 et 360 minutes, au lieu de 270 et 330) et\n"
        "  poussée des données brutes (scores par jeton, textes des actions) ; test du plafond de l'amorce ajouté (cas sain et\n"
        "  artefact, R5).")
    t = remplacer(
        t,
        "- **Relecture courte du traitement** : `[à faire : sous-agent neuf ; fichiers donnés explicitement ; rapport (chemin et\n"
        "  empreinte)]`.",
        "- **Relecture courte du traitement** : `[après la relecture courte : rapport (chemin et empreinte) et son traitement]`.")
    t = remplacer(
        t,
        "brouillon 2.\n\n## Hypothèse",
        "brouillon 2.\n\n**Changements depuis le brouillon 4** (candidat 1) : champs « au candidat » remplis (commit du code `03cb538`, empreintes\n"
        "des scripts de l'instance, tests attendus, borne de téléchargement et montants de l'étape, chaîne et contrôle à cinq minutes,\n"
        "TC-11, TC-20 (d), traitement des constats de la chaîne) ; T4 retenu (R-203) ; parties restantes du traitement de la chaîne\n"
        "tranchées (R-215) ; instances au lancement (R-212, R-214) ; scripts de l'instance alignés sur ce texte et poussée des données\n"
        "brutes, au commit du code.\n\n## Hypothèse")
    assert "[au candidat" not in t and "`[au candidat]`" not in t, "champ au candidat restant"
    Path(dst).write_text(t, encoding="utf-8")


if __name__ == "__main__":
    main(*sys.argv[1:4])
