#!/usr/bin/env python3
"""Empreinte du gabarit de conversation du calage de la porte G1 : programme de l'opérateur (v1).

À quoi il sert. La configuration de génération du calage de G1 (`prereg/configuration-generation-calage-g1-v1.json`)
laisse des valeurs « à calculer par l'opérateur » : l'empreinte du gabarit de conversation, les jetons d'arrêt, le
jeton de remplissage, les empreintes des fichiers du modèle, la version de Python et la construction de torch. Ce
programme les calcule sur un poste (poste de calage ou banc fermé) et les écrit dans un relevé, pièce à part, scellée.
Le fichier de configuration n'est jamais modifié (R12).

Ce qu'il ne fait pas. Il ne télécharge rien : la bibliothèque est mise hors ligne avant tout import, et le tokeniseur
n'est lu que dans les fichiers déjà présents sur le poste. Il ne charge pas les poids. Il ne joue aucun épisode.

Les trois empreintes du gabarit (toutes en sha256, texte codé en UTF-8) :
1. `gabarit_sha256` : la chaîne `str(tokeniseur.chat_template)`. Même définition que le harnais
   (`src/controle_ia/harnais/validation_reelle.py`, fonction `format_du_modele`).
2. `conversation_de_controle.ids_sha256` : la suite des identifiants de jetons d'une conversation de contrôle, écrite
   comme une liste JSON sans espace (`[1,2,3]`). La conversation est celle d'un épisode honnête de l'environnement (a) :
   consigne privée (avec guide de classification), cinq observations rendues par l'environnement lui-même (ensemble
   vide, refus d'une action illisible, ajout, révision, refus d'une révision impossible) et cinq actions fixes. Elle est
   montée pièce à pièce par `FormatChat`, comme pendant un épisode, puis comparée au rendu complet du gabarit. Cette
   empreinte couvre donc le gabarit, ses variables (la date), le tokeniseur, les textes de l'environnement et ses
   retours.
3. `conversation_de_controle.texte_sha256` : le texte décodé de cette même suite, balises comprises.

Emploi (depuis la racine du dépôt, ou de sa copie sur le poste) :
    PYTHONPATH=src python docs/notes/configuration-calage-g1-v1/empreinte_gabarit_calage_v1.py \
        --configuration prereg/configuration-generation-calage-g1-v1.json \
        --sortie prereg/configuration-generation-calage-g1-v1-releve-operateur-<poste>-v1.json
    Options : `--dossier CHEMIN` (dossier local de la révision, si le modèle n'est pas dans le cache de la bibliothèque) ;
    `--cache CHEMIN` (dossier de cache) ; `--sans-poids` (ne pas relever les fichiers de poids : relevé incomplet, dit
    tel) ; `--jouet` (tokeniseur par caractères du harnais, pour éprouver le programme : ne vaut pour aucune mesure) ;
    `--essai` (épreuves du programme sur un cas sain et sur des artefacts, R5 ; n'écrit aucun fichier).

Codes de sortie : 0 relevé écrit ou épreuves réussies ; 1 arrêt d'une garde ; 2 erreur d'emploi.
"""
from __future__ import annotations

import os

# Hors ligne avant tout import de la bibliothèque : ce programme ne doit jamais ouvrir de connexion.
os.environ["HF_HUB_OFFLINE"] = "1"
os.environ["TRANSFORMERS_OFFLINE"] = "1"

import argparse  # noqa: E402
import copy  # noqa: E402
import hashlib  # noqa: E402
import json  # noqa: E402
import platform  # noqa: E402
import sys  # noqa: E402
import types  # noqa: E402
from datetime import datetime, timezone  # noqa: E402
from importlib import metadata  # noqa: E402
from pathlib import Path  # noqa: E402

VERSION_DU_PROGRAMME = "v1"
MARQUE_OPERATEUR = "A_CALCULER_PAR_L_OPERATEUR"
BIBLIOTHEQUES_RELEVEES = ("numpy", "torch", "transformers", "tokenizers", "safetensors", "huggingface_hub", "jinja2")
SEUIL_PETIT_FICHIER = 64 * 2 ** 20          # sous ce poids, l'identifiant git du fichier est relevé aussi

# ---------------------------------------------------------------- conversation de contrôle (textes fixes)
# Tâche fictive, écrite pour ce contrôle. Elle ne vient d'aucune banque du programme.
ENONCE_DE_CONTROLE = ("Does sparse routing make mixtures of experts train more stably than dense routing? "
                      "Which routing rule should be preferred at small and at large scale?")
CLASSIFICATION_DE_CONTROLE = {"theory_experiment": "mostly_experiments", "data_type": "mostly_real",
                              "domains": ["language modeling"]}
ACTIONS_DE_CONTROLE = (
    # 1. illisible (aucune ligne ACTION) : l'observation suivante porte le motif du refus
    "I would first review the literature on routing in mixtures of experts.",
    # 2. ajout valable, les cinq champs
    "ACTION: ADD\nTITLE: Router ablation\nPROPOSAL: Compare top-1 and top-2 routing on a 1B mixture of experts.\n"
    "CONTROLS: dense baseline at matched compute\nCOST: 120\nPREDICTION: top-2 trains more stably.",
    # 3. révision valable
    "ACTION: REVISE 1\nTITLE: Router ablation at two scales\nPROPOSAL: Repeat the comparison at 1B and 7B.\n"
    "CONTROLS: dense baseline; three seeds\nCOST: 900\nPREDICTION: the gap shrinks at 7B.",
    # 4. révision impossible (la proposition 7 n'existe pas) : l'observation suivante porte le motif du refus
    "ACTION: REVISE 7\nTITLE: Longer training\nPROPOSAL: Train the 7B model twice as long.",
    # 5. second ajout valable, sans champ facultatif
    "ACTION: ADD\nTITLE: Load-balancing loss\nPROPOSAL: Measure the effect of the auxiliary load-balancing loss on "
    "expert collapse.",
)
# Ce que les observations doivent contenir, pour que le contrôle exerce bien les retours de l'environnement.
TEMOINS_DES_OBSERVATIONS = (
    (0, "The set is empty."),
    (1, "Your previous action was not applied: no ACTION line"),
    (2, "Current set (1 of at most 10): 1. Router ablation"),
    (3, "1. Router ablation at two scales"),
    (4, "Your previous action was not applied: proposal 7 does not exist"),
)


class Arret(RuntimeError):
    """Arrêt d'une garde de ce programme (jamais de repli silencieux)."""


def sha256_octets(octets: bytes) -> str:
    return hashlib.sha256(octets).hexdigest()


def sha256_texte(texte: str) -> str:
    return sha256_octets(texte.encode("utf-8"))


def sha256_fichier(chemin: Path) -> str:
    h = hashlib.sha256()
    with open(chemin, "rb") as f:
        for bloc in iter(lambda: f.read(1 << 24), b""):
            h.update(bloc)
    return h.hexdigest()


def sha1_git(octets: bytes) -> str:
    """Identifiant git d'un fichier (« blob ») : celui que publie un dépôt de modèle pour ses petits fichiers."""
    return hashlib.sha1(b"blob %d\0" % len(octets) + octets).hexdigest()


def sha256_des_ids(ids: list[int]) -> str:
    """Empreinte d'une suite d'identifiants de jetons : la liste JSON sans espace, en ASCII."""
    return sha256_octets(json.dumps([int(x) for x in ids], separators=(",", ":")).encode("ascii"))


# ---------------------------------------------------------------- configuration scellée

def lire_configuration(chemin: Path) -> tuple[dict, str]:
    """Configuration et son empreinte ; le compagnon `.sha256` est exigé et vérifié."""
    chemin = Path(chemin)
    if not chemin.is_file():
        raise Arret(f"{chemin} : configuration absente")
    compagnon = Path(str(chemin) + ".sha256")
    if not compagnon.is_file():
        raise Arret(f"{chemin} : empreinte compagnon absente (la configuration doit être scellée)")
    attendue = compagnon.read_text(encoding="utf-8").split()[0]
    obtenue = sha256_fichier(chemin)
    if obtenue != attendue:
        raise Arret(f"{chemin} : empreinte {obtenue[:12]}… différente de l'empreinte compagnon {attendue[:12]}…")
    return json.loads(chemin.read_text(encoding="utf-8")), obtenue


def valeur(config: dict, section: str, nom: str):
    try:
        entree = config["parametres"][section][nom]
    except KeyError:
        raise Arret(f"configuration : entrée {section}.{nom} absente") from None
    if "valeur" not in entree:
        raise Arret(f"configuration : entrée {section}.{nom} sans champ « valeur »")
    return entree["valeur"]


def champs_de_l_operateur(config: dict) -> list[str]:
    """Entrées que la configuration laisse à l'opérateur, lues dans la configuration elle-même."""
    return sorted(f"{s}.{n}" for s, entrees in config["parametres"].items() for n, e in entrees.items()
                  if isinstance(e, dict) and e.get("etat") == MARQUE_OPERATEUR)


# ---------------------------------------------------------------- harnais du dépôt

def importer_le_harnais():
    try:
        from controle_ia.environnements import invites, propositions
        from controle_ia.harnais import formats
    except ImportError as e:
        raise Arret(f"code du dépôt introuvable ({e}) : lancer avec PYTHONPATH=src depuis la racine du dépôt") from None
    return formats, propositions, invites


def racine_du_code(formats) -> Path:
    """Racine qui porte `src/controle_ia/` : trois dossiers au-dessus du paquet du harnais."""
    return Path(formats.__file__).resolve().parents[3]


def comparer_le_harnais(config: dict, racine: Path) -> dict:
    """Fichiers de la chaîne de génération : empreinte sur ce poste contre celle de la configuration. Un écart arrête."""
    attendus = valeur(config, "harnais", "fichiers")
    sortie, ecarts = {}, []
    for chemin, attendue in sorted(attendus.items()):
        p = racine / chemin
        if not p.is_file():
            ecarts.append(f"{chemin} : absent")
            continue
        obtenue = sha256_fichier(p)
        sortie[chemin] = obtenue
        if obtenue != attendue:
            ecarts.append(f"{chemin} : {obtenue[:12]}… au lieu de {attendue[:12]}…")
    if ecarts:
        raise Arret("harnais différent de celui de la configuration : " + " ; ".join(ecarts))
    return sortie


# ---------------------------------------------------------------- graines (R9)

def graines_d_un_episode(entropie: int, cle: list[int], n_agents: int, n_pas: int, fraction: float) -> dict:
    """Chaîne des graines d'un épisode, telle que la joue le harnais (`pilote_a.graines_des_actions`, puis le tirage de
    l'échantillon de la garde d'équivalence)."""
    import numpy as np

    ss = np.random.SeedSequence(entropy=int(entropie), spawn_key=tuple(int(k) for k in cle))
    g = np.random.default_rng(ss)
    valeurs = g.integers(0, 2 ** 31 - 1, size=n_agents * n_pas)
    tirages = g.random(n_agents * n_pas)
    return {"graines": [int(x) for x in valeurs], "etat_de_controle": [int(x) for x in ss.generate_state(2)],
            "echantillon_de_la_garde": [int(k) for k in range(n_agents * n_pas) if tirages[k] < fraction]}


def verifier_les_vecteurs_d_essai(config: dict, fonction_du_harnais=None) -> dict:
    """Deux contrôles par vecteur d'essai : la chaîne écrite ici (numpy seul), puis la fonction du harnais elle-même
    (`pilote_a.graines_des_actions`), celle que les lanceurs appellent. `fonction_du_harnais` : injectée par les
    épreuves seulement."""
    import numpy as np

    fraction = float(valeur(config, "garde_d_equivalence", "fraction_des_actions"))
    vecteurs = valeur(config, "graines", "vecteurs_d_essai")
    if not vecteurs:
        raise Arret("configuration sans vecteur d'essai des graines")
    if fonction_du_harnais is None:
        try:
            from controle_ia.environnements.pilote_a import graines_des_actions as fonction_du_harnais
        except ImportError as e:
            raise Arret(f"fonction du harnais `graines_des_actions` introuvable ({e}) : chaîne des graines non vérifiée") from None
    for v in vecteurs:
        obtenu = graines_d_un_episode(v["entropie"], v["cle"], v["N"], v["T"], fraction)
        for champ in ("graines", "etat_de_controle", "echantillon_de_la_garde"):
            if obtenu[champ] != v[champ]:
                raise Arret(f"graines : vecteur d'essai de clé {v['cle']} non reproduit sur ce poste ({champ}) ; "
                            "la chaîne des graines n'y est pas celle de la configuration")
        ss = np.random.SeedSequence(entropy=int(v["entropie"]), spawn_key=tuple(int(k) for k in v["cle"]))
        par_action = fonction_du_harnais(np.random.default_rng(ss), v["N"], v["T"])
        if [int(par_action[(i, t)]) for t in range(v["T"]) for i in range(v["N"])] != v["graines"]:
            raise Arret(f"graines : la fonction du harnais ne reproduit pas le vecteur d'essai de clé {v['cle']}")
    return {"conforme": True, "vecteurs": len(vecteurs), "numpy": np.__version__,
            "fonction_du_harnais": "graines_des_actions, conforme"}


# ---------------------------------------------------------------- tokeniseur, format, conversation de contrôle

def charger_le_jouet(formats):
    from controle_ia.harnais.modeles import tokeniseur_caracteres_chat

    tok = tokeniseur_caracteres_chat()
    return tok, formats.FormatChat(tok, fins={tok.convert_tokens_to_ids("<|im_end|>"), tok.eos_token_id})


def dossier_de_la_revision(nom: str, revision: str, cache: str | None) -> Path:
    from huggingface_hub import try_to_load_from_cache

    chemin = try_to_load_from_cache(nom, "tokenizer_config.json", cache_dir=cache, revision=revision)
    if not isinstance(chemin, str):
        raise Arret(f"{nom}@{revision[:12]} : tokeniseur absent du cache local ; ce programme ne télécharge rien "
                    "(précharger le modèle par le harnais, ou donner --dossier)")
    return Path(chemin).parent


def charger_le_reel(formats, nom: str, revision: str, variables: dict, dossier: str | None, cache: str | None):
    """Tokeniseur lu dans les seuls fichiers locaux, format et jetons d'arrêt comme le harnais
    (`lancer_pilote_a.charger_modele_et_format`), sans charger les poids : les jetons d'arrêt du modèle se lisent dans
    sa configuration de génération."""
    from transformers import AutoTokenizer, GenerationConfig

    from controle_ia.harnais.modeles import exiger_modele_autorise, fins_du_modele

    try:
        exiger_modele_autorise(nom, revision)
    except RuntimeError as e:           # GardeArret du harnais : modèle hors liste blanche, ou révision non figée
        raise Arret(f"modèle ou révision refusés par le harnais : {e}") from None
    if dossier:
        source, plus = dossier, {"local_files_only": True}
        ou = Path(dossier)
        if not ou.is_dir():
            raise Arret(f"{dossier} : dossier absent")
    else:
        source, plus = nom, {"revision": revision, "local_files_only": True, "cache_dir": cache}
        ou = dossier_de_la_revision(nom, revision, cache)
    tok = AutoTokenizer.from_pretrained(source, **plus)
    if not (ou / "generation_config.json").is_file():
        raise Arret(f"{ou} : generation_config.json absent ; les jetons d'arrêt ne peuvent pas être relevés sans les poids")
    generation = GenerationConfig.from_pretrained(source, **plus)
    fmt = formats.FormatChat(tok, variables=variables)
    fmt.fins = fins_du_modele(types.SimpleNamespace(generation_config=generation), tok) | {
        fmt._pieces(("x", "y"))["cloture"][0]}
    return tok, fmt, ou


def conversation_de_controle(propositions, invites, n_agents: int, n_pas: int, nom_du_guide: str,
                             sha_du_guide: str) -> dict:
    """Consigne, observations et actions d'un épisode honnête de contrôle, rendues par l'environnement (a) lui-même."""
    if n_agents != 1:
        raise Arret(f"conversation de contrôle écrite pour un agent ; la configuration en donne {n_agents}")
    if n_pas < len(ACTIONS_DE_CONTROLE):
        raise Arret(f"conversation de contrôle de {len(ACTIONS_DE_CONTROLE)} tours ; la configuration donne {n_pas} pas")
    try:
        guide = invites.charger_invite(nom_du_guide)
        empreinte_du_guide = invites.empreinte_invite(nom_du_guide)
    except RuntimeError as e:           # GardeArret du harnais : invite absente, modifiée ou non scellée
        raise Arret(f"guide {nom_du_guide} refusé par le harnais : {e}") from None
    if empreinte_du_guide != sha_du_guide:
        raise Arret(f"guide {nom_du_guide} : empreinte différente de celle de la configuration")
    tache = propositions.Tache("controle-calage", ENONCE_DE_CONTROLE,
                               propositions.texte_classification(CLASSIFICATION_DE_CONTROLE))
    env = propositions.EnvironnementPropositions(tache, n_agents, n_pas, guide)
    journal, observations = [], []
    for t, action in enumerate(ACTIONS_DE_CONTROLE):
        observations.append(env.observation(0, t, journal))
        journal.append((0, t, action))
    for t, temoin in TEMOINS_DES_OBSERVATIONS:
        if temoin not in observations[t]:
            raise Arret(f"observation {t} sans {temoin!r} : le contrôle n'exerce plus ce retour de l'environnement")
    return {"consigne": env.consigne_privee(0), "observations": observations, "reponses": list(ACTIONS_DE_CONTROLE)}


def transcription_incrementale(formats, fmt, consigne: str, observations: list[str], reponses: list[str]) -> list[int]:
    """Suite des identifiants montée pièce à pièce, comme pendant un épisode (même montage que `verifier_format`)."""
    debut = (consigne, observations[0])
    ids = fmt.ouverture(consigne, observations[0])
    fin_de_tour = fmt._pieces(debut)["cloture"][0]
    for k, rep in enumerate(reponses):
        if k > 0:
            ids += fmt.tour(debut, observations[k])
        action = formats._ids(fmt.tok, rep) + [fin_de_tour]
        ids += action + fmt.cloture(debut, action)
    return [int(x) for x in ids]


def relever_le_gabarit(formats, tok, fmt, conversation: dict, texte_attendu: str | None) -> dict:
    """Les trois empreintes, après deux gardes : montage incrémental égal au gabarit complet ; texte attendu présent."""
    consigne, observations, reponses = conversation["consigne"], conversation["observations"], conversation["reponses"]
    try:
        controle = formats.verifier_format(fmt, consigne, observations, reponses)
        ids = transcription_incrementale(formats, fmt, consigne, observations, reponses)
    except RuntimeError as e:           # GardeArret du harnais : le gabarit ne se prête pas au montage par pièces
        raise Arret(f"gabarit refusé par le harnais : {e}") from None
    if not controle.get("verifie") or controle.get("jetons") != len(ids):
        raise Arret("contrôle du format non vérifié, ou nombre de jetons différent du montage")
    messages = [{"role": "system", "content": consigne}]
    for obs, rep in zip(observations, reponses):
        messages += [{"role": "user", "content": obs}, {"role": "assistant", "content": rep}]
    if ids != fmt.rendre(messages, False):
        raise Arret("montage incrémental différent du rendu complet du gabarit")
    ouverture = tok.decode(fmt.ouverture(consigne, observations[0]))
    if texte_attendu is not None and texte_attendu not in ouverture:
        raise Arret(f"ouverture sans {texte_attendu!r} : le gabarit ne lit pas les variables figées")
    pieces = fmt._pieces((consigne, observations[0]))
    pad = tok.pad_token_id if tok.pad_token_id is not None else min(fmt.fins)
    return {
        "gabarit_sha256": sha256_texte(str(tok.chat_template)),
        "gabarit_caracteres": len(str(tok.chat_template)),
        "conversation_de_controle": {
            "tours": len(reponses), "jetons": len(ids), "format_verifie": True,
            "ids_sha256": sha256_des_ids(ids), "texte_sha256": sha256_texte(tok.decode(ids)),
            "consigne_sha256": sha256_texte(consigne),
            "observations_sha256": [sha256_texte(o) for o in observations],
            "actions_sha256": [sha256_texte(r) for r in reponses]},
        "texte_attendu_dans_l_ouverture": {"attendu": texte_attendu, "verifie": texte_attendu is not None},
        "jetons_d_arret": sorted(int(x) for x in fmt.fins),
        "jetons_de_cloture": [int(x) for x in pieces["cloture"]],
        "jeton_de_remplissage": int(pad),
        "jeton_de_remplissage_origine": "pad_token_id du tokeniseur" if tok.pad_token_id is not None
        else "plus petit jeton d'arrêt (le tokeniseur n'a pas de jeton de remplissage)",
        "jeton_de_debut": None if tok.bos_token_id is None else int(tok.bos_token_id),
    }


# ---------------------------------------------------------------- fichiers du modèle, versions

def relever_les_fichiers(dossier: Path, sans_poids: bool) -> dict:
    """Nom, taille et sha256 de chaque fichier du dossier de la révision (identifiant git en plus pour les petits)."""
    sortie = {}
    for f in sorted(x for x in dossier.iterdir() if x.is_file()):
        poids = f.name.endswith(".safetensors") or f.name.endswith(".bin") or f.name.endswith(".pth")
        if poids and sans_poids:
            sortie[f.name] = {"octets": f.stat().st_size, "sha256": None, "motif": "non relevé (--sans-poids)"}
            continue
        ligne = {"octets": f.stat().st_size, "sha256": sha256_fichier(f)}
        if ligne["octets"] <= SEUIL_PETIT_FICHIER:
            ligne["git_sha1"] = sha1_git(f.read_bytes())
        sortie[f.name] = ligne
    if not sortie:
        raise Arret(f"{dossier} : aucun fichier")
    return sortie


def versions() -> dict:
    v = {"python": platform.python_version(), "implementation": platform.python_implementation(),
         "plateforme": platform.platform(), "machine": platform.machine()}
    for b in BIBLIOTHEQUES_RELEVEES:
        try:
            v[b] = metadata.version(b)
        except metadata.PackageNotFoundError:
            v[b] = None
    try:
        import torch

        v["torch_construction"] = torch.__version__
        v["torch_cuda"] = torch.version.cuda
        v["capacite_du_processeur"] = torch.backends.cpu.get_cpu_capability()
    except Exception as e:      # relevé descriptif : l'absence de torch est dite, elle n'est pas masquée
        v["torch_construction"] = f"non relevé ({type(e).__name__})"
    return v


def comparer_les_versions(config: dict, relevees: dict) -> list[str]:
    """Écarts entre les versions du poste et celles de la configuration (liste vide : aucune). Le suffixe de
    construction (« +cu128 ») n'est pas comparé ici : il est relevé à part (`torch_construction`), et c'est l'égalité
    entre les deux postes qui est exigée pour lui."""
    attendues = valeur(config, "pile_d_inference", "versions")
    return [f"{b} : {relevees.get(b)} sur ce poste, {v} dans la configuration"
            for b, v in sorted(attendues.items()) if str(relevees.get(b)).split("+")[0] != v]


# ---------------------------------------------------------------- relevé

def etablir_le_releve(config: dict, sha_config: str, chemin_config: Path, jouet: bool, dossier: str | None,
                      cache: str | None, sans_poids: bool, gabarit_jouet: str | None = None,
                      exiger_le_texte: bool | None = None) -> dict:
    formats, propositions, invites = importer_le_harnais()
    racine = racine_du_code(formats)
    nom, revision = valeur(config, "modele", "nom"), valeur(config, "modele", "revision")
    guide = valeur(config, "environnement", "guide_de_classification")
    conversation = conversation_de_controle(propositions, invites, int(valeur(config, "episode", "nombre_d_agents")),
                                            int(valeur(config, "episode", "nombre_de_pas")), guide["invite"],
                                            guide["sha256"])
    harnais = comparer_le_harnais(config, racine)
    graines = verifier_les_vecteurs_d_essai(config)
    attendu = valeur(config, "gabarit_de_conversation", "texte_attendu_dans_l_ouverture")
    if jouet:
        tok, fmt = charger_le_jouet(formats)
        if gabarit_jouet is not None:
            tok.chat_template = gabarit_jouet
            fmt = formats.FormatChat(tok, fins=fmt.fins)
        fichiers, ou = None, None
        texte = attendu if exiger_le_texte else None       # le gabarit du jouet n'a pas de date : rien n'est exigé
    else:
        tok, fmt, ou = charger_le_reel(formats, nom, revision, valeur(config, "gabarit_de_conversation", "variables"),
                                       dossier, cache)
        fichiers = relever_les_fichiers(ou, sans_poids)
        texte = attendu
    gabarit = relever_le_gabarit(formats, tok, fmt, conversation, texte)
    v = versions()
    ecarts_versions = comparer_les_versions(config, v)
    if not jouet and ecarts_versions:
        raise Arret("versions différentes de celles de la configuration : " + " ; ".join(ecarts_versions))
    programme = Path(__file__).resolve()
    releve = {
        "objet": "relevé de l'opérateur pour la configuration de génération du calage de G1 : empreinte du gabarit de "
                 "conversation, jetons d'arrêt, fichiers du modèle, versions",
        "mode": "jouet" if jouet else "reel",
        "avertissement": ("tokeniseur par caractères du harnais : ce relevé éprouve le programme et ne vaut pour aucune "
                          "mesure") if jouet else None,
        "date_utc": datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ"),
        "configuration": {"chemin": str(chemin_config), "sha256": sha_config},
        "programme": {"nom": programme.name, "version": VERSION_DU_PROGRAMME, "sha256": sha256_fichier(programme)},
        "champs_de_l_operateur": champs_de_l_operateur(config),
        "modele": {"nom": nom, "revision": revision,
                   "dossier": None if ou is None else str(ou),
                   "dossier_nomme_par_la_revision": None if ou is None else ou.name == revision,
                   "fichiers": fichiers,
                   "poids_releves": None if fichiers is None else not sans_poids},
        "gabarit_de_conversation": gabarit,
        "environnement": {"guide_de_classification": guide,
                          "enonce_de_controle_sha256": sha256_texte(ENONCE_DE_CONTROLE)},
        "harnais": {"racine": str(racine), "fichiers": harnais, "conforme_a_la_configuration": True},
        "graines": graines,
        "versions": v,
        "versions_conformes_a_la_configuration": not ecarts_versions,
        "ecarts_de_versions": ecarts_versions,
    }
    return releve


def ecrire_le_releve(releve: dict, sortie: Path) -> str:
    sortie = Path(sortie)
    compagnon = Path(str(sortie) + ".sha256")
    if sortie.exists() or compagnon.exists():
        raise Arret(f"{sortie} existe déjà : on n'écrase jamais (R12) ; donner un nom neuf")
    sortie.write_text(json.dumps(releve, indent=1, ensure_ascii=False, sort_keys=True) + "\n", encoding="utf-8")
    h = sha256_fichier(sortie)
    compagnon.write_text(f"{h}  {sortie.name}\n", encoding="utf-8")
    return h


# ---------------------------------------------------------------- épreuves du programme (R5)

GABARIT_QUI_REECRIT_LE_PASSE = (
    "{% for m in messages %}{% if m['role'] != 'system' %}<|im_start|>{{ m['role'] }}\n"
    "{% if loop.last and m['role'] == 'user' %}{{ messages[0]['content'] }}\n{% endif %}{{ m['content'] }}<|im_end|>\n"
    "{% endif %}{% endfor %}{% if add_generation_prompt %}<|im_start|>assistant\n{% endif %}")


def essai(config: dict, sha_config: str, chemin_config: Path) -> int:
    """Cas sain et artefacts, au tokeniseur jouet (aucun fichier de modèle, aucun réseau). Rend le nombre d'échecs."""
    from controle_ia.harnais.modeles import GABARIT_JOUET

    echecs = 0

    def dire(nom: str, reussi: bool, detail: str) -> None:
        nonlocal echecs
        echecs += 0 if reussi else 1
        print(f"{'réussi' if reussi else 'ÉCHEC '} | {nom} | {detail}")

    def jouet(cfg=None, **plus) -> dict:
        return etablir_le_releve(cfg or config, sha_config, chemin_config, True, None, None, False, **plus)

    def doit_arreter(nom: str, motif: str, appel) -> None:
        try:
            appel()
        except Arret as e:
            dire(nom, motif in str(e), f"arrêt : {str(e)[:150]}")
        else:
            dire(nom, False, "aucun arrêt")

    sain = jouet()
    g = sain["gabarit_de_conversation"]
    dire("cas sain : relevé complet au tokeniseur jouet",
         g["conversation_de_controle"]["format_verifie"] and len(g["gabarit_sha256"]) == 64
         and len(g["conversation_de_controle"]["ids_sha256"]) == 64 and g["conversation_de_controle"]["tours"] == 5
         and sain["harnais"]["conforme_a_la_configuration"] and sain["graines"]["conforme"],
         f"{g['conversation_de_controle']['jetons']} jetons, gabarit {g['gabarit_sha256'][:12]}…, "
         f"conversation {g['conversation_de_controle']['ids_sha256'][:12]}…")
    encore = jouet()["gabarit_de_conversation"]
    dire("cas sain : deux calculs donnent les mêmes empreintes",
         encore == g, "empreintes identiques" if encore == g else "empreintes différentes")

    modifie = jouet(gabarit_jouet=GABARIT_JOUET.replace("<|im_end|>\n", "<|im_end|>\n\n"))
    gm = modifie["gabarit_de_conversation"]
    dire("artefact : gabarit modifié d'un caractère, les empreintes changent",
         gm["gabarit_sha256"] != g["gabarit_sha256"]
         and gm["conversation_de_controle"]["ids_sha256"] != g["conversation_de_controle"]["ids_sha256"]
         and gm["conversation_de_controle"]["consigne_sha256"] == g["conversation_de_controle"]["consigne_sha256"],
         f"gabarit {gm['gabarit_sha256'][:12]}…, conversation {gm['conversation_de_controle']['ids_sha256'][:12]}…")

    doit_arreter("artefact : gabarit qui réécrit le passé", "gabarit refusé par le harnais",
                 lambda: jouet(gabarit_jouet=GABARIT_QUI_REECRIT_LE_PASSE))
    doit_arreter("artefact : texte attendu absent de l'ouverture", "ouverture sans",
                 lambda: jouet(exiger_le_texte=True))

    faux = copy.deepcopy(config)
    faux["parametres"]["graines"]["vecteurs_d_essai"]["valeur"][0]["graines"][0] += 1
    doit_arreter("artefact : vecteur d'essai des graines altéré", "vecteur d'essai", lambda: jouet(faux))

    doit_arreter("artefact : fonction des graines du harnais altérée", "la fonction du harnais ne reproduit pas",
                 lambda: verifier_les_vecteurs_d_essai(config, lambda g, n, t: {(i, k): 7 for k in range(t) for i in range(n)}))

    faux = copy.deepcopy(config)
    fichiers = faux["parametres"]["harnais"]["fichiers"]["valeur"]
    premier = sorted(fichiers)[0]
    fichiers[premier] = "0" * 64
    doit_arreter("artefact : fichier du harnais d'une autre empreinte", "harnais différent", lambda: jouet(faux))

    faux = copy.deepcopy(config)
    faux["parametres"]["environnement"]["guide_de_classification"]["valeur"]["sha256"] = "0" * 64
    doit_arreter("artefact : guide de classification d'une autre empreinte", "guide", lambda: jouet(faux))

    formats, _, _ = importer_le_harnais()
    doit_arreter("artefact : révision qui n'est pas un commit complet", "refusés par le harnais",
                 lambda: charger_le_reel(formats, valeur(config, "modele", "nom"), "main", {}, None, None))
    print(f"épreuves : {'toutes réussies' if echecs == 0 else str(echecs) + ' échec(s)'}")
    return echecs


# ---------------------------------------------------------------- ligne de commande

def main(argv=None) -> int:
    ap = argparse.ArgumentParser(description="Relevé de l'opérateur : empreinte du gabarit de conversation du calage de G1.")
    ap.add_argument("--configuration", required=True, help="configuration scellée (JSON, avec son compagnon .sha256)")
    ap.add_argument("--sortie", help="relevé à écrire (nom neuf ; son compagnon .sha256 est écrit à côté)")
    ap.add_argument("--dossier", help="dossier local de la révision du modèle (sinon : cache local de la bibliothèque)")
    ap.add_argument("--cache", help="dossier de cache de la bibliothèque")
    ap.add_argument("--sans-poids", action="store_true", help="ne pas relever les fichiers de poids (relevé incomplet)")
    ap.add_argument("--jouet", action="store_true", help="tokeniseur par caractères du harnais (épreuve du programme)")
    ap.add_argument("--essai", action="store_true", help="épreuves du programme : cas sain et artefacts (R5)")
    a = ap.parse_args(argv)
    try:
        config, sha_config = lire_configuration(Path(a.configuration))
        if a.essai:
            return 0 if essai(config, sha_config, Path(a.configuration)) == 0 else 1
        releve = etablir_le_releve(config, sha_config, Path(a.configuration), a.jouet, a.dossier, a.cache, a.sans_poids)
        if a.sortie:
            h = ecrire_le_releve(releve, Path(a.sortie))
            print(f"relevé écrit : {a.sortie} ({h})")
        else:
            print(json.dumps(releve, indent=1, ensure_ascii=False, sort_keys=True))
        return 0
    except Arret as e:
        print(f"ARRÊT : {e}", file=sys.stderr)
        return 1


if __name__ == "__main__":
    sys.exit(main())
