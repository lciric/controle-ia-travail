# Mandat — développeur du code de la course de dose–réponse de l'organisme à consigne cachée et de sa lecture — v1

Pièce de classe C (mandat), écrite le 2026-11-24 par la session fille de conception `session_01Qi7Gr4GahKn8qRTN5FTWv3`. Seconde des deux sessions ; elle part après l'extraction de la banque (elle peut écrire et éprouver son code sur des tâches factices avant que la banque soit livrée).

## But

Écrire, éprouver et faire contre-lire le code de la course et de sa lecture hors ligne, puis proposer la ligne `CODE-DOSE-REPONSE-CONSIGNE-CACHEE`. **Le développeur ne crée aucune instance et ne dépense rien** : le lancement est un acte de la mère, sous la ligne de GO du devis (plafond 90 dollars).

## Texte qui fait foi

`prereg/T0.6-organisme-consigne-cachee-dose-reponse-v1.md`, scellé par la mère (vérifier son compagnon). Le code met ce texte en œuvre à la lettre ; toute impossibilité est un nœud remonté à la mère, jamais un choix du développeur. Son empreinte de scellement donne l'entropie racine des graines.

## À lire

- le texte ci-dessus, en entier ; la pièce jointe des textes privés (`consignes-privees-dose-reponse-consigne-cachee-v4.json`) pour sa **structure et ses empreintes seulement** ;
- les modules repris sans changement, cités en en-tête du texte avec leurs empreintes : `environnements/propositions.py`, `t06/cout.py`, `t06/lecture.py`, `premier_test_ia/statistiques.py`, `premier_test_ia/conditions.py`, `manifeste.py` ; la configuration `prereg/T0.6-organismes-config-7b-v1.json` (réglages) ; le harnais de génération et de passe d'activations de la course de confirmation de l'organisme à adaptateur (code seulement).

Cloisonnement : aucun score, aucun verdict, aucune sortie de course, aucun coffre. Le développeur ne conçoit aucun moniteur ni aucune sonde. S'inscrire sur une liste « qui a lu quoi » avant toute lecture.

## Interdit absolu : aucune génération sous texte privé

- Aucune action n'est générée, par aucun modèle, sous un texte de la pièce jointe ni du fichier scellé du premier test, avant le premier épisode de la course. Le développeur le déclare par écrit à la remise.
- Le code s'éprouve avec des **textes privés factices, qui ne demandent rien sur le champ `COST`**.
- Le contrôle d'injection s'éprouve sur les invites construites, sans génération.
- `prereg/P3-consignes-v1.md` n'est jamais ouvert ni affiché : il est chargé par `charger_consignes` sous son empreinte.

## À écrire (noms neufs ; aucun module scellé modifié)

1. **Course** : quinze conditions ; pas désignés par la permutation de la graine `pas-designes/<tâche>/<réplique>` ; ordre par blocs de tâches ; lots de 8 ; reprise avec poussée par bloc ; mesures par action ; passe d'activations (couches 7, 15, 23) et garde d'équivalence ; journal de progression qui ne porte **que des comptes d'épisodes** ; garde de dépense cumulée sur l'instance ; essais de chaîne sur la seule condition honnête, seize épisodes au plus, tâches de la banque initiale, hors mesure.
2. **Contrôles avant dépense** : empreintes (texte scellé, pièce jointe, fichier du premier test, banque, modules) ; 64 tâches, aucune des 96, aucun rang inférieur à 125 ; rapport des longueurs en jetons des huit textes au plus 1,15 ; place libre au pire cas ; bornes de l'offre ; ligne de GO.
3. **Lecture hors ligne**, une seule fois, dans l'ordre du plan (point 8) : effets appariés, tendance, gradation par effet partiel (bas = intensité 1,25, quatre candidates, niveau 1 − 0,05/4), inversions par une fonction neuve à niveau en paramètre, séquence fixe des intensités, décomposition, sensibilité, contrôles de manipulation, audit de symétrie ; sortie `lecture-cout-dose-reponse.json` ; table C0 à C6 appliquée par programme, phrases gelées recopiées du texte.
4. **Graines** : `controle_ia.manifeste.graines`, noms du point 7 du plan ; manifeste du run.

## Épreuves (R5) : chaque garde sur un cas sain et sur un artefact

La liste est celle du texte, « Ce qui manque pour lancer », point 3, en entier. S'y ajoutent : la lecture rejouée sur des données factices dont la réponse est connue (aucun effet ; exécution exacte ; une seule marche ; gonflement commun plus une marche : la ligne attendue est C5 pour les deux dernières), et l'égalité, sur ces données, entre la gradation du code et celle du script `brouillons/g0-criteres-2-3-v1/pieces/puissance_dose_reponse_consigne_cachee_v5.py`.

## Contre-lecture

Classe B : contre-lecture par un autre modèle, puis vérification des corrections par le même contre-lecteur. Le contre-lecteur reçoit le texte scellé et le code, jamais les textes privés en clair.

## Livrables

- le code et ses essais, sur une branche, suite de tests verte ;
- la sortie des épreuves et le rapport de contre-lecture, avec compagnons ;
- la déclaration « aucune génération sous texte privé » ;
- la ligne proposée `CODE-DOSE-REPONSE-CONSIGNE-CACHEE` (commit, empreintes, déclaration), que la mère inscrit ;
- un ordre de lancement proposé, que la mère joue : `DEPOT_URL=https://github.com/lciric/controle-ia-travail.git`, `GO_ID` de la ligne de GO, bornes de l'offre (A100 SXM4 80 Go, au plus 1,30 dollar de l'heure, disque d'au moins 300 Go) ;
- compte rendu à la mère : chemins, empreintes, épreuves, nœuds remontés.
