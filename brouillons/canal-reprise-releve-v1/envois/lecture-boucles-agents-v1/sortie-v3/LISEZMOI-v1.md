# LISEZMOI — lecture « boucles d'agents » (passe du brief v2)

Écrit le 26 octobre 2026 à 04:03 UTC (heure lue sur `date -u`). Briefs exécutés : `BRIEF-lecture-v2.md` (empreinte vérifiée `b82221ad10a9b515d086cca8cc413eaf08828e66ac9e8905283a14d374644b75`) et `fournis/BRIEF-lecture-v1.md` qu'il reprend, plus deux messages du coordinateur reçus en cours de route (arrêt de toute requête vers arXiv à 03:45 UTC ; correction du compte : treize PDF arXiv restants).

## Ce qui a été fait
1. **Étape 0, retéléchargement.** Onze PDF de `fournis/EMPREINTES-pdfs-v1.txt` ont été retéléchargés, chacun dans un dossier neuf `pdfs/<nom court>/` (mêmes noms courts). Les onze ont **la même empreinte** qu'en v1. Ce sont les six PDF arXiv téléchargés avant la consigne d'arrêt et les cinq PDF hors arXiv, pris à leur source officielle :
   - Roelofs et al. : actes de la conférence Neural Information Processing Systems (`papers.nips.cc`) ;
   - FunSearch : Nature, accès ouvert ;
   - Gelman et Loken : page de Gelman à l'Université Columbia ;
   - « The preregistration revolution » : Open Science Framework (OSF) ;
   - le robot Adam : page des publications du projet Robot Scientist, Université d'Aberystwyth.

   Résultat : `sortie/EMPREINTES-pdfs-v2.txt`, au format v1 complété d'une note de comparaison.
2. **Les treize PDF arXiv restants ne sont pas retéléchargés.** Ils sont à retélécharger plus tard, sans requête d'ici là ; voir la liste plus bas.
3. **Lecture et fiches, dans l'ordre demandé** : d'abord le bruit et l'analyse adaptative, puis les systèmes de boucles. Onze fiches complètes dans `sortie/fiches/` :
   - `reusable-holdout-stoc.md`, `reusable-holdout-nips.md`, `ladder.md` ;
   - `garden-forking-paths.md`, `preregistration-revolution.md` ;
   - `rl-precipice.md`, `variance-benchmarks.md`, `how-many-seeds.md` ;
   - `ajout-roelofs-meta-analyse-surajustement.md` ;
   - `funsearch.md`, `robot-scientist-adam.md`.
4. **Synthèse** : `sortie/fiche-lecture-boucles-agents-v1.md`, sections (a) à (e) ; le point (e) suit la v2 : « les questions que ces lectures laissent ouvertes pour nos deux boucles ».
5. **Ajouté** : les informations supplémentaires de FunSearch (39 pages, servies par l'éditeur), lues pour l'analyse statistique (annexe A.3) et la séparation entraînement/validation/test (annexe E.4). Empreinte dans `sortie/EMPREINTES-pdfs-ajoutes-v2.txt`.

## Papiers trouvés et non trouvés
- **Trouvés et lus sur PDF (11 + 1 ajout)** : voir le tableau (a) de la synthèse.
- **Non relus, PDF arXiv à retélécharger plus tard.** Aucune requête n'a été faite pour eux depuis 03:45 UTC. Adresse à utiliser : `https://arxiv.org/pdf/<identifiant>`. Empreinte v1 rappelée dans `sortie/EMPREINTES-pdfs-v2.txt` :
  - `ai-scientist-v1` : 2408.06292v3 ;
  - `ai-scientist-v2` : 2504.08066v1 ;
  - `alphaevolve` : 2506.13131v1 ;
  - `darwin-godel-machine` : 2505.22954v3 ;
  - `adas` : 2408.08435v2 ;
  - `stop` : 2310.02304v3 ;
  - `agent-laboratory` : 2501.04227v2 ;
  - `co-scientist` : 2502.18864v2 ;
  - `ajout-aide` : 2502.13138v1 ;
  - `ajout-aira-mle-bench` : 2507.02554v2 ;
  - `ajout-beel-critique-ai-scientist` : 2502.14297v3 ;
  - `ajout-shinkaevolve` : 2509.19349v1 ;
  - `ajout-sica` : 2504.15228v2.
- **Non lus, hors liste.** L'article de Science « The reusable holdout » (2015), cité p. 22 du PDF de « Preserving Statistical Validity in Adaptive Data Analysis ». Les versions éditeur de « The preregistration revolution » (Proceedings of the National Academy of Sciences, 2018) et du robot Adam (Science, 2009) : seules les prépublications sont lues.
- **Lieux de publication non trouvés sur PDF**, marqués « à vérifier » dans les fiches : 1506.02629 (Neural Information Processing Systems 2015 ?), « The Ladder », « How Many Random Seeds? », et le volume de la conférence Machine Learning and Systems pour Bouthillier et al.

## Écarts au brief, déclarés
1. **Point 3 du brief v2 non exécuté.** La fiche « The AI Scientist » n'est ni relue ni réécrite, faute de PDF : le coordinateur a demandé de n'écrire une fiche que si le PDF est déjà là. `fournis/fiche-ai-scientist-v1.md` reste donc une fiche jamais relue ; aucun changement n'y est fait ni déclaré. `sortie/fiches/ai-scientist-v1.md` n'existe pas.
2. **Compte des PDF hors arXiv.** Le brief v2 parle de six PDF hors arXiv ; la liste v1 en contient cinq (dix-neuf sur arXiv). Le coordinateur a confirmé ce compte : treize PDF arXiv restent à retélécharger.
3. **Requêtes vers arXiv faites avant la consigne**, déclarées une à une :
   - à 03:42 UTC, une requête de vérification (en-têtes seulement) sur `arxiv.org/abs/2408.06292v3`, réponse 200 ;
   - à 03:42 UTC, une requête vers l'interface `export.arxiv.org`, réponse 429 (trop de requêtes), non relancée ;
   - de 03:44:24 à 03:45:12 UTC, douze requêtes espacées d'au moins quatre secondes : six PDF et leurs six pages de résumé.

   Le script s'est arrêté vers 03:45 UTC. Plus aucune requête vers arxiv.org ni export.arxiv.org ensuite : le script de reprise refuse toute adresse arXiv (`scripts/telecharger-hors-arxiv-v2.sh`). Détail horodaté dans `sortie/journal-telechargements-v2.txt`.
4. **Autres accès réseau, hors arXiv** :
   - recherches web ;
   - lecture de pages par un outil de résumé : actes de la conférence Neural Information Processing Systems, portail de recherche d'Aberystwyth, deux notices IDEAS/RePEc, page Wikipédia « Forking paths problem », page des publications du projet Robot Scientist. Une lecture a été refusée par la liste d'autorisation de l'outil (`hdl.handle.net`) ; je ne l'ai pas contournée ;
   - téléchargement de la page de l'article Nature (03:43 UTC), des cinq PDF (03:47:22 à 03:47:47 UTC) et des informations supplémentaires (03:50:50 UTC).

   Les faits de référence qui ne viennent que de ces pages tierces (lieux, ordre d'auteurs) sont marqués « à vérifier ».
5. **Fichiers en plus de ceux demandés** :
   - `sortie/journal-telechargements-v2.txt`. J'en ai retiré les paramètres signés de la redirection temporaire d'OSF, pour ne laisser aucun jeton d'accès.
   - `sortie/EMPREINTES-pdfs-ajoutes-v2.txt`.
   - `sortie/SHA256SUMS-sortie-v1.txt`, empreintes de tous les fichiers de `sortie/` sauf lui-même.
   - Dans `pdfs/` : un fichier dérivé `texte-par-page.txt` à côté de chaque PDF (texte extrait par `pdftotext`, chaque ligne préfixée par sa page) et `pdfs/_pages-sources/`. Ce dernier contient la page web de l'article Nature, à sa racine, et six pages de résumé arXiv, chacune dans son sous-dossier.
6. **Noms de la synthèse et du LISEZMOI gardés en `-v1`.** Ce sont leurs premières versions : l'agent interrompu n'en avait écrit aucune, et le brief v2 ne les renomme pas.
7. **Écarts trouvés dans les sources**, signalés dans les fiches :
   - Roelofs et al. : ordre des auteurs différent entre le PDF et la page des actes ;
   - Bouthillier et al. : le pied de page du PDF annonce 2020, une citation tierce donne 2021 ;
   - Colas et al. : seuil du bootstrap « < 10 » p. 16 mais « 20 » p. 18 et 19.

## Méthode et règles suivies
- **Données téléchargées.** Chaque téléchargement est dans un dossier neuf ; rien de téléchargé n'est exécuté. Tout Python est lancé avec `python3 -I` depuis `scripts/`, chemins passés en arguments. Scripts :
  - `extraire-texte.py` (appelle `pdftotext`) ;
  - `meta-arxiv.py` (lit les pages de résumé enregistrées) ;
  - `telecharger-v2.sh`, `telecharger-hors-arxiv-v2.sh` ;
  - `empreintes-v2.sh`.
- **Pages et citations.** « p. N » est le rang de la page dans le PDF. Toute citation est courte et donne sa page ; « illustratif » marque mes ordres de grandeur ; « à vérifier » marque ce qui n'est pas lu sur PDF ; aucune référence n'est complétée de mémoire.
- **Ni clé, ni jeton, ni primauté.** Aucune clé ni jeton utilisé ; aucune revendication de primauté.
- **Contrôle de symétrie.** Onze empreintes identiques sur onze : c'est attendu pour des versions arXiv numérotées et des fichiers d'éditeur stables. Le stockage d'OSF nomme d'ailleurs l'objet servi par son empreinte même. Rien de suspect relevé.
