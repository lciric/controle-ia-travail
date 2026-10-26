# Brief — synthèse pour Lazar du tour « littérature des boucles proposer, tester, éliminer, itérer » (collisionneur v2.5, étage III, trois tours) — v1

Écrit par la lignée conv-audit le 26 octobre 2026 à 03:39 UTC (heure lue sur `date -u`) pour un sous-agent neuf. Tu lis
uniquement le dossier `/var/tmp/fournis-synthese-litterature-boucles-v1/` et tu écris uniquement dans
`/var/tmp/synthese-collisionneur-litterature-boucles-v1/`. Ni git, ni réseau, ni sous-agents, ni dépense ; aucune recherche
récursive ailleurs.

## Pièces
- `question-litterature-boucles-agents-collisionneur-v1.md` : la question (écrite par conv-audit, figée au départ du tour,
  empreinte `962130b7…`) ; `LISEZMOI-v1.md` et `EMPREINTES-v1.txt` : le tour (huit cellules valides sur neuf ; Opus a
  refusé au tour III.2 ; ce refus n'est pas fourni et ne doit pas être supposé ; ses réponses aux tours III.1 et III.3 sont
  valides).
- `cellules/` : les huit réponses valides (III.1 conception : A = Claude Fable, B = Claude Opus, C = Gemini Argon ; III.2
  équipe rouge : A, C ; III.3 riposte : A, B, C). Lis-les en entier.
- `EMPREINTES-pdfs-v1.txt` : la liste des vingt-quatre papiers qu'un agent de lecture avait téléchargés plus tôt (noms
  courts et identifiants ; aucun n'est fourni ni lu ici), pour marquer dans ta table les références qui y figurent.
- `exemple-synthese-precedente-v1.md` : la synthèse d'un tour précédent, pour la forme seulement.

## Ce qui s'est décidé depuis la question (tu ne le rejuges pas)
- Quatrième pilote : texte final, courses parties ; la lecture contre le bruit est fixée par le texte (intervalle de Wilson
  à 97,5 % par classe ; test apparié génération 0 contre génération 3 sur la part `test_final`, correction de Holm) ; à
  ces tailles, le verdict « au-dessus de la référence » est impossible même à un score parfait.
- Boucle extérieure : registre d'hypothèses de conception écrit avant tout score ; verdicts par des agents neufs qui ne
  voient que la sortie d'un script de lecture ; protocole en cours d'écriture par un autre agent.
- Boucle intérieure : la primitive d'expérience bornée est dessinée par la lignée session-depot ; toute opération qui
  écrit dans le modèle reste fermée aux organismes, derrière un test d'évasion.
- Pilote décisif à plusieurs graines : hypothèses écrites (deux paliers de quatre graines par objet, seuil de 0,10).

## Ce que tu écris : `synthese-collisionneur-litterature-boucles-v1.md` (trois pages au plus, français, sans acronymes)
1. En trois lignes : convergences des modèles, divergences, ce que les tours II et III ont changé.
2. Par point de la question (1 à 6) : positions (une ligne par modèle, cellule citée), attaques de l'équipe rouge,
   ripostes ; ce qui survit.
3. **Table des travaux cités** : titre, auteurs, année, lieu, modèles qui le citent (A, B, C), « à vérifier » partout ; une
   colonne « dans la liste des vingt-quatre » (oui ou non, par nom court ou identifiant) ; marque les références citées
   par un seul modèle et celles que deux modèles décrivent différemment (signal possible de confabulation) ; aucune
   référence ajoutée de ta mémoire.
4. **Pour la boucle extérieure** : ce que les réponses proposent d'emprunter et d'éviter en le justifiant par la
   littérature (pas par préférence) ; fausses éliminations, fausses conservations, réutilisation adaptative des soixante
   tâches, fuite vers les vérités par la correction ; gardes minimales ; répétitions minimales ; contenu d'une hypothèse de
   conception éliminable.
5. **Pour la boucle intérieure** : la même chose.
6. **Antériorité** : ce que ces travaux occupent selon les réponses ; ce qui ne le serait pas (« à vérifier ») ; ce que le
   programme ne doit pas revendiquer (rien de « premier »).
7. Les idées neuves (que la question ne contenait pas) et les questions que les modèles renvoient.
8. Réserves de lecture : ambiguïtés de la question, hors-sujet, contradictions internes, ce que l'absence d'Opus au tour
   III.2 change, écarts à ce brief. Tu es le même modèle que B : signale ce biais de proximité possible dans l'en-tête.
Puis `LISEZMOI-sortie-v1.md` (ce que tu as fait, chemins, empreintes SHA-256 de tes fichiers, écarts déclarés), et le
compagnon `.sha256` de chaque fichier (format « empreinte, deux espaces, nom nu »).

Règles : tout chiffre des réponses est « illustratif » sauf raisonnement explicite ; ne reproduis aucun contenu de réflexion
interne des réponses s'il y en a ; aucun verbe de jugement sur des scores (il n'y en a pas) ; tutoiement nulle part
(pièce) ; aucun critère ni aucune stratégie de classement des tâches n'est à recopier, même si une réponse en propose ;
heure lue sur `date -u` dans la commande même où tu l'écris.
