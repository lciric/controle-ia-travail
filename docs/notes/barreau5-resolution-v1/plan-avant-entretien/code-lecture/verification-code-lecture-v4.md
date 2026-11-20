# Vérification du code de lecture v4 du barreau 5 (couples A à D de l'addendum 1)

Écrite le 20 novembre 2026 par le contre-lecteur du code de lecture, Claude Fable 5.2, sous-agent de la session mère (`session_01XJ6Mgr8BN6UanALsQatc5E`). Pièce d'instrument. Suite de `verification-corrections-code-lecture-v2.md` (`92d4f8fb…`).

Pièces, à la tête de `main` : rapport v4 (`1bc78521…`, lu en entier), `lecture_v1.py` (`d877d2de…`), amorce (`54a676f3…`), essais de la lecture (`3e7bc259…`), outil et sortie des mutations du développeur (`156a1d36…`, `53079730…`), addendum 1 scellé (`2afa2186…`). Les sept empreintes sont égales aux attendues. L'addendum scellé a l'empreinte du candidat que j'ai lu en entier à la vérification précédente : c'est le même texte, à l'octet.

## Verdict

**Conforme.** Aucune correction.

## 1. Les quatre couples, et rien d'autre

Différence de `lecture_v1.py` entre ma dernière vérification (commit `15edb889`) et cette version, lue en entier : cinq passages changés, tous des couples.

| couple | où | jugement |
|---|---|---|
| A, tâches retenues (addendum, point 2) | `manipulation` | appliqué à la lettre : le code est celui que j'avais donné. Les deux comptes et le motif du cas limite sont écrits dans `details` ; la fonction `d`, inchangée, écarte la famille sans tâche retenue de M1 et de M3 (choix « absente ») |
| B, borne de la phrase E (point 3) | `phrases` | appliqué à la lettre : `SEUIL_EMPREINTE * sep['delta_app']`, au même format que le reste de la phrase |
| C, en-tête et docstring de `manipulation` | en-tête du module | appliqué. L'en-tête cite l'addendum pour le niveau d'une issue, la règle 4, m_i et la borne ; il dit bien que M1 et M3 fondent les issues S, D et C |
| D, commentaire de `issue` | `issue` | appliqué à la lettre |

Rien d'autre n'a changé dans ce fichier : aucun calcul hors de `manipulation` et de la phrase E. Le niveau d'une issue et la règle 4 étaient déjà dans le code.

Une précision sur l'origine des couples. Les couples de code A à D sont ceux de ma vérification `fb1b7d04…`, section 5, comme le dit le rapport v4. Le fichier `contre-lecture-addendum-1-v1.md` porte aussi des couples nommés A à D, mais ce sont des couples sur le texte de l'addendum, non sur le code ; je n'y ai cherché que ces titres.

## 2. Les essais éprouvent les trois points

| point de l'addendum | cas sain | artefact | essai |
|---|---|---|---|
| point 2, tâche sans coût lisible chez un seul membre | deux tâches retenues, chaque membre y garde tous ses coûts lisibles (une ligne illisible du jumeau dans une tâche retenue ne la retire pas) | la troisième tâche, illisible chez le seul jumeau, sort pour les trois membres ; comptes 3 et 2 écrits | `test_addendum_point_2_tache_sans_cout_lisible_chez_un_seul_membre_…` |
| point 2, cas limite « absente » | neuf familles à huit tâches retenues, motif vide | une famille sans aucune tâche retenue : absente de M1 et de M3, motif écrit, neuf familles et seuil 1 ; E3 garde dix familles | `test_addendum_point_2_famille_sans_tache_retenue_absente_de_m1_et_de_m3` |
| point 3, borne de la phrase E | la phrase finit par la moitié du Δ_app qu'elle écrit elle-même | l'essai exige que cette moitié diffère du plus grand écart, l'ancienne lecture | `test_addendum_point_3_borne_de_la_phrase_e_moitie_de_la_separation_apprise` |
| point 1, niveau d'une issue | dix familles partout : aucun « 95 % » dans la phrase (témoin de l'essai de la phrase) | M1 seule à sept familles : issues D et C à 95 % ; M1 et M3 à sept par le cas limite : issue S à 95 %, « au plus 0,005 » | `test_niveau_de_l_issue_porte_celui_de_m1` (repris, en D et en C) ; `test_addendum_point_1_issue_s_…` |
| point 1, règle 4 | — | M1 seule à cinq familles : NI, un motif ; coûts illisibles : M1 et M3 à cinq, les deux dans le motif, séparés par « ; » | `test_manipulation_sous_six_familles_motif_niveau_non_atteignable` (repris) |

Les trois essais repris retirent bien les saboteurs de la table au lieu de rendre leurs coûts illisibles, comme je l'avais demandé ; le motif attendu a changé là où il devait.

## 3. `MIN_ESSAIS=146` est juste

Les essais de la lecture passent de 97 à 102 : quatre essais neufs, et un essai repris joué deux fois (D et C). 102 + 20 + 24 = 146. Seule cette ligne change dans l'amorce. L'essai qui exige l'égalité avec le compte collecté passe.

## 4. Essais et mutations

- Les six fichiers de la lecture, d'un seul passage sur le dépôt : **244 passés, aucun échec**, en 551 s (même compte que le rapport v4).
- Trois mutations sur les couples A et B (`mutations-verification-v3.py`), témoin vert (102 passés) : **3 attrapées sur 3**.

| id | défaut réintroduit | essais qui l'attrapent |
|---|---|---|
| Y1 | couple A : chaque membre reprend sa moyenne sur ses propres tâches lisibles (l'ancienne lecture) | quatre, dont les deux essais du point 2 |
| Y2 | couple A, cas limite : famille sans tâche retenue comptée pour une différence nulle (l'option que Lazar n'a pas retenue) | trois, dont l'essai du cas limite |
| Y3 | couple B : borne égale à Δ_app entier | l'essai du point 3 |

## 5. Hors de ce qui m'était soumis

La même plage de commits ajoute deux modules sous `src/controle_ia/barreau5_familles/` (`epreuve_verite_plantee_v1.py`, `juge_verite_plantee_v1.py`) et un fichier d'essais. Je ne les ai pas ouverts : la fabrique des mondes revient à un autre agent. Deux conséquences à connaître :
- ils sont sous `src/`, donc dans l'arbre gelé que compare la garde du code au commit : le commit de `CODE-LECTURE-B5F` doit les porter dans leur état final, sinon la marche et l'ouverture refuseront ;
- leur fichier d'essais commence par `test_barreau5_familles_` mais n'est pas un des trois que joue l'amorce : le plancher de 146 n'en dépend pas.

Restent, inchangés : la garde de l'arbre extrait à jouer tôt sur le dépôt réel ; la branche des entrées, d'un seul commit, avant la commande de création.

## Procédure

Aucun réseau, une commande simple à la fois, aucun refus d'outil, aucun commit, aucune dépense. Temporaires sous `/dev/shm/b5f-contre-lecture/` et copie de travail sous le bloc-notes, effacés. Rien de `diag/`.
