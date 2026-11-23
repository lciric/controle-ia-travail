#!/usr/bin/env python3
"""Fabrique les brouillons 5 de l'additif et du devis de la voie (A) depuis les brouillons 4, par remplacements exacts.

Usage : faire_brouillons5.py DOSSIER HEURE_UTC (« 18:55 »). Chaque remplacement doit se trouver le nombre de fois attendu,
sinon arrêt. Les passages non nommés restent ceux du brouillon 4, à l'octet. Outil de travail du rédacteur, non versé.
"""
import hashlib
import pathlib
import sys

D = pathlib.Path(sys.argv[1])
H = sys.argv[2]


def sha(nom: str) -> str:
    return hashlib.sha256((D / nom).read_bytes()).hexdigest()


H_PY, H_OUT = sha("calcul-devis-voie-A-v5.py"), sha("sortie-calcul-devis-voie-A-v5.txt")
H_ADD4, H_DEV4 = sha("additif-ordre-course-voie-A-v1-brouillon4.md"), sha("devis-voie-A-v1-brouillon4.md")
assert H_ADD4 == "12196e82731d8f60645e5e813b62c3d3ff92e0c7d1b2081e125bd297318d675f"
assert H_DEV4 == "02730ddd46c95366d76d4184770a95fcb4f7022b4d10db16a895fae673e03983"
MANDAT5 = "c25267a7d9dd8e6a3d9007b15f8b567a493ba4ac7e0d4edea68a1330178bf473"
NOTE4 = "b5e73a07a68893784a513932e87ef78b4aa1205123745f31406eeb050ecdf6fc"
NOEUDS = "853969df7fe58d56de7d58680ce6b24df6dfb4d95d42fa9c845ef8f3958be178"
MANDAT4 = "c5c2d5de3565f75b28e1a75ecf801345d49a45351f3d5f3e63a825f51086188d"
ERR1 = "4642543ba8e0371e55d03535f3a05a9f1eaa90ce707ce4a27494f1c8847ee3f9"
ERR2 = "a25933195cd84437b0672aa89fbf8ad4c1c7c364042e2463f84d7e2718862793"
NOTE3 = "b96d839e57f7a915eb74b702c14657dc0c21ab2e56e61041c9a54d925dce419b"
TETE5, REG5 = "e50edee227f8776993f9e24ec246e68b73544591", "f09e28de6eb833e7c14556be497797495623c6ed2ae8b66a8349e27b6d726311"
TETE4, REG4 = "4e47b5d6901540d07285632d469166ccb9634465", "7776d2003ba19b856475f9be8022a7bc05eca663843c847758b24d4386f4a5c5"


class Texte:
    def __init__(self, nom: str):
        self.t = (D / nom).read_text(encoding="utf-8")

    def r(self, vieux: str, neuf: str, n: int = 1) -> None:
        assert self.t.count(vieux) == n, (self.t.count(vieux), vieux[:100])
        self.t = self.t.replace(vieux, neuf)

    def _ligne(self, prefixe: str) -> str:
        lignes = [l for l in self.t.split("\n") if l.startswith(prefixe)]
        assert len(lignes) == 1, (len(lignes), prefixe)
        return lignes[0]

    def ligne(self, prefixe: str, neuf: str) -> None:
        """Remplace en entier la seule ligne qui commence par `prefixe`."""
        vieux = self._ligne(prefixe)
        assert self.t.count(vieux + "\n") == 1
        self.t = self.t.replace(vieux + "\n", neuf + "\n")

    def ajoute_en_fin(self, prefixe: str, suite: str) -> None:
        vieux = self._ligne(prefixe)
        self.ligne(prefixe, vieux + suite)

    def bloc(self, debut: str, fin: str, neuf: str) -> None:
        """Remplace les lignes entières, de celle qui commence par `debut` à celle qui commence par `fin`, comprises."""
        a, b = self._ligne(debut), self._ligne(fin)
        i, j = self.t.index(a + "\n"), self.t.index(b + "\n") + len(b) + 1
        assert i < j
        self.t = self.t[:i] + neuf + "\n" + self.t[j:]

    def ecrit(self, nom: str) -> None:
        assert not (D / nom).exists() or "--refaire" in sys.argv, nom
        (D / nom).write_text(self.t, encoding="utf-8")


# ================================================================== ADDITIF
A = Texte("additif-ordre-course-voie-A-v1-brouillon4.md")
A.r("puis course — v1, brouillon 4", "puis course — v1, brouillon 5")

A.ligne("- **Statut** : brouillon 4,", (
    f"- **Statut** : brouillon 5, pièce décisive (ordre d'une course payante). Écrit le 2026-11-22 vers {H}Z (`date -u`) par Claude Fable 5.2, rédacteur, du côté du saboteur, "
    f"sous le mandat `registres/iib-executante/mandat-fable-brouillon5-voie-A-v1.md` (`{MANDAT5}`), branche `claude/iib-executante-v6` ; les interdits des mandats précédents restent en vigueur. "
    f"Il est écrit au-dessus du brouillon 4 du même rédacteur (`additif-ordre-course-voie-A-v1-brouillon4.md`, `{H_ADD4}`), lui-même écrit sous le mandat "
    f"`registres/iib-executante/mandat-fable-brouillon4-voie-A-v1.md` (`{MANDAT4}`) et ses errata 1 (`{ERR1}`) et 2 (`{ERR2}`). "
    "Le brouillon 3 (`additif-ordre-course-voie-A-v1-brouillon3.md`, `3d658ce0d6af1a44cc69a8b10306379a9cdae51f59a35e7a29005ddf6845152f`) a été rédigé par Claude Opus 5.5 en l'absence de Fable ; "
    "Fable l'a relu en entier au brouillon 4 et en a pris la responsabilité de rédacteur. "
    "Les brouillons 1 (`7cef2bda410de2dea0d467eeb891c04c22942db603165327054ebe85bf74537d`), 2 (`709e15357d6d9d53461414ca77a39746a95af3131eb8804185fc3d205731d15d`), 3 et 4 restent intacts (R12). "
    "Ni scellé ni remis avant : la relecture de cette version par le même contre-lecteur, le remplissage de ses derniers champs (§ 6) et son scellement par la mère. "
    "Le rédacteur entre dans la liste d'exclusion des rôles côté sondes. Il n'a ouvert aucune consigne privée, aucune sortie de mesure, aucune pièce du côté des sondes ; "
    "il n'a rien dépensé, appelé aucun loueur, supprimé aucun fichier."))

A.ligne("- **Cause de la version** :", (
    "- **Cause de la version** : la vérification du brouillon 4 par le même contre-lecteur (`registres/iib-executante/contre-lecture-voie-A-v1/note-verification-brouillon4-voie-A-cl2.md`, "
    f"branche `claude/iib-executante-v6`, `{NOTE4}` : « scellable après corrections », deux majeurs et deux mineurs, tous sur le deuxième rempart de dépense) ; "
    "et les décisions de la mère sur cette vérification, prises le 22 novembre à 18:21Z (mandat ; registre des nœuds de l'exécutante, étage 2, sous `GO-2026-11-22-106`). "
    "Quatre points : seuil du deuxième rempart à l'échéance plus 80 minutes ; aucune destruction sans rapatriement vérifié ; un instant d'arrêt placé dans le futur est refusé, huitième cas de garde ; "
    "troisième rempart tenu par la mère. Les causes du brouillon 4 restent portées : la vérification du brouillon 3 "
    f"(`registres/iib-executante/contre-lecture-voie-A-v1/note-verification-brouillon3-voie-A-cl2.md`, `{NOTE3}`), les correctifs 0024 et 0025 et le code final de la voie, "
    "la configuration de la voie sans son entropie. Différences, une par ligne : `differences-voie-A-brouillon4-vers-5-v1.md` "
    "(les précédentes : `differences-voie-A-brouillon3-vers-4-v1.md`, `differences-voie-A-brouillon2-vers-3-v1.md`, `differences-voie-A-brouillon1-vers-2-v1.md`)."))

A.r(f"et au brouillon 4 à la tête `{TETE4}`, registre `{REG4}`)",
    f"au brouillon 4 à la tête `{TETE4}`, registre `{REG4}`, et au brouillon 5 à la tête `{TETE5}`, registre `{REG5}`)")
A.ajoute_en_fin("- **Ligne d'accord** :", (
    " **Et `GO-2026-11-22-106`** (décision, mots de Lazar vers 17:40Z) : autonomie de douze heures des sessions, « dépenses sous les lignes inscrites seulement » ; "
    "c'est sous elle que la mère a pris, à l'étage 2 de la chaîne de décision, les décisions que ce brouillon porte."))

A.ajoute_en_fin("- **Pièces citées** ", (
    " **Pièces neuves du brouillon 5**, même branche, commit `468bc194ea147a1115159cb7f5cc4bb834c8bac8`, chacune conforme à son compagnon : la vérification du brouillon 4 "
    f"(`registres/iib-executante/contre-lecture-voie-A-v1/note-verification-brouillon4-voie-A-cl2.md`, `{NOTE4}`) ; le mandat du brouillon 5 (`{MANDAT5}`) ; "
    f"le registre des nœuds de l'exécutante (`registres/iib-executante/registre-noeuds-autonomie-executante-v1.md`, `{NOEUDS}`), ligne de 18:21Z."))

A.ligne("- **Devis de la voie** :", (
    f"- **Devis de la voie** : `devis-voie-A-v1-brouillon5.md`, à côté (empreinte dans son compagnon, relevée au § 6) ; arithmétique `calcul-devis-voie-A-v5.py` (`{H_PY}`), "
    f"sortie `sortie-calcul-devis-voie-A-v5.txt` (`{H_OUT}`) ; les renvois [Mnn] vont à cette sortie. La v5 refait [M29], [M30] et [M32] et change la sous-commande `second-rempart` ; "
    "aucune autre ligne ne change (comparé à la sortie v4, `df2a357dd1e7f538b6120bef77961f8d696d0b1227309dea97966254257d0065`)."))

A.ajoute_en_fin("- **Code lu, et vérifié par exécution sur processeur** :", (
    " **Au brouillon 5** : la minuterie des deux amorces et la sous-commande `destruction` du lanceur sont relues à l'arbre de la voie, ligne à ligne. "
    "La vérification des gardes du lanceur n'est pas rejouée : rien de ce qu'elle joue ne change (mandat) ; sa sortie v4 reste celle que ce texte cite."))

# --- A2
A.r("après son rapatriement vérifié ; sans rapatriement vérifié, aucune destruction, sauf par la minuterie de l'amorce, à l'échéance (ordre scellé ; A3), "
    "et sauf par le second rempart, sur une machine que cette minuterie n'a pas détruite (A3).",
    "après son rapatriement vérifié. **Sans rapatriement vérifié, aucune destruction par une session** : ni par l'exécutante, ni par le deuxième rempart, ni sur un mot donné d'avance "
    "(règle de Lazar, R-3661 ; décision de la mère du 22 novembre à 18:21Z). Sur la machine, la minuterie de l'amorce détruit à l'échéance, après avoir consigné et poussé "
    "(ordre scellé ; A3 ; § 7, point 3). Le geste du troisième rempart, tenu par la mère, n'est pas écrit dans cet ordre (A3 ; § 7, point 12).")

# --- A3
A.r("`python3 -I calcul-devis-voie-A-v4.py echeance 55 COMPTE", "`python3 -I calcul-devis-voie-A-v5.py echeance 55 COMPTE")

A.ligne("  - **Premier rempart, sur la machine", (
    "  - **Premier rempart, sur la machine : la minuterie de l'amorce.** À l'échéance, elle consigne et pousse ce qui est écrit (40 minutes au plus), puis détruit la machine "
    "(30 minutes d'essais au plus) : c'est une destruction, non un arrêt. Sa fenêtre normale dure donc 70 minutes après l'échéance : pendant ce temps, une machine qui tourne n'est pas un défaut. "
    "Si elle joue seule, les deux gardes de la session tombées, le pire de la voie est de 55 + 1,61 = **56,61 USD**, sous le plafond de 60 USD. Pour une course, elle n'a jamais été éprouvée (§ 7)."))

DEJA_A_L_ARRET = A._ligne("    - **Une machine déjà à l'arrêt à cet instant**")
A.bloc("  - **Deuxième rempart, du côté de la session", "    - **Épreuve avant toute création (R5)**", "\n".join((
    "  - **Deuxième rempart, du côté de la session : l'exécutante, à l'échéance plus 80 minutes** (décision de la mère du 22 novembre à 18:21Z). "
    "Le seuil est la fenêtre normale de la minuterie, plus 10 minutes : 2 400 + 1 800 + 600 = 4 800 secondes. Avant lui, arrêter la machine couperait la consignation et tuerait la minuterie. "
    "Règle par programme, sans appréciation : `python3 -I calcul-devis-voie-A-v5.py second-rempart ECHEANCE_S $(date +%s) ETAT`. ETAT est lu à l'inventaire en champs filtrés : « absente » ; "
    "« arret » (état `exited` ou `stopped`, la liste fermée du lanceur) ; « tourne » (tout autre état). Un inventaire illisible n'est pas une absence. "
    "**Cette règle n'ordonne jamais une destruction.**",
    "    - **Code 0, avant le seuil** : aucun geste par cette règle, même si la machine tourne.",
    "    - **Code 4** : la machine tourne encore au seuil ; la minuterie a fait défaut. L'exécutante l'arrête aussitôt par son identifiant, relit son état et note l'instant de l'arrêt. "
    "Le lanceur ne détruit jamais une machine qui tourne (sa sous-commande `destruction` refuse tout état hors de sa liste fermée).",
    "    - **Puis** `second-rempart ECHEANCE_S $(date +%s) arret INSTANT_DE_L_ARRET`. **Code 5** : elle rapatrie ce qui est versé et le vérifie, comme à l'ordre scellé (§ 5, étape 5) : "
    "chaque fichier listé, un par un. La machine à l'arrêt ne coûte que le stockage : 0,16 USD au plus pour deux heures.",
    "    - **Rapatriement vérifié** : elle détruit la machine par son identifiant, par la sous-commande `destruction`, avec `RAPATRIEMENT_VERIFIE=oui` au seul sens « rapatriement vérifié ». "
    "Puis elle rend la main à la mère : nœud.",
    "    - **Code 7, deux heures après l'arrêt, sans rapatriement vérifié : la machine est gardée à l'arrêt, le disque est gardé, nœud à Lazar.** L'exécutante ne détruit pas. "
    "Elle porte au nœud, par la mère : l'instant de l'arrêt ; ce qui est vérifié et ce qui manque ; le compte de la voie ; l'heure à laquelle ce compte atteint 60 USD au prix du stockage.",
    "    - **Aucune destruction sans rapatriement vérifié** (règle de Lazar, R-3661 ; décision de la mère). Le mot que la mère donne d'avance (A2) ne couvre aucun écart. "
    "Le code 6 du brouillon 4, qui détruisait « rapatriement vérifié ou non », est retiré : le programme ne le rend plus.",
    "    - **Code 2** (état illisible ; instant illisible ou incohérent : arrêt daté d'avant le seuil, ou placé dans le futur) : aucun geste par cette règle ; message à la mère aussitôt.",
    DEJA_A_L_ARRET,
    "    - **Ce que ce rempart coûte** [M29]. Rapatriement vérifié : **57,23 USD** au pire. Machine gardée à l'arrêt : 57,07 USD à l'instant de l'arrêt, puis 0,08 USD par heure ; "
    "58,99 USD à 24 heures ; **60,91 USD à 48 heures, au-delà du plafond**. Le total reste sous 60 USD tant que l'arrêt dure moins de 36,6 heures. Réserve nommée (§ 7, point 9).",
    "    - **Épreuve avant toute création (R5)** : l'exécutante rejoue les huit cas de [M30], cas sains et artefacts, et les compare à la sortie. Dès la création confirmée, "
    "elle programme son réveil à l'échéance plus 80 minutes et le porte au compte rendu. Épreuve non conforme : aucune création.")))

A.ligne("  - **Troisième rempart : la mère**", (
    "  - **Troisième rempart, tenu par la mère.** Dès la création, elle double la minuterie dans son propre conteneur, sur la même échéance absolue : l'instant passé en sixième argument de `creation`. "
    "Comme pour la machine des lentilles. Ce rempart ne dépend ni de la machine ni de la session de l'exécutante. Il n'est compté dans aucun pire. "
    "Son geste n'est pas écrit dans cet ordre (§ 7, point 12)."))

A.ligne("  - **Ce qui est tenu** :", (
    "  - **Ce qui est tenu** : 59,76 USD au plus [M14], si la minuterie de l'amorce joue, ou si l'exécutante joue et que son rapatriement est vérifié. "
    "**Ce qui ne l'est pas** : deux réserves nommées. Une (§ 7, point 9) : la machine arrêtée par le deuxième rempart et gardée à l'arrêt sans rapatriement vérifié coûte 0,08 USD par heure, "
    "sans borne tenue par un code ; le total passe 59,76 USD après 33,6 heures d'arrêt, et le plafond après 36,6 heures. "
    "Deux (§ 7, point 8) : la surveillance et le deuxième rempart vivent dans la session de l'exécutante. Si la minuterie et cette session font défaut ensemble, "
    "rien dans cet ordre ne borne la dépense ; seul le doublement par la mère reste."))

A.ligne("- **Ligne de session de l'exécutante.**", (
    "- **Ligne de session de l'exécutante.** `GO-2026-11-22-94` échoit le 2026-11-25. Le deuxième rempart demande l'exécutante jusqu'à 3 heures 30 après l'échéance de la machine : "
    "4 800 secondes de seuil, 600 de geste, 7 200 de rapatriement, soit 12 600 secondes [M32]. Avant chaque création : si l'échéance calculée plus 12 600 secondes dépasse "
    "2026-11-26T00:00:00Z (`1795651200`), aucune création sans un mot de Lazar qui prolonge la session, ou sans que la mère prenne par écrit le deuxième rempart. "
    "Pour une course à l'échéance de 30 heures : création au plus tard le 2026-11-24 à 14:30Z [M32]."))

# --- A4, A5
A.r("`python3 -I calcul-devis-voie-A-v4.py rythme-etalonnage 55 0`", "`python3 -I calcul-devis-voie-A-v5.py rythme-etalonnage 55 0`")
A.r("`python3 -I calcul-devis-voie-A-v4.py garde-de-rythme 55 COMPTE", "`python3 -I calcul-devis-voie-A-v5.py garde-de-rythme 55 COMPTE")

# --- § 3.4
A.r("autre que `carte`, arrêt (§ 5) ; à l'échéance plus 10 minutes, le deuxième rempart (A3) |", "autre que `carte`, arrêt (§ 5) ; à l'échéance plus 80 minutes, le deuxième rempart (A3) |")
A.r("| § 9, devis | le devis de la voie (A), brouillon 4 |", "| § 9, devis | le devis de la voie (A), brouillon 5 |")

# --- § 4.3, § 4.4
A.r("6. **Deuxième rempart éprouvé** sur les sept cas de [M30]", "6. **Deuxième rempart éprouvé** sur les huit cas de [M30]")
A.r("la vérification avant l'échéance et, à l'échéance plus 10 minutes, le deuxième rempart (A3).", "la vérification avant l'échéance et, à l'échéance plus 80 minutes, le deuxième rempart (A3).")
A.r("7. **Destruction** après le rapatriement vérifié (A2).", "7. **Destruction** après le rapatriement vérifié (A2), jamais sans lui.")

# --- § 5
A.r("échéance calculée plus 8 400 secondes au-delà de la ligne de session", "échéance calculée plus 12 600 secondes au-delà de la ligne de session")
A.ligne("- **Toute machine de la voie, après son échéance**", (
    "- **Toute machine de la voie, après son échéance** : jusqu'à l'échéance plus 80 minutes, aucun geste par le deuxième rempart : la minuterie de l'amorce consigne, puis détruit. "
    "À l'échéance plus 80 minutes, deuxième rempart (A3) : la machine qui tourne encore est arrêtée par son identifiant, puis rapatriée. Rapatriement vérifié : destruction par l'identifiant. "
    "Rapatriement non vérifié deux heures après l'arrêt : machine gardée à l'arrêt, disque gardé, nœud à Lazar ; aucune destruction. État ou instant illisible : message à la mère aussitôt. "
    "Une machine à l'arrêt depuis 24 heures sans destruction : nœud."))
A.r("aucune sortie supprimée avant son versement scellé.**", "aucune sortie supprimée avant son versement scellé ; aucune machine détruite par une session sans rapatriement vérifié.**")

# --- § 6
A.r("Champ rempli au brouillon 3 : la vérification du correctif 0021.", "Champ rempli au brouillon 3 : la vérification du correctif 0021. Le brouillon 5 ne remplit ni n'ajoute aucun champ.")
A.r("`devis-voie-A-v1-brouillon4.md.sha256`", "`devis-voie-A-v1-brouillon5.md.sha256`")

# --- § 7
A.r("Le deuxième rempart détruit aussi, après un rapatriement de deux heures au plus.",
    "Par une session, rien n'est détruit sans rapatriement vérifié : le deuxième rempart ne détruit qu'après lui.")
A.ligne("8. **Réserve nommée, pour Lazar", (
    "8. **Réserve nommée, pour Lazar : ce que les remparts de dépense tiennent** (A3, [M29]). La minuterie de l'amorce seule : 56,61 USD. L'exécutante seule, à l'échéance plus 80 minutes, "
    "rapatriement vérifié : 57,23 USD. Fin normale, puis 48 heures d'arrêt : 58,84 USD. Le pire annoncé de 59,76 USD couvre ces trois cas. Il ne couvre pas le cas où la minuterie et l'exécutante "
    "font défaut ensemble : la surveillance du lanceur, seule, laisse aller jusqu'à 64,76 USD, au-delà du plafond ; et si la session de l'exécutante est morte, rien dans cet ordre ne borne la dépense. "
    "Le doublement de la minuterie par la mère couvre ce cas ; il n'est pas compté."))
A.ligne("9. **Forme du deuxième rempart", (
    "9. **Deuxième rempart : forme tranchée par la mère ; réserve nommée de plus, pour Lazar** (A3, [M29]). Décisions du 22 novembre à 18:21Z, sur la vérification du brouillon 4 : "
    "seuil à l'échéance plus 80 minutes ; aucune destruction sans rapatriement vérifié ; deux heures après l'arrêt sans rapatriement vérifié, machine gardée à l'arrêt, disque gardé, nœud à Lazar. "
    "Le code 6 du brouillon 4 est retiré. **Prises ensemble, les deux décisions coûtent plus que le chiffre donné avec la seconde.** Les 59,30 USD de la vérification et du mandat sont calculés "
    "au seuil de 10 minutes. Au seuil de 80 minutes, la machine tourne 90 minutes après son échéance : 57,07 USD à l'instant de l'arrêt, puis 0,08 USD par heure. Soit 58,99 USD à 24 heures, "
    "et **60,91 USD à 48 heures, au-delà du plafond de 60 USD**. Le total reste sous 59,76 USD jusqu'à 33,6 heures d'arrêt, sous 60 USD jusqu'à 36,6 heures. "
    "Aucun code ne tient cette durée : elle dépend de la réponse au nœud. Le rédacteur n'a changé aucune des deux décisions ; il rend le chiffre. "
    "Deux faits pour le nœud, lus à l'ordre scellé et au code de la voie : aucune commande ne lit le disque d'une machine à l'arrêt ; un redémarrage après l'échéance pousse ce qui attend, "
    "puis détruit la machine (amorce). Cet ordre ne permet pas ce redémarrage."))
A.r("au plus tard le 24 novembre à 15:40Z pour que son deuxième rempart tienne dans la ligne ;",
    "au plus tard le 24 novembre à 14:30Z pour que son deuxième rempart tienne dans la ligne (70 minutes plus tôt qu'au brouillon 4 : le seuil passe de 10 à 80 minutes) ;")
ONZE = A._ligne("11. **Scellement d'un même geste**")
A.ligne("11. **Scellement d'un même geste**", ONZE + "\n" + (
    "12. **Troisième rempart : son geste reste à écrire par la mère** (A3). Cet ordre dit qu'elle double la minuterie dans son conteneur, dès la création, sur la même échéance absolue. "
    "Il ne dit ni ce que ce doublement fait, ni à quel instant. Deux points à fixer par elle avant la création. Un : à l'échéance, la minuterie de l'amorce consigne pendant 40 minutes au plus, "
    "puis détruit ; un geste de la mère dans les 70 minutes qui suivent l'échéance couperait cette consignation. C'est le défaut que la vérification du brouillon 4 a relevé pour le deuxième rempart "
    "(majeur M1). Deux : une destruction par ce doublement se ferait sans rapatriement vérifié, comme celle de la minuterie de l'amorce ; un arrêt par l'identifiant garderait le disque."))

for interdit in ("calcul-devis-voie-A-v4.py", "8 400", "15:40", "sept cas", "2 heures 20", "55,62", "brouillon4.md.sha256"):
    assert interdit not in A.t.replace("`calcul-devis-voie-A-v4.py`", ""), interdit
assert A.t.count("<<") == 6 and A.t.count("À REVOIR") == 0      # trois champs, deux occurrences chacun, comme au brouillon 4
A.ecrit("additif-ordre-course-voie-A-v1-brouillon5.md")

# ================================================================== DEVIS
V = Texte("devis-voie-A-v1-brouillon4.md")
V.r("puis course — v1, brouillon 4", "puis course — v1, brouillon 5")
V.ligne("- **Statut** : brouillon 4,", (
    f"- **Statut** : brouillon 5, pièce décisive (devis). Écrit le 2026-11-22 vers {H}Z (`date -u`) par Claude Fable 5.2, rédacteur, du côté du saboteur, "
    f"sous le mandat `mandat-fable-brouillon5-voie-A-v1.md` (`{MANDAT5}`) ; les interdits des mandats précédents restent en vigueur. "
    f"Il est écrit au-dessus du brouillon 4 du même rédacteur (`{H_DEV4}`), lui-même écrit sous le mandat `mandat-fable-brouillon4-voie-A-v1.md` (`{MANDAT4}`) "
    "et ses errata 1 (`4642543b…`) et 2 (`a2593319…`). Le brouillon 3 (`109ca7c3500ed56805f6a5c069ba545208d3fe367cfe02f9553528642fd34604`) a été rédigé par Claude Opus 5.5 en l'absence de Fable ; "
    "Fable l'a relu en entier au brouillon 4 et en a pris la responsabilité de rédacteur. "
    "Les brouillons 1 (`12dd845cb700c83388a0705c41d029069edbb769ddc9e6b7b8f4bcedbf86aca6`), 2 (`9b48987ba823426ed4c7a4c564bdeeec2290ad9a24cb54a4d06da2d0c9ff119e`), 3 et 4 restent intacts (R12). "
    "Aucune dépense n'est engagée par ce document. Relecture de cette version par le même contre-lecteur avant tout scellement."))
V.ligne("- **Cause de la version** :", (
    f"- **Cause de la version** : la vérification du brouillon 4 (`note-verification-brouillon4-voie-A-cl2.md`, `{NOTE4}`, « scellable après corrections ») "
    "et les décisions de la mère sur elle, prises le 22 novembre à 18:21Z : seuil du deuxième rempart à l'échéance plus 80 minutes ; aucune destruction sans rapatriement vérifié ; "
    "un huitième cas de garde ; troisième rempart tenu par la mère. Les causes du brouillon 4 restent portées : la vérification du brouillon 3 "
    f"(`note-verification-brouillon3-voie-A-cl2.md`, `{NOTE3}`) ; le code final de la voie (correctifs 0024 et 0025). "
    "Différences, une par ligne : `differences-voie-A-brouillon4-vers-5-v1.md`."))
V.r(f"puis à la tête `{TETE4}`, `{REG4}` : lignes inchangées)",
    f"puis à la tête `{TETE4}`, `{REG4}`, puis à la tête `{TETE5}`, `{REG5}` : lignes inchangées)")
V.r("`additif-ordre-course-voie-A-v1-brouillon4.md`, à côté", "`additif-ordre-course-voie-A-v1-brouillon5.md`, à côté")
V.ligne("- **Arithmétique** :", (
    f"- **Arithmétique** : `calcul-devis-voie-A-v5.py` (`{H_PY}`), sortie `sortie-calcul-devis-voie-A-v5.txt` (`{H_OUT}`), à côté. "
    "Depuis la v4 : [M29], [M30] et [M32] refaits, sous-commande `second-rempart` changée ; aucune autre ligne ne change. Chaque chiffre renvoie à une ligne [Mnn] de cette sortie."))

V.r("**59,76 USD**, tenu tant qu'un des deux premiers remparts joue [M14] [M29] ; réserve au § 7, point 8",
    "**59,76 USD**, tenu si la minuterie de l'amorce joue, ou si l'exécutante joue et vérifie son rapatriement [M14] [M29] ; deux réserves au § 7, points 8 et 9")

V.r("`python3 -I calcul-devis-voie-A-v4.py rythme-etalonnage 55 0`", "`python3 -I calcul-devis-voie-A-v5.py rythme-etalonnage 55 0`")
V.r("`python3 -I calcul-devis-voie-A-v4.py garde-de-rythme 55 COMPTE", "`python3 -I calcul-devis-voie-A-v5.py garde-de-rythme 55 COMPTE")

V.ligne("| **deuxième rempart**, la minuterie en défaut", "\n".join((
    "| **deuxième rempart**, la minuterie en défaut : l'exécutante, à l'échéance plus 80 minutes (décision de la mère) ; rapatriement vérifié | elle arrête la machine par son identifiant, "
    "rapatrie et vérifie en deux heures au plus, puis la détruit par son identifiant | 55 + 2,07 + 0,16 = **57,23 USD** |",
    "| le même, **rapatriement non vérifié deux heures après l'arrêt** | machine gardée à l'arrêt, disque gardé, aucune destruction ; nœud à Lazar | 57,07 USD à l'instant de l'arrêt, "
    "puis 0,08 USD par heure : 58,99 USD à 24 heures ; **60,91 USD à 48 heures : au-delà du plafond** ; sous 60 USD jusqu'à 36,6 heures d'arrêt |")))
V.ligne("| **troisième rempart** : la mère double", (
    "| **troisième rempart**, tenu par la mère : dès la création, elle double la minuterie dans son propre conteneur, sur la même échéance absolue | "
    "son geste et son instant restent à écrire par elle (additif, § 7, point 12) | non compté |"))
V.ligne("Le pire annoncé de 59,76 USD couvre les trois premières lignes.", (
    "Le pire annoncé de 59,76 USD couvre la première, la deuxième et la quatrième ligne. La troisième et la cinquième sont des réserves nommées (§ 7, points 9 et 8). "
    "La règle du deuxième rempart est jouée par programme (`python3 -I calcul-devis-voie-A-v5.py second-rempart …`), éprouvée avant toute création sur huit cas, sains et artefacts [M30]. "
    "Elle n'ordonne jamais une destruction."))

V.ligne("| machine qui tourne encore à l'échéance plus 10 minutes", (
    "| machine qui tourne encore à l'échéance plus 80 minutes (la minuterie a fait défaut) | toute machine de la voie | deuxième rempart : arrêt par l'identifiant, rapatriement ; "
    "destruction par l'identifiant après rapatriement vérifié seulement ; sans lui, deux heures après l'arrêt : machine gardée à l'arrêt, nœud à Lazar |"))
V.r("échéance plus 8 400 secondes au-delà de la ligne de session", "échéance plus 12 600 secondes au-delà de la ligne de session")

V.ligne("9. Le deuxième rempart détruit après deux heures", (
    "9. **Réserve nommée : la machine gardée à l'arrêt** [M29]. Le deuxième rempart ne détruit qu'après un rapatriement vérifié. Sans lui, deux heures après l'arrêt, la machine reste à l'arrêt "
    "et le nœud va à Lazar : 57,07 USD à l'instant de l'arrêt, puis 0,08 USD par heure, sans borne tenue par un code. Soit 58,99 USD à 24 heures et 60,91 USD à 48 heures, au-delà du plafond ; "
    "le total reste sous 59,76 USD jusqu'à 33,6 heures d'arrêt, sous 60 USD jusqu'à 36,6 heures. Les 59,30 USD de la vérification du brouillon 4 sont calculés au seuil de 10 minutes ; "
    "au seuil de 80 minutes, ils ne valent plus. Les 10 minutes de geste et les 48 heures d'arrêt comptées au pire sont des hypothèses ; aucun code ne les tient."))
V.r("au plus tard le 24 novembre à 15:40Z pour que le deuxième rempart tienne dans cette ligne [M32]",
    "au plus tard le 24 novembre à 14:30Z pour que le deuxième rempart tienne dans cette ligne [M32]")

V.ligne("| forme du deuxième rempart |", "\n".join((
    "| forme du deuxième rempart | **tranchée par la mère le 22 novembre à 18:21Z** : arrêt à l'échéance plus 80 minutes ; destruction après rapatriement vérifié seulement ; "
    "sans lui, deux heures après l'arrêt, machine gardée à l'arrêt et nœud à Lazar | — |",
    "| machine gardée à l'arrêt sans rapatriement vérifié (§ 7, point 9) | **accepter la réserve, et répondre au nœud dans les 33 heures qui suivent l'arrêt** : le total reste alors sous le pire annoncé. "
    "Détruire sans versement est exclu (règle de Lazar). Revenir à un seuil plus court rouvrirait le défaut relevé par la vérification du brouillon 4 | moyenne |")))

for interdit in ("calcul-devis-voie-A-v4.py", "8 400", "15:40", "sept cas", "55,62", "plus 10 minutes", "brouillon4.md"):
    assert interdit not in V.t, interdit
assert V.t.count("<<") == 0
V.ecrit("devis-voie-A-v1-brouillon5.md")
print("écrits ; calcul", H_PY[:8], "sortie", H_OUT[:8])
