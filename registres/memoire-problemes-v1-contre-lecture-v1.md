# Contre-lecture de la mémoire pilote des problèmes récurrents — version 1

**Objet.** `registres/memoire-problemes-v1.md`, empreinte attendue `85b72d0427d5d3bc0bec3dda2cb8eb76df005e2fc2d07ac99e9d7c53cae2a91d` ; empreinte recalculée par `sha256sum` : identique ; compagnon `.sha256` conforme. Fichier lu en entier (522 lignes).

**Contre-lecteur.** Sous-agent neuf lancé par la session mère, modèle Claude Opus 5.5 ; n'a écrit ni la mémoire ni aucune des lignes citées. Date : 2026-11-19.

**Ce qui a été lu.** La mémoire en entier ; dans `registres/decisions.md`, les lignes R- citées par les vingt problèmes vérifiés (extraits de 700 à 3 000 caractères, recherches par mot dans les lignes longues) et les lignes R-3600 à R-3653 (extraits de 900 à 1 000 caractères) ; les passations `2026-11-13-1553.md` (une ligne) et `2026-11-19-0635.md` (trois lignes). Rien ouvert sous `diag/`, `runs/`, `donnees/`, `docs/verdicts/`, `brouillons/ii-b-saboteur-budget-v1/`, ni aucun fichier dont le nom contient « consigne-privee » ou « conception-ii-b ». La ligne R-2059 n'a pas été lue (exclue par programme). **Lectures incidentes, déclarées** : noms de chemins sous `brouillons/ii-b-saboteur-budget-v1/` cités dans R-3340 et R-3558 (noms seuls) ; l'entier d'entropie d'un texte scellé imprimé dans R-3612 ; aucune valeur de résultat, de seuil ni de mécanisme.

**Aucun refus d'outil** pendant ce travail.

---

## Conclusions

**Employable par la mère** — sous les corrections de fidélité listées en section 2, aucune ne renversant un problème.

**Partition commune diffusable aux sessions filles : non, pas avant :**
1. que les renvois R- de la partition diffusée soient retirés, ou remplacés par des renvois que la fille a le droit d'ouvrir : 16 des 158 lignes citées par « commune » nomment le côté saboteur (R-1966, R-2013, R-2014, R-2057, R-3411, R-3412, R-3520, R-3529, R-3531, R-3539, R-3551, R-3553, R-3565, R-3570, R-3610, R-3622), et 6 des 7 lignes citées par « côté sondes » aussi (R-3539, R-3580, R-3583, R-3601, R-3610, R-3612). Le texte est propre ; le renvoi mène au contenu cloisonné ;
2. que la tentative R-3622 de M-016 sorte de « commune » (elle décrit le lanceur du côté saboteur) ;
3. que la tentative R-3113 / R-3118 de M-015 passe à la partition « mère » (elle apprend à toutes les sessions que le programme d'attestation du cloisonnement protège moins qu'annoncé) ;
4. que la tentative R-3538 / R-3547 / R-3553 de M-001 soit réécrite sans dire qu'un geste non rejouable a été mené au bout ;
5. que la pièce diffusée soit extraite par programme : en-tête réduit aux règles 1 à 6, plus « commune », sans « Comptes » ni « Ce que je n'ai pas pu classer » (qui nomment les partitions et d'autres chantiers) ;
6. qu'une vérification courte de cette version 2 par un agent neuf constate les points 1 à 5.

---

## 1. Cloisonnement, entrée par entrée

Méthode : lecture de chaque entrée ; recherche par programme, dans « commune », des mots saboteur, sonde, moniteur, lentille, organisme, bras, Carbon, Argon, témoin, juge, verdict, seuil, lecture, barreau, G1, idéation, mécanisme, course ; puis, pour « commune » et « côté sondes », recherche dans les lignes R- citées des mots qui désignent le côté saboteur.

**Constat général.** Le texte des entrées tient la règle 3 de l'en-tête : aucun score, aucune valeur de seuil, aucun fragment de consigne, aucun contenu de verdict. Les fuites sont de deux sortes : des renvois R- qui mènent au contenu cloisonné, et quatre tentatives qui disent ce qu'un côté fait.

| entrée | phrase | raison | gravité |
|---|---|---|---|
| M-016 (commune) | « 11-19, relevé croisé avant un départ : contrôle d'un lanceur sur les fichiers d'entrée ; […] ce contrôle échoue là où le chargeur de la course accepte les deux formes de fichiers, la répétition sur jouets n'en écrivant qu'une ; lanceur seul corrigé (R-3622) » | R-3622 est le relevé de l'exécutante du saboteur à budget ; la phrase apprend au côté sondes qu'une course du saboteur est imminente, avec un lanceur, un chargeur partagé et une répétition sur jouets. Le renvoi mène au nom du chantier et aux chemins de ses scripts. | à retirer de « commune » ; à garder en « côté saboteur » |
| M-015 (commune) | « six artefacts construits pour éprouver un programme d'attestation ; […] la contre-lecture montre ensuite par artefact que la garde protège moins que la ligne ne l'affirmait (R-3118) » | Ce programme atteste qui a lu quoi : la phrase signale à toute session fille une faiblesse du dispositif de cloisonnement, et R-3118 en donne la recette (nombre de caractères comparés). La mémoire est elle-même un canal d'attaque (en-tête, section c.8 de la lecture de Yu). | à passer en « mère » |
| M-001 (commune) | « 11-18, session fille et mère : avant un geste qui ne se rejoue pas, risque écrit et bornes […] ; observé : geste mené au bout sans redémarrage (R-3553) » | Dit l'état d'avancement d'une lecture décisive (R-3553 : fichier de lecture de l'étape B bis écrit). Ce n'est pas un résultat, mais c'est ce qu'un autre côté fait. | réécrire : « geste long et non rejouable : bornes de durée et de mémoire mesurées sur jouets avant le lancement (R-3547) » sans l'issue |
| M-013 (commune) | « lance un travail chez un fournisseur pendant une course dont le texte scellé exigeait l'usage exclusif de ce fournisseur » | Révèle un élément de plan d'une course d'attaque (usage exclusif d'un fournisseur). | faible ; acceptable, ou « pendant une course dont le texte scellé interdisait ce geste » |
| M-017 (commune) | « fournisseur surchargé non déclaré dans une tentative unique ; […] étape « non mesurée », tentative consommée (R-3398) » | Issue technique d'une course de l'organisme, déjà dans M-027 ; pas un résultat d'expérience. | faible ; acceptable |
| M-009 (commune) | « mot de Lazar reçu chez elle pour une session où un refus du classifieur est en cours » | Duplique M-024 (côté sondes) ; ne dit pas quel côté. | aucune |
| Partition « côté sondes » (M-024, M-025) | — | Texte propre : rien sur le saboteur. Mais 6 des 7 lignes citées nomment le côté saboteur ou l'exécutante (voir conclusions, point 1). | renvois à retirer |
| Partition « côté saboteur » (M-022, M-023) | — | Rien sur les sondes ; « côté exposé » désigne bien le côté saboteur (R-3558). | aucune |
| « Comptes » et « Ce que je n'ai pas pu classer » | noms des six partitions ; « codage des billets », « lot arrêté par les garde-fous du modèle » | Nomment les chantiers. | ne pas diffuser |
| Toutes partitions | — | Aucun résultat d'expérience. Le plus proche : M-029, « le code de sortie de la course ne confirme pas la vérification que l'état affirmait » (épreuve d'instrument, partition « bras A et relance », déjà connue de cette session). | aucune |

---

## 2. Fidélité

**Tirage.** Les 33 problèmes autres que les cinq dits les plus coûteux, tirés par `random.Random(20261119).sample(pool, 15)` : M-002, M-003, M-007, M-010, M-013, M-015, M-017, M-021, M-022, M-025, M-030, M-032, M-035, M-036, M-038. Plus les cinq imposés : M-001, M-016, M-026, M-029, M-034. Vingt problèmes, toutes leurs lignes R- citées ouvertes (sauf R-2059).

**Fidèles sans réserve (faits, dates, coûts retrouvés dans la ligne citée)** : M-003, M-007, M-013, M-015, M-017, M-021, M-022, M-025, M-030, M-032, M-034 (≈ 182 dollars, 49 minutes, treize sous-agents : R-3123), M-035, M-036, M-038. Les « attendu : écrit avant » de M-017 (R-3273 avant R-3398) et de M-002 (R-2536 et passation 2026-11-13-1553 avant R-3350) sont vrais. Les parades « en vigueur » de ces problèmes sont bien écrites dans les lignes citées (R-3590, R-3183, R-3327, R-3423, R-2128, R-3320, R-3455, R-3530, R-3131, R-3216, R-3123, R-3228, R-3347, R-3501).

**Erreurs de fidélité (avant → après).**

1. **M-026, troisième tentative** — avant : « attendu : « sinon le même échec est probable » (écrit avant, source R-3398) ; […] même échec […] — attente juste ». L'attente de R-3398 portait sur une relance *sans* diagnostic ; le diagnostic a été fait (R-3446) et sa correction écrite avant (provision de pensée relevée) n'a pas levé l'échec. → après : « attendu : la correction de R-3446 (provision relevée, sortie et délai corrigés) lève la cause (écrit avant, source R-3446) ; observé : même échec aux trois lots (R-3584) — attente fausse ». Effet sur les comptes : 6 justes, 2 fausses, 3 non vérifiables. C'est l'erreur la plus importante : elle transforme le seul diagnostic éprouvé de la mémoire en succès de prévision.
2. **M-001, deux tentatives, et M-016, une tentative : source d'une attente « écrite avant » qui est la ligne du résultat** — R-2796 (11-14), R-3010 (11-16) et R-2828 (11-14) sont les lignes qui rapportent le résultat ; la règle de l'en-tête (ligne 7) exige une pièce antérieure. Les attentes existent bien, mais ailleurs : → après : « écrit avant, source : limite déclarée de la commande v14, citée par R-2796 » ; « source : addenda de relance des jeux, cités par R-3010 » ; « source : mineur m2 de la contre-lecture de sûreté de la commande, cité par R-2828 ».
3. **M-001, quatrième tentative** — avant : « un autre jeu, lancé six heures plus tôt, avait été tué le matin même (R-2964) ». Le jeu de R-2964 est parti à 00:29:50Z et a été tué vers 06:13Z ; il précède de dix-sept heures le jeu tué en R-3010. → après : « un autre jeu, lancé vers 00:30Z, avait été tué vers 06:13Z le matin même (R-2964) ».
4. **M-010, première tentative et parade** — avant : « erreur corrigée avant tout geste, question de confirmation reposée (R-1978) » ; parade « question fermée de confirmation avant tout geste (R-1978, R-3361) ». R-1978 dit « Écart déclaré à Lazar », non une question reposée ; et c'est la question fermée elle-même qui portait l'erreur (mauvais fichier). → après : « erreur corrigée avant tout geste, écart déclaré à Lazar, la règle portera sur un lanceur neuf (R-1978) » ; parade : « question fermée de confirmation (R-3361), dont chaque nom de fichier est relu avant l'envoi (R-1978) ».
5. **M-029, deuxième tentative** — avant : « sept lanceurs écrits pour deux courses ayant atteint un modèle externe ». R-3132 : « sept lanceurs écrits, deux courses seulement ont atteint un modèle externe ». → après, à la lettre. Avant : « le code de sortie de la course ne confirme pas la vérification que l'état affirmait » ; R-3132 : « le code de sortie 4 atteste que les témoins plantés n'ont PAS été retrouvés — l'état affirmait exactement l'inverse ». → après : « le code de sortie atteste le contraire de ce que l'état affirmait ».
6. **M-029, parade et état** — avant : « aucune règle écrite comme telle » ; « état : clos ». R-3145 écrit une règle (« la garde de cumul […] est une constante figée qui ne relit pas la dépense réelle : à corriger avant toute course suivante ») et R-3249 la règle du registre dérivé ; et R-3641 (11-19) montre la récidive du produit non gardé (« la sortie de la course v6 ne garde aucun fichier de cartes, et l'orchestrateur a vidé le dossier des sessions à la fin »). → après : parade citant R-3145 et R-3249 ; état « ouvert ».
7. **M-016, deuxième tentative** — datée « 11-14 » ; R-2844 et R-2869 sont du 11-15. → après : « 11-14 et 11-15 ».
8. **M-002, première tentative** — « mère : session sans réseau » ; R-2164 parle de la session fille du niveau 3, R-2178 de la mère. → après : « session fille puis mère ». Parade : « hôtes ajoutés par Lazar (R-2570) » ; R-2570 dit que l'environnement par défaut est devenu « sans restriction ». → après, à la lettre.
9. **M-009, état** — « tenu depuis 2026-11-18 ». Le 11-19, un mot rapporté non relu à la source (« enleve la troncature pour carbon ») est « appliqué au devis de la version neuve » (R-3617), et deux autres mots rapportés modifient une version en cours (R-3641). Aucune ligne d'accord n'en dépend, mais la règle « rien ne se joue sur un mot rapporté » n'est pas tenue à la lettre. → après : « ouvert », avec ces deux tentatives.
10. **En-tête, sources** — « 1 692 lignes, de R-1949 à R-3639 » ; recompté par programme : 1 693 lignes R- dans cette plage (doublon compris). → après : « 1 693 lignes ».

Les cinq problèmes dits les plus coûteux : M-034 et M-016 fidèles hors points 2 et 7 ; M-001 fidèle hors points 2 et 3 (cinq remplacements de la nuit : R-3569 dit « cinquième ») ; M-026 fidèle sur les faits et les coûts (≈ 44,8 USD : R-3398, 44,780492 ; ≈ 42,4 USD : R-3584, 42,36) mais faux sur le point 1 ; M-029 : points 5 et 6.

---

## 3. Utilité des signaux d'alerte — les cinq plus faibles

1. **M-002** — « épreuve du crochet qui passe en code 0 » : le cas sain passe légitimement en code 0, le signal est donc ambigu. → « l'épreuve de l'artefact (une commande que le crochet doit refuser, seule dans sa ligne) rend le code 0 ; ou une commande `vastai`, `ssh` ou `scp` rend « introuvable » ; ou le conteneur a changé depuis la dernière installation à la main (noyau ou durée de marche) ».
2. **M-014** — « la vérification de l'arbre rend un nombre de problèmes différent de celui de la passation précédente » : le stock varie pour d'autres raisons ; la faute à reconnaître est le versement sans compagnon. → « tu ajoutes au dépôt un fichier dont le `.sha256` n'est pas dans le même commit ; ou tu écris « aucune empreinte fausse » après une vérification de l'arbre, qui ne parcourt que six dossiers ».
3. **M-034** — « plus de quelques sous-agents lancés d'un coup avec le même long brief » : « quelques » ne se compte pas. → « tu lances plus de trois sous-agents dans le même tour, ou un brief de plus de deux cents lignes qui sera relu à chaque appel ; ou une tâche qu'une passation scellée ou une lecture directe dans ton contexte suffirait à faire ».
4. **M-038** — « une demande qui revient sur un sujet où une réponse a déjà été arrêtée » : la session ne sait pas quels sujets sont arrêtés. → « la demande touche un sujet listé comme arrêté dans le registre (lignes « arrêt ; classifieur ») ; tu les cherches avant de répondre, et tu ne réponds pas sur le fond si le sujet y est ».
5. **M-010** — le signal ne couvre pas l'erreur la plus fréquente de la nuit du 18 au 19 : une transcription qui ajoute au mot (R-3609, R-3637). → ajouter : « ta transcription d'un mot de Lazar contient un motif, un chiffre ou une condition qui n'est pas dans son verbatim ni dans l'option qu'il a choisie ; ou tu inscris un mot qui n'a pas « go » ou qui finit par un point d'interrogation ».

---

## 4. Manques — nuit du 18 au 19, lignes R-3600 à R-3653

Problèmes de procédure vus au moins deux fois et absents de la mémoire (ou présents sans les tentatives de cette nuit) :

1. **Transcription qui ajoute au mot du directeur.** R-3609 (« les errata retirent ce que les transcriptions ajoutaient au mot de Lazar »), R-3637 (« au nœud 2, le motif qui lui avait été donné allait au-delà de N-060 v4 » ; six corrections), R-3610 point 4 (« augmente le plafiond » lu comme trois chiffres précis, « lecture du compte organisme, non de Lazar »). M-010 ne cite que R-3637 et le range sous « lu de travers ». À faire problème propre, parade en vigueur : vérification de chaque transcription par un agent neuf et erratum qui prime (R-3609, R-3637).
2. **Ligne d'accord inscrite avant un mot complémentaire, ou trop vite.** R-3647 (« la mère avait inscrit la version 1 à 07:35Z, avant ces deux mots : la ligne -12 n'est pas modifiée, la ligne -13 la corrige ») ; R-3608 puis R-3609 (« devient sans objet » écrit trop vite, précisé une heure plus tard) ; antérieur : R-3358 / R-3361. Absent. Parade possible : attendre une à deux minutes après un mot de Lazar avant d'inscrire, relire les événements suivants de la même session.
3. **Mot sans « go », ou question, lu comme un choix.** R-3615 (« il cite la recommandation sans le mot « go » ; la mère le lit […] comme le choix de révoquer »), R-3640 (« go a » lu comme l'option (a) de la dernière décision posée, lecture dite), R-3652 (« (b) Cinq non ? » : la mère ne l'inscrit pas, bonne pratique). Partiellement dans M-010 ; les tentatives de la nuit manquent.
4. **Compte repris d'un texte ancien sans recoupement, dans une option posée à Lazar.** R-3648 (« la mère avait repris le compte du texte archivé sans le recouper avec le nœud 10 » : cinq moniteurs au lieu de quatre) ; antérieurs : R-2204 (chiffre d'avant corrections), R-2811 (montant de mémoire). M-032 a les deux anciens, pas R-3648 ; et M-010 a R-1978 (option posée nommant le mauvais fichier). À réunir en « option posée à Lazar construite sur un fait non recoupé ».
5. **Dépense faite avant sa ligne.** R-3617 est dans M-033 ; aucune autre occurrence dans la plage. Couvert.
6. **Produit d'une course vidé par l'orchestrateur, condition de conservation non tenue.** R-3641 (11-19) répète R-3446 (11-18). M-021 a R-3446, pas la récidive, qui montre que la parade « verser au fil de l'eau » ne couvre pas un dossier que l'orchestrateur vide lui-même.
7. **Crédit du loueur partagé avec les machines d'autres projets.** R-3606, R-3632, R-3644 (et R-3550) : la baisse du crédit est expliquée chaque fois après coup par les machines d'une autre session. M-019 a l'idée (R-3285) sans ces tentatives.
8. **Suite d'essais de la routine dominée par des échecs anciens hors des travaux en cours.** R-3603 (393 échecs dans d'autres chantiers), antérieurs R-2776 et R-2552 (inventaires d'essais en retard sur le code, échec non signalé par les passations). Vu au moins trois fois, absent : la routine de reprise ne distingue plus un échec neuf d'un échec connu. Parade à écrire : liste scellée des échecs connus, comparée par programme.
9. **Compagnons d'empreinte.** R-3621 (102 problèmes, dont un compagnon « mal nommé », chemin complet au lieu du nom) : forme neuve de M-014, non citée.
10. **Revendication scellée avant la contre-lecture de la lecture qui la fonde.** R-3627 (complément 1 de N-073 scellé), R-3629 (« elle est peut-être trop généreuse »), R-3636 (« onze erreurs à corriger »), R-3643 (complément 2). Vu une fois dans la plage, sans coût de dépense ; à garder en observation.

---

## 5. Comptes recomptés par programme

Script : découpage par en-têtes « ## Partition », comptage des « ### M- » et des lignes de tentative (indentées sous « - tentatives »), des sources « écrit avant, source », des fins « attente juste », « attente fausse », « attente non vérifiable », et des états.

| partition | problèmes | tentatives |
|---|---|---|
| commune | 21 | 111 |
| côté saboteur | 2 | 7 |
| côté sondes | 2 | 7 |
| organisme d'idéation | 3 | 13 |
| bras A et relance | 3 | 7 |
| mère | 7 | 23 |
| total | 38 | 168 |

Attentes écrites avant : 11 ; sans : 157. Parmi les 11 : 7 justes, 1 fausse, 3 non vérifiables. États : 24 ouverts, 9 tenus, 5 clos. **Tous les comptes du fichier sont exacts tels qu'écrits.** Après les corrections de la section 2 : 6 justes, 2 fausses, 3 non vérifiables (point 1) ; états 26 ouverts, 8 tenus, 4 clos (points 6 et 9).
