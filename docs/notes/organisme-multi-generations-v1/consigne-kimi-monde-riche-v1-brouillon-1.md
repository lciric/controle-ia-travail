# Consigne de Kimi — écriture d'un monde riche caché — brouillon 1 (non envoyée)

**Statut** : brouillon de conception, écrit le 12 novembre 2026 par un concepteur neuf (Claude Opus 5.5, `claude-opus-5-5`),
sous-agent de la session mère `session_01XJ6Mgn4MZR4nxqK44C8Ea3`. **Rien n'est envoyé** : l'envoi demande une ligne de GO
neuve (R-2444) et le compte de Kimi rechargé (suspendu faute de crédit le 11 novembre, R-2389). Pièce de la conception
`conception-monde-riche-doublons-v1.md`, section 2. Le texte servi à Kimi est **la partie entre les deux filets** ci-dessous,
et elle seule ; il sera gelé (empreinte) avant l'appel, avec les exigences `sorties-v1/exigences-monde-riche-v1.json`.

**Ce que l'instance reçoit** : ce texte, rien d'autre (un appel sans historique, par le relais Kimi). **Ce qu'elle ne reçoit
jamais** : aucun score, aucune proposition, aucune carte, aucun verdict, aucun relevé d'une course, aucun monde antérieur
(ni S-V1, ni un monde synthétique de la conception), aucun nom de proposeur, aucun code du juge, aucune mention du programme
de contrôle. Les ordres de grandeur de la section « Tailles » sont des estimations tirées de mondes synthétiques écrits par
programme (`outils-v1/normes_coefficients_v1.py`), jamais d'un résultat de course.

---8<--- début du texte servi ---8<---

Tu écris un **monde caché** pour une expérience de découverte automatique de lois. D'autres programmes chercheront plus tard
les régularités de ce monde à partir d'exemples tirés de lui. Tu ne verras jamais ce qu'ils proposent ni comment ils sont
jugés, et ton monde ne leur sera jamais montré.

**Le monde.** Chaque instance porte huit traits réels z0 à z7, tirés indépendamment d'une loi normale centrée réduite, et
une sous-population g ∈ {0, 1, 2}, tirée uniformément. Chaque instance a une issue parmi trois (0, 1, 2). Le monde donne la
probabilité de chaque issue sachant les traits et la sous-population : trois scores (un par issue), puis une fonction
softmax. Les scores sont la somme d'un biais (trois nombres) et des **effets** que tu choisis.

**Les six sortes d'effets** (chacune ajoute un vecteur de trois nombres aux scores, dans certaines instances seulement) :
1. `principal` : ajoute `pente × z_trait` (pente : trois nombres) ;
2. `seuil` : ajoute `decalage` quand `z_trait > seuil` ;
3. `interaction_seuil` : ajoute `pente × z_trait` seulement quand `z_trait_condition > seuil` (l'effet d'un trait dépend
   d'un autre trait) ;
4. `interaction_sous_population` : ajoute `pente × z_trait` seulement dans la sous-population `sous_population` ;
5. `sous_population` : ajoute `decalage` dans la sous-population `sous_population` ;
6. `latent` : un trait caché u ∈ {+1, −1}, jamais observé (u = +1 avec la probabilité `poids_melange`), ajoute
   `u × decalage` (au plus un effet de ce type).

**Ce que tu dois rendre** : un seul objet JSON, dans un seul bloc de code `json`, sans aucun autre texte dans le bloc, de
cette forme exacte :

```json
{
 "version": "monde-riche-spec-v1",
 "nombre_issues": 3,
 "dimension": 8,
 "sous_populations": 3,
 "biais": [b0, b1, b2],
 "effets": [
  {"id": "E1", "classe": "forte", "type": "principal", "trait": 0, "pente": [p0, p1, p2]},
  {"id": "E2", "classe": "faible", "type": "seuil", "trait": 0, "seuil": s, "decalage": [d0, d1, d2]},
  {"id": "E3", "classe": "moyenne", "type": "interaction_seuil", "trait_condition": 0, "seuil": s, "trait": 0, "pente": [p0, p1, p2]},
  {"id": "E4", "classe": "moyenne", "type": "interaction_sous_population", "sous_population": 0, "trait": 0, "pente": [p0, p1, p2]},
  {"id": "E5", "classe": "faible", "type": "sous_population", "sous_population": 0, "decalage": [d0, d1, d2]},
  {"id": "E6", "classe": "moyenne", "type": "latent", "poids_melange": 0.5, "decalage": [d0, d1, d2]}
 ],
 "distracteurs": [t, t]
}
```

(Les valeurs ci-dessus sont des emplacements ; les traits, seuils et sous-populations montrés sont des exemples de forme,
pas des choix.) Pour chaque effet, seules les clés de son type sont permises ; **aucun texte libre, aucun commentaire,
aucune autre clé**, nulle part.

**Règles** :
- entre 7 et 9 effets, identifiants `E1`, `E2`, … ; exactement **2 effets de classe « forte »**, **2 ou 3 « moyenne »**,
  **2 à 4 « faible »** ;
- **au moins 2 interactions** (`interaction_seuil` ou `interaction_sous_population`) ; au plus **2 conditions de seuil
  distinctes** (couples trait et seuil) dans tout le monde ; au plus un effet `latent` ;
- **au moins 2 traits distracteurs** : des traits qu'aucun effet n'utilise (ni comme trait, ni comme condition), listés
  exactement dans `distracteurs` ;
- tous les nombres bornés : biais, pentes et décalages dans [−4 ; 4] ; seuils dans [−1,5 ; 1,5] ; `poids_melange` dans
  [0,2 ; 0,8] ; un effet `interaction_seuil` ne conditionne pas un trait sur lui-même ;
- varie les issues que chaque effet favorise ; évite qu'un seul effet décide presque seul de l'issue.

**Tailles** (mesurées par un programme ; unité : nat par instance). La taille d'un effet est l'information qu'on perd en le
retirant du monde, les autres gardés (divergence moyenne entre le monde et le monde sans cet effet). Bornes : **forte** de
0,10 à 0,25 ; **moyenne** de 0,04 à 0,08 ; **faible** de 0,02 à 0,035. Le monde entier doit rapporter entre 0,30 et 0,90
nat par instance de plus que la loi qui ne connaît que la fréquence des issues. Ordres de grandeur **estimés** (écart entre la plus grande et la plus petite
des trois composantes du vecteur, quand les autres effets sont présents) : effet principal fort ≈ 1,4 à 2,4 ; principal
faible ≈ 0,6 à 0,9 ; seuil faible ≈ 1,1 à 1,8 ; sous-population faible ≈ 1,0 à 1,5 ; interaction de seuil moyenne ≈ 1,3 à
1,8 ; interaction de sous-population moyenne ≈ 1,8 à 2,6. Un programme mesurera chaque taille ; il peut ramener par un seul
facteur d'échelle un effet hors de sa classe dans sa classe, sans toucher à ses traits, à sa condition, à sa direction.

Rends uniquement le bloc `json`.

---8<--- fin du texte servi ---8<---

## Notes de conception (non servies)

- **Forme de sortie** : un bloc `json` ; l'extraction prend le dernier bloc `json` de la réponse, le lit en JSON strict,
  et l'écrit tel quel (octets) avec son empreinte ; la réponse brute entière de l'interface est versée à part, au dossier
  privé du monde (section 2.3 de la conception), jamais au dépôt public.
- **Paramètres de l'appel** : `kimi-k3.1-pro` par le relais (`relais_kimi_v3.py`, `d54ed2bc…`), raisonnement par défaut,
  borne de sortie 131 072 jetons (comme la configuration v8), délai 7 200 s ; une seule réponse ; aucun outil (la recherche
  du relais v4 reste éteinte : `--max-recherches 0`).
- **Exemple de forme** : les emplacements du gabarit ne portent aucun nombre ; les identifiants de traits montrés (0) sont
  des exemples de forme. La section « Tailles » ne donne que des fourchettes de classe, jamais un monde.
- **Correction** (si l'étalonnage par programme n'est pas retenu par Lazar, question Q-3 de la conception) : au plus deux
  appels de correction, chacun sans historique, qui reçoivent ce texte, le JSON rendu et le seul message de refus du
  vérificateur (contrôle, identifiant d'effet, taille mesurée, bornes) — rien d'autre.
