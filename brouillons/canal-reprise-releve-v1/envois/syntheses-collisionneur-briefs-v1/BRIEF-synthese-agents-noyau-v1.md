# Brief — synthèse pour Lazar du tour « faire tester des agents sur le noyau pendant la conception par essais-erreurs » (collisionneur v2.5, étage III, trois tours) et de la réponse reformulée d'Opus — v1

Écrit par la lignée conv-audit le 26 octobre 2026 (vers 01:33 UTC) pour un sous-agent neuf. Tu lis uniquement ce dossier
(`/var/tmp/fournis-synthese-agents-noyau-v1/`) et tu écris uniquement dans `/var/tmp/synthese-collisionneur-agents-noyau-v1/`.
Ni git, ni réseau, ni sous-agents, ni dépense ; aucune recherche récursive ailleurs.

## Pièces
- `question-agents-noyau-essais-erreurs-collisionneur-v1.md` : la question (écrite par conv-audit) ; `LISEZMOI-v1.md` et
  `EMPREINTES-v1.txt` : le tour (sept cellules valides sur neuf ; Opus a refusé au III.1 et au III.3 ; ces refus ne sont pas
  fournis et ne doivent pas être supposés).
- `cellules/` : les sept réponses valides (III.1 conception : A = Claude Fable, C = Gemini Argon ; III.2 équipe rouge :
  A, B = Claude Opus, C ; III.3 riposte : A, C). Lis-les en entier.
- `methodo/` : la question reformulée par session-depot pour Opus seul (« conception itérative, plan statistique », sans
  les familles de tâches) et sa réponse `E3-T1-conception-B.md` ; `LISEZMOI-v1.md`.
- `exemple-synthese-precedente-lecture-pilote-v1.md` : la synthèse d'un tour précédent, pour la forme seulement.

## Ce qui s'est décidé depuis la question (pour que tu saches ce qui est déjà tranché ; tu ne le rejuges pas)
Lazar (26 octobre, Paris) : 01:56, pilotes de conception sur la banque v3 (préenregistrement et scellement levés, relecture
gardée, scores lisibles dès la fin de chaque course) ; 02:09 (chez session-depot, R-471), « go » pour une primitive
d'expérience bornée dans le noyau (lecture (1), boucle intérieure) ; 02:17, « go » pour la boucle extérieure (lecture (4)
tenue par des agents neufs à la fin de chaque course : registre d'hypothèses écrit avant tout score, verdicts par hypothèse,
ronde suivante proposée, relance sur son mot). Ta synthèse sert à dessiner ces deux boucles et à garder ce que les modèles
ont vu que personne n'avait vu.

## Ce que tu écris : `synthese-collisionneur-agents-noyau-v1.md` (trois pages au plus, français, sans acronymes)
1. En trois lignes : convergences des modèles, divergences, ce que les tours II et III ont changé.
2. Par point de la question (1 à 6) : positions (une ligne par modèle, cellule citée), attaques de l'équipe rouge,
   ripostes ; ce qui survit.
3. **Pour la boucle extérieure** : ce que les réponses prescrivent (journal, règle d'arrêt, un facteur à la fois,
   sur-ajustement aux 60 tâches, nombre d'itérations avant la confirmation, ce qu'on garde fermé, séparation
   exploration/confirmation, contamination) ; les gardes qu'elles demandent ; ce qu'une « hypothèse de conception » doit
   contenir pour être éliminable d'après elles.
4. **Pour la boucle intérieure** (primitive d'expérience bornée) : le dessin minimal sûr d'après elles, les risques
   (sortie de l'isolation, accès à la vérité des tâches, coût, reproductibilité), les essais du noyau à faire avant toute
   course ; ce que la réponse reformulée d'Opus ajoute ou contredit.
5. **Bruit** : ce qu'elles disent qu'on peut conclure à une course par objet, les répétitions minimales, la lecture
   contre le bruit des tâches ; ce qui reste invisible sans répétition.
6. Références citées : titre, auteurs, année, « à vérifier » ; aucune ajoutée de ta mémoire.
7. Les idées neuves (que la question ne contenait pas), et les questions que les modèles renvoient.
8. Réserves de lecture : ambiguïtés de la question, hors-sujet, contradictions internes, ce que l'absence d'Opus aux
   tours I et III change, écarts à ce brief.
Puis `LISEZMOI-sortie-v1.md` (ce que tu as fait, chemins, empreintes SHA-256 de tes fichiers, écarts déclarés).
Règles : tout chiffre des réponses est « illustratif » sauf raisonnement explicite ; ne reproduis aucun contenu de
réflexion interne des réponses s'il y en a ; aucun verbe de jugement sur des scores (il n'y en a pas) ; tutoiement nulle
part (pièce) ; aucun critère ni stratégie de classement des tâches n'est à recopier, même si une réponse en propose.
