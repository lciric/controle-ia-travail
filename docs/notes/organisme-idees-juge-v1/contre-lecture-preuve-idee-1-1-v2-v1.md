# Contre-lecture (R2) — preuve, version 2, de l'idée 1.1 (poids du nul : nul limité, projection par blocs, lecture à 40 instants, rejet par famille) — v1

- Contre-lecteur : sous-agent neuf de la session mère. Je n'ai écrit ni cette preuve, ni la preuve v1, ni leurs
  contre-lectures, ni les brouillons du préenregistrement v2, ni la synthèse, ni les rendus des angles, ni leurs
  réfutations, ni le juge, ni les nuls v8 et v9.
- Date (UTC) : 2026-11-15, de 21:23 à 21:50 environ (`date -u`). Dépôt `/home/user/controle-ia-travail`, `main`, tête
  `119276b1` (commit de la preuve, 21:22:18). Aucun commit, aucune poussée, aucun appel réseau ni payant ; preuve non
  modifiée. Rien lu sous `diag/`, `runs/` de 7a ou 7b, `donnees/bras-attaque*`, `donnees/mode-tenu-a-l-ecart*`,
  `docs/notes/bras-attaque/`. Aucune valeur de clé lue ; ni `env` ni `printenv`.
- **Texte relu** : `docs/notes/organisme-idees-juge-v1/preuve-idee-1-1-poids-du-nul-v2.md`,
  `83789a45be3745f75527d92f943e7232e455157de8bce4080357b5597e204013` (égale à son compagnon), avec son dossier
  `preuve-idee-1-1-poids-du-nul-v2-outils/` (script et cinq sorties).
- Calculs : Python 3.13.18, numpy 2.4.6, scipy 1.17.1 (`.venv/bin/python -I -B`), processeur seul.

## 0. Verdict

**La preuve suffit comme préalable au scellement du préenregistrement : oui, après corrections** (section 6, couples
« ancien → nouveau »). Aucun bras du brouillon 3 ne perd sa garantie de taille. Deux majeurs, tous deux sur le texte de
la preuve, aucun sur un théorème de taille :

- **M1 — le constat « le trou de P4 n'est ouvert que par `sans_remise`, pas par `moyenne_glissante` » est faux.**
  `valider_loi` ne contrôle pas `lissage`. Une `moyenne_glissante` à lissage négatif est acceptée et prédit **contre**
  ce qu'elle a vu : fenêtre 1, lissage −0,6, deux issues → « l'autre issue, sûrement » ; fenêtre ≥ horizon, lissage −c →
  **la même loi que `sans_remise` [c, …, c]** (écart mesuré sur le code réel : 10⁻¹², le plancher). Sans garde :
  espérance exacte de la valeur e de bloc 4/3 (premier bloc de 2) et 3/2 (bloc de 2 suivant) ; Ville violée d'un facteur
  5,33 (blocs de 2, 12 tirages) ; **promotion à α = 0,05 avec probabilité 0,1016** (12 tirages, monde uniforme, terme
  projeté seul). Les deux gardes (refus par type, gel) couvrent ce cas : le lemme 3, le lemme 4 et le théorème 8 ne
  sont pas touchés. Ce qui tombe : une phrase des sections 0 et 11, et la lecture qu'on en tirerait (« Hg nul ⇒ les
  moyennes glissantes sont sûres »).
- **M2 — la première moitié de H4 (« V_m(t) ne dépend que de l'engagement et de y_1..y_t ») est fausse sur le code du
  v9 pour les membres par morceaux.** `maximiser_par_lots` traite en un lot les coupes de tous les instants, avec des
  arrêts communs (`dec.max() < DECREMENT_ARRET`, compteur de pas par palier, repli commun de la résolution). Mesuré sur
  une copie de travail : la valeur à t = 25 change quand on ne change que les issues 26 à 50 (23 valeurs sur 144, écart
  au plus 4,3·10⁻¹⁰ nat). **Les théorèmes de taille (1, 8, 10 (a), 11) n'emploient que la majoration V ≥ sup, vraie pour
  tout point, et tiennent.** Les énoncés « valeur arrêtée = valeur e » qui posent un temps d'arrêt sur une
  bibliothèque à membres par morceaux (corollaire 1 pour J9, La, Ld ; théorème 10 (b) ; proposition 13) ne tiennent
  que **sous la réserve** que D_t soit calculé sans lire d'issue postérieure à t. Le corollaire 9 (J9-P, La-P) n'est
  pas touché : W^reste n'a pas de membre par morceaux, et ses membres ajustés sont calculés instant par instant.

Rejeu du script de l'auteur : **cinq sorties identiques à l'octet**. Mes énumérations écrites à part retrouvent 4/3,
7/5, les huit espérances de premier bloc, et la taille de la réunion sous α. Vingt-huit empreintes citées : toutes
égales.

## 1. Pièces lues

Lues en entier : la preuve v2 (sections 0 à 15, annexe comparée au script par `diff` : identique) ; les cinq sorties ;
`selection_pari.py` de la copie `94bfd92`, l. 1 à 430 ; `nul_v9.py` de la copie `a41b7b5`, l. 1 à 112 et 150 à 584 ;
`nul_filles_v2.py`, `valeurs_ajustees` (l. 154 à 186) ; `cycle.py`, l. 305 à 330 ; [R-PROJ] § 5 ; du brouillon 3
(`ea6def09…06b8`, égale à son compagnon) : en-tête, « Garantie de chaque bras », « Bras », lignes Hs, Hm, Hg, H7.
**Survolées seulement** (plan, énoncés, passages cités — je le dis) : la preuve v1, [CL], la synthèse, [PROJ] § 3
(définition, P1 à P6), [R-UNI] § 8.1. **Non rouvertes** : [LIB], [R-LIB], [B1], [CL2], [PROJ] § 7 ; les renvois que la
preuve leur fait ne sont donc pas vérifiés par moi, sauf leurs empreintes.

## 2. Verdict par énoncé

| énoncé | verdict | motif |
|---|---|---|
| lemmes V, Λ, M | **tient** | arrêt optionnel borné ; q_t mesurable par rapport au passé (H5) suffit ; (b) est une inclusion d'événements, pas une propriété de surmartingale du minimum — écrit ainsi, juste |
| théorème 1 (La, Ld, taille) | **tient** | seule la majoration D_t ≥ log-vraisemblance du monde sert ; le certificat de `_certificats` (l. 218 à 229) est bien « valeur + max(0, plus grande dérivée à un sommet − t) », borné par 0, valide en tout point admissible |
| corollaire 1 (valeur e arrêtée ; e-BH) | **tient sous réserve** | M2 : τ n'est un temps d'arrêt que si D_t ne lit pas l'avenir ; théorème e-BH cité, non relu (dit) |
| proposition 2 (encadrements) | **tient** | l. 413 : s = −∞ et `np.unique(z[:t])` ; une coupe élaguée garde sa borne dans le maximum (l. 276 à 288, 317) |
| lemme 3 (garde « refus ») | **tient** (sur la copie) | j'ai recompté les clés par lesquelles `proba` descend : `lois` (dictionnaire ou liste), `defaut`, `composantes`, `si`, `sinon`, `loi`, `base` — toutes visitées par `types_de_la_loi` ; aucun état global ; `_condition` ne lit que l'instance |
| lemme 4 (garde « gel ») | **tient** ; (v) **sous réserve mineure** | fenêtre vide ⇒ loi uniforme seulement si le lissage est fini et non nul (lissage 0 : division par zéro, mesuré) |
| lemme 5 (valeur e de bloc) | **tient** | réserve à écrire : les lois connues L_j elles-mêmes ne doivent pas lire l'historique (m1) |
| lemme 6, proposition 7 | **tient** | condition d'optimalité et Jensen refaits à la main |
| théorème 8, corollaire 9 | **tient** | minimum traité par inclusion, classe par classe ; aux fins de bloc seulement ; W^reste de J9-P sans membre par morceaux, donc adapté |
| théorème 10 (a) | **tient** | |
| théorème 10 (b) | **tient sous réserve** | M2 |
| théorème 11 (J9-D, réunion) | **tient** | minimum de deux bornes hautes ; les trois événements sont dans R* ; vérifié par assertion suite par suite dans mon énumération |
| « S n'est pas une valeur e » | **tient** | 7/5 refait en fractions ; 1,50 sur mon cas à trois membres |
| proposition 12 | **tient** | |
| proposition 13 | **tient sous réserve** | M2 pour « temps d'arrêt » ; l'égalité des événements tient sans réserve |
| § 10.4, J9-Dc | **non établi** | l'auteur le dit ; préalable de code |
| § 11, contre-exemple 4/3 | **tient** | refait en fractions |
| § 11, « toutes avec `sans_remise` », le trou atteint « par celles qui savent la composition » | **faux** comme constat sur la grammaire | M1 |
| proposition 14 (lois estimées) | **tient** | sortie E identique au rejeu ; non refaite à part ; sans objet pour le banc |

## 3. Les hypothèses implicites, une à une

- **Indépendance des tirages frais.** H2 et H6 la posent. Le point fin : la graine des issues dérive de l'empreinte de
  l'engagement, donc de la carte ; la preuve conditionne à la carte et suppose le générateur indépendant d'elle. Vrai
  tant que la carte n'est pas écrite en connaissant la dérivation de la graine. À dire en une ligne (m4).
- **Poids gelés mesurables par rapport au passé.** P3 et P4 l'écrivent ; le pas 1 du lemme 5 est le seul à s'en servir,
  et il s'en sert correctement. Le brouillon 3 le garde par code (journal avant tirage, garde d'accès).
- **Linéarité du nul en ses poids.** Vraie pour les familles du v9. Les sommets sont bien ceux que dit la preuve : le
  polytope {μ_c ≥ 0, ρ ≥ 0, Σ_j μ_{c,j} + Σ_k ρ_k = 1 pour chaque cellule} est l'enveloppe convexe de « ρ = δ_k, μ = 0 »
  et de « ρ = 0, une loi connue par cellule » (produit de simplexes à masse de bruit commune).
- **Ce que le « certificat exact » majore.** Dans la projection : (1/b)·Σ_s m_s(θ) sur le polytope, donc E_θ[Π r_s]
  par l'inégalité des moyennes — **seulement** si les r_s sont fixés avant le bloc et si les issues du bloc sont
  indépendantes. Il ne majore rien si la carte lit le bloc (section 11 de la preuve, juste). Dans le v9 : le maximum de
  la log-vraisemblance d'une coupe sur les t premières instances, en tout point admissible.
- **Ville.** Chaque usage porte sur Λ (lemme Λ) ou sur W^{F*} aux fins de bloc (lemme 5), jamais sur le minimum
  lui-même. Les instants de lecture peuvent être quelconques pour la taille. La valeur arrêtée demande en plus
  l'adaptation (M2).
- **Lemme 3 et grammaire réelle.** Treize types dans `TYPES_LOI` ; `proba` en traite treize ; deux lisent
  `historique` ; six transmettent ; cinq sont des feuilles. Rien d'omis.

## 4. Le constat sur `moyenne_glissante` (point 4 de la demande)

`valider_loi`, l. 212 à 214, ne contrôle que `nombre_issues` et `fenetre`. Essai sur une copie de travail du code :

```
(i) lissage -0.6 : acceptée par valider_loi ; proba historique [], [0], [1] : [[0.5, 0.5], [0.0, 1.0], [1.0, 0.0]] ; types : ['moyenne_glissante']
(i) lissage -0.4 : acceptée par valider_loi ; proba historique [], [0], [1] : [[0.5, 0.5], [1.0, 0.0], [0.0, 1.0]] ; types : ['moyenne_glissante']
(i) lissage 0.0 : acceptée par valider_loi ; proba historique [], [0], [1] : ['ZeroDivisionError', [1.0, 0.0], [0.0, 1.0]] ; types : ['moyenne_glissante']
(i) lissage nan : acceptée par valider_loi ; proba historique [], [0], [1] : [[0.5, 0.5], [0.5, 0.5], [0.5, 0.5]] ; types : ['moyenne_glissante']
moyenne_glissante(fenêtre 200, lissage −c) contre sans_remise [c, …, c], code réel : plus grand écart de probabilité 9.999e-13
```

Mécanisme : (compte + λ)/(longueur + K·λ) avec λ < −fenêtre/K a numérateur et dénominateur négatifs tant que le compte
est sous |λ| ; la loi est ∝ max(0, |λ| − compte dans la fenêtre) : un tirage sans remise sur fenêtre glissante.
Énumération exacte (ma partie 4, sortie en annexe) : espérance de la valeur e de bloc 1,3333 puis 1,5000 ; sous gel
1,0000 partout ; sup_α P/α = 5,33 ; P(promotion à α = 0,05) = 0,1016 à 12 tirages.

**Lissage positif** : je n'ai pas trouvé de violation. Grille exacte (fenêtres 1 à 5, lissages 0,001 à 5, deux et trois
issues, blocs de 2 à 5, cinq historiques d'avant-bloc, mondes constants en grille) et 24 000 cartes composées
(`transformee`, `melange`, `enveloppe`, alternance par instance) : plus grande espérance 1,000000000000, atteinte à un
monde certain. **Ce n'est pas une preuve d'impossibilité** : raison heuristique seulement (une moyenne à lissage
positif tire la loi moyenne du bloc vers ce qui a été vu, ce qui baisse la valeur e).

**Juge complet** : dans une miniature (12 tirages, deux issues, famille linéaire à deux lois connues dépendant d'un
trait, W^reste = bibliothèque ordinaire du juge v0, monde ½·L1 + ½·L2), le terme projeté seul passe 1 (jusqu'à 1,49),
le minimum avec W^reste reste sous 1 sur les 24 cas essayés. Le point « ouvert » de la preuve (une carte de la
grammaire atteint-elle le trou dans le juge complet) **reste ouvert** ; il l'est maintenant pour les deux types.

## 5. Ce que le brouillon 3 emploie, bras par bras (point 3)

| bras | énoncé qui le couvre | repose sur du « plausible » ou de l'« ouvert » ? |
|---|---|---|
| La, Ld | théorème 1, proposition 2 | réserve log-linéaire du v8 (ouverte, héritée, commune à tous les bras à maximum) |
| J9-P, La-P avec refus | lemmes 3, 5, 6 ; théorème 8 | non ; lemme 3 prouvé sur la copie `94bfd92`, celle que le brouillon 3 cite pour le juge ; W^reste porte la réserve log-linéaire |
| J9-P avec gel | lemme 4 ; théorème 8 pour la carte gelée | non ; la promotion porte sur la carte gelée (dit) |
| W^reste | théorème 1, pas 1 et 2, numérateur = carte jugée | même définition dans les deux textes (bibliothèque privée des membres linéaires et par morceaux) |
| J9-D40 | théorème 10 (a) | non pour la taille ; **« sa valeur arrêtée reste une valeur e » (brouillon 3, « Garantie ») : sous la réserve M2** |
| J9-D | théorème 11 | non ; « famille » = membre nommé, comme R1 |
| J9-Dc | § 10.4 | **oui : plausible** ; bras descriptif, sans critère, retirable (dit dans les deux textes) |
| J9-P-nu | aucun (artefact voulu) | sans objet |
| lecture entre deux fins de bloc ; pari à fraction sous projection | ouverts | **non employés** : J9-P lu sur T₈ seulement, pari plein seulement |

Aucun bras à critère ne repose sur un énoncé « plausible » ou « ouvert », hors la réserve log-linéaire héritée. Le
brouillon 3 cite encore la preuve v1 et [R-UNI] comme appuis : à remplacer par la v2 une fois scellée.

## 6. Corrections demandées (ancien → nouveau)

1. **M1, section 0, point 6.** « avec la carte `sans_remise` de composition [1, 1], écrite dans la grammaire » →
   ajouter : « ; une `moyenne_glissante` à lissage négatif, que `valider_loi` accepte, donne la même violation (fenêtre
   ≥ horizon et lissage −c : même loi que `sans_remise` [c, …, c]) ».
2. **M1, section 11.** « sur 48 configurations […] 12 violent Ville sous la forme sans garde, toutes avec
   `sans_remise` » et « le trou n'est pas atteint par **toute** carte qui lit l'historique, il l'est par celles qui
   « savent » la composition du bloc » → « les quatre moyennes glissantes essayées ont un lissage positif ; à lissage
   négatif, `moyenne_glissante` prédit contre ce qu'elle a vu et ouvre le trou autant que `sans_remise` ; à lissage
   positif, aucune violation trouvée, sans preuve d'impossibilité ».
3. **M1, section 14.** Ligne « une carte de la grammaire atteint le trou dans le juge complet : ouvert » → préciser
   « pour les deux types qui lisent l'historique ».
4. **M2, H4.** « V_m(t) ne dépend que de l'engagement et de y_1..y_t » → « V_m(t) est calculé par le code sur
   l'engagement et les issues ; pour les membres par morceaux du v9, calculés en un lot sur tous les instants, il peut
   dépendre des issues postérieures à t par les arrêts communs du solveur (mesuré : 4·10⁻¹⁰ nat) ; la majoration, elle,
   vaut en tout point ». Et H7 : « D_t ne lit que y_1..y_t » → « hypothèse des seuls énoncés de valeur arrêtée ».
5. **M2, corollaire 1, théorème 10 (b), proposition 13.** Ajouter l'hypothèse « D_t (ou V*_m(t)) calculé sans lire
   d'issue postérieure à t — un appel par instant, issues tronquées — sinon énoncé non établi ». Théorème 10, « des
   solveurs qui peuvent différer (départs chaînés différents) » → « (départs chaînés et arrêts communs du lot) ».
6. **m1, P6.** Ajouter : « les lois connues L_j ne lisent pas l'historique (même test `types_de_la_loi` que pour la
   carte) ; sinon P_v(· | x_s) dépend des issues du bloc et le pas 1 du lemme 5 tombe ». Vrai sur le banc (lois
   `softmax`), non gardé en général.
7. **m2, lemme 4 (v).** « donc la loi uniforme » → « donc la loi uniforme si le lissage est fini et non nul ».
8. **m3, en-tête.** « rédaction de 20:45 à 21:35 UTC environ » : le fichier est daté de 21:21:13 et commité à
   21:22:18 → corriger l'heure de fin.
9. **m4, H2.** Ajouter : « le générateur des issues est indépendant de la carte : la carte n'est pas écrite en
   connaissant la dérivation de la graine ».

**Pour le préenregistrement (hors de cette preuve, à la mère de décider)** : remplacer les renvois à la preuve v1 par
la v2 ; marquer « valeur arrêtée de J9-D40 » sous la réserve M2 ; à P12 et à l'étage 7, écrire qu'un résultat nul sur
Hg (lissage 0,5) ne dit rien des moyennes glissantes à lissage négatif. Ajouter une ligne de banc à lissage négatif
serait un changement du plan : je le signale, je ne le demande pas.

## 7. Rejeu et énumérations indépendantes (point 2)

**Rejeu du script de l'auteur** (`134661a1…e30`, copié dans un dossier neuf du bloc-notes, parties A, B, C, E puis D ;
D : 5 min 21 s) : les cinq sorties sont identiques à l'octet aux fichiers versés (`cmp`), sorties d'erreur vides.

**Mon programme** (annexe A, bibliothèque standard seule, fractions exactes pour les parties 1, 2 et 4 (a)) :

| résultat | auteur | moi |
|---|---|---|
| E[e_B], `sans_remise` [1, 1], bloc de 2, p = 1/2 ; 0,3 ; 0,1 | 1,333333 ; 1,120000 ; 0,480000 | 1,333333333 ; 1,120000000 ; 0,480000000 |
| le même sous gel ; plus grand certificat | 1,000000 ; 1,000000 | 1,000000000 ; 1,000000000 |
| P(e_B ≥ 1/α)/α à α = 3/8 | 1,3333 | 1,333333 |
| E[e_B1], [2,2] b = 2, 3, 4 ; [3,3] b = 4, 6 ; [6,6] b = 2, 3, 4 | 1,1657 ; 1,4311 ; 1,5404 ; 1,4440 ; 1,6793 ; 1,0455 ; 1,0982 ; 1,1609 | les mêmes, à quatre décimales |
| exemple à la main, E[max(Λ_1, Λ_2)] | 1,4000 | 7/5 |
| E[S] au-dessus de 1, cas à plusieurs membres | 2,2828 (son cas) | 1,4959 (mon cas, autre construction) |
| E[E′_c], c = 4 | 0,8056 | 0,9690 |
| réunion J9-D, plus grand P/α | 0,48 ; 0,46 ; 0,68 (α = 0,5 ; 0,25 ; 0,1) | 0,57 ; 0,34 ; 0,11 ; 0 (α = 0,5 ; 0,25 ; 0,1 ; 0,05) |

Mon cas pour la réunion : 12 tirages, trois membres à maximum exact (lois constantes ; liste finie de lois par
cellule ; loi fixe), deux engagements dont les bornes diffèrent d'un excès positif propre à chacun (deux solveurs),
3 plans × 3 cartes × 5 mondes. La réunion est dans R* et dans l'événement de Ville du monde sur chaque suite
(assertions). Les chiffres des deux dernières lignes ne sont pas comparables un à un (cas différents) ; ils disent la
même chose : sous α, et S au-dessus de 1.

## 8. Incidents de ma main

- La première commande de rejeu a dépassé dix minutes (partie E) et est passée en arrière-plan ; elle a fini seule,
  code de sortie 0. Aucun processus arrêté.
- Trois modules lancés depuis une **copie de travail** dans mon dossier du bloc-notes (`selection_pari`, `nul_v9` et
  leurs dépendances de `pole/`) : jamais depuis les dossiers de copie du dépôt. Dossier supprimé à la fin.
- Pièces de la section 15 non rouvertes ou seulement survolées : dites en section 1.
- Aucun `pytest`. Aucune écriture au dépôt hors de ce rapport et de son compagnon.

## Annexe A — programme d'énumération (écrit à part) et sorties

```python
"""Contre-lecture de la preuve, version 2, de l'idée 1.1 : énumérations exactes indépendantes.
Écrit sans recopier le script de l'auteur. Bibliothèque standard seule (fractions, itertools, math).
Parties :
 1. espérance de la valeur e d'un bloc sans la garde P4, carte sans_remise [1, 1] (attendu : 4/3), en fractions ;
 2. statistique S du rejet par famille : exemple à la main (attendu 7/5), puis cas à trois membres ;
 3. taille de la réunion J9 ou J9-D40 ou « par membre », bornes des deux engagements différentes ;
 4. carte moyenne_glissante de la grammaire sans garde : lissage négatif (accepté par valider_loi), puis balayage à
    lissage positif.
"""
import itertools
import math
from fractions import Fraction as F

PLANCHER = F(1, 10 ** 12)


def norme(p):
    p = [max(PLANCHER, F(x)) for x in p]
    s = sum(p)
    return [x / s for x in p]


def sans_remise(composition, hist):
    return norme([max(0, c - sum(1 for h in hist if h == k)) for k, c in enumerate(composition)])


def moyenne_glissante(k, w, lam, hist):
    """Même formule que selection_pari.proba (copie 94bfd92, l. 131 à 135), en fractions."""
    t = len(hist)
    rec = hist[max(0, t - w):t]
    den = len(rec) + k * lam
    return norme([(sum(1 for h in rec if h == i) + lam) / den for i in range(k)])


def valeur_e_bloc_constantes(lois, ys):
    """Famille des lois constantes (sommets δ_k). Projection d'information inverse = moyenne des lois du bloc
    (maximise Σ_y (Σ_s q_s(y)) log θ(y)). Certificat = max_k (1/b) Σ_s q_s(k)/φ(k)."""
    b, k = len(lois), len(lois[0])
    phi = [sum(q[i] for q in lois) / b for i in range(k)]
    cert = max(sum(q[i] / phi[i] for q in lois) / b for i in range(k))
    e = F(1)
    for q, y in zip(lois, ys):
        e *= q[y] / phi[y]
    return e / max(F(1), cert) ** b, cert


def esperance_bloc(carte, k, b, monde, avant=(), gel=False):
    """E_monde[e_B] exacte, bloc de b tirages après l'historique `avant` ; carte(hist) -> loi."""
    tot, cmax = F(0), F(0)
    for ys in itertools.product(range(k), repeat=b):
        lois = [carte(list(avant) + ([] if gel else list(ys[:i]))) for i in range(b)]
        e, c = valeur_e_bloc_constantes(lois, ys)
        p = F(1)
        for y in ys:
            p *= monde[y]
        tot += p * e
        cmax = max(cmax, c)
    return tot, cmax


def partie1():
    print("1. sans P4, sans_remise [1, 1], bloc de 2, famille des lois constantes")
    for p in (F(1, 2), F(3, 10), F(1, 10)):
        nu, c = esperance_bloc(lambda h: sans_remise([1, 1], h), 2, 2, [p, 1 - p])
        gel, _ = esperance_bloc(lambda h: sans_remise([1, 1], h), 2, 2, [p, 1 - p], gel=True)
        print(f"   p = {p} : E[e_B] sans garde = {float(nu):.9f} (16/3·p(1−p) = {float(F(16, 3) * p * (1 - p)):.9f}) ; "
              f"sous gel = {float(gel):.9f} ; plus grand certificat = {float(c):.9f}")
    # Ville : P(e_B ≥ 1/α) pour α = 3/8
    p = F(1, 2)
    proba = F(0)
    for ys in itertools.product(range(2), repeat=2):
        lois = [sans_remise([1, 1], list(ys[:i])) for i in range(2)]
        e, _ = valeur_e_bloc_constantes(lois, ys)
        if e >= F(8, 3) * (1 - F(1, 10 ** 9)):
            proba += p * p
    print(f"   P(e_B ≥ 8/3 au plancher près) = {proba} ; rapport à α = 3/8 : {float(proba / F(3, 8)):.6f}")
    for comp, b in (([2, 2], 2), ([2, 2], 3), ([2, 2], 4), ([3, 3], 4), ([3, 3], 6), ([6, 6], 2), ([6, 6], 3), ([6, 6], 4)):
        nu, _ = esperance_bloc(lambda h, c=comp: sans_remise(c, h), 2, b, [F(1, 2), F(1, 2)])
        print(f"   sans_remise {comp}, bloc de {b} : E[e_B] sans garde = {float(nu):.4f}")


def partie2():
    print("2. statistique S = min_m max_t q/exp(V_m)")
    q, tot = [F(9, 10), F(1, 10)], F(0)
    vals = []
    for ys in itertools.product(range(2), repeat=2):
        l1 = q[ys[0]] / F(1, 2)
        l2 = l1 * q[ys[1]] / F(1, 2)
        vals.append(max(l1, l2))
        tot += F(1, 4) * max(l1, l2)
    print(f"   exemple à la main : valeurs {sorted(float(v) for v in vals)} ; E[S] = {tot} = {float(tot)}")


# --- parties 2 (suite) et 3 : trois membres à maximum exact -----------------------------------------------------------
def cas_trois_membres(n, plan, carte, mondes, T8, T40, alphas, c_arret, jeu):
    """Membres : m0 = lois constantes (maximum exact Σ c log(c/t)) ; m1 = liste finie de lois dépendant de la cellule ;
    m2 = une loi fixe. Bornes de l'engagement à T8 : maximum exact + excès e8 ≥ 0 ; de l'engagement à T40 : + e40 ≥ 0
    (excès déterministes, fonctions du préfixe : deux solveurs différents)."""
    fam1 = [[[0.8, 0.2], [0.3, 0.7]], [[0.6, 0.4], [0.6, 0.4]], [[0.2, 0.8], [0.9, 0.1]]]
    fixe = [0.35, 0.65]

    def exces(pref, sel):
        h = (sum((i + 1) * (y + 1) for i, y in enumerate(pref)) * (7 if sel else 11)) % 13
        return 0.02 * h / 13.0

    res = {a: dict(j9=0.0, d40=0.0, pm=0.0, union=0.0, ville=0.0) for a in alphas}
    es = ee = emaxl = 0.0
    for ys in itertools.product(range(2), repeat=n):
        pw = 1.0
        for s, y in enumerate(ys):
            pw *= mondes[plan[s]][y]
        lq = lw = 0.0
        cnt = [0, 0]
        l1 = [0.0] * len(fam1)
        l2 = 0.0
        w8, w40, wm, lam = {}, {}, {}, {}
        for s, y in enumerate(ys):
            t = s + 1
            lq += math.log(carte[plan[s]][y])
            lw += math.log(mondes[plan[s]][y])
            cnt[y] += 1
            for i, f in enumerate(fam1):
                l1[i] += math.log(f[plan[s]][y])
            l2 += math.log(fixe[y])
            v = [sum(c * math.log(c / t) for c in cnt if c), max(l1), l2]
            lam[t] = lq - lw
            if t in T40:
                v40 = [x + exces(ys[:t], 0) for x in v]
                v8 = [x + exces(ys[:t], 1) for x in v] if t in T8 else None
                w40[t] = lq - max(v40)
                if v8:
                    w8[t] = lq - max(v8)
                wm[t] = [lq - (min(a, b) if v8 else a) for a, b in zip(v40, v8 or v40)]   # sur les bornes réunies V*
                wm40 = [lq - a for a in v40]
                w40.setdefault(("pm", t), wm40)
        m8 = max(w8.values())
        m40 = max(v for k, v in w40.items() if not isinstance(k, tuple))
        pm40 = min(max(w40[("pm", t)][m] for t in T40) for m in range(3))      # règle par membre, engagement jumeau
        s_star = min(max(wm[t][m] for t in T40) for m in range(3))             # S sur les bornes réunies
        mv = max(lam.values())
        es += pw * math.exp(s_star)
        emaxl += pw * math.exp(mv)
        # forme arrêtée membre par membre, seuil c_arret
        termes = []
        for m in range(3):
            tau = next((t for t in sorted(T40) if wm[t][m] >= math.log(c_arret)), n)
            termes.append(wm[tau][m])
        ee += pw * math.exp(min(termes))
        for a in alphas:
            th = math.log(1 / a)
            j9, d40, pm = m8 >= th, m40 >= th, pm40 >= th
            un = j9 or d40 or pm
            assert (not un) or s_star >= th - 1e-12, "réunion hors de R*"
            assert (not un) or mv >= th - 1e-12, "réunion hors de l'événement de Ville du monde"
            r = res[a]
            r["j9"] += pw * j9
            r["d40"] += pw * (j9 or d40)
            r["pm"] += pw * pm
            r["union"] += pw * un
            r["ville"] += pw * (mv >= th)
    return res, es, ee, emaxl


def partie3():
    print("2 (suite) et 3. trois membres {constantes ; liste finie par cellule ; loi fixe}, n = 12, T8 = {6, 12}, "
          "T40 = {2, 4, …, 12}, deux engagements à bornes différentes")
    n = 12
    plans = [[0, 1] * 6, [0, 0, 1, 1, 0, 1, 1, 0, 0, 1, 0, 1], [0] * 4 + [1] * 8]
    cartes = [[[0.9, 0.1], [0.2, 0.8]], [[0.75, 0.25], [0.45, 0.55]], [[0.55, 0.45], [0.05, 0.95]]]
    mondes = {"constante 0,5": [[0.5, 0.5]] * 2, "constante 0,3": [[0.3, 0.7]] * 2,
              "liste, loi 1": [[0.8, 0.2], [0.3, 0.7]], "liste, loi 3": [[0.2, 0.8], [0.9, 0.1]], "fixe": [[0.35, 0.65]] * 2}
    alphas = (0.5, 0.25, 0.1, 0.05)
    pire = {a: dict(j9=0.0, d40=0.0, pm=0.0, union=0.0, ville=0.0) for a in alphas}
    pes = pee = pml = 0.0
    for plan in plans:
        for carte in cartes:
            for nom, monde in mondes.items():
                res, es, ee, eml = cas_trois_membres(n, plan, carte, monde, {6, 12}, set(range(2, 13, 2)), alphas, 4.0, None)
                for a in alphas:
                    for k in pire[a]:
                        pire[a][k] = max(pire[a][k], res[a][k] / a)
                pes, pee, pml = max(pes, es), max(pee, ee), max(pml, eml)
    for k, nom in (("j9", "J9"), ("d40", "J9-D40"), ("pm", "par membre"), ("union", "réunion J9-D"), ("ville", "Ville du monde")):
        print("   plus grand P/α, " + nom.ljust(15) + " : " + " ; ".join(f"α={a} : {pire[a][k]:.4f}" for a in alphas))
    print(f"   plus grande E[S] = {pes:.4f} ; plus grande E[E'_c] (c = 4) = {pee:.4f} ; plus grande E[max_t Λ_t] = {pml:.4f}")


# --- partie 4 : moyenne_glissante sans garde ---------------------------------------------------------------------------
def ville_multi_blocs(carte, k, b, n, monde, gel=False):
    """sup_x x·P(∃ fin de bloc : W ≥ x), W = produit des valeurs e des blocs écoulés ; énumération des k^n suites."""
    evts = []
    for ys in itertools.product(range(k), repeat=n):
        p, w, m = 1.0, 1.0, 0.0
        for d in range(0, n, b):
            lois = [carte(list(ys[:d]) + ([] if gel else list(ys[d:d + i]))) for i in range(b)]
            e, _ = valeur_e_bloc_constantes(lois, ys[d:d + b])
            w *= float(e)
            m = max(m, w)
        for y in ys:
            p *= monde[y]
        evts.append((m, p))
    evts.sort(reverse=True)
    cum, best, bx = 0.0, 0.0, None
    i = 0
    while i < len(evts):
        x = evts[i][0]
        while i < len(evts) and evts[i][0] >= x * (1 - 1e-12):
            cum += evts[i][1]
            i += 1
        if x > 1 and cum * x > best:
            best, bx = cum * x, x
    return best, bx


def partie4():
    print("4. moyenne_glissante sans garde, famille des lois constantes")
    print("   (a) lissage négatif : {type: moyenne_glissante, nombre_issues: 2, fenetre: 1, lissage: -0.6}")
    carte = lambda h: moyenne_glissante(2, 1, F(-6, 10), h)
    print("       lois : historique vide", [float(x) for x in carte([])], "; après 0", [float(x) for x in carte([0])],
          "; après 1", [float(x) for x in carte([1])])
    for b in (2, 3, 4, 5):
        for avant in ((), (0,)):
            nu, c = esperance_bloc(carte, 2, b, [F(1, 2), F(1, 2)], avant=avant)
            gel, _ = esperance_bloc(carte, 2, b, [F(1, 2), F(1, 2)], avant=avant, gel=True)
            print(f"       bloc de {b}, historique avant le bloc {list(avant)} : E[e_B] sans garde = {float(nu):.6f} ; "
                  f"sous gel = {float(gel):.6f} ; plus grand certificat = {float(c):.6f}")
    for b, n in ((2, 2), (2, 8), (2, 12), (4, 12)):
        r, x = ville_multi_blocs(carte, 2, b, n, [0.5, 0.5])
        rg, _ = ville_multi_blocs(carte, 2, b, n, [0.5, 0.5], gel=True)
        pa = sum(1 for _ in [0])
        print(f"       blocs de {b}, n = {n} : sup_α P(∃ fin de bloc : W ≥ 1/α)/α sans garde = {r:.4f} (α = {1 / x:.4f}) ; sous gel = {rg:.4f}")
    # probabilité de promotion à α = 0,05, blocs de 2, n = 12
    for b, n in ((2, 12), (2, 16)):
        pr = 0.0
        for ys in itertools.product(range(2), repeat=n):
            w, m = 1.0, 0.0
            for d in range(0, n, b):
                lois = [carte(list(ys[:d + i])) for i in range(b)]
                e, _ = valeur_e_bloc_constantes(lois, ys[d:d + b])
                w *= float(e)
                m = max(m, w)
            if m >= 20:
                pr += 0.5 ** n
        print(f"       blocs de {b}, n = {n}, monde uniforme : P(∃ fin de bloc : W ≥ 20) sans garde = {pr:.6f} (α = 0,05)")
    print("   (b) lissage positif : balayage du plus grand E_θ[e_B] sans garde (θ constante, grille), K = 2 et 3")
    pire, ou = F(0), None
    for k in (2, 3):
        grille = ([[F(i, 10), 1 - F(i, 10)] for i in range(0, 11)] if k == 2 else
                  [[F(i, 6), F(j, 6), 1 - F(i + j, 6)] for i in range(7) for j in range(7 - i)])
        for w in (1, 2, 3, 5):
            for lam in (F(1, 1000), F(1, 10), F(1, 2), F(1), F(5)):
                for b in ((2, 3, 4, 5) if k == 2 else (2, 3, 4)):
                    for avant in ((), (0,), (0, 1), (0, 0, 1), (1, 0, 0, 0, 1)):
                        if k == 3 and len(avant) > 2:
                            continue
                        for monde in grille:
                            nu, _ = esperance_bloc(lambda h: moyenne_glissante(k, w, lam, h), k, b, monde, avant=avant)
                            if nu > pire:
                                pire, ou = nu, (k, w, float(lam), b, avant, [float(x) for x in monde])
    print(f"       plus grand E_θ[e_B] = {float(pire):.6f} en (K, fenêtre, lissage, bloc, historique avant, θ) = {ou}")


if __name__ == "__main__":
    import sys
    for p in (sys.argv[1:] or ["1", "2", "3", "4"]):
        {"1": partie1, "2": partie2, "3": partie3, "4": partie4}[p]()
```

Sortie (`.venv/bin/python -I -B enum_contre_lecture_preuve_v2.py`) :

```
1. sans P4, sans_remise [1, 1], bloc de 2, famille des lois constantes
   p = 1/2 : E[e_B] sans garde = 1.333333333 (16/3·p(1−p) = 1.333333333) ; sous gel = 1.000000000 ; plus grand certificat = 1.000000000
   p = 3/10 : E[e_B] sans garde = 1.120000000 (16/3·p(1−p) = 1.120000000) ; sous gel = 1.000000000 ; plus grand certificat = 1.000000000
   p = 1/10 : E[e_B] sans garde = 0.480000000 (16/3·p(1−p) = 0.480000000) ; sous gel = 1.000000000 ; plus grand certificat = 1.000000000
   P(e_B ≥ 8/3 au plancher près) = 1/2 ; rapport à α = 3/8 : 1.333333
   sans_remise [2, 2], bloc de 2 : E[e_B] sans garde = 1.1657
   sans_remise [2, 2], bloc de 3 : E[e_B] sans garde = 1.4311
   sans_remise [2, 2], bloc de 4 : E[e_B] sans garde = 1.5404
   sans_remise [3, 3], bloc de 4 : E[e_B] sans garde = 1.4440
   sans_remise [3, 3], bloc de 6 : E[e_B] sans garde = 1.6793
   sans_remise [6, 6], bloc de 2 : E[e_B] sans garde = 1.0455
   sans_remise [6, 6], bloc de 3 : E[e_B] sans garde = 1.0982
   sans_remise [6, 6], bloc de 4 : E[e_B] sans garde = 1.1609
2. statistique S = min_m max_t q/exp(V_m)
   exemple à la main : valeurs [0.2, 0.36, 1.8, 3.24] ; E[S] = 7/5 = 1.4
2 (suite) et 3. trois membres {constantes ; liste finie par cellule ; loi fixe}, n = 12, T8 = {6, 12}, T40 = {2, 4, …, 12}, deux engagements à bornes différentes
   plus grand P/α, J9              : α=0.5 : 0.4891 ; α=0.25 : 0.1542 ; α=0.1 : 0.0000 ; α=0.05 : 0.0000
   plus grand P/α, J9-D40          : α=0.5 : 0.5312 ; α=0.25 : 0.3403 ; α=0.1 : 0.0000 ; α=0.05 : 0.0000
   plus grand P/α, par membre      : α=0.5 : 0.5683 ; α=0.25 : 0.3403 ; α=0.1 : 0.1090 ; α=0.05 : 0.0000
   plus grand P/α, réunion J9-D    : α=0.5 : 0.5683 ; α=0.25 : 0.3403 ; α=0.1 : 0.1090 ; α=0.05 : 0.0000
   plus grand P/α, Ville du monde  : α=0.5 : 0.8347 ; α=0.25 : 0.8884 ; α=0.1 : 0.8179 ; α=0.05 : 0.9045
   plus grande E[S] = 1.4959 ; plus grande E[E'_c] (c = 4) = 0.9690 ; plus grande E[max_t Λ_t] = 8.2383
4. moyenne_glissante sans garde, famille des lois constantes
   (a) lissage négatif : {type: moyenne_glissante, nombre_issues: 2, fenetre: 1, lissage: -0.6}
       lois : historique vide [0.5, 0.5] ; après 0 [3.333333333332222e-13, 0.9999999999996667] ; après 1 [0.9999999999996667, 3.333333333332222e-13]
       bloc de 2, historique avant le bloc [] : E[e_B] sans garde = 1.333333 ; sous gel = 1.000000 ; plus grand certificat = 1.000000
       bloc de 2, historique avant le bloc [0] : E[e_B] sans garde = 1.500000 ; sous gel = 1.000000 ; plus grand certificat = 1.000000
       bloc de 3, historique avant le bloc [] : E[e_B] sans garde = 1.000000 ; sous gel = 1.000000 ; plus grand certificat = 1.000000
       bloc de 3, historique avant le bloc [0] : E[e_B] sans garde = 1.093750 ; sous gel = 1.000000 ; plus grand certificat = 1.000000
       bloc de 4, historique avant le bloc [] : E[e_B] sans garde = 1.137778 ; sous gel = 1.000000 ; plus grand certificat = 1.000000
       bloc de 4, historique avant le bloc [0] : E[e_B] sans garde = 1.125000 ; sous gel = 1.000000 ; plus grand certificat = 1.000000
       bloc de 5, historique avant le bloc [] : E[e_B] sans garde = 1.000000 ; sous gel = 1.000000 ; plus grand certificat = 1.000000
       bloc de 5, historique avant le bloc [0] : E[e_B] sans garde = 0.966725 ; sous gel = 1.000000 ; plus grand certificat = 1.000000
       blocs de 2, n = 2 : sup_α P(∃ fin de bloc : W ≥ 1/α)/α sans garde = 1.3333 (α = 0.3750) ; sous gel = 0.0000
       blocs de 2, n = 8 : sup_α P(∃ fin de bloc : W ≥ 1/α)/α sans garde = 2.6667 (α = 0.0234) ; sous gel = 0.0000
       blocs de 2, n = 12 : sup_α P(∃ fin de bloc : W ≥ 1/α)/α sans garde = 5.3333 (α = 0.0059) ; sous gel = 0.0000
       blocs de 4, n = 12 : sup_α P(∃ fin de bloc : W ≥ 1/α)/α sans garde = 1.2800 (α = 0.0069) ; sous gel = 0.0000
       blocs de 2, n = 12, monde uniforme : P(∃ fin de bloc : W ≥ 20) sans garde = 0.101562 (α = 0,05)
       blocs de 2, n = 16, monde uniforme : P(∃ fin de bloc : W ≥ 20) sans garde = 0.117188 (α = 0,05)
   (b) lissage positif : balayage du plus grand E_θ[e_B] sans garde (θ constante, grille), K = 2 et 3
       plus grand E_θ[e_B] = 1.000000 en (K, fenêtre, lissage, bloc, historique avant, θ) = (2, 1, 0.001, 2, (0,), [1.0, 0.0])
```

## Annexe B — essais sur la copie de travail du code (lissage ; issues postérieures)

```python
"""Essais sur une copie de travail du code (copie 94bfd92 et nul_v9 a41b7b5), lancés hors du dossier de copie."""
import sys, random, itertools
sys.path.insert(0, sys.argv[1])
import numpy as np
from pole import selection_pari as sp
from pole import nul_v9

# (i) valider_loi et lissage
for lam in (-0.6, -0.4, 0.0, float("nan")):
    loi = {"type": "moyenne_glissante", "nombre_issues": 2, "fenetre": 1, "lissage": lam}
    try:
        sp.valider_loi(loi, 2, 2)
        ok = "acceptée par valider_loi"
    except Exception as e:
        ok = f"refusée : {e}"
    sorties = []
    for h in ([], [0], [1]):
        try:
            sorties.append([round(x, 6) for x in sp.proba(loi, {"z": [0.0, 0.0], "g": 0}, h, len(h))])
        except Exception as e:
            sorties.append(type(e).__name__)
    print(f"(i) lissage {lam} : {ok} ; proba historique [], [0], [1] : {sorties} ; types : {sorted(sp.types_de_la_loi(loi))}")

# (ii) V_m(t) du membre par morceaux lit-il des issues postérieures à t ?
rng = random.Random(20261115)
K, d, n = 3, 2, 50
pire, nb_diff, nb = 0.0, 0, 0
for essai in range(12):
    inst = sp.tirer_instances(rng, n, d, 2)
    lois = [sp.loi_softmax_aleatoire(rng, K, d) for _ in range(2)]
    membres = nul_v9.membres_morceaux(lois, d)
    monde = {"type": "si_sinon", "condition": {"indice": 0, "seuil": 0.2}, "si": lois[0], "sinon": lois[1]}
    y = [sp.tirer_categorie(rng, sp.proba(monde, inst[t], [], t)) for t in range(n)]
    ref = nul_v9.detail_morceaux_groupe(membres, sp.Cache(y, inst), y, [25, 50])
    for variante in range(4):
        y2 = y[:25] + [rng.randrange(K) for _ in range(25)]
        alt = nul_v9.detail_morceaux_groupe(membres, sp.Cache(y2, inst), y2, [25, 50])
        for nom in ref:
            dif = abs(ref[nom][25]["valeur"] - alt[nom][25]["valeur"])
            nb += 1
            nb_diff += dif > 0
            pire = max(pire, dif)
    seul = nul_v9.detail_morceaux_groupe(membres, sp.Cache(y, inst), y[:25] + y[25:], [25, 50])
print(f"(ii) valeur à t = 25 d'un membre par morceaux, issues 26 à 50 changées : {nb_diff} valeurs différentes sur {nb} ; "
      f"plus grand écart absolu {pire:.3e} nat (tolérance du code 1e-3)")
# même question, instants seuls : [25] contre [25, 50], mêmes issues
pire2 = 0.0
for essai in range(6):
    inst = sp.tirer_instances(rng, n, d, 2)
    lois = [sp.loi_softmax_aleatoire(rng, K, d) for _ in range(2)]
    membres = nul_v9.membres_morceaux(lois, d)
    y = [rng.randrange(K) for _ in range(n)]
    a = nul_v9.detail_morceaux_groupe(membres, sp.Cache(y, inst), y, [25, 50])
    b = nul_v9.detail_morceaux_groupe(membres, sp.Cache(y, inst), y, [5, 10, 15, 20, 25, 50])
    for nom in a:
        pire2 = max(pire2, abs(a[nom][25]["valeur"] - b[nom][25]["valeur"]))
print(f"(iii) valeur à t = 25, instants [25, 50] contre [5, …, 25, 50], mêmes issues : plus grand écart {pire2:.3e} nat")
```

```
(i) lissage -0.6 : acceptée par valider_loi ; proba historique [], [0], [1] : [[0.5, 0.5], [0.0, 1.0], [1.0, 0.0]] ; types : ['moyenne_glissante']
(i) lissage -0.4 : acceptée par valider_loi ; proba historique [], [0], [1] : [[0.5, 0.5], [1.0, 0.0], [0.0, 1.0]] ; types : ['moyenne_glissante']
(i) lissage 0.0 : acceptée par valider_loi ; proba historique [], [0], [1] : ['ZeroDivisionError', [1.0, 0.0], [0.0, 1.0]] ; types : ['moyenne_glissante']
(i) lissage nan : acceptée par valider_loi ; proba historique [], [0], [1] : [[0.5, 0.5], [0.5, 0.5], [0.5, 0.5]] ; types : ['moyenne_glissante']
(ii) valeur à t = 25 d'un membre par morceaux, issues 26 à 50 changées : 23 valeurs différentes sur 144 ; plus grand écart absolu 4.303e-10 nat (tolérance du code 1e-3)
(iii) valeur à t = 25, instants [25, 50] contre [5, …, 25, 50], mêmes issues : plus grand écart 4.539e-07 nat
```

## Annexe C — cartes composées à lissage positif ; miniature du juge complet

```python
"""Complément de la partie 4 : cartes composées de la grammaire autour d'une moyenne_glissante à lissage POSITIF, sans garde,
famille des lois constantes ; plus grand E_θ[e_B] (flottants). Formules des types recopiées à la main de la lecture de proba."""
import itertools, math, random
PL = 1e-12
def norme(p):
    p = [max(PL, x) for x in p]; s = sum(p); return [x / s for x in p]
def mg(k, w, lam, h):
    t = len(h); rec = h[max(0, t - w):t]
    return norme([(rec.count(i) + lam) / (len(rec) + k * lam) for i in range(k)])
def carte(spec, h, s):
    genre = spec[0]
    if genre == "mg": return mg(spec[1], spec[2], spec[3], h)
    if genre == "fixe": return norme(spec[1])
    if genre == "melange":
        a, b = carte(spec[2], h, s), carte(spec[3], h, s); return norme([spec[1] * x + (1 - spec[1]) * y for x, y in zip(a, b)])
    if genre == "enveloppe":
        a, b = carte(spec[1], h, s), carte(spec[2], h, s); return norme([max(x, y) for x, y in zip(a, b)])
    if genre == "transformee":
        p = carte(spec[1], h, s)
        if spec[2] is not None: p = norme([max(x, PL) ** spec[2] for x in p])
        if spec[3] is not None: p = norme([x * math.exp(b) for x, b in zip(p, spec[3])])
        return norme(p)
    if genre == "alterne":  # si_sinon sur un trait du plan : instances paires / impaires
        return carte(spec[1] if s % 2 == 0 else spec[2], h, s)
def e_bloc(lois, ys):
    b, k = len(lois), len(lois[0]); phi = [sum(q[i] for q in lois) / b for i in range(k)]
    c = max(sum(q[i] / phi[i] for q in lois) / b for i in range(k)); e = 1.0
    for q, y in zip(lois, ys): e *= q[y] / phi[y]
    return e / max(1.0, c) ** b
def esp(spec, k, b, monde, avant):
    tot = 0.0
    for ys in itertools.product(range(k), repeat=b):
        lois = [carte(spec, list(avant) + list(ys[:i]), len(avant) + i) for i in range(b)]
        p = 1.0
        for y in ys: p *= monde[y]
        if p: tot += p * e_bloc(lois, ys)
    return tot
rng = random.Random(7)
pire, ou, nb = 0.0, None, 0
for essai in range(6000):
    k = rng.choice((2, 2, 3))
    def une_mg(): return ("mg", k, rng.choice((1, 1, 2, 3, 5)), rng.choice((0.001, 0.05, 0.3, 0.5, 1.0, 4.0)))
    def une_fixe(): return ("fixe", [rng.random() + 0.02 for _ in range(k)])
    forme = rng.randrange(6)
    if forme == 0: spec = ("transformee", une_mg(), rng.choice((0.2, 0.5, 2.0, 6.0)), [rng.gauss(0, 1.5) for _ in range(k)])
    elif forme == 1: spec = ("melange", rng.random(), une_mg(), rng.choice((une_fixe(), une_mg())))
    elif forme == 2: spec = ("enveloppe", une_mg(), rng.choice((une_fixe(), une_mg())))
    elif forme == 3: spec = ("alterne", une_mg(), rng.choice((une_fixe(), une_mg())))
    elif forme == 4: spec = ("transformee", ("enveloppe", une_mg(), une_fixe()), rng.choice((0.3, 3.0)), None)
    else: spec = ("alterne", ("transformee", une_mg(), rng.choice((0.3, 3.0)), [rng.gauss(0, 1) for _ in range(k)]), ("melange", rng.random(), une_mg(), une_fixe()))
    b = rng.choice((2, 3, 4)) if k == 2 else rng.choice((2, 3))
    avant = [rng.randrange(k) for _ in range(rng.choice((0, 1, 2, 5)))]
    for _ in range(4):
        monde = [rng.random() ** 2 for _ in range(k)]; s = sum(monde); monde = [x / s for x in monde]
        if rng.random() < 0.3: monde = [1.0 if i == rng.randrange(k) else 0.0 for i in range(k)]; monde = [x / max(sum(monde), 1e-300) for x in monde] if sum(monde) else [1.0 / k] * k
        v = esp(spec, k, b, monde, avant); nb += 1
        if v > pire: pire, ou = v, (spec, b, avant, [round(x, 4) for x in monde])
print(f"cartes composées autour d'une moyenne glissante à lissage positif : {nb} cas ; plus grand E_θ[e_B] sans garde = {pire:.12f}")
print("   atteint en :", ou)
```

```
cartes composées autour d'une moyenne glissante à lissage positif : 24000 cas ; plus grand E_θ[e_B] sans garde = 1.000000000000
   atteint en : (('transformee', ('enveloppe', ('mg', 3, 3, 0.3), ('fixe', [0.7406772713715515, 0.5141907536198433, 0.3041765785526914])), 0.3, None), 2, [2, 2, 2, 0, 2], [0.0, 0.0, 1.0])
```

```python
"""Miniature du « juge complet » de J9-P : W = min(W^reste, W^F), F = famille linéaire {w1·L1 + w2·L2 + ρ0·δ0 + ρ1·δ1},
W^reste = bibliothèque ordinaire du juge v0 (uniforme, marginale ajustée, moyennes glissantes 5/10/20/50, lissage 0,5),
monde = ½·L1 + ½·L2 (dans F, hors de W^reste), carte de la grammaire = melange([monde, moyenne_glissante à lissage
négatif], [1 − λ, λ]). Énumération exacte des 2^n suites ; sup_α P(∃ fin de bloc : W ≥ 1/α)/α, sans garde et sous gel."""
import itertools, math
PL = 1e-12
def norme(p):
    p = [max(PL, x) for x in p]; s = sum(p); return [x / s for x in p]
def mg(k, w, lam, h):
    t = len(h); rec = h[max(0, t - w):t]
    return norme([(rec.count(i) + lam) / (len(rec) + k * lam) for i in range(k)])
L1 = {0: [0.95, 0.05], 1: [0.05, 0.95]}
L2 = {0: [0.5, 0.5], 1: [0.5, 0.5]}
def monde(x): return [0.5 * a + 0.5 * b for a, b in zip(L1[x], L2[x])]
def comp(x): return [L1[x], L2[x], [1.0, 0.0], [0.0, 1.0]]
def carte(lam_mix, w, lam, x, h):
    a, m = mg(2, w, lam, h), monde(x)
    return norme([(1 - lam_mix) * u + lam_mix * v for u, v in zip(m, a)])
def projection(lois, xs, pas=400):
    wts = [0.25] * 4
    for _ in range(pas):
        acc = [0.0] * 4
        for q, x in zip(lois, xs):
            C = comp(x)
            for y in range(2):
                p = sum(wts[i] * C[i][y] for i in range(4))
                for i in range(4):
                    acc[i] += q[y] * wts[i] * C[i][y] / p
        wts = [a / len(lois) for a in acc]
    return wts
def e_bloc(lois, xs, ys, cache):
    cle = (tuple(tuple(q) for q in lois), tuple(xs))
    if cle not in cache:
        wts = projection(lois, xs)
        P = [[sum(wts[i] * comp(x)[i][y] for i in range(4)) for y in range(2)] for x in xs]
        c = max(sum(sum(comp(x)[i][y] * q[y] / p[y] for y in range(2)) for q, x, p in zip(lois, xs, P)) / len(lois) for i in range(4))
        cache[cle] = (P, c)
    P, c = cache[cle]
    e = 1.0
    for q, p, y in zip(lois, P, ys): e *= q[y] / p[y]
    return e / max(1.0, c) ** len(lois)
def reste_denominateur(ys):
    """max des membres ordinaires à chaque t (log), formules de selection_pari l. 303 à 331."""
    n = len(ys); out = []
    cnt = [0, 0]; marg = []
    for t, y in enumerate(ys, 1):
        cnt[y] += 1; marg.append(sum(c * math.log(c / t) for c in cnt if c))
    best = None
    for w in (5, 10, 20, 50):
        compte, file, cum, tr = [0, 0], [], 0.0, []
        for y in ys:
            cum += math.log((compte[y] + 0.5) / (len(file) + 1.0)); tr.append(cum); file.append(y); compte[y] += 1
            if len(file) > w: compte[file.pop(0)] -= 1
        best = tr if best is None else [max(a, b) for a, b in zip(best, tr)]
    return [max(-(t + 1) * math.log(2), marg[t], best[t]) for t in range(n)]
def sup_ratio(evts):
    evts.sort(reverse=True); cum, best, bx, i = 0.0, 0.0, None, 0
    while i < len(evts):
        x = evts[i][0]
        while i < len(evts) and evts[i][0] >= x * (1 - 1e-12): cum += evts[i][1]; i += 1
        if x > 1 and cum * x > best: best, bx = cum * x, x
    return best, bx
def cas(n, b, xs, lam_mix, w, lam):
    cache = {}
    res = {}
    for forme in ("nu", "gel"):
        e_min, e_proj, e_reste, e_monde, esp1 = [], [], [], [], 0.0
        for ys in itertools.product(range(2), repeat=n):
            pw = 1.0
            for x, y in zip(xs, ys): pw *= monde(x)[y]
            den = reste_denominateur(ys)
            lq = lw = 0.0; wf = 1.0; m_min = m_proj = m_reste = m_monde = 0.0
            for d in range(0, n, b):
                lois = [carte(lam_mix, w, lam, xs[d + i], list(ys[:d]) + ([] if forme == "gel" else list(ys[d:d + i]))) for i in range(b)]
                e = e_bloc(lois, xs[d:d + b], ys[d:d + b], cache)
                if d == 0: esp1 += pw * e
                wf *= e
                for i in range(b):
                    lq += math.log(lois[i][ys[d + i]]); lw += math.log(monde(xs[d + i])[ys[d + i]])
                wr = math.exp(lq - den[d + b - 1])
                m_min = max(m_min, min(wr, wf)); m_proj = max(m_proj, wf); m_reste = max(m_reste, wr); m_monde = max(m_monde, math.exp(lq - lw))
            e_min.append((m_min, pw)); e_proj.append((m_proj, pw)); e_reste.append((m_reste, pw)); e_monde.append((m_monde, pw))
        res[forme] = (esp1, sup_ratio(e_proj), sup_ratio(e_min), sup_ratio(e_reste), sup_ratio(e_monde))
    return res
if __name__ == "__main__":
    n = 12
    plans = {"alterné": [0, 1] * 6, "paires": [0, 0, 1, 1] * 3}
    print("juge miniature, n = 12, K = 2 ; par cas : E[e_B1] ; sup_α P/α du terme projeté ; du minimum (juge complet) ; de W^reste ; du rapport au monde")
    for nom, xs in plans.items():
        for b in (2, 4):
            for (lm, w, lam) in ((1.0, 1, -0.6), (0.5, 1, -0.6), (0.3, 1, -0.6), (0.5, 2, -1.5), (0.5, 1, 0.5), (0.5, 1, 0.001)):
                r = cas(n, b, xs, lm, w, lam)
                for forme in ("nu", "gel"):
                    e1, pr, mi, re, mo = r[forme]
                    f = lambda t: f"{t[0]:.4f}" + (f" (α={1 / t[1]:.4f})" if t[1] else "")
                    print(f"  plan {nom}, blocs de {b}, part {lm} de moyenne_glissante(fenêtre {w}, lissage {lam}), {forme:3s} : "
                          f"E[e_B1] {e1:.4f} ; projeté {f(pr)} ; minimum {f(mi)} ; reste {f(re)} ; monde {f(mo)}"
                          + ("   <-- minimum au-dessus de 1" if mi[0] > 1 + 1e-9 else ""))
```

Sortie (lignes « nu » à lissage négatif, plan « paires » ; les 48 lignes ont été lues) :

```
juge miniature, n = 12, K = 2 ; par cas : E[e_B1] ; sup_α P/α du terme projeté ; du minimum (juge complet) ; de W^reste ; du rapport au monde
  plan paires, blocs de 2, part 1.0 de moyenne_glissante(fenêtre 1, lissage -0.6), nu  : E[e_B1] 1.0633 ; projeté 1.4873 (α=0.0059) ; minimum 0.7975 (α=0.5000) ; reste 0.7975 (α=0.5000) ; monde 1.0000 (α=0.3988)
  plan paires, blocs de 2, part 0.5 de moyenne_glissante(fenêtre 1, lissage -0.6), nu  : E[e_B1] 1.2053 ; projeté 1.1400 (α=0.3000) ; minimum 0.7535 (α=0.8639) ; reste 0.8894 (α=0.9003) ; monde 0.8009 (α=0.5965)
  plan paires, blocs de 2, part 0.3 de moyenne_glissante(fenêtre 1, lissage -0.6), nu  : E[e_B1] 1.1335 ; projeté 1.0630 (α=0.7516) ; minimum 0.8045 (α=0.7948) ; reste 1.5380 (α=0.2144) ; monde 0.7300 (α=0.7897)
  plan paires, blocs de 2, part 0.5 de moyenne_glissante(fenêtre 2, lissage -1.5), nu  : E[e_B1] 1.1043 ; projeté 1.0128 (α=0.7885) ; minimum 0.7549 (α=0.8798) ; reste 1.6452 (α=0.1011) ; monde 0.7545 (α=0.7435)
  plan paires, blocs de 4, part 1.0 de moyenne_glissante(fenêtre 1, lissage -0.6), nu  : E[e_B1] 0.7858 ; projeté 0.7236 (α=0.1099) ; minimum 0.6360 (α=0.1250) ; reste 0.6360 (α=0.1250) ; monde 1.0000 (α=0.0795)
  plan paires, blocs de 4, part 0.5 de moyenne_glissante(fenêtre 1, lissage -0.6), nu  : E[e_B1] 1.3844 ; projeté 0.9868 (α=0.7030) ; minimum 0.4915 (α=0.3709) ; reste 0.7099 (α=0.9003) ; monde 0.5329 (α=0.2163)
  plan paires, blocs de 4, part 0.3 de moyenne_glissante(fenêtre 1, lissage -0.6), nu  : E[e_B1] 1.2799 ; projeté 1.0501 (α=0.7516) ; minimum 0.6921 (α=0.8529) ; reste 1.4138 (α=0.2116) ; monde 0.5709 (α=0.9246)
  plan paires, blocs de 4, part 0.5 de moyenne_glissante(fenêtre 2, lissage -1.5), nu  : E[e_B1] 1.2322 ; projeté 0.9537 (α=0.6674) ; minimum 0.6313 (α=0.9251) ; reste 1.5625 (α=0.1011) ; monde 0.4976 (α=0.5860)
```
