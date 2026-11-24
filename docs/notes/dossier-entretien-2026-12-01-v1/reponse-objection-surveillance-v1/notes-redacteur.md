# Notes du rédacteur — réponse à l'objection « surveillance peu prometteuse » (v1)

- 23 novembre 2026, 18:25 UTC (`date -u`). Rédacteur : Claude Fable 5.2, effort élevé. Travail repris après une interruption de quota ; les extractions de texte faites avant l'interruption ont été réemployées (mêmes fichiers, empreintes vérifiées au départ). Aucun commit, aucune dépense, aucun appel réseau, aucun contact. Rien n'est écrit hors de ce dossier du bloc-notes.

## Ce que j'ai vérifié, ce jour, sur les fichiers sources

- **Empreintes** (`sha256sum -c` sur les compagnons) : les deux PDF et les deux pages web ; la lecture des trois sources, la note v6, la carte v2 et son erratum 1 ; les décisions N-053, N-056, N-062, N-075 v3 et ses errata 1, 2 et 3 v2, N-076 et son erratum 1. Toutes conformes. Le programme v2 : empreinte égale à celle de `docs/sha256sums-lancement-v2.txt`.
- **Pagination** : aux pages citées (papier : 2, 9, 10 ; Gan et al. : 2, 7, 8, 10, 11, 24, 29, 37), le rang de la page dans le fichier égale le numéro imprimé.
- **13 chiffres** de la page, chacun retrouvé dans le texte tiré : 16 tâches, note de 1 à 10, quatre moniteurs, meilleur de cinq, 1,5 à 3 fois (Gasteiger et al.) ; trois modèles, 31 personnes, 9 dépôts, 11 sabotages, 0,77, 42 %, 0,68, deux heures (Gan et al.). **12 citations** en anglais, chacune recopiée du texte tiré. **7 extraits** de décisions et du programme. Table de vérification : 31 lignes, à la fin de la page.
- **Absences vérifiées par recherche** : « monitor » ne figure ni dans le fichier HTML brut du billet de Hebbar ni dans son texte tiré ; « probe » et « activation » ne figurent ni dans le texte tiré du billet de Hebbar ni dans celui de la page de Gasteiger et al. ; dans le papier, « monitor » ne revient qu'à la p. 2 et en bibliographie (p. 13, 14).

## Le raccourci corrigé

La note v6 (objection 1) et la lecture des trois sources (§ 2, « un modèle plus faible lit la transcription ») réduisent Gasteiger et al. à un moniteur faible. La page dit : « We use these same four models to monitor transcripts » (section « Setup »), dont le modèle du saboteur (Claude 3.5 Sonnet). Trois nuances gardées, pour ne pas tomber dans l'excès inverse :
- ce modèle « more clearly distinguishes the different models », mais sa courbe de détection « is only slightly better » ; « sépare mieux » se dit donc des modèles, non de la détection du sabotage ;
- le « performs decently » vaut pour la seconde partie (les justifications), que les auteurs disent « preliminary » ;
- la conclusion d'ensemble des auteurs reste « very low recall ».
J'écris « dits plus faibles » pour les trois autres : les auteurs écrivent « we use weaker models as monitors », mais notent aussi que Claude 3.5 Haiku est « on par » avec le saboteur sur ces tâches (section « Mitigations »).
La lecture des trois sources porte le même raccourci (§ 2, première puce) : un erratum serait à prévoir ; je n'y ai pas touché.

## Ce que je n'ai pas pu vérifier, ou pas vérifié

- **Taylor et al. 2025** : hors de ma liste de sources. « Sondes essayées, tâches à réponse claire, résultats mêlés » est repris de la note v6 (phrase 1, objection 3) et dit comme tel dans la page. Seul fait vérifié par moi : le papier les cite p. 9.
- **« Aucune mesure publiée de sonde sur une tâche difficile à noter »** : repris de la note v6 (huit requêtes du concepteur, trois titres restant à lire, d'après son § 4). Je n'ai fait aucune recherche. La page écrit « non trouvé », une question.
- **« Ni chez nous »** (objection 1, gardé de la v6) : je n'ai ouvert aucun résultat du programme ; je ne peux ni le confirmer ni l'infirmer.
- **Les figures** des trois sources : lues par leurs légendes seulement. Gasteiger et al. ne donnent aucun rappel chiffré dans le texte ; la page l'écrit (« en courbes, sans chiffre ») et n'en invente pas.
- **Changement de titre** de 2604.16286 (« Auditing Sabotage Bench » dans le PDF, « ASMR-Bench » dans la bibliographie du papier) : constaté, non expliqué ; sans effet sur la page.
- Des décisions, je n'ai lu que les sections citées (N-053 en entier ; N-056, « Ce que cela fixe » ; N-062, « Ce que la décision fixe » et la suite ; N-075 v3, § 2 et 3, errata 1 et 2, erratum 3 v2, en-tête et § 4 ; N-076, § 2 et 9, erratum 1). Du programme : lignes 40 à 46 et 90 à 96, et une recherche de mots sur les sondes.

## Cloisonnement

Rien d'ouvert sous `docs/verdicts/`, `runs/`, `diag/`, ni sorties de course. La décision N-056 (point 5) nomme en passant « les sondes figées de P3 » : c'est une mention dans un texte de décision, sans résultat ; je n'en ai rien tiré. Aucune phrase de la page ne porte un résultat du programme ; là où la phrase en demanderait un, elle dit qu'il n'est pas cité.

## Choix

1. **Longueur** : 799 mots entre les deux repères de la page, table comprise (mots portant une lettre ou un chiffre) ; l'en-tête et la table de vérification sont hors de la page.
2. **Une table pour les trois sources**, puis un court paragraphe pour ce que la table ne peut pas porter (le saboteur comme moniteur ; aucune lecture des états internes).
3. **Le chiffre de la sonde auditée chez Gan et al. (p. 24) n'est pas donné** : la note v6 (§ 4) interdit de le dire sans quatre réserves, et une page n'a pas la place de les porter.
4. **La p. 9** est citée pour deux faits (Wen et al., détection ; Taylor et al., cités). **La p. 10** (voies « promising » qui sont des formes de surveillance de texte, selon la carte v2) n'est pas dans la page : lecture un peu interprétative (« also look promising »), laissée à la carte.
5. **Le détecteur de sous-rendement du papier** (p. 6, 25-26) entre dans la page : c'est son expérience la plus proche de la surveillance, et c'est elle qui fixe l'exigence de réattaque. J'écris « la plus proche », non « la seule », faute d'avoir relu les 84 pages.
6. **« La garantie vient d'un audit au hasard »** est toujours suivie de « là où son oracle reconnaît le dommage » (note v6, § 4 : ne pas dire que l'audit borne le dommage sans cette condition).
7. **Phrase de fin** : « mon programme doit le mesurer », non « je mesure » ni « je veux mesurer contre leur attaque refaite » : la première forme dirait une mesure en cours, la seconde dépend d'un mot de Lazar (note v6, phrase 4). « Contre un attaquant informé » renvoie au bras d'attaque décidé (N-056, point 6).
8. **Dans l'objection 1**, une précision au-delà de la correction demandée : « trop faible pour détecter (Gasteiger et al.) ou pour incriminer (Gan et al.) », au lieu de « trop faible pour incriminer » pour les deux. La v6 la donnait déjà en marge de sa phrase 10. À retirer si Lazar veut la correction stricte.
9. **Identifiants** (N-053, H1, etc.) : toujours après le nom en clair.

## À porter à la mère

- La lecture des trois sources v1 (§ 2) porte le même raccourci sur Gasteiger et al. que la note v6.
- La note v6, phrase 10 et phrase 1, ne sont pas touchées ; elles restent compatibles avec la page.
