"""Porte les neuf marqueurs restants du candidat du texte de lecture v2 des lentilles (39118ac1...).

Usage : python -I porter_marqueurs_v1.py CANDIDAT SORTIE DIFF
Chaque marqueur doit apparaître une seule fois ; aucun autre octet ne change ; le différentiel est écrit.
"""
import difflib
import hashlib
import re
import sys

ATTENDU = "39118ac138dee5ddb21142d1f8cdda6b005e15e0d156b6abaadbbb30d47fef8a"
NL = "docs/notes/neuron-lens-v1"
LB = "docs/notes/lecture-sondes-bbis-par-lentilles-v1"

V = {
    "CONTRE_LECTURE_4": (
        "contre-lecteur, sous-agent neuf de la session des lentilles sur Claude Opus 5.5 (`claude-opus-5-5`), autre modèle "
        "que les rédacteurs des brouillons 4 à 6 (Fable 5.2) ; choix de forme de la session principale, une entrée à trois "
        "rapports, dans l'ordre : (i) contre-lecture du brouillon 4 (`prereg/lecture-sondes-bbis-par-lentilles-v2-brouillon4.md`, "
        "`fe46a9468b8b985a76d4e700a5bed82b3b970851335214216c8319e5f8084e4b`), rapport "
        f"`{NL}/contre-lecture-texte-lecture-lentilles-v2-brouillon4-v1.md` "
        "(`08a698577a952669dd3cd75fa7d7bcb7447a5b1e795106b322bf0e377792c17b`), verdict « scellable après corrections » (B1 à B4 "
        "bloquantes, N1 à N10) ; (ii) vérification des corrections du brouillon 5 (`prereg/lecture-sondes-bbis-par-lentilles-v2-brouillon5.md`, "
        "`88a2011a8b9e02ba9f6f2933ee4ec01ee6f156abf44ccf19960d9b7de3d75003`), rapport "
        f"`{NL}/verification-corrections-texte-lecture-lentilles-v2-brouillon5-v1.md` "
        "(`04282064d10c6cdd2a4266bf9e5a526c9835463476108dec8a54dfcae2f64328`), verdict « scellable après corrections » (C1, M1 à M6) ; "
        "(iii) vérification des corrections du brouillon 6 (`prereg/lecture-sondes-bbis-par-lentilles-v2-brouillon6.md`, "
        "`f707bced9c7fb1605e99250797cfc52a178f58fe2633772778e72a780a963000`), rapport "
        f"`{NL}/verification-corrections-texte-lecture-lentilles-v2-brouillon6-v1.md` "
        "(`d6f7a166c547d91a6c90970b76ee2fda5cc83439d7552f6341f9e1263af1c015`), verdict « scellable après corrections », R1 exigée, "
        "R2 recommandée, aucun brouillon de plus ; la version scellée est le brouillon 6 avec R1 et R2 portées par programme "
        f"(`{NL}/scellement-texte-lecture-v2/differentiel-brouillon6-candidat.diff`, "
        "`e99425605c59b1e4ed737607f3b2e17a355fa1448a83b394a67c6239c2dff76d`), puis ces marqueurs, portés par programme par la "
        "session principale (différentiel versé à côté de la version)"
    ),
    "CONTRE_LECTURE_ET_SCELLEMENT_DU_CRITERE": (
        f"critère scellé `{NL}/devis-reajustement/critere-identite-reajustement-lentilles-v8.md` "
        "(`541bb86b15088c5cea5a291a294cccdd1067fe39be995b7f9014661f96cb3940`, égale à celle citée ici), compagnon "
        "`critere-identite-reajustement-lentilles-v8.md.sha256`, ligne `CRITERE-IDENTITE-REAJUSTEMENT-LENTILLES` de "
        "`registres/scellements-v1.md` (2026-11-19T13:03:14Z, R-3819) ; contre-lectures et vérifications, sous "
        f"`{NL}/` : `contre-lecture-critere-identite-reajustement-v1.md` "
        "(`9241903708eacef5244bf81b0b071131edab0023195d8a068dc7051cd57883ff`, R-3721, « pas avant ») ; "
        "`verification-critere-identite-reajustement-v2-v1.md` (`8a6045bb3db81188e9c0889fbd69bafa57085c5336bff6db7dec7e24de1a4f94`, "
        "R-3728, « pas avant ») ; `contre-lecture-critere-et-devis-v4-v1.md` "
        "(`c61466fae8712769e498bfcabb24079bbc2934657e1899f005599e42a143ca3d`, R-3747, Opus 5.5, « pas avant ») ; "
        "`verification-critere-et-devis-v5-v1.md` (`cd93416cb4df693f5092da0e07002fd895cf99fad061d897de29233f76589478`, R-3779, "
        "« scellable après sept couples ») ; `verification-critere-v6-devis-v7-programme-v4-v1.md` "
        "(`e56e0a75a91360053d1bb94d11407702462713b50dd327d53eb9ef3be2bb859a`, R-3803, « scellable après un couple exact ») ; "
        "`verification-critere-v8-devis-v8-v1.md` (`caa7753edbab84f5e297268960c9cdfab4440048d764fc7dc23e5cf792d809bc`, R-3815, "
        "« scellable ») ; pièce de la session des lentilles qui relève cette chaîne, "
        f"`{LB}/scellement-v2/pieces-critere-pour-texte-lecture-v2-v1.md` "
        "(`9acc3749457ba3d0918a3b5533fc775c36c08141e2a5651977ae58e153ea696e`, branche des lentilles, commit `e0dc1ffc`) ; aucun "
        "rapport n'est trouvé par son nom pour les versions 3 et 7 du critère"
    ),
    "DECISION_DATEE_DE_LA_RETENUE": (
        "ligne R-4119 de `registres/decisions.md` (branche principale), inscrite le 2026-11-20 à 05:50:18Z (heure relevée par "
        "`date -u`) : « la lecture humaine de la première passe […] est retenue jusqu'au scellement de la v2 ou jusqu'à son "
        "abandon écrit. Elle ne change rien à la v1. »"
    ),
    "DECLARATION_DE_LAZAR_SUR_LE_VERDICT": (
        "Lazar, interrogé le 2026-11-20 par la session des lentilles (savait-il ou non ce que disait le verdict de "
        "l'apprentissage des sondes sur la tâche quand il a ajouté la seconde passe), répond « non je ne crois pas pourquoi? » "
        "(message de Lazar, événement `32532749-1333-4399-8d60-624a220ba9d7`, 2026-11-20T09:52:12Z, relu à la source par la "
        "session principale, ligne R-4178 de `registres/decisions.md` ; note "
        f"`{NL}/mot-lazar-declaration-verdict-seconde-passe-2026-11-20-v1.md`, "
        "`b28a8d430f37e76e236f15ad065a4331dd50abca45644638f4168117098f7875`, branche des lentilles, commit `d800d02d`) : une "
        "réponse négative avec une réserve de mémoire, que ce texte ne durcit pas"
    ),
    "DECLARATION_DE_LA_SESSION_DES_LENTILLES": (
        f"pièce `{LB}/scellement-v2/declaration-session-lentilles-texte-lecture-v2-v1.md` "
        "(`1f63b57d51d9dfc2e238f935e3ca7bf8344e04a2c8aed0c9739f4c7b6d92d58f`, branche des lentilles, commit `e0dc1ffc`), qui dit "
        "ce qu'elle a lu ou non de ce verdict et de cette chaîne ; mandat du rédacteur du brouillon 2, versé mot pour mot : "
        f"`{LB}/mandats/mandat-redacteur-texte-lecture-v2-brouillon2-v1.md` "
        "(`9a0a82cf5d8b3850f0d2fdd1d7aa78c99da8caf4c103096d41471633d29950b0`)"
    ),
    "DECLARATION_DE_LA_SESSION_PRINCIPALE": (
        "pièce `" + NL + "/scellement-texte-lecture-v2/declaration-session-principale-v1.md` "
        "(`477ca61edd9dced4026370b8692684e69f9023a1a1af6e2e176707f4fc5900b4`), écrite par la session principale qui reprend "
        "(`session_01QPDgKgejkqwnuaJHJ31Ydo`, 2026-11-20, R-4175) : elle n'a lu ni le verdict de l'apprentissage des sondes sur "
        "la tâche, ni aucune table de la première passe, ni rien de la chaîne des sondes, et elle déclare les valeurs du "
        "verdict de la tranche B-β qu'elle a vues dans le rapport du lecteur désigné ; les sessions principales d'avant "
        "déclarent n'avoir pas ouvert ce verdict (R-3559, R-4119) ; « 00:13:25Z » est l'heure d'inscription de la clé "
        "`VERDICT-BBIS`, et « vers 01:01Z » n'est pas une heure du verdict, mais celle de la passation de la mère (R-3573) et des "
        "canaux entre sessions v5 (R-3574) ; elle confirme qu'aucune ligne de la session principale ne fixe un seuil, un "
        "critère ni un choix d'analyse de l'ajout"
    ),
    "DIFFERENCES_DU_BROUILLON_2_A_LA_VERSION": (
        "`prereg/pieces-lecture-sondes-bbis-par-lentilles-v1/changements-brouillon2-vers-version-v2-v1.md` "
        "(`49b3749eefd7dfdd84d2ecbca61de91304df506277bdbab4f59a925868b3c857`, branche des lentilles, commit `32503e58`), avec, "
        "pour les deux derniers pas, le différentiel du brouillon 6 au candidat (`e99425605c59b1e4ed737607f3b2e17a355fa1448a83b394a67c6239c2dff76d`) "
        "et celui du candidat à la version, qui ne porte que les marqueurs"
    ),
    "ETAT_DE_LA_PREMIERE_PASSE_AU_SCELLEMENT": (
        "registre propre `registres/lecture-sondes-bbis-par-lentilles-v1.md` relu juste avant le scellement "
        "(`93a2d638be007260569ef240f359e6798ccd4ca4e137576d816203d3c9db32c0`) : trois lignes, `ABSENCE-VERDICT-LENTILLES-BBIS` "
        "et `SCELLEMENT-LENTILLES-BBIS` (2026-11-18T19:05:35Z), `ADDENDUM-CONCENTRATION-LENTILLES-BBIS` (2026-11-19T16:35:35Z) ; "
        "aucune ligne `CODE-LENTILLES-BBIS`, `MONTAGE-…`, `ENTREES-…`, `TABLES-LENTILLES-BBIS`, `OUVERTURE-LENTILLES-BBIS` ni "
        "`LECTURE-LENTILLES-BBIS` ; aucune table de la première passe n'est inscrite, aucune n'a été ouverte par une personne "
        "à la connaissance de la session principale (retenue R-4119 ; déclarations des deux sessions)"
    ),
    "ETAT_DU_REGISTRE_PROPRE_A_L_ANCRE": (
        "deux lignes, `ABSENCE-VERDICT-LENTILLES-BBIS` (2026-11-18T19:05:35Z, `registres/t07-etape-b-bis-v1.md`, "
        "`55a6580687d490fcd4aa622225f735686a4e5cd4cacb4379a403dd4ce950836a`) et `SCELLEMENT-LENTILLES-BBIS` (2026-11-18T19:05:35Z, "
        "`prereg/lecture-sondes-bbis-par-lentilles-v1.md`, `ca5066d757df604cbf642db84f8a8fc56a0db8b6cc183f734842b7abdaf6d572`) ; "
        "`TABLES-LENTILLES-BBIS` absente (et encore absente au scellement) ; `ADDENDUM-CONCENTRATION-LENTILLES-BBIS` est "
        "postérieure à l'ancre (2026-11-19T16:35:35Z)"
    ),
}


def main(candidat, sortie, diff):
    src = open(candidat, encoding="utf-8").read()
    if hashlib.sha256(src.encode("utf-8")).hexdigest() != ATTENDU:
        sys.exit("ARRET : empreinte du candidat")
    out = src
    for nom, val in V.items():
        cle = "<<" + nom + ">>"
        if out.count(cle) != 1:
            sys.exit(f"ARRET : {nom} trouvé {out.count(cle)} fois")
        out = out.replace(cle, val)
    restants = re.findall(r"<<[A-Z0-9_]+>>", out)
    if restants:
        sys.exit(f"ARRET : marqueurs restants {restants}")
    reconstruit = src
    for nom, val in V.items():
        reconstruit = reconstruit.replace("<<" + nom + ">>", val)
    assert reconstruit == out
    with open(sortie, "x", encoding="utf-8") as f:
        f.write(out)
    d = "".join(difflib.unified_diff(src.splitlines(True), out.splitlines(True), "candidat", "version", n=0))
    with open(diff, "x", encoding="utf-8") as f:
        f.write(d)
    print("version", hashlib.sha256(out.encode("utf-8")).hexdigest())
    print("aucun marqueur restant ; neuf portés")


if __name__ == "__main__":
    main(*sys.argv[1:4])
