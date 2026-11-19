# Différences entre les versions 1 et 2 des pièces de la lecture de Yu et al. (2026) — v1

- **Qui écrit** : le lecteur neuf qui a écrit les versions 1 et 2 (modèle Fable 5.2, `claude-fable-5-2`), le 19 novembre 2026, à partir de 07:21Z (`date -u`).
- **Pourquoi des versions 2** : contre-lecture d'un lecteur d'un autre modèle, Opus 5.5 — `contre-lecture-lecture-yu-v1.md`, `97ac990c4fd450c3cd1cc3775db1bcf73f0ade242564f7ce94a5c392b723bb9f` (empreinte vérifiée, lue en entier). Sa section « Erreurs à corriger » compte onze erreurs, numérotées 1 à 11 ; son point 10 liste les failles de la proposition (c). Les numéros d'erreur ci-dessous sont les siens.
- **Les versions 1 restent en place, intactes** (R12) ; leurs empreintes compagnons se vérifient toujours : note `70c5941f…`, mémoire rétrospective `d117d45e…`, courriel `a87b3e01…`.
- **Inchangés, sans version 2** : `recalcul_etude_appariee_v1.py` (`1c1bc914…`) et `recalcul_etude_appariee_v1.txt` (`e6877d59…`) — rejoués par le contre-lecteur, sortie identique octet pour octet.
- **Comment cette liste est faite** : les versions 2 sont dérivées des versions 1 par un programme de remplacements, chacun vérifié unique ; la liste des blocs vient de `diff v1 v2` (numéros de lignes : version 1 → version 2).
- **Toutes les onze corrections sont appliquées ; aucune n'est contestée.** Deux précisions sont écrites dans la section « Corrections contestées » de la note v2.

## 1. `lecture-yu-approfondie-v1.md` → `lecture-yu-approfondie-v2.md`

`diff` : 36 blocs ; 60 lignes de la version 1 retirées ou changées, 125 lignes de la version 2 ajoutées ou changées ; 301 → 366 lignes.

| bloc de `diff` (v1 → v2) | section | changement | erreur traitée |
|---|---|---|---|
| 1c1 | titre | « v1 » → « v2 » | — |
| 6c6,7 | en-tête | ligne « Version 2 » ajoutée ; heures | — |
| 17c18 | en-tête | noms des fichiers du dossier (v2, différences) | — |
| 27c28 | a.1, le plan | « l'autre continue sans mémoire » → « sans cette mémoire (avec le seul historique ordinaire de la course cible) » | 1 (même faute hors de la rédaction) |
| 45c46 | a.1, ce que l'étude établit | « sans aucune mémoire » → « sans la mémoire d'amélioration » | 1 |
| 49c50 | a.2, point 1 | le bras « harnais seul » garde l'historique ordinaire (p. 5, p. 20) ; la première ligne du tableau 1 décrite pour ce qu'elle est (harnais de départ non évolué, banc source, première course, non au transfert ; correspond à « bras 2 moins bras 1 ») ; rappel que la question de l'héritage est posée par les auteurs (p. 2) | 1, 2, 11 (point 1 du rapport) |
| 80c81 | a.3 | tableau 7 : « course unique » dite inférence | remarque sans correction exigée |
| 111c112 | a.5 | page 18 ajoutée à la liste des pages où paraît « predict » | remarque sans correction exigée |
| 128c129 | a.5 | consignes de l'annexe D.2 sans mention des prédictions ; « défaite » → « changée » (mot du papier, p. 29) | remarque sans correction exigée |
| 135a137,138 | a.6 | paragraphe ajouté : le concepteur des deux voisins est Claude Opus 4.6 (SkillHone p. 4, p. 6 ; Meta-Harness p. 5, p. 15) ; indices voisins contre « un concepteur fort peut s'en passer » ; ne testent pas la mémoire transmise | 4 |
| 138c141 | a.7, SkillHone | date : « déposé le 7 juin 2026 » → « en juin 2026 d'après l'identifiant ; le PDF empreinté ne porte que la version 4 du 29 octobre ; le jour vient de l'interface d'arXiv, hors pièce » ; ablation : la condition retire l'historique **et** passe à un signal scalaire (p. 6), effets confondus | 5, 6 |
| 140c143 | a.7, Meta-Harness | citations rendues à la lettre du PDF (« +1--3pp », « 3--5 ») | remarque sans correction exigée |
| 143c146 | a.7, synthèse | « l'ablater » → « l'ablater (avec la confusion dite plus haut) » | 5 |
| 149c152 | a.8 | « sans mémoire » → « sans la mémoire d'amélioration » | 1 |
| 159,163c162,170 | (b) 1 | titre du point (« trop généreuse » → « à préciser ») ; premier tiret : Yu et al. **posent** la question de l'expérience héritée (p. 2), c'est la séparation qui manque à leur plan ; deuxième tiret : les dix réglages en course unique et le bras « causes seules » dits ; **rédaction proposée remplacée par celle du contre-lecteur** (son point 8), sans changement ; dernier tiret : « six travaux… » → « parmi les travaux cités p. 3 et 15-16, aucun n'a été lu ici » ; un mot signalé (« dans les autres réglages ») | 1, 2, 3 |
| 174c181 | (b) 8 | « n'ont pas été contre-lus » → « contre-lus une fois (Opus 5.5) » | — |
| 198,200c205,207 | c.2 | champ `prediction` : agrégat (signe, tranche), plus d'identifiant d'item planté ; champ `resultat` : au grain du retour ordinaire ; champ `retenue` renommé `gardee`, décidé par programme sur l'oracle et le coût, jamais par le juge | 10 (failles « `retenue` », « prédiction », « retour de l'oracle ») |
| 203c210,212 | c.2 | paragraphe ajouté : pourquoi `retenue` pouvait transporter le verdict du juge (N-053, point 5) ; règle ; le champ n'existe pas si la sélection dépend du juge | 10 (« `retenue` ») |
| 208a218,226 | c.3 bis (neuf) | la prédiction sur des items plantés nommés livrerait la clé de l'oracle : « sous cette forme, le champ ne peut pas exister » ; forme retenue (agrégat) ; forme fine sous condition d'un appariement par programme, non vérifié | 10 (« fuite de la clé ») |
| 211c229, 213c231 | c.4 | « depuis le même état » → « depuis le même organisme » ; en-têtes du tableau (« mémoire structurée ») | 10 (« ce que les bras héritent ») |
| 219,225c237,264 | c.4 | contrastes redits (héritage « au-delà de ce que l'organisme hérité porte déjà ») ; **sept règles** : même organisme de départ ; `historique` de la source remis à zéro dans les trois bras ; même retour de l'oracle au même grain ; budget égal **et** coût dans le signal (deux choses, N-045 v2 énoncé 2) ; dépense réelle rapportée (N-058) ; règle de retrait d'appels gelée et uniforme ; cloisonnement entre bras et même suite de mondes ; K ≥ 3 « choix repris de l'horizon de l'énoncé 5 » ; **bras de diagnostic D-a à D-e à part**, entrées fausses plantées dans D-d seulement | 10 (toutes les failles d'identification, les deux renvois à N-045 v2, les témoins faux) |
| 231,233c270,278 | c.5 et c.5 bis (neuf) | deux contrastes principaux ; **règle de multiplicité** : un seul test décisif par contraste (rangs signés exact), procédure de Holm sur les deux, rien d'autre ne porte de seuil | 10 (« multiplicité ») |
| 237,240c282,286 | c.6 | réfutations redites aux nouveaux seuils ; renvois aux bras D-a, D-b ; réfutation « forme » ajoutée (bras D-c) | 10 |
| 244c290 | c.7 | titre | — |
| 247,249c293,296 | c.7 | point ajouté sur `gardee` ; aucun identifiant ni nombre d'items plantés servi | 10 (« `retenue` », « fuite de la clé ») |
| 257,258c304,306 | c.8 | l'agent n'écrit ni résultat ni `gardee` ; ligne neuve « faire porter par la mémoire le verdict du juge » | 10 (« `retenue` ») |
| 261,265c309,313 | c.8 | parades renvoyées aux bras de diagnostic D-d, D-e ; ligne « apprendre la clé de l'oracle » ; ligne « lire la mémoire d'un autre bras » | 10 (« témoins faux », « fuite de la clé », « fuite entre bras ») |
| 267c315 | c.8 | phrase de synthèse complétée (« au grain que tous les bras reçoivent déjà ; rien du juge n'y entre ») | 10 |
| 273,276c321,324 | c.9 | source du compte de 55 appels (devis v2b, ligne 11) ; « mémoire pleine » ; renvoi aux règles 4 à 6 ; bras de diagnostic au devis | 10 |
| 280c328,336 | c.10 et c.11 (neuf) | compte corrigé : 6 / 3 / 5 à ± 20 %, 5 / 4 / 5 à ± 10 %, A1 et E2 contestables, « deux tranchées, deux fausses » sur le problème A ; **réserves propres au plan** (cinq) | 9 ; 10 (réserves écrites) |
| 286c342 | (d) | renvoi au courriel v2 | 11 |
| 292c348 | réserve 1 | la version 1 a été contre-lue ; la version 2 ne l'est pas | — |
| 296c352 | réserve 5 | indices voisins contre « un concepteur fort peut s'en passer » | 4 |
| 300c356 | réserve 9 | la proposition (c) version 2 répond au point 10 ; non contre-lue à son tour | 10 |
| 301a358,366 | « Corrections contestées » (neuve) | aucune correction refusée ; deux précisions (un mot de la rédaction ; fragilité du classement de D2) | — |

## 2. `memoire-retrospective-auto-conception-v1.md` → `memoire-retrospective-auto-conception-v2.md`

`diff` : 14 blocs ; 21 lignes retirées ou changées, 28 ajoutées ou changées ; 107 → 114 lignes.

| bloc de `diff` (v1 → v2) | section | changement | erreur traitée |
|---|---|---|---|
| 1c1 | titre | « v1 » → « v2 » | — |
| 3a4 | en-tête | ligne « Version 2 » | — |
| 22,23c23,26 | règle de classement | une attente jamais jouée est non vérifiable ; **deux tolérances écrites**, ± 20 % et ± 10 %, et le compte change de l'une à l'autre (la version 1 disait le contraire) ; un devis se compare à la même étape ; A1 et E2 contestables | 7, 8, 9 |
| 31c34 | A1 | « fausse » → « fausse — contestable comme prédiction », avec la raison (constat d'une épreuve faite) | 9 (son point 9) |
| 33,34c36,37 | A2, A3 | A2 : « fausse (réfutée sans course) » → « **non vérifiable** (jamais jouée ; attente implicite réfutée par la documentation) », et la citation dite pour ce qu'elle est (un calcul de coût) ; A3 : « fausse », raison ajoutée (prémisse démentie) | 7 |
| 48c51 | C2 | l'estimation de coût du devis v2b valait déjà : non vérifiable ici, comptée une fois en C3 | son point 9 (incohérence mineure) |
| 58,59c61,62 | D1, D2 | D1 : comparée à la part des proposeurs, 28,32 USD (devis v2b, ligne 11), **+ 58 %** ; nombres par rôle attribués au manifeste et non à la ligne 11 ; D2 : « non vérifiable » → part « proposition » 47,26 estimés (devis v2f, ligne 11), 42,36 observés, − 10,4 % : **juste à ± 20 %, fausse à ± 10 %**, biaisée par l'échec de Carbon | 8 |
| 71c74 | E2 | « juste » → « juste, indice faible — contestable comme prédiction », avec la raison | 9 (son point 9) |
| 82c85, 84,90c87,95, 92c97 | compte | tableau aux deux tolérances : **6 / 3 / 5 à ± 20 %, 5 / 4 / 5 à ± 10 %** ; sans A1 et E2 : 5 / 2 / 5 et 4 / 3 / 5 ; « sur le problème A : deux tranchées, deux fausses » | 9 |
| 96c101 | lecture du compte, point 1 | « trois sur trois » retiré ; constat qualitatif gardé | 9 |
| 103c108 | réserve 1 | deux tolérances | 9 |
| 107a113,114 | réserves 6 et 7 (neuves) | faits tirés des seuls manifestes non revérifiés par la contre-lecture ; fragilité de D2 | 8 |

## 3. `courriel-auteurs-brouillon-v1.md` → `courriel-auteurs-brouillon-v2.md`

`diff` : 4 blocs ; 3 lignes retirées ou changées, 4 ajoutées ou changées ; 42 → 43 lignes.

| bloc de `diff` (v1 → v2) | changement | erreur traitée |
|---|---|---|
| 1c1 | « v1 » → « v2 » | — |
| 2a3 | ligne « Version 2 » dans l'en-tête interne | — |
| 6c7 | renvoi à la note v2 | — |
| 25c26 | question 4 : « has no memory » → « has no SIM … (it keeps the ordinary target-run history D_t) » ; « the only comparison of that kind » → « The closest comparison …, which tests SIM during an initial run from the seed harness rather than after a transfer (Appendix C.5), and is a single run » | 11 |

## 4. Table des onze erreurs

| erreur | où elle est traitée |
|---|---|
| 1 — « sans aucune mémoire » | note v2 : a.1, a.2, a.8, (b) 1 |
| 2 — « Yu et al. ne posent pas la question » | note v2 : a.2 point 1, (b) 1 premier tiret |
| 3 — « six travaux » | note v2 : (b) 1 dernier tiret |
| 4 — concepteur fort des voisins | note v2 : a.6, réserve 5 |
| 5 — ablation de SkillHone confondue | note v2 : a.7 |
| 6 — date de SkillHone | note v2 : a.7 |
| 7 — A2 | mémoire v2 : A2, règle de classement |
| 8 — D1 et D2 | mémoire v2 : D1, D2, réserve 7 |
| 9 — compte, « 3 sur 3 », « ± 10 % ne change rien » | mémoire v2 : compte, lecture du compte ; note v2 : c.10 |
| 10 — renvois à N-045 v2 et failles du plan | note v2 : c.2 à c.11 |
| 11 — courriel, question 4 | courriel v2 ; note v2 : a.2 point 1, (d) |
