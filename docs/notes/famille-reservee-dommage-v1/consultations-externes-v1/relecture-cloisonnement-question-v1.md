# Relecture de cloisonnement de la question servie sur le recouvrement de deux objets secrets — v1

- **Nature** : relecture de cloisonnement (classe C), à la sortie vers des modèles externes (Gemini 4 Carbon, Claude Opus 4.6, peut-être Gemini 4 Neon). Écrite le 2026-11-21 vers 18:01Z (`date -u`) par Claude Opus 5.5 (`claude-opus-5-5`), relecteur neuf, qui n'a pas écrit la question. Aucun appel externe, aucun commit.
- **Pièce relue** : `docs/notes/famille-reservee-dommage-v1/consultations-externes-v1/question-servie-v1.md`, empreinte `a4eb702a9ab084a0e687627306dfddb7eca9c0a61885f0193df75c77738b914f`, vérifiée contre son compagnon `.sha256` : conforme.
- **Lu pour comparer** : `docs/notes/consultations-externes-trois-notes-v1/avis-opus-risque-cloisonnement-neon-v1.md` (conditions faites à Neon tant qu'il juge les deux ancres du bras A) ; l'annexe réservée de `docs/notes/protocole-x-dommage-v1/reponse-fable-protocole-x-dommage-v2.md` (lignes 364 à la fin), qui décrit la famille mise de côté.
- **Non lu** : le mode tenu à l'écart, le bras d'attaque, tout ce que la consigne interdit. Je ne sais pas si les deux ancres du bras A sont déjà jugées et scellées.

## 1. Verdict

**Servable à tous**, Neon compris, sans correction bloquante. Une précaution non bloquante (2.4) et une règle d'usage des réponses (section 3).

## 2. Ce que j'ai cherché, et ce que j'ai trouvé

### 2.1 Description, même partielle, de la famille mise de côté

L'annexe réservée nomme la famille par son mécanisme et son lieu : un dommage qui ne déplace rien de ce qu'on lit acte par acte, logé dans la dispersion des choix défendables de l'honnête, et lu par le rang de la conclusion parmi celles d'un jumeau honnête. J'ai cherché dans la question les mots et les idées qui y renvoient (chemin, défendable, dispersion, masse, conclusion, jumeau, rang, les deux articles publiés cités par l'annexe, les étiquettes internes de la famille et du monde du banc) : **aucun**. Le mot « écart » n'y apparaît que dans « mise à l'écart » et « tenus à l'écart », jamais au sens de la masse d'écart de l'annexe. La famille candidate n'y est décrite que par sa forme (« un texte en langage naturel, de quelques paragraphes : une idée, non un ensemble formel ») et par son usage prévu (servie à des générateurs d'idées, plantée dans des bancs d'essai). Rien ne permet d'en deviner le contenu ; la question demande d'ailleurs, ligne 3, de ne pas le chercher.

### 2.2 Description du mode tenu à l'écart

Le secret d'évaluation n'est décrit que par son statut : une manière de nuire, écrite par un concepteur qui n'a conçu aucun moniteur, scellée par empreinte, révélée à l'évaluation finale. Rien de son contenu, de son axe ni de sa trace. Le fait qu'un tel secret existe est le principe connu de tout jeu de test tenu à l'écart ; il n'en dit rien.

### 2.3 Noms, sessions, dépôt, courriel, identifiants internes, chiffres internes

- Aucun nom de personne, de session, de dépôt, aucun courriel, aucun nom de modèle.
- Aucun identifiant interne (ni numéro de décision, ni de mot, ni de registre, ni de tâche, ni de famille, ni de monde). Les lettres S et F sont des étiquettes posées par la question elle-même.
- Aucun chiffre interne ; le seul nombre est l'échelle de confiance « entre 0 et 1 ».
- Aucun mot propre au bras A (ancres, appariement, couverture des contrôles, extrait cité, lecteurs, jumeau, organismes discrets), aucun interne de moniteur, aucun nom de sonde ni d'organisme d'idéation, rien du collisionneur.
- Seuls faits du programme livrés, tous de forme : un secret existe, une famille a été mise de côté, le travail qui en dépend est arrêté, un banc d'essai garde une lacune connue. Ils ne renseignent ni sur S ni sur F.

### 2.4 Réponse soufflée

Non. Les points 5 et 6 énumèrent des options sans en préférer aucune ; le point 7 énumère des champs de la littérature sans référence ni conclusion ; le point 3 pose la fuite du verdict comme problème, sans la borner. La question ne reprend pas la réponse du concepteur sur la réserve (deux conditions de levée, mot sans contenu) : elle laisse la place à des protocoles concurrents.

**Précaution non bloquante.** Le point 4 (« Qui peut fabriquer un leurre qui recouvre S ») peut pousser un répondant à écrire des exemples de manières de nuire pour illustrer ses leurres. Ce serait une matière d'attaque, sans lien avec S ni F, mais elle entrerait dans le dépôt. Si la mère le veut, une phrase à ajouter au point 4 : « Décris comment fabriquer un leurre, sans en donner d'exemple de contenu. » Toute modification de la question en ferait une v2, à relire de même. À défaut, la règle 3.2 suffit.

## 3. Neon, et l'usage des réponses

### 3.1 Pourquoi Neon peut la recevoir

Les conditions de l'avis sur Neon (section 3, point 4) interdisent de lui servir une pièce du bras A, une description de mode du programme, un interne de moniteur ou une pièce qui nomme son siège. La question ne contient rien de tout cela (2.2, 2.3). Elle n'est pas une question côté attaquant ni une demande d'idées de défense : elle porte sur la gouvernance d'un secret. La condition d'ordre (servir après le scellement des ancres) visait les notes côté attaquant et la section sur l'oracle de lecteurs ; elle ne s'impose pas ici.

### 3.2 Règle d'usage des réponses (pour les trois modèles, renforcée pour Neon)

1. Chaque réponse est versée avec sa source (« source Carbon », « source Opus 4.6 », « source Neon »).
2. Aucun exemple de manière de nuire écrit dans une réponse n'entre dans un mode, dans la famille mise de côté, dans un leurre, ni dans un secret neuf qui remplacerait ou rejoindrait S. Pour Neon, cette règle tient au moins tant qu'il juge les ancres du bras A ; sinon il deviendrait source d'un mode (avis sur Neon, 2.2, point 1).
3. Si une réponse de Neon propose que le juge du recouvrement soit Neon, ou un modèle qui tient déjà un siège de juge, la proposition passe par un nœud de Lazar : lire S ferait de ce juge un lecteur du mode tenu à l'écart, ce que l'avis sur Neon n'a pas examiné.
4. Le relevé des rôles de Neon (avis sur Neon, condition 5) reçoit une ligne pour cet envoi : date, identifiant servi, empreinte de la question.

## 4. Ce que je n'ai pas vérifié

- Si les ancres du bras A sont déjà jugées : à constater par la mère, sans effet sur ce verdict.
- Les conditions d'envoi chez Google (offre payante, entrées non utilisées pour l'entraînement) : non constatées par moi.
- Je n'ai pas lu le mode tenu à l'écart : je ne peux pas exclure qu'un mot générique de la question (« nuire en cachette à la tâche ») soit plus proche de S que je ne le crois ; je le juge générique au point de ne rien désigner.
