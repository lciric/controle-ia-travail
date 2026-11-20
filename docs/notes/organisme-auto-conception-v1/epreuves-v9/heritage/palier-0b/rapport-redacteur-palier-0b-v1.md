# Rapport du rédacteur — préenregistrement du palier 0b de l'épreuve sur l'héritage (étage sur processeur) — v1

- Auteur : rédacteur neuf, modèle F. Pièce de travail (classe C). Rendu le 2026-11-19T15:52Z (`date -u`).
- Mandat : `mandat-redacteur-preenregistrement-palier-0b-v1.md` (`e8eff3612760b166bed3a6d76d44b0c62f6f986a37c2e4661d8f25de5e7ab383`), empreinte vérifiée avant de commencer.
- Sur processeur seul : aucun appel à un fournisseur de modèles, aucune dépense, aucun commit, aucune poussée, aucune écriture dans le dépôt ; aucun tirage, aucune simulation. **Aucun refus d'outil.** Un incident : la première écriture de mon petit calcul d'ordres de grandeur était trop lente ; je l'ai arrêtée par son identifiant de tâche et récrite.

## 1. Fichiers rendus (bloc-notes de la session, dossier `redacteur-palier-0b/`)

| fichier | empreinte SHA-256 |
|---|---|
| `preenregistrement-heritage-palier-0b-etage-processeur-v1.md` | `a7189bbb598d0dbc4bc6d0390381d45d5ec652a4cf78b9e077898f690449db74` |
| `calcul_ordres_de_grandeur_palier_0b_v1.py` (calcul analytique, sans tirage) | `83d3f97df49fb36c1912a945a8ee8436d08a24170cf1571984edc30173f72d34` |
| `calcul-ordres-de-grandeur-palier-0b-v1.json` (sa sortie, rejouée deux fois à l'octet) | `fad2ce800745053eaf51acc5900ae57afb05b3a944a8ec1688311290aece33ad` |
| `rapport-redacteur-palier-0b-v1.md` | compagnon `.sha256` à côté |

Le préenregistrement passe le validateur du gabarit à une remarque près, attendue : la section « Contre-lecture » n'a pas encore ses deux empreintes. Il n'est pas scellable avant la contre-lecture, ni avant l'erratum qui inscrira le commit du code.

## 2. Ce que j'ai gelé, et pourquoi

| valeur | gelée à | raison courte |
|---|---|---|
| maximum de la grille étendue | 48 (gardé) | par approximation normale, voir à 0,8 la moitié de la taille de référence au seuil de 0,025 demande environ 40 sources, 47 avec 15 % de différences nulles (calcul joint) |
| grille à dose nulle | 5 à 16 (gardée) | 5 est le plus petit nombre où la règle unilatérale peut se déclencher ; 16 couvre trois quarts de la taille de référence |
| tirages par case | 10 000, emboîtés (gardé) | sépare 0,05 de 0,06 et 0,8 de 0,78 (intervalles exacts au calcul joint) ; l'emboîtement évite que n et m sautent par hasard |
| taux d'échec de l'expérimentateur | 0,25 pour ce qui décide ; 0 et 0,5 rejoués à la taille de référence | aucune mesure ; milieu de ce que la règle du palier 1 tolère ; les deux bords calculés d'avance |
| règles de retrait | celle de la version 2 du plan décide ; celle de la version 1 pour le seul point 8 | lettre du plan |
| taille de référence | un écart-type entre courses jumelles (gardée) ; grille 0,5 ; 0,75 ; 1 ; 1,5 | unité du pilote de bruit |
| ce que reçoit l'expérimentateur | engagement scellé et description bornée, entre balises ; le reste de la fiche en textes neutres de l'orchestrateur | proposition du plan, précisée par le palier 0a |
| forme des engagements à cet étage | celle, imposée, du tour fermé | seule forme gardée contre un script qui fabrique ses lignes (palier 0a, essai E2) |
| tranche d'épreuve ; condition des lois fausses ; marges du générateur | la moitié ; valeur du plan ; 0,25 nat et 0,55 d'exactitude équilibrée | propositions du plan, ou cinq fois le seuil de l'oracle |
| règle du point 7 | « presque autant » = quatre cinquièmes, lue sur l'intervalle du rapport des écarts ; trois issues | même fraction que C2 et C5 ; elle ne décide que d'une revue |

**Trois valeurs proposées par le plan sont changées, avec raison écrite** (à vérifier d'abord par le contre-lecteur) :

1. **C1 et C4** : la clause « taux observé au plus 0,05 » est remplacée par un tirage de confirmation à 100 000 tirages (échec si sa borne basse dépasse 0,05) ; la borne haute à 0,06 est gardée. Le test étant exact, son niveau vrai peut frôler 0,05 ; le taux observé le dépasserait alors près d'une fois sur deux, et l'étage se dirait « à reconstruire » sans défaut.
2. **« Atteint à un nombre »** (C2, C3, n et m) : tenu à ce nombre et à tous les suivants de la grille.
3. **Le suiveur de forme** répond à la taille du registre servi, non à sa seule présence : à la génération finale les bras 2 et 3 ont tous deux un registre non vide, et le suiveur du plan n'aurait aucun écart d'héritage à montrer à la règle de validité. Le suiveur « à la lettre » est gardé à côté, sans critère.

**Ajouts de dessin du banc, à contre-lire** : deux couches (mécanique, sur objets réels, pour les gardes ; statistique, au grain de la loi, pour les 10 000 tirages), liées par une garde d'équivalence ; la puissance de chaque contraste tirée avec l'autre sans effet (borne prudente sous la procédure de Holm) ; l'effet de tenue du lecteur planté par paramètre.

## 3. Les six décisions de Lazar

Toutes portées, telles quelles (table à la section « Hypothèse » du préenregistrement) : test de mort comme épreuve, sans activer le branchement ; `resultat` et `gardee` servis, repli mesuré et règle chiffrée écrite ; témoins jugés hors de tout, **écrit comme écart déclaré à la lettre de N-058**, aucun juge ; deux contrastes décisifs ; pas de base « tirages indépendants » ; expérimentateur modèle gardé, nommé, échecs simulés à un taux égal dans les trois bras. Aucune n'est contredite ni étendue.

## 4. Ce que changent les deux manques du palier 0a

- **Étiquette liée à la promotion** : la mesure ne peut pas employer l'étiquette de l'oracle. Un comparateur sans juge est défini (appariement à 0,05 nat sur la loi relue dans l'engagement scellé, par domaine ; ne lit jamais la promotion), avec sa garde.
- **Aucun générateur de mondes composés** : il est défini ici (mondes en domaines, douze lois vraies par monde cible, huit dans la source, lois dépendantes composées de deux lois de la source par sous-population, lois fausses « demi-vraies », domaines sans structure) et doit être écrit et audité avant tout. « Retrouver une loi parmi plusieurs » est fixé par le domaine.
- **À écrire en code avant tout tirage** : générateur et audit ; comparateur ; part servie et tranche d'épreuve ; registre et sa projection gardée ; enveloppe autour de l'étage (lots de douze, statut de budget, seuil relu) ; exécuteur simulé et échecs ; compteur de coût ; proposeurs ; test exact ; étalonnage ; analyse. L'étage des tests de mort n'est pas réécrit.

## 5. Ce que je n'ai pas pu faire, et ce qui reste ouvert

- **Lire le code de l'organisme** : il n'est pas dans le conteneur (`/home/user/ideation-organism` absent). Tout repose sur le rapport du palier 0a. La composition par sous-population n'est pas vérifiée contre la grammaire des lois ; si elle ne tient pas, c'est un arrêt et un erratum.
- **Les quatre constats de forme** : trouvés dans la vérification de la version 3, au § 19 du plan et dans les consignes de la mère ; tous portés (annexe B). **La ligne R-3858 sur `main` ne les nomme pas** ; la phrase est dans les consignes seulement.
- `main` est lu au commit `ccafc3b0`, postérieur au commit `f9209a97` du mandat (qui en est un ancêtre).
- Rien ne dit que la taille de référence est atteignable à la dose 0,25 ; rien n'a été tiré. La liste d'arrêt dit quoi faire.
- Le code est à écrire après la contre-lecture ; son commit entre par erratum avant le scellement final.
- Deux formules du plan (« en échec à tout nombre ») se lisent de deux façons ; ma lecture est écrite (réserve 6).
- Aucun chiffre de la littérature n'a été relu sur PDF ; les deux chiffres de Qin et al. sont dans les mots de N-073.

## 6. Décisions pour Lazar

**Décision 1 — Le lecteur témoin des tests de mort est-il joué aux paliers payants ?**
Enjeu : l'étage l'exige et ouvre une session par tentative (au plus 0,10 USD chacune, soit au plus 3 290 USD à cinq espèces ; devis, § 5 et § 9) ; il ne pèse sur aucun verdict ; le mot « on garde l'expérimentateur » ne le vise pas.
- (a) Doublure par programme au palier 0b (c'est écrit), lecteur réel au seul palier 1, pour voir s'il relève quelque chose, puis décision. Avantage : une mesure avant de trancher. Inconvénient : quelques dollars au palier 1.
- (b) Doublure partout. Avantage : aucun coût. Inconvénient : il n'est pas vérifié qu'un lanceur réel accepte la doublure (palier 0a) ; on perd un témoin.
- (c) Lecteur réel partout. Avantage : l'étage tel qu'il est. Inconvénient : jusqu'à 3 290 USD pour un rôle sans poids.
Recommandation : (a), confiance 0,6. Défaut sous 48 heures : aucun, c'est une dépense ; la question se tranche au devis du palier 1 et ne bloque pas le palier 0b.

**Décision 2 — Le contraste de la tenue n'a pas de contrôle de forme : que dit-on d'une tenue « établie » ?**
Enjeu : la règle de validité ne joue que les bras 2 et 3 à dose nulle ; elle protège l'héritage. Un effet dû à la seule présence d'un registre servi gonflerait le contraste de la tenue (bras 2 moins bras 1) sans rien déclencher. Le palier 0b le mesure sur un suiveur écrit par programme.
- (a) Garder le dessin ; écrire d'avance, au préenregistrement de l'étage payant, qu'une tenue établie se dit « servir un registre tenu, forme comprise », les bras de diagnostic du plan (résultats permutés, registre paraphrasé) venant après, sur devis. Avantage : aucun coût, aucune pièce changée. Inconvénient : la tenue dit moins.
- (b) Ajouter au critère un bras témoin de forme pour la tenue (un registre de même taille au contenu brouillé). Avantage : la tenue est protégée comme l'héritage. Inconvénient : le dessin et le devis changent ; un bras de plus.
- (c) Rendre la tenue descriptive. Avantage : plus simple. Inconvénient : revient sur le nœud 4, tranché.
Recommandation : (a), confiance 0,6. Défaut sous 48 heures : aucun, c'est la formulation d'un résultat ; à trancher avant le préenregistrement de l'étage payant, sans effet sur le palier 0b.

**Décision 3 — Forme des engagements aux paliers payants : imposée, ou libre ?**
Enjeu : un engagement libre (fichier, colonne, statistique au choix du proposeur) n'a aucune garde contre un script qui fabrique ses lignes ; la forme imposée du tour fermé a un contre-calcul, mais borne ce qu'un proposeur peut engager aux lois de la grammaire.
- (a) Forme imposée partout, comme au palier 0b. Avantage : le verdict est contre-calculé. Inconvénient : l'épreuve ne vaut que pour les lois de la grammaire.
- (b) Forme libre, limite dite. Avantage : l'organisme tel qu'il propose. Inconvénient : un « tient » peut être fabriqué sans être vu.
Recommandation : (a), confiance 0,7. Défaut sous 48 heures : (a), pour le préenregistrement court du palier 1.

**Pour information, sans décision** : les trois changements du § 2 sont dans mon mandat (« changée avec raison écrite ») et vont au contre-lecteur. Si le palier 0b rend « presque autant » au point 7, la revue du nœud 2 sera proposée à ce moment-là. Je ne recommande aucune réduction du dessin ; c'est ma recommandation, non une règle reçue.
