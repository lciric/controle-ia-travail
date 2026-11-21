# Devis — course « seuil et moniteurs », option (b) : l'étage des tests de mort seul, sur les propositions déjà rendues — v2

- Auteur : rédacteur de la conception de la course seuil et moniteurs, modèle F. Écrit le 2026-11-21 ; relevé de `date -u` : 07:03:52Z.
- Version : la v2 remplace la v1 (`e70ffce878a4dca9b837730ad142e9d9bcb1ae8686c17929819027cbde9128ee`, gardée intacte) après GO-2026-11-21-16 (option (b), plafond indicatif de 120 USD) et après la contre-lecture de la v1 (`18b630f702ae394dded262dda84b7f64d2bb84806202c558da06d7008240e2d4`, « À corriger »).
- Statut : **pièce de travail (classe C), non contre-lue.** Aucun appel, aucune dépense. GO-2026-11-21-16 n'ouvre aucune dépense : « la dépense part sur un devis contre-lu et une ligne de calcul ». **Ce devis demande cette ligne.**
- Calcul : `calcul_devis_course_seuil_et_moniteurs_v2.py`, sortie `calcul-devis-course-seuil-et-moniteurs-v2.json`, même dossier ; empreintes à la table v2. Joué deux fois sous Python 3.13.18 (`python3 -B`), sorties égales à l'octet (`cmp` muet). Arithmétique seule. Le programme v1 reste intact.
- Aucun nom de modèle ; les clés sont dites par leur désignation au registre. Montants en USD.

## 0. Verdict

| | cas bas | cas haut | pire |
|---|---|---|---|
| l'étage : onze candidates et trois témoins, expérimentateur modèle — **règle du rédacteur** | 14,93 | 75,13 | 84,00 |
| la mise en fiches : deux traducteurs, seize textes — **règle du rédacteur** | 3,84 | 17,28 | 20,48 |
| la machine jetable du bac et son essai — **règle du rédacteur** | 2,00 | 5,00 | 10,00 |
| **total** | **20,77** | **97,41** | **114,48** |

- **Ligne de calcul à demander : 114,48 USD**, sous le plafond indicatif de 120 (marge : 5,52). Elle se partage en trois plafonds d'arrêt : étage 84 ; mise en fiches 20,48 ; machine 10.
- **Les quatorze unités partent toutes, au cas haut comme au pire**, sous la règle de réservation (§ 3). C'est calculé par le programme, non à la main.
- **Aucune des trois lignes n'est une mesure.** L'étage n'a jamais été joué en réel ; aucun traducteur n'a jamais tourné ; le prix de la machine n'a qu'une source, « quelques dollars ». Les plafonds tiennent la dépense ; les cas bas et haut sont des règles de ma main.
- **Le nombre de textes sources (quatorze) est supposé.** La mère le remplace par le sien ; chaque texte de plus coûte au pire 1,28 (deux appels à 0,64).

## 1. Sources de chaque chiffre

| clé | chiffre | source | empreinte |
|---|---|---|---|
| S1 | coûts réels des proposeurs de la course v9 : 4,17 ; 4,75 ; 7,43 ; 17,58 ; 24,72, onze appels chacun | devis v6 de la course « nouvelles attaques », `docs/notes/ideation-nouvelles-attaques-v1/preenregistrement-court-v7/devis-course-nouvelles-attaques-v6.md`, § 1, ligne S1 ; égal à la source selon la contre-lecture, § 1, point 3 | `d825cb313898ea5111ede1ef3103ab25b1b923e1f52103481427919ce9d19c2c` |
| S2 | facteur du cas haut de la proposition : 1,1940 | préenregistrement court v9 de la même course, section « Seuil » | `864f39a7ecd41a613f8892efbf66607c14da34252d643a4fd40032b5d2b500c2` |
| S3 | prix par million de jetons : le plus haut 10 et 50, le plus bas des espèces présentes 4 et 20 ; garde de 2,5 caractères par jeton | table du collisionneur v9 v3, `docs/notes/collisionneur-v9/collisionneur_v9_v3.py`, lignes 100 à 141 | `850df311807384fc66c44f6a6b90d3c8a9a3288d2b88a2b74312f9a78c4d4910` |
| S4 | plafond indicatif : 120 | `registres/go.md` sur `origin/main`, commit `332080c5f64d436627351cfbfc17a9603248454c`, GO-2026-11-21-16 | `ba9ba9eb9876e309d6719f009a0f158b10183b093abc5532fc38c94c518b69fa` |
| S5 | machine jetable : « sur devis de quelques dollars » | `registres/decisions.md`, même commit, R-3984 | `a1f662faa31c55252b1cde109c727fa2496b74d64d63e1e4457b7b4206e9042b` |
| S6 | soldes et parts des clés : R-4258, R-4342, R-4356 ; GO-2026-11-20-22, -64, -67, -68 ; GO-2026-11-21-02 | les deux registres, même commit | idem S4 et S5 |
| S7 | coûts réels de deux consultations sur l'énoncé neutre : 0,65 (au prix haut) et 0,41 | `registres/decisions.md`, R-4371 | idem S5 |

## 2. L'étage — règle du rédacteur

Quatorze unités : onze candidates, et les trois témoins de l'étage, qui passent par l'expérimentateur comme elles.

- **Cas bas** : une session par unité, au coût réel moyen d'un appel de proposeur de la course v9 (58,65 / 55 = 1,07) : **14,93**.
- **Cas haut** : deux sessions par unité, chacune au coût réel le plus haut d'un appel (24,72 / 11), fois le facteur du haut (1,1940), soit 2,68 la session : **75,13**.
- **Pire** : deux sessions par unité au **plafond de session de 3,00**, soit 6,00 l'unité : **84,00**. Ce plafond de session est neuf : la v1 reprenait les 6,05 d'un proposeur, calibrés pour des entrées de plus de cent mille caractères. L'expérimentateur ne reçoit qu'une fiche et la description d'une interface.

Le lecteur et le comparateur sont des programmes : zéro dollar. Le contrôle de fidélité (trois seconds programmes écrits par un développeur) se fait en session : zéro dollar d'appels d'interface, mais du temps de place.

## 3. La règle de réservation — calculée par le programme

L'étage ne lance une unité que si son pire (6,00) tient dans ce qui reste de son plafond. La contre-lecture de la v1 a montré que cette règle, à 110 de plafond et 12,10 de pire, ne laissait partir que dix-neuf candidates sur vingt au cas haut. Le programme v2 porte la règle (champ `regle_de_reservation`) :

| | plafond de l'étage | unités qui partent | dépense | plafond qu'il faudrait pour toutes |
|---|---|---|---|---|
| v2, cas haut | 84,00 | **14 sur 14** | 75,13 | 75,76 |
| v2, tout au pire | 84,00 | **14 sur 14** | 84,00 | 84,00 |
| contrôle : v1, vingt candidates | 110,00 | 19 sur 20 | 101,96 | 114,06 |
| contrôle : v1, dix candidates | 55,00 | 8 sur 10 | — | 60,40 |

**Pourquoi tout part sous (b).** Le plafond de l'étage est posé égal au pire de toutes les unités (14 × 6,00) : la réservation ne peut plus refuser personne. C'est le prix d'un plafond de session bas.

**Un centime d'écart avec la contre-lecture.** Elle écrit 114,07 pour le plafond des vingt ; le programme rend 114,06 (19 × 5,36649… + 12,10 = 114,0633). Les trois autres chiffres sont égaux aux siens.

**Ce que le plafond indicatif permettrait de plus.** La marge de 5,52 ne paie pas une douzième candidate au pire (6,00). À 120,48, elle partirait.

## 4. La mise en fiches — règle du rédacteur

Deux traducteurs ; un appel par texte et par traducteur ; quatorze textes sources supposés, plus deux textes témoins : trente-deux appels.

| | entrée | sortie | prix | par appel | les trente-deux |
|---|---|---|---|---|---|
| cas bas | 25 000 caractères | 4 000 jetons | 4 et 20 | 0,12 | 3,84 |
| cas haut | 60 000 caractères | 6 000 jetons | 10 et 50 | 0,54 | 17,28 |
| pire | 60 000 caractères (garde) | 8 000 jetons (plafond) | 10 et 50 | 0,64 | 20,48 |

Un texte de plus de 60 000 caractères est refusé avant l'envoi ; la mère le coupe en deux textes, chacun empreinté. **Repère, qui n'entre dans aucun total** : deux consultations réelles sur l'énoncé neutre ont coûté 0,65 et 0,41 (S7) ; le cas haut par appel, 0,54, est du même ordre.

## 5. La machine — règle du rédacteur

Inchangée depuis la v1 : 2 / 5 / **10 de plafond**, location, essai du bac et étage compris ; processeur seul. Elle se loue sous le devis du premier étage payant à tests de mort, l'essai du bac en première étape (GO-2026-11-20-05, point 4b). **L'offre du loueur est à relever et à mettre à la place de cette règle avant la ligne de calcul.** Si la course principale d'auto-conception loue la machine avant celle-ci, cette ligne se réduit à l'usage, et le devis se refait.

## 6. Plafonds par relais, et clés désignées

| relais | son rôle | cas bas | cas haut | pire |
|---|---|---|---|---|
| relais de l'expérimentateur | l'expérimentateur de l'étage | 14,93 | 75,13 | 84,00 |
| relais du premier traducteur | seize appels | 1,92 | 8,64 | 10,24 |
| relais du second traducteur | seize appels | 1,92 | 8,64 | 10,24 |
| loueur | la machine | 2,00 | 5,00 | 10,00 |

Les lignes des traducteurs sont la moitié de la ligne de mise en fiches du calcul (moitiés faites à la main, hors de sa sortie). Je n'ai pas lu de quels relais relèvent l'expérimentateur et les traducteurs : c'est au complément de valeurs.

**Ce que le registre dit des soldes** (aucune clé lue par moi, aucune valeur, aucun nom de variable) :

| clé désignée | ce que le registre en dit | ce qui la tient déjà |
|---|---|---|
| Minuit | reste net **estimé** 162,56 (R-4258 : « estimation de l'organisme, non un relevé ») | part de 156,56 dans la course « nouvelles attaques » ; marge de 24,90 au-delà de son cas haut (R-4356) |
| Luc | reste net **estimé** d'environ 214,00 (R-4258, même réserve ; la v1 écrivait à tort « déclaré ») | l'aiguilleur et l'espèce 4 de la course « nouvelles attaques » (GO-2026-11-20-22) ; le juge de l'étage 2 de la ligne 3 (GO-2026-11-20-68) |
| Rigaud | solde déclaré 25 (GO-2026-11-21-02) | hors course ; ne garde que la réserve de 8,35 du bras A |
| deuxième relais (Google) | la carte paie au-delà du crédit, jusqu'au cas haut des appels **déjà accordés** (GO-2026-11-20-64) | course « nouvelles attaques », étage 2 de la ligne 3, collisionneurs |
| troisième relais (OpenAI) | recharge automatique ; reste lu contre 17,01 (R-4356) | course « nouvelles attaques », collisionneurs |
| loueur | crédit 90,56 (`registres/etat.md`, commit `55f7f6e1…`, ligne 628) | les machines de la formation |

**Proposition.** Si l'expérimentateur est un modèle Claude, sa part (cas haut 75,13, pire 84) va sur **une** clé Claude désignée dont le solde relu la couvre ; aucune ne peut la promettre aujourd'hui sans empiéter sur une part scellée de la course « nouvelles attaques » (somme des parts 439,59 sous 456). Deux chemins : attendre la clôture de cette course, ou une recharge de 84. Les parts des traducteurs (10,24 chacune au pire) tiennent sur les relais Google et OpenAI si le mot sur la carte est étendu à cette course pour le premier, et par le reste lu pour le second. Une clé dont le reste relu ne couvre pas sa part : départ refusé.

## 7. Ce qui n'est pas chiffré

1. Le temps des sessions (ordre de course v2, § 10).
2. Le contrôle de fidélité, fait en session.
3. Le coût réel de l'expérimentateur : cette course, ou celle que Lazar met en tête, sera la première à le mesurer.
4. Une proposition jouée sur plus de mondes que prévu ne coûte rien de plus : c'est du processeur sur la machine louée, dans son plafond.

## 8. Décision demandée

**Décision en une phrase.** Accorder, ou non, une ligne de calcul de 114,48 USD pour l'étage de tests de mort de la course « seuil et moniteurs », en trois plafonds d'arrêt : 84 pour l'étage, 20,48 pour la mise en fiches, 10 pour la machine.

**Enjeu.** Onze propositions déjà rendues, éprouvées au calcul sur vérité plantée ; contre une dépense de l'ordre de 20 à 115 USD, dont aucune ligne n'est une mesure.

**Options.**
- (a) 114,48, onze candidates. Avantage : sous le plafond indicatif, toutes les unités partent même au pire. Inconvénient : si plus de onze fiches sont calculables, les autres ne sont pas jouées.
- (b) 120,48, douze candidates. Avantage : une de plus. Inconvénient : quarante-huit centimes au-dessus du plafond indicatif.
- (c) 78,48, cinq candidates et trois témoins (étage 8 × 6,00 = 48 ; plus 20,48 et 10 ; chiffre fait à la main, hors de la sortie du calcul). Avantage : trente-six dollars de moins au pire. Inconvénient : il ne reste presque que les propositions nommées par Lazar ; aucun tirage.

**Recommandation : (a), confiance 0,6.** Ce qui me ferait changer : que la mise en fiches rende moins de six fiches calculables — alors (c) suffit, et le reste n'est pas dépensé de toute façon.

**Défaut sous 48 heures : aucun.** C'est une dépense.

**Ligne de calcul proposée**, à la lettre :

> **Course « seuil et moniteurs », étage de tests de mort seul** (GO-2026-11-21-16) : mise en fiches des propositions déjà rendues par deux traducteurs, puis onze candidates et trois témoins devant l'expérimentateur modèle, sur mondes plantés scellés ; départ quand le préenregistrement court, les mondes plantés et leur table, le complément de valeurs, le programme de mise en fiches et le véhicule sont contre-lus et scellés, et que l'essai du bac est passé ; plafonds d'arrêt : étage 84 USD, mise en fiches 20,48 USD, machine jetable et essai du bac 10 USD ; arrêt net à chaque plafond. | 114,48 USD |
