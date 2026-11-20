# Contre-lecture — préenregistrement court v7 et devis v5 de la course « nouvelles attaques » — v1

- Contre-lecteur neuf, modèle O. J'ai contre-lu la v4 et vérifié les v5 et v6, ainsi que les devis v3 et v4. Je n'ai écrit ni la v7, ni le devis v5, ni la question, ni la note de périmètre, ni la partie servie. Règle R2 ; pièces décisives (classe A). Écrit le 2026-11-20 ; relevé de `date -u` : 13:00:45Z, avant l'écriture.
- Demande : message de la session de l'organisme (versement au commit `bbbd794b`). Mêmes interdits que mon mandat (`01f9e057…`). Mandat du rédacteur lu d'abord (`09ad78ba66e7d11ead6ceac08e4ce1cabcd3469a1b68dcdec3ad75d16e4b1e4b`, égal à son compagnon).
- Processeur seul. Aucun appel à un fournisseur de modèles, aucune dépense, aucun lancement, aucune écriture dans le dépôt, aucun commit. Réseau : un `git fetch origin main`. Pendant ma lecture, `origin/main` est passé à `b09e483c405544a8bce91f42b9f3a440e40d263c` ; je cite chaque registre par son commit. **Aucun refus de permission, de classifieur ni de garde.**
- Ce rapport ne contient aucune recette, aucun nom ni énoncé de mode, aucun identifiant de modèle et aucune valeur de clé.

## Verdict

**À corriger.**
- **Préenregistrement v7 :** douze corrections de lettre, K'1 à K'12. Aucune ne change un tirage, un seuil, un arrêt ni un total.
- **Devis v5 :** il est juste au centime près. Il ne porte pas la décision de la mère R-4265 (sonde de l'espèce 6 à 0,05 USD), prise après son écriture. Cette décision touche aussi la v7, et elle change des chiffres dérivés (plafond total, cas haut, parts de l'espèce 6). C'est à la mère de la faire porter par une passe de rédacteur, avec les chiffres refaits au § 4.
- **Rejeux :** les deux passages de l'outil, rejoués sur la v6 et le devis v4 scellés, sont égaux à l'octet. Le calcul v4, joué deux fois, est égal à l'octet à la sortie versée. Mon recalcul indépendant rend les mêmes chiffres, à un centime d'arrondi près dans cinq cases.

## 1. Empreintes et rejeux

- **Sources scellées tirées de `main` par `git show` :** la v6 (`7e240c8c…`), le devis v4 (`620de369…`), la question v5 (`eaf5db8a…`), la partie servie (`4cd360ba…`, 2 957 octets, un seul emplacement de case), la synthèse servie v5 (`f74c6064…`, 32 260 octets) et la note de périmètre v3 (`dd6fea0e…`). Les empreintes sont recalculées, toutes égales à celles de la table.
- **Pièces versées :** toutes égales à leur compagnon. Ce sont la v7 (`1837a685…`), le devis v5 (`41a09f77…`), les deux jeux JSON et les deux journaux, les deux différentiels, le calcul v4 (`7dff52cd…`) et sa sortie (`aabdec42…`), la sortie du validateur et le rapport du rédacteur (`f1751793…`).
- **Registres :**
  - `go.md` est identique à `ee888da7` et à `b09e483c` (`7799734e…`). Aucun mot de Lazar sur l'épreuve 4 n'y figure.
  - `decisions.md` vaut `46cf019b…` à `ee888da7` (égal à la table) et `9dcc73bb…` à `b09e483c`, qui ajoute R-4261 à R-4265.
- **Outil (`391db990…`) :**
  - v6 vers v7 : « FAIT : 35 », sortie `1837a685…`, `cmp` égal.
  - devis v4 vers v5 : « FAIT : 11 », sortie `41a09f77…`, `cmp` égal.
  - Les différentiels refaits ne diffèrent que par les deux lignes d'en-tête.
- **Calcul v4 du rédacteur :** joué deux fois, sorties égales entre elles et à `aabdec42…`.
- **Validateur :** sur la v7, « problemes : aucun », égal à la sortie versée. Ce « aucun » ne vaut pas « complet » : la section « Contre-lecture » dit seulement « La v7 n'est pas contre-lue » ; il faut une entrée 5 (texte au § 7).

## 2. Les dix points du mandat, à la lettre des décisions

| point | jugement |
|---|---|
| 1. Pièces servies | Conforme. Partie servie seule, avec l'épreuve « aucun programme n'ouvre la question ». Ligne de case avec ses contraintes et son épreuve. Requête assemblée journalisée avec son empreinte. Synthèse v5. Gabarit et tailles vérifiés. |
| 2. Racine | Conforme : `0x2cf2aae035beef43e999e3cd8b0fb7ba`, citée à la lettre de GO-2026-11-20-42, point 2. |
| 3. Arrêts n° 14 et n° 16 | Conformes. Liste complète des pièces fixes ; normalisation ; témoin positif par motif ; refus nommé ; épreuve par famille ; course, sondes et témoins couverts ; liste jamais servie. |
| 4. GO-2026-11-20-46 | Points 3, 4, 5, 6 et 9 conformes aux recommandations de la note v3, § 8 (relues), et au § 4. Le portier est lu à la lettre de la condition du point 3 et du point 1 ; la mère a retenu cette lecture après coup (R-4265) : K'6 le cite. |
| 5. GO-2026-11-20-50 | Les six garde-fous sont cités à la lettre et ont chacun un arrêt (n° 17 à n° 23) et une épreuve sur cas sain et artefact. Les épreuves 1, 2, 3 et 4 se jouent par programme en moteur simulé. Les épreuves 5 et 6 et l'arrêt n° 18 sont en partie procéduraux, ce que la v7 dit. Un défaut de lettre : le chapeau de la liste d'arrêt veut toutes les épreuves « avant la course », alors que les arrêts n° 20 à n° 23 gardent ce qui suit la course (K'9). |
| 6. R-4250, R-4260 | Conforme. Les classes « refus du modèle » et « réponse illisible » ne sont pas dans R-4250 : K'7 les marque comme précision du rédacteur. |
| 7. Épreuve 4 | Conforme : deux branches, au même rang, sans trancher. |
| 8. Sondes | Conforme à la lettre. Le plafond de la sonde de l'espèce 6 n'est plus celui que la mère a décidé (R-4265 : 0,05 USD) ; voir § 4. |
| 9. Ordre de course | Conforme au mandat (le texte de l'erratum est au rapport). Deux manques : la v7 ne cite pas ce rapport par chemin et empreinte, et elle ignore l'erratum 1 de la question v5 que la mère a décidé (R-4265) (K'8, K'12). |
| 10. Tenue | Un défaut : la table des pièces laisse le devis en blanc (« au scellement, par la mère »). La ligne C1 de la v6, gardée, dit encore « « devis v3 » … renvoie à ce devis v4 », alors que la clause (d) le renvoie au devis v5 (K'1 à K'4). |

**Aucune recette :** la v7 et le devis v5 ne portent ni procédé, ni nom ni énoncé de mode (comptes à 0 sur les noms de familles de la note), ni identifiant de modèle. La clé de l'espèce 6 n'est désignée que par le nom de sa variable, comme à la v4.

## 3. La clause « Lecture de ce texte depuis la v7 »

Les passages non récrits se lisent juste sous ses points (a) à (c), y compris M1, M3, le plan d'analyse, la règle d'antériorité, l'arrêt n° 5, la course arrêtée et la table « un par un ». **Deux passages restent faux malgré elle :**
1. **La ligne C1 de la table des pièces.** Elle renvoie « devis v3 » au devis v4 et contredit le point (d). Le point (d) lui-même renvoie au devis v5 « dès son scellement », alors que la table n'en porte ni le chemin ni l'empreinte (règle R6). K'1 à K'4 corrigent.
2. **« Ce qui reste à écrire », point 6.** Il retire de ce qui reste l'attestation « aucune recette » de la pièce d'antériorité, alors que la section « Hypothèse », point 4, la veut encore. Aucun registre lu n'inscrit cette attestation pour la synthèse v5 : R-4229 n'inscrit qu'un contrôle des noms, des identifiants et des chemins. K'11 corrige.

S'y ajoute une incohérence de compte, hors de la clause : « Soixante-sept cases restent en réserve », alors que la sonde en consomme une (« soixante-six le restent ») (K'10).

## 4. Le devis v5

**Refait indépendamment** par `recalcul_contre_lecteur_devis_v5_v1.py` (fractions exactes, joué deux fois, égal à l'octet). Sortie : `recalcul-contre-lecteur-devis-v5-v1.json`.

**Égal au rédacteur :**
- Tailles : 3 205 octets pour la partie servie remplie (2 957 − 8 + 256), 35 465 octets pour la requête d'un proposeur à la génération 1.
- Sonde de l'espèce 6 :
  - à 0,01 USD : 3 205 jetons d'entrée, 0,00641 USD, 359 jetons de sortie au plus ; 743 au compte de 2,5 octets par jeton ;
  - à 0,05 USD : 4 359 jetons de sortie ;
  - avec la synthèse en plus : 0,07093 USD d'entrée.
- Repères de l'espèce 6 : 2,34 ; 4,98 ; 7,62 ; 12,90 ; 23,46 ; 0,9768 ; 90 587.
- Totaux : 262,23 ; 548,66 ; 576,01.
- Confrontation : toutes les cases au cas bas et au pire, Minuit et Luc partout, et le cas avec le collisionneur (9,54 ; 18,37).

**Un centime d'écart dans cinq cases « au cas haut ».** Le rédacteur soustrait le reste arrondi du besoin arrondi ; l'exact donne :

| case | rédacteur | exact |
|---|---|---|
| Rigaud, lecture du registre, lots à 45 | 32,46 | 32,47 |
| Rigaud, lecture corrigée, lots à 45 | 15,75 | 15,76 |
| troisième relais | 5,50 à 8,10 | 5,51 à 8,11 |
| espèce 6 | 56,32 | 56,31 |

Sans effet sur un verdict « tient / ne tient pas ». Mais « recharger jusqu'au cas haut (… 5,50 à 8,10 USD) » est un « au moins » trop bas d'un centime : la passe du point suivant l'écrit à l'exact.

**Ce qui tient et ce qui ne tient pas :** juste, et dit sans trancher. Les trois manières de fixer les parts sont correctement chiffrées.

**Non porté : R-4265, sonde de l'espèce 6 à 0,05 USD** (décision de la mère, 12:49:39Z, après l'écriture). La v7 et le devis v5 demandent 0,01 USD avec 359 jetons, et disent 0,05 « non accordée ». À porter par une passe de rédacteur sur les deux textes, avec ces chiffres refaits par mon programme :

| | 0,01 (textes actuels) | 0,05 (R-4265) |
|---|---|---|
| plafond total | 576,01 | **576,05** |
| total au cas haut | 548,66 | **548,70** |
| écarts à cinq espèces (plafond ; haut) | +120,01 ; +129,23 | +120,05 ; +129,27 |
| attendu | 262,23 | 262,23 |
| sortie de la sonde (un jeton par octet ; 2,5 octets par jeton) | 359 ; 743 | 4 359 ; 4 743 |
| clé de l'espèce 6, sonde comprise : bas / haut / pire | 35,20 / 88,56 / 199,66 | 35,24 / 88,60 / 199,70 |
| manques sur 32,24 : bas / haut / pire | 2,96 / 56,32 / 167,42 | 3,00 / 56,36 (56,35 exact) / 167,46 |
| avec le collisionneur au pire, bas | 9,54 | 9,58 |

Lieux à toucher dans la v7 : ligne 128 (548,66 ; 576,01), lignes 167 et 168 (sonde ; plafond total), 231, 242, 247 (valeur ouverte de la borne de sortie), 264 à 266 (paragraphe de la sonde), 288, 368 (arrêt n° 2), 406 et 407. Dans le devis v5 : § 0, § 4 (table et sondes), § 6 (ligne de l'espèce 6 et texte), § 9 (options, « tu accordes aussi », décision de la v5), et le calcul (une version v5 du programme, constante de la sonde).

**Remarques de lettre sur le devis, à porter dans la même passe** (sans cette passe, sans suite) :
1. « 2,5 octets par jeton, le compte de prudence pris pour le collisionneur » : R-4251 dit 2,5 *caractères* par jeton. Le compte en octets est plus prudent (un caractère accentué fait deux octets) ; il suffit de le dire.
2. « Dans ce devis, « préenregistrement court v4 » se lit … « préenregistrement court v7 » » : il faut nommer la version scellée.
3. Les cinq centimes ci-dessus.

## 5. Les douze points non tranchés du rédacteur

| n° | point | suite | avis, confiance |
|---|---|---|---|
| 1 | épreuve 4, « avec » ou « sans » ; les quatre épreuves ou la quatrième seule | au directeur | Les deux branches sont justes et complètes ; son mot doit aussi dire « quatre ou une ». 0,8 |
| 2 | le portier | sans suite ; K'6 cite R-4265 | La lecture suit GO-2026-11-20-46, point 1 (v5 au niveau de l'idée, procédé ensuite) et la condition du point 3. La mère l'a retenue (R-4265). 0,85 |
| 3 | « aucune carte ne nourrit le mode tenu à l'écart » | au directeur | Le garder d'ici son mot est la lecture prudente ; R-4265 le pose déjà à Lazar. 0,75 |
| 4 | sonde de l'espèce 6, 0,01 avec 359 jetons | à la mère | R-4265 a fixé 0,05 USD. 359 jetons laissent peu de place à une réponse lisible, surtout si l'espèce dépense des jetons de raisonnement ; 0,05 en laisse 4 359. Passe de rédacteur sur les deux textes, chiffres au § 4. La sonde ne porte pas la synthèse : c'est juste, à 0,05 USD l'entrée seule ne tiendrait pas (0,0709). 0,8 |
| 5 | case de la sonde | sans suite, K'10 | Première case de la réserve, aucun tirage neuf : juste. Elle n'existe qu'après le tirage scellé (point 7 avant le point 10 de « ce qui reste »). Le compte de la réserve est corrigé. 0,75 |
| 6 | identifiant neutre | à la mère (additif) | Les contraintes sont gelées ; une construction tirée prendrait une clé de tirage neuve, déjà écrite. 0,8 |
| 7 | parts des clés | au directeur et à la mère | Lazar recharge, la mère dit où ; chiffres justes (§ 4). GO-2026-11-20-52 note pour un autre conteneur « Kimi absent : pas de relais » : le relais de l'espèce 6 doit exister dans le conteneur de la course. 0,8 |
| 8 | revue externe encore citée par la question v5 et l'ordre | à corriger (K'8, K'12) et à la mère (errata de R-4265) | La question v5 n'en a qu'une mention, non servie. La v7 doit dire l'erratum et qu'elle prime d'ici là pour la mesure interne. 0,8 |
| 9 | qui (session à part, liste de référence, lecteur du garde-fou 5, liste nominative) | au directeur | Valeurs ouvertes bien placées ; R-4265 le pose à Lazar. 0,8 |
| 10 | « refus du modèle », « réponse illisible » | à corriger (K'7) | Utiles pour que la réponse vide motivée reste distincte ; à marquer comme précision du rédacteur. 0,75 |
| 11 | garde de motifs sur le registre servi | à la mère | Le risque de faux refus vaut aussi pour les requêtes de l'aiguilleur et des juges, qui portent des fiches. La famille « composition et tenue » vise des mots courants, dont un ou plusieurs paraissent déjà dans le gabarit (1 ligne) et dans la synthèse (5 lignes, compte grossier). Écrire la liste contre ces deux pièces scellées et faire jouer la garde aux témoins plantés à l'épreuve des témoins. 0,7 |
| 12 | table des pièces | à corriger (K'1 à K'4) ; à la mère | Les deux contre-lectures et le journal de dérivation sont bien sur `main`. Le reste net comptable (`62c625ab…`) n'y est pas (constaté par `git cat-file`) : à verser sur `main` avant le scellement. 0,8 |

## 6. Corrections à texte exact, sur la v7 (`1837a685…`)

Chaque « Ancien » est compté une fois par `grep -c -F -e`. Les douze remplacements sont dans `corrections-preenregistrement-court-v7-v1.json`, à côté de ce rapport. Passés à l'outil sur une copie : « FAIT : 12 remplacement(s) », sortie `8487e6895090af7c6404c76c9daa1bda58929ae6946a1d3321dd4b252a72e924`. Le validateur rend « aucun » sur la copie. La version neuve, sous un nom neuf, porte aussi la passe R-4265 du § 4 si la mère la fait.

- **K'1** (table, ligne C1). Ancien : « | devis à six espèces, v4 (« devis v3 » dans ce texte, hors la citation de GO-2026-11-20-34, renvoie à ce devis v4, qui ne change du devis v3 que la lettre des corrections K5 à K9, sans total, seuil ni section changés ; « devis » seul renvoie au devis v2) | » — Neuf : « | devis à six espèces, v4, scellé (R-4206) ; il ne change du devis v3 que la lettre des corrections K5 à K9, sans total, seuil ni section changés. Depuis la v7, « devis v3 » dans ce texte, hors la citation de GO-2026-11-20-34, renvoie au devis de la ligne « devis à six espèces, en vigueur » ci-dessous ; « devis » seul renvoie au devis v2 | »
- **K'2** (table, ligne neuve après les décisions de la v7). Ancien : « R-4250, R-4255, R-4256, R-4258, R-4260 | `46cf019bb9f3cd84bb39ab741def1270366b1a58d63046a856160aa940f40ff9` | » — Neuf : le même texte, un saut de ligne, puis « | décisions de la mère postérieures à l'écriture de la v7 (portier ; sonde de l'espèce 6 ; erratum 1 de la question v5 et de l'ordre de course) | `registres/decisions.md` sur `main`, commit `b09e483c405544a8bce91f42b9f3a440e40d263c` : R-4265 | `9dcc73bb3eeba20fbbe94b6df86021332c500b724a2ae0c6e248c5b28b9caf4a` | »
- **K'3** (table, ligne neuve du devis). Ancien : « | outil de remplacement | `scripts/remplacer_texte_exact_v1.py` | `391db990734dd36f7c827b8b6c77dc0de1bda324f671b65748ccfe68c56a53d6` | » — Neuf : le même texte, un saut de ligne, puis « | devis à six espèces, en vigueur : le devis v5, scellé par la mère avec ce texte ; sortie de son calcul, `NA/preenregistrement-court-v7/calcul-devis-course-nouvelles-attaques-v4.json`, `aabdec424100bcf48d05bed8676eca7a2b783763554b60bf3615b2c1fdf84d46` ; programme `calcul_devis_course_nouvelles_attaques_v4.py`, `7dff52cd739a5ab9c54ad91c737dce9f1edf9d3fbc416f1db0ade0088eaaedef` | `NA/preenregistrement-court-v7/devis-course-nouvelles-attaques-v5.md` | `41a09f77be48d33b0847888cdd4cf251c5c4fa511d47d69981e27b7d3f0fa22a` | ». Si la passe R-4265 récrit le devis, cette ligne nomme le devis récrit, son calcul, leurs chemins et leurs empreintes, et je les vérifie.
- **K'4** (sous la table). Ancien : « Le devis v5 et la sortie de son calcul sont rendus avec ce texte et ne sont pas scellés à son écriture : la table ne porte que des pièces scellées ou versées, et leur chemin et leur empreinte y entrent au scellement, par la mère ; c'est le seul blanc de cette table. » — Neuf : « Le devis v5 et la sortie de son calcul sont versés avec ce texte et scellés par la mère avec lui ; leur chemin et leur empreinte sont à la ligne « devis à six espèces, en vigueur ». La table n'a aucun blanc. »
- **K'5** (clause, point (d)). Ancien : « (d) « Devis v3 » renvoie, dès son scellement, au devis v5, qui garde » — Neuf : « (d) « Devis v3 » renvoie au devis v5, ligne « devis à six espèces, en vigueur » de la table des pièces, qui garde »
- **K'6** (le portier). Ancien : « **dans cette course, le procédé n'est pas permis.** » — Neuf : « **dans cette course, le procédé n'est pas permis** ; c'est la lecture que la mère retient (R-4265). »
- **K'7** (classes d'issue d'appel). Ancien : « Chaque appel de proposeur reçoit une **classe d'issue d'appel**, parmi quatre, exclusives : » — Neuf : « Chaque appel de proposeur reçoit une **classe d'issue d'appel**, parmi quatre, exclusives (« réponse vide motivée » : R-4250 ; « refus du modèle » et « réponse illisible » : précision du rédacteur de la v7, pour que la première reste distincte) : »
- **K'8** (lecture de l'ordre de course). Ancien : « Il se lit avec un erratum d'une ligne, que la mère écrit et scelle ; le texte exact que cet erratum doit porter est au rapport du rédacteur de la v7. » — Neuf : « Il se lit avec un erratum d'une ligne, que la mère écrit et scelle ; le texte exact que cet erratum doit porter est au § 5 du rapport du rédacteur de la v7 (`NA/preenregistrement-court-v7/rapport-redacteur-preenregistrement-court-v7-devis-v5-v1.md`, `f1751793f9b48b8258d66292adbf6239d8159b4ff281d0782697bca9cc6981c1`) ; là où ce texte écrit « préenregistrement court v7 », l'erratum nomme la version de ce préenregistrement que la mère scelle. La question v5 se lit de même avec son erratum 1 (§ 3 et § 7), décidé par la mère (R-4265) pour remplacer « après la revue de sécurité externe » ; ces passages ne sont pas servis, et d'ici cet erratum ce texte prime sur eux pour la mesure interne (section « Critères de lecture gelés », paragraphe « Portée »). »
- **K'9** (chapeau de la liste d'arrêt). Ancien : « Chaque garde est éprouvée sur un cas sain et sur un artefact avant la course (règle R5), et l'épreuve est consignée. » — Neuf : « Chaque garde est éprouvée sur un cas sain et sur un artefact avant la course (règle R5), et l'épreuve est consignée ; les arrêts n° 20 à n° 23, qui gardent ce qui suit la course, le sont avant le premier usage de ce qu'ils gardent (section « Hypothèse », paragraphe « Garde-fous »). »
- **K'10** (réserve). Ancien : « Soixante-sept cases restent en réserve. » — Neuf : « Soixante-sept cases restent en réserve ; la première d'entre elles, dans l'ordre canonique, sert aux sondes de refus (section « Seuil », paragraphe « Sonde de refus de l'espèce 6 ») : soixante-six restent fraîches. »
- **K'11** (ce qui reste, point 6). Ancien : « 6. La pièce d'antériorité servie : depuis la v7, c'est la synthèse servie v5, scellée (R-4229 ; table des pièces). » — Neuf : le même texte, suivi de « Reste son attestation « aucune recette » par la mère (section « Hypothèse », point 4), inscrite au registre des décisions avant tout allumage : R-4229 n'inscrit qu'un contrôle des noms, des identifiants et des chemins. »
- **K'12** (ce qui reste, point 15). Ancien : « 15. (v7) **L'erratum d'une ligne à l'ordre de course v3**, écrit et scellé par la mère. » — Neuf : « 15. (v7) **L'erratum d'une ligne à l'ordre de course v3** et **l'erratum 1 de la question v5** (§ 3 et § 7 ; R-4265), écrits et scellés par la mère. »

**Devis v5 :** aucune correction de lettre de ma part hors la passe R-4265 (§ 4), qui porte aussi les trois remarques du § 4.

## 7. Texte à porter à la section « Contre-lecture »

À la place de « - **La v7 n'est pas contre-lue.** … scellement par la mère. », la mère écrit l'empreinte de ce rapport, prise à son compagnon, et le traitement :

« - **Contre-lecture 5** (la v7 et le devis v5, par un agent d'un autre modèle) : contre-lecteur neuf, modèle O, sous-agent de la session de l'organisme, le 2026-11-20 ; il n'a écrit ni la v7, ni le devis v5, ni la question, ni la note de périmètre, ni la partie servie. Brouillons relus : la v7, `1837a6850269d925e75744828f44c4437e0c7894595218bce3358ccfdeac551d`, et le devis v5, `41a09f77be48d33b0847888cdd4cf251c5c4fa511d47d69981e27b7d3f0fa22a`. Rapport : `contre-lecture-preenregistrement-court-v7-devis-v5-v1.md`, verdict « À corriger » : K'1 à K'12 sur ce texte, toutes de lettre ; décision de la mère R-4265 (sonde de l'espèce 6 à 0,05 USD) à porter sur les deux textes. Rejeux de l'outil égaux à l'octet ; calcul du devis refait indépendamment, égal au centime d'arrondi près. »

## 8. Écarts

1. J'ai tiré les noms des pièces versées du rapport du rédacteur et des journaux, sans commande de liste.
2. `origin/main` a bougé pendant ma lecture. Je cite les registres par leur commit : `ee888da7` pour la table de la v7 ; `b09e483c` pour R-4265.
3. Pour le point 11, j'ai compté par `grep -c` les lignes de la synthèse et du gabarit qui portent quelques mots de la famille « composition et tenue » et des noms de familles de modèles. Ce sont des comptes seulement : rien n'en est recopié, et aucune fiche n'existe.
4. Mes essais sont dans le sous-dossier `v7/` de mon dossier ; rien n'est écrit ailleurs.

— contre-lecteur neuf, modèle O
