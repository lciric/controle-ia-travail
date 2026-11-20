# Contre-lecture de l'additif 2 v4 (recréation des relances tombées avant leur marche)

Pièces :
- additif v4 : sha256 307255c2902d65dcb7ad963acd767807a317420af7425c9f17158b086e2367f7 (vérifiée) ;
- différentiel v3 → v4 : sha256 a0e5b8a62d2241333977f27ed69a7286be605c595c5cc6c0ad3bd72e034581cc (vérifiée ; refait par `diff -u`, il est fidèle) ;
- v3 de départ : 82829c2a…455b.

Faits tenus pour vrais : ceux qu'atteste la mère.

**Verdict : scellable après ces couples.** Aucun n'est bloquant ; quatre sont importants. Les questions de la mère sont tranchées dans les couples 1, 2, 3 et 4. La vérification du code de lecture figé est à la fin.

## Couples

**1. Le calcul de 198,34 dollars n'est pas une borne haute. La règle, elle, est juste.**
- Constat. Ce que le calcul compte est juste : 22,34 + 43 + 104 + 29 = 198,34. Mais il omet trois dépenses qui viendront :
  - celle des premières tentatives 2, 3 et 4 entre 15:18Z et leur arrêt, puis pendant le versement final ;
  - le stockage des premières tentatives arrêtées mais non détruites, jusqu'à leur destruction, qui attend le mot de Lazar vers 00:45Z ;
  - la dépense de la première tentative 1 depuis 15:18Z.

  Le texte le reconnaît lui-même (« en sens inverse… »). Avec 1,66 dollar de marge, environ 1 dollar par tentative suffit à rendre la quatrième recréation impossible. La règle, relever avant chaque recréation, reste conservatrice et juste. C'est l'étiquette « borne haute » qui est fausse, et elle peut faire croire à Lazar que quatre recréations tiennent.
- Correction. Remplacer « Borne haute, en comptant… » par « Estimation au relevé de 15:18Z ; ce n'est pas une borne haute : elle omet la dépense des premières tentatives 2, 3 et 4 jusqu'à leur arrêt et le stockage des premières tentatives jusqu'à leur destruction. La quatrième recréation (instance 4) est donc probablement un nœud ; seul le relevé fait avant chaque recréation décide. » Dans la règle, ajouter à la somme : « pour chaque première tentative arrêtée et non détruite, son stockage jusqu'à l'heure prévue de sa destruction ».
- Gravité : important.

**2. Une relance muette au-delà de la borne de 3600 secondes : rien n'est dit, et le muet est ambigu.**
- Constat. La condition 1 attend un arrêt écrit par l'amorce. Or les relances 2, 3 et 4 n'ont rien écrit depuis le clonage, et deux cas restent ouverts :
  - **amorce bloquée hors de sa minuterie**, par exemple dans une entrée-sortie réseau : aucun arrêt ne sera jamais écrit. L'instance dépense alors jusqu'à sa minuterie, ce qui ruine la réserve, et elle tombe dans les nœuds (« l'arrêt d'une relance qui n'est pas tombée d'elle-même ») ;
  - **réseau de l'hôte coupé** : les lignes « B5F » peuvent aussi ne plus remonter jusqu'à la session. « Aucune ligne » ne prouve alors ni l'absence d'arrêt, ni l'absence de « marche : début ».

  Le plan range déjà « garde d'instance » et « échéance atteinte » parmi les causes qui ne lisent aucune sortie.
- Correction. Ajouter à la condition 1 : « ou bien, au clonage plus 3600 secondes plus 15 minutes, l'instance n'a écrit aucune ligne « B5F » neuve : la session l'arrête par son identifiant au titre de la garde d'instance (cause du plan), ce qui n'est pas un arrêt sur présomption mais une échéance mécanique ». À la condition 2, ajouter : « et l'inventaire du disque (pas 2 ; noms et tailles seulement) ne montre aucun dossier de famille ni aucune sortie sous le dossier de la marche ; sinon, nœud ». Dans la section 1, remplacer « Elles sont encore dans l'installation des paquets » par « leur état n'est pas connu ».
- Gravité : important.

**3. L'exclusion de la machine touche le texte scellé, et l'additif cite un passage qui n'y est pas.**
- Constat.
  - Le texte dit : « crée autant d'instances qu'il y a d'offres acceptées par la garde du code, dans l'ordre… ». Retirer des offres que la garde accepte crée moins d'instances que le texte ne le prescrit. C'est donc un écart au texte, et pas seulement au plan de marche. L'écart est restrictif : il ne desserre aucune borne du devis, et il ne lit que le marché (`machine_id`) et un fait d'exploitation, sans aucune sortie. Il est donc compatible avec la règle mécanique et avec le point 12.
  - Mais la table de la section 3 attribue « aucune autre préférence » au « plan », c'est-à-dire au texte scellé. Cette phrase est dans le plan de marche v1 de la session, point 1.3, qui n'est pas un texte que l'additif modifie. Un texte scellé porterait ainsi une citation fausse.
- Correction.
  - Dans la table, remplacer la colonne de gauche par « plan, lancement au fil des offres : « crée autant d'instances qu'il y a d'offres acceptées par la garde du code » ». Remplacer la colonne de droite par « pour les seules recréations : sont retirées de la recherche les offres de la machine d'une relance tombée ; écart restrictif, aucune borne du devis desserrée ».
  - Dans la section 2, remplacer « Le choix de l'offre, tel que le relaie la session mère, ne connaît « aucune autre préférence » » par « Le texte crée autant d'instances qu'il y a d'offres acceptées par la garde du code (le plan de marche de la session, point 1.3, ajoute « aucune autre préférence » ; il est retouché en conséquence par la session) ».
  - Dans l'en-tête, retirer la phrase sur « aucune autre préférence ».
- Gravité : important.

**4. L'ordre des recréations.**
- Constat. L'ordre 1, 2, 3, 4, puis 5, puis 7 suit l'ordre des coupes du plan. Couper d'abord la troisième famille d'apprentissage (l'instance 7), puis l'instance 5, garde 1 à 4 en priorité : l'ordre est juste. Mais les relances ne tombent pas en même temps, et un ordre strict ferait attendre une relance tombée derrière une autre qui ne l'est pas encore. L'arrêt peut ne venir que bien plus tard (couple 2), et on ne sait pas si la suivante attend. Par ailleurs, « celle-ci et les autres sont un nœud » est prudent, même quand une recréation à 17 dollars tiendrait. C'est voulu, et Lazar tranche.
- Correction. Écrire « Les recréations dont les trois conditions sont remplies au même relevé partent une à une dans l'ordre du plan (1, 2, 3, 4, 5, 7). Une relance dont l'état n'est pas encore tranché ne retient pas les suivantes, mais sa coupure entière est comptée dans la réserve tant qu'elle peut encore être recréée. »
- Gravité : important. Sans cette phrase, une relance non tranchée peut à la fois bloquer les autres et sortir de la réserve.

**5. Les arrêts admis à la condition 1 ne renvoient pas au code.**
- Constat. Les quatre libellés (« clonage », « extraction partielle », « installation des paquets », « descente du modèle ») ne renvoient à aucune ligne de l'amorce. Un libellé un peu différent ferait d'une chute légitime un nœud : c'est sans danger, mais coûteux en temps. Par ailleurs, « installation des paquets » peut aussi échouer d'une manière déterministe, et ne serait alors pas réseau.
- Correction.
  - Citer chaque libellé avec sa ligne dans `scripts/amorce_b5f_formation_v1.sh`, au commit `4bdf0d22…`, relevée par qui a lu l'amorce.
  - Ajouter : « l'arrêt tient au réseau ou à l'hôte si la même étape a passé sur une relance d'une autre machine (ici 5 et 7, essais passés) ; sinon, nœud ».
- Gravité : mineur.

**6. Le plancher est mal cité.**
- Constat. « son plancher de huit familles tenues à l'écart (sous ce plancher : nœud) » ne reprend pas tout le plancher du plan. Le plan, à la coupe 4, dit : « huit familles tenues à l'écart et deux familles d'apprentissage, toutes à trois membres, 30 adaptateurs, dix tirages ». À la coupe 5 : « sous le plancher : nœud 6 (niveau déclaré de 95 %) ».
- Correction. Citer ces deux phrases à la lettre.
- Gravité : mineur.

**7. Le stockage de la première tentative 1 jusqu'au mot de Lazar.**
- Constat. La première tentative 1 est arrêtée, mais elle n'est détruite qu'après le mot de Lazar. Son disque se paie jusque-là. C'est le même trou que dans le couple 1, pour une instance déjà arrêtée.
- Correction. Couverte par le couple 1 ; rien d'autre à écrire.
- Gravité : mineur.

## Vérification dans le code de lecture figé (`lecture-figee-neuve`, `lecture_v1._familles_formees`)

« Une seule marche `-x1` par instance » est exact. La fonction cherche, sous `donnees/` de la branche de la formation, les dossiers `*-b5f-formation-<n>-x1` dont le nom égale exactement `[0-9]{8}-[0-9]{6}-b5f-formation-<n>-x1`, et exige `len(marches) == 1`, sinon elle refuse. Une recréation sous un identifiant de marche neuf est donc lue si, et seulement si, aucun dossier de la première tentative n'entre sous ce nom dans la branche de la formation, ce que tiennent le pas 3 et la section 3. « -x2 » est refusé par les quatre voies déjà vérifiées pour la v1 : `instance_de`, `prefixe_de_copie`, `exiger_copie_lue` et `episodes_propres`.

## Points tenus sans constat
- Le mot unique de Lazar, qui accorde l'additif et les destructions futures selon la règle, est bien posé. Les pas 1 à 3 n'attendent pas ce mot.
- Une recréation au plus par relance ; mêmes noms, mêmes graines ; même commit de course ; aucun changement du code ni du registre. La coupure de l'instance 7 (17 dollars) est juste.
- La section 4 n'a changé que par « par exemple ».
