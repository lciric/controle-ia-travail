# Contre-lecture (R2) — « Le pari apparié borné — conception v8 » (Opus 5.5) et le code v7, version 25 — rapport v1

Contre-lecteur : sous-agent neuf **Fable 5.1**, autre modèle que l'auteur ; je n'ai écrit ni la v8, ni le code, ni une
contre-lecture antérieure. Début : mardi 27 octobre 2026, **21:57:14 UTC** (`date -u`, appel séparé). Portée étroite : ce
que la v8 et la version 25 changent. Aucun fichier du dépôt modifié (module importé sans écriture de bytecode ; le dossier
`pole/__pycache__` date de 17:40, heure de Paris, avant ma session) ; tout ce que j'ai écrit est dans
`/tmp/claude-0/-home-claude/c5a45195-121d-5962-9d0a-4896cc046231/scratchpad/contre-lecture-pari-signe-v8/`. Aucune clé
ni aucun jeton lu, affiché ou cherché ; aucune dépense (processeur seul, 4 secondes). Empreintes vérifiées avant lecture
(section 7) ; le code conforme à `EMPREINTES-orchestrateur-pole-v7-v25.txt` (`sha256sum -c … | grep -v ': OK'` vide).

## Verdict

1. **La v8 et la version 25 ferment K7-1, K7-2, K7-3, K7-5, K7-9, K7-10 au sens où la v8 les énonce** ; K7-4, K7-6, K7-7,
   K7-8 sont correctement déclarées ouvertes (obligation d'orchestrateur ou réserve théorique, chacune nommée). Le refus de
   `lire()` ferme l'artefact « j'ajoute si ça monte, je saute sinon » **sans déclaration** : 1 000 courses sur 1 000
   refusées à la première génération, 0 fausse promotion (contrôle honnête 0,038 et 0,044).
2. **Deux chemins restent, l'un dit, l'autre à dire.** (a) La **déclaration `sans_partie` mensongère** reproduit l'artefact
   entier : **0,396** d'au moins une fausse promotion sur 10 générations, **0,978** sur 30 (nul complet, monde A′, α = 0,05) —
   c'est exactement ce que la v8 renvoie à l'orchestrateur (« toute partie calculée est ajoutée »), donc pas une faute de
   la v8, mais le chiffre manque et la phrase « le code ne peut pas la vérifier » n'est écrite que pour l'abandon (K8-2).
   (b) **`empreinte_unites` est facultative** (`None` passe sans trace) : la même partie ajoutée deux fois sans empreinte
   est acceptée (e = 4 au lieu de 2) ; et l'empreinte vérifie l'**égalité** de l'ensemble d'unités, pas la **fraîcheur** :
   un sur-ensemble (banque qui grandit d'une unité : 101 unités contre 100, clé différente puisque la population est
   l'empreinte de la banque) passe pour une partie neuve ; une relance sous une autre identité aussi (K8-1).
3. **La clé (partie, Λ) est juste ; tous les chiffres de la v8 sont justes contre leurs fichiers** (1,77 ; 0,379 ; 0,982 ;
   0,034 ; 1,9 ; k* = 2 et 4 ; « versions 20 à 25 » ; 262 essais) ; les cinq essais nommés passent et testent ce qu'ils
   disent, avec deux trous (Λ non testée dans la clé, `empreinte_unites=None` non testé). **Amender en v9 par deux phrases
   et une garde (K8-1, K8-2) ; pas refaire.**

---

## 1. Réponses aux questions

### Q1 — Fermetures et réserves

| constat v7 | état en v8 / version 25 | vérifié par |
|---|---|---|
| K7-1 partie sautée invisible | **fermé au niveau du code** : `lire()` refuse une fiche active sans partie ni déclaration ; l'état reste intact après le refus (génération 1, aucune trace écrite, A (5)) ; texte « exactement une » et obligation de l'orchestrateur écrite | B : 1 000 / 1 000 courses refusées, 0 promotion ; A (5) |
| K7-2 unités non identifiées | **fermé à moitié** : `evaluer` rend `empreinte_unites` (recalculée à l'identique : banque, partie, identifiants triés, A (9)) ; la `Course` refuse une répétition **exacte** pour **la même fiche**, **si** l'empreinte est passée | A (1) à (4) : trois contournements, K8-1 |
| K7-3 partie et Λ hors clé | **fermé** : `partie` et `lambdas` dans la clé ; développement ≠ épreuve ; Λ changée ⇒ clé changée (A (8)) | A (8) |
| K7-5 abandon d'une gelée silencieux, pas de trace | **fermé** : partie pour une gelée refusée ; `abandons[fiche] = (génération, mode, motif)` ; `retirer` garde une liste de motifs | essai `test_abandon_d_une_gelee_et_traces` ; A (6), (7) |
| K7-9 partage de α_g | **fermé** (texte D-S25 bis (1) et docstring de `Course`) | lecture |
| K7-10 en-tête, commentaire de l'essai | **fermé** (« versions 20 à 25 » ; « sans la retirée : k* = 2 ; avec : k* = 4 ») | lecture, ligne 1 du module |
| K7-4 scellement détecte, n'empêche pas | **déclaré ouvert**, comme obligation d'orchestrateur (consignation hors de l'objet) — juste | lecture |
| K7-6 alignement par rang | **déclaré ouvert**, correction prévue nommée ; « exact quand chaque unité porte les deux étiquettes » — juste | lecture |
| K7-7 ordre secret dérivé de toute la banque | **déclaré ouvert**, correction prévue nommée — juste | lecture |
| K7-8 échangeabilité par unité | **déclaré ouvert**, τ dit nominal, « sans effet sur la garantie des e-valeurs » — juste | lecture |

### Q2 — Le refus de `lire()` ferme-t-il l'artefact ? Chemins restants

- **Fermé** : sans déclaration, la lecture lève une erreur dès la première génération où une fiche active n'a pas de partie ;
  l'état n'est pas modifié (A (5)) ; aucune promotion possible (B, 0 sur 1 000).
- **Déclaration `sans_partie` mensongère** (la partie a été vue, on déclare « monde indisponible ») : l'artefact passe
  entier — **0,396** (10 générations), **0,978** (30) ; E[e maximale] 47 et 102 (seuil d'arrêt 80 = m/α). Le code ne peut
  pas le voir ; la v8 le renvoie à l'orchestrateur ; la trace `sans_partie[(génération, fiche)] = motif` permet l'audit
  après coup si le monde journalise ses parties calculées (à dire : K8-2).
- **Abandon « avant partie » mensonger** (la partie a été vue, elle descend, on gèle avec `avant_partie=True`) : accepté
  (A (6)), mais ce canal **ne compose pas** : la fiche est gelée pour toujours, l'espérance de l'e-valeur gelée est au plus
  E[max(1, e_g)] = 1,77 une seule fois ; mesuré : 0,025 et 0,023 de fausse promotion (≤ α). La v8 le dit à la charge de
  l'orchestrateur, tracé (génération, mode, motif). Juste.
- **`empreinte_unites` absente** : chemin **silencieux** (A (1) : même partie deux fois sans empreinte, acceptée, e = 4 ;
  A (2) : empreinte donnée puis omise, acceptée). Rien ne force l'orchestrateur à la passer, rien ne trace son absence.
  K8-1.
- **Déclaration pour une fiche non active** : `sans_partie` d'une gelée ou promue est enregistrée sans effet — inoffensif.

### Q3 — `empreinte_unites` suffit-elle à « unités fraîches » ?

Non, trois manques (A (1) à (4)) : (i) facultative ; (ii) **égalité** d'ensemble, pas **disjonction** : la banque grandie
d'une unité donne 101 unités, une empreinte différente, une clé différente (population = empreinte de la banque) — la
`Course` accepte la seconde partie, qui relit les 100 premières unités dans un autre ordre secret (e-valeur en espérance
élevée au carré sur la part commune) ; (iii) **par fiche** : une relance sous une autre identité (`entrer` d'une fiche neuve)
lit les mêmes unités sans refus — la v7 demandait « et, par la mémoire, pour la lignée de la clé », la v8 écrit seulement
« une fiche ne reçoit jamais deux fois la même », vrai mais plus étroit que D-S25 bis (5). Le cas (iii) est bénin si la
fiche relancée n'hérite rien (budget neuf, e-valeur à 0) ; il ne l'est plus si l'héritage par clé (hors code) lui transmet
la valeur de l'ancienne fiche. Correction : garder par fiche (et par lignée, par la mémoire) l'**ensemble des identifiants**
(banque, partie, unité) et refuser toute **intersection** ; `evaluer(monde, engagement, unites_exclues=…)` pour ne lire que
le neuf ; refuser `empreinte_unites=None` (ou le tracer comme « partie sans identité »).

### Q4 — La clé avec la partie et Λ

Juste : champs `comparateurs, contrastes, garde, lambdas, m_max, partie, ponderation, population, seuils, strate, tau`
(A (8)) ; `partie` et `lambdas` y sont ; développement ≠ épreuve ; Λ changée ⇒ clé changée ; le budget reste hors clé
(voulu). Suffisante pour ce que D-S18 nomme. Reste hors clé, mineur : la **règle de combinaison** des e-processus sur Λ
(moyenne) et la règle d'arrêt — une version du module qui changerait la combinaison à Λ constante garderait la clé. À
nommer dans la clé (« version de l'e-processus ») ou à dire. La partie de calibrage est refusée dès `construire` : bien.

### Q5 — Les essais testent-ils ce qu'ils disent ?

Les 5 essais nommés passent (U : 3 + 1 + 1, 0 échec, 0 erreur ; les deux fichiers entiers : 22 et 5, 0 échec) ; 262
`def test_` dans `essais/` (le « 262 » du LISEZMOI v25).
- `test_partie_sautee_refusee_a_la_lecture` : refus puis déclaration tracée `(1, "b")` — teste ce qu'il dit (cas sain et
  artefact, R5).
- `test_unites_deja_lues_refusees` : répétition exacte refusée, autre empreinte acceptée — juste ; **ne teste pas**
  `empreinte_unites=None` (qui passe) ni une seconde fiche.
- `test_abandon_d_une_gelee_et_traces` : partie pour une gelée refusée, trace d'abandon, deux motifs de retrait gardés —
  juste ; le second `abandonner("a")` sans partie est « sans effet » et **sans trace** (A (7)), ce que l'essai entérine.
- `test_cle_de_l_heritage` : `partie="developpement"` ajouté — ferme K7-3 ; Λ non testée (je l'ai fait : A (8), clé différente).
- `test_bout_en_bout` : la même lecture du même engagement refusée deux fois dans une course — juste (K7-2 au sens exact).

### Q6 — Chiffres : section 5. Tous justes.

## 2. Constats, du plus grave au moins grave

### Touche la garantie (par une voie que la v8 croit fermée)

**K8-1 — « Unités fraîches » n'est vérifié que pour une répétition exacte, par fiche, et seulement si l'empreinte est passée.**
- **Où.** `Course.ajouter_trajectoire` (`if empreinte_unites is not None`) ; `unites_lues` par fiche, ensemble d'empreintes
  entières ; v8 verdict 2 « la condition « unités fraîches » devient vérifiable » et D-S25 bis (5) « une fiche ne reçoit
  jamais deux fois la même ».
- **Ce qui manque.** A (1) : sans empreinte, la même partie deux fois est acceptée (e = 4) ; A (2) : empreinte puis
  omission, acceptée ; A (3) : fiche relancée sous un autre nom, même empreinte, acceptée ; A (4) : banque grandie d'une
  unité → 101 unités, empreinte et clé différentes, seconde partie acceptée (100 unités relues). La v8 dit « vérifiable » ;
  le code vérifie l'égalité, pas la fraîcheur.
- **Correction.** Refuser `None` (ou tracer « partie sans identité ») ; garder les identifiants d'unités, refuser toute
  intersection par fiche et, par la mémoire, par lignée de clé ; texte : « vérifiable pour une répétition exacte ; la
  disjonction des unités entre parties reste à l'orchestrateur » tant que le code ne la tient pas.

### Clarté sur une obligation d'orchestrateur (la garantie en dépend, la v8 le dit déjà)

**K8-2 — La déclaration `sans_partie` mensongère reproduit l'artefact entier ; la v8 ne le chiffre pas et ne dit « non
vérifiable par le code » que pour l'abandon.**
- **Où.** D-S25 bis (2) v8 ; `Course.lire`.
- **Ce qui manque.** B : 0,396 (10 générations), 0,978 (30), E[e max] 47 et 102, contre 0,038 et 0,044 honnête. La trace
  `sans_partie` ne vaut audit que si le monde journalise les parties qu'il a calculées (sinon rien à confronter).
- **Correction.** Une phrase : « la déclaration « sans partie » est à la charge de l'orchestrateur, le code la trace sans
  pouvoir la vérifier ; une déclaration fausse rouvre l'artefact entier (0,40 et 0,98) ; le monde journalise toute partie
  calculée (identifiant, empreinte des unités) pour que la trace soit confrontable ». Mieux, déjà dit par la v8 : le monde
  remet la partie à la course.

### Contrat (R5) et trace

**K8-3 — Second abandon d'une gelée sans partie : silencieux, sans trace** (A (7)) ; `sans_partie` d'une fiche non active
enregistrée sans effet. Sans biais. Correction : consigner (liste d'abandons, comme `retirees`), ou refuser.

### Clé (mineur)

**K8-4 — La règle de combinaison sur Λ et la règle d'arrêt sont hors clé** (Q4). Ajouter un champ « version de
l'e-processus », ou dire que la clé suppose le module figé.

### Essais (mineur)

**K8-5 — `empreinte_unites=None` et Λ dans la clé ne sont pas testés** (Q5) ; l'essai de K7-2 n'a qu'un cas « même fiche,
même empreinte ». Ajouter : `None` refusé (après K8-1), seconde fiche, Λ.

## 3. Décisions de la v8 : avis

| décision | avis |
|---|---|
| D-S25 bis précisée (0,85) | juste ; 0,85 tenable pour « exactement une partie ou déclaration » et « partie calculée ajoutée » ; « unités identifiées » n'est vrai qu'au sens étroit (K8-1) : dire « répétition exacte refusée », 0,75 sinon |
| D-S18 précisée (0,85) | juste et codée (partie, Λ) ; 0,85 tenable |

## 4. Mathématiques en trois lignes

- Déclaration mensongère = politique de saut : E[e_g · 1(e_g ≥ 1) + 1(e_g < 1)] = E[max(1, e_g)] = 1,7666 par génération
  (exact, binomial sur 20 pas ; A (10)), composé jusqu'au seuil 80 : 0,40 puis 0,98 de fausse promotion.
- Abandon mensonger : gel définitif à la valeur favorable, E ≤ 1,77 **une fois** (non composé) ; la règle e-BH tolère
  E[e] ≤ 1,77 au pire 1,77·α ; mesuré 0,025 ≤ α.
- Sur-ensemble d'unités : la part commune est lue deux fois dans deux ordres secrets ; sous le nul, E[e₁·e₂] n'est plus
  borné par 1 (dépendance par les mêmes unités) ; seule la disjonction donne la martingale de D-S25 bis (5).

## 5. Chiffres de la v8 contre leurs fichiers

| où (v8) | cité | fichier, valeur | verdict |
|---|---|---|---|
| en-tête | v7 `fb422cbc…`, rapport v7 `1e21163f…`, script `f6760b9d…`, sortie `a75668ec…` | `sha256sum` (section 7) | justes |
| en-tête | verdict v7 : K6-1, K6-3, K6-5 à K6-12 fermés, K6-2 à moitié ; retrait valide ; seuil conforme strict tient ; K7-1 à K7-3 touchent la garantie ; chiffres justes ; « corrections locales » | rapport v7, verdict 1 à 3 | juste |
| en-tête, verdict 1, D-S25 bis (2) | 0,379 (10), 0,982 (30), 0,034 (tout ajouté), 1,77 à 20 pas | rapport v7 l. 19-20, 67-68, 259, 312-313 ; recalcul exact 1,7666 (A (10)) ; mes graines : 0,396 / 0,978 / 0,038 | justes |
| réserve K7-6 | borne grossière 1,9 | rapport v7 K7-6 et § 4 | juste |
| K7-10 | « versions 20 à 25 » ; k* = 2 sans, 4 avec | `pari_apparie.py` l. 1 ; rapport v7 K7-10 et Q6 | justes |
| § 3 | signatures `lire(sans_partie=None)`, `ajouter_trajectoire(..., empreinte_unites=None)`, `abandonner(..., motif="", empreinte_unites=None)`, `retirer` garde les motifs ; partie et Λ dans la clé ; `evaluer` rend `empreinte_unites` | `pari_apparie.py` l. 272, 296, 316, 340 ; `engagement_apparie.py` l. 63-64, 95-96 | justes |
| § 3 | essais nommés (cinq) ; total « voir LISEZMOI v25 » | `CorrectionsV8` (3), `test_cle_de_l_heritage`, `test_bout_en_bout` ; LISEZMOI v25 : 262 ; 262 `def test_` comptés | justes |
| en-tête | rédaction commencée après 21:52:27 UTC | rapport v7 fini à 21:50:08 UTC | cohérent |

## 6. Vérifications sur processeur

Interpréteur `/opt/venv-essaim-sim-v1/bin/python -I -B` (numpy 2.5.4) ; graines `numpy.random.SeedSequence(2026102723,
spawn_key=(section, indice))` → `random.Random` (R9) ; 1 000 répétitions par politique et par horizon ; 3,9 secondes ;
manifeste dans la sortie. Première version du script lancée avec des incréments au lieu du logarithme cumulé (mon erreur,
corrigée : la `Course` lit des trajectoires cumulées ; `hash()` remplacé par un indice fixe) ; seule la version corrigée est
rendue.

| fichier | SHA-256 |
|---|---|
| `contre-verification-pari-signe-v8.py` | `2a5f7b61e0fa6734dd9f79098e58ffc7af9d9d8a17ee93edcd04e16bad574207` |
| `contre-verification-pari-signe-v8-sortie.json` | `a3f3a2f0f959c5027dd258b6bbc32668bfe455f12ba94986b138a4bf0376e615` |

- **U** : `CorrectionsV8` 3/3, `test_cle_de_l_heritage` 1/1, `test_bout_en_bout` 1/1 ; fichiers entiers 22 et 5 ; 0 échec.
- **A** : (1) sans empreinte, même partie deux fois : acceptée, e = 4 ; (2) empreinte puis omise : acceptée ; (3) relance
  sous une autre identité, même empreinte : acceptée ; (4) banque grandie 100 → 101 unités : empreintes différentes, clé
  différente, seconde partie acceptée ; (5) refus de `lire` : génération 1, `sans_partie` vide, aucune lecture ; (6) abandon
  « avant partie » après `lire` : `(2, "avant_partie", "m")` ; (7) second abandon : trace inchangée ; (8) clé : 11 champs,
  Λ = (0,1 ; 0,3 ; 0,6 ; 0,9), développement ≠ épreuve, Λ changée ⇒ clé changée ; (9) `empreinte_unites` recalculée
  identique ; (10) E[max(1, e₂₀)] = 1,7666.
- **B** (nul complet, A′ 20 pas, 4 fiches, α = 0,05, 1 000 courses) : honnête 0,038 (10 g.) et 0,044 (30 g.) ; saut sans
  déclaration : 1 000 / 1 000 refusées, 0 promotion ; déclaration mensongère 0,396 et 0,978, E[e max] 47 et 102 ; abandon
  mensonger 0,025 et 0,023.

**Limites.** Monde A′ illustratif ; K7-6, K7-7, K7-8 non resimulés (déclarés ouverts, hors portée) ; `monde_banque_scores`
non relu (inchangé, même empreinte `306c47df…` qu'en v24) ; le lien au cycle (mémoire, héritage par clé) n'existe pas en
code, donc (iii) de Q3 est raisonné, pas mesuré ; la v7 n'a été relue que par le rapport v7 et son empreinte.

Pour reproduire, depuis le dossier de mes fichiers :
```
REP=1000 /opt/venv-essaim-sim-v1/bin/python -I -B contre-verification-pari-signe-v8.py > contre-verification-pari-signe-v8-sortie.json
```

## 7. Fichiers lus et empreintes SHA-256 complètes

Dossier `…/` = `/home/claude/canal-conv-audit-n04/brouillons/canal-reprise-releve-v1/envois/pole-scientifique-automatique-v1/`.
Tous conformes à leurs compagnons `.sha256` ; le code conforme à `EMPREINTES-orchestrateur-pole-v7-v25.txt`, lui-même
conforme à son compagnon.

| fichier | SHA-256 |
|---|---|
| `…/pari-de-signe/conception-pari-de-signe-v8.md` | `3e9609fcaef05b539ed37065d229c7b46a86e9cbbfe79bb3e9b8233637b766f5` |
| `…/pari-de-signe/contre-lecture-v7/rapport-contre-lecture-pari-signe-v7.md` | `1e21163faf3ebd1f9afddb5f28c1bd6b90e6d2bd86c1bd099f9013fdbadb8860` |
| `…/pari-de-signe/conception-pari-de-signe-v7.md` (empreinte seulement) | `fb422cbc2614eee112d5a0b430f4827ead879102892a039f388110e942995819` |
| `…/pari-de-signe/contre-lecture-v7/contre-verification-pari-signe-v7.py` (empreinte seulement) | `f6760b9df0ad31c1497b0eadea50d0d0353a7cb4dbbeb5dee237532b53ab8663` |
| `…/pari-de-signe/contre-lecture-v7/contre-verification-pari-signe-v7-sortie.json` (empreinte seulement) | `a75668ecf265c6856bf598cdf70a080c7eaf88a23771fe9e31448d00dabaf1aa` |
| `…/orchestrateur-pole-v7/EMPREINTES-orchestrateur-pole-v7-v25.txt` | `572dbb7df722abf425070fd478576a354b57ca8a0d12b9e3557c61783f25af08` |
| `…/orchestrateur-pole-v7/LISEZMOI-orchestrateur-pole-v7-v25.md` (l. 13-15) | `c2f6dc691cf580584e62aafeef08ab707380d29f6c80ae2b80f27e3dfcf4883a` |
| `…/orchestrateur-pole-v7/pole/pari_apparie.py` (l. 1-3, 150-348) | `6bb9be5a1b1bab961350670d7e6d2e55798b3a5d146adf2f56fbbd59952c4066` |
| `…/orchestrateur-pole-v7/pole/engagement_apparie.py` | `b519d8606633c9b33ae841ee53678b72e46188ba8ca9a34114861d2aad97b846` |
| `…/orchestrateur-pole-v7/pole/monde_banque_scores.py` (l. 115-138 ; inchangé depuis v24) | `306c47df85bef6732159467a42d49738db341f5d3b86bc29d3908b7847bb449e` |
| `…/orchestrateur-pole-v7/essais/test_v7_pari_apparie.py` (l. 275-314, liste des essais) | `446830387283a0a482bc46595bb1c5dd2c6e0357bba2640c62e666e853fc2f9f` |
| `…/orchestrateur-pole-v7/essais/test_v7_engagement_apparie.py` | `4aa2725487d4efd96cc8a0875858d85677fc47a367c8fa4233ead6830d85cf80` |
| `…/orchestrateur-pole-v7/essais/test_v7_monde_banque_scores.py` (l. 12-26, `banque_synthetique`) | conforme à `EMPREINTES-…-v25.txt` |

Heure de fin (lue sur `date -u` dans un appel séparé, juste avant cette ligne) : mardi 27 octobre 2026, **22:03:28 UTC**.
