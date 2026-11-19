"""Produit la version 3 (erratum) du préenregistrement du palier 0b par remplacements exacts sur la version 2.

Usage : python3 -I -B appliquer_corrections_palier_0b_v3.py CHEMIN_V2 CHEMIN_V3 HEURE_FIN
Chaque chaîne cherchée doit être trouvée une seule fois ; sinon le programme s'arrête sans rien écrire.
Aucun tirage, aucun réseau.
"""
import hashlib
import sys
from pathlib import Path

EMPREINTE_V2 = "0a80a1adac833a3858754855f09bc420e569f2aeeb8c62e7cb0630bd4677becf"
GO = "`GO-2026-11-19-81`"
VERIF = (
    "`palier-0b/verification-preenregistrement-palier-0b-v2-v1.md` "
    "(`9d18eab3f578258d04f1295e54a9ddc35261e7e66114ba56d0248f9f0b4eafef`)"
)

PHRASE_NON_REGLABLES = (
    "Les proposeurs sans réglage (les deux sourds, le copieur, le suiveur à la lettre à sa valeur de φ) "
    "sont joués de même à l'étalonnage, avec leur jumelle, à chaque dose et à chaque taux d'échec de leurs "
    "familles, pour leur seul écart-type entre jumelles, gelé dans le même fichier."
)
PHRASE_USAGES = (
    " Cet écart-type sert au rapport d'écarts-types de la famille A (M9), à M8 en taille réduite et à M14."
)

REMPLACEMENTS = [
    # --- en-tête -----------------------------------------------------------------------------
    (
        "en-tête, titre",
        "aucun appel de modèle — v2\n",
        "aucun appel de modèle — v3\n",
    ),
    (
        "en-tête, version",
        "**Version 2** : elle remplace la version 1 (",
        "**Version 3 (erratum)** : elle remplace la version 2 "
        "(`palier-0b/preenregistrement-heritage-palier-0b-etage-processeur-v2.md`, `" + EMPREINTE_V2 + "`), "
        "qui reste intacte (règle R12), et n'en change que les quatre corrections de la vérification "
        "(annexe E, dernière section) : ni le dessin, ni un critère, ni un seuil. "
        "La version 2 remplaçait la version 1 (",
    ),
    (
        "en-tête, dates",
        "version 2 de 16:39Z à 16:51Z environ (`date -u`)",
        "version 2 de 16:39Z à 16:51Z environ, version 3 de 22:00Z à @HEURE_FIN@ environ (`date -u`)",
    ),
    (
        "en-tête, mandat de la version 3",
        "- Mandat de la version 2 : ",
        "- Mandat de la version 3 : `docs/notes/organisme-auto-conception-v1/epreuves-v9/heritage/"
        "mandat-redacteur-preenregistrement-palier-0b-v3-v1.md` "
        "(`084207ec830f3b438f54633882611fada4ea7301411ae8dc5be60eb58a281de8`, branche `lot/compte-organisme-v1`, "
        "commit `817e0a1ebc37502414e18e7ef322250afca7f7e9`). Ligne d'accord relue sur `main` au commit "
        "`d4449d3273f3820b71e78e9e9adc44674f6ea31b` (`registres/go.md`, "
        "`78efe8782883f4de91fa6d06d84d1b93498f8bb3ee5a70e111ffc2d9cd8c1275`) : " + GO + ", mot de Lazar du "
        "19 novembre à 21:47:18Z — pour le palier 0b, version 2 : A, option (a), le seuil de « beaucoup plus de "
        "sources » tel qu'écrit ; B, option (a), l'engagement seul pour l'expérimentateur aux paliers payants ; "
        "aucune dépense.\n"
        "- Mandat de la version 2 : ",
    ),
    (
        "en-tête, vérification citée",
        "dit ici « la contre-lecture ».",
        "dit ici « la contre-lecture » ;\n"
        "  - vérification des corrections de la version 2, par le même contre-lecteur : " + VERIF + ", § 6 ; "
        "dit ici « la vérification ».",
    ),
    # --- correction 1 ------------------------------------------------------------------------
    (
        "correction 1, B4 (iv)",
        "(iv) la question « l'engagement seul aux paliers payants ? » est posée à Lazar pour le "
        "préenregistrement du palier 1 (rapport du rédacteur de la version 2, décision B).",
        "(iv) aux paliers payants, dès le palier 1, l'expérimentateur reçoit l'engagement seul, `enonce` "
        "redevenant un texte neutre (décision de Lazar, option (a), ligne " + GO + ") ; la garde 11, déjà "
        "éprouvée sur cette liste, s'y applique sans code neuf.",
    ),
    (
        "correction 1, réserve 16",
        "la réduire est posé à Lazar, non fait.",
        "Lazar a retenu l'engagement seul pour les paliers payants, dès le palier 1 (ligne " + GO + ") ; à cet "
        "étage, où l'expérimentateur est simulé, la description reste servie et la garde 11 est éprouvée sur "
        "les deux listes.",
    ),
    (
        "correction 1, valeurs gelées",
        "précisée au banc, B4, par ce que le palier 0a a lu du code |",
        "précisée au banc, B4, par ce que le palier 0a a lu du code ; aux paliers payants : l'engagement seul "
        "(ligne " + GO + ") |",
    ),
    # --- correction 2 ------------------------------------------------------------------------
    (
        "correction 2, réserve 14",
        "**Le seuil de « beaucoup plus de sources » (S9) est un choix du rédacteur**, écrit avant tout tirage",
        "**Le seuil de « beaucoup plus de sources » (S9) est une proposition du rédacteur, accordée par Lazar "
        "(option (a), ligne " + GO + ")**, écrite avant tout tirage",
    ),
    (
        "correction 2, valeurs gelées",
        "| **ajouté à la version 2**, sans critère (S9) |",
        "| **ajouté à la version 2**, sans critère (S9) ; accordé par Lazar, option (a) (ligne " + GO + ") |",
    ),
    # --- correction 3 ------------------------------------------------------------------------
    (
        "correction 3, B7, ligne du lecteur",
        "il forme les paires de ces lois et en examine",
        "il forme les paires des lois **distinctes** de ces entrées (une loi étant identifiée par son texte "
        "dans l'engagement scellé) et en examine",
    ),
    (
        "correction 3, repli",
        "le lecteur forme alors ses paires sur **toutes** les entrées venues de la source",
        "le lecteur forme alors ses paires sur les lois distinctes de **toutes** les entrées venues de la source",
    ),
    # --- correction 4 ------------------------------------------------------------------------
    (
        "correction 4, B7, réglage",
        "celle du contraste de la tenue pour τ. Une cible est **atteignable**",
        "celle du contraste de la tenue pour τ. " + PHRASE_NON_REGLABLES + PHRASE_USAGES
        + " Une cible est **atteignable**",
    ),
    (
        "correction 4, forme, C1",
        "et sur 24 cases au moins",
        "et sur 72 cases",
    ),
    # --- section « Contre-lecture » ------------------------------------------------------------
    (
        "contre-lecture, état",
        "**La vérification des corrections par le même contre-lecteur n'est pas faite à l'heure où cette "
        "version 2 est rendue ; ce texte ne peut pas être scellé avant elle**",
        "**Vérification des corrections faite, sur la version 2** (même contre-lecteur, modèle O) : rapport "
        + VERIF + " ; verdict : « scellable après corrections », quatre corrections de la taille d'un erratum, "
        "portées par cette version 3 (annexe E, dernière section). **La relecture du seul erratum par le même "
        "contre-lecteur n'est pas faite à l'heure où cette version 3 est rendue ; ce texte ne peut pas être "
        "scellé avant elle**",
    ),
    (
        "contre-lecture, fichiers à donner",
        "le calcul de la version 2 et sa sortie, le rapport du rédacteur de la version 2.",
        "le calcul de la version 2 et sa sortie, le rapport du rédacteur de la version 2. Pour la relecture de "
        "l'erratum : cette version et la version 2, leur différentiel, la vérification, le mandat de la "
        "version 3, la ligne " + GO + ", le rapport du rédacteur de la version 3.",
    ),
]

QUEUE = """
### Erratum de la version 3 — sort des quatre corrections de la vérification

Mandat : `mandat-redacteur-preenregistrement-palier-0b-v3-v1.md` (empreinte en tête). Vérification : @VERIF@, § 6. La version 2 (`@V2@`) n'est pas modifiée. **Tout ce qui n'est pas nommé dans cette section est repris à l'octet de la version 2** : cette version est produite par 16 remplacements exacts sur la version 2, chacun trouvé une seule fois, et par l'ajout de cette section ; le programme (`appliquer_corrections_palier_0b_v3.py`) et le différentiel ligne à ligne sont dans le dossier de travail du rédacteur, à verser avec ce texte. **Aucune des quatre corrections ne touche un calcul** : le calcul de la version 2 et sa sortie ne sont ni changés ni rejoués, et aucun calcul neuf n'est écrit ; le « 72 cases » de la raison de C1 est déjà celui de la sortie de la version 2 (champ `regle_corrigee_de_C1_et_de_C4`).

| n° | correction | sort | où |
|---|---|---|---|
| 1 | engagement seul pour l'expérimentateur aux paliers payants : décision de Lazar à inscrire | appliquée dans les mots de la vérification ; « ligne `GO-…` à inscrire » devient « ligne @GO@ », la ligne étant inscrite sur `main` | B4, « Ce que la forme imposée change pour l'expérimentateur », point (iv) ; réserve 16 ; valeurs gelées, ligne « ce que l'expérimentateur reçoit du champ `tentative` » |
| 2 | seuil de « beaucoup plus de sources » : décision de Lazar à inscrire | appliquée dans les mots de la vérification : proposition du rédacteur, accordée par Lazar, option (a), ligne @GO@ ; les deux chiffres du seuil (S9) sont inchangés | réserve 14 ; valeurs gelées, ligne « beaucoup plus de sources » |
| 3 | paires formées sur les lois distinctes des entrées, une loi étant identifiée par son texte dans l'engagement scellé | appliquée dans les mots de la vérification | B7, ligne du lecteur réglé pour l'héritage ; B7, « Le repli du point 7 » |
| 4 | écart-type entre jumelles des proposeurs sans réglage (les deux sourds, le copieur, le suiveur à la lettre), joué à l'étalonnage et gelé dans le même fichier | appliquée : la phrase de la vérification est reprise à l'octet. **Deux choix du rédacteur, de forme** : elle est placée après la phrase qui commence par « Pour chaque proposeur réglable, chaque dose et chaque taille réduite visée, », et non au milieu d'elle ; elle est suivie d'une phrase qui nomme les trois usages que donne la vérification (rapport d'écarts-types de la famille A, M8 en taille réduite, M14). M9 n'est pas changée : elle dit déjà que l'écart-type entre jumelles est celui de l'étalonnage, gelé dans le fichier des réglages | B7, « Réglage par programme, sur des graines d'étalonnage » |
| forme | dans la raison de C1, « sur 24 cases au moins » devient « sur 72 cases » | appliquée | table des critères, C1 |

**Autres changements de la version 3, tous de tenue du texte** : en-tête (titre, version, heures, mandat de la version 3 et ligne @GO@ relue sur `main`, vérification citée) ; section « Contre-lecture » (vérification inscrite, relecture de l'erratum à faire, fichiers à donner).

**Ce qui n'est pas changé par la version 3** : tout le reste — l'hypothèse, les pronostics, les métriques, les grilles, les six critères et leurs seuils, S7, S8 et S9 dans leurs chiffres, le banc hors des deux passages de B7 nommés ci-dessus, les gardes, les critères de lecture, la liste d'arrêt, les annexes A à D, les réserves 1 à 13 et 15, la racine des graines.
"""


def main() -> int:
    if len(sys.argv) != 4:
        print("usage : CHEMIN_V2 CHEMIN_V3 HEURE_FIN", file=sys.stderr)
        return 2
    source, cible, heure = Path(sys.argv[1]), Path(sys.argv[2]), sys.argv[3]
    octets = source.read_bytes()
    if hashlib.sha256(octets).hexdigest() != EMPREINTE_V2:
        print("arrêt : la version 2 n'a pas l'empreinte attendue", file=sys.stderr)
        return 1
    texte = octets.decode("utf-8")
    # Tous les comptes sont pris sur la version 2 d'origine, avant tout remplacement.
    for nom, ancien, _ in REMPLACEMENTS:
        compte = texte.count(ancien)
        if compte != 1:
            print(f"arrêt : « {nom} » trouvé {compte} fois", file=sys.stderr)
            return 1
    for _, ancien, nouveau in REMPLACEMENTS:
        if texte.count(ancien) != 1:
            print("arrêt : un remplacement en a touché un autre", file=sys.stderr)
            return 1
        texte = texte.replace(ancien, nouveau.replace("@HEURE_FIN@", heure))
    if not texte.endswith("\n"):
        print("arrêt : fin de fichier inattendue", file=sys.stderr)
        return 1
    queue = QUEUE.replace("@VERIF@", VERIF).replace("@V2@", EMPREINTE_V2).replace("@GO@", GO)
    texte += queue
    if "@" in queue or "@HEURE_FIN@" in texte:
        print("arrêt : un gabarit n'a pas été rempli", file=sys.stderr)
        return 1
    if cible.exists():
        print("arrêt : la cible existe déjà (on n'écrase pas)", file=sys.stderr)
        return 1
    cible.write_bytes(texte.encode("utf-8"))
    print(len(REMPLACEMENTS), "remplacements ;", hashlib.sha256(texte.encode("utf-8")).hexdigest())
    return 0


if __name__ == "__main__":
    sys.exit(main())
