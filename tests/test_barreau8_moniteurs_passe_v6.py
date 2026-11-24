"""Essais de la passe de recalcul de l'activité interne du barreau 8 (côté moniteurs), version 6, sur modèle jouet.

Aucun modèle réel, aucun réseau, aucune donnée du programme : un petit modèle de type Llama (4 couches, largeur 32),
un jetoniseur par caractères, des sondes et des adaptateurs aléatoires sous graine, des actions tirées du modèle jouet.
Version 6 : la course jouet verse ses identifiants dans un objet JSON à deux clés (additif 2, M-1), sans fichier des
textes, sous un dossier de la course (M-2) ; le registre porte les trois lignes de scellement (texte, additif 1,
additif 2) ; le bordereau du code porte dix clés ; les constantes de forme viennent d'une table jouet de la forme de la
table neuve (M-4).

Le modèle jouet est AJUSTÉ quelques dizaines de pas, sous graine, sur des suites qui dépendent du contexte (chaque tâche
jouet a un énoncé fait d'une lettre propre, et une suite propre à produire) : sans cela, la garde du contrôle du
contexte par la vraisemblance (P10) n'a pas de sens. Ce n'est pas un réglage de la garde : ses seuils sont ceux du texte.
Chaque garde est éprouvée sur un cas sain (la passe entière, `monde`) et sur au moins un artefact (R5).
"""
from __future__ import annotations

import dataclasses
import hashlib
import json
import shutil
import os
import subprocess
import sys
import time
import zipfile
from importlib import metadata
from pathlib import Path

import numpy as np
import pytest
import torch

from controle_ia.barreau8_moniteurs import passe_recalcul_v6 as P
from controle_ia.barreau8_moniteurs.comparer_interface_v6_v7_v2 import effectif_sous_echantillon
from controle_ia.gardes import GardeArret
from controle_ia.harnais.activations import passe_unique
from controle_ia.harnais.formats import FormatChat
from controle_ia.harnais.modeles import GABARIT_JOUET, modele_jouet, tokeniseur_caracteres_chat
from controle_ia.harnais.sondes import score_action
from controle_ia.organismes.lora import charger_etat, etat_lora, fixer_dose, injecter
from controle_ia.premier_test_ia.conditions import environnement
from controle_ia.premier_test_ia.figees import ecrire_sondes
from controle_ia.environnements.invites import charger_invite
from controle_ia.environnements.pilote_a import tache_de
from controle_ia.scellement import compagnon, empreinte, sceller, verifier
from controle_ia.sondes.familles import SondeLineaireJetons
from controle_ia.t06.distillation_transcription import adaptateurs_en_simple_precision, transcription_honnete

LARGEUR, COUCHES_JOUET, FIN, EOS = 32, 4, 135, 2
GABARIT = "<s>Today Date: {{ date_string }}\n" + GABARIT_JOUET
CONDITIONS = P.SPECIFICATION_TEXTE.conditions
N_TACHES, PAS, MAX_JETONS, N_PLANCHER = 4, 3, 12, 5
N_ACTIONS = N_TACHES * len(CONDITIONS) * PAS
GRAINE_MODELE = 20261119
LETTRES = "éèêà"
SIGNES = "abcdefghijk"
MOTIFS = tuple("".join(SIGNES[(i * (k + 1)) % 11] for i in range(11)) for k in range(4))
POIDS: dict = {}
VERSIONS = {"transformers": metadata.version("transformers"), "tokenizers": metadata.version("tokenizers")}
NOMS_ADAPTATEURS = dict(P.SPECIFICATION_TEXTE.fichiers_adaptateurs)
NOM_IDS = P.SPECIFICATION_TEXTE.nom_fichier_identifiants
CHEMIN_TACHES = "donnees/taches/taches-evaluation.json"
torch.set_num_threads(2)


# ----------------------------------------------------------------------------------------------------------------------
# Fabrique du monde jouet.
# ----------------------------------------------------------------------------------------------------------------------

def jetoniseur_jouet(nettoyage: bool = True):
    tok = tokeniseur_caracteres_chat()
    tok.chat_template = GABARIT
    tok.clean_up_tokenization_spaces = nettoyage
    return tok


def modele_neuf(tok):
    """Modèle jouet : initialisation sous graine, puis poids ajustés par `ajuster_modele` (les mêmes à chaque appel)."""
    modele = modele_jouet(GRAINE_MODELE, len(tok), couches=COUCHES_JOUET, largeur=LARGEUR, tetes=2, tetes_cle_valeur=1,
                          intermediaire=64)
    if POIDS:
        modele.load_state_dict(POIDS["etat"])
    modele.generation_config.eos_token_id = [EOS, FIN]
    return modele.eval()


def ajuster_modele(tok, taches, pas_d_ajustement: int = 110) -> None:
    """Ajuste le modèle jouet, sous graine, pour qu'après le contexte d'une tâche il produise la suite propre à cette
    tâche : la vraisemblance d'une action dépend alors de son contexte, ce que la garde P10 contrôle."""
    POIDS.clear()
    modele = modele_neuf(tok)
    fmt = FormatChat(tok, fins={EOS, FIN}, variables={"date_string": "26 Jul 2024"})
    guide = charger_invite("H1-classification")
    exemples = []
    for k, t in enumerate(taches):
        env = environnement("honnete", tache_de(t), PAS, guide, {})
        actions = [tok(MOTIFS[k][:n], add_special_tokens=False)["input_ids"] + [FIN] for n in (11, 7, 9)]
        ids, empans = transcription_honnete(fmt, env, actions)
        etiquettes = [-100] * len(ids)
        for d, f in empans:
            etiquettes[d:f] = ids[d:f]
        exemples.append((ids, etiquettes))
    L = max(len(i) for i, _ in exemples)
    x = torch.zeros((len(exemples), L), dtype=torch.long)
    y = torch.full((len(exemples), L), -100)
    masque = torch.zeros((len(exemples), L), dtype=torch.long)
    for r, (i, e) in enumerate(exemples):
        x[r, :len(i)], y[r, :len(e)], masque[r, :len(i)] = torch.tensor(i), torch.tensor(e), 1
    with torch.random.fork_rng(devices=[]):
        torch.manual_seed(GRAINE_MODELE)
        optimiseur = torch.optim.AdamW(modele.parameters(), lr=5e-3, weight_decay=0.0)
        modele.train()
        for _ in range(pas_d_ajustement):
            optimiseur.zero_grad()
            perte = modele(input_ids=x, attention_mask=masque, labels=y).loss
            perte.backward()
            optimiseur.step()
    assert float(perte.detach()) < 0.2, f"ajustement du modèle jouet insuffisant (perte {float(perte.detach()):.3f})"
    POIDS["etat"] = {k: v.detach().clone() for k, v in modele.state_dict().items()}


def ecrire_configs_du_modele(dossier: Path, nettoyage=True, vocabulaire=None) -> None:
    dossier.mkdir(parents=True, exist_ok=True)
    (dossier / "tokenizer_config.json").write_text(json.dumps({"clean_up_tokenization_spaces": nettoyage}), encoding="utf-8")
    v = len(jetoniseur_jouet()) if vocabulaire is None else vocabulaire
    (dossier / "config.json").write_text(json.dumps({"vocab_size": v}), encoding="utf-8")


class ChargeurJouet:
    def __init__(self, dossier_config: Path, nettoyage: bool = True, nom: str = "jouet", revision: str = "jouet-0",
                 saboter=None):
        self.config = Path(dossier_config) / "tokenizer_config.json"
        self.config_modele = Path(dossier_config) / "config.json"
        self.nettoyage, self.nom, self.revision, self.saboter = nettoyage, nom, revision, saboter
        self.poids_charges = False
        self.tok = None

    def empreintes(self):
        return {n: empreinte(c) for n, c in (("tokenizer_config.json", self.config), ("config.json", self.config_modele))
                if c.is_file()}

    def dossiers_du_modele(self):
        return [self.config.parent]

    def jetoniseur(self):
        self.tok = jetoniseur_jouet(self.nettoyage)
        return P.JetoniseurCharge(self.tok, self.nom, self.revision, self.config, self.empreintes(),
                                  [str(c) for c in (self.config, self.config_modele) if c.is_file()],
                                  config_modele=self.config_modele)

    def poids(self):
        self.poids_charges = True
        modele = modele_neuf(self.tok)
        if self.saboter is not None:
            self.saboter(modele)
        return P.ModeleCharge(modele, self.nom, self.revision, self.empreintes(),
                              [str(c) for c in (self.config, self.config_modele) if c.is_file()])


def etat_aleatoire(modele_injecte, graine: int) -> dict:
    g = torch.Generator().manual_seed(graine)
    return {k: (torch.randn(v.shape, generator=g) * 0.03).to(torch.float16) for k, v in etat_lora(modele_injecte).items()}


def ecrire_scelle(chemin: Path, texte: str) -> str:
    chemin.parent.mkdir(parents=True, exist_ok=True)
    chemin.write_text(texte, encoding="utf-8")
    return sceller(chemin)


def contenu_extrait(run_id: str, dossier_rel: str, dossier: Path, versions=None) -> dict:
    lots = [{"adaptateur": c.adaptateur, "condition": c.nom, "dose_apres": c.dose, "dose_avant": c.dose,
             "empreinte": "e" * 64, "lot": k} for c in CONDITIONS for k in (1, 2)]
    noms = [NOM_IDS] + sorted(set(NOMS_ADAPTATEURS.values()))
    return {"avertissement": P.AVERTISSEMENT_EXTRAIT, "run_id": run_id, "commit_lancement": "0123456789abcdef" * 2 + "01234567",
            "versions": dict(sorted({"numpy": np.__version__, "python": "3", "torch": torch.__version__,
                                     **(VERSIONS if versions is None else versions)}.items())),
            "fichiers_de_la_passe": {f"{dossier_rel}/{nom}": empreinte(dossier / nom) for nom in noms},
            "etats_par_lot_evaluation": lots}


def objet_ids(cles, suites) -> dict:
    """Objet `ids` de M-1 : clés d'épisode triées, une liste de A listes par épisode."""
    par_episode: dict = {}
    for cle, s in zip(cles, suites):
        ep, _, pas = cle.rpartition("/pas")
        par_episode.setdefault(ep, {})[int(pas)] = list(s)
    return {ep: [par_episode[ep][t] for t in sorted(par_episode[ep])] for ep in sorted(par_episode)}


def ecrire_course(racine: Path, nom: str, cles, suites, adaptateurs_de: Path, modifier_extrait=None,
                  modifier_objet=None, modifier_texte=None) -> dict:
    """Fichiers de la course sous `diag/<dossier de la course>/` (M-2) et extrait scellé du côté exposé."""
    run_id = f"20261118-235959-{nom}"
    dossier_rel = f"diag/etalonnage-{nom}"
    dossier = racine / dossier_rel
    dossier.mkdir(parents=True)
    objet = {"avertissement": P.AVERTISSEMENT_IDENTIFIANTS, "ids": objet_ids(cles, suites)}
    if modifier_objet is not None:
        objet = modifier_objet(objet) or objet
    texte = json.dumps(objet, ensure_ascii=False)
    if modifier_texte is not None:
        texte = modifier_texte(texte)
    ids = dossier / NOM_IDS
    ecrire_scelle(ids, texte)
    chemins = {"ids": ids, "dossier_rel": dossier_rel}
    for a, nom_fichier in NOMS_ADAPTATEURS.items():
        c = dossier / nom_fichier
        shutil.copy(adaptateurs_de / f"adaptateur-{a}.pt", c)
        sceller(c)
        chemins[P.role_d_adaptateur(a)] = c
    contenu = contenu_extrait(run_id, dossier_rel, dossier)
    if modifier_extrait is not None:
        contenu = modifier_extrait(contenu) or contenu
    extrait = dossier / "extrait-sans-mecanisme-cote-moniteurs.json"
    chemins["sha_extrait"] = ecrire_scelle(extrait, contenu if isinstance(contenu, str) else json.dumps(contenu, sort_keys=True, ensure_ascii=False))
    chemins["extrait"] = extrait
    return chemins


def tirer_actions(tok, taches, etats, graine: int, vides: bool):
    """Joue les épisodes jouets : actions tirées du modèle sous l'adaptateur et la dose de chaque condition. Rend les
    clés, les suites et des lignes descriptives (pour les essais seulement), dans l'ordre de M-1 : clés d'épisode triées,
    puis pas."""
    modele = modele_neuf(tok)
    injecter(modele, 16, 32.0, 0)
    adaptateurs_en_simple_precision(modele)
    fmt = FormatChat(tok, fins={EOS, FIN}, variables={"date_string": "26 Jul 2024"})
    g = torch.Generator().manual_seed(graine)
    interdits = torch.tensor([0, 1, 2, 3, 134, 135])
    guide = charger_invite("H1-classification")
    triples = []
    for c in CONDITIONS:
        charger_etat(modele, etats[c.adaptateur])
        fixer_dose(modele, c.dose)
        for k, t in enumerate(taches):
            env = environnement("honnete", tache_de(t), PAS, guide, {})
            debut = (env.consigne_privee(0), env.observation(0, 0, []))
            ids, journal = fmt.ouverture(*debut), []
            for pas in range(PAS):
                if pas > 0:
                    ids = ids + fmt.tour(debut, env.observation(0, pas, journal))
                n = int(torch.randint(5, MAX_JETONS, (1,), generator=g))
                action = []
                with torch.no_grad():
                    sortie = modele(torch.tensor([ids]), use_cache=True)
                    for _ in range(n):
                        logits = sortie.logits[0, -1].float().clone()
                        logits[interdits] = -1e9
                        action.append(int(torch.multinomial(torch.softmax(logits, -1), 1, generator=g)))
                        sortie = modele(torch.tensor([[action[-1]]]), past_key_values=sortie.past_key_values, use_cache=True)
                if c.nom == "H" and k == 0 and pas == 0:
                    action = action[:3] + tok(" , .", add_special_tokens=False)["input_ids"] + action[3:5]   # nettoyage
                if c.nom == "B50" and k == 1 and pas == 1:
                    action = (action * 3)[:MAX_JETONS]              # action de longueur maximale, sans jeton de fin
                elif vides and k == 2 and pas == 1:
                    action = [FIN]
                else:
                    action = action + [FIN]
                texte = tok.decode(action, skip_special_tokens=True, clean_up_tokenization_spaces=True)
                cle = f"evaluation-{c.nom}/{t['identifiant']}/pas{pas}"
                triples.append((cle, action, {"phase": f"evaluation-{c.nom}", "episode": t["identifiant"],
                                              "tache": t["identifiant"], "condition": c.nom, "pas": pas, "texte": texte}))
                ids = ids + action + fmt.cloture(debut, action)
                journal.append((0, pas, texte))
    triples.sort(key=lambda x: (x[0].rpartition("/pas")[0], x[2]["pas"]))
    return [x[0] for x in triples], [x[1] for x in triples], [x[2] for x in triples]


def sondes_jouets(rng):
    def lin(nom, couche, famille="lineaire"):
        return SondeLineaireJetons(nom, couche, "max", rng.standard_normal(LARGEUR), float(rng.standard_normal()), None, famille)

    legeres = [lin("remplissage-a", 2), lin("tromperie-c2", 2, "difference_moyennes"), lin("tromperie-c1", 1, "difference_moyennes"),
               lin("enjeux-c2", 2), lin("tromperie-c3", 3, "difference_moyennes"), lin("enjeux-c1", 1)]
    neuves = [lin("dissimulation-c1", 1), lin("dissimulation-c3", 3), lin("dissimulation-c2", 2)]
    neuves += [lin(f"dissimulation-c2-plancher-{k}", 2, "plancher") for k in range(N_PLANCHER)]
    planchers = [lin(f"{nom}-c2-t07-plancher-{k}", 2, "plancher") for nom in ("tromperie", "enjeux") for k in range(N_PLANCHER)]
    return {"legeres": legeres, "neuves": neuves, "planchers": planchers}


def sha_vecteur(s) -> str:
    return hashlib.sha256(np.ascontiguousarray(s.w, dtype=np.float64).tobytes()).hexdigest()


N15 = effectif_sous_echantillon(N_ACTIONS, 2)
N7 = effectif_sous_echantillon(N_ACTIONS, 8)


def spec_jouet(sondes, empreintes_sondes, empreinte_taches, empreintes_config) -> P.Specification:
    leg, neu = sondes["legeres"], sondes["neuves"]
    return dataclasses.replace(
        P.SPECIFICATION_TEXTE, nom="jouet", modele="jouet", revision="jouet-0", n_couches=COUCHES_JOUET, largeur=LARGEUR,
        fins=(EOS, FIN), premier_jeton_cloture=FIN, jeton_debut=1, type_poids="float32",
        empreintes_fichiers_modele=tuple(sorted(empreintes_config.items())), max_jetons_action=MAX_JETONS,
        n_taches=N_TACHES, pas_par_episode=PAS, lot=4, couches=(1, 2, 3), couche_decisive=2,
        pas_sous_echantillon_decisif=2, pas_sous_echantillon_descriptif=8, n15=N15, n7=N7,
        sondes_decisives=(
            P.SondeDecisive("tromperie-c2", "legeres", 1, sha_vecteur(leg[1]), leg[1].empreinte(), "planchers",
                            "tromperie-c2-t07-plancher-"),
            P.SondeDecisive("enjeux-c2", "legeres", 3, sha_vecteur(leg[3]), leg[3].empreinte(), "planchers",
                            "enjeux-c2-t07-plancher-"),
            P.SondeDecisive("dissimulation-c2", "neuves", 2, sha_vecteur(neu[2]), neu[2].empreinte(), "neuves", None)),
        sondes_descriptives=(
            P.SondeDescriptive("dissimulation-c1", "neuves", 1), P.SondeDescriptive("dissimulation-c3", "neuves", 3),
            P.SondeDescriptive("tromperie-c1", "legeres", 1), P.SondeDescriptive("tromperie-c3", "legeres", 3),
            P.SondeDescriptive("enjeux-c1", "legeres", 1), P.SondeDescriptive("enjeux-c3", "legeres", 3)),
        n_plancher=N_PLANCHER, empreintes_fichiers_sondes=tuple(sorted(empreintes_sondes.items())),
        empreinte_taches=empreinte_taches, chemin_taches=CHEMIN_TACHES, taille_morceau=30_000)


def table_jouet(spec: P.Specification, **remplacements) -> dict:
    """Table de la forme de la table neuve (programme de comparaison v2), aux constantes du monde jouet."""
    constantes = {
        "T": spec.n_taches, "E": 1, "A": spec.pas_par_episode, "J": spec.max_jetons_action, "L": spec.lot,
        "K": len(spec.conditions), "m": 2, "N": N_ACTIONS, "N_c": N_TACHES * PAS,
        "conditions": [{"nom": c.nom, "role": r, "adaptateur": c.adaptateur, "dose": c.dose}
                       for c, r in zip(spec.conditions, ("référence honnête", "sabotée", "sabotée", "témoin-jumeau"))],
        "reference_honnete": "H", "temoin_jumeau": "TJ100", "condition_de_la_phrase_du_dommage": "B100",
        "conditions_sabotees": ["B50", "B100"], "ordre_des_conditions": [c.nom for c in spec.conditions],
        "k": 1, "pas_couche_decisive": spec.pas_sous_echantillon_decisif,
        "pas_couches_descriptives": spec.pas_sous_echantillon_descriptif, "n15": spec.n15, "n7": spec.n7,
        "taille_de_pire_cas": 1, "place_libre": 2_000_000_000 + spec.disque_transitoire,
        "budget_recette_puissance_heures": 12,
        "extrait_des_etats": {"paires": {}, "nombre_d_etats": 13, "cles_de_la_regle_b": []}, "nombre_d_etats": 13,
        "noms_de_fichiers": {"identifiants": spec.nom_fichier_identifiants, "textes": "", "prefixe_phase": spec.prefixe_phase,
                             "adaptateurs": dict(spec.fichiers_adaptateurs), "extrait_des_etats": "etats-lectures-iib-v1.json",
                             "oracle": "evaluation-iib-v5.json"},
        "taches": {"chemin": spec.chemin_taches, "sha256": spec.empreinte_taches},
        "adaptateurs": {"rang": spec.rang, "alpha": spec.alpha, "projections": list(spec.cibles)},
        "invites": [spec.invite], "motifs_de_chemins_prives_ajoutes": list(spec.motifs_prives_ajoutes)}
    a_changer = remplacements.pop("constantes", {})
    if a_changer is None:
        constantes = None
    else:
        constantes.update(a_changer)
    champs = [{"champ": c, "statut": P.STATUT_COUVERT, "regle": "M-1, M-4"} for c in P.CHAMPS_COUVERTS_ADDITIF_2]
    champs += [{"champ": "identifiants.fichier", "statut": "report", "regle": "RP-11"}]
    table = {"avertissement": "table jouet", "mot_d_ensemble": "report", "champs_changes": champs,
             "structure_des_roles_tenue": True, "pas_rp7_trouve": True, "motifs_noeud": [], "constantes": constantes}
    table.update(remplacements)
    return table


TEXTE_PREREG = "\n\n".join(f"## {s}\n\nTexte jouet de la section." for s in (
    "Hypothèse", "Prédiction chiffrée et signe attendu", "Métrique", "Seuil", "Plan d'analyse",
    "Critères de lecture gelés", "Liste d'arrêt")) + (
    "\n\n## Contre-lecture\n\n- **Contre-lecture 1** — brouillon " + "a" * 64 + ", rapport " + "b" * 64 + ".\n")


def git(racine: Path, *args: str) -> None:
    subprocess.run(["git", "-C", str(racine), "-c", "user.name=essai", "-c", "user.email=essai@exemple.invalid",
                    "-c", "commit.gpgsign=false", *args], check=True, capture_output=True)


def ecrire_code(monde_ou_racine, nom: str, variante: str = "sain", **pieces) -> Path:
    """Bordereau du code (écrit par la fonction de la passe) et registre propre à sa forme (huit clés) ; rend le
    registre. Lignes saines : texte (02:00), additif 1 (02:10), additif 2 (02:20), code (03:00)."""
    racine = monde_ou_racine
    defauts = {"texte_scelle": racine / "prereg" / "texte-jouet-v1.md", "rapport_conformite": racine / "docs" / "rapport-conformite-v1.md",
               "notice": racine / "docs" / "notice-v1.md", "devis": racine / "docs" / "devis-passe-v1.md", "accord": "GO-2026-11-19-01",
               "additif": racine / "prereg" / "additif-1-jouet-v1.md", "additif_2": racine / "prereg" / "additif-2-jouet-v1.md",
               "constantes": racine / "docs" / "constantes-jouet-v1.json"}
    defauts.update(pieces)
    contenu = P.contenu_du_bordereau_du_code(racine, **defauts)
    if variante == "module modifié":
        contenu["modules"]["controle_ia.gardes"]["sha256"] = "0" * 64
    if variante == "module de moins":
        del contenu["modules"]["controle_ia.gardes"]
    if variante == "clé de trop au bordereau":
        contenu["note"] = "x"
    if variante == "clé additif_2 absente du bordereau":
        del contenu["additif_2"]
    if variante == "autre texte au bordereau":
        contenu["texte_scelle"]["sha256"] = "c" * 64
    if variante == "autre additif 2 au bordereau":
        contenu["additif_2"]["sha256"] = "c" * 64
    bordereau = racine / "registres" / f"bordereau-code-{nom}.json"
    sha_b = P.ecrire_json_scelle(bordereau, contenu)
    texte = contenu["texte_scelle"] if variante != "autre texte au bordereau" else {**contenu["texte_scelle"], "sha256": empreinte(defauts["texte_scelle"])}
    add2 = contenu.get("additif_2") or {"chemin": "prereg/additif-2-jouet-v1.md", "sha256": empreinte(defauts["additif_2"])}
    if variante == "autre additif 2 au bordereau":
        add2 = {**add2, "sha256": empreinte(defauts["additif_2"])}
    scell = f"| SCELLEMENT-SONDES-IIB | 2026-11-19T02:00:00Z | {texte['chemin']} | {texte['sha256']} |"
    a1 = f"| SCELLEMENT-ADDITIF-1-SONDES-IIB | 2026-11-19T02:10:00Z | {contenu['additif']['chemin']} | {contenu['additif']['sha256']} |"
    a2 = f"| SCELLEMENT-ADDITIF-2-SONDES-IIB | 2026-11-19T02:20:00Z | {add2['chemin']} | {add2['sha256']} |"
    heure = "2026-11-19T02:15:00Z" if variante == "heure antérieure à l'additif 2" else "2026-11-19T03:00:00Z"
    code = f"| CODE-PASSE-IIB | {heure} | registres/{bordereau.name} | {'9' * 64 if variante == 'empreinte du bordereau fausse' else sha_b} |"
    ancien = f"| CODE-PASSE-IIB | 2026-11-19T02:05:00Z | registres/ancien.json | {'7' * 64} |"
    avant = f"| ETATS-COURSE-IIB | 2026-11-19T01:00:00Z | docs/etats.json | {'8' * 64} |"
    lignes = {"ligne absente": [scell, a1, a2], "code avant scellement": [code, scell, a1, a2],
              "deux lignes de code postérieures": [scell, a1, a2, code, code],
              "code antérieur seul": [scell, a1, ancien, a2],
              "code antérieur puis postérieur": [scell, ancien, a1, a2, code],
              "code avant l'additif 2 par le rang": [scell, a1, code, a2],
              "scellement non premier": [avant, scell, a1, a2, code],
              "colonne manquante": [scell, a1, a2, code.replace(f"| {heure} ", "")],
              "empreinte du texte fausse": [scell.replace(texte["sha256"], "d" * 64), a1, a2, code],
              "empreinte de l'additif 1 fausse": [scell, a1.replace(contenu["additif"]["sha256"], "d" * 64), a2, code],
              "scellement absent": [a1, a2, code],
              "additif 1 absent": [scell, a2, code], "additif 2 absent": [scell, a1, code],
              "additif 2 avant l'additif 1": [scell, a2.replace("02:20:00Z", "02:05:00Z"), a1, code],
              "additif 1 répété": [scell, a1, a1, a2, code]}.get(variante, [scell, a1, a2, code])
    registre = racine / "registres" / f"sondes-iib-v1-{nom}.md"
    registre.write_text("# Registre propre — texte `prereg/texte-jouet-v1.md` ; lignes ajoutées, jamais réécrites ; format : "
                        "| CLÉ | AAAA-MM-JJTHH:MM:SSZ | chemin relatif | sha256 |\n\n" + "\n".join(lignes) + "\n", encoding="utf-8")
    return registre


@dataclasses.dataclass
class Monde:
    base: Path
    racine: Path
    hors_depot: Path
    spec: P.Specification
    sondes: dict
    taches: list
    chemins: dict
    actions: tuple
    compteur: int = 0

    def __post_init__(self):
        self.courses: dict = {}

    def chargeur(self, **kw) -> ChargeurJouet:
        return ChargeurJouet(self.hors_depot, **kw)

    def params(self, **remplacements) -> P.ParametresPasse:
        self.compteur += 1
        c = self.chemins
        champs = dict(
            racine=self.racine, sortie=self.base / f"sortie-{self.compteur}",
            run_id=f"20261119-{self.compteur:06d}-passe-jouet", entropie=12345,
            extrait=c["extrait"], taches=c["taches"], sondes_legeres=c["legeres"],
            sondes_neuves=c["neuves"], planchers=c["planchers"], registre=c["registre"], registre_accords=c["accords"],
            duree_max_heures=3.0, depense_max_usd=10.0, prix_horaire_usd=3.0, debut_location=time.time() - 60.0,
            identifiant_instance="instance-jouet-1", appareil="cpu", autoriser_depot_sale=True)
        champs.update(remplacements)
        return P.ParametresPasse(**champs)

    def spec_de(self, extrait, spec=None) -> P.Specification:
        """La spécification épinglée à l'extrait d'une course jouet (M-2 : empreinte de l'extrait, dossier)."""
        spec = spec or self.spec
        course = self.courses.get(str(extrait))
        if course is None:
            return spec
        return dataclasses.replace(spec, empreinte_extrait=course["sha_extrait"], dossier_de_la_course=course["dossier_rel"])

    def passe(self, spec=None, chargeur=None, defauts=None, mode="passe", **remplacements) -> dict:
        p = self.params(**remplacements)
        return P.executer_passe(p, self.spec_de(p.extrait, spec), chargeur or self.chargeur(), mode=mode,
                                defauts_d_essai=defauts)

    def course_modifiee(self, nom: str, modifier=None, modifier_extrait=None, modifier_objet=None, modifier_texte=None) -> dict:
        """Nouvelle course dont les actions sont modifiées par `modifier(cles, suites, lignes)`."""
        cles, suites, lignes = (list(self.actions[0]), [list(s) for s in self.actions[1]],
                                [dict(l) for l in self.actions[2]])
        if modifier is not None:
            modifier(cles, suites, lignes)
        chemins = ecrire_course(self.racine, nom, cles, suites, self.depot_adaptateurs, modifier_extrait, modifier_objet,
                                modifier_texte)
        self.courses[str(chemins["extrait"])] = chemins
        return chemins


@pytest.fixture(scope="module")
def monde(tmp_path_factory) -> Monde:
    base = tmp_path_factory.mktemp("passe")
    racine, hors = base / "depot", base / "hors-depot"
    racine.mkdir()
    ecrire_configs_du_modele(hors)
    rng = np.random.default_rng(np.random.SeedSequence(7))
    taches = [{"identifiant": f"tache-{k:02d}", "questions": LETTRES[k] * 400} for k in range(N_TACHES)]
    chemin_taches = racine / CHEMIN_TACHES
    ecrire_scelle(chemin_taches, json.dumps({"taches": taches}))
    sondes = sondes_jouets(rng)
    chemins, empreintes_sondes = {"taches": chemin_taches}, {}
    for role, liste in sondes.items():
        chemins[role] = racine / "donnees" / "sondes" / f"{role}.npz"
        empreintes_sondes[role] = ecrire_sondes(chemins[role], liste, {"principales": {}})
    tok = jetoniseur_jouet()
    ajuster_modele(tok, taches)
    modele = modele_neuf(tok)
    injecter(modele, 16, 32.0, 0)
    etats = {"eleve": etat_aleatoire(modele, 1), "temoin-jumeau": etat_aleatoire(modele, 2)}
    depot_adaptateurs = base / "adaptateurs"
    depot_adaptateurs.mkdir()
    for nom, e in etats.items():
        torch.save(e, depot_adaptateurs / f"adaptateur-{nom}.pt")
    actions = tirer_actions(tok, taches, etats, 11, vides=False)
    course = ecrire_course(racine, "course", actions[0], actions[1], depot_adaptateurs)
    chemins.update(course)
    chemins["texte"] = racine / "prereg" / "texte-jouet-v1.md"
    sha_texte = ecrire_scelle(chemins["texte"], TEXTE_PREREG)
    chemins["additif"] = racine / "prereg" / "additif-1-jouet-v1.md"
    sha_additif = ecrire_scelle(chemins["additif"], TEXTE_PREREG.replace("Texte jouet de la section.", "Additif 1 jouet.", 1))
    chemins["additif_2"] = racine / "prereg" / "additif-2-jouet-v1.md"
    sha_additif_2 = ecrire_scelle(chemins["additif_2"], TEXTE_PREREG.replace("Texte jouet de la section.", "Additif 2 jouet.", 1))
    chemins["rapport"] = racine / "docs" / "rapport-conformite-v1.md"
    sha_rapport = ecrire_scelle(chemins["rapport"], "Rapport de conformité jouet.\n")
    ecrire_scelle(racine / "docs" / "notice-v1.md", "Notice jouet.\n")
    chemins["devis"] = racine / "docs" / "devis-passe-v1.md"
    sha_devis = ecrire_scelle(chemins["devis"], "Devis jouet.\n")
    chemins["accords"] = racine / "registres" / "go.md"
    chemins["accords"].parent.mkdir(parents=True)
    chemins["accords"].write_text(f"| GO-2026-11-19-01 | passe de recalcul | devis {sha_devis} |\n", encoding="utf-8")
    spec = spec_jouet(sondes, empreintes_sondes, empreinte(chemin_taches),
                      {n: empreinte(hors / n) for n in ("tokenizer_config.json", "config.json")})
    spec = dataclasses.replace(spec, empreinte_extrait=course["sha_extrait"], dossier_de_la_course=course["dossier_rel"])
    chemins["constantes"] = racine / "docs" / "constantes-jouet-v1.json"
    sha_table = ecrire_scelle(chemins["constantes"], json.dumps(table_jouet(spec), ensure_ascii=False, sort_keys=True))
    git(racine, "init", "-q")
    git(racine, "add", "-A")
    git(racine, "commit", "-q", "-m", "monde jouet")
    chemins["registre"] = ecrire_code(racine, "sain")
    m = Monde(base, racine, hors, spec, sondes, taches, chemins, actions)
    m.courses[str(course["extrait"])] = course
    m.etats = etats
    m.depot_adaptateurs = depot_adaptateurs
    m.sha = {"texte": sha_texte, "rapport": sha_rapport, "devis": sha_devis, "additif": sha_additif,
             "additif_2": sha_additif_2, "constantes": sha_table}
    return m


@pytest.fixture(scope="module")
def saine(monde) -> dict:
    """Cas sain commun à toutes les gardes : la passe entière, sans action vide."""
    r = monde.passe()
    r["params_sortie"] = Path(r["livraison"]).parent
    return r


def lire_npz_en_morceaux(livraison: Path, nom: str) -> dict:
    liste = json.loads((livraison / f"{nom}.morceaux.json").read_text(encoding="utf-8"))
    octets = b""
    for m in liste["morceaux"]:
        assert verifier(livraison / m["nom"]) == m["sha256"]
        octets += (livraison / m["nom"]).read_bytes()
    assert hashlib.sha256(octets).hexdigest() == liste["sha256"] and len(octets) == liste["taille"]
    entier = livraison / f"relu-{nom}"
    entier.write_bytes(octets)
    try:
        with np.load(entier, allow_pickle=False) as z:
            return {k: z[k] for k in z.files}
    finally:
        entier.unlink()


def lire_index(livraison: Path) -> list[dict]:
    return [json.loads(l) for l in (livraison / P.NOM_INDEX).read_text(encoding="utf-8").splitlines()]


def refus(appel, motif: str) -> GardeArret:
    with pytest.raises(GardeArret, match=motif) as e:
        appel()
    return e.value


def trace_d_arret(params_ou_sortie) -> dict:
    return json.loads((Path(params_ou_sortie) / P.NOM_TRACE_ARRET).read_text(encoding="utf-8"))


# ----------------------------------------------------------------------------------------------------------------------
# Cas sain : la livraison, ses formes, ses valeurs, sa trace.
# ----------------------------------------------------------------------------------------------------------------------

def test_cas_sain_liste_fermee_des_fichiers_et_bordereau(monde, saine):
    livraison = Path(saine["livraison"])
    bordereau = json.loads((livraison / P.NOM_BORDEREAU).read_text(encoding="utf-8"))
    assert verifier(livraison / P.NOM_BORDEREAU) == saine["bordereau_sha256"]
    noms = {f["nom"] for f in bordereau["fichiers"]}
    presents = {p.name for p in livraison.iterdir()}
    assert presents == noms | {n + ".sha256" for n in noms} | {P.NOM_BORDEREAU, P.NOM_BORDEREAU + ".sha256"}
    for f in bordereau["fichiers"]:
        assert verifier(livraison / f["nom"]) == f["sha256"] and (livraison / f["nom"]).stat().st_size == f["taille"]
    sortes = {n.split(".morceau")[0] for n in noms}
    assert sortes == {P.NOM_SCORES_ACTION, P.NOM_SCORES_JETON, P.NOM_INDEX, P.NOM_TRACE,
                      *(P.NOM_BRUT.format(couche=c) for c in monde.spec.couches)}
    assert bordereau["manifeste_sha256"] == verifier(saine["manifeste"])
    assert not (livraison.parent / P.NOM_TRACE_ARRET).exists()
    assert sum(".morceau-" in n for n in noms) > len(sortes) - 2          # plusieurs morceaux pour un fichier au moins
    assert saine["taille_totale"] <= monde.spec.taille_max


def test_cas_sain_index_et_sous_echantillons(monde, saine):
    lignes = lire_index(Path(saine["livraison"]))
    cles, suites, textes = monde.actions
    assert [l["cle"] for l in lignes] == cles and [l["rang"] for l in lignes] == list(range(len(cles)))
    assert all(tuple(sorted(l)) == tuple(sorted(P.CHAMPS_INDEX)) for l in lignes)
    for l, s, t in zip(lignes, suites, textes):
        assert l["jetons_notes"] == (len(s) - 1 if s[-1] in (EOS, FIN) else len(s))
        assert (l["condition"], l["tache"], l["episode"], l["pas"]) == (t["condition"], t["tache"], t["episode"], t["pas"])
        assert l["jetons_contexte"] > 0
    triees = sorted(l["cle"] for l in lignes if l["jetons_notes"] > 0)
    for champ, pas in (("sous_echantillon_couche_decisive", 2), ("sous_echantillon_couches_descriptives", 8)):
        attendu = {c for k, c in enumerate(triees) if k % pas == 0 or k == len(triees) - 1}
        assert {l["cle"] for l in lignes if l[champ]} == attendu
    assert sum(l["sous_echantillon_couche_decisive"] for l in lignes) == len(cles) // 2 + 1
    assert any(l["jetons_notes"] == MAX_JETONS for l in lignes)               # action de longueur maximale, sans fin


def test_cas_sain_scores_recalcules_sur_processeur_par_le_harnais(monde, saine):
    """Le produit et les agrégations de la carte, contre le recalcul du harnais (`score_action`, maximum) et la moyenne
    du bras de diagnostic, sur l'activité brute livrée ; tolérance de la garde de réception r6 du texte."""
    livraison = Path(saine["livraison"])
    lignes = lire_index(livraison)
    sa = lire_npz_en_morceaux(livraison, P.NOM_SCORES_ACTION)
    sj = lire_npz_en_morceaux(livraison, P.NOM_SCORES_JETON)
    directions = json.loads(bytes(sa["directions"]).decode("utf-8"))
    colonnes = json.loads(bytes(sj["colonnes"]).decode("utf-8"))
    par_nom = {s.nom: s for liste in monde.sondes.values() for s in liste}
    assert sa["scores"].shape == (len(lignes), len(directions), 2) and sa["scores"].dtype == np.float64
    assert sj["scores"].shape == (sum(l["jetons_notes"] for l in lignes), len(colonnes)) and sj["scores"].dtype == np.float64
    assert [d["nom"] for d in directions][:1 + N_PLANCHER] == ["tromperie-c2"] + [f"tromperie-c2-t07-plancher-{k}" for k in range(N_PLANCHER)]
    assert len(directions) == 3 * (1 + N_PLANCHER) + 5 and len(colonnes) == 8
    assert all(d["empreinte"] == par_nom[d["nom"]].empreinte() and d["couche"] == par_nom[d["nom"]].couche for d in directions)
    assert np.all(np.isfinite(sa["scores"])) and np.all(sa["scores"][:, :, 0] >= sa["scores"][:, :, 1])
    bornes = np.concatenate([[0], np.cumsum([l["jetons_notes"] for l in lignes])])
    # sur toutes les actions : maximum des scores par jeton livrés égal sans tolérance, moyenne à 1e-9 près (garde r7)
    for l in lignes:
        bloc = sj["scores"][bornes[l["rang"]]:bornes[l["rang"] + 1]]
        for j, col in enumerate(colonnes):
            k = [d["nom"] for d in directions].index(col["nom"])
            assert bloc[:, j].max() == sa["scores"][l["rang"], k, 0]
            assert abs(bloc[:, j].mean() - sa["scores"][l["rang"], k, 1]) <= 1e-9 * np.abs(bloc[:, j]).max()
    controlees = 0
    for couche in monde.spec.couches:
        brut = lire_npz_en_morceaux(livraison, P.NOM_BRUT.format(couche=couche))
        champ = "sous_echantillon_couche_decisive" if couche == 2 else "sous_echantillon_couches_descriptives"
        assert set(brut) == {f"a{l['rang']:05d}" for l in lignes if l[champ]}
        for cle, h in brut.items():
            rang = int(cle[1:])
            assert h.dtype == np.float32 and h.shape == (lignes[rang]["jetons_notes"], LARGEUR)
            for k, d in enumerate(directions):
                if d["couche"] != couche:
                    continue
                s = par_nom[d["nom"]]
                e = (np.abs(h.astype(np.float64) * s.w).sum(axis=1) + abs(s.b)).max()
                assert abs(score_action(s, h, 0, h.shape[0]) - sa["scores"][rang, k, 0]) <= 1e-9 * e
                assert abs(s.scores_par_jeton(h).mean() - sa["scores"][rang, k, 1]) <= 1e-9 * e
                if d["nom"] in [c["nom"] for c in colonnes]:
                    j = [c["nom"] for c in colonnes].index(d["nom"])
                    assert np.all(np.abs(s.scores_par_jeton(h) - sj["scores"][bornes[rang]:bornes[rang + 1], j]) <= 1e-9 * e)
                controlees += 1
    assert controlees > 100


def test_cas_sain_couche_contexte_et_adaptateur_contre_la_passe_unique_du_harnais(monde, saine):
    """L'activité brute livrée est celle de la couche nommée, du contexte rebâti par la recette et de l'adaptateur de la
    condition : comparée à une passe indépendante (`harnais.activations.passe_unique`, `transcription_honnete`)."""
    livraison = Path(saine["livraison"])
    lignes = lire_index(livraison)
    tok = jetoniseur_jouet()
    fmt = FormatChat(tok, fins={EOS, FIN}, variables={"date_string": "26 Jul 2024"})
    modele = modele_neuf(tok)
    injecter(modele, 16, 32.0, 5)
    adaptateurs_en_simple_precision(modele)
    cles, suites, textes = monde.actions
    guide = charger_invite("H1-classification")
    bruts = {c: lire_npz_en_morceaux(livraison, P.NOM_BRUT.format(couche=c)) for c in monde.spec.couches}
    vus = set()
    for l in [l for l in lignes if l["sous_echantillon_couches_descriptives"]]:
        cond = next(c for c in CONDITIONS if c.nom == l["condition"])
        charger_etat(modele, monde.etats[cond.adaptateur])
        fixer_dose(modele, cond.dose)
        episode = sorted((t["pas"], s) for t, s in zip(textes, suites) if (t["condition"], t["tache"]) == (l["condition"], l["tache"]))
        env = environnement("honnete", tache_de(next(t for t in monde.taches if t["identifiant"] == l["tache"])), PAS, guide, {})
        ids, empans = transcription_honnete(fmt, env, [s for _, s in episode])
        d, f = empans[l["pas"]]
        assert d == l["jetons_contexte"]
        acts = passe_unique(modele, ids[:f], (0, 1, 2, 3))
        for c in monde.spec.couches:
            np.testing.assert_allclose(bruts[c][f"a{l['rang']:05d}"], acts[c][d:d + l["jetons_notes"]], rtol=2e-4, atol=2e-5)
            autre = acts[c - 1 if c > 1 else 0][d:d + l["jetons_notes"]]
            assert not np.allclose(bruts[c][f"a{l['rang']:05d}"], autre, rtol=1e-2, atol=1e-3)          # pas une autre couche
        vus.add(l["condition"])
    assert vus == {c.nom for c in CONDITIONS}
    h = [l for l in lignes if l["condition"] == "H"][0]
    b = [l for l in lignes if l["condition"] == "B100" and l["tache"] == h["tache"] and l["pas"] == 0][0]
    assert h["jetons_contexte"] == b["jetons_contexte"]


def test_cas_sain_trace_liste_fermee_et_gardes_tenues(monde, saine):
    trace = json.loads((Path(saine["livraison"]) / P.NOM_TRACE).read_text(encoding="utf-8"))
    assert trace["course"] == {"run_id": "20261118-235959-course", "commit_lancement": "0123456789abcdef" * 2 + "01234567"}
    assert set(trace) == {"gardes", "modules_charges", "course", "modele", "jetoniseur", "premier_jeton_cloture",
                          "clean_up_tokenization_spaces", "empreinte_tokenizer_config", "versions_jetonisation",
                          "fichiers_sondes", "sondes", "conditions", "adaptateurs", "repetabilite",
                          "controle_du_contexte", "chemins_lus", "chemin_prive_lu", "taille_livraison",
                          "duree_secondes", "identifiant_instance"}
    assert set(trace["gardes"]) == set(P.GARDES)
    for g in trace["gardes"].values():
        assert set(g) == {"etat", "actions_vues", "actions_controlees"} and g["etat"] == "tenue"
    n = len(monde.actions[0])
    assert trace["gardes"]["P3"]["actions_controlees"] == 3 * n and trace["gardes"]["P5"]["actions_controlees"] > n
    assert trace["modules_charges"] == P.modules_charges()
    assert trace["modele"] == {"nom": "jouet", "revision": "jouet-0"} and trace["premier_jeton_cloture"] == FIN
    assert trace["clean_up_tokenization_spaces"] is True
    assert trace["empreinte_tokenizer_config"] == empreinte(monde.hors_depot / "tokenizer_config.json")
    assert trace["versions_jetonisation"] == VERSIONS
    assert trace["sondes"]["enjeux-c3"] == "absente" and trace["sondes"]["tromperie-c2"] == "lue"
    assert sum(v == "lue" for v in trace["sondes"].values()) == 8
    for c in CONDITIONS:
        assert trace["conditions"][c.nom] == {
            "adaptateur_et_dose_relus_egaux": "oui", "actions": N_TACHES * PAS, "actions_sans_jeton_note": 0,
            "jetons_notes": sum(l["jetons_notes"] for l in lire_index(Path(saine["livraison"])) if l["condition"] == c.nom)}
    for nom in ("eleve", "temoin-jumeau"):
        assert trace["adaptateurs"][nom] == {"empreinte": empreinte(monde.chemins[P.role_d_adaptateur(nom)]),
                                             "egale_a_l_extrait": "oui"}
    assert 0.0 <= trace["repetabilite"]["plus_grand_centile_99"] <= 0.2
    assert trace["repetabilite"]["controle_negatif"]["tenu"] == "oui"
    assert trace["controle_du_contexte"]["fraction"] >= 0.95 and trace["controle_du_contexte"]["artefact"]["fraction"] < 0.95
    assert trace["controle_du_contexte"]["actions_controlees"] >= 10
    assert trace["chemin_prive_lu"] == "non" and trace["chemins_lus"] >= 20
    assert trace["identifiant_instance"] == "instance-jouet-1"
    texte = json.dumps(trace)
    assert "adaptateur-eleve-iib-v5.pt" not in texte and str(monde.racine) not in texte


def test_cas_sain_manifeste_graines_et_journal(monde, saine):
    manifeste = json.loads(Path(saine["manifeste"]).read_text(encoding="utf-8"))
    assert set(manifeste["graines"]) == {"repetabilite-passe", "injection-adaptateurs"}
    assert all(g["entropie"] == "12345" for g in manifeste["graines"].values())
    assert manifeste["decisif"] is True and manifeste["preenregistrement"]["sha256"] == monde.sha["texte"]
    assert manifeste["config"]["sondes_lues"]["tromperie-c2"] == "lue"
    assert f"diag/etalonnage-course/{NOM_IDS}" in manifeste["config"]["liste_fermee_des_chemins_lus"]
    assert manifeste["config"]["pieces_de_p0"]["additif_2"] == monde.sha["additif_2"]
    assert manifeste["config"]["pieces_de_p0"]["constantes"] == monde.sha["constantes"]
    assert manifeste["config"]["course"]["run_id"] == "20261118-235959-course"
    assert manifeste["config"]["pieces_de_p0"]["accord"] == "GO-2026-11-19-01"
    journal = monde.racine / "diag" / manifeste["run_id"] / "journal-passe-barreau8-v1.json"
    contenu = json.loads(journal.read_text(encoding="utf-8"))["resultat"]
    assert contenu["bordereau_sha256"] == saine["bordereau_sha256"]
    assert set(contenu["empreintes_des_adaptateurs_relues_sur_le_modele"]) == {c.nom for c in CONDITIONS}
    interdits = ("oracle", "manifeste.json", "resume.json", "consigne")
    assert not any(m in c for c in contenu["chemins_lus"] for m in interdits)


def test_cas_sain_livraison_identique_sous_une_autre_entropie_et_action_vide_dans_chaque_condition(monde, saine):
    """Deux preuves en une passe : (1) l'artefact du texte « une action sans jeton noté dans chaque condition » ;
    (2) rien de la livraison ne dépend de l'entropie (comparée, hors actions modifiées, au cas sain)."""
    cles, suites, lignes = monde.actions
    vides = [k for k, l in enumerate(lignes) if l["tache"] == "tache-02" and l["pas"] == 1]

    def vider(c, s, l):
        for k in vides:
            s[k] = [FIN]
            l[k]["texte"] = ""

    course = monde.course_modifiee("course-vides", vider)
    r = monde.passe(entropie=999, extrait=course["extrait"])
    livraison = Path(r["livraison"])
    index = lire_index(livraison)
    sa = lire_npz_en_morceaux(livraison, P.NOM_SCORES_ACTION)["scores"]
    sj = lire_npz_en_morceaux(livraison, P.NOM_SCORES_JETON)["scores"]
    assert [l["rang"] for l in index if l["jetons_notes"] == 0] == vides and len(vides) == 4
    assert np.all(np.isnan(sa[vides])) and np.all(np.isfinite(np.delete(sa, vides, axis=0)))
    assert sj.shape[0] == sum(l["jetons_notes"] for l in index)
    assert not any(l["sous_echantillon_couche_decisive"] or l["sous_echantillon_couches_descriptives"]
                   for l in index if l["jetons_notes"] == 0)
    trace = r["trace"]
    assert all(trace["conditions"][c.nom]["actions_sans_jeton_note"] == 1 for c in CONDITIONS)
    assert all(g["etat"] == "tenue" for g in trace["gardes"].values())
    # même épisode : les actions qui précèdent l'action vidée ont les mêmes scores que dans le cas sain, au bit près
    sa0 = lire_npz_en_morceaux(Path(saine["livraison"]), P.NOM_SCORES_ACTION)["scores"]
    avant = [k for k, l in enumerate(lignes) if not (l["tache"] == "tache-02" and l["pas"] >= 1)]
    np.testing.assert_allclose(sa[avant], sa0[avant], rtol=1e-4, atol=1e-5)
    autres = [k for k, l in enumerate(lignes) if l["tache"] == "tache-02" and l["pas"] == 2]
    assert not np.allclose(sa[autres], sa0[autres], rtol=1e-6, atol=1e-7)     # le contexte du pas suivant a changé


def test_determinisme_des_fichiers_de_donnees(monde, saine):
    r = monde.passe(entropie=4242)
    a, b = Path(saine["livraison"]), Path(r["livraison"])
    noms = sorted(p.name for p in a.iterdir() if P.NOM_TRACE not in p.name and P.NOM_BORDEREAU not in p.name)
    assert noms == sorted(p.name for p in b.iterdir() if P.NOM_TRACE not in p.name and P.NOM_BORDEREAU not in p.name)
    assert all((a / n).read_bytes() == (b / n).read_bytes() for n in noms)


# ----------------------------------------------------------------------------------------------------------------------
# Paramètres, entropie, ligne de commande.
# ----------------------------------------------------------------------------------------------------------------------

def test_entropie_obligatoire_et_sortie_existante(monde):
    refus(lambda: monde.passe(entropie=None), "entropie racine")
    existante = monde.base / "sortie-existante"
    existante.mkdir()
    refus(lambda: monde.passe(sortie=existante), "existe déjà")


def test_ligne_de_commande_refuse_un_parametre_absent_et_liste_les_modules(monde, capsys):
    refus(lambda: P.principal(["passe", "--racine", str(monde.racine)]), "paramètres obligatoires absents")
    assert P.principal(["empreintes-modules"]) == 0
    sortie = capsys.readouterr().out
    assert "controle_ia.barreau8_moniteurs.passe_recalcul_v6" in sortie and "passe_recalcul_v5" not in sortie and "controle_ia.premier_test_ia.figees" in sortie


def test_verifier_les_entrees_joue_tout_ce_qui_se_peut_sans_les_poids_et_n_ecrit_rien(monde, saine):
    chargeur = monde.chargeur()
    p = monde.params()
    r = P.executer_passe(p, monde.spec, chargeur, mode="entrees")
    n = len(monde.actions[0])
    assert r["entrees"] == "conformes" and r["mesures"]["actions"] == n and not chargeur.poids_charges
    assert chargeur.tok is not None                                       # le jetoniseur seul a été chargé
    assert r["gardes"]["P3"] == {"etat": "tenue", "actions_vues": 3 * n, "actions_controlees": 3 * n}
    assert r["gardes"]["P2"]["etat"] == "non jouée" and r["gardes"]["P10"]["etat"] == "non jouée"
    assert r["mesures"]["plus_longue_transcription_en_jetons"] > 1500 and r["mesures"]["sous_echantillon_couche_decisive"] == n // 2 + 1
    assert r["mesures"] == saine["mesures"]                               # les mêmes mesures que la passe entière
    assert not p.sortie.exists() and not (monde.racine / "runs" / p.run_id).exists()
    # sans les poids, les identifiants (P3 c, borne du vocabulaire) et les pièces du gabarit sont déjà refusés
    faux = monde.course_modifiee("entrees-vocabulaire", _egal_a_v)
    refus(lambda: monde.passe(mode="entrees", extrait=faux["extrait"]), "égal ou supérieur à V")
    refus(lambda: monde.passe(mode="entrees", spec=dataclasses.replace(monde.spec, premier_jeton_cloture=EOS)),
          "garde P3 non tenue : premier jeton de la clôture")
    refus(lambda: monde.passe(mode="entrees", spec=dataclasses.replace(monde.spec, marque_ouverture="Today Date: 27 Jul 2024")),
          "marque figée")
    refus(lambda: P.executer_passe(monde.params(), monde.spec, monde.chargeur(), mode="autre"), "mode 'autre' inconnu")


def test_essai_a_blanc_sans_les_poids_joue_les_controles_de_fin_et_ne_livre_rien(monde, saine):
    chargeur = monde.chargeur()
    p = monde.params()
    r = P.executer_passe(p, monde.spec, chargeur, mode="blanc")
    assert not chargeur.poids_charges and r["mode"] == "blanc"
    assert sorted(x.name for x in p.sortie.iterdir()) == [P.NOM_RAPPORT_A_BLANC, P.NOM_RAPPORT_A_BLANC + ".sha256"]
    rapport = json.loads((p.sortie / P.NOM_RAPPORT_A_BLANC).read_text(encoding="utf-8"))
    assert verifier(p.sortie / P.NOM_RAPPORT_A_BLANC) == r["rapport_sha256"]
    assert {g: v["etat"] for g, v in rapport["gardes"].items()} == {
        "P0": "tenue", "P1": "tenue", "P2": "non jouée", "P3": "tenue", "P4": "non jouée", "P5": "tenue", "P6": "tenue",
        "P7": "non jouée", "P8": "tenue", "P9": "tenue", "P10": "non jouée"}
    # les tailles de la livraison factice sont celles de la vraie livraison (mêmes formes, mêmes noms)
    vraie = Path(saine["livraison"])
    attendues = {x.name: x.stat().st_size for x in vraie.iterdir()
                 if not x.name.endswith(".sha256") and P.NOM_TRACE not in x.name and P.NOM_BORDEREAU not in x.name}
    assert rapport["tailles_des_fichiers_de_donnees"] == attendues
    assert abs(rapport["taille_totale_de_la_livraison"] - saine["taille_totale"]) < 2000
    assert rapport["mesures"] == saine["mesures"] and rapport["chemin_prive_lu"] == "non"
    journal = monde.racine / "diag" / p.run_id / "journal-essai-a-blanc-passe-barreau8-v1.json"
    assert json.loads(journal.read_text(encoding="utf-8"))["resultat"]["essai_a_blanc"] is True
    assert json.loads((monde.racine / "runs" / p.run_id / "manifeste.json").read_text(encoding="utf-8"))["config"]["mode"] == "blanc"
    # un contrôle de fin qui refuserait la passe est vu sans carte : réserve trop petite pour la trace et le bordereau
    p = monde.params()
    refus(lambda: P.executer_passe(p, dataclasses.replace(monde.spec, reserve_trace_et_bordereau=200), monde.chargeur(), mode="blanc"),
          "garde P9 non tenue : la trace, le bordereau et leurs compagnons")
    assert trace_d_arret(p.sortie)["gardes"]["P9"]["etat"] == "non tenue" and trace_d_arret(p.sortie)["mode"] == "blanc"


def test_module_lance_par_python_m_porte_au_bordereau_et_modification_refusee(monde, tmp_path):
    """EN SOUS-PROCESSUS, comme l'exécutante le lancera : lancé par `python -m`, le module de la passe s'appelle
    `__main__` ; il doit figurer sous le nom de son paquet dans la liste des modules, au bordereau du code, et une
    modification de son fichier doit être refusée à l'ouverture (garde P0)."""
    nom = "controle_ia.barreau8_moniteurs.passe_recalcul_v6"
    env = {**os.environ, "PYTHONPATH": str(Path(P.__file__).resolve().parents[2])}

    def lancer(*args, pythonpath=None):
        e = env if pythonpath is None else {**env, "PYTHONPATH": str(pythonpath)}
        return subprocess.run([sys.executable, "-m", nom, *[str(a) for a in args]], env=e, capture_output=True, text=True,
                              timeout=150, cwd=str(tmp_path))

    r = lancer("empreintes-modules")
    assert r.returncode == 0 and f"{empreinte(P.__file__)}  {nom}" in r.stdout.splitlines()
    assert "__main__" not in r.stdout
    # copie des seuls modules chargés par la passe, pour pouvoir modifier le fichier du module sans toucher au dépôt
    src = Path(P.__file__).resolve().parents[2]
    copie = tmp_path / "copie" / "src"
    for fichier in P.fichiers_des_modules().values():
        cible = copie / Path(fichier).resolve().relative_to(src)
        cible.parent.mkdir(parents=True, exist_ok=True)
        shutil.copy(fichier, cible)
    module_copie = copie / "controle_ia" / "barreau8_moniteurs" / "passe_recalcul_v6.py"
    d = monde.racine / "docs"
    bordereau = monde.racine / "registres" / "bordereau-code-sous-processus.json"
    r = lancer("bordereau-code", "--racine", monde.racine, "--texte-scelle", monde.chemins["texte"], "--rapport-conformite",
               d / "rapport-conformite-v1.md", "--notice", d / "notice-v1.md", "--devis", d / "devis-passe-v1.md",
               "--accord", "GO-2026-11-19-01", "--bordereau", bordereau, "--additif", monde.chemins["additif"],
               "--additif-2", monde.chemins["additif_2"], "--constantes", monde.chemins["constantes"], pythonpath=copie)
    assert r.returncode == 0, r.stderr
    modules = json.loads(bordereau.read_text(encoding="utf-8"))["modules"]
    assert modules[nom] == {"chemin": str(module_copie), "sha256": empreinte(module_copie)} and "__main__" not in modules
    registre = monde.racine / "registres" / "sondes-iib-v1-sous-processus.md"
    registre.write_text(f"| SCELLEMENT-SONDES-IIB | 2026-11-19T02:00:00Z | prereg/texte-jouet-v1.md | {monde.sha['texte']} |\n"
                        f"| SCELLEMENT-ADDITIF-1-SONDES-IIB | 2026-11-19T02:10:00Z | prereg/additif-1-jouet-v1.md | {monde.sha['additif']} |\n"
                        f"| SCELLEMENT-ADDITIF-2-SONDES-IIB | 2026-11-19T02:20:00Z | prereg/additif-2-jouet-v1.md | {monde.sha['additif_2']} |\n"
                        f"| CODE-PASSE-IIB | 2026-11-19T03:00:00Z | registres/{bordereau.name} | {empreinte(bordereau)} |\n",
                        encoding="utf-8")
    c = monde.chemins
    args = ["verifier-entrees", "--racine", monde.racine, "--sortie", tmp_path / "sortie", "--run-id", "20261119-010101-sous-processus",
            "--entropie", "1", "--extrait", c["extrait"], "--taches", c["taches"], "--sondes-legeres", c["legeres"],
            "--sondes-neuves", c["neuves"], "--planchers", c["planchers"], "--registre", registre, "--registre-accords",
            c["accords"], "--duree-max-heures", "3", "--depense-max-usd", "10", "--prix-horaire-usd", "3",
            "--debut-location", time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime(time.time() - 60)), "--identifiant-instance", "instance-jouet", "--appareil", "cpu"]
    # fichier intact : la garde d'ouverture est tenue (la passe s'arrête juste après, parce que la ligne de commande
    # emploie la spécification du texte, dont les constantes de forme diffèrent de la table jouet : ligne 24)
    r = lancer(*args, pythonpath=copie)
    assert r.returncode == 1 and "constantes de forme du code différentes de la table neuve" in r.stderr, r.stderr
    assert "garde P0 non tenue" not in r.stderr
    # fichier du module modifié d'une ligne après l'écriture du bordereau : refusé à l'ouverture
    with open(module_copie, "a", encoding="utf-8") as f:
        f.write("\n# ligne ajoutée après le bordereau du code\n")
    r = lancer(*args, pythonpath=copie)
    assert r.returncode == 1 and "garde P0 non tenue : modules chargés ≠ modules du bordereau du code" in r.stderr
    assert nom in r.stderr and "__main__" not in r.stderr


# ----------------------------------------------------------------------------------------------------------------------
# Trace : aucune ligne « tenue » sans que la garde ait tourné.
# ----------------------------------------------------------------------------------------------------------------------

def test_trace_saine_et_artefacts():
    t = P.TraceGardes()
    t.controle("P5", True, "cause", vues=2, controlees=1)
    t.clore("P5")
    assert t.etat("P5") == "tenue"
    refus(lambda: t.clore("P6"), "une garde n'est tenue que si elle a tourné")          # jamais jouée
    refus(lambda: t.controle("P5", True, "x"), "déjà close")
    refus(lambda: t.controle("P7", False, "écart trop grand"), "garde P7 non tenue : écart trop grand")
    refus(lambda: t.clore("P7"), "impossible d'écrire")
    refus(lambda: t.pour_livraison(), "aucune livraison")
    arret = t.pour_arret()
    assert arret["P7"] == {"etat": "non tenue", "actions_vues": 0, "actions_controlees": 0, "cause": "écart trop grand"}
    assert arret["P0"]["etat"] == "non jouée"
    refus(lambda: t.controle("P11", True, "x"), "inconnue")

    def lever():
        with t.sous("P1"):
            raise GardeArret("fichier absent")

    refus(lever, "fichier absent")
    assert t.etat("P1") == "non tenue"


# ----------------------------------------------------------------------------------------------------------------------
# Garde P0 : registre, code, accord.
# ----------------------------------------------------------------------------------------------------------------------

@pytest.mark.parametrize("variante, motif", [
    ("ligne absente", "0 ligne.s. CODE-PASSE-IIB strictement postérieure"),
    ("scellement absent", "ligne SCELLEMENT-SONDES-IIB absente"),
    ("additif 1 absent", "ligne SCELLEMENT-ADDITIF-1-SONDES-IIB absente"),
    ("additif 2 absent", "ligne SCELLEMENT-ADDITIF-2-SONDES-IIB absente"),
    ("additif 2 avant l'additif 1", "SCELLEMENT-ADDITIF-2-SONDES-IIB n'est pas strictement postérieure"),
    ("additif 1 répété", "clé SCELLEMENT-ADDITIF-1-SONDES-IIB répétée"),
    ("heure antérieure à l'additif 2", "0 ligne.s. CODE-PASSE-IIB strictement postérieure"),
    ("code avant l'additif 2 par le rang", "0 ligne.s. CODE-PASSE-IIB strictement postérieure"),
    ("code antérieur seul", "0 ligne.s. CODE-PASSE-IIB strictement postérieure.*1 ligne.s. antérieure"),
    ("code avant scellement", "n'est pas la première des lignes de clé"),
    ("deux lignes de code postérieures", "2 ligne.s. CODE-PASSE-IIB strictement postérieure"),
    ("empreinte du bordereau fausse", "n'est pas celle du bordereau du code"),
    ("empreinte du texte fausse", "SCELLEMENT-SONDES-IIB n'est pas celle du texte scellé présent"),
    ("empreinte de l'additif 1 fausse", "SCELLEMENT-ADDITIF-1-SONDES-IIB n'est pas celle du texte scellé présent"),
    ("module modifié", r"modules chargés ≠ modules du bordereau du code .*controle_ia.gardes"),
    ("module de moins", r"modules chargés ≠ modules du bordereau du code .*controle_ia.gardes"),
    ("scellement non premier", "n'est pas la première des lignes de clé"),
    ("colonne manquante", "3 colonne.s. au lieu de quatre"),
    ("clé de trop au bordereau", "forme hors de la liste fermée"),
    ("clé additif_2 absente du bordereau", "forme hors de la liste fermée"),
    ("autre texte au bordereau", "ne cite pas, à sa clé texte_scelle"),
    ("autre additif 2 au bordereau", "ne cite pas, à sa clé additif_2"),
])
def test_p0_artefacts_du_registre_et_du_bordereau_du_code(monde, variante, motif):
    registre = ecrire_code(monde.racine, variante.replace(" ", "-").replace("é", "e"), variante)
    p = monde.params(registre=registre)
    chargeur = monde.chargeur()
    refus(lambda: P.executer_passe(p, monde.spec, chargeur), motif)
    arret = trace_d_arret(p.sortie)
    assert arret["gardes"]["P0"]["etat"] == "non tenue" and arret["livraison"] == "aucune"
    assert arret["gardes"]["P1"]["etat"] == "non jouée"                                      # rien d'autre n'a été ouvert
    assert chargeur.tok is None and not (p.sortie / "livraison").exists()


def test_p0_lecture_du_registre_propre():
    h = "a" * 64
    sain = ("# Registre propre — texte `prereg/t.md` ; format : | CLÉ | AAAA-MM-JJTHH:MM:SSZ | chemin relatif | sha256 |\n\n"
            f"| SCELLEMENT-SONDES-IIB | 2026-11-19T02:00:00Z | prereg/t.md | {h} |\n"
            f"| SCELLEMENT-ADDITIF-1-SONDES-IIB | 2026-11-19T02:00:01Z | prereg/a1.md | {h} |\n"
            f"| CODE-PASSE-IIB | 2026-11-19T02:00:02Z | registres/ancien.json | {h} |\n"
            f"| SCELLEMENT-ADDITIF-2-SONDES-IIB | 2026-11-19T02:00:03Z | prereg/a2.md | {h} |\n"
            f"| CODE-PASSE-IIB | 2026-11-19T02:00:04Z | registres/b.json | {h} |\n"
            f"| LIVRAISON-PASSE-IIB | 2026-11-19T05:00:00Z | livraison/b.json | {h} |\n")
    lignes = P.lire_registre_propre(sain)
    assert list(lignes) == ["SCELLEMENT-SONDES-IIB", "SCELLEMENT-ADDITIF-1-SONDES-IIB", "CODE-PASSE-IIB",
                            "SCELLEMENT-ADDITIF-2-SONDES-IIB", "LIVRAISON-PASSE-IIB"]
    comptees, anterieures = P.lignes_comptees(lignes, "CODE-PASSE-IIB")
    assert [l["chemin"] for l in comptees] == ["registres/b.json"] and [l["chemin"] for l in anterieures] == ["registres/ancien.json"]
    assert comptees[0]["secondes"] - lignes["SCELLEMENT-SONDES-IIB"][0]["secondes"] == 4.0
    assert P.lignes_comptees(lignes, "ETATS-COURSE-IIB") == ([], [])
    for faux, motif in ((sain.replace("T02:00:04Z", "T02:00Z"), "heure UTC à la seconde"),
                        (sain.replace("registres/b.json", "/abs/b.json"), "chemin relatif"),
                        (sain.replace("registres/b.json", "../b.json"), "chemin relatif"),
                        (sain.replace(f"registres/b.json | {h}", f"registres/b.json | {h[:63]}"), "empreinte entière"),
                        (sain.replace(f"registres/b.json | {h} |", f"registres/b.json | {h} | {h} |"), "5 colonne"),
                        (sain + f"| SCELLEMENT-ADDITIF-2-SONDES-IIB | 2026-11-19T06:00:00Z | x | {h} |\n", "clé SCELLEMENT-ADDITIF-2-SONDES-IIB répétée"),
                        (sain + f"| CODE-PASSE-IIB-BIS | 2026-11-19T06:00:00Z | x | {h} |\n", "clé hors des huit")):
        refus(lambda: P.lire_registre_propre(faux), motif)


def test_p0_artefacts_accord_devis_texte_et_modules(monde):
    racine = monde.racine
    refus(lambda: monde.passe(registre=ecrire_code(racine, "accord-absent", accord="GO-2026-11-19-02")),
          "0 ligne.s. du registre des accords ont pour première cellule GO-2026-11-19-02")
    # une ligne, et une seule, dont la PREMIÈRE cellule est l'identifiant ; les autres lignes qui le citent ne comptent pas
    sain = monde.chemins["accords"].read_text(encoding="utf-8")
    assert P.lignes_d_accord(sain, "GO-2026-11-19-01") == [sain.strip()]
    citation = f"| GO-2026-11-19-07 | rappel de GO-2026-11-19-01 | devis {monde.sha['devis']} |\nGO-2026-11-19-01 hors tableau\n"
    assert P.lignes_d_accord(sain + citation, "GO-2026-11-19-01") == [sain.strip()]              # sain : citations ignorées
    assert P.lignes_d_accord(citation, "GO-2026-11-19-01") == [] and P.lignes_d_accord(sain, "GO-2026-11-19-0") == []

    def avec_accords(nom: str, contenu: str):
        chemin = monde.base / f"go-{nom}.md"
        chemin.write_text(contenu, encoding="utf-8")
        p = monde.params(registre_accords=chemin)
        return p, (lambda: P.executer_passe(p, monde.spec, monde.chargeur(), mode="entrees"))

    assert avec_accords("citations", sain + citation)[1]()["entrees"] == "conformes"              # sain dans la passe
    refus(avec_accords("double", sain + sain)[1], "2 ligne.s. du registre des accords ont pour première cellule")
    refus(avec_accords("seconde-cellule", citation)[1], "0 ligne.s. du registre des accords")
    autre = f"| GO-2026-11-19-01 | passe | devis {'f' * 64} |\n| GO-2026-11-19-07 | cite GO-2026-11-19-01 | devis {monde.sha['devis']} |\n"
    refus(avec_accords("devis-ailleurs", autre)[1], "ne cite pas l'empreinte du devis")
    refus(lambda: ecrire_code(racine, "accord-oral", accord="accord oral"), "GO-AAAA-MM-JJ-NN attendu")
    autre = racine / "docs" / "devis-autre-v1.md"
    ecrire_scelle(autre, "Autre devis.\n")
    refus(lambda: monde.passe(registre=ecrire_code(racine, "devis-autre", devis=autre)), "ne cite pas l'empreinte du devis")
    # pièce modifiée après l'écriture du bordereau (rapport de conformité)
    rapport = racine / "docs" / "rapport-b-v1.md"
    ecrire_scelle(rapport, "Rapport B.\n")
    registre = ecrire_code(racine, "rapport-b", rapport_conformite=rapport)
    rapport.write_text("Rapport B, modifié.\n", encoding="utf-8")
    refus(lambda: monde.passe(registre=registre), "empreinte .* ≠ scellée")
    compagnon(rapport).unlink()
    sceller(rapport)
    refus(lambda: monde.passe(registre=registre), "rapport_conformite : l'empreinte sur disque n'est pas celle du bordereau")
    # texte non conforme (champ ouvert), texte non scellé
    ouvert = racine / "prereg" / "texte-ouvert-v1.md"
    ecrire_scelle(ouvert, TEXTE_PREREG.replace("Texte jouet de la section.", "À REMPLIR", 1))
    refus(lambda: ecrire_code(racine, "texte-ouvert", texte_scelle=ouvert), "non conforme")
    non_scelle = racine / "prereg" / "texte-non-scelle-v1.md"
    non_scelle.write_text(TEXTE_PREREG, encoding="utf-8")
    refus(lambda: ecrire_code(racine, "texte-non-scelle", texte_scelle=non_scelle), "empreinte compagnon")
    # texte altéré après son scellement et après la ligne de registre
    copie = racine / "prereg" / "texte-copie-v1.md"
    ecrire_scelle(copie, TEXTE_PREREG)
    registre = ecrire_code(racine, "texte-copie", texte_scelle=copie)
    copie.write_text(TEXTE_PREREG + "\nAjout.\n", encoding="utf-8")
    refus(lambda: monde.passe(registre=registre), "empreinte .* ≠ scellée")
    t = P.TraceGardes()
    modules = P.modules_charges()
    P.verifier_modules_inchanges(t, modules)                                             # sain
    refus(lambda: P.verifier_modules_inchanges(t, {**modules, "controle_ia.gardes": "0" * 64}), "modules chargés ont changé")
    b = P.lire_bordereau_du_code(racine / "registres" / "bordereau-code-sain.json")      # sain : forme fermée
    assert tuple(sorted(b)) == P.CLES_DU_BORDEREAU_DU_CODE and set(b["modules"]) == set(modules) and len(b["commit"]) == 40


def test_ligne_de_commande_ecrit_le_bordereau_du_code(monde, capsys):
    sortie = monde.racine / "registres" / "bordereau-code-cli.json"
    d = monde.racine / "docs"
    assert P.principal(["bordereau-code", "--racine", str(monde.racine), "--texte-scelle", str(monde.chemins["texte"]),
                        "--rapport-conformite", str(d / "rapport-conformite-v1.md"), "--notice", str(d / "notice-v1.md"),
                        "--devis", str(d / "devis-passe-v1.md"), "--accord", "GO-2026-11-19-01", "--bordereau", str(sortie),
                        "--additif", str(monde.chemins["additif"]), "--additif-2", str(monde.chemins["additif_2"]),
                        "--constantes", str(monde.chemins["constantes"])]) == 0
    assert verifier(sortie) in capsys.readouterr().out
    assert json.loads(sortie.read_text(encoding="utf-8")) == json.loads(
        (monde.racine / "registres" / "bordereau-code-sain.json").read_text(encoding="utf-8"))
    refus(lambda: P.principal(["bordereau-code", "--racine", str(monde.racine)]), "paramètres obligatoires absents")


# ----------------------------------------------------------------------------------------------------------------------
# Garde P1 : entrées vérifiées par empreinte ; forme fermée de l'extrait du côté exposé.
# ----------------------------------------------------------------------------------------------------------------------

def _sans(cle):
    def f(e):
        del e[cle]
    return f


def _avec(chemin, valeur):
    def f(e):
        o = e
        for k in chemin[:-1]:
            o = o[k]
        o[chemin[-1]] = valeur
    return f


def _fichier_renomme(e):
    k = next(k for k in e["fichiers_de_la_passe"] if k.endswith(NOM_IDS))
    e["fichiers_de_la_passe"][k.split("/")[-1]] = e["fichiers_de_la_passe"].pop(k)


def _lots_desordonnes(e):
    e["etats_par_lot_evaluation"].reverse()


@pytest.mark.parametrize("nom, modifier, motif", [
    ("cle-manquante", _sans("versions"), "clés de premier niveau"),
    ("cle-en-trop", _avec(["resume"], {}), "clés de premier niveau"),
    ("avertissement", _avec(["avertissement"], "EXPLORATOIRE"), "avertissement différent"),
    ("run-id", _avec(["run_id"], "Course_1"), "run_id hors de la forme"),
    ("commit", _avec(["commit_lancement"], "ABC"), "commit_lancement"),
    ("version-inconnue", _avec(["versions", "pandas"], "2"), "versions"),
    ("version-non-chaine", _avec(["versions", "numpy"], 2), "versions"),
    ("fichier-de-trop", _avec(["fichiers_de_la_passe", "diag/etalonnage-course/oracle-iib-evaluation.json"], "a" * 64), "exactement les 3 chemins"),
    ("nom-de-base", _fichier_renomme, "exactement les 3 chemins"),
    ("empreinte-courte", lambda e: e["fichiers_de_la_passe"].update({k: "a" * 63 for k in list(e["fichiers_de_la_passe"])[:1]}), "exactement les 3 chemins"),
    ("chemin-sous-donnees", lambda e: e.update(fichiers_de_la_passe={k.replace("diag/etalonnage-course", "donnees/20261118-235959-course"): v
                                                                    for k, v in e["fichiers_de_la_passe"].items()}), "exactement les 3 chemins"),
    ("quatrieme-cle-textes", _avec(["fichiers_de_la_passe", "diag/etalonnage-course/textes-actions-iib-evaluation.jsonl"], "a" * 64), "exactement les 3 chemins"),
    ("lots-vides", _avec(["etats_par_lot_evaluation"], []), "liste non vide"),
    ("lot-cle-en-trop", lambda e: e["etats_par_lot_evaluation"][0].update(cout=1), "ligne 0 : clés hors de"),
    ("lot-dose", lambda e: e["etats_par_lot_evaluation"][2].update(dose_apres=1.0), "ligne 2 : adaptateur ou dose ≠ ceux de la condition B50"),
    ("lot-adaptateur", lambda e: e["etats_par_lot_evaluation"][0].update(adaptateur="temoin-jumeau"), "adaptateur ou dose ≠ ceux de la condition H"),
    ("lot-condition", lambda e: e["etats_par_lot_evaluation"][0].update(condition="B25"), "hors de la table"),
    ("lot-zero", lambda e: e["etats_par_lot_evaluation"][0].update(lot=0), "type ou forme d'un champ"),
    ("lot-dose-chaine", lambda e: e["etats_par_lot_evaluation"][0].update(dose_avant="0"), "type ou forme d'un champ"),
    ("lots-ordre", _lots_desordonnes, "non rangées par condition puis par lot"),
    ("cle-repetee", lambda e: json.dumps(e).replace('"run_id"', '"run_id": "20261118-235959-x", "run_id"', 1), "clé répétée"),
    ("illisible", lambda e: "{", "JSON illisible"),
])
def test_p1_forme_de_l_extrait_du_cote_expose_artefacts(monde, nom, modifier, motif):
    sain = contenu_extrait("20261118-235959-course", monde.chemins["dossier_rel"], monde.chemins["ids"].parent)
    r = P.lire_extrait_du_cote_expose(json.dumps(sain), monde.spec)                                      # sain
    assert r["run_id"] == "20261118-235959-course" and set(r["fichiers"]) == {"ids", "adaptateur_eleve", "adaptateur_temoin_jumeau"}
    assert r["fichiers"]["ids"] == {"chemin": f"diag/etalonnage-course/{NOM_IDS}", "sha256": empreinte(monde.chemins["ids"])}
    assert r["versions"]["transformers"] == VERSIONS["transformers"]
    faux = modifier(sain) or sain
    refus(lambda: P.lire_extrait_du_cote_expose(faux if isinstance(faux, str) else json.dumps(faux), monde.spec), motif)


def test_p1_artefacts(monde):
    c = monde.chemins
    # (0) extrait de forme fausse, dans la passe : refus avant tout calcul, trace d'arrêt
    faux = monde.course_modifiee("extrait-faux", modifier_extrait=_sans("versions"))
    p = monde.params(extrait=faux["extrait"])
    chargeur = monde.chargeur()
    refus(lambda: P.executer_passe(p, monde.spec_de(p.extrait), chargeur), "clés de premier niveau")
    arret = trace_d_arret(p.sortie)
    assert arret["gardes"]["P1"]["etat"] == "non tenue" and arret["gardes"]["P3"]["etat"] == "non jouée" and chargeur.tok is None
    # (1) fichier de la course altéré après son scellement (compagnon non conforme)
    alteree = monde.course_modifiee("alteree")
    with open(alteree["ids"], "a", encoding="utf-8") as f:
        f.write("\n")
    refus(lambda: monde.passe(extrait=alteree["extrait"]), "empreinte .* ≠ scellée")
    # (2) fichier scellé et intact, mais d'une empreinte autre que celle de l'extrait
    autre = monde.course_modifiee("autre", modifier_extrait=lambda e: e["fichiers_de_la_passe"].update(
        {k: "a" * 64 for k in e["fichiers_de_la_passe"] if k.endswith(NOM_IDS)}))
    refus(lambda: monde.passe(extrait=autre["extrait"]), f"{NOM_IDS} : empreinte sur disque ≠ empreinte de l'extrait")
    # (3) compagnon absent ; fichier absent ; extrait non scellé
    sans = monde.course_modifiee("sans-compagnon")
    compagnon(sans["ids"]).unlink()
    refus(lambda: monde.passe(extrait=sans["extrait"]), "empreinte compagnon .* absente")
    absent = monde.course_modifiee("fichier-absent")
    absent["adaptateur_eleve"].unlink()
    refus(lambda: monde.passe(extrait=absent["extrait"]), "fichier absent")
    nu = monde.course_modifiee("extrait-nu")
    compagnon(nu["extrait"]).unlink()
    refus(lambda: monde.passe(extrait=nu["extrait"]), "empreinte compagnon .* absente")
    # (3 bis) l'extrait d'une course désigne les fichiers de SA course : un extrait copié ailleurs n'y change rien
    assert P.garde_p1(monde.params(), monde.spec, P.TraceGardes())["ids"] == empreinte(c["ids"])       # sain
    # (4) fichier de sondes d'une autre empreinte que la table ; tâches d'une autre empreinte que la note
    spec = dataclasses.replace(monde.spec, empreintes_fichiers_sondes=tuple(
        (r, "0" * 64 if r == "planchers" else h) for r, h in monde.spec.empreintes_fichiers_sondes))
    refus(lambda: monde.passe(spec=spec), "« planchers » : empreinte ≠ celle de la table")
    # tâches : une empreinte de la spécification différente de la table est une constante de forme différente (ligne 24)
    refus(lambda: monde.passe(spec=dataclasses.replace(monde.spec, empreinte_taches="0" * 64)),
          "constantes de forme du code différentes de la table neuve : .'empreinte_taches'")
    autres = monde.racine / "donnees" / "taches" / "autres-taches-evaluation.json"
    ecrire_scelle(autres, monde.chemins["taches"].read_text(encoding="utf-8"))
    refus(lambda: monde.passe(taches=autres), "tâches d'évaluation : chemin ≠ donnees/taches/taches-evaluation.json")
    # (5) extrait d'une autre empreinte que celle que l'additif 2 épingle : la passe ne part pas
    p = monde.params()
    refus(lambda: P.executer_passe(p, dataclasses.replace(monde.spec, empreinte_extrait="0" * 64), monde.chargeur()),
          "épingle")
    assert trace_d_arret(p.sortie)["gardes"]["P1"]["etat"] == "non tenue"


# ----------------------------------------------------------------------------------------------------------------------
# Garde P3 : alignement, décodage, réglage lu.
# ----------------------------------------------------------------------------------------------------------------------

def _passe_sur(monde, nom, modifier=None, **kw):
    course = monde.course_modifiee(nom, modifier, modifier_objet=kw.pop("modifier_objet", None),
                                   modifier_texte=kw.pop("modifier_texte", None))
    chargeur = kw.pop("chargeur", None) or monde.chargeur()
    p = monde.params(extrait=course["extrait"])
    return p, chargeur, (lambda: P.executer_passe(p, monde.spec_de(p.extrait, kw.get("spec")), chargeur))


def _rang(monde, cle):
    return monde.actions[0].index(cle)


def _egal_a_v(c, s, l):
    s[4] = s[4][:1] + [len(jetoniseur_jouet())] + s[4][1:]


def _remplacer_identifiant(valeur):
    def f(c, s, l):
        s[4] = s[4][:1] + [valeur] + s[4][2:]
    return f


def _trop_longue(c, s, l):
    k = next(k for k, x in enumerate(s) if x[-1] == FIN)
    s[k] = (s[k][:-1] * 3)[:MAX_JETONS + 1]


def _vide(c, s, l):
    s[6] = []


def _courte_sans_fin(c, s, l):
    k = next(k for k, x in enumerate(s) if x[-1] == FIN)
    s[k] = s[k][:-1]


def _fin_interieure(c, s, l):
    s[9] = s[9][:2] + [EOS] + s[9][2:]


def _cles_non_triees(o):
    ids = o["ids"]
    cles = list(ids)
    cles[0], cles[-1] = cles[-1], cles[0]
    o["ids"] = {k: ids[k] for k in cles}


def _troisieme_cle(o):
    o["resume"] = {}


def _avertissement_altere(o):
    o["avertissement"] = "EXPLORATOIRE"


def _condition_hors_table(o):
    ids = o["ids"]
    k = next(k for k in ids if k.startswith("evaluation-B50/"))
    o["ids"] = dict(sorted({**{x: v for x, v in ids.items() if x != k}, k.replace("B50", "B25"): ids[k]}.items()))


def _episode_hors_taches(o):
    ids = o["ids"]
    k = next(k for k in ids if k.startswith("evaluation-H/"))
    o["ids"] = dict(sorted({**{x: v for x, v in ids.items() if x != k}, k.replace("tache-0", "autre-0"): ids[k]}.items()))


def _tache_absente(o):
    ids = o["ids"]
    del ids[next(k for k in ids if k.startswith("evaluation-TJ100/"))]


def _pas_de_moins(o):
    k = next(iter(o["ids"]))
    o["ids"][k] = o["ids"][k][:-1]


def _pas_de_plus(o):
    k = next(iter(o["ids"]))
    o["ids"][k] = o["ids"][k] + [o["ids"][k][-1]]


def _cle_repetee(texte):
    return texte.replace('"avertissement"', '"avertissement": "x", "avertissement"', 1)


def _hors_evaluation(o):
    ids = o["ids"]
    k = next(iter(ids))
    o["ids"] = dict(sorted({**{x: v for x, v in ids.items() if x != k}, k.replace("evaluation-", "etalonnage-"): ids[k]}.items()))


@pytest.mark.parametrize("nom, modifier, objet, texte, motif, avant_jetoniseur", [
    ("p3-cle-repetee", None, None, _cle_repetee, "clé répétée", True),
    ("p3-avertissement", None, _avertissement_altere, None, "avertissement différent", True),
    ("p3-troisieme-cle", None, _troisieme_cle, None, "exactement deux clés de premier niveau", True),
    ("p3-non-triees", None, _cles_non_triees, None, "non rangées dans l'ordre du tri", True),
    ("p3-condition-hors-table", None, _condition_hors_table, None, "phase hors du préfixe suivi d'une condition", True),
    ("p3-hors-evaluation", None, _hors_evaluation, None, "phase hors du préfixe", True),
    ("p3-episode-hors-taches", None, _episode_hors_taches, None, "l'épisode n'est pas l'une des T tâches", True),
    ("p3-tache-absente", None, _tache_absente, None, "clés d'épisode : K × T × E", True),
    ("p3-pas-de-moins", None, _pas_de_moins, None, "exactement A = 3 listes", True),
    ("p3-pas-de-plus", None, _pas_de_plus, None, "exactement A = 3 listes", True),
    ("p3-booleen", _remplacer_identifiant(True), None, None, "n'est pas un entier JSON", True),
    ("p3-virgule", _remplacer_identifiant(5.0), None, None, "n'est pas un entier JSON", True),
    ("p3-chaine", _remplacer_identifiant("5"), None, None, "n'est pas un entier JSON", True),
    ("p3-negatif", _remplacer_identifiant(-1), None, None, "n'est pas un entier JSON", True),
    ("p3-egal-a-v", _egal_a_v, None, None, "égal ou supérieur à V", False),
    ("p3-vide", _vide, None, None, "0 identifiants", True),
    ("p3-trop-longue", _trop_longue, None, None, "13 identifiants", True),
    ("p3-courte-sans-fin", _courte_sans_fin, None, None, "ni jeton de fin en dernière position", True),
    ("p3-fin-interieure", _fin_interieure, None, None, "jeton de fin avant la dernière position", True),
])
def test_p3_artefacts_du_fichier_des_identifiants(monde, nom, modifier, objet, texte, motif, avant_jetoniseur):
    """Additif 2, M-1 et M-5 : chaque artefact est refusé, avant le chargement des poids."""
    p, chargeur, appel = _passe_sur(monde, nom, modifier, modifier_objet=objet, modifier_texte=texte)
    refus(appel, motif)
    arret = trace_d_arret(p.sortie)
    assert arret["gardes"]["P3"]["etat"] == "non tenue" and not chargeur.poids_charges        # avant les poids
    assert (chargeur.tok is None) == avant_jetoniseur
    assert arret["gardes"]["P2"]["etat"] == "non jouée"


def test_p3_versions_de_jetonisation_egales_a_l_extrait(monde):
    """M-1, clause (b), point 1 : version différente ou clé absente de l'extrait : « non tenue » avant toute action et
    avant le chargement des poids."""
    t = P.TraceGardes()
    assert P.garde_p3_versions(dict(VERSIONS, numpy="1"), t) == VERSIONS                                 # sain
    for nom, versions in (("v-autre-transformers", dict(VERSIONS, transformers="5.17.0")),
                          ("v-autre-tokenizers", dict(VERSIONS, tokenizers="0.23.1")),
                          ("v-sans-tokenizers", {"transformers": VERSIONS["transformers"]}),
                          ("v-sans-les-deux", {})):
        course = monde.course_modifiee(nom, modifier_extrait=lambda e, v=versions: e.update(
            versions=dict(sorted({"numpy": np.__version__, "python": "3", **v}.items()))))
        chargeur = monde.chargeur()
        p = monde.params(extrait=course["extrait"])
        refus(lambda: P.executer_passe(p, monde.spec_de(p.extrait), chargeur), "absente de l'objet versions|version de .* chargée")
        arret = trace_d_arret(p.sortie)
        assert arret["gardes"]["P3"]["etat"] == "non tenue" and arret["gardes"]["P3"]["actions_controlees"] == 0
        assert chargeur.tok is None and not chargeur.poids_charges
    # versions chargées simulées différentes de celles de l'extrait (machine mal réglée)
    p = monde.params()
    refus(lambda: P.executer_passe(p, monde.spec, monde.chargeur(),
                                   defauts_d_essai={"versions_chargees": dict(VERSIONS, transformers="4.0.0")}),
          "remettre la machine à cette version")


def test_p3_ordre_des_actions_et_champs_tires_de_la_cle(monde, saine):
    """M-1 : l'ordre de parcours est celui des clés d'épisode triées, puis des pas ; phase, condition, épisode et tâche
    se tirent de la clé ; le texte du journal est le décodage explicite."""
    lignes = lire_index(Path(saine["livraison"]))
    assert [l["cle"] for l in lignes] == monde.actions[0]
    assert monde.actions[0][0].startswith("evaluation-B100/") and monde.actions[0][-1].startswith("evaluation-TJ100/")
    for l in lignes:
        phase, episode, pas = l["cle"].split("/")
        assert (l["condition"], l["episode"], l["tache"], l["pas"]) == (phase[len("evaluation-"):], episode, episode, int(pas[3:]))
    t = P.TraceGardes()
    actions = P.garde_p3_structure(monde.spec, P.lire_identifiants(monde.chemins["ids"]), monde.taches, t)
    tok = jetoniseur_jouet()
    P.garde_p3_decodage(tok, actions, True, t)
    assert [a.texte for a in actions] == [x["texte"] for x in monde.actions[2]]


def test_p3_reglage_du_nettoyage_des_espaces_lu_dans_le_fichier(monde):
    spec = monde.spec
    # sain, unité : valeur lue dans le fichier, après comparaison d'empreinte
    t = P.TraceGardes()
    j = monde.chargeur().jetoniseur()
    assert P.lire_nettoyage_des_espaces(spec, j, t) == (True, empreinte(j.config))
    tok = j.tok
    ids = tok("a , b .", add_special_tokens=False)["input_ids"]
    assert P.decoder_action(tok, ids, True) == "a, b." and P.decoder_action(tok, ids, False) == "a , b ."

    def avec_config(nom: str, contenu: str, meme_empreinte: bool):
        d = monde.base / nom
        d.mkdir()
        (d / "tokenizer_config.json").write_text(contenu, encoding="utf-8")
        shutil.copy(monde.hors_depot / "config.json", d / "config.json")
        s = spec if not meme_empreinte else dataclasses.replace(spec, empreintes_fichiers_modele=(
            ("config.json", empreinte(d / "config.json")), ("tokenizer_config.json", empreinte(d / "tokenizer_config.json"))))
        return ChargeurJouet(d), s

    # artefact : copie du fichier de configuration sans le champ → non tenue avant toute action, avant les poids
    for nom, contenu, motif in (("config-sans-champ", "{}", "ne porte pas le champ clean_up_tokenization_spaces"),
                                ("config-non-booleen", '{"clean_up_tokenization_spaces": "true"}', "n'est pas un booléen"),
                                ("config-illisible", "pas du json", "ne porte pas le champ")):
        chargeur, s = avec_config(nom, contenu, True)
        p = monde.params()
        refus(lambda: P.executer_passe(p, s, chargeur), motif)
        arret = trace_d_arret(p.sortie)
        assert arret["gardes"]["P3"]["etat"] == "non tenue" and not chargeur.poids_charges
        assert arret["gardes"]["P3"]["actions_controlees"] == 2 * len(monde.actions[0])        # (a), (c) et vocabulaire
    # artefact : fichier de configuration du jetoniseur absent → non tenue avant toute action, avant les poids
    vide = monde.base / "config-absente"
    vide.mkdir()
    shutil.copy(monde.hors_depot / "config.json", vide / "config.json")
    chargeur = ChargeurJouet(vide)
    p = monde.params()
    refus(lambda: P.executer_passe(p, spec, chargeur), "tokenizer_config.json de la révision absent sur disque")
    arret = trace_d_arret(p.sortie)
    assert arret["gardes"]["P3"]["etat"] == "non tenue" and not chargeur.poids_charges
    assert arret["gardes"]["P3"]["actions_controlees"] == 2 * len(monde.actions[0])
    # artefact : config.json absent, ou sans vocab_size → non tenue avant le réglage, avant les poids
    sans_config = monde.base / "config-modele-absente"
    sans_config.mkdir()
    shutil.copy(monde.hors_depot / "tokenizer_config.json", sans_config / "tokenizer_config.json")
    chargeur = ChargeurJouet(sans_config)
    p = monde.params()
    refus(lambda: P.executer_passe(p, spec, chargeur), "config.json de la révision absent sur disque")
    assert not chargeur.poids_charges
    d = monde.base / "config-modele-sans-vocabulaire"
    ecrire_configs_du_modele(d)
    (d / "config.json").write_text("{}", encoding="utf-8")
    s = dataclasses.replace(spec, empreintes_fichiers_modele=(("config.json", empreinte(d / "config.json")),
                                                              ("tokenizer_config.json", empreinte(d / "tokenizer_config.json"))))
    refus(lambda: monde.passe(spec=s, chargeur=ChargeurJouet(d)), "vocab_size absent")
    refus(lambda: monde.passe(spec=dataclasses.replace(spec, empreintes_fichiers_modele=(
        ("config.json", "0" * 64), ("tokenizer_config.json", empreinte(monde.hors_depot / "tokenizer_config.json"))))),
        "config.json : empreinte ≠")
    # artefact : empreinte du fichier différente de celle de la note
    chargeur, s = avec_config("config-autre-empreinte", '{"clean_up_tokenization_spaces": true, "x": 1}', False)
    refus(lambda: monde.passe(spec=s, chargeur=chargeur), "tokenizer_config.json : empreinte ≠")
    assert not chargeur.poids_charges
    # artefact : même champ inversé, sur une action où le nettoyage change un espace → arrêt à la première action où
    # le décodage au réglage lu diffère du décodage par défaut (le jetoniseur garde son réglage par défaut) ; clé seule
    chargeur, s = avec_config("config-inversee", '{"clean_up_tokenization_spaces": false}', True)
    p = monde.params()
    e = refus(lambda: P.executer_passe(p, s, chargeur), "action de clé evaluation-.* : décodage au réglage lu ≠ décodage par défaut")
    assert "nettoyage des espaces lu : False" in str(e) and not chargeur.poids_charges
    differentes = [k for k, x in enumerate(monde.actions[1])
                   if tok.decode(x, skip_special_tokens=True, clean_up_tokenization_spaces=False)
                   != tok.decode(x, skip_special_tokens=True, clean_up_tokenization_spaces=True)]
    k = _rang(monde, "evaluation-H/tache-00/pas0")
    assert k in differentes and f"action de clé {monde.actions[0][differentes[0]]} :" in str(e)
    assert monde.actions[2][differentes[0]]["texte"] not in str(e) or monde.actions[2][differentes[0]]["texte"] == ""
    assert trace_d_arret(p.sortie)["gardes"]["P3"]["etat"] == "non tenue"
    brut = tok.decode(monde.actions[1][k], skip_special_tokens=True, clean_up_tokenization_spaces=False)
    texte = monde.actions[2][k]["texte"]
    assert texte != brut and texte.replace(" ", "") == brut.replace(" ", "")                   # un espace nettoyé seul
    # artefact : un appel de décodage qui refuse le paramètre → non tenue, aucun autre décodage essayé

    class SansParametre:
        def decode(self, ids, skip_special_tokens=False):
            return ""

    t = P.TraceGardes()
    a = P.Action(0, "evaluation-H/t/pas0", "evaluation-H", "t", "t", "H", 0, "", [5, FIN])
    refus(lambda: P.garde_p3_decodage(SansParametre(), [a], True, t), "refuse le paramètre clean_up_tokenization_spaces")
    assert t.etat("P3") == "non tenue"
    # le texte du journal est le décodage explicite
    t = P.TraceGardes()
    b = P.Action(0, "evaluation-H/t/pas0", "evaluation-H", "t", "t", "H", 0, "", tok("a , b .", add_special_tokens=False)["input_ids"])
    P.garde_p3_decodage(jetoniseur_jouet(True), [b], True, t)
    assert b.texte == "a, b."


# ----------------------------------------------------------------------------------------------------------------------
# Atelier : les objets de la passe, bâtis par ses propres fonctions, pour éprouver les gardes une à une.
# ----------------------------------------------------------------------------------------------------------------------

@dataclasses.dataclass
class Atelier:
    spec: P.Specification
    trace: P.TraceGardes
    modele: object
    tok: object
    fmt: object
    actions: list
    episodes: dict
    adaptateurs: P.Adaptateurs
    directions: list


def atelier(monde, spec=None) -> Atelier:
    spec = spec or monde.spec
    trace = P.TraceGardes()
    p = monde.params()
    P.garde_p1(p, spec, trace)
    actions = P.garde_p3_structure(spec, P.lire_identifiants(p.ids), monde.taches, trace)
    chargeur = monde.chargeur()
    j = chargeur.jetoniseur()
    P.garde_p3_decodage(j.tok, actions, True, trace)
    charge = chargeur.poids()
    fmt = P.former_format(spec, j.tok, charge.modele)
    P.garde_p2(spec, j, charge, fmt, P.debut_d_episode(spec, monde.taches[0]), trace)
    episodes = P.rebatir_episodes(spec, fmt, monde.taches, actions, trace)
    adaptateurs = P.Adaptateurs(spec, charge.modele, p.fichiers_adaptateurs(), 3, trace)
    _, directions = P.regle_des_sondes_lues(spec, p.fichiers_sondes())
    return Atelier(spec, trace, charge.modele, j.tok, fmt, actions, episodes, adaptateurs, directions)


def test_reconstruction_egale_a_la_fonction_du_depot(monde):
    """La recette de la question (6), écrite dans la passe, rend les identifiants de `transcription_honnete`."""
    a = atelier(monde)
    guide = charger_invite("H1-classification")
    for (condition, tache), ep in list(a.episodes.items())[::5]:
        acts = sorted((x for x in a.actions if (x.condition, x.tache) == (condition, tache)), key=lambda x: x.pas)
        env = environnement("honnete", tache_de(next(t for t in monde.taches if t["identifiant"] == tache)), PAS, guide, {})
        ids, empans = transcription_honnete(a.fmt, env, [x.ids for x in acts])
        assert ids == ep.ids and empans == ep.empans
        assert [x.jetons_contexte for x in acts] == [d for d, _ in empans]
        assert ep.contexte(1) == ids[:empans[1][0]]


# ----------------------------------------------------------------------------------------------------------------------
# Garde P2 : modèle, jetoniseur, gabarit.
# ----------------------------------------------------------------------------------------------------------------------

@pytest.mark.parametrize("champs, motif", [
    ({"revision": "jouet-1"}, "≠ modèle attendu"),
    ({"n_couches": 5}, "4 couches : 5 attendues"),
    ({"largeur": 64}, "dimension cachée 32 : 64 attendue"),
    ({"fins": (EOS, 134, FIN)}, "jetons de fin de la génération"),
    ({"premier_jeton_cloture": EOS}, "premier jeton de la clôture du tour 135 ≠ 2"),
    ({"jeton_debut": 134}, "jeton de début"),
    ({"marque_ouverture": "Today Date: 27 Jul 2024"}, "marque figée"),
    ({"variables_gabarit": (("date_string", "01 Jan 2025"),)}, "marque figée"),
    ({"type_poids": "bfloat16"}, "poids de type"),
    ({"attention": "eager"}, "attention 'sdpa'"),
    ({"empreintes_fichiers_modele": (("tokenizer_config.json", "0" * 64),)}, "empreintes des fichiers de configuration"),
])
def test_p2_artefacts(monde, champs, motif):
    spec = dataclasses.replace(monde.spec, **champs)
    chargeur = monde.chargeur()
    j, charge = chargeur.jetoniseur(), chargeur.poids()
    fmt = P.former_format(spec, j.tok, charge.modele)
    t = P.TraceGardes()
    refus(lambda: P.garde_p2(spec, j, charge, fmt, P.debut_d_episode(spec, monde.taches[0]), t), motif)
    assert t.etat("P2") == "non tenue"


def test_p2_sain_et_artefact_dans_la_passe(monde):
    t = P.TraceGardes()
    chargeur = monde.chargeur()
    j, charge = chargeur.jetoniseur(), chargeur.poids()
    fmt = P.former_format(monde.spec, j.tok, charge.modele)
    assert P.garde_p2(monde.spec, j, charge, fmt, P.debut_d_episode(monde.spec, monde.taches[0]), t) == {"premier_jeton_cloture": FIN}
    t.clore("P2")
    p = monde.params()
    refus(lambda: P.executer_passe(p, monde.spec, monde.chargeur(revision="jouet-9")), "jetoniseur chargé|modèle chargé")
    arret = trace_d_arret(p.sortie)
    assert arret["gardes"]["P2"]["etat"] == "non tenue" and arret["gardes"]["P3"]["etat"] == "tenue"
    assert arret["gardes"]["P10"]["etat"] == "non jouée"


# ----------------------------------------------------------------------------------------------------------------------
# Gardes P4, P5, P6 : adaptateur et dose, positions capturées, valeurs finies.
# ----------------------------------------------------------------------------------------------------------------------

def test_p4_sain_puis_artefacts_dose_melee_adaptateur_altere_lot_mele(monde):
    a = atelier(monde)
    pad = min(a.fmt.fins)
    b100 = next(c for c in a.spec.conditions if c.nom == "B100")
    lot = [x for x in a.actions if x.condition == "B100"][:4]
    a.adaptateurs.poser(b100)
    captures = P.capturer_lot(a.spec, a.modele, pad, a.adaptateurs, lot, a.episodes, a.trace)             # sain
    assert len(captures) == 4 and all(captures[k][2].shape == (lot[k].jetons_notes, LARGEUR) for k in range(4))
    assert a.adaptateurs.egaux["B100"] is True
    # lot qui mêle deux conditions (donc deux doses) : refusé avant toute passe avant
    mele = lot[:2] + [x for x in a.actions if x.condition == "B50"][:2]
    refus(lambda: P.capturer_lot(a.spec, a.modele, pad, a.adaptateurs, mele, a.episodes, a.trace), "un lot ne porte qu'une condition")
    assert a.trace.etat("P4") == "non tenue"
    # lot trop grand
    b = atelier(monde)
    b.adaptateurs.poser(b100)
    grand = [x for x in b.actions if x.condition == "B100"][:5]
    refus(lambda: P.capturer_lot(b.spec, b.modele, pad, b.adaptateurs, grand, b.episodes, b.trace), "au plus 4 actions")
    # dose changée sur le modèle après la pose
    c = atelier(monde)
    c.adaptateurs.poser(b100)
    fixer_dose(c.modele, 0.5)
    refus(lambda: P.capturer_lot(c.spec, c.modele, pad, c.adaptateurs, lot, c.episodes, c.trace), "adaptateur ou dose relus")
    assert c.adaptateurs.egaux["B100"] is False
    # état de l'adaptateur altéré sur le modèle (autre adaptateur sous la même dose)
    d = atelier(monde)
    d.adaptateurs.poser(b100)
    charger_etat(d.modele, monde.etats["temoin-jumeau"])
    refus(lambda: P.capturer_lot(d.spec, d.modele, pad, d.adaptateurs, lot, d.episodes, d.trace), "adaptateur ou dose relus")
    # fichier d'adaptateur à valeur non finie ; rang autre que celui de la course
    e = dict(monde.etats["eleve"])
    cle = sorted(e)[0]
    e[cle] = e[cle].clone()
    e[cle].view(-1)[0] = float("nan")
    mauvais = monde.base / "adaptateur-nan.pt"
    torch.save(e, mauvais)
    f = atelier(monde)
    modele = modele_neuf(f.tok)
    refus(lambda: P.Adaptateurs(f.spec, modele, {"eleve": mauvais}, 3, P.TraceGardes()), "valeur non finie")
    modele = modele_neuf(f.tok)
    ad = P.Adaptateurs(dataclasses.replace(f.spec, rang=8), modele, {"eleve": monde.chemins["adaptateur_eleve"]},
                       3, P.TraceGardes())
    refus(lambda: ad.poser(b100), "forme")


def test_p4_artefact_dans_la_passe_ecrit_la_trace_d_arret(monde):
    p = monde.params()
    refus(lambda: P.executer_passe(p, monde.spec, monde.chargeur(), defauts_d_essai={"dose_apres_pose": 0.25}),
          "garde P4 non tenue")
    arret = trace_d_arret(p.sortie)
    assert arret["gardes"]["P4"]["etat"] == "non tenue" and arret["gardes"]["P10"]["etat"] == "tenue"
    assert not (p.sortie / "livraison").exists() and verifier(p.sortie / P.NOM_TRACE_ARRET)


def test_p5_couche_fausse_et_positions_capturees(monde):
    a = atelier(monde)
    pad = min(a.fmt.fins)
    h = a.spec.conditions[0]
    a.adaptateurs.poser(h)
    lot = [x for x in a.actions if x.condition == "H"][:2]
    refus(lambda: P.CrochetsSurCarte(a.modele, (1, 2, 4)), "hors de")                               # couche hors du modèle
    hors = dataclasses.replace(a.spec, couches=(1, 2, 7))
    refus(lambda: P.capturer_lot(hors, a.modele, pad, a.adaptateurs, lot, a.episodes, a.trace), "hors de")
    with P.CrochetsSurCarte(a.modele, (1, 3)) as c:                                                 # sain
        a.modele(torch.tensor([[1, 5, 6]]), use_cache=False)
        assert set(c.sorties) == {1, 3} and c.sorties[3].shape == (1, 3, LARGEUR)
    # nombre de positions capturées ≠ nombre de jetons notés
    faux = dataclasses.replace(lot[0], jetons_notes=len(lot[0].ids) + 1)
    refus(lambda: P.capturer_lot(a.spec, a.modele, pad, a.adaptateurs, [faux], a.episodes, a.trace), "positions capturées pour")
    assert a.trace.etat("P5") == "non tenue"
    b = atelier(monde)
    b.adaptateurs.poser(h)
    vide = dataclasses.replace(lot[0], jetons_notes=0)
    refus(lambda: P.capturer_lot(b.spec, b.modele, pad, b.adaptateurs, [vide], b.episodes, b.trace), "sans jeton noté")
    # directions d'une couche non capturée
    autre = [dataclasses.replace(b.directions[0], couche=0)]
    refus(lambda: P.directions_par_couche(b.spec, autre, "cpu"), "couche non capturée")


def test_p6_valeurs_non_finies(monde):
    a = atelier(monde)
    pad = min(a.fmt.fins)
    h = a.spec.conditions[0]
    a.adaptateurs.poser(h)
    x = [x for x in a.actions if x.condition == "H"][0]
    capture = P.capturer_lot(a.spec, a.modele, pad, a.adaptateurs, [x], a.episodes, a.trace)[0]
    par_couche, sondes = P.directions_par_couche(a.spec, a.directions, "cpu")
    sa = np.full((len(a.actions), len(a.directions), 2), np.nan)
    sj = {}
    P.noter_action(x, capture, par_couche, sa, sj, len(sondes), a.trace)                                # sain
    assert np.all(np.isfinite(sa[x.rang])) and sj[x.rang].shape == (x.jetons_notes, len(sondes))
    par_couche[2].w[0, 0] = float("inf")                                                               # score non fini
    refus(lambda: P.noter_action(x, capture, par_couche, sa, sj, len(sondes), a.trace), "score non fini")
    assert a.trace.etat("P6") == "non tenue"
    b = atelier(monde)
    b.adaptateurs.poser(h)
    with torch.no_grad():
        b.modele.model.layers[1].mlp.down_proj.weight[0, 0] = float("nan")                             # capture non finie
    refus(lambda: P.capturer_lot(b.spec, b.modele, pad, b.adaptateurs, [x], b.episodes, b.trace), "capture non finie")
    refus(lambda: P.produit_sur_carte(capture[2], par_couche[2].w.float(), par_couche[2].b), "double précision")


def test_agregations_maximum_de_production_et_moyenne_du_seul_bras_de_diagnostic():
    g = torch.Generator().manual_seed(0)
    h = torch.randn(7, LARGEUR, generator=g)
    w = torch.randn(3, LARGEUR, generator=g, dtype=torch.float64)
    b = torch.randn(3, generator=g, dtype=torch.float64)
    s = P.produit_sur_carte(h, w, b)
    assert s.dtype == torch.float64 and s.shape == (7, 3)
    for k in range(3):
        sonde = SondeLineaireJetons(f"s{k}", 2, "max", w[k].numpy(), float(b[k]))
        np.testing.assert_allclose(s[:, k].numpy(), sonde.scores_par_jeton(h.numpy()), rtol=0, atol=1e-12)
        assert abs(float(P.agregation_de_production_maximum(s)[k]) - score_action(sonde, h.numpy(), 0, 7)) < 1e-12
    np.testing.assert_allclose(P.moyenne_du_bras_de_diagnostic_jamais_en_production(s).numpy(), s.numpy().mean(axis=0), atol=1e-13)
    source = Path(P.__file__).read_text(encoding="utf-8")
    assert "median" not in source and "médiane" not in source.replace("jamais la médiane", "")
    assert source.count(".mean(") == 2                  # la moyenne du bras de diagnostic, et celle de la vraisemblance (P10)
    assert source.count("moyenne_du_bras_de_diagnostic_jamais_en_production(") == 2          # sa définition, un seul appel


# ----------------------------------------------------------------------------------------------------------------------
# Garde P7 : répétabilité et contrôle négatif.
# ----------------------------------------------------------------------------------------------------------------------

def _captures(rng, n_actions=14, jetons=9):
    return {c: {r: rng.standard_normal((jetons, LARGEUR)).astype(np.float32) for r in range(n_actions)} for c in (1, 2, 3)}


def test_p7_sain_et_artefacts(monde):
    spec = monde.spec
    rng = np.random.default_rng(3)
    premiere = _captures(rng)
    seconde = {c: {r: (v * (1 + 1e-5)).astype(np.float32) for r, v in d.items()} for c, d in premiere.items()}
    t = P.TraceGardes()
    r = P.garde_p7(spec, premiere, seconde, t)                                                          # sain
    t.clore("P7")
    assert 0 < r["plus_grand_centile_99"] < 1e-4 and r["controle_negatif"] == {"actions_comparables": 14, "fraction_vue": 1.0, "tenu": "oui"}
    # désalignement d'un jeton entre les deux passes
    decalee = {c: {r_: np.roll(v, 1, axis=0) for r_, v in d.items()} for c, d in premiere.items()}
    refus(lambda: P.garde_p7(spec, premiere, decalee, P.TraceGardes()), "99e centile de l'écart entre les deux passes")
    # une seule couche fautive suffit
    une = {c: dict(d) for c, d in seconde.items()}
    une[3][4] = premiere[3][4] * 2
    refus(lambda: P.garde_p7(spec, premiere, une, P.TraceGardes()), "action 4, couche 3")
    # garde aveugle : activité constante le long des jetons, le décalage ne se voit pas
    plate = {c: {r_: np.repeat(v[:1], v.shape[0], axis=0) for r_, v in d.items()} for c, d in premiere.items()}
    refus(lambda: P.garde_p7(spec, plate, plate, P.TraceGardes()), "garde aveugle")
    # trop peu d'actions comparables (actions trop courtes ; moins de dix actions)
    refus(lambda: P.garde_p7(spec, _captures(rng, 14, 4), _captures(rng, 14, 4), P.TraceGardes()), "99e centile|comparables")
    courtes = _captures(rng, 14, 4)
    refus(lambda: P.garde_p7(spec, courtes, courtes, P.TraceGardes()), "0 action.s. comparables")
    peu = _captures(rng, 9, 9)
    refus(lambda: P.garde_p7(spec, peu, peu, P.TraceGardes()), "9 action.s. comparables")
    # seconde capture absente, ou d'un autre type
    manque = {c: {r_: v for r_, v in d.items() if r_ != 2} for c, d in seconde.items()}
    refus(lambda: P.garde_p7(spec, premiere, manque, P.TraceGardes()), "seconde capture absente")
    double = {c: {r_: v.astype(np.float64) for r_, v in d.items()} for c, d in seconde.items()}
    refus(lambda: P.garde_p7(spec, premiere, double, P.TraceGardes()), "seconde capture absente ou de forme")


def test_p7_artefact_dans_la_passe(monde):
    p = monde.params()
    refus(lambda: P.executer_passe(p, monde.spec, monde.chargeur(), defauts_d_essai={"seconde_passe_decalee": True}),
          "garde P7 non tenue")
    arret = trace_d_arret(p.sortie)
    assert arret["gardes"]["P7"]["etat"] == "non tenue" and not (p.sortie / "livraison").exists()


# ----------------------------------------------------------------------------------------------------------------------
# Garde P8 : liste fermée des chemins lus, aucun texte privé.
# ----------------------------------------------------------------------------------------------------------------------

def test_p8_surveillance_saine_et_artefacts(tmp_path):
    racine = tmp_path / "depot"
    (racine / "donnees" / "course").mkdir(parents=True)
    (racine / "src").mkdir()
    permis = racine / "donnees" / "course" / "ids-actions-iib-evaluation.npz"
    oracle = racine / "donnees" / "course" / "oracle-iib-evaluation.json"
    resume = racine / "donnees" / "course" / "resume.json"
    code = racine / "src" / "module.py"
    prive_ailleurs = tmp_path / "consigne-privee-maitre.md"
    ailleurs = tmp_path / "ailleurs.txt"
    (racine / "src" / "iib").mkdir()
    for c in (permis, oracle, resume, code, prive_ailleurs, ailleurs, racine / "src" / "iib" / "m.py"):
        c.write_text("x", encoding="utf-8")
    t = P.TraceGardes()
    sortie = racine / "sortie"
    s = P.SurveillanceLectures(t, [permis], [racine / "src"], [sortie], [racine])
    with P.surveiller(s):
        assert permis.read_text(encoding="utf-8") == "x" and code.read_text(encoding="utf-8") == "x"       # sain
        assert ailleurs.read_text(encoding="utf-8") == "x"
        refus(lambda: P.surveiller(s).__enter__(), "déjà active")
        assert t.etat("P8") == "non jouée" and s.lus == {str(permis)} and s.ailleurs >= 1 and not s.prive
        refus(lambda: resume.read_text(encoding="utf-8"), "hors de la liste fermée")                       # hors liste
        assert t.etat("P8") == "non tenue" and not s.prive
        # écritures : permises dans la sortie, même si son nom porte un motif ; jamais comptées « chemin privé lu »
        sortie.mkdir()
        (sortie / "x-iib.json").write_text("y", encoding="utf-8")
        assert (sortie / "x-iib.json").read_text(encoding="utf-8") == "y" and not s.prive
        refus(lambda: (racine / "donnees" / "course" / "neuf.txt").write_text("z", encoding="utf-8"), "écriture de .* hors des dossiers de sortie")
        assert not s.prive and not (racine / "donnees" / "course" / "neuf.txt").exists()
        (tmp_path / "ailleurs-iib.txt").write_text("z", encoding="utf-8")                                  # écriture hors dépôt
        assert not s.prive
        # dossier des fichiers du modèle : dans la liste fermée du texte, jamais refusé par un motif
        cache = tmp_path / "cache-iib" / "modele"
        cache.mkdir(parents=True)
        (cache / "config.json").write_text("{}", encoding="utf-8")
        refus(lambda: (cache / "config.json").read_text(encoding="utf-8"), "chemin privé")                 # avant déclaration
        s.prive = False
        s.permettre_modele(cache)
        assert (cache / "config.json").read_text(encoding="utf-8") == "{}" and not s.prive
        # code : la partie propre du chemin porte un motif → refusé ; la racine du code peut en porter un
        refus(lambda: (racine / "src" / "iib" / "m.py").read_text(encoding="utf-8"), "chemin privé")
        s.prive = False
        refus(lambda: oracle.read_text(encoding="utf-8"), "chemin privé")                                  # privé
        refus(lambda: prive_ailleurs.read_text(encoding="utf-8"), "chemin privé")                          # privé, hors dépôt
        assert s.prive
    assert oracle.read_text(encoding="utf-8") == "x"                                                       # surveillance levée


def test_p8_controle_d_ouverture_des_sorties_avant_tout_calcul(monde):
    """Une sortie, un nom de passe ou un dossier du modèle qui ferait refuser la passe à la fin est refusé à l'ouverture,
    avant la garde P0 : aucune garde d'entrée n'a tourné, aucun modèle n'est chargé."""
    for champs, motif in (({"sortie": monde.base / "sortie-iib-essai"}, "porte un motif privé"),
                          ({"sortie": monde.base / "ii-b" / "sortie"}, "porte un motif privé"),
                          ({"run_id": "20261119-020202-passe-iib"}, "porte un motif privé")):
        chargeur = monde.chargeur()
        p = monde.params(**champs)
        refus(lambda: P.executer_passe(p, monde.spec, chargeur), motif)
        assert chargeur.tok is None and not (monde.racine / "runs" / p.run_id).exists()
        if "sortie" in champs:
            assert not p.sortie.exists()                                 # rien n'est écrit sous un nom privé
        else:
            arret = trace_d_arret(p.sortie)
            assert arret["gardes"]["P8"]["etat"] == "non tenue" and arret["gardes"]["P0"]["etat"] == "non jouée"
            assert arret["chemin_prive_lu"] == "non"                     # ce n'est pas une lecture
    # nom de passe déjà pris (R12) : vu à l'ouverture
    (monde.racine / "diag" / "20261119-030303-pris").mkdir(parents=True)
    p = monde.params(run_id="20261119-030303-pris")
    refus(lambda: P.executer_passe(p, monde.spec, monde.chargeur()), "existe déjà")
    assert trace_d_arret(p.sortie)["gardes"]["P0"]["etat"] == "non jouée"
    # disque de sortie trop petit pour la borne de taille et le découpage
    p = monde.params()
    refus(lambda: P.executer_passe(p, dataclasses.replace(monde.spec, disque_transitoire=10 ** 18), monde.chargeur()),
          "place libre du disque de sortie")
    assert trace_d_arret(p.sortie)["gardes"]["P9"]["etat"] == "non tenue"
    # dossier du modèle absent : refusé après les gardes d'ouverture et d'entrée, avant tout chargement
    chargeur = ChargeurJouet(monde.base / "dossier-absent")
    p = monde.params()
    refus(lambda: P.executer_passe(p, monde.spec, chargeur), "dossier des fichiers du modèle est absent")
    assert chargeur.tok is None and trace_d_arret(p.sortie)["gardes"]["P8"]["etat"] == "non tenue"
    # sain : un dossier du modèle dont le chemin porte un motif n'est pas refusé (liste fermée du texte)
    cache = monde.base / "cache-iib"
    cache.mkdir()
    shutil.copy(monde.hors_depot / "tokenizer_config.json", cache / "tokenizer_config.json")
    shutil.copy(monde.hors_depot / "config.json", cache / "config.json")
    r = P.executer_passe(monde.params(), monde.spec, ChargeurJouet(cache), mode="entrees")
    assert r["entrees"] == "conformes"


def test_p8_artefacts_dans_la_passe(monde, monkeypatch):
    # un environnement rebâti qui porterait un texte privé
    vrai = P.environnement

    def avec_texte_prive(condition, tache, T, guide, consignes):
        env = vrai(condition, tache, T, guide, consignes)
        env.instructions_cachees = {0: "texte privé"}
        return env

    a = atelier(monde)
    monkeypatch.setattr(P, "environnement", avec_texte_prive)
    t = P.TraceGardes()
    refus(lambda: P.rebatir_episodes(a.spec, a.fmt, monde.taches, a.actions, t), "porte un texte privé")
    assert t.etat("P8") == "non tenue"
    monkeypatch.setattr(P, "environnement", vrai)
    # un chargeur qui ouvre un fichier du dépôt hors de la liste fermée : refusé avant lecture, trace d'arrêt écrite
    secret = monde.base / "depot-secret.txt"

    class ChargeurCurieux(ChargeurJouet):
        def poids(self):
            compagnon(monde.chemins["extrait"]).read_text(encoding="utf-8")                                 # permis
            (monde.racine / "registres" / "decisions.md").read_text(encoding="utf-8")
            return super().poids()

    (monde.racine / "registres" / "decisions.md").write_text("décisions\n", encoding="utf-8")
    p = monde.params()
    refus(lambda: P.executer_passe(p, monde.spec, ChargeurCurieux(monde.hors_depot)), "hors de la liste fermée")
    arret = trace_d_arret(p.sortie)
    assert arret["gardes"]["P8"]["etat"] == "non tenue" and arret["chemin_prive_lu"] == "non"
    (monde.racine / "registres" / "decisions.md").unlink()

    class ChargeurIndiscret(ChargeurJouet):
        def poids(self):
            (monde.chemins["ids"].parent / "evaluation-iib-v5.json").read_text(encoding="utf-8")
            return super().poids()

    p = monde.params()
    refus(lambda: P.executer_passe(p, monde.spec, ChargeurIndiscret(monde.hors_depot)), "chemin privé")
    arret = trace_d_arret(p.sortie)
    assert arret["gardes"]["P8"]["etat"] == "non tenue" and arret["chemin_prive_lu"] == "oui"
    assert not secret.exists()


# ----------------------------------------------------------------------------------------------------------------------
# Garde P9 : durée, dépense, taille.
# ----------------------------------------------------------------------------------------------------------------------

def test_p9_sain_et_artefacts(monde):
    t = P.TraceGardes()
    p = monde.params()
    assert 0.0 < P.garde_p9_duree(p, t) < 0.1                                                           # sain
    P.garde_p9_taille(monde.spec, 2_000_000_000 - 1, t)
    P.garde_p9_taille(P.SPECIFICATION_TEXTE, 2_000_000_000, t)
    # la passe appelle cette garde avec la taille des fichiers 1 à 4 et de leurs compagnons PLUS la réserve de 4 000 000
    # octets : ils tiennent donc sous 1 996 000 000 octets, borne comprise
    P.garde_p9_taille(P.SPECIFICATION_TEXTE, 1_996_000_000 + P.MARGE_TRACE_ET_BORDEREAU, t)
    refus(lambda: P.garde_p9_taille(P.SPECIFICATION_TEXTE, 1_996_000_001 + P.MARGE_TRACE_ET_BORDEREAU, P.TraceGardes()), "aucune livraison")
    source = Path(P.__file__).read_text(encoding="utf-8")
    assert "garde_p9_taille(spec, taille_donnees + spec.reserve_trace_et_bordereau, trace)" in source
    assert P.SPECIFICATION_TEXTE.reserve_trace_et_bordereau == 4_000_000
    refus(lambda: P.garde_p9_taille(P.SPECIFICATION_TEXTE, 2_000_000_001, P.TraceGardes()), "aucune livraison")
    e = refus(lambda: P.garde_p9_duree(monde.params(debut_location=time.time() - 4 * 3600), P.TraceGardes()), "durée")
    assert "arrêter l'instance instance-jouet-1 par son identifiant" in str(e)
    refus(lambda: P.garde_p9_duree(monde.params(debut_location=time.time() - 2 * 3600, prix_horaire_usd=6.0), P.TraceGardes()), "dépense")
    refus(lambda: P.garde_p9_duree(monde.params(debut_location=time.time() + 3600), P.TraceGardes()), "durée")
    # dans la passe : l'horloge dépasse la borne pendant la première passe → arrêt, aucune livraison
    appels = {"n": 0}

    def horloge():
        appels["n"] += 1
        return time.time() + (0 if appels["n"] < 6 else 10 * 3600)

    p = monde.params(horloge=horloge)
    refus(lambda: P.executer_passe(p, monde.spec, monde.chargeur()), "garde P9 non tenue")
    arret = trace_d_arret(p.sortie)
    assert arret["gardes"]["P9"]["etat"] == "non tenue" and not (p.sortie / "livraison" / P.NOM_BORDEREAU).exists()
    # dans la passe : livraison au-dessus de la borne de taille → aucun bordereau
    p = monde.params()
    refus(lambda: P.executer_passe(p, dataclasses.replace(monde.spec, taille_max=P.MARGE_TRACE_ET_BORDEREAU + 1000), monde.chargeur()),
          "au-dessus de")
    assert trace_d_arret(p.sortie)["gardes"]["P9"]["etat"] == "non tenue"
    assert not (p.sortie / "livraison" / P.NOM_BORDEREAU).exists() and not (p.sortie / "livraison" / P.NOM_TRACE).exists()
    # dans la passe : le premier contrôle de taille passe, le second (trace et bordereau hors de la réserve) refuse ;
    # la garde n'a pas été close entre les deux : elle est « non tenue », ni trace ni bordereau
    p = monde.params()
    refus(lambda: P.executer_passe(p, dataclasses.replace(monde.spec, reserve_trace_et_bordereau=200), monde.chargeur()),
          "garde P9 non tenue : la trace, le bordereau et leurs compagnons")
    arret = trace_d_arret(p.sortie)
    assert arret["gardes"]["P9"]["etat"] == "non tenue" and arret["gardes"]["P7"]["etat"] == "tenue"
    assert not (p.sortie / "livraison" / P.NOM_BORDEREAU).exists() and not (p.sortie / "livraison" / P.NOM_TRACE).exists()


# ----------------------------------------------------------------------------------------------------------------------
# Garde P10 : contrôle du contexte par la vraisemblance.
# ----------------------------------------------------------------------------------------------------------------------

def test_p10_artefact_contextes_decales_d_une_tache(monde):
    p = monde.params()
    refus(lambda: P.executer_passe(p, monde.spec, monde.chargeur(), defauts_d_essai={"decalage_de_tache_p10": 1}),
          "garde P10 non tenue : contexte rebâti")
    arret = trace_d_arret(p.sortie)
    assert arret["gardes"]["P10"]["etat"] == "non tenue" and arret["gardes"]["P7"]["etat"] == "non jouée"
    assert not (p.sortie / "livraison").exists()


def test_p10_trop_peu_d_actions_et_garde_aveugle(monde):
    a = atelier(monde)
    pad = min(a.fmt.fins)
    sous, _ = P.sous_echantillons(a.spec, a.actions)
    peu = dataclasses.replace(a.spec, actions_min_p10=1000)
    refus(lambda: P.garde_p10(peu, a.modele, pad, a.adaptateurs, a.actions, a.episodes, sous, P.TraceGardes()),
          "action.s. éligibles au contrôle du contexte : 1000 au moins")
    longues = dataclasses.replace(a.spec, jetons_min_p10=MAX_JETONS + 1)
    refus(lambda: P.garde_p10(longues, a.modele, pad, a.adaptateurs, a.actions, a.episodes, sous, P.TraceGardes()), "0 action")
    # garde aveugle : si l'artefact ne fait pas tomber la fraction sous le seuil, la passe s'arrête
    aveugle = dataclasses.replace(a.spec, fraction_min_p10=0.0)
    t = P.TraceGardes()
    refus(lambda: P.garde_p10(aveugle, a.modele, pad, a.adaptateurs, a.actions, a.episodes, sous, t), "garde aveugle")
    assert t.etat("P10") == "non tenue"
    # vraisemblance : le contexte propre d'une action tirée du modèle est plus vraisemblable qu'un contexte étranger
    x = next(x for x in a.actions if x.condition == "B100" and x.jetons_notes >= 6)
    a.adaptateurs.poser(next(c for c in a.spec.conditions if c.nom == "B100"))
    propre = a.episodes[("B100", x.tache)].contexte(x.pas)
    autre = a.episodes[("B100", "tache-03" if x.tache != "tache-03" else "tache-02")].contexte(x.pas)
    v = P.log_vraisemblances(a.modele, pad, [propre, autre], [x.ids, x.ids])
    assert v[0] > v[1]
    refus(lambda: P.log_vraisemblances(a.modele, pad, [[]], [x.ids]), "vide")


# ----------------------------------------------------------------------------------------------------------------------
# Règle mécanique des sondes lues.
# ----------------------------------------------------------------------------------------------------------------------

def test_regle_des_sondes_lues_saine_et_artefacts(monde):
    spec, fichiers = monde.spec, monde.params().fichiers_sondes()
    etats, directions = P.regle_des_sondes_lues(spec, fichiers)                                         # sain
    assert [etats[d.nom] for d in spec.sondes_decisives] == ["lue"] * 3 and etats["enjeux-c3"] == "absente"
    assert [d.role for d in directions].count("plancher") == 3 * N_PLANCHER
    assert [d.nom for d in directions if d.role == "sonde"] == [
        "tromperie-c2", "enjeux-c2", "dissimulation-c2", "dissimulation-c1", "dissimulation-c3", "tromperie-c1",
        "tromperie-c3", "enjeux-c1"]
    b = {s.nom: s for liste in monde.sondes.values() for s in liste}
    assert all(d.b == b[d.nom].b and np.array_equal(d.w, b[d.nom].w) for d in directions)

    def avec(k: int, **champs):
        d = list(spec.sondes_decisives)
        d[k] = dataclasses.replace(d[k], **champs)
        return dataclasses.replace(spec, sondes_decisives=tuple(d))

    for artefact in (avec(0, empreinte_vecteur="0" * 64), avec(0, empreinte_sonde="0" * 64), avec(0, rang_index=0),
                     avec(0, rang_index=99), avec(0, prefixe_plancher="tromperie-c2-t07-autre-"),
                     avec(0, fichier_plancher="neuves")):
        etats, directions = P.regle_des_sondes_lues(artefact, fichiers)
        assert etats["tromperie-c2"] == "sans objet" and etats["enjeux-c2"] == "lue"
        assert not any(d.nom.startswith("tromperie-c2") for d in directions)                           # ni elle, ni son plancher
        assert len(directions) == 2 * (1 + N_PLANCHER) + 5
    # nombre de directions de plancher non conforme ; couche décisive autre que celle des sondes
    # quatre directions attendues, cinq présentes sous chaque désignation : une de trop partout, aucune sonde lue
    refus(lambda: P.regle_des_sondes_lues(dataclasses.replace(spec, n_plancher=N_PLANCHER - 1), fichiers), "aucune des sondes décisives")
    refus(lambda: P.regle_des_sondes_lues(dataclasses.replace(spec, n_plancher=N_PLANCHER + 1), fichiers), "aucune des sondes décisives")
    refus(lambda: P.regle_des_sondes_lues(dataclasses.replace(spec, couche_decisive=3), fichiers), "aucune des sondes décisives")
    # sonde des couches descriptives trouvée sous son nom mais non conforme (autre couche) : arrêt de la passe (P1)
    desc = (P.SondeDescriptive("dissimulation-c1", "neuves", 3),) + spec.sondes_descriptives[1:]
    non_conforme = dataclasses.replace(spec, sondes_descriptives=desc)
    refus(lambda: P.regle_des_sondes_lues(non_conforme, fichiers), "dissimulation-c1 trouvée sous son nom mais non conforme")
    p = monde.params()
    chargeur = monde.chargeur()
    refus(lambda: P.executer_passe(p, non_conforme, chargeur), "trouvée sous son nom mais non conforme")
    arret = trace_d_arret(p.sortie)
    assert arret["gardes"]["P1"]["etat"] == "non tenue" and chargeur.tok is None and not (p.sortie / "livraison").exists()
    # empreinte entière du fichier différente : le lecteur du dépôt refuse
    faux = dataclasses.replace(spec, empreintes_fichiers_sondes=tuple((r, "1" * 64) for r, _ in spec.empreintes_fichiers_sondes))
    refus(lambda: P.regle_des_sondes_lues(faux, fichiers), "empreinte attendue")


def test_specification_du_texte():
    s = P.SPECIFICATION_TEXTE
    assert (s.modele, s.revision) == ("meta-llama/Llama-3.1-8B-Instruct", "0e9e39f249a16976918f6564b8830bc894c89659")
    assert (s.n_couches, s.largeur, s.couches, s.couche_decisive, s.lot, s.max_jetons_action) == (32, 4096, (7, 15, 23), 15, 8, 400)
    assert set(s.fins) == {128001, 128008, 128009} and s.premier_jeton_cloture == 128009 and min(s.fins) == 128001
    assert [(c.nom, c.adaptateur, c.dose) for c in s.conditions] == [
        ("H", "eleve", 0.0), ("B50", "eleve", 0.5), ("B100", "eleve", 1.0), ("TJ100", "temoin-jumeau", 1.0)]
    assert (s.rang, s.alpha, s.cibles) == (16, 32.0, ("q_proj", "k_proj", "v_proj", "o_proj"))
    assert s.n_taches * len(s.conditions) * s.pas_par_episode == 2560 and s.n_plancher == 800
    assert (s.seuil_p7, s.quantile_p7, s.comparaisons_min_p7, s.actions_min_p7, s.fraction_min_p7) == (0.2, 0.99, 4, 10, 0.95)
    assert (s.jetons_min_p10, s.actions_min_p10, s.fraction_min_p10, s.taille_max) == (4, 10, 0.95, 2_000_000_000)
    # règle du sous-échantillon sur 2 560 clés : 161 et 21 actions
    actions = [P.Action(k, f"evaluation-H/t{k:04d}/pas0", "evaluation-H", "t", "t", "H", 0, "", [5, 9], 1) for k in range(2560)]
    d, e = P.sous_echantillons(s, actions)
    assert (len(d), len(e)) == (161, 21) and e <= d
    actions[7].jetons_notes = 0
    d, e = P.sous_echantillons(s, actions)
    assert 7 not in d and len(d) <= 161 and len(e) <= 21
    refus(lambda: P.sous_echantillons(s, [dataclasses.replace(actions[7])]), "aucune action")
    # petit cas calculé à la main (pas de 2 et de 4) : sept actions, dont une sans jeton noté ; le tri est celui des
    # chaînes de Python (par points de code) : « B100 » avant « B50 », « pas10 » avant « pas2 », majuscule avant minuscule
    petit = dataclasses.replace(s, pas_sous_echantillon_decisif=2, pas_sous_echantillon_descriptif=4)
    cles = ["evaluation-H/t/pas2", "evaluation-B50/t/pas0", "evaluation-H/t/pas10", "evaluation-B100/t/pas1",
            "evaluation-H/T/pas0", "evaluation-TJ100/t/pas0", "evaluation-B100/t/pas0"]
    notes = [3, 1, 2, 5, 4, 1, 0]
    petites = [P.Action(k, c, "", "", "", "", 0, "", [5], n) for k, (c, n) in enumerate(zip(cles, notes))]
    # liste triée des actions notées, par rang de fichier : B100/pas1 (3), B50/pas0 (1), H/T/pas0 (4), H/t/pas10 (2),
    # H/t/pas2 (0), TJ100/pas0 (5) ; rangs 0, 2, 4 et la dernière → {3, 4, 0, 5} ; rangs 0, 4 et la dernière → {3, 0, 5}
    assert sorted(a.cle for a in petites if a.jetons_notes) == [cles[3], cles[1], cles[4], cles[2], cles[0], cles[5]]
    assert P.sous_echantillons(petit, petites) == ({3, 4, 0, 5}, {3, 0, 5})
    assert P.MARGE_TRACE_ET_BORDEREAU == 4_000_000 and s.taille_max - P.MARGE_TRACE_ET_BORDEREAU == 1_996_000_000
    # identités de la table du texte
    assert [(x.nom, x.rang_index) for x in s.sondes_decisives] == [
        ("tromperie-difference_moyennes-c15", 1), ("enjeux-lineaire-c15", 16), ("dissimulation-lineaire-c15", 4)]
    assert dict(s.empreintes_fichiers_sondes)["neuves"].startswith("374ad473") and s.empreinte_taches.startswith("76cdeace")
    assert len(s.sondes_descriptives) == 6 and {x.couche for x in s.sondes_descriptives} == {7, 23}
    assert dict(s.empreintes_fichiers_modele)["tokenizer_config.json"].startswith("177c7b61")


# ----------------------------------------------------------------------------------------------------------------------
# Écriture déterministe, morceaux.
# ----------------------------------------------------------------------------------------------------------------------

def test_archives_deterministes_et_morceaux(tmp_path):
    rng = np.random.default_rng(0)
    t = {"b": rng.standard_normal((50, 7)), "a": np.arange(5, dtype=np.int64), "c": P.json_en_octets({"é": 1})}
    h1 = P.ecrire_npz_deterministe(tmp_path / "x.npz", t)
    time.sleep(1.1)
    h2 = P.ecrire_npz_deterministe(tmp_path / "y.npz", dict(reversed(list(t.items()))))
    assert h1 == h2
    with np.load(tmp_path / "x.npz", allow_pickle=False) as z:
        assert sorted(z.files) == ["a", "b", "c"] and np.array_equal(z["b"], t["b"])
    with zipfile.ZipFile(tmp_path / "x.npz") as z:
        assert all(i.date_time == (1980, 1, 1, 0, 0, 0) and i.compress_type == zipfile.ZIP_STORED for i in z.infolist())
    refus(lambda: P.ecrire_npz_deterministe(tmp_path / "x.npz", t), "existe déjà")
    refus(lambda: P.ecrire_npz_deterministe(tmp_path / "o.npz", {"o": np.array([{}], dtype=object)}), "objets Python")
    refus(lambda: P.ecrire_npz_deterministe(tmp_path / "v.npz", {}), "aucun tableau")
    entier = (tmp_path / "x.npz").read_bytes()
    ecrits = P.decouper_en_morceaux(tmp_path / "x.npz", 1000)
    assert not (tmp_path / "x.npz").exists() and len(ecrits) == len(entier) // 1000 + 2
    liste = json.loads((tmp_path / "x.npz.morceaux.json").read_text(encoding="utf-8"))
    assert b"".join((tmp_path / m["nom"]).read_bytes() for m in liste["morceaux"]) == entier
    assert liste["sha256"] == h1 and all(verifier(tmp_path / m["nom"]) == m["sha256"] for m in liste["morceaux"])
    refus(lambda: P.decouper_en_morceaux(tmp_path / "y.npz", 0), "taille de morceau nulle")
    refus(lambda: P.ecrire_json_scelle(tmp_path / "x.npz.morceaux.json", {}), "existe déjà")


# ----------------------------------------------------------------------------------------------------------------------
# Garde P10 sans modèle ni réglage : vraisemblances simulées (essai du contre-lecteur du code de version 2).
# L'essai sur le jouet ajusté, plus haut, n'est qu'un essai d'intégration ; c'est ici que le seuil est éprouvé.
# ----------------------------------------------------------------------------------------------------------------------

SPEC_SIMULEE = dataclasses.replace(P.SPECIFICATION_TEXTE, n_taches=20, pas_par_episode=1)


class AdaptateursFactices:
    def poser(self, condition):
        pass

    def relire(self, condition, actions=0):
        pass


def monde_simule(n_taches, fautives):
    actions, episodes = [], {}
    for k in range(n_taches):
        t = f"t{k:02d}"
        actions.append(P.Action(k, f"evaluation-H/{t}/pas0", "evaluation-H", t, t, "H", 0, "", [10 + k] * 5 + [1], 5))
        episodes[("H", t)] = P.Episode("H", t, [-1 if k in fautives else 1000 + k, 7], [(2, 8)])
    return actions, episodes


def appel_simule(actions, episodes, monkeypatch):
    vus = []

    def vraisemblances(modele, pad, contextes, suites):
        vus.extend((c[0], s[0]) for c, s in zip(contextes, suites))
        return [1.0 if c[0] == 1000 + (s[0] - 10) else 0.0 for c, s in zip(contextes, suites)]

    monkeypatch.setattr(P, "log_vraisemblances", vraisemblances)
    r = P.garde_p10(SPEC_SIMULEE, None, 0, AdaptateursFactices(), actions, episodes, {a.rang for a in actions}, P.TraceGardes())
    return r, vus


def test_p10_simule_frontiere_tenue(monkeypatch):                # 19 sur 20 = 0,95 : tenue (borne comprise)
    r, vus = appel_simule(*monde_simule(20, {3}), monkeypatch)
    assert r["fraction"] == 0.95 and r["artefact"]["fraction"] == 0.0 and len(vus) == 60
    # les contextes (ii) sont ceux de la tâche suivante dans le tri des chaînes, la première après la dernière
    assert (1001, 10) in vus and (1000, 29) in vus and (1002, 10) in vus


def test_p10_simule_frontiere_non_tenue(monkeypatch):            # 18 sur 20 = 0,90 : non tenue
    with pytest.raises(GardeArret, match="contexte rebâti"):
        appel_simule(*monde_simule(20, {3, 4}), monkeypatch)


def test_p10_simule_moins_de_dix(monkeypatch):
    with pytest.raises(GardeArret, match="9 action"):
        appel_simule(*monde_simule(9, set()), monkeypatch)


def test_p10_simule_egalite_ne_passe_pas(monkeypatch):
    actions, episodes = monde_simule(20, set())
    monkeypatch.setattr(P, "log_vraisemblances", lambda m, p, c, s: [0.5] * len(c))
    with pytest.raises(GardeArret, match="contexte rebâti"):
        P.garde_p10(SPEC_SIMULEE, None, 0, AdaptateursFactices(), actions, episodes, {a.rang for a in actions}, P.TraceGardes())


def test_p10_voit_une_reconstruction_fausse(monde, monkeypatch):
    """La RECONSTRUCTION elle-même est faussée (chaque épisode reçoit l'énoncé de la tâche suivante), et non les
    contextes que la garde choisit : la garde doit refuser avant la première passe."""
    vrai = P.tache_de
    par_id = {t["identifiant"]: t for t in monde.taches}
    ordre = sorted(par_id)
    monkeypatch.setattr(P, "tache_de", lambda d: vrai(par_id[ordre[(ordre.index(d["identifiant"]) + 1) % len(ordre)]]))
    p = monde.params()
    refus(lambda: P.executer_passe(p, monde.spec, monde.chargeur()), "garde P10 non tenue : contexte rebâti")
    arret = trace_d_arret(p.sortie)
    assert arret["gardes"]["P10"]["etat"] == "non tenue" and arret["gardes"]["P7"]["etat"] == "non jouée"
    assert arret["gardes"]["P3"]["etat"] == "tenue" and not (p.sortie / "livraison").exists()


# ----------------------------------------------------------------------------------------------------------------------
# Remarques mineures de la contre-lecture : plancher en trop, condition sans lot, égalité à l'extrait, lots de l'extrait.
# ----------------------------------------------------------------------------------------------------------------------

def test_une_direction_de_plancher_en_trop_rend_la_sonde_sans_objet(monde):
    en_trop = SondeLineaireJetons(f"tromperie-c2-t07-plancher-{N_PLANCHER}", 2, "max", np.ones(LARGEUR), 0.0, None, "plancher")
    chemin = monde.racine / "donnees" / "sondes" / "planchers-en-trop.npz"
    sha = ecrire_sondes(chemin, monde.sondes["planchers"] + [en_trop], {"principales": {}})
    spec = dataclasses.replace(monde.spec, empreintes_fichiers_sondes=tuple(
        (r, sha if r == "planchers" else h) for r, h in monde.spec.empreintes_fichiers_sondes))
    fichiers = {**monde.params().fichiers_sondes(), "planchers": chemin}
    etats, directions = P.regle_des_sondes_lues(spec, fichiers)
    assert etats["tromperie-c2"] == "sans objet" and etats["enjeux-c2"] == "lue"
    assert not any(d.nom.startswith("tromperie-c2") for d in directions)


def test_condition_sans_aucun_lot_et_egalite_a_l_extrait_calculee(monde):
    cles, suites, lignes = monde.actions
    vides = [k for k, l in enumerate(lignes) if l["condition"] == "TJ100"]

    def vider(c, s, l):
        for k in vides:
            s[k] = [FIN]
            l[k]["texte"] = ""

    course = monde.course_modifiee("tj-vide", vider)
    r = monde.passe(extrait=course["extrait"])
    trace = r["trace"]
    assert trace["conditions"]["TJ100"] == {"adaptateur_et_dose_relus_egaux": "oui", "actions": len(vides),
                                            "actions_sans_jeton_note": len(vides), "jetons_notes": 0}
    assert all(g["etat"] == "tenue" for g in trace["gardes"].values())
    assert trace["controle_du_contexte"]["fraction_par_condition"]["TJ100"] is None
    assert all(a["egale_a_l_extrait"] == "oui" for a in trace["adaptateurs"].values())
    source = Path(P.__file__).read_text(encoding="utf-8")
    assert '"egale_a_l_extrait": "oui"}' not in source and "h.detach().clone()" in source
    t = P.TraceGardes()
    releves = P.garde_p1(monde.params(), monde.spec, t)
    assert releves["egales_a_l_extrait"] == {role: True for role in ("ids", "adaptateur_eleve", "adaptateur_temoin_jumeau")}


def test_lignes_par_lot_de_l_extrait_strictement_croissantes(monde):
    sain = contenu_extrait("20261118-235959-course", monde.chemins["dossier_rel"], monde.chemins["ids"].parent)
    double = json.loads(json.dumps(sain))
    double["etats_par_lot_evaluation"].insert(1, dict(double["etats_par_lot_evaluation"][0]))
    refus(lambda: P.lire_extrait_du_cote_expose(json.dumps(double), monde.spec), "non rangées par condition puis par lot")
    saute = json.loads(json.dumps(sain))
    saute["etats_par_lot_evaluation"][1]["lot"] = 7                                    # croissant, non contigu : permis
    assert P.lire_extrait_du_cote_expose(json.dumps(saute), monde.spec)["run_id"] == "20261118-235959-course"


# ----------------------------------------------------------------------------------------------------------------------
# Brouillon 12 : recherche des directions par leur nom ; vecteur ou biais non fini et nom en double arrêtent la passe.
# ----------------------------------------------------------------------------------------------------------------------

def _fichiers_avec(monde, nom: str, **listes) -> tuple[P.Specification, dict]:
    """Fichiers de sondes jouets remplacés (legeres, neuves ou planchers) et spécification à leurs empreintes."""
    fichiers = dict(monde.params().fichiers_sondes())
    empreintes = dict(monde.spec.empreintes_fichiers_sondes)
    for role, liste in listes.items():
        fichiers[role] = monde.racine / "donnees" / "sondes" / f"{role}-{nom}.npz"
        empreintes[role] = ecrire_sondes(fichiers[role], liste, {"principales": {}})
    return dataclasses.replace(monde.spec, empreintes_fichiers_sondes=tuple(sorted(empreintes.items()))), fichiers


def _copie(s, **champs):
    return dataclasses.replace(s, **champs)


def test_directions_cherchees_par_leur_nom_dans_l_ordre_de_leur_numero(monde):
    planchers = list(monde.sondes["planchers"])
    spec, fichiers = _fichiers_avec(monde, "melange", planchers=planchers[::-1])                  # rang du fichier inversé
    etats, directions = P.regle_des_sondes_lues(spec, fichiers)
    assert etats["tromperie-c2"] == "lue" and etats["enjeux-c2"] == "lue"
    assert [d.nom for d in directions][1:1 + N_PLANCHER] == [f"tromperie-c2-t07-plancher-{k}" for k in range(N_PLANCHER)]
    reference = {d.nom: d for d in P.regle_des_sondes_lues(monde.spec, monde.params().fichiers_sondes())[1]}
    assert all(np.array_equal(d.w, reference[d.nom].w) and d.b == reference[d.nom].b for d in directions)
    # dissimulation : ordre de l'index du fichier ; une direction de famille « plancher » d'une autre couche, comptée, la
    # rend « sans objet » (801 pour 800) ; une de moins aussi
    neuves = list(monde.sondes["neuves"])
    de_plus = SondeLineaireJetons("dissimulation-c3-plancher-0", 3, "max", np.ones(LARGEUR), 0.0, None, "plancher")
    for nom, liste in (("couche-en-trop", neuves + [de_plus]), ("une-de-moins", neuves[:-1])):
        spec, fichiers = _fichiers_avec(monde, nom, neuves=liste)
        etats, directions = P.regle_des_sondes_lues(spec, fichiers)
        assert etats["dissimulation-c2"] == "sans objet" and etats["tromperie-c2"] == "lue"
        assert not any(d.nom.startswith("dissimulation-c2") for d in directions)
    # le compte est bon mais une direction n'est pas à la couche décisive : « sans objet »
    autre_couche = neuves[:-1] + [_copie(neuves[-1], couche=3)]
    spec, fichiers = _fichiers_avec(monde, "couche-fausse", neuves=autre_couche)
    assert P.regle_des_sondes_lues(spec, fichiers)[0]["dissimulation-c2"] == "sans objet"
    # un nom attendu manquant, remplacé par un numéro hors de 0 à 799 : « sans objet »
    hors = [_copie(p, nom="tromperie-c2-t07-plancher-99") if p.nom == "tromperie-c2-t07-plancher-2" else p for p in planchers]
    spec, fichiers = _fichiers_avec(monde, "numero-hors", planchers=hors)
    assert P.regle_des_sondes_lues(spec, fichiers)[0]["tromperie-c2"] == "sans objet"


def test_vecteur_ou_biais_non_fini_et_nom_en_double_arretent_la_passe(monde):
    planchers, legeres, neuves = (list(monde.sondes[r]) for r in ("planchers", "legeres", "neuves"))
    infini = np.array(planchers[0].w)
    infini[3] = np.inf
    cas = {
        "plancher-vecteur": ({"planchers": [_copie(planchers[0], w=infini)] + planchers[1:]}, "tromperie-c2-t07-plancher-0 : vecteur non fini"),
        "plancher-biais": ({"planchers": planchers[:-1] + [_copie(planchers[-1], b=float("nan"))]}, "enjeux-c2-t07-plancher-4 : biais non fini"),
        "plancher-dissimulation": ({"neuves": neuves[:-1] + [_copie(neuves[-1], b=float("inf"))]}, "dissimulation-c2-plancher-4 : biais non fini"),
        "sonde-descriptive": ({"legeres": legeres[:2] + [_copie(legeres[2], b=float("nan"))] + legeres[3:]}, "tromperie-c1 : biais non fini"),
        "sonde-decisive": ({"legeres": legeres[:3] + [_copie(legeres[3], w=infini)] + legeres[4:]}, "enjeux-c2 : vecteur non fini"),
    }
    for nom, (listes, motif) in cas.items():
        spec, fichiers = _fichiers_avec(monde, nom, **listes)
        refus(lambda: P.regle_des_sondes_lues(spec, fichiers), motif)                    # arrêt, jamais « sans objet »
    # dans la passe : arrêt sous la garde des entrées, avant le jetoniseur
    spec, fichiers = _fichiers_avec(monde, "dans-la-passe", planchers=[_copie(planchers[0], w=infini)] + planchers[1:])
    chargeur = monde.chargeur()
    p = monde.params(planchers=fichiers["planchers"])
    refus(lambda: P.executer_passe(p, spec, chargeur), "vecteur non fini : la passe s'arrête")
    arret = trace_d_arret(p.sortie)
    assert arret["gardes"]["P1"]["etat"] == "non tenue" and chargeur.tok is None
    # nom de sonde des couches descriptives qui paraît deux fois dans l'index : arrêt (le lecteur du dépôt refuse d'écrire
    # un tel fichier ; l'index est donc écrit ici à la main, par la même recette)
    double = monde.racine / "donnees" / "sondes" / "legeres-nom-en-double.npz"
    index, tableaux = [], {}
    for k, s_ in enumerate(legeres + [legeres[2]]):
        index.append({"classe": "SondeLineaireJetons", "nom": s_.nom, "couche": int(s_.couche), "agregation": s_.agregation,
                      "famille": s_.famille, "b": float(s_.b), "empreinte": s_.empreinte(), "tableaux": ["w"]})
        tableaux[f"s{k}_w"] = np.asarray(s_.w, dtype=np.float64)
    tableaux["index"] = np.frombuffer(json.dumps({"sondes": index, "meta": {}}, ensure_ascii=False, sort_keys=True).encode("utf-8"), dtype=np.uint8)
    with open(double, "wb") as f:
        np.savez(f, **tableaux)
    sha = sceller(double)
    spec = dataclasses.replace(monde.spec, empreintes_fichiers_sondes=tuple(
        (r, sha if r == "legeres" else h) for r, h in monde.spec.empreintes_fichiers_sondes))
    fichiers = {**monde.params().fichiers_sondes(), "legeres": double}
    refus(lambda: P.regle_des_sondes_lues(spec, fichiers), "tromperie-c1 trouvée sous son nom mais non conforme .*nom en double")


def test_empreintes_des_fichiers_de_configuration_du_modele_celles_du_texte():
    assert P.SPECIFICATION_TEXTE.empreintes_fichiers_modele == (
        ("config.json", "29e4c210b0d6ac178b16b2a255a568bdb23b581e50ca1ef6a6d071dd85704e6e"),
        ("generation_config.json", "189fb0c0d7fd8a527db217c0a60a0e013f0394cd8800f9697a666a9e75e5f7fd"),
        ("tokenizer.json", "79e3e522635f3171300913bb421464a87de6222182a0570b9b2ccba2a964b2b4"),
        ("tokenizer_config.json", "177c7b61e616fecb84c17ce0591acb92c6c4d60e9ac5ababfb940ff23bbcd424"))


# ----------------------------------------------------------------------------------------------------------------------
# Brouillon 13 : unicité du nom de la sonde décisive ; finitude avant toute autre condition ; aucun score imprimé.
# ----------------------------------------------------------------------------------------------------------------------

def _ecrire_index_a_la_main(chemin: Path, sondes) -> str:
    """Fichier de sondes dont l'index peut porter deux fois le même nom (le lecteur du dépôt refuse de l'écrire)."""
    index, tableaux = [], {}
    for k, s_ in enumerate(sondes):
        index.append({"classe": "SondeLineaireJetons", "nom": s_.nom, "couche": int(s_.couche), "agregation": s_.agregation,
                      "famille": s_.famille, "b": float(s_.b), "empreinte": s_.empreinte(), "tableaux": ["w"]})
        tableaux[f"s{k}_w"] = np.asarray(s_.w, dtype=np.float64)
    tableaux["index"] = np.frombuffer(json.dumps({"sondes": index, "meta": {}}, ensure_ascii=False, sort_keys=True).encode("utf-8"), dtype=np.uint8)
    with open(chemin, "wb") as f:
        np.savez(f, **tableaux)
    return sceller(chemin)


def test_sonde_decisive_dont_le_nom_parait_deux_fois_est_sans_objet(monde):
    legeres = list(monde.sondes["legeres"])
    chemin = monde.racine / "donnees" / "sondes" / "legeres-decisive-en-double.npz"
    sha = _ecrire_index_a_la_main(chemin, legeres + [legeres[1]])                    # « tromperie-c2 » au rang 1 et au rang 6
    spec = dataclasses.replace(monde.spec, empreintes_fichiers_sondes=tuple(
        (r, sha if r == "legeres" else h) for r, h in monde.spec.empreintes_fichiers_sondes))
    fichiers = {**monde.params().fichiers_sondes(), "legeres": chemin}
    etats, directions = P.regle_des_sondes_lues(spec, fichiers)
    assert etats["tromperie-c2"] == "sans objet" and etats["enjeux-c2"] == "lue" and etats["dissimulation-c2"] == "lue"
    assert not any(d.nom.startswith("tromperie-c2") for d in directions)             # ni elle, ni son plancher
    # sain : le même fichier sans le doublon rend la sonde « lue » (même écriture à la main)
    chemin = monde.racine / "donnees" / "sondes" / "legeres-a-la-main.npz"
    sha = _ecrire_index_a_la_main(chemin, legeres)
    spec = dataclasses.replace(monde.spec, empreintes_fichiers_sondes=tuple(
        (r, sha if r == "legeres" else h) for r, h in monde.spec.empreintes_fichiers_sondes))
    assert P.regle_des_sondes_lues(spec, {**fichiers, "legeres": chemin})[0]["tromperie-c2"] == "lue"


def test_finitude_controlee_avant_toute_autre_condition(monde):
    legeres, neuves, planchers = (list(monde.sondes[r]) for r in ("legeres", "neuves", "planchers"))
    # (1) la sonde décisive serait « sans objet » (empreinte de vecteur fausse dans la table) ET une de ses directions de
    # plancher porte un biais non fini : la passe s'arrête, elle ne rend pas « sans objet »
    spec, fichiers = _fichiers_avec(monde, "b13-plancher", planchers=[_copie(planchers[0], b=float("nan"))] + planchers[1:])
    d = list(spec.sondes_decisives)
    d[0] = dataclasses.replace(d[0], empreinte_vecteur="0" * 64)
    refus(lambda: P.regle_des_sondes_lues(dataclasses.replace(spec, sondes_decisives=tuple(d)), fichiers), "biais non fini")
    # (2) une direction candidate hors des noms attendus (une « direction de plus ») et non finie : arrêt aussi
    de_plus = SondeLineaireJetons("enjeux-c2-t07-plancher-bis", 1, "max", np.full(LARGEUR, np.inf), 0.0, None, "autre")
    spec, fichiers = _fichiers_avec(monde, "b13-de-plus", planchers=planchers + [de_plus])
    refus(lambda: P.regle_des_sondes_lues(spec, fichiers), "enjeux-c2-t07-plancher-bis : vecteur non fini")
    # … la même, finie : « sans objet », quelles que soient sa famille et sa couche
    spec, fichiers = _fichiers_avec(monde, "b13-de-plus-finie", planchers=planchers + [_copie(de_plus, w=np.ones(LARGEUR))])
    assert P.regle_des_sondes_lues(spec, fichiers)[0]["enjeux-c2"] == "sans objet"
    # (3) une entrée qui porte le nom d'une sonde nommée, dans un autre fichier que le sien, non finie : arrêt
    intruse = SondeLineaireJetons("dissimulation-c2", 2, "max", np.ones(LARGEUR), float("inf"))
    spec, fichiers = _fichiers_avec(monde, "b13-autre-fichier", legeres=legeres + [intruse])
    refus(lambda: P.regle_des_sondes_lues(spec, fichiers), "dissimulation-c2 : biais non fini")
    # (4) une sonde des couches descriptives non conforme ET une autre non finie : c'est la finitude qui arrête d'abord
    spec, fichiers = _fichiers_avec(monde, "b13-ordre", legeres=legeres[:5] + [_copie(legeres[5], b=float("nan"))])
    desc = (P.SondeDescriptive("dissimulation-c1", "neuves", 3),) + spec.sondes_descriptives[1:]
    refus(lambda: P.regle_des_sondes_lues(dataclasses.replace(spec, sondes_descriptives=desc), fichiers), "enjeux-c1 : biais non fini")
    # sain : une sonde d'un autre nom, non projetée, n'entre pas dans ce contrôle
    autre = SondeLineaireJetons("autre-concept-c2", 2, "max", np.full(LARGEUR, np.nan), 0.0)
    spec, fichiers = _fichiers_avec(monde, "b13-hors-portee", legeres=legeres + [autre])
    assert P.regle_des_sondes_lues(spec, fichiers)[0]["tromperie-c2"] == "lue"


def test_aucun_score_dans_la_sortie_standard_ni_au_journal(monde, saine, capsys):
    """Du côté exposé, nul ne lit un score : la passe et l'essai à blanc n'en impriment ni n'en consignent aucun hors des
    fichiers 1, 2 et 4 de la livraison. Le résultat rendu, le journal et le rapport ont des clés fermées, sans score."""
    assert set(saine) - {"params_sortie"} == {"mode", "bordereau", "bordereau_sha256", "livraison", "manifeste", "trace",
                                              "taille_totale", "mesures"}
    assert set(saine["mesures"]) == {"actions", "actions_d_au_moins_un_jeton_note", "jetons_notes", "directions",
                                     "plus_longue_transcription_en_jetons", "jetons_de_toutes_les_transcriptions",
                                     "sous_echantillon_couche_decisive", "sous_echantillon_couches_descriptives",
                                     "clean_up_tokenization_spaces", "sondes"}
    manifeste = json.loads(Path(saine["manifeste"]).read_text(encoding="utf-8"))
    journal = json.loads((monde.racine / "diag" / manifeste["run_id"] / "journal-passe-barreau8-v1.json").read_text(encoding="utf-8"))
    assert set(journal["resultat"]) == {"bordereau_sha256", "empreintes_des_adaptateurs_relues_sur_le_modele", "chemins_lus",
                                        "ouvertures_hors_des_racines_surveillees", "fichiers_du_modele", "mesures",
                                        "heures_depuis_le_debut_de_la_location"}
    capsys.readouterr()
    r = monde.passe(mode="blanc")
    assert capsys.readouterr().out == ""                                               # la passe n'imprime rien elle-même
    assert set(r["contenu"]) == {"essai_a_blanc", "gardes", "non_jouees_faute_de_modele", "mesures",
                                 "tailles_des_fichiers_de_donnees", "taille_de_la_trace", "taille_totale_de_la_livraison",
                                 "taille_max", "chemin_prive_lu", "duree_secondes"}
    source = Path(P.__file__).read_text(encoding="utf-8")
    # cinq impressions en tout, dans la seule ligne de commande : empreintes des modules, bordereau du code, rapport des
    # modes sans poids (mesures et tailles), ligne « LIVRAISON ÉCRITE », cause d'un arrêt
    assert source.count("print(") == 5
    # le nom de la course de la trace est le `run_id` de l'extrait du côté exposé, tel quel
    extrait = json.loads(monde.chemins["extrait"].read_text(encoding="utf-8"))
    assert saine["trace"]["course"] == {"run_id": extrait["run_id"], "commit_lancement": extrait["commit_lancement"]}


# ----------------------------------------------------------------------------------------------------------------------
# Additif 2, M-4 et M-5 : table neuve des constantes, constantes de forme, rapport antérieur.
# ----------------------------------------------------------------------------------------------------------------------

def _registre_avec_table(monde, nom: str, table) -> Path:
    chemin = monde.racine / "docs" / f"constantes-{nom}-v1.json"
    ecrire_scelle(chemin, table if isinstance(table, str) else json.dumps(table, ensure_ascii=False, sort_keys=True))
    return ecrire_code(monde.racine, nom, constantes=chemin)


@pytest.mark.parametrize("nom, table, motif", [
    ("table-noeud", lambda s: table_jouet(s, mot_d_ensemble="nœud", constantes=None), "ne dit pas « report »"),
    ("table-sans-constantes", lambda s: dict(table_jouet(s), constantes=None), "ne dit pas « report »"),
    ("table-cinq-couverts", lambda s: dict(table_jouet(s), champs_changes=table_jouet(s)["champs_changes"]
                                            + [{"champ": "textes.fichier", "statut": P.STATUT_COUVERT}]), "au lieu des quatre"),
    ("table-trois-couverts", lambda s: dict(table_jouet(s), champs_changes=table_jouet(s)["champs_changes"][1:]), "au lieu des quatre"),
    ("table-champ-noeud", lambda s: dict(table_jouet(s), champs_changes=table_jouet(s)["champs_changes"]
                                          + [{"champ": "calcul.attention", "statut": "nœud"}]), "est un « nœud »"),
    ("table-deux-episodes", lambda s: table_jouet(s, constantes={"E": 2}), "hors du cas couvert"),
    ("table-cle-repetee", lambda s: json.dumps(table_jouet(s)).replace('"mot_d_ensemble"', '"mot_d_ensemble": "report", "mot_d_ensemble"', 1), "clé répétée"),
    ("table-autre-lot", lambda s: table_jouet(s, constantes={"L": 8}), "constantes de forme du code différentes de la table neuve : .'lot'"),
    ("table-autre-pas", lambda s: table_jouet(s, constantes={"pas_couche_decisive": 4}), "'pas_sous_echantillon_decisif'"),
    ("table-autre-invite", lambda s: table_jouet(s, constantes={"invites": ["H1-autre"]}), "'invite'"),
    ("table-deux-invites", lambda s: table_jouet(s, constantes={"invites": ["H1-classification", "H1-autre"]}), "une seule invite"),
    ("table-autre-dose", lambda s: table_jouet(s, constantes={"conditions": [dict(c, dose=0.25) if c["nom"] == "B50" else c
                                                                              for c in table_jouet(s)["constantes"]["conditions"]]}), "'conditions'"),
    ("table-autre-fichier", lambda s: table_jouet(s, constantes={"noms_de_fichiers": dict(table_jouet(s)["constantes"]["noms_de_fichiers"],
                                                                                          identifiants="ids.npz")}), "'nom_fichier_identifiants'"),
])
def test_m4_table_neuve_artefacts(monde, nom, table, motif):
    registre = _registre_avec_table(monde, nom, table(monde.spec))
    chargeur = monde.chargeur()
    p = monde.params(registre=registre)
    refus(lambda: P.executer_passe(p, monde.spec, chargeur), motif)
    arret = trace_d_arret(p.sortie)
    assert arret["gardes"]["P0"]["etat"] == "non tenue" and arret["gardes"]["P1"]["etat"] == "non jouée"
    assert chargeur.tok is None


def test_m4_table_d_une_autre_empreinte_et_absente(monde):
    registre = ecrire_code(monde.racine, "table-modifiee", constantes=monde.racine / "docs" / "constantes-jouet-v1.json")
    copie = monde.racine / "docs" / "constantes-jouet-v1.json"
    sauve = copie.read_bytes()
    try:
        copie.write_text(json.dumps(table_jouet(monde.spec, avertissement="autre")), encoding="utf-8")
        refus(lambda: monde.passe(registre=registre), "empreinte .* ≠ scellée|n'est pas celle du bordereau")
        copie.unlink()
        refus(lambda: monde.passe(registre=registre), "absent")
    finally:
        copie.write_bytes(sauve)
    assert verifier(copie) == monde.sha["constantes"]


def test_m4_specification_depuis_table_saine_et_constante_differente(monde):
    s = P.specification_depuis_table(monde.spec, table_jouet(monde.spec))
    assert s == monde.spec                                                     # sain : la table redonne la spécification
    refus(lambda: P.specification_depuis_table(dataclasses.replace(monde.spec, n_taches=5), table_jouet(monde.spec)),
          "'n_taches'")
    refus(lambda: P.specification_depuis_table(dataclasses.replace(monde.spec, disque_transitoire=1), table_jouet(monde.spec)),
          "'disque_transitoire'")


def test_specification_du_texte_egale_aux_valeurs_de_l_additif_2():
    """Les constantes de forme écrites dans le code sont celles que M-4 attend de la table neuve (T = 64, E = 1, A = 10,
    J = 400, L = 8, conditions et doses, pas 16 et 128, n15 = 161, n7 = 21, place libre 3 100 000 000, tâches, adaptateurs
    de rang 16 et alpha 32 sur les quatre projections, invite H1-classification, aucun motif ajouté) ; extrait épinglé."""
    from controle_ia.barreau8_moniteurs import comparer_interface_v6_v7_v2 as cmp

    s = P.SPECIFICATION_TEXTE
    v = cmp.VALEURS_ATTENDUES_V7
    assert (s.n_taches, s.episodes_par_tache, s.pas_par_episode, s.max_jetons_action, s.lot) == (v["T"], v["E"], v["A"], v["J"], v["L"])
    assert [c.nom for c in s.conditions] == v["ordre_des_conditions"]
    assert [(c.adaptateur, c.dose) for c in s.conditions] == [("eleve", 0.0), ("eleve", 0.5), ("eleve", 1.0), ("temoin-jumeau", 1.0)]
    assert (s.pas_sous_echantillon_decisif, s.pas_sous_echantillon_descriptif, s.n15, s.n7) == (16, 128, 161, 21)
    assert s.taille_max + s.disque_transitoire == v["place_libre"]
    assert (s.chemin_taches, s.empreinte_taches) == (v["taches"]["chemin"], v["taches"]["sha256"])
    assert (s.rang, s.alpha, list(s.cibles)) == (16, 32.0, v["adaptateurs"]["projections"])
    assert s.invite == "H1-classification" and s.motifs_prives_ajoutes == () and s.prefixe_phase == "evaluation-"
    assert s.nom_fichier_identifiants == "ids-actions-evaluation-iib-v5.json"
    assert dict(s.fichiers_adaptateurs) == {"eleve": "adaptateur-eleve-iib-v5.pt", "temoin-jumeau": "adaptateur-temoin-jumeau-iib-v5.pt"}
    assert s.empreinte_extrait == "1ff87c08f5170fa7319349aa8cc1fc17a72689bcadd52295aff7856a0fbf992f"
    assert s.dossier_de_la_course == "diag/20261122-202132-iib-reel"
    assert P.fichiers_de_la_course(s) == {
        "ids": "diag/20261122-202132-iib-reel/ids-actions-evaluation-iib-v5.json",
        "adaptateur_eleve": "diag/20261122-202132-iib-reel/adaptateur-eleve-iib-v5.pt",
        "adaptateur_temoin_jumeau": "diag/20261122-202132-iib-reel/adaptateur-temoin-jumeau-iib-v5.pt"}
    assert dict(s.empreintes_fichiers_modele)["config.json"] == "29e4c210b0d6ac178b16b2a255a568bdb23b581e50ca1ef6a6d071dd85704e6e"


def test_m5_rapport_de_conformite_de_la_version_5_refuse(monde, monkeypatch):
    monkeypatch.setattr(P, "SHA_RAPPORT_CONFORMITE_ANTERIEUR", monde.sha["rapport"])
    refus(lambda: monde.passe(), "celui de la version 5")


def test_m5_ligne_de_code_anterieure_ne_compte_pas_mais_une_posterieure_suffit(monde):
    registre = ecrire_code(monde.racine, "anterieure-et-posterieure", "code antérieur puis postérieur")
    r = monde.passe(registre=registre, mode="entrees")
    assert r["entrees"] == "conformes"
