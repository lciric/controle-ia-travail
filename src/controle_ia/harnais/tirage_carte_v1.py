"""Tirage des jetons sur l'appareil du modèle, v1 (correctif 0020) : chemin NEUF, à côté de l'ancien, jamais à sa place.

Constat (diagnostic de la mère, 22 novembre) : `harnais.episode.generer_lot`, `environnements.noter_rejeu_juges_v2.
generer_lot_borne` et `iib.modele_v1.ModeleTorch._suites_cache_duplique` copient à chaque pas les logits du dernier jeton vers
le processeur (un vocabulaire de 128 000 jetons par ligne), puis font softmax et `multinomial` ligne par ligne, avec un
générateur processeur par ligne. Sur une carte, c'est un aller-retour et une boucle Python par ligne et par jeton.

**Méthode retenue : Gumbel-max à bruit compté** (et non des générateurs par ligne sur la carte).
- Jeton tiré = argmax(logits / T + G), G de loi de Gumbel i.i.d. par jeton du vocabulaire : c'est un tirage *exact* de
  softmax(logits / T), sans softmax ni normalisation.
- G est une fonction pure de (graine de la ligne, numéro du pas, indice du jeton), calculée par un hachage entier vectorisé
  (`_melange32`, multiplications par une constante < 2³¹ sur des valeurs < 2³², donc sans dépassement des entiers de 64 bits,
  identique sur processeur et sur carte), deux tirages de 32 bits réunis en un uniforme de 53 bits, puis G = −log(−log(u)) en
  double précision. Aucune boucle Python par ligne, aucune copie des logits, aucun état de générateur.
- Pourquoi pas des générateurs par ligne sur la carte : un `torch.Generator` par ligne impose une boucle par ligne (un appel de
  tirage par générateur) ; et l'état d'un générateur dépend de tout ce qu'il a tiré avant. Le bruit compté, lui, ne dépend que
  de (graine, pas, jeton) : **une ligne ne dépend pas des autres lignes du lot**, ni de leur nombre, ni de leur ordre ; et la
  même ligne rejouée seule rend les mêmes jetons (à logits égaux).
- Ce qui change par rapport à l'ancien chemin : le flux aléatoire. Mêmes graines par ligne, même loi, **pas les mêmes jetons**
  que `multinomial` sous un générateur processeur. Les deux chemins ne se mélangent donc pas dans une même mesure. À température
  nulle : argmax sur les logits en simple précision, comme l'ancien.
- Ce qui ne change pas : interfaces et valeurs rendues, remplissage à gauche, positions explicites, cache, logits du dernier jeton
  seuls, jetons de fin gardés et lignes finies remplies de `pad_id`, arrêts (fin, budget, bloc clos), `decalage_positions`.
- Copies vers le processeur qui restent : à chaque pas, un booléen (« reste-t-il une ligne active ? ») et les indices des lignes
  qui viennent de finir ou de tirer un jeton déclencheur (pour l'arrêt « bloc clos », la fonction `arreter` de l'appelant ne
  se joue que sur ces lignes-là, en Python, comme dans l'ancien chemin) ; à la fin, les jetons et les longueurs ; et les logits
  **seulement** si `empreinte_logits` est demandé (diagnostic de rejeu, comme l'ancien).
- Résolution : uniforme sur 53 bits (deux hachages indépendants de 32 et 21 bits, correctif 0021) ; un jeton de probabilité inférieure à environ 2⁻⁵³ n'est jamais tiré (sans effet mesurable).

Gardes (essais `tests/test_tirage_carte_v1.py`) : graine entière dans [0, 2⁶⁴[ (sinon refus) ; logits finis à la ligne tirée
(un NaN, un +inf ou une ligne entièrement à −inf rendrait un argmax arbitraire : arrêt ; −inf sur une partie du vocabulaire reste permis, comme sous softmax) ; température finie ; lot, contextes et graines comme l'ancien.
"""
from __future__ import annotations

import math

import torch

from ..gardes import GardeArret

MASQUE32 = 0xFFFFFFFF
_MULT = 0x45D9F3B                       # constante du mélange (< 2³¹ : produit < 2⁶³, aucun dépassement)
_SEL_PAS, _SEL_JETON, _SEL_DEUX = 0x9E3779B1, 0x7F4A7C15, 0x2545F491
_SEL_JETON_2, _SEL_BASE_2 = 0x6C8E9CF5, 0x1B873593          # correctif 0021 (cl1, m1) : second hachage, indépendant du premier
METHODE = "gumbel-max à bruit compté (hachage entier de la graine, du pas et du jeton), v1, uniforme à 53 bits (correctif 0021)"


def _melange32(x: torch.Tensor) -> torch.Tensor:
    """Hachage entier de 32 bits (valeurs dans [0, 2³²[), en int64, vectorisé, identique sur tout appareil."""
    x = x & MASQUE32
    x = ((x >> 16) ^ x) * _MULT & MASQUE32
    x = ((x >> 16) ^ x) * _MULT & MASQUE32
    return (x >> 16) ^ x


def moities_des_graines(graines, appareil) -> torch.Tensor:
    """(B, 2) : moitiés basse et haute de chaque graine ; refus d'une graine hors de [0, 2⁶⁴[ ou non entière."""
    out = []
    for g in graines:
        if isinstance(g, bool) or not isinstance(g, int) or not 0 <= g < 2 ** 64:
            raise GardeArret(f"graine {g!r} : entier dans [0, 2^64[ exigé (tirage sur l'appareil)")
        out.append((g & MASQUE32, g >> 32))
    return torch.tensor(out, dtype=torch.int64, device=appareil)


def deux_hachages(moities: torch.Tensor, pas: int, taille_vocabulaire: int) -> tuple[torch.Tensor, torch.Tensor]:
    """(a, b), chacun (B, V) dans [0, 2³²[ : deux hachages **indépendants** de (graine, pas, jeton) (correctif 0021, cl1, m1)."""
    appareil = moities.device
    base = _melange32(_melange32(moities[:, 0] ^ _SEL_DEUX) ^ moities[:, 1])
    base = _melange32(base ^ ((int(pas) * _SEL_PAS) & MASQUE32))                             # (B,)
    v = torch.arange(int(taille_vocabulaire), dtype=torch.int64, device=appareil)
    a = _melange32(base[:, None] ^ _melange32(v ^ _SEL_JETON)[None, :])
    b = _melange32(_melange32(base ^ _SEL_BASE_2)[:, None] ^ _melange32(v ^ _SEL_JETON_2)[None, :])
    return a, b


def bruit_de_gumbel(moities: torch.Tensor, pas: int, taille_vocabulaire: int) -> torch.Tensor:
    """(B, V) en double précision : G[b, v] = −log(−log(u(graine_b, pas, v))), fonction pure de ses entrées ; u sur 53 bits,
    21 bits de `a` et 32 bits de `b`."""
    a, b = deux_hachages(moities, pas, taille_vocabulaire)
    u = ((a >> 11).double() * 2.0 ** 32 + b.double() + 0.5) / 2.0 ** 53                       # 21 + 32 = 53 bits, u dans ]0, 1[
    return -torch.log(-torch.log(u))


def tirer(logits: torch.Tensor, temperature: float, moities: torch.Tensor, pas: int, actives: torch.Tensor | None = None) -> torch.Tensor:
    """Un jeton par ligne, sur l'appareil des logits : argmax à température nulle, sinon Gumbel-max. Rend (B,) long.
    `actives` (correctif 0021, cl1, m2) : la garde des logits ne juge que les lignes actives (une ligne finie n'arrête rien,
    comme dans l'ancien chemin, qui ne lisait pas ses logits)."""
    if not math.isfinite(float(temperature)):
        raise GardeArret(f"température {temperature!r} non finie (refus)")
    l = logits.float()
    vues = l if actives is None else l[actives]
    if vues.numel() and bool(torch.isnan(vues).any() | torch.isposinf(vues).any() | torch.isneginf(vues.amax(dim=-1)).any()):
        raise GardeArret("logits invalides au tirage (NaN, +inf, ou ligne entièrement à −inf) : arrêt, aucun argmax arbitraire")
    if temperature <= 0:
        return torch.argmax(l, dim=-1)
    return torch.argmax(l.double() / float(temperature) + bruit_de_gumbel(moities, pas, l.shape[-1]), dim=-1)


def _verifier_lot(contextes, graines, max_nouveaux) -> None:
    if max_nouveaux < 1:
        raise GardeArret("max_nouveaux < 1")
    if not contextes or len(graines) != len(contextes) or any(len(c) == 0 for c in contextes):
        raise GardeArret("lot vide, contexte vide ou graines en nombre différent des contextes")


def _lot_rempli(contextes, pad_id):
    B, L = len(contextes), max(len(c) for c in contextes)
    ids = torch.full((B, L), int(pad_id), dtype=torch.long)
    masque = torch.zeros((B, L), dtype=torch.long)
    for r, c in enumerate(contextes):
        ids[r, L - len(c):] = torch.tensor(c, dtype=torch.long)
        masque[r, L - len(c):] = 1
    return B, L, ids, masque, (masque.cumsum(dim=1) - 1).clamp(min=0)


def _boucle(modele, contextes, max_nouveaux, temperature, graines, fins, pad_id, decalage_positions=0, empreinte_logits=False,
            declencheurs=None, arreter=None):
    """Cœur commun : rend (jetons par ligne, plan, arrêts par ligne)."""
    import hashlib

    _verifier_lot(contextes, graines, max_nouveaux)
    B, L, ids, masque, positions = _lot_rempli(contextes, pad_id)
    appareil = next(modele.parameters()).device
    moities = moities_des_graines(list(graines), appareil)
    fins_t = torch.tensor(sorted(int(f) for f in fins), dtype=torch.long, device=appareil)
    decl_t = torch.tensor(sorted(int(f) for f in (declencheurs or ())), dtype=torch.long, device=appareil)
    sorties = torch.full((B, int(max_nouveaux)), int(pad_id), dtype=torch.long, device=appareil)
    longueurs = torch.zeros(B, dtype=torch.long, device=appareil)
    actives = torch.ones(B, dtype=torch.bool, device=appareil)
    arrets = ["budget"] * B
    empreintes = [hashlib.sha256() for _ in range(B)] if empreinte_logits else None
    masque_a, passes = masque.to(appareil), 0
    with torch.no_grad():
        sortie = modele(input_ids=ids.to(appareil), attention_mask=masque_a, position_ids=positions.to(appareil), use_cache=True,
                        logits_to_keep=1)
        suivante = (positions[:, -1:] + 1 + int(decalage_positions)).to(appareil)
        for pas in range(int(max_nouveaux)):
            logits = sortie.logits[:, -1]
            if empreintes is not None:                                   # diagnostic de rejeu seulement (comme l'ancien chemin)
                cpu = logits.to("cpu", torch.float32)
                act = actives.to("cpu").tolist()
                for r in range(B):
                    if act[r]:
                        empreintes[r].update(cpu[r].contiguous().numpy().tobytes())
            j = tirer(logits, temperature, moities, pas, actives)
            j = torch.where(actives, j, torch.full_like(j, int(pad_id)))
            sorties[:, pas] = j
            longueurs += actives.long()
            finit = actives & torch.isin(j, fins_t)
            if arreter is not None:
                cand = actives & ~finit & torch.isin(j, decl_t)
                for r in torch.nonzero(cand).flatten().tolist():          # seules les lignes au jeton déclencheur (rares)
                    if arreter(sorties[r, :pas + 1].tolist()):
                        actives[r] = False
                        arrets[r] = "bloc clos"
            for r in torch.nonzero(finit).flatten().tolist():
                arrets[r] = "fin"
            actives = actives & ~finit
            if not bool(actives.any()) or pas == int(max_nouveaux) - 1:
                break
            masque_a = torch.cat([masque_a, torch.ones((B, 1), dtype=torch.long, device=appareil)], dim=1)
            sortie = modele(input_ids=j[:, None], attention_mask=masque_a, position_ids=suivante, past_key_values=sortie.past_key_values,
                            use_cache=True, logits_to_keep=1)
            suivante = suivante + 1
            passes += 1
    lignes, n = sorties.to("cpu").tolist(), longueurs.to("cpu").tolist()
    nouveaux = [lignes[r][:n[r]] for r in range(B)]
    plan = {"longueur_remplie": L, "passes_decodage": passes, "remplissage": [L - len(c) for c in contextes], "tirage": METHODE}
    if empreintes is not None:
        plan["empreintes_logits"] = [h.hexdigest() for h in empreintes]
    return nouveaux, plan, arrets


def generer_lot_carte(modele, contextes, max_nouveaux: int, temperature: float, graines, fins, pad_id: int,
                      empreinte_logits: bool = False, decalage_positions: int = 0):
    """Même interface et mêmes valeurs rendues que `harnais.episode.generer_lot` (plan : plus la clé `tirage`)."""
    nouveaux, plan, _ = _boucle(modele, contextes, max_nouveaux, temperature, graines, fins, pad_id, decalage_positions, empreinte_logits)
    return nouveaux, plan


def generer_lot_borne_carte(modele, contextes, max_nouveaux: int, temperature: float, graines, fins, pad_id: int, declencheurs,
                            arreter):
    """Même interface que `environnements.noter_rejeu_juges_v2.generer_lot_borne` : (jetons, arrêts par ligne)."""
    nouveaux, _, arrets = _boucle(modele, contextes, max_nouveaux, temperature, graines, fins, pad_id, declencheurs=set(declencheurs),
                                  arreter=arreter)
    return nouveaux, arrets


def suites_cache_duplique_carte(modele, prefixe, graines, max_jetons: int, temperature: float, fins, pad_id: int):
    """Même rendu que `iib.modele_v1.ModeleTorch._suites_cache_duplique` : un préremplissage, cache dupliqué K fois, une graine
    par suite ; tirage sur l'appareil (le bruit d'une suite ne dépend que de sa graine, du pas et du jeton)."""
    K = len(graines)
    if not prefixe or K == 0:
        raise GardeArret("suites du jumeau : préfixe ou graines vides")
    appareil = next(modele.parameters()).device
    moities = moities_des_graines(list(graines), appareil)
    fins_t = torch.tensor(sorted(int(f) for f in fins), dtype=torch.long, device=appareil)
    sorties = torch.full((K, int(max_jetons)), int(pad_id), dtype=torch.long, device=appareil)
    longueurs = torch.zeros(K, dtype=torch.long, device=appareil)
    actives = torch.ones(K, dtype=torch.bool, device=appareil)
    pos = len(prefixe)
    with torch.no_grad():
        sortie = modele(input_ids=torch.tensor([list(prefixe)], device=appareil), use_cache=True, logits_to_keep=1)
        cache = sortie.past_key_values
        cache.batch_repeat_interleave(K)
        logits = sortie.logits[:, -1].repeat(K, 1)
        for pas in range(int(max_jetons)):
            j = tirer(logits, temperature, moities, pas, actives)
            j = torch.where(actives, j, torch.full_like(j, int(pad_id)))
            sorties[:, pas] = j
            longueurs += actives.long()
            actives = actives & ~torch.isin(j, fins_t)
            if not bool(actives.any()) or pas == int(max_jetons) - 1:
                break
            sortie = modele(input_ids=j[:, None], attention_mask=torch.ones((K, pos + 1), dtype=torch.long, device=appareil),
                            position_ids=torch.full((K, 1), pos, dtype=torch.long, device=appareil), past_key_values=cache,
                            use_cache=True, logits_to_keep=1)
            cache = sortie.past_key_values
            logits = sortie.logits[:, -1]
            pos += 1
    lignes, n = sorties.to("cpu").tolist(), longueurs.to("cpu").tolist()
    return [lignes[r][:n[r]] for r in range(K)]
