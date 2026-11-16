# Réfutation — « ensemble de confiance pour les poids du nul, puis maximum sur cet ensemble » — v1

**Statut.** Mise au point exploratoire, **aucune revendication**. Rien n'est préenregistré ; aucun essai ne visait un signe ;
toutes les issues sont rapportées de la même façon. Processeur seul, aucun appel réseau ni payant, aucun commit, aucun
fichier de l'auteur modifié.

- **Réfutateur** : sous-agent neuf, d'un autre modèle que l'auteur ; je n'ai écrit aucune des pièces citées.
- **Date** : 2026-11-15, de 16:00 à 18:00 UTC (`date -u`) ; dépôt lu sur `main`, tête `108c0bd1`.
- **Calculs** : Python 3.13.18, numpy 2.4.6, scipy 1.17.1 (`.venv/bin/python -I -B`), machine partagée très chargée.
- **Objet** : le rendu « confiance » (`methodes-confiance-v1.md`, `b2cb2685…f266`, et ses programmes), même dossier.

## 0. En tête

1. **La validité tient.** Les cinq méthodes à ensemble de confiance gardent la taille α. La preuve se suit sans pas faux.
   Un calcul exact sur un nul jouet, aux tailles du juge, donne au pire 1,75 % de promotions à tort
   (α = 5 %). Mon attaque, écrite sans recopier le code de l'auteur, sur 15 000 mondes du nul (8 cas, dénominateurs
   serrés) : **0 copie exacte promue**, par les dix bras ; carte hors classe : au plus 1/2000 par bras. Les cartes faites
   pour être le pire cas sont promues au plus 11/1000 fois (borne haute 0,0196, sous 0,05). Non-couverture au plus
   5/2000 à β = 0,01 et 14/2000 à β = 0,025.
2. **Les deux façons des fiches échouent bien**, dans le banc de l'auteur (rejeu) comme dans le mien : la façon « en ligne »
   promeut une copie exacte dans 80,3 % à 100,0 % de mes mondes, la façon « moitié » dans
   5,0 % à 48,8 %.
3. **Le gain de puissance annoncé ne tient pas.** Le rejeu rend ses chiffres à l'identique, mais la comparaison au maximum
   certifié n'est pas loyale : le « v9 du banc » est calculé par 80 pas d'un algorithme lent, et son majorant certifié reste
   loin du vrai maximum (sur ses mondes de dose 0,50 : écart médian de richesse 2,1 nat, jusqu'à 19,7 nat). Les bras à
   ensemble de confiance échappent en partie à cet écart ; c'est lui qui fait le « gain ». Sur **ses** 200 mondes, mêmes tirages,
   mêmes instants, mêmes seuils, même ensemble, avec des maxima serrés : dose 0,50, v9 0,600 et ensemble coupé 0,600
   (il annonçait 0,395 et 0,515) ; dose 0,75, 0,820 et 0,815 (il annonçait 0,630 et 0,745).
   Part du prix regagnée avec 1 000 tirages de confiance : 0 % et −7 %, au lieu de 42 % et 55 %.
4. **Réserves.** (R1) Ces méthodes perdent une protection du v9 : une carte qui est elle-même un membre du nul peut être
   promue quand le monde est hors du nul (calcul exact sur un nul jouet : 6,9 % à 23,9 % ; le v9 : 0, toujours). (R2) Le banc de
   l'auteur n'a que neuf coupures par trait : il ne montre pas la taille sur toute la classe du v9. (R3) Le coût annoncé
   pour le vrai v9 est sous-estimé.

### Verdict par méthode (détail en section 8)

| méthode | l'auteur dit | validité (taille α) | fausse promotion observée (mon attaque) | puissance annoncée | verdict |
|---|---|---|---|---|---|
| BB_A | valide | tient | copie : 0 ; pire carte : 11/1000, borne haute 0,0196 | « jamais plus que le v9 » : confirmé | **tient** (validité seule) |
| BB_T_seq | valide | tient | copie : 0 ; pire carte : 11/1000, borne haute 0,0196 | gain annoncé à 1 000 tirages : non retrouvé | **tient** (validité seule) |
| BB_T_coupe | valide | tient | copie : 0 ; pire carte : 11/1000, borne haute 0,0196 | « regagne 14 %, 42 %, 55 % » : **ne tient pas** (0 % à maxima serrés) | **tient** (validité seule) |
| BB_S_moitie | valide | tient | copie : 0 ; pire carte : 18/2000, borne haute 0,0142 | « perd toujours » : confirmé | **tient** (validité seule) |
| BB_Q_blocs | valide | tient | copie : 0 ; pire carte : 3/1000, borne haute 0,0087 | « perd toujours » : confirmé | **tient** (validité seule) |
| F1_en_ligne | non valide | ne tient pas | copie promue : 80,3 % à 100,0 % | sans objet | **ne tient pas** (échec réel) |
| F2_moitie | non valide | ne tient pas | copie promue : 5,0 % à 48,8 % | sans objet | **ne tient pas** (échec réel) |

« Tient » veut dire ici : la méthode est un test de niveau α sur les mondes du nul. Cela ne dit pas qu'elle regagne la
puissance perdue : pour les cinq méthodes, elle ne la regagne pas (section 6).

## 1. Ce que j'ai lu (empreintes recalculées le 15 novembre, égales à leurs compagnons)

| pièce | chemin | empreinte |
|---|---|---|
| preuve de validité du nul limité | `docs/notes/organisme-idees-juge-v1/preuve-validite-nul-limite-v1.md` | `44f249409193778ccbaaa12b6c5e74d64434dfb87be77382d8bb9438459281b2` |
| préenregistrement de l'idée 1.1 | `docs/notes/organisme-idees-juge-v1/prereg-nul-par-morceaux-limite-v1.md` | `46ef2b92119ee5dff05727b90ca8bdd3ba57b52f9c1c75893750c792a2abc089` |
| contre-lecture (échec des deux façons refait) | `docs/notes/organisme-idees-juge-v1/contre-lecture-prereg-nul-limite-et-preuve-v1.md` | `763fc6e29cd80868dcdb1d848eafdc928a39fca7244fa16eb0ac721ec705014e` |
| code du nul v9 (lu, jamais exécuté) | `docs/notes/organisme-idees-juge-v1/copie-nul-v9-a41b7b5/orchestrator/pole/nul_v9.py` | `7ae450df2482246122bf9fbcf0fa5ef30b4a7e4c6f0d09531e83af048e46ee95` |
| jugement d'une carte, pari, nul v8, membres (lus, jamais exécutés) | `docs/notes/organisme-courbe-dose-reponse-v1/code-organisme-94bfd92/orchestrator/pole/` : `a_blanc_v59.py`, `selection_pari.py`, `nul_v8.py`, `nul_filles_v2.py` | `606aa8b4…0826c`, `35992811…306bc`, `cc452aaf…6b888`, `0ed9b4ad…38910` (égales à la liste `empreintes-copie-v1.txt` de la copie) |
| relevé d'idées, § 1.1 | `docs/notes/organisme-conception-propre-v1/relecture-exploratoire-v2/releve-idees-reutilisables-v1.md` | `bd253b6c68f6baada0e61b5381f029b52838ca34aa092502e55253c662451c6c` |
| fiches argon-p1-01 (n° 0), argon-p2-01 (n° 14), opus-p1-05 (n° 9), fable-p1-05 (n° 13), champ `demande_organisme` | `runs/course-ideation-conception-propre-v1/20261113-235541-course-ideation-conception-propre-v1-g1/copies/sortie--fiches-validees.json` | `a9f9594e2dc3a7a553c54577202817758e3f7ef231445f1a48d500fc647389d5` |
| verdict de la validation du v9 (seul fichier ouvert dans son dossier, par son chemin exact) | `docs/verdicts/verdict-validation-nul-v9-v1.md` | `1407e460367754bb9f76b37174f3a21585970864eb9beaa2699494d90125c1ea` |
| dossier de l'auteur : note, six programmes, 73 sorties | `docs/notes/organisme-idees-juge-v1/correction-poids-v1/confiance/` | 80 compagnons vérifiés, 0 écart ; note `b2cb2685f5fc1b10d0cbb2be9deef158d11e2979e2a519dbfc682bb5a293f266` |

« Puissance perdue » (verdict, par son chemin exact) : le v9 tient ses 18 lignes fatales, mais sur la ligne I02 sa puissance
appariée est sous celle du v8 de 0,105, plus du double de la marge de 0,05. La question posée à l'auteur : regagner ce prix
sans perdre la taille, en « apprenant les poids » d'une façon valide.

## 2. (a) La preuve, pas à pas

**Théorème BB (section 3 de la note de l'auteur).** Je n'ai trouvé aucun pas faux.
1. *Domination.* Sur l'événement « le monde θ* est dans C », un majorant certifié du maximum sur C domine la
   log-vraisemblance du monde à chaque instant. C'est une inégalité tirage par tirage : elle ne demande rien sur le lien
   entre C et les tirages évalués. Juste.
2. *Majoration.* La richesse reste alors sous le rapport de vraisemblance Λ de la carte contre le monde. Juste.
3. *Surmartingale et Ville.* Λ est une surmartingale positive partie de 1 dès que la carte est gelée avant les tirages
   frais. La carte peut dépendre des tirages de confiance : l'argument se fait sachant ces tirages. Juste.
4. *Somme.* Promotion ≤ non-couverture + passage de Λ au-dessus de 1/(α − β) ≤ β + (α − β). Juste.
- Version par blocs : même raisonnement bloc par bloc, sur l'événement « couvert à tous les blocs » (Ville sur une seule
  martingale). Juste.
- Couverture (hypothèse B1) : elle vient de l'inégalité de Markov ou de Ville appliquée au produit m/p_θ*. Elle demande que le
  prédicteur m soit une vraie loi sur les issues, sachant l'instance et le passé. Je l'ai vérifié dans le code : le
  prédicteur est (1 − 0,002)·p + 0,002/K, où p est un membre du nul à poids normalisés (`proba_lissee`). Juste.
- Hypothèse « l'entraînement vient du même monde » : lue dans `a_blanc_v59.juger_carte`, lignes 169 et 170. Les 100 instances
  et leurs issues sont bien tirées de la loi du monde. Aujourd'hui le juge n'en garde que les fréquences ; la méthode
  demanderait de garder les couples (instance, issue). L'auteur le dit (l'ensemble entre dans l'engagement).

**Lemme 1.** Juste : un ensemble de la forme {ℓ_t ≥ seuil} bâti sur les tirages évalués contient le maximum de vraisemblance
dès qu'il n'est pas vide. La conséquence chiffrée (« si m = q, promotion quand la richesse du v9 passe 1/max(α − β, β) »)
est juste aussi : avec α = 0,05 et β = 0,01 le seuil devient 25 au lieu de 20.

**Lemme 2.** Juste : dualité faible de Lagrange, puis certificat de Frank-Wolfe d'un problème concave. Le certificat reste
valable avec le plancher 10⁻¹² du code : pour tout point u, log p_v ≤ log p_u + p_v/p_u − 1 (tangente du logarithme), et le
maximum d'une fonction linéaire sur le polytope est pris en un sommet. Je l'ai reprogrammé et comparé à un solveur convexe
indépendant (section 4.1).

**Ce que le théorème ne dit pas** (ce n'est pas un pas faux, c'est une limite de l'énoncé). Il borne la promotion quand
**le monde** est dans le nul. Le v9 a une propriété de plus, qui ne dépend pas du monde : une carte qui est elle-même un
membre du nul a une richesse au plus égale à 1 à chaque tirage ([PREUVE] § 4, remarque (ii) ; c'est la règle d'audit A1).
Les méthodes à ensemble de confiance perdent cette propriété : une carte membre du nul, mais hors de C, peut être promue
quand le monde est hors du nul. Voir la réserve R1 (section 7), avec un calcul exact.

**Remarques sans effet sur la validité.**
- La note parle de « 64 lots » (section 5) ; le résumé en lit 69 (7 800 mondes).
- « λ = 0 rend la valeur du v9 du banc, la méthode n'est donc jamais moins puissante que le v9 au même niveau » : vrai pour
  les valeurs calculées par le banc. Cela ne dit rien de la qualité de ces valeurs ; c'est là que la comparaison de
  puissance se défait (section 6).

**Calcul exact sur un nul jouet** (aucune simulation ; programmation dynamique ; mode `exact` de mon programme). Issue
binaire, sans traits ; 200 tirages frais ; instants 25 à 200 ; α = 0,05 ; ensemble « coupé » comme BB_T_coupe (prédicteur
ajusté sur une moitié des tirages de confiance, lissé à 0,2 %, ensemble sur l'autre moitié) ; maximum exact sur l'ensemble.

- Nul convexe [0,3 ; 0,8], 100 tirages de confiance (`exact-A1-v1.json`), cinq mondes du nul, quinze cartes constantes :
  pire promotion 1,75 % (β = 0,01) et 0,99 % (β = 0,025) ; pire non-couverture
  5,5 × 10⁻⁵ et 3,3 × 10⁻⁴, très sous β ; pour comparer, le maximum sur tout le nul (façon v9) : 2,29 %.
- Même nul, 1 000 tirages de confiance (`exactm-A2-*.json`), deux mondes, huit cartes : pire promotion 1,45 % et 0,97 % ;
  pire non-couverture 3,1 × 10⁻⁵ et 1,5 × 10⁻⁴.
- Nul non convexe (deux lois, 0,3 et 0,7, sans leurs mélanges), monde dans le nul (`exactm-C-*.json`) : promotion au plus
  1,34 %.
- Partout la borne α = 5 % est tenue, avec de la marge. Aucun contre-exemple au théorème.
- La façon « moitié » des fiches (F2), dans ce même jouet à un seul paramètre : copie exacte promue jusqu'à 4,96 %,
  carte voisine jusqu'à 5,25 % (monde 0,65, carte 0,6) : au-dessus de 5 % dès un paramètre, de peu. L'échec net vient avec le
  nombre de paramètres (section 5).

## 3. (b) Rejeu des programmes de l'auteur

- **Résumé** (`essai_confiance_resume_v1.py`, sur ses 69 lots, dans l'ordre de son champ `sources`) : sortie identique à
  l'octet, empreinte `ac6bd796164910e0111aa7cdd775145be8fee2e748e2af35e6ffd692de6eab11`, celle de `sorties/resume-v1.json`.
  Les tables de sa note (sections 5 à 7) sont égales au résumé, chiffre pour chiffre (taille, non-couverture, audit A1,
  puissance, paires discordantes, « β = 0,01 au moins égal à β = 0,025 » : 45 comparaisons sur 45).
- **Lots** (`essai_confiance_lot_v1.py`) : 18 lots rejoués sur 69, un par groupe (cas, nombre de lois, taille de
  l'entraînement), soit 1 875 mondes sur 7 800. 42 225 valeurs comparées (richesse maximale et promotion, par monde, carte
  et méthode) : **0 écart de promotion, 0 écart de couverture, écart maximal de log-richesse 0,0**. Les 51 autres lots ne
  sont pas rejoués (temps) ; leurs chiffres sont pris dans ses fichiers scellés.
- **Certificat** (`essai_confiance_certificat_v1.py`) : le script entier a dépassé dix minutes sur la machine chargée ; il a
  été arrêté par la limite (aucune sortie). Rejeu partiel par ses propres fonctions, mêmes graines : les 40 premiers
  problèmes (160 lignes) ; borne identique (écart 0,0), référence identique à 3·10⁻⁷ près.
- Pièces du rejeu : `rejeu-v1/comparaison-rejeu-v1.json` (lot par lot) et `rejeu-v1/rejeu-certificat-partiel-v1.json`.
- **Coût** (`essai_confiance_cout_v1.py`) : non rejoué. Ce sont des temps ; la machine portait une charge de 10 à 21 pour
  4 cœurs pendant mon passage. Voir la réserve R3 sur le coût annoncé.

## 4. (c) Mon attaque

### 4.1 Le programme

`attaque_confiance_v1.py`, écrit sans recopier le code de l'auteur : les méthodes sont reprogrammées d'après leur énoncé
(sa note, sections 3 et 4). Aucun module de l'auteur n'y est importé.
- **Banc.** Trois issues, deux traits gaussiens, une sous-population, 200 tirages frais, huit instants, α = 0,05, β = 0,01
  et 0,025. Archive : lois softmax, plus une loi « si_sinon » sur une coupure de l'archive (deux quand l'archive a huit
  lois). Nul du banc : mélange par morceau des lois connues et bruit aveugle commun, sur les partitions « aucune »,
  sous-population, coupures de l'archive, neuf déciles par trait. C'est la même classe que le « v9 du banc » de l'auteur
  (même définition, autre code). Un monde membre de cette classe est aussi membre du vrai v9 ; comme la classe du banc est
  plus petite, son maximum est plus bas : l'épreuve de taille est **plus dure** que sur le vrai v9.
- **Maximum certifié.** Points intérieurs (Newton, barrière logarithmique), puis le même certificat que le juge (écart de
  Frank-Wolfe, borne par 0). L'écart de certificat mesuré est de l'ordre de 0,002 nat (au plus 0,0035 nat sur tous
  les lots). Maximum sur l'ensemble : dualité de Lagrange, six valeurs du multiplicateur.
- **Contrôle du majorant** (mode `certificat`, `sorties-attaque-v1/certificat-v1.json`) : 150 petits problèmes, trois
  rayons, comparés à un solveur convexe indépendant (SLSQP, six départs) : **0 violation sur 450 cas**, marge
  médiane 0,044 nat.
- **Méthodes.** BB_A, BB_T_seq, BB_T_coupe, BB_S_moitie, BB_Q_blocs aux deux β (dix bras), le v9 du banc, et les deux
  artefacts F1 et F2. Prédicteur des ensembles : celui de l'énoncé (meilleur membre ajusté, réajusté tous les 25 tirages,
  lissé à 0,2 %).
- **Cartes.** « copie » (la loi du monde) ; « hors classe » (0,7 monde + 0,3 softmax tirée au hasard) ; trois cartes
  « pari », faites pour être le pire cas de l'inégalité de Ville : elles misent tout sur quelques issues choisies d'avance
  (rapport de vraisemblance d'au moins 30, ou 150, avec une probabilité d'au plus 1/30, ou 1/150), puis copient le monde.
- **Arrêt optionnel.** La promotion compte dès que la richesse passe le seuil à l'un des huit instants (quatre pour
  BB_S_moitie, par construction de la méthode).
- **Graines.** `numpy.random.SeedSequence(entropy=2026111577, spawn_key=(mode, cas, monde))`, écrites dans chaque sortie.

- **Écart à l'énoncé, dit** : mon prédicteur de l'ensemble coupé s'arrête à 60 pas au plus (80 chez l'auteur). Sur 18 de ses
  mondes, mon prédicteur séquentiel rend le sien à 10⁻¹³ près ; mon seuil de l'ensemble coupé diffère du sien d'au plus
  0,59 nat. Tout prédicteur prévisible donne un ensemble valide.

### 4.2 Taille : monde = membre du nul, au moins 2 000 mondes par cas obligatoire

Nombre de mondes où la carte est promue à l'un des instants lus, par méthode (β = 0,01), et intervalle de Clopper-Pearson à
95 % du taux. « Non couverts » : mondes où le vrai monde est hors de l'ensemble. « Audit » : mondes couverts calculés en
entier, plus petite marge (majorant moins log-vraisemblance du monde, sur tous les instants), violations (marge < 0).

| cas | mondes | méthode | copie | hors classe | pari début | pari milieu | pari fort | non couverts | audit |
|---|---|---|---|---|---|---|---|---|---|
| copie_interieure | 2000 | BB_A | 0 [0 ; 0,0018] | 0 | 0 | 0 | 1 | 3 [0,0003 ; 0,0044] | 201 ; 1,1289 ; 0 |
| copie_interieure | 2000 | BB_T_seq | 0 [0 ; 0,0018] | 0 | 0 | 0 | 1 | 2 [0,0001 ; 0,0036] | 202 ; 1,1289 ; 0 |
| copie_interieure | 2000 | BB_T_coupe | 0 [0 ; 0,0018] | 0 | 0 | 0 | 1 | 3 [0,0003 ; 0,0044] | 209 ; 1,1064 ; 0 |
| copie_interieure | 2000 | BB_S_moitie | 0 [0 ; 0,0018] | 0 | 0 | 0 | 0 | 2 [0,0001 ; 0,0036] | 162 ; 1,0340 ; 0 |
| copie_interieure | 2000 | BB_Q_blocs | 0 [0 ; 0,0018] | 0 | 0 | 0 | 1 | 2 [0,0001 ; 0,0036] | 202 ; 1,4081 ; 0 |
| copie_interieure | 2000 | v9 | 0 [0 ; 0,0018] | 0 | 0 | 0 | 3 |  | 221 ; 1,1064 ; 0 |
| poids_extremes | 2000 | BB_A | 0 [0 ; 0,0018] | 0 | 8 | 15 | 4 | 1 [0,0000 ; 0,0028] | 154 ; 0,0000 ; 0 |
| poids_extremes | 2000 | BB_T_seq | 0 [0 ; 0,0018] | 0 | 8 | 15 | 4 | 0 [0 ; 0,0018] | 154 ; 0,0000 ; 0 |
| poids_extremes | 2000 | BB_T_coupe | 0 [0 ; 0,0018] | 0 | 8 | 15 | 4 | 0 [0 ; 0,0018] | 155 ; 0,0000 ; 0 |
| poids_extremes | 2000 | BB_S_moitie | 0 [0 ; 0,0018] | 0 | 0 | 13 | 0 | 0 [0 ; 0,0018] | 132 ; 0,0000 ; 0 |
| poids_extremes | 2000 | BB_Q_blocs | 0 [0 ; 0,0018] | 0 | 2 | 0 | 2 | 0 [0 ; 0,0018] | 154 ; 0,0000 ; 0 |
| poids_extremes | 2000 | v9 | 0 [0 ; 0,0018] | 0 | 11 | 15 | 4 |  | 161 ; 0,0000 ; 0 |
| bord_simplexe | 2000 | BB_A | 0 [0 ; 0,0018] | 1 | 9 | 6 | 7 | 2 [0,0001 ; 0,0036] | 159 ; 0,0002 ; 0 |
| bord_simplexe | 2000 | BB_T_seq | 0 [0 ; 0,0018] | 1 | 9 | 6 | 7 | 0 [0 ; 0,0018] | 159 ; 0,0000 ; 0 |
| bord_simplexe | 2000 | BB_T_coupe | 0 [0 ; 0,0018] | 1 | 9 | 6 | 7 | 1 [0,0000 ; 0,0028] | 160 ; 0,0000 ; 0 |
| bord_simplexe | 2000 | BB_S_moitie | 0 [0 ; 0,0018] | 1 | 0 | 7 | 0 | 0 [0 ; 0,0018] | 127 ; 0,0002 ; 0 |
| bord_simplexe | 2000 | BB_Q_blocs | 0 [0 ; 0,0018] | 0 | 4 | 0 | 3 | 0 [0 ; 0,0018] | 160 ; 0,0000 ; 0 |
| bord_simplexe | 2000 | v9 | 0 [0 ; 0,0018] | 1 | 14 | 7 | 7 |  | 167 ; 0,0002 ; 0 |
| beaucoup_de_composantes | 2000 | BB_A | 0 [0 ; 0,0018] | 0 | 0 | 0 | 0 | 4 [0,0006 ; 0,0051] | 204 ; 2,4493 ; 0 |
| beaucoup_de_composantes | 2000 | BB_T_seq | 0 [0 ; 0,0018] | 0 | 0 | 0 | 0 | 0 [0 ; 0,0018] | 200 ; 2,4493 ; 0 |
| beaucoup_de_composantes | 2000 | BB_T_coupe | 0 [0 ; 0,0018] | 0 | 0 | 0 | 0 | 1 [0,0000 ; 0,0028] | 200 ; 2,4117 ; 0 |
| beaucoup_de_composantes | 2000 | BB_S_moitie | 0 [0 ; 0,0018] | 0 | 0 | 0 | 0 | 2 [0,0001 ; 0,0036] | 160 ; 2,4126 ; 0 |
| beaucoup_de_composantes | 2000 | BB_Q_blocs | 0 [0 ; 0,0018] | 0 | 0 | 0 | 0 | 1 [0,0000 ; 0,0028] | 199 ; 2,4493 ; 0 |
| beaucoup_de_composantes | 2000 | v9 | 0 [0 ; 0,0018] | 0 | 0 | 0 | 0 |  | 226 ; 2,4493 ; 0 |
| peu_de_tirages | 2000 | BB_A | 0 [0 ; 0,0018] | 0 | 1 | 0 | 2 | 5 [0,0008 ; 0,0058] | 198 ; 1,1152 ; 0 |
| peu_de_tirages | 2000 | BB_T_seq | 0 [0 ; 0,0018] | 0 | 1 | 0 | 2 | 1 [0,0000 ; 0,0028] | 198 ; 1,1152 ; 0 |
| peu_de_tirages | 2000 | BB_T_coupe | 0 [0 ; 0,0018] | 0 | 1 | 0 | 2 | 1 [0,0000 ; 0,0028] | 198 ; 1,1152 ; 0 |
| peu_de_tirages | 2000 | BB_S_moitie | 0 [0 ; 0,0018] | 0 | 0 | 0 | 0 | 1 [0,0000 ; 0,0028] | 153 ; 1,2726 ; 0 |
| peu_de_tirages | 2000 | BB_Q_blocs | 0 [0 ; 0,0018] | 0 | 0 | 0 | 1 | 3 [0,0003 ; 0,0044] | 202 ; 1,1152 ; 0 |
| peu_de_tirages | 2000 | v9 | 0 [0 ; 0,0018] | 0 | 1 | 0 | 2 |  | 216 ; 1,1152 ; 0 |
| morceaux_archive | 2000 | BB_A | 0 [0 ; 0,0018] | 0 | 20 | 19 | 5 | 0 [0 ; 0,0018] | 170 ; 0,0000 ; 0 |
| morceaux_archive | 2000 | BB_T_seq | 0 [0 ; 0,0018] | 0 | 20 | 19 | 5 | 0 [0 ; 0,0018] | 168 ; 0,0000 ; 0 |
| morceaux_archive | 2000 | BB_T_coupe | 0 [0 ; 0,0018] | 0 | 20 | 19 | 5 | 0 [0 ; 0,0018] | 168 ; 0,0000 ; 0 |
| morceaux_archive | 2000 | BB_S_moitie | 0 [0 ; 0,0018] | 0 | 0 | 18 | 0 | 0 [0 ; 0,0018] | 144 ; 0,0000 ; 0 |
| morceaux_archive | 2000 | BB_Q_blocs | 0 [0 ; 0,0018] | 0 | 5 | 1 | 1 | 0 [0 ; 0,0018] | 168 ; 0,0000 ; 0 |
| morceaux_archive | 2000 | v9 | 0 [0 ; 0,0018] | 0 | 23 | 21 | 5 |  | 172 ; 0,0000 ; 0 |
| morceaux_hors_archive | 2000 | BB_A | 0 [0 ; 0,0018] | 1 | 25 | 11 | 8 | 1 [0,0000 ; 0,0028] | 153 ; 0,0000 ; 0 |
| morceaux_hors_archive | 2000 | BB_T_seq | 0 [0 ; 0,0018] | 1 | 25 | 11 | 8 | 0 [0 ; 0,0018] | 153 ; 0,0000 ; 0 |
| morceaux_hors_archive | 2000 | BB_T_coupe | 0 [0 ; 0,0018] | 1 | 25 | 11 | 8 | 1 [0,0000 ; 0,0028] | 153 ; 0,0000 ; 0 |
| morceaux_hors_archive | 2000 | BB_S_moitie | 0 [0 ; 0,0018] | 0 | 0 | 11 | 0 | 0 [0 ; 0,0018] | 130 ; 0,0000 ; 0 |
| morceaux_hors_archive | 2000 | BB_Q_blocs | 0 [0 ; 0,0018] | 0 | 6 | 0 | 4 | 0 [0 ; 0,0018] | 153 ; 0,0000 ; 0 |
| morceaux_hors_archive | 2000 | v9 | 0 [0 ; 0,0018] | 1 | 27 | 13 | 8 |  | 162 ; 0,0000 ; 0 |
| seuil_reel_classe_elargie | 1000 | BB_A | 0 [0 ; 0,0037] | 0 | 11 | 4 | 1 | 1 [0,0000 ; 0,0056] | 79 ; 0,0000 ; 0 |
| seuil_reel_classe_elargie | 1000 | BB_T_seq | 0 [0 ; 0,0037] | 0 | 11 | 4 | 1 | 0 [0 ; 0,0037] | 79 ; 0,0000 ; 0 |
| seuil_reel_classe_elargie | 1000 | BB_T_coupe | 0 [0 ; 0,0037] | 0 | 11 | 4 | 1 | 0 [0 ; 0,0037] | 80 ; 0,0000 ; 0 |
| seuil_reel_classe_elargie | 1000 | BB_S_moitie | 0 [0 ; 0,0037] | 0 | 0 | 2 | 0 | 0 [0 ; 0,0037] | 63 ; 0,0000 ; 0 |
| seuil_reel_classe_elargie | 1000 | BB_Q_blocs | 0 [0 ; 0,0037] | 0 | 3 | 0 | 0 | 0 [0 ; 0,0037] | 79 ; 0,0000 ; 0 |
| seuil_reel_classe_elargie | 1000 | v9 | 0 [0 ; 0,0037] | 0 | 12 | 4 | 1 |  | 82 ; 0,0000 ; 0 |

Les cas : `copie_interieure` = copie exacte, poids intérieurs ; `poids_extremes` = poids extrêmes (une seule loi connue) ; `bord_simplexe` = bord du simplexe (arête et sommet, coupure hors de l’archive) ; `beaucoup_de_composantes` = beaucoup de composantes (huit lois connues) ; `peu_de_tirages` = peu de tirages (20 tirages de confiance) ; `morceaux_archive` = copie par morceaux sur une coupure de l’archive ; `morceaux_hors_archive` = copie par morceaux hors de l’archive (décile) ; `seuil_reel_classe_elargie` = copie par morceaux sur un seuil réel quelconque (classe élargie à ce seuil).

À β = 0,025 (mêmes mondes) : nombre de copies promues, de cartes hors classe promues, de paris gagnés et promus (début /
milieu / fort), de mondes non couverts.

| cas | mondes | BB_A | BB_T_seq | BB_T_coupe | BB_S_moitie | BB_Q_blocs |
|---|---|---|---|---|---|---|
| copie_interieure | 2000 | 0 ; 0 ; 0/0/0 ; 5 | 0 ; 0 ; 0/0/0 ; 2 | 0 ; 0 ; 0/0/0 ; 13 | 0 ; 0 ; 0/0/0 ; 6 | 0 ; 0 ; 0/0/0 ; 2 |
| poids_extremes | 2000 | 0 ; 0 ; 6/13/4 ; 3 | 0 ; 0 ; 6/13/4 ; 0 | 0 ; 0 ; 6/13/4 ; 1 | 0 ; 0 ; 0/10/0 ; 2 | 0 ; 0 ; 2/0/2 ; 0 |
| bord_simplexe | 2000 | 0 ; 0 ; 2/3/6 ; 3 | 0 ; 0 ; 2/3/6 ; 0 | 0 ; 0 ; 2/3/6 ; 3 | 0 ; 0 ; 0/4/0 ; 0 | 0 ; 0 ; 1/0/1 ; 1 |
| beaucoup_de_composantes | 2000 | 0 ; 0 ; 0/0/0 ; 14 | 0 ; 0 ; 0/0/0 ; 4 | 0 ; 0 ; 0/0/0 ; 5 | 0 ; 0 ; 0/0/0 ; 6 | 0 ; 0 ; 0/0/0 ; 4 |
| peu_de_tirages | 2000 | 0 ; 0 ; 0/0/1 ; 10 | 0 ; 0 ; 0/0/1 ; 4 | 0 ; 0 ; 0/0/1 ; 3 | 0 ; 0 ; 0/0/0 ; 1 | 0 ; 0 ; 0/0/1 ; 10 |
| morceaux_archive | 2000 | 0 ; 0 ; 9/12/5 ; 2 | 0 ; 0 ; 9/12/5 ; 0 | 0 ; 0 ; 9/12/5 ; 0 | 0 ; 0 ; 0/9/0 ; 3 | 0 ; 0 ; 2/0/1 ; 0 |
| morceaux_hors_archive | 2000 | 0 ; 1 ; 14/4/8 ; 2 | 0 ; 1 ; 14/4/8 ; 0 | 0 ; 1 ; 14/4/8 ; 1 | 0 ; 0 ; 0/7/0 ; 2 | 0 ; 0 ; 3/0/4 ; 0 |
| seuil_reel_classe_elargie | 1000 | 0 ; 0 ; 8/3/1 ; 1 | 0 ; 0 ; 8/3/1 ; 0 | 0 ; 0 ; 8/3/1 ; 1 | 0 ; 0 ; 0/1/0 ; 2 | 0 ; 0 ; 2/0/0 ; 0 |

**Lecture.**
- **Copie exacte** : 0 promotion sur les 15 000 mondes, pour les dix bras ; borne haute par cas au plus 0,0037 (seuil_reel_classe_elargie, 1 000 mondes).
- **Carte hors classe** dans un monde du nul : au plus 1/2000 par bras (bord_simplexe, BB_A, β = 0,01) ; 10 promotions en tout sur les dix bras.
- **Cartes « pari »** : la carte « pari début » gagne son pari dans 1,1 % à 2,1 % des mondes selon le cas ; elle est alors promue quand le nul a peu de
  jeu (monde à un sommet). Pire cas : 11/1000 = 1,10 %, borne haute 0,0196 (seuil_reel_classe_elargie, BB_A, β = 0,01, carte pari_debut). Le v9 du
  banc promeut les mêmes (12/1000 au pire). C'est sous α = 0,05 et sous le seuil de Ville (au plus 1/30 pour ces cartes). L'attaque a
  donc des dents : le taux mesuré n'est pas nul, et il reste sous la borne.
- **Non-couverture** : au pire 5/2000 (borne haute 0,0058) à β = 0,01 (peu_de_tirages, BB_A) ; 14/2000 (borne haute 0,0117) à β = 0,025
  (beaucoup_de_composantes, BB_A). L'hypothèse de couverture tient.
- **Audit du majorant** : 14 013 couples (monde couvert, méthode) calculés en entier ; plus petite marge 0,0000 nat ; **0 violation**. Une
  marge nulle se voit quand le monde est à un sommet du nul : le maximum est alors atteint au monde lui-même.
- Les cas « peu de tirages » (20 tirages de confiance) et « huit lois connues » ne changent rien : la validité ne dépend ni de
  la taille de l'ensemble ni du nombre de composantes.

## 5. (d) L'artefact : les deux façons des fiches

Dans **mon** banc, sur les mêmes mondes et aux mêmes instants que les méthodes valides (partition du monde lui-même, comme
chez l'auteur : le cas le plus favorable aux fiches). Nombre de mondes promus et intervalle à 95 %.

| cas | mondes | F1 en ligne, copie | F1, hors classe | F2 moitié, copie | F2, hors classe |
|---|---|---|---|---|---|
| copie_interieure | 2000 | 1870 [0,9233 ; 0,9454] | 537 | 661 [0,3099 ; 0,3516] | 263 |
| poids_extremes | 2000 | 2000 [0,9982 ; 1,0000] | 1871 | 99 [0,0404 ; 0,0599] | 19 |
| bord_simplexe | 2000 | 2000 [0,9982 ; 1,0000] | 1814 | 376 [0,1711 ; 0,2058] | 97 |
| beaucoup_de_composantes | 2000 | 1607 [0,7854 ; 0,8207] | 359 | 975 [0,4654 ; 0,5097] | 456 |
| peu_de_tirages | 2000 | 1894 [0,9363 ; 0,9564] | 580 | 648 [0,3035 ; 0,3450] | 256 |
| morceaux_archive | 2000 | 2000 [0,9982 ; 1,0000] | 1934 | 189 [0,0820 ; 0,1082] | 25 |
| morceaux_hors_archive | 2000 | 2000 [0,9982 ; 1,0000] | 1916 | 179 [0,0774 ; 0,1029] | 30 |
| seuil_reel_classe_elargie | 1000 | 1000 [0,9963 ; 1,0000] | 952 | 95 [0,0775 ; 0,1149] | 8 |

Dans le banc de **l'auteur** (ses lots, dont 18 rejoués à l'identique), sur ses quatre cas obligatoires de 1 000 mondes : F1
promeut une copie exacte dans 93,6 % à 100 % des mondes ; F2 dans 31,8 % (intérieur), 20,3 % (bord), 9,6 % (morceaux sur
l'archive), 5,2 % (sommet). Sur ses cas en plus : F1 84,8 % à 100 %, F2 4,4 % à 42,8 %.

**Lecture.** L'échec est réel et n'est pas un défaut de son banc. La raison est celle de la preuve du nul limité, § 8 : pour une copie, le
rapport de la carte au nul appris est d'espérance au moins 1, et sa log-richesse est le regret du prédicteur. F1 échoue
partout. F2 échoue nettement dès que le nul a plusieurs paramètres libres ; quand le monde est une seule loi connue
(« poids extrêmes ») son taux retombe près de 5 %, chez lui (5,2 %) comme chez moi (5,0 %) : sur ce cas seul, aucun des deux bancs
ne sépare F2 du niveau nominal. Aucun rejet à tort.

## 6. (e) La puissance

### 6.1 Rejeu : ses chiffres se retrouvent

Les lots de puissance rejoués (un par dose et par taille d'entraînement, 9 lots) rendent ses valeurs à l'identique
(section 3). Les tables de sa section 7 sont celles de son résumé.

### 6.2 La comparaison est-elle loyale ?

- **Mêmes tirages** : oui. Un seul générateur par monde, tirages frais tirés avant l'entraînement ; toutes les méthodes lisent
  les mêmes 200 issues.
- **Mêmes instants** : oui pour BB_A, BB_T_seq, BB_T_coupe, BB_Q_blocs (huit instants). BB_S_moitie ne lit que quatre
  instants : c'est sa définition, l'auteur le dit.
- **Même seuil** : le v9 est lu à log(1/α), les méthodes à ensemble à log(1/(α − β)). Les deux tests ont le même niveau total
  α : c'est la comparaison loyale. Vérifié dans `essai_confiance_methodes_v1.juger`.
- **Même maximum certifié** : **non, et c'est le défaut.** Le « v9 du banc » rend un majorant certifié, donc valide, mais
  calculé par 80 pas d'un algorithme qui converge lentement. Le maximum sur 21 partitions prend le plus haut des majorants,
  souvent celui d'une partition mal convergée. Les bras à ensemble de confiance résolvent d'autres problèmes (tirages de confiance pondérés),
  qui convergent mieux, puis prennent le minimum : ils retrouvent une partie de ce que le « v9 du banc » a perdu par son
  optimiseur. Ce gain-là n'existe pas contre un v9 bien calculé (le vrai v9 vise 10⁻³ nat, `nul_v9.py`, `TOLERANCE_GROUPE`).

**Preuve par les fonctions de l'auteur elles-mêmes** (`attaque_confiance_ecart_certificat_v1.py`,
`sorties-attaque-v1/ecart-certificat-V1_0.50-r0000-0020-v1.json`). Sur ses 20 premiers mondes de dose 0,50, le dénominateur du
v9 est calculé de trois façons, sur les mêmes tirages : (a) comme son banc, `em_certifie`, 80 pas, départ chaud ; (b) la
même fonction, 5 000 pas ; (c) mon optimiseur.
- (b) et (c) donnent la même richesse à 0,0007 nat près : le vrai maximum est bien celui que je calcule.
- Le v9 promeut **9** mondes avec (a), **14** avec (b), **14** avec (c).
- L'écart de certificat de (a), pris à son pire instant : médiane 20,1 nat par monde, maximum 76,6 nat ;
  il dépasse 1 nat dans 95 % des mondes.

Même mesure à la dose 0,75 (20 mondes) : 12, 17 et 17 mondes promus ; écart de (b) à (c) au plus 0,0005 nat.

### 6.3 Rejeu serré : ses mondes, ses tirages, son ensemble, des maxima serrés

`attaque_confiance_rejeu_serre_v1.py` refait ses mondes de puissance (mêmes graines), calcule le seuil de son ensemble coupé
par son code, et calcule tous les maxima par mon optimiseur (écart de certificat au plus 0,0015 nat). « Grille de l'auteur » :
ses quatre valeurs de λ. Taux de promotion ; paires discordantes (ensemble coupé seul / v9 seul) ; part du prix du v9
regagnée, (coupé − v9) / (v8 − v9), avec intervalle à 95 % par rééchantillonnage des mondes.

| dose | tirages d'entraînement | mondes | calcul | v8 | limité | v9 | ensemble coupé, β = 0,01 | paires (coupé / v9) | part regagnée |
|---|---|---|---|---|---|---|---|---|---|
| 0,25 | 100 | 500 | banc de l'auteur | 0,330 | 0,264 | 0,120 | 0,110 | 2 / 7 | −5 % [−11 % ; 1 %] |
| 0,25 | 100 | 500 | **maxima serrés** | 0,396 | 0,360 | **0,288** | **0,280** | 0 / 4 | −7 % [−17 % ; −2 %] |
| 0,50 | 100 | 500 | banc de l'auteur | 0,728 | 0,650 | 0,424 | 0,448 | 16 / 4 | 8 % [2 % ; 13 %] |
| 0,50 | 100 | 500 | **maxima serrés** | 0,776 | 0,738 | **0,668** | **0,650** | 0 / 9 | −17 % [−31 % ; −7 %] |
| 0,75 | 100 | 500 | banc de l'auteur | 0,862 | 0,788 | 0,616 | 0,646 | 19 / 4 | 12 % [5 % ; 20 %] |
| 0,75 | 100 | 500 | **maxima serrés** | 0,910 | 0,890 | **0,850** | **0,844** | 0 / 3 | −10 % [−25 % ; 0 %] |
| 0,25 | 1000 | 200 | banc de l'auteur | 0,385 | 0,295 | 0,135 | 0,170 | 9 / 2 | 14 % [2 % ; 26 %] |
| 0,25 | 1000 | 200 | **maxima serrés** | 0,410 | 0,375 | **0,300** | **0,300** | 0 / 0 | 0 % [0 % ; 0 %] |
| 0,50 | 1000 | 200 | banc de l'auteur | 0,680 | 0,610 | 0,395 | 0,515 | 24 / 0 | 42 % [29 % ; 56 %] |
| 0,50 | 1000 | 200 | **maxima serrés** | 0,725 | 0,680 | **0,600** | **0,600** | 2 / 2 | 0 % [−18 % ; 16 %] |
| 0,75 | 1000 | 200 | banc de l'auteur | 0,840 | 0,790 | 0,630 | 0,745 | 24 / 1 | 55 % [38 % ; 70 %] |
| 0,75 | 1000 | 200 | **maxima serrés** | 0,890 | 0,865 | **0,820** | **0,815** | 0 / 1 | −7 % [−29 % ; 0 %] |
| 0,50 | 5000 | 60 | **maxima serrés** | 0,683 | 0,650 | **0,533** | **0,567** | 3 / 1 | 22 % [−25 % ; 60 %] |

Avec ma grille plus fine de λ (huit valeurs), les taux serrés sont les mêmes à un monde près (champ `coupe_grille_union` du
résumé). À β = 0,025 l'ensemble coupé fait moins bien qu'à β = 0,01, comme l'auteur le dit.

**Lecture.**
- Bien calculé, le v9 du banc a un taux de promotion de 0,600 à la dose 0,50 et de 0,820 à la dose 0,75 (1 000 tirages d'entraînement), et non 0,395 et 0,630. Sur ces 400 mondes,
  79 sont promus par le v9 serré et pas par le « v9 du banc », 0 dans l'autre sens.
- Le **prix du v9** sur ce banc (v8 moins v9) est de 12,5 et 7,0 points, et non 28,5 et 21,0. Il est du même ordre que
  celui de la validation du v9 (0,105 sur la ligne I02), pas deux à trois fois plus grand.
- Avec les 100 tirages d'entraînement du juge, l'ensemble coupé **perd** contre le v9 serré : paires 0 / 4, 0 / 9, 0 / 3 aux trois doses (il annonçait 2 / 7, 16 / 4 et 19 / 4). C'est le prix β, sans contrepartie.
- Avec 1 000 tirages d'entraînement, l'ensemble coupé **ne regagne rien** : paires 2 / 2 et 0 / 1 (il annonçait 24 / 0 et 24 / 1).
  L'ensemble ne change la richesse que dans 26 % et 22 % des mondes (gain médian 0 nat), et le seuil plus haut coûte le reste.
- Des 48 mondes « gagnés » par son ensemble coupé contre son v9, 46 sont promus aussi par le v9 serré.

**Sonde à 5 000 tirages d'entraînement** (2 500 pour l'ensemble ; 60 de ses mondes de dose 0,50, peu de mondes, exploratoire) :
v9 32/60, ensemble coupé 34/60, paires 3 / 1. L'ensemble mord enfin (richesse changée dans 77 % des
mondes), mais de peu : gain médian 0,42 nat, quartile haut 0,99 nat, quand il faut environ 3 nats pour passer le seuil.

### 6.4 Mes mondes (banc indépendant, maxima serrés)

Ligne V1 du préenregistrement (effet neuf global), carte = loi du monde. Taux de promotion (β = 0,01) ; entre parenthèses, les
paires discordantes contre le v9 (méthode seule / v9 seul).

| dose | tirages d'entraînement | mondes | v8 | limité | v9 | BB_A | BB_T_seq | BB_T_coupe | BB_S_moitie | BB_Q_blocs |
|---|---|---|---|---|---|---|---|---|---|---|
| 0,25 | 100 | 100 | 0,390 | 0,370 | 0,310 | 0,290 (0 / 2) | 0,290 (0 / 2) | 0,290 (0 / 2) | 0,130 (0 / 18) | 0,040 (0 / 27) |
| 0,50 | 100 | 100 | 0,700 | 0,650 | 0,610 | 0,600 (0 / 1) | 0,600 (0 / 1) | 0,600 (0 / 1) | 0,350 (1 / 27) | 0,200 (0 / 41) |
| 0,75 | 100 | 100 | 0,910 | 0,890 | 0,850 | 0,850 (0 / 0) | 0,850 (0 / 0) | 0,850 (0 / 0) | 0,670 (0 / 18) | 0,530 (0 / 32) |
| 0,50 | 1000 | 100 | 0,700 | 0,650 | 0,610 |  | 0,610 (0 / 0) | 0,610 (0 / 0) |  |  |
| 0,75 | 1000 | 100 | 0,910 | 0,890 | 0,850 |  | 0,850 (0 / 0) | 0,850 (0 / 0) |  |  |
| 0,50 | 5000 | 40 | 0,500 | 0,475 | 0,450 |  |  | 0,450 (0 / 0) |  |  |
| 0,75 | 5000 | 40 | 0,950 | 0,950 | 0,950 |  |  | 0,950 (0 / 0) |  |  |

**Lecture.**
- BB_A ne promeut jamais un monde que le v9 ne promeut pas (lemme 1) : confirmé.
- BB_T_seq et BB_T_coupe : aucun gain, ni à 100 ni à 1 000 tirages d'entraînement ; ils perdent parfois le prix β.
- BB_S_moitie et BB_Q_blocs perdent beaucoup, comme l'auteur le dit ; à maxima serrés la perte est plus grande que dans
  son banc (BB_Q_blocs : 0 monde gagné contre 100 perdus sur 300).
- Le jeu entre mon majorant et le meilleur point trouvé dans l'ensemble est petit. À 1 000 tirages, pour l'ensemble coupé : médiane 0,25 nat, et si l'on ajoutait tout ce jeu à la richesse le taux serait 62/100 au lieu de 61/100 (dose 0,50) ; médiane 0,25 nat, et si l'on ajoutait tout ce jeu à la richesse le taux serait 87/100 au lieu de 85/100 (dose 0,75). Une grille de λ plus fine ne changerait donc presque rien.

- Sonde à 5 000 tirages, dose 0,50 (40 mondes) : v9 18/40, ensemble coupé 18/40 (0 / 0) ; gain médian de richesse 0,18 nat.
- Sonde à 5 000 tirages, dose 0,75 (40 mondes) : v9 38/40, ensemble coupé 38/40 (0 / 0) ; gain médian de richesse 0,28 nat.

### 6.5 Ce que cela veut dire pour la correction

L'ensemble de confiance est une façon **valide** d'apprendre les poids, mais il ne mord pas aux tailles du juge. Son rayon
(regret du prédicteur plus log(1/β), une dizaine de nats sur les tirages de confiance) laisse passer le maximum de
vraisemblance des 200 tirages frais tant que les tirages de confiance ne sont pas des milliers. Ordre de grandeur (compte
heuristique, non démontré) : le surajustement permis dans l'ensemble décroît comme la racine de (tirages frais / tirages
de confiance) ; pour le ramener à 1 nat il faudrait de l'ordre de 25 000 tirages de confiance par monde. La sonde à 5 000
va dans ce sens (l'ensemble mord, de moins de 1 nat en médiane).

## 7. Réserves

**R1 — Une carte membre du nul peut être promue quand le monde est hors du nul.** Sous le v9, une carte qui est un membre
du nul a une richesse au plus 1, quel que soit le monde : elle n'est jamais promue. Sous une méthode à ensemble de
confiance, elle peut l'être si elle est hors de l'ensemble et bat tout l'ensemble sur les tirages frais. Le théorème ne
l'interdit pas : il ne parle que des mondes du nul. Or l'organisme travaille dans des mondes qui portent une vraie
composante, donc hors du nul.
- *Calcul exact* (`exactm-C-*.json`). Nul = deux lois connues sans leurs mélanges (probabilités 0,3 et 0,7). Monde hors du
  nul (0,5), carte = copie exacte de la loi 0,7. Le v9 : **0**. L'ensemble coupé : **6,9 %** avec 100 tirages de
  confiance, **13,8 %** avec 1 000. Monde 0,45, même carte : 8,9 % et 23,9 %. Carte 0,3 dans le monde 0,5 : 8,7 % et
  12,9 %. C'est au-dessus de 5 %, et cela croît avec le nombre de tirages de confiance : plus l'ensemble est serré, plus
  il exclut l'une des deux lois.

- *Dans mon banc.* Monde = recollage de S1 et S2 sur une coupure oblique (z₀ + z₁ > 0), hors du nul du banc. Cartes
  membres du nul : recollage sur z₀ > 0, sur z₁ > 0, copie de S1, meilleur membre ajusté sur 1 000 tirages à part.

  | tirages d'entraînement | mondes | méthode | cartes membres promues (z₀ ; z₁ ; S1 ; ajusté) | cartes membres de richesse > 1 |
  |---|---|---|---|---|
  | 100 | 200 | v9 | 0 ; 0 ; 0 ; 0 | 0 ; 0 ; 0 ; 0 |
  | 100 | 200 | BB_T_seq | 0 ; 0 ; 0 ; 0 | 0 ; 0 ; 0 ; 0 |
  | 100 | 200 | BB_T_coupe | 0 ; 0 ; 0 ; 0 | 1 ; 0 ; 0 ; 0 |
  | 1000 | 150 | v9 | 0 ; 0 ; 0 ; 0 | 0 ; 0 ; 0 ; 0 |
  | 1000 | 150 | BB_T_seq | 1 ; 0 ; 0 ; 1 | 7 ; 2 ; 1 ; 1 |
  | 1000 | 150 | BB_T_coupe | 1 ; 0 ; 1 ; 1 | 15 ; 7 ; 1 ; 4 |
  | 5000 | 40 | v9 | 0 ; 0 ; 0 ; 0 | 0 ; 0 ; 0 ; 0 |
  | 5000 | 40 | BB_T_coupe | 0 ; 0 ; 0 ; 0 | 4 ; 5 ; 1 ; 1 |

  Sous le v9 : aucune carte membre promue, aucune de richesse supérieure à 1 (c'est la règle d'audit A1). Sous les méthodes à
  ensemble : au pire 1/150 carte membre promue (membre_coupe_z0, BB_T_seq, 1 000 tirages), et des richesses supérieures à 1 dès 1 000 tirages. Dans mon banc
  l'effet est rare, parce que l'ensemble mord peu ; il grandirait avec l'ensemble, donc dans le régime même où la méthode
  deviendrait utile. La règle d'audit A1 (« une carte membre promue = défaut de code ») ne vaudrait plus que dans les mondes
  du nul.

  Dans les mondes V1 (effet neuf global), cartes « copie de S1 » et « membre ajusté » : 0 promotion, toutes méthodes à ensemble, toutes doses et toutes tailles confondues (100, 100, 100, 40, 100, 100, 40 mondes selon le cas).

**R2 — Le banc de l'auteur ne montre pas la taille « sur toute la classe du v9 ».** Son « v9 du banc » n'a que neuf coupures
par trait ; le vrai v9 couvre tout seuil réel. L'auteur le déclare (« le banc n'est pas le juge »), mais sa tête de note dit
« sur toute la classe du v9 ».
Mesure, dans mon banc à neuf coupures : une copie par morceaux sur un seuil hors de la grille est promue par le v9 du
banc dans 66/150 mondes et par l'ensemble coupé dans 60/150. Ce n'est pas un défaut des méthodes : c'est la classe du banc qui est
trop petite. Quand la classe contient le seuil (cas `seuil_reel_classe_elargie`, 1000 mondes) : 0 copie promue.

Pour le vrai v9, le maximum sur l'ensemble doit parcourir toutes les coupures qui séparent les tirages frais **et** les
tirages de confiance (voir R3). Ce calcul n'est fait ni par l'auteur ni par moi.

**R3 — Le coût annoncé pour le vrai v9 est sous-estimé** (compte, non mesuré). L'auteur écrit « environ quatre fois le coût
du v9 pour quatre valeurs de λ ». Sur le vrai v9, toute coupure réelle compte : à l'instant t il y a t + 1 coupures par
trait, chacune un problème à t tirages. Avec un ensemble de confiance, deux coupures qui séparent pareil les tirages frais
mais pas les tirages de confiance ne sont plus le même problème : il y a t + n_c + 1 coupures par trait, chacune à t + n_c
tirages. Si le coût suit le produit (coupures × tirages), le rapport par valeur de λ, sommé sur les huit instants, est
d'environ 3 pour n_c = 100, 24 pour n_c = 500 et 78 pour n_c = 1 000 ; avec quatre valeurs de λ : 12, 95 et 310 fois le
coût du v9, avant tout élagage. Le banc de l'auteur ne le voit pas, parce que sa grille de neuf coupures est fixe.

**R4 — La forme pour la règle e-BH** (section 9.2 de l'auteur) : il a raison, la méthode rend un test et non une valeur e.
Sa valeur p, min(1, β + 1/W), est valide (vérifié à la main : pour u > β, P(β + 1/W ≤ u) ≤ β + (u − β)). Rien de mesuré,
ni par lui ni par moi.

## 8. Verdict par méthode

**BB_A_memes_tirages — tient (validité).** Preuve juste (théorème, lemme 1). Mon attaque : copie exacte promue, 0 sur 15 000 mondes × 2 β ; pire carte : 11/1000 (borne haute 0,0196, seuil_reel_classe_elargie, pari_debut) ; non-couverture au pire 14/2000 à β = 0,025. Puissance : jamais un
monde de plus que le v9, par construction ; mes mondes, 100 tirages : 0,290 contre 0,310 (0 / 2) ; 0,600 contre 0,610 (0 / 1) ; 0,850 contre 0,850 (0 / 0). L'auteur l'écarte à raison.

**BB_T_seq — tient (validité) ; le gain annoncé ne tient pas.** Preuve juste. Mon attaque : copie exacte promue, 0 sur 15 000 mondes × 2 β ; pire carte : 11/1000 (borne haute 0,0196, seuil_reel_classe_elargie, pari_debut) ; non-couverture au pire 2/2000 à β = 0,01. Puissance, mes mondes
(doses 0,25, 0,50, 0,75, méthode contre v9, paires) : à 100 tirages, 0,290 contre 0,310 (0 / 2) ; 0,600 contre 0,610 (0 / 1) ; 0,850 contre 0,850 (0 / 0) ; à 1 000 tirages, 0,610 contre 0,610 (0 / 0) ; 0,850 contre 0,850 (0 / 0). L'auteur
annonçait à 1 000 tirages 0,160 / 0,445 / 0,725 contre 0,135 / 0,395 / 0,630 : cet écart vient du v9 mal calculé de son banc.

**BB_T_coupe — tient (validité) ; le gain annoncé ne tient pas.** Preuve juste. Mon attaque : copie exacte promue, 0 sur 15 000 mondes × 2 β ; pire carte : 11/1000 (borne haute 0,0196, seuil_reel_classe_elargie, pari_debut) ; non-couverture au pire 13/2000 à β = 0,025. Puissance : sur les
mondes de l'auteur, à maxima serrés, ensemble coupé contre v9 : à 100 tirages, 0,280 contre 0,288 ; 0,650 contre 0,668 ; 0,844 contre 0,850 aux trois doses ; à 1 000 tirages, 0,600 contre 0,600 (dose 0,50) et 0,815 contre 0,820 (dose 0,75) ;
sur mes mondes, à 1 000 tirages, 0,610 contre 0,610 (0 / 0) ; 0,850 contre 0,850 (0 / 0). « Regagne 14 %, 42 %, 55 % du prix » : non retrouvé. Ce n'est pas « la seule
voie qui regagne une part du prix » : aux tailles essayées (100, 1 000, 5 000) elle n'en regagne pas. Réserve R1.

**BB_S_moitie — tient (validité).** Preuve juste. Mon attaque : copie exacte promue, 0 sur 15 000 mondes × 2 β ; pire carte : 18/2000 (borne haute 0,0142, morceaux_archive, pari_milieu) ; non-couverture au pire 6/2000 à β = 0,025. Puissance : perd, comme annoncé ; mes mondes, 100
tirages : 0,130 contre 0,310 (0 / 18) ; 0,350 contre 0,610 (1 / 27) ; 0,670 contre 0,850 (0 / 18).

**BB_Q_blocs — tient (validité).** Preuve juste. Mon attaque : copie exacte promue, 0 sur 15 000 mondes × 2 β ; pire carte : 3/1000 (borne haute 0,0087, seuil_reel_classe_elargie, pari_debut) ; non-couverture au pire 10/2000 à β = 0,025. Puissance : perd, comme annoncé, et davantage à maxima
serrés ; mes mondes, 100 tirages : 0,040 contre 0,310 (0 / 27) ; 0,200 contre 0,610 (0 / 41) ; 0,530 contre 0,850 (0 / 32).

**F1_en_ligne — ne tient pas (non valide, comme le dit l'auteur).** Échec réel : copie exacte promue dans 80,3 % à 100,0 % de
mes mondes, 84,8 % à 100 % des siens. Contre-exemple : toute copie exacte d'un membre du nul.

**F2_moitie — ne tient pas (non valide, comme le dit l'auteur).** Échec réel : copie exacte promue dans 5,0 % à 48,8 % de mes
mondes, 4,4 % à 42,8 % des siens. Au sommet (une seule loi connue), aucun des deux bancs ne la sépare
du niveau nominal ; le calcul exact sur le nul jouet la met juste au-dessus de 5 %.

## 9. Déclarations et écarts de procédure

- **Raccourci du mode « taille »** (dit en tête de `attaque_confiance_v1.py`) : le maximum contraint n'est calculé que dans
  les mondes où une promotion est possible (monde hors de l'ensemble, ou rapport de vraisemblance d'une carte au-dessus du
  seuil), et dans un monde sur vingt fixé d'avance (audit). Ailleurs la promotion est impossible pour tout majorant
  valide ; la couverture et le rapport de vraisemblance y sont calculés exactement. L'audit vérifie la seule chose que le
  raccourci suppose : le majorant domine la log-vraisemblance du monde quand le monde est couvert.
- **Réglages faits sur des mondes d'essai, avant les lots gardés** (mondes 0 à 90 de quelques cas, relancés ensuite dans les
  lots) : (a) l'algorithme lent du premier jet a été remplacé par des points intérieurs quand j'ai vu son écart de
  certificat (jusqu'à 70 nats) ; (b) les cartes « pari » ont été refaites (rang médian, cibles 30 et 150) parce que la
  première version ne gagnait presque jamais ses paris ; (c) l'audit est passé d'un monde sur cinq à un sur vingt, pour le
  temps. Aucun de ces réglages ne dépend d'une issue des méthodes jugées.
- **Processus arrêtés par leur numéro** (R10), tous à moi : trois processus de rejeu dont le dossier de travail avait
  disparu du dossier temporaire partagé (rejeu relancé dans un dossier au nom propre, rien de perdu) ; la première campagne
  (dix processus) au bout de sept minutes, parce que ses lots de 500 mondes auraient dépassé dix minutes sous la charge ;
  un calcul exact qui ne pouvait pas finir à temps (deux processus) ; deux lanceurs arrivés, en fin de liste, sur ce même
  calcul exact déjà abandonné (six processus).
- **Limite de dix minutes atteinte** : un essai du mode `exact` entier a duré 590 s (non gardé) ; les parties `exact A2`
  (une fois) et `exact BC` (deux fois) ont été coupées à 600 s, sans sortie ; le script de certificat de l'auteur a été coupé
  à 600 s, sans sortie. Les calculs exacts ont été refaits par morceaux (`attaque_confiance_exact_morceaux_v1.py`, même
  fonction, importée telle quelle) ; la partie « puissance sur le nul jouet » n'a pas été refaite et n'est pas citée.
- **Lots lancés deux fois** : quatre lots de taille ont été lancés par deux files à la fois ; le second a été refusé par la
  garde « jamais d'écrasement », sans effet. Tous les lots gardés ont duré moins de dix minutes (au plus 439 s).
- **Sondes ajoutées en cours de route** (5 000 tirages d'entraînement ; écart de certificat du banc) : décidées après avoir vu
  que l'ensemble ne mordait pas à 1 000 tirages. Exploratoires, peu de mondes, dites comme telles.
- **Priorité** : la première campagne tournait en priorité basse ; trois processus ont été remis en priorité normale, comme
  les autres travaux de la machine, puis toute la suite a tourné en priorité normale.
- **Mondes réduits, faute de temps** : dits dans chaque table (colonne « mondes »).
- **Mes bancs ne sont pas le juge** : mêmes simplifications que celles que l'auteur déclare (neuf coupures par trait au lieu
  de toutes, pas de membres log-linéaires), plus les miennes (une ou deux lois « si_sinon » dans l'archive, cartes « pari »
  qui ne sont pas dans la grammaire du juge). Les chiffres valent pour ces bancs.
- Aucun fichier de l'auteur n'a été modifié. Aucun fichier des dossiers de copie n'a été exécuté ni importé. Aucune
  recherche dans `docs/verdicts/`. Rien lu sous `diag/` ni `donnees/`.

## 10. Fichiers du réfutateur (même dossier, tous scellés par un compagnon `.sha256`)

| fichier | rôle | sha256 |
|---|---|---|
| `attaque_confiance_v1.py` | programme d'attaque (modes taille, hors_nul, exact, certificat) | `7bb1f318a1fb071bc1c861eb04a577ecfb064dd8330d5e78a39f9c84a1de5e3d` |
| `attaque_confiance_rejeu_serre_v1.py` | rejeu serré : mondes de l'auteur, maxima serrés | `b5313ee41728a47006ec2d14149edface82bf0403c45662108c0bc058e896477` |
| `attaque_confiance_ecart_certificat_v1.py` | écart de certificat du « v9 du banc », par les fonctions de l'auteur | `8e37aa9d4bdaabca5889755eba5e6dc8aa291b506b827a06d134265af89333a6` |
| `attaque_confiance_exact_morceaux_v1.py` | calcul exact par morceaux | `c160dc2345aaa6d68becca1ec02fcb59828b1fdea0248571951f435b0006978e` |
| `attaque_confiance_sonde_v1.py` | sonde à 5 000 tirages d'entraînement | `b36aa59c7f2f91e9addbe97bd34313f996c71d76ad8c196fdb00be5aed8050db` |
| `attaque_confiance_resume_v1.py` | résumé des lots | `660ed4154cb692810e4c3f75249aa7659dfe16447aea09db4ba6055045856728` |
| `attaque-confiance-v1.json` | **sortie** : résumé de tous les lots, avec l'empreinte de chacun (champ `sources`) | `d94573fcc19775a4feb2d36f1b0eea149f9940b93da439abb3681c59d9313e02` |
| `rejeu-v1/compare_rejeu_v1.py` | comparaison des 18 lots rejoués aux lots de l'auteur | `7638c4099c4cff836ec17c54c91ad3dfc85ad6c6f27c4b5be84bdeaca3473bd0` |
| `rejeu-v1/comparaison-rejeu-v1.json` | sa sortie (aussi recopiée dans le résumé) | `dc49b4eb6d6b5de957ca56eb1b2a1885ea184cb2a771227950f1b937f9e739dd` |
| `rejeu-v1/rejeu_certificat_partiel_v1.py` | rejeu partiel du script de certificat de l'auteur | `ff426eaf31dd577c82586258c57e3486f4d09f54c04d13edf8b368dd75b13a6b` |
| `rejeu-v1/rejeu-certificat-partiel-v1.json` | sa sortie | `ee89d6a015cf86294048b1a4c66af7bf2ecedeab38a84c1bd905afe3dfd1ba95` |
| `sorties-attaque-v1/` | 166 lots (85 de taille, 40 hors du nul, 28 de rejeu serré, 2 d'écart de certificat, 10 de calcul exact, 1 de certificat) | une empreinte par lot : compagnon `.sha256` et champ `sources` du résumé |

La note elle-même a son empreinte dans son compagnon `refutation-confiance-v1.md.sha256`. Les lots rejoués de l'auteur ne sont
pas gardés (ils sont égaux aux siens) ; leur comparaison l'est. Tous les chiffres des sections 0 et 4 à 8 viennent de
`attaque-confiance-v1.json`.

## 11. Références (toutes « à vérifier sur pièce » ; aucun chiffre n'en est repris)

- R. L. Berger et D. D. Boos, 1994 (maximum sur un ensemble de confiance du paramètre de nuisance) ; à vérifier sur pièce.
- L. Wasserman, A. Ramdas, S. Balakrishnan, « Universal inference », 2020 ; à vérifier sur pièce.
- J. Ville, 1939 (inégalité pour les surmartingales positives) ; à vérifier sur pièce.
