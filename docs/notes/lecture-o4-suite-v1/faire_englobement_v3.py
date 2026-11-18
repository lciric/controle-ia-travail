"""Écrit la note d'englobement de O4, v3, depuis la v2 (R12 : fichier neuf ; la v2 reste en place).

Porte la contre-lecture de la v2 (modèle K, `contre-lecture-lecture-o4-englobement-v2.md`, `04287f0f…`, « porte la décision après
corrections », 3 majeurs, 4 mineurs) : nom de modèle resté en section 3.2 retiré (repéré par motif, non recopié ici) ; pages décisives de
LIU mises sur la version de septembre ; temps réel dit pour le banc d'essai de KL, non pour ses systèmes optimisés ; section 5, point 1,
mis à jour ; ligne des versions complétée ; section 6 marquée « (v1) ». Remplacements comptés ; refus si un texte visé n'est pas présent
le nombre de fois dit. Usage : python3 -I faire_englobement_v3.py NOTE_V2 SORTIE HEURE_UTC
"""
import hashlib, os, re, sys

V2_SHA = "9c3c81a9423ea3dcc03d43f940f3e67c85582abcbe94056ab219525b765fc0d1"


def main():
    src, sortie, heure = sys.argv[1:4]
    if os.path.exists(sortie):
        sys.exit("REFUS : sortie existante (R12)")
    b = open(src, "rb").read()
    if hashlib.sha256(b).hexdigest() != V2_SHA:
        sys.exit("REFUS : empreinte de la v2")
    t = b.decode("utf-8")
    n = [0]

    def r(o, nv, k=1):
        nonlocal t
        c = t.count(o)
        if c != k:
            sys.exit(f"REFUS : « {o[:90]} » présent {c} fois, {k} attendu(s)")
        t = t.replace(o, nv)
        n[0] += 1

    r("tests d'englobement — v2\n", "tests d'englobement — v3\n")
    r("Le verdict ne change pas. Les noms de modèles de la v1 sont retirés (R-2690).",
      "Le verdict ne change pas. Les noms de modèles de la v1 sont retirés (R-2690).\n"
      f"- **Version 3** (R12 ; la v2, `{V2_SHA[:16]}…`, reste en place) : écrite par le modèle A à {heure} (`date -u`) ; porte la contre-lecture\n"
      "  de la v2 par le modèle K (`contre-lecture-lecture-o4-englobement-v2.md`, `04287f0f…`, « porte la décision après corrections », 0\n"
      "  bloquant, 3 majeurs, 4 mineurs) : nom de modèle resté en section 3.2 retiré ; pages décisives de LIU (section 2) mises sur la version\n"
      "  de septembre ; temps réel dit pour le banc d'essai de KL, non établi pour ses systèmes optimisés (section 0, point 1) ; section 5,\n"
      "  point 1, à jour ; section 6 marquée « (v1) ». La v2 changeait aussi, sans le dire dans sa ligne, l'en-tête (règle de lecture) et le\n"
      "  paragraphe « Conséquence proposée » (constat 5). Le verdict ne change pas.")
    m = re.search(r"proposeur modèles de langue \([^)]*, p\. 24\)", t)
    if not m:
        sys.exit("REFUS : passage de la section 3.2 absent")
    r(m.group(0), "proposeur modèles de langue (un modèle de langue du commerce, p. 24)")
    r("| **occupe en partie** : principe pour des hypothèses de modèle de langue, hors boucle | 1, 4, 8, 14, 18, 22, 26, 28, 36 |",
      "| **occupe en partie** : principe pour des hypothèses de modèle de langue, hors boucle | septembre : 1, 5, 6, 11, 15, 19, 22, 29, 30, 32, 38, 40, 42, 57 ; avril : 14, 15 |")
    r("""   - **pour des systèmes à modèle de langue optimisés, dont les prédictions sont faites en temps réel, avant que le rendement n'existe**,
     jugées par leur gain d'explication sur des déterminants connus (Koijen et Levy, SSRN 6474601, date imprimée 30 juin 2026, p. 1, 3, 8,
     11, 16 ; la date de dépôt sur SSRN n'est pas lue).""",
      """   - **pour des systèmes à modèle de langue, sur un banc d'essai en temps réel où les prédictions sont recueillies avant que le
     rendement n'existe**, jugées par leur gain d'explication sur des déterminants connus (Koijen et Levy, SSRN 6474601, date imprimée
     30 juin 2026, p. 1, 3, 8, 11 ; la date de dépôt sur SSRN n'est pas lue) ; pour les systèmes **optimisés**, que le texte fasse émettre
     les prédictions de la seconde moitié du trimestre avant les événements est probable, non établi (p. 11, 16).""")
    r("En v1 : refusé (section 6). La copie lue (hôte d'une conférence, juin 2026) porte la date d'avril 2026 et un résumé identique à la notice SSRN ; l'identité exacte n'est pas vérifiable.",
      "En v1 : refusé (section 6), et la v1 lisait la copie d'avril d'un hôte de conférence ; la version officielle de septembre en diffère (84 p. contre 71 ; correspondance des citations : lecture SSRN v2, section 1).")
    r("## 6. Refus et incidents (tels quels)", "## 6. Refus et incidents (tels quels) (v1)")
    with open(sortie, "x", encoding="utf-8") as f:
        f.write(t)
    print(f"{n[0]} remplacements comptés")


if __name__ == "__main__":
    main()
