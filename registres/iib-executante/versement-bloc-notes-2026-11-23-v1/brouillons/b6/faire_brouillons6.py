#!/usr/bin/env python3
"""Fabrique les brouillons 6 de l'additif et du devis de la voie (A) depuis les brouillons 5, par remplacements exacts.

Usage : faire_brouillons6.py DOSSIER HEURE_UTC (« 18:55 »). Chaque remplacement doit se trouver le nombre de fois attendu,
sinon arrêt. Les passages non nommés restent ceux du brouillon 5, à l'octet. Outil de travail du rédacteur, non versé.
"""
import hashlib
import pathlib
import sys

D = pathlib.Path(sys.argv[1])
H = sys.argv[2]


def sha(nom: str) -> str:
    return hashlib.sha256((D / nom).read_bytes()).hexdigest()


H_PY6, H_OUT6 = sha("calcul-devis-voie-A-v6.py"), sha("sortie-calcul-devis-voie-A-v6.txt")
H_PY5, H_OUT5 = sha("calcul-devis-voie-A-v5.py"), sha("sortie-calcul-devis-voie-A-v5.txt")
H_ADD5, H_DEV5 = sha("additif-ordre-course-voie-A-v1-brouillon5.md"), sha("devis-voie-A-v1-brouillon5.md")
assert H_ADD5 == "e7d9189ce58853c25a9e3bbb1f30f973870abc087ece0d49a303c275bf6231ab"
assert H_DEV5 == "356f53aebfa770e540d1093e8bb50db8fa1b2c5887773a96ec706fb54aaa2e2d"
assert H_PY5 == "9e4bb97e61b40ea8dbbb3038e517d4b039ad8687a318ac973fae6f67ee0524f1"
assert H_OUT5 == "ec46db500d9fdf0bca7f49db5f17b5495a3fe9c18f22d46c4fbc0e04ca151d15"
MANDAT6 = "b9e923fb71ff8dfb365b7024a7051b2b4d725ade0b3f3b16df72324d6ee45814"
MANDAT5 = "c25267a7d9dd8e6a3d9007b15f8b567a493ba4ac7e0d4edea68a1330178bf473"
NOTE5 = "5a09da27a12c909854991c9aeef1137d6a93c29baadabe98e78665793d71e086"
NOEUDS6 = "74c84711e7f6daca1b349f659c40671dfb337bfb7355d79ff5a9e1d3326042cf"
COMMIT6 = "20c6901ebea927f71af1c11c828f3eb10b0ff313"
TETE6, REG6 = "41d2e571588f81e575d2956f79be5bb77f4ad7e7", "4f3ee6cdabb3e858faf30027dc64ec2e84ef98ff9a87b9949ad945589a6e98ca"
TETE5, REG5 = "e50edee227f8776993f9e24ec246e68b73544591", "f09e28de6eb833e7c14556be497797495623c6ed2ae8b66a8349e27b6d726311"
H_ADD4 = "12196e82731d8f60645e5e813b62c3d3ff92e0c7d1b2081e125bd297318d675f"
H_DEV4 = "02730ddd46c95366d76d4184770a95fcb4f7022b4d10db16a895fae673e03983"
SORTIE4 = "df2a357dd1e7f538b6120bef77961f8d696d0b1227309dea97966254257d0065"
NOTE5_CHEMIN = "registres/iib-executante/contre-lecture-voie-A-v1/note-verification-brouillon5-voie-A-cl2.md"


class Texte:
    def __init__(self, nom: str):
        self.t = (D / nom).read_text(encoding="utf-8")

    def r(self, vieux: str, neuf: str, n: int = 1) -> None:
        assert self.t.count(vieux) == n, (self.t.count(vieux), vieux[:100])
        self.t = self.t.replace(vieux, neuf)

    def ecrire(self, nom: str) -> None:
        assert not (D / nom).exists() or "--refaire" in sys.argv, nom
        (D / nom).write_text(self.t, encoding="utf-8")


# =============================================================== ADDITIF ===============================================================
A = Texte("additif-ordre-course-voie-A-v1-brouillon5.md")

# --- en-têtes
A.r("puis course — v1, brouillon 5\n", "puis course — v1, brouillon 6\n")
A.r(f"- **Statut** : brouillon 5, pièce décisive (ordre d'une course payante). Écrit le 2026-11-22 vers 18:39Z (`date -u`) par Claude Fable 5.2, rédacteur, du côté du saboteur, sous le mandat `registres/iib-executante/mandat-fable-brouillon5-voie-A-v1.md` (`{MANDAT5}`), branche `claude/iib-executante-v6` ; les interdits des mandats précédents restent en vigueur. Il est écrit au-dessus du brouillon 4 du même rédacteur (`additif-ordre-course-voie-A-v1-brouillon4.md`, `{H_ADD4}`), lui-même écrit sous le mandat",
    f"- **Statut** : brouillon 6, pièce décisive (ordre d'une course payante). Écrit le 2026-11-22 vers {H}Z (`date -u`) par Claude Fable 5.2, rédacteur, du côté du saboteur, sous le mandat `registres/iib-executante/mandat-fable-brouillon6-voie-A-v1.md` (`{MANDAT6}`), branche `claude/iib-executante-v6` ; les interdits des mandats précédents restent en vigueur. Il est écrit au-dessus du brouillon 5 du même rédacteur (`additif-ordre-course-voie-A-v1-brouillon5.md`, `{H_ADD5}`), que le même contre-lecteur a vérifié : « scellable une fois les champs remplis ». Le brouillon 5 est écrit sous le mandat `registres/iib-executante/mandat-fable-brouillon5-voie-A-v1.md` (`{MANDAT5}`), au-dessus du brouillon 4 (`additif-ordre-course-voie-A-v1-brouillon4.md`, `{H_ADD4}`), lui-même écrit sous le mandat")
A.r("3 et 4 restent intacts (R12)", "3, 4 et 5 restent intacts (R12)")
A.r("- **Cause de la version** : la vérification du brouillon 4 par le même contre-lecteur (",
    f"- **Cause de la version** : la vérification du brouillon 5 par le même contre-lecteur (`{NOTE5_CHEMIN}`, branche `claude/iib-executante-v6`, `{NOTE5}` : « scellable une fois les champs remplis ») ; et deux décisions de la mère, prises le 22 novembre à 18:42Z (mandat ; registre des nœuds de l'exécutante, étage 2, sous `GO-2026-11-22-106`). Une : la borne horaire du nœud qui suit le code 7, selon la règle la plus étroite que propose cette vérification (section C). Deux : le geste du troisième rempart, le même que celui du deuxième. Rien d'autre ne change sur le fond. Les causes du brouillon 5 restent portées : la vérification du brouillon 4 par le même contre-lecteur (")
A.r("Différences, une par ligne : `differences-voie-A-brouillon4-vers-5-v1.md` (les précédentes : `differences-voie-A-brouillon3-vers-4-v1.md`,",
    "Différences, une par ligne : `differences-voie-A-brouillon5-vers-6-v1.md` (les précédentes : `differences-voie-A-brouillon4-vers-5-v1.md`, `differences-voie-A-brouillon3-vers-4-v1.md`,")
A.r(f", et au brouillon 5 à la tête `{TETE5}`, registre `{REG5}`)",
    f", au brouillon 5 à la tête `{TETE5}`, registre `{REG5}`, et au brouillon 6 à la tête `{TETE6}`, registre `{REG6}`)")
A.r(", ligne de 18:21Z.\n- **Devis de la voie**",
    f", ligne de 18:21Z. **Pièces neuves du brouillon 6**, même branche, commit `{COMMIT6}`, chacune conforme à son compagnon : la vérification du brouillon 5 (`{NOTE5_CHEMIN}`, `{NOTE5}`) ; le mandat du brouillon 6 (`{MANDAT6}`) ; le registre des nœuds de l'exécutante, relu (`{NOEUDS6}`), ligne de 18:42Z.\n- **Devis de la voie**")
A.r("- **Devis de la voie** : `devis-voie-A-v1-brouillon5.md`, à côté", "- **Devis de la voie** : `devis-voie-A-v1-brouillon6.md`, à côté")
A.r(f"arithmétique `calcul-devis-voie-A-v5.py` (`{H_PY5}`), sortie `sortie-calcul-devis-voie-A-v5.txt` (`{H_OUT5}`) ; les renvois [Mnn] vont à cette sortie. La v5 refait [M29], [M30] et [M32] et change la sous-commande `second-rempart` ; aucune autre ligne ne change (comparé à la sortie v4, `{SORTIE4}`).",
    f"arithmétique `calcul-devis-voie-A-v6.py` (`{H_PY6}`), sortie `sortie-calcul-devis-voie-A-v6.txt` (`{H_OUT6}`) ; les renvois [Mnn] vont à cette sortie. La v6 ajoute la ligne [M33] et la sous-commande `borne-du-noeud` ; les 28 autres lignes sont égales à l'octet à la sortie v5 (`{H_OUT5}`), et la sous-commande `second-rempart` est inchangée. La v5 (`{H_PY5}`) avait refait [M29], [M30] et [M32] et changé la sous-commande `second-rempart` (comparé à la sortie v4, `{SORTIE4}`).")
A.r("sa sortie v4 reste celle que ce texte cite.\n\n## 0.",
    "sa sortie v4 reste celle que ce texte cite. **Au brouillon 6** : aucun code n'est relu ; rien de ce que joue cette vérification ne dépend de la borne du nœud ni du troisième rempart.\n\n## 0.")

# --- commandes
A.r("python3 -I calcul-devis-voie-A-v5.py", "python3 -I calcul-devis-voie-A-v6.py", 4)

# --- A2
A.r("Le geste du troisième rempart, tenu par la mère, n'est pas écrit dans cet ordre (A3 ; § 7, point 12).",
    "Le troisième rempart, tenu par la mère, ne détruit pas davantage : son geste est un arrêt par l'identifiant (A3).")

# --- A3 : borne horaire du nœud du code 7
A.r("le compte de la voie ; l'heure à laquelle ce compte atteint 60 USD au prix du stockage.\n",
    "le compte de la voie ; l'heure à laquelle ce compte atteint 60 USD au prix du stockage ; l'instant « arrêt plus 33 heures », rendu par le programme.\n"
    "    - **Borne horaire de ce nœud** (décision de la mère du 22 novembre à 18:42Z, selon la règle la plus étroite de la vérification du brouillon 5) [M33]. Par programme, sans appréciation : `python3 -I calcul-devis-voie-A-v6.py borne-du-noeud INSTANT_DE_L_ARRET $(date +%s)`. Il rend trois instants absolus, en UTC, comptés depuis l'arrêt.\n"
    "      - **Arrêt plus 33 heures : le nœud porte cet instant.** Lazar est prié de répondre avant lui : destruction sur son mot exprès, ou relèvement du plafond de la ligne. Le total est alors de 59,71 USD au plus, sous le pire annoncé de 59,76 USD.\n"
    "      - **Arrêt plus 24 heures, sans mot de Lazar (code 8)** : la mère relance Lazar, avec les deux mêmes issues. Total : 58,99 USD au plus.\n"
    "      - **Arrêt plus 36 heures, sans mot de Lazar (code 9)** : le passage du plafond de 60 USD est déclaré à Lazar comme dépense hors devis, à 0,08 USD par heure. Total à cet instant : 59,95 USD au plus ; le plafond est passé après 36,6 heures d'arrêt. La machine reste à l'arrêt.\n"
    "      - **Le silence de Lazar ne vaut jamais accord de destruction.** Aucun de ces codes n'ordonne une destruction.\n"
    "      - **Qui tient le nœud** : l'exécutante tant que sa ligne de session court ; la mère une fois cette ligne échue. Pour une course créée à la dernière heure permise, le code 7 tombe à la fin de cette ligne [M32] : la mère tient alors seule la borne.\n"
    "      - **La mère prévient Lazar de ce cas dès maintenant**, sans attendre qu'il survienne. Aucune ligne d'accord ne couvre une dépense au-delà de 60 USD.\n"
    "      - **Deux faits pour la réponse**, lus à l'ordre scellé et au code de la voie : aucune commande ne lit le disque d'une machine à l'arrêt ; un redémarrage après l'échéance pousse ce qui attend, puis détruit la machine (amorce). Cet ordre ne permet pas ce redémarrage.\n"
    "      - Ces totaux sont comptés pour un arrêt venu à l'échéance plus 90 minutes au plus. Le compte vrai de la voie, porté au nœud, prime sur eux.\n")
A.r("Le total reste sous 60 USD tant que l'arrêt dure moins de 36,6 heures. Réserve nommée (§ 7, point 9).",
    "Le total reste sous 60 USD tant que l'arrêt dure moins de 36,6 heures. Cette durée est bornée par l'heure et par la réponse de Lazar, non par un code [M33]. Réserve nommée (§ 7, point 8).")
A.r("l'exécutante rejoue les huit cas de [M30], cas sains et artefacts, et les compare à la sortie.",
    "l'exécutante rejoue les huit cas de [M30] et les sept cas de [M33], cas sains et artefacts, et les compare à la sortie.")

# --- A3 : troisième rempart
A.r("  - **Troisième rempart, tenu par la mère.** Dès la création, elle double la minuterie dans son propre conteneur, sur la même échéance absolue : l'instant passé en sixième argument de `creation`. Comme pour la machine des lentilles. Ce rempart ne dépend ni de la machine ni de la session de l'exécutante. Il n'est compté dans aucun pire. Son geste n'est pas écrit dans cet ordre (§ 7, point 12).\n",
    "  - **Troisième rempart, tenu par la mère : le même geste que le deuxième** (décision de la mère du 22 novembre à 18:42Z). Dès la création, elle double la minuterie dans son propre conteneur, sur la même échéance absolue : l'instant passé en sixième argument de `creation`. Comme pour la machine des lentilles. Ce rempart ne dépend ni de la machine ni de la session de l'exécutante.\n"
    "    - **Aucun geste avant l'échéance plus 80 minutes** : plus tôt, il couperait la consignation de la minuterie de l'amorce.\n"
    "    - **Ensuite, si la machine tourne encore : arrêt par l'identifiant, jamais de destruction.** Machine absente ou déjà à l'arrêt : aucun geste.\n"
    "    - **Puis les mêmes codes 5 et 7**, par la même règle `second-rempart` : rapatriement et vérification ; destruction après rapatriement vérifié seulement ; sinon machine gardée à l'arrêt, nœud à Lazar, et la borne horaire écrite plus haut.\n"
    "    - **Message à la mère et à Lazar**, aussitôt.\n"
    "    - **Ce qu'il change** [M29]. Si la minuterie fait défaut et que la session de l'exécutante meurt, la réserve de 64,76 USD tombe au chemin de 57,07 USD à l'instant de l'arrêt ; ensuite, le stockage seul.\n"
    "    - **Il n'est compté dans aucun pire** : il vit dans le conteneur de la mère, et cet ordre ne l'éprouve pas.\n")
A.r("**Ce qui ne l'est pas** : deux réserves nommées. Une (§ 7, point 9) : la machine arrêtée par le deuxième rempart et gardée à l'arrêt sans rapatriement vérifié coûte 0,08 USD par heure, sans borne tenue par un code ; le total passe 59,76 USD après 33,6 heures d'arrêt, et le plafond après 36,6 heures. Deux (§ 7, point 8) : la surveillance et le deuxième rempart vivent dans la session de l'exécutante. Si la minuterie et cette session font défaut ensemble, rien dans cet ordre ne borne la dépense ; seul le doublement par la mère reste.",
    "**Ce qui ne l'est pas** : deux réserves nommées (§ 7, point 8). Une : la machine arrêtée par le deuxième ou le troisième rempart et gardée à l'arrêt sans rapatriement vérifié coûte 0,08 USD par heure, sans borne tenue par un code. La borne est horaire, et tient à la réponse de Lazar : le total passe 59,76 USD après 33,6 heures d'arrêt, et le plafond après 36,6 heures ; à 36 heures, la dépense est déclarée hors devis [M33]. Deux : la surveillance et le deuxième rempart vivent dans la session de l'exécutante. Si la minuterie et cette session font défaut ensemble, seul le troisième rempart reste : il ramène la voie au chemin de 57,07 USD à l'instant de l'arrêt. S'il fait défaut lui aussi, rien dans cet ordre ne borne la dépense.")

# --- § 3, § 4, § 5, § 6
A.r("les quatre sous-commandes du programme de calcul rejouées sur leurs cas de contrôle ([M18], [M20] à [M26], [M30])",
    "les cinq sous-commandes du programme de calcul rejouées sur leurs cas de contrôle ([M18], [M20] à [M26], [M30], [M33])")
A.r("| § 9, devis | le devis de la voie (A), brouillon 5 |", "| § 9, devis | le devis de la voie (A), brouillon 6 |")
A.r("6. **Deuxième rempart éprouvé** sur les huit cas de [M30], et **ligne de session vérifiée**",
    "6. **Deuxième rempart éprouvé** sur les huit cas de [M30], **borne du nœud éprouvée** sur les sept cas de [M33], et **ligne de session vérifiée**")
A.r("l'épreuve du deuxième rempart, l'instant de son réveil et, s'il a joué, chacun de ses codes et de ses gestes ;",
    "l'épreuve du deuxième rempart et celle de la borne du nœud, l'instant du réveil et, si le rempart a joué, chacun de ses codes et de ses gestes ; après un code 7, les trois instants de la borne du nœud ;")
A.r("épreuve du deuxième rempart non conforme à [M30] ;",
    "épreuve du deuxième rempart non conforme à [M30], ou de la borne du nœud non conforme à [M33] ;")
A.r("Rapatriement non vérifié deux heures après l'arrêt : machine gardée à l'arrêt, disque gardé, nœud à Lazar ; aucune destruction. État ou instant illisible",
    "Rapatriement non vérifié deux heures après l'arrêt : machine gardée à l'arrêt, disque gardé, nœud à Lazar ; aucune destruction. Le nœud porte l'instant « arrêt plus 33 heures » ; à l'arrêt plus 24 heures sans mot de Lazar, la mère le relance ; à l'arrêt plus 36 heures, le passage du plafond est déclaré comme dépense hors devis ; le silence de Lazar ne vaut jamais accord de destruction (A3). Si l'exécutante est muette à l'échéance plus 80 minutes, la mère fait le même geste, par la même règle : arrêt par l'identifiant, jamais de destruction (troisième rempart, A3). État ou instant illisible")
A.r("Le brouillon 5 ne remplit ni n'ajoute aucun champ.", "Les brouillons 5 et 6 ne remplissent ni n'ajoutent aucun champ.")
A.r("`devis-voie-A-v1-brouillon5.md.sha256`", "`devis-voie-A-v1-brouillon6.md.sha256`")

# --- § 7 : points tranchés retirés (anciens points 9 et 12), réserves réunies au point 8
A.r("le deuxième rempart ne détruit qu'après lui.\n", "le deuxième rempart ne détruit qu'après lui ; le geste du troisième est un arrêt.\n")
i8, i9, i10 = A.t.index("\n8. **Réserve nommée, pour Lazar : ce que les remparts de dépense tiennent**"), A.t.index("\n9. **Deuxième rempart : forme tranchée par la mère"), A.t.index("\n10. **Ligne de session de l'exécutante**")
i11, i12 = A.t.index("\n11. **Scellement d'un même geste**"), A.t.index("\n12. **Troisième rempart : son geste reste à écrire par la mère**")
assert i8 < i9 < i10 < i11 < i12 and A.t.endswith("un arrêt par l'identifiant garderait le disque.\n")
POINT8 = ("\n8. **Réserves nommées, pour Lazar : ce que les remparts de dépense tiennent** (A3, [M29], [M33]). La minuterie de l'amorce seule : 56,61 USD. "
          "L'exécutante seule, à l'échéance plus 80 minutes, rapatriement vérifié : 57,23 USD. Fin normale, puis 48 heures d'arrêt : 58,84 USD. "
          "Le pire annoncé de 59,76 USD couvre ces trois cas. Deux cas restent hors de lui. "
          "**Un : la machine gardée à l'arrêt sans rapatriement vérifié** (code 7). Elle coûte 57,07 USD à l'instant de l'arrêt, puis 0,08 USD par heure : "
          "59,71 USD à 33 heures, 59,95 USD à 36 heures, 60,91 USD à 48 heures. Aucun code ne borne cette durée : la borne est horaire, et tient à la réponse de Lazar. "
          "À 36 heures sans son mot, la dépense est déclarée hors devis, et la machine reste à l'arrêt ; son silence ne vaut jamais accord de destruction. "
          "**Deux : la minuterie et l'exécutante en défaut ensemble.** La surveillance du lanceur, seule, laisserait aller jusqu'à 64,76 USD ; "
          "elle vit dans la session de l'exécutante, et tombe avec elle. Le troisième rempart, tenu par la mère, ramène ce cas au chemin de 57,07 USD à l'instant de l'arrêt. "
          "Il n'est compté dans aucun pire : s'il fait défaut lui aussi, rien dans cet ordre ne borne la dépense.")
point10 = A.t[i10:i11].replace("\n10. **Ligne de session de l'exécutante**", "\n9. **Ligne de session de l'exécutante**")
assert point10.endswith("Les créations restent permises par la ligne de calcul jusqu'au 26 inclus.")
point10 += " Après un code 7, la mère tient le nœud une fois cette ligne échue (A3)."
point11 = A.t[i11:i12].replace("\n11. **Scellement d'un même geste**", "\n10. **Scellement d'un même geste**")
A.t = A.t[:i8] + POINT8 + point10 + point11 + "\n"

assert A.t.count("<<ENTROPIE_VOIE_A>>") == 2 and A.t.count("<<EMPREINTE_CONFIG_VOIE_A>>") == 2 and A.t.count("<<COMMIT_LANCEMENT_ETALONNAGE_VOIE_A>>") == 2
assert A.t.count("<<") == 6 and "point 12" not in A.t and "§ 7, point 9" not in A.t and "calcul-devis-voie-A-v5" not in A.t
A.ecrire("additif-ordre-course-voie-A-v1-brouillon6.md")

# ================================================================ DEVIS ================================================================
V = Texte("devis-voie-A-v1-brouillon5.md")
V.r("puis course — v1, brouillon 5\n", "puis course — v1, brouillon 6\n")
V.r(f"- **Statut** : brouillon 5, pièce décisive (devis). Écrit le 2026-11-22 vers 18:39Z (`date -u`) par Claude Fable 5.2, rédacteur, du côté du saboteur, sous le mandat `mandat-fable-brouillon5-voie-A-v1.md` (`{MANDAT5}`) ; les interdits des mandats précédents restent en vigueur. Il est écrit au-dessus du brouillon 4 du même rédacteur (`{H_DEV4}`), lui-même écrit sous le mandat",
    f"- **Statut** : brouillon 6, pièce décisive (devis). Écrit le 2026-11-22 vers {H}Z (`date -u`) par Claude Fable 5.2, rédacteur, du côté du saboteur, sous le mandat `mandat-fable-brouillon6-voie-A-v1.md` (`{MANDAT6}`) ; les interdits des mandats précédents restent en vigueur. Il est écrit au-dessus du brouillon 5 du même rédacteur (`{H_DEV5}`), que le même contre-lecteur a vérifié : « scellable une fois les champs remplis ». Le brouillon 5 est écrit sous le mandat `mandat-fable-brouillon5-voie-A-v1.md` (`{MANDAT5}`), au-dessus du brouillon 4 (`{H_DEV4}`), lui-même écrit sous le mandat")
V.r("3 et 4 restent intacts (R12)", "3, 4 et 5 restent intacts (R12)")
V.r("- **Cause de la version** : la vérification du brouillon 4 (`note-verification-brouillon4-voie-A-cl2.md`,",
    f"- **Cause de la version** : la vérification du brouillon 5 (`note-verification-brouillon5-voie-A-cl2.md`, `{NOTE5}`, « scellable une fois les champs remplis ») et deux décisions de la mère, prises le 22 novembre à 18:42Z : la borne horaire du nœud qui suit une machine gardée à l'arrêt, selon la règle la plus étroite de cette vérification ; le geste du troisième rempart, le même que celui du deuxième. Aucun chiffre du brouillon 5 ne change ; deux chiffres s'ajoutent, 59,71 et 59,95 USD [M33]. Les causes du brouillon 5 restent portées : la vérification du brouillon 4 (`note-verification-brouillon4-voie-A-cl2.md`,")
V.r("Différences, une par ligne : `differences-voie-A-brouillon4-vers-5-v1.md`.", "Différences, une par ligne : `differences-voie-A-brouillon5-vers-6-v1.md`.")
V.r(f"puis à la tête `{TETE5}`, `{REG5}` : lignes inchangées)", f"puis à la tête `{TETE5}`, `{REG5}`, puis à la tête `{TETE6}`, `{REG6}` : lignes inchangées)")
V.r("- **Ordre chiffré** : `additif-ordre-course-voie-A-v1-brouillon5.md`", "- **Ordre chiffré** : `additif-ordre-course-voie-A-v1-brouillon6.md`")
V.r(f"- **Arithmétique** : `calcul-devis-voie-A-v5.py` (`{H_PY5}`), sortie `sortie-calcul-devis-voie-A-v5.txt` (`{H_OUT5}`), à côté. Depuis la v4 : [M29], [M30] et [M32] refaits, sous-commande `second-rempart` changée ; aucune autre ligne ne change.",
    f"- **Arithmétique** : `calcul-devis-voie-A-v6.py` (`{H_PY6}`), sortie `sortie-calcul-devis-voie-A-v6.txt` (`{H_OUT6}`), à côté. Depuis la v5 (`{H_PY5}`, sortie `{H_OUT5}`) : ligne [M33] et sous-commande `borne-du-noeud` ajoutées ; les 28 autres lignes sont égales à l'octet.")
V.r("python3 -I calcul-devis-voie-A-v5.py", "python3 -I calcul-devis-voie-A-v6.py", 3)

# --- § 4
V.r("| machine gardée à l'arrêt, disque gardé, aucune destruction ; nœud à Lazar | 57,07 USD à l'instant de l'arrêt, puis 0,08 USD par heure : 58,99 USD à 24 heures ; **60,91 USD à 48 heures : au-delà du plafond** ; sous 60 USD jusqu'à 36,6 heures d'arrêt |",
    "| machine gardée à l'arrêt, disque gardé, aucune destruction ; nœud à Lazar, qui porte l'instant « arrêt plus 33 heures » ; relance par la mère à 24 heures ; à 36 heures, passage du plafond déclaré comme dépense hors devis (décision de la mère du 22 novembre à 18:42Z) | 57,07 USD à l'instant de l'arrêt, puis 0,08 USD par heure : 58,99 USD à 24 heures ; 59,71 USD à 33 heures ; 59,95 USD à 36 heures [M33] ; **60,91 USD à 48 heures : au-delà du plafond** ; sous 60 USD jusqu'à 36,6 heures d'arrêt |")
V.r("| son geste et son instant restent à écrire par elle (additif, § 7, point 12) | non compté |",
    "| le même geste que le deuxième (décision de la mère du 22 novembre à 18:42Z) : aucun geste avant l'échéance plus 80 minutes ; ensuite, si la machine tourne encore, arrêt par l'identifiant, jamais de destruction ; puis les mêmes codes 5 et 7 ; message à la mère et à Lazar | non compté ; s'il joue, la ligne précédente tombe au chemin de 57,07 USD à l'instant de l'arrêt |")
V.r("éprouvée avant toute création sur huit cas, sains et artefacts [M30]. Elle n'ordonne jamais une destruction.",
    "éprouvée avant toute création sur huit cas, sains et artefacts [M30]. Elle n'ordonne jamais une destruction. La borne horaire du nœud est jouée par programme elle aussi (`python3 -I calcul-devis-voie-A-v6.py borne-du-noeud …`), éprouvée sur sept cas [M33]. Elle n'ordonne aucune destruction non plus : le silence de Lazar ne vaut jamais accord de destruction.")

# --- § 6
V.r("sans lui, deux heures après l'arrêt : machine gardée à l'arrêt, nœud à Lazar |",
    "sans lui, deux heures après l'arrêt : machine gardée à l'arrêt, nœud à Lazar, borné par l'heure (réponse avant 33 heures ; relance à 24 ; dépense hors devis déclarée à 36). Exécutante muette : la mère fait le même geste (troisième rempart) |")
V.r("| épreuve du deuxième rempart non conforme ;", "| épreuve du deuxième rempart ou de la borne du nœud non conforme ;")

# --- § 7
V.r("Le doublement de la minuterie par la mère couvre ce cas ; il n'est pas compté.",
    "Le troisième rempart, tenu par la mère, couvre ce cas par le même geste que le deuxième : arrêt par l'identifiant à l'échéance plus 80 minutes, jamais de destruction. La voie revient alors au chemin de 57,07 USD à l'instant de l'arrêt. Il n'est pas compté : s'il fait défaut lui aussi, rien dans l'ordre ne borne la dépense.")
V.r("le total reste sous 59,76 USD jusqu'à 33,6 heures d'arrêt, sous 60 USD jusqu'à 36,6 heures. Les 59,30 USD",
    "le total reste sous 59,76 USD jusqu'à 33,6 heures d'arrêt, sous 60 USD jusqu'à 36,6 heures. **Borne horaire, décidée par la mère le 22 novembre à 18:42Z** [M33] : le nœud porte l'instant « arrêt plus 33 heures » (59,71 USD au plus) ; à 24 heures sans mot de Lazar, la mère le relance (destruction sur son mot exprès, ou relèvement du plafond de la ligne) ; à 36 heures (59,95 USD au plus), le passage du plafond est déclaré comme dépense hors devis, à 0,08 USD par heure, et la machine reste à l'arrêt. Le silence de Lazar ne vaut jamais accord de destruction. La mère tient ce nœud une fois échue la ligne de session de l'exécutante ; elle prévient Lazar de ce cas dès maintenant. Les 59,30 USD")

# --- § 8
V.r("| **accepter la réserve, et répondre au nœud dans les 33 heures qui suivent l'arrêt** : le total reste alors sous le pire annoncé. Détruire sans versement est exclu (règle de Lazar). Revenir à un seuil plus court rouvrirait le défaut relevé par la vérification du brouillon 4 | moyenne |",
    "| **règle tranchée par la mère le 22 novembre à 18:42Z** : borne horaire du nœud. Ce qui reste demandé à Lazar : répondre au nœud avant l'arrêt plus 33 heures, par la destruction ou par le relèvement du plafond de la ligne ; le total reste alors sous le pire annoncé. Son silence ne vaut jamais accord de destruction ; à 36 heures sans son mot, la dépense est déclarée hors devis | — |")
V.r("| **l'accepter, avec le doublement de la minuterie par la mère** ; sinon,",
    "| **l'accepter, avec le troisième rempart tenu par la mère**, dont le geste est tranché (arrêt par l'identifiant à l'échéance plus 80 minutes, jamais de destruction) ; sinon,")

assert "<<" not in V.t and "point 12" not in V.t and "calcul-devis-voie-A-v5" not in V.t
V.ecrire("devis-voie-A-v1-brouillon6.md")
print("additif", len(A.t), "devis", len(V.t), H_PY6, H_OUT6)
