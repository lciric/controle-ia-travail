# Vérification des corrections — brouillon 16 du préenregistrement de la course du banc fermé — v1

- Vérificateur : Claude Opus 5.5, le contre-lecteur du brouillon 15 (R2, même contre-lecteur).
- Date (UTC, `date -u`) : 2026-11-22, 12:52.
- Pièces, empreintes recalculées : brouillon 16, `docs/notes/attaquant-informe-v1/course-brouillon16-v1/course-banc-ferme-v1-brouillon16.md`, `d0c767b377a5dfd6a8994ddb926a6d49e9103535e8bba12d688cfe69f7c2cf3f` ; brouillon 15, `7cca176bd6e76319c4847422496ff76d54aceaf8d1b43bc738b2f17b07febd16` ; demande, `…/course-brouillon16-v1/demande-brouillon16-remplacements-v1.md`, `2ac75bdade3e0580fed4c1f85eab122fcd26e6fe957357b21d3a05628ed0adf4` ; réponse de Fable, `…/course-brouillon16-v1/reponse-v1/relecture-fable-api.md`, `83371480a3358394f7fecde7ecd6897fb48460941e34c63dc72b7ac0401014fb` ; mon rapport, `…/course-brouillon15-v1/contre-lecture-brouillon15-v2.md`, `ca3069273bf0c5c662047a92f43ab6528b345176b3b6c504b3ed8ba2ee6fed10` ; `registres/go.md` au commit `050e5f398ff588c5bf1b7f3c2713100c2efdc3da`.

**Verdict : à corriger** (un majeur nouveau, sur le point 1 ; le reste est acquis ou mineur).

**Différence entre les brouillons 15 et 16** (`diff`) : quinze blocs, qui recouvrent les dix-neuf remplacements. Tous relèvent de la demande (les neuf points, le repère [GO85], la réserve 9, l'en-tête). Aucune hypothèse, aucun signe, aucun seuil, aucune valeur fixée d'avance ne change. La ligne d'arrêt de l'oracle hors gabarit est resserrée : les contrôles hors gabarit ne l'arrêtent plus. C'est l'application directe du mot du directeur, et non un écart.

## Point par point

| Point | Traitement de Fable | Vérification |
|---|---|---|
| 1, majeur, oracle hors gabarit | appliqué | La contradiction est levée en D6, dans la liste d'arrêt, en D8 et dans « Embargo ». Pour les trois choix de conception, voir plus bas : un reste majeur, le point nouveau A. |
| 2, majeur, repère [GO85] | appliqué autrement | **Acquis.** J'ai recalculé les trois valeurs : le commit `050e5f39…` existe ; le fichier y a l'empreinte `e6615990…` ; la ligne 684 est GO-2026-11-21-85 ; la ligne seule, fin de ligne comprise, a l'empreinte `92d95c09…`, la même à `d2333ca4`. Les deux repères sont vrais, à deux états. La phrase de renvoi global suffit. Reste mineur : la colonne dit encore « non recalculées » (point nouveau E). |
| 3, nœuds tranchés | appliqué autrement | **Acquis.** La réserve sur le gel est plus fidèle que « la même ». |
| 4, second dépôt | appliqué autrement | **Acquis.** L'addendum B, scellé avant la course, ne peut pas porter le second dépôt ; le registre le reçoit, ce qui est juste. Les bornes données (après le scellement des réponses, avant toute lecture par un moniteur) suffisent. |
| 5, [PR-3] | appliqué | acquis |
| 6, champs n° 13 et 19 | appliqué pour le n° 13 ; refusé pour le n° 19 | Le n° 13 est acquis. Le refus pour le n° 19 est conforme à mon rapport : c'est **à la mère de trancher**, et c'est encore à faire. |
| 7, auteur | appliqué | **Acquis.** Le doute est levé, et signalé à Lazar. |
| 8, date | appliqué | **Mineur résiduel.** « Vers 12:44 » est faux. Le fichier du brouillon 15 a été écrit à 12:42:22 et son compagnon à 12:42:39 (date du fichier sur disque) ; mon rapport, de 12:43, le suit. Écrire « vers 12:42 UTC ». |
| 9, verdict du brouillon 14 | appliqué autrement | **Acquis.** Le champ n° 20, « À REMPLIR (champ n° 20) », est dans la section « Contre-lecture » et dans la liste des champs d'avant scellement. Le validateur (`src/controle_ia/prereg.py`, `MARQUEUR = "À REMPLIR"`) le voit et refuse de sceller la section. |

## Les trois choix de conception du bloc 9

- **Le lieu du rapport** (fichier sous embargo, par condition, au schéma fermé) découle de la règle déjà écrite : tout agrégat par condition est sous embargo. Pas de nœud.
- **Le lanceur** (le monteur de l'oracle) découle de D8 : il est seul, hors du coffre, à tenir les produits extraits et les listes, et l'opérateur comme le juge en sont exclus par le texte. Pas de nœud, mais un mineur (point nouveau B).
- **Le sens de « à part »** (ni dans la métrique 3, ni dans l'accord, ni dans un critère gelé) suit la lettre du mot du directeur, puisque la métrique 3 est faite des réponses des lecteurs. Il laisse pourtant un cas ouvert, que Fable signale lui-même en réserve 2 (point nouveau A).

## Points nouveaux

- **A, majeur. D6, puce « Contrôles hors gabarit », et liste d'arrêt.** Le cas n'est pas écrit où la règle de réunion de l'oracle ne peut pas appliquer son seuil sans les contrôles hors gabarit. Le dommage tenu serait alors mesuré sur une partie des contrôles, sans que rien ne le dise : c'est un repli silencieux (R5). Correction : dans la puce et dans la ligne d'arrêt jumelle, écrire ce cas comme « rien ne part ; nœud pour Lazar » ; le monteur l'atteste, sans contenu, à l'addendum O. Un nœud n'est à ouvrir que si le cas se produit.
- **B, mineur. D6 (i) et D8.** Il n'est pas dit que le monteur ne lit pas les sorties du programme de jugement qu'il lance. Correction : « il ne les lit pas ; elles sont scellées en quarantaine ».
- **C, mineur. Déroulement, point 9 (« Agrégats »).** Ses entrées ne comprennent pas les sorties du jugement par programme, alors que D6 (ii) l'y renvoie. Correction : les ajouter à la liste des entrées.
- **D, mineur. Signalements à Lazar.** Deux choses sont dites « signalées à Lazar au scellement » sans figurer dans « Champs ouverts et nœuds » : les choix de conception du bloc 9 et l'auteur appelé à la demande de l'attaquant informé. Correction : une ligne « à signaler au scellement » qui les nomme.
- **E, mineur. Repère [GO85].** Il dit « non recalculées ». Correction : « recalculées par le vérificateur des corrections ».

## Ce que Fable a vu sans le corriger

- **Le commit de [GO85] et les heures** : réglés ci-dessus (point 2, et point 8 à corriger).
- **Les citations sans crochets** : la phrase de renvoi suffit, rien à faire.
- **Pas de numéro de métrique pour le rapport à part** : c'est voulu, puisque « à part » veut dire hors des métriques ; rien à faire. Le manifeste ne nomme pas le second dépôt : rien à faire, ce dépôt a lieu après la course.
- **La ligne d'arrêt de la seconde confirmation** (« points 8 et 21 »), alors que la condition 17 dit 8, 18 et 21, et que la ligne M3 de la contre-lecture 7 l'avait acceptée pour le point 18 : **à corriger avant le scellement**, sous un motif nommé « défaut ancien ».
- **« La même contre-lectrice »** dans le paragraphe d'état, alors que la vérification est faite par le même contre-lecteur : **à corriger avant le scellement**, c'est un mineur de forme.
- **La ligne M2 de la contre-lecture 6** est de l'historique : elle reste telle.
