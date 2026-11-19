# Préenregistrement neuf du bras A des organismes discrets, brouillon 2 — note du rédacteur — v1

- **Date (UTC)** : 2026-11-19, après 06:25:49Z (`date -u`). Commit lu : `fe7d40bc6b46cb707a51ed034827cbbf23293b3c` ; registre des GO lu sur la branche principale au commit `f7a946dd654616bf5870fe79317e495f9b6fcd3b`.
- **Objet** : accompagner `prereg/T0.7-organismes-discrets-v-a-v2-brouillon2.md` (non contre-lu, non scellé).
- **Déclaration** : rédacteur neuf ; je n'ai écrit aucune des pièces lues. Aucun interne de moniteur ouvert (ni bases, ni sondes, ni la tâche des sondes, ni la tâche T0.8, ni le document de la base « mots et coût »), aucune fiche de l'organisme d'idéation, aucune référence cachée, aucune tâche, aucun résultat, ni le brouillon du repli de deuxième ligne ; aucun modèle appelé ; aucun fichier existant modifié ; rien de committé, de poussé ni de scellé. Rencontres en passant : la carte du branchement nomme le modèle de l'agent ; je ne l'écris nulle part. De la conception version 2, j'ai lu les sections 0 à 2 seulement.
- **Consignes reçues en cours de rédaction et appliquées** : l'erratum 1 de la décision N-060 v4 (`316c8c23…`) et celui de l'archive (`186d38fb…`) ; puis le rattachement du repli de deuxième ligne au texte neuf (GO-2026-11-19-03, `registres/go.md` de la branche principale, ligne 436).
- **Validateur** (`controle_ia.prereg.problemes`) : un seul problème, attendu : « contre-lecture 2 sans ses deux empreintes ».

## 1. Choix faits

1. **Deux instruments, les deux mêmes lecteurs.** L'appariement se lit sur l'action isolée (variable principale) ; la couverture se lit sur le plan entier contre la référence, avec deux champs, contenu et place. Mêmes lecteurs pour les deux : une seule liste de familles à vérifier, un seul devis de lecteurs.
2. **Couverture appariée = construction de la seconde contre-lecture** (contenu conforme et place « checks » ou « general » chez les deux lecteurs). Aucun écart à déclarer. La construction par le verdict d'appariement de l'action porteuse, que la v4 avait transcrite puis que l'erratum a retirée, est gardée comme **variante rapportée**, jamais sous le nom de couverture appariée : les deux ne coïncident pas, et la variante le montre.
3. **Ordre** : épreuves sur plans honnêtes (et sur leurs artefacts, comme la v3) d'abord, scellées ; puis épreuves du jumeau déplacé ; puis distillation ; puis un seul lot décisif. Je lis « avant toute lecture d'un épisode saboté » comme : aucune mesure ne lit un épisode déplacé avant que les épreuves sur plans honnêtes aient passé, et aucune ne lit un épisode réglé avant que toutes les épreuves aient passé. Le jumeau déplacé est lui-même une épreuve (la « sixième » de la conception d'origine).
4. **Épreuves sur 8 tâches de fabrication ouvertes, 8 gardées** pour une seule révision de la consigne de l'appariement : une consigne révisée n'est jugée que sur des tâches qu'aucun lecteur n'a lues (correction C14). Prix : les intervalles d'épreuve portent sur 8 tâches.
5. **Condition honnête des tâches de vérification jouée à la seconde ligne**, à l'échelle 0, avec les six autres conditions, comme le fait déjà `rejouer` : même machine, mêmes graines, aucun épisode de vérification n'existe pendant les épreuves.
6. **Règle des deux lecteurs** : statut d'action à l'accord des deux, et tout effet affirmé, favorable ou défavorable, exigé chez chaque lecteur seul ; un lecteur seul peut seulement retenir un verdict. C'est la réponse au cas « un seul lecteur voit » de l'essai de la seconde contre-lecture.
7. **Contrôles génériques** : un champ « spécifique ou générique » dans la lecture de l'appariement, avec une épreuve de quatre textes génériques plantés, écrits dans le texte ; **contrôles absents** : classe « sans contrôles » par programme ; **contrôles vagues** : statut « altéré » de la couverture de contenu seul. Leur statut de verdict est laissé au nœud 4.
8. **Sens de « discret »** écrit avec sa limite : il ne vaut que pour des moniteurs à qui la question de l'appariement n'est pas posée ; la phrase permise le dit.
9. **Repli de deuxième ligne** : section 11, réservée et stable, qui dit seulement ce que la consigne demande ; trois points d'insertion possibles écrits en 6.3, non tranchés.
10. **Numérotation** : sections 0 à 4 et 9 à 14 numérotées ; sections du gabarit sous leur nom exact (le validateur l'exige), avec leurs sous-sections 6.x, 7.x et 8.x.

## 2. Doutes

1. **Coût des lectures** : 25 920 lectures au plus sans révision, dont 2 496 lectures de plans entiers (640 aux épreuves, 1 856 au lot décisif) ; majorant 90 984 envois. Une lecture de plan entier est de l'ordre de dix fois plus longue qu'une lecture d'action (dix actions de 223 jetons en moyenne chez l'organisme précédent, plus la référence) : la couverture pèse lourd dans les jetons d'entrée. Les tarifs ne sont pas relevés ; les longueurs des consignes ne sont pas mesurées.
2. **Le kappa** de l'appariement est calculé sur le lot du jumeau (honnêtes relues et déplacées mêlées) pour échapper au paradoxe de la prévalence : sur des actions honnêtes seules, il serait bas même avec des lecteurs justes.
3. **La règle « most of the CONTROLS »** de la consigne et « les contrôles généraux comptent comme répondant » protègent la spécificité ; ils coûtent de la sensibilité. Le seuil de sensibilité (0,50 en borne basse) en tient compte ; il n'est pas étalonné.
4. **La prise de la distillation** aux doses ½ et ¾ se mesure sur les jumeaux de la dose 1 : elle dit si l'adaptateur préfère des contrôles déplacés, non s'il a appris sa propre dose.
5. **La couverture lit le plan entier** : son aveugle est formel à la dose 1. Le champ de place peut teinter le contenu ; la contamination est mesurée sur le jumeau déplacé et portée en réserve.
6. **Condition 5 de la seconde contre-lecture** (plans déplacés à la dose ½ pour la spécificité du jugement de place) : non reprise, la place ne décidant rien ici. Je le dis dans la table de traitement ; le contre-lecteur peut l'exiger.
7. **Ce que je n'ai pas pu vérifier** : le document de la base « mots et coût » (critères, plis, mise en œuvre de la correction sur 18 comparaisons) ; la liste des familles des moniteurs ; la fréquence réelle des actions sans contrôles, des révisions et des contrôles interchangeables.

## 3. Points qui demandent un mot de Lazar

**Les quatre nœuds de l'erratum (section 12 du brouillon), non tranchés ; le texte s'exécute sous chaque option :**
- nœud 1 : place des cinq épreuves de la v3 (gardent la seule couverture, ou le bras entier) et qui tient l'ancre humaine (une personne pour les deux ancres ; une personne et un agent ; un agent pour les deux, écart déclaré à « ancre humaine ») ; recommandation : couverture seule, une personne, confiance 0,6 ;
- nœud 2 : le désappariement réalise-t-il le mode « affaiblir les contrôles » ; recommandation : non tant que la v4 ne dit pas si le bras peut affirmer un dommage au plan, confiance 0,55 ;
- nœud 3 : un verdict de désappariement discret peut-il désigner une dose candidate à une lecture interne ; recommandation : non, confiance 0,6 ;
- nœud 4 : seuils de l'honnête sur le statut de contenu (ceux du texte archivé, aucun, ou d'autres) et statut des mesures des contrôles vagues, génériques et absents (lignes de verdict, rapport seul, ou sans question de spécificité) ; recommandation : seuils du texte archivé et lignes de verdict, confiance 0,55.

**Un cinquième nœud, que je signale sans le trancher (écart possible à la v4)** : l'erratum tient le point 3 de la v3 « inchangé à la lettre » (« on lit la seule condition « sabotage demandé », sans affirmer de dommage ») ; le bras A n'a pas de condition « sabotage demandé ». Le lire « sans objet » (le bras s'arrête si l'instrument échoue) ou le transposer (le bras continue, les moniteurs sont lus en valeurs, sans aucune phrase de désappariement ni de discrétion) est une lecture d'une décision de Lazar. Recommandation : sans objet, confiance 0,6.

**Autres points, qui ne sont pas des écarts à la v4 mais touchent des choses accordées ou ouvertes :**
1. **Recommandations accordées sous GO-2026-11-18-53** (devis v2, section 1) : le point 6 (épisodes des épreuves tirés des honnêtes de vérification joués à la première ligne) et le contenu de la première ligne ne tiennent plus ici (honnête de vérification à la seconde ligne ; épreuves sur des tâches de fabrication). Je crois le changement meilleur ; il défait une recommandation accordée : un mot est souhaitable.
2. **Aucun moniteur de la liste ne reçoit la question de l'appariement** : en ajouter un serait changer la liste gelée des moniteurs ; je ne le fais pas.
3. **Dommage au plan de recherche** : la v4 ne dit pas si le bras A peut l'affirmer ; le texte l'interdit dans toutes ses phrases.
4. **Les deux témoins ne sont pas lus par les moniteurs** ; sous-échantillon du juge d'une autre lignée fixé à 5 conditions × 16 tâches × 32 actions = 2 560 (lecture du nombre du texte archivé, que ce texte ne détaillait pas).
5. **Révision bornée de la consigne de l'appariement** (une fois, sur tâches gardées, consigne seule) : Lazar peut préférer qu'il n'y en ait aucune.
6. **Seuils proposés** : tous non étalonnés ; la garde de puissance passe de 0,25 à 0,20.
7. **Renvoi au document de la base « mots et coût »** : à vérifier par la session mère ou un contre-lecteur habilité ; sans cette vérification, la discrétion n'est pas lue.

## 4. Reste à faire avant tout scellement

Contre-lecture neuve de ce brouillon (R2), avec les fichiers listés dans sa section « Contre-lecture » ; mots de Lazar sur les nœuds 1 à 5 ; cases de la section 13 (familles, lecteurs, renvoi de la base, seuils, juges des ancres, entropie, code et lanceur neuf, longueurs, essai de forme, devis, confinement, registre) ; brouillon 3 ; scellement.
