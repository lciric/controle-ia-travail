# Rapport du préparateur — commande du compte 3, phase A (v2) puis phase C (v2, v3) — v2

- **Rédacteur** : le préparateur de la v1, sous-agent de la session mère `session_01QPDgKgACWyCkCN8HjqwNXy` (modèle A) ; ni lecteur
  ni juge d'aucun verdict ; aucune sortie de 7a, 7b ou T0.7 ouverte (noms, tailles, empreintes et champs `fichier`, `octets`,
  `sha256` du manifeste des morceaux seulement) ; aucune machine, aucune dépense, aucun commit. Heures (`date -u`) : début de la
  version 2 2026-11-14T12:07:52Z ; fin en dernière ligne.
- **Demande** : commande v2 en deux temps (phase A d'abord, remettable seule ; puis phase C, dont CL3-07), réponse à Q11, décisions de
  Lazar R-2741 et R-2740 portées ; sceller, ne pas committer.

## Verdict

1. **Phase A remettable seule** : `commande-compte-3-phase-a-v2.md` (`25635d99…`), répétée de bout en bout sur dépôts jouets,
   **21 conformes sur 21** (artefacts X1 à X5 compris), après les préalables de la mère (§ 0.2 de la commande).
2. **Phase C : remettre la v3** `commande-compte-3-phase-c-v3.md` (`9d788919…`), répétée de bout en bout, **53 conformes sur 53**
   (tous les blocs, bloc M compris ; appel interrompu, poussées refusées puis reprises, code 2, artefacts de chaque garde ajoutée par
   la contre-lecture). La v2 (`fee4caaa…`, 44 sur 44) reste (R12) ; dans ses blocs, la v3 ne change que C5 et le nom de la commande
   au bloc 0b-C ; sa répétition ajoute neuf artefacts.
3. **Contrôle à blanc v2 sur l'état actuel des registres**, code pris à C7 comme au bloc C1 : **aucun refus, 12 manques**, tous
   attendus avant les préalables (audit, pièce « mots et coût », données à placer, plan de B bis).

## Erreurs, écarts, constats (une ligne chacun)

- **Erreur de méthode, corrigée** : j'ai scellé la phase C v2 et sa répétition, puis modifié les deux fichiers ; ils sont rendus à leur
  texte scellé (sceaux conformes, vérifiés), et les changements portés sous un nom neuf, la v3 (R12 ; le module de scellement refuse
  d'écraser, je ne l'ai pas contourné).
- **Défauts trouvés par la répétition de la phase C, corrigés avant le sceau de la v2** : C4b rendait le code 1 après succès (dernière
  ligne `[ -e … ] && echo`) ; F-C n'était pas relançable (nouveau nom de journal à chaque relance) et son contrôle final était muet ;
  le bloc M continuait après un échec d'extraction. Défaut du jouet : le `.gitignore` réel (`donnees/`) privait le main jouet du jeu
  scellé `dissimulation-v2.jsonl` (premier passage : 24 sur 39), corrigé par `git add -f` comme au dépôt réel (R-352).
- **Défaut trouvé en écrivant les artefacts (porté en v3)** : en v2, C5 écrivait le bordereau avant le filtre de noms ; une faute de nom
  laissait un bordereau écrit, qui bloquait la relance, et une pièce d'un essai manqué restait dans `pieces/`.
- **La phase A (scellée) nomme `commande-compte-3-phase-c-v2.md`** comme commande à part : la v3 la remplace ; Lazar donne le chemin et
  l'empreinte de la v3 à la remise (le bloc 0b-C les vérifie). Noms du bac inchangés de la v2 à la v3, à dessein (aucun second appel).
- **`CODE-T07` refuse depuis la copie de travail de la mère** : un paquet non suivi sous `src/controle_ia/` y est apparu entre 11:29 et
  12:55 ; un contrôle à blanc lancé avec `PYTHONPATH=src` refuse donc. La phase C prend le code d'une arborescence détachée à C7 et n'est
  pas touchée ; jamais l'étape B ni le contrôle à blanc depuis la copie de travail de `main`. Ma sortie qui nommait ce paquet est effacée
  (cloisonnement) et remplacée par la passe faite avec le code de C7.
- **Disque de ce conteneur presque plein** (97 à 98 % à 13:07, 1,1 à 1,4 Gio libres) : mes dossiers de travail finis sont effacés ; les
  plus gros dossiers restants du bloc-notes ne sont pas les miens (je n'y ai pas touché).
- **Erratum de `prealables-v1.md`** (CL3-16) : R-2704 dit « embargo de P3-bis levé » et non « plus sous embargo » ; la règle appliquée
  ne change pas.

## Traitement de chaque constat de la contre-lecture (`contre-lecture-commande-compte-3-v1.md`, `092acef6…`)

| constat | traitement | où | éprouvé par |
|---|---|---|---|
| CL3-01 majeur | le verdict A reste sur `verdict/t06-table-a-7b-compte-3-v1` et n'entre dans `main` qu'après la ligne `CODE-MOTS-ET-COUT-T06` (décision de la mère, R-2735) ; journal provisoire limité aux lignes STATUT, FICHIERS, DÉCLARATIONS, MESSAGE | phase A § 0.1, § 2, § 15 ; bloc F-A (P3A-003, P3A-005) | répétition A : « aucune ligne ISSUE », main inchangé |
| CL3-02 majeur | exclusion de l'hôte étendue : NARCBench (rédaction, contre-lecture, course), brouillons des papiers B et C, code de la pièce « mots et coût », aucune tâche du lot ; en phase C, cellule `CELLULE_HOTE` exigée telle quelle par l'attestation v3 ; plus l'analyse du verdict B et tout rôle de lecteur de B bis | phase A § 1, F-A (P3A-004) ; phase C § 1, 1C, 2C, F-C (P3C-005) | essai v3 17/17 ; répétition C v3 : cellule autre → 2C arrête |
| CL3-03 majeur | aucune ligne du registre des décisions chez le lecteur A (R-2704 retirée) ; filtre de contenu sur chaque extrait (A3) ; phase C : ligne `<<R_BA_L2>>` dédiée exigée (C0 : présente, sans mot de B bis, nomme BA-L2), filtre de contenu de l'extrait et filtre de noms (C5) | phase A A3 ; phase C C0, C5 | répétition A : X3 ; répétition C v3 : trois artefacts de C0, nom interdit et contenu de B bis en C5 ; registre réel : 0 ligne touchée ce jour |
| CL3-04 majeur | C4 scindé : C4a (marqueur posé avant l'appel, refus s'il existe), C4-attente (`kill -0` seul), C4b (commits gardés par marqueurs, poussée, relançable seul) ; F-C rendu relançable de même | phase C § 4, § 8, F-C | C4a relancé → arrêt ; poussée refusée → C4b puis F-C reprennent à la poussée ; toujours quatre commits |
| CL3-05 majeur | durée mesurée (1,6 à 2,1 s par comparaison au plancher ; 0,6 à 2,2 min pour l'étape B) ; appel détaché (`setsid nohup`) ; borne 60 min → nœud, jamais d'arrêt du processus | phase C § 0.3, C4a, C4-attente | `mesure-duree-etape-b-sortie-v1.txt` ; répétition : « en cours » puis « finie » |
| CL3-06 majeur | section 9 du contrôle à blanc v2 : la garde `lecture_v4.ouvrir` du module sur une copie du registre, puis lectures de structure (issue « mots et coût », épisodes, colonnes des mesures), sans rien afficher ; la mère accepte cette lecture par programme en remettant (§ 0.4) | contrôle à blanc v2 ; bloc C3 (`--chaine`) | essai v2 19/19 (V3 à V11 : refus du module), non-régression 28/28 ; répétition : « AUTORISÉE » |
| CL3-07 bloquant | répétitions de bout en bout archivées et scellées : phase A (tous ses blocs, X1 à X5) ; phase C v3 (tous les blocs et le bloc M, avec un module jouet qui joue la vraie garde et la vraie écriture du résultat) | `repetition_phase_a_jouet_v2.sh` ; `repetition_phase_c_jouet_v3.sh` | 21/21 ; 53/53 |
| CL3-08 mineur | C1 approfondit un clone peu profond (`--unshallow`, refspec explicite) avant de chercher C7 | phase C C1 | non exercé (clone jouet complet) : réserve |
| CL3-09 mineur | C1a à part, relançable ; versions exactes exigées de tout interpréteur ; 9 Gio libres exigés avant installation | phase C C1a | « versions : 2.4.6 1.17.1 2.14.1 » ; installation non exercée : réserve |
| CL3-10 mineur | `place` admet un fichier présent, suivi ou non, s'il est égal au blob ; scores admis s'ils égalent `SCORES-T07` ; recomposition relançable | phase C C2 | C2 relancé : « déjà là, égal », « scores déjà recomposés » |
| CL3-11 mineur | marqueur retiré ; lecteur du modèle C ; à défaut, arrêt et nœud de Lazar, aucun repli sur le modèle A | phase A § 0.3, § 2 ; phase C § 2, C6 | texte |
| CL3-12 mineur | traces réconciliées : 9 + 2 fichiers listés par les deux `empreintes.sha256` = les « 11 traces » de R-2413 ; A2 exige les noms exacts et 11 fichiers à leur empreinte | phase A A2 | répétition A : « 11 traces » |
| CL3-13 mineur | un seul agent lit et prononce (Lazar, R-2741, N-B (a)), écrit | phase A § 2 | texte |
| CL3-14 mineur | essai du contrôle à blanc complété : `arret-etape-b.json` présent, `arret.json` de T0.6 présent, ouverture `pleine-anticipee`, empreinte de ligne autre que le fichier, `CODE-T07` sur une copie jetable modifiée puis saine | essai v2 | C1 à C6 de l'essai v2 |
| CL3-15 mineur | toute sortie d'essai, de répétition et de mesure versée et scellée | dossier | sceaux |
| CL3-16 mineur | attestation par identifiant de session et par ses 12 premiers caractères ; ligne du lot par identifiant ; contrôle de nouveauté (aucune branche `lot/compte-3-v1`, aucun `registres-provisoires/compte-3-*`) ; v3 : ligne de l'hôte admise à sa seule cellule ; citation de R-2704 corrigée ici | phase A bloc 2 ; phase C 2C | essais v2 12/12 et v3 17/17 ; répétition A : X1 |
| CL3-17 mineur | blocs 0b et 0b-C : récupération de `main` par refspec et avance rapide avant toute lecture ; tout poussé sur `main` avant l'ouverture de la session | phase A 0b, § 0.2 ; phase C 0b-C | répétitions |
| CL3-18 mineur | motif exact des noms du verdict, sans archive | phase A A5 ; phase C C7 | répétition A : X5 ; répétition C v3 : archive → arrêt |
| CL3-19 mineur | C7 joué, S7 déclaré (mêmes `src/` et `tests/`, P9) ; la mère garde avec `lecture-t07.json` le chemin et l'empreinte du manifeste de T0.7 de `donnees/t07-etape-a-v1` | phase C § 0.1, § 0.3, § 15 (3) | texte |
| CL3-20 mineur | chemin du plan de B bis imprimé seulement en cas d'écart ; C4-attente n'imprime que des noms et des nombres de lignes, jamais la fin du journal | contrôle à blanc v2, section 8 ; phase C C4-attente | essai v2 : V1b |
| CL3-21 mineur | le lecteur recopie le message reçu dans son espace fermé ; l'hôte le compare au message scellé avant tout commit ; sinon arrêt et nœud | phase A A4, A5 ; phase C C6, C7 | répétition A : X4 ; répétition C v3 : message autre → arrêt |

## Q11

Oui, sous conditions, et elles sont écrites : l'hôte est **une session neuve, distincte de toute session du lot** du compte 3, qui
n'exécute aucune tâche du lot ; son exclusion (analyse du verdict A, étape B bis, T0.8, G0, préenregistrement NARCBench, brouillons
des papiers B et C, code de la pièce « mots et coût ») est écrite dans la commande (phase A § 1), dans son journal (P3A-004) et, pour la
phase C, dans la liste « qui a lu quoi » v3 (cellule `CELLULE_HOTE`, exigée telle quelle). Contrôles : attestation par identifiant et
préfixe, contrôle de nouveauté, ligne de l'hôte admise à sa seule cellule.

## Décisions de Lazar portées

- R-2741 : N-A (a) pas d'extracteur ; N-B (a) un seul agent pour la table A ; N-C bloc M (ci-dessous) ; N-D le lot NARCBench continue en
  parallèle sans rien ouvrir de T0.7, 7a ou 7b avant les verdicts ; N-E aucune attente de la grille de G0.
- R-2740 : même hôte, lecteurs distincts (aucun lecteur de B bis pour l'étape B ; rien de cette branche dans un espace de B bis avant le
  verdict de B bis) ; GO-2026-11-14-09 (40 USD) hors de la phase C, qui ne dépense rien ; plan de B bis scellé avant toute lecture de
  l'étape B : ligne `SCELLEMENT-PLAN-BBIS` exigée au bloc C0 et par la section 8 du contrôle à blanc, strictement avant l'appel, dans un
  registre propre (`registres/etape-b-bis-v1.md`, proposition : le lecteur de registre de T0.7 refuse toute clé inconnue).

## Bloc M (N-C) et ordre de la remise

- `lecture_etat_ba_l2_mere_v1.py` (`6d63e9d6…`, essai 10/10) n'affiche que « ÉTAT BA-L2 : ne s'applique pas » (code 0), « … s'applique »
  (code 3 : mot de Lazar avant l'étape B) ou « … illisible » (code 2) ; il vérifie la ligne `LECTURE-T08-BASE-A`, l'empreinte et le
  compagnon du fichier, et ne lit que `lignes.BA-L2.s_applique`. Le bloc M (phase C, § 15) le lance sur ce seul fichier, extrait de la
  branche de la pièce dans un dossier jetable ; il s'arrête si la ligne manque ou si la branche est absente (répété).
- Ordre : (1) audit des fuites, ligne `AUDIT-FUITES-T07` ; (2) code de la pièce, ligne `CODE-MOTS-ET-COUT-T06` (alors seulement le
  verdict A peut entrer dans `main`) ; (3) course de la pièce, lignes `LECTURE-T08-BASE-A` puis `ISSUE-MOTS-ET-COUT-T06` ; (4) **bloc M**,
  puis la ligne dédiée `<<R_BA_L2>>` du registre des décisions ; (5) plan de B bis scellé ; (6) consigne du lecteur B, liste v3, marqueurs ;
  (7) remise de la phase C v3.

## Réserves

- Le calcul de l'étape B n'est pas rejoué sur des données valides (mesuré à part) ; le module jouet joue la vraie garde et la vraie écriture.
- Voies du module qui exigent d'ouvrir les scores (index des sondes dans les scores, nombre de directions) : non éprouvées avant l'appel,
  par construction ; un code 3 y reste possible.
- Approfondissement du clone (C1) et installation de l'environnement (C1a) : non exercés par la répétition.
- Format de la pièce : `base-a-t08.json` doit porter `lignes.BA-L2.s_applique` (booléen), sinon `--cle-json` ; à fixer dans la consigne
  du développeur de la pièce.
- À écrire par la mère : consignes des lecteurs A et B (format fermé, noms permis sans archive, fichier du message reçu, aucun nombre hors
  des fichiers scellés), listes « qui a lu quoi » v2 et v3, lignes R de N-B et de CL3-01.
- Transport local dans les répétitions (`file://`), non GitHub.

## Pièces (dossier `docs/procedures/lecture-7b-etape-b-compte-3-v1/`, toutes scellées)

| pièce | empreinte |
|---|---|
| `commande-compte-3-phase-a-v2.md` | `25635d99acd1f1f73b466b185daa21339ae65e0424a6c9ea56e0270563f02c3f` |
| `attestation_qui_a_lu_quoi_compte_3_v2.py` ; essai ; sortie (12/12) | `be9dc21357eba7a736a0466adc5835e5ef68a48466b71f860fc3ff7cf6744047` ; `22b76f4fe3807b4e1aea1f3006f62e3226f32becf3b11a505025b9c6791f502f` ; `b2e14b4ac450ad4956b14c9cf5e11e7294342bdb19521feb4535f3cac55686f5` |
| `repetition_phase_a_jouet_v2.sh` ; sortie (21/21) | `ebdd22491cd158b8057e8c4b37fa5b26e3edd8d9df04074f0848111ffdcfcd11` ; `968b99705b7559d0cb6f6aba7cfcb9236c5b6d3e3b03f2e6f30ad33e54b85ad3` |
| `commande-compte-3-phase-c-v3.md` (à remettre) | `9d7889198238c171447a06f56f1a37beb4190572c3a9ceceb18144541c258d2e` |
| `repetition_phase_c_jouet_v3.sh` ; sortie (53/53) | `8be57168fe40b27ad7ac2bd0c1e3908733c316b53e00a2bab883653c67a081ee` ; `d9ee7f84e977ef7d56acdb94f4d8e7ba3c759edfdae2e9ed7b83cd57c6da7478` |
| `commande-compte-3-phase-c-v2.md` (gardée) | `fee4caaa2f9fcca99201f5bf5ea9a94a84af4053397baec543e5eaa2f36d9d5c` |
| `repetition_phase_c_jouet_v2.sh` ; sortie (44/44) | `7a9da18097ae415e2e5b9afb81e5d215308419ff0f95e99531e77cdbec1ee841` ; `7f01ef2c1746dc3b2053691448a7139b0167ea85de85e73ceb975a9ca2d2e3ac` |
| `etape_b_jouet_v1.py` (module jouet, répétitions seulement) | `4043655b42d4fc058e849c6825967fec078ad70ef93e304c24ed8bd212f5ead0` |
| `controle_a_blanc_etape_b_compte_3_v2.py` | `21310d805b0578f658e26cf1792c2072fe1b1c71c9de205f565e2e056a638795` |
| essai du contrôle à blanc v2 ; sortie (19/19) ; essai v1 rejoué sur le v2 (28/28) | `b53560a5f47922266e9dff8a9982abc488d826d51d69e0d8419e8e9592f4350b` ; `495d1f9dc4c7bc2d8052b52df9e7726d8d6c3da40b43919a1a05e4c9a6090292` ; `ad8d7c0ca9404d09cae26fdaa813b4726ee47542631ee2cc8ba75e5e687a2013` |
| `controle-a-blanc-v2-etat-actuel-sortie-v1.txt` (0 refus, 12 manques) | `a837459f7341b4a49440d56adb57a67e05a76a0876c04b516b4b8da7611f2043` |
| `attestation_qui_a_lu_quoi_compte_3_v3.py` ; essai ; sortie (17/17) | `a20f137c92022c58fd8090a2c1e25d8c575fec1b0e8a15d2190a1b1bae505a62` ; `22375890bc37e4d908e494cf6185c720e7a5dfb50feaec2914bb84cde43132c6` ; `6d02b64047871ef4446d6a3f5a96feec3b4de09631b4cb516c79efc7ff59fd6c` |
| `lecture_etat_ba_l2_mere_v1.py` ; essai ; sortie (10/10) | `6d63e9d6e7036310597a7a19711e431910278cf07b48132a376edcf147cf44d0` ; `21fc789cced9512cdb6ccc2b1c170b080c3e246be6b224a1ad41741fda6b1121` ; `51261a83cc42c5a5d97c63e4050932264ac618473c9d1a3f21bf8d6bcc00d033` |
| `mesure_duree_etape_b_v1.py` ; sortie | `2f300ecf8326b1aad6862beacc75c93e8ae9a6f693b398ecc0ee4a5d96196368` ; `e77e06f18c5b6006d0e7c965fedb93de5b0739bc334d08ad95bc8035894496c6` |

Fin : 2026-11-14T13:09:02Z (`date -u`).
