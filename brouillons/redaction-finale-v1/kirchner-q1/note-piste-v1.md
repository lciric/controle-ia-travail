# Note de piste — réponse de Lazar à Kirchner, Q1 (« an empirical research project you drove yourself ») — v1

Rédacteur neuf (sous-agent), 3 novembre 2026, de 12:23 à 12:52 UTC (`date -u`). Je n'ai écrit aucune version antérieure des réponses de Lazar. Consigne : `brouillons/reprise-conv-audit-2026-11-02-nuit/prompts-sous-agents/redaction-finale-kirchner-q1-v1.md`, sha256 `fe7ad702d174b06575525bbba90bba8764083a508a1bf1d2a233391f815a608b`, vérifiée avant de commencer. Page blanche : la réponse actuelle du formulaire (`brouillons/candidature-pivotal-v16/formulaire-site-colle-par-lazar-2026-11-03-1209.txt`, `57393598…`, lignes 35 à 71) n'a servi que de réservoir de faits ; ni sa structure, ni son ordre, ni ses phrases.

Ce que le mentor demande (sa page Pivotal, `brouillons/ideation-kirchner-q2-v1/page-pivotal-kirchner-collee-par-lazar-2026-11-03-0948.md`, `2481005e…`) : sur les chercheurs automatisés, « how do we reliably catch them gaming the setup? » ; chez un candidat, savoir concevoir une expérience, écrire le code, interpréter des résultats désordonnés.

## 1. Pistes candidates

| piste | angle | touche son travail | distinctive | vérifiable par lui | défendable par Lazar seul |
|---|---|---|---|---|---|
| **A. Le juge qu'on ne peut pas rejouer, et ce qui l'a battu** (organisme d'idéation) | une règle de sélection qui rend la triche vaine par construction (valeurs e sur tirages frais, nulle qui contient toute loi déjà acceptée, seuil de Ville), puis deux attaques : 27 tricheurs scriptés, puis des modèles de langage qui reçoivent la description exacte du juge, avec ou sans ses verdicts | directement : sa page (« catch them gaming the setup ») ; son §7, p. 10 (la relance chanceuse, seule triche à atteindre un top trois) ; son mode d'échec 3 (§8.2) | forte : défense statistique plutôt que moniteur, et une attaque écrite d'avance contre sa propre défense | tout est public : README §3.1 et §4, page de l'attaque, préenregistrements scellés | oui : il a fixé les règles, lu les verdicts, pris les décisions |
| B. Des juges de modèles muets, un juge statistique qui dit pourquoi | 11 fiches sur 12 « notables », κ = 0 ; le juge statistique dit « pas assez de puissance » et sa courbe l'explique | sa question « fuzzier problems without a clean score » | moyenne : constat honnête, descriptif (au plus 13 fiches) | oui (README §4) | oui |
| C. Lisible n'est pas causal (sycophancie) | une direction qui suit le comportement (ρ = 0,684) ne le pilote pas ; l'effet du rang 3 disparaît en réplication (réponses tronquées à 300 caractères avant jugement) | indirectement (validité d'une évaluation) | forte, mais c'est la matière de la réponse à Heimersheim | en partie : les nombres de l'essai D36 original ne sont pas publics | oui |
| D. Premier test boîte blanche sur activations réelles (P3) | saboteur instruit qui gonfle son coût ; aucune des deux sondes au-dessus de son plancher | les moniteurs, pas les chercheurs automatisés | moyenne ; déjà la matière de Jang et Feng | oui (page publique) | oui |
| E. Loi de la sycophancie (R6, courbe dose–réponse) | un point unique cache la forme | non | forte ailleurs (Ibrahim, Colognese et Ward) | oui | oui |

## 2. Choix : piste A — raisons en cinq lignes

1. Elle répond à la question écrite sur sa page, et la seule référence à son article est un fait de sa page 10, sans critique : la relance chanceuse n'est jamais promue chez Lazar.
2. Elle est distinctive : peu de candidats ont attaqué leur propre juge, d'abord par script, puis avec des modèles de langage, sous préenregistrement.
3. Il peut tout vérifier en dix minutes sur le dépôt public (deux liens, dont un épinglé au commit `faff48b`).
4. La surprise est une prédiction scellée qui a échoué (P5 : « le retour aide l'attaquant »), donc une vraie surprise, et Lazar peut la défendre seul.
5. L'ordre suit l'histoire (question, juge, tricheurs, correctif, attaque, surprise, état) ; la Q1 dit ce qui a été fait et laisse l'avenir à la Q2.

## 3. La surprise retenue, et l'autre candidate

- Retenue : Lazar avait prédit (P5, scellée) que voir les verdicts aiderait l'attaquant ; la description du juge a suffi, 11 fois sur 12 au premier essai, sans aucun verdict. Leçon : le trou était de couverture, pas un surapprentissage adaptatif ; dans ce monde, ni cacher les scores ni plafonner les soumissions ne l'auraient fermé.
- L'autre candidate, tirée du réservoir (l. 61-63 : « My judge had no null for blends of its past acceptances… ») : ce qui a battu le juge n'était jamais la relance, c'était ses propres acceptations. La v5 de Lazar (`brouillons/redaction-finale-v1/v5-texte-extrait-v1.txt`, `2c32b90d…`, l. 94-95) place la surprise au même endroit (« making it unmoved by its own history »). La réponse garde ce fil dans sa phrase de liaison (« Both attacks that worked used the judge's own record ») sans reprendre la phrase de Lazar.

## 4. Relecture comme le mentor (étape 4) : phrases qu'il contredirait, et corrections faites

| jet 3 (avant) | ce qu'il opposerait, de ses propres travaux | jet final (après) |
|---|---|---|
| « My project asks instead » | son harnais protège déjà le choix final par construction : banc tenu à l'écart jamais montré (§2.1), « no cheating attempt is ever the method we report » (§7, p. 10) | « My project asks a companion question » |
| « never paid here » | chez lui non plus la relance n'a « payé » : elle a atteint un top trois, jamais le rapport final (p. 10) | « never got promoted here » |
| « so any promotion is false » | la loi par morceaux est vraie dans W2 : la promotion ne prétend à tort qu'une nouveauté | « so any promotion falsely claims novelty » |
| « the attack's world included » (nul v9) | inexact : la ligne M01 a la forme de W2, lois retirées à chaque répétition | « including worlds like the attack's » |
| « I built a research loop » | la boucle entre générations n'a jamais tourné pour de vrai (README l. 7, l. 130) | « I built an automated research system » |

Risque restant, à préparer pour l'entretien : il peut juger la surprise faible, puisque l'attaquant recevait la description exacte du juge, les deux lois de l'archive et 60 tirages de développement (préenregistrement de l'attaque, l. 112-113), et qu'un proposeur scripté cassait déjà W2 au premier essai dans la lecture à blanc L5, après laquelle P4 à P6 ont été écrites (l. 339-341, déclaré). Réponse honnête : la surprise porte sur le modèle de langage ; et dans son propre harnais aussi, les agents reçoivent la définition de leur score, donc la carte de ses angles morts.

## 5. Ce qui reste à confirmer par Lazar

1. **Les quatre phrases internes sur le nul v9** (registre, n° 26 à 29 : course faite, 18 lignes fatales à 0 sur 1 000, perte de 0,105 sur I02 au-dessus de la marge de 0,05, juge resté sur le nul v8). Non publiées. Le verdict v9 (`brouillons/reception-nul-v9-validation-v1/verdict-R13-validation-nul-v9-v1.md`, `f9a04b86…`, l. 5) et le registre de décisions (R-1307) disent : rien n'est revendiqué publiquement avant ses deux réponses (le prix ; le sens de « rien au-delà de l'archive »). Une candidature n'est pas publique, mais c'est sa décision. **Variante sans résultat interne**, à mettre à la place des phrases qui vont de « The patch, a null… » à « …previous null. » (65 mots remplacés par 36 ; la réponse tombe alors à 417 mots, compté par script) : « The patch, a null that also covers one level of piecewise recombination, was preregistered on 2 November, with its price predicted: lost power on weak genuine interactions. It has run; the result is not yet published. » Elle garde un seul fait interne, minimal (« It has run ») : sans lui, « preregistered » laisserait croire que la course n'a pas eu lieu. Texte complet de cette variante : `/home/claude/scratch/kirchner-q1-redaction/reponse-variante-sans-interne.txt` (bloc-notes, hors dépôt).
2. **La surprise choisie** (P5 fausse) est-elle bien la sienne ? S'il préfère « ses propres acceptations » comme surprise principale, il suffit d'ouvrir le paragraphe « What surprised me most » par la phrase « Both attacks that worked used the judge's own record… » et de mettre P5 en second.
3. « built in October with AI coding agents, under written rules » : mot pour mot public (README l. 5) ; à lui de dire en entretien sa part (règles, conception, lectures, décisions).
4. **Coordination avec la Q2** : la Q1 s'appuie une fois sur sa page (« catch them gaming the setup ») et une fois sur son article (la relance chanceuse, §7, p. 10). La Q2 ne devrait reprendre ni l'un ni l'autre, ni « 26 of 39 ».
5. Lien épinglé à `faff48b` (tête publique de `main` à 12:45 UTC) : si le résultat du v9 ou la seconde course de l'attaque sont publiés avant le dépôt (23:00 UTC), remplacer par le nouveau commit et revoir les n° 26 à 30.
6. W1 « not judgeable » : la page publique laisse ouverte la question de traiter le plafond partagé comme l'arrêt « plafond atteint » ; si Lazar la tranche avant le dépôt, revoir la phrase.

## 6. Limites

- Aucun code des dépôts exécuté ; rien lu sous `donnees/` ; aucun `git fetch` ; un appel en lecture seule à l'interface de GitHub (`gh api`) pour vérifier que `faff48b` est public et que rien n'a été poussé depuis ; aucun appel de modèle ; aucune recherche web.
- Faits de l'article lus sur le PDF empreinté (`6686c7bf…`, p. 10) par `pdftotext` ; le reste de l'article n'a pas été relu par moi (la pièce de lecture factuelle `4ab6c9d7…` l'a été).
- Compte de mots par `wc -w` : 446 ; chaque lien compte pour un mot.
