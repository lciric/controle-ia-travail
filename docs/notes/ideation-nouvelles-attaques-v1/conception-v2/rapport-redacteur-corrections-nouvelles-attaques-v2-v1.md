# Rapport du rédacteur — corrections de la conception de la course « nouvelles attaques », pièces v2 — v1

- Auteur : rédacteur neuf, modèle F. Écrit le 2026-11-20 ; relevé de `date -u` : 02:02:21Z, après la production des pièces et avant l'écriture de ce rapport.
- Mandat : `docs/notes/ideation-nouvelles-attaques-v1/conception-v1/mandat-redacteur-corrections-conception-nouvelles-attaques-v2-v1.md` (`42c8276ab4994784432278cf9c072f2c17acc7338de050053009aa905dc01b64`, vérifiée contre son compagnon).
- Contre-lecture appliquée : `contre-lecture-conception-nouvelles-attaques-v1.md` (`ae9d4ae44027476bee4821e72c4e9f9b12f39d10f3dc6749ae60ae61d07c1fed`, recalculée).
- Outil : `scripts/remplacer_texte_exact_v1.py` (`391db990734dd36f7c827b8b6c77dc0de1bda324f671b65748ccfe68c56a53d6`). Python 3.13.18.
- Processeur seul. Aucun appel à un fournisseur de modèles, aucune dépense, aucune écriture dans l'arbre du dépôt, aucun commit. Réseau : un seul `git fetch origin main` (tête `72a452cf3ba411e5beab40ec299d93d2288d8c23`). Aucune commande sur un chemin sous `archives-reponses-modeles/`. **Aucun refus d'outil ni de classifieur.**

## 1. Verdict

1. **Les vingt et une corrections C1 à C21 sont appliquées à la lettre**, par l'outil contre-lu, sous des noms neufs. Cinq appels de l'outil, tous « FAIT » au premier essai : 26 remplacements pour l'ordre, 11 pour la question, 18 pour le devis, 7 pour le programme, 11 pour le rapport de conception.
2. **Le calcul change** (C17, C18) : programme v2, joué deux fois, sorties égales à l'octet (`cmp` muet). Le reste du premier relais vaut 162,562437 USD ; les manques valent 287,44, 32,44 et 0,00 ; le troisième relais vaut 199,65 dans les trois compositions. Ce sont les valeurs attendues par la contre-lecture.
3. **Le plafond et la ligne ne changent pas** : ligne de course 450 USD exactement, plafond total 456 USD (cinq espèces) ; 195 et 201 (trois espèces) ; 150 et 156 (deux espèces).
4. Aucune pièce ne contient de méthode, de procédé ni de détail opérant ; aucune ne porte d'identifiant de modèle. Le véhicule de la course n'est nommé ni v69, ni v70, ni « lanceur version 11 » : ces noms ne restent que là où les pièces parlent du palier 1 de l'héritage.

## 2. Pièces rendues

Dossier : `/tmp/claude-0/-home-user-controle-ia-travail/227b647d-2ece-5654-bf04-8493b3ed2f19/scratchpad/redacteur-nouvelles-attaques-v2/`. Chaque fichier a son compagnon `.sha256`.

| pièce | empreinte |
|---|---|
| `question-course-nouvelles-attaques-v2.md` | `ebce048030d39d717e50a6cd00125306e77885695dba234942e4ce9f7d488ff4` |
| `ordre-course-nouvelles-attaques-v2.md` | `1a18cd2ef63e590b227a97fd36c26b7d6e3083d2c58268fa6da36f230b122586` |
| `devis-course-nouvelles-attaques-v2.md` | `714e4fc6a9a292626022adac4a5ddcc4f3e16fd14f81629b6b8a98cf89fcf028` |
| `calcul_devis_course_nouvelles_attaques_v2.py` | `cefe97837267d4db517c40437dc89288842d1d7dd5252b225fe0e0f05edede9b` |
| `calcul-devis-course-nouvelles-attaques-v2.json` (les deux jeux) | `ffecbd1172888b815e6f7af84ae54f52c1991554d6d2ff376481af694e60b7cf` |
| `rapport-redacteur-conception-nouvelles-attaques-v2.md` | `831a2bc4b340f24266cf8c536c39a9c74dedb4830120b833fa9d0b4f326767f4` |

Fichiers de remplacements :

| fichier | empreinte |
|---|---|
| `remplacements-question-v1-vers-v2.json` | `a1c24165d990c39e6ffa9d3034db4bf6683efa1184bb727d66b8d4d03832b8db` |
| `remplacements-ordre-v1-vers-v2.json` | `6cd6e5d8df849c482dcd75561b27204c908b9e2f70537e81a54a75ff47f63e42` |
| `remplacements-devis-v1-vers-v2.json` | `165e90dcc0a4e49f5875e39ad493aa461ec72dad8a6c8a129efc69ee22480123` |
| `remplacements-calcul-devis-v1-vers-v2.json` | `94fdaffbd2f2e3acdce2121749e3c90e5e7ce1105d2551d5643ab055af4cc595` |
| `remplacements-rapport-conception-v1-vers-v2.json` | `9c05100efc1927ba9005bbbdd2bda885b947a3ab301c46d24c178387ef8b60f3` |

Journaux de l'outil (un par sortie, nom de la sortie suivi de `.journal-remplacements-v1.json`) :

| journal de | empreinte |
|---|---|
| la question v2 | `f37036b2845a696c45ef0b3809b23fb731396cdd9788586617ebe653d89bf164` |
| l'ordre v2 | `fe7724e987aca7d9e2ab732b1918f8cabcc06b41d0284ff87e91b522f068fe5c` |
| le devis v2 | `6775af808742f11fdd222553a01b3f765aecdd4b1dd3c7dd1b7204f40a925850` |
| le programme v2 | `fd44e22cac25e5e1e5e18e96dda3336e2fb70bb4589c1adfad8512adddb659ba` |
| le rapport de conception v2 | `b92a1a3c1ee234d09217fad44a47a87a9ad581f3f740e0055e9f4dd8a9dcc5af` |

Différentiels `diff -u`, v1 vers v2 :

| fichier | empreinte |
|---|---|
| `differentiel-question-v1-vers-v2.diff` | `03599ecbd38268579b38d18ee36b6721f2f1e4162fbaadacf08f7adc1b5dc421` |
| `differentiel-ordre-v1-vers-v2.diff` | `4c5ec4088f9b87fb79d4d1193413d48a252f26cac6a2a90a889c520fe5951ff8` |
| `differentiel-devis-v1-vers-v2.diff` | `01dc0f965be55beb119cd7d6f968259e3c532360496b9bef35b9572d3e81c3ea` |
| `differentiel-programme-calcul-v1-vers-v2.diff` | `79cd3fdf184af2b54c512c3e6ff1c30413cc431b416a099442f7d69fdc6706e5` |
| `differentiel-sortie-calcul-v1-vers-v2.diff` | `c4f09d317cc6b26a19843bcb4d3d243eabf58f8368733ec6ba63a44f1d5a2f2a` |
| `differentiel-rapport-conception-v1-vers-v2.diff` | `40655973e8c92fe6f81caa0f96098837c6ed2ce0bb04c1a89a91d23c85544d46` |

Le sous-dossier `rejeu/` garde le second jeu du calcul ; ce n'est pas une pièce rendue. Les pièces v1, recalculées avant tout geste, sont égales aux empreintes de la contre-lecture, § 1.

## 3. Correction par correction

| n° | pièce touchée | état | remarque |
|---|---|---|---|
| C1 | ordre, § 0, point 1 | appliquée | |
| C2 | ordre, § 0, point 2 | appliquée | |
| C3 | ordre, § 0, point 3 | appliquée | |
| C4 | ordre, § 2, le régime | appliquée | |
| C5 | ordre, § 2 (points 1, 2 et 6, coût, phrase du point 6), § 3, § 13 réserve 1 | appliquée, sept remplacements | |
| C6 | ordre, § 5 | appliquée | le bloc entier remplacé ; la marque de citation de la contre-lecture n'est pas reprise ; recommandation gardée, voir § 5 |
| C7 | ordre, § 12 | appliquée | |
| C8 | ordre, § 13, réserve 5 | appliquée | |
| C9 | rapport de conception (§ 1, § 4, D2, D3, § 6) ; devis (§ 2, § 7, point 3) | appliquée, sept remplacements | |
| C10 | question (§ 1, § 2 deux fois, § 5) ; ordre, § 9 | appliquée, cinq remplacements | |
| C11 | ordre, § 6 | appliquée | |
| C12 | ordre, § 9 et § 13 réserve 4 ; devis, § 7, point 2 | appliquée, trois remplacements | |
| C13 | ordre, § 9 | appliquée | |
| C14 | ordre, § 9 (sources, table) ; question, § 2 ; rapport de conception, § 4 | appliquée, quatre remplacements | |
| C15 | ordre, § 4 | appliquée | |
| C16 | question, § 4 et § 5 | appliquée, deux remplacements | |
| C17 | devis, § 3 ; programme | appliquée | table et paragraphe de répartition ; le programme rend 199,65 aux trois compositions |
| C18 | devis (§ 0, § 6 quatre fois, § 9 deux fois) ; rapport de conception (D1, D7) ; programme (deux remplacements) | appliquée | reste 162,562437 ; manques 287,44, 32,44, 0,00 |
| C19 | devis, § 1, ligne S4 (chiffre et chemin) | appliquée, deux remplacements | le § 3.2 de S4 existe (ligne 44 de la pièce) |
| C20 | rapport de conception, D6 | appliquée | |
| C21 | ordre, en-tête | appliquée | |

## 4. Ce que j'ai ajouté, et pourquoi

1. **Tenue** (mandat, point 3) : titre « v2 » et une ligne « Version » dans chaque pièce ; dans la question et l'ordre, les noms des pièces sœurs passent en v2 ; dans le devis, la ligne « Calcul » cite le programme v2 et sa sortie, avec leurs empreintes (la contre-lecture le demande, C18, dernière phrase) ; dans le programme, le titre, la ligne d'usage, le message d'usage et le champ `piece`.
2. **Deux remplacements du devis hors de la liste de la contre-lecture**, portés par le mandat (« le véhicule de cette course prend un nom neuf, ni v69 ni v70, ni lanceur version 11 ») :
   - § 3 : « comme le lanceur version 11 devra le faire » devient « comme le lanceur de la course devra le faire » ;
   - § 7, point 1 : « version 69 de l'orchestrateur, lanceur version 11, additif » devient « version de l'orchestrateur qui porte la course et son lanceur (ordre de course, § 2, points 1 et 2), additif ».

   La contre-lecture avait corrigé ces noms dans l'ordre et le rapport, non dans le devis. C'est un écart à « aucune autre modification » ; je le déclare. Sans lui, le devis v2 nommait encore le véhicule par deux noms retirés.
3. **Une sixième pièce, le rapport de conception en v2.** Le mandat ne nomme que la question, l'ordre et le devis ; mais C9, C14, C18 et C20 corrigent le rapport de conception. Je l'ai donc produit sous un nom neuf. Ses § 2, § 3 et § 7 décrivent la session de la v1 et ne sont pas retouchés ; sa ligne « Version » le dit.

## 5. La recommandation de D2 : gardée

Le mandat me laisse la main sur la recommandation du nœud qui remplace D2. **Je garde (a), le registre entier, confiance 0,55.** Raison : ton mot 2b dit « toutes les tentatives » ; le compte du coffre est le seul moyen de les compter toutes sans rien relire du coffre. Et le risque de l'option (a) est borné par le tirage : les cases sont tirées sans remise, donc le compte par case porte sur des cases que la génération suivante ne reçoit pas. La confiance reste basse parce que rien n'est mesuré ; l'épreuve des témoins peut la renverser, comme le § 5 de l'ordre le dit.

## 6. Décisions pour Lazar

Elles sont au rapport de conception v2, § 5. Je les redonne ici au format, telles qu'elles sont après corrections.

### D1 — La ligne de course et la composition
**Décision.** Quelle ligne de course accordes-tu, à quelle composition ?
**Enjeu.** La dépense ; la diversité des proposeurs ; la charge de relecture de la mère ; le crédit de la clé du premier relais.
**Options.** (a) cinq espèces, ligne 450 USD, total 456 : la composition mesurée et la diversité entière, mais la dépense la plus haute, 282 fiches à relire et un crédit à recharger d'au moins 287,44 USD. (b) trois espèces, ligne 195, total 201 : le tiers du prix, mais deux espèces retirées sans preuve, et un crédit qui manque encore de 32,44 USD. (c) deux espèces, ligne 150, total 156 : le crédit lu suffit, mais la diversité la plus pauvre.
**Recommandation.** (a), confiance 0,55. **Défaut.** Aucun : dépense.

### D2 — La forme du registre servi, sous ton mot 2b
**Décision.** Dans cette course, qui n'exécute aucune épreuve, le registre des tentatives de ton mot 2b sert-il aussi le compte des tentatives au coffre ?
**Enjeu.** Ton mot 2b fixe la règle : toutes les tentatives et leur classe d'issue, sans verdict ni tri. Ici la seule issue est l'aiguillage du portier, un modèle ; ce qui est au coffre n'est jamais relu (R-607).
**Options.** (a) le registre entier, le coffre en compte par case seulement : la lettre de 2b, mais le compte dit où la question a glissé vers le concret. (b) le même registre sans les comptes du coffre : rien du coffre n'est servi, mais c'est un écart à la lettre de 2b.
**Recommandation.** (a), confiance 0,55. **Défaut.** Aucun : ce qui est servi à un agent est un nœud ; sans ton mot, la course ne part pas.

### D3 — Le véhicule de la course
**Décision.** Donnes-tu le mot d'activation de principe d'un régime de plus, « trois générations, sans étage de tests de mort, lecture du registre des tentatives », qui fait écrire en routine la version de l'orchestrateur, le lanceur et l'additif qui le portent ?
**Enjeu.** Ton mot 1a réserve la version suivante, le lanceur version 11 et leur additif au seul palier 1 de l'héritage ; 2b demande une version de plus pour la lecture du registre. Aucune version prévue ne porte cette course.
**Options.** (a) oui, pour ce seul régime, écrit après la version du palier 1 et sur elle, numéros fixés par les mandats : la course peut partir dès ton accord de calcul ; cela prend de la place du modèle F. (b) attendre la lecture du palier 1 de l'héritage : une base éprouvée en réel, mais la course attend un résultat qui ne la concerne pas. (c) trois courses d'une génération par le lanceur en place, le registre porté à la main : rien à écrire, mais le code n'est plus figé (N-044) et il faut trois lignes.
**Recommandation.** (a), confiance 0,7. **Défaut.** Aucun pour l'allumage, qui est un nœud ; écrire le code éteint, sans dépense, reste de la routine.

### D4 — Qui lit les fiches, et le mode tenu à l'écart
**Décision.** Toutes les fiches sont-elles relues par la mère, ou une part l'est-elle par un lecteur hors de la défense ?
**Enjeu.** Ce que la mère a lu est un mode vu pour la défense, et ne peut plus fonder un mode tenu à l'écart.
**Options.** (a) tout est relu par la mère, et aucune carte de cette course ne nourrit le mode tenu à l'écart : la lettre de `GO-2026-11-19-94`, simple. (b) une part scellée d'avance est relue par un lecteur isolé : des cartes inconnues de la défense, mais un écart à cette lettre et une cloison de plus.
**Recommandation.** (a), confiance 0,65. **Défaut sous 48 heures.** (a).

### D5 — La famille de cases tenue à l'écart
**Décision.** Tient-on à l'écart, sans jamais la servir, une famille entière de cases ?
**Enjeu.** Garder un terrain que l'organisme n'a pas exploré, pour une mesure d'universalité ultérieure (N-044).
**Options.** (a) oui, vingt cases, tirées par graine parmi les cinq valeurs nommées, scellées : un terrain neuf gardé, pour un sixième du vivier. (b) non : tout le vivier est ouvert, mais rien ne reste inédit pour l'organisme.
**Recommandation.** (a), confiance 0,6. **Défaut sous 48 heures.** (a).

### D6 — Les juges
**Décision.** Joue-t-on les juges, pour information seulement ?
**Enjeu.** 27,81 USD au cas bas sur la course ; la lecture des témoins plantés ; l'ordre de lecture de la mère.
**Options.** (a) joués, jamais servis, jamais critère. (b) non joués : moins cher, mais les témoins plantés ne sont lus que par le portier.
**Recommandation.** (a), confiance 0,55. **Défaut.** Aucun : les juges sont une part de la dépense de D1 et se tranchent avec elle.

### D7 — Le crédit
**Décision.** Recharges-tu la clé du premier relais avant la course ?
**Enjeu.** Au dernier chiffre lu, il reste environ 162,56 USD ; le lanceur refuse le départ sous la part au pire (450, 195 ou 150 selon D1). La dispense des deux autres clés (R-3237) est à redire pour cette course.
**Options.** (a) recharge à la part au pire de la ligne retenue. (b) pas de recharge : seule la ligne à deux espèces part.
**Recommandation.** (a), après un relevé du jour. **Défaut.** Aucun : compte et dépense.

## 7. Écarts et réserves

1. **Deux remplacements du devis hors de la liste**, et **une sixième pièce** : § 4, points 2 et 3.
2. **Une commande composée.** Pour compter les espaces insécables des pièces v1, j'ai lancé une commande qui enchaînait un changement de dossier et une boucle, contre « une commande simple à la fois ». Elle n'a fait que lire les cinq pièces v1 et une ligne du devis S4 ; son premier filtre était mal écrit et je l'ai refait en une commande simple. Rien n'a été écrit.
3. **Une phrase du rapport de conception garde le chiffre de la v1** : § 7, point 5, « Le crédit de 162,57 USD ». La contre-lecture ne la corrige pas ; je ne l'ai pas touchée. La ligne « Version » du rapport v2 le dit.
4. **Le nom du véhicule.** Les textes de la contre-lecture disent « postérieure à celle du palier 1 ». Le mandat de l'additif réserve aussi le nom suivant à la lecture du registre pour l'héritage. Les pièces v2 ne donnent aucun numéro (« numéros fixés par leurs mandats ») : c'est conforme, mais le mandat du véhicule devra prendre un nom qui suit les deux noms réservés.
5. **Une tension légère entre C6 et C10.** C6 dit que la seule issue d'une tentative est « passée » ou « au coffre ». C10 ajoute qu'une fiche dont les champs fermés diffèrent de la case servie est « refusée par le portier et comptée ». L'additif devra dire si ce refus est une troisième classe d'issue du registre.
6. **Le registre des dépenses.** Le devis v2 cite le commit `6f7cd0f8` et l'empreinte `a6d50eca…`, lus par le contre-lecteur. J'ai recalculé l'empreinte du registre des dépenses sur la tête de `main` de ce jour (`72a452cf3`) : elle est la même. Je n'ai pas relu les lignes 528, 532 et 536 moi-même ; l'arithmétique, elle, est rejouée par le programme.
7. **La répartition des relais par espèce (C17) est une lecture du contre-lecteur** (sa réserve 2). Je l'ai recopiée, non vérifiée aux sources.
8. **Ce que le programme v2 garde de la v1**, faute de correction demandée : les noms de clés `relais_1_aiguilleur_et_un_juge`, `relais_2_un_juge`, `relais_3_un_proposeur_seul` et `course_ideation_pilier_attaque_reel_une_generation_usd`, que C17 et C19 rendent imprécis ; et la constante de 199,03, qui n'entre plus dans aucun calcul.
9. Les pièces v2 ne sont ni contre-lues ni scellées. Le code de l'orchestrateur n'est toujours lu par personne dans cette chaîne (contre-lecture, réserve 1).

— rédacteur neuf, modèle F
