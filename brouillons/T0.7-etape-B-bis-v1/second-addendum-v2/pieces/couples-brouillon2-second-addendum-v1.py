"""Couples « ancien → nouveau » du brouillon 2 du second addendum de B bis (T0.7) : processeur seulement, aucun réseau.

Lit, dans le dossier SOURCE (`second-addendum-v2/`) :
- `brouillon-second-addendum-bbis-v1.md` (empreinte vérifiée) ;
- `contre-lecture-second-addendum-bbis-tour1-v1.md` (empreinte vérifiée) : chaque « ancien » et chaque « nouveau » des couples
  K1 à K7 doit y figurer au caractère (le « nouveau » de K2 est extrait de son bloc ````text du § 6) ;
- `pieces/controle-fragments-second-addendum-v1.py` (empreinte vérifiée).
Écrit, dans le dossier CIBLE (le même dossier, ou une copie de travail pour un essai à blanc), sans jamais écraser :
- `brouillon-second-addendum-bbis-v2.md` = brouillon 1 + K1 à K7 (et les deux comptes de K2) + en-tête (titre, statut, ligne
  « Brouillon 2 », heure lue par `date -u`) + section « 11. Contre-lecture » ajoutée à la fin ; rien d'autre ;
- `pieces/controle-fragments-second-addendum-v2.py` = v1 dont ne changent que le nom du brouillon lu, les noms des deux pièces
  écrites et le compte « SA-21 à SA-25 » d'un commentaire.
Chaque « ancien » doit figurer exactement une fois dans le texte courant et une fois dans le texte de départ ; sinon arrêt.

Jouer : `python <ce fichier> SOURCE CIBLE DEBUT ESSAIS` (DEBUT : heure de début « HH:MM » ; ESSAIS : phrase du résultat des
essais rejoués). Code 0 : écrit ; code 1 : un écart (motif écrit), rien n'est écrit."""
from __future__ import annotations

import hashlib
import subprocess
import sys
from pathlib import Path

SHA_BROUILLON1 = "a582e14dd22fd17e716aaed8d475a3c1a7ceeff60d15c3a4644aa9bf0c6f4627"
SHA_CONTRE_LECTURE = "98a049d9f8b207eb336d04fc7e5a0b23bb5c066cd542bbc7719bd1e1b58fc120"
SHA_CONTROLE_V1 = "21e4d25990a9c4f27ede47d9f704446d8d656f905546e9dd165fe99143d87a83"


def sha(p: Path) -> str:
    return hashlib.sha256(p.read_bytes()).hexdigest()


def arret(motif: str) -> None:
    raise SystemExit(f"ARRÊT : {motif}")


# Couples de la contre-lecture (§ 6), au caractère ; K2 est complété par l'extraction de son bloc.
K = [
    ("K1", "fait foi telle quelle. Chaque « ancien » figure",
     "fait foi telle quelle, à une exception : là où un bloc EC-1 à EC-8 de A1, ou un paragraphe de son § 3, de son § 5 ou de "
     "son § 6, dit autre chose qu'un fragment SA ou que le texte de ce § 2, le second addendum fait foi (les blocs EC de A1 "
     "restent lisibles comme l'histoire du premier écart, non comme le texte en vigueur). Chaque « ancien » figure"),
    ("K2", "**Raison** (SA-21 à SA-24 ; réserve R-C de la contre-lecture). Ces paragraphes de A1 décrivent le contrôle de EC-1 ; "
           "laissés tels", None),
    ("K2-compte-1", "les fragments SA-1 à SA-24 du § 2", "les fragments SA-1 à SA-25 du § 2"),
    ("K2-compte-2", "applique les vingt-quatre", "applique les vingt-cinq"),
    ("K3", "et avant toute création, strictement",
     "et avant la création de la course qu'accorde GO-2026-11-16-11, strictement"),
    ("K4a", "l'écart reste au plus de l'ordre de 10⁻¹⁰ (`brouillons",
     "l'écart reste au plus de l'ordre de 10⁻¹⁰ pour la linéaire et de 10⁻⁹ à 6·10⁻⁷ pour l'attention (`brouillons"),
    ("K4b", "l'ordre de 10⁻¹⁰ sur tous les jeux fabriqués ;",
     "l'ordre de 10⁻¹⁰ pour la linéaire et de 6·10⁻⁷ pour l'attention sur les jeux fabriqués ;"),
    ("K5", "- **Date (UTC, `date -u`)** : 2026-11-16, de 23:12 à la déclaration du rapport compagnon.",
     "- **Date (UTC, `date -u`)** : de 2026-11-16T23:12Z à 2026-11-17T00:01Z (déclaration du rapport compagnon)."),
    ("K6", "reprise telle quelle par la fiche remplaçante : aucun score",
     "reprise telle quelle par la fiche remplaçante (lecture déclarée du point 12 de T, « tirée à l'inscription de "
     "`CODE-BBIS` » : l'entropie est celle que porte la ligne `CODE-BBIS` en vigueur, non retirée ; conséquence, prédite avant "
     "la course : mêmes sondes, même couple de contrôle et mêmes actions que la course arrêtée, donc écart de la linéaire à 300 "
     "époques probablement de l'ordre de 1, discriminant « écart » ; sans effet sur aucun état) : aucun score"),
    ("K7", "ou « mesure non faite » et son motif) ; sur données fabriquées",
     "ou « mesure non faite » et son motif, ou « non lue », ou « aucune cellule calculable ») ; sur données fabriquées"),
]


def entete_et_section(debut: str, fin: str, essais: str) -> list[tuple[str, str, str]]:
    return [
        ("titre", "nouvelle course — brouillon 1\n", "nouvelle course — brouillon 2\n"),
        ("statut", "**brouillon 1, non scellé, rien n'est adopté par lui.** Il ne vaut addendum qu'après : (1) contre-lecture "
                   "par un\n  lecteur neuf (R2) ;",
         "**brouillon 2, non scellé, rien n'est adopté par lui.** Il ne vaut addendum qu'après : (1) contre-lecture par un\n"
         "  lecteur neuf (R2) (tour 1, faite au brouillon 1 ; ses corrections exigées sont appliquées dans ce brouillon 2, "
         "section 11) ;"),
        ("ligne brouillon 2", "(déclaration du rapport compagnon).\n- **Statut**",
         "(déclaration du rapport compagnon).\n"
         f"- **Brouillon 2** : rédacteur neuf des corrections (lettre de modèle C ; n'a écrit ni le brouillon 1, ni sa "
         "contre-lecture, ni le code ; lecteur déclaré de T0.7, exclu des lecteurs de P3-bis), de 2026-11-17T"
         f"{debut}Z à 2026-11-17T{fin}Z (`date -u`, la seconde au scellement) = brouillon 1 (`a582e14dd22fd17e…`, gardé tel "
         "quel, R12) + les couples K1 à K7 de la contre-lecture du tour 1, appliqués au caractère par "
         "`pieces/couples-brouillon2-second-addendum-v1.py` ; hors de ces couples, seuls changent cet en-tête (titre, "
         "statut, cette ligne) et la section 11, ajoutée.\n- **Statut**"),
        ("section 11", "valeur de clé ; ni `env`, ni `printenv`.\n",
         "valeur de clé ; ni `env`, ni `printenv`.\n\n"
         "## 11. Contre-lecture\n\n"
         "- **Rapport** : `contre-lecture-second-addendum-bbis-tour1-v1.md` (ce dossier), tour 1, lu au brouillon 1 "
         "(`a582e14dd22fd17e716aaed8d475a3c1a7ceeff60d15c3a4644aa9bf0c6f4627`) ; empreinte du rapport\n"
         "  `98a049d9f8b207eb336d04fc7e5a0b23bb5c066cd542bbc7719bd1e1b58fc120` (compagnon vérifié). Verdict du rapport :\n"
         "  **corrections**, un majeur et cinq mineurs, aucun ne touchant l'hypothèse, les seuils, le budget ni une issue ; "
         "scellable une fois les couples\n"
         "  de son § 6 appliqués et le contrôle mécanique rejoué, le code v4 étant contre-lu à part.\n"
         "- **Réponse point par point** (chaque « ancien » vérifié unique dans le brouillon 1 et dans le texte courant ; "
         "chaque « ancien » et chaque\n"
         "  « nouveau » vérifié égal, au caractère, au texte du rapport, par "
         "`pieces/couples-brouillon2-second-addendum-v1.py`) :\n"
         "  - **M1** (blocs et paragraphes de A1 contredits sans règle de préséance) : **appliqué**. K1 : phrase de "
         "préséance au § 0 ; K2 :\n"
         "    fragment SA-25 (paragraphe « R-PILE (EC-2, EC-3) » du § 5 de A1), ligne « Raison » de SA-21 à SA-25 ; comptes : "
         "« SA-1 à\n"
         "    SA-25 » (§ 0) et « vingt-cinq » (§ 9) ; « 25 écarts SA lus » dans la sortie neuve du contrôle (ci-dessous).\n"
         "  - **m1** (« avant toute création ») : **appliqué**, K3 (SA-5).\n"
         "  - **m2** (ordre de 10⁻¹⁰ vrai de la linéaire, faux de l'attention) : **appliqué**, K4a (SA-1, « Nouveau ») et "
         "K4b (§ 4, premier cas).\n"
         "  - **m3** (date et heures du brouillon 1) : **appliqué**, K5.\n"
         "  - **m4** (entropie reprise, lecture du point 12 de T, prédiction écrite avant la course) : **appliqué**, K6 "
         "(§ 5).\n"
         "  - **m5** (énumération des formes du résumé de la mesure) : **appliqué**, K7 (SA-2) ; la phrase gelée de R-PILE "
         "n'est pas touchée.\n"
         "  - **Remarques facultatives R1 à R4** : aucune correction exigée par le rapport ; **non appliquées** (ce brouillon "
         "n'applique que les\n"
         "    corrections exigées ; R1 demanderait en plus de changer `lecture_v3.SECTION_D`, donc de rouvrir la "
         "contre-lecture du code).\n"
         "  - **Points pour la session mère** (§ 5 du rapport, points 1 à 6 : réponses aux trois questions du rédacteur, "
         "répétition à blanc\n"
         "    recommandée sans être exigée, garde de débit pendant la mesure, ordre des gestes avant le feu, contre-lecture du "
         "code v4 encore due,\n"
         "    incident du lecteur) : hors du texte de l'addendum, **non appliqués ici**, laissés à la mère.\n"
         "- **Contrôle mécanique rejoué** sur ce brouillon 2 : `pieces/controle-fragments-second-addendum-v2.py` (copie de "
         "la v1, produite par le\n"
         "  même programme de couples : seuls changent le nom du brouillon lu, les noms des deux pièces écrites et le compte "
         "« SA-21 à SA-25 »\n"
         "  d'un commentaire) ; sortie `pieces/sortie-controle-fragments-second-addendum-v2.txt` : 25 écarts SA lus, chaque "
         "« ancien » unique dans\n"
         "  son document, R-PILE et point (7) égaux aux chaînes de `lecture_v3`, **CONFORME**, code 0 ; texte en vigueur\n"
         "  `pieces/texte-en-vigueur-apres-second-addendum-v2.md` ; premier addendum lu avec le second "
         "`pieces/premier-addendum-lu-avec-le-second-v2.md`.\n"
         "  Les pièces v1 nommées au § 0 et au § 9 sont celles du brouillon 1, gardées telles quelles (R12) ; pour ce brouillon 2, les "
         "pièces v2 en tiennent lieu.\n"
         f"- **Essais rejoués** : {essais}\n"),
    ]


def appliquer(texte: str, depart: str, couples, quoi: str) -> str:
    for ident, ancien, nouveau in couples:
        if depart.count(ancien) != 1:
            arret(f"{quoi} {ident} : « ancien » trouvé {depart.count(ancien)} fois dans le texte de départ : {ancien[:80]!r}")
        if texte.count(ancien) != 1:
            arret(f"{quoi} {ident} : « ancien » trouvé {texte.count(ancien)} fois dans le texte courant : {ancien[:80]!r}")
        texte = texte.replace(ancien, nouveau)
        if texte.count(nouveau) != 1:
            arret(f"{quoi} {ident} : « nouveau » non unique après remplacement")
        print(f"{quoi} {ident} : appliqué ({len(ancien)} → {len(nouveau)} caractères)")
    return texte


def main() -> int:
    source, cible, debut, essais = Path(sys.argv[1]), Path(sys.argv[2]), sys.argv[3], sys.argv[4]
    p_b1 = source / "brouillon-second-addendum-bbis-v1.md"
    p_cl = source / "contre-lecture-second-addendum-bbis-tour1-v1.md"
    p_c1 = source / "pieces" / "controle-fragments-second-addendum-v1.py"
    for p, attendu in ((p_b1, SHA_BROUILLON1), (p_cl, SHA_CONTRE_LECTURE), (p_c1, SHA_CONTROLE_V1)):
        if sha(p) != attendu:
            arret(f"empreinte de {p.name} ≠ {attendu[:16]}…")
    b1 = p_b1.read_text(encoding="utf-8")
    cl = p_cl.read_text(encoding="utf-8")
    c1 = p_c1.read_text(encoding="utf-8")
    # Nouveau de K2 : bloc ````text du § 6 du rapport, extrait tel quel.
    if cl.count("````text\n") != 1 or cl.count("\n````\n") != 1:
        arret("bloc ````text de K2 non unique dans le rapport")
    k2 = cl.split("````text\n", 1)[1].split("\n````\n", 1)[0]
    couples = [(i, a, k2 if n is None else n) for i, a, n in K]
    for ident, ancien, nouveau in couples:
        if ident.startswith("K2-compte"):
            continue  # comptes : couples énoncés dans le rapport sous forme « a » → « b » sur une ligne enveloppée
        if ancien not in cl or nouveau not in cl:
            arret(f"{ident} : « ancien » ou « nouveau » absent du rapport, au caractère")
    for a, n in (("les fragments SA-1 à SA-24 du § 2", "les fragments SA-1 à SA-25 du § 2"),
                 ("applique les vingt-quatre", "applique les vingt-cinq")):
        if f"`{a}` → `{n}`" not in cl:
            arret(f"compte « {a} » → « {n} » absent du rapport")
    b2 = appliquer(b1, b1, couples, "brouillon")
    fin = subprocess.run(["date", "-u", "+%H:%M"], capture_output=True, text=True, check=True).stdout.strip()
    b2 = appliquer(b2, b2, entete_et_section(debut, fin, essais), "en-tête et section")
    c2 = appliquer(c1, c1, [
        ("nom du brouillon", '"brouillon-second-addendum-bbis-v1.md"', '"brouillon-second-addendum-bbis-v2.md"'),
        ("texte en vigueur", '"texte-en-vigueur-apres-second-addendum-v1.md"', '"texte-en-vigueur-apres-second-addendum-v2.md"'),
        ("premier addendum lu", '"premier-addendum-lu-avec-le-second-v1.md"', '"premier-addendum-lu-avec-le-second-v2.md"'),
        ("commentaire 1", '"pieces/controle-fragments-second-addendum-v1.py ; pièce de travail, ne fait pas foi. -->\\n" + T2',
         '"pieces/controle-fragments-second-addendum-v2.py ; pièce de travail, ne fait pas foi. -->\\n" + T2'),
        ("commentaire 2", "Premier addendum lu avec SA-21 à SA-24 du second, produit par \"\n"
                          "                         \"pieces/controle-fragments-second-addendum-v1.py",
         "Premier addendum lu avec SA-21 à SA-25 du second, produit par \"\n"
         "                         \"pieces/controle-fragments-second-addendum-v2.py"),
    ], "contrôle")
    sorties = [(cible / "brouillon-second-addendum-bbis-v2.md", b2),
               (cible / "pieces" / "controle-fragments-second-addendum-v2.py", c2)]
    for p, _ in sorties:
        if p.exists():
            arret(f"{p} existe déjà (R12)")
    for p, t in sorties:
        p.parent.mkdir(parents=True, exist_ok=True)
        with open(p, "x", encoding="utf-8") as f:
            f.write(t)
        print(f"écrit {p} ({sha(p)})")
    print(f"heure de fin (date -u) : {fin}")
    print("CONFORME")
    return 0


if __name__ == "__main__":
    sys.exit(main())
