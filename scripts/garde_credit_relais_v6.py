#!/usr/bin/env python3
"""Garde de crédit d'un relais à solde illisible (Argon, Astra, Carbon) — version 6 (course d'affinage, lanceur v6).

Version 6 (R12 ; la v5, `6cf87869…`, reste en place) — contre-lecture de la v5 de la course d'affinage, constat 5 : un message
de quota qui porte aussi une limite de débit (« per minute », « rate limit », « requests per », « too many requests ») compte
comme soupçon dans la v5. La v6 garde cette lettre **par défaut** et la rend **réglable** : l'option
`--limite-de-debit-pas-soupcon`, posée avant `--`, fait ignorer une telle ligne (sans mot de crédit ni de facturation) pour le
soupçon. Le lanceur v6 la pose si et seulement si la déclaration des relais porte
`"compter_limite_de_debit_comme_soupcon": false` (choix de la mère ; vrai par défaut). Le reste est la v5, inchangé.

    python3 -I -B garde_credit_relais_v6.py DOSSIER ETIQUETTE [--limite-de-debit-pas-soupcon] -- COMMANDE ARGS…

Texte de la v5 :

Garde de crédit d'un relais à solde illisible (Argon, Astra, Carbon) — version 5 (course d'auto-conception, lanceur v1).

Version 5 (R12 ; la v4, `9673b0f6…`, reste en place) — contre-lecture de la v4 de la course d'affinage, constat 3 : le message
« You exceeded your current quota … billing details » **ne suffit pas seul** à arrêter la course (il peut venir d'une limite
d'usage ou de palier, et non d'un crédit épuisé). Une ligne qui porte ce message, et aucun motif de crédit non ambigu
(`insufficient funds`, `credit balance`, `402` en contexte HTTP, « crédits épuisés »…), écrit un **soupçon**
(`soupcon-credit-ETIQUETTE-N.json`, jamais le texte ni une clé) au lieu d'un arrêt ; **le deuxième soupçon du même relais**
écrit l'arrêt (`arret-credit-ETIQUETTE.json`), que le lanceur surveille. Le reste est la v4, inchangé.

Texte de la v4 :

Garde de crédit d'un relais à solde illisible (Argon, Astra, Carbon) — version 4 (course d'affinage, lanceur v4).

Version 4 (R12 ; la v3, `686546a6…`, reste en place) — contre-lecture de la v3, constat 4 : la sortie d'erreur n'est lue
que si le code de la commande est non nul ; une limite de débit (« 429 RESOURCE_EXHAUSTED … rate limit »), « 402 ms » ou
« billing » seul ne valent pas refus de crédit ; 402 n'est lu que dans un contexte HTTP ; « resource_exhausted » et « quota
exceeded » ne valent que sur la même ligne qu'un mot de crédit ou de facturation ; « crédits épuisés », « depleted »,
« prepay » reconnus. Les formes exactes des messages de chaque amont ne sont pas vérifiées (aucun réseau).

Texte de la v3 :

Décision de la mère R-3237, point (2) : pour les clés dont aucune session ne lit le solde (R-3222), départ permis sous
dispense écrite, **arrêt de la course au premier refus pour crédit**, coût compté au prix des fichiers (celui que la commande
du relais rend dans `cout_usd`). Cette enveloppe est mise par le lanceur v3 devant la commande déclarée du relais :

    python3 -I -B garde_credit_relais_v3.py DOSSIER_DES_ARRETS ETIQUETTE -- COMMANDE ARGS…

Elle passe l'entrée standard à la commande, renvoie sa sortie standard et sa sortie d'erreur **telles quelles** et son code ;
elle lit seulement la dernière ligne JSON de la sortie (contrat de la commande externe : `{"texte", "cout_usd", …}`). Si cette
ligne, ou la sortie d'erreur, porte un motif de refus pour crédit, elle écrit (une fois) `DOSSIER_DES_ARRETS/arret-credit-
ETIQUETTE.json` (motif, code ; jamais le texte ni une clé), que le lanceur surveille : il arrête alors l'orchestrateur par
son PID (signal SIGTERM, arrêt propre, manifestes écrits). Aucune valeur de clé n'est lue ; l'environnement est passé tel quel.

Bibliothèque standard seulement.
"""
from __future__ import annotations

import json
import os
import re
import subprocess
import sys

VERSION = "garde_credit_relais_v6"
MOTIFS_CREDIT = re.compile(r"(insufficient[_ ]?(funds|balance|credits?)|payment required|credit balance|out of credits?|"
                           r"credits? (are |is |have been )?(depleted|exhausted)|prepay(ment|ed)?\b[^\n]{0,40}(depleted|exhausted|empty|insufficient)|"
                           r"billing (hard |soft )?limit|"
                           r"(http|status|code|erreur|error)\D{0,6}402\b|"
                           r"cr[ée]dits? (insuffisants?|[ée]puis[ée]s?)|solde (insuffisant|[ée]puis[ée]))", re.I)
# Formes ambiguës : ne valent refus de crédit que sur la même ligne qu'un mot de crédit ou de facturation.
AMBIGUS = re.compile(r"(resource_exhausted|quota exceeded|insufficient[_ ]quota)", re.I)
MOTS_CREDIT = re.compile(r"(credit|crédit|billing|balance|prepay|funds|solde|facturation)", re.I)
# v5 (constat 3) : message de quota d'usage, ambigu ; soupçon seulement, arrêt au deuxième soupçon du même relais.
QUOTA_AMBIGU = re.compile(r"exceeded your current quota", re.I)
SOUPCONS_AVANT_ARRET = 2
LIMITE_DE_DEBIT = re.compile(r"(rate[ _-]?limit|per minute|par minute|requests per|too many requests)", re.I)


def derniere_ligne_json(texte: str):
    for ligne in reversed([l for l in texte.splitlines() if l.strip()]):
        try:
            o = json.loads(ligne)
        except ValueError:
            return None
        return o if isinstance(o, dict) else None
    return None


def motif_credit(sortie: str, erreur: str, code: int = 0) -> str | None:
    """Motif de refus pour crédit **non ambigu**, ou None. La sortie d'erreur n'est lue que si le code est non nul.
    v5 : une ligne qui porte le message de quota ambigu n'est jamais un motif de crédit à elle seule."""
    for ligne in _lignes(sortie, erreur, code):
        if LIMITE_DE_DEBIT.search(ligne) and not MOTS_CREDIT.search(ligne):
            continue
        m = MOTIFS_CREDIT.search(ligne)
        if m:
            return m.group(0)
        if QUOTA_AMBIGU.search(ligne):
            continue
        a = AMBIGUS.search(ligne)
        if a and MOTS_CREDIT.search(ligne):
            return a.group(0)
    return None


def soupcon_credit(sortie: str, erreur: str, code: int = 0, limite_de_debit_soupcon: bool = True) -> str | None:
    """v5 : le message de quota ambigu, sans motif de crédit non ambigu sur la même réponse. v6 : si
    `limite_de_debit_soupcon` est faux, une ligne qui porte une limite de débit sans mot de crédit n'est pas un soupçon."""
    if motif_credit(sortie, erreur, code):
        return None
    for ligne in _lignes(sortie, erreur, code):
        if not limite_de_debit_soupcon and LIMITE_DE_DEBIT.search(ligne) and not MOTS_CREDIT.search(ligne):
            continue
        q = QUOTA_AMBIGU.search(ligne)
        if q:
            return q.group(0)
    return None


def _lignes(sortie: str, erreur: str, code: int) -> list:
    o = derniere_ligne_json(sortie)
    morceaux = [erreur or ""] if code != 0 else []
    if o is not None:
        morceaux += [str(o.get(k) or "") for k in ("erreur", "motif", "statut", "code_http", "message")]
    return "\n".join(morceaux).splitlines()


def _nom(etiquette: str) -> str:
    return re.sub(r"[^a-z0-9-]", "-", etiquette.lower())


def ecrire_une_fois(chemin: str, objet: dict) -> bool:
    try:
        with open(chemin, "x", encoding="utf-8") as f:
            json.dump(objet, f)
        return True
    except FileExistsError:
        return False


def noter(dossier: str, etiquette: str, motif: str | None, soupcon: str | None, code: int) -> None:
    """Écrit l'arrêt (motif non ambigu, ou deuxième soupçon du même relais) ou un soupçon numéroté."""
    if not (motif or soupcon):
        return
    os.makedirs(dossier, exist_ok=True)
    arret = os.path.join(dossier, f"arret-credit-{_nom(etiquette)}.json")
    if motif:
        ecrire_une_fois(arret, {"version": VERSION, "relais": etiquette, "motif": motif, "code_commande": code})
        return
    for n in range(1, 1000):
        if ecrire_une_fois(os.path.join(dossier, f"soupcon-credit-{_nom(etiquette)}-{n}.json"),
                           {"version": VERSION, "relais": etiquette, "soupcon": soupcon, "code_commande": code, "rang": n}):
            break
    if n >= SOUPCONS_AVANT_ARRET:
        ecrire_une_fois(arret, {"version": VERSION, "relais": etiquette, "motif": f"{soupcon} (soupçon n° {n} du même relais)",
                                "code_commande": code})


def principal(argv: list) -> int:
    limite_soupcon = True
    if len(argv) >= 3 and argv[2] == "--limite-de-debit-pas-soupcon":
        limite_soupcon = False
        argv = argv[:2] + argv[3:]
    if len(argv) < 4 or argv[2] != "--":
        print(json.dumps({"texte": "", "cout_usd": 1e-06, "erreur": "garde de crédit : usage DOSSIER ETIQUETTE "
                                                                     "[--limite-de-debit-pas-soupcon] -- COMMANDE"}))
        return 2
    dossier, etiquette, commande = argv[0], argv[1], argv[3:]
    entree = sys.stdin.buffer.read()
    p = subprocess.run(commande, input=entree, capture_output=True)
    sortie, erreur = p.stdout.decode("utf-8", "replace"), p.stderr.decode("utf-8", "replace")
    sys.stdout.buffer.write(p.stdout)
    sys.stdout.flush()
    sys.stderr.buffer.write(p.stderr)
    sys.stderr.flush()
    noter(dossier, etiquette, motif_credit(sortie, erreur, p.returncode), soupcon_credit(sortie, erreur, p.returncode, limite_soupcon), p.returncode)
    return p.returncode


if __name__ == "__main__":
    raise SystemExit(principal(sys.argv[1:]))
