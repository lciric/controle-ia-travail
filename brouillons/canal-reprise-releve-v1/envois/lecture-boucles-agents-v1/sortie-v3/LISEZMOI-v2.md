# LISEZMOI — lecture « boucles d'agents » (passe v3)

Écrit le 26 octobre 2026 à 06:45 UTC (heure lue sur `date -u`). Cette passe exécute le message du coordinateur (lignée conv-audit) reçu après la fin des courses du quatrième pilote (06:05:46 UTC) : reprise des treize PDF arXiv. Briefs inchangés : `BRIEF-lecture-v2.md` (empreinte vérifiée `b82221ad10a9b515d086cca8cc413eaf08828e66ac9e8905283a14d374644b75`) et `fournis/BRIEF-lecture-v1.md`. `sortie/LISEZMOI-v1.md` reste intact et décrit la passe précédente.

## Ce qui a été fait
1. **Téléchargement des treize PDF arXiv restants**, par `scripts/telecharger-arxiv-v3.sh`.
   - PDF seulement (`https://arxiv.org/pdf/<identifiant>`), aucune page de résumé, aucune requête vers export.arxiv.org.
   - Chaque PDF dans un dossier neuf `pdfs/<nom court>/`, sous le même agent utilisateur qu'en passe v2.
   - Treize requêtes, de 06:10:08 à 06:16:27 UTC, à 31 secondes d'intervalle au moins ; toutes en réponse 200 `application/pdf`, sans redirection, sans 429 ni 403.
   - Arrêts prévus mais non déclenchés : sur 429 ou 403 (tout arrêter), et par prudence sur toute autre réponse que 200 ou tout fichier qui ne commence pas par « %PDF- ».
   - Les treize ont la même empreinte qu'en v1. Journal : `sortie/journal-telechargements-v3.txt`.
2. **Extraction du texte** par `scripts/extraire-texte.py` (appelle `pdftotext`) : un `texte-par-page.txt` à côté de chaque PDF, chaque ligne préfixée par sa page. Rien de téléchargé n'est exécuté ; Python est lancé avec `python3 -I` depuis `scripts/`, chemins en arguments.
3. **Lecture et fiches, dans l'ordre demandé**, treize fiches nouvelles dans `sortie/fiches/` :
   - d'abord ceux qui disent comment un système juge ses propres variantes : `ai-scientist-v1.md` (relue), `ai-scientist-v2.md`, `ajout-beel-critique-ai-scientist.md`, `alphaevolve.md`, `darwin-godel-machine.md`, `ajout-shinkaevolve.md`, `ajout-sica.md` ;
   - puis les autres : `adas.md`, `stop.md`, `agent-laboratory.md`, `co-scientist.md`, `ajout-aide.md`, `ajout-aira-mle-bench.md`.

   Avec les onze de la passe v2, `sortie/fiches/` compte vingt-quatre fiches. Avant l'empreinte finale, les treize fiches nouvelles ont été recontrôlées contre le texte des PDF. Corrections faites :
   - pages et attributions précisées ;
   - acronymes développés ;
   - incohérence de 50 et 60 tâches relevée dans la Darwin Gödel Machine (p. 6) ;
   - correction de Henry Cohn rapportée dans AlphaEvolve (p. 39).
4. **Point 3 du brief v2 exécuté** : la fiche « The AI Scientist » de l'agent interrompu est relue contre le PDF. Version relue : `sortie/fiches/ai-scientist-v1.md` ; changements listés plus bas.
5. **Synthèse nouvelle** : `sortie/fiche-lecture-boucles-agents-v2.md`.
   - Elle reprend la v1 (laissée intacte) et ajoute les treize.
   - En tête, sur moins d'une page, ce qui change pour la boucle extérieure : bruit entre graines, sélection sur le bruit, ensemble de test réutilisé, juge interne.
   - Puis les sections (a) à (e) mises à jour.
6. **Empreintes.**
   - `sortie/EMPREINTES-pdfs-v3.txt`, écrit par `scripts/empreintes-v3.sh`, qui refuse d'écraser : vingt-quatre PDF de la liste v1 et le supplément de FunSearch, tous à la même empreinte qu'avant.
   - `sortie/SHA256SUMS-sortie-v2.txt` : tous les fichiers de `sortie/` sauf lui-même, contrôlés par `sha256sum -c`.

## Changements apportés à la fiche « The AI Scientist » de l'agent interrompu
Comparaison de `fournis/fiche-ai-scientist-v1.md` à `sortie/fiches/ai-scientist-v1.md` :
1. **Affiliations** complétées d'après le PDF (p. 1) : FLAIR (Université d'Oxford), Vector Institute, chaire Canada CIFAR.
2. **Dates et lieu.** La date de la première version (12 août 2024) venait de l'interface d'arXiv, pas du PDF : elle devient « à vérifier ». Version lue : 1er septembre 2024 (tampon, p. 1). Lieu : « aucun lieu indiqué sur le PDF », au lieu d'une mention des métadonnées d'arXiv.
3. **Pages lues** : 1 à 21, au lieu de 1 à 8 et 12 à 20. Les annexes sont fouillées par mots clés, notamment p. 35 à 38, au lieu de « non lues ».
4. **Relecteur automatique.** Il n'est pas « calibré » mais validé contre les décisions de 500 articles soumis à la conférence International Conference on Learning Representations 2022, avec un seuil fixé après coup (p. 6). Chiffres ajoutés (p. 6 et 7) :
   - exactitude de 70 % contre 73 % ;
   - exactitude équilibrée de 0,65 contre 0,66 ;
   - faux positifs 0,31 contre 0,17 ; faux négatifs 0,39 contre 0,52 ;
   - corrélation de 0,18 contre 0,14 ;
   - seuil relevé à 8 pour Sonnet 3.5, à cause d'un biais d'optimisme.
5. **Graines corrigées.** La fiche fournie disait que nanoGPT et « grokking » lançaient trois graines sur certains jeux et une sur les autres. Sur le PDF :
   - nanoGPT : trois graines sur Shakespeare, une sur enwik8 et text8 (p. 15) ;
   - « grokking » : trois graines sur chacun de ses quatre jeux (p. 16) ;
   - diffusion : nombre de graines non indiqué (p. 14).
6. **Ajouts** :
   - aucune baisse du score observée quand les idées sont générées sans attendre les évaluations (p. 13) ;
   - nouveauté auto-évaluée par chaque modèle (p. 13) ;
   - limites du relecteur : données possiblement vues en pré-entraînement, pas d'accès aux figures (p. 18) ;
   - « minimal direct sandboxing » (p. 19) ;
   - 49 idées sur 51 jugées nouvelles (tableau 3, p. 14) ;
   - coût de 10 à 15 dollars par article (p. 13), en plus de « less than $15 » (p. 1) ;
   - boucle ouverte « in principle » : renvois élargis à p. 1 à 4 (la fiche fournie donnait p. 3 et 4) ; l'expression elle-même est p. 2.
7. **Lieu du papier de Beel.** Le lieu « SIGIR Forum » n'est pas sur le PDF de Beel : retiré et signalé. SIGIR Forum n'y apparaît que dans la référence d'un autre article des mêmes auteurs (p. 16).
8. **Citations** raccourcies et gardées en anglais, avec leur page, au lieu de traductions présentées entre guillemets.
9. **Lignes « à emprunter » ajustées** : un juge interne se valide contre une vérité de terrain, avec ses taux de faux positifs et de faux négatifs (p. 6). Ajout d'une ligne « vérifié par des tiers » : The AI Scientist v2 cite Beel comme évaluation indépendante (p. 14 de son PDF).

Ce qui tenait est gardé : description de la boucle, exemples d'échecs (p. 15, 18 et 19), chiffres du tableau 3 (p. 14).

## Papiers trouvés et non trouvés
- **Lus sur PDF : les vingt-quatre de la liste v1**, plus les informations supplémentaires de FunSearch. Les annexes longues sont lues par mots clés seulement ; le détail des pages est dans chaque fiche. Les plus partielles sont :
  - The AI Scientist : 186 pages, annexes p. 22 à 186 ;
  - le co-scientifique : 157 pages ;
  - Agent Laboratory : 84 pages ;
  - la Darwin Gödel Machine : 72 pages ;
  - The AI Scientist v2 : 69 pages.
- **Non lus, hors liste** :
  - l'article de Science « The reusable holdout » (2015) ;
  - les versions éditeur de « The preregistration revolution » et du robot Adam ;
  - les papiers cités comme source d'évaluations reprises : MLE-Bench (Chan et al.) et RE-Bench (METR), repris par AIDE et AIRA ;
  - Lehman et al. (2023), cité par FunSearch.
- **À vérifier, faute d'indication sur le PDF** :
  - lieu de publication de Beel ;
  - date et lieu du co-scientifique : PDF sans tampon arXiv ni date, rendu par Google Docs, titre interne « [CoS] Nature revision AAP », citant des modèles récents (p. 24) ;
  - lieux d'AIDE, d'AIRA, de ShinkaEvolve, de SICA, d'Agent Laboratory, de The AI Scientist et de sa v2 (aucun sur le PDF) ;
  - date de la première version de The AI Scientist ;
  - source exacte des chiffres d'accord 53,3 % et 56,1 % qu'Agent Laboratory attribue à The AI Scientist (p. 19), absents du PDF de The AI Scientist (recherche par mots clés).

## Écarts au brief et aux consignes, déclarés
1. **Fichier temporaire écrit hors du dossier autorisé.**
   - Vers 06:40 UTC, pour compter les mots de l'en-tête de la synthèse, j'ai écrit par erreur un extrait de cet en-tête dans le dossier temporaire de la session, hors de `/var/tmp/lecture-boucles-agents-v2/`. Je l'ai supprimé aussitôt (heure de la vérification : 06:40:27 UTC).
   - La commande de vérification a affiché la liste des noms de fichiers de ce dossier temporaire. Je n'ai ouvert aucun de ces fichiers.
   - Le comptage a ensuite été refait sans fichier intermédiaire.
2. **Sorties d'outil hors du dossier.** Pendant mes lectures, deux sorties d'outil trop longues ont été enregistrées automatiquement par l'environnement hors du dossier. Je ne les ai pas ouvertes ; les pages concernées ont été relues par plages plus courtes.
3. **Fichiers en plus de ceux demandés** : `scripts/telecharger-arxiv-v3.sh`, `scripts/empreintes-v3.sh`, et les `texte-par-page.txt` des treize PDF.
4. **Fichiers de la passe v2 non modifiés** : synthèse v1, `LISEZMOI-v1.md`, `SHA256SUMS-sortie-v1.txt`, empreintes v2, journal v2 et les onze fiches de la passe v2. `SHA256SUMS-sortie-v1.txt` se vérifie toujours.
5. **Écarts trouvés dans les sources**, signalés dans les fiches :
   - Darwin Gödel Machine : un sous-ensemble annoncé de 50 tâches, puis de 60 (p. 6) ;
   - AlphaEvolve : borne annoncée comme nouvelle, battue par un article de 2019, selon la note des auteurs (p. 39) ;
   - Agent Laboratory : attribution des chiffres d'accord (p. 19) ;
   - titres changés entre versions : le co-scientifique et Beel, d'après les citations de The AI Scientist v2 (p. 15 de son PDF).

## Méthode et règles suivies
- Une requête vers arXiv toutes les 31 secondes au moins, PDF seulement, même agent utilisateur, heures lues sur `date -u` ; aucun site n'a refusé ; aucun contournement.
- « p. N » est le rang de la page dans le PDF. Toute citation est courte et donne sa page ; « illustratif » marque mes ordres de grandeur et mes lectures personnelles ; « à vérifier » marque ce qui n'est pas lu sur PDF ; aucune référence n'est complétée de mémoire.
- Ni `git`, ni sous-agent, ni clé, ni jeton ; aucune revendication de primauté. Les revendications citées dans la synthèse (section (d)) sont celles des auteurs, rapportées comme telles.
- **Contrôle de symétrie.** Treize empreintes identiques sur treize, après onze sur onze en passe v2. C'est attendu : arXiv sert le fichier stocké d'une version numérotée explicite. Rien de suspect relevé ; les contrôles de format (code 200, type `application/pdf`, en-tête « %PDF- ») ont tous passé.
