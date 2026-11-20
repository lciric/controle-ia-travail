"""Graines (règle R9 ; préenregistrement v6, B8).

Une racine gelée, `numpy.random.SeedSequence(2026111902)`. Chaque tâche dérive sa graine d'une étiquette en clair : les quatre
premiers mots de 32 bits de l'empreinte SHA-256 de l'étiquette forment la clé de dérivation (`spawn_key`).

Couches disjointes (B8) : « etalonnage », « mecanique » (étape 4), « mecanique-reglages » (étape 6 bis), « audit » (étape 3),
« essai-de-forme », « essai » (essais du code), « decisif », « confirmation ». Les deux dernières ne se dérivent **jamais sans
autorisation** : un objet `Autorisation` qui nomme le préenregistrement scellé et l'erratum contre-lu qui inscrit le commit du
code, vérifiés sur disque par empreinte (liste d'arrêt, point 1). Aucune autorisation n'est construite dans ce travail ; l'essai
final (`test_heritage_etage_processeur_v1_zz_aucune_graine_decisive.py`) contrôle le journal du processus.
"""

import hashlib
import os

import numpy as np

from .constantes import RACINE_GRAINES

COUCHES = ("etalonnage", "mecanique", "mecanique-reglages", "audit", "essai-de-forme", "essai", "decisif", "confirmation")
COUCHES_DECISIVES = ("decisif", "confirmation")
ORDRE_DES_CHAMPS = ("couche", "famille", "proposeur", "dose", "taille", "force", "taux", "retrait", "repere", "bras", "jumelle",
                    "tirage", "lot", "source", "generation", "monde", "role", "essai", "tour")

# Journal du processus : chaque dérivation (couche, étiquette) ; chaque refus de dérivation décisive.
JOURNAL = []
REFUS = []


class GraineRefusee(RuntimeError):
    pass


def _exiger_numpy():
    morceaux = np.__version__.split(".")
    majeur, mineur = int(morceaux[0]), int("".join(c for c in morceaux[1] if c.isdigit()))
    if (majeur, mineur) < (1, 25):
        raise GraineRefusee(f"numpy {np.__version__} : au moins 1.25 exigé (R9)")


def _texte(v):
    if isinstance(v, bool):
        return "oui" if v else "non"
    if isinstance(v, float):
        return repr(v)
    return str(v)


def etiquette(**champs):
    """L'étiquette en clair d'une tâche : champs dans l'ordre gelé `ORDRE_DES_CHAMPS`, « nom=valeur » joints par « | ».
    Un champ inconnu ou une couche inconnue est refusé ; la couche est exigée."""
    inconnus = sorted(set(champs) - set(ORDRE_DES_CHAMPS))
    if inconnus:
        raise GraineRefusee(f"champs d'étiquette inconnus : {inconnus}")
    if champs.get("couche") not in COUCHES:
        raise GraineRefusee(f"couche inconnue ou absente : {champs.get('couche')!r}")
    for k, v in champs.items():
        t = _texte(v)
        if "|" in t or "=" in t:
            raise GraineRefusee(f"valeur d'étiquette interdite (| ou =) : {k}={t!r}")
    return "|".join(f"{k}={_texte(champs[k])}" for k in ORDRE_DES_CHAMPS if k in champs)


def couche_de(texte_etiquette):
    premier = texte_etiquette.split("|", 1)[0]
    if not premier.startswith("couche="):
        raise GraineRefusee(f"étiquette sans couche en tête : {texte_etiquette!r}")
    return premier[len("couche="):]


def cle_de_derivation(texte_etiquette):
    """Quatre premiers mots de 32 bits (gros-boutiste) de SHA-256(étiquette en UTF-8)."""
    h = hashlib.sha256(texte_etiquette.encode("utf-8")).digest()
    return tuple(int.from_bytes(h[4 * i: 4 * i + 4], "big") for i in range(4))


def _sha256_fichier(chemin):
    h = hashlib.sha256()
    with open(chemin, "rb") as f:
        for bloc in iter(lambda: f.read(1 << 20), b""):
            h.update(bloc)
    return h.hexdigest()


class Autorisation:
    """Autorisation de dériver une graine décisive : préenregistrement scellé et erratum contre-lu, chacun vérifié par
    empreinte sur disque et par son compagnon `.sha256`, l'erratum devant citer l'empreinte du préenregistrement. Jamais
    construite dans ce travail."""

    def __init__(self, preenregistrement, sha_preenregistrement, erratum, sha_erratum):
        for chemin, sha in ((preenregistrement, sha_preenregistrement), (erratum, sha_erratum)):
            if not os.path.isfile(chemin) or _sha256_fichier(chemin) != sha:
                raise GraineRefusee(f"autorisation refusée : {chemin} absent ou d'empreinte différente")
            compagnon = chemin + ".sha256"
            if not os.path.isfile(compagnon):
                raise GraineRefusee(f"autorisation refusée : {chemin} non scellé (compagnon absent)")
            with open(compagnon, encoding="ascii") as f:
                if (f.read().split() or [""])[0] != sha:
                    raise GraineRefusee(f"autorisation refusée : {chemin} non scellé (compagnon faux)")
        with open(erratum, encoding="utf-8") as f:
            if sha_preenregistrement not in f.read():
                raise GraineRefusee("autorisation refusée : l'erratum ne cite pas l'empreinte du préenregistrement")
        self.sha_preenregistrement, self.sha_erratum = sha_preenregistrement, sha_erratum


class Graines:
    """Fabrique de graines d'un run. `autorisation` n'est exigée que pour les couches décisives."""

    def __init__(self, racine=RACINE_GRAINES, autorisation=None):
        _exiger_numpy()
        if isinstance(racine, bool) or not isinstance(racine, int) or racine < 0:
            raise GraineRefusee(f"racine : entier ≥ 0 attendu (reçu {racine!r})")
        if autorisation is not None and not isinstance(autorisation, Autorisation):
            raise GraineRefusee("autorisation : objet Autorisation attendu")
        self.racine, self.autorisation = racine, autorisation
        self.etiquettes = []

    def sequence(self, texte_etiquette):
        couche = couche_de(texte_etiquette)
        if couche not in COUCHES:
            raise GraineRefusee(f"couche inconnue : {couche!r}")
        if couche in COUCHES_DECISIVES and self.autorisation is None:
            REFUS.append(texte_etiquette)
            raise GraineRefusee(f"graine de la couche « {couche} » refusée : aucune autorisation (préenregistrement scellé et "
                                "erratum contre-lu exigés ; liste d'arrêt, point 1)")
        JOURNAL.append((couche, texte_etiquette))
        self.etiquettes.append(texte_etiquette)
        return np.random.SeedSequence(self.racine, spawn_key=cle_de_derivation(texte_etiquette))

    def generateur(self, texte_etiquette):
        return np.random.Generator(np.random.PCG64(self.sequence(texte_etiquette)))

    def entier(self, texte_etiquette):
        """Un entier de 64 bits (pour `random.Random`, comme `boucle_fermee_v59.graine_de_tache` de l'organisme)."""
        return int(self.sequence(texte_etiquette).generate_state(1, dtype=np.uint64)[0])

    def g(self, **champs):
        return self.generateur(etiquette(**champs))

    def e(self, **champs):
        return self.entier(etiquette(**champs))


def verifier_graines_des_bras(etiquettes_par_bras):
    """Garde 20 (B9) : `etiquettes_par_bras` = {bras: {"monde": [...], "echantillonnage": [...]}}. Les étiquettes de monde sont
    les mêmes pour tous les bras ; les étiquettes d'échantillonnage sont disjointes entre bras ; sinon arrêt."""
    bras = sorted(etiquettes_par_bras)
    mondes = [tuple(etiquettes_par_bras[b]["monde"]) for b in bras]
    if any(m != mondes[0] for m in mondes):
        raise GraineRefusee("garde 20 : graines des mondes différentes entre bras : arrêt")
    vues = {}
    for b in bras:
        for e in etiquettes_par_bras[b]["echantillonnage"]:
            cle = cle_de_derivation(e)
            if cle in vues and vues[cle] != b:
                raise GraineRefusee(f"garde 20 : même graine d'échantillonnage dans les bras {vues[cle]} et {b} : arrêt")
            vues[cle] = b
    return True


def exiger_couches_disjointes(etiquettes_a, etiquettes_b):
    """Liste d'arrêt, point 8 : aucune graine commune à deux couches (étalonnage et tirages décisifs, par exemple)."""
    commun = {cle_de_derivation(e) for e in etiquettes_a} & {cle_de_derivation(e) for e in etiquettes_b}
    if commun:
        raise GraineRefusee(f"graine commune à deux couches ({len(commun)}) : lecture invalide (liste d'arrêt, point 8)")
    return True


def couches_derivees():
    return sorted({c for c, _ in JOURNAL})
