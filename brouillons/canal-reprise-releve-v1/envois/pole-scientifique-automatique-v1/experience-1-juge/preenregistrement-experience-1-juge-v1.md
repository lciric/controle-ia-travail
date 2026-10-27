# Préenregistrement — expérience 1 du pôle : le juge v1 contre la dérive non modélisée — v1

- Auteur : lignée conv-audit (instance du 27 octobre 2026, autre compte ; Claude Opus 5.5).
- Date (UTC) : 2026-10-27, écrit à partir de 07:42 (heure lue sur `date -u`).
- Commit du code d'analyse : le commit de `canal/conv-audit-n04` qui porte ce texte et le dossier
  `envois/pole-scientifique-automatique-v1/orchestrateur-pole-v2/` (session-depot le relit et le consigne au scellement) ;
  le code est identifié fichier par fichier par `orchestrateur-pole-v2/EMPREINTES-orchestrateur-pole-v2-v1.txt`, dont
  l'empreinte est donnée au message n° 103 ; le manifeste de l'exécution consigne l'empreinte de chaque module de `pole/`.
- Documents qui font foi (chemin + empreinte) : note de conception du juge
  `experience-1-juge/conception-experience-1-juge-v1.md`
  (`560f4a4cd985f28f2a9fcb838644c2dab62c81d983a5d255e4fe84eb07f1a217`) ; conception du pôle
  `conception-pole-scientifique-v1.md` (`a4f94148c9c55b76f208edecd7220b51a8e21ca69f52e50c7f2abb6484b81b52`) ;
  LISEZMOI de v0 `orchestrateur-v0/LISEZMOI-orchestrateur-v1.md`
  (`39101ffb8e4404fc7a5dafea4f4d80ad841e9c87a4c359323bf103c6f97db481`) et ses chiffres
  `demo/experience-critere-v1/controles-fatals-v1.json` (`2b86b37f504ddc5028b97a8dc9d55fde55e514be3d8565f1f15160291d871173`,
  dans `orchestrateur-v0-demo-v1.zip`) ; LISEZMOI de v2 `orchestrateur-pole-v2/LISEZMOI-orchestrateur-pole-v2-v1.md`.
- Chemins relatifs à `brouillons/canal-reprise-releve-v1/envois/pole-scientifique-automatique-v1/`.

## Hypothèse

Instrument du pôle « scientifique automatique » (priorité de Lazar depuis le 26 octobre) ; aucune hypothèse numérotée du
programme n'est en jeu. Voie (c) : simulation à vérité connue, sur processeur, aucune activation, aucune dépense.

Le **juge v1** = juge v0 + ordre d'exécution secret (permutation tirée par le noyau après le gel ; issues rangées par
indice du plan ; évaluation dans l'ordre du plan) + membre « urne » (maximum sur les lois échangeables, Π_k c_k(t)!/t!)
dans la bibliothèque nulle 𝓛 ; les autres membres et le critère des filles (nul augmenté des parents, marge 2δ₀) sont
ceux de v0, inchangés. H-J1 a deux parties :

- **(a) Socle** — pour une fiche sans parents, sous tout monde où les issues sont indépendantes des traits, quelle que
  soit leur structure temporelle, le juge v1 promeut une loi aveugle, même une loi qui connaît la dérive (« calendrier »)
  ou la composition exacte des issues (« composition »), avec une probabilité d'au plus α = 0,05 ; il garde les
  contrôles de v0 (T1a, T6, T3 à composante nette fausse) et sa puissance sur un effet net fort (T3, ε = 0,2).
- **(b) Critère des filles** — le nul augmenté de v0 rejette (taux ≤ α) les filles sans contenu nouveau sur les traits :
  les sept tricheurs de v0, la concaténation de T9, le parent plus la connaissance de la dérive (T1b-fille), le parent
  mélangé à une loi aveugle fixe (tricheur ajouté, voir plus bas) ; il promeut une fille réellement neuve (puissance ≥ 0,90).

Hypothèses de travail : K = 3 issues, traits de dimension 2, deux sous-populations, 200 tirages frais par répétition
(250 instances dont 50 de calibrage pour les filles), α = 0,05, lecture continue (promotion dès que W_t ≥ 1/α ; inégalité
de Ville), δ₀ = 0,01 nat par tirage. Les six structures de la batterie T1b, toutes absentes de 𝓛 : dérive linéaire (celle
de v0), rupture à n/2, sinusoïde de période n/3, marche aléatoire des logits (écart 0,15 par pas), calendrier
déterministe par blocs de 20, monde auto-excité (moyenne glissante de fenêtre 10, lissage 0,1 ; 𝓛 n'a que le lissage
0,5). Détail exact de chaque monde, loi et juge : `pole/controles_pari_v1.py` (empreinte dans le fichier d'empreintes).

**Ce qui a été vu avant d'écrire ce texte** (graine 777, refusée par le code pour l'expérience ; déclaré, R-473) :
deux essais de fumée de 20 répétitions de toutes les lignes, et une exploration de 200 répétitions sur deux lignes de
filles. Chiffres : `orchestrateur-pole-v2/LISEZMOI-orchestrateur-pole-v2-v1.md`, section « Essais de fumée et
exploration ». En bref : socle 0/20 sur ses 18 contrôles fatals ; T1b-fille 3/20, puis 29/200 (uniquement quand la
moyenne de la dérive est loin de l'uniforme) ; « parent + loi aveugle fixe », sans dérive : 58/200 sous v0, 63/200 sous
v1 ; pari couvert ε = 0,05 : 2/20 sous v1 contre 20/20 sous v0. **Changements faits après l'essai 1, et pourquoi** :
ajout du tricheur « parent et loi aveugle » (pour montrer que le trou du critère des filles ne tient ni à la dérive ni à
l'ordre secret) ; lecture en deux parties, socle et filles (le socle sert seul à la génération 0, qui n'a pas de
parents) ; refus de la graine 777. Aucun seuil, aucun monde, aucune loi des lignes existantes n'a été changé.

## Prédiction chiffrée et signe attendu

Taux de promotion par ligne (1 000 répétitions), juge v1 sauf mention ; confiance entre parenthèses.

- **Socle, 18 contrôles fatals** : tous ≤ α (0,85) ; chacun ≤ 0,02 (0,8). Les six lignes « composition » valent exactement
  0/1 000 : c'est garanti par construction (log W_t ≤ 0 à tout instant, l'urne dominant la loi sans remise) ; un taux non
  nul y serait un défaut de code. T1a ≤ 0,018 (le taux le plus haut de v0) sur chaque nul (0,8).
- **Critère des filles, 10 contrôles fatals** : T1b-fille > α, attendu 0,10 à 0,20 (0,85) ; « parent et loi aveugle »
  > α, attendu 0,15 à 0,40 (0,85) ; les sept tricheurs de v0 et T9 ≤ α (0,95), à 0 pour T9 et les formes contenues dans
  le nul (par construction).
- **Artefacts requis (doivent être vus, taux > α)** : v0 sous dérive linéaire, oracle « calendrier », 0,55 à 0,80 (v0 :
  0,652) ; v1 sans urne sous calendrier déterministe, loi « composition », ≥ 0,95 (log W final ≈ 5,47 nats, constant) ;
  permutation de l'ordre d'évaluation, ≥ 0,99 ; 𝓛 réduite à l'uniforme ≥ 0,80 (v0 : 0,957) ; dénominateur ajusté à
  part 0,30 à 0,60 (v0 : 0,439) ; en ligne ≥ 0,75 (v0 : 0,903) ; filles sans parents dans le nul : forme 0,35 à 0,70
  (v0 : 0,474), enveloppe 0,45 à 0,80 (v0 : 0,700). Tous vus (0,9).
- **Puissance** : fille neuve ≥ 0,95 (0,9) ; T3 ε = 0,2 ≥ 0,95 (0,9) ; perte sur la fille neuve, v0 − v1, ≤ 0,05 (0,9) ;
  T3 ε = 0,05 : 0,05 à 0,35 sous v1 contre ≥ 0,85 sous v0 (0,7) — coût de l'urne sur les petits effets, rapporté.
- **Issues** : socle « adopté » (0,85) ; critère des filles « non adopté » (0,85), cédant sur T1b-fille et « parent et loi
  aveugle » ; issue globale (règle de la note) « non adopté » (0,85).
- **Ce qui réfuterait mes prédictions** : un contrôle fatal du socle > α (le socle ne tient pas pour cette structure) ;
  T1b-fille et « parent et loi aveugle » ≤ α (le trou vu à l'exploration n'est pas confirmé) ; un artefact non vu.
  Les deux sens se lisent (R3, R4) : un socle adopté ne dit rien des filles, et des filles non adoptées ne disent rien
  contre le socle.

## Métrique

- Par ligne : taux de promotion = promotions / répétitions ; une promotion est W_t ≥ 1/α = 20 à un instant t quelconque
  (lecture continue) — et, pour une fille, gain moyen de score logarithmique sur la meilleure enveloppe ≥ 2δ₀ = 0,02 nat
  par tirage (règle de v0) ; T9 exige en plus log W max ≤ 10⁻⁹ (règle de v0).
- Rapportés sans être décisifs : borne haute unilatérale à 95 % de Wilson ; log W maximal observé ; médiane de log W
  final ; membre dominant du dénominateur au dernier tirage (sous v1, l'urne doit y apparaître).
- Perte de puissance sur la fille neuve = taux(v0) − taux(v1), mêmes graines de scénario.

## Seuil

- α = 0,05. Un contrôle fatal passe si son taux observé est ≤ 0,05 (T9 : et log W max ≤ 10⁻⁹). Un artefact requis est vu
  si son taux est > 0,05. Une puissance décisive passe si son taux est ≥ 0,90 (fille neuve ; T3 ε = 0,2). La note listait
  T3 ε = 0,2 dans la « lecture minimale gelée » de puissance sans la reprendre dans sa règle d'adoption : elle y est reprise.
- Fixés avant toute lecture. Risque d'échec à tort d'une ligne valide (plus de 50 promotions sur 1 000 alors que le
  taux vrai est plus bas ; queue binomiale exacte) : 3·10⁻⁹ pour un taux vrai de 0,02 ; 2,4·10⁻⁴ pour 0,03 ; 0,049 pour
  0,04 ; 0,20 pour 0,045. La théorie (Ville) place les taux vrais du socle bien plus bas.

## Plan d'analyse

- Données : produites par le code, à la graine maîtresse, 1 000 répétitions par ligne, 70 lignes (socle : 18 fatales,
  6 artefacts, 1 puissance décisive, 29 descriptives ; filles : 10 fatales, 2 artefacts, 1 puissance décisive, 3
  descriptives). 1 000 répétitions bornent la largeur de l'intervalle de Wilson à environ ± 0,014 autour de 0,05.
- Graines : graine maîtresse **tirée par session-depot juste après le scellement**, par
  `numpy.random.SeedSequence().entropy` (128 bits), écrite dans un fichier scellé avant toute exécution ; jamais 20261026
  (exploration de v0) ni 777 (essais de fumée) — le code les refuse. Dérivation : `graine_derivee(graine, étiquette,
  répétition[, « frais » | « noyau »])` (SHA-256, bibliothèque standard ; écart à R9 déjà écrit pour v0) ; tirages frais
  et ordre secret dérivent en plus de l'empreinte de chaque engagement. Les étiquettes sont dans le rapport.
- Comparaisons : trois juges (v1 ; v0 ; v1 sans urne) sur les mêmes graines de scénario ; puissance appariée v0 contre
  v1. Aucune correction pour comparaisons multiples : la lecture est conjonctive (un seul contrôle fatal au-dessus de α
  suffit à « non adopté ») ; elle penche donc vers le rejet du juge, jamais vers son adoption.
- Exécution, depuis `orchestrateur-pole-v2/` au commit consigné : `sha256sum -c EMPREINTES-orchestrateur-pole-v2-v1.txt`
  (tout « OK ») ; `$PY -I -B -m unittest` (105 essais, « OK ») ; puis
  `$PY -I -B pole --experience-juge-v1 --graine-maitresse G --sortie DOSSIER_NEUF --horodatage "$(date -u +%Y-%m-%dT%H:%M:%SZ)"`,
  où `$PY` est un Python ≥ 3.11 qui ne voit pas `claude_agent_sdk` (environnement virtuel sans paquets du système).
  Durée attendue : environ 15 minutes sur un cœur.
- Lecture : le rapport `experience-1-juge-v1.md` applique mécaniquement les critères ci-dessous (`juger_v1`) ; un
  sous-agent neuf, ni auteur de ce texte ni de l'analyse, relit le rapport JSON contre ces critères et prononce (R13).

## Critères de lecture gelés

| partie | condition | issue |
|---|---|---|
| socle | un contrôle fatal du socle > α, ou T3 ε = 0,2 < 0,90 | non adopté |
| socle | sinon, un artefact requis du socle non vu | non concluant |
| socle | sinon | adopté — le juge v1 peut servir aux fiches sans parents (génération 0) |
| filles | un contrôle fatal des filles > α, ou fille neuve < 0,90 | non adopté |
| filles | sinon, un artefact requis des filles non vu | non concluant |
| filles | sinon | adopté — le critère des filles peut servir |
| global (règle de la note) | les deux parties « adopté » | adopté pour tout le pôle |
| global | une partie « non adopté » | non adopté (on dit ce qui a cédé) |
| global | sinon | non concluant |

- Un « non adopté » nomme les lignes qui ont cédé, avec taux et borne de Wilson ; un « non concluant » nomme l'artefact
  sans dents.
- Prédictions (section précédente) lues séparément des issues : chacune tenue ou non tenue, sans effet sur l'issue.
- **Audit de symétrie (R4)**, écrit avant de prononcer, si : une ligne « composition » sous v1 a une promotion ou un
  log W max > 10⁻⁹ (défaut de code) ; l'urne n'est jamais membre dominant final sous v1 dans les lignes T1a et T1b ; une
  ligne du juge v1 ne porte pas « ordre_secret » ; les promotions de v0 et de v1 sont égales, une à une, sur toutes les
  lignes de puissance appariées (le juge v1 n'aurait pas été appliqué) ; toutes les lignes fatales du socle valent
  0/1 000 (vérifier que chacune a 1 000 répétitions et un log W max fini) ; ou mes prédictions de cédage des filles sont
  contredites (≤ α) — dans les deux sens, le même audit.

## Liste d'arrêt

- Empreintes non conformes, ou essais autres que « 105, OK » : on ne lance pas ; rapport à conv-audit.
- Graine refusée, moins de 1 000 répétitions, exécution partielle, dossier de sortie non vide : le code refuse
  (essayé : `essais/test_juge_v1.py`) ; on corrige le paramètre, sans rien lire.
- Exception pendant l'exécution, ou rapport sans l'une des 70 lignes, ou une ligne à moins de 1 000 répétitions :
  aucune lecture ; rapport à Lazar et à conv-audit ; toute relance est un écart au préenregistrement scellé (nœud de
  décision de Lazar), avec une graine neuve.
- Un Python qui voit `claude_agent_sdk` : on n'exécute pas (prendre l'environnement isolé).
- Un déclencheur R4 : audit écrit avant le prononcé ; le prononcé attend l'audit.

## Contre-lecture

En cours : sous-agent neuf (modèle Fable 5.1), à qui les fichiers à lire sont donnés explicitement (R2). La section sera
remplie avant la livraison : brouillon relu (empreinte), rapport (chemin, empreinte), verdict, traitement de chaque
remarque.
