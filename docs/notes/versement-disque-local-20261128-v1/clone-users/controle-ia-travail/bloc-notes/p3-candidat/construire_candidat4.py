"""Candidat 4 du préenregistrement de P3, tiré du candidat 3 (R-227) : la borne de stockage tient sur une ligne (premier banc
officiel des contrôles, cas A44l), la chaîne passe au brouillon 4 (copies versées sous docs/procedures/P3-premier-test-v2/,
R12), et VE3-01, VE3-02 sont repris. Chaque remplacement doit trouver son motif une seule fois.
Usage : python3 -I construire_candidat4.py CANDIDAT3 SORTIE EMPREINTE_TRAITEMENT_DU_BANC"""
import sys
from pathlib import Path


def remplacer(t: str, avant: str, apres: str) -> str:
    n = t.count(avant)
    if n != 1:
        raise SystemExit(f"motif trouvé {n} fois (une attendue) : {avant[:90]!r}")
    return t.replace(avant, apres)


def main(src: str, dst: str, sha_traitement: str) -> None:
    t = Path(src).read_text(encoding="utf-8")
    # en-tête (VE3-02)
    t = remplacer(
        t,
        "- Auteur : la session de mise en œuvre du programme de Lazar (Claude ; brouillons 1 à 4 par la session 15, candidats 1 à 3\n"
        "  par la session 14). Candidat 3 du 2026-10-19, tiré du candidat 2 (`brouillons/P3-premier-test-i-a-v1-candidat2.md`,\n"
        "  `57e0d473596611b65978002a55ba15c189dd21d05058f088da08ba45b6e42a53`, gardé tel quel, R12), lui-même tiré du candidat 1\n"
        "  (`brouillons/P3-premier-test-i-a-v1-candidat1.md`, `8070b64085ae649c68b79222fdfbb1aea1fc7e99edc5510822ea387b82805dd0`)\n"
        "  et du brouillon 4 (`brouillons/P3-premier-test-i-a-v1-brouillon4.md`,\n"
        "  `94e5ff12b45437760638309fe88031b181d7e49d0a49810b8525e12eebc7383b`) : il traite la contre-lecture R2 du brouillon 3 et du\n"
        "  code, celle de la chaîne (brouillon 1), la relecture courte du traitement (trois relecteurs neufs, R-218), la relecture de\n"
        "  l'écart du candidat 2 (sous-agent neuf, R-218, point 4) et les décisions de Lazar du 17 octobre (R-202, R-203) ;\n"
        "  changements : ci-dessous. Le texte scellé sera la copie, octet pour octet, du candidat relu.",
        "- Auteur : la session de mise en œuvre du programme de Lazar (Claude ; brouillons 1 à 4 par la session 15, candidats 1 à 4\n"
        "  par la session 14). Candidat 4 du 2026-10-19, tiré du candidat 3 (`brouillons/P3-premier-test-i-a-v1-candidat3.md`,\n"
        "  `3682c254ee93ebf2ce183ba925e362344bd80e08cce092af2508586aec589d86`, gardé tel quel, R12) ; le candidat 3 était tiré du\n"
        "  candidat 2 (`brouillons/P3-premier-test-i-a-v1-candidat2.md`,\n"
        "  `57e0d473596611b65978002a55ba15c189dd21d05058f088da08ba45b6e42a53`), le candidat 2 du candidat 1\n"
        "  (`brouillons/P3-premier-test-i-a-v1-candidat1.md`, `8070b64085ae649c68b79222fdfbb1aea1fc7e99edc5510822ea387b82805dd0`),\n"
        "  et le candidat 1 du brouillon 4 (`brouillons/P3-premier-test-i-a-v1-brouillon4.md`,\n"
        "  `94e5ff12b45437760638309fe88031b181d7e49d0a49810b8525e12eebc7383b`). Ce texte traite la contre-lecture R2 du brouillon 3\n"
        "  et du code, celle de la chaîne (brouillon 1), la relecture courte du traitement (trois relecteurs neufs, R-218), la\n"
        "  relecture de l'écart du candidat 2 (sous-agent neuf, R-218, point 4), le premier banc officiel des contrôles (R-227) et\n"
        "  les décisions de Lazar du 17 octobre (R-202, R-203) ; changements : ci-dessous. Le texte scellé sera la copie, octet pour\n"
        "  octet, du candidat relu.")
    # ligne « Lancement » : dossier des copies versées
    t = remplacer(t, "lanceur de session `docs/procedures/P3-premier-test-v1/lancer_p3_v1.sh`",
                  "lanceur de session `docs/procedures/P3-premier-test-v2/lancer_p3_v1.sh`")
    # changements depuis le candidat 2 (VE3-02) puis depuis le candidat 3
    t = remplacer(
        t,
        "versions (VE-06) ; relecture de l'écart dans l'ordre de la chaîne, nom du candidat relu dans les copies versées des contrôles\n"
        "(VE-07) ; sources de la durée attendue citées (VE-08).",
        "versions (VE-06) ; relecture de l'écart dans l'ordre de la chaîne, nom du candidat relu dans les copies versées des contrôles\n"
        "(VE-07) ; sources de la durée attendue citées (VE-08) ; entrée « Relecture de l'écart » ajoutée à la section « Contre-lecture ».\n"
        "\n"
        "**Changements depuis le candidat 3** (candidat 4, R-227) : la borne de stockage tient sur une ligne (le banc des contrôles\n"
        "fabrique l'artefact « texte sans la borne de stockage » ligne par ligne ; au candidat 3, la phrase était coupée, l'artefact\n"
        "n'était pas fabriqué et le premier banc officiel rendait un cas non conforme, A44l) ; chaîne en brouillon 4 (copies versées\n"
        "sous `docs/procedures/P3-premier-test-v2/`, R12 ; chemin du candidat relu écrit dans la chaîne) ; en-tête et entrée de la\n"
        "relecture de l'écart précisés (VE3-01, VE3-02).")
    # borne de stockage sur une ligne (A44l)
    t = remplacer(
        t,
        "   phase 0), au moins 16 cœurs effectifs (`cpu_cores_effective`) et 128 000 Mo de mémoire vive (`cpu_ram`), stockage au plus\n"
        "   0,03 USD de l'heure (RCh-04), téléchargement au plus 0,05 USD par Go (CH-04, CH-10 ;\n",
        "   phase 0), au moins 16 cœurs effectifs (`cpu_cores_effective`) et 128 000 Mo de mémoire vive (`cpu_ram`),\n"
        "   stockage au plus 0,03 USD de l'heure (RCh-04), téléchargement au plus 0,05 USD par Go (CH-04, CH-10 ;\n")
    # chaîne de lancement : brouillon 4, dossier v2
    t = remplacer(
        t,
        "Scripts de session, brouillon 3 (`brouillons/P3-chaine-v1-brouillon3/`, quatorze fichiers scellés au commit `ffdbcda`,\n"
        "dont le traitement de la relecture courte, `traitement-relecture-courte-v1.md`,\n"
        "`31e00a19cc6f22e8ec9cd6821af71a841e8f14bbf4571d768d75a9bb2a66ebab`), versés sous\n"
        "`docs/procedures/P3-premier-test-v1/` avant S,",
        "Scripts de session, brouillon 4 (`brouillons/P3-chaine-v1-brouillon4/`, quatorze fichiers scellés, dont le traitement du\n"
        f"premier banc officiel des contrôles, `traitement-banc-controles-v1.md`, `{sha_traitement}`), égal au\n"
        "brouillon 3 (`brouillons/P3-chaine-v1-brouillon3/`, scellé au commit `ffdbcda`, dont le traitement de la relecture courte,\n"
        "`traitement-relecture-courte-v1.md`, `31e00a19cc6f22e8ec9cd6821af71a841e8f14bbf4571d768d75a9bb2a66ebab`) sauf le dossier\n"
        "des copies versées et le chemin du candidat relu des contrôles ; versés sous `docs/procedures/P3-premier-test-v2/` avant S\n"
        "(le versement du dossier `docs/procedures/P3-premier-test-v1/`, au commit `be7658d`, est abandonné et gardé tel quel,\n"
        "R12),")
    t = remplacer(
        t,
        "Les copies\n"
        "versées ne diffèrent du brouillon 3 que par les valeurs « A_EPINGLER » des contrôles (candidat, configuration et consignes\n"
        "relus, rapports, code relu, journal de la répétition jouet) et par le chemin du candidat relu des contrôles,\n"
        "`CANDIDAT_RELU_CHEMIN` (`brouillons/P3-premier-test-i-a-v1-candidat3.md` : ce candidat, nommé après la relecture de l'écart,\n"
        "R12). Ordre :",
        "Les copies\n"
        "versées ne diffèrent du brouillon 4 que par les valeurs « A_EPINGLER » des contrôles (candidat, configuration et consignes\n"
        "relus, rapports, code relu, journal de la répétition jouet). Ordre :")
    # contre-lecture : relecture de l'écart (VE3-01), vérification des corrections, banc officiel
    t = remplacer(
        t,
        "  majeur, trois mineurs (VE-01 à VE-03), cinq pour information (VE-04 à VE-08), tous traités dans ce candidat 3 ; code\n"
        "  `7a54d43` et chaîne en brouillon 3 versables tels quels. Les corrections sont vérifiées par le même sous-agent avant le\n"
        "  versement : rapport `prereg/contre-lectures/verification-ecart-P3-candidat3-v1.md`, cité avec son empreinte au registre\n"
        "  des décisions.",
        "  majeur, trois mineurs (VE-01 à VE-03), cinq pour information (VE-04 à VE-08), tous traités au candidat 3 ; code `7a54d43`\n"
        "  et chaîne en brouillon 3 versables, avec le chemin du candidat relu changé dans les copies versées (VE3-01). Corrections\n"
        "  vérifiées par le même sous-agent : `prereg/contre-lectures/verification-ecart-P3-candidat3-v1.md`\n"
        "  (`e3a1b7ca7c2b319cd7a1c1af72e6bc281a4c3689348bfe1324bfcd878051a02b`), « versable » (VE3-01, VE3-02 pour information,\n"
        "  repris au candidat 4).\n"
        "- **Premier banc officiel des contrôles** (R-227) : au commit des préalables `be7658d`, un cas non conforme (A44l), dû à la\n"
        "  phrase de la borne de stockage coupée au candidat 3 ; les trois autres bancs conformes ; traité par ce candidat 4 et la\n"
        "  chaîne en brouillon 4 ; l'écart (candidat 3 au candidat 4, brouillon 3 au brouillon 4) est relu par le même sous-agent :\n"
        "  rapport `prereg/contre-lectures/verification-ecart-P3-candidat4-v1.md`, cité avec son empreinte au registre des décisions.")
    assert "[au candidat" not in t and "[après la relecture" not in t
    assert "docs/procedures/P3-premier-test-v1/lancer" not in t
    Path(dst).write_text(t, encoding="utf-8")


if __name__ == "__main__":
    main(*sys.argv[1:4])
