"""Conception v5 -> v6 : couples « ancien -> nouveau » de la contre-lecture v5, tour 1 (M-1, m-1 à m-5), en-tête et section
« Contre-lecture ». Vérifie l'empreinte de la v5 et du rapport, que chaque « ancien » figure exactement une fois dans la v5 et
dans le texte courant au moment où il s'applique, et refuse d'écraser la cible (ouverture en mode « x »).

Usage : python appliquer_corrections_v6_v1.py HEURE_UTC   (heure lue par `date -u` juste avant le passage et le scellement)
"""
import hashlib
import pathlib
import sys

ICI = pathlib.Path(__file__).resolve().parent.parent
SOURCE = ICI / "conception-monde-riche-doublons-v5.md"
SHA_SOURCE = "a12ab1e50190b8d27ce6daa0e5c44b81f04c674a916103f518d093400b7481d9"
RAPPORT = ICI / "contre-lecture-conception-v5-tour1-v1.md"
SHA_RAPPORT = "8ad9488e8f3f10a84298421ad6613a720d7fe5a2faf199810d4faf4e2cd1a28a"
CIBLE = ICI / "conception-monde-riche-doublons-v6.md"
DEBUT_V6 = "2026-11-17 01:11:23"


def sha(p):
    return hashlib.sha256(p.read_bytes()).hexdigest()


def couples(heure):
    section = f"""## Contre-lecture (v6 : réponse à la contre-lecture de la v5, tour 1)

- **Rapport** : `contre-lecture-conception-v5-tour1-v1.md`, `{SHA_RAPPORT}` (égale à son
  compagnon) ; lecteur neuf (modèle C), d'une autre lignée que le rédacteur de la v5 (modèle A) et que le lecteur de la v4
  (modèle B) : la condition de lignée posée au §7 (réserve « Lignée ») est remplie pour la v5.
- **Verdict du rapport** : « Corrections » ; neuf corrections de la v4 jugées appliquées, règle jugée opératoire, dénominateur
  jugé conforme à GO-2026-11-17-05 ; **une correction majeure (M-1) et cinq mineures (m-1 à m-5)** (le verdict d'une ligne du
  rapport dit « quatre mineures », sa liste en porte cinq : les cinq sont traitées ici) ; quatre remarques facultatives.
- **Pièce de départ** : v5, `{SHA_SOURCE}` (égale à son compagnon).
- **Méthode** : programme `outils-v6/appliquer_corrections_v6_v1.py` (empreinte dans son compagnon `.sha256`, scellé avant son
  passage) : il vérifie l'empreinte de la v5 et du rapport, que chaque « ancien » figure exactement une fois dans la v5 et dans
  le texte courant au moment où il s'applique, et refuse d'écraser la cible. Différentiel `differentiel-conception-v5-v6.diff`
  (`diff -u`, compagnon `.sha256`). Rédacteur de la v6 : modèle C, neuf, qui n'a écrit ni la v5 ni son rapport.
- **Contrôles faits avant d'appliquer** (lecture seule) : M-1 : les lignes 34, 68, 150 et 188 du devis du banc v3
  (`ec5a6e99…`, égale) disent bien que le banc importe `monde_riche_v4.py` sans le modifier et lisent « code v68 gelé » comme
  l'arbre v68 à v74 du pilote ; m-1 : dans `course` de `monde_riche_v4.py` (`4b165847…`, égale), la graine du flux de
  proposition (ligne 212) et celle du juge (ligne 231) portent le drapeau `masquage` ; celle du test de mort aussi (ligne 237),
  ce que le rapport ne cite pas et que le texte neuf de m-1 couvre (« la graine du flux »).

| point | réponse | où | ancien (v5) → nouveau (v6) |
|---|---|---|---|
| **M-1** (majeure) : « code v68 gelé » donné pour conforme au GO alors qu'il contredit le devis v3 du banc | **appliquée** | §8, première ligne de la table | « conformément à GO-2026-11-17-05 (banc complet) » → « au titre de GO-2026-11-17-05 (banc complet), **lecture à confirmer par la mère** : le devis v3 importe `monde_riche_v4.py` sans le modifier […] ; la pièce des règles du banc et le devis du banc complet fixent laquelle des deux lectures vaut, avant tout engagement de secret » (texte du rapport, recopié). La tension reste **ouverte** : elle se tranche dans la pièce des règles du banc et le devis du banc complet, non ici |
| **m-1** : « même flux » faux pour la passe sans masquage dans le code v4 | **appliquée** | §3.2, « Passes rapportées » | « (indice de flux = rang r ; `course` tire une » → la même phrase, précédée de : dans la v4 la graine du flux porte le drapeau de masquage, la passe 0,25 « sans masquage » n'a donc pas le même flux, sauf si le module neuf sépare la graine du drapeau, à coder et à essayer (R5). L'« égalité des flux entre passes » lue par l'audit de symétrie (§3.2) n'est pas réécrite : le rapport ne la vise par aucun couple |
| **m-2** : « et rien d'autre » dépasse la table des changements | **appliquée** | en-tête, « Statut » | « **et rien d'autre** » → « **et rien d'autre que des mises en cohérence sans effet sur un chiffre, ajoutées sans ligne propre dans la table : dernier point du §5, cellule « §17 (devis) » du §6, réserves du §7** » |
| **m-3** : noms de modèles encore dans la pièce | **appliquée** pour les trois couples donnés | en-tête, « Rédacteur » ; §7, réserve « Lignée » | le nom du modèle du rédacteur → « modèle A » (deux fois) ; le nom de la lignée du lecteur de la v4 → « une autre lignée (modèle B) ». La consigne de la tâche (aucun identifiant de modèle ; lettres A, B, C) est lue comme visant ces noms de rédacteurs et de lecteurs |
| m-3, suite : noms des proposeurs et des relais cités du verdict v2 et des lignes de GO (§5, deux points du devis ; §8, lignes « x = 0 sur 14 », « Deux appels tronqués », « Durées par appel ») | **non appliquée** | — | le rapport ne donne **aucun couple** et renvoie la décision à la mère ; ce sont des noms cités de pièces qui font foi (verdict v2, GO), où ils désignent les proposeurs mesurés et les lignes de dépense, non un rédacteur. Inchangés ; à trancher par la mère |
| **m-4** : portée de la sélection C6 dite trop large | **appliquée** | §4.1, « Sélection déclarée » | « il **ne sélectionne pas** sur les conditionnelles » → « il **n'a pas sélectionné** sur les conditionnelles dans ces 12 graines (8 tirages refusés, aucune « K1 + conditionnelle » en écart) ; rien ne le garantit pour les 24 mondes du banc, où les refus se rapportent par motif (§3.2) » |
| **m-5** : réserve du verdict v2 omise au §8 | **appliquée** | §8, ligne « Taux d'erreur du texte » | « il ne l'a pas réfuté. « Une issue » → « il ne l'a pas réfuté ; le verdict écrit aussi que x = 0 sur 14 est « trop propre pour l'hypothèse » (réserve d'audit, qui ne change pas l'issue). « Une issue » |
| remarques facultatives (audit presque certain ; type de E1 pour C0 ; hypothèses de la table du §3.4 ; nom de fichier du §0) | **non appliquées** | — | non exigées par le rapport ; la tâche borne la v6 aux corrections exigées |
| en-tête | mis à jour | titre, « Statut », « Rédacteur de la v6 », « Heures » | version v5 → v6 ; heures de la v6 par `date -u` |

**Rien d'autre ne change** : aucun chiffre de la v5 n'est modifié ; les suggestions S-1 à S-6 de la contre-lecture v4 restent non
appliquées. **Reste à faire** : les couples appliqués sont à revoir par un lecteur neuf (tour 2), qui ne soit ni le rédacteur de
la v6 ni celui du rapport ; la lecture de « code v68 gelé » (M-1) et les noms cités du verdict (m-3, suite) attendent la mère.
"""
    return [
        ("titre",
         "— v5 (famille MR-2, corrections de la contre-lecture v4, règle de garde opératoire)",
         "— v6 (famille MR-2, corrections des contre-lectures v4 et v5, règle de garde opératoire)"),
        ("en-tête, statut",
         "- **Statut** : conception **v5** (aucun préenregistrement, aucun GO consommé, aucune dépense). Elle est la v4",
         "- **Statut** : conception **v6** (aucun préenregistrement, aucun GO consommé, aucune dépense). Elle est la v5\n"
         f"  (`conception-monde-riche-doublons-v5.md`, `{SHA_SOURCE}`, versée inchangée,\n"
         "  R12) avec les seules corrections exigées par sa contre-lecture, tour 1 (M-1, m-1 à m-5 ; section « Contre-lecture », en\n"
         "  fin de pièce), et l'en-tête mis à jour. La v5 était la v4"),
        ("m-2",
         "**et rien d'autre**",
         "**et rien d'autre que des mises en cohérence sans effet sur un chiffre, ajoutées sans ligne propre dans la table : "
         "dernier point du §5, cellule « §17 (devis) » du §6, réserves du §7**"),
        ("m-3 (a)",
         "Claude Opus 5.5, sous-agent neuf",
         "modèle A, sous-agent neuf"),
        ("en-tête, rédacteur de la v6",
         "- **Interpréteur** : Python 3.13.18",
         "- **Rédacteur de la v6** : modèle C, sous-agent neuf d'un script d'orchestration ; je n'ai écrit ni la v4, ni la v5, ni\n"
         "  leurs contre-lectures ; j'ai appliqué les couples de la contre-lecture v5, tour 1, par un programme (section\n"
         "  « Contre-lecture »), sous l'interpréteur du venv du dépôt ; aucun calcul neuf, aucun chiffre neuf.\n"
         "- **Interpréteur** : Python 3.13.18"),
        ("en-tête, heures",
         "fin de la rédaction 2026-11-17 01:04:25.",
         f"fin de la rédaction 2026-11-17 01:04:25 (v5). **v6** : début {DEBUT_V6} ; application des couples et scellement\n"
         f"  {heure}."),
        ("m-1",
         "(indice de flux = rang r ; `course` tire une",
         "(indice de flux = rang r ; dans la v4 la graine du flux porte le drapeau de masquage : la passe 0,25 « sans masquage » "
         "n'a donc pas le même flux que les autres, sauf si le module neuf sépare la graine du drapeau, à coder et à essayer (R5) ; "
         "`course` tire une"),
        ("m-4",
         "il **ne sélectionne pas** sur les conditionnelles",
         "il **n'a pas sélectionné** sur les conditionnelles dans ces 12 graines (8 tirages refusés, aucune « K1 + conditionnelle » "
         "en écart) ; rien ne le garantit pour les 24 mondes du banc, où les refus se rapportent par motif (§3.2)"),
        ("m-3 (b)",
         "(Claude Opus 5.5) ; la contre-lecture de la v4 venait",
         "(modèle A) ; la contre-lecture de la v4 venait"),
        ("m-3 (c)",
         "d'une autre lignée de la même maison (Fable) ; celle de la v5",
         "d'une autre lignée (modèle B) ; celle de la v5"),
        ("M-1",
         "conformément à GO-2026-11-17-05 (banc complet) |",
         "au titre de GO-2026-11-17-05 (banc complet), **lecture à confirmer par la mère** : le devis du banc v3 (`ec5a6e99…`, "
         "lignes 34, 68, 150 et 188) importe `monde_riche_v4.py` sans le modifier et lit « code v68 gelé » comme l'arbre v68 à v74 "
         "du pilote, alors que E-5 exige un module à noms neufs égal à la v4 (R5-7) ; la pièce des règles du banc et le devis du "
         "banc complet fixent laquelle des deux lectures vaut, avant tout engagement de secret |"),
        ("m-5",
         "il ne l'a pas réfuté. « Une issue",
         "il ne l'a pas réfuté ; le verdict écrit aussi que x = 0 sur 14 est « trop propre pour l'hypothèse » (réserve d'audit, "
         "qui ne change pas l'issue). « Une issue"),
        ("section Contre-lecture",
         "coûts : pièce du devis de la course, non ici |\n\n",
         "coûts : pièce du devis de la course, non ici |\n\n" + section),
    ]


def main():
    if len(sys.argv) != 2:
        sys.exit("usage : appliquer_corrections_v6_v1.py HEURE_UTC")
    heure = sys.argv[1]
    if sha(SOURCE) != SHA_SOURCE:
        sys.exit("empreinte de la v5 inattendue : arrêt")
    if sha(RAPPORT) != SHA_RAPPORT:
        sys.exit("empreinte du rapport inattendue : arrêt")
    if CIBLE.exists():
        sys.exit("cible déjà présente : refus d'écraser")
    original = SOURCE.read_text(encoding="utf-8")
    texte = original
    for nom, ancien, nouveau in couples(heure):
        n0, n1 = original.count(ancien), texte.count(ancien)
        if n0 != 1 or n1 != 1:
            sys.exit(f"couple {nom} : « ancien » trouvé {n0} fois dans la v5, {n1} fois dans le texte courant : arrêt")
        texte = texte.replace(ancien, nouveau, 1)
        print(f"appliqué : {nom}")
    with open(CIBLE, "x", encoding="utf-8") as f:
        f.write(texte)
    print(f"écrit : {CIBLE.name} {hashlib.sha256(texte.encode('utf-8')).hexdigest()}")


if __name__ == "__main__":
    main()
