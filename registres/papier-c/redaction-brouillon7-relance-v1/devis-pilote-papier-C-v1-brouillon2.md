# Devis — pilote du papier C (étape 1 du préenregistrement HC1 à HC3) — v1, brouillon 2

Écrit le 2026-11-22 par le rédacteur du brouillon 7 de relance du préenregistrement (session fille
`session_013QMayk1rjSZrn2u9UAVhEp`). Classe A (devis) : à contre-lire par un autre modèle, à sceller par la session
mère, puis mot du directeur. **Rien n'est lancé ni inscrit par ce document.** Il part du brouillon 1 du 19 novembre
(`registres/papier-c/redaction-brouillon6-relance-v1/redacteur/devis-pilote-papier-C-v1-brouillon1.md`,
`a4c9bdbcac3feb0ea975518e1b60121907a9facd2325609ee203d1c6c51460dc`, branche `claude/papier-c-preenregistrement-v1`),
qui reste tel quel.

**Pourquoi ce devis.** Décision D-24 du directeur (GO-2026-11-22-123) : « ligne de calcul propre au pilote du
papier C, sur devis (aucune dépense avant le devis et son GO) ». Le préenregistrement ne nomme aucun identifiant
d'accord (décision D-18, option (b), GO-2026-11-19-74) : le lanceur reçoit l'identifiant de la ligne au lancement et
le vérifie par les règles de la garde de calcul.

Texte de référence : `brouillons/papier-C-preenregistrement-HC1-HC3-v1-brouillon7-relance-2026-11-22-c2.md`, Plan
d'analyse, section 1 ; à remplacer, à l'inscription de la ligne, par le texte scellé et son empreinte. Aucun prix
n'est inventé : chaque montant renvoie à une ligne d'un registre du dépôt, ou il est dit « lu au lancement ».

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

Vérification des décomptes : 1.2, 30 × 3 × 3 = 270 ; 1.3, 20 × 3 × (2 × 18 + 7) = 2 580 ; 1.4, 60 × 98 × 3 = 17 640 ;
1.5, 10 × 6 × 3 = 180. Juges : Llama-3.1-8B-Instruct, Qwen2.5-7B-Instruct, Mistral-7B-Instruct-v0.3, révisions figées
au scellement du préenregistrement. Les lectures en mode direct sont une passe avant sans génération ; seules les
180 lectures du point 1.5 génèrent.

Nombre de lancements : un ; un second seulement si le premier est perdu par l'hôte ou arrêté par une garde avant la
fin, dans le cumul de 4 heures et dans le plafond du § 4. Une panne technique déclarée n'est pas un résultat : la
relance se fait sur la même ligne (règle du 22 novembre, GO-2026-11-22-77).

## 2. Machine

| élément | valeur | source |
|---|---|---|
| carte | 1 × A100 80 Go | devis de la phase 0, `livrables/premier-rendu-v1/devis-v1.md` (`16d71feb…`), ligne « Instance de référence » |
| loueur | Vast.ai | `CLAUDE.md`, routine de reprise ; `registres/depenses.md` |
| offre exacte (identifiant, hôte, prix, disque, réseau) | lue au lancement par le lanceur, la moins chère des offres conformes ; consignée dans `registres/depenses.md` avant la création | règle du lanceur ; § 5 |
| descente des trois modèles | lue au lancement ; ordre de grandeur connu pour un modèle : ≈ 16 Go (Llama-3.1-8B) | `registres/depenses.md`, ligne du 2026-10-05, instance 54298522 |

## 3. Durée et prix

| poste | valeur | source |
|---|---|---|
| heures de carte, borne | **4 heures au plus, en cumul** | `registres/go.md`, GO-2026-10-17-01 ; texte, Plan, section 1 |
| heures de carte, attendu | non chiffré : aucun débit de lecture directe par ces trois juges n'est consigné dans une pièce que ce rédacteur peut lire ; la borne tient lieu d'attendu | — |
| prix unitaire, indicatif | 0,80 à 1,30 USD/h (central 1,00) | devis de la phase 0 (`16d71feb…`), ligne « Instance de référence » |
| prix unitaire, relevés | 1,08 à 1,2133 USD/h en octobre (offres A100 SXM4 80 Go) ; 1,1833 USD/h le 2026-11-18 (instance 61276240) ; 1,22 USD/h stockage compris le 2026-11-19 (instance 61414494) | `registres/depenses.md`, lignes de ces dates |
| plafond de prix horaire | **1,50 USD/h**, stockage compris (valeur implicite de GO-2026-10-17-01 : 6 USD pour 4 heures) | `registres/go.md`, GO-2026-10-17-01 |
| réseau | prix au gigaoctet lu sur l'offre ; relevés : 0,038 USD/Go (2026-10-04) et 0,026 USD/Go (2026-11-19) | `registres/depenses.md`, lignes de ces dates |
| pire cas de carte | 4 h × 1,50 USD/h = **6,00 USD** | calcul sur les deux bornes ci-dessus |
| reste pour le réseau et le disque hors marche | 10,00 − 6,00 = **4,00 USD** ; au-delà, pas de création (§ 5) | plafond du § 4 |

## 4. Ligne à inscrire

Ligne de type « calcul » proposée pour `registres/go.md`, à inscrire sur le mot du directeur :

> pilote du papier C (étape 1 du préenregistrement scellé de HC1 à HC3 ; devis `devis-pilote-papier-C-v1`, chemin et
> empreinte de sa version scellée) : 4 heures de carte au plus en cumul ; deux lancements au plus, le second
> seulement après une perte par l'hôte ou un arrêt par une garde ; plafond de prix 1,50 USD/h ; **plafond 10 USD,
> tout compris** (carte, stockage, réseau) ; lancé seulement après le scellement du préenregistrement contre-lu, de
> sa configuration, de son module et de l'addendum de lancement ; ligne d'accord du jour exigée à chaque lancement ;
> échéance 2026-12-31.

Ce que cette ligne reprend sans le changer : les 4 heures de GO-2026-10-17-01 ; les 10 USD au plus par lancement de
la délégation GO-2026-10-20-07, qui deviennent ici un plafond pour le pilote entier, plus serré ; l'accord du jour
par lancement. Ce qu'elle change : le pilote a son propre plafond et sa propre échéance, et ne dépend plus de la
date de l'enveloppe de la phase 0 (GO-2026-10-04-08, prolongée par GO-2026-10-20-06 puis GO-2026-11-22-93). **Un
point à dire avec le mot** : si ce plafond se compte dans les 150 USD de l'enveloppe de la phase 0, ou à part ; la
ligne proposée le compte à part, pour qu'aucun autre chantier ne puisse le consommer.

## 5. Ce qui arrête la dépense

- Avant toute carte : essais du module et banc de reproduction sur processeur ; échec : arrêt, aucune location.
- Préalables (liste d'arrêt 2 du texte) : texte scellé et contre-lu, verdict complété de P3, addendum de lancement
  scellé (adaptateur réel, décision D-20), ligne de type « calcul » valide au jour du lancement, ligne d'accord du
  jour ; l'un manque : arrêt avant la création de l'instance.
- Avant la création : prix de l'offre au-dessus de 1,50 USD/h, ou réseau estimé (taille des trois modèles aux
  révisions figées × prix au gigaoctet de l'offre) plus disque au-dessus de 4,00 USD : pas de création.
- Borne du lanceur : durée = min(4 heures moins les heures déjà consommées, ce que le reste du plafond permet au
  prix relu) ; à la borne et à la fin, l'instance s'arrête par son identifiant (R10), consigné dans
  `registres/arrets.md`.
- Prix relu après création au-dessus du plafond de prix : destruction aussitôt, par l'identifiant.
- Toute garde de la liste d'arrêt du texte qui dit « arrêt » ou « nœud » : arrêt du run, instance arrêtée.
- Récupération avant destruction (consigne du programme) : inventaire des sorties (noms, tailles, empreintes),
  versement scellé, puis seulement destruction.

## 6. Hors devis

- L'étape 2 (décisive : TC.1 à TC.3) et le bras « saboteur sans consigne » (décision D-23), qui demandent un devis
  et un accord à part, après la porte G0.
- Le bras « contrôlabilité » et son banc ; les lectures de sondes ; toute génération par l'agent.
- La grille de la clause de repli, les essais du module, la dérivation : sur processeur, sans dépense.
- Un rejeu du pilote au-delà du cumul de 4 heures, ou un troisième lancement : nœud.
- Tout appel à un modèle par une interface payante : il n'y en a aucun dans le pilote.

## 7. Avant le lancement

1. Contre-lecture de ce devis par un autre modèle, corrections, scellement par la session mère.
2. Mot du directeur ; inscription de la ligne de type « calcul » dans `registres/go.md`.
3. Scellement du préenregistrement, de la configuration, du module ; addendum de lancement scellé.
4. Contrôle du crédit du loueur ; création par identifiant avec `GO_ID`.

## 8. Non vérifié par ce rédacteur

Le débit des lectures (d'où la durée attendue) ; la taille de Qwen2.5-7B-Instruct et de Mistral-7B-Instruct-v0.3 ; le
nombre de variantes et de réponses imposées de la configuration (les décomptes du § 1 sont par variante essayée) ;
les décomptes du § 1 sont recalculés par moi d'après le texte, non d'après la configuration, qui n'est pas écrite.
