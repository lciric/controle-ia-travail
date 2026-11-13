# Contre-lecture différentielle (R2) — `lanceur_v19` : relance seule et assemblage — témoin de Bailey, v1

**Verdict : conforme après corrections.** Les constats C-1 à C-9 de la relecture v18 sont traités, et la différence
v18 → v19 ne contient rien d'autre que ce qui est annoncé. Les nouvelles gardes d'entrée sont toutes placées avant la
création de l'instance et avant toute dépense. Dans le cas réel, `verifier_relance_seule` passe avec les sept instances
antérieures du script v12 (appel fait, voir § 2). Aucun constat n'est bloquant pour le lancement prévu, mais deux points
sont à faire avant :
- R-1 : la garde C-1 est juste mais pas suffisante. « Dépense des antérieures ≥ D₁ » ne prouve pas que le coût de la
  première exécution est compté. La borne proposée en v18 et l'égalité des taux sont à ajouter.
- R-2 : le script de conduite doit passer à `lanceur_v19` et fournir les deux nouveaux champs, avec un chemin absolu
  pour le manifeste.

Les autres constats (R-3 à R-8) sont des remarques : des essais manquent, un motif d'essai est trop large, une copie est
sautée en silence.

Contre-lecteur neuf, auteur d'aucun des fichiers relus ni du rapport v18. Cloisons tenues : je n'ai ouvert aucun journal
de notes, aucun journal technique, ni le journal des durées ou des gardes. Je n'ai lu ni `etat.md` ni `decisions.md`, et
aucun fichier sous `donnees/bras-attaque*`, `donnees/mode-tenu-a-l-ecart*` ou `docs/notes/bras-attaque/`. Du dossier
`reprise-v10-2/`, j'ai lu seulement `manifeste-v3-regle.json` : ses clés et sa `regle_tours`, qui sont des paramètres de
budget (B, R, D, c, t, H, K). Je n'ai fait aucune commande réseau et je n'ai modifié aucun fichier existant.

## Objets relus (empreintes : début du SHA-256)
| Objet | Empreinte | Note |
|---|---|---|
| `src/controle_ia/temoin_bailey/lanceur_v19.py` | `1fa00722886ca2de…` | commit `10a2cd15`, compagnon vérifié |
| `tests/test_temoin_bailey_condition6_v19.py` | `c55a0e04d5f6876d…` | commit `10a2cd15`, compagnon vérifié |
| `docs/notes/…/relecture-code-condition6-v18-relance-seule-bailey-v1.md` | `cd540827665767…` | conforme à la citation de la docstring v19 |
| `runs/temoin-bailey-v1-20261111/lancer-conduite-v12.py` | `684eb5efcdecbac7…` | commit `4abda085`, non scellé, inchangé depuis la relecture v18 |
| Autres fichiers lus | — | `lecture_v8.py` (`_etat_etape`, `valider` l. 455-470, `lire` l. 750-775) ; `analyse_v3.nombre_de_tours` ; `scellement.verifier` ; `lanceur_v19.py` (`Poste`, `instances_du_poste`, `conduire`, `fabriquer_archive`) |

Essais lancés :
- `pytest -q -p no:cacheprovider tests/test_temoin_bailey_condition6_v19.py -k test_v19_` : **29 passés**, 169
  désélectionnés, aucun sauté, en 70 s. L'essai sur la structure réelle a donc tourné.
- 15 essais de contre-lecture, hors du dépôt, dans
  `/tmp/claude-0/-home-user-controle-ia-travail/2cfa1854-671e-5aa7-83ff-79ac90ee7d37/scratchpad/test_relecture_v19.py` :
  15 passés en 48 s. Ils reprennent les aides du fichier d'essais v19 et sont décrits aux constats.

## 1. La différence v18 → v19, constat par constat
La différence (`diff lanceur_v18.py lanceur_v19.py`) contient seulement :
- la docstring ;
- `VEILLEUR_MODULE` et son commentaire ;
- deux chaînes qui nomment le module (`lanceur_v19 veilleur-arret`, `lanceur_v19 reprendre`), conséquence directe du
  changement de module ;
- l'appel des gardes d'entrée (l. 1628-1629) ;
- `_relance_seule` (l. 1785-1802) ;
- `verifier_relance_seule` (l. 2594-2624) ;
- trois blocs d'`assembler_lecture` (l. 2670-2676 et 2688-2693).

Aucune autre ligne ne change.

| Constat v18 | Traitement v19 | Jugement |
|---|---|---|
| C-1 (D compte les antérieures) | l. 2619-2624 : `instance_premiere` parmi les antérieures, et dépense des antérieures ≥ D₁ | Juste, mais insuffisant : voir R-1 |
| C-2 (même mise en place) | l. 2673-2676 : égalité de `pas_par_tour`, `longueur_suffixe`, `ecart_10` et `empreintes_cibles_attendues` entre l'état de mise en place de la relance et celui de la première, tous deux lus par `lc._etat_etape` | Bonne comparaison pour la lecture, partielle pour l'instance : voir R-3 |
| C-3 (H recalculé) | l. 1791-1800 : `H_heures` vient de `an.nombre_de_tours(B, D, c, t)` ; `premiere_execution` garde l'ancien | Conforme. Essai hors du dépôt : le H de la relance diffère de celui de la première, donc l'essai du dépôt ne passe pas pour une mauvaise raison |
| C-4 (gardes d'entrée) | l. 2611-2618 : B égal au B du manifeste ; K₁ ≥ 20 ; K′ < K₁ ; empreinte du manifeste de la règle vérifiée ; règle passée égale à la `regle_tours` scellée | Conforme. Les gardes tombées de la première ne sont pas vérifiées à l'entrée : voir R-8 |
| C-5 (graines, code public, B) | l. 2670-2672 : présents et égaux | Conforme. Le cas « différents » n'a pas d'essai dans le dépôt : voir R-4 |
| C-6 (motif de l'essai) | essai l. 4097 : `GardeArret`, motif « empreinte » | Mieux, mais le motif reste trop large : voir R-5 |
| C-7 (essais) | (a) l. 3997, 3955-3974 ; (b) l. 3887 ; (c) l. 3902 ; (d) l. 4073, 4081 ; (e) partiel | Voir R-4 |
| C-8 (cosmétique) | commentaire corrigé ; `m_mep` retiré de `_relance_seule` (il reste utilisé par le pilote, l. 1719) | Conforme |
| C-9 (manifestes de la relance) | l. 2688-2693 : copie sous `relance-manifestes/` | Conforme, avec une copie sautée en silence : voir R-6 |

**Emplacement des gardes d'entrée.** `verifier_relance_seule` (l. 1629) s'exécute dans cet ordre :
- après `instances_du_poste`, la vérification du GO et de sa non-révocation, l'échéance, le seuil local, `GO_ID` et le
  jeton ;
- **avant** le contrôle du dossier de sortie, `mkdir`, `fabriquer_archive`, `Poste` et `fournisseur.creer`
  (l. 1630-1650).

Aucune garde ne peut donc tomber après une dépense. `scellement.verifier` lève `GardeArret`, comme les autres gardes.
Essai hors du dépôt `test_gardes_d_entree_aucun_dossier_de_sortie` : avec l'artefact `instance_premiere` absente, il n'y a
ni `creer` ni dossier de sortie.

**Comparaison C-2.** `lire` audite la relance avec `validite_["mise_en_place"]`
(`lecture_v8.py:465`, puis l. 762-765 : `pas_par_tour`, `empreintes_cibles_attendues`, `ecart_10`). C'est l'état
`_etat_etape(racine, "mise-en-place", …)` du dossier assemblé, c'est-à-dire celui de la **première** conduite. Comparer
ce même état, lu par la même fonction, à l'état de la relance est donc la bonne comparaison pour la lecture.
`longueur_suffixe` en plus est prudent. Les quatre champs sont vérifiés dans les deux sens par des essais hors du dépôt :
chaque champ modifié est refusé. Un état de la première absent est refusé aussi (par `mep1 = {}`, avec un message
trompeur : voir R-7).

## 2. Le cas réel : `lancer-conduite-v12.py` → `lanceur_v19`
J'ai appelé `verifier_relance_seule` en Python avec les valeurs suivantes :
- les `ANTERIEURES` du script, chargées depuis le fichier puis passées par `instances_du_poste(…, 75.0)` ;
- K′ = `TOURS_COMPLETS_PREMIERE` = 8, la constante du script (le journal des durées n'a pas été lu) ;
- la `regle_tours` de `sortie-conduite-v11/reprise-v10-2/manifeste-v3-regle.json` ;
- `instance_premiere = "60417353"` et B = 75.

**Résultat : la garde passe.** Elle passe avec le manifeste en chemin absolu, en chemin relatif depuis la racine du dépôt,
et avec l'identifiant donné en entier.

| Grandeur | Valeur |
|---|---|
| Règle de la première | B = 75,0 ; R = 10 ; D₁ = 5,0331 ; c₁ = 1,342111… ; t = 1 315,9926 s ; H = 44,68 h ; K = 72 |
| Dépense des sept antérieures | 14,4398 USD (≥ D₁) |
| Coût de 60417353 seule | 11,6617 USD ; son c (1,342111…) est égal à c₁ |
| Borne v18 : D₁ + c₁ × K′ × t / 3 600 | 8,9580 USD : satisfaite aussi |
| K de la relance (c de 1,2 à 1,6 ; mise en place de 0,5 à 1 h) | 72 dans les six cas |

À changer dans le script (constat R-2) :
1. l. 77 : `from controle_ia.temoin_bailey import lanceur_v19 as L`.
2. `relance_seule()`, l. 134 : ajouter `"instance_premiere": "60417353"` et `"manifeste_regle": str(m)`.
   - `m` vaut `REPRISE / "manifeste-v3-regle.json"`, un chemin **absolu** puisque `BASE` l'est.
   - Il ne faut **pas** passer le chemin relatif `sortie-conduite-v11/reprise-v10-2/manifeste-v3-regle.json` : il serait
     résolu depuis le dossier courant (la racine du dépôt), et la garde tomberait sur « fichier absent ».
3. La docstring, l. 3, 5 et 64-66, nomme encore `lanceur_v18`, « commit du code v18 », `lanceur_v13`, `4988f3f4` et
   `bilan-lancement-v2.json` (C-10 de la v18, non corrigé). `manifeste-local-v6.json` est encore absent. Son
   `commit_code` doit être un commit qui contient `lanceur_v19` (≥ `10a2cd15`), pour que l'ordre de lancement
   (l. 1663) nomme le code qui conduit. Le code envoyé sur l'instance (`CHEMINS_ARCHIVE`) n'a pas changé de v18 à v19.
4. R12 : le script v12 est commité (`4abda085`) et écrit pour `lanceur_v18`. Je recommande un nouveau nom
   (`lancer-conduite-v13.py`, avec sortie, bilan et PID en v13) plutôt qu'une réécriture du v12, puis le scellement du
   script et du manifeste v6 avant le lancement.
5. Point préexistant, mineur : le fichier PID est écrit (l. 153) avant le contrôle du bilan (l. 156) et avant
   `relance_seule()`. Un refus à ces étapes laisse un PID qui bloque un nouvel essai sous le même nom (R12). C'est
   prudent, mais il faut le savoir.

## Constats
| N° | Gravité | Fichier : ligne | Constat et preuve | Correction proposée |
|---|---|---|---|---|
| R-1 | à corriger (non bloquant ici) | `lanceur_v19.py:2619-2624` ; `instances_du_poste`, l. 706-719 | La garde C-1 exige la **présence** de l'instance de la première et une dépense des antérieures ≥ D₁. Or D₁ est la dépense **au moment de la règle**, avant le run principal. Si la destruction de 60417353 est mal relevée (par exemple 1,7 h après sa création), la somme vaut environ 5,06 ≥ 5,0331 : la garde passe, et D est sous-compté d'environ 9,4 USD. La garde « B − 2 » laisserait alors dépasser B d'autant. Preuve : essai hors du dépôt `test_c1_destruction_de_la_premiere_tronquee_passe_la_garde`. Par ailleurs, `instances_du_poste` accepte destruction < création, donc une durée négative qui réduit la somme (essai `test_c1_duree_negative_acceptee_par_instances_du_poste`). Cas réel : 14,44 ≥ 8,96, donc sans effet sur le lancement prévu. | Dans `verifier_relance_seule`, exiger trois choses : (i) dépense des antérieures ≥ D₁ + c₁ × K′ × t / 3 600, la borne de la relecture v18 ; (ii) `c` de `instance_premiere` égal à c₁ de la règle (vrai dans le cas réel) ; (iii) dans `instances_du_poste`, destruction ≥ création. Essais : cas sain réel, et l'artefact « destruction tronquée ». |
| R-2 | à faire avant le lancement (script, hors du code relu) | `lancer-conduite-v12.py:3, 5, 64-66, 77, 123-134` | Le script importe `lanceur_v18`. `relance_seule()` ne rend ni `instance_premiere` ni `manifeste_regle` : avec `lanceur_v19`, la garde tomberait sur « … instance et manifeste de la première exécution requis » (avant toute création, donc sans dépense). Docstring périmée (C-10 v18). | Voir § 2, points 1 à 4 : import v19, deux champs avec chemin absolu, manifeste v6 au commit v19, nouveau nom (R12), scellement, contre-lecture du script. |
| R-3 | remarque | `lanceur_v19.py:2673-2676` | C-2 compare les **états** de mise en place, ce qu'utilise la lecture. Mais l'instance de la relance lit `pas_par_tour` dans le **manifeste** « relance » (l. 1703-1704, puis 1799), et ce manifeste n'est pas comparé au manifeste de la règle de la première, qui porte `pas_par_tour`, `longueur_suffixe` et `ecart_10`. Preuve : essai hors du dépôt `test_c2_manifeste_relance_different_de_la_premiere_accepte`. Avec des états égaux et un `pas_par_tour` du manifeste « relance » différent, l'assemblage accepte. Les deux viennent de la même sortie de commande : risque faible. | Ajouter l'égalité de ces trois champs entre `m_rel` et `m_reg`, comme le proposait la seconde moitié de C-2. |
| R-4 | remarque (essais) | `tests/…_v19.py:3955-3994, 4064-4070, 4102-4112` | (a) C-2 : seul `pas_par_tour` est essayé. (b) C-5 : la docstring dit « absents des deux côtés, puis différents », mais l'essai ne fait que retirer les clés. (c) C-4 : aucun essai pour un manifeste de la règle altéré ou absent, ni pour l'absence des clés `instance_premiere` ou `manifeste_regle`. (d) « avant toute création » n'essaie qu'un artefact et ne vérifie pas l'absence du dossier de sortie. (e) aucun essai du cas réel (les sept antérieures, la règle réelle). Tous ces cas se comportent correctement dans les essais hors du dépôt (`test_c2_autres_champs_refuses` ×3, `test_c5_differents_refuses` ×3, `test_c4_manifeste_regle_altere_refuse`, `…_absent_refuse`, `test_gardes_d_entree_aucun_dossier_de_sortie`). Aucun essai du dépôt ne passe pour une mauvaise raison : le H de C-3 diffère bien de celui de la première ; « K′ ≥ K » n'est pas atteignable après K′ < 20 ≤ K, comme le dit l'essai. | Paramétrer C-2 sur les quatre champs. Ajouter le cas « différents » à C-5, les artefacts de manifeste et de clés à C-4, et l'absence du dossier de sortie. Ajouter un essai de la garde sur les valeurs réelles. |
| R-5 | remarque | `tests/…_v19.py:4097` | Le motif « empreinte » couvre aussi le message C-2 « (« empreintes_cibles_attendues ») ». L'essai passerait si cette garde tombait à la place du scellement. Ce n'est pas le cas ici, puisque l'altération vise `principal-relance`, mais le motif ne le distingue pas. | Motif « ≠ scellée ». |
| R-6 | remarque (R5 : aucun repli silencieux) | `lanceur_v19.py:2692` | `if src.is_file()` saute en silence un manifeste absent de la conduite de relance. Preuve : `test_c9_manifeste_initial_absent_saute_en_silence`. Les trois manifestes existent toujours quand `principal-relance` a tourné : le cas est anormal et devrait refuser. | Exiger les trois manifestes et leurs compagnons ; sinon `GardeArret`. |
| R-7 | remarque (cosmétique) | `lanceur_v19.py:2620, 2673` | La branche `.get("destruction") is None` est inatteignable, parce que `instances_du_poste` refuse avant. `mep1 = … or {}` refuse un état de la première absent avec le message « mise en place de la relance différente », qui est trompeur. | Message propre pour un état absent de la première ; retirer la branche morte ou la commenter. |
| R-8 | remarque | `lanceur_v19.py:2594-2624` | Les conditions de `relance_permise` pour la première exécution (ni « sonde orientée » ni « dépense » parmi les gardes tombées) ne sont pas vérifiées à l'entrée. Elles ne sont rattrapées qu'à la lecture, donc après la dépense. La v18 le suggérait (C-4, « au besoin »). Je n'ai pas ouvert le journal des gardes. | Faire lire par le script, ou par une garde, les gardes tombées de la première dans le journal des gardes et dans `gardes-lanceur` (aucune note), et refuser sur « sonde orientée » ou « dépense ». |
