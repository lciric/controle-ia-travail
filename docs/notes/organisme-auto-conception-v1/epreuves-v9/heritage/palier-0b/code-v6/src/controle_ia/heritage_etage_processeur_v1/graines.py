"""Graines (règle R9 ; préenregistrement v6, B8).

Une racine gelée, `numpy.random.SeedSequence(2026111902)`. Chaque tâche dérive sa graine d'une étiquette en clair : les quatre
premiers mots de 32 bits de l'empreinte SHA-256 de l'étiquette forment la clé de dérivation (`spawn_key`).

Couches disjointes (B8) : « etalonnage », « mecanique » (étape 4), « mecanique-reglages » (étape 6 bis), « audit » (étape 3),
« essai-de-forme », « essai » (essais du code), « decisif », « confirmation ». Les deux dernières ne se dérivent **jamais sans
autorisation** (liste d'arrêt, point 1). L'essai final (`test_heritage_etage_processeur_v1_zz_aucune_graine_decisive.py`)
contrôle le journal du processus.

Code v5 (préenregistrement v11, B8, versions 7, 9 et 10 ; note D6 ; décisions de la mère R-4123 et R-4182, remarque 4 de
l'annexe H, « Version 9 », points (a) à (e) ; « Ce qui demande un code v5 », point 4) : le verrou est un objet `Autorisation`,
construit sur le texte présenté et la racine de l'arbre lancé, qui ne s'obtient que si :
- le texte présenté est scellé (son compagnon) ;
- la pièce d'autorisation du verrou existe à `CHEMIN_PIECE_D_AUTORISATION` sous la racine de l'arbre lancé et est scellée ;
  « scellée » s'entend au sens de `controle_ia.scellement.verifier` (un compagnon d'une ligne, au bon nom, dont l'empreinte est
  égale), réécrit ici (`verifier_scelle`) parce que ce paquet se lance seul ;
- la pièce porte quatre lignes « nom : valeur », dans l'ordre de la décision R-4123 (`CHAMPS_DE_LA_PIECE`), et son contenu égale
  les valeurs attendues : l'identifiant du GO figure dans la première colonne d'une ligne de `registres/go.md` de l'arbre lancé ;
  le commit du code est celui que le texte inscrit en tête (« Commit du code d'analyse ») ; l'empreinte du texte est celle du
  texte présenté, recalculée ; l'heure est en UTC (forme seule) ;
- chaque module du code lancé (les fichiers `.py` de ce paquet et le `__init__.py` du paquet parent) a l'empreinte que la table
  de l'en-tête du texte lui donne, et la table ne nomme aucun module qui ne soit lancé.
Aucune empreinte du texte n'est écrite dans le code. Le manifeste inscrit l'empreinte du texte présenté, celle de la pièce et
l'heure (module `tirages`). Les essais n'éprouvent le verrou que sur des arbres factices, dans un dossier temporaire, et ne
dérivent aucune graine décisive.
"""

import datetime
import hashlib
import os
import re

import numpy as np

from .constantes import (CHAMPS_DE_LA_PIECE, CHEMIN_PIECE_D_AUTORISATION, CHEMIN_REGISTRE_DES_GO, LIGNE_DU_COMMIT,
                         PREFIXE_DES_MODULES, RACINE_GRAINES)

COUCHES = ("etalonnage", "mecanique", "mecanique-reglages", "audit", "essai-de-forme", "essai", "decisif", "confirmation")
COUCHES_DECISIVES = ("decisif", "confirmation")
# Code v6 (audit des trous du code v5, point 1) : le champ `mode` (« sources » pour les cases du mode « sources » de B8 ; jamais
# écrit au mode « tirages ») s'insère après `repere`. Une étiquette ne porte que les champs qu'on lui donne, dans cet ordre :
# toute étiquette sans le champ `mode` est celle du code v5, à l'octet, et aucune graine existante ne change.
ORDRE_DES_CHAMPS = ("couche", "famille", "proposeur", "dose", "taille", "force", "taux", "retrait", "repere", "mode", "bras",
                    "jumelle", "tirage", "lot", "source", "generation", "monde", "role", "essai", "tour")

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


# --- verrou des graines décisives (code v5) -------------------------------------------------------------------------------------

_LIGNE_COMPAGNON = re.compile(r"^([0-9a-f]{64})  (\S.*)$")  # celle de `controle_ia.scellement`
_LIGNE_DE_TABLE = re.compile(r"^([0-9a-f]{64})  (\S.*)$")
_COMMIT = re.compile(r"`([0-9a-f]{40})`")
_IDENTIFIANT_DU_GO = re.compile(r"^GO-\d{4}-\d{2}-\d{2}-\d{2,}$")
# SILENCE de forme (remarque 4, point (b) : « l'heure est contrôlée dans sa forme seule (UTC) ») : la sortie de `date -u` dans
# la locale C, ou la forme ISO 8601 terminée par Z
FORMES_DE_L_HEURE = ("%a %b %d %H:%M:%S UTC %Y", "%Y-%m-%dT%H:%M:%SZ")


def _refus(message):
    return GraineRefusee(f"autorisation refusée : {message} (B8 ; liste d'arrêt, point 1)")


def verifier_scelle(chemin):
    """« Scellée » au sens de `controle_ia.scellement.verifier` (remarque 4, point (a)) : le fichier existe, son compagnon
    `.sha256` existe, porte une seule ligne non vide « <empreinte>  <nom de base> » au bon nom, et l'empreinte recalculée du
    fichier lui est égale. Rend l'empreinte ; refus sinon."""
    if not os.path.isfile(chemin):
        raise _refus(f"{chemin} absent sur disque")
    compagnon = chemin + ".sha256"
    if not os.path.isfile(compagnon):
        raise _refus(f"{chemin} non scellé (compagnon absent)")
    with open(compagnon, encoding="utf-8") as f:
        lignes = [l for l in f.read().splitlines() if l.strip()]
    if len(lignes) != 1:
        raise _refus(f"{compagnon} : une seule ligne attendue, {len(lignes)} trouvées")
    m = _LIGNE_COMPAGNON.match(lignes[0])
    if not m:
        raise _refus(f"{compagnon} : ligne illisible")
    if m.group(2) != os.path.basename(chemin):
        raise _refus(f"{compagnon} : nom {m.group(2)!r} au lieu de {os.path.basename(chemin)!r}")
    obtenue = _sha256_fichier(chemin)
    if obtenue != m.group(1):
        raise _refus(f"{chemin} : empreinte différente de son compagnon")
    return obtenue


def lire_en_tete_du_texte(chemin_texte):
    """L'en-tête du texte présenté : le commit du code (le premier `<40 chiffres hexadécimaux>` entre accents graves de la seule
    ligne qui commence par `LIGNE_DU_COMMIT`) et la table des empreintes (les lignes « <empreinte>  <chemin> » du premier bloc
    de code qui suit cette ligne, entre deux lignes « ``` »). Rend (commit, {chemin : empreinte}) ; refus sinon."""
    with open(chemin_texte, encoding="utf-8") as f:
        lignes = f.read().split("\n")
    rangs = [i for i, l in enumerate(lignes) if l.startswith(LIGNE_DU_COMMIT)]
    if len(rangs) != 1:
        raise _refus(f"le texte porte {len(rangs)} ligne(s) « {LIGNE_DU_COMMIT.strip()} » au lieu d'une")
    commits = _COMMIT.findall(lignes[rangs[0]])
    if not commits:
        raise _refus("aucun commit du code dans la ligne « Commit du code d'analyse » du texte")
    i = rangs[0] + 1
    while i < len(lignes) and lignes[i].strip() != "```":
        i += 1
    j = i + 1
    table = {}
    while j < len(lignes) and lignes[j].strip() != "```":
        ligne = lignes[j].strip()
        if ligne:
            m = _LIGNE_DE_TABLE.match(ligne)
            if not m or m.group(2) in table:
                raise _refus(f"table des empreintes du texte illisible ou à chemin double : {ligne!r}")
            table[m.group(2)] = m.group(1)
        j += 1
    if j >= len(lignes) or not table:
        raise _refus("table des empreintes du texte absente ou non fermée")
    return commits[0], table


def modules_lances():
    """Les modules du code lancé : les fichiers `.py` de ce paquet et le `__init__.py` du paquet parent, sous les chemins
    relatifs de la table du texte (`src/controle_ia/heritage_etage_processeur_v1/…`). Rend {chemin de la table : chemin sur
    disque}."""
    paquet = os.path.dirname(os.path.abspath(__file__))
    parent = os.path.dirname(paquet)
    prefixe = f"{PREFIXE_DES_MODULES}{os.path.basename(parent)}/"
    out = {f"{prefixe}{os.path.basename(paquet)}/{f}": os.path.join(paquet, f) for f in sorted(os.listdir(paquet))
           if f.endswith(".py") and os.path.isfile(os.path.join(paquet, f))}
    out[f"{prefixe}__init__.py"] = os.path.join(parent, "__init__.py")
    return out


def verifier_modules(table):
    """Chaque module du code lancé a l'empreinte que la table du texte lui donne ; la table ne nomme aucun module (chemin sous
    `src/`) qui ne soit lancé. Refus sinon."""
    lances = modules_lances()
    attendus = {k: v for k, v in table.items() if k.startswith(PREFIXE_DES_MODULES)}
    manquants, en_trop = sorted(set(lances) - set(attendus)), sorted(set(attendus) - set(lances))
    if manquants or en_trop:
        raise _refus(f"modules lancés et table du texte différents : absents de la table {manquants}, non lancés {en_trop}")
    for nom in sorted(set(lances) & set(attendus)):
        if not os.path.isfile(lances[nom]) or _sha256_fichier(lances[nom]) != attendus[nom]:
            raise _refus(f"le module lancé {nom} n'a pas l'empreinte que la table du texte lui donne")
    return True


def lire_piece(chemin_piece):
    """Les quatre lignes « nom : valeur » de la pièce, dans l'ordre de `CHAMPS_DE_LA_PIECE` (un saut de ligne final permis).
    Rend {nom : valeur} ; refus sinon."""
    with open(chemin_piece, encoding="utf-8") as f:
        lignes = f.read().split("\n")
    if lignes and lignes[-1] == "":
        lignes = lignes[:-1]
    if len(lignes) != len(CHAMPS_DE_LA_PIECE):
        raise _refus(f"la pièce d'autorisation porte {len(lignes)} ligne(s) au lieu de {len(CHAMPS_DE_LA_PIECE)}")
    valeurs = {}
    for rang, ligne in enumerate(lignes):
        nom, separateur, v = ligne.partition(" : ")
        if not separateur or nom not in CHAMPS_DE_LA_PIECE or nom in valeurs:
            raise _refus(f"ligne de la pièce d'autorisation hors de la forme « nom : valeur » : {ligne!r}")
        if nom != CHAMPS_DE_LA_PIECE[rang]:
            raise _refus(f"la pièce d'autorisation porte « {nom} » au rang {rang + 1} (ordre de la décision R-4123)")
        if not v or v != v.strip():
            raise _refus(f"valeur vide ou entourée de blancs : « {nom} »")
        valeurs[nom] = v
    return valeurs


def go_inscrit(racine, identifiant):
    """L'identifiant du GO figure dans la première colonne d'une ligne du registre des GO de l'arbre lancé."""
    chemin = os.path.join(racine, CHEMIN_REGISTRE_DES_GO)
    if not os.path.isfile(chemin):
        raise _refus(f"registre des GO absent de l'arbre lancé : {chemin}")
    with open(chemin, encoding="utf-8") as f:
        for ligne in f.read().split("\n"):
            cellules = ligne.split("|")
            if ligne.startswith("|") and len(cellules) > 2 and cellules[1].strip() == identifiant:
                return True
    return False


def exiger_heure_utc(heure):
    for forme in FORMES_DE_L_HEURE:
        try:
            datetime.datetime.strptime(heure, forme)
            return True
        except ValueError:
            continue
    raise _refus(f"heure hors des formes UTC admises : {heure!r}")


class Autorisation:
    """Le verrou des graines décisives (code v5 ; voir l'en-tête du module). `texte` : le texte présenté ; `racine` : la racine
    de l'arbre lancé, qui porte la pièce d'autorisation et `registres/go.md`. Tout est vérifié à la construction, et de nouveau
    par `verifier` avant chaque lancement d'une couche décisive (module `tirages`)."""

    def __init__(self, texte, racine):
        self.texte, self.racine = os.path.abspath(texte), os.path.abspath(racine)
        self.verifier()

    def verifier(self):
        sha_texte = verifier_scelle(self.texte)
        commit_du_texte, table = lire_en_tete_du_texte(self.texte)
        piece = os.path.join(self.racine, CHEMIN_PIECE_D_AUTORISATION)
        sha_piece = verifier_scelle(piece)
        valeurs = lire_piece(piece)
        go, commit, empreinte, heure = (valeurs[c] for c in CHAMPS_DE_LA_PIECE)
        if not _IDENTIFIANT_DU_GO.match(go):
            raise _refus(f"identifiant du GO mal formé : {go!r}")
        if not go_inscrit(self.racine, go):
            raise _refus(f"{go} ne figure dans la première colonne d'aucune ligne de {CHEMIN_REGISTRE_DES_GO}")
        if commit != commit_du_texte:
            raise _refus("le commit du code de la pièce n'est pas celui que le texte inscrit en tête")
        if empreinte != sha_texte:
            raise _refus("l'empreinte du texte de la pièce n'est pas celle du texte présenté")
        exiger_heure_utc(heure)
        verifier_modules(table)
        self.sha_texte, self.sha_piece, self.go, self.commit, self.heure = sha_texte, sha_piece, go, commit, heure
        return True


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
            raise GraineRefusee(f"graine de la couche « {couche} » refusée : aucune autorisation (texte scellé, pièce "
                                "d'autorisation du verrou et modules conformes à la table du texte exigés ; liste d'arrêt, "
                                "point 1)")
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
