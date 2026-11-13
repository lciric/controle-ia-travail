# Addendum 5 au préenregistrement du témoin de Bailey (`prereg/temoin-attaque-publiee-bailey-v1.md`, `fb6c2f34…`) — relance de la liste d'arrêt jouée par une conduite neuve (code v18) — brouillon 1

13 novembre 2026. Session « attaquant informé » (`session_01XJ6MgnEhQMZteN9F8a1BST`), branche
`claude/compassionate-meitner-d4ryyk`. **Brouillon 1 : non contre-lu (R2), non scellé.** Le préenregistrement et ses
addenda 1 à 4 restent tels quels ; en cas de conflit, le préenregistrement prime et l'écart est un nœud. Cet addendum ne
contient aucun résultat : aucune note de la boucle n'a été lue ; les notes de la première exécution du run principal sont
scellées sans lecture.

## 1. Pourquoi
Troisième série (addendum 4, `89d2f647…`) : pilote fini (3 tours, aucune garde tombée) ; règle K = 72 ; run principal
lancé le 13 novembre à 00:52:59Z sur l'instance 60417353. **Interruption** pendant le tour 8 (vers 04:21Z) : le compte
Vast n'avait plus de crédit (`credit` 0, `balance` −0,93 USD ; mot de Lazar « plus de credits sur vast ») ; Vast a arrêté
l'instance ; la conduite l'a déclarée injoignable et ne l'a pas détruite (aucun transfert ne faisait foi). Reprise
(lecture 38 de l'addendum 2) après le crédit du compte par Lazar : transfert complet, empreintes comparées et scellées
(`runs/temoin-bailey-v1-20261111/sortie-conduite-v11/reprise-v10-2/`), instance détruite. Champs techniques seulement :
**K′ = 8 tours complets** (journal des durées, tours 0 à 7) ; toutes les gardes passées. Notes :
`registres/passations/2026-11-13-0548-…`, `…-0610-…`, `…-0731-…-cause-credit-vast-epuise.md` (`f6e09ff5…`),
`…-0803-…-k-prime-8-noeud-relance.md` (`ab372ed1…`).

Issue de la liste d'arrêt (texte l. 338, 371) : interruption pendant le tour e₀ = 8, K′ = 8 < 20 : **une seule relance
entière**, même graine, dossiers neufs, K recalculé par la même règle sur le budget restant (même B, t du pilote), si ce
K est ≥ 20 ; seule la relance porte le verdict ; les notes de la première exécution restent scellées sans lecture jusqu'à
la fin de la relance et le scellement de ses journaux. Décision de Lazar : « go (a), vérifie le chemin de code de la
relance » (`registres/passations/2026-11-13-HHMM-decision-lazar-bailey-relance-a.md`, `@@`).

## 2. Écart de mise en œuvre (pas de fond) : la relance jouée par une conduite neuve
Le code scellé (`lanceur_v17`, addendum 4) ne joue la relance que dans la conduite du run principal, sur la même
instance, juste après lui. L'instance de la série 3 est détruite et sa conduite finie : la relance demande une conduite
neuve sur une instance neuve. Le code v18 (`lanceur_v18`) l'ajoute, sans rien changer d'autre :
1. **Relance seule.** Même chemin que la conduite scellée jusqu'au contrôle du juge compris (création, auto-arrêt,
   amorce, mise en place, contrôle du juge, sur l'instance neuve : ses gardes s'appliquent, et leur chute arrête avant la
   relance) ; puis, **sans pilote ni règle sur l'instance**, K = `analyse_v3.nombre_de_tours(B, D, c, t)` avec B = 75,
   D = dépense du poste au moment du calcul (toutes les instances du poste, dont les sept antérieures), c = taux de
   l'instance neuve, **t = t du pilote de la série 3** (1 315,9926 s, manifeste de la règle transféré par la reprise) ;
   K < 20 : arrêt, pas de verdict, nœud ; sinon manifeste « relance » (`regle_tours` : K, D, c, `relance: true`,
   `premiere_execution` : la règle de la série 3) et exécution `principal-relance`, graine du run principal (1865327867),
   dossiers neufs. C'est le calcul de la relance de `lanceur_v17` (l. 1716-1726 : `self.poste.depense`, `self.c`, t de la
   règle), avec le c de l'instance neuve.
2. **Gardes d'entrée** (avant toute création, aucune dépense si l'une tombe) : K′ entier, 0 ≤ K′ < 20 ; règle de la
   première exécution complète ; t > 0. La conduite de lancement (`lancer-conduite-v12.py`) vérifie en outre les
   empreintes du manifeste de la règle et du journal des durées de la reprise, et exactement les tours 0 à 7.
3. **Assemblage pour la lecture** (`assembler_lecture`) : un dossier neuf qui réunit les transferts de la série 3 (mise
   en place, contrôle du juge, pilote, règle, principal, manifestes) et ceux de la relance (`principal-relance`,
   manifeste « relance ») ; la mise en place et le contrôle du juge de l'instance de la relance y sont copiés à part et
   doivent avoir passé toutes leurs gardes ; toutes les empreintes copiées sont vérifiées ; le manifeste de relance doit
   citer la règle de la série 3, mêmes graines, même code public. `lecture_v8.valider` et `lire` (inchangés) lisent ce
   dossier comme une conduite unique : la première exécution comme interrompue (K′ = 8), la relance comme portant le
   verdict. Aucune note n'est lue par l'assemblage.

Ce qui rend l'écart compatible avec l'objet de R3 : la relance est celle du texte ; aucune note de la première exécution
n'a été lue ; la règle de K est celle du texte ; la graine est celle du texte.

## 3. Code, essais, contre-lecture
Commit du code : `@@`. Seul change, par rapport à l'addendum 4 :

| Rôle | Module | SHA-256 |
|---|---|---|
| Lanceur local | `lanceur_v18.py` | `@@` |

Instance (`instance_v16`), exécution (`execution_v4`), lecture (`lecture_v8`), journaliseur, conventions, analyse :
inchangés ; l'archive envoyée sur l'instance est la même liste de fichiers. Manifeste neuf (R12) :
`manifeste-local-v6.json` (`@@`), seule différence avec le v5 : `commit_code`.

Essais (R5) : `tests/test_temoin_bailey_condition6_v18.py` (`@@`) : les essais v17 rejoués sur `lanceur_v18` ; plus :
relance seule de bout en bout (première conduite interrompue à 3 tours, relance seule par une conduite neuve, K = 22 par
la règle, assemblage, `valider` : K′ = 22, première exécution interrompue à 3, `lire` : verdict au régime réduit K = 22) ;
artefacts : gardes d'entrée (K′ = 20, booléen, négatif, t nul, règle incomplète : aucune création), K de relance < 20
(arrêt, aucune relance), contrôle du juge hors seuil (arrêt avant la relance), assemblage refusé (cible présente, relance
déjà présente, mise en place de la relance tombée, fichier scellé altéré, manifeste qui ne cite pas la règle) ; un mutant
(t divisé par deux) fait tomber les essais visés. Résultat : @@.

Contre-lecture du code (R2) : `docs/notes/reproduction-attaque-publiee-v1/relecture-code-condition6-v18-relance-seule-bailey-v1.md`
(`@@`).

Pièces de lancement : `lancer-conduite-v12.py` (`@@`), poste `poste-hetzner-v12.sh` et constructeur
`construire-donnees-demarrage-v12.py` (`@@`).

## 4. Ce qui ne change pas
Hypothèse, prédictions, métriques, seuils, population, juge, modèle, bras, graines, B, critères de lecture gelés, liste
d'arrêt, lectures actées. Une seconde erreur avant 20 tours complets de la relance : arrêt, pas de verdict, nœud (texte
l. 371). La relance est la seule ; aucune autre série sans nouvelle décision et nouvel addendum.

## 5. Risques déclarés
Ceux des addenda 2 à 4, gardés. En plus :
- (a) **crédit du compte Vast** : une relance coupée faute de crédit est une seconde erreur (arrêt, pas de verdict) ; la
  session relève le crédit avant la création et ne lance pas si le crédit ne couvre pas la dépense attendue (≈ 26 h au
  taux de l'offre, plus la mise en place) ; la garde de dépense du texte (D ≥ B − 2) ne protège pas contre un compte vide ;
- (b) la mise en place de l'instance neuve refait le contrôle du juge sous la graine du pilote (garde de mise en place) :
  il produit des réponses et des notes du juge, comme à chaque série ; ce n'est pas une lecture ;
- (c) le pilote n'est pas rejoué : t est celui de la série 3 ; si l'instance neuve est plus lente, la relance peut dépasser
  le budget : la garde de dépense l'arrête (run tronqué, lu sur K′ ≥ 20 s'il est atteint) ;
- (d) l'assemblage est un code neuf de lecture ; il ne lit aucune note ; s'il refuse, le verdict n'est pas prononcé : nœud.

## 6. Conditions de lancement
1 à 6 : comme à l'addendum 4 (condition 6 : cet addendum, scellé, pour la relance). 7 : le mot de Lazar « go (a), vérifie
le chemin de code de la relance », pour la seule relance. 8 : poste Hetzner autonome neuf (v12). En plus : crédit Vast
relevé et suffisant (risque (a)). Aucune instance avant le scellement de cet addendum.

## Contre-lecture
À venir (R2).
