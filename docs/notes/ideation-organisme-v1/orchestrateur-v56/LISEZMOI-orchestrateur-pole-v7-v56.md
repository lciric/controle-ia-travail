# Orchestrateur du pôle scientifique automatique — v56 (corrections de la contre-lecture CL20)

**Verdict de l'auteur** : les 15 constats de CL20 sont traités dans une couche v56 neuve (R12 : aucun fichier de la v55 n'est
modifié) ; aucun lancement réel n'est essayé ici (processeur seulement, sans réseau, sans clé). Le pré-pilote reste
**non lançable** tant que N5 (A21), le gel du brouillon 10 (contre-lecture 5) et les pièces externes ne sont pas là (section 5).

Rédaction : un premier rédacteur (Opus) a été coupé le 31 octobre vers 13:30 UTC ; son travail en cours, archivé et scellé
(`orchestrateur-v56-travail-coupe-v1/v56dev-2026-10-31-1330.tar.gz`, empreinte `e4908c4f…` vérifiée contre son compagnon), a été
déplié dans un dossier temporaire neuf hors du dépôt, relu et vérifié par un second rédacteur (Opus, 1er novembre 2026), qui l'a
corrigé, complété, essayé et livré. Rien de ce travail coupé n'avait été essayé.

## 1. Ce qui est livré

| fichier | rôle |
|---|---|
| `pole/budget_v56.py` | règle d'A1 du brouillon 10 (plafonds de relais du devis v6, plafond dur fixé au lancement), statuts de coupure de la ligne 11b, second programme (`rejouer_consommations_v56`), formule indépendante (`plafond_independant`) |
| `pole/adaptateurs_v56.py` | commande externe qui recopie le modèle servi (CL20-01) ; portes de plafond d'étape (`noyau`, `environnement`, `commande`) ; contrôle de la lecture interdite du kit (CL20-06) |
| `pole/noyau_v56.py` | `OrchestreV56` : budget v56, plafond recalculé deux fois puis transmis et accusé à chaque lancement d'étape, A2 en arrêt de rôle, présence des verdicts, arrêt propre sur signal |
| `pole/course2_v56.py` | génération et course : fusions complètes seules, archive `fusions-inachevees.json`, déclaration des bras sans repli silencieux, causes de M9, fin écrite sur tout chemin |
| `pole/prepilote_v56.py` | pré-pilote : É9 entière lue réduite, M6b écrite en É1, `_exempts_a8` retiré après É3, S6 avec numérotation, D-i, interrupteur A21 en attente de N5 |
| `pole/configuration_v56.py` | plan de dépense v56, DEP4 et A15 (porte par relais), spécification scellée, Gu-Krenn « substitut », D-i recoupé |
| `pole/etage_entre_generations_v56.py` | machine jetable par liste blanche (variable `POLE_MACHINE_JETABLE_V56`) |
| `pole/gardes_e0_v56.py` | table R5 v56 : lignes 1, 5, 11a, 11b, 29 |
| `pole/simulation_v56.py` | moteur simulé : rédacteur de M6b |
| `demonstrations/ideation_v8.py` | lanceur v8 (rend la main au v7 sans `--course-2` ni `--pre-pilote`) |
| `essais/aides_v56.py`, `essais/test_v56_corrections.py`, `essais/mutations_v56.py` | aides, essais, banc de mutations |

L'arbre du dossier reprend, à l'identique, chaque fichier de `EMPREINTES-orchestrateur-pole-v7-v55.txt` (406 fichiers, empreintes
vérifiées à la copie, dont 116 compagnons `.sha256` historiques déjà listés par la v55) et cette liste elle-même ; s'y ajoutent les
13 fichiers v56 ci-dessus et les trois livrables. Aucun compagnon `.sha256` neuf n'est écrit (les compagnons par fichier que
l'appelant a ajoutés à la v55 ne sont pas recopiés) : le scellement est laissé à l'appelant.

## 2. Table « constat CL20-xx → fichier et ligne »

| constat | gravité | correction (fichier:ligne) | essais (cas sain / artefact) | mutations |
|---|---|---|---|---|
| CL20-01 | bloquant | `pole/adaptateurs_v56.py:54-95` (`AdaptateurCommandeExterneV56.lancer` recopie `modele_servi` après le contrôle de la commande) ; `demonstrations/ideation_v8.py:59-81` (le lanceur branche Argon par cette classe) ; `pole/gardes_e0_v56.py:49-74` (ligne 1 de la table R5 sur le vrai adaptateur) | `TestCL20_01AdaptateurReel` : vrai adaptateur sur une commande factice (servi égal / v55 qui le perd, servi absent, servi autre) ; **flux complet** d'une génération dont Argon passe par le vrai adaptateur (cas sain : aucun arrêt, verdicts d'Argon lus) ; artefact : adaptateur v55 dans le même flux → arrêt du rôle, pas de l'exécution | 2 |
| CL20-02 | bloquant | `pole/budget_v56.py:118-249` (règle d'A1, plafond dur au centime inférieur, statuts 11b `:105-115`), `:252-328` (second programme, formule indépendante, vérifications 11a) ; `pole/noyau_v56.py:225-283` (recalcul double, transmission, accusé, plafond tenu par appel, coupure, arrêt si cumul > S17) ; `pole/adaptateurs_v56.py:108-219` (portes) ; `pole/configuration_v56.py:42-113` (plan v56, `reservation_usd` et `dep4_phrase` refusées), `:162-180` (A15 : porte par relais) ; `pole/prepilote_v56.py:268-281` (É9 entière : réduction vérifiée d'abord, `lue_reduite`) ; `pole/gardes_e0_v56.py:77-132` (lignes 11a, 11b) | `TestCL20_02Budget` (17 essais : formule, protégée qui n'affame pas les suivantes, rejeu des plafonds depuis `consommations.json`, réservation et phrase DEP4 refusées, relais réel sans porte, porte qui accuse faux, porte en retard, second programme et formule indépendante faussés, relais qui ne tient pas son plafond, protégée coupée → nœud, É9 lue réduite / non mesurée) | 15 |
| CL20-03 | majeur | `pole/configuration_v56.py:119-151` (préenregistrement et contre-lecture nommés, à leur empreinte, scellés, sans marqueur, empreinte de la contre-lecture citée) ; `demonstrations/ideation_v8.py:88-91` (exigée conforme au moteur réel) ; manifeste de départ (`pole/course2_v56.py:308-320` ; `pole/prepilote_v56.py:291-311`) ; `pole/gardes_e0_v56.py:135-165` (ligne 29) | `TestCL20_03Specification`, `TestLanceurV8.test_moteur_reel_refuse_sans_specification_conforme` | 5 |
| CL20-04 | majeur | `pole/noyau_v56.py:39-90` (`ArretSurSignal`, `ArretParSignal`, `motif_arret`) ; `pole/course2_v56.py:322-386` (fin écrite sur tout chemin : sessions rangées, consommations, archive des fusions, manifeste de fin, empreintes de sortie) ; `pole/prepilote_v56.py:291-350` ; `pole/course2_v56.py:393-442` (bilan de course) ; lanceur : code 2 | `TestCL20_04Signal` : aucun signal (cas sain, gestionnaires restaurés) ; SIGTERM et SIGINT reçus pendant un appel (génération, pré-pilote) ; interruption clavier ; **SIGTERM envoyé par identifiant de processus à un enfant** en cours d'étape | 3 |
| CL20-05 | majeur | `pole/course2_v56.py:180-289` (entrée du bisociateur sans fusion ; archive des fusions non écrites, incohérentes, sans passeport, non jugées, jugées en partie, ou d'une étape des fusions coupée ; `lot_mesure` : complètes seules) ; `pole/noyau_v56.py:192-222` (présence des verdicts) | `TestCL20_05Fusions` : cas sain (3 fusions complètes dans les quatre canaux) ; artefacts : plafond de relais des fusions à 0 ; 0,02 ; 0,04 ; 0,07 ; 0,13 USD, fusion incohérente, fusion jugée en partie dans une étape jouée ; contrôle des quatre canaux (classement et fiches, mémoire, héritage, entrée de l'étage) | 6 |
| CL20-06 | majeur | `pole/adaptateurs_v56.py:225-251` ; `pole/noyau_v56.py:108-113` (vérifié à la construction, sessions rangées sinon) ; `demonstrations/ideation_v8.py:59-81` (`interdire_lecture = [base des sessions, sortie]`, base créée avant les adaptateurs) | `TestCL20_06LectureInterdite` | 3 |
| CL20-07 | majeur | `pole/prepilote_v56.py:99-115` (`prepilote.d_i` exigé ; (2) et (3) refusés : non codés) ; `pole/configuration_v56.py:192-193` (D-i recoupé avec `decisions_a15.d_i`) | `TestCL20_07DiEtN5` | 2 |
| CL20-08 | majeur | `pole/prepilote_v56.py:61-82` (liste scellée DEP2c), `:116-130` (pièces `m6b.fiches` / `.sources` refusées), `:177-206` (rédaction en É1, tirage `pp2-m6b`, clé au coffre), `:245-287` (É9b sur les fiches scellées d'É1, ligne 31 sur le flux complet) ; `pole/simulation_v56.py` | `TestCL20_08M6b` : flux complet (aucune source dans l'entrée du vérificateur) ; artefacts : source citée par la fiche, fiche mal formée, fiches écrites hors du pré-pilote, fiches modifiées avant É9b | 5 |
| CL20-09 | mineur | `pole/prepilote_v56.py:210-214` | `TestCL20_08M6b.test_cl20_09_…` (présente pendant É3, retirée après) | 1 |
| CL20-10 | mineur | `pole/configuration_v56.py:53-62` (mode « substitut » seul ; « modele » refusé avec son motif) ; `pole/course2_v56.py:58-157` (forme de l'annexe vérifiée d'abord ; refus légitimes nommés ; toute autre exception = `ErreurInterneBras`, arrêt) | `TestCL20_10_11Bras` | 3 |
| CL20-11 | mineur | `pole/course2_v56.py:291-304` ((iii) Gu-Krenn « moins de 2 fiches notables » ; (iv) bras basique « moins de 2 fiches étiquetées » ; cause méta hors texte retirée) | `TestCL20_10_11Bras.test_cl20_11_causes` | 2 |
| CL20-12 | mineur | `pole/noyau_v56.py:137-189` (A2 « modèle servi absent » : arrêt de ce rôle), `:206-211` (version de juge changée : arrêt de ce rôle) | `TestCL20_12A2Role` | 2 |
| CL20-13 | mineur | `pole/prepilote_v56.py:41-55` (numérotation de liste comptée à part) ; `pole/gardes_e0_v56.py` (ligne 5) | `TestCL20_13_14` | 1 |
| CL20-14 | mineur | `pole/etage_entre_generations_v56.py:23-46` (liste blanche fermée, noms exacts ajoutés par la configuration, nom de clé refusé même ajouté ; variable `POLE_MACHINE_JETABLE_V56`) | `TestCL20_13_14.test_machine_jetable_liste_blanche` (les 11 noms que CL20 avait vus passer sont refusés) | 2 |
| CL20-15 | mineur | ce LISEZMOI, section 4 ; `essais/test_v56_corrections.py` ne lit rien hors de l'arbre ; essai R12 v56 ignoré, motif dit, si la liste v55 manque | `TestR12V56` | — |
| N5 (CL19-03) | décision de Lazar | **non tranché** : `pole/prepilote_v56.py:35-36, 109-115` — interrupteur `prepilote.a21_lecture`, documenté « en attente de N5 » : absent ou `programme_journalise` = comportement v55 (défaut) ; `stricte` = refus de lancement (non codé) ; écrit au manifeste de départ | `TestCL20_07DiEtN5.test_n5_…` | 1 |

## 3. Essais et mutations (rejoués sur l'arbre livré, dans un miroir du dépôt hors du dépôt)

Python 3, pytest 9.1.1, `python -I -B`, processeur seulement, sans réseau ; miroir du dépôt hors du dépôt (ce dossier + les trois
fichiers de contexte de la section 4) ; machine partagée (temps indicatifs).

| mesure | résultat |
|---|---|
| `essais/test_v56_corrections.py` seul | 64 essais réussis, 0 échoué (sous-essais compris), environ 30 s |
| Suite entière (`essais/`), sans déclaration | 771 réussis, **14 échoués**, 1 ignoré, 487 sous-essais, 514 s : les 14 échecs sont tous des essais de bac réel qui exigent `bwrap` (absent ici) et refusent d'être ignorés en silence (CL15-04) |
| Suite entière, `POLE_ESSAI_BAC_REEL_NON_JOUE=1` (déclaration explicite, comme la v55) | **772 réussis, 1 échoué, 13 ignorés**, 487 sous-essais, 535 s ; l'échec est `test_v51_bac_reel.py::TestV51::test_v51_06_programme_du_filtre_d_appels_systeme` (exige le vrai bac, comme en v55) ; ignorés : 12 essais de bac réel, motif « ESSAI RÉEL NON JOUÉ », et 1 « kit d'agent absent » |
| Banc de mutations `essais/mutations_v56.py` | **156 mutations (v54 : 56, v55 : 47, v56 : 53), 156 tuées pour la raison attendue**, 0 autre raison, 0 défaut du banc, 0 survivante, 0 non appliquée ; témoin avant et après : 175 essais, 0 échec ; 335 s |

Audit de propreté (R4) : 53 sur 53 n'est pas tenu pour une preuve d'absence de défaut ; un premier passage avait montré 2
survivantes (deux gardes de défense en profondeur que les essais ne pouvaient distinguer : l'essai de l'entrée du bisociateur a été
rendu discriminant, une mutation mal formée a été réécrite), 2 « autres raisons » (motifs attendus corrigés après lecture de la
trace) et 4 fragments mal indentés (corrigés). Le banc ne dit rien des gardes absentes.

## 4. Comment jouer la suite (CL20-15)

Depuis ce dossier, dans le dépôt : `python3 -I -B -m pytest -q -p no:cacheprovider essais/` et `python3 -I -B essais/mutations_v56.py
[--raisons] [--v56-seulement]`. La suite entière lit, hors de ce dossier, `../EMPREINTES-orchestrateur-v52b.txt`, le brouillon 7
et l'annexe réelle du bras méta (`brouillons/…/pre-pilote-course-2-v1/`) : elle se joue **dans le dépôt** (ou un miroir qui porte
ces trois fichiers). L'archive `CODE-orchestrateur-pole-v7-v56.zip` porte le code (même périmètre que l'archive v55 : `pole/`,
`essais/`, `demonstrations/`, `exemples/`, `conception-v7-v1.md`) ; `essais/test_v56_corrections.py` s'y joue seul (l'essai R12 v56
est alors ignoré avec son motif, la liste v55 n'étant pas dans l'archive) ; les essais R12 des versions antérieures exigent
l'arbre complet du dossier.

## 5. Choix pris seuls (à relire)

1. **D-CL20-1** : la règle du brouillon 10 (option (a), relais du devis v6) est codée, comme la consigne le demande ; la règle
   « réservation » n'est plus jouée par la v56 (refusée à la configuration).
2. **Plafond dur** arrondi au centime **inférieur** ; le plafond transmis au relais et celui que tient l'orchestrateur sont le même
   nombre de centimes ; égalité « au centime » pour le second programme, la formule indépendante et l'accusé.
3. **Portes de plafond** : trois formes (noyau pour le moteur simulé seulement, refusée pour un relais réel ; environnement de la
   commande d'Argon, `ETAPE_POLE` et `PLAFOND_ETAPE_USD` ; commande de l'opérateur qui relance un relais persistant et accuse par
   une ligne JSON). Le relais Kimi v4 et le relais de Claude doivent fournir cette commande (A15) : **elle n'existe pas encore**.
4. **Fusions** (défaut (b) de D-CL20-2, recommandé par CL20) : seules les fusions complètes reviennent ; ajout de ma part : une
   étape des fusions coupée par son relais ou non mesurée ne rend **aucune** fusion (même complète avant la coupure) ; toutes sont
   archivées avec leur cause, jamais le bras.
5. **CL20-12** : A2 arrête le rôle (texte du brouillon 10), plus l'exécution ; la réponse n'est pas lue ; A14 juge ensuite l'étape.
6. **CL20-11** : « notables » de la cause (iii) lu comme « au moins deux concepts lus » (interprétation du premier rédacteur,
   gardée) ; à confirmer sur le texte.
7. **CL20-13** : la numérotation (1 ou 2 chiffres suivis de « . » ou « ) » en début de ligne, après tiret ou puce, ou après « : »
   et « ; ») est comptée à part ; « 2 axes », une année, un décimal restent des nombres ajoutés. Le maximum reste à Lazar.
8. **CL20-01** : la commande d'Argon reçoit aussi `ETAPE_POLE` et `PLAFOND_ETAPE_USD` ; un second contrôle de conformité du modèle
   servi à la recopie est gardé en défense en profondeur (le contrôle de la commande v49 le précède : aucun essai ne peut le
   distinguer, il n'a pas de mutation).
9. **Signal** : SIGTERM et SIGINT seulement (SIGKILL ne se rattrape pas : la destruction de la machine jetable ne laisse aucune
   fin écrite, limite déclarée) ; un signal reçu pendant l'écriture de la fin est noté, sans lever.
10. Lanceur v8 : la base des sessions est un dossier temporaire neuf, créé avant les adaptateurs ; le dossier de base d'une course
    vide en fin de course peut rester (vide).

## 6. Ce qui reste (hors de ce code ou à décider)

- **N5** (A21, CL19-03) : ta réponse ; l'interrupteur ne fait que refuser la lecture « stricte », non codée.
- **D-i** : seule la variante (1) est codée ; (2) et (3) sont refusées tant qu'elles ne sont pas codées.
- **D-g** (b) : le texte du brouillon 10 et ce code concordent (rédacteur en É1) ; la liste scellée des sources (DEP2c) et la
  consigne de rédaction sont à fournir.
- **Commandes de porte** des relais persistants (Kimi v4, Claude) et lecture de `PLAFOND_ETAPE_USD` par la commande d'Argon :
  à écrire côté opérateur ; sans elles, A15 refuse tout lancement réel.
- **DEP3** : l'analyseur de l'étage 1 n'existe pas ; la ligne de commande seule ne démarre pas le pré-pilote (inchangé).
- Pièces externes (lignes 6, 8, 9, 10, 17, 19), lots du bras d'attaque (sinon M4 « non étalonné »), fiches d'antériorité d'É9.
- Course 2 : `verifier_go_v56` reprend l'égalité exacte de la v55 entre la cellule de plafond et le montant requis ; le
  GO-2026-10-31-04 (160 USD « séquencé ») ne se lira pas tel quel (CL20, §9) — à trancher.
- Essais de bac réel (`bwrap`) : à jouer sur la machine du run ; contre-lecture neuve de la v56 (R2) avant tout lancement.

## 7. Réserves

- Le chiffrage de C13 du devis v6 n'est pas rejoué ici.
- La porte « commande » et la porte « environnement » n'ont été essayées que sur des commandes factices locales ; aucun relais réel.
- Le brouillon 10 n'a été lu qu'au travers de CL20 et de la consigne (non gelé ; R7 : aucun chiffre du brouillon n'est repris ici
  hors S17 = 50 USD et l'arrêt d'étape à 45, qui restent des valeurs de configuration).
