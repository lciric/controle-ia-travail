# Addendum 5 au préenregistrement du témoin de Bailey (`prereg/temoin-attaque-publiee-bailey-v1.md`, `fb6c2f34…`) — relance de la liste d'arrêt jouée par une conduite neuve (code v18)

13 novembre 2026, scellé après contre-lecture (R2). Session « attaquant informé » (`session_01XJ6MgnEhQMZteN9F8a1BST`),
branche `claude/compassionate-meitner-d4ryyk`. Brouillons archivés tels quels (R12) : brouillon 1
(`brouillons/temoin-attaque-publiee-bailey-v1-addendum-5-relance-seule-brouillon1.md`, `600dd0a9…`, écrit pour le code
v18) ; brouillon 2 (`…-brouillon2.md`, contre-lu). Le préenregistrement et ses
addenda 1 à 4 restent tels quels ; en cas de conflit, le préenregistrement prime et l'écart est un nœud. Cet addendum ne
contient aucun résultat : aucune note de la boucle n'a été lue ; les notes de la première exécution du run principal sont
scellées sans lecture.

## 1. Pourquoi
Troisième série (addendum 4, `89d2f647…`) : pilote fini (3 tours, aucune garde tombée) ; règle K = 72 ; run principal
lancé le 13 novembre à 00:52:59Z sur l'instance 60417353. **Interruption** pendant le tour 8 (vers 04:21Z) : le compte
Vast n'avait plus de crédit (`credit` 0, `balance` −0,93 USD ; mot de Lazar « plus de credits sur vast ») ; Vast a arrêté
l'instance (cause la plus probable, note 0731 ; non établie autrement) ; la conduite l'a déclarée injoignable et ne l'a pas détruite (aucun transfert ne faisait foi). Reprise
(lecture 38 de l'addendum 2) après le crédit du compte par Lazar : transfert complet, empreintes comparées et scellées
(`runs/temoin-bailey-v1-20261111/sortie-conduite-v11/reprise-v10-2/`), instance détruite. Champs techniques seulement :
**K′ = 8 tours complets** (journal des durées, tours 0 à 7) ; toutes les gardes passées. Notes :
`registres/passations/2026-11-13-0548-…` (`b797cb97…`), `…-0610-…` (`01ff293b…`),
`…-0731-…-cause-credit-vast-epuise.md` (`f6e09ff5…`), `…-0803-…-k-prime-8-noeud-relance.md` (`ab372ed1…`). Pièces de la
reprise : bilan `bilan-reprise-v10.json` (`085f5c1c…`) ; manifeste de la règle `manifeste-v3-regle.json`
(`2e8b7837dc49ebb60b36781541c2ada6147f06694c18e2e525783d2ccbe6360a`) ; journal des durées
`principal/transfert-1/sortie-durees-v3.jsonl` (`9ff59e4beb8e8d4461bff18e157751f9464f6022d95b04b0b88904eccdb671f4`) ;
journaux de gardes `principal/transfert-1/journal/gardes-v3.jsonl` (`4acfddd3…`) et `…/gardes-lanceur-v3.jsonl`
(`bc474c4d…`).

Classement : interruption pendant le tour e₀ = 8 (l. 338), lue comme une coupure de l'hôte (l. 371 : instance arrêtée
par le fournisseur, processus tué) ; lecture de la session, présentée à Lazar (notes 0548, 0803) et couverte par sa
décision ; à la lecture, l'état absent est reconstitué avec un code de sortie non nul
(`lecture_v8.etat_reconstitue_lecture`), ce qui permet la relance (`relance_permise`).

Issue de la liste d'arrêt (texte l. 338, 371) : interruption pendant le tour e₀ = 8, K′ = 8 < 20 : **une seule relance
entière**, même graine, dossiers neufs, K recalculé par la même règle sur le budget restant (même B, t du pilote), si ce
K est ≥ 20 ; seule la relance porte le verdict ; les notes de la première exécution restent scellées sans lecture jusqu'à
la fin de la relance et le scellement de ses journaux. Décision de Lazar : « go (a), vérifie le chemin de code de la
relance » (`registres/passations/2026-11-13-0821-decision-lazar-bailey-relance-a.md`, `357f18b9…`).

## 2. Écart de mise en œuvre (pas de fond) : la relance jouée par une conduite neuve
Le code scellé (`lanceur_v17`, addendum 4) ne joue la relance que dans la conduite du run principal, sur la même
instance, juste après lui. L'instance de la série 3 est détruite et sa conduite finie : la relance demande une conduite
neuve sur une instance neuve. Le code v20 (`lanceur_v20` ; v18, puis v19 et v20 corrigées par leurs contre-lectures) l'ajoute, sans rien
changer d'autre :
1. **Relance seule.** Même chemin que la conduite scellée jusqu'au contrôle du juge compris (création, auto-arrêt,
   amorce, mise en place, contrôle du juge, sur l'instance neuve : ses gardes s'appliquent, et leur chute arrête avant la
   relance) ; puis, **sans pilote ni règle sur l'instance**, K = `analyse_v3.nombre_de_tours(B, D, c, t)` avec B = 75,
   D = dépense du poste au moment du calcul (toutes les instances du poste, dont les sept antérieures), c = taux de
   l'instance neuve, **t = t du pilote de la série 3** (1 315,9926 s, manifeste de la règle transféré par la reprise) ;
   K < 20 : arrêt, pas de verdict, nœud ; sinon manifeste « relance » (`regle_tours` : K, D, c, H, `relance: true`,
   `premiere_execution` : la règle de la série 3) et exécution `principal-relance`, graine du run principal (1865327867),
   dossiers neufs. C'est le calcul de la relance de `lanceur_v17` (l. 1717-1726 : `self.poste.depense`, `self.c`, t de la
   règle), avec le c de l'instance neuve et H recalculé (C-3 de la relecture v18).
2. **Gardes d'entrée** (avant toute création et tout dossier de sortie, aucune dépense si l'une tombe) : K′ entier,
   0 ≤ K′ < 20 ; règle de la première exécution complète, B égal au B du manifeste, K de la première ≥ 20, t > 0 ; règle
   égale à celle du manifeste scellé de la règle de la première (empreinte vérifiée) ; instance de la première
   exécution (60417353) parmi les antérieures, avec le taux de la règle ; toute antérieure détruite après sa création ;
   dépense des antérieures ≥ D de la première règle + c × K′ × t / 3 600 (sinon D serait sous-compté) ; aucune garde
   « sonde orientée » ni « dépense » tombée à la première exécution (conditions de `relance_permise`, lues par le script
   dans les journaux de gardes transférés, sans note). La conduite de lancement (`lancer-conduite-v13.py`) vérifie en
   outre les empreintes du manifeste de la règle, du journal des durées et des journaux de gardes de la reprise, et
   exactement les tours 0 à 7. Relevé sur les valeurs réelles : les gardes passent (dépense des sept antérieures
   ≈ 14,44 USD ≥ 5,0331 + 1,3421 × 8 × 1 315,99 / 3 600 ≈ 8,96 ; aucune garde tombée).
3. **Assemblage pour la lecture** (`assembler_lecture`) : un dossier neuf qui réunit les transferts de la série 3 (mise
   en place, contrôle du juge, pilote, règle, principal, manifestes) et ceux de la relance (`principal-relance`,
   manifeste « relance ») ; la mise en place et le contrôle du juge de l'instance de la relance y sont copiés à part et
   doivent avoir passé toutes leurs gardes **et être identiques à celles de la première** (pas par tour, longueur du
   suffixe, écart 10, empreintes des cibles ; mêmes champs dans le manifeste « relance » que dans le manifeste de la
   règle), puisque la lecture audite la relance avec la mise en place de la première ; toutes les empreintes copiées sont
   vérifiées ; le manifeste de relance doit citer la règle de la série 3 ; graines, code public et B présents et égaux ;
   manifestes de la conduite de relance copiés à part (`relance-manifestes/`), un manquant fait refuser. `lecture_v8.valider` et `lire` (inchangés) lisent ce
   dossier comme une conduite unique : la première exécution comme interrompue (K′ = 8), la relance comme portant le
   verdict. Aucune note n'est lue par l'assemblage.

Ce qui rend l'écart compatible avec l'objet de R3 : la relance est celle du texte ; aucune note de la première exécution
n'a été lue ; la règle de K est celle du texte ; la graine est celle du texte.

## 3. Code, essais, contre-lecture
Commit du code : `f60c2620a3891ebe579a807b2a90afb06e9e3ea5`. Seul change, par rapport à l'addendum 4 :

| Rôle | Module | SHA-256 |
|---|---|---|
| Lanceur local | `lanceur_v20.py` | `0a5469193e5278ad344dff6d6eed358b630f6754742a7ed7c1045b6b9908897b` |

`lanceur_v18.py` (`5302c346…`) et `lanceur_v19.py` (`1fa00722…`) restent tels quels (R12) et ne tournent pas.

Instance (`instance_v16`), exécution (`execution_v4`), lecture (`lecture_v8`), journaliseur, conventions, analyse :
inchangés ; l'archive envoyée sur l'instance est la même liste de fichiers. Manifeste neuf (R12) :
`manifeste-local-v6.json` (`5e62c0d8…`), seule différence avec le v5 : `commit_code`.

Essais (R5) : `tests/test_temoin_bailey_condition6_v20.py` (`a19611a9…`) : les essais v17 rejoués sur `lanceur_v20` ;
plus : relance seule de bout en bout (première conduite interrompue à 3 tours, t = 3 600 s ; relance seule par une
conduite neuve, D = 3,2 avec l'antérieure, K = 53 par la règle, H recalculé ; assemblage ; `valider` : K′ = 53, première
exécution interrompue à 3 ; `lire` : verdict au régime réduit K = 53) ; même chose avec une première exécution sans
état transféré (forme réelle de la reprise : reconstituée à la lecture) ; assemblage sur une copie de la structure réelle
de `reprise-v10-2` réduite aux dossiers et aux JSON (aucun journal) ; valeurs réelles du script (gardes passées, K = 72) ;
artefacts : gardes d'entrée (K′ = 20, booléen, négatif, t nul, règle incomplète, B, K de la première < 20, règle ≠
manifeste, manifeste altéré ou absent, clés manquantes, instance absente, taux différent, destruction avant création,
dépense sous la borne, gardes « dépense » ou « sonde orientée » tombées, liste illisible : aucune création, aucun
dossier de sortie) ; K de relance < 20 (antérieure de 45 h : K = 17, arrêt) ; contrôle du juge hors seuil ; assemblage
refusé (cible présente, relance déjà présente, mise en place de la relance tombée ou différente sur chaque champ,
manifeste de relance différent, juge de la relance non tenu, relance avec pilote, première incomplète, mise en place de
la première absente, fichier scellé altéré, manifeste absent sans créer la cible, graines, code public ou B absents ou
différents, manifeste qui ne cite pas la règle). Résultat : 220 passés, 1 sauté (configurations publiques non
fournies). L'essai des valeurs réelles lit la conduite v12, dont les instances antérieures sont égales à celles de la v13 ;
la v13 (`relance_seule()`, journaux de gardes compris) est vérifiée par la contre-lecture de cet addendum.
`test_v20_modules` est défini deux fois ; la première définition ne tourne pas (ses assertions, vérifiées à la main par
la contre-lecture, sont vraies).

Contre-lectures du code (R2) : `docs/notes/reproduction-attaque-publiee-v1/relecture-code-condition6-v18-relance-seule-bailey-v1.md`
(`cd540827…`, v18 : conforme après corrections, C-1 à C-11) ; `…/relecture-differentielle-code-v19-relance-seule-bailey-v1.md`
(`8fa2fdc5…`, v19 : conforme après corrections, R-1 à R-8) ; corrections dans v19 puis v20 (R-2 dans les pièces de
lancement, R-8 aussi déclarée au § 5). La différence de la v19 à la v20 (R-1, R-3, R-6, R-7, R-8) et la conduite v13 sont
lues par la contre-lecture de cet addendum (rapport cité en fin de texte) : conformes, sous K-7 et K-8.

Pièces de lancement : `lancer-conduite-v13.py` (`db950a6d…`, `lanceur_v20`, manifeste v6, sept antérieures, essai à
vide : refus sans `GO_ID`, gardes d'entrée passées sur les valeurs réelles) ; poste `poste-hetzner-v12.sh`
(`0990ff20…`, offre comme au poste v11, garde du commit `f60c2620`) et constructeur `construire-donnees-demarrage-v12.py`
(`233793c7…`). `lancer-conduite-v12.py` (`684eb5ef…`, écrite pour `lanceur_v18`) n'a jamais tourné. Déclaré (K-8) : la
docstring de la v13 garde, sous son en-tête, l'historique des versions antérieures (`lanceur_v13`, commit `4988f3f4`) ;
la v13 vérifie les fichiers de la reprise contre leurs compagnons (les empreintes fixées ci-dessus, § 1, referment ce point
à la lecture) ; son fichier de PID est écrit avant `relance_seule()` : un refus à ce stade, sans dépense, bloque une
nouvelle exécution sous le même nom (R12 : nouvelle version).

## 4. Ce qui ne change pas
Hypothèse, prédictions, métriques, seuils, population, juge, modèle, bras, graines, B, critères de lecture gelés, liste
d'arrêt, lectures actées. Une seconde erreur avant 20 tours complets de la relance : arrêt, pas de verdict, nœud (texte
l. 371). La relance est la seule ; aucune autre série sans nouvelle décision et nouvel addendum. Un arrêt avant le
lancement de `principal-relance` n'est pas une seconde erreur : la relance n'a pas commencé. Mise en place tombée :
refaite selon le texte (l. 363), par une conduite et un poste neufs (R12), sur un nouveau mot de Lazar, sans nouvel
addendum si le code ne change pas. Contrôle du juge hors seuil : nœud, aucun nouveau contrôle sans version nouvelle du
texte (l. 365) ; la première exécution reste rapportée comme interrompue ; pas de verdict.

## 5. Risques déclarés
Ceux des addenda 2 à 4, gardés. En plus :
- (a) **crédit du compte Vast**, partagé avec d'autres chantiers (note 0731) : une coupure faute de crédit avant 20 tours
  complets de la relance est une seconde erreur (arrêt, pas de verdict, nœud) ; après 20 tours, un run tronqué (l. 372).
  La garde de dépense (D ≥ B − 2) ne protège pas d'un compte vide. Dépense permise de la relance : jusqu'à B − 0,5 − D,
  soit ≈ 60 USD au compte prudent ; durée attendue ≈ 28 à 32 h (72 tours, durées de la première exécution, marge 1,15) ;
  condition 9 ;
- (b) la mise en place de l'instance neuve refait le contrôle du juge sous la graine du pilote (garde de mise en place) :
  il produit des réponses et des notes du juge, comme à chaque série ; ce n'est pas une lecture ;
- (c) le pilote n'est pas rejoué : t est celui de la série 3 ; si l'instance neuve est plus lente, la relance peut dépasser
  le budget : la garde de dépense l'arrête (run tronqué, lu sur K′ ≥ 20 s'il est atteint) ;
- (d) l'assemblage est un code neuf de lecture ; il ne lit aucune note ; s'il refuse, le verdict n'est pas prononcé : nœud ;
  l'égalité de la mise en place n'est contrôlée qu'à l'assemblage, après la dépense ; risque faible (valeurs
  déterministes) ;
- (e) la liste des gardes tombées de la première exécution vient des journaux de gardes transférés par la reprise ; une
  garde d'une ligne coupée au moment de l'interruption n'y figurerait pas ; `valider` la relit à la lecture ; dans le cas
  réel, aucune ligne coupée (dernière ligne complète) ; une ligne coupée ferait refuser le script avant toute création.

## 6. Conditions de lancement
1 à 6 : comme à l'addendum 4 (condition 6 : cet addendum, scellé, pour la relance). 7 : le mot direct de Lazar pour le
lancement de la relance, demandé après le scellement de cet addendum et le relevé du crédit (condition 9) ; le « go (a),
vérifie le chemin de code de la relance » (`357f18b9…`) engage l'addendum et le code, pas la création de l'instance.
8 : poste Hetzner autonome neuf (v12) ; l'ordre de lancement relève la tête poussée (addendum scellé présent) et
l'empreinte imprimée par le constructeur (`0990ff20…`). 9 : crédit relevé (champs `credit` et `balance`, heure,
consignés dans l'ordre de lancement) au plus tard une heure avant la création, au moins égal à B − 0,5 − D du poste au
relevé, plus la consommation prévue des autres instances du compte pendant 45 h ; sinon aucune création. Si le poste
attend une offre plus d'une heure, le crédit est relevé de nouveau avant la création. Relevé de la session, non consigné :
28,72 USD à 08:52Z, insuffisant. Aucune instance avant le scellement de cet addendum, le crédit suffisant et le mot de
Lazar.

## Contre-lecture
Rapport (R2) : `docs/notes/reproduction-attaque-publiee-v1/contre-lecture-addendum-5-relance-seule-bailey-v1.md`
(`2e274b1619ec84c3ef02c3b7b8c71b71b0f73067f391728fd914383459d9ebdb`), contre-lecteur neuf, sur le brouillon 2 :
« scellable après corrections », aucun bloquant. Traitement : K-1 (condition 7 réécrite selon (ii), recommandée) ; K-2
(risque (a) réécrit, condition 9 ajoutée, texte du rapport) ; K-3 (§ 1 : cause la plus probable ; classement) ; K-4 (§ 4 :
arrêts avant la relance) ; K-5 (§ 3) ; K-6 (empreintes ajoutées ; crédit « non consigné » ; phrase du mutant retirée,
faute de pièce) ; K-7 (§ 3, déclaré) ; K-8 (§ 3, déclaré) ; K-9 (risque (e)) ; K-10 (§ 2.1) ; K-11 (risque (d)).
