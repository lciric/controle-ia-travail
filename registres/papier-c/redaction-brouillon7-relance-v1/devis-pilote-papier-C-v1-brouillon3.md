# Devis — pilote du papier C (étape 1 du préenregistrement HC1 à HC3) — v1, brouillon 3

Écrit le 2026-11-22 par le rédacteur du brouillon 7 de relance du préenregistrement (session fille
`session_013QMayk1rjSZrn2u9UAVhEp`). Classe A (devis) : contre-lu par un autre modèle, à sceller par la session
mère, puis mot du directeur. **Rien n'est lancé ni inscrit par ce document.** Il remplace, sans l'écraser, le
brouillon 2 (`40069732…`), après sa contre-lecture (rapport
`contre-lecteur/rapport-verification-c2-et-contre-lecture-devis-v1.md`, `52b9ce5f…` : 2 majeures, 4 mineures ;
traitement : `table-traitement-contre-lecture-devis-brouillon2-v1.md`).

**Pourquoi ce devis.** Décision D-24 du directeur (GO-2026-11-22-123) : « ligne de calcul propre au pilote du
papier C, sur devis (aucune dépense avant le devis et son GO) ». Le préenregistrement ne nomme aucun identifiant
d'accord (décision D-18, option (b), GO-2026-11-19-74) : le lanceur reçoit l'identifiant de la ligne au lancement et
le vérifie par les règles de la garde de calcul.

Texte de référence : `brouillons/papier-C-preenregistrement-HC1-HC3-v1-brouillon7-relance-2026-11-22-c3.md`, Plan
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

Nombre de lancements : un ; un second seulement si le premier est perdu par l'hôte ou arrêté par une garde avant la
fin, dans le cumul de 4 heures et dans le plafond du § 4. Une panne technique déclarée n'est pas un résultat : la
relance se fait sur la même ligne (règle du 22 novembre, GO-2026-11-22-77).

## 2. Machine

| élément | valeur | source |
|---|---|---|
| carte | 1 × A100 80 Go | devis de la phase 0, `livrables/premier-rendu-v1/devis-v1.md` (`16d71feb…`), ligne « Instance de référence » |
| loueur | Vast.ai | `CLAUDE.md`, routine de reprise ; `registres/depenses.md` |
| **offre conforme** | une carte A100 de 80 Go (SXM4 ou PCIe), à la demande ; disque d'au moins 80 Go ; fiabilité affichée d'au moins 0,97 ; prix horaire, stockage compris, d'au plus 1,50 USD | fiabilités relevées au registre pour les offres retenues : 0,978 à 0,9973 (`registres/depenses.md`) ; disque : trois modèles de l'ordre de 16 Go chacun, image, roues et sorties |
| offre retenue | la moins chère des offres conformes à la recherche du lanceur ; identifiant, hôte, prix, prix du réseau et du disque consignés dans `registres/depenses.md` avant la création | règle du lanceur ; § 5 |
| descente | trois modèles, l'image et les roues ; ordre de grandeur connu pour un modèle : ≈ 16 Go (Llama-3.1-8B, offre A100, instance 54298522, 2026-10-05) ; les deux autres tailles sont lues aux révisions figées | `registres/depenses.md` |

## 3. Durée et prix

| poste | valeur | source |
|---|---|---|
| heures de carte, borne | **4 heures au plus, en cumul**, descentes et chargements compris | `registres/go.md`, GO-2026-10-17-01 ; texte, Plan, section 1 |
| heures de carte, attendu | **non sourcé**. Aucun débit de lecture directe par ces trois juges n'est consigné dans une pièce que ce rédacteur peut lire. Seul repère au registre, pour une autre charge (génération) : un rejeu de juges sur 180 notations a pris 1,53 h, descente et chargement compris (instance 58178416, 2026-10-29). La garde de projection du § 5 remplace cet attendu par une mesure dès les premières lectures | `registres/depenses.md`, lignes du 2026-10-29 |
| prix unitaire, indicatif | 0,80 à 1,30 USD/h (central 1,00) | devis de la phase 0 (`16d71feb…`), ligne « Instance de référence » |
| prix unitaire, relevés (offres A100 SXM4 80 Go) | 1,08 à 1,2133 USD/h en octobre ; 1,1833 USD/h le 2026-11-18 (instance 61276240) ; 1,22 USD/h stockage compris le 2026-11-19 (instance 61414494) | `registres/depenses.md`, lignes de ces dates |
| plafond de prix horaire | **1,50 USD/h**, stockage compris ; **dérivé** : GO-2026-10-17-01 écrit « 4 heures de carte (≈ 6 USD) », soit 1,50 USD/h ; ce n'est pas une borne que l'accord d'origine écrivait | `registres/go.md`, GO-2026-10-17-01 |
| réseau | prix au gigaoctet lu sur l'offre ; relevés : 0,026 USD/Go (offre A100, instance 61414494, 2026-11-19) ; 0,038 USD/Go (offre H100, instance 54183350, 2026-10-04) | `registres/depenses.md`, lignes de ces dates |
| disque d'une instance arrêtée | facturé tant qu'elle existe ; relevés : ≈ 0,027 USD/h (A100, instance 54298522) ; ≈ 0,074 USD/h (H100, instance 54183350) | `registres/depenses.md`, lignes des 2026-10-04 et 2026-10-05 |
| pire cas de carte | 4 h × 1,50 USD/h = **6,00 USD** (dérivé) | calcul sur les deux bornes |
| reste, au pire, pour le réseau et le disque | 10,00 − 6,00 = **4,00 USD**, pour les deux lancements ensemble | plafond du § 4 |

## 4. Ligne à inscrire, et ce qu'elle change

Ligne de type « calcul » proposée pour `registres/go.md`, à inscrire sur le mot du directeur :

> pilote du papier C (étape 1 du préenregistrement scellé de HC1 à HC3 ; devis `devis-pilote-papier-C-v1`, chemin et
> empreinte de sa version scellée) : 4 heures de carte au plus en cumul ; deux lancements au plus, le second
> seulement après une perte par l'hôte ou un arrêt par une garde ; plafond de prix 1,50 USD/h ; **plafond 10 USD,
> tout compris et en cumul** (carte, stockage, réseau, disque jusqu'à la destruction), compté dans l'enveloppe de
> calcul de la phase 0 ; lancé seulement après le scellement du préenregistrement contre-lu, de sa configuration, de
> son module et de l'addendum de lancement ; ligne d'accord du jour exigée à chaque lancement ; échéance 2026-12-31.

| | accords d'origine | ligne proposée | nature du changement |
|---|---|---|---|
| durée | 4 heures de carte (GO-2026-10-17-01) | 4 heures de carte au plus, en cumul | aucun |
| montant | « ≈ 6 USD » pour le pilote (GO-2026-10-17-01) ; 10 USD au plus **par lancement** (délégation GO-2026-10-20-07) | 10 USD **pour le pilote entier**, tout compris | **neuf** : au-dessus de « ≈ 6 USD » (qui ne comptait que la carte), au-dessous de ce que la délégation permettait sur plusieurs lancements |
| nombre de lancements | non borné ; accord du directeur à chaque lancement | deux au plus ; accord du jour à chaque lancement | **neuf**, plus serré |
| prix horaire | aucun plafond écrit | 1,50 USD/h au plus | **neuf**, dérivé de « ≈ 6 USD » pour 4 heures |
| enveloppe | « dans les 150 USD de GO-2026-10-04-08 » (GO-2026-10-17-01) ; « à l'intérieur de ce plafond » (GO-2026-10-04-08) | dans cette enveloppe | aucun (voir l'option ci-dessous) |
| échéance | 2026-11-01, puis 2026-11-30 (GO-2026-10-20-06), puis 2026-12-31 par la prolongation générale (GO-2026-11-22-93) | 2026-12-31, propre à la ligne | la date ne dépend plus de celle de l'enveloppe |
| préalables | préenregistrement scellé et contre-lu ; accord par lancement | les mêmes, plus la configuration, le module et l'addendum de lancement scellés | précisé (décision D-20) |

**Option posée au directeur, sur l'enveloppe.** (A) Le plafond du pilote se compte dans les 150 USD de la phase 0 :
c'est la lettre des deux accords d'origine, et c'est ce que la ligne proposée écrit ; le lanceur vérifie alors que le
cumul de l'enveloppe lu dans `registres/depenses.md`, plus 10 USD, ne dépasse pas 150 USD. (B) Il se compte à part :
aucun autre chantier ne peut le consommer, mais c'est un écart à la lettre de GO-2026-10-04-08 et de GO-2026-10-17-01,
que seul le mot du directeur peut ouvrir. Recommandation : (A), confiance 0,7.

## 5. Ce qui arrête la dépense

Ces règles s'écrivent dans l'addendum de lancement (décision D-20), scellé avant le pilote. Elles sont plus serrées
que la borne du texte (Plan, point 1.6 : par lancement, sur la carte seule, strictement sous 10 USD), qui reste donc
tenue : le texte n'est pas contredit.

- Avant toute carte : essais du module et banc de reproduction sur processeur ; échec : arrêt, aucune location.
- Préalables (liste d'arrêt 2 du texte) : texte scellé et contre-lu, verdict complété de P3, addendum de lancement
  scellé, ligne de type « calcul » valide au jour du lancement, ligne d'accord du jour ; l'un manque : arrêt avant la
  création de l'instance.
- **Règle cumulative, avant chaque création.** Le lanceur relève le crédit du loueur ; il calcule : dépensé jusque-là
  pour le pilote (somme des baisses de crédit relevées aux lancements précédents) + heures de carte restantes × prix
  de l'offre + réseau estimé (tailles des trois modèles aux révisions figées, de l'image, des roues et des sorties ×
  prix au gigaoctet de l'offre) + disque jusqu'à la destruction (durée de marche restante plus le délai ci-dessous ×
  prix du disque de l'offre). Si le total dépasse 10 USD, ou si le prix de l'offre dépasse 1,50 USD/h : pas de
  création.
- **Pendant la marche.** Durée bornée par min(4 heures moins les heures déjà consommées, ce que le reste du plafond
  permet au prix relu) ; prix relu après création au-dessus de 1,50 USD/h : destruction aussitôt, par l'identifiant.
  Le crédit du loueur est relevé au moins toutes les 30 minutes : une baisse, depuis la création, plus grande que le
  reste du plafond : arrêt, puis destruction.
- **Garde de projection.** Après les 500 premières lectures du point 1.4, le lanceur projette la durée totale
  (lectures restantes de tous les points × temps moyen par lecture mesuré, plus le chargement des modèles restants).
  Si la projection dépasse les heures restantes : arrêt avant de dépenser plus, sorties versées, nœud. La garde ne
  lit que des durées, aucun score.
- **Après l'arrêt.** L'instance s'arrête par son identifiant à la borne et à la fin (R10), consigné dans
  `registres/arrets.md`. Inventaire des sorties (noms, tailles, empreintes) et versement scellé, vérifié, puis
  destruction par l'identifiant, **au plus tard 2 heures après l'arrêt** ; si le versement n'est pas vérifié à ce
  délai : la machine reste arrêtée, disque gardé, nœud (rien n'est détruit avant le versement).
- **Compte de la dépense.** Crédit du loueur relevé avant la création et après la destruction ; l'écart, qui
  comprend le réseau et le stockage, est la dépense du lancement, consignée dans `registres/depenses.md`.
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
2. Mot du directeur, option de l'enveloppe comprise ; inscription de la ligne de type « calcul ».
3. Scellement du préenregistrement, de la configuration, du module ; addendum de lancement scellé, qui porte les
   règles du § 5.
4. Contrôle du crédit du loueur ; création par identifiant avec `GO_ID`.

## 8. Non vérifié par ce rédacteur

Le débit des lectures (d'où l'absence d'attendu) ; la taille de Qwen2.5-7B-Instruct et de Mistral-7B-Instruct-v0.3,
de l'image et des roues ; le nombre de variantes et de réponses imposées de la configuration (les décomptes du § 1
sont par variante essayée) ; le cumul de l'enveloppe de la phase 0 au jour du lancement ; ce que l'interface du
loueur permet de relever en marche (crédit, prix du disque).
