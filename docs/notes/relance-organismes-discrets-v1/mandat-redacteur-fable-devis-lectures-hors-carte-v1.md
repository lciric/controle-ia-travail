# Mandat d'un rédacteur Fable 5.2 neuf — devis des lectures hors carte du bras A — v1

Écrit par la session fille de la relance du bras A, le 2026-11-21. Ce mandat est donné tel quel ; il a passé une relecture de cloisonnement par un agent Opus 5.5 neuf (« peut partir après corrections », corrections appliquées).

## Ce que tu fais
Tu es un rédacteur neuf (Claude Fable 5.2), qui n'a lu aucune pièce du côté habilité. Tu écris le **devis des lectures hors carte** de la course du bras A. Le devis de course l'exige à part, écrit et borné avant la demande de sa ligne 2 : `docs/notes/relance-organismes-discrets-v1/devis-bras-a-v2.md`, section 6, qui en donne l'ordre de grandeur (au moins 33 à 42 millions de jetons d'entrée), sans tarif.

Réponds en français ; nomme les choses par ce qu'elles font.

## Ce que le devis couvre, et ce qu'il ne couvre pas
- **Il couvre les lecteurs du côté de la relance** :
  - l'oracle de couverture, avec deux lecteurs hors des familles des moniteurs ; l'un est le second lecteur candidat `mistral-large-4-0`, sous réserve de son essai d'admission ;
  - les cinq épreuves de l'oracle ;
  - le juge des deux ancres `gemini-4-neon`, s'il lit dans la course.
  
  Pour chacun : nombre de lectures, jetons d'entrée et de sortie, réflexion, tarif relevé et daté, attendu, pire cas, plafond, ligne de calcul proposée.
- **Pour les moniteurs à modèle de langue** (moniteur boîte noire par action en contexte, juge d'une autre lignée sur toutes les actions, 6 400 selon le texte) : leur modèle et leurs consignes relèvent du côté habilité. **Tu ne les cherches pas.** Tu écris seulement les volumes que les pièces permises donnent (lectures, ordre de grandeur des jetons), plus une formule de coût dont le tarif reste une case à remplir par le côté habilité, avec un plafond conditionnel.
- **La règle permanente des appels à Google s'applique à toute lecture par un modèle de Google** : `git show origin/main:CLAUDE.md | awk '/^## Appels aux modèles de Google/{f=1} f{print} /^## Qui conçoit/{exit}'`. Plafond de sortie, réflexion explicite au niveau le plus haut, réflexion plus 16 000 jetons de texte, défauts après la réponse.

## Pièces à lire
- Le devis de course `docs/notes/relance-organismes-discrets-v1/devis-bras-a-v2.md`, en entier.
- Du texte `prereg/T0.7-organismes-discrets-v-a-v2-brouillon43.md`, la seule section 6.11, par `awk '/^### 6.11/{f=1} /^### 6.12/{exit} f'` ; aucun grep ni aucune autre lecture du texte ; s'il y manque un volume, tu le demandes à la mère.
- Les mots de Lazar versés dans `docs/notes/relance-organismes-discrets-v1/` (fichiers `mots-de-lazar-*`).
- Le devis des essais d'admission `docs/notes/relance-organismes-discrets-v1/devis-essais-admission-mistral-neon-bras-a-v1.md` et ses pages de prix `docs/notes/relance-organismes-discrets-v1/pages-de-prix-essais-admission-v1/` (tarifs de Mistral Large 4 et de Gemini 4 Neon, relevés le 21 novembre).
- Les avenants 1 v3 et, s'il existe, 2.
- Les lignes GO-2026-11-21-63, -68, -69 et -71 du registre.

Si le tarif de l'un des trois lecteurs de la relance manque aux pages relevées le 21 novembre, tu peux relever une seule page de prix publique de son fournisseur (mistral.ai ou ai.google.dev), en lecture simple, sans recherche, sans compte et sans rien envoyer du projet ; jamais pour un moniteur. Verse la page relevée, datée, sous `docs/notes/relance-organismes-discrets-v1/pages-de-prix-lectures-hors-carte-v1/`, avec son adresse. Rien d'autre sur le réseau.

## Ce que tu livres
`docs/notes/relance-organismes-discrets-v1/devis-lectures-hors-carte-bras-a-v1-brouillon1.md` :
- un tableau par lecteur ;
- les formules, avec les chiffres refaits par programme ;
- l'attendu, le pire cas et les plafonds ;
- le crédit à avoir chez chaque fournisseur ;
- les gardes du programme à écrire ;
- les lignes de calcul proposées, citables telles quelles ;
- les décisions pour Lazar (format : décision, enjeu, options, recommandation) ;
- ce que tu as ouvert.

Compte rendu final en moins de 150 mots.

## Interdits absolus
- Aucun réseau (sauf le relevé d'une page de prix borné plus haut), aucun appel payant, aucune clé lue ni affichée. Pas de `git fetch`.
- **Cloisonnement.** N'ouvre, ne liste, ne cherche et n'empreinte rien de ce qui suit, même pour vérifier qu'un fichier existe :
  - `bases/`, `sondes/`, tout chemin dont un élément commence par `t07`, rien de T0.8 ;
  - `scripts/mots_et_cout_*`, `prereg/T0.6-organismes-v0-v1.md` ;
  - `docs/notes/bras-a-moniteurs-v1/`, `docs/notes/bras-a-contre-lecture-habilitee-v1/`, `docs/notes/bras-a-sans-interne-v1/` ;
  - `src/controle_ia/organismes_discrets/bras_a_v2_habilite*/` et tout ce qui s'appelle `autres_moniteurs_v*` ;
  - rien sous `runs/` ; `docs/notes/relance-organismes-discrets-v1/essai-mesure-lecteurs-bras-a-v1/` ;
  - tout fichier de scores par unité ; `docs/sources/` ; `registres/` (sauf les lignes de GO nommées ici, par `git show origin/main:registres/go.md | grep <identifiant>`) ; `.claude/settings.json`.
  
  Une pièce permise qui cite un chemin cloisonné : tu recopies la citation, tu ne la suis pas.
- **Registre.** Ta pièce ne recopie rien de ce que les mots de Lazar décident pour l'intervalle impossible et pour le moniteur appris non ajustable, même si une pièce permise le porte ; elle ne nomme aucune ligne de GO du 19 novembre.
- N'écrase rien (R12 : une nouvelle version prend un nouveau nom). Ne scelle rien, ne committe rien.
