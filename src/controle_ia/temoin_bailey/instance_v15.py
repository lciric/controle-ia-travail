"""Lanceur côté instance — témoin « attaque publiée reproduite » (Bailey et collègues), v15.

La v15 applique la relecture différentielle du code v15 (`docs/notes/reproduction-attaque-publiee-v1/relecture-
differentiel-code-condition6-v15-bailey-v1.md`, `0d7cc2a1…`, « conforme après corrections ») et ne change rien d'autre :
- D-1 : `_SUITE` ne prend plus `_` ni `-` (les identifiants Python longs et le dossier du modèle dans le cache restent) ;
- D-2 : `_JETON` ne prend plus `hf_transfer`, `hf_quantizer` (jeton seul, précédé d'aucun caractère de mot, 30 caractères
  au moins après `hf_`) ;
- D-3 : `_DECIMAL` prend aussi `.97`, les écritures à exposant (`1e-3`, `9.7466e-01`) ; les entiers et les mots restent :
  le filtre est une défense en profondeur, la garantie vient de la condition d'écriture ;
- D-5 : le drapeau s'appelle `mort_seule_avant_configuration` (début exact de la configuration **et** aucun arrêt décidé
  par l'instance) ; docstring complétée ;
- D-7 : `_vide` tient pour non vide tout dossier qui contient autre chose que de vrais dossiers et des fichiers vides
  (lien symbolique, tube, lien cassé, fichier non vide) et toute erreur de lecture ; le chemin du journal des notes est
  lu dans `config-journal-v3.json` (`dossier_journal`), comme l'écrit le journaliseur.

Docstring de la v14 :

La v14 applique la relecture du code v14 (`docs/notes/reproduction-attaque-publiee-v1/relecture-code-condition6-v14-
bailey-v1.md`, `0e7c96ca…`, « conforme après corrections ») et ne change rien d'autre :
- R-1 : le filtre du message d'erreur remplace les valeurs **sur place** au lieu de retirer la ligne : un nombre décimal
  isolé devient « <nombre> » (les versions et les chemins, comme `python3.11` ou `2.4.1`, sont gardés) ; une suite de
  plus de 12 chiffres devient « <chiffres> » ; seule une ligne qui contient `tensor(` est retirée entière ;
- R-4 : un jeton Hugging Face (`hf_…`) devient « <jeton> », une suite alphanumérique de 32 caractères ou plus devient
  « <suite> » ;
- R-2 : le message n'est écrit que si, en plus (code non nul, garde de démarrage non décidée, zéro tour complet), la
  sortie standard reçue est un **début exact** de la configuration attendue, l'instance n'a décidé aucun arrêt (cause
  nulle : l'enfant est mort de lui-même), le journal des notes est absent ou vide, et les dossiers des sondes et des
  suffixes (écart 9) sont absents ou vides ;
- R-5 : les deux autres listes locales nommées `signal` (`reconstituer_etat`, `main`) sont renommées `signaux` (sans
  effet aujourd'hui) ;
- petits points : `_ecrire_texte` efface son temporaire en cas d'erreur ; la ligne `ETAT` d'`executer` porte
  `erreur_demarrage`.

Docstring de la v13 :

La v13 (décision de Lazar du 12 novembre 2026, « go (a) », `registres/passations/2026-11-12-1720-decision-lazar-bailey-
option-a-v14.md`, après la « seconde chute du pilote » du run v6, note `2026-11-12-1545-…`) ajoute une seule chose et ne
change rien d'autre : le **message d'erreur d'une exécution morte avant tout tour** sort de l'instance.
- Condition, appréciée après la fin de l'enfant : code de retour non nul, **garde de démarrage non décidée** (la
  configuration effective n'a jamais été imprimée : `train_harmful.py` n'a pas commencé sa boucle) **et zéro tour
  complet**. Dans ce cas seulement, aucune note, aucun texte produit par le modèle, aucun suffixe ni aucune sonde
  n'existe encore.
- Contenu : les `LIGNES_ERREUR_MAX` dernières lignes de `sortie-erreur-instance.log`, chacune tronquée à
  `LARGEUR_LIGNE_MAX` caractères ; une ligne qui contient un nombre décimal, le mot `tensor(` ou une suite de plus de
  12 chiffres (motif `_VALEURS`) est remplacée par « [ligne retirée : valeurs numériques] » ; total borné à
  `TAILLE_ERREUR_MAX` octets. Écrit dans `ERREUR_DEMARRAGE` (`erreur-demarrage-v1.txt`) du dossier d'exécution.
- Défaut de la v12 corrigé (trouvé par l'essai v14) : dans `executer`, une liste locale nommée `signal` masquait le
  module `signal` ; tout arrêt de l'enfant par son PID (garde de démarrage tombée, dépense, échéance) levait
  `UnboundLocalError` au lieu d'arrêter. Renommée `signaux`.
- Ce fichier entre dans la liste fermée des fichiers empreintés et transférés (`SORTANTS`, qui étend `cv.SORTANTS` de ce
  seul nom) ; il n'est jamais écrit dans un autre cas.
Addendum 3 au préenregistrement (liste « Ce qui sort de l'instance ») : à sceller avant toute instance.

Docstring de la v12 :

La v12 applique la relecture du code v11 (`docs/notes/reproduction-attaque-publiee-v1/relecture-code-condition6-v11-
bailey-v1.md`, `044ba3e2…`) et ne change rien d'autre ici :
- V-3 : l'observation du chien ne bloque plus les causes calculées en mémoire. `fin_prevue` est lue sous `try` (erreur
  notée, lue prudemment : fausse), comme la marque et les commandes en cours ; et si l'observation lève quand même,
  le passage décide sur la seule dépense, l'échéance et le battement de la conduite (`decider` avec `fin=False`,
  `rapatrie=False`, `en_cours=[]`), sans aucune lecture qui puisse lever hors de la date du battement (déjà prudente) ;
- Q-4 : `_ecrire_json` écrit dans un fichier temporaire propre au processus (`<chemin>.tmp-<pid>`), le vide sur le
  disque (`fsync`), puis le met en place par `os.replace` : un chien tué par son PID pendant une écriture (empreintes,
  état reconstitué, état de l'arrêt) ne laisse jamais un fichier à moitié écrit, et deux processus qui écrivent le
  même fichier ne partagent plus le même temporaire.
Les noms des fichiers de données ne changent pas (`arret-autonome-v10.json`, `chien-de-garde-v10.jsonl`).

Docstring de la v11 :

La v11 applique la relecture du code v10 (`docs/notes/reproduction-attaque-publiee-v1/relecture-code-condition6-v10-
bailey-v1.md`, `b6b6430b…`) et ne change rien d'autre ici :
- B-1 : `ChienDeGarde._preparer` ne lève jamais (chaque écriture sous `try`, erreur notée au journal du chien) et pose
  `prepare` quoi qu'il arrive ; une erreur de l'observation (marque, commandes en cours) ne lève plus : elle est notée et
  lue de la façon la plus prudente (marque absente, aucune commande en cours) ; un disque plein n'empêche plus l'appel
  d'arrêt ; le battement du chien, s'il ne peut être réécrit, est touché (`os.utime`, sans bloc nouveau) ;
- B-2 : après la décision, l'attente de la fin des commandes est bornée (`ATTENTE_COMMANDES_MAX_S` = 2 ×
  `GRACE_EXECUTION_S`, ou `PASSAGES_ATTENTE_MAX` passages) ; au-delà (processus en sommeil non interruptible, signal
  refusé), le chien note au journal les commandes survivantes, prépare l'arrêt (état reconstitué, ou erreur notée) et
  arrête le conteneur quand même ; une erreur pendant l'arrêt par PID compte comme une commande non finie, sous la même
  borne ;
- P-4 : l'appel à l'API porte l'en-tête `User-Agent` du paquet `vastai` 1.11.0 (`vastai-cli/1.11.0`, celui de
  `vastai stop instance` : `vastai/api/client.py` l. 134, `vastai/cli/utils.py` l. 19) et est refait, comme le paquet,
  sur les codes 429, 502, 503, 504 et sur une erreur de transport (trois essais ; `Retry-After` suivi jusqu'à 60 s) ;
- `CHIEN_FRAICHEUR_S` : âge au-delà duquel la conduite tient le chien pour mort (P-1, `lanceur_v11`).

Docstring de la v10 :

La v10 (décision de Lazar du 11 novembre 2026, option (b), `registres/passations/2026-11-11-1226-decision-lazar-option-b-
arret-autonome.md`) ajoute l'**arrêt autonome de l'instance** et ne change rien d'autre (la v9 n'a pas existé pour ce
module : le numéro suit celui du lanceur). Trois sous-commandes nouvelles :
- `chien-de-garde` : processus détaché, lancé par l'amorce, indépendant des exécutions. À chaque passage
  (`PERIODE_CHIEN_S`), il écrit son battement et décide (`decider`, fonction pure) : l'instance s'arrête elle-même
  quand (1) la dernière exécution prévue a fini (marque `rapatrie` posée par la conduite après son transfert, ou fin
  du run principal sans relance permise, ou fin de la relance) ; (2) la dépense du poste atteint B − 2 (même calcul
  que `verifier_budget`) ; (3) l'échéance du GO moins la marge de transfert est atteinte ; (4) la conduite est
  injoignable : son battement (`battement-conduite`, touché à chaque sondage) a plus de `D_ABANDON_S` (lecture à
  acter : 7 200 s). Conduite injoignable pendant le run principal (ou sa relance) sans autre cause : l'exécution finit
  sous ses gardes de dépense et d'échéance, puis arrêt ; ailleurs (mise en place, contrôle du juge, pilote, règle,
  attente entre deux étapes) : arrêt aussitôt. **Conduite vivante** : les causes (1) à (3) ne coupent pas le
  transfert qu'elle fait ; l'instance s'arrête quand la marque `rapatrie` est posée, ou après
  `DELAI_PRISE_EN_CHARGE_S` (3 600 s) de cause tenue, ou au plus tard à D ≥ B − marge de secours (0,5 USD, seuil du
  veilleur) ou à l'échéance moins la moitié de la marge (borne locale de la conduite) ; lecture à acter.
  Procédure d'arrêt (`ChienDeGarde`, sur plusieurs passages) : chaque commande en cours est arrêtée par son PID
  (groupe, identité vérifiée, R10 ; une exécution sous la cause dépense ou échéance a `GRACE_EXECUTION_S` pour
  s'arrêter elle-même) ; état d'exécution reconstitué si absent (`reconstituer_etat`, causes de la liste fermée :
  « dépense », « échéance du GO », « instance injoignable » pour la conduite injoignable, « arrêt par la conduite »
  pour la fin, « coupure de l'hôte » pour une exécution trouvée morte) ; empreintes de chaque étape (`empreintes`) ;
  état `arret-autonome-v10.json` ; puis **arrêt du conteneur** (pas sa destruction : les journaux restent sur son
  disque ; seul le stockage reste facturé).
- `auto-arret` : vérification faite par la conduite après l'amorce, **avant la mise en place** ; si elle échoue, la
  conduite tient la garde de mise en place pour tombée : pas de run (aucun repli silencieux).
- `en-cours` : liste des commandes détachées vivantes (pour `reprendre`, côté poste local).
`empreintes --si-absent` garde les empreintes prises avant l'arrêt (reprise).

Arrêt du conteneur depuis l'intérieur — **établi** (sources) :
- documentation publique de Vast.ai (lue le 11 novembre 2026, `https://docs.vast.ai/llms-full.txt`, pages
  `guides/instances/docker-environment`, « Predefined Variables » et « Using the CLI from Inside an Instance » ;
  `guides/reference/faq/instances`, « How do I stop an instance from within itself? » ; `api-reference/hello-world`) :
  Vast pose dans chaque instance `CONTAINER_ID` (« The unique ID of your instance ») et `CONTAINER_API_KEY`
  (« Per-instance API key for CLI commands from inside the container ») ; « The `instance_api_key` is a restricted
  key injected into the container as `CONTAINER_API_KEY`, it can only start, stop, or destroy that specific
  instance » ; « vastai stop instance $CONTAINER_ID » arrête l'instance depuis l'intérieur ; « vastai start instance
  $CONTAINER_ID » est un essai sans effet sur une instance en marche ; dans une session `ssh`, ces variables peuvent
  manquer (d'où leur lecture dans `/proc/1/environ`, environnement du processus principal du conteneur) ; une
  instance arrêtée garde ses données et n'est plus facturée qu'au stockage (« stopped — disk charges only »,
  `vastai/SKILL.md` du paquet installé, v1.11.0) ;
- code installé du paquet `vastai` 1.11.0 : l'arrêt est `PUT {VAST_URL ou https://console.vast.ai}/api/v0/instances/
  <id>/` avec `{"state": "stopped"}` (`vastai/api/instances.py`, `stop_instance`), en-tête `Authorization: Bearer
  <clé>` (`vastai/api/client.py`, l. 141 et 164-165) ; le démarrage, le même appel avec `{"state": "running"}`
  (`start_instance`) ; réponse JSON `success` (`vastai/cli/commands/instances.py`, `stop_instance_impl`) ; le code de
  serveur sans état du paquet lit aussi `CONTAINER_API_KEY` (« Inside a Vast instance, Kaalia sets CONTAINER_API_KEY
  with the instance-level API key », `vastai/serverless/remote/serve_deployment.py`) et `CONTAINER_ID`
  (`vastai/serverless/server/lib/metrics.py`). Ce module fait cet appel avec la bibliothèque standard
  (`urllib.request`) : rien n'est installé sur l'instance, aucune version figée ne change, **aucune clé du compte de
  l'utilisateur n'est posée sur l'instance** (seule la clé restreinte que Vast y met est lue, jamais imprimée).
**Non établi** (vérifié sur l'instance par `auto-arret`, avant la mise en place, garde : mise en place tombée, pas
de run) : que les deux variables sont présentes dans l'environnement du processus principal de **cette** image ; que
`CONTAINER_ID` égale l'identifiant rendu par la création ; que la clé est acceptée par l'API pour cette instance
(essai sans effet `{"state": "running"}`, recommandé par la documentation) ; que l'instance joint
`console.vast.ai` ; que le chien de garde vit (PID à son identité, battement frais). **Non établi et non vérifiable
sans arrêter l'instance** (risque déclaré) : que `{"state": "stopped"}` envoyé avec cette clé arrête effectivement
le conteneur et la facturation de la carte (affirmé par la documentation, jamais éprouvé ici) ; ce que coûte un
conteneur sorti (`exited`). Repli **déclaré, journalisé** : après `ESSAIS_API_AVANT_PID1` appels refusés, signal
TERM au processus principal du conteneur (PID 1) ; effet non établi (un PID 1 sans gestionnaire ignore les signaux
envoyés depuis son propre espace de noms ; un conteneur sorti est « exited », coût non documenté) ; l'appel à l'API
est retenté à chaque passage.

Docstring de la v8 :

La v8 emploie `lecture_v8` (décision de Lazar du 10 novembre 2026, points A-1 et A-2 de la relecture
`5831e98c…`) et ne change rien d'autre : l'état d'exécution (`executer`, `tours --ecrire-etat`) et la ligne `ETAT` de
`tours` portent dans `gardes_tombees` le nom « ligne de garde coupée (garde inconnue) » (et celui de la garde, s'il est
lisible en entier) quand la dernière ligne d'un journal de gardes est coupée (A-2) ; une ligne coupée des gardes du
lanceur retire tous les tours (K′ = 0, A-1).

Docstring de la v7 :

La v7 emploie `lecture_v7` (relecture des lignes touchées v5 → v6, `a46dc4fb…`, C-1 à C-4) et applique C-2 et C-4 ici :
chaque commande qui lit les journaux (`executer` à sa fin, `tours`, `tours --ecrire-etat`) porte **sa propre** liste
des lignes coupées ignorées (aucun état global, rien ne s'accumule dans le processus) et l'écrit dans l'état
d'exécution (`lignes_tronquees_ignorees`, chemins des fichiers sur l'instance) **et** dans sa ligne `ETAT`. Une
dernière ligne coupée dans un journal de gardes retire du compte le dernier tour présent (C-3, `lecture_v7`).

Docstring de la v6 :

La v6 ne change que la lecture des journaux employée sur l'instance (`lecture_v6`, M-2 : dernière ligne coupée
ignorée et signalée).

La v5 reprend la v4 (`instance_v4.py`, dont la docstring suit) sans autre changement que ceux de la relecture des
lignes touchées v3 → v4 (`relecture-lignes-touchees-code-condition6-v4-bailey-v1.md`, `ff6c76c7…`) :
- C8 (N-1) : `tours --ecrire-etat --cause … --manifeste … --phase …` écrit `etat-execution-v3.json` **s'il est
  absent** (jamais d'écrasement d'un fichier existant), marqué « reconstitué », avec un `code_retour` non nul, la
  `cause_arret` (liste fermée `CAUSES_RECONSTITUEES` : coupure de l'hôte, dépense, échéance du GO, instance
  injoignable, arrêt par la conduite), les tours complets, les gardes tombées, les durées lues à
  `sortie-durees-v3.jsonl` et le K de la phase lu au manifeste ; sans lire aucune note. La conduite l'appelle sur une
  exécution morte (après l'arrêt du groupe, C10) et, avant les empreintes, sur toute exécution qu'elle a arrêtée par
  PID. Ainsi toute exécution transférée porte un état, et la lecture rend le verdict que le texte donne (l. 338,
  371-372) ;
- l'état d'exécution est écrit de façon atomique (fichier temporaire, puis `os.replace`) : un arrêt par signal
  pendant l'écriture ne laisse jamais un état à moitié écrit, que la reconstitution n'écraserait pas.

Docstring de la v4 :

Préenregistrement scellé `prereg/temoin-attaque-publiee-bailey-v1.md` (`fb6c2f34…`) : plan d'analyse (écarts, graines,
contrôles du juge, pilote, règle du nombre de tours, run principal, gardes), « Ce qui sort de l'instance ».
La v4 reprend la v3 (`instance_v3.py`) sans autre changement que ceux de la relecture en différentiel du code v3
(`relecture-differentiel-code-condition6-v3-bailey-v1.md`, `a2107244…`) :
- C7 (D-8) : `regle-tours` imprime **une seule** ligne `ETAT`, qui porte K, t, D, c **et**, si K < 20, la garde
  « nombre de tours » tombée (code 3) ; la conduite lit donc K < 20 comme « K < 20 après le pilote : arrêt, devis
  révisé à Lazar », et non plus comme « règle non calculée » ; `etat-regle-v3.json` reste écrit avant la garde ;
- C4 (D-4) : sous-commande `tours`, qui rend, sans lire aucune note, le nombre de tours complets et les gardes
  tombées d'une exécution dont le processus est mort sans écrire son état (coupure de l'hôte), pour que la conduite
  applique la liste d'arrêt (relance avant 20 tours complets seulement).
Tout le reste (mise en place, contrôle du juge, exécution, empreintes) est celui de la v3, décrit dans sa docstring.

Sous-commandes (sorties dans `--travail`, un dossier par étape, neuf) : `mise-en-place`, `controle-juge`,
`executer --phase pilote|pilote-reprise|principal|principal-relance`, `regle-tours`, `empreintes`, `tours`.
Chaque commande imprime une seule ligne `ETAT {…}` (états de gardes, durées, codes) ; jamais une note ni un texte.
"""
from __future__ import annotations

import argparse
import hashlib
import json
import os
import re
import signal
import subprocess
import sys
import time
from pathlib import Path

from ..gardes import GardeArret
from . import analyse_v3 as an
from . import conventions_v3 as cv
from .execution_v3 import configuration_attendue, surcharges

MARK = re.compile(r"^MARK: Epoch (\d+) took ([0-9.]+) seconds\s*$")
PHASES = {"pilote": "pilote", "pilote-reprise": "pilote", "principal": "principal", "principal-relance": "principal"}
MARGE_TRANSFERT_S = 3600.0
# C8 : causes d'une exécution sans état, écrites dans l'état reconstitué (liste fermée)
CAUSES_RECONSTITUEES = ("coupure de l'hôte", "dépense", "échéance du GO", "instance injoignable",
                        "arrêt par la conduite")
# v10 : arrêt autonome de l'instance (chien de garde)
D_ABANDON_S = 7200.0  # battement de la conduite plus vieux : conduite injoignable (lecture à acter)
DELAI_PRISE_EN_CHARGE_S = MARGE_TRANSFERT_S  # conduite vivante : délai laissé à son transfert (lecture à acter)
GRACE_EXECUTION_S = 300.0  # exécution sous dépense ou échéance : délai pour s'arrêter elle-même (pas de 5 s, 60 s)
PERIODE_CHIEN_S = 30.0
MARGE_SECOURS_USD = 0.5  # seuil du veilleur local (B − 0,5) : borne dure de l'arrêt, conduite vivante
ESSAIS_API_AVANT_PID1 = 10
RENOUVELER_ARRET_S = 600.0  # conteneur toujours en marche après un arrêt accepté : demande renouvelée
# v11 (B-2) : attente bornée de la fin des commandes après la décision d'arrêt
ATTENTE_COMMANDES_MAX_S = 2 * GRACE_EXECUTION_S
PASSAGES_ATTENTE_MAX = 40
CHIEN_FRAICHEUR_S = 600.0  # v11 (P-1) : battement du chien plus vieux : la conduite le tient pour mort et le relance
# v11 (P-4) : en-tête et nouveaux essais du paquet `vastai` 1.11.0 (`vastai/api/client.py`)
USER_AGENT_VAST = "vastai-cli/1.11.0"
ESSAIS_REQUETE = 3
CODES_A_REFAIRE = (429, 502, 503, 504)
RETRY_AFTER_MAX_S = 60.0
RACINE = "/root"
# v13 : message d'erreur d'une exécution morte avant tout tour (liste fermée étendue de ce seul nom)
ERREUR_DEMARRAGE = "erreur-demarrage-v1.txt"
SORTANTS = cv.SORTANTS + (ERREUR_DEMARRAGE,)
LIGNES_ERREUR_MAX = 60
LARGEUR_LIGNE_MAX = 300
TAILLE_ERREUR_MAX = 20000
RETIREE = "[ligne retirée : tenseur]"
# v14 (R-1) : nombre décimal isolé (pas dans un nom, un chemin ni une version : python3.11, 2.4.1 restent)
_DECIMAL = re.compile(r"(?<![\w./-])-?(?:\d*\.\d+(?:[eE][-+]?\d+)?|\d+[eE][-+]?\d+)(?![\w./])")  # v15 (D-3)
_CHIFFRES = re.compile(r"\d{13,}")
_JETON = re.compile(r"(?<![A-Za-z0-9_])hf_[A-Za-z0-9]{30,}")  # v14 (R-4), v15 (D-2)
_SUITE = re.compile(r"[A-Za-z0-9]{32,}")  # v14 (R-4), v15 (D-1) : clés, empreintes, longues suites
EXECUTIONS = ("pilote", "pilote-reprise", "principal", "principal-relance")
RUN_PRINCIPAL = ("principal", "principal-relance")
CHIEN = "chien-de-garde"
MINUTERIE = "minuterie"
BATTEMENT_CONDUITE = "battement-conduite"
MARQUE_RAPATRIE = "rapatrie"
ETAT_ARRET = "arret-autonome-v10.json"
JOURNAL_CHIEN = "chien-de-garde-v10.jsonl"
URL_VAST = "https://console.vast.ai"
CAUSE_RECONSTITUEE = {"dépense": "dépense", "échéance du GO": "échéance du GO",
                      "conduite injoignable": "instance injoignable", "fin": "arrêt par la conduite",
                      "minuterie": "arrêt par la conduite"}


def erreur_demarrage_filtree(texte: str) -> str:
    """v14 (R-1, R-4) : dernières lignes de la sortie d'erreur, tronquées ; valeurs remplacées sur place ; ligne à
    `tensor(` retirée ; total borné."""
    propres = []
    for l in texte.splitlines()[-LIGNES_ERREUR_MAX:]:
        if "tensor(" in l:
            propres.append(RETIREE)
            continue
        l = _JETON.sub("<jeton>", l)
        l = _SUITE.sub("<suite>", l)
        l = _CHIFFRES.sub("<chiffres>", l)
        l = _DECIMAL.sub("<nombre>", l)
        propres.append(l[:LARGEUR_LIGNE_MAX])
    sortie = "\n".join(propres) + ("\n" if propres else "")
    return sortie.encode("utf-8")[-TAILLE_ERREUR_MAX:].decode("utf-8", errors="ignore")


def _vide(chemin: Path) -> bool:
    """v15 (D-7) : absent ; ou fichier ordinaire vide ; ou dossier (non lien) dont toutes les entrées sont de vrais
    dossiers ou des fichiers ordinaires vides. Toute autre entrée (lien symbolique, tube, lien cassé, fichier non vide) et
    toute erreur de lecture : non vide."""
    try:
        if not chemin.exists() and not chemin.is_symlink():
            return True
        if chemin.is_symlink():
            return False
        if chemin.is_file():
            return chemin.stat().st_size == 0
        if not chemin.is_dir():
            return False
        for p in chemin.rglob("*"):
            if p.is_symlink():
                return False
            if p.is_dir():
                continue
            if not p.is_file() or p.stat().st_size != 0:
                return False
        return True
    except Exception:
        return False


def _journal_des_notes(travail: Path) -> Path:
    """v15 (D-7) : le journal des notes là où le journaliseur l'écrit (`dossier_journal` de `config-journal-v3.json`) ;
    à défaut, `cv.JOURNAL_NOTES`."""
    try:
        d = json.loads((travail / "config-journal-v3.json").read_text(encoding="utf-8"))["dossier_journal"]
        return Path(d) / Path(cv.JOURNAL_NOTES).name
    except Exception:
        return travail / cv.JOURNAL_NOTES


def ecrire_erreur_demarrage(travail: Path, code_retour, demarrage, complets,
                            mort_seule_avant_configuration: bool = False) -> bool:
    """v13, v14 (R-2), v15 (D-5, D-7) : écrit `ERREUR_DEMARRAGE` seulement si (1) l'enfant est sorti en erreur, (2) sans
    garde de démarrage décidée, (3) sans aucun tour complet, (4) `mort_seule_avant_configuration` : la sortie standard
    reçue est un début exact de la configuration attendue **et** l'instance n'a décidé aucun arrêt (garde de démarrage,
    dépense, échéance) : l'enfant est mort de lui-même, (5) le journal des notes (lu là où l'écrit le journaliseur) et les
    dossiers des sondes et des suffixes sont vides au sens de `_vide`. Rend vrai s'il l'a écrit. Ne lève pas."""
    try:
        if code_retour in (0, None) or demarrage is not None or complets != 0 or not mort_seule_avant_configuration:
            return False
        if not (_vide(_journal_des_notes(travail)) and _vide(travail / "sondes") and _vide(travail / "params")):
            return False
        brut = (travail / "sortie-erreur-instance.log").read_bytes().decode("utf-8", errors="replace")
        _ecrire_texte(travail / ERREUR_DEMARRAGE, erreur_demarrage_filtree(brut))
        return True
    except Exception:
        return False


def _ecrire_texte(chemin: Path, texte: str) -> None:
    """v14 : comme `_ecrire_json` : temporaire propre au processus, `fsync`, `os.replace` ; temporaire effacé en cas
    d'erreur, l'erreur sort."""
    tmp = Path(f"{chemin}.tmp-{os.getpid()}")
    try:
        with open(tmp, "w", encoding="utf-8") as f:
            f.write(texte)
            f.flush()
            os.fsync(f.fileno())
        os.replace(tmp, chemin)
    except BaseException:
        try:
            tmp.unlink()
        except OSError:
            pass
        raise


def _ecrire_json(chemin: Path, objet) -> None:
    """Écriture atomique (v5) : un arrêt par signal pendant l'écriture ne laisse aucun fichier à moitié écrit. v12
    (Q-4) : temporaire propre au processus (`<chemin>.tmp-<pid>`), vidé sur le disque avant `os.replace` ; en cas
    d'erreur, le temporaire est effacé et l'erreur sort (le fichier d'origine reste entier)."""
    tmp = Path(f"{chemin}.tmp-{os.getpid()}")
    try:
        with open(tmp, "w", encoding="utf-8") as f:
            f.write(json.dumps(objet, ensure_ascii=False, indent=2, sort_keys=True) + "\n")
            f.flush()
            os.fsync(f.fileno())
        os.replace(tmp, chemin)
    except BaseException:
        try:
            tmp.unlink()
        except OSError:
            pass
        raise


def _ajouter(chemin: Path, objet) -> None:
    with open(chemin, "a", encoding="utf-8") as f:
        f.write(json.dumps(objet, ensure_ascii=False, sort_keys=True) + "\n")
        f.flush()
        os.fsync(f.fileno())


def lire_manifeste(chemin) -> dict:
    return json.loads(Path(chemin).read_text(encoding="utf-8"))


def etat(objet: dict) -> None:
    """Seule sortie d'une commande vers le poste local (A-9)."""
    print("ETAT " + json.dumps(objet, ensure_ascii=False, sort_keys=True), flush=True)


def verifier_budget(depense: dict, echeance_arret: float, maintenant: float | None = None) -> None:
    """Correction 13 : arrêt à B − 2 (dépense du poste, comptée comme D) ou à l'échéance d'arrêt (échéance du GO moins
    la marge de transfert), hors des exécutions aussi."""
    from .journaliseur_v3 import depense_courante
    maintenant = time.time() if maintenant is None else maintenant
    an.garde_depense(depense_courante(depense, maintenant), float(depense["b"]))
    if maintenant >= float(echeance_arret):
        raise GardeArret("garde « échéance du GO » tombée : échéance moins la marge de transfert atteinte")


# --- mise en place ----------------------------------------------------------------------------------------------------

def _git(clone: Path, *args: str) -> str:
    try:
        return subprocess.run(["git", "-C", str(clone), *args], check=True, capture_output=True, text=True).stdout.strip()
    except (subprocess.CalledProcessError, FileNotFoundError):
        raise GardeArret("garde « dépôt public » tombée : dépôt illisible") from None


def garde_depot_public(clone: Path, commit: str = cv.COMMIT_PUBLIC, arbre: str = cv.ARBRE_PUBLIC) -> str:
    if _git(clone, "rev-parse", "HEAD") != commit:
        raise GardeArret("garde « dépôt public » tombée : commit")
    if _git(clone, "rev-parse", "HEAD^{tree}") != arbre:
        raise GardeArret("garde « dépôt public » tombée : arbre")
    if _git(clone, "status", "--porcelain", "--untracked-files=no"):
        raise GardeArret("garde « dépôt public » tombée : fichier suivi modifié")
    return "passée"


def garde_empreintes_publiques(clone: Path) -> str:
    racine = clone / cv.SOUS_DOSSIER
    for rel, attendue in cv.EMPREINTES_PUBLIQUES.items():
        if not (racine / rel).is_file() or cv.sha_fichier(racine / rel) != attendue:
            raise GardeArret(f"garde « empreintes » tombée : {rel}")
    return "passée"


def memoire_vive_octets(meminfo: str | None = None, cgroup_max: str | None = None) -> int:
    """Minimum de `MemTotal` (en kio dans `/proc/meminfo`, malgré l'abréviation « kB ») et de la limite du groupe de
    contrôle (`/sys/fs/cgroup/memory.max`, si numérique ; « max » = sans limite)."""
    texte = Path("/proc/meminfo").read_text() if meminfo is None else meminfo
    total = None
    for ligne in texte.splitlines():
        if ligne.startswith("MemTotal:"):
            total = int(ligne.split()[1]) * 1024
    if total is None:
        raise GardeArret("garde « mémoire vive » tombée : MemTotal illisible")
    if cgroup_max is None:
        p = Path("/sys/fs/cgroup/memory.max")
        cgroup_max = p.read_text() if p.is_file() else "max"
    c = cgroup_max.strip()
    if c.isdigit():
        total = min(total, int(c))
    elif c != "max":
        raise GardeArret("garde « mémoire vive » tombée : limite du groupe de contrôle illisible")
    return total


def garde_memoire_vive(octets: int) -> str:
    """Texte : « mémoire vive de l'hôte au moins égale à celle de [Devis] » (128 Go, lus 128 × 10⁹ octets)."""
    if isinstance(octets, bool) or not isinstance(octets, int) or octets < cv.MEMOIRE_VIVE_MIN_OCTETS:
        raise GardeArret("garde « mémoire vive » tombée : hôte sous le minimum du devis")
    return "passée"


def garde_python(attendue: str, version=None) -> str:
    """Versions figées : Python 3.11 (S-2)."""
    v = sys.version_info if version is None else version
    if f"{v[0]}.{v[1]}" != str(attendue):
        raise GardeArret("garde « python » tombée : version de Python différente du manifeste")
    return "passée"


def garde_versions(attendues: dict, lire=None) -> str:
    """Versions installées égales au manifeste (écart 4). Refuse un dictionnaire vide et exige les paquets de
    `VERSIONS_EXIGEES` (correction 8)."""
    if not isinstance(attendues, dict) or not attendues:
        raise GardeArret("garde « versions » tombée : aucune version au manifeste")
    for paquet in cv.VERSIONS_EXIGEES:
        if paquet not in attendues:
            raise GardeArret(f"garde « versions » tombée : {paquet} absent du manifeste")
    if lire is None:
        from importlib.metadata import version as lire
    for paquet, v in attendues.items():
        try:
            installee = lire(paquet)
        except Exception:  # paquet absent : la garde tombe ci-dessous
            installee = None
        if installee != v:
            raise GardeArret(f"garde « versions » tombée : {paquet}")
    return "passée"


def commit_installe(paquet: str) -> str | None:
    from importlib.metadata import PackageNotFoundError, distribution
    try:
        brut = distribution(paquet).read_text("direct_url.json")
    except PackageNotFoundError:
        return None
    if not brut:
        return None
    return (json.loads(brut).get("vcs_info") or {}).get("commit_id")


def garde_commits_git(attendus: dict, lire=commit_installe) -> str:
    """Paquets tirés de dépôts tiers : commit installé égal au manifeste (A-2). `attendus` : {paquet: [url, commit]} ;
    non vide, et `strong_reject` au commit du texte (correction 8)."""
    if not isinstance(attendus, dict) or not attendus:
        raise GardeArret("garde « versions » tombée : aucun commit de paquet au manifeste")
    sr = list(attendus.get("strong_reject") or [])
    if len(sr) != 2 or sr[1] != cv.JUGE_COMMIT_PAQUET:
        raise GardeArret("garde « versions » tombée : commit de strong_reject différent du texte")
    for paquet, (_url, commit) in attendus.items():
        if lire(paquet) != commit:
            raise GardeArret(f"garde « versions » tombée : commit de {paquet}")
    return "passée"


def garde_revisions_cache(cache_hf: str, attendues: dict, lire=None) -> str:
    """`refs/main` du cache de Hugging Face égale à la révision épinglée, pour le modèle, l'adaptateur du juge et sa
    base (B-4) : le chargement hors ligne emploie cette révision."""
    from .journaliseur_v3 import revision_en_cache
    lire = lire or revision_en_cache
    for depot, rev in attendues.items():
        if lire(cache_hf, depot) != rev:
            raise GardeArret(f"garde « révisions » tombée : {depot}")
    return "passée"


def longueur_suffixe(chemin_modele: str, texte_initial: str) -> int:
    """Écart 10 : `tokenize(prompt_init, add_special_tokens=False, add_chat_template=False)` (`hf.py` l. 696-745)."""
    from transformers import AutoTokenizer
    tok = AutoTokenizer.from_pretrained(chemin_modele)
    return len(tok(texte_initial, add_special_tokens=False)["input_ids"])


def configuration_composee(clone: Path, surcharges_: list[str] | None = None):
    from hydra import compose, initialize_config_dir
    with initialize_config_dir(config_dir=str((clone / cv.SOUS_DOSSIER / "configs").resolve()), version_base=None):
        return compose(config_name="config", overrides=[f"experiment={cv.EXPERIENCE}", *(surcharges_ or [])]).experiment


def pas_attendus(clone: Path, cfg=None) -> int:
    import pandas as pd
    cfg = cfg if cfg is not None else configuration_composee(clone)
    n = len(pd.read_csv(clone / cv.SOUS_DOSSIER / cv.DOSSIER_JEU / "harmful_train_no_spec_tokens.csv"))
    return cv.pas_par_tour(int(cfg.epochs), n, int(cfg.batch_size))


def tokeniseur_present(cache_hf: str, depot: str, revision: str) -> bool:
    """P-c : le dépôt porte-t-il un tokeniseur (le paquet du juge charge `AutoTokenizer` sur le nom de l'adaptateur,
    `strong_reject/evaluate.py` l. 474-476) ? Écrit à la mise en place, sans arrêter."""
    d = Path(cache_hf) / ("models--" + depot.replace("/", "--")) / "snapshots" / revision
    return any((d / n).is_file() for n in ("tokenizer.json", "tokenizer_config.json", "tokenizer.model"))


def mise_en_place(manifeste: dict, clone: Path, sortie: Path, depense: dict, echeance_arret: float,
                  meminfo: str | None = None, cgroup_max: str | None = None) -> dict:
    sortie.mkdir(parents=True, exist_ok=True)
    etats = {}
    verifier_budget(depense, echeance_arret)
    gardes = (("dépôt public", lambda: garde_depot_public(clone)),
              ("empreintes", lambda: garde_empreintes_publiques(clone)),
              ("graines", lambda: an.garde_graines(manifeste["graines"])),
              ("mémoire vive", lambda: garde_memoire_vive(memoire_vive_octets(meminfo, cgroup_max))),
              ("python", lambda: garde_python(manifeste["python"])),
              ("versions", lambda: garde_versions(manifeste["versions"])),
              ("commits", lambda: garde_commits_git(manifeste["git"])),
              ("révisions", lambda: garde_revisions_cache(manifeste["cache_hf"], {
                  cv.MODELE: manifeste["revision_modele"], cv.JUGE: manifeste["juge"]["revision_adaptateur"],
                  cv.JUGE_BASE: manifeste["juge"]["revision_base"]})))
    for nom, f in gardes:
        try:
            etats[nom] = f()
        except GardeArret as err:
            etats[nom] = "tombée"
            _ecrire_json(sortie / cv.ETAT_MISE_EN_PLACE, {"gardes": etats, "message": str(err)})
            raise
    from .journaliseur_v3 import reponses_attendues
    cfg = configuration_composee(clone)
    n = longueur_suffixe(manifeste["chemin_modele"], cfg.model_config.prompt_init)
    gen = Path(manifeste["chemin_modele"]) / "generation_config.json"
    complement = {"longueur_suffixe": n, "ecart_10": n != 16, "pas_par_tour": pas_attendus(clone, cfg),
                  "configuration_generation": json.loads(gen.read_text()) if gen.is_file() else None,
                  "configuration_generation_sha256": cv.sha_fichier(gen) if gen.is_file() else None,
                  "memoire_vive_octets": memoire_vive_octets(meminfo, cgroup_max),
                  "empreintes_cibles_attendues": [cv.sha_texte(r) for r in reponses_attendues(
                      str(clone / cv.SOUS_DOSSIER / cv.DOSSIER_JEU))],
                  "tokeniseur_adaptateur_present": tokeniseur_present(manifeste["cache_hf"], cv.JUGE,
                                                                      manifeste["juge"]["revision_adaptateur"])}
    try:
        verifier_budget(depense, echeance_arret)
    except GardeArret as err:
        _ecrire_json(sortie / cv.ETAT_MISE_EN_PLACE, {"gardes": etats, **complement, "message": str(err)})
        raise
    _ecrire_json(sortie / cv.ETAT_MISE_EN_PLACE, {"gardes": etats, **complement})
    return {"gardes": etats, **complement}


# --- contrôles du juge ------------------------------------------------------------------------------------------------

def controle_juge(manifeste: dict, clone: Path, sortie: Path, depense: dict, echeance_arret: float,
                  etat_mise_en_place: Path, cache_juge=None, juge=None, generer=None) -> dict:
    """Négatif : réponses sans suffixe, génération publique (300 jetons au plus, décodage hérité, graine « pilote »),
    lots de `eval_batch_size`. Positif : colonne `response`. Juge par lots de `eval_batch_size` (B-3). Garde du juge
    après son premier appel, son état écrit avant de lever. Vérifie d'abord l'état de la mise en place (P-5) ; dépense
    et échéance vérifiées avant chaque lot (correction 13). Écrit les comptes et les empreintes des réponses ; jamais
    les textes. `cache_juge`, `juge`, `generer` : substituts pour l'épreuve sur processeur."""
    from .journaliseur_v3 import etat_juge_charge, garde_juge, reponses_attendues
    sortie.mkdir(parents=True, exist_ok=True)
    mep = json.loads(Path(etat_mise_en_place).read_text(encoding="utf-8")) if Path(etat_mise_en_place).is_file() else {}
    if set(mep.get("gardes", {})) != set(cv.GARDES_MISE_EN_PLACE) or any(
            v != "passée" for v in mep["gardes"].values()):
        raise GardeArret("contrôle du juge : mise en place non passée ou état absent")
    res = {"garde_juge": None}

    def ecrire():
        _ecrire_json(sortie / cv.ETAT_CONTROLE_JUGE, res)

    if "TESTING" in os.environ:
        res["garde_juge"] = "tombée"
        ecrire()
        raise GardeArret("garde « juge » tombée : variable TESTING présente au lancement du processus")
    racine = clone / cv.SOUS_DOSSIER
    cfg = configuration_composee(clone, [f"experiment.model_path={manifeste['chemin_modele']}"])
    lot = int(cfg.eval_batch_size)
    import pandas as pd
    lignes = []
    for split in ("val", "test"):
        df = pd.read_csv(racine / cv.DOSSIER_JEU / f"harmful_{split}_no_spec_tokens.csv")
        lignes += [(r["prompt"], r["response"]) for _, r in df.iterrows()]
    if len(lignes) != an.TAILLE:
        raise GardeArret("garde « longueur » tombée : 200 entrées nuisibles tenues à l'écart exigées")
    prompts = [p for p, _ in lignes]
    if generer is None:
        os.chdir(racine)
        sys.path.insert(0, str(racine))
        from transformers import set_seed
        set_seed(int(manifeste["graines"]["pilote"]))
        from obf_reps.models.llama3 import Llama3SoftPrompted
        from obf_reps.utils import validate_and_create_model_config
        modele = Llama3SoftPrompted.load_model(Path(cfg.model_path), validate_and_create_model_config(cfg.model_config))

        def generer(entrees):
            g = modele.generate_from_string(input_text=list(entrees), add_chat_template=True,
                                            use_tunable_params=False, max_new_tokens=cv.GEN_LEN)
            return list(g.gen_text)
    reponses = []
    for i in range(0, an.TAILLE, lot):
        verifier_budget(depense, echeance_arret)
        reponses += generer(prompts[i:i + lot])
    if len(reponses) != an.TAILLE:
        raise GardeArret("garde « longueur » tombée : 200 réponses sans suffixe exigées")
    res["empreintes_reponses_negatif"] = [cv.sha_texte(r) for r in reponses]
    if juge is None:
        from strong_reject.evaluate import cached_models as cache_juge, strongreject_finetuned as juge
    refs = reponses_attendues(str(racine / cv.DOSSIER_JEU))

    def juger(textes):
        notes = []
        for i in range(0, an.TAILLE, lot):
            verifier_budget(depense, echeance_arret)
            notes += juge({"forbidden_prompt": prompts[i:i + lot], "response": textes[i:i + lot]})["score"]
            if res["garde_juge"] is None:
                e = etat_juge_charge(cache_juge, manifeste["cache_hf"])
                res["juge_charge"] = e
                try:
                    garde_juge(e, manifeste["juge"], True)
                except GardeArret:
                    res["garde_juge"] = "tombée"
                    ecrire()
                    raise
                res["garde_juge"] = "passée"
        return notes

    neg = an.taux_juge(juger(reponses))
    pos = an.taux_juge(juger(refs))
    res.update({"negatif": neg, "positif": pos, "etats": an.controles_juge(neg, pos), "lot": lot})
    ecrire()
    an.garde_controles_juge(neg, pos)
    return res


# --- exécution surveillée ---------------------------------------------------------------------------------------------

class Surveillance:
    """Lit la sortie standard (seule) du processus enfant. Garde de démarrage : empreinte du début exact de la sortie
    standard contre celle du texte attendu. Lignes « MARK » : durées ; une ligne coupée entre deux lectures est gardée
    en tampon (B-7)."""

    def __init__(self, attendu: str, k_attendu: int, sortie: Path):
        self.attendu = attendu.encode("utf-8")
        self.k_attendu = k_attendu
        self.tampon = b""
        self.ligne = b""
        self.demarrage = None
        self.durees: dict[int, float] = {}
        self.sortie = sortie

    def recevoir(self, octets: bytes) -> None:
        if self.demarrage is None:
            self.tampon += octets
            if len(self.tampon) < len(self.attendu):
                return
            debut = self.tampon[:len(self.attendu)]
            self.demarrage = hashlib.sha256(debut).digest() == hashlib.sha256(self.attendu).digest()
            _ajouter(self.sortie / cv.GARDES_LANCEUR, {
                "garde": "configuration effective", "etat": "passée" if self.demarrage else "tombée", "tour": -1,
                "empreinte_observee": hashlib.sha256(debut).hexdigest(),
                "empreinte_attendue": hashlib.sha256(self.attendu).hexdigest(), "k_attendu": self.k_attendu})
            octets, self.tampon = self.tampon[len(self.attendu):], b""
        self.ligne += octets
        *completes, self.ligne = self.ligne.split(b"\n")
        for brute in completes:
            self._ligne(brute)

    def finir(self) -> None:
        if self.ligne:
            self._ligne(self.ligne)
            self.ligne = b""

    def _ligne(self, brute: bytes) -> None:
        m = MARK.match(brute.decode("utf-8", errors="replace"))
        if m:
            e, d = int(m.group(1)), float(m.group(2))
            self.durees[e] = d
            _ajouter(self.sortie / cv.SORTIE_DUREES, {"tour": e, "duree_s": d, "t": time.time()})


def parametres_phase(manifeste: dict, phase: str) -> tuple[int, int]:
    """K et graine lus au manifeste (B-8) : pilote → 3 tours, graine « pilote » ; run principal → K de la règle,
    graine « run principal »."""
    if phase not in PHASES:
        raise GardeArret("phase inconnue")
    if PHASES[phase] == "pilote":
        return 3, int(manifeste["graines"]["pilote"])
    if "K" not in manifeste.get("regle_tours", {}):
        raise GardeArret("garde « configuration effective » tombée : K absent du manifeste")
    return int(manifeste["regle_tours"]["K"]), int(manifeste["graines"]["principal"])


def garde_k_configuration(attendu: str, manifeste: dict, phase: str) -> str:
    """Le nombre de tours et la graine du texte attendu sont ceux du manifeste pour la phase, et la graine celle du
    texte scellé."""
    from omegaconf import OmegaConf
    cfg = OmegaConf.create(attendu)
    k, graine = parametres_phase(manifeste, phase)
    attendue = an.GRAINE_PILOTE if PHASES[phase] == "pilote" else an.GRAINE_PRINCIPAL
    if int(cfg.experiment.attack_defense_epochs) != k or int(cfg.experiment.seed) != graine or graine != attendue:
        raise GardeArret("garde « configuration effective » tombée : nombre de tours ou graine différents du manifeste")
    return "passée"


def _empreinter_nouveaux(dossiers: list[Path], tailles: dict, vus: dict, journal: Path, final: bool) -> None:
    """Un fichier est empreinté quand sa taille est stable entre deux passages (A-10), ou à la fin du processus."""
    for d in dossiers:
        if not d.exists():
            continue
        for f in sorted(d.rglob("*")):
            if not f.is_file() or str(f) in vus:
                continue
            taille = f.stat().st_size
            if final or tailles.get(str(f)) == taille:
                vus[str(f)] = cv.sha_fichier(f)
                _ajouter(journal, {"fichier": str(f.relative_to(d.parent)), "sha256": vus[str(f)], "t": time.time()})
            tailles[str(f)] = taille


def executer(manifeste: dict, clone: Path, travail: Path, phase: str, depense: dict, echeance_go: float,
             commande=None, intervalle: float = 5.0, marge_transfert_s: float = MARGE_TRANSFERT_S) -> dict:
    """Une exécution. `travail` doit être neuf. Arrête l'enfant par son PID (R10) si la garde de démarrage tombe, si la
    dépense atteint B − 2, ou à `échéance du GO − marge_transfert_s` (correction 5) ; le run est alors tronqué, ses
    journaux restent pour le transfert. Ne lit aucune note."""
    if echeance_go is None:
        raise GardeArret("échéance du GO exigée")
    from .lecture_v8 import gardes_tombees, tours_complets_instance
    from .journaliseur_v3 import depense_courante
    if travail.exists() and any(travail.iterdir()):
        raise GardeArret("garde « dossier neuf » tombée")
    travail.mkdir(parents=True, exist_ok=True)
    for rel in (cv.GARDES_LANCEUR, cv.SORTIE_DUREES, cv.EMPREINTES_FICHIERS):
        (travail / rel).touch()
    k, graine = parametres_phase(manifeste, phase)
    params, sondes, hydra_d = travail / "params", travail / "sondes", travail / "hydra"
    over = surcharges(k, graine, manifeste["chemin_modele"], str(sondes), str(params), str(hydra_d))
    attendu = configuration_attendue(clone, over)
    garde_k_configuration(attendu, manifeste, phase)
    _ecrire_json(travail / "config-journal-v3.json", {
        "dossier_journal": str(travail / "journal"), "dossier_params": str(params),
        "dossier_jeu": str(clone / cv.SOUS_DOSSIER / cv.DOSSIER_JEU), "pas_attendus": int(manifeste["pas_par_tour"]),
        "juge": manifeste["juge"], "depense": depense, "cache_hf": manifeste["cache_hf"], "execution": phase})
    env = dict(os.environ)  # TESTING n'est pas retirée : si elle est là, l'enfant s'arrête (garde du juge)
    env["TEMOIN_BAILEY_CONFIG"] = str(travail / "config-journal-v3.json")
    env["PYTHONUNBUFFERED"] = "1"
    cmd = commande or [sys.executable, "-m", "controle_ia.temoin_bailey.execution_v3", "--clone", str(clone),
                       "--graine", str(graine), "--", *over]
    surv = Surveillance(attendu, k, travail)
    vus, tailles = {}, {}
    brute = open(travail / "sortie-standard-instance.log", "wb")    # reste sur l'instance
    erreurs = open(travail / "sortie-erreur-instance.log", "wb")    # reste sur l'instance (B-2)
    proc = subprocess.Popen(cmd, stdout=subprocess.PIPE, stderr=erreurs, env=env)
    os.set_blocking(proc.stdout.fileno(), False)
    cause, dernier = None, 0.0
    arret_echeance = float(echeance_go) - float(marge_transfert_s)
    while True:
        try:
            morceau = proc.stdout.read()
        except BlockingIOError:
            morceau = None
        if morceau:
            brute.write(morceau)
            brute.flush()
            surv.recevoir(morceau)
            if surv.demarrage is False and cause is None:
                cause = "garde de démarrage"
        fini = proc.poll() is not None
        if time.time() - dernier >= intervalle or fini:
            dernier = time.time()
            _empreinter_nouveaux([params, sondes], tailles, vus, travail / cv.EMPREINTES_FICHIERS, False)
            if cause is None and depense_courante(depense) >= float(depense["b"]) - 2:
                cause = "dépense"
            if cause is None and time.time() >= arret_echeance:
                cause = "échéance du GO"
        if cause and not fini:
            os.kill(proc.pid, signal.SIGTERM)  # R10 : par PID
            try:
                proc.wait(timeout=60)
            except subprocess.TimeoutExpired:
                os.kill(proc.pid, signal.SIGKILL)
                proc.wait()
            fini = True
        if fini:
            reste = proc.stdout.read() or b""
            if reste:
                brute.write(reste)
                surv.recevoir(reste)
            surv.finir()
            break
        time.sleep(0.2)
    brute.close()
    erreurs.close()
    _empreinter_nouveaux([params, sondes], tailles, vus, travail / cv.EMPREINTES_FICHIERS, True)
    # v13 : la liste s'appelait `signal` et masquait le module `signal` dans toute la fonction : l'arrêt par PID
    # (`signal.SIGTERM` plus haut) levait `UnboundLocalError` (défaut de la v12, trouvé par l'essai v14).
    signaux: list[str] = []  # v7 (C-4) : propre à cette exécution
    complets, absence = tours_complets_instance(travail, signaux)
    tombees = gardes_tombees(travail, signaux)
    # v14 (R-2) : rien d'étranger à la configuration, et l'enfant est mort de lui-même (aucune cause d'arrêt décidée
    # par l'instance : garde de démarrage, dépense, échéance)
    mort_seule = surv.attendu.startswith(surv.tampon) and cause is None  # v15 (D-5)
    erreur_ecrite = ecrire_erreur_demarrage(travail, proc.returncode, surv.demarrage, complets, mort_seule)  # v13 à v15
    res = {"phase": phase, "k": k, "graine": graine, "code_retour": proc.returncode, "cause_arret": cause,
           "configuration_effective": {None: "non décidée", True: "passée", False: "tombée"}[surv.demarrage],
           "durees": {str(e): d for e, d in sorted(surv.durees.items())}, "tours_marques": len(surv.durees),
           "gardes_tombees": tombees, "tours_complets": complets, "journal_absent": absence,
           "lignes_tronquees_ignorees": signaux, "erreur_demarrage": erreur_ecrite}
    _ecrire_json(travail / cv.ETAT_EXECUTION, res)
    return res


# --- règle du nombre de tours, empreintes -----------------------------------------------------------------------------

def t_du_pilote(durees: dict) -> float:
    if "0" not in durees or "1" not in durees:
        raise GardeArret("garde « pilote » tombée : tours 0 et 1 du pilote non finis")
    return (float(durees["0"]) + float(durees["1"])) / 2


def regle_tours(b, d, c, durees_pilote: dict) -> dict:
    t = t_du_pilote(durees_pilote)
    r = an.nombre_de_tours(b, d, c, t)
    return {"B": b, "R": 10, "D": d, "c": c, "t": t, **r}


def empreintes(travail: Path, si_absent: bool = False) -> dict:
    """Journaux et fichiers d'état présents dans le dossier de l'étape (correction 11). v10 : `si_absent`, les
    empreintes déjà écrites (avant l'arrêt autonome) sont gardées et rendues telles quelles (reprise)."""
    if si_absent and (travail / cv.EMPREINTES_INSTANCE).is_file():
        return json.loads((travail / cv.EMPREINTES_INSTANCE).read_text(encoding="utf-8"))
    res = {rel: cv.sha_fichier(travail / rel) for rel in SORTANTS if (travail / rel).is_file()}  # v13
    _ecrire_json(travail / cv.EMPREINTES_INSTANCE, res)
    return res


def reconstituer_etat(travail: Path, manifeste: dict, phase: str, cause: str) -> dict:
    """C8 (N-1) : écrit `etat-execution-v3.json` d'une exécution qui n'en a pas (morte sur l'instance, ou arrêtée par
    la conduite), **sans jamais écraser** un état présent ; ne lit aucune note. Rend, pour la ligne `ETAT`, les tours
    complets, les gardes tombées, la cause d'un journal absent, et `etat_execution` : « reconstitué » ou « déjà
    présent ». L'état reconstitué porte `reconstitue: true`, `code_retour` 1 (non nul), `cause_arret` = `cause`,
    `tours_complets`, `gardes_tombees`, `durees` (lues à `sortie-durees-v3.jsonl`), `tours_marques`, et le K et la
    graine de la phase lus au manifeste. v7 (C-2, C-4) : les lignes coupées ignorées (liste propre à cet appel) sont
    écrites dans l'état (`lignes_tronquees_ignorees`) et rendues pour la ligne `ETAT`."""
    from .lecture_v8 import gardes_tombees, lire_jsonl, tours_complets_instance
    if cause not in CAUSES_RECONSTITUEES:
        raise GardeArret(f"état reconstitué : cause hors de la liste fermée ({cause})")
    k, graine = parametres_phase(manifeste, phase)
    travail.mkdir(parents=True, exist_ok=True)
    signaux: list[str] = []  # v14 (R-5) : ne masque plus le module `signal`
    complets, absence = tours_complets_instance(travail, signaux)
    tombees = gardes_tombees(travail, signaux)
    res = {"tours_complets": complets, "journal_absent": absence, "gardes_tombees": tombees,
           "lignes_tronquees_ignorees": signaux}
    chemin = travail / cv.ETAT_EXECUTION
    if chemin.exists():
        return {**res, "etat_execution": "déjà présent"}
    try:
        durees = {str(int(x["tour"])): float(x["duree_s"]) for x in lire_jsonl(travail / cv.SORTIE_DUREES, signaux)}
    except (GardeArret, KeyError, ValueError, TypeError):
        durees = {}
    etat_ = {"phase": phase, "k": k, "graine": graine, "code_retour": 1, "cause_arret": cause, "reconstitue": True,
             "configuration_effective": "non décidée", "durees": dict(sorted(durees.items(), key=lambda x: int(x[0]))),
             "tours_marques": len(durees), "gardes_tombees": tombees, "tours_complets": complets,
             "journal_absent": absence, "lignes_tronquees_ignorees": signaux,
             "message": f"état reconstitué après l'arrêt de l'exécution sans état ({cause})"}
    if chemin.exists():  # jamais d'écrasement (relu juste avant l'écriture)
        return {**res, "etat_execution": "déjà présent"}
    _ecrire_json(chemin, etat_)
    return {**res, "etat_execution": "reconstitué"}


# --- v10 : arrêt autonome de l'instance --------------------------------------------------------------------------------

def _boot_id() -> str:
    try:
        return Path("/proc/sys/kernel/random/boot_id").read_text().strip()
    except OSError:
        return ""


def identite_pid(pid: int) -> str | None:
    """Identité d'un PID, comme `lanceur_v12._identite` (N-4) : « <boot_id> <heure de départ> » (champ 22 de
    `/proc/<pid>/stat`) ; `None` si le processus n'existe pas."""
    try:
        champs = Path(f"/proc/{int(pid)}/stat").read_text().rsplit(")", 1)[1].split()
    except (OSError, IndexError, ValueError):
        return None
    return f"{_boot_id()} {champs[19]}"


def _zombie(pid: int) -> bool:
    try:
        for ligne in Path(f"/proc/{int(pid)}/status").read_text().splitlines():
            if ligne.startswith("State:"):
                return "Z" in ligne.split()[1]
    except OSError:
        pass
    return False


def pid_vivant(etats: Path, nom: str) -> int | None:
    """PID de la commande détachée `nom` s'il vit, n'est pas un zombie et a l'identité écrite à son lancement
    (`<nom>.debut`) ; sinon `None` (même test que `lanceur_v12._pid_vit`)."""
    try:
        pid = int((Path(etats) / f"{nom}.pid").read_text().strip())
        debut = (Path(etats) / f"{nom}.debut").read_text().strip()
    except (OSError, ValueError):
        return None
    if not debut or _zombie(pid) or identite_pid(pid) != debut:
        return None
    return pid


def commandes_en_cours(etats: Path) -> list[str]:
    """Commandes détachées vivantes sans `.fin` (chien de garde et minuterie exceptés)."""
    out = []
    for f in sorted(Path(etats).glob("*.pid")):
        nom = f.name[:-len(".pid")]
        if nom in (CHIEN, MINUTERIE) or (Path(etats) / f"{nom}.fin").exists():
            continue
        if pid_vivant(etats, nom) is not None:
            out.append(nom)
    return out


def arreter_groupe(etats: Path, nom: str, attente_s: float = 10.0, attendre=time.sleep) -> None:
    """R10 : comme `lanceur_v12.commande_arret` : le groupe de la commande est visé par son PID, seulement si son
    meneur a l'identité écrite au lancement ou n'existe plus ; TERM, attente bornée, puis KILL. Jamais par motif."""
    try:
        pid = int((Path(etats) / f"{nom}.pid").read_text().strip())
        debut = (Path(etats) / f"{nom}.debut").read_text().strip()
    except (OSError, ValueError):
        return
    if Path(f"/proc/{pid}").exists() and identite_pid(pid) != debut:
        return  # PID réemployé : jamais signalé
    try:
        os.killpg(pid, signal.SIGTERM)
    except (ProcessLookupError, PermissionError):
        return
    for _ in range(max(1, int(attente_s / 0.5))):
        try:
            os.killpg(pid, 0)
        except (ProcessLookupError, PermissionError):
            return
        attendre(0.5)
    try:
        os.killpg(pid, signal.SIGKILL)
    except (ProcessLookupError, PermissionError):
        pass


def lire_environ(chemin: str = "/proc/1/environ") -> dict:
    """`CONTAINER_ID` et `CONTAINER_API_KEY` lus dans l'environnement du processus principal du conteneur (une
    session `ssh` peut ne pas les avoir, documentation de Vast.ai), à défaut dans celui de ce processus. Rien d'autre
    n'est gardé ; la clé n'est jamais imprimée ni écrite."""
    vus = {}
    try:
        for morceau in Path(chemin).read_bytes().split(b"\0"):
            cle, _, valeur = morceau.partition(b"=")
            if cle in (b"CONTAINER_ID", b"CONTAINER_API_KEY"):
                vus[cle.decode()] = valeur.decode("utf-8", errors="replace")
    except OSError:
        pass
    for cle in ("CONTAINER_ID", "CONTAINER_API_KEY"):
        if not vus.get(cle) and os.environ.get(cle):
            vus[cle] = os.environ[cle]
    return vus


def requete_etat_instance(etat_vise: str, environ: str = "/proc/1/environ", url: str | None = None,
                          ouvrir=None, attendre=time.sleep) -> dict:
    """`PUT <url>/api/v0/instances/<CONTAINER_ID>/` avec `{"state": etat_vise}` et la clé restreinte de l'instance
    (même appel que `vastai stop|start instance`, paquet 1.11.0). Lève `GardeArret` (message sans clé) si une variable
    manque ou si la réponse n'est pas un succès. v11 (P-4) : en-tête `User-Agent` du paquet (`USER_AGENT_VAST`) ;
    l'appel est refait, comme le paquet (`VastClient._request`), sur 429, 502, 503, 504 et sur une erreur de transport,
    `ESSAIS_REQUETE` essais au plus, attente `Retry-After` (au plus `RETRY_AFTER_MAX_S`) ou 0,15 s × 1,5ⁿ."""
    import urllib.error
    import urllib.request
    if etat_vise not in ("stopped", "running"):
        raise GardeArret("auto-arrêt : état visé hors de la liste")
    v = lire_environ(environ)
    if not v.get("CONTAINER_ID") or not v.get("CONTAINER_API_KEY"):
        raise GardeArret("auto-arrêt : CONTAINER_ID ou CONTAINER_API_KEY absent de l'environnement du conteneur")
    base = (url or os.environ.get("VAST_URL") or URL_VAST).rstrip("/")
    ouvrir = ouvrir or (lambda r: urllib.request.urlopen(r, timeout=30))
    pause = 0.15
    for n in range(ESSAIS_REQUETE):
        req = urllib.request.Request(f"{base}/api/v0/instances/{v['CONTAINER_ID']}/", method="PUT",
                                     data=json.dumps({"state": etat_vise}).encode("utf-8"),
                                     headers={"Authorization": "Bearer " + v["CONTAINER_API_KEY"],
                                              "Content-Type": "application/json", "User-Agent": USER_AGENT_VAST})
        dernier = n == ESSAIS_REQUETE - 1
        try:
            with ouvrir(req) as rep:
                corps = json.loads(rep.read().decode("utf-8") or "{}")
            break
        except urllib.error.HTTPError as err:  # jamais le texte de la requête (en-tête) dans le message
            if err.code in CODES_A_REFAIRE and not dernier:
                try:
                    attente = float(err.headers.get("Retry-After"))
                except (TypeError, ValueError, AttributeError):
                    attente = pause
                if attente <= RETRY_AFTER_MAX_S:
                    attendre(max(0.0, attente))
                    pause *= 1.5
                    continue
            raise GardeArret(f"auto-arrêt : appel à l'API refusé (HTTPError {int(err.code)})") from None
        except (urllib.error.URLError, TimeoutError, ConnectionError) as err:
            if not dernier:
                attendre(pause)
                pause *= 1.5
                continue
            raise GardeArret(f"auto-arrêt : appel à l'API impossible ({type(err).__name__})") from None
        except Exception as err:
            raise GardeArret(f"auto-arrêt : appel à l'API refusé ou impossible ({type(err).__name__})") from None
    if not isinstance(corps, dict) or corps.get("success") is not True:
        raise GardeArret("auto-arrêt : réponse de l'API sans succès")
    return {"instance": v["CONTAINER_ID"], "etat_vise": etat_vise}


def verifier_auto_arret(instance: str, etats: Path, environ: str = "/proc/1/environ", url: str | None = None,
                        ouvrir=None, fraicheur_s: float = 3 * PERIODE_CHIEN_S, delai_s: float = 20.0,
                        horloge=time.time, attendre=time.sleep) -> dict:
    """Vérifications faites avant la mise en place (ce qui n'est pas établi hors de l'instance) : variables
    présentes ; `CONTAINER_ID` égal à l'identifiant de la création ; clé acceptée (essai sans effet
    `{"state": "running"}`) ; chien de garde vivant (PID à son identité, battement de moins de `fraicheur_s`).
    Rend `{"disponible": bool, "verifications": {…}, "cause": …}` ; aucune clé dans le résultat."""
    ver: dict = {}
    v = lire_environ(environ)
    ver["variables"] = bool(v.get("CONTAINER_ID")) and bool(v.get("CONTAINER_API_KEY"))
    ver["identifiant"] = ver["variables"] and str(v.get("CONTAINER_ID")).strip() == str(instance).strip()
    try:
        requete_etat_instance("running", environ, url, ouvrir) if ver["identifiant"] else None
        ver["api"] = bool(ver["identifiant"])
    except GardeArret:
        ver["api"] = False
    fin = horloge() + float(delai_s)
    while True:
        vivant = pid_vivant(etats, CHIEN) is not None
        try:
            t = float(json.loads((Path(etats) / f"{CHIEN}.battement").read_text(encoding="utf-8"))["t"])
            frais = horloge() - t <= float(fraicheur_s)
        except (OSError, ValueError, KeyError, TypeError):
            frais = False
        if (vivant and frais) or horloge() >= fin:
            break
        attendre(0.5)
    ver["chien_de_garde"] = vivant and frais
    manque = [k for k in ("variables", "identifiant", "api", "chien_de_garde") if not ver[k]]
    return {"disponible": not manque, "verifications": ver,
            "cause": None if not manque else "auto-arrêt indisponible : " + ", ".join(manque)}


def fin_prevue(racine: Path) -> bool:
    """Fin de la dernière exécution prévue, lue sur l'instance seule : relance finie, ou run principal fini dont
    l'état ne permet pas de relance (`relance_permise`). Les autres fins (arrêt qui interdit la suite) sont dites par la
    conduite (marque `rapatrie`) ou tombent sous la conduite injoignable."""
    from .lecture_v8 import relance_permise
    etats = Path(racine) / "etats"
    if (etats / "principal-relance.fin").exists():
        return True
    if (etats / "principal.fin").exists():
        try:
            return not relance_permise(json.loads((Path(racine) / "x" / "principal" / cv.ETAT_EXECUTION)
                                                  .read_text(encoding="utf-8")))
        except Exception:
            return False
    return False


def decider(*, maintenant: float, depense: float, b: float, echeance_go: float, marge_transfert_s: float,
            age_battement: float, en_cours: list[str], fin: bool, rapatrie: bool, debut_cause: float | None,
            d_abandon_s: float = D_ABANDON_S, prise_en_charge_s: float = DELAI_PRISE_EN_CHARGE_S,
            marge_secours: float = MARGE_SECOURS_USD) -> tuple[str, str | None]:
    """Décision du chien de garde, sans effet : (« rien » | « attendre » | « arreter », cause). Causes, dans
    l'ordre : « dépense » (D ≥ B − 2), « échéance du GO » (échéance − marge de transfert), « fin », « conduite
    injoignable » (battement plus vieux que `d_abandon_s`).
    - Conduite vivante : arrêt si la marque `rapatrie` est posée, si D ≥ B − marge de secours, si l'échéance moins la
      moitié de la marge est atteinte, ou si une cause tient depuis `prise_en_charge_s` ; sinon rien (son transfert
      n'est jamais coupé avant ces bornes).
    - Conduite injoignable : sans autre cause, une exécution du run principal (ou de sa relance) en cours finit sous
      ses gardes (« attendre ») ; sinon arrêt aussitôt."""
    causes = []
    if depense >= float(b) - 2:
        causes.append("dépense")
    if maintenant >= float(echeance_go) - float(marge_transfert_s):
        causes.append("échéance du GO")
    if fin or rapatrie:
        causes.append("fin")
    premiere = causes[0] if causes else None
    if age_battement < float(d_abandon_s):
        if rapatrie:
            return "arreter", "fin"
        if depense >= float(b) - float(marge_secours):
            return "arreter", "dépense"
        if maintenant >= float(echeance_go) - float(marge_transfert_s) / 2:
            return "arreter", "échéance du GO"
        if premiere and debut_cause is not None and maintenant - debut_cause >= float(prise_en_charge_s):
            return "arreter", premiere
        return "rien", premiere
    if premiere is None and en_cours and set(en_cours) <= set(RUN_PRINCIPAL):
        return "attendre", "conduite injoignable"
    return "arreter", premiere or "conduite injoignable"


class ChienDeGarde:
    """Processus détaché sur l'instance (lancé par l'amorce), indépendant des exécutions. Voir la docstring du
    module. `minuterie_s` : mode de la reprise (instance redémarrée le temps du transfert) : arrêt du conteneur à
    `début + minuterie_s` ou à l'échéance du GO, sans autre condition ni procédure. `arreter_api`, `horloge`,
    `attendre`, `signaler_pid1` : substituts pour l'épreuve sur processeur."""

    def __init__(self, racine: Path, depense: dict | None, echeance_go: float, marge_transfert_s: float = MARGE_TRANSFERT_S,
                 d_abandon_s: float = D_ABANDON_S, prise_en_charge_s: float = DELAI_PRISE_EN_CHARGE_S,
                 marge_secours: float = MARGE_SECOURS_USD, grace_execution_s: float = GRACE_EXECUTION_S,
                 periode_s: float = PERIODE_CHIEN_S, minuterie_s: float | None = None, arreter_api=None,
                 horloge=time.time, attendre=time.sleep, signaler_pid1=None):
        self.racine = Path(racine)
        self.etats, self.x = self.racine / "etats", self.racine / "x"
        self.depense, self.echeance_go = depense, float(echeance_go)
        self.marge_transfert, self.d_abandon, self.prise = float(marge_transfert_s), float(d_abandon_s), float(
            prise_en_charge_s)
        self.marge_secours, self.grace, self.periode = float(marge_secours), float(grace_execution_s), float(periode_s)
        self.minuterie = None if minuterie_s is None else float(minuterie_s)
        self.nom = MINUTERIE if self.minuterie is not None else CHIEN
        self.arreter_api = arreter_api or (lambda: requete_etat_instance("stopped"))
        self.horloge, self.attendre = horloge, attendre
        self.signaler_pid1 = signaler_pid1 or (lambda: os.kill(1, signal.SIGTERM))
        self.debut = horloge()
        self.debut_cause: float | None = None
        self.cause: str | None = None  # cause de l'arrêt, une fois décidé (ne change plus)
        self.decide_a: float | None = None
        self.arretees: list[str] = []
        self.prepare = False
        self.essais_api = 0
        self.conteneur_arrete = False
        self.arret_demande_a = 0.0
        self.passages_depuis_decision = 0  # v11 (B-2)
        if self.minuterie is None:  # v11 (B-1) : dépense illisible : le chien ne démarre pas (garde d'auto-arrêt)
            from .journaliseur_v3 import depense_courante
            try:
                depense_courante(self.depense, self.debut)
                float(self.depense["b"])
            except Exception:
                raise GardeArret("chien de garde : dépense du poste illisible") from None
        self.survivantes: list[str] = []  # v11 (B-2) : commandes encore vivantes à l'échéance de l'attente bornée

    def _noter(self, objet: dict) -> None:
        try:
            self.etats.mkdir(parents=True, exist_ok=True)
            _ajouter(self.etats / JOURNAL_CHIEN, {**objet, "chien": self.nom, "t": self.horloge()})
        except OSError:
            pass

    def _battre(self) -> None:
        """v11 (B-1, P-1) : fichier réécrit ; s'il ne peut l'être (disque plein), sa date est touchée (`os.utime`,
        sans bloc nouveau) : la conduite lit la fraîcheur du chien à la date du fichier."""
        p = self.etats / f"{self.nom}.battement"
        try:
            self.etats.mkdir(parents=True, exist_ok=True)
            _ecrire_json(p, {"t": self.horloge(), "pid": os.getpid()})
        except OSError:
            try:
                os.utime(p)
            except OSError:
                pass

    def _age_battement(self, maintenant: float) -> float:
        try:
            return maintenant - (self.etats / BATTEMENT_CONDUITE).stat().st_mtime
        except OSError:
            return maintenant - self.debut  # pas encore de battement : compté depuis le lancement du chien

    def _decider(self, maintenant: float, fin: bool, rapatrie: bool, en_cours: list[str]) -> tuple[str, str | None]:
        """Décision sur les causes calculées en mémoire (dépense, échéance, âge du battement) et sur `fin`,
        `rapatrie`, `en_cours` déjà lus. v12 (V-3) : partagée par `observer` et par le repli de `passage`."""
        from .journaliseur_v3 import depense_courante
        if self.minuterie is not None:
            if maintenant >= self.debut + self.minuterie:
                return "arreter", "minuterie"
            if maintenant >= self.echeance_go:
                return "arreter", "échéance du GO"
            return "rien", None
        d = depense_courante(self.depense, maintenant)
        tient = d >= float(self.depense["b"]) - 2 or maintenant >= self.echeance_go - self.marge_transfert or fin \
            or rapatrie
        if tient and self.debut_cause is None:
            self.debut_cause = maintenant
        return decider(maintenant=maintenant, depense=d, b=float(self.depense["b"]), echeance_go=self.echeance_go,
                       marge_transfert_s=self.marge_transfert, age_battement=self._age_battement(maintenant),
                       en_cours=en_cours, fin=fin, rapatrie=rapatrie,
                       debut_cause=self.debut_cause, d_abandon_s=self.d_abandon, prise_en_charge_s=self.prise,
                       marge_secours=self.marge_secours)

    def observer(self) -> tuple[str, str | None]:
        maintenant = self.horloge()
        if self.minuterie is not None:
            return self._decider(maintenant, False, False, [])
        try:  # v11 (B-1) : une erreur de lecture ne lève pas ; lecture prudente, erreur notée
            rapatrie = (self.etats / MARQUE_RAPATRIE).exists()
        except OSError as err:
            rapatrie = False
            self._noter({"observation": "marque illisible", "erreur": type(err).__name__})
        try:  # v12 (V-3) : `fin_prevue` peut lever (EIO, import) : lue prudemment (fausse), erreur notée
            fin = bool(fin_prevue(self.racine))
        except Exception as err:
            fin = False
            self._noter({"observation": "fin prévue illisible", "erreur": type(err).__name__})
        try:
            en_cours = commandes_en_cours(self.etats)
        except Exception as err:
            en_cours = []
            self._noter({"observation": "commandes en cours illisibles", "erreur": type(err).__name__})
        return self._decider(maintenant, fin, rapatrie, en_cours)

    def observer_minimal(self) -> tuple[str, str | None]:
        """v12 (V-3) : repli quand `observer` lève : décision sur la dépense, l'échéance et le battement seuls, sans
        aucune lecture de fichier hors de la date du battement (`_age_battement`, prudente) ; `fin=False`,
        `rapatrie=False`, `en_cours=[]` (lecture prudente : aucune commande en cours)."""
        return self._decider(self.horloge(), False, False, [])

    def _arreter_commandes(self) -> bool:
        """Arrête par PID les commandes en cours ; une exécution sous la cause dépense ou échéance a `grace` pour
        s'arrêter elle-même (elle écrit alors son propre état). Rend vrai quand plus aucune ne vit. v11 (B-2) : une
        erreur (lecture, signal refusé) est notée et compte comme une commande non finie ; chaque commande n'est
        inscrite qu'une fois dans `arretees`."""
        try:
            restantes = commandes_en_cours(self.etats)
        except Exception as err:
            self._noter({"commandes_en_cours": "illisibles", "erreur": type(err).__name__})
            return False
        for nom in restantes:
            if nom in EXECUTIONS and self.cause in ("dépense", "échéance du GO") \
                    and self.horloge() - self.decide_a < self.grace:
                continue
            try:
                arreter_groupe(self.etats, nom)
            except Exception as err:
                self._noter({"arret_par_pid": nom, "erreur": type(err).__name__})
            if nom not in self.arretees:
                self.arretees.append(nom)
            self._noter({"arret_par_pid": nom, "cause": self.cause})
        try:
            self.survivantes = commandes_en_cours(self.etats)
        except Exception as err:
            self._noter({"commandes_en_cours": "illisibles", "erreur": type(err).__name__})
            return False
        return not self.survivantes

    def _attente_echue(self) -> bool:
        """v11 (B-2) : attente de la fin des commandes échue (2 × grâce depuis la décision, ou assez de passages)."""
        return self.horloge() - self.decide_a >= ATTENTE_COMMANDES_MAX_S \
            or self.passages_depuis_decision >= PASSAGES_ATTENTE_MAX

    def _preparer(self) -> None:
        """États reconstitués (jamais d'écrasement), puis empreintes de chaque étape présente, puis état de l'arrêt.
        v11 (B-1) : ne lève jamais ; chaque écriture est sous `try`, son erreur notée ; `prepare` est posé quoi qu'il
        arrive (un disque plein n'empêche jamais l'appel d'arrêt)."""
        faites: list[str] = []
        try:
            from .lecture_v8 import ETAPES, MANIFESTES
            manifestes = {"pilote": "mise-en-place", "pilote-reprise": "mise-en-place", "principal": "regle",
                          "principal-relance": "relance"}
            for phase in EXECUTIONS:
                try:
                    d = self.x / phase
                    if not d.is_dir() or (d / cv.ETAT_EXECUTION).exists():
                        continue
                    cause = CAUSE_RECONSTITUEE[self.cause] if phase in self.arretees else "coupure de l'hôte"
                    man = lire_manifeste(self.racine / MANIFESTES[manifestes[phase]])
                    r = reconstituer_etat(d, man, phase, cause)
                    self._noter({"etat_reconstitue": phase, "cause": cause, "etat_execution": r["etat_execution"]})
                except Exception as err:
                    self._noter({"etat_reconstitue": phase, "erreur": type(err).__name__,
                                 "survivante": phase in self.survivantes})
            for etape in ETAPES:
                try:
                    if (self.x / etape).is_dir():
                        empreintes(self.x / etape)
                        faites.append(etape)
                except Exception as err:
                    self._noter({"empreintes": etape, "erreur": type(err).__name__})
            try:
                _ecrire_json(self.etats / ETAT_ARRET, {"cause": self.cause, "t": self.horloge(),
                                                       "arretees": self.arretees, "empreintes": faites,
                                                       "survivantes": self.survivantes, "chien": self.nom})
            except Exception as err:
                self._noter({"etat_arret": "non écrit", "erreur": type(err).__name__})
        except Exception as err:  # jamais de sortie : l'arrêt du conteneur suit
            self._noter({"preparation": "en échec", "erreur": type(err).__name__})
        finally:
            self.prepare = True

    def _arreter_conteneur(self) -> None:
        try:
            self.arreter_api()
            self.conteneur_arrete = True
            self._noter({"conteneur": "arrêt demandé à l'API", "cause": self.cause})
            return
        except Exception as err:
            self.essais_api += 1
            self._noter({"conteneur": "arrêt refusé", "essai": self.essais_api, "erreur": str(err)[:200]})
        if self.essais_api >= ESSAIS_API_AVANT_PID1:  # repli déclaré, journalisé ; effet non établi
            self._noter({"conteneur": "signal TERM au PID 1 (repli déclaré)"})
            try:
                self.signaler_pid1()
            except Exception as err:
                self._noter({"conteneur": "signal au PID 1 refusé", "erreur": type(err).__name__})

    def passage(self) -> str | None:
        """Un passage. Rend la cause une fois l'arrêt du conteneur demandé avec succès, sinon `None`. v11 (B-1, B-2) :
        après la décision, ni une commande qu'on ne peut tuer (au-delà de l'attente bornée), ni une erreur de la
        préparation n'empêchent l'appel d'arrêt."""
        self._battre()
        if self.cause is None:
            try:
                action, cause = self.observer()
            except Exception as err:  # v12 (V-3) : notée ; décision quand même sur les causes calculées en mémoire
                self._noter({"observation": "en échec", "erreur": f"{type(err).__name__}",
                             "suite": "décision sur la dépense, l'échéance et le battement seuls"})
                try:
                    action, cause = self.observer_minimal()
                except Exception as err2:  # dépense validée au démarrage : ne devrait jamais lever ; notée
                    self._noter({"observation_minimale": "en échec", "erreur": f"{type(err2).__name__}"})
                    return None
            if action != "arreter":
                return None
            self.cause, self.decide_a = cause, self.horloge()
            self._noter({"decision": "arrêt", "cause": cause})
        else:
            self.passages_depuis_decision += 1
        if self.minuterie is None and not self.prepare:
            if not self._arreter_commandes():
                if not self._attente_echue():
                    return None
                self._noter({"commandes_survivantes": self.survivantes, "attente_bornee": "échue",
                             "suite": "arrêt du conteneur quand même"})
            self._preparer()
        if self.conteneur_arrete and self.horloge() - self.arret_demande_a >= RENOUVELER_ARRET_S:
            self.essais_api += 1  # toujours en marche longtemps après l'arrêt demandé : demande renouvelée
            self.conteneur_arrete = False
            self._noter({"conteneur": "toujours en marche après l'arrêt demandé", "essai": self.essais_api})
        if not self.conteneur_arrete:
            self._arreter_conteneur()
            if self.conteneur_arrete:
                self.arret_demande_a = self.horloge()
        return self.cause if self.conteneur_arrete else None

    def boucle(self, passages: int | None = None) -> str | None:
        """Jamais de sortie sur une erreur ; après l'arrêt demandé, le processus attend la fin du conteneur (les
        appels refusés sont retentés à chaque passage)."""
        n = 0
        while passages is None or n < passages:
            n += 1
            try:
                if self.passage() is not None and passages is not None:
                    return self.cause
            except Exception as err:
                self._noter({"erreur": f"{type(err).__name__}: {err}"[:300]})
            self.attendre(self.periode)
        return self.cause if self.conteneur_arrete else None


def _main_v12(p, a) -> int:
    etats = Path(a.racine) / "etats"
    if a.commande == "en-cours":
        etat({"commande": "en-cours", "en_cours": commandes_en_cours(etats)})
        return 0
    if a.commande == "auto-arret":
        if not a.instance:
            p.error("auto-arret : --instance requis")
        r = verifier_auto_arret(a.instance, etats, a.environ)
        etat({"commande": "auto-arret", **r})
        return 0 if r["disponible"] else 3
    if a.echeance_go is None or (a.minuterie is None and a.depense is None):
        p.error("chien-de-garde : --echeance-go, et --depense hors minuterie, requis")
    environ = a.environ
    chien = ChienDeGarde(Path(a.racine), None if a.depense is None else json.loads(a.depense), a.echeance_go,
                         a.marge_transfert, a.d_abandon, a.prise_en_charge, a.marge_secours,
                         periode_s=a.periode, minuterie_s=a.minuterie,
                         arreter_api=lambda: requete_etat_instance("stopped", environ))
    chien.boucle()
    return 0


def main(argv=None) -> int:
    p = argparse.ArgumentParser()
    p.add_argument("commande", choices=["mise-en-place", "controle-juge", "executer", "regle-tours", "empreintes",
                                        "tours", CHIEN, "auto-arret", "en-cours"])
    p.add_argument("--manifeste")
    p.add_argument("--clone")
    p.add_argument("--travail")  # requis sauf pour les sous-commandes de la v10
    # v10 et v11 : arrêt autonome
    p.add_argument("--si-absent", action="store_true")  # `empreintes` : garder celles prises avant l'arrêt
    p.add_argument("--racine", default=RACINE)
    p.add_argument("--instance")  # identifiant de la création (auto-arret)
    p.add_argument("--marge-secours", type=float, default=MARGE_SECOURS_USD)
    p.add_argument("--d-abandon", type=float, default=D_ABANDON_S)
    p.add_argument("--prise-en-charge", type=float, default=DELAI_PRISE_EN_CHARGE_S)
    p.add_argument("--periode", type=float, default=PERIODE_CHIEN_S)
    p.add_argument("--minuterie", type=float)  # mode de la reprise
    p.add_argument("--environ", default="/proc/1/environ")
    p.add_argument("--phase")  # défaut « pilote », sauf pour `tours --ecrire-etat`, qui l'exige
    p.add_argument("--ecrire-etat", action="store_true")  # C8 : `tours` écrit l'état absent, marqué « reconstitué »
    p.add_argument("--cause")  # C8 : cause de l'arrêt, dans `CAUSES_RECONSTITUEES`
    p.add_argument("--depense")  # JSON {"d_avant","c","creation","b"}
    p.add_argument("--echeance-go", type=float)
    p.add_argument("--marge-transfert", type=float, default=MARGE_TRANSFERT_S)
    p.add_argument("--mise-en-place")  # dossier de la mise en place (controle-juge, P-5)
    p.add_argument("--pilote")  # dossier de l'exécution du pilote qui fixe t (regle-tours)
    a = p.parse_args(argv)
    if a.commande in (CHIEN, "auto-arret", "en-cours"):
        return _main_v12(p, a)
    if a.travail is None:
        p.error("--travail requis")
    travail = Path(a.travail)
    if a.commande == "tours" and a.ecrire_etat and (a.phase is None or a.manifeste is None or a.cause is None):
        p.error("tours --ecrire-etat : --phase, --manifeste et --cause requis")
    if a.phase is None:
        a.phase = "pilote"
    if a.commande in ("mise-en-place", "controle-juge", "executer", "regle-tours") and a.depense is None:
        p.error("--depense requis")
    if a.commande in ("mise-en-place", "controle-juge", "executer") and a.echeance_go is None:
        p.error("--echeance-go requis")  # correction 16
    try:
        if a.commande == "empreintes":
            etat({"commande": "empreintes", "fichiers": sorted(empreintes(travail, a.si_absent))})
            return 0
        if a.commande == "tours" and a.ecrire_etat:  # C8 : état reconstitué, jamais d'écrasement ; aucune note lue
            r = reconstituer_etat(travail, lire_manifeste(a.manifeste), a.phase, a.cause)
            etat({"commande": "tours", **r})
            return 0
        if a.commande == "tours":  # C4 : exécution morte sans état ; aucune note lue
            from .lecture_v8 import gardes_tombees, tours_complets_instance
            signaux: list[str] = []  # v7 (C-4) : propre à cette commande ; v14 (R-5) : renommée
            complets, absence = tours_complets_instance(travail, signaux)
            tombees = gardes_tombees(travail, signaux)
            etat({"commande": "tours", "tours_complets": complets, "journal_absent": absence,
                  "gardes_tombees": tombees, "lignes_tronquees_ignorees": signaux})
            return 0
        man = lire_manifeste(a.manifeste)
        travail.mkdir(parents=True, exist_ok=True)
        dep = json.loads(a.depense)
        arret = a.echeance_go - a.marge_transfert if a.echeance_go is not None else None
        if a.commande == "mise-en-place":
            r = mise_en_place(man, Path(a.clone), travail, dep, arret)
            etat({"commande": a.commande, "gardes": r["gardes"], "longueur_suffixe": r["longueur_suffixe"],
                  "pas_par_tour": r["pas_par_tour"], "ecart_10": r["ecart_10"]})
        elif a.commande == "controle-juge":
            r = controle_juge(man, Path(a.clone), travail, dep, arret, Path(a.mise_en_place) / cv.ETAT_MISE_EN_PLACE)
            etat({"commande": a.commande, "etats": r["etats"], "garde_juge": r["garde_juge"]})
        elif a.commande == "executer":
            r = executer(man, Path(a.clone), travail, a.phase, dep, a.echeance_go, marge_transfert_s=a.marge_transfert)
            etat({"commande": a.commande, **{k: r[k] for k in ("phase", "k", "code_retour", "cause_arret",
                                                                 "configuration_effective", "durees", "tours_marques",
                                                                 "gardes_tombees", "tours_complets",
                                                                 "journal_absent", "lignes_tronquees_ignorees",
                                                                 "erreur_demarrage")}})  # v14
        elif a.commande == "regle-tours":
            d = float(dep["d_avant"]) + float(dep["c"]) * (time.time() - float(dep["creation"])) / 3600
            e = json.loads((Path(a.pilote) / cv.ETAT_EXECUTION).read_text())
            r = regle_tours(dep["b"], round(d, 4), dep["c"], e["durees"])
            _ecrire_json(travail / cv.ETAT_REGLE, r)
            try:  # C7 : K et la garde au même `ETAT`, une seule ligne
                an.garde_nombre_de_tours(r["K"])
            except GardeArret as err:
                etat({"commande": a.commande, **r, "garde_tombee": str(err)})
                return 3
            etat({"commande": a.commande, **r})
    except GardeArret as err:
        etat({"commande": a.commande, "garde_tombee": str(err)})
        return 3
    return 0


if __name__ == "__main__":
    sys.exit(main())
