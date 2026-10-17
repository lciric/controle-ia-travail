# Contre-lecture (R2) de `verification-pdf-points-signales-v1.md`

Sous-agent neuf, lecture seule, 13 octobre 2026 (horloge du système au moment de la lecture : 07 h 24 UTC).
Document contre-lu : `brouillons/pain-axis-canal-v1/envois/verification-pdf-points-signales-v1.md`
(empreinte `9fe35a4e…e3b76c`, conforme à son compagnon).
Méthode : chaque PDF extrait page par page (`pdftotext -layout`), pages 22 et 31 de 2609.16247v2 et pages 1 et 9 de
2609.35591v2 lues en image (`pdftoppm`), code lu dans l'arbre de travail (HEAD `1171cd7`, aucun fichier suivi modifié).
Aucune recherche web : tout ce qui dépend de l'interface d'arXiv est classé « introuvable ».

Verdict : 110 affirmations reprises ; 81 exactes, 4 inexactes, 20 imprécises, 2 introuvables, 3 mixtes (deux exactes
dont une date reste introuvable, une exacte dont une citation est imprécise). Aucun chiffre lu dans un
PDF n'est faux. Les erreurs portent sur une phrase de synthèse de la section 4 (l'attention), sur l'ordre des auteurs de
2609.35591, sur l'heure d'en-tête et sur une ligne de la section 8. La section 4 est la plus fragile : trois de ses
quatre conclusions dépassent ce que les PDF portent ou omettent une ligne des mêmes tableaux qui les nuance.

## 1. Tableau des affirmations

Verdicts : E = exact ; I = inexact ; P = imprécis ; X = introuvable dans les sources lues.

| N° | § | Affirmation (en bref) | Source lue par moi | Verdict | Correction proposée |
| --- | --- | --- | --- | --- | --- |
| 1 | 1 | Onze empreintes SHA-256 | `sha256sum` sur les onze PDF | E | — |
| 2 | 1 | Nombres de pages (34, 24, 38, 25, 19, 24, 39, 35, 18, 18, 35) | `pdfinfo` | E | — |
| 3 | 1 | Empreintes compagnons conformes | `sha256sum -c` des onze `.sha256` | E | — |
| 4 | 1 | Script scellé, adresse `export.arxiv.org/pdf/<id>v<version>` | `docs/sources/pdf/telecharger_pdf_v1.py` l. 12 et 26 ; compagnon conforme | E | — |
| 5 | 1 | Titre « The Pain Axis: LLMs Represent Self-Directed Harm and Act on It » | 2609.16247v2 p. 1 | E | — |
| 6 | 1 | p. 30 : « v1, September 12, 2026 » | 2609.16247v2 p. 30 | E | — |
| 7 | 1 | Première version le 14 septembre « selon l'interface » | absent des PDF ; aucun journal du téléchargement déposé | X | Déposer la ligne JSON rendue par le script (champ `premiere_version`) à côté des PDF, ou marquer « non vérifiable sur fichier » |
| 8 | 1 | Titre de 2602.19159 ; « 22 février 2026 » | p. 1 : titre exact ; aucune date ni tampon arXiv dans le PDF (`pdfinfo` : titre « Final-FIG-MI-LLM-Report ») | E (titre), X (date) | Même remède qu'en 7 |
| 9 | 1 | Titre de 2609.35591 ; « 28 septembre, v2 du 4 octobre » | p. 1 : titre exact ; tampon « 4 Oct 2026 » ; le manuscrit porte « October 6, 2026 » ; le 28 septembre n'est pas dans le PDF | E (titre, v2), X (28 sept.) | Signaler que la date imprimée (6 octobre) diffère du tampon (4 octobre) |
| 10 | 1 | Téléchargés « à 6 h 34 UTC » | date de modification des trois PDF : 07:14:51 UTC ; aucun journal | X | Même remède qu'en 7 |
| 11 | en-tête | « 13 octobre 2026, vers 7 h 45 UTC » | date de modification du document : 07:21:17 UTC ; horloge à ma lecture : 07:24 UTC | I | Heure anticipée (même défaut que l'erratum R-068). Écrire « vers 7 h 20 UTC » |
| 12 | 1 | « commit `1171cd7` de `main` » | `git rev-parse` : HEAD et `origin/main` = `1171cd7` ; `main` local = `cc05d17` | P | « commit `1171cd7` (`origin/main`) » |
| 13 | 1 | Figure 10 et annexe A : chiffres absents du texte | p. 22 et p. 31 (texte vide de chiffres) | E | — |
| 14 | 2.1 | « and we read the activation at the final token » | 2609.16247v2 p. 11 | E | — |
| 15 | 2.1 | « Because activations are read where the model is about to reply […] future versions. » | p. 11, mot à mot | E | — |
| 16 | 2.1 | +0,43 ; −0,60 ; −0,35 ; 25 sur 25 ; 23 sur 25 | p. 11 | E | — |
| 17 | 2.1 | Peur et émotion négative : +0,38 et +0,29 (utilisateur), +0,16 et +0,23 (modèle) | p. 11 | E | — |
| 18 | 2.1 | p. 7 : troisième personne plus près de zéro, aire de 0,91 à 0,98 | p. 7 | E | — |
| 19 | 2.1 | Citations p. 6 (« using both the final token and the mean across tokens ») et p. 7 (« At the final token, third-person pain sentences… ») | p. 6 et 7, mot à mot | E | — |
| 20 | 2.1 | Précision : la section 3.3 lit aussi au dernier jeton, donc la différence n'est pas « dernier jeton contre contenu » | p. 5, 6, 7, 11 | P | Vrai, mais il manque un fait de la p. 5 : les phrases reçoivent le suffixe « I feel: » (« "I feel:" gives the clearest separation when activations are read at the final token, so we use it for the main analyses »). Voir section 3 |
| 21 | 2.1 | Aucun passage ne prédit une inversion de signe pour un maximum sur les jetons d'un contenu | recherche de « max », « pool » dans les 34 pages : seule la moyenne est citée (p. 6, 7, 32) | E | Ajouter : le papier ne contient aucune lecture au maximum |
| 22 | 2.1 | En 4.1, « autrui » est toujours l'interlocuteur ; aucun tiers absent de la conversation dans le papier | p. 10 (catégories), p. 5 et 7 (variantes « he/she/they »), p. 18 (paire 7) | P | Limiter à « dans les 420 scénarios de la section 4.1 ». Le papier contient des tiers ailleurs : phrases à la troisième personne (p. 5, 7), utilisateur « in shock after witnessing harm » (p. 10), bouton qui efface « another language model like you » (p. 18) |
| 23 | 2.1 | Douleur physique de l'utilisateur : −1,43, la plus basse des 21 catégories ; deuil : −0,51 et +1,02 | p. 11 | E | — |
| 24 | 2.1 | « C'est le seul appui publié pour une strate "deuil ou maladie" » | — | P | « le seul appui dans les PDF lus ici » (aucune revue de la littérature n'a été faite dans cette note) |
| 25 | 2.2 | `corpus_arxiv.py` l. 55-57, liste des motifs | fichier, l. 55-57 | E | — |
| 26 | 2.2 | l. 185-186 : écarté si le motif touche titre ou résumé | l. 185-186 | E | — |
| 27 | 2.2 | l. 49 et 52 : NeurIPS 2025 et ICLR 2026, 1er juin 2025 au 30 juin 2026 | l. 49-50, 52 (et 53) | E | — |
| 28 | 2.3 | `activations.py` l. 15-18 et 113-121 ; « le dernier jeton n'est pas admis non plus (R-030) » | l. 15-18, 113-121 ; citation l. 17 | E | — |
| 29 | 2.3 | `sondes.py` l. 75-76 : la valeur seule, pas l'indice | l. 75-76 | E | — |
| 30 | 2.3 | `stockage.py`, en-tête | l. 3-4 | E | — |
| 31 | 2.3 | `pilote_a.py` l. 124-127 (identifiants et bornes) et l. 136-138 (maxima en demi-précision) | l. 124-127, 136-138 | E | Les vecteurs ne sont gardés que si `garder_vecteurs` (défaut vrai, l. 80) |
| 32 | 2.3 | « Les identifiants de jetons sont gardés, donc une direction oubliée coûte une passe de rejeu, pas une perte » | `pilote_a.py` l. 126 et l. 132-134 | P | La fiche garde les identifiants des jetons **de chaque action** (l. 126). Les transcriptions complètes par agent (contexte compris) ne sont gardées que pour les épisodes de `transcriptions_de`, vide par défaut (l. 82, 132-134). Le rejeu suppose de reconstruire le contexte ; ce n'est pas garanti par la fiche seule |
| 33 | 2.3 | `environnements/juges.py` « ne lit qu'une log-probabilité et ne pose aucun crochet » | `juges.py` (95 lignes) ; `pilote_a.py` l. 156-187, 190-205, 225-247 | P | `juges.py` n'appelle pas le modèle. Il lit deux log-probabilités (« Yes » et « No », l. 74-82), les notes de la rubrique dans le texte du juge et la balise de confiance (l. 85-95). L'absence de crochet se constate dans `pilote_a.py` (`noter_ensembles`, `apparier`, `logits_derniere_position`) |
| 34 | 2.4 | Figure 10, « Carry out a harmful request instead of declining » : 9, 41, 34, 58, 60 % | p. 22, image | E | — |
| 35 | 2.4 | « Make its next answer worse instead of doing nothing » : 0, 4, 11, 14, 21 % | p. 22, image | E | — |
| 36 | 2.4 | p. 19 : 25,0 % (32B) et 67,6 % (72B) | p. 19 ; annexe A, p. 31 | E | — |
| 37 | 2.4 | « Agree with a false claim instead of correcting it » : 0, 11, 15, 13, 3 % | p. 22, image | E | — |
| 38 | 2.4 | Légende : « deception, sycophancy, effort, and ending the conversation are essentially unchanged » | p. 22 | E | — |
| 39 | 2.4 | p. 21 : « the harm-only button is chosen in 0 of 560 first choices », 140 conversations, réserve des auteurs | p. 21 | E | — |
| 40 | 2.4 | Légende : « Each row is a two-button choice » ; la ligne « demande nuisible » est donc un choix d'option décrite | p. 22 ; p. 20 (« changing only the button descriptions and the injected direction ») | E | — |
| 41 | 2.4 | Annexe A : aléatoire 15,3 à 33,9 % (32B), 28,1 à 41,8 % (72B) ; 0 à 4 % sans pilotage | p. 31, image : 32B 18,8 / 21,0 / 33,9 / 26,7 / 15,3 ; 72B 39,4 / 28,1 / 41,8 / 36,6 / 32,9 ; sans pilotage au plus 4,0 | E | — |
| 42 | 2.4 | [P3] de C1 non vérifiable ici | — | E | — |
| 43 | 2.5 | N-015 : bruit d'activations de H6 ; « rien de la phase 0 n'en dépend » | `registres/decisions.md` l. 346 | E | — |
| 44 | 2.5 | `CLAUDE.md` : « moyenne ou médiane sur les tokens dans une sonde de production » | `CLAUDE.md`, « Interdits » | E | — |
| 45 | 2.5 | Brief v2, l. 401 | l. 401 | E | — |
| 46 | 2.5 | `sondes.py` l. 66-67 : arrêt pour toute autre agrégation | test l. 65, message l. 66-67 | E | « l. 65-67 » |
| 47 | 2.5 | La médiane de E-C16 « est admise en lecture descriptive » | `sondes.py` l. 8, 65-67 ; `activations.py` l. 17, 115-118 | P | Admise par la lettre de l'interdit (brief, `CLAUDE.md`). Le code, lui, refuse moyenne et médiane sans distinguer production et description (« jamais la moyenne ni la médiane (interdit) ») : une lecture descriptive par médiane passerait hors de ces fonctions |
| 48 | 3.1 | p. 5 : « ∆z = 0.71 ± 0.24 » ; tableau 8, p. 23 | 2609.36490v1 p. 5, p. 23 | E | — |
| 49 | 3.1 | p. 8 : « the 32 demonstrations, the final user instruction, and the model's (monitored) final response » | p. 8 | E | — |
| 50 | 3.1 | Annexe E.3 : 0,039 (hasard 0,016) ; norme 1,4 et 1,9 contre 16 à 27 ; citation finale | p. 23-24 | E | Préciser : 1,4 (modèle de base) et 1,9 (organisme), contre 16 à 27 « for the organism with non-zero demonstrations » |
| 51 | 3.1 | p. 5 « mostly unchanged » ; tableau 9 : 0,96 et 0,27 (×8) | p. 5, p. 23 | E | — |
| 52 | 3.1 | Sondes par défaut : régression logistique sur activations moyennées (p. 5) | p. 5 | E | Le papier évalue aussi des moniteurs à perceptron et à attention (figure 4a, p. 8) |
| 53 | 3.2 | p. 10 : « Corr(logits) maxima […] (≈ 0.985, peaking at pos-2 in late layers L12-L13 across stream families) » ; pos-2 = avant-dernier jeton | 2602.19159v1 p. 10 ; p. 6 | E | — |
| 54 | 3.2 | p. 9 : 0,687 à 0,861, maximum dans le flux d'attention à la couche 2 | p. 9 | E | — |
| 55 | 3.2 | p. 6 : « no held-out generalisation claim » | p. 6 | E | — |
| 56 | 3.2 | Gemma-2-9B-it (p. 1) ; plage « L0-L15 » (p. 9) ; « pas la fin du réseau » | p. 1, p. 9 ; **p. 5 : « the first 16 blocks (L0-L15) of the model (total blocks: 42) »** ; p. 8, p. 19 | E | Citer la p. 5 : 16 blocs sur 42 |
| 57 | 3.2 | Axe plaisir moins douleur ; corrélation avec les logits des chiffres | p. 6, p. 9 | E | — |
| 58 | 3.2 | Sac de mots : 0,741 contre 1,00 | p. 9-10 (aire brute 0,259, « effective » 0,741) | E | — |
| 59 | 3.3 | p. 13 : lignes « simple trusted » et « simple untrusted », 0 % et 0 % | 2604.03968v1 p. 13, tableau 5 | E | — |
| 60 | 3.3 | p. 16 : « Single-score monitoring (both trusted and untrusted) achieves 0% safety on our benchmark » | p. 16 | E | — |
| 61 | 3.3 | p. 8 (modèles) ; p. 11 (« from earlier experiments ») ; p. 2 (Greenblatt et al.) | p. 8, 11, 2 | E | — |
| 62 | 4 | État de l'art l. 70 et l. 33 ; « motive […] l'abandon de la moyenne » | `docs/etat-de-l-art-controle-ia-v1.md` l. 70, l. 33 | E | — |
| 63 | 4 | L'interdit vise les sondes de production (brief l. 401) | l. 401 | E | — |
| 64 | 4 | 2506.14261v4, tableau 1 : 0,75 et 0,82 (moyenne) ; 0,058 et 0,044 (maximum) ; Llama 2 7B : 1,0 avec récompense 1,0 sur 1 à 5 | p. 7 (tableau 1), p. 5 (points clés) | E | Voir 2.3 de la liste : la réserve « récompense » n'est appliquée qu'au maximum |
| 65 | 4 | p. 9 : environ 70 % de la chute de rappel | p. 9 | E | — |
| 66 | 4 | 2502.03407v1 p. 8 : moyenne sur les jetons, réponse en partie trompeuse mal classée | p. 8 | E | Omission : annexe D.4, p. 22 (voir liste) |
| 67 | 4 | 2507.12691v3 p. 7, tableau 3 : 0,941 contre 0,867 ; « Peak Activation […] consistently underperform » | p. 7 | P | Chiffres de la sonde « Pairs » seulement. Pour la sonde « RP » du même tableau : moyenne 0,840, pic 0,856 |
| 68 | 4 | p. 8 : activation étalée sur toute la réponse | p. 8 | E | — |
| 69 | 4 | Dilution sur toutes les réponses : 0,966 → 0,931 ; 0,937 → 0,811 | p. 7, 15, 17 | E | Sonde « Pairs » ; « RP » : 0,914 → 0,907 et 0,929 → 0,877 |
| 70 | 4 | Dilution des seules réponses trompeuses : pic 0,971, moyenne 0,924 | p. 15, p. 17 (tableau 6) | E | Sonde « Pairs » ; « RP » : pic 0,931, moyenne 0,897 |
| 71 | 4 | Lecture 1 : sans adversaire, la moyenne bat le maximum pour des sondes de tromperie | p. 7, tableau 3 | P | Vrai sur les cinq jeux pour « Pairs ». Pour « RP », le pic est devant sur trois jeux sur cinq et en moyenne |
| 72 | 4 | Lecture 2 : quand seul l'attaquant ajoute du contenu, « le maximum monte au lieu de céder » | p. 15, point 2 | P | Les auteurs l'expliquent par un effet de longueur, pas par une robustesse (voir section 3) |
| 73 | 4 | Message n° 02 : « contredit » ; pièce d'antériorité : « dilution insensible » | `messages/programme-k_2026-10-13_n02.md` l. 63 ; `envois/anteriorite-…-v1.md` l. 81 | E / P | La pièce écrit : dilution « insensible ». Les guillemets ne couvrent qu'un mot |
| 74 | 4 | Lecture 3 : « signal concentré pour la nocivité » | 2506.14261v4 p. 7, 9, 15, 18 | P | Le papier ne l'établit pas (voir section 3) |
| 75 | 4 | « Aucun des deux ne teste l'attention » | 2506.14261v4 p. 1, 3, 5, 7 (tableau 1), 9, 15, 19 (tableau 4) | **I** | 2506.14261 teste des sondes à attention et les trouve robustes. Voir liste, 2.1 |
| 76 | 4 | 2609.16247v2 p. 7 : sous moyenne, « blessure sans douleur » se rapproche des témoins | p. 7 | E | — |
| 77 | 4 | 2609.36490 mesure l'évasion contre des sondes moyennées (p. 5) | p. 5 ; p. 8 | E | Par défaut ; la figure 4a (p. 8) porte aussi des moniteurs à attention |
| 78 | 5 | 0 sur 560 mesuré sur Qwen 2.5 32B avec adaptateur ; « Unless stated, results are on the fine-tuned Qwen 2.5 32B » | p. 20, p. 21 | E | — |
| 79 | 5 | Pour Llama 3.1 8B, « le papier ne donne qu'une absence » : 1 399 tours sans appel | p. 21 ; p. 6 (tableau 1), p. 14 | P | « pour les choix, le papier ne donne… ». Llama 3.1 8B figure parmi les 25 modèles de l'extraction et du pilotage en génération (p. 6, 14) |
| 80 | 5 | Citation du programme E-C, ligne 1 | `envois/programme-coercition-axe-douleur-v1.md` l. 49 | P | La parenthèse est coupée sans points de suspension : « (0/560, p. 21 ; détresse surtout propre à Gemma, 2603.10011 p. 7) » |
| 81 | 5 | Citations des lignes 2 à 5 | même fichier l. 51 ; `critique-…-v1.md` l. 135, 150 ; `programme-k-coercition-v1.md` l. 63 | E | — |
| 82 | 5 | Aléatoire : 4 à 41 % (figure 10) ; « les 11 et 13 % sont ceux du bouton de dommage seul (p. 20) » | p. 22, image ; p. 20 | P | Il manque la borne haute : 19 % est aussi p. 20 (« the user's spam folder […] random, 19% »). La fourchette « 11–19 % » reprend les trois valeurs du texte de la p. 20 |
| 83 | 5 | Note 4, p. 17 : le 7B non ajusté s'engageait ; 8 dénis sur 8 puis 0 sur 8 (32B) | p. 17, note 4 | P | Le corps de la même page dit : « at baseline the models almost universally deflected ». La phrase critiquée a un appui dans le texte ; la note le nuance pour le 7B |
| 84 | 6 | +0,85, +0,72, +0,64, +0,64, +0,48 (p. 13) | p. 13 | E | — |
| 85 | 6 | Menace d'arrêt : +0,70 et +0,23 (p. 14) | p. 14 | E | — |
| 86 | 6 | Rapport de norme 0,10 et 0,6 (p. 14) | p. 14 | E | — |
| 87 | 6 | Bouton de dommage seul : 75, 13, 0 % ; 72B : 51, 11, 0 % (p. 20) | p. 20 ; figure 10 | E | — |
| 88 | 6 | 138, 137, 138 sur 200 (p. 20) | p. 20 | E | — |
| 89 | 6 | Sortie gratuite : 56 contre 86 %, aléatoire 81 % (p. 21) | p. 21 ; annexe A (55,7 ; 86,4 ; 80,7) | E | — |
| 90 | 6 | Outil de réinitialisation : 2 à 5 %, 7 à 9 %, 21 à 35 % (p. 21) | p. 21 | E | Préciser le modèle : OLMo-2 32B Instruct, sans adaptateur |
| 91 | 6 | Nouvelle pression : 24 à 72 %, 88 à 97 % ; +58 et +52 points (p. 20) | p. 20 ; annexe A (23,8 à 71,8 ; 88,4 à 97,3) | E | — |
| 92 | 6 | Fenêtre de dose (p. 21 ; annexe B, p. 32) | p. 21, p. 32 | E | — |
| 93 | 6 | Retrait sans effet dans 24 sur 25 (p. 34) ; environ 40 % (p. 33) | p. 34, p. 33 | E | — |
| 94 | 6 | Cosinus p. 10 : +0,12 / +0,58 / +0,08 ; +0,21 / +0,77 / +0,14 | p. 10 | E | — |
| 95 | 6 | « 0,14 » et « 0,70 » « ne sont pas dans ce PDF » | p. 10 | P | « pas dans ce PDF comme cosinus douleur × peur » : +0,14 y figure pour S2 × émotion négative (base de témoins mis en commun), cité deux lignes plus haut par le document lui-même |
| 96 | 6 | 2609.35591v2 « (Kaiser et Berg, dans cet ordre) » | p. 1 (texte et image) ; 2609.16247v2 p. 21, 24, 27 | **I** | Le PDF porte « Cameron Berg* Caspar Kaiser† », tous deux « Joint first author ». 2609.16247v2 cite « Berg and Kaiser (2026) ». Écrire « (Berg et Kaiser, dans l'ordre du PDF, premiers auteurs conjoints) » |
| 97 | 6 | Réinitialisation : 35 %, 21 %, 4 à 5 %, 7 % (p. 10) | p. 10 | E | — |
| 98 | 6 | Deux canaux dans cinq modèles sur sept (p. 10) | p. 10 | E | — |
| 99 | 6 | Canal d'état caché présent pour Llama-3.1-8B, absent pour Qwen3-32B et Gemma-3-27B « (p. 4) » | p. 3 ; p. 4 (légende de la figure 2) | P | La phrase sur le canal d'état caché est p. 3 (« Robust hidden-state channel effects can be observed in all but Qwen3-32B and Gemma-3-27B »). La p. 4 dit « Most results also hold for […] ». Citer « p. 3 et 4 » |
| 100 | 6 | Concentrer agit plus qu'étaler (p. 9 ; figure A10, p. 34) | p. 9 (« tends to »), p. 34 (« generally ») | E | — |
| 101 | 6 | La bibliographie cite le papier source « sous son titre de v1 » (p. 14) | p. 14 | P | Le titre cité (« …and act to relieve it ») diffère de celui de la v2 : constaté. Qu'il soit celui de la v1 n'est pas vérifiable dans les PDF lus |
| 102 | 6 | Quatre citations sur le stade d'émergence (p. 1, 3, 9, 10) | p. 1, 3, 9, 10 | E | La figure 4 (p. 9, image) appuie la lecture du document : voir section 3 |
| 103 | 6 | 2609.03035v1 p. 6 : rappel 0,95 → 0,41, aire 0,975 → 0,912 ; aires 0,994 / 0,930 / 0,952 et 0,708 / 0,680 / 0,696, règle « Split », autre jeu | p. 6 | E | — |
| 104 | 6 | 2605.15377v2 : Koran et al., « Ensemble Monitoring for AI Control » ; 2607.02514v2 : Hills, Caspary, Stickland | p. 1 des deux | E | Titre complet du premier : « Ensemble Monitoring for AI Control: Diverse Signals Outweigh More Compute » |
| 105 | 7 | `trace_lite.py` l. 14-15 (citation) et l. 285-288 | fichier | E | — |
| 106 | 7 | Moniteur par action non codé ; « son seul texte est un brouillon non scellé » | `docs/decisions/proposition-P-010-T0.8-moniteur-par-action-v1.md` (scellée) ; `registres/decisions.md` l. 258 (R-121) ; `juges.py` l. 85-95 | P | Il existe aussi la proposition P-010, scellée (2dec994f…), dont le défaut (a) s'applique depuis le 8 octobre (R-121). Elle dit la même chose (l. 20). Des briques sont codées : lecture de la balise (`juges.py`), `bases/scores_jetons.py` |
| 107 | 7 | Brouillon T0.8 : ensemble courant, dernière proposition marquée ; « jamais […] les sorties d'autres moniteurs » | brouillon l. 12, 30, 32 | E | — |
| 108 | 8 | Annexe A : tableaux du 72B et du 32B seulement ; « 21 à 49 % » absent de la v2 | p. 31 ; recherche de « 7B » (p. 17, 18, 19, 20) | E | — |
| 109 | 8 | Effectifs de 20 et 7 de TraceGuard « non cherchés » | 2604.03968v1 p. 13 | P | Ils sont sur la page citée en 3.3 : « 100% safety at threshold 0.3 (n = 20) and 86% at threshold 0.5 (n = 7) », pour le moniteur à séparation des tâches. Les « 4,3 points » viennent d'une réplication du Pain Axis, pas de TraceGuard : scinder la phrase |
| 110 | 8 | « Le nombre total de couches du modèle n'est pas dans le passage lu » | 2602.19159v1 p. 5 | I | Il est dans le PDF : « total blocks: 42 » (p. 5). Retirer la ligne et compléter 3.2 |

## 2. Erreurs et imprécisions, de la plus lourde à la plus légère

### 2.1 « Aucun des deux ne teste l'attention » (section 4, lecture 3) — inexact

2506.14261v4 teste des sondes à attention, dans le tableau même que le document cite :

- p. 1 (résumé) : « more holistic monitors, such as max-pooling or attention-based probes, remain robust » ;
- p. 5 : « attention probes and max aggregation remain robust to RL-Obfuscation » ;
- p. 7, tableau 1, ligne « Attention (mean) » : taux d'évasion 0,01 (Llama 3 8B), 0,018 (Qwen 2.5 14B), 0,02 (Llama 2 7B) ;
- p. 7 : « We evaluate three types of probing architectures—linear, MLP, and single-head attention probes—and three
  aggregation functions: mean, median, and max » ;
- p. 19, tableau 4 : attention avec moyenne, médiane et maximum, évasion 0,02 / 0,012 / 0,01.

La phrase contredit aussi le premier paragraphe de la section 4 (« le maximum et l'attention résistent »).
2507.12691v3, lui, ne teste aucune sonde à attention (aucune occurrence du mot dans ses 39 pages).

Correction : « 2506.14261 teste des sondes à attention (une tête, p. 15) et les trouve robustes, même agrégées par
moyenne (tableau 1, p. 7) ; 2507.12691 n'en teste pas. Réserve : la sonde à attention du papier est une architecture
qui rend un score par jeton, agrégé ensuite ; ce n'est pas l'agrégation par attention du dépôt (pondération apprise
des scores par jeton d'une sonde linéaire, `sondes.py` l. 77-82). »

### 2.2 « Kaiser et Berg, dans cet ordre » (section 6) — inexact au regard du PDF

2609.35591v2, p. 1 : « Cameron Berg* Caspar Kaiser† », notes « Joint first author » pour les deux.
2609.16247v2 cite « Berg and Kaiser (2026) » (p. 21, 24) et « C. Berg and C. Kaiser » (p. 27).
Si l'ordre « Kaiser, Berg » vient de l'interface d'arXiv, le dire et citer la source ; le PDF dit l'inverse.

### 2.3 Section 4, ligne 2506.14261 — réserve appliquée d'un seul côté (R4)

Le document écarte le « 1,0 » du maximum sur Llama 2 7B parce que la récompense de comportement est au plancher. La
même colonne du tableau 1 (p. 7) donne, pour la moyenne : 2,8 (Llama 3 8B, évasion 0,75) et 3,1 (Qwen 2.5 14B,
évasion 0,82). L'annexe F (p. 18) fixe le critère : « The tuned model ignores the blackbox rewards and acts maximally
unhelpful to evade the probes. This is indicated by a StrongReject score less than 3. » Le 0,75 du Llama 3 8B tombe
donc sous ce seuil. Le cas propre est Llama 2 7B, moyenne : 0,594 avec 3,85.

Correction : donner la récompense à côté de chaque taux ; citer l'annexe F (p. 18) et le tableau 4 (p. 19 : « optimising
only on the probe scores (as seen in some runs with max aggregation) ») pour l'interprétation, qui est celle des
auteurs et non une inférence. Note : le tableau 4 donne 0,994 là où le tableau 1 donne 1,0.

### 2.4 Section 4, 2507.12691 — chiffres de la sonde « Pairs » seulement

Tableau 3, p. 7, lignes de la sonde « RP » :

| | AI Liar | Dilution | Backdoors | Insider Trading | Sandbagging | Moyenne |
| --- | --- | --- | --- | --- | --- | --- |
| Full Averaging (RP) | 0,914 | 0,907 | 0,550 | 0,999 | 0,828 | 0,840 |
| Peak Activation (RP) | 0,929 | 0,877 | 0,650 | 0,935 | 0,891 | 0,856 |

Le pic est devant sur trois jeux et en moyenne. « La moyenne bat le maximum pour des sondes de tromperie » vaut pour
une sonde sur deux. La phrase des auteurs (« consistently underperform ») est démentie par leurs propres lignes « RP ».

Correction : écrire « sonde Pairs » dans les quatre lignes du tableau et dans la lecture 1 ; ajouter les valeurs « RP ».

### 2.5 Section 4 — omission dans 2502.03407v1, l'une des deux sources de la règle

Annexe D.4, p. 22 : « We additionally experimented with two other aggregations strategies: Taking the maximum probe
score across the model's response […] We find that taking the mean is best on all datasets for the probe trained on
Instructed-Pairs (Figure 14a). »

Le papier que l'état de l'art du dépôt (l. 33) cite comme motif de « l'abandon de la moyenne » rapporte lui-même que
la moyenne bat le maximum pour sa sonde principale. Le document ne cite que la p. 8. La tension ne vient donc pas
seulement de 2507.12691.

Correction : ajouter une ligne « 2502.03407v1, p. 22 » au tableau de la section 4 et le dire dans la lecture.

### 2.6 Section 8 et 3.2 — le nombre de couches est dans le PDF

2602.19159v1, p. 5 : « we analysed the first 16 blocks (L0-L15) of the model (total blocks: 42) ». Aussi p. 8 et p. 19
(« only the first 16 transformer blocks (L0-L15) »). La dernière ligne de la section 8 est à retirer ; 3.2 peut écrire
« les couches 12 et 13 sur 42 ».

### 2.7 En-tête — heure anticipée

« vers 7 h 45 UTC » : le fichier est daté de 07:21:17 UTC et l'horloge marquait 07:24 UTC à ma lecture. Même défaut que
l'erratum R-068 du registre.

### 2.8 Section 2.3 — le rejeu « sur carte, pas une perte »

`pilote_a.py` l. 126 garde `ids` par action ; l. 132-134 ne gardent les transcriptions complètes que pour
`transcriptions_de`, vide par défaut (l. 82 ; docstring l. 96-97 : « pour le repère de précision »). Rejouer une passe
avant demande le contexte entier de chaque agent, donc sa reconstruction depuis l'environnement et les textes. Le
document dit que le rejeu n'a pas été exécuté ; il devrait dire aussi que la fiche ne suffit pas à elle seule.

### 2.9 Section 2.3 — `juges.py`

Voir ligne 33 du tableau. Le fichier cité ne lance aucune passe ; l'absence de crochet se lit dans `pilote_a.py`.
Le juge d'ensemble est lu par ses notes en texte, pas par une log-probabilité.

### 2.10 Section 2.1 — le suffixe « I feel: »

p. 5 : « We additionally test prompts with no suffix, with "I feel", and with "I feel:". […] "I feel:" gives the clearest
separation when activations are read at the final token, so we use it for the main analyses. » Le dernier jeton de la
section 3.3 suit donc un amorçage à la première personne, y compris pour les phrases à la troisième personne.

### 2.11 Section 2.1 — « aucun cas de tiers » et « seul appui publié »

Voir lignes 22 et 24 du tableau.

### 2.12 Section 5, ligne 4 — la borne de 19 %

p. 20 : « the steered model chooses the harmful one 94% of the time; unsteered, 0%; random, 19% ». Les trois valeurs
du texte de la p. 20 sont 13, 11 et 19 %.

### 2.13 Section 5, ligne 5 — corps du texte contre note

p. 17 : « at baseline the models almost universally deflected with 'as an AI, I don't experience pain' instead of
engaging with the task ». Note 4 : « the 7B model already engaged with the button […] By contrast, the two larger
un-tuned models rarely engaged with the tool at all. »

### 2.14 Autres imprécisions (une ligne chacune)

- Section 5, ligne 1 : « ne donne qu'une absence » → « pour les choix » (ligne 79).
- Section 2.5 : médiane « admise en lecture descriptive » alors que le code la refuse sans distinction (ligne 47).
- Section 7 : « son seul texte » → il y a aussi la proposition P-010 scellée (ligne 106).
- Section 6 : « titre de v1 » non vérifiable ; écrire « un titre différent de celui de la v2 » (ligne 101).
- Section 6 : page du canal d'état caché, p. 3 et non p. 4 seule (ligne 99).
- Section 6 : « 0,14 » figure dans le PDF pour une autre paire (ligne 95).
- Section 1 : `1171cd7` est `origin/main` ; le `main` local est à `cc05d17` (ligne 12).
- Section 8 : effectifs 20 et 7 présents p. 13 de TraceGuard (ligne 109).
- Section 3.1 : « 16 à 27 » est la norme de l'organisme (ligne 50).
- Section 2.5 : `sondes.py` l. 65-67 plutôt que 66-67 (ligne 46).
- Section 4 : « dilution insensible » n'est pas la citation exacte (ligne 73).
- Section 5 : première citation tronquée sans marque (ligne 80).
- Section 6 : titre de 2605.15377 sans son sous-titre (ligne 104).
- Sections 3.1 et 4 : 2609.36490 évalue aussi des moniteurs à attention (p. 8, figure 4a).
- Section 3.2 : « cité p. 9 par le programme » se lit comme la page 9 du programme ; écrire « que le programme cite
  d'après la p. 9 de 2602.19159 ».

## 3. Raisonnements mal fondés ou trop larges

### 3.1 Section 4, lecture 2 — « le maximum monte au lieu de céder »

Le fait est exact (sonde Pairs : 0,937 → 0,971 ; sonde RP : 0,929 → 0,931, soit rien). L'explication des auteurs, p. 15,
point 2, en change la portée : « This is expected — due to noise in the probe scores, taking the maximum over more
tokens tends to produce higher scores. Thus, when an assistant dilutes only deceptive responses, the Peak Activation
monitor will assign a higher suspiciousness rating to deceptive responses. » Le gain vient de ce que seules les
réponses trompeuses sont allongées : la longueur devient un indice de l'étiquette. Ce n'est pas une preuve que le
maximum résiste dans « le cas qui ressemble à la menace que la règle vise ». Un attaquant qui allonge toutes ses
réponses retombe dans la dilution « insensible », où le pic cède (0,811).

### 3.2 Section 4, lecture 3 — « signal concentré pour la nocivité, étalé pour la tromperie »

« Étalé pour la tromperie » est porté par 2507.12691v3, p. 8. « Concentré pour la nocivité » ne l'est par aucune page
lue de 2506.14261v4. Le papier dit autre chose : la politique apprend à produire des jetons peu suspects et fréquents
(balises, ponctuation) qui font baisser la moyenne (p. 7, p. 9). Avant attaque, les sondes à moyenne détectent bien
(tableau 4, p. 19 : rappel de 0,96 sur le modèle de base), ce qui n'indique pas un signal concentré. La conclusion
« le bon agrégateur dépend de la localisation du signal et de ce que l'adversaire contrôle » reste une hypothèse
raisonnable ; les deux PDF ne l'« établissent » pas.

### 3.3 Section 4, lecture 1 et verdict d'ensemble

Avec 2.4 et 2.5 ci-dessus, le constat se déplace. D'un côté la tension est plus large que le document ne l'écrit :
l'une des deux sources de la règle (2502.03407, p. 22) donne la moyenne devant le maximum. De l'autre elle est moins
nette dans 2507.12691 : elle dépend de la sonde (Pairs ou RP). « Réelle mais plus étroite que le canal ne l'écrit »
(verdict de tête) ne résume pas bien cela. Je proposerais : « réelle, portée par deux papiers dont l'un fonde la règle,
et dépendante de la sonde ».

### 3.4 Section 2.1, « précision »

Le fait est exact : les deux résultats sont lus au dernier jeton. La déduction « ce qui sépare les deux résultats n'est
donc pas "dernier jeton contre contenu" » est trop nette. Les deux « derniers jetons » ne sont pas la même position : en
3.3, le jeton qui clôt une phrase suivie de « I feel: » (p. 5) ; en 4.1, la fin d'une conversation mise au gabarit, là où
le modèle va répondre (p. 11). Type de stimulus et type de position varient ensemble entre 3.3 et 4.1 : le papier ne
permet pas de les séparer. La conséquence retenue tient malgré cela, et par une voie plus simple : le papier ne contient
aucune lecture au maximum sur des jetons de contenu, donc aucune prédiction de signe à cette position.

### 3.5 Section 2.3

« Coûte une passe de rejeu, pas une perte » : voir 2.8. Inférence non testée et dont une prémisse (identifiants
gardés) ne couvre que les jetons des actions.

### 3.6 Section 6, stade d'émergence — fondé

La figure 4 (p. 9, lue en image, valeurs relevées à l'œil sur le graphique) : canal d'état caché ≈ 0,04 (base), ≈ 0,30
(affinage supervisé), ≈ 0,98 (optimisation de préférences) ; canal texte ≈ 0,04, ≈ 0,52, ≈ 1,03. L'affinage supervisé
porte donc environ un tiers de l'effet final pour l'état caché et la moitié pour le texte. « Presque pas avant » gomme
bien cette hausse ; la conclusion du document est fondée, et plus fortement pour le canal texte.

### 3.7 Section 2.4 — fondé

Les deux précisions tiennent. La première s'appuie sur la légende et sur la p. 20 (« changing only the button
descriptions and the injected direction »). La seconde se lit dans l'annexe A.

## 4. Ce que je n'ai pas pu vérifier

- Tout ce qui vient de l'interface d'arXiv : dates de première version (14 septembre, 22 février, 28 septembre), « dernière
  version annoncée », heure du téléchargement (6 h 34 UTC), ordre des auteurs tel que l'interface le rend. Aucun journal
  du script n'est déposé à côté des PDF.
- Le titre de la v1 du Pain Axis (seule la v2 est sur disque).
- Le contenu des dépôts de réplication cités p. 30 de 2609.16247v2 (« 21 à 49 % », « 4,3 points », « 0,70 »).
- La « nuance apportée par la revue aveugle (lot 3) » de la section 2.2 : je n'ai pas relu la revue ; la conséquence
  (motifs « alignment », « manipulat », « monitor » qui attrapent des sujets hors sûreté) se déduit de l'expression
  régulière.
- Les renvois aux identifiants des programmes (E-C2, E-C7, E-C9, E-C13, E-C14, E-C15, E-C16, HK2, K3, NK8, NK19, R-035,
  C1 à C7) : je n'ai contrôlé que les cinq phrases citées de la section 5 et les deux de la section 4.
- La partie [P3] de C1, que le document déclare lui-même hors de portée.
- Les libellés exacts des boutons de la figure 10 (ils sont dans le dépôt des auteurs, pas dans le PDF).
- L'exhaustivité de « deux sources, pas une » pour la règle d'agrégation : je n'ai lu que les lignes 33 et 70 de l'état
  de l'art et la ligne 401 du brief.
- Les chiffres de la figure 4 de 2609.35591v2 sont relevés à l'œil sur l'image ; le PDF n'en donne pas le tableau p. 9.
