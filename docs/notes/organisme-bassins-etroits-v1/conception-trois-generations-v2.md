# Conception — l'atelier d'idées sur les bassins étroits et profonds, trois générations — v2

Écrite par le préparateur (Claude Opus 5.5), sous-agent de la session mère, le 13 novembre 2026 (reprise à 13:57 UTC, heure
relevée par `date -u`), sur la consigne de corrections `consigne-preparateur-organisme-bassins-etroits-corrections-v1.md`
(`e9bef586…`) et la contre-lecture `contre-lecture-lanceur-bassins-etroits-v1.md` (`3aaf9981…`). **Remplace la v1**
(`conception-trois-generations-v1.md`, `4c90a3a5…`, gardée, R12). Ligne : **GO-2026-11-13-03** (60 USD ; par course 12 + 8 ;
échéance 2026-11-30). Rôle : **atelier d'idées** (N-065, rôle 2) — fiches = matériau, jamais preuve ; usage décisif = R1.
Citations obligatoires (N-064) : POPPER (Huang et al., ICML 2025), Dwork et al. (arXiv 1506.02629), Blum et Hardt « The
Ladder » (arXiv 1502.04585), Co-Scientist (Nature 655, p. 487-496).

Pièces : question `question-organisme-bassins-etroits-v1.md` (`c188fa9a…`, inchangée), témoins `temoins-bassins-etroits-v2.json`
(`f1ddcef9…`), devis `devis-organisme-bassins-etroits-v2.md`, rapport `rapport-preparateur-v2.md`, lanceur
`scripts/lancer_course_ideation_bassins_etroits_v2.py` et ses essais.

## 1. Trois courses enchaînées, sans changer l'orchestrateur

- **Orchestrateur** : clone en lecture `/home/user/lciric/ideation-organism`, commit `be6b5af9…` ; les neuf fichiers de la
  chaîne de lancement ont les empreintes du lanceur v3 ; course à fiches (sans `--course-2`), comme le 8 novembre. Rien n'y
  est modifié ni importé par le lanceur.
- **Une génération = course, lecture, bras.** (1) **Course** : proposeurs en deux passes, juge Opus, consigne du juge Argon
  mise en attente scellée. (2) **Lecture** par **la mère** (Lazar peut s'y substituer, § 6) de toutes les fiches validées,
  relecture « aucune recette » (R-607), puis attestation scellée. (3) **Bras** : le juge Argon note, l'orchestrateur écrit le
  classement agrégé.
- **Commande**, seule et exacte : `/usr/local/bin/python3 -I -B scripts/lancer_course_ideation_bassins_etroits_v2.py G`,
  G ∈ {1, 2, 3}. **Lancement détaché (M7)** : le lanceur démarre un superviseur dans une session de processus neuve (sorties
  vers des fichiers, PID et heure de départ du processus au manifeste de départ scellé), qui lance l'orchestrateur, relaie
  SIGTERM, SIGINT et SIGHUP **par PID** et scelle le code de sortie ; le lanceur rend la main. La **même** commande, relancée :
  un superviseur vivant → rien, compte rendu (code 3) ; fini → manifeste de fin scellé (code 0) ; mort sans code scellé →
  manifeste de fin « mort sans fin propre », dépense comptée au plafond, génération verrouillée. Rien ne part tant qu'un
  superviseur de ce lanceur vit. Arrêt : `kill -TERM <PID du superviseur>` (R10). La durée de vie de l'outil qui lance ne
  borne plus la course.
- **Relances** (R3) : une génération jouée n'est jamais rejouée ; une course n'est relancée que si chaque tentative
  précédente a fini proprement **et** que sa dépense relevée est au plus 10⁻⁵ USD (refus « rien envoyé » de la commande
  d'Argon, coût plancher 10⁻⁶, prouvé par le relevé ; M2) ; trois tentatives au plus. Un bras n'est relancé que si chaque
  bras précédent a fini proprement en « non joué, rien envoyé » (trace de l'orchestrateur) ; jamais après un bras joué,
  payé ou refusé pour taille (M3) ; trois au plus.

## 2. Ce que chaque génération reçoit

| | Proposeurs (`--piece`) | Juges (`--piece-juge`) |
|---|---|---|
| Toutes | la question (la même) ; `faits-v1.md` (`d19b5400…`) | `faits-v1.md` |
| Génération 1 | le **recoupement des méthodes** (mère) | le même |
| Générations 2 et 3 | les **fiches reçues** de la génération précédente (§ 3) | les mêmes |

- **Recoupement (M8)** : `docs/notes/organisme-bassins-etroits-v1/recoupement-methodes-v1.md`, scellé, UTF-8, non vide, au
  plus 40 000 caractères, **et** l'attestation scellée de sa relecture par la mère,
  `attestations/attestation-relecture-recoupement-v1.json` : `{"lecteur", "lu_le", "recoupement_sha256",
  "niveau_methode_aucune_recette_aucun_secret": true, "temoin_vrai_absent": true}` ; les deux empreintes entrent au manifeste
  de départ. Le recoupement n'est pas épinglé dans le lanceur (il n'existe pas encore) : c'est l'attestation qui l'arrête.
- **Tailles** : contrôle d'Argon ≈ 322 800 caractères (génération 1) et ≈ 332 900 (pièce de 50 000) contre une garde de
  400 000 ; plancher de la commande d'Argon à 3 caractères par jeton 1,45 et 1,48 USD, sous le contrôle externe relevé à
  **1,7** (M2) ; le lanceur remesure par l'orchestrateur (sans appel) et garde à 3 caractères par jeton.

## 3. Règle de passage, écrite d'avance (M4)

Appliquée par programme (`choisir_fiches_recues`) sur les seuls fichiers scellés de la génération g − 1 : `classement.json`,
`fiches-validees.json`, `noyau/cles-anonymisation-par-juge.json`, `doublons-par-juge.json`, `doublons-bras-rapporte.json`.
**Aucune mesure de l'orchestrateur** (ni mesures de convergence, ni appariement des passes, que l'orchestrateur dit « jamais
pour une sélection ») n'y entre.

1. **Source** : le classement agrégé du bras, seulement s'il est lisible (témoins tenus chez chaque juge). Sinon : aucune fiche
   transmise, génération suivante refusée, nœud.
2. **Ordre** : le rang de l'orchestrateur (éligibles ; total ; max(avantage, originalité) ; robustesse ; empreinte).
   Témoins et inéligibles exclus.
3. **Prise** : dans cet ordre, une fiche est sautée si **un juge l'a signalée explicitement en doublon** d'une fiche déjà prise
   (union des signalements des deux juges, sans fermeture transitive : A~B chez l'un et B~C chez l'autre laissent passer A et
   C si B n'est pas pris) ; ou si la **pièce entière** dépasserait 50 000 caractères (on passe à la suivante). Une fiche de
   passe 2 n'est **jamais** sautée pour le seul fait d'être la version d'une fiche de passe 1 déjà prise. Arrêt à cinq.
4. **Service** : ordre des empreintes ; étiquettes `G<g>-R1`…`R5` ; la tête de la pièce dit que le numéro n'est pas un rang, et
   qu'une mention « raffine G…-R… » dans une fiche reçue renvoie à une génération que le lecteur ne voit pas ; ni note, ni
   rang, ni auteur, ni passe. Sélection détaillée (identifiants, rangs, fiches sautées, motifs) au manifeste de départ.
5. **Toute donnée manquante ou mal formée arrête** (code 2, motif) : juge sans fichier de doublons, étiquette inconnue, ligne
   sans rang, fiche classée absente, aucune fiche prise.
6. **Confirmation (M5)** : générations 2 et 3 refusées tant que `attestations/confirmation-regle-de-passage-v1.md` (mot de
   Lazar recopié par la mère, scellé) n'existe pas. La génération 1 n'en dépend pas. Ce que cette confirmation couvre, dit
   par la contre-lecture et repris ici : la sélection est une fonction des notes des juges de l'atelier, même si aucune note
   n'est servie ; le texte de tête dit aux proposeurs et aux juges suivants que ces fiches viennent d'un tournoi ; ces trois
   courses ne servent ni le rôle 1 (juges sous attaque) ni une revendication sur l'effet des générations.

## 4. Proposeurs et juges

Proposeurs Opus 5.5, Fable 5.1, Argon (deux passes, six fiches au plus par passe) ; juge Opus 5.5 ; juge Argon différé. Le
code permet Fable 5.1, pas 5.2 (`MODELES_REELS_PERMIS`) ; il impose Argon à la fois proposeur et juge externe : **aucun juge
n'est d'une lignée absente des proposeurs**. Le bras est armé avec `--moteur claude-sdk --confirmer-moteur-reel` (m6) pour
que les vérifications du modèle servi par la commande d'Argon agissent ; accepté par l'analyseur réel (essai sans appel).
Graine 2026111300 + g. Plafonds : proposeurs 2,0 ; juge Opus 1,5 ; Argon passe 1 1,3, passe 2 1,9, contrôle externe 1,7 ;
juge Argon 2,5, contrôle court 0,6. Somme Claude 9,9 ≤ 12 ; somme externe transmise 7,6 < 8 ; pire cas externe avec bras
8,0 ≤ 8.

## 5. Témoins (`temoins-bassins-etroits-v2.json`, `f1ddcef9…`)

| Classe | Témoin | Attendu |
|---|---|---|
| vrai | « Estimateur de Chao des bassins non vus, validé contre l'oracle du monde planté » : la borne f1² / (2 f2) des groupes de doublons sous-estime-t-elle les composantes non couvertes quand une composante est étroite ? | éligible |
| jumeau | la même idée réécrite (« Combien de bassins reste-t-il ? ») | éligible, doublon du vrai |
| faux falsifiabilité | « Indice d'élégance profonde noté par les proposeurs eux-mêmes » (repris de la v1) | inéligible, falsifiabilité ≤ 1 |
| faux antériorité | « Montée de la température d'échantillonnage » présentée comme inédite (repris de la v1) | inéligible, originalité ≤ 1 |

Chargés sans erreur par le chargeur réel de l'orchestrateur (sans appel). **Règle du témoin vrai (M9)** : il ne doit pas
pouvoir être jugé « occupé » à bon droit par une pièce servie aux juges. Le témoin de la v1 (courbe nulle 1 − (1 − r)^n à coût
égal) était presque énoncé par la question elle-même ; celui de la v2 vient d'un autre domaine (estimation du nombre d'espèces
non vues) et n'est ni dans la question ni dans les faits. Pour les pièces variables, la mère le certifie : champ
`temoin_vrai_absent` de l'attestation de relecture du recoupement (génération 1) ; champ
`temoin_vrai_absent_des_fiches_validees` de l'attestation de lecture de la génération g − 1 (générations 2 et 3, puisque les
fiches reçues en sont un sous-ensemble). Faux ou absent : génération refusée, témoins à changer (version neuve), nœud.
**Réserve** : les témoins sont écrits par Claude Opus 5.5, modèle d'un proposeur et du juge `opus-juge` ; « tiers » vaut pour
l'instance, pas pour le modèle. Les témoins faux restent faciles (ils écartent des fautes grossières, non des juges médiocres) ;
les longueurs servies (≈ 1 400 à 3 400 caractères) les distinguent des fiches réelles ; aucun n'éprouve l'auto-préférence.

## 6. Lecture et attestation (M6)

- **Qui** : la mère lit (décision R-2537) ; Lazar peut s'y substituer. Le champ `lecteur` le dit en clair (par exemple « la
  session mère, Claude Opus 5.5 » ou « Lazar »). Conséquence dite : la mère étant un modèle, « lecture humaine » est le nom du
  champ de l'orchestrateur, non un fait ; avec la règle de permission et les attestations de la mère, les six lancements
  peuvent s'enchaîner sans geste humain, sauf la confirmation de la règle de passage (§ 3.6), qui porte un mot de Lazar.
- **Quoi** : `fiches_validees_sha256` (égale à l'empreinte de `fiches-validees.json` de la course) et
  `consignes_en_attente_sha256` (`argon-juge`, égale à celle que la course a scellée) ; plus
  `temoin_vrai_absent_des_fiches_validees` (vrai ou faux).
- **Quand** : `lu_le`.
- **Où** : `attestations/attestation-lecture-humaine-g<g>-v<N>.json`, scellée ; la plus haute version est lue (une attestation
  fautive se remplace par une version neuve, jamais en écrasant). Le manifeste de fin de la course imprime les deux
  empreintes et la liste des champs.

## 7. Mesures d'une génération à l'autre — sans juge de plus

Par programme, après la course, sur fichiers scellés ; jamais servies à un agent, jamais dans la sélection. (1) Part
**déclarée** (`raffine G<g>-R<i>` ou `nouvelle` dans `questions_servies`) ; (2) part **lexicale** (plus petite distance
d'édition sur les mots à une fiche reçue ; « proche » si ≤ 0,6, seuil exploratoire non calibré) ; (3) concordance ; (4)
doublons par juge, éligibles, témoins, couverture Q1 à Q5, coût. **Non mesuré** : la nouveauté de fond. **Limite (M5 iii)** :
l'étiquette `raffine …` est dans un champ lu par les juges, qui reçoivent aussi les fiches reçues comme pièce : la mesure (1)
n'est pas indépendante du jugement. Le programme de ces mesures n'est pas écrit ; à écrire et contre-lire avant la lecture
de la génération 2.

## 8. Limites

- Juges à modèles : matériau. Même lignée entre juges et proposeurs : on ne peut conclure ni sur la valeur relative des
  proposeurs, ni qu'une idée survivante est bonne (seulement que deux familles qui la proposent et la jugent la préfèrent), ni
  que des témoins tenus valident les juges au-delà des fautes grossières, ni sur l'effet des générations (aucun bras témoin).
- La règle de passage pousse au raffinement des bassins déjà classés : c'est ce que les mesures du § 7 décrivent, sans le
  prouver.
- **Garde lexicale « niveau méthode »** de l'orchestrateur (faite pour le pilier attaque) : des mots ordinaires d'une fiche
  de mathématiques (« injection », « exploiter », « étape 1 : », « pour éviter … juge ») mettent une fiche en quarantaine
  (contre-lecture, m9 : 7 phrases d'essai sur 10). À compter par motif après la course et à lire par la mère.
- Aucun accès au Web ; antériorités RAPPORTE ou SUPPOSE seulement.
- Dix des treize modules `pole` chargés ne sont tenus que par le commit `be6b5af9`, non comparé au commit du v3 hors des neuf
  fichiers (commit absent du clone peu profond).

## 9. Options laissées à la mère ou à Lazar

(a) Telle quelle (recommandée, confiance 0,65) ; (b) troisième juge Fable 5.1 (médiane ; plus robuste, plus fragile aux
témoins ; + 1,5 USD de plafond Claude par génération, somme 11,4 ≤ 12).
