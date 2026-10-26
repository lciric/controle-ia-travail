# Brief — rétrodiction sur littérature réelle : la marche « à la Swanson » relie-t-elle mieux les champs éloignés ? — v1

Écrit par la lignée conv-audit le 26 octobre 2026 (heure au pied) pour un sous-agent neuf (Opus 5.5). Français, sans
acronymes. Tu lis `/var/tmp/retrodiction-swanson-v1/donnees/` (empreintes : `EMPREINTES-donnees-v1.txt`, à vérifier
d'abord) et tu écris seulement sous `/var/tmp/retrodiction-swanson-v1/sortie/`. Mot de Lazar (20:51 heure de Paris) :
« go » sur le test de la marche sur la littérature réelle.

## Le contexte

Sur des mondes synthétiques à ponts plantés, la marche « à la Swanson » (relier A à C par un intermédiaire B rare) a été
la meilleure forme de tirage (+3,5 à +3,8 points de précision sur un tirage stratifié, **+17 quand les termes passe-partout
dominent**), sous le seuil d'adoption de 12 points. La littérature réelle est saturée de termes passe-partout : on teste
si l'avantage s'y confirme, **et s'il dépasse les méthodes classiques de prédiction de liens** (indice d'Adamic-Adar,
allocation de ressources, voisins communs, attachement préférentiel), dont la marche « à la Swanson » est très proche —
sans cela, rien de nouveau.

## Les données

`arxiv-2003-2016-v1.parquet` : 999 260 articles d'arXiv (première version de 2003 à 2016), colonnes `id`, `annee`,
`categories` (la première est la catégorie principale), `title`, `abstract`. Source : jeu `librarian-bots/arxiv-metadata-
snapshot`, révision consignée dans `provenance-jeu-v1.txt`. Environnement : `/tmp/claude-0/-home-claude/b6fe1a7c-3ed9-5bb1-
972e-307cc09379be/scratchpad/venv-retro-v1/bin/python -I` (duckdb, numpy, scipy). Machine : 2 processeurs, 7 Go de
mémoire : travaille en matrices creuses et par lots.

## Le protocole, figé par ce brief (tu ne le changes pas après avoir vu une issue)

1. **Avant de calculer la moindre issue**, écris `sortie/preenregistrement-retrodiction-v1.md` (le protocole ci-dessous,
   avec tes choix d'implémentation qui ne touchent pas aux issues), calcule son empreinte et écris-la dans
   `sortie/preenregistrement-retrodiction-v1.md.sha256`. Heure lue sur `date -u`.
2. **Périodes** : avant = années 2003 à 2010 ; après = 2011 à 2016. Aucune donnée d'après n'entre dans un score (essai
   automatique qui le vérifie).
3. **Termes** : titre + résumé en minuscules, commandes LaTeX et formules retirées ; jetons alphabétiques d'au moins trois
   lettres ; liste de mots vides anglais fixe (écris-la dans le code) plus une liste fixe de mots académiques génériques
   (« paper », « results », « show », « method », « approach », « study », « propose », « using », « based »… ; écris-la) ;
   unigrammes et bigrammes de jetons consécutifs non vides ; vocabulaire = termes de fréquence documentaire **avant**
   entre 50 et 5 % des documents d'avant. Un document = l'ensemble de ses termes (présence).
4. **Champs** : groupe de premier niveau de la catégorie principale : math ; cs ; physique (astro-ph, cond-mat, gr-qc,
   hep-*, math-ph, nlin, nucl-*, physics.*, quant-ph) ; q-bio ; q-fin ; stat. Champ d'un terme = le groupe qui porte la
   plus grande part de ses documents d'avant ; terme **spécifique** si cette part ≥ 0,6.
5. **Paires candidates** : (A, C) termes spécifiques de **champs différents**, de fréquence d'avant entre 50 et 3 000,
   **jamais cooccurrents avant** (dans aucun document d'avant). Tire **1 000 000** de paires candidates, stratifiées par
   paire de champs (proportionnellement au nombre de paires possibles de chaque strate), graines par
   `numpy.random.SeedSequence` consignées.
6. **Issue** : une paire est **positive** si A et C cooccurrent dans **au moins 3** documents d'après. Rapporte le taux de
   base global et par paire de champs.
7. **Méthodes** (scores calculés sur les données d'avant seulement) :
   - (S) **marche à la Swanson** : Σ_B P(B|A)·P(C|B)·idf(B), avec P(B|A) = n(A,B)/Σ_B′ n(A,B′), P(C|B) = n(B,C)/Σ_C′ n(B,C′),
     idf(B) = ln(N_avant/df(B)), B parcourant tout le vocabulaire ;
   - (AA) Adamic-Adar : Σ_{B voisin commun} 1/ln(deg B) (deg = nombre de termes distincts cooccurrents) ;
   - (RA) allocation de ressources : Σ 1/deg B ;
   - (CN) voisins communs ;
   - (PA) attachement préférentiel : df(A)·df(C) ;
   - (ST) **tirage stratifié** : ordre aléatoire à l'intérieur de chaque paire de champs, les k premiers pris en proportion
     des strates ;
   - (U) tirage uniforme.
8. **Mesures** : précision à k = 1 000 et k = 10 000 ; précision moyenne ; aire sous la courbe ROC ; intervalles à 95 % par
   rééchantillonnage des paires (1 000 tirages) ; mêmes mesures dans la strate « dominée par les termes passe-partout »
   (paires dont plus de la moitié de la masse de S passe par des B du 1 % des termes les plus fréquents).
9. **Décisions, figées** :
   - **D1 (le test du collisionneur)** : la marche (S) est **retenue** comme règle de tirage de la version 0 si sa précision à
     10 000 dépasse celle du tirage stratifié (ST) de **12 points ou plus** ; sinon **réfutée**.
   - **D2 (nouveauté)** : la marche (S) n'est une **contribution** que si elle bat la meilleure méthode classique parmi
     {AA, RA, CN, PA} d'au moins **2 points** de précision à 10 000, intervalles disjoints ; sinon on adopte la meilleure
     méthode classique **sous son nom**, sans revendication (règle R8 du programme).
10. **Contrôles** : (a) issues permutées au hasard → toutes les méthodes au taux de base (sinon : fuite) ; (b) découpage
   placebo entièrement dans le passé (avant = 2003-2006, après = 2007-2010), mêmes méthodes : stabilité de l'ordre des
   méthodes ; (c) essai automatique d'absence de fuite temporelle.

## Ce que tu rends

`sortie/retrodiction-swanson-v1.md` (décisions D1 et D2 en tête, chiffres dans les deux sens, contrôles, ce que le test ne
dit pas — par exemple : des termes de titre et de résumé ne sont pas des concepts ; arXiv n'est pas toute la littérature),
le préenregistrement et son empreinte, le code, les résultats bruts (json), les compagnons `.sha256`. Réponse finale en
cinq lignes : D1, D2, les précisions à 10 000 de S, du meilleur classique et de ST avec intervalles, les contrôles,
l'empreinte du rapport.

## Interdits

Aucun réseau, aucun `git`, aucun sous-agent, aucune clé ; rien lu hors de `donnees/`, rien écrit hors de `sortie/` ; rien
installé ; Python avec `-I` ; heures lues sur `date -u` dans la commande qui les écrit ; les seuils, les périodes, le
vocabulaire et les décisions sont figés ici : si tu crois l'un d'eux mal posé, dis-le à part, sans changer la décision.

Horodatage : écrit le 2026-10-26 19:57:40 UTC (heure lue sur `date -u` dans la commande qui écrit cette ligne).
