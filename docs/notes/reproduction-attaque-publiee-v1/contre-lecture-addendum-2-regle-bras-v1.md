# Contre-lecture (R2) — addendum 2 à la règle du bras d'attaque, non scellé

Date (`date -u`) : Tue Nov 10 12:33:29 UTC 2026. Contre-lecteur : sous-agent neuf, qui n'a écrit aucune des pièces lues.
Je reçois d'office le `CLAUDE.md` du dépôt. Ce rapport n'est pas scellé.

## Pièces lues et empreintes (`sha256sum`, relevées ici)

| Pièce | Empreinte |
|---|---|
| `prereg/bras-attaque-regle-v1-addendum-2.md` (objet, non scellé) | `89249e6692df30a3b355ff7edca40ec08cbb0cc3c4961130285e3b9a17b079db` |
| `prereg/bras-attaque-regle-v1.md` (lignes 110-120, 136-144, 226-236, 272-284, 350-360 seulement) | `88418df09c2e969cbdc77d220fe59dbf64f866d858ff02a039be5662c6d1f904` |
| `prereg/temoin-attaque-publiee-bailey-v1.md` (l. 31-47, 324-357, 376-392) | `fb6c2f34355d98ba08798cab1a4964a03b41eedf57d687454663f01c9646f2c3` |
| `prereg/bras-attaque-regle-v1-addendum-1.md` (pour la forme, l. 1-40) | `edfa69a292cc968afcaf396a11699a359ab99e929b3412728cda5d2d4c5b14ad` |
| `registres/passations/2026-11-10-1240-decision-lazar-noeud5-lecture-b2.md` | `2f3e8e3a0bbb37543b9cada3f019eb77d700acb734c0f75638332e7f4871f2a2` |
| `docs/notes/reproduction-attaque-publiee-v1/devis-temoin-attaque-publiee-bailey-v4.md` (§ 5, nœud 5, l. 145-158) | `f9c8c66e32a68b58cc63291fbe25a106a2e50cd5d49e52c35aa3fa9bb4c5ca44` |
| `docs/notes/reproduction-attaque-publiee-v1/noeud-5-valeur-temoin-recommandation-v1.md` | `0b2268b4e654c385ea351edfbfa97e0eabb3b1fda1ce6c7b6ecee52133a70488` |
| [RJ] brouillon 5, `origin/claude/upbeat-cray-dmauvv` (l. 110-125 seulement) | `527a3e7ec2a0f28221f57398794433793e3cf518360cca6ca9a8071ccbc2e414` |

**Non lu (cloisons)** : `donnees/`, `docs/notes/bras-attaque/`, `docs/notes/programme-et-4-familles-evasion/`, `diag/`,
tout résultat, note ou seuil de sonde ou de moniteur, tout résultat d'attaque contre le juge (A1-v3, A1-v4),
`registres/decisions.md`, `registres/etat.md`, le reste de `docs/notes/integration-bras-attaque-v1/`, le reste de la règle
et de [RJ].
**Outils** : `sha256sum`, `sed -n`, `grep -n`, `cat -n`, `git show`, `git log` (dates de commit), `stat`, `date -u`. Aucun
`git fetch` n'a été nécessaire (la référence était présente). Aucune requête réseau. Aucun refus de classifieur.

## (1) Fidélité à l'option (c) et au mot de Lazar

Mot verbatim : « go c, go lecture B − 2 ». Lecture consignée dans la note de décision, point 1 ; option (c) du devis v4
(l. 152-153) et de la recommandation.

- **Point 1** : fidèle (« il établit l'exécution de l'attaque publiée telle que publiée (étape 1) » ; ne tient pas seul le
  témoin). Rien d'ajouté.
- **Point 2** : fidèle sur le fond (même protocole, Llama-3.1-8B-Instruct, notre harnais, préenregistrement, devis et GO
  propres). Deux ajouts :
  - « même sonde publiée, mêmes critères que [TB], sauf le modèle et le harnais » : précision de « même protocole ».
    Elle découle de [RJ] l. 118 (« contre une sonde publiée, elle aussi reproduite ») ; acceptable. Mais « mêmes
    critères » lie d'avance le préenregistrement de l'étape 2 : certains critères de [TB] tiennent au banc des auteurs
    (contrôles et gardes calés sur leur code) et devront peut-être être adaptés. Voir correction C2.
  - « scellés et contre-lus » appliqué aussi au devis et au GO : R1/R2 visent le préenregistrement ; un GO est un geste
    de Lazar, il ne se contre-lit pas. Correction C2.
  - **Décision neuve** : « Le régime exigé à l'étape 2 (publié seulement, ou réduit compris) est fixé par ce
    préenregistrement, avant sa course. » Ni (c) ni le mot de Lazar ne tranchent ce régime. L'addendum en confie le choix
    au préenregistrement de l'étape 2, c'est-à-dire à son auteur. Or [TB] (l. 41-42) et la règle (l. 232, 278-279) placent
    « ce que vaut le verdict pour le témoin » dans un mot de Lazar ou un addendum scellé à la règle. De plus, [RJ] l. 118
    dit « à son régime », ce qui tire vers le régime publié. Correction C3 (bloquante).
- **Point 3** : découle de la règle scellée. La l. 352 dit : « un témoin applicable non constitué ou non tenu → échelon
  sans objet ». La l. 355 dit : « insuffisante pour ce témoin selon l'addendum → l'échelon 4 est sans objet ». Ce n'est pas
  une décision neuve. Il faut ajouter le renvoi à la l. 352 (C4).
- **Point 4** : **décision neuve**. Le mot de Lazar ne subordonne pas l'étape 2 à l'issue de l'étape 1. La phrase
  « l'étape 2 ne part pas sans un nœud à Lazar » est restrictive, donc sans danger pour les verdicts. Elle est pourtant
  redondante avec le GO propre de l'étape 2. La parenthèse « ne dit rien d'utile sur notre modèle » est un jugement de
  l'auteur, et il est contestable. Un échec de l'étape 1 peut venir de notre exécution ; c'est précisément ce que la
  recommandation dit que l'étape 1 sépare, et la règle l. 140 dit « met en cause la reproduction ». Correction C5.
- **Point 5** : découle des pièces. La formule vient mot pour mot de la note de décision. « Jamais « sur notre modèle »
  avant l'étape 2 » découle du devis v4 (l. 155-156) et de [TB] l. 355 (« rien sur Llama-3.1-8B-Instruct »). Il manque
  la condition « si l'étape 1 rend « effet reproduit » » (C6, clarté).
- Section « Ce que cet addendum ne fait pas » : fidèle.

## (2) Seuils, critères, renvois

Aucun seuil ni critère de la règle ou de [TB] n'est modifié. Les verdicts de [TB] (l. 331-334) sont rapportés tels quels
au point 1. Le seul risque de glissement est le point 2, régime de l'étape 2 (C3).

Vérification des renvois :

| Ligne | Contenu relu | Cité par l'addendum ? | Compatible |
|---|---|---|---|
| 116 | échelon 4 : « attaque publiée reproduite d'abord ([TB] …), puis comme 2, sur devis » | non (cité par la recommandation) | oui |
| 140 | « une attaque publiée non reproduite met en cause la reproduction » | non (cité par la recommandation) | oui ; la parenthèse du point 4 s'en écarte (C5) |
| 232 | table d'applicabilité : « ce qu'il vaut est porté par un addendum scellé avant toute course » | oui | oui |
| 278-279 | « ce qu'il vaut pour ce témoin, et quand il est *tenu*, sont portés par un addendum scellé avant toute course qui en dépend » | oui | oui ; l'addendum dit les deux (valeur ; « tenu » au point 2), sauf le régime de l'étape 2 (C3) |
| 355 | « Attaque publiée non reproduite, ou insuffisante pour ce témoin selon l'addendum … : l'échelon 4 est « sans objet » » | oui | oui |
| 352 | « témoin applicable … non tenu → échelon « sans objet » » | non | à ajouter au point 3 (C4) |

[RJ] l. 118 : la citation de l'addendum est exacte, au mot près.

## (3) Empreintes et chemins

Tous les chemins existent. Tous les préfixes cités sont égaux aux empreintes relevées : `88418df0`, `edfa69a2`,
`fb6c2f34…` (en entier), `f9c8c66e…` (en entier), `527a3e7e`, `0b2268b4`, `2f3e8e3a`.
**Heure** : l'en-tête de l'addendum porte « ≈ 12:40 UTC ». Le fichier date de 12:33:04 UTC (`stat`), et ma lecture a eu
lieu à 12:33:29 UTC. L'en-tête reproduit donc l'erreur d'heure que l'addendum signale lui-même pour la note de décision
(commit `edde1558` à 12:32:37 UTC). Correction C1. En passant, hors de l'objet : la recommandation porte « ≈ 12:35 UTC »,
mais elle a été committée à 12:27:00 UTC (`7eca9330`).

## (4) Clarté pour un lecteur qui n'a que les pièces

Le texte est clair et court, et sa forme suit celle de l'addendum 1. Il lui manque deux choses. D'abord, une phrase qui
dise que cet addendum remplit la condition de lancement 5 de [TB] et doit être scellé avant la création de l'instance de
[TB], comme le dit la note de décision (C7). Ensuite, la condition du point 5 (C6).

## Corrections (texte exact)

- **C1** (l. 3) : remplacer « 10 novembre 2026, ≈ 12:40 UTC. » par « 10 novembre 2026, ≈ 12:33 UTC. »
- **C2** (point 2) : remplacer « (même attaque publiée, même sonde publiée, mêmes critères que [TB], sauf le modèle et le
  harnais) » par « (même attaque publiée, même sonde publiée, critères de [TB] repris, sauf ce qui tient au modèle et au
  harnais, chaque écart écrit et motivé dans son préenregistrement) ». Remplacer aussi « sous un préenregistrement, un
  devis et un GO propres, scellés et contre-lus avant sa course » par « sous un préenregistrement contre-lu et scellé
  (R1, R2), un devis et un GO propres, avant sa course ».
- **C3** (point 2, bloquante) : remplacer « Le régime exigé à l'étape 2 (publié seulement, ou réduit compris) est fixé
  par ce préenregistrement, avant sa course. » par « Le régime exigé à l'étape 2 (publié seulement, ou réduit compris)
  n'est pas tranché ici : il est soumis à Lazar et écrit dans un addendum scellé à la règle avant la course de l'étape 2
  (l. 232, 278-279) ; tant qu'il ne l'est pas, l'étape 2 ne tient pas le témoin. »
- **C4** (point 3) : remplacer « (règle, l. 355) » par « (règle, l. 352 et 355) ».
- **C5** (point 4) : remplacer « elles sont rapportées ; l'étape 2 ne part pas sans un nœud à Lazar (une exécution qui
  ne retrouve pas l'effet sur le banc des auteurs ne dit rien d'utile sur notre modèle). » par « elles sont rapportées,
  et mettent en cause la reproduction (règle, l. 140). Leur effet sur l'étape 2 n'est pas tranché ici : le GO de l'étape
  2 (point 2) les cite. »
- **C6** (point 5) : remplacer « **Formule publique**, en attendant l'étape 2 : » par « **Formule publique**, si l'étape
  1 rend « effet reproduit » et en attendant l'étape 2 : ».
- **C7** (fin de l'introduction, après « aucune autre ligne. ») : ajouter « Il remplit la condition de lancement 5 de
  [TB] et est scellé avant la création de l'instance de [TB] (note de décision, point 1). »

## Verdict

**Scellable après corrections** : C3 est bloquante, C1 à C7 sont à appliquer. Après correction, l'addendum ne porte plus
de décision que Lazar n'a pas prise.
