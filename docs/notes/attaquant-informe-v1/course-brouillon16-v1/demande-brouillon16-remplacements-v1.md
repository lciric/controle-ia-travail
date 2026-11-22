# Demande à Fable 5.2 — brouillon 16 du préenregistrement de la course du banc fermé : corrections de la contre-lecture, en remplacements exacts

Tu as produit le brouillon 15 par 20 remplacements exacts appliqués au brouillon 14. La pièce « piece » jointe est le brouillon 15, avec les mêmes marques réversibles : ⟦D⟧ et ⟦d⟧ tiennent la place du nom du directeur, ⟦S1⟧ à ⟦S5⟧ celle d'identifiants de session, ⟦C1⟧ et ⟦C2⟧ celle de deux chemins que la course cite sans les lire. **Recopie ces marques telles quelles ; n'en invente aucune.** N'écris jamais « ⟦S?⟧ » : cette marque de la copie de la contre-lecture n'a pas de valeur et serait refusée.

Un contre-lecteur neuf (Opus 5.5) a rendu « à corriger » : aucun point bloquant, 2 majeurs et 7 mineurs. Son rapport est joint en remarques, ainsi que ta réponse précédente, avec ses sections « Vu et non corrigé » et « Réserves ».

## Ce que le brouillon 16 doit porter, et rien d'autre

1. **Les 9 points du rapport**, chacun appliqué, appliqué autrement ou refusé avec un motif. Pour le majeur 1, qui porte sur l'oracle hors gabarit :
   - le mot du directeur (GO-2026-11-21-85, option a, repli interne) dit : « contrôles hors gabarit jugés par programme sur la liste scellée, rapportés à part, jamais envoyés aux lecteurs externes » ;
   - le lieu du rapport « à part » et le lanceur du programme de jugement ne sont pas fixés par ce mot. Propose-les selon la logique déjà écrite du texte, et dis-le comme un choix de conception de l'auteur. Si aucun ne découle du texte sans un choix nouveau de fond, écris un nœud pour le directeur au lieu de trancher.
2. **Le repère du mot du directeur**, pour le majeur 2. Il entre dans la table « Documents qui font foi » sous le repère [GO85] : `registres/go.md` sur `main`, au commit `050e5f398ff588c5bf1b7f3c2713100c2efdc3da`, où la ligne est entrée. Ligne 684. Empreinte du fichier à ce commit : `e66159900ddc52529f115841f3866adc9437edc1bfeb5a1fcd74c5cf773ab634`. Empreinte de la seule ligne : `92d95c09c9f78f60a45a71d1d3d787f7538d8776b82da871b08fd6237c718cde`. Ces valeurs sont fournies par la session qui t'appelle, et non par le contre-lecteur. Fais pointer les citations de ce mot vers ce repère, là où cela ne demande qu'un renvoi.
3. **La réserve 9 de ta réponse précédente** (« six conditions » pour douze), sous un motif qui la nomme « défaut ancien du brouillon 14 ».
4. **L'en-tête** : « brouillon 16 » partout où le texte se désigne lui-même. La date du brouillon 15 est « 2026-11-22, vers 12:44 UTC ». Celle du brouillon 16 porte « [heure lue par date -u au scellement] ». Le paragraphe d'état dit ce que le brouillon 16 porte de neuf. La ligne « Auteur » lève le doute qu'a relevé le contre-lecteur : tu es appelé par l'interface d'Anthropic à la demande de la session de l'attaquant informé. Tu n'as lu ni le lot, ni les sorties, ni le coffre, et tu n'as conçu aucun moniteur. La ligne le dit, et le signale au directeur pour le scellement.

## Interdits

Ils sont les mêmes que la fois précédente :
- aucune hypothèse, aucun signe, aucun seuil, aucune valeur fixée d'avance, aucun critère gelé ne change ;
- aucun champ « À REMPLIR » n'est rempli ;
- niveau méthode seulement : aucun mode, aucune recette, aucun paramètre d'attaque, aucun nom de famille ;
- aucune autre correction : ce que tu vois de plus se signale à la fin, hors de la liste.

## Format

Il est le même, à la lettre. Pour chaque remplacement k (k = 1, 2, 3…, sans trou), une ligne « Motif k : … », qui renvoie au numéro du point du rapport ou au point 2, 3 ou 4 ci-dessus. Puis le bloc, dont les trois marqueurs occupent chacun une ligne entière, hors de tout bloc de code :

<<<ANCIEN k
texte exact du brouillon 15, qui n'y figure qu'une fois
===NOUVEAU k
texte de remplacement
>>>FIN k

Aucune ligne d'un texte ne commence par un marqueur. L'ancien texte recopie le brouillon 15 au caractère près.

Après le dernier bloc :
- « Table des corrections » : une ligne par point du rapport, avec « appliqué », « appliqué autrement » ou « refusé », le motif et les numéros de blocs ;
- « Vu et non corrigé » ;
- « Réserves » ;
- puis la ligne « FIN DE LA RÉPONSE ».
