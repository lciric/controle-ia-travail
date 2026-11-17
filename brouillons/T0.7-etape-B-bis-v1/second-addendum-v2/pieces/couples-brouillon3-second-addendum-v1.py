"""Couples « ancien → nouveau » du brouillon 3 du second addendum de B bis (T0.7) : processeur seulement, aucun réseau.

Lit, dans le dossier SOURCE (`second-addendum-v2/`) :
- `brouillon-second-addendum-bbis-v2.md` (empreinte vérifiée) ;
- `contre-lecture-second-addendum-bbis-tour2-v1.md` (empreinte vérifiée) : l'« ancien » et le « nouveau » du seul couple exigé,
  m1, doivent y figurer au caractère (lignes « - Ancien : `…` » et « - Nouveau : `…` » de son § 4) ;
- `pieces/controle-fragments-second-addendum-v2.py` (empreinte vérifiée).
Écrit, dans le dossier CIBLE (le même dossier, ou une copie de travail pour un essai à blanc), sans jamais écraser :
- `brouillon-second-addendum-bbis-v3.md` = brouillon 2 + m1 + en-tête (titre, statut, ligne « Brouillon 3 », heure lue par
  `date -u`) + section « 11. Contre-lecture » complétée (intertitre et note du tour 1, dont le texte est gardé tel quel ; tour 2
  ajouté à la fin) ; rien d'autre : le programme vérifie que toutes les lignes entre le titre du § 0 et celui du § 11 sont égales, octet
  pour octet, à celles du brouillon 2 ;
- `pieces/controle-fragments-second-addendum-v3.py` = v2 dont ne changent que le nom du brouillon lu et les noms des deux pièces
  écrites (dans le code et dans leurs lignes de commentaire).
Chaque « ancien » doit figurer exactement une fois dans le texte courant et une fois dans le texte de départ ; sinon arrêt.

Jouer : `python <ce fichier> SOURCE CIBLE DEBUT` (DEBUT : heure de début « HH:MM »). Code 0 : écrit ; arrêt (code non nul) :
un écart (motif écrit), rien n'est écrit."""
from __future__ import annotations

import hashlib
import subprocess
import sys
from pathlib import Path

SHA_BROUILLON2 = "ab66d5fa67a640679465581d48d9fc97a1da7d81c7b41b18e81865274c91f62c"
SHA_CONTRE_LECTURE = "f4843729df2528b864b77e370c6c8725e94adccbedb99ff096e14028783a9f4e"
SHA_CONTROLE_V2 = "35a369f6079ad1a87f377c404142cb42284468cbd1b3dcb2fb045e146cd3ba76"


def sha(p: Path) -> str:
    return hashlib.sha256(p.read_bytes()).hexdigest()


def arret(motif: str) -> None:
    raise SystemExit(f"ARRÊT : {motif}")


# Seul couple exigé par la contre-lecture du tour 2 (§ 4, m1), au caractère.
M1 = ("m1", "(lettre de modèle C ; n'a écrit ni le brouillon 1", "(lettre de modèle A ; n'a écrit ni le brouillon 1")

TOUR2 = (
    "\n"
    "### Tour 2 — rapport lu au brouillon 2, correction dans ce brouillon 3\n"
    "\n"
    "- **Rapport** : `contre-lecture-second-addendum-bbis-tour2-v1.md` (ce dossier), tour 2, lu au brouillon 2\n"
    "  (`ab66d5fa67a640679465581d48d9fc97a1da7d81c7b41b18e81865274c91f62c`) ; empreinte du rapport\n"
    "  `f4843729df2528b864b77e370c6c8725e94adccbedb99ff096e14028783a9f4e` (compagnon vérifié). Verdict du rapport : **corrections**, une\n"
    "  seule exigée (m1, mineure), aucun majeur ; scellable une fois m1 appliqué, aucun autre changement requis ; le code v4 reste à\n"
    "  contre-lire à part.\n"
    "- **Réponse point par point** (l'« ancien » de m1 vérifié unique dans le brouillon 2 et dans le texte courant, son « ancien » et son\n"
    "  « nouveau » vérifiés présents, au caractère, dans le rapport, par `pieces/couples-brouillon3-second-addendum-v1.py`) :\n"
    "  - **§ 2 et § 3 du rapport** (couples K1 à K7 du tour 1 appliqués au caractère ; contrôle mécanique, essais et épreuves rejoués par\n"
    "    le lecteur, conformes ; code v4 inchangé) : constats, rien à appliquer.\n"
    "  - **m1** (lettre de modèle du rédacteur du brouillon 2) : **appliqué**, au caractère, dans la ligne « Brouillon 2 » de l'en-tête\n"
    "    (« lettre de modèle C » devient « lettre de modèle A »). Le rapport laissait le point à trancher par la mère, qui lance les\n"
    "    rédacteurs ; la commande de ce tour, venue d'elle, dit les corrections écrites par le modèle A ; le rédacteur du brouillon 3 n'a\n"
    "    pas d'autre source sur ce point et tient de la même commande la lettre de sa propre ligne.\n"
    "  - **R1** (pièces v1 encore nommées au § 0 et au § 9) : remarque facultative, **non appliquée** : ce brouillon n'applique que la\n"
    "    correction exigée et ne change que l'en-tête et cette section (pour ce brouillon 3, ce seraient d'ailleurs les pièces v3, non les\n"
    "    v2) ; la lecture reste celle du tour 1 : les pièces v1 nommées au § 0 et au § 9 sont celles du brouillon 1, gardées telles quelles\n"
    "    (R12) ; pour ce brouillon 3, les pièces v3 en tiennent lieu (ci-dessous).\n"
    "  - **R2** (remarques R1 à R4 du tour 1 laissées non appliquées) : remarque facultative, rien à appliquer ; elles restent non\n"
    "    appliquées.\n"
    "  - **Points pour la session mère** (§ 5 du rapport, points 1 à 6 : m1 à trancher, scellement et ligne `ADDENDUM-ECART-2-BBIS` avant\n"
    "    la seconde ligne `CODE-BBIS`, entropie reprise, gestes encore dus avant le feu, répétition à blanc, garde de débit pendant la\n"
    "    mesure, incidents du lecteur) : hors du texte de l'addendum, **non appliqués ici**, laissés à la mère.\n"
    "- **Contrôle mécanique rejoué après le couple** : `pieces/controle-fragments-second-addendum-v3.py` (copie de la v2, produite par le\n"
    "  même programme de couples : seuls changent le nom du brouillon lu et les noms des deux pièces écrites, dans le code et dans leurs\n"
    "  lignes de commentaire) ; sortie `pieces/sortie-controle-fragments-second-addendum-v3.txt` ; texte en vigueur\n"
    "  `pieces/texte-en-vigueur-apres-second-addendum-v3.md` ; premier addendum lu avec le second\n"
    "  `pieces/premier-addendum-lu-avec-le-second-v3.md`. Aucune ligne entre le titre du § 0 et celui de cette section ne change (aucun\n"
    "  fragment SA, aucun chiffre, aucun seuil) : vérifié par le programme de couples, ces lignes sont égales, octet pour octet, à celles\n"
    "  du brouillon 2.\n"
    "- **Essais rejoués après le couple** : le code du dossier `code/` n'est touché par aucun couple ; mêmes deux fichiers d'essais que les\n"
    "  brouillons 1 et 2 (34 essais neufs, 17 du contrôle v3) ; sortie `essais/sortie-essais-second-addendum-v3.txt`.\n"
)


def entete_et_section(debut: str, fin: str) -> list[tuple[str, str, str]]:
    return [
        ("titre", "nouvelle course — brouillon 2\n", "nouvelle course — brouillon 3\n"),
        ("statut",
         "**brouillon 2, non scellé, rien n'est adopté par lui.** Il ne vaut addendum qu'après : (1) contre-lecture par un\n"
         "  lecteur neuf (R2) (tour 1, faite au brouillon 1 ; ses corrections exigées sont appliquées dans ce brouillon 2, section 11) ;",
         "**brouillon 3, non scellé, rien n'est adopté par lui.** Il ne vaut addendum qu'après : (1) contre-lecture par un\n"
         "  lecteur neuf (R2) (tour 1, faite au brouillon 1, ses corrections exigées appliquées au brouillon 2 ; tour 2, faite au brouillon 2,\n"
         "  sa seule correction exigée appliquée dans ce brouillon 3 ; section 11) ;"),
        ("ligne brouillon 3", "et la section 11, ajoutée.\n- **Statut**",
         "et la section 11, ajoutée.\n"
         "- **Brouillon 3** : rédacteur neuf de la correction du tour 2 (lettre de modèle A ; n'a écrit aucun des brouillons 1 et 2, ni "
         "leurs contre-lectures, ni le code ; lecteur déclaré de T0.7, exclu des lecteurs de P3-bis), de 2026-11-17T"
         f"{debut}Z à 2026-11-17T{fin}Z (`date -u`, la seconde au scellement) = brouillon 2 (`ab66d5fa67a64067…`, gardé tel quel, "
         "R12) + le couple m1 de la contre-lecture du tour 2, appliqué au caractère par "
         "`pieces/couples-brouillon3-second-addendum-v1.py` ; hors de ce couple, seuls changent cet en-tête (titre, statut, cette "
         "ligne) et la section 11 (intertitre et note du tour 1, dont le texte est gardé tel quel ; tour 2 ajouté à la fin).\n"
         "- **Statut**"),
        ("intertitre du tour 1",
         "## 11. Contre-lecture\n\n- **Rapport** : `contre-lecture-second-addendum-bbis-tour1-v1.md`",
         "## 11. Contre-lecture\n\n"
         "### Tour 1 — rapport lu au brouillon 1, corrections dans le brouillon 2\n\n"
         "Texte du brouillon 2, gardé tel quel : « ce brouillon », « ce brouillon 2 » et « de ma main » y désignent le brouillon 2 et son "
         "rédacteur.\n\n"
         "- **Rapport** : `contre-lecture-second-addendum-bbis-tour1-v1.md`"),
        ("tour 2", "La suite entière sur un arbre de la forme de l'instance n'est pas rejouée (code inchangé).\n",
         "La suite entière sur un arbre de la forme de l'instance n'est pas rejouée (code inchangé).\n" + TOUR2),
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


def corps(texte: str) -> str:
    """Lignes du titre du § 0 (compris) au titre du § 11 (exclu)."""
    if texte.count("\n## 0. Textes qui font foi") != 1 or texte.count("\n## 11. Contre-lecture\n") != 1:
        arret("titres du § 0 ou du § 11 introuvables ou en double")
    return texte.split("\n## 0. Textes qui font foi", 1)[1].split("\n## 11. Contre-lecture\n", 1)[0]


def main() -> int:
    source, cible, debut = Path(sys.argv[1]), Path(sys.argv[2]), sys.argv[3]
    p_b2 = source / "brouillon-second-addendum-bbis-v2.md"
    p_cl = source / "contre-lecture-second-addendum-bbis-tour2-v1.md"
    p_c2 = source / "pieces" / "controle-fragments-second-addendum-v2.py"
    for p, attendu in ((p_b2, SHA_BROUILLON2), (p_cl, SHA_CONTRE_LECTURE), (p_c2, SHA_CONTROLE_V2)):
        if sha(p) != attendu:
            arret(f"empreinte de {p.name} ≠ {attendu[:16]}…")
    sorties = [cible / "brouillon-second-addendum-bbis-v3.md", cible / "pieces" / "controle-fragments-second-addendum-v3.py"]
    for p in sorties:
        if p.exists():
            arret(f"{p} existe déjà (R12)")
    b2 = p_b2.read_text(encoding="utf-8")
    cl = p_cl.read_text(encoding="utf-8")
    c2 = p_c2.read_text(encoding="utf-8")
    ident, ancien, nouveau = M1
    if cl.count(f"- Ancien : `{ancien}`\n") != 1 or cl.count(f"- Nouveau : `{nouveau}`\n") != 1:
        arret("m1 : « ancien » ou « nouveau » absent du rapport, au caractère")
    if not b2.endswith("La suite entière sur un arbre de la forme de l'instance n'est pas rejouée (code inchangé).\n"):
        arret("le brouillon 2 ne finit pas par la dernière ligne attendue de sa section 11")
    b3 = appliquer(b2, b2, [M1], "brouillon")
    fin = subprocess.run(["date", "-u", "+%H:%M"], capture_output=True, text=True, check=True).stdout.strip()
    b3 = appliquer(b3, b3, entete_et_section(debut, fin), "en-tête et section")
    if corps(b3) != corps(b2):
        arret("une ligne entre le titre du § 0 et celui du § 11 a changé")
    if b3.count("(lettre de modèle C ; n'a écrit ni le brouillon 1") != 0 or b3.count(nouveau) != 1:
        arret("m1 : compte final inattendu")
    if not b3.endswith(TOUR2):
        arret("le tour 2 n'est pas à la fin")
    c3 = appliquer(c2, c2, [
        ("nom du brouillon", '"brouillon-second-addendum-bbis-v2.md"', '"brouillon-second-addendum-bbis-v3.md"'),
        ("texte en vigueur", '"texte-en-vigueur-apres-second-addendum-v2.md"', '"texte-en-vigueur-apres-second-addendum-v3.md"'),
        ("premier addendum lu", '"premier-addendum-lu-avec-le-second-v2.md"', '"premier-addendum-lu-avec-le-second-v3.md"'),
        ("commentaire 1", '"pieces/controle-fragments-second-addendum-v2.py ; pièce de travail, ne fait pas foi. -->\\n" + T2',
         '"pieces/controle-fragments-second-addendum-v3.py ; pièce de travail, ne fait pas foi. -->\\n" + T2'),
        ("commentaire 2", '"pieces/controle-fragments-second-addendum-v2.py ; pièce de travail, ne fait pas foi. -->\\n" + A1b',
         '"pieces/controle-fragments-second-addendum-v3.py ; pièce de travail, ne fait pas foi. -->\\n" + A1b'),
    ], "contrôle")
    if "v2" in c3:
        arret("contrôle : un « v2 » reste dans la copie v3")
    for p, t in zip(sorties, (b3, c3)):
        p.parent.mkdir(parents=True, exist_ok=True)
        with open(p, "x", encoding="utf-8") as f:
            f.write(t)
        print(f"écrit {p} ({sha(p)})")
    print(f"heure de fin (date -u) : {fin}")
    print("CONFORME")
    return 0


if __name__ == "__main__":
    sys.exit(main())
