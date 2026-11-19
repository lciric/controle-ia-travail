"""Constat de lancement de la lecture de la discrétion, bras A des organismes discrets (préenregistrement
`prereg/T0.7-organismes-discrets-v-a-v2-brouillon28.md`, conventions, « Ce constat est fait par un programme, non à la
main » ; 8.4, ligne « constat de lancement » ; 13.2 ; vérification du brouillon 26, C-1).

**Pourquoi un programme.** Le programme d'analyse est sans réseau : il ne peut pas vérifier le registre courant de la
branche principale. La session qui lance, qui a le réseau, le fait donc pour lui, **juste avant la lecture**, et lui
remet le résultat comme une pièce. Fait à la main, ce constat pouvait être oublié, et n'avait ni cas sain ni artefact.

**Entrées**, données par la session qui lance :
- la configuration scellée de la livraison (`livraison-<rang>/configuration-de-l-analyse-de-la-discretion-bras-a.json`) ;
- la pièce de l'état figé du registre des accords — le registre de la branche principale tel qu'il était quand cette
  configuration a été scellée —, ou rien quand la configuration inscrit `null` (première livraison) ;
- le registre courant de la branche principale, et le commit auquel il a été pris ;
- la date du constat, en temps universel.

**Ce qu'il constate**, sur le registre courant :
- `configuration_inscrite` : vrai quand l'empreinte entière de la configuration s'y lit ;
- `revocation_entree` : vrai quand une ligne du registre courant, absente de l'état figé, révoque la ligne de GO que
  la lecture emploie. Pour une première livraison, sans ligne de GO à lire, il est faux.
Il vérifie que la pièce de l'état figé a bien l'empreinte que la configuration inscrit, et que le registre courant
contient chacune des lignes de l'état figé (un registre ne perd pas de ligne).

**Sortie.** Le constat a six champs et eux seuls : `date_utc`, `sha256_de_la_configuration`,
`sha256_du_registre_fige`, `commit_du_registre_courant`, `configuration_inscrite`, `revocation_entree`.
- **Constat sain** (configuration inscrite, aucune révocation entrée) : il est écrit **sans reste** et scellé,
  `constat-de-lancement-bras-a.json`, dans le dossier de la livraison ; la session le cite au manifeste ; la lecture
  peut partir.
- **Constat malsain** : il est rendu et affiché, pour le manifeste, **mais aucun fichier n'est scellé** dans le
  dossier de la livraison, et le programme sort en échec. La lecture ne part pas : le programme d'analyse exige le
  fichier. Ainsi le constat peut être refait quand la configuration est inscrite, sans rien écraser (R12).

**Ce que ce programme ne décide pas.** Après une révocation entrée, il faut une ligne de GO neuve et une
configuration neuve : c'est un mot de Lazar. Rien n'est lu de la livraison ici ; ce n'est pas un arrêt de la lecture
de la discrétion.

**Valeurs d'exemple fictif, refusées** (précision de la session principale, que le texte portera au prochain
brouillon). Un exemple fictif sera demandé au côté habilité ; ses valeurs sont l'identifiant de ligne
`GO-0000-00-00-00` et l'empreinte de soixante-quatre zéros. Elles ne doivent jamais servir à une lecture. Le programme
s'arrête donc, sans constat et sans fichier (garde ordinaire) :
- quand une empreinte de soixante-quatre zéros est inscrite dans la configuration (module du côté habilité, rapport de
  contre-lecture, registre des accords), ou citée par une ligne du registre sur laquelle ce constat s'appuie ;
- quand une ligne du registre sur laquelle ce constat s'appuie a pour identifiant `GO-0000-00-00-00`.
Les lignes sur lesquelles ce constat s'appuie : dans l'état figé, toute ligne qui porte la phrase d'accord d'une
livraison refaite (la lecture peut en employer une) ; dans le registre courant, toute ligne qui inscrit l'empreinte de
la configuration. Une ligne du registre qui ne sert à rien ici n'est pas regardée : le registre ne perd jamais de
ligne, et un refus sur une ligne étrangère serait sans remède.

**Hypothèses, écrites pour le contre-lecteur** (relevé des défauts du texte, version 8) :
- « la ligne de GO que la lecture emploie » n'est pas une entrée du texte. Ce programme la retrouve : c'est, dans
  l'état figé, toute ligne qui porte la phrase d'accord d'une livraison refaite et cite le module et le rapport de
  contre-lecture que la configuration inscrit. S'il y en a plusieurs, une révocation de l'une quelconque compte ;
- une révocation est une ligne du registre de type « révocation » qui nomme l'identifiant de cette ligne.

Usage :
    PYTHONPATH=src python scripts/constat_de_lancement_discretion_bras_a_v1.py CONFIGURATION REGISTRE_COURANT \\
        --commit COMMIT --date-utc AAAA-MM-JJTHH:MM:SSZ [--registre-fige PIECE]

Sans réseau, sans appel de modèle. Fichiers lus : la configuration, les deux registres remis. Fichier écrit : le
constat, s'il est sain.
"""
from __future__ import annotations

import argparse
import hashlib
import json
import re
import sys
from pathlib import Path

from controle_ia.gardes import GardeArret
from controle_ia.organismes_discrets import configuration_bras_a_v8 as configuration_bras_a
from controle_ia.organismes_discrets import depots_bras_a_v8 as depots_bras_a
from controle_ia.organismes_discrets import graines_bras_a_v8 as graines_bras_a

_DATE = re.compile(r"\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}Z")
_COMMIT = re.compile(r"[0-9a-f]{7,40}")
_CELLULE_DU_TYPE = 2
GO_FICTIF = "GO-0000-00-00-00"          # identifiant de ligne de l'exemple fictif demandé au côté habilité
EMPREINTE_FICTIVE = "0" * 64            # empreinte de l'exemple fictif


def _cellules(ligne: str) -> list[str]:
    return [c.strip() for c in ligne.split("|")[1:-1]] if ligne.startswith("|") else []


def lignes_de_go_employees(lignes_figees: list[str], configuration) -> list[str]:
    """Identifiants des lignes de GO que la lecture d'une livraison refaite peut employer sous cette configuration :
    dans l'état figé, les lignes qui portent la phrase d'accord d'une livraison refaite et citent le module et le
    rapport de contre-lecture que la configuration inscrit."""
    module = configuration_bras_a.module_du_cote_habilite(configuration)
    rapport = configuration_bras_a.rapport_de_contre_lecture(configuration)
    phrase = graines_bras_a.PHRASE_DE_L_ACCORD_D_UNE_LIVRAISON_REFAITE.casefold()
    employees = []
    for ligne in lignes_figees:
        cellules = _cellules(ligne)
        citees = graines_bras_a.empreintes_citees(ligne)
        if cellules and phrase in ligne.casefold() and module in citees and rapport in citees:
            employees.append(cellules[0])
    return employees


def refuser_les_empreintes_fictives_de_la_configuration(configuration) -> None:
    """Refuse (garde ordinaire) une configuration qui inscrit une empreinte de soixante-quatre zéros — module du côté
    habilité, rapport de contre-lecture ou registre des accords : c'est la valeur de l'exemple fictif."""
    if configuration["sha256"] == EMPREINTE_FICTIVE:
        raise GardeArret("constat de lancement : l'empreinte de la configuration est faite de soixante-quatre zéros — "
                         "valeur d'un exemple fictif, refusée")
    for nom, valeur in sorted(configuration["pieces_attendues"].items()):
        if valeur == EMPREINTE_FICTIVE:
            raise GardeArret(f"constat de lancement : `pieces_attendues.{nom}` de la configuration est une empreinte de "
                             "soixante-quatre zéros — valeur d'un exemple fictif, refusée")


def refuser_les_lignes_fictives(configuration, lignes_figees: list[str], lignes_courantes: list[str]) -> None:
    """Refuse (garde ordinaire) une ligne du registre sur laquelle le constat s'appuie quand son identifiant est
    `GO-0000-00-00-00`, ou quand elle cite une empreinte de soixante-quatre zéros : ce sont les valeurs de l'exemple
    fictif. Les lignes regardées : dans l'état figé, celles qui portent la phrase d'accord d'une livraison refaite ;
    dans le registre courant, celles qui inscrivent l'empreinte de la configuration."""
    phrase = graines_bras_a.PHRASE_DE_L_ACCORD_D_UNE_LIVRAISON_REFAITE.casefold()
    inscription = re.compile(r"(?<![0-9a-f])" + configuration["sha256"] + r"(?![0-9a-f])")
    appuis = [("état figé", ligne) for ligne in lignes_figees if phrase in ligne.casefold()]
    appuis += [("registre courant", ligne) for ligne in lignes_courantes if inscription.search(ligne)]
    for registre, ligne in appuis:
        cellules = _cellules(ligne)
        if cellules and cellules[0].casefold() == GO_FICTIF.casefold():
            raise GardeArret(f"constat de lancement : une ligne du registre ({registre}) a pour identifiant {GO_FICTIF} — "
                             "ligne d'un exemple fictif, refusée")
        if EMPREINTE_FICTIVE in graines_bras_a.empreintes_citees(ligne):
            raise GardeArret(f"constat de lancement : une ligne du registre ({registre}) cite une empreinte de "
                             "soixante-quatre zéros — valeur d'un exemple fictif, refusée")


def constater(configuration_scellee, registre_courant, *, commit_du_registre_courant, date_utc, registre_fige) -> tuple[dict, Path | None]:
    """Fait le constat de lancement. Rend (le constat, le chemin du fichier scellé) ; le chemin vaut `None` quand le
    constat est malsain : rien n'est alors scellé. Tous les arguments nommés sont exigés, sans valeur par défaut ;
    `registre_fige` vaut `None` quand, et seulement quand, la configuration inscrit `null` pour le registre.
    Refus (gardes ordinaires, sans fichier) : configuration qui ne se lit pas ; pièce de l'état figé absente, de trop,
    ou d'une autre empreinte que celle que la configuration inscrit ; registre courant absent ou illisible ; registre
    courant qui ne contient pas une ligne de l'état figé ; commit ou date hors de leur forme ; une valeur de l'exemple
    fictif (`refuser_les_empreintes_fictives_de_la_configuration`, `refuser_les_lignes_fictives`) ; un constat déjà scellé avec un autre contenu (R12)."""
    configuration = configuration_bras_a.lire_la_configuration_scellee(configuration_scellee)
    refuser_les_empreintes_fictives_de_la_configuration(configuration)
    if not isinstance(commit_du_registre_courant, str) or _COMMIT.fullmatch(commit_du_registre_courant) is None:
        raise GardeArret("constat de lancement : le commit du registre courant est exigé (7 à 40 signes hexadécimaux)")
    if not isinstance(date_utc, str) or _DATE.fullmatch(date_utc) is None:
        raise GardeArret("constat de lancement : la date du constat est exigée, en temps universel (AAAA-MM-JJTHH:MM:SSZ)")
    attendu = configuration["pieces_attendues"][configuration_bras_a.REGISTRE_ATTENDU]
    if attendu is None:
        if registre_fige is not None:
            raise GardeArret("constat de lancement : la configuration n'inscrit aucun registre figé (`null`, première "
                             "livraison) — aucune pièce de l'état figé n'est à donner")
        figees = []
    else:
        figees = graines_bras_a.lire_le_registre_fige(registre_fige, attendu)      # vérifie l'empreinte de la pièce
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
    restantes = list(courantes)
    for ligne in figees:
        if ligne not in restantes:
            raise GardeArret("constat de lancement : le registre courant ne contient pas une ligne de l'état figé — ce n'est "
                             "pas un état postérieur du même registre (une ligne du registre n'est jamais retirée ni changée)")
        restantes.remove(ligne)
    entrees_depuis = restantes
    refuser_les_lignes_fictives(configuration, figees, courantes)
    inscrite = any(re.search(r"(?<![0-9a-f])" + configuration["sha256"] + r"(?![0-9a-f])", ligne) for ligne in courantes)
    revocation = False
    for go in lignes_de_go_employees(figees, configuration):
        for ligne in entrees_depuis:
            cellules = _cellules(ligne)
            if len(cellules) > _CELLULE_DU_TYPE and cellules[0] != go \
                    and cellules[_CELLULE_DU_TYPE].casefold() == graines_bras_a.TYPE_DE_REVOCATION \
                    and re.search(re.escape(go) + r"(?!\d)", ligne):
                revocation = True
    constat = {"date_utc": date_utc, "sha256_de_la_configuration": configuration["sha256"],
               "sha256_du_registre_fige": attendu, "commit_du_registre_courant": commit_du_registre_courant,
               "configuration_inscrite": inscrite, "revocation_entree": revocation}
    if sorted(constat) != sorted(configuration_bras_a.CHAMPS_DU_CONSTAT_DE_LANCEMENT):
        raise GardeArret("constat de lancement : ses six champs, et eux seuls")
    if not inscrite or revocation:
        return constat, None
    chemin = configuration_bras_a.dossier_de_la_livraison(configuration) / configuration_bras_a.NOM_DU_CONSTAT_DE_LANCEMENT
    depots_bras_a.ecrire_et_sceller(chemin, json.dumps(constat, ensure_ascii=False, sort_keys=True, indent=1) + "\n")
    return constat, chemin


def main(argv: list[str]) -> int:
    lecteur = argparse.ArgumentParser(description="Constat de lancement de la lecture de la discrétion, bras A.")
    lecteur.add_argument("configuration", help="configuration scellée de la livraison")
    lecteur.add_argument("registre_courant", help="registre courant de la branche principale, remis comme une pièce")
    lecteur.add_argument("--commit", required=True, help="commit auquel le registre courant a été pris")
    lecteur.add_argument("--date-utc", required=True, help="date du constat, AAAA-MM-JJTHH:MM:SSZ")
    lecteur.add_argument("--registre-fige", default=None, help="pièce de l'état figé du registre (rien pour une première livraison)")
    a = lecteur.parse_args(argv)
    try:
        constat, chemin = constater(a.configuration, a.registre_courant, commit_du_registre_courant=a.commit,
                                    date_utc=a.date_utc, registre_fige=a.registre_fige)
    except GardeArret as e:
        print(f"ARRÊT : {e}", file=sys.stderr)
        return 2
    sortie = {"constat": constat, "sain": chemin is not None, "fichier": None if chemin is None else str(chemin),
              "sha256_du_fichier": None if chemin is None else hashlib.sha256(chemin.read_bytes()).hexdigest()}
    print(json.dumps(sortie, ensure_ascii=False, sort_keys=True, indent=1))
    if chemin is None:
        print("CONSTAT MALSAIN : la lecture ne part pas — "
              + ("la configuration n'est pas inscrite au registre courant" if not constat["configuration_inscrite"]
                 else "une révocation de la ligne de GO est entrée depuis l'état figé"), file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
