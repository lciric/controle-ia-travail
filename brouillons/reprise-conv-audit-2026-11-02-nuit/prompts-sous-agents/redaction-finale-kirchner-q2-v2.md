Tu es un **rédacteur neuf** d'une réponse de Lazar Ciric au formulaire Pivotal (Lazar remplit le formulaire maintenant). Tu n'as écrit aucune version de ses réponses. Notes en français, sans sigle non développé ; la réponse elle-même en anglais ; toute heure vient de `date -u`. Vise **25 minutes** : Lazar attend ; écris `reponse-v4.md` dès que tu as une version complète, puis améliore-la.

## La question
- Mentor : **Jan Hendrik Kirchner** (article arXiv:2608.28945 sur des chercheurs d'alignement automatiques qui grimpent un classement) ; question (texte exact, `/home/claude/controle-ia-travail/brouillons/candidature-pivotal-v16/formulaire-site-colle-par-lazar-2026-11-03-1209.txt`, ligne 73) : « Pick an open problem in AI alignment you think is underrated. What experiment would you run first, and what result would change your mind? » ; aucune limite écrite ; **au plus 450 mots**.

## Les règles de Lazar (mots du 3 novembre, heure de Paris)
- 13:05 et 13:06 : « on sélectionne d'abord la piste la plus fructueuse, les arguments les plus forts et les plus fertiles, on repart de zéro, page blanche, je ne veux pas de ma réponse générique » ; « jamais de structure préétablie ».
- **Sa réponse actuelle** (même fichier, lignes 75 à 79) n'est qu'un réservoir de faits : ni sa structure, ni son ordre, ni ses phrases.

## Pourquoi cette réécriture (mots de Lazar, 4 novembre, 00:14 heure de Paris)
« la Q2 kirshner repond elle vraiment a la question ?? ce qui est underrated de maniere generale comme probleme dans l'alignement ? ce me semble etre un probleme plus large que le probleme ultra specifique choisi, tu peux utiliser les fiches et bridges de la course d'ideation et du collisionneur pour choisir un probleme qui repond mieux a la question ? »
La réponse actuelle (`brouillons/redaction-finale-v1/kirchner-q2/reponse-v3.md`) part d'une question laissée ouverte par l'annexe D.3 de son article (la part de bruit sélectionné dans la montée au-dessus de la médiane) : trop étroite pour « un problème d'alignement sous-estimé ». Ne la lis pas avant d'avoir écrit ta propre version ; ensuite, seulement pour ne pas contredire ses faits vérifiés.

## La piste (choisie par Lazar hors règle, sur la meilleure fiche du classement)
- Groupe **« Contrôle affaibli par la sélection »** : à contrôle figé et sans adaptation des agents, la seule sélection par le score (classement, meilleur de n, filtrage) retient ou fait naître une population où le contrôle se trompe davantage que là où on l'a validé. Sa meilleure fiche, **KM-15**, est **la première du classement** (rang 1) : dans une boucle de chercheurs automatiques départagés par un classement, sans gradient contre le moniteur, le rappel d'un moniteur figé est plus bas parmi les violations que le classement retient que sur l'ensemble.
- **Formule le problème en termes généraux d'abord** (une ou deux phrases que n'importe quel chercheur en alignement reconnaît : on valide un moniteur ou une garde sur une population, puis on l'applique à celle que notre propre sélection a produite ; la sélection seule, sans intention ni gradient, concentre ses angles morts, et presque personne ne mesure le contrôle **sur la population retenue**), puis ancre-le dans son dispositif (classement, garde de capacité, moniteur) et dans les résultats publics de Lazar.
- **Dossier de piste** (les cinq fiches du groupe, complètes, avec moisson, notes et drapeaux ; puis les autres fiches en une ligne) : `/home/claude/controle-ia-travail/brouillons/ideation-kirchner-q2-v1/dossier-piste-kirchner-q2-controle-affaibli-v1.md` (sha256 `a29e8e1f781c5ec99acb07cf1c8bf51877ee8d359ef081a918f346f0be24c1f5`). Groupes : `/home/claude/scratch/kirchner-rapport/piste-kirchner/groupes-problemes-v2.md` ; classement : `/home/claude/scratch/kirchner-rapport/classement-D/classement-K-v2.md`.
- **Dans la piste, garde les arguments qui ont un appui public et une mesure qui tue.** KM-15, KM-26 et KM-17 portent un drapeau (voir le dossier) : reprends-les corrigés de ce que le drapeau dit, ou pas du tout. Les fiches d'autres groupes (par exemple « Défenses corrélées », KM-09 et KM-11) peuvent servir d'une phrase si elles renforcent le problème général.
- Prends tout fait de son article dans la lecture du PDF ci-dessous, jamais dans une fiche.

## Sources (lis-les avant d'écrire)
- Faits de son article vérifiés sur le PDF, pages citées : `brouillons/ideation-conception-organisme-v1/piece-lecture-2608-28945-parties-factuelles-v1.md` (sha256 `4ab6c9d780ac3ae9f44b70ff97e785c77d973d178a7aec3d027f8e06e584026b`).
- Ce que fait le mentor : `brouillons/candidature-pivotal-v16/lecture-approfondie-v1/rapport-kirchner-v1.md`.
- Résultats publics de Lazar : `brouillons/ideation-kirchner-q2-v1/piece-nos-resultats-v1.md` ; README public `/home/claude/ideation-organism/README.md` et ses `resultats/` ; état réel (faits internes) : `brouillons/ideation-conception-organisme-v1/piece-etat-reel-organisme-v1.md`.
- Corrections établies par une lectrice indépendante : `brouillons/canal-fable-v1/fable_2026-11-03_n001.md`.
- Affirmations déjà vérifiées par un vérificateur neuf (verdict et source par phrase), pour d'anciennes réécritures : `brouillons/candidature-pivotal-v16/lecture-approfondie-v1/recoupement-v1.md` (sha256 `bea573aa1e62d5d5bfb1aa677a902c9ec977ea1740941eed5b4277bae0e4fe0a`). Prends-y les verdicts et les sources, jamais l'ordre ni les phrases. Ses lignes « ρ = 0,68, < 1 %, 68 % : programme non publié » sont dépassées par la lectrice indépendante (fichier Fable ci-dessus) : D36 est public au commit `146b2a4` ; ρ = 0,684 et le bras « 1 % » sont **deux objets distincts** (le bras 1 % est celui de l'essai original seul, non public, non refait) ; ne les fonds jamais en une phrase.
- Ce qui est public sur ses pages : `brouillons/candidature-pivotal-v16/lecture-approfondie-v1/rapport-pages-publiques-v1.md` et `relecture-pages-publiques-v1.md`.
- Dépôts publics, clones frais en lecture seule (n'exécute jamais leur code) : `/home/claude/scratch/depots-publics-2026-11-03/sycophancy-construct-validity` (commit `146b2a4`), `/home/claude/scratch/depots-publics-2026-11-03/sycophancy-psychophysical-law` (commit `b3ecaec`), `/home/claude/ideation-organism` (branche `main`, `faff48b`). Dans la réponse, les liens vont vers `https://github.com/lciric/…`, épinglés à un commit quand cela aide à vérifier.
- Faits internes du programme de contrôle (non publics) : dépôt `/home/claude/controle-ia-travail` (registres, `diag/`, `papiers/`), en lecture seule ; un fait interne n'entre dans la réponse que dit comme non publié, et seulement si tu le retrouves dans un fichier daté (chemin et sha256).
- **Coordination** : sa Q1 pour le même mentor, version finale (`brouillons/redaction-finale-v1/kirchner-q1/reponse-v6.md`, sha256 `8d1332a6d10a87e8…`, le terme y est « reward hacking ») décrit déjà l'organisme, son juge, l'attaque et la relance chanceuse. La Q2 regarde vers l'avant : ne reprends ni la relance chanceuse, ni « 26 of 39 », ni la description du juge au-delà d'une demi-phrase.
- Résultats internes du nul v9 : **interdits** dans la réponse (R-1307 : aucune revendication publique avant la décision de Lazar).
Tous les chemins relatifs partent de `/home/claude/controle-ia-travail`.

## Ce que tu fais
1. **Arguments** : dans la piste, choisis les deux ou trois arguments les plus forts (raisons en cinq lignes), en appliquant la règle ci-dessus.
2. **Registre des affirmations** : chaque affirmation de la réponse, avec sa source (chemin et sha256, ou papier et page) et sa force (« publique et vérifiée » ; « interne vérifiée » ; « non vérifiée » : interdite). Un travail non fait n'entre que dit comme tel.
3. **La réponse**, en anglais, à la première personne de Lazar : un problème sous-estimé (et pourquoi), la première expérience (ce qu'on mesure, sur quoi, combien), le résultat qui ferait changer d'avis (avec son signe et son seuil, fixés d'avance). Simple, concret, phrases courtes, sans titres ni listes ; chaque nombre dans le registre ; liens publics quand ils aident.
4. **Relis-toi** comme le mentor : la phrase qu'il contredirait de son article ; corrige.

## Ce que tu écris (fichiers neufs, `brouillons/redaction-finale-v1/kirchner-q2/`)
`note-piste-v2.md` (français), `registre-affirmations-v2.md`, `reponse-v4.md` (la réponse seule, puis son compte de mots par script). Ces noms sont neufs : n'ouvre ni n'écrase les versions antérieures du dossier.

## Interdits
Aucun commit, aucun `.sha256`, aucun fichier existant modifié ; rien sous `donnees/` ; aucun `git fetch` ; aucun appel de modèle autre que toi ; `WebFetch` seulement pour vérifier un fait que les sources ne donnent pas ; rien sous `/home/claude/coffre-*`.

## Rendu
Réponse finale : les arguments retenus en une ligne ; le compte de mots ; le registre résumé ; ce qui reste à confirmer par Lazar ; chemins et sha256.

**N'attends aucune approbation** : si un outil en demande une, renonce à l'appel et note-le. Toute commande : `timeout 60 nice -n 10 …`.
