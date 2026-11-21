# Contre-lecture des changements de la v8 — pièce de sécurité du banc fermé — v7

- **Pièce relue** : `docs/notes/piece-securite-banc-ferme-v1/piece-securite-banc-ferme-v8.md`, branche `claude/piece-securite-banc-ferme-v1`, commit `556c6491cd8a60f056f8cd38b7bce54ff4c436f2`. Empreinte recalculée : `668bd2a734a2065f06a81ab20754ceef8221b259058ecd42a7d246c95b425d15`, égale au `.sha256`. Les v1 à v7 sont intactes, toutes recalculées.
- **Mandat** : GO-2026-11-21-76 (sur `main` au commit `ee0a8f5f`, ligne 675, lue). Contre-lecture des seules différences avec la v7, par la même contre-lectrice (Opus 5.5).
- **Nature du changement** : c'est un changement de fond. Il ouvre une voie qui envoie des contenus de quarantaine chez des fournisseurs de modèles extérieurs. Je l'ai donc relu comme une pièce neuve de classe A, sur ce qu'il ajoute.
- **Date** : 21 novembre 2026, vers 19:05 UTC.

## Sources neuves contrôlées

- **[GO75]** : `registres/go.md` au commit `f3785230`. Empreinte recalculée `d77f5675…`, égale à celle que cite la pièce. Seule la ligne 674 a été lue. Elle porte : « Banc fermé : lecteurs du dommage confiés aux lecteurs externes du monteur de l'oracle (écart à N-060 v3 point 1) : « go » ». C'est fidèlement repris.
- **[ML3]** : la note du mot de Lazar sur la v8, au commit `559cbb57`. Empreinte recalculée `1b750a1c…`, égale à son compagnon. Je n'en ai lu que les lignes 1 à 12, celles qui disent le mot, son objet et son exécution. Le mot verbatim, « go reco b, pièce de sécurité v8 », est conforme.
- **GO-2026-11-21-76** : il inscrit maintenant [ML3] au registre (`main`, commit `ee0a8f5f`, ligne 675). La réserve 12 et la ligne d'arrêt « mot de [ML3] non lisible au registre » sont donc dépassées depuis l'écriture de la v8 ; voir le point M5.
- **[PC]** : le brouillon 4 du préenregistrement de la course. Je ne l'ai **pas** ouvert. La v8 le cite comme brouillon non scellé, lu en partie, et je vérifie la pièce sans lui. Les renvois au champ n° 18 et au point 7 du déroulement sont pris comme l'auteur les rapporte (réserve 14).

## Ce qui est juste

- **La voie est bornée.** Seul le produit extrait part, dans une enveloppe à schéma fermé, un produit par appel. La consigne, le lot, la table des conditions, le journal, les états du monde, les transcriptions et les activations ne partent jamais.
- **Les clés restent chez l'envoyeur.** Elles ne vont ni sur le banc ni sur le poste de transit, et l'envoyeur n'a pas la table des conditions.
- **Chaque appel est journalisé avant de partir.** Une seule réponse par produit et par lecteur ; les réponses reviennent en quarantaine.
- **Un refus arrête.** Il n'y a ni reformulation, ni renvoi, ni remplacement du lecteur. C'est conforme à la liste d'arrêt de [PR] et à CLAUDE.md.
- **L'exception est nommée et ne fait pas précédent.** L'écart au sixième garde-fou de GO-2026-11-20-50 et à la liste d'arrêt des v4 à v7 est déclaré, et le reste demeure sous la revue externe. C'est la bonne lecture des deux mots de Lazar ; le point 1 de l'auteur tient.
- **Les gardes 14 à 17 s'éprouvent sans dépense**, contre un faux fournisseur local, chacune sur un cas sain et un artefact (R5). Le constat des réglages par un appel anodin est une dépense, sur GO.
- **Le reste n'est pas atténué.** La pièce dit qu'un envoi ne se rappelle pas, que la garde de fuite ne voit que le recouvrement littéral (réserve 15, point 2 de l'auteur) et qu'un repli est écrit vers les deux juges.
- **Aucun contenu d'attaque.** Aucun refus de classifieur.

## Points

### Bloquant

**B3 — Le quatrième trait de la section 6.4 n'est ni établi ni gardé.**
La v8 tient la voie pour « une lecture et non un partage » par quatre traits, et dit que si l'un tombe, elle redevient un partage et attend la revue externe. Le troisième de ces traits est que « rien n'est rendu lisible à une personne hors du programme » ; c'est le quatrième dans l'ordre que j'ai demandé de suivre. Or les conditions des fournisseurs de modèles prévoient couramment une conservation pour le contrôle des abus, avec une **revue humaine** possible des contenus signalés. Un produit écrit sous une consigne d'évasion, ou refusé par un classifieur, est le plus susceptible d'être signalé. La rubrique « Conservation » du champ n° 18 demande la durée, l'usage pour l'entraînement et les fonctions de garde. Elle ne demande pas si une personne du fournisseur peut lire l'envoi. Aucune garde ne le vérifie.

Correction demandée :
- ajouter au champ n° 18 une rubrique « Lecture humaine chez le fournisseur » (oui, non, ou sous quelles conditions, par exemple contrôle des abus ou contenu signalé), établie sur le texte du fournisseur pour le type de compte employé ;
- ajouter le même constat à la garde 16 et au point 24 ;
- écrire la règle : si une lecture humaine est possible, le trait tombe et, à la lettre de 6.4, la voie attend la revue externe. Soit ce lecteur ne lit pas, soit c'est un nœud à Lazar, sans défaut à 48 heures ;
- le dire à la réserve 13. Si un fournisseur sans revue humaine possible n'existe pas pour un lecteur prévu, il faut le savoir avant d'écrire le code de l'envoi.

### Mineurs

**M8 — Les questions fermées de l'oracle partent avec le produit, sans garde.** La condition 1 interdit à l'enveloppe de nommer la condition ou la famille. Mais si les questions de l'oracle varient selon la condition, la famille ou le mode, elles portent elles-mêmes l'étiquette. Il faut ajouter à la condition 1, à la garde 14 et au point 25 : les questions sont les mêmes pour tous les produits d'un même lecteur, ou tirées d'une liste fermée scellée qui ne dépend pas de la condition. La garde vérifie par programme que la question appartient à cette liste. L'artefact d'épreuve : une question propre à une condition.

**M9 — La ligne d'arrêt de la voie se contredit sur le calendrier du vérificateur.** La deuxième ligne neuve de 4.2 exige, avant tout envoi, une « pièce du vérificateur sans « oui » aux points 24 à 30 ». Or la fin de 6.1 et l'ordre des gestes de 6.4 disent que les points 26, 29 et 30 se vérifient **après** les envois. Il faut écrire : avant tout envoi, le premier temps de la pièce du vérificateur répond « oui » aux points 24, 25, 27 et 28 ; avant la levée de l'embargo, le second temps répond « oui » aux points 26, 29 et 30, sinon embargo maintenu et nœud.

**M10 — Restes de comptes anciens.** La section 6.3, point 1, dit « les treize gardes de la section 4.1 forment la condition ». La réserve 11 compare encore douze et treize. La pièce en compte dix-sept depuis la v8. Dans 6.3, écrire « les gardes de la section 4.1 (treize à la décision du 21 novembre, dix-sept depuis la v8, toutes exigées) ». Mettre la réserve 11 à jour ; il faut aussi une confirmation de la mère que GO-2026-11-21-71 vaut pour les dix-sept. La section 6.2 peut rester telle quelle, puisqu'elle décrit un état passé et se dit tel (point 4 de l'auteur).

**M11 — Contrôle avant envoi par un lecteur déjà admis.** Le reste du risque 13, ce qu'un produit laisse voir du mode sans en reprendre les mots, n'est « mesuré par personne avant l'envoi ». Un lecteur déjà inscrit au registre des accès, comme le juge, pourrait poser une question fermée sur chaque produit avant son départ : « ce produit, lu seul, apprend-il un procédé ? ». La pièce doit dire si cette option est retenue ou écartée, et pourquoi. Une raison valable de l'écarter : ce contrôle contaminerait la mesure du premier temps de [PC]. Ce n'est pas bloquant : la pièce nomme honnêtement ce reste, et c'est un choix de procédure.

**M12 — Registre dépassé.** GO-2026-11-21-76 inscrit [ML3] sur `main`. La réserve 12, la ligne de l'en-tête « ligne du registre attendue », la première condition de la ligne d'arrêt de la voie et l'ordre des gestes de 6.4 sont à mettre à jour. [ML3] est à citer par GO-2026-11-21-76.

## Le reste des points que l'auteur signale

- **Point 3** (numérotation 24 à 30, le point 23 restant la conclusion) : accepté. Aucun renvoi n'est déplacé.
- **Point 5** (trois recommandations à confiance 0,7) : elles sont justes et bien données comme hors décision. Le repli vers les deux juges est bien dit être un nœud, et non un geste de l'opérateur.

## Verdict

**À corriger** : un point bloquant (B3) et cinq mineurs (M8 à M12). Le reste de la voie d'envoi est solidement écrit. Une v9 qui ne corrige que ces points sera vérifiée sur sa seule différence (`verification-des-corrections-v8.md`).

**Refus de classifieur** : aucun.
