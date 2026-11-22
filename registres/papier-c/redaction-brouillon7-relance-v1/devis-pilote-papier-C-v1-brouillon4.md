# Devis — pilote du papier C (étape 1 du préenregistrement HC1 à HC3) — v1, brouillon 4

Écrit le 2026-11-22 par le rédacteur du brouillon 7 de relance du préenregistrement (session fille
`session_013QMayk1rjSZrn2u9UAVhEp`). Classe A (devis) : contre-lu par un autre modèle, à sceller par la session
mère, puis mot du directeur. **Rien n'est lancé ni inscrit par ce document.** Il remplace, sans l'écraser, le
brouillon 3 (`d68649ef…`), après sa vérification par le même contre-lecteur (rapport
`contre-lecteur/rapport-verification-c3-et-devis-brouillon3-v1.md`, `265f62e7…` : 1 majeure, 3 mineures ;
traitement : `table-traitement-verification-devis-brouillon3-v1.md`).

**Pourquoi ce devis.** Décision D-24 du directeur (GO-2026-11-22-123) : « ligne de calcul propre au pilote du
papier C, sur devis (aucune dépense avant le devis et son GO) ». Le préenregistrement ne nomme aucun identifiant
d'accord (décision D-18, option (b), GO-2026-11-19-74) : le lanceur reçoit l'identifiant de la ligne au lancement et
le vérifie par les règles de la garde de calcul.

Texte de référence : `brouillons/papier-C-preenregistrement-HC1-HC3-v1-brouillon7-relance-2026-11-22-c4.md`, Plan
d'analyse, section 1 ; à remplacer, à l'inscription de la ligne, par le texte scellé et son empreinte. Aucun prix
n'est inventé : chaque montant renvoie à une ligne d'un registre du dépôt, il est dit « dérivé » quand il vient d'un
calcul, ou « lu au lancement ».

## 1. Ce qui tourne

Le pilote ne mesure que des propriétés de dessin (lisibilité des consignes, gains des formulations du vivier sans
destination, contrôle positif de la chaîne) ; il ne décide d'aucune hypothèse. Trois juges lisent des contenus ;
aucun agent ne génère, aucune sonde n'est lue.

| point du texte | ce qui est lu | lectures (une lecture = un juge, un contenu, une condition) |
|---|---|---|
| 1.0 | sur processeur, avant toute carte : essais du module, banc de reproduction | aucune dépense |
| 1.1 | empreintes ; règle du jeton en contexte, par juge × consigne × variante | négligeable |
| 1.2 banc sur carte | 30 items × 3 conditions × 3 juges, par réponse imposée essayée | 270 par réponse imposée |
| 1.3 lisibilité des consignes | 20 contenus × 3 juges × (consignes A et B : 1 + 15 formulations + 2 témoins ; alarme : 1 + 4 + 2), par variante essayée | 2 580 par variante |
| 1.4 vivier | n_cal contenus (60 au plus) × (1 + 80 formulations + 16 témoins + constat nu) × 3 juges, consigne A, mode direct | 17 640 au plus |
| 1.5 mode raisonné | 10 contenus × (1 + 5) × 3 juges, 384 jetons générés au plus par lecture | 180 |

Décomptes vérifiés par le contre-lecteur sur le Plan, section 1 : 270 ; 20 × 3 × (2 × 18 + 7) = 2 580 ;
60 × 98 × 3 = 17 640 ; 180. Juges : Llama-3.1-8B-Instruct, Qwen2.5-7B-Instruct, Mistral-7B-Instruct-v0.3, révisions
figées au scellement du préenregistrement. Les lectures en mode direct sont une passe avant sans génération ; seules
les 180 lectures du point 1.5 génèrent.

Nombre de lancements : un. Un second seulement dans le cumul de 4 heures et dans le plafond du § 4, et dans deux cas :
(a) le premier est perdu par l'hôte ou arrêté pour une cause technique déclarée (prix relu, dépense, réseau, perte du
conteneur) : une panne technique n'est pas un résultat, la relance se fait sur la même ligne, avec l'accord du jour
(règle du 22 novembre, GO-2026-11-22-77) ; (b) le premier est arrêté par une garde de projection (§ 5) : ce n'est
pas une panne, c'est un constat de dimension ; le second lancement ne s'ouvre alors que sur le mot du directeur, qui
dit sur quel périmètre.

## 2. Machine

| élément | valeur | source |
|---|---|---|
| carte | 1 × A100 80 Go | devis de la phase 0, `livrables/premier-rendu-v1/devis-v1.md` (`16d71feb…`), ligne « Instance de référence » |
| loueur | Vast.ai | `CLAUDE.md`, routine de reprise ; `registres/depenses.md` |
| **offre conforme** | une carte A100 de 80 Go (SXM4 ou PCIe), à la demande ; disque d'au moins 80 Go **et** d'au moins la place calculée ci-dessous ; fiabilité affichée d'au moins 0,97 ; prix horaire, stockage compris, d'au plus 1,50 USD | fiabilités relevées au registre pour les offres retenues : 0,978 à 0,9986 (`registres/depenses.md`, 13 relevés) |
| offre retenue | la moins chère des offres conformes à la recherche du lanceur ; identifiant, hôte, prix horaire, prix du réseau au gigaoctet et prix du disque consignés dans `registres/depenses.md` avant la création | règle du lanceur ; § 5 |
| **fichiers descendus** | fixés par motifs de fichiers à l'addendum de lancement : par modèle, **un seul jeu de poids**, la configuration et le découpeur en jetons, aux révisions figées ; rien d'autre du dépôt du modèle. Le lanceur lit la taille de chaque fichier retenu avant la création ; leur somme, plus l'image, les roues et les sorties, est la **place calculée** et le volume du **réseau estimé** | relevé du contre-lecteur, non vérifié par moi : un dépôt de modèle peut porter deux jeux de poids de taille voisine (celui de Mistral-7B-Instruct-v0.3) ; ordre de grandeur connu pour un jeu : ≈ 16 Go (Llama-3.1-8B, offre A100, instance 54298522, 2026-10-05, `registres/depenses.md`) |

## 3. Durée et prix

| poste | valeur | source |
|---|---|---|
| heures de carte, borne | **4 heures au plus, en cumul**, descentes et chargements compris | `registres/go.md`, GO-2026-10-17-01 ; texte, Plan, section 1 |
| heures de carte, attendu | **non sourcé**. Aucun débit de lecture directe par ces trois juges n'est consigné dans une pièce que ce rédacteur peut lire. Seul repère au registre, pour une autre charge (génération) : un rejeu de juges sur 180 notations a pris 1,53 h, descente et chargement compris (instance 58178416, 2026-10-29). Les deux gardes de projection du § 5 remplacent cet attendu par des mesures dès les premières lectures | `registres/depenses.md`, lignes du 2026-10-29 |
| prix unitaire, indicatif | 0,80 à 1,30 USD/h (central 1,00) | devis de la phase 0 (`16d71feb…`), ligne « Instance de référence » |
| prix unitaire, relevés (offres A100 SXM4 80 Go) | 1,08 à 1,2133 USD/h en octobre ; 1,1833 USD/h le 2026-11-18 (instance 61276240) ; 1,22 USD/h stockage compris le 2026-11-19 (instance 61414494) | `registres/depenses.md`, lignes de ces dates |
| plafond de prix horaire | **1,50 USD/h**, stockage compris ; **dérivé** : GO-2026-10-17-01 écrit « 4 heures de carte (≈ 6 USD) », soit 1,50 USD/h ; ce n'est pas une borne que l'accord d'origine écrivait | `registres/go.md`, GO-2026-10-17-01 |
| réseau | prix au gigaoctet lu sur l'offre ; relevés : 0,026 USD/Go (offre A100, instance 61414494, 2026-11-19) ; 0,038 USD/Go (offre H100, instance 54183350, 2026-10-04) | `registres/depenses.md`, lignes de ces dates |
| disque d'une instance arrêtée | facturé tant qu'elle existe ; relevés : ≈ 0,027 USD/h (A100, instance 54298522) ; ≈ 0,074 USD/h (H100, instance 54183350) ; à 0,027 USD/h, un dollar de reste tient environ 37 heures (dérivé : 1 ÷ 0,027) | `registres/depenses.md`, lignes des 2026-10-04 et 2026-10-05 |
| pire cas de carte | 4 h × 1,50 USD/h = **6,00 USD** (dérivé) | calcul sur les deux bornes |
| reste, au pire, pour le réseau et le disque | 10,00 − 6,00 = **4,00 USD**, pour les deux lancements ensemble | plafond du § 4 |

## 4. Ligne à inscrire, et ce qu'elle change

Ligne de type « calcul » proposée pour `registres/go.md`, à inscrire sur le mot du directeur :

> pilote du papier C (étape 1 du préenregistrement scellé de HC1 à HC3 ; devis `devis-pilote-papier-C-v1`, chemin et
> empreinte de sa version scellée) : 4 heures de carte au plus en cumul ; deux lancements au plus, le second
> seulement après une perte par l'hôte ou un arrêt pour une cause technique déclarée, ou, après un arrêt par une
> garde de projection, sur le mot du directeur ; plafond de prix 1,50 USD/h ; **plafond 10 USD, tout compris et en
> cumul** (carte, stockage, réseau, disque jusqu'à la destruction), dépense comptée par instance, compté dans
> l'enveloppe de calcul de la phase 0 ; lancé seulement après le scellement du préenregistrement contre-lu, de sa
> configuration, de son module et de l'addendum de lancement ; ligne d'accord du jour exigée à chaque lancement ;
> échéance 2026-12-31.

| | accords d'origine | ligne proposée | nature du changement |
|---|---|---|---|
| durée | 4 heures de carte (GO-2026-10-17-01) | 4 heures de carte au plus, en cumul | aucun |
| montant | « ≈ 6 USD » pour le pilote (GO-2026-10-17-01) ; 10 USD au plus **par lancement** (délégation GO-2026-10-20-07) | 10 USD **pour le pilote entier**, tout compris | **neuf** : au-dessus de « ≈ 6 USD » (qui ne comptait que la carte), au-dessous de ce que la délégation permettait sur plusieurs lancements |
| nombre de lancements | non borné ; accord du directeur à chaque lancement | deux au plus ; accord du jour à chaque lancement ; mot du directeur après un arrêt par une garde de projection | **neuf**, plus serré |
| prix horaire | aucun plafond écrit | 1,50 USD/h au plus | **neuf**, dérivé de « ≈ 6 USD » pour 4 heures |
| enveloppe | « dans les 150 USD de GO-2026-10-04-08 » (GO-2026-10-17-01) ; « à l'intérieur de ce plafond » (GO-2026-10-04-08) | dans cette enveloppe | aucun (voir l'option ci-dessous) |
| échéance | 2026-11-01, puis 2026-11-30 (GO-2026-10-20-06), puis 2026-12-31 par la prolongation générale (GO-2026-11-22-93) | 2026-12-31, propre à la ligne | la date ne dépend plus de celle de l'enveloppe |
| préalables | préenregistrement scellé et contre-lu ; accord par lancement | les mêmes, plus la configuration, le module et l'addendum de lancement scellés | précisé (décision D-20) |

**Deux points à dire avec le mot.**

1. **L'enveloppe.** (A) Le plafond du pilote se compte dans les 150 USD de la phase 0 : c'est la lettre des deux
   accords d'origine, et c'est ce que la ligne proposée écrit ; le lanceur vérifie alors que le cumul de l'enveloppe
   lu dans `registres/depenses.md`, plus 10 USD, ne dépasse pas 150 USD. (B) Il se compte à part : aucun autre
   chantier ne peut le consommer, mais c'est un écart à la lettre de GO-2026-10-04-08 et de GO-2026-10-17-01, que
   seul le mot du directeur peut ouvrir. Recommandation : (A), confiance 0,7.
2. **Le seul cas où le plafond peut être dépassé.** Une instance arrêtée dont le versement des sorties n'est pas
   vérifié garde son disque, qui coûte (§ 5, « Après l'arrêt ») ; la consigne du programme interdit de détruire avant
   le versement. Si le directeur ne tranche pas avant que le reste du plafond soit consommé, deux règles se
   contredisent. Le devis propose : rien n'est détruit, le dépassement se fait au seul prix du disque, il est
   consigné heure par heure comme écart à la ligne et porté au directeur. L'autre lecture (détruire au plafond)
   perd des sorties payées. Recommandation : garder le disque, confiance 0,8.

## 5. Ce qui arrête la dépense

Ces règles s'écrivent dans l'addendum de lancement (décision D-20), scellé avant le pilote. Elles sont plus serrées
que la borne du texte (Plan, point 1.6 : par lancement, sur la carte seule, strictement sous 10 USD), qui reste donc
tenue : le texte n'est pas contredit.

- Avant toute carte : essais du module et banc de reproduction sur processeur ; échec : arrêt, aucune location.
- Préalables (liste d'arrêt 2 du texte) : texte scellé et contre-lu, verdict complété de P3, addendum de lancement
  scellé, ligne de type « calcul » valide au jour du lancement, ligne d'accord du jour ; l'un manque : arrêt avant la
  création de l'instance.
- **Dépense du pilote : comptée par instance, jamais par le crédit du compte.** Le compte du loueur sert à d'autres
  chantiers et porte une recharge automatique (`registres/go.md`, GO-2026-11-22-77) : son crédit ne mesure pas la
  dépense du pilote. Pour chaque instance du pilote, par son identifiant, deux valeurs :
  - le **calcul du lanceur** : heures de marche (de la création à l'arrêt, à son horloge) × prix horaire relu de
    l'instance, stockage compris ; plus gigaoctets descendus et montés × prix au gigaoctet de l'offre (volumes lus à
    l'interface pour cet identifiant ; à défaut, somme des tailles des fichiers que le lanceur descend et verse
    lui-même, image et roues comprises) ; plus heures d'existence à l'arrêt × prix du disque de l'offre ;
  - le **coût lu** : le coût que l'interface du loueur attribue à cet identifiant (coût de l'instance ou ligne de
    facture), là où elle le donne.

  La dépense d'une instance est **la plus grande des deux** ; si l'interface ne donne aucun coût par identifiant,
  c'est le calcul du lanceur, et ce défaut est consigné. La dépense du pilote est la somme des dépenses de ses
  instances, consignée dans `registres/depenses.md`.
- **Le crédit du compte : un contrôle.** Relevé avant la création, au moins toutes les 30 minutes en marche et après
  la destruction, avec, à chaque relevé, les recharges survenues et les autres instances actives du compte
  (identifiants seulement). La baisse corrigée (baisse du crédit, plus les recharges, moins le coût des autres
  instances lu par leurs identifiants) est comparée à la dépense du pilote : si elle la dépasse, c'est elle qui est
  retenue comme dépense, et l'écart est consigné. Si le coût des autres instances ne peut pas être lu, le contrôle
  est écrit « non exploitable » : il n'arrête rien et ne corrige rien.
- **Règle cumulative, avant chaque création.** Dépense du pilote jusque-là (au sens ci-dessus) + heures de carte
  restantes × prix de l'offre + réseau estimé (place calculée du § 2 × prix au gigaoctet de l'offre) + disque
  jusqu'à la destruction (durée de marche restante plus le délai ci-dessous × prix du disque de l'offre). Si le
  total dépasse 10 USD, si le prix de l'offre dépasse 1,50 USD/h, ou si la place calculée dépasse le disque de
  l'offre : pas de création.
- **Pendant la marche.** Durée bornée par min(4 heures moins les heures déjà consommées, ce que le reste du plafond
  permet au prix relu) ; prix relu après création au-dessus de 1,50 USD/h : destruction aussitôt, par l'identifiant.
  La dépense du pilote est recalculée au moins toutes les 30 minutes ; si elle atteint le plafond moins le disque
  jusqu'à la destruction : arrêt, versement, puis destruction.
- **Gardes de projection** (elles ne lisent que des durées, aucun score).
  - Lectures directes : après les 500 premières lectures du point 1.4, le lanceur projette la durée des lectures
    directes qui restent (nombre restant × temps moyen par lecture directe mesuré, plus le chargement des modèles
    restants). Cette projection ne compte pas le mode raisonné, et le dit.
  - Mode raisonné : après les 6 premières lectures raisonnées de chaque juge (un contenu), le lanceur projette la
    durée des lectures raisonnées qui restent (nombre restant × temps moyen par lecture raisonnée mesuré).
  - Si l'une des deux projections dépasse les heures restantes : arrêt avant de dépenser plus, sorties versées,
    nœud. Cet arrêt n'ouvre pas de lui-même le second lancement (§ 1, cas (b)).
- **Après l'arrêt.** L'instance s'arrête par son identifiant à la borne et à la fin (R10), consigné dans
  `registres/arrets.md`. Inventaire des sorties (noms, tailles, empreintes) et versement scellé, vérifié, puis
  destruction par l'identifiant, **au plus tard 2 heures après l'arrêt**. Si le versement n'est pas vérifié à ce
  délai : la machine reste arrêtée, disque gardé, nœud (rien n'est détruit avant le versement). Le disque gardé
  au-delà des 2 heures **entre dans le plafond** : le lanceur écrit dans le nœud l'heure à laquelle le reste du
  plafond sera consommé (reste ÷ prix du disque relu), et le nœud est à trancher avant cette heure ; au-delà, voir le
  point 2 du § 4.
- Toute garde de la liste d'arrêt du texte qui dit « arrêt » ou « nœud » : arrêt du run, instance arrêtée.

## 6. Hors devis

- L'étape 2 (décisive : TC.1 à TC.3) et le bras « saboteur sans consigne » (décision D-23), qui demandent un devis
  et un accord à part, après la porte G0.
- Le bras « contrôlabilité » et son banc ; les lectures de sondes ; toute génération par l'agent.
- La grille de la clause de repli, les essais du module, la dérivation : sur processeur, sans dépense.
- Un rejeu du pilote au-delà du cumul de 4 heures, ou un troisième lancement : nœud.
- Tout appel à un modèle par une interface payante : il n'y en a aucun dans le pilote.

## 7. Avant le lancement

1. Vérification de ce brouillon par le même contre-lecteur, puis scellement par la session mère.
2. Mot du directeur, avec les deux points du § 4 ; inscription de la ligne de type « calcul ».
3. Scellement du préenregistrement, de la configuration, du module ; addendum de lancement scellé, qui porte les
   règles du § 5 et les motifs de fichiers du § 2.
4. Création par identifiant avec `GO_ID` ; relevés du § 5 dès avant la création.

## 8. Non vérifié par ce rédacteur

Le débit des lectures (d'où l'absence d'attendu) ; les tailles des fichiers des trois modèles, de l'image et des
roues, et le fait qu'un dépôt porte deux jeux de poids (relevé du contre-lecteur) ; le nombre de variantes et de
réponses imposées de la configuration (les décomptes du § 1 sont par variante essayée) ; l'ordre dans lequel le
module joue les points et les juges (les gardes de projection sont écrites pour tout ordre) ; le cumul de
l'enveloppe de la phase 0 au jour du lancement ; **ce que l'interface du loueur donne par identifiant d'instance**
(coût, volumes de réseau, prix du disque) : le § 5 dit ce que fait le lanceur dans les deux cas, et l'auteur du
lanceur le constate avant l'addendum de lancement.
