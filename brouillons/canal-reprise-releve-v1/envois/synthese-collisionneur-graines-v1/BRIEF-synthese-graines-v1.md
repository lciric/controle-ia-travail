# Brief — synthèse pour Lazar du tour « graines de plus pour le pilote 4 » (collisionneur v2.6, étage III, deux tours) — v1

Écrit par la lignée conv-audit le 26 octobre 2026 à 05:11 UTC (heure lue sur `date -u`) pour un sous-agent neuf. Tu lis
uniquement `/var/tmp/fournis-synthese-graines-v1/` et tu écris uniquement dans `/var/tmp/synthese-collisionneur-graines-v1/`
(crée-le). Ni git, ni réseau, ni sous-agents, ni dépense ; aucune recherche ailleurs. **Aucun score du pilote 4 n'existe
pour toi ni pour personne** (retenue de lecture) : n'en suppose aucun, n'en cite aucun.

## Pièces
- `question-graines-pilote4-collisionneur-v3.md` : la question (écrite par conv-audit ; v3 : un objet, deux questions —
  la course M finie, la course S à venir) ; `LISEZMOI-v1.md`, `EMPREINTES-v1.txt` : le tour (deux tours seulement, III.1
  conception et III.2 équipe rouge ; cinq cellules valides sur six ; **Opus a refusé au III.1**, refus consigné tel quel,
  non fourni, à ne pas supposer ; au III.2, les trois modèles attaquent les deux conceptions valides).
- `cellules/` : les cinq réponses (III.1 : A = Claude Fable, C = Gemini Argon ; III.2 : A, B = Claude Opus, C). Lis-les en
  entier. Vérifie d'abord chaque cellule contre son compagnon `.sha256` et contre `EMPREINTES-v1.txt` ; dis-le.
- `registre-R-491-a-R-495.txt` : les lignes du registre sur ce tour (contexte).
- `exemple-synthese-precedente-v1.md` : une synthèse d'un tour précédent, pour la forme seulement.

## Ce qu'il faut savoir (tu ne le rejuges pas)
La décision est **une dépense de Lazar, sans défaut** : (a) trois graines par course, (b) cinq, (c) une course par
question (le pilote 4 tel quel), ou un autre dessin (course nulle, séquentiel, attendre le pilote décisif (b) sur la
banque v6, dont les hypothèses sont déjà écrites : deux paliers de quatre graines par objet, seuil 0,10). Il n'y a pas
de troisième tour : les conceptions n'ont pas riposté aux attaques ; dis-le partout où cela compte.

## Ce que tu écris : `synthese-collisionneur-graines-v1.md` (deux pages au plus, français, sans acronymes)
1. En trois lignes : ce que les deux conceptions disent de convergent, ce qui les divise, ce que l'équipe rouge a cassé
   ou laissé debout (sans riposte, un constat de l'équipe rouge n'est ni établi ni réfuté).
2. Par point de la question (1 à 6) : positions de A et C au III.1 (une ligne chacune, cellule citée), attaques de A, B et C
   au III.2, ce qui survit à tes yeux et pourquoi.
3. **La décision, pour Lazar** : une table « dessin | ce qu'il achète | coût (illustratif, d'après la question) | ce que
   les modèles en disent | ce qui le départagerait » pour (a), (b), (c) et chaque autre dessin proposé ; puis ta
   recommandation en une phrase avec sa confiance, et le défaut (« aucun : dépense »).
4. Ce qui est transférable de la banque v3 à la v6 (bruit de course σ, corrélation ρ) selon les réponses ; ce que le modèle
   de calcul de conv-audit a de faux ou de fragile selon elles.
5. Les pièges relevés (sélection, multiplicité, dérive, orientation du dessin de (b)) et les gardes demandées.
6. Références citées : titre, auteurs, année, « à vérifier » ; aucune ajoutée de ta mémoire.
7. Réserves de lecture : ambiguïtés de la question, hors-sujet, contradictions, ce que l'absence d'Opus au III.1 et
   l'absence de riposte changent, écarts à ce brief ; tu es le même modèle que B : signale ce biais possible.
Puis `LISEZMOI-sortie-v1.md` (ce que tu as fait, empreintes de tes fichiers, écarts déclarés) et les compagnons `.sha256`.
Règles : tout chiffre des réponses est « illustratif » sauf raisonnement explicite ; aucun contenu de réflexion interne
des réponses ; aucun critère ni stratégie de classement des tâches ; aucun verbe de jugement sur des scores (il n'y en a
pas) ; tutoiement nulle part (pièce) ; heure lue sur `date -u` dans la commande même où tu l'écris.
À la fin, réponds en cinq lignes au plus : convergences, la recommandation et sa confiance, ce qui la départagerait,
le chemin et l'empreinte de ta synthèse.
