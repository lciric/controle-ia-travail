# Devis — une consultation du collisionneur sur la question v8 « modes de sabotage » — v1

> Écrit par Claude Opus 5.5 (sous-agent, effort maximal) à la place de Fable 5.2, dont le quota de l'abonnement est épuisé jusqu'au 29 novembre 2026 à 18:00 UTC (R-5071, `registres/decisions.md` l. 5211) : écart à R-3735 et à GO-2026-11-21-75 déclaré, sur GO-2026-11-22-145 (`registres/go.md` l. 831). Commande : GO-2026-11-23-03 (`registres/go.md` l. 841). 23 novembre 2026, 05:05 UTC (`date -u`). Pièce de classe A (devis), **non scellée** : contre-lecture par un Opus neuf, vérification des corrections par le même, puis remise à Lazar. **Elle n'autorise aucune dépense.**
>
> Fait sans envoi à un modèle, sans dépense, sans commit. Rien lu sous une branche `coffre/*` ni dans un chemin qui contient « coffre » : la porte d'admissibilité v5 n'est pas lue, seule son empreinte, donnée par la commande, est citée. Aucune cellule d'un dossier de modes, d'attaques, de quarantaine ou de mode tenu à l'écart n'a été ouverte : le relevé exclut par programme tout dossier dont le nom touche ces mots (§ 13). Deux branches de courses récupérées en lecture seule (références locales) pour leurs journaux ; mots et caractères des cellules comptés par programme, jamais affichés. Commande `devis` des moteurs jouée en local, sans réseau.

## 0. En bref

1. **Telle quelle, la question v8 ne part pas.** Servie depuis son titre, elle est refusée avant tout envoi par la garde de motifs de tous les moteurs du collisionneur : 19 chemins internes et 3 identifiants d'accord (§ 3). Préalable neuf : une version servie qui ne change que la provenance (décision 1, § 11).
2. **Ce préalable levé**, une consultation de cinq espèces à l'étage III coûte **≈ 10,6 USD attendus** (12,1 au haut) ; pire cas sans relance 40,2 USD ; borne absolue, toutes relances du moteur épuisées, 99,1 USD, que le plafond rend inatteignable. **Plafond proposé : 25 USD** (décision 2, § 11).
3. **Les quatre réserves** (§ 5) : la longueur tient sans toucher la consigne (tours de conception et de réponse à 3 500 mots, au-dessus des ≈ 3 300 demandés) ; Astra tient à 8 000 jetons (marge 13 %) et passe à 128 000 par l'option `--sortie-max`, déjà contre-lue ; l'arithmétique de la garde tient pour toutes les espèces, Carbon avec la marge la plus mince (10 %) ; préalable 2 : **tenu** pour toutes les espèces, **sous réglage** pour Astra.

## 1. Objet et périmètre

- **Une consultation** (GO-2026-11-23-03) : un dossier, un passage, sans héritage, **étage III seul**. Ses trois tours — conception (III.1), critique croisée (III.2), réponse (III.3) — sont les trois tours de la question (v8 l. 128, 141, 143).
- **Étages I et II non joués.** Les deux devis modèles chiffrent trois étages parce que la commande `devis` du moteur les imprime tous : 88,60 USD = 21,09 + 34,87 + 32,64 (`devis-v8d-six-especes-question-collisionneur-v3-v1.txt` l. 19, 38, 57) ; 58,77 USD = 13,45 + 23,87 + 21,45 (`devis-commande-collisionneur-v9-v2-dopamine-v1.txt` l. 19, 38, 57). Les dossiers comparables servis par l'abonnement le 22 novembre n'ont joué que l'étage III, en quatre heures environ, kits compris (journaux, § 13).
- **Texte servi** : la v8 depuis son titre (sa ligne 1 : « Le texte à servir commence au titre »), dans la version servie de la décision 1. Le même fichier va en faits et en question, comme l'a proposé le devis « modes et attaques » v3 (l. 143), accordé par Lazar (GO-2026-11-21-08, `registres/go.md` l. 607). Le moteur exige un fichier de faits pour un dossier neuf (`collisionneur_v9_v8d.py` l. 2794-2796) et met les deux blocs dans chaque invite (l. 877, 883-886).
- **Pas de resserrement en cours de service.** La règle « on resserre la question servie à chaque coupure » (GO-2026-11-22-109, point 3, `registres/go.md` l. 795) visait le collisionneur « modes et attaques » ; ici la commande fixe une consultation unique. Un refus mène à une absence décidée, jamais à une question réécrite.
- **Moteur recommandé : `collisionneur_v9_v8m.py` sous la voie abonnement v6, avec `--sortie-max`** — l'attelage des trois dossiers du protocole X servis par l'abonnement le 22 novembre (conscience et anesthésie, deux dossiers ; puits étroits).
  - Le v8d de `main`, nommé dans la commande, ne suffit pas pour la composition recommandée : il ne sait pas servir une espèce Claude par l'abonnement, que Lazar veut à la place de l'interface payante (GO-2026-11-22-70, `registres/go.md` l. 757), ni relever le premier plafond d'Astra sans code neuf.
  - Le v8m est le v8d plus les changements v8g à v8m (acceptation nommée d'un motif dans une cellule, espèces neuves, `--sortie-max`, `--effort-max`, rejeu d'effort). **Tours, consignes, préambule, motifs de la garde et catalogue des six espèces y sont identiques à ceux du v8d** (comparaison par programme, § 13).
  - Il est sur la branche `runs/collisionneurs-reprise-v8d-v1` (470f7e6f…), pas sur `main`. Vérifié « conforme » après corrections (`docs/notes/collisionneur-v9/verification-corrections-collisionneur-v9-v8m-opus-v1.md`, 6f8dcf86…, même branche) ; voie abonnement v6 contre-lue « conforme », corrections conformes (`…/abonnement-v1/contre-lecture-voie-abonnement-v6-opus-v1.md`, 10adda04…).
  - Les versions plus récentes de la même branche ne conviennent pas : v8n et v8o (ajout d'une espèce après coup) ne sont pas branchées sur la voie abonnement, qui ne connaît que v8m et v8p (`voie_abonnement_v6.py` l. 80-83) ; v8p impose des duels balisés aux tours III.1 et III.3, qui contrediraient la forme de la question.
  - Le v8d tel quel reste l'option (c) de la décision 2.

## 2. Préalables, avant tout envoi

| | préalable | état |
|---|---|---|
| P1 | Source 19 (question v5 servie le 22 novembre) versée hors du coffre | **fait** : empreinte c8cd5f2c… vérifiée sur la copie du bloc-notes partagé ; la branche `service/collisionneur-modes-v8-v1` existe au commit c43204f7… (référence distante relevée, contenu non relu) |
| P2 | Longueur d'un tour ≥ 3 300 mots | **tenu**, sous réglage pour Astra (§ 5.4) |
| P3 | Garde de motifs (**neuf**) | **bloquant** : la v8 ne passe pas ; version servie à faire (§ 3, décision 1) |
| P4 | Opératrice et rangement | une session opératrice cloisonnée ; versement vers une branche de coffre neuve (§ 8) |
| P5 | Clés et crédit | `GEMINI_API_KEY` (Argon, Carbon, Neon) et `OPENAI_API_KEY_2` (Astra, GO-2026-11-22-111, `registres/go.md` l. 797) : présence lue par leur nom et crédit relu avant le lancement ; aucune dépense d'Anthropic dans l'option recommandée |
| P6 | Ce devis | contre-lu par un Opus neuf, corrections vérifiées, puis GO de Lazar sur les deux décisions (§ 11) ; les fichiers de calcul du § 13 versés d'abord à côté de ce devis (R6) |

## 3. Le préalable neuf : la garde de motifs refuse la v8

**Ce que fait la garde.** Avant tout envoi, le moteur cherche dans l'invite entière des motifs interdits : nom de personne, identifiant de session, courriel, chemin interne, identifiant d'accord, identifiant de registre (`collisionneur_v9_v8d.py` l. 552-568 ; chemins internes l. 560-565 ; identifiants d'accord l. 566).
- Un motif trouvé : refus nommé, code 7, rien n'est envoyé ni retiré du texte (l. 589-599 ; appel avant chaque envoi, l. 1932).
- La voie abonnement fait la même garde avant d'écrire un kit (`voie_abonnement_v6.py` l. 39 et 193).
- Le v8m a les mêmes motifs. Son acceptation nommée n'admet que la catégorie « chemin interne », et seulement dans le bloc d'une cellule écrite par un modèle, jamais dans la question (`collisionneur_v9_v8m.py` l. 116-118 et 753).

**Ce qu'elle trouve** sur la v8 servie depuis son titre (33 925 caractères ; 5 717 mots au découpage de Python, la commande en compte 5 555 sur le fichier entier ; empreinte du texte servi depuis le titre, calculée ici et non versée : 38a1a8e9…) :
- **19 chemins internes**, tous dans la table des sources (v8 l. 159 à 168, 170 à 176 et 179 ; le nom du dépôt y figure, l. 159) ;
- **3 identifiants d'accord** (fait 16, l. 77 ; fait 17, l. 78 ; source 21, l. 179) ;
- la ligne 169 (`donnees/…`) n'est pas prise par la garde mais relève de la même règle.

**Précédents.**
- Les questions « modes » et « attaques » ne partaient que si elles passaient la garde de motifs, « aucun chemin interne, aucun nom » (GO-2026-11-21-08, `registres/go.md` l. 607).
- « Les textes sont corrigés à la source, au prix d'une version de plus et d'une contre-lecture » (GO-2026-11-22-95, l. 782).
- Contrôle par programme avant scellement (devis « modes et attaques » v3, l. 15).

**Version servie proposée** (décision 1, option a ; nom neuf, R12 : `question-collisionneur-modes-sabotage-v8-servie-v1.md`) :
1. le texte depuis le titre, sans la ligne 1 ;
2. faits 16 et 17 : « [source 21, ligne de GO-…] » devient « [source 21, décision du 22 novembre 2026 sur …] », sans identifiant ;
3. table des sources : la colonne « Chemin » ne garde que la description déjà écrite entre parenthèses, les empreintes restent ; source 21 devient « registre des accords du programme, cinq lignes du 22 novembre 2026 », ses deux empreintes gardées ; source 11 traitée de même ;
4. rien d'autre ne change : chaque remplacement fait à texte exact par programme, le diff versé, la garde repassée par programme (zéro refus exigé), contre-lecture courte par un Opus neuf ; le fait 4 garde sa coupe, comme Lazar l'a accordé (GO-2026-11-22-152, l. 838) ;
5. **le gardien du coffre** confirme que la porte d'admissibilité v5, scellée en visant l'empreinte de la v8 (047eeddf…), s'applique au texte servi, et dit quel texte les trieurs reçoivent. Recommandé : le texte servi, avec le diff de provenance, puisque c'est ce que les modèles auront lu.

Coût : 0 USD ; environ une heure.

## 4. Composition et réglages recommandés

| lettre | espèce | voie | prix compté (USD par million, entrée / sortie) | plafond, premier envoi / relance | provision de réflexion | réflexion ou effort | délai d'un envoi | relances du moteur |
|---|---|---|---|---|---|---|---|---|
| A | Opus 5.5 (`claude-opus-5-5`) | abonnement : kit, session fille éphémère sans dépôt | 4 / 20, pour la marge exigée avant le kit seulement ; coût d'interface zéro | 128 000 (marge) | 0 | effort « high » | session | aucune par cette voie |
| B | Argon (`gemini-4-argon`) | interface, flux | 4 / 20 (facturé 2 / 10 jusqu'au 30 novembre) | 65 536 / 65 536 | 16 384 | niveau « high », le plus haut admis | 10 800 s | relance identique, puis dernier recours au niveau « medium » |
| C | Astra (`gpt-6.2-astra`) | interface, arrière-plan | 10 / 50 (barème de `gpt-6-astra`, supposé) | 128 000 / 128 000 | 0 | aucun réglage envoyé | 10 800 s | une relance |
| D | Carbon (`gemini-4-carbon`) | interface, flux | 4 / 20 (facturé 2 / 10 jusqu'au 1er décembre, rapporté) | 65 536 / 65 536 | 49 152 | niveau « high » | 10 800 s | relance identique, puis dernier recours « medium » ; pas de repli par lot |
| E | Neon (`gemini-4-neon`) | interface, flux | 3 / 15 | 65 536 / 65 536 | 32 768 | niveau « xhigh », le plus haut admis | 10 800 s | relance identique, puis dernier recours « high » |

Sources :
- catalogue et prix : `collisionneur_v9_v8d.py` l. 219-244 et 315-333, identiques au v8m ;
- plafonds sous `--sortie-max` : `collisionneur_v9_v8m.py` l. 458-465 (« 128,000 max output tokens » pour Astra, page d'OpenAI lue le 22 novembre) ;
- délais : même fichier, l. 484 (10 800 s, supposés, accordés par l'arbitre le 22 novembre) ;
- niveaux de réflexion : `garde_google_v3.py` l. 68-70 ;
- relances : `collisionneur_v9_v8d.py` l. 418, 1814-1821, 1965-1967 ; Carbon refusé par lot, l. 163-165 ;
- effort « high » pour une cellule de collisionneur : GO-2026-11-22-114 (`registres/go.md` l. 800) et `voie_abonnement_v6.py` l. 88 et 391-392 ; aucune relance par l'abonnement : même fichier, l. 29.

Pourquoi ces cinq :
- **une seule espèce Claude** : un mode imaginé par Claude a plus de chances d'être deviné par les concepteurs de moniteurs, qui sont des Claude (devis « modes et attaques » v3, l. 54, accordé par GO-2026-11-21-08) ;
- **Opus plutôt que Fable** : le quota de Fable est épuisé jusqu'au 29 novembre (R-5071) ; Fable est réservé aux pièces décisives, et une cellule de collisionneur n'en est pas une (`CLAUDE.md` l. 81-82). La voix Claude du passage « modes » du 22 novembre était Fable (`registres/depenses.md` l. 601) : Opus en donne une autre ;
- **sans Kimi**, comme Lazar l'a choisi pour la question « modes » (devis v3, l. 58 ; GO-2026-11-21-08) ;
- **Neon gardé** : Lazar l'a ajouté au collisionneur des modes (GO-2026-11-22-112, `registres/go.md` l. 798).

## 5. Les quatre réserves

### 5.1 Consignes de mots

- **Ce que la question demande** : six modes au plus (v8 l. 98), environ 500 mots par fiche (l. 124), puis une fin de réponse (l. 139), soit ≈ 3 300 mots aux tours de conception et de réponse. Elle garde la limite du tour : « si elle ne laisse pas la place de six fiches entières et de la fin de réponse, propose moins de modes » (l. 124).
- **Limites du moteur** (`collisionneur_v9_v8d.py` l. 460-469, ligne de format l. 495 ; identiques au v8m) : III.1 conception 3 500 ; III.2 critique croisée 3 000 ; III.3 réponse 3 500 ; I.1 « méta » 2 500.
- **Constat** :
  - tours III.1 et III.3 à 3 500 mots, au-dessus des 3 300 demandés : **la v8 se sert sans relever la consigne** ;
  - tour III.2 à 3 000 mots : la question n'y demande aucune fiche ; avec cinq espèces, chacune critique au plus 24 modes, soit au moins 125 mots par mode ; tenu pour la forme demandée, au prix d'une critique serrée ;
  - tour I.1 à 2 500 mots : non tenu, mais il n'est pas joué (§ 1).
- **Relever la consigne** demanderait un moteur neuf (la table des tours est une constante, sans option), pièce d'instrument à contre-lire. Et la garde de Google refuserait Carbon au-delà de 3 900 mots (§ 5.3). **Non recommandé pour ce service.**
- **Relevé** :
  - par l'abonnement, Opus a rendu 12 cellules de l'étage III le 22 novembre, toutes valides : de 3 718 à 3 948 mots au tour III.1, de 3 685 à 3 825 au tour III.3 ;
  - les trois espèces de Google dépassent la consigne : médianes de 4 328 à 5 721 mots par tour ;
  - Astra écrit court : médianes de 1 855 à 2 619 mots, au plus 2 976. Il proposera peut-être moins de fiches, ce que la question admet ; ce n'est pas une troncature.

### 5.2 Astra

- **Au v8d**, le premier envoi est plafonné à 8 000 jetons, raisonnement compris (`collisionneur_v9_v8d.py` l. 325-326 ; corps de l'envoi l. 1430 ; raisonnement ajouté à la sortie l. 1488-1492), avec une relance à 32 000.
- **Relevé** sur 64 réponses d'Astra à l'étage III (§ 13) : toutes valides, aucune coupée, à 8 000 comme à 128 000 ; sortie la plus longue 4 797 jetons ; raisonnement au plus 104 jetons ; de 1,58 à 1,83 jeton par mot rendu en médiane selon le tour, 1,98 au plus.
- **Arithmétique** : 3 300 × 1,98 = 6 534, sous 8 000 ; à la limite du tour, 3 500 × 1,98 = 6 930, sous 8 000. **8 000 suffit, avec 13 % de marge.**
- **Proposé** : `--sortie-max`, qui porte Astra à 128 000 dès le premier envoi (`collisionneur_v9_v8m.py` l. 461 et 465). L'option est déjà contre-lue et a servi le 22 novembre ; aucun code neuf.
- **Coût** : rien sur l'attendu, puisque Astra s'arrête de lui-même. La marge exigée avant chaque envoi d'Astra passe de 2,6 à 7,4 USD au plus, et le plafond proposé de 21 à 25 USD (§ 6.5).
- **Variante** : garder 8 000 (sans `--sortie-max`). Une coupure ferait perdre au plus 1,44 USD et coûterait une relance à 32 000 d'au plus 2,64 USD (§ 6.2).

### 5.3 L'arithmétique de la garde, espèce par espèce

- **Règle (3) de la garde de Google** : ⌈mots × jetons par mot⌉ < plafond − provision (`garde_google_v3.py` l. 148-150).
- **Jetons par mot** : Argon 5,1, Carbon 4,2, Neon 5,1 (l. 80). C'est le plus haut mesuré par espèce, en jetons de texte par mot de la limite du tour (l. 3-8).
- **Plancher** : 16 000 jetons de texte au-delà de la réflexion (l. 77 ; `CLAUDE.md` l. 63-67).
- Le moteur vérifie cette règle avec la limite du tour, avant chaque envoi (`collisionneur_v9_v8d.py` l. 1947-1959 et 2003-2012).
- Pour les espèces hors de Google, aucune garde : même calcul, avec le plus haut rapport relevé ici (jetons de sortie, réflexion comprise, par mot rendu).

| espèce | plafond de texte | 3 300 mots | 3 500 mots (limite du tour) | marge à 3 500 | plus longue sortie relevée (texte seul chez Google, sortie entière ailleurs) |
|---|---|---|---|---|---|
| Argon | 65 536 − 16 384 = 49 152 | × 5,1 = 16 830 | 17 850 | 31 302 | 20 107 |
| Carbon | 65 536 − 49 152 = 16 384 | × 4,2 = 13 860 | 14 700 | **1 684 (10 %)** | 15 013 |
| Neon | 65 536 − 32 768 = 32 768 | × 5,1 = 16 830 | 17 850 | 14 918 | 13 378 |
| Astra | 8 000 (128 000 sous `--sortie-max`) | × 1,98 = 6 534 | 6 930 | 1 070 (13 %) | 4 797 |
| Opus par l'interface (option c) | 64 000 | × 9,14 = 30 162 | 31 990 | 32 010 | 35 140 |
| Fable par l'interface (option c) | 49 000, relance 64 000 | × 12,52 = 41 316 | 43 820 | 5 180 (11 %) | 41 494 |

**Tout tient.** Carbon a la marge la plus mince :
- sa garde refuserait une consigne au-delà de 3 900 mots (⌈3 900 × 4,2⌉ = 16 380 < 16 384 ; ⌈3 901 × 4,2⌉ = 16 385) ;
- une sortie de Carbon au-delà de 16 384 jetons de texte finirait coupée, puis déclencherait la relance identique et le dernier recours. Sur 56 essais de Carbon à ces réglages, aucune n'a été relevée (§ 6.1).

### 5.4 Préalable 2 : verdict par espèce

| espèce (voie) | verdict | appui |
|---|---|---|
| Argon (interface) | **tenu** | § 5.3 ; médianes de 5 127 à 5 721 mots rendus par tour |
| Carbon (interface) | **tenu**, marge la plus mince | § 5.3 |
| Neon (interface) | **tenu** | § 5.3 |
| Astra (interface) | **tenu sous réglage** (`--sortie-max`) ; tenu à 8 000 avec 13 % de marge | § 5.2 |
| Opus (abonnement) | **tenu** | aucun plafond d'interface ; 12 réponses valides, plus de 3 300 mots aux tours III.1 et III.3 (§ 5.1) |
| Fable (abonnement, option b) | **tenu** | 12 réponses valides le 22 novembre, de 3 221 à 3 893 mots aux tours III.1 et III.3 |
| Opus et Fable (interface, option c) | **tenu** ; Fable avec 11 % de marge | § 5.3 |

Aucune espèce n'est « non tenu ». Hors de l'étage III, le tour « méta » à 2 500 mots ne tiendrait pas : ne pas y servir la v8.

## 6. Coût

### 6.1 Méthode

- **Invites.** Construites par les fonctions du moteur v8m (les mêmes que celles du v8d), dans un dossier temporaire, sur le texte servi depuis le titre. La version servie ne change que la provenance : sa taille ne bouge que de quelques centaines de caractères. L'invite du tour III.1 fait 70 572 caractères, dont deux fois les 33 925 de la question.
- **Pièces des tours III.2 et III.3.** Taille médiane des cellules relevées par espèce et par tour pour l'attendu ; taille maximale relevée pour la borne. La borne du moteur, mots permis × 7 caractères (`collisionneur_v9_v8d.py` l. 2564-2565), sous-estime les espèces de Google : Argon a rendu jusqu'à 65 748 caractères au tour III.1.
- **Attendu.**
  - entrée = caractères ÷ caractères par jeton mesurés en médiane (Google 3,26 à 3,62 ; Astra 3,29 à 3,94) ;
  - sortie = médiane relevée des jetons facturés, réflexion comprise, par espèce et par tour ;
  - prix de la table ;
  - plus l'espérance des pannes : taux relevé × coût compté au pire.
- **Haut.** Sorties au 90e centile, pièces au maximum relevé.
- **Pire cas d'un envoi.** La formule du moteur : garde d'entrée = ⌈⌈caractères ÷ 2,5⌉ × 1,01⌉ + 32 au prix d'entrée, plus plafond et provision au prix de sortie (`collisionneur_v9_v8d.py` l. 431 et 1592-1601). Au lancement, le compte réel des jetons remplace les 2,5 caractères par jeton (relevé : au moins 3,05 chez Google et Astra) : ce pire cas majore donc celui du moteur.
- **Prix.** Comptés à la table, comme le journal du moteur. Avant le 1er décembre, Argon et Carbon sont facturés moitié moins (`collisionneur_v9_v8d.py` l. 226-228 et 234-235) : la dépense facturée de l'option recommandée serait alors d'environ 3 USD sous la dépense comptée. Le plafond se lit sur la dépense comptée.
- **Relevé.** 32 dossiers de l'étage III, 417 essais. Taux de panne aux réglages actuels : Carbon 7 sur 56 (12,5 %, toutes des coupures de flux) ; Argon 5 sur 62 (8,1 % : 4 coupures, 1 refus) ; Neon 1 sur 26 ; Astra 0 sur 64.

Programmes et sorties : § 13.

### 6.2 Option recommandée, cellule par cellule (USD)

| cellule | modèle | entrée attendue (jetons) | sortie attendue (jetons) | attendu | pire sans relance | pire avec relances | marge exigée avant l'envoi |
|---|---|---|---|---|---|---|---|
| III.1 conception A | Opus, abonnement | — | — | 0,00 | 0,00 | 0,00 | 2,67 |
| III.1 conception B | Argon | 19 486 | 24 203 | 0,56 | 1,75 | 5,26 | 1,75 |
| III.1 conception C | Astra | 17 919 | 2 963 | 0,33 | 6,69 | 13,37 | 6,69 |
| III.1 conception D | Carbon | 19 483 | 33 819 | 0,75 | 2,41 | 7,22 | 2,41 |
| III.1 conception E | Neon | 19 795 | 34 709 | 0,58 | 1,56 | 4,68 | 1,56 |
| III.2 critique A | Opus, abonnement | — | — | 0,00 | 0,00 | 0,00 | 2,95 |
| III.2 critique B | Argon | 49 023 | 31 842 | 0,83 | 1,97 | 5,92 | 1,97 |
| III.2 critique C | Astra | 55 864 | 4 007 | 0,76 | 7,44 | 14,88 | 7,44 |
| III.2 critique D | Carbon | 50 300 | 43 090 | 1,06 | 2,66 | 7,97 | 2,66 |
| III.2 critique E | Neon | 50 175 | 42 520 | 0,79 | 1,76 | 5,28 | 1,76 |
| III.3 réponse A | Opus, abonnement | — | — | 0,00 | 0,00 | 0,00 | 2,98 |
| III.3 réponse B | Argon | 64 865 | 21 848 | 0,70 | 2,06 | 6,19 | 2,06 |
| III.3 réponse C | Astra | 66 401 | 4 191 | 0,87 | 7,42 | 14,84 | 7,42 |
| III.3 réponse D | Carbon | 65 591 | 34 491 | 0,95 | 2,71 | 8,13 | 2,71 |
| III.3 réponse E | Neon | 67 672 | 37 488 | 0,77 | 1,78 | 5,34 | 1,78 |
| **total** | | | | **8,95** | **40,21** | **99,07** | la plus grande : **7,44** |

- **Espérance des pannes** comptées au pire : 1,63 USD. **Attendu avec pannes : 10,59 USD** ; haut : 10,47 + 1,63 = **12,10 USD**.
- **Par clé**, attendu sans pannes : `GEMINI_API_KEY` 6,99 ; `OPENAI_API_KEY_2` 1,96 ; Anthropic 0. Les pannes attendues tombent toutes sur la clé de Google.
- **Sans `--sortie-max`** : même attendu ; pire sans relance 22,21 ; avec relances 66,67 ; plus grande marge 2,71. Astra coûte alors au pire 0,69, 1,44 et 1,42 au premier envoi, et 1,89, 2,64 et 2,62 de marge avec la relance.
- **Rapprochement** : sur les trois dossiers servis par l'abonnement le 22 novembre (six espèces, les quatre mêmes par l'interface, questions plus courtes), la dépense comptée a été de 12,50, 12,59 et 9,03 USD. Les pannes en font 4,76 et 5,12 dans les deux premiers : deux coupures de Carbon chacun, plus un refus d'Argon dans le second (journaux, § 13 ; `registres/depenses.md` l. 604).

### 6.3 Totaux des options (USD)

| option | attendu avec pannes | haut avec pannes | pire sans relance | pire avec relances | plus grande marge | plafond proposé |
|---|---|---|---|---|---|---|
| (a) cinq espèces maintenant, Opus par l'abonnement, `--sortie-max` | 10,59 | 12,10 | 40,21 | 99,07 | 7,44 | **25** |
| (a) sans `--sortie-max` | 10,59 | 12,10 | 22,21 | 66,67 | 2,71 | 21 |
| (b) six espèces après le 29 novembre 18:00 UTC, Fable et Opus par l'abonnement, `--sortie-max` | 10,86 | 12,41 | 40,61 | 100,10 | 7,54 | 26 |
| (c) moteur v8d tel quel, tout par l'interface, cinq espèces (Opus) | 13,01 | 15,06 | 26,97 | 76,20 | 2,71 | 24 |
| (c) moteur v8d tel quel, six espèces (Fable et Opus) | 19,78 | 23,13 | 37,32 | 99,37 | 4,32 | 33 |

Pour comparaison, la commande `devis` du moteur, avec sa borne de pièces (mots × 7), donne pour l'étage III : 35,24 USD pour les six espèces du v8d, 47,38 pour les cinq espèces du v8m sous `--sortie-max` (sorties au § 13).

### 6.4 Règle des relances

- **Google** (Argon, Carbon, Neon), à plafonds égaux : après une sortie vide, coupée, ou arrêtée sans texte, une relance identique déclarée, puis un dernier recours déclaré, un niveau de réflexion plus bas au même plafond ; trois essais au plus (`collisionneur_v9_v8d.py` l. 418, 1814-1821, 1965-1967). D'où « pire avec relances » = 3 × pire.
- **Astra** : une relance au plafond de relance ; 2 × pire.
- **Opus par l'abonnement** : aucune relance par la voie (`voie_abonnement_v6.py` l. 29). Une réponse vide ou coupée laisse la cellule absente ; l'arbitre décide.
- **Coupure de flux, délai, erreur du serveur, refus de crédit** : le moteur s'arrête, compte l'envoi au pire et ne renvoie jamais (`collisionneur_v9_v8d.py` l. 15-16 et 2083-2085). C'est une panne technique : la cellule a droit à **une** relance sur le même accord (GO-2026-11-22-77, `registres/go.md` l. 764 ; `CLAUDE.md` l. 75-76).
  - La relance se fait par une commande neuve sur le même dossier, sous le même plafond, et s'inscrit comme « faux échec » avec son issue codée.
  - Argon et Neon peuvent passer par le lot, à moitié prix (`--repli-lot`) ; Carbon non (l. 163-165).
  - Une seconde panne de la même cellule : l'arbitre décide (absence acceptée, consignée) ; une troisième tentative demande le mot de Lazar.
- **La borne absolue** (99,07 USD) suppose que chaque cellule épuise ses relances au plafond. Elle n'est pas atteignable : **le plafond borne la dépense**. Le moteur refuse avant l'envoi tout essai dont le pire cas ferait dépasser le plafond du dossier ou la ligne (l. 2014-2022 ; la voie fait de même avant chaque kit, `voie_abonnement_v6.py` l. 189-204).

### 6.5 Plafond proposé

- **Formule** : plafond = haut avec pannes + plus grande marge exigée avant un envoi + réserve de deux relances après panne technique de Carbon au tour le plus long, arrondi à l'unité supérieure.
- **Option recommandée** : 12,10 + 7,44 + 2 × 2,71 = 24,96, soit **25 USD**. La valeur est posée à la fois en plafond du dossier (`--plafond-usd 25`) et en ligne (`--ligne-usd 25`).
- **Lecture** : le point le plus haut du chemin attendu est le départ de la réponse d'Astra. Environ 7,5 USD sont alors dépensés, pannes attendues comprises ; avec la marge de 7,42, on arrive vers 15 USD. Le plafond laisse donc place à environ quatre pannes de plus, comptées au pire.
- **Plafond atteint** : refus avant l'envoi, code 4, rien ne part. Rien ne repart sans une ligne de reprise accordée par Lazar (`--ligne-reprise-usd` avec son GO, `collisionneur_v9_v8d.py` l. 166-169).
- **Hors du plafond, à 0 USD** : la version servie, les trieurs et la note de fin de dossier, tous par l'abonnement. S'ils devaient passer par une interface payante, ils feraient l'objet d'un devis à part.

## 7. Conditions d'arrêt

**Avant l'envoi** (rien ne part, 0 USD) :
1. garde de motifs, code 7 ; un chemin relatif inventé par un modèle dans une cellule peut être accepté nommément par l'arbitre (`--accepter-motif`), jamais un motif de la question ;
2. réglages de Google, code 1 : niveau explicite, plafond au moins égal à la provision plus 16 000, mots × rapport sous le plafond de texte ;
3. comptage d'entrée impossible ou invraisemblable, code 8 ;
4. plafond ou ligne, code 4 ;
5. espèces ou options autres que celles scellées dans le dossier, code 1.

**Pendant le service** :
6. panne technique, code 5 : § 6.4 ;
7. refus d'un modèle : définitif dans le dossier, jamais de reformulation ; l'arbitre accepte l'absence (`--accepter-absence`), consignée ;
8. modèle servi différent du modèle demandé, code 3 : arrêt ;
9. garde de dépense (code 6), réponse de Google sans pensées (code 10), sortie sans texte après le dernier recours (code 9) : arrêt, aucune relance au même réglage ; l'arbitre décide ;
10. **moins de trois conceptions valides** à la fin du tour III.1, relances faites : arrêt et nœud à Lazar, car une critique croisée sur deux pièces ne vaut plus la consultation ;
11. **cloisonnement** : toute lecture d'une cellule par la mère, par un concepteur de moniteur ou par un concepteur d'instrument de la vérité du dommage arrête le versement ; l'incident est consigné et le lecteur rayé de ces conceptions (devis v3, l. 133).

**À la fin** :
12. la commande `verifier` doit rendre « tout tient » sur le dossier avant le versement et le tri.

## 8. Qui lance, ce qui est versé, et où

1. **Opératrice.** Une session cloisonnée, neuve ou celle du 22 novembre, qui ne conçoit et n'a conçu aucun moniteur ni aucun instrument de la vérité du dommage, inscrite à « qui a lu quoi » avant le lancement.
   - Elle crée elle-même les trois sessions filles d'Opus, une par tour. La mère ne le peut pas sans lire les kits des tours III.2 et III.3, qui portent les modes des autres espèces.
   - Ses créations de sessions et ses poussées vers le coffre demandent le mot de Lazar dans sa session, comme le 22 novembre (R-4934, `registres/decisions.md` l. 5073).
2. **Pendant le service**, le dossier ne vit que dans le conteneur de l'opératrice, hors de tout `runs/` d'une branche lisible. L'option `--branche` de la voie pointe vers la branche de coffre du point 3, jamais vers son défaut, `runs/collisionneurs-reprise-v8d-v1`, qui est une branche lisible (`voie_abonnement_v6.py` l. 87 et 218).
3. **À la fin, ou à tout arrêt** (« récupérer ce qui est récupérable », `CLAUDE.md` l. 106-107) : archive et empreinte de chaque fichier, versées sur une **branche orpheline neuve de coffre**, avec sa règle d'ouverture écrite (gardien et Lazar).
   - Nom proposé : `coffre/service-collisionneur-modes-v8-v1`, que le gardien vérifie libre.
   - Y vont les cellules, tous les essais (refusés, coupés et interrompus compris), les kits et les réponses d'Opus, le journal, la composition, les consignes et l'état.
4. **Sur `main`, un inventaire seulement**, dans `docs/notes/service-collisionneur-modes-v8-v1/` : noms, tailles, empreintes, statuts, dépense par clé.
   - S'y ajoutent une ligne de dépense, une ligne de décision, et la version servie avec son diff et la sortie de la garde : aucune de ces pièces ne porte de mode.
   - Aucun texte de mode, aucun nom de mode (devis v3, l. 129-135 ; R-5022, `registres/decisions.md` l. 5162).

## 9. Tri après service : la porte d'admissibilité scellée v5

1. **Remise.** Après le versement, le gardien du coffre remet à **trois trieurs neufs**, qui n'ont jamais vu le coffre, la porte v5 (29c8a3c1…, au coffre, non lue ici), le texte servi et les réponses.
2. **Non-recouvrement**, vérifié par le gardien : aucun trieur n'a lu le coffre ; aucun ne conçoit de moniteur ni d'instrument de la vérité du dommage ; tous sont distincts de l'opératrice et des sessions d'Opus.
3. **La porte décide seule** : ses critères sont écrits et scellés avant le tour (v8 l. 124), et ce devis ne les restitue pas. À rapprocher par le gardien : la question annonce « deux trieurs indépendants » (l. 124), la commande en nomme trois.
4. **Sortie** : fiches et verdicts des trieurs scellés au coffre ; sur `main`, un inventaire seulement.
5. **Coût** : 0 USD par l'abonnement ; l'effort est fixé par le gardien selon GO-2026-11-22-114.

## 10. Note pédagogique de fin de dossier (Markdown et PDF)

- **Règle** : `CLAUDE.md` l. 69-70 (GO-2026-11-22-74). La note dit ce que chaque modèle propose, les accords et les désaccords, ce qui est neuf ou fragile, les références à vérifier, les propositions retenues et pourquoi. Le dossier n'est jamais « fini » sans elle.
- **Cloisonnement**, selon le précédent du dossier « modes d'attaque » (R-5022, `registres/decisions.md` l. 5162) :
  - la note est écrite après le tri, par un agent neuf qui n'a d'autre accès que le dossier versé et les sorties des trieurs ;
  - elle est scellée sur la branche de coffre du service, et lue par le gardien et Lazar ;
  - une fiche qui vise les lecteurs de la vérité du dommage va au gardien seul ;
  - la mère ne reçoit que des chemins et des empreintes.
- **Forme** : PDF fait par `docs/notes/collisionneur-v9/notes-de-sortie-v1/md_vers_pdf_v1.py` (branche `runs/collisionneurs-reprise-v8d-v1`, 6ba10aa9…), joint au compte rendu de fin de dossier, que le gardien transmet à Lazar.
- **Coût** : 0 USD par l'abonnement.

## 11. Décision demandée à Lazar

### Décision 1 — le texte servi (préalable)

**Décision.** Servir la v8 dans une version qui ne change que sa provenance (19 chemins internes et 3 identifiants d'accord), le fond restant mot pour mot.

**Enjeu.**
- Telle quelle, la v8 est refusée avant tout envoi par tous les moteurs.
- La garde existe pour qu'aucun chemin du dépôt, ni son nom, ni un identifiant d'accord ne parte chez Google ou chez OpenAI.
- La porte v5 a été scellée en visant l'empreinte de la v8.

**Options.**
- **(a) Version servie à provenance neutre** (§ 3).
  - Avantage : la règle de GO-2026-11-21-08 et de GO-2026-11-22-95 est tenue ; le fond est inchangé.
  - Inconvénient : une version de plus, une contre-lecture courte et l'accord du gardien sur la porte, environ une heure ; un écart à « telle quelle », que toi seul accordes.
- **(b) Moteur neuf qui exempte de la garde le bloc de la question.**
  - Avantage : texte servi au caractère près.
  - Inconvénient : chemins, nom du dépôt et identifiants d'accord partent chez deux fournisseurs ; c'est contraire à la condition de GO-2026-11-21-08 ; pièce d'instrument à écrire et à contre-lire.
- **(c) Ne pas servir.**
  - Avantage : aucun coût.
  - Inconvénient : aucun mode neuf pour les modes tenus à l'écart.

**Recommandation** : (a), confiance 0,85. **Pas de défaut** : nœud sur le texte servi d'une question visée par une porte scellée.

### Décision 2 — la dépense

**Décision.** Accorder une seule consultation du collisionneur, à l'étage III, sur la version servie de la v8, avec un plafond et une ligne de 25 USD.

**Enjeu.**
- Environ 10,6 USD attendus (12,1 au haut) pour des modes inédits, candidats au rôle de mode tenu à l'écart ; chaque lecture décisive en consomme un neuf (v8, fait 3).
- Le choix des espèces règle la diversité des voix, la part Claude et le délai.

**Options.**
- **(a) Cinq espèces maintenant** : Opus 5.5 par l'abonnement ; Argon, Astra, Carbon et Neon par l'interface ; moteur v8m sous la voie abonnement v6, avec `--sortie-max`. Plafond 25 USD (21 sans `--sortie-max`).
  - Avantage : une seule voix Claude ; Claude sans coût d'interface (GO-2026-11-22-70) ; départ dès les préalables levés ; Astra sans risque de coupure.
  - Inconvénient : pas de Fable ; trois sessions filles d'Opus à créer par l'opératrice, avec ton mot dans sa session ; moteur hors de `main`.
- **(b) Six espèces** après la remise du quota de Fable (29 novembre, 18:00 UTC), Fable et Opus par l'abonnement. Plafond 26 USD.
  - Avantage : une voix de plus.
  - Inconvénient : six jours d'attente ; deux voix Claude sur six ; Fable employé hors des pièces décisives.
- **(c) Moteur v8d de `main` tel quel, tout par l'interface, maintenant** : cinq espèces, plafond 24 USD, ≈ 13,0 USD attendus ; ou six espèces, plafond 33 USD, ≈ 19,8 USD attendus.
  - Avantage : moteur de `main`, sans session fille.
  - Inconvénient : de 2,4 à 9,2 USD attendus de plus ; Claude payé sur la clé d'Anthropic ; Astra à 8 000.

**Recommandation** : (a) avec `--sortie-max`, confiance 0,65. **Pas de défaut** : c'est une dépense.

## 12. Ce qui reste incertain

- **Prix d'Astra** : le barème de `gpt-6.2-astra` n'a pas été relu ; celui de `gpt-6-astra` est supposé (`collisionneur_v9_v8d.py` l. 230-233).
- **Délais** sous `--sortie-max` : supposés (`collisionneur_v9_v8m.py` l. 484).
- **Coût réel d'une coupure de Carbon** : inconnu ; il est compté au pire.
- **Longueurs** : relevées sur d'autres questions, plus courtes que la v8, qui demande six fiches structurées. Carbon, le plus serré, pourrait écrire plus long (§ 5.3).
- **Refus** : leur risque sur ce sujet n'est pas mesuré hors du coffre ; un refus d'Argon a été relevé sur un sujet voisin (§ 6.1).
- **Porte v5** : non lue. Le nombre de trieurs, le texte qu'ils reçoivent et l'objet du tri (fiches du tour III.1, du tour III.3, ou des deux) relèvent du gardien.

## 13. Sources, empreintes et calculs

Empreintes sha256 des fichiers entiers, relevées le 23 novembre 2026 vers 05:00 UTC. Les registres croissent par la fin : les lignes citées ne bougent pas.

| pièce | où | empreinte | lignes citées |
|---|---|---|---|
| question v8 | bloc-notes partagé, `…/svc-v8/service-collisionneur-modes-v8-v1/question-collisionneur-modes-sabotage-v8.md` ; branche `service/collisionneur-modes-v8-v1`, c43204f7… | 047eeddf… | 1, 3, 17, 77, 78, 98, 124, 128, 139, 141, 143, 153-179 |
| question v5 servie le 22 novembre (source 19) | même dossier du bloc-notes | c8cd5f2c… | — |
| moteur v8d | `docs/notes/collisionneur-v9/collisionneur_v9_v8d.py` (`main`) | b7803838… | citées au fil du texte |
| garde de Google v3 | `src/controle_ia/garde_google_v3.py` (`main`) | 923679b5… | 3-8, 68-70, 73-75, 77, 80-83, 148-150 |
| devis modèle, protocole X | `docs/notes/protocole-x-conscience-anesthesie-v1/devis-collisionneur/devis-v8d-six-especes-question-collisionneur-v3-v1.txt` | def3f890… | 19, 38, 57, 58 |
| devis modèle, « dopamine » | `docs/notes/papier-dopamine-moniteur-v1/devis-commande-collisionneur-v9-v2-dopamine-v1.txt` | a41c3d7b… | 19, 38, 57, 58 |
| devis « modes et attaques » v3 | `docs/notes/collisionneur-modes-et-attaques-v1/devis-collisionneur-modes-et-attaques-v3.md` | fadb7d09… | 15, 54, 58, 129-135, 143 |
| registre des accords | `registres/go.md` | 16830ee4… | 607, 757, 761, 764, 782, 795, 797, 798, 800, 831, 838, 841 |
| registre des décisions | `registres/decisions.md` | 2ebbbd2f… | 5073, 5162, 5211, 5229, 5256 |
| registre des dépenses | `registres/depenses.md` | bddf5b57… | 601, 604 |
| consignes permanentes | `CLAUDE.md` | 605db83a… | 63-67, 69-70, 75-76, 81-82, 106-107 |
| moteur v8m | `docs/notes/collisionneur-v9/collisionneur_v9_v8m.py`, branche `runs/collisionneurs-reprise-v8d-v1` (470f7e6f…) | 420394f9… | 116-118, 458-465, 484, 753 |
| voie abonnement v6 | `docs/notes/collisionneur-v9/abonnement-v1/voie_abonnement_v6.py`, même branche | d99f3358… | 29, 39, 56-66, 80-83, 87-88, 189-204, 218, 391-392 |
| vérifications du v8m | `…/verification-collisionneur-v9-v8m-opus-v1.md` et `…/verification-corrections-collisionneur-v9-v8m-opus-v1.md`, même branche | 81b7a6ad… ; 6f8dcf86… | verdicts |
| contre-lecture de la voie v6 | `…/abonnement-v1/contre-lecture-voie-abonnement-v6-opus-v1.md`, même branche | 10adda04… | verdict |
| outil Markdown vers PDF | `docs/notes/collisionneur-v9/notes-de-sortie-v1/md_vers_pdf_v1.py`, même branche | 6ba10aa9… | — |
| journaux | `runs/*/journal.jsonl` des branches `runs/collisionneurs-reprise-v8d-v1` (470f7e6f…) et `runs/collisionneurs-reprise-minuit-v1` (761c2c5a…) : 32 dossiers, 417 essais de l'étage III ; exclus par programme les dossiers dont le nom touche coffre, modes, attaques, sabotage, quarantaine, évasion, tenu ou coercition | — | champs `usage`, `cout_usd`, `statut`, `compte_entree`, `max_tokens`, `provision_reflexion` |

**Calculs.** Fichiers de travail, non versés, dans `/tmp/claude-0/-home-user/671ef03f-3066-5c11-8191-dd9cb263ed2c/scratchpad/devis-v8/`. **À verser par la mère avant la contre-lecture**, par exemple dans `docs/notes/service-collisionneur-modes-v8-v1/calculs-v1/` :

| fichier | empreinte | ce qu'il donne |
|---|---|---|
| `comparer_moteurs_et_garde_v1.py` → `sortie-comparer-moteurs-et-garde-v1.txt` | 58ecdeb0… → f46b1c9a… | v8d et v8m identiques (tours, consignes, préambule, motifs, catalogue) ; motifs trouvés par ligne (§ 3) |
| `servi/question-v8-depuis-le-titre.md` | 38a1a8e9… | texte servi depuis le titre, avant la version servie |
| `releve_journaux_v1.py` → `sortie-releve-journaux-v1.txt`, `releve-journaux-v1.json` | 6287bad1… → af161b76…, eec933e5… | mots rendus et jetons par mot, par espèce et par tour |
| `releve_journaux_v2.py` → `sortie-releve-journaux-v2.txt`, `releve-journaux-v2.json` | 22223250… → a43b8514…, 52cd710f… | coûts, sorties (médiane, 90e centile), tailles des cellules, caractères par jeton d'entrée, aux réglages actuels ; rejoué deux fois, identique |
| `releve_non_ok_v1.py` → `sortie-releve-non-ok-v1.txt` | 7c01a8af… → 25139741… | essais non valides, réglages et coûts comptés |
| `taux_pannes_v1.py` → `sortie-taux-pannes-v1.txt` | af4026fa… → b1a888c9… | taux de panne par espèce aux réglages actuels |
| `calcul_devis_v8_v2.py` → `sortie-calcul-devis-v8-v2.txt` | 8bfdbca7… → c96f9533… | tables des § 6.2 et 6.3, options (a), (a) sans `--sortie-max`, (b) et (c) à six espèces |
| `calcul_devis_v8_v2_option_interface.py` → `sortie-calcul-devis-v8-v2-option-interface.txt` | 0ff77783… → e8ee482b… | option (c) à cinq espèces |
| `sortie-devis-v8d-six-especes.txt` ; `sortie-devis-v8m-cinq-especes-sortie-max.txt` | dcfd4ff5… ; 6431b62d… | commande `devis` des moteurs (§ 6.3) |

**Rejeu** (sans réseau, après une récupération en lecture des deux branches de courses) :
- `python3 -I releve_journaux_v2.py releve-journaux-v2.json` ;
- `PYTHONPATH=src python3 calcul_devis_v8_v2.py collisionneur_v9_v8m.py question-v8-depuis-le-titre.md releve-journaux-v2.json` ;
- `PYTHONPATH=src python3 docs/notes/collisionneur-v9/collisionneur_v9_v8d.py devis --fable --opus --argon --astra --carbon --neon --faits Q --question Q`, où Q est le texte servi.

Tout changement de la question, d'une espèce ou d'un réglage demande de refaire ces calculs.
