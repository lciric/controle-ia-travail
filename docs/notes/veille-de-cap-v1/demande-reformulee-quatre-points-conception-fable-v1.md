# Veille de cap — les quatre points et la demande reformulée (conception par Fable, v1)

Écrit le 22 novembre 2026 à 15:00Z par la session fille de conception, **avant toute lecture du dépôt** : seuls étaient connus les consignes permanentes chargées à l'ouverture et le message de la session mère. Pièce de travail (classe C). Rien n'est mesuré ici.

## La demande du directeur, verbatim

« si je m'inspire du fonctionnement du cerveau humain et que je l'applique à notre programme, il faudrait vraiment avoir une session veille qui régulièrement boucle ce qu'on est en train de faire avec ce qui a été fait il y a longtemps genre une semaine deux semaines etc un mois deux mois, et c'est une boucle qui doit être informative, c'est-à-dire on vérifie qu'on ne dérive pas, qu'on réutilise bien surtout les idées et qu'on teste bien ce qu'on voulait faire, qu'on tient le cap etc, c'est une session fille qui doit répondre directement à la session mère et qui doit commit sur github très régulièrement afin de pouvoir tout retrouver en cas de changement de compte ou tout simplement parce que le temps a passé et qu'une bonne idée a été enterrée ou jamais testée ? je ne veux plus jamais avoir de bonnes idées oubliées et non testées ou abandonnées car test mal lu comme un échec. »

## 1. Ce qu'un expert ferait ici, et que tu ne demandes pas

Le domaine : la mémoire des organisations et la conduite de programmes de recherche (retours d'expérience, registres d'hypothèses, assurance de la qualité des essais).

1. **Séparer quatre oublis, qui n'ont pas le même remède.** (a) L'idée jamais consignée. (b) L'idée consignée et jamais relue. (c) L'idée « testée » par un essai qui n'a pas pu la juger, puis classée échec. (d) L'idée qui s'éteint sans que personne l'ait décidé. Ta demande nomme (b) et (c) ; (a) et (d) sont en général les plus nombreux, et une veille qui ne lit que des registres ne voit jamais (a).
2. **Exiger qu'un échec se prouve.** Un résultat négatif ne compte que si l'essai pouvait réussir : il a atteint la mesure, un témoin positif est passé, la puissance suffisait, le critère écrit d'avance a été appliqué. Sinon l'essai est « non évaluable » et l'idée reste « non testée ». C'est la règle des essais cliniques (sujet non évaluable) et des chaînes de construction logicielle (panne de l'infrastructure contre vrai rouge).
3. **Faire de l'abandon un acte.** Une liste fermée d'états ; l'état « abandonnée » exige une décision nommée, une raison codée et une condition de réveil (ce qui devrait changer pour rouvrir). Sans cela, l'idée est « en souffrance », et son âge se compte.
4. **Traiter la veille comme un instrument, donc l'éprouver** (ta règle R5 appliquée à elle-même) : sur un cas sain, sur un artefact, avec des idées plantées dont elle ignore la clé. Rappel, précision, délai de détection.
5. **Estimer ce qu'elle ne voit pas.** Deux extractions indépendantes de la même tranche de traces brutes ; leur recouvrement donne une estimation du nombre d'idées que ni l'une ni l'autre n'a vues (capture et recapture).
6. **Tenir la traçabilité dans les deux sens.** Chaque chantier actif renvoie à une hypothèse, une porte ou une décision (sinon : dérive). Chaque hypothèse revendiquée et chaque essai promis a un essai fait, daté, ou retiré par décision (sinon : négligence).
7. **Borner l'attention demandée.** Peu de signaux par cycle, classés, chacun finissant par une décision à prendre ; et suivre la part des signaux qui ont reçu une décision. Une veille qui signale tout est oubliée à son tour.
8. **Regarder en avant aussi.** Le « pré-mortem » (on suppose l'échec dans deux mois et on en écrit les causes) et la visite périodique des abandons quand les conditions ont changé (outil neuf, résultat neuf, budget neuf).
9. **Se méfier de sa source.** La veille lit des registres écrits par ceux qu'elle surveille : des données déjà interprétées. L'expert repart de traces que personne n'a résumées.

## 2. Les données brutes qu'il prendrait au départ

Au lieu de l'état vivant, des synthèses et du registre des idées déjà tenu (tous déjà analysés) :

- **l'historique git lui-même** : commits datés, différences, fichiers supprimés ou renommés, branches jamais fusionnées ;
- **les journaux de course et les manifestes** : codes de sortie, lignes d'erreur, durées, nombre d'enregistrements produits contre nombre prévu ;
- **les textes scellés pris par paires** : le préenregistrement (la promesse) contre le résultat et le verdict (la livraison) ;
- **le registre des GO, celui des dépenses et celui des arrêts** : un GO jamais consommé est un essai jamais lancé ; une dépense sans verdict est un essai jamais lu ; un arrêt dit pourquoi une course est morte ;
- **les passations dans l'ordre** : la « prochaine action » de l'une contre le « fait » de la suivante, pour voir les chaînes rompues ;
- **tes mots, verbatim, dans les transcriptions versées** : c'est là que naissent les idées et les intentions, avant toute reformulation ;
- **les sorties brutes des collisionneurs, de l'organisme d'idéation et des mentors** : les propositions elles-mêmes, pas les notes qui les résument.

## 3. Les méthodes et les outils

- **Un registre des idées à états fermés**, lisible par programme (une fiche par idée : énoncé verbatim, lieu et date de naissance avec empreinte, état, essais rattachés, décision, condition de réveil), et **un programme de contrôle** qui refuse le registre s'il viole un invariant (abandon sans décision, échec sans contrôle de validité, citation qui ne se retrouve pas au lieu cité).
- **Une liste de contrôle du « faux échec »**, appliquée à tout essai classé négatif : la course a-t-elle atteint la mesure ? témoin positif ? effectif réel contre effectif prévu ? fautes d'instrument dans le journal (authentification, plafond de sortie, troncature, délai dépassé) ? critère gelé appliqué ? Quatre issues seulement : négatif valide, non concluant, non évaluable, jamais lancé.
- **Une extraction par motifs** sur les traces brutes (« à faire », « on testera », « plus tard », « reporté », « piste », « échec », « erreur », « 401 »…) qui ne fait que proposer des candidats ; le jugement vient ensuite, par lecture.
- **Des fenêtres de retour à intervalles croissants** (une semaine, deux semaines, un mois, deux mois), comme la répétition espacée, plus une tranche ancienne tirée au sort à chaque cycle, comme le rejeu qui entrelace l'ancien et le neuf.
- **La double extraction avec estimateur de capture et recapture** (Chapman) pour chiffrer les idées manquées.
- **La matrice de traçabilité** (hypothèses, chantiers, essais, verdicts) et la liste des orphelins des deux côtés.
- **Le grand livre des promesses** : chaque « prochaine action », chaque « à faire » et chaque GO, avec son âge et sa condition d'échéance.
- **Le « pré-mortem » mensuel et le retour d'expérience** à la fermeture d'un chantier.
- Outils : `git log` et ses filtres, recherche par motifs, empreintes, un script du dépôt avec ses essais (pièce d'instrument, donc contre-lue par un autre modèle), une tâche planifiée pour la cadence.

## 4. Ce qui, hors de toi et de moi, vérifierait la validité

- **Des idées plantées à clé scellée.** Quelqu'un d'autre que la veille prépare des cas dont la réponse est connue : des enfouissements vrais du passé, retrouvés par une autre voie, et des promesses témoins réelles posées dans le flux. L'empreinte de la clé est déposée avant le cycle ; la clé reste hors de ce que la veille lit. On mesure le rappel et le délai.
- **Un audit à l'aveugle.** Un agent neuf d'un autre modèle, qui n'a pas vu le registre de la veille, refait l'extraction sur une tranche tirée au sort ; on compare, et l'estimateur chiffre le reste.
- **Des contrôles par programme, sans modèle.** Chaque citation du registre se retrouve mot pour mot au chemin et à l'empreinte cités ; chaque invariant tient ; les dates des commits prouvent la cadence.
- **Une épreuve à froid.** Une session neuve, d'un autre compte, avec le seul dépôt, doit retrouver une idée désignée en un temps borné.
- **L'issue elle-même.** Le nombre d'idées rouvertes par la veille dont le nouvel essai a changé le verdict (ce qu'elle rapporte), et le nombre d'enfouissements découverts plus tard par une autre voie (ce qui lui a échappé).
- **Ton œil, sur échantillon.** Cinq fiches tirées au sort par mois, dix minutes : l'énoncé est-il fidèle, l'état est-il juste ? Et, si tu le décides, un lecteur extérieur au programme.

## La demande reformulée

« Conçois pour le programme une fonction de mémoire et de tenue du cap dont la valeur se mesure hors de ceux qui la font tourner. Elle part des traces brutes — historique git, journaux et codes de sortie des courses, textes scellés pris par paires, registres des GO, des dépenses et des arrêts, passations dans l'ordre, mots verbatim du directeur, sorties brutes des collisionneurs, de l'organisme et des mentors — et non des synthèses. Elle livre : (1) un registre des idées à états fermés, où aucune idée ne s'éteint sans décision nommée et condition de réveil, et où aucun essai ne vaut échec sans preuve qu'il pouvait réussir ; (2) une boucle à intervalles croissants (une semaine, deux semaines, un mois, deux mois, plus une tranche ancienne tirée au sort) qui confronte ce qui se fait à ce qui fut voulu, promis et testé — dérive, réemploi, essais promis, cap — et rend à la session mère un petit nombre de signaux classés, chacun avec la décision à prendre ; (3) l'épreuve de la veille elle-même : idées plantées à clé scellée, double extraction indépendante avec estimation des idées manquées, audit à l'aveugle par un autre modèle, contrôles par programme, échantillon relu par le directeur ; (4) des critères chiffrés qui disent quand la veille marche, quand elle dégrade et quand elle doit être refaite ; (5) le tout dans git à chaque cycle, retrouvable à froid par une session neuve d'un autre compte en un temps borné. Dis ce qui existe déjà et tient, ce qui manque, et dans quel ordre le poser sans alourdir la procédure. »
