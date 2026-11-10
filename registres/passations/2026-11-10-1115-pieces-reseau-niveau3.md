# Passation — session fille « pièces à réseau » du niveau 3 de l'état de l'art

Écrite le 2026-11-10T11:15:01Z (heure relevée par `date -u`), à la demande de la session mère (quota hebdomadaire du compte à 92 % à 11:11 UTC). À reprendre par une instance neuve sur un autre compte, dans un environnement à réseau ouvert.

## Identité
- Nom : « pièces à réseau » (niveau 3 de l'état de l'art). Identifiant : `session_01QPDgKghHndLJyQ4EpoutjR`.
- Mère : `session_01QPDgKgACWyCkCN8HjqwNXy`. Sœur sans réseau (traçabilité, lecture des PDF déjà au dépôt, synthèse finale) : `session_01QPDgKefT7L1TvJMZ4BiBNb`, branche `prep/etat-de-l-art-niveau3-v1`.
- Branche : `prep/etat-de-l-art-niveau3-pieces-v1`, partie de `main` a325a6a4. Tête au moment de la passation : voir le commit qui porte ce fichier (précédent : be52f78c).

## Mandat (mot de Lazar du 10 novembre 2026 : vérification approfondie de l'état de l'art sur ce qui n'a pas été vérifié)
Tout ce qui demande le réseau : récupérer, empreinter, faire lire sur source par des lecteurs neufs. Ordre : (1) antériorité de HC2 (MIRAGE, Karne) ; (2) littérature hors archives ouvertes ; (3) suites et voisins nommés ; (4) pièces demandées par la sœur. Verdicts à la mère ; toute collision = message immédiat, rien n'est modifié.

## Fait
Pièces versées sous `docs/sources/pdf/niveau3-v1/` (compagnons `.sha256`, notes `provenance-niveau3-lot*-v1.md`) :
- lot 1 : MIRAGE 2606.10304v1, Karne 2609.05797v3 ;
- lot 2 : hors archives — actes (ICML 2025, ICLR 2025 et 2026, NeurIPS 2025, atelier GEM d'ACL 2026), Greenblatt 2024, 2606.30449, 2610.04575 ; billets non versés (droits réservés) ;
- lot 3 : suites de NARCBench, institut britannique, recherche arXiv depuis le 6 octobre (19 PDF) ;
- lot 4 : 66 travaux citant POPPER (liste), 41 PDF, références 43 et 44 d'E-valuator, e-valeurs à nul composite ;
- lot 5 : première liste de la sœur (15 PDF, dont 2606.08892 v3 du 4 novembre) ;
- lot 6 : Truth Audit Labs = 2609.03035 v2 ; Bednarik et Schultze 2015 ;
- lot 7 : listes D1, D2, D3, C2 (39 PDF) ; lot 10 : listes C1, C3, B2, C4, C5 (18 PDF, versions 1, 2, 4 de NARCBench, CaMeL v1) ; lot 12 : deux pistes de H9 ;
- lot 8 : EN COURS, pièces scellées déjà poussées, **note de provenance pas encore écrite**.

Rapports de lecture scellés sous `docs/sources/lecture-pdf-niveau3/` (citations contrôlées par script, 0 échec) :
| rapport | commit | verdict |
|---|---|---|
| `rapport-lot1-HC2-mirage-karne-v1.md` | f8789fe6 | **HC2 occupée en partie** par MIRAGE (p. 1-2, 4, 7, 12, 18-20) ; chiffres de MIRAGE non opposables (dénominateur réel 6, p. 20) ; Karne voisin ; HC2b, HC4 non occupées |
| `rapport-lot5A-sequentiel-multi-agents-v1.md` | 4e4ad4d0 | **squelette spatio-temporel du papier B occupé en partie en boîte noire** (2601.05427, 2605.11135) ; H2 : occupation partielle boîte noire de plus (2606.20746) ; T : voisin fort |
| `rapport-lot7A-sondes-agents-H1-H2-v1.md` | 1da1e1ef | 2610.17301 (« The Agent Knew ») **n'occupe ni H1 ni H2** ; H8 « voisin fort », lecture dure « occupée en partie » à trancher (p. 37, p. 6) ; contre-indice H1 (texte supervisé égale la sonde) |
| `rapport-lot5B-sondes-agents-diffus-v3-v1.md` | 217bb817 | 2606.08892 v3 : aucun ajout boîte blanche ou séquentiel ; H2 : occupation partielle boîte noire (2606.04141) |
| `rapport-lot7D-delegation-H9-v1.md` | 9a417b13 | **H9 occupée en partie sur son cœur** (MasDrift 2608.07556v3, Sun 2608.24569v2) ; réserve de N-035 confirmée |

Messages de nœud déjà envoyés à la mère : HC2 ; papier B et H2 en boîte noire ; H8 (Fayyazi) ; H9. Copies à la sœur.

## Reste
Sous-agents encore en cours à l'écriture de cette passation (leurs rapports arrivent dans les chemins ci-dessous ; **à la reprise : vérifier sur disque et par empreinte, R11 ; un rapport sans compagnon `.sha256` est inachevé et se relance**) :
- lectures : 7-B (`rapport-lot7B-collusion-papier-B-v1.md` : 2611.02153, 2611.10620, 2609.03035 v2, 2610.24052, 2602.15198 — **les candidats les plus proches du papier B, priorité 1**) ; 7-C (`rapport-lot7C-juges-papier-C-v1.md`, en cours d'écriture, non committé) ; 3-A (`rapport-lot3A-sondes-sabotage-injection-v1.md` : 2610.12445 v4, FakeLab v2, trois articles HC2 sous injection) ; 2-A et 2-B (billets ; sources dans le dossier temporaire de la session, voir « réserves ») ; 4-A (organisme, O2 : 2511.06701, 2611.01449, 2611.04420 contre N-058…) ; 4-B (juges de la recherche automatisée) ; 10-A (sondes pendant la génération ; **histoire des versions de NARCBench, v1 à v5 : datation de l'annonce séquentielle, déclencheur de bascule de H2**) ; 12 (pistes de H9) ;
- récupérations : lot 8 (NeurIPS 165252 « What the Monitor Saw », billets LessWrong, Anthropic, OpenAI, METR, SANS, Angell, Scientific Reports ; Ramtin et collègues, Huang-Wang-Poor, Koning, échangeabilité, Donoho-Jin) ; lot 9 (citations de 2606.08892, 2512.07810, 2606.10456 ; listes arXiv du 1er au 10 novembre ; pages de Redwood, Apollo, FAR.AI, METR ; OpenReview ICLR 2027) ; lot 11 (Meincke PNAS, PAIR, GPTFuzzer, NOICE, Lorden, Moustakides, Rebholz, Soll et Larrick, Kumaran, Asher, SSRN 6569258, Constitutional Classifiers++, licences).
Non lancé : lecteurs des lots 8, 9, 11 (après leur rendu) ; lecteurs du reste du lot 10 (2602.21262 « Under the Influence » pour la forme de g de HC1, 2608.11247, 2607.00415, 2604.19784, 2305.11888, 2609.00731, 2110.00115, 2103.08402, 2603.24792) et du second rang des lots 3 et 4 ; sept pièces de `docs/sources/pdf/anteriorite-P-041-v2/c8/` proposées par la sœur ; affiche WiML de NeurIPS 2025 (à chercher sous Za, Bainiaksina, Ostrovsky, « Persuasion Attacks… » ; sinon dire « non attestée ») ; rendu final à la mère.

## Réserves
- Les pièces non versées (billets à droits réservés, Yaniv 2000 et 2004, rapport « Loss of Oversight ») ne vivent que dans le dossier temporaire de cette session (`/tmp/claude-0/-home-user-controle-ia-travail/ba75ee53-729a-59d5-934a-27a4eace4393/scratchpad/lot{2,3,6}/non-verses/`) : **perdues à la fin du conteneur**. Leurs adresses, heures et empreintes sont dans les notes de provenance : une instance neuve les retélécharge et compare les empreintes (une page web peut avoir changé).
- Les consignes communes des agents (récupération et lecture) sont copiées ci-dessous dans `docs/sources/lecture-pdf-niveau3/consignes-v1/`.
- Inaccessibles : SSRN (Panin 7424179 : 403), OpenReview (contrôle de navigateur), ScienceDirect (captcha), GitHub hors du dépôt du programme (mandataire), OpenAlex (quota jusqu'à minuit), Harvey et Fischer 1997 (payant).
- Doublons de fichiers entre lots (mêmes empreintes) : 2601.05427v3, 2608.27808v1, 2610.40588v1, 2611.10620v1 (lots 3 et 5 ou 7) ; 2210.01948v2 (lot 5 et dépôt). Sans effet.
- Erratum connu, note du lot 2, section 1 bis, ligne 10 : lire « 22, 14, 9, 13 » au lieu de « 21, 14, 8, 11 » (R12 : une v2 le portera).
- Lecteur 5-A : preuves de 2601.05427 non vérifiées (pages parcourues par titres). Lecteur 7-A : 124 pages en six minutes, à tenir pour une lecture rapide.
- Le script `docs/sources/pdf/telecharger_pdf_v1.py` met le nom du projet dans son en-tête de requête : ne pas l'employer ; employer `docs/sources/pdf/niveau3-v1/lot5/arxiv_dl_v1.py`.

## Interdits tenus
Interdits communs v2 (`docs/notes/g0-deux-semaines-v1/consignes-mere-2026-11-10-0500-v1/interdits-communs-v2.md`, 1ee3b370…), règle 9 comprise ; R7, R2, R8 ; aucune requête portant le nom de Lazar, du projet, du fonds ou une adresse ; aucune dépense, aucun modèle payant, aucune machine ; jamais les chemins du bras d'attaque, de la course 7a, de P3-bis, de l'étiqueteur, ni la branche `claude/compassionate-meitner-d4ryyk` ni un dossier `anteriorite-bras-informe*` ; rien dans `main` ; garde des secrets à 0 avant chaque commit. Seule écriture dans les registres : cette passation, demandée par la mère. Aucun refus de permissions ni de classifieur rencontré par la session elle-même ; refus de sites notés dans les provenances.

## Prochaine action exacte
1. `git fetch origin prep/etat-de-l-art-niveau3-pieces-v1` ; `ls docs/sources/lecture-pdf-niveau3/` : pour chaque rapport attendu ci-dessus, vérifier le compagnon `.sha256` ; committer et pousser ceux qui sont complets ; relancer un lecteur neuf pour chaque rapport absent ou sans compagnon, avec `consignes-v1/consigne-commune-lecture-v1.md` et la liste de PDF donnée ci-dessus.
2. Lire d'abord 7-B (2611.02153 et 2611.10620) : toute occupation du papier B par des états internes est un nœud, message immédiat à la mère.
3. Écrire la note de provenance du lot 8 (et des lots 9 et 11 si leurs agents n'ont pas rendu), puis lancer leurs lecteurs.
4. Rendu final à la mère : branche et commits, pièces récupérées et inaccessibles, verdicts, refus.

## Instances de calcul
Aucune. Aucune dépense.
