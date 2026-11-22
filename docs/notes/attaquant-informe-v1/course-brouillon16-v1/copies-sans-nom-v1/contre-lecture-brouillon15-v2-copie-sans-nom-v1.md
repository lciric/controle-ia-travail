<!-- Copie servie, classe C : `docs/notes/attaquant-informe-v1/course-brouillon15-v1/contre-lecture-brouillon15-v2.md` (sha256 ca3069273bf0c5c662047a92f43ab6528b345176b3b6c504b3ed8ba2ee6fed10). Le nom du directeur est remplacé par ⟦D⟧ (⟦d⟧ en minuscule), les identifiants de session par ⟦S?⟧ ; rien d'autre n'est changé. -->

# Contre-lecture du brouillon 15 du préenregistrement de la course du banc fermé — v2

La v1 (`75d355a5bd222c0e7d8e63bb63fb5eb5abdcab5dd3d45d882347d332b99ce050`) dépassait la borne de 1 200 mots ; la v2 la raccourcit, sans changer ni verdict ni point.

- Contre-lecteur : Claude Opus 5.5, sous-agent neuf (R2), n'ayant écrit aucune version de la pièce.
- Date (UTC, `date -u`) : 2026-11-22, 12:43.
- Pièces lues, empreintes recalculées par `sha256sum` :
  - brouillon 15, `docs/notes/attaquant-informe-v1/course-brouillon15-v1/course-banc-ferme-v1-brouillon15.md` : `7cca176bd6e76319c4847422496ff76d54aceaf8d1b43bc738b2f17b07febd16` ;
  - brouillon 14, `origin/claude/prereg-course-banc-ferme-v1:prereg/course-banc-ferme-v1-brouillon14.md` : `4489d39957b7dba53d015521867c2d7cb56ee01a6d3e2070523b889555173784` ;
  - demande, `…/course-brouillon15-v1/demande-brouillon15-remplacements-v2.md` : `3f0915438d3b2dcf5d6dde18e4f9ca173b9eda714af2015d7575ed8087ea27bb` ;
  - réponse de Fable, `…/course-brouillon15-v1/reponse-v1/relecture-fable-api.md` : `5b7947e9b57874764a4dee96e3d45e3cd3104ccd470cd0922e5f5cbc1d2fef03` ;
  - additif 3, version 2, `…/additif-3-regle-bras-v1/reponse-v2/relecture-fable-api.md` : `5fbdef7c20213970cbf695ea02bd53bd303a427337107c3b594c8f43c8bda1f8` ;
  - son erratum 1, `…/additif-3-regle-bras-v1/additif-3-v2-erratum-1.md` : `bde08a2012735d7bdf634d849c1a44081aa62d5fcfb1a9d0681a9bbce5cddddb` ;
  - mot du directeur, `origin/main:registres/go.md`, ligne 684 seule (GO-2026-11-21-85), commit `d2333ca44891f094142529def2e500db3b5963ca`, fichier `63a046a9b83bb5d16df477c8386a46caa02916b2e5d9140d73f989f669302797`.

**Verdict : à corriger** (aucun bloquant, deux majeurs, sept mineurs).

## Ce qui a été vérifié et tient

- **Différence complète** (`diff` des deux brouillons) : quinze blocs de différence, qui recouvrent exactement les vingt remplacements de la table de Fable. Chacun relève d'un des six points. Aucune hypothèse, aucun signe, aucun seuil, aucune valeur fixée d'avance, aucun critère gelé ne change. Aucune marque ⟦…⟧ ne reste.
- **Point 7** : comparé par programme à la section 6 de l'additif. Il est identique au caractère près, sauf la parenthèse « (`[chemin]`, `[empreinte]`, à remplir au scellement) », remplie par le chemin et l'empreinte justes. C'est le remplissage attendu, non un écart. L'emplacement est le bon. Les renvois internes tiennent. L'erratum 1 ne touche pas la section 6.
- **Repère [PR-3]** : les chemins sont justes. Les deux empreintes, que j'ai recalculées, sont égales à celles du texte et des compagnons `.sha256`.
- **Nœuds 13 et 14** : portés en D6, dans « Dépôt daté chez un tiers », dans la ligne d'arrêt et dans la liste des nœuds, conformément au mot du directeur. Aucun passage hors des tables d'historique ne dit encore l'un de ces nœuds ouvert.
- **Champs** : tous les marqueurs « À REMPLIR (champ n° k) » sont gardés, et aucun champ n'est rempli.

## Points

1. **Majeur. D6, puce « Si l'oracle de la famille ne se ramène pas à ce gabarit… », et ligne d'arrêt jumelle (« L'oracle de la famille ne se ramène pas au gabarit… »).** Défaut : ces deux lieux disent encore « rien ne part ; nœud pour ⟦D⟧ », alors que la puce neuve dit les contrôles hors gabarit « décidé[s] par ⟦D⟧ ». On ne sait pas si un oracle hors gabarit arrête la course ou passe au repli interne. De plus, rien ne dit où se rapporte « à part » le jugement par programme : le schéma fermé de la garde 12 et la section « Embargo » n'ont pas de place pour lui. D8 ne dit pas non plus qui lance ce programme, ni où, alors qu'il lit la référence. Correction : dans la puce et dans la ligne d'arrêt, écrire que, pour les contrôles hors gabarit, le repli interne s'applique (GO-2026-11-21-85), et ne garder « rien ne part ; nœud » que pour le cas que la décision ne couvre pas (questions différentes entre jumeaux, si la mère confirme que la question posée au directeur ne le comprenait pas) ; nommer le fichier sous embargo comme lieu du rapport à part, en entiers et proportions par condition, conformes au schéma fermé ; dire dans D8 qui lance le programme, et où (par exemple le monteur de l'oracle, là où est la référence).
2. **Majeur. Table « Documents qui font foi ».** Défaut : GO-2026-11-21-85 est cité neuf fois sans repère, sans ligne et sans empreinte (R6), contre l'usage de [GO75] à [GO80]. Fable le signale en réserve 2. Correction : un repère [GO85] : `registres/go.md` sur `main` au commit `d2333ca44891f094142529def2e500db3b5963ca`, ligne 684, fichier `63a046a9b83bb5d16df477c8386a46caa02916b2e5d9140d73f989f669302797` (lues et calculées par moi). Les citations renvoient ensuite à [GO85].
3. **Mineur. Table « Nœuds tranchés ».** Défaut : les nœuds 13 et 14, décidés, n'y figurent pas, alors que les autres nœuds tranchés y sont. Correction : deux lignes, avec la décision, « ⟦D⟧, [GO85] » et la recommandation de l'auteur (« la même » pour les deux).
4. **Mineur. « Après la course, dans cet ordre » et addendum B.** Défaut : le second dépôt décidé n'est placé dans aucune liste ordonnée. Correction : l'insérer après le scellement des réponses des lecteurs et avant toute lecture par un moniteur, comme le dit le nœud 13, en geste de ⟦D⟧, avec son identifiant, sa date et son empreinte relue.
5. **Mineur. Repère [PR-3], colonne des empreintes.** Défaut : « dit scellé par la demande… non recalculées par l'auteur du brouillon 15 ». C'est désormais vérifié. Correction : « recalculées par le contre-lecteur du brouillon 15 ; compagnons `.sha256` présents et égaux ».
6. **Mineur. Champs de l'étalonnage, n° 13 et n° 19.** Jugement sur le champ n° 13 : il relève de l'étalonnage, mais indirectement. Le volume des activations dépend du champ n° 2 (pas, jetons, agents) et du devis, nommés au point 6 : la mention est défendable, mais moins exacte. Correction : « (attend l'étalonnage du saboteur à budget, par le champ n° 2 et le devis) ». Le champ n° 19 (poste de calage, « le poste sur lequel la campagne de calage de G1 tournera ») tient à la configuration du calage au moins autant : la mère doit trancher s'il reçoit la mention et l'écrire. Ailleurs, aucune mention ne manque.
7. **Mineur. En-tête, ligne « Auteur ».** Défaut : « Cela vaut pour les brouillons 1 à 14 » laisse entendre que l'indépendance de l'auteur à l'égard de l'attaquant informé ne vaut plus pour le brouillon 15, demandé par sa session. Correction : dire que l'appel à Fable n'est pas la session de l'attaquant informé, que cette session a écrit la demande et appliqué le programme sans rien rédiger, et le signaler au directeur au scellement (Fable, « Vu et non corrigé »).
8. **Mineur. En-tête, ligne « Date ».** Défaut : le brouillon 15 est déjà scellé avec la marque « [heure lue par date -u au scellement] » non remplie ; elle ne peut plus l'être (R12). Correction : la version suivante porte l'heure du brouillon 15, lue au manifeste ou au commit (la réponse de Fable est datée de 12:42:07Z).
9. **Mineur. Section « Contre-lecture », entrée du brouillon 14.** Défaut : « son chemin et son empreinte restent à porter ici » est un blanc sans marqueur, que le validateur ne verra pas. Correction : porter le chemin et l'empreinte du verdict « accepté sans reste » avant le scellement définitif, ou poser un marqueur.

## Ce que Fable a vu et non corrigé

- Oracle hors gabarit (trois lieux) : **à traiter avant le scellement**, voir le point 1.
- Second dépôt et « Nœuds tranchés » : points 4 et 3 ; la ligne M2 d'historique reste telle.
- Auteur demandé par l'attaquant informé : point 7 ; au directeur d'en juger, signalement au scellement.
- Réserve 9 (« les six conditions de D6 », qui en résume douze) : défaut ancien, hors des six points. À corriger dans la même version, sous un motif nommé dans la demande suivante, pour ne pas créer de différence hors liste.
- Commentaire de la copie et erratum 1 : rien à faire.
