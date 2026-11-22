# Devis de la passe X rallongée — course « nouvelles attaques » — v1

Pièce de travail, non scellée, à contre-lire. Auteur : Opus, 2026-11-22, relevé `date -u` 11:41Z. Processeur seul : aucun appel de modèle, aucun réseau, aucune clé lue, aucune dépense, rien écrit dans un dépôt.

- Programme : `calcul_devis_passe_x_v1.py` (même dossier). Sortie : `calcul-devis-passe-x-v1.json`. Joué deux fois, sorties égales à l'octet (`cmp`). Sept contrôles tenus (JSON l. 2-8). Les empreintes sont dans les compagnons `.sha256`.
- Sigles. **J** = la sortie JSON ; « J l. n » renvoie à sa ligne. **AV** = `controle-ia-travail/docs/notes/ideation-nouvelles-attaques-v1/additif-vehicule-na-projet-v2/additif-vehicule-na-projet-v2.md` (`6e9bb88e680211b1…`). **DV** = `main-lecture/prereg/ideation-nouvelles-attaques-v1/devis-course-nouvelles-attaques-v11.md` (`205e08f23ef9ced9…`). **V9** = `…/preenregistrement-court-course-nouvelles-attaques-v9.md` (`864f39a7ecd41a61…`). **CV** = `…/complement-valeurs-…-lot-1-v3.md` (`b4ef87dc6d5cce13…`). **AC** = `…/additif-1-complement-…-espece-3-sur-minuit-v2.md` (`ce76e0d6a0a6e65f…`). **PL** = `…/noeuds-et-part-luc-v2/recalcul-part-luc-153-v2.md` (`f71451b96dc9552a…`) et **PJ** = son `.json` (`3e0e06dcbfd31353…`). **LQ** = `…/proposition-liste-questions-ouvertes-passe-x-v1.md` (`e46bab3597169fdc…`). **TK** = `docs/sources/tarifs/kimi-2026-11-22/lecture-tarif-et-limite-kimi-v1.md` (`b1e4f3f061842725…`). **RQ** = `…/rapport-qualite-prix-modeles-v1.md` (`02463387aeea1699…`). **GO** = `main-lecture/registres/go.md` (`c40f367163c37f61…`).

## Résumé (moins de 350 mots)

**Pire de la passe X : 96,80 USD, sous le plafond de 200 USD, marge 103,20 (J l. 11, l. 169-174). Rien à couper.**

1. **Pièce fusionnée** : dix-sept corps sans titre, une ligne vide entre eux ; 19 921 signes, 20 570 octets (J l. 1256-1263). Entrée d'une requête : 6 811 jetons attendus, 10 217 au cas haut, 21 082 au pire, à un jeton par octet (J l. 337-341). Le mot « quarantaine » n'y figure plus (J l. 1258).
2. **Plafond de sortie : 96 000 jetons.** Chez Google, 64 000 de réflexion au plus et 32 000 de texte : la règle « réflexion + 16 000 » tient. Il est sous les 128 000 de Claude 4.6. Chaque tentative reste sous 6,05 USD même à 50 USD par million, ce qui cesse au-delà de 116 783 jetons (J l. 1473-1484). Sorties maximales des espèces 1 à 5 et de Kimi : **à relever**.
3. **Devis** : huit proposeurs, seize tentatives au pire, repli GO-35 lu à la lettre. Attendu 8,75 ; haut 24,84 ; pire calculé 44,40 ; **pire de lettre 96,80**, à 6,05 par tentative (P4, AV l. 129). Par clé : Luc 72,60 ; Google 12,10 ; OpenAI 6,05 ; Kimi 6,05 (J l. 158-165). Le plafond de 55 USD de GO-43 est dépassé. Les cinq espèces seules redonnent les 54,45 de X-10 (J l. 4).
4. **Additif** : lieux et lettre au § 4 (X-1 à X-11, Q2, Q9, L-1, P-lignes, arrêts n° 11, 12 et 38, appariement), avec la phrase sur le lot en quarantaine.

**Réserves.**
- GO-45 et GO-46 sont absents de la copie de `go.md` lue : je les prends au mandat.
- Les espèces 3 et 4 ne sont pas identifiées : je les compte à 10 / 50.
- Après la course, il ne resterait qu'environ 16,96 USD sur Luc : la passe X y exige un compte payant.
- **Point bloquant** : si GO-45 met aussi l'espèce 3 de la course sur Luc, la part de 136,04 ne tient plus (256,01 au cas haut).

## 1. Taille de la pièce fusionnée et entrée d'une requête

**Règle de formation** (lettre de X-3, AV l. 186, étendue sous (d)) :
- corps à l'octet, la ligne de titre « # … » retirée quand elle existe (neuf pièces) ;
- QN, puis QA, puis les quinze autres dans l'ordre du mandat (la liste de Lazar reste à nommer) ;
- une ligne vide entre deux corps, une fin de ligne finale.

| grandeur | valeur | source |
|---|---|---|
| dix-sept fichiers, titres compris | 21 404 signes, 22 127 octets | J l. 1256-1266 (`somme_…`) ; `wc` sur les fichiers |
| **pièce fusionnée** | **19 921 signes, 20 570 octets**, 47 points d'interrogation, empreinte `d93f1ec63bc63b59…` | J l. 1256-1263 |
| QN et QA | empreintes égales à celles de la table de l'additif | AV l. 23-24 ; J l. 3 |
| « quarantaine » | 1 occurrence dans le titre de la pièce du lot, **0 dans son corps**, 0 dans la pièce fusionnée | J l. 1258 ; J, pièce `…lot-quarantaine…` |

**Écart de compte avec LQ.** LQ l. 13-25 compte les signes **du fichier** (QN : 1 121 ; J l. 1277). Le corps servi en a moins (QN : 1 003). Le contrôle d'ancrage de LQ l. 25 a mordu sur le **titre** ; le corps servi ne porte pas le mot.

**Rapport signes par jeton.**
- *Attendu* : 3 signes par jeton, le bas de la fourchette « 3 à 3,5 » de LQ l. 34. Ce chiffre est dit, non mesuré.
- *Haut* : 2 signes par jeton. C'est plus prudent que les 2,5 octets par jeton de DV l. 211, parce que la pièce est dense en accents et en guillemets.
- *Pire* : 1 jeton par octet, la règle de DV l. 210.

Aucun tokeniseur n'a été joué : tous ces chiffres sont des règles, non des mesures. Pour le coût, l'écart est négligeable : l'entrée pèse au plus 0,21 USD par tentative (21 082 jetons à 10 USD par million).

**Entrée totale d'une requête.** C'est la question fusionnée seule (X-2, AV l. 185), plus une enveloppe bornée à 512 octets (valeur du rédacteur, à geler, K-2 (5), AV l. 229) :

| cas | jetons d'entrée | source |
|---|---|---|
| attendu | 6 811 | J l. 338 |
| haut | 10 217 | J l. 340 |
| pire | 21 082 | J l. 341 |
| *variante, si l'on ajoutait la synthèse servie (32 260 octets, DV l. 72) et la partie servie (3 205 octets, DV l. 97)* | 18 633 ; 27 949 ; 56 547 | J l. 344-347 |

Même dans cette variante, le pire de lettre ne change pas (96,80 USD, J l. 1088 et suivantes) : chaque tentative reste sous 6,05 USD.

## 2. Plafond de sortie

**Proposé : 96 000 jetons par tentative**, réflexion comprise, pour chaque (rôle de passe X, modèle). C'est un jeu A7 propre à la passe X (AV l. 82).

**Pourquoi.**
- *Le besoin.* Les dix-sept pièces demandent de l'ordre de cent éléments de réponse : numéros, puces, « pour chacune », 47 points d'interrogation (J l. 1260). À 150 à 300 jetons par élément, il faut 15 000 à 30 000 jetons de texte, plus des preuves (pièce « théorème négatif »).
- *Le texte visé.* Je vise 32 000 jetons de texte visible (J l. 1485, `texte_vise_jetons`), soit environ 96 000 signes, environ 1 900 jetons par question.
- *La réflexion.* La réflexion des espèces à effort haut consomme beaucoup. Chez Kimi, 32 765 jetons de raisonnement sur 32 768 ont déjà été pris, avec un contenu vide (RQ l. 52). Il faut donc une réserve d'au moins le double du texte.
- *La borne haute.* Au-delà de 116 783 jetons, une tentative au tarif de 50 USD par million dépasse 6,05 USD (J l. 1475). Le pire scellé (DV l. 119 ; P4 et P15, AV l. 129 et l. 143) cesserait alors de borner chaque tentative.

Le choix de 96 000 jetons garde 20 % de marge sous cette borne.

**Ce qu'il tient.**

| contrainte | tenue ? | source |
|---|---|---|
| sortie maximale de Claude Opus 4.6 et Sonnet 4.6 (128 000, référence de l'outil, non relue) | oui | mandat ; J l. 1484 |
| règle Google : plafond ≥ réflexion + 16 000 jetons de texte | oui, si le budget de réflexion des espèces 1 et 5 est fixé à **64 000 au plus** (il reste alors 32 000 jetons de texte) | AV l. 111 (G-6) ; J l. 1474, l. 1477 |
| sortie maximale des espèces 1, 2, 4 et 5, de l'espèce 3 et de Kimi | **inconnue** : aucune pièce lue ne la donne (TK ne la porte pas) | J l. 1478-1483 |

**Ce qu'il faut faire si une sortie maximale est plus basse.** Le plafond de ce modèle prend sa sortie maximale. Le coût baisse, sans autre écart. Pour Google, la réflexion devient au plus la sortie maximale moins 32 000 jetons, et jamais moins de 16 000 jetons sont laissés au texte.

**Réserve.** Une fin en plafond de jetons reste possible chez Google et chez Kimi. C'est un défaut journalisé, jamais rejoué (G-2 et G-6, AV l. 106 et l. 111). Je ne sais pas si Google facture la réflexion au-delà du plafond (RQ l. 37) : le pire suppose que non.

## 3. Devis par proposeur

**Tarifs**, en USD par million de jetons (J l. 1487 et suivantes).

| famille | tarif | source |
|---|---|---|
| espèces 1 et 5 (Google) | attendu 2/10 ; haut 4/20 ; pire 8,3/41,5 | RQ l. 25, l. 26 et l. 28 ; cités, non vérifiés |
| espèce 2 (OpenAI) | 10/50 | RQ l. 29 ; repris par citation |
| espèces 3 et 4 | 10/50, le plus haut tarif Claude cité ; leur identité est hors des pièces lues | RQ l. 31 |
| Kimi (`kimi-k3.1-pro`) | 2/10 | TK l. 10-11 ; vérifié sur page gardée |
| Opus 4.6 | 5/25 | mandat ; **non relu sur page officielle** ; même repère en PJ l. 92-103 |
| Sonnet 4.6 | 3/15 | mandat ; **non relu sur page officielle** ; même repère en PJ l. 96-107 |

**Règles des trois cas.** La sortie vaut 40 % du plafond pour l'attendu, 80 % pour le haut et 100 % pour le pire. L'entrée suit le § 1. Les tentatives se comptent ainsi :
- *attendu* : une tentative par proposeur ;
- *haut* : un repli servi pour les espèces 3 et 4 et pour l'ajout Opus 4.6 ;
- *pire* : la chaîne entière.

**Chaîne de repli au pire** (GO-35, GO l. 722 : « rejoué une fois sur claude-opus-4-6, puis […] sur claude-sonnet-4-6 »), en **lecture littérale** :
- espèces 3 et 4 : la tentative de l'espèce, puis Opus 4.6, puis Sonnet 4.6 ;
- ajout Opus 4.6 : Opus 4.6, Opus 4.6, Sonnet 4.6 ;
- ajout Sonnet 4.6 : Sonnet 4.6, Opus 4.6, Sonnet 4.6 ;
- autres fournisseurs : une tentative, le n° 1 garde sa lettre (P1, AV l. 126).

Les montants sont calculés à 96 000 jetons, en lecture littérale (J l. 12-174). Le pire de lettre compte 6,05 USD par tentative.

| proposeur | clé payeuse | pire calculé par tentative | attendu | haut | pire calculé | tentatives au pire | **pire de lettre** |
|---|---|---|---|---|---|---|---|
| espèce 1 | deuxième relais (Google) | 4,16 | 0,40 | 1,58 | 4,16 | 1 | 6,05 |
| espèce 2 | troisième relais (OpenAI) | 5,02 | 1,99 | 3,95 | 5,02 | 1 | 6,05 |
| espèce 3 | **Luc** (GO-45, selon le mandat) | 5,02 ; 2,51 ; 1,51 | 1,99 | 5,92 | 9,02 | 3 | 18,15 |
| espèce 4 | Luc | 5,02 ; 2,51 ; 1,51 | 1,99 | 5,92 | 9,02 | 3 | 18,15 |
| espèce 5 | deuxième relais (Google) | 4,16 | 0,40 | 1,58 | 4,16 | 1 | 6,05 |
| ajout Kimi | `KIMI_API_KEY`, nommée par son nom seulement | 1,01 | 0,40 | 0,79 | 1,01 | 1 | 6,05 |
| ajout Opus 4.6 | Luc | 2,51 ; 2,51 ; 1,51 | 1,00 | 3,95 | 6,52 | 3 | 18,15 |
| ajout Sonnet 4.6 | Luc | 1,51 ; 2,51 ; 1,51 | 0,60 | 1,19 | 5,52 | 3 | 18,15 |
| **total** | | | **8,75** | **24,84** | **44,40** | **16** | **96,80** |

**Par clé, au pire de lettre** (J l. 158-165) :

| clé | pire de lettre (USD) |
|---|---|
| Luc | 72,60 (pire calculé 30,08) |
| deuxième relais (Google) | 12,10 |
| troisième relais (OpenAI) | 6,05 |
| Kimi | 6,05 |

**Marge sous 200 USD : 103,20** (J l. 11). Le plafond de 55 USD (GO-43, GO l. 730) est dépassé : la ligne demande le mot de GO-46.

**Lecture « modèle déjà tenté sauté »**, proposée comme écart pour les deux ajouts Claude (J l. 176-335) :
- ajout Opus 4.6 : Opus 4.6, puis Sonnet 4.6 ;
- ajout Sonnet 4.6 : Sonnet 4.6 seul ;
- résultat : 13 tentatives, pire de lettre **78,65**, dont 54,45 sur Luc ; marge 121,35.

**Recommandation : ligne P_X = 96,80 USD**, en lecture littérale. Elle tient quelle que soit la lecture que la mère retient. Confiance 0,7.

**Options, si l'on voulait couper** (aucune n'est nécessaire). Chiffres en USD ; le pire de lettre compte au moins 6,05 par tentative.

| option | attendu | pire calculé | pire de lettre | marge sous 200 | source |
|---|---|---|---|---|---|
| plafond de 64 000 jetons | 5,94 | 30,22 | 96,80 (inchangé : chaque tentative reste sous 6,05) | 103,20 | J l. 684 et suivantes |
| plafond de 128 000 jetons (la sortie maximale de Claude) | 11,57 | 58,58 | 98,49 (les tentatives à 10/50 passent à 6,62, au-dessus de 6,05 : P4 demande alors une version neuve) | 101,52 | J l. 517 et suivantes |
| sans les deux ajouts Claude | 7,16 | 32,37 | 60,50 | 139,50 | J l. 961 et suivantes |
| cinq espèces seules | 6,76 | 31,37 | 54,45 (égal à X-10) | 145,55 | J l. 851 et suivantes |
| deux requêtes de 64 000 jetons par proposeur | 11,58 | 58,63 | 193,60 | 6,40 | J l. 350 et suivantes |

Baisser le plafond ne réduit pas le pire de lettre : celui-ci est fixé par le nombre de tentatives. Seul le retrait de proposeurs le réduit. Le découpage en deux requêtes double le pire (marge 6,40) : il est déconseillé.

## 4. Ce que l'ajout touche dans l'additif, et la lettre proposée

| lieu (AV) | ce qui change | lettre proposée |
|---|---|---|
| § 7, table des lectures (l. 171-178) et l. 180 | (d) remplace (c) (GO-42, GO l. 729 : « option d […] go ») | « **Lettre de la lecture (d)**, retenue par GO-2026-11-22-42 et étendue par GO-2026-11-22-46. » La ligne (c) est gardée et barrée de la mention « remplacée ». |
| X-1 (l. 184) | cinq requêtes deviennent huit ; les réglages changent | « Une requête de plus, hors des générations : la passe X, une par **proposeur de passe X** (huit) : les cinq espèces de la course, et trois **proposeurs ajoutés** (le proposeur de la clé Kimi, le premier et le second modèle de repli tenus comme proposeurs ; identifiants dans la configuration, GO-2026-11-22-46). Chaque requête part par le relais de la clé de X-11, avec le **jeu A7 de passe X** : plafond de sortie de 96 000 jetons, réflexion de Google au plus 64 000, aucune limite de mots (G-6). » Les ajouts ne prennent **aucun numéro d'espèce** : le numéro 6 a été retiré (DV l. 29). |
| X-2 (l. 185) | inchangée | La question fusionnée seule, à l'octet, plus l'enveloppe bornée de K-2 (5). |
| X-3 (l. 186) | dix-sept corps ; empreinte neuve | « Le corps de QN, de QA, puis des quinze pièces de la liste fermée, dans l'ordre que Lazar nomme. Chaque corps est pris sans sa ligne de titre quand il en a une, une ligne vide entre deux corps. Chaque pièce passe la garde de motifs et le contrôle d'ancrage (K-1) avant la fusion. » Ajouter la phrase : « **La question du lot en quarantaine est servie aux proposeurs sur le mot du directeur (GO-2026-11-22-46) ; le lot lui-même reste fermé.** Elle est servie telle quelle, avec la réserve « orientée faiblement au test de devinette » (GO-2026-11-22-37). » Huit pièces n'ont pas passé le collisionneur (LQ l. 31) : leur épreuve de garde est consignée avant le scellement. |
| X-4 (l. 187) | inchangée | L'empreinte vaut celle de la pièce scellée. Pour cette version, elle est égale à `d93f1ec6…` si l'ordre du mandat est gardé. |
| X-5 (l. 188) | trois écarts ajoutés | « Une réponse à la question du lot ne donne **aucun accès** au lot, ni à son identité, ni à son contenu. Elle va à la quarantaine de la course, sous les arrêts n° 17 et 18, et n'est servie à personne. » La règle du séquestre de N-054 vaut pour toute réponse qui décrit une façon de dégrader. Elle couvre aussi les réponses des proposeurs ajoutés. |
| X-6 et X-7 (l. 189-190) | inchangées | Elles s'étendent aux proposeurs ajoutés. |
| X-8 (l. 191) | la numérotation devient ambiguë | « Le compte des propositions porte sur **la question 6 de la pièce QA**. Les réponses sont rangées **par pièce** (dix-sept) et par proposeur. Les proposeurs ajoutés forment une ligne à part, jamais additionnée à une espèce. » |
| X-9 (l. 192) et P1 (l. 126) | chaîne des ajouts Claude | Sous la lecture littérale, aucun écart : « Pour un proposeur ajouté sur clé Anthropic, la chaîne suit GO-35 à la lettre. » Sous la lecture « déjà tenté sauté », un écart déclaré : « un modèle de repli égal au modèle déjà refusé est sauté ». Kimi n'a aucun repli : le n° 1 garde sa lettre. |
| X-10 (l. 193) | formule et montant | « P_X = 6,05 × le nombre de tentatives au pire = **16 × 6,05 = 96,80 USD** (lecture littérale ; 78,65 sous l'autre), sous le plafond de 200 USD de GO-2026-11-22-46. Cette ligne **remplace** « au moins 54,45 » et la ligne de 55 USD de GO-2026-11-22-43. Sous-parts par clé : Luc 72,60 ; deuxième relais 12,10 ; troisième relais 6,05 ; Kimi 6,05. » |
| X-11 (l. 194), arrêts n° 11 et 12 (V9 l. 382-383) | la clé change | « Tout appel à Anthropic de la passe X se paie sur **Luc** (GO-2026-11-22-45) ; **Minuit n'est pas appelée** (sans crédit). Les n° 11 et 12 se lisent par clé, contre la sous-part de X-10 et le reste relu au moment de Q9 (a). » Chiffre : après la course, Luc a un reste d'environ 153 − 136,04 = **16,96** (PL l. 76 ; PJ l. 176). C'est sous la sous-part (72,60) et même sous le pire calculé (30,08). La passe X sur Luc ne part donc que si Lazar dit Luc **compte payant**, avec sa recharge automatique (GO-40, GO l. 727 ; GO-42, l. 729 : « la laisser agir »). Sinon, le contrôle de ligne refuse les quatre requêtes Anthropic. |
| Q2 (l. 275) | répondue | « Accordée : 55 USD (GO-43), puis au plus 200 USD sur ce devis (GO-46). Ligne demandée : 96,80. » |
| Q9 (l. 277-283) | réécrite | Les options (a) et (b) chiffrées sur Minuit tombent. Il reste : « (a) après la génération 3 ; Anthropic sur Luc, Google et OpenAI sur leurs relais, Kimi sur sa clé ». L'option (b) ferait passer Luc sous sa part avant la course : à écarter. |
| L-1 (l. 162) | **le point qui bloque** | La passe X est comptée contre P_X, non contre la part : L-1 garde 136,04 pour la passe X. **Mais** si GO-45 met aussi le juge et le proposeur de l'espèce 3 *de la course* sur Luc (lecture du mandat, non vérifiée au registre), le cas haut des rôles de Luc devient 124,35 + 131,66 = **256,01** (AC l. 56-57). C'est au-dessus de 136,04 : la répartition ne tient plus (CV l. 116, L-2). Il faut un complément de valeurs neuf et le mot de Lazar. |
| P4 et P15 (l. 129, l. 143) | inchangées | Le pire de 6,05 « non baissé » vaut pour chaque tentative de passe X. Il tient, puisque chaque tentative calculée à 96 000 jetons reste sous 6,05 (J l. 6). |
| P5 (l. 130) | précision | Les tentatives de la passe X ne repassent **pas** les n° 6 et 7 de génération. Elles repassent le plafond P_X. |
| P7 et P9 (l. 132, l. 137) | attribution | Une réponse servie par repli va au modèle servi, sous « servies par repli ». Le coût d'un proposeur ajouté va à la ligne « passe X », jamais à M4. |
| P11 et P13 (l. 139, l. 141) | sonde | Aucune sonde de refus n'est faite pour la passe X : sa requête est sa propre sonde. Un refus arrête la chaîne de ce seul proposeur (n° 1, portée « appel ») et ne retire aucune espèce de la course. |
| P14 (l. 142) | complété | « La passe X compte ses replis dans P_X, non dans la ligne de 450. » |
| K-1 (l. 228) | inchangée | Le mot « quarantaine » n'est pas un candidat de mode. Il n'est pas dans le corps servi (J l. 1258). |
| arrêt n° 38 (l. 247) | étendu | Il vaut pour chacune des dix-sept pièces, avant la fusion. |
| **appariement** (lecture de l'auteur : le terme n'est dans aucune pièce lue) | identité des requêtes | Les huit proposeurs reçoivent la **même** requête (même empreinte, V9 l. 77). Une réponse d'Opus 4.6 ou de Sonnet 4.6 servie par repli pour l'espèce 3 ou 4 double la réponse de cet ajout. Les deux sont gardées, jamais fusionnées ni dédoublonnées, et la rubrique « servies par repli » le dit. La comparaison entre proposeurs se fait par pièce, sur des réponses appariées à la même requête. |

## Réserves

1. GO-2026-11-22-45 et -46 n'ont **aucune occurrence** dans `go.md` lu (`c40f367163c37f61…`, 730 lignes ; la dernière est GO-43). Leur lettre est prise au mandat.
2. Les tarifs d'Opus et de Sonnet 4.6 ne sont pas relus sur la page officielle. Ceux de Google et d'OpenAI sont cités, non vérifiés (RQ l. 25-31). Le pire de lettre (6,05 par tentative) ne dépend d'eux que si une tentative calculée dépassait 6,05.
3. L'espèce de chaque modèle de la course est hors des pièces lues : les espèces 3 et 4 sont comptées au tarif Claude le plus haut cité.
4. Les sorties maximales autres que celle de Claude 4.6 ne sont pas relevées.
5. Les rapports signes par jeton sont des règles, non une mesure.
6. L'ordre des quinze pièces après QN et QA est celui du mandat, non une liste de Lazar.
