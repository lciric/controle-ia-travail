# Protocole du croisement « conception de l'organisme » : analyse de conv-audit contre tour du collisionneur — v1 (gelé avant toute sortie)

Session conv-audit (Claude), 3 novembre 2026, vers 10:40 UTC (`date -u`). Mot de Lazar (11:26, heure de Paris) : « … qu'il fasse la même analyse, recos etc. et on croisera avec toi avant d'envoyer la course d'idéation sur le prompt final fusionné ». **Aucune sortie n'existe au gel** : le tour n'a pas tourné.

## 1. Entrées
- **Source conv-audit** : `analyse-conv-audit-conception-organisme-v1.md` (`01608648…`), gelée à 10:29 UTC, avant l'écriture de la question servie.
- **Sources du collisionneur** : les cellules du tour (conception, critique croisée, réponse, par espèce), sur la question `question-collisionneur-conception-organisme-v1.md`, scellées par session-depot avant toute lecture et copiées à l'octet ; liste de copie vérifiée avant lecture. Version d'une espèce : la plus récente (réponse si elle révise, sinon conception) ; critiques et réponses jointes aux éléments qu'elles visent. Une espèce absente est déclarée.

## 2. Lecteur neuf X (n'a écrit ni la question, ni les pièces, ni l'analyse de conv-audit)
- **Aveugle aux provenances autant que possible** : le directeur lui sert les six sources sous des identifiants opaques (`S-1` à `S-6`, ordre permuté par `numpy.random.SeedSequence`, graine tirée de l'empreinte de la liste de copie), **en-têtes et provenances retirés**, lettres d'espèce remplacées ; la clé reste au directeur.
- **Éléments** : chaque source est découpée en éléments, chacun rangé dans une rubrique : (1) ce que ferait l'expert ; (2) données brutes ; (3) méthodes et outils ; (4) vérification extérieure ; (R) demande reformulée ; (D) recommandation ou décision ; (E) première expérience ; (F) cause d'échec du plan.
- **Dédoublonnage par structure** : deux éléments sont un seul s'ils proposent la même action sur le même objet avec la même mesure, quels que soient les mots ; l'élément fusionné garde la liste de ses sources (dans la clé).
- **Statuts** : *accord* (au moins deux sources, dans leurs versions de conception, sans que l'une reprenne l'autre) ; *né de la critique* (accord apparu seulement dans les réponses) ; *apport seul* ; *divergence* (positions incompatibles, chacune avec ses sources) ; *objection* (sourcée : une pièce et sa section ; non sourcée sinon) ; *réfuté* seulement si une pièce citée contredit l'élément, ou s'il se contredit lui-même — **jamais par accord ou désaccord de sources**. Tout le reste est gardé.
- **Chiffres** : tout chiffre d'un élément est vérifié sur la pièce qu'il cite ; un chiffre sans source est marqué « non vérifié », jamais corrigé par le lecteur.

## 3. Le prompt fusionné (proposé par X, décidé par Lazar)
- Il prend **tous les éléments gardés** des rubriques (1) à (4), (R) et (E), sans en écarter un parce qu'il est seul ; une divergence n'est pas tranchée par X : elle devient une **décision pour Lazar** (options, sources, ce qui la ferait trancher).
- Il garde la forme de la demande de Lazar (« version plus approfondie, pas plus longue ») : une demande reformulée d'un paragraphe, puis ses annexes (éléments par rubrique, décisions ouvertes).
- X écrit à part la **liste de ce que chaque source a seule** (par identifiant opaque) ; la clé n'est levée qu'après, par le directeur, pour le rapport à Lazar.

## 4. Après le croisement
Le directeur lève la clé, rapporte à Lazar (accords, apports seuls par source nommée, divergences en décisions), et ne lance la course de l'organisme sur le prompt final qu'après la décision de Lazar, le prompt final scellé et la ligne de GO inscrite chez session-depot sur son mot direct.
