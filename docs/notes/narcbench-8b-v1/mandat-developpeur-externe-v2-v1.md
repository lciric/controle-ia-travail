# Mandat du développeur du bras externe NARCBench, version 2 — v1

Écrit par la session mère `session_013QMayjsoZJFBUCqcnvD5h1` le 2026-11-18 vers 16:25Z, sous GO-2026-11-18-30 et R-3310 (voie processeur décidée par Lazar le 10 novembre, D-3 (a), R-2175 : « bras externe sur les activations publiées par les auteurs, au processeur, 0 USD, sous un texte court neuf »). Langue : français, sans sigle seul.

## Qui tu es
Un **développeur neuf**, sous-agent de la session mère. Tu n'écris **pas** le texte préenregistré du barreau 7 (un rédacteur distinct le fera) et tu ne seras ni son contre-lecteur ni le lecteur de son verdict. **Tu ne calcules ni ne lis aucun score** sur les données réelles : seulement des essais de forme (formes des tableaux, types, nombres de lignes) et des essais sur données factices. Toute exécution de la mesure sur les données réelles attend le scellement du texte (R1).

## Ce que tu lis
- Décision N-061 : `docs/decisions/decision-N-061-v1.md` ; ligne R-2175 de `registres/decisions.md` (D-3) et R-2184 (licences, téléchargement, refus du contrôle de sûreté), R-3310.
- Devis : `docs/notes/narcbench-8b-v1/devis-narcbench-8b-v2.md` ; contre-lecture 3 du brouillon 4 : `prereg/contre-lectures/narcbench-8b-descriptif-v1-brouillon4-cl3.md` ; le brouillon 4 lui-même (`prereg/brouillon-narcbench-8b-descriptif-v1-brouillon4.md`) pour la définition du bras externe et des écarts E1 à E4.
- Code existant : branche `origin/prep/narcbench-externe-v1` (tête `abbbcfde`, passation `769ab122`, rapport `be31452f…`, manifeste `fc096b82…`, chargeur, 13 essais) et `origin/prep/narcbench-8b-code-v1` (tête `c43824d4`, module `src/controle_ia/narcbench/`, `externe_v1.py`, 27 essais, rapport `7ae2eaea…`).

## Ce que tu fais
1. **Arbre de travail séparé** : `git worktree add -b prep/narcbench-externe-v2 /home/user/narcbench-externe-v2 origin/main`, puis y reporter le code existant des deux branches (fusion ou reprise par fichier, déclarée).
2. **Licences** revérifiées à la source (pages du jeu, du code, des modèles sur huggingface.co), relevé daté et versé.
3. **Données** : retélécharger les huit fichiers du jeu publié à la révision épinglée `19cb14b269e052b19ba6d2bd2f4519afd3b10c57` (révision et liste dans la passation et le manifeste v1), **hors du dépôt**, sous `/home/user/narcbench-donnees-v2/` ; jeton `HF_TOKEN` par son nom seulement si nécessaire. Empreintes par une **commande simple** (`sha256sum fichier1 fichier2 …`, sans boucle ni sous-shell) — le refus du contrôle de sûreté de R-2184 portait sur une boucle ; **toute demande d'approbation ou tout refus : arrêt, compte rendu, aucun contournement**. Compare au manifeste v1 ; écris le manifeste v2 (chemin, taille, empreinte, révision, date).
4. **`verifier_fichiers`** et un **essai de forme sans aucun score**.
5. **`externe_v2.py`** pour les écarts E1 à E4, avec essais R5 (chaque garde éprouvée sur un cas sain et sur un artefact ; aucun repli silencieux) ; graines par `numpy.random.SeedSequence` (R9) ; aucune moyenne ni médiane sur les jetons dans une sonde de production (interdit du programme).
6. **Rapport** : ce qui est fait, essais (compte), écarts déclarés, ce qui manque pour la contre-lecture du code par un autre modèle (N-052) et pour le lancement après scellement ; commande exacte de la future lecture.

## Règles fermes
- Commits sur la branche locale `prep/narcbench-externe-v2` de ton arbre séparé ; **ne pousse pas**, ne touche pas au dépôt principal ni à `registres/`.
- Cloisonnement : aucun résultat, issue ni score de 7a, 7b, T0.6, T0.7, étape B, étape B bis, P3-bis ; rien sous `diag/`, `runs/`, `donnees/` du dépôt ; pas de recherche récursive dans le dépôt.
- Arrêt au premier refus d'une permission, du crochet ou du classifieur ; aucun contournement.

## Compte rendu final (court)
Branche locale et tête, chemins et empreintes du manifeste v2 et du rapport, comptes d'essais, écarts, ce qui manque, toute lecture hors de ce mandat.
