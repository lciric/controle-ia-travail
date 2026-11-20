"""Constat de lancement de la lecture de la discrétion, bras A des organismes discrets — version 5 du programme
(préenregistrement `prereg/T0.7-organismes-discrets-v-a-v2-brouillon35.md`, conventions, « Ce constat est fait par un
programme, non à la main », « Reconnaître par le sens, non par le type », « Trace d'un constat malsain », « Moment du
constat », « Rejeu d'une lecture interrompue avant tout résultat écrit » ; 8.4, lignes « constat de lancement » et
« garde du registre au constat : une autre configuration inscrite » ; 13.2).

`constat_de_lancement_discretion_bras_a_v4.py` n'est pas modifié (R12). Le brouillon 35 nomme la version 4 ; **cette
version 5** change la garde du registre, comme le demandent la vérification du code de la version 11 (M-2, M-3) et
celle du brouillon 35 (C-1), que le brouillon 36 portera au texte : **une configuration de rang 1 est refusée dès
que le registre courant porte la ligne d'inscription d'une autre configuration de l'analyse du bras A, qu'aucune
ligne de type « révocation » citant son empreinte entière ne retire** (`refuser_une_seconde_premiere_livraison`).
- **Une configuration abandonnée se retire** (M-3) : à la version 4, une configuration inscrite puis abandonnée avant
  sa lecture bloquait toute configuration suivante, sans remède. Une ligne de type « révocation » qui cite son
  empreinte entière la retire — un mot de Lazar — ; **le constat de la configuration retirée sort alors malsain**
  (la ligne qui la retire cite son empreinte sans être sa ligne d'inscription).
- **La dispense « suivie d'une reprise » est retirée** (M-2 ; vérification du brouillon 35, C-1) : à la version 4,
  n'importe quelle ligne de GO de reprise entrée après l'inscription levait la garde, sans citer aucune empreinte ;
  le brouillon 35 exigeait qu'elle cite un fichier d'arrêt ou un constat, mais la dispense, sans usage légitime —
  toute reprise ouvre un rang supérieur à 1 —, ouvrait une fenêtre entre l'inscription de la ligne de reprise et
  celle de la configuration de rang 2. Aucune ligne de reprise ne lève plus la garde.
**Ce qui avait changé à la version 4** (vérification du brouillon 34, M-1) : la garde elle-même. La limite « une autre
course, avec un autre dossier des arrêts » se ferme au lancement : le programme d'analyse ne voit que le dossier des
arrêts que sa configuration nomme, mais toute configuration est inscrite au registre. Les lignes d'accord se lisent
par leur cellule d'objet exacte (`graines_bras_a_v12.dit_l_accord`), et les configurations par
`configuration_bras_a_v12`, qui refuse un rang supérieur à 1 sans registre figé. **Ce qui avait changé à la version 3**
(vérification du code de la version 9, M-1 et M-2 ; brouillon 32, conventions) : **un contrôle, sain ou malsain, est
scellé sous un nom versionné**, `controle-de-lancement-bras-a-<date>.json`, dans le dossier de la livraison — le
programme d'analyse exige que le plus récent soit sain, et en exige un pour le rejeu d'une lecture interrompue après
son acte de reprise ; **seize signes du début de l'empreinte de la configuration suffisent à la citer, et
l'identifiant d'une ligne de GO se reconnaît à ses lettres et à ses chiffres**, quels que soient la casse et les
séparateurs (`graines_bras_a_v12`).

**Pourquoi un programme.** Le programme d'analyse est sans réseau : il ne peut pas vérifier le registre courant de la
branche principale. La session qui lance, qui a le réseau, le fait donc pour lui, **dans la même exécution que la
lecture, le constat d'abord**, et lui remet le résultat comme une pièce.

**Entrées**, données par la session qui lance :
- la configuration scellée de la livraison (`livraison-<rang>/configuration-de-l-analyse-de-la-discretion-bras-a.json`) ;
- la pièce de l'état figé du registre des accords — le registre de la branche principale tel qu'il était quand cette
  configuration a été scellée —, ou rien quand la configuration inscrit `null` (première livraison) ;
- **la ligne de GO que la lecture emploie** (son identifiant), ou rien pour une première livraison ;
- le registre courant de la branche principale, et le commit auquel il a été pris ;
- la date du constat, en temps universel.

**Ce qu'il constate**, sur le registre courant — **par le sens, non par le type** (brouillon 30) :
- `configuration_inscrite` : vrai quand **la ligne d'inscription** de la configuration — type « inscription », la
  marque `CONFIG-ANALYSE-DISCRETION-BRAS-A`, puis l'empreinte entière —, **et elle seule**, cite l'empreinte de la
  configuration dans le registre courant. Le type et la marque sont deux constantes de `graines_bras_a_v12`, que la
  session principale peut changer ;
- `revocation_entree` : vrai dès qu'**une ligne entrée depuis l'état figé nomme l'identifiant de la ligne de GO
  employée, quel que soit son type, ou cite l'empreinte de la configuration sans être sa ligne d'inscription**
  (`graines_bras_a_v12.ligne_neuve_a_voir`). Une révocation mal orthographiée, une décision qui dit l'accord révoqué,
  une ligne qui retire la configuration, une simple mention : toutes sont des « lignes neuves à voir ». Le programme
  ne juge pas ce que la ligne veut dire. L'identifiant se compare en entier.
Il vérifie que la pièce de l'état figé a bien l'empreinte que la configuration inscrit, que le registre courant
contient chacune des lignes de l'état figé (un registre ne perd pas de ligne), que la ligne de GO donnée se lit
comme un accord dans l'état figé et cite le module et le rapport de la configuration, et **que sa propre empreinte
est celle que la configuration inscrit** (`pieces_attendues.sha256_du_programme_du_constat`).

**Sortie.** Le constat a **huit champs et eux seuls** : `date_utc`, `sha256_de_la_configuration`,
`sha256_du_registre_fige`, `commit_du_registre_courant`, `configuration_inscrite`, `revocation_entree`,
`sha256_du_programme_du_constat`, `ligne_de_go`. Le programme y écrit sa propre empreinte. **Dans tous les cas, il
écrit le constat sur sa sortie standard, en une ligne JSON.**
- **Constat sain** (configuration inscrite, aucune ligne neuve à voir) : il est aussi écrit **sans reste** et scellé,
  `constat-de-lancement-bras-a.json`, dans le dossier de la livraison ; la session le cite au manifeste ; code de
  sortie 0.
- **Constat malsain** : **aucun fichier** sous le nom du constat ; la ligne de la sortie standard est sa trace, que
  la session verse au manifeste du lancement, qui est scellé ; la cause est dite sur la sortie d'erreur ; code de
  sortie 1. La lecture ne part pas : le programme d'analyse exige le fichier.
- **Pièces fautives** : arrêt, rien sur la sortie standard, code de sortie 2.

**Mode de contrôle** (brouillon 31 ; option `--controle`). Avant le rejeu d'une lecture interrompue sans résultat,
la session qui lance rejoue ce programme **à titre de contrôle**, dans la même exécution que le rejeu, le contrôle
d'abord : il fait le même constat — la même configuration, le même état figé, la même ligne de GO, et le registre
courant, le commit et la date du moment du contrôle — ; il **ne touche pas au constat d'origine** ; il écrit sur sa
sortie standard le constat à huit champs, en une ligne JSON ; il sort en succès si le constat est sain, en échec
sinon. **Sain ou malsain, le contrôle est scellé sous un nom versionné**, `controle-de-lancement-bras-a-<date>.json`
(la date du contrôle, `AAAAMMJJTHHMMSSZ`), dans le dossier de la livraison, à côté du constat d'origine — les mêmes
huit champs, à la date du contrôle (brouillon 32 ; vérification du code de la version 9, M-1 : sans fichier, rien ne
disait au programme d'analyse que le contrôle avait eu lieu ; et si seul le contrôle sain était scellé, un contrôle
sain plus ancien couvrirait une révocation). **Il s'arrête si ce nom est pris** : un contrôle ne s'écrase pas, et ne
se refait pas à la même seconde. Le programme d'analyse exige que le plus récent des contrôles soit sain, et en exige
un pour rejouer une lecture après son acte de reprise.

**La ligne qui cause un arrêt** (brouillon 31). Un constat ou un contrôle malsain, comme un arrêt du programme, nomme
sur la sortie d'erreur **la ligne du registre qui l'a causé, par son identifiant** — jamais par son texte.

**Valeurs d'exemple fictif, refusées.** L'identifiant `GO-0000-00-00-00` et l'empreinte de soixante-quatre zéros
servent d'exemple dans les échanges avec la session principale et ne désignent rien. Le programme s'arrête, sans
constat et sans fichier : quand la configuration inscrit cette empreinte ; quand la ligne de GO donnée est cet
identifiant ; quand une ligne sur laquelle le constat s'appuie porte cet identifiant ou cite cette empreinte. **Les
lignes sur lesquelles le constat s'appuie** : dans l'état figé, la ligne de GO de la livraison refaite ; dans le
registre courant, les lignes qui citent l'empreinte de la configuration et celles, entrées depuis l'état figé, qui
nomment la ligne de GO employée (les lignes « qui révoquent », au sens du constat). Une telle ligne ailleurs au
registre n'arrête rien : le registre ne perd jamais de ligne, et l'arrêt serait sans remède.

**Ce que ce programme ne décide pas.** Après une ligne neuve à voir, le remède est toujours le même : une ligne de GO
neuve, donc un autre mot de Lazar, et une configuration neuve, scellée sur le nouvel état du registre ; pour une
première livraison, une configuration neuve et sa ligne d'inscription. Rien n'est lu de la livraison ici ; ce n'est
pas un arrêt de la lecture de la discrétion.

Usage :
    PYTHONPATH=src python scripts/constat_de_lancement_discretion_bras_a_v5.py CONFIGURATION REGISTRE_COURANT \\
        --commit COMMIT --date-utc AAAA-MM-JJTHH:MM:SSZ [--registre-fige PIECE --ligne-de-go GO-AAAA-MM-JJ-NN] [--controle]

Sans réseau, sans appel de modèle. Fichiers lus : la configuration, les deux registres remis, et ce programme, pour
son empreinte. Fichier écrit : le constat, s'il est sain ; en mode de contrôle, le contrôle, sain ou malsain.
"""
from __future__ import annotations

import argparse
import hashlib
import json
import re
import sys
from pathlib import Path

from controle_ia.gardes import GardeArret
from controle_ia.organismes_discrets import configuration_bras_a_v12 as configuration_bras_a
from controle_ia.organismes_discrets import depots_bras_a_v12 as depots_bras_a
from controle_ia.organismes_discrets import graines_bras_a_v12 as graines_bras_a

_DATE = re.compile(r"\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}Z")
_COMMIT = re.compile(r"[0-9a-f]{7,40}")
GO_FICTIF = "GO-0000-00-00-00"          # identifiant de ligne de l'exemple fictif demandé au côté habilité
EMPREINTE_FICTIVE = "0" * 64            # empreinte de l'exemple fictif
CAUSE_NON_INSCRITE = "la ligne d'inscription de la configuration, et elle seule, ne cite pas son empreinte au registre courant"
MODE_CONSTAT, MODE_CONTROLE = "constat", "contrôle"


def _identifiant(ligne: str) -> str:
    """L'identifiant d'une ligne du registre (sa première cellule), pour nommer la ligne qui cause un arrêt."""
    return (_cellules(ligne) or ["ligne hors de la table"])[0] or "ligne sans identifiant"


def empreinte_du_programme() -> str:
    """L'empreinte de ce programme, lue de son propre fichier : le huitième champ du constat."""
    return hashlib.sha256(Path(__file__).read_bytes()).hexdigest()


def _cellules(ligne: str) -> list[str]:
    return [c.strip() for c in ligne.split("|")[1:-1]] if ligne.startswith("|") else []


def refuser_les_empreintes_fictives_de_la_configuration(configuration) -> None:
    """Refuse (garde ordinaire) une configuration qui inscrit une empreinte de soixante-quatre zéros — module du côté
    habilité, rapport de contre-lecture, registre des accords ou programme du constat : c'est la valeur de l'exemple
    fictif."""
    if configuration["sha256"] == EMPREINTE_FICTIVE:
        raise GardeArret("constat de lancement : l'empreinte de la configuration est faite de soixante-quatre zéros — "
                         "valeur d'un exemple fictif, refusée")
    for nom, valeur in sorted(configuration["pieces_attendues"].items()):
        if valeur == EMPREINTE_FICTIVE:
            raise GardeArret(f"constat de lancement : `pieces_attendues.{nom}` de la configuration est une empreinte de "
                             "soixante-quatre zéros — valeur d'un exemple fictif, refusée")


def lignes_d_appui(configuration, ligne_de_go: str | None, ligne_de_go_figee: str | None,
                   entrees_depuis: list[str], lignes_courantes: list[str]) -> list[tuple[str, str]]:
    """Les lignes sur lesquelles le constat s'appuie (conventions, « Valeurs fictives ») : dans l'état figé, la ligne
    de GO de la livraison refaite ; dans le registre courant, les lignes qui citent l'empreinte de la configuration,
    et celles, entrées depuis l'état figé, qui nomment la ligne de GO employée."""
    appuis = [] if ligne_de_go_figee is None else [("état figé", ligne_de_go_figee)]
    appuis += [("registre courant", l) for l in lignes_courantes if graines_bras_a.cite_l_empreinte(l, configuration["sha256"])]
    if ligne_de_go is not None:
        appuis += [("registre courant", l) for l in entrees_depuis if graines_bras_a.nomme_l_identifiant(l, ligne_de_go)]
    return appuis


def refuser_les_lignes_fictives(appuis: list[tuple[str, str]]) -> None:
    """Refuse (garde ordinaire) une ligne d'appui dont l'identifiant est `GO-0000-00-00-00`, ou qui cite une empreinte
    de soixante-quatre zéros : ce sont les valeurs de l'exemple fictif. Les autres lignes du registre ne sont pas
    regardées."""
    for registre, ligne in appuis:
        cellules = _cellules(ligne)
        if cellules and graines_bras_a.nomme_l_identifiant(cellules[0], GO_FICTIF):
            raise GardeArret(f"constat de lancement : une ligne d'appui ({registre}) a pour identifiant {GO_FICTIF} — "
                             "ligne d'un exemple fictif, refusée")
        if EMPREINTE_FICTIVE in graines_bras_a.empreintes_citees(ligne):
            raise GardeArret(f"constat de lancement : une ligne d'appui ({registre} ; {_identifiant(ligne)}) cite une "
                             "empreinte de soixante-quatre zéros — valeur d'un exemple fictif, refusée")


def configuration_inscrite(lignes_courantes: list[str], sha256_de_la_configuration: str) -> bool:
    """Vrai quand la ligne d'inscription de la configuration, **et elle seule**, cite son empreinte dans le registre
    courant : une ligne exactement la cite, et c'est sa ligne d'inscription."""
    qui_citent = [l for l in lignes_courantes if graines_bras_a.cite_l_empreinte(l, sha256_de_la_configuration)]
    return len(qui_citent) == 1 and graines_bras_a.est_la_ligne_d_inscription(qui_citent[0], sha256_de_la_configuration)


def refuser_une_seconde_premiere_livraison(lignes_courantes: list[str], sha256_de_la_configuration: str) -> None:
    """**Garde nommée d'une seule première livraison, au registre** (vérification du brouillon 34, M-1 ;
    vérification du code de la version 11, M-2 et M-3 ; vérification du brouillon 35, C-1). Pour une configuration de
    rang 1 : le registre courant ne doit porter la ligne d'inscription d'aucune **autre** configuration de l'analyse
    du bras A — type « inscription », la marque, une empreinte entière qui n'est pas la sienne — **qui ne soit
    retirée** : une ligne de type « révocation », entrée après elle, qui cite son empreinte entière
    (`graines_bras_a.retire_l_inscription`). Sinon le programme s'arrête, sans constat ni fichier, en nommant la ligne
    par son identifiant : une seconde première livraison est arrêtée au lancement, et non seulement visible au
    registre.
    **Aucune ligne de reprise ne lève cette garde** (version 5 du programme) : la version 4 tenait une inscription
    pour levée dès qu'une ligne de GO de reprise la suivait — une ligne sans rapport y suffisait (M-2), et, même
    resserrée, cette dispense ouvrait une fenêtre entre l'inscription de la ligne de reprise et celle de la
    configuration de rang 2 qu'elle ouvre (vérification du brouillon 35, C-1). Elle n'a aucun usage : toute reprise
    ouvre un rang supérieur à 1, que cette garde ne regarde pas."""
    for place, ligne in enumerate(lignes_courantes):
        autre = graines_bras_a.empreinte_inscrite(ligne)
        if autre is None or autre == sha256_de_la_configuration:
            continue
        if not any(graines_bras_a.retire_l_inscription(suivante, autre) for suivante in lignes_courantes[place + 1:]):
            raise GardeArret(f"constat de lancement : le registre courant porte la ligne d'inscription d'une autre "
                             f"configuration de l'analyse du bras A ({_identifiant(ligne)}), qu'aucune ligne de type "
                             "« révocation » citant son empreinte entière ne retire — une course n'a qu'une première "
                             "livraison : une configuration de rang 1 ne part pas ; toute autre pièce passe par la règle "
                             "d'octroi, à un rang supérieur à 1 (6.9)")


def lignes_neuves_a_voir(entrees_depuis: list[str], ligne_de_go: str | None, sha256_de_la_configuration: str) -> list[str]:
    """Les motifs des lignes entrées depuis l'état figé qui rendent le constat malsain (`ligne_neuve_a_voir`), chacun
    avec l'identifiant de sa ligne — jamais son texte."""
    motifs = []
    for ligne in entrees_depuis:
        motif = graines_bras_a.ligne_neuve_a_voir(ligne, ligne_de_go=ligne_de_go,
                                                  sha256_de_la_configuration=sha256_de_la_configuration)
        if motif is not None:
            motifs.append(f"{_identifiant(ligne)} — {motif}")
    return motifs


def cause_de_la_non_inscription(lignes_courantes: list[str], sha256_de_la_configuration: str) -> str:
    """La cause d'une configuration dite non inscrite, avec l'identifiant des lignes qui citent son empreinte, s'il y
    en a : aucune ligne ; une ligne qui n'est pas sa ligne d'inscription ; plusieurs lignes."""
    qui_citent = [_identifiant(l) for l in lignes_courantes if graines_bras_a.cite_l_empreinte(l, sha256_de_la_configuration)]
    return CAUSE_NON_INSCRITE + (" (aucune ligne ne la cite)" if not qui_citent else f" (lignes qui la citent : {', '.join(qui_citent)})")


def constater(configuration_scellee, registre_courant, *, commit_du_registre_courant, date_utc, registre_fige,
              ligne_de_go, mode) -> tuple[dict, Path | None, list[str]]:
    """Fait le constat de lancement. Rend (le constat à huit champs, le chemin du fichier scellé, les causes) ; le
    chemin vaut `None` quand le constat est malsain : rien n'est alors scellé, et les causes disent pourquoi — chacune
    nomme, par son identifiant, la ligne qui la fait. Tous les arguments nommés sont exigés, sans valeur par défaut ;
    `registre_fige` et `ligne_de_go` valent `None` quand, et seulement quand, la configuration inscrit `null` pour le
    registre (première livraison).
    **`mode`** : `MODE_CONSTAT`, ou `MODE_CONTROLE` — le même constat, à la date du contrôle ; le constat d'origine
    n'est ni lu ni touché. **Sain ou malsain, le contrôle est scellé sous son nom versionné**
    (`controle-de-lancement-bras-a-<date>.json`), et son chemin est rendu ; ce sont les causes, vide ou non, qui le
    disent sain ou malsain. Si ce nom est déjà pris, le programme s'arrête (brouillon 32 ; vérification du code de la
    version 9, M-1).
    Refus (gardes ordinaires, sans constat ni fichier) : configuration qui ne se lit pas, ou qui inscrit une autre
    empreinte de programme que celle de ce programme ; pièce de l'état figé absente, de trop, ou d'une autre empreinte
    que celle que la configuration inscrit ; ligne de GO absente, de trop, qui ne se lit pas comme un accord dans
    l'état figé, ou qui ne cite pas le module et le rapport de la configuration ; registre courant absent ou
    illisible, ou qui ne contient pas une ligne de l'état figé ; commit ou date hors de leur forme ; une valeur de
    l'exemple fictif ; **pour une configuration de rang 1, une autre configuration de l'analyse du bras A inscrite au
    registre courant, qu'aucune ligne de type « révocation » citant son empreinte entière ne retire** ; un constat
    déjà scellé avec un autre contenu (R12)."""
    if mode not in (MODE_CONSTAT, MODE_CONTROLE):
        raise GardeArret(f"constat de lancement : mode {mode!r} — « {MODE_CONSTAT} » ou « {MODE_CONTROLE} » exigé")
    configuration = configuration_bras_a.lire_la_configuration_scellee(configuration_scellee)
    refuser_les_empreintes_fictives_de_la_configuration(configuration)
    programme = empreinte_du_programme()
    if configuration_bras_a.programme_du_constat(configuration) != programme:
        raise GardeArret("constat de lancement : la configuration scellée inscrit l'empreinte d'un autre programme du constat "
                         f"que celui-ci ({programme[:16]}…) — le programme d'analyse refuserait ce constat (conventions)")
    if not isinstance(commit_du_registre_courant, str) or _COMMIT.fullmatch(commit_du_registre_courant) is None:
        raise GardeArret("constat de lancement : le commit du registre courant est exigé (7 à 40 signes hexadécimaux)")
    if not isinstance(date_utc, str) or _DATE.fullmatch(date_utc) is None:
        raise GardeArret("constat de lancement : la date du constat est exigée, en temps universel (AAAA-MM-JJTHH:MM:SSZ)")
    attendu = configuration["pieces_attendues"][configuration_bras_a.REGISTRE_ATTENDU]
    if isinstance(ligne_de_go, str) and graines_bras_a.nomme_l_identifiant(ligne_de_go, GO_FICTIF):
        raise GardeArret(f"constat de lancement : la ligne de GO donnée est {GO_FICTIF} — identifiant d'un exemple fictif, "
                         "refusé")
    if attendu is None:
        if registre_fige is not None or ligne_de_go is not None:
            raise GardeArret("constat de lancement : la configuration n'inscrit aucun registre figé (`null`, première "
                             "livraison) — ni pièce de l'état figé ni ligne de GO ne sont à donner")
        figees, ligne_figee = [], None
    else:
        if ligne_de_go is None:
            raise GardeArret("constat de lancement : la configuration inscrit un registre figé (livraison refaite) — la ligne "
                             "de GO que la lecture emploie est exigée")
        figees = graines_bras_a.lire_le_registre_fige(registre_fige, attendu)      # vérifie l'empreinte de la pièce
        ligne_figee = graines_bras_a.ligne_d_accord(ligne_de_go, graines_bras_a.PHRASE_DE_L_ACCORD_D_UNE_LIVRAISON_REFAITE,
                                                    registre_fige=registre_fige, sha256_au_scellement=attendu)
        citees = graines_bras_a.empreintes_citees(ligne_figee)
        if configuration_bras_a.module_du_cote_habilite(configuration) not in citees \
                or configuration_bras_a.rapport_de_contre_lecture(configuration) not in citees:
            raise GardeArret(f"constat de lancement : {ligne_de_go} ne cite pas le module et le rapport de contre-lecture que "
                             "la configuration inscrit — ce n'est pas une ligne que cette lecture peut employer")
    try:
        present = isinstance(registre_courant, (str, Path)) and Path(registre_courant).is_file()
    except OSError:
        present = False
    if not present:
        raise GardeArret("constat de lancement : le registre courant de la branche principale est exigé (le chemin d'un "
                         "fichier, remis par la session qui lance)")
    try:
        courantes = Path(registre_courant).read_bytes().decode("utf-8").splitlines()
    except UnicodeDecodeError:
        raise GardeArret("constat de lancement : registre courant illisible") from None
    entrees_depuis = list(courantes)
    for ligne in figees:
        if ligne not in entrees_depuis:
            raise GardeArret(f"constat de lancement : le registre courant ne contient pas une ligne de l'état figé "
                             f"({_identifiant(ligne)}) — ce n'est "
                             "pas un état postérieur du même registre (une ligne du registre n'est jamais retirée ni "
                             "changée) ; il faut une configuration neuve, scellée sur le nouvel état")
        entrees_depuis.remove(ligne)
    refuser_les_lignes_fictives(lignes_d_appui(configuration, ligne_de_go, ligne_figee, entrees_depuis, courantes))
    if configuration["rang"] == 1:
        refuser_une_seconde_premiere_livraison(courantes, configuration["sha256"])
    inscrite = configuration_inscrite(courantes, configuration["sha256"])
    a_voir = lignes_neuves_a_voir(entrees_depuis, ligne_de_go, configuration["sha256"])
    constat = {"date_utc": date_utc, "sha256_de_la_configuration": configuration["sha256"],
               "sha256_du_registre_fige": attendu, "commit_du_registre_courant": commit_du_registre_courant,
               "configuration_inscrite": inscrite, "revocation_entree": bool(a_voir),
               "sha256_du_programme_du_constat": programme, "ligne_de_go": ligne_de_go}
    if tuple(constat) != tuple(configuration_bras_a.CHAMPS_DU_CONSTAT_DE_LANCEMENT):
        raise GardeArret("constat de lancement : ses huit champs, et eux seuls")
    causes = ([] if inscrite else [cause_de_la_non_inscription(courantes, configuration["sha256"])]) + a_voir
    dossier = configuration_bras_a.dossier_de_la_livraison(configuration)
    if mode == MODE_CONTROLE:
        chemin = dossier / configuration_bras_a.nom_du_controle_de_lancement(date_utc)
        if chemin.exists() or Path(str(chemin) + ".sha256").exists():
            raise GardeArret(f"contrôle de lancement : le nom {chemin.name} est déjà pris — un contrôle ne s'écrase pas, "
                             "et ne se refait pas à la même date ; rejouer le contrôle, à sa date")
        depots_bras_a.ecrire_et_sceller(chemin, json.dumps(constat, ensure_ascii=False, sort_keys=True, indent=1) + "\n")
        return constat, chemin, causes
    if causes:
        return constat, None, causes
    chemin = dossier / configuration_bras_a.NOM_DU_CONSTAT_DE_LANCEMENT
    depots_bras_a.ecrire_et_sceller(chemin, json.dumps(constat, ensure_ascii=False, sort_keys=True, indent=1) + "\n")
    return constat, chemin, []


def main(argv: list[str]) -> int:
    lecteur = argparse.ArgumentParser(description="Constat de lancement de la lecture de la discrétion, bras A.")
    lecteur.add_argument("configuration", help="configuration scellée de la livraison")
    lecteur.add_argument("registre_courant", help="registre courant de la branche principale, remis comme une pièce")
    lecteur.add_argument("--commit", required=True, help="commit auquel le registre courant a été pris")
    lecteur.add_argument("--date-utc", required=True, help="date du constat, AAAA-MM-JJTHH:MM:SSZ")
    lecteur.add_argument("--registre-fige", default=None, help="pièce de l'état figé du registre (rien pour une première livraison)")
    lecteur.add_argument("--ligne-de-go", default=None, help="ligne de GO que la lecture emploie (rien pour une première livraison)")
    lecteur.add_argument("--controle", action="store_true",
                         help="mode de contrôle, avant le rejeu d'une lecture interrompue : sain ou malsain, il est scellé "
                              "sous un nom versionné ; le constat d'origine n'est pas touché")
    a = lecteur.parse_args(argv)
    try:
        constat, chemin, causes = constater(a.configuration, a.registre_courant, commit_du_registre_courant=a.commit,
                                            date_utc=a.date_utc, registre_fige=a.registre_fige, ligne_de_go=a.ligne_de_go,
                                            mode=MODE_CONTROLE if a.controle else MODE_CONSTAT)
    except GardeArret as e:
        print(f"ARRÊT : {e}", file=sys.stderr)
        return 2
    print(json.dumps(constat, ensure_ascii=False))             # une ligne JSON, dans la forme à huit champs : sain ou malsain
    if causes:
        print((f"CONTRÔLE MALSAIN, scellé ({chemin.name}) : le rejeu ne part pas" if a.controle
               else "CONSTAT MALSAIN : la lecture ne part pas, aucun fichier n'est écrit") + " — " + " ; ".join(causes)
              + ". Verser la ligne de la sortie standard au manifeste du lancement.", file=sys.stderr)
        return 1
    print(("contrôle sain, scellé (le constat d'origine n'est pas touché ; le rejeu peut partir)" if a.controle
           else "constat sain, scellé") + f" : {chemin} ({hashlib.sha256(chemin.read_bytes()).hexdigest()})", file=sys.stderr)
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
