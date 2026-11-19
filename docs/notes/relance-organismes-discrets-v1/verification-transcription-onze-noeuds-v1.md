# Vérification de la transcription des choix de Lazar sur les onze nœuds du texte neuf du bras A — v1

**Verdict : fidèle sous corrections listées.** Les onze options retenues sont bien les onze recommandations de la décision posée ; aucune n'est inversée. Six points de rédaction sont à corriger, par un erratum (la transcription scellée reste telle quelle) : une condition retirée au nœud 1, « ici » retiré au nœud 3, le contenu de la mesure retiré au nœud 4, « pour toutes les doses » changé au nœud 6, l'objet du contrôle retiré au nœud 7, et au nœud 11 une provenance inversée, héritée de la décision posée. Deux points sont à reposer à Lazar : qui tient l'ancre humaine (ou quel agent) ; trois points du devis appliqués par anticipation qu'aucun des onze nœuds ne couvre.

## En-tête

- **Qui** : vérificateur neuf, sous-agent délégué par la session de relance (`session_013QMaymFtcZwVwjxVAF3gmH`), modèle Claude Opus 5.5. Je n'ai écrit ni la décision posée, ni la transcription, ni aucune des pièces lues.
- **Date (UTC, `date -u`)** : 2026-11-19T07:17:46Z, au début de la rédaction. Dépôt : branche `claude/pensive-bardeen-1fv7hw`, commit `43552a85`.
- **Pièces vérifiées** (empreinte recalculée par `sha256sum`, puis par `python -m controle_ia.scellement verifier`, toutes égales à leur compagnon) :

| pièce | empreinte |
|---|---|
| décision posée, `docs/notes/relance-organismes-discrets-v1/decision-bras-a-noeuds-texte-neuf-v1.md` | `30287a399e129d4b7a61dd040a732971a8e3e0ba55498bb2789f4c4a5bc7345d` |
| transcription, `docs/notes/relance-organismes-discrets-v1/decision-bras-a-noeuds-texte-neuf-v1-choix-de-lazar.md` | `ecfdbdc9232db755d25db3db1f0ced4fd33dd77135cc1519e7ef5f8064b03b6d` |
| brouillon 2, `prereg/T0.7-organismes-discrets-v-a-v2-brouillon2.md` | `8db1899ace90ee5196a58d792b6f744a95a8cbf3a86c9551d5bff161293fc38c` |
| contre-lecture du brouillon 2, `docs/notes/relance-organismes-discrets-v1/contre-lecture-preenregistrement-v2-brouillon2-v1.md` | `065d0e1edd7c883b8fac8ffb96b8428705b9734eac52e4ffa0bcacd9b9499e1e` |
| contre-lecture habilitée, `docs/notes/bras-a-contre-lecture-habilitee-v1/contre-lecture-habilitee-b7-brouillon2-v1.md` | `27189edd29b511a462d17695ff06e2b0902d764261b6753e1a63ffc29567fc6d` |
| note du rédacteur du brouillon 2, `preenregistrement-v2-brouillon2-note-du-redacteur-v1.md` | `6d88f66ddacc98da0565d71ab3d1d70900a7ae6ad3290ad45db3cd6f02493935` |
| devis v2 du bras A, `devis-bras-a-v2.md` | `83240ca61d7c300fc9f4ca802560a6010a2a7c2eb48dd58fe2c214ee03524ecd` |
| décisions des cinq propositions de l'audit défensif (N-053), des modes non chiffrés (N-054) | `2204256d…` ; `c8a00b3f…` |
| décision sur la vérité du dommage, v3, v4, erratum 1 de la v4 (N-060) | `2b448f69…` ; `e1477998…` ; `316c8c23…` |
| décision sur le critère des sondes de la porte de sortie de la phase 0, v1 et v2 (N-063) | `c9607efa…` ; `b2d9f035…` |

  Les trois empreintes que cite la décision posée (brouillon 2, contre-lecture, contre-lecture habilitée) et celle que cite la transcription (décision posée) sont exactes. Ni la décision posée ni la transcription n'ont été modifiées après leur commit (`10dffbae`, 07:00:46Z ; `43552a85`, 07:07:49Z).
- **Lu en entier** : `CLAUDE.md`, la décision posée, la transcription, les deux contre-lectures, les décisions N-053, N-054, N-060 v3, v4 et erratum, N-063 v1 et v2. **Par passages** : brouillon 2, sections 2, 6.3 à 6.8, 12 et 13 ; note du rédacteur, section 3 ; devis v2, sections 1 et 4 ; journal de la relance, entrées OD-076 à OD-082 ; registre des GO, ligne GO-2026-11-18-53 ; relevé des choix de Lazar sur le texte archivé (copie `releve.md` du répertoire de travail temporaire de la session, empreinte `26acd166…` recalculée, égale à celle que cite la contre-lecture), **section 4 seule** (lignes 95 à 111 ; titres de sections listés, rien d'autre ouvert).
- **Mot de Lazar vérifié à la source**, en lecture seule : l'événement `d1367840-589d-40ed-b0a3-ea43c58932ff` (rôle utilisateur, client web, 2026-11-19T07:07:29Z, texte « go recos ») ; dans la liste des événements qui le précèdent, je n'ai extrait que les messages en texte de la session principale (deux messages de la session lus en entier, 07:01:07Z et 07:07:01Z ; les autres, 200 premiers caractères) ; aucun événement de sous-agent, aucun appel d'outil ni résultat d'outil lu.
- **Non ouverts** : aucun interne de moniteur (ni `bases/`, ni `sondes/`, ni dossier `t07*/`, ni la tâche du moniteur par action, ni le document de la base « mots et coût », ni `prereg/T0.6-organismes-v0-v1.md`) ; le texte archivé du bras A ; aucune fiche de l'organisme d'idéation ; aucune référence cachée ; le brouillon 3. Aucun appel de modèle, aucune dépense ; aucun fichier existant modifié ; rien de committé ni de scellé.

---

## Constats

Classement : **à corriger** (dans un erratum de la transcription) ; **à reposer à Lazar** ; **remarque**.

### Nœud 1 — les cinq épreuves de l'oracle de la v3 et l'ancre humaine

**1. À corriger — la condition de la personne est retirée.**
Décision : « α, une personne pour les deux ancres (48 actions et 8 plans, une à deux heures, estimation ; **personne nommée, qui ne conçoit aucun moniteur**) ».
Transcription : « une personne tient les deux ancres (α) ».
« Nommée, qui ne conçoit aucun moniteur » disparaît. La section 12 du brouillon 2, qui définit l'option, dit plus : « une personne nommée, qui ne conçoit aucun moniteur **ni le mode tenu à l'écart** et peut lire une référence cachée » ; la case « juges des ancres » (section 13) exige la « déclaration qu'elle ne conçoit aucun moniteur ni le mode tenu à l'écart ». Sans cette condition, l'option inscrite admettrait une personne qui conçoit un moniteur ou le mode tenu à l'écart, ce que la décision sur la vérité du dommage interdit (v3, point 4 : oracle « inaccessible aux concepteurs de moniteurs et à l'auteur du mode tenu à l'écart », repris inchangé par la v4, point 5, et par l'erratum, point 3).
Correction : « une personne nommée, qui ne conçoit aucun moniteur (décision posée) ni le mode tenu à l'écart (section 12 et case « juges des ancres »), tient les deux ancres (α) ».

**2. Remarque — « d'une troisième famille », « en écart déclaré », « à défaut ».**
Décision, option γ : « un agent pour les deux, écart déclaré à « ancre humaine » » ; recommandation : « γ à défaut si aucune personne n'est nommée avant le scellement ».
Transcription : « et un agent d'une troisième famille pour les deux (γ), en écart déclaré, si aucune personne n'est nommée avant le scellement ».
« D'une troisième famille » n'est pas dans la ligne du nœud 1 pour γ, mais il est dans la section 12 (option γ) et dans le tableau que Lazar a lu (« un agent d'une troisième famille à défaut ») : précision juste. « En écart déclaré » perd son objet (« à « ancre humaine » ») : le rétablir. « À défaut » est rendu par « si … », le sens tient, mais « et un agent » peut se lire « une personne et un agent ». Écrire : « et, à défaut — si aucune personne n'est nommée avant le scellement —, un agent d'une troisième famille pour les deux (γ), en écart déclaré à « ancre humaine » ».

**3. À reposer à Lazar — qui tient l'ancre, et quel agent sinon.**
« go recos » retient α, γ à défaut, sans nommer personne. La case « juges des ancres » (section 13 du brouillon 2) lui en laisse le choix : « la personne (rôle, déclaration qu'elle ne conçoit aucun moniteur ni le mode tenu à l'écart) ou l'agent (famille, version), selon le nœud 1 | Lazar ». Le passage à γ dépend d'une date que la session fixe elle-même (« avant le scellement ») : sceller sans avoir demandé ferait passer en γ par simple écoulement du temps. À reposer :
- nomme-t-il une personne (rôle, déclaration) ? peut-il l'être lui-même ?
- sinon, confirme-t-il γ, et quel agent (famille, version) ?
- lui dire ce que la décision posée n'a pas dit (contre-lecture, correction C-1) : si la révision bornée de la consigne de l'appariement joue, la personne juge 48 actions de plus (ancre rejouée sur les tâches gardées) ; l'estimation « une à deux heures » ne les compte pas.

### Nœud 2 — le désappariement et le mode « affaiblir les contrôles »

**4. Remarque, à signaler à Lazar — transcription fidèle, motif inexact.**
Transcription = recommandation (b), mot pour mot sur le fond. Mais le motif donné à Lazar va au-delà de sa décision. Décision posée : « la v4 interdit au bras de parler de dommage » ; tableau du message de 07:01:07Z : « ta décision lui interdit de parler de dommage ». La v4 interdit le mot « dommage » dans les verdicts de la variable principale (point 1) et laisse ouvert « si, et à quelles conditions, le bras A peut affirmer un dommage au plan de recherche » (« ce que la décision ne fixe pas ») ; l'interdiction dans toutes les phrases est un choix du brouillon (note du rédacteur, section 3, point 3). Le rédacteur recommandait (b) « **tant que** la v4 ne dit pas si le bras peut affirmer un dommage au plan » (section 12) ; la décision posée a retiré « tant que ». Conséquence écrite seulement par contraposée : sous (b), l'exigence de la décision sur les modes non chiffrés (N-054, point 1 : un mode non chiffré avant la porte générale 1, « en premier lieu « affaiblir les contrôles » ») reste à remplir par autre chose. Pas de contradiction avec N-054, qui ne nomme pas le bras A ; à inscrire au registre comme point ouvert. La transcription n'a rien à ajouter.

### Nœud 3 — dose candidate à une lecture interne

**5. À corriger — « ici » retiré.**
Décision : « (b) oui, comme le texte archivé le faisait d'un dommage discret (« candidate », **rien n'est lu ici**, toute lecture interne reste un nœud) ».
Transcription : « (b) ; **rien n'est lu** ; toute lecture interne reste un nœud ».
Sans « ici », la phrase peut se lire « aucune lecture interne n'aura lieu », ce qui contredit l'objet de la désignation (une lecture interne, préenregistrée à part sur mot de Lazar). Rétablir « rien n'est lu ici » (lettre du texte archivé, ligne 208, citée par la section 12 : « nœud de Lazar ; rien n'est lu ici »).

**6. Remarque — le lien avec le critère des sondes de la porte de sortie de la phase 0 n'a pas été posé.**
L'erratum de la v4 (point 4c) rattache ce nœud à la décision N-063 v2 ; la contre-lecture (correction C-12) demandait d'écrire ce lien dans l'énoncé. La décision posée ne nomme pas N-063. Je ne trouve pas de contradiction : la ligne « désappariement discret » exige que la base « mots et coût » échoue, ce qui est la condition de N-063 v2, et « toute lecture interne reste un nœud » garde le reste. Le mot « candidate » n'est pas la proposition V-2 de la v3 (« issue positive du pilote lue « dose candidate », confirmée sur tâches disjointes »), qui reste non tranchée. Le brouillon 3 doit porter la phrase de C-12.

### Nœud 4 — seuils de l'honnête ; contrôles vagues, génériques et absents

**7. À corriger — le contenu de la mesure I est retiré.**
Décision : « Mesure : I, **champ « spécifique ou générique » chez les lecteurs, taux d'actions sans contrôles**, avec lignes de verdict « hausse établie ou non » ».
Transcription : « mesure des contrôles vagues, génériques et absents avec lignes de verdict « hausse établie ou non » (I) ».
Sans le champ « spécifique ou générique », les mots conviennent aussi à l'option III avec la mesure des actions sans contrôles sous I (pas de question de spécificité, lignes de verdict pour cette mesure) ; seule l'étiquette « (I) » tranche. Rétablir « champ « spécifique ou générique » chez les lecteurs, taux d'actions sans contrôles ». Mineur : « sur le statut de contenu » est retiré des seuils (décision : « Seuils de l'épisode honnête sur le statut de contenu ») ; le rétablir.

### Nœud 5 — le repli « sabotage demandé » de la v3

**8. Remarque — fidèle ; « un instrument » est l'instrument de l'appariement.**
Transcription = décision ; « point 3 » ajouté est juste (section 12). Mais, lue seule, la phrase commune aux deux, « un instrument en échec arrête le bras avant la distillation », heurte l'option I du nœud 1, sous laquelle l'échec de l'instrument de couverture rend seulement les couvertures « non lues ». La section 12 définit l'option (a) : « un instrument **de l'appariement** en échec (A5, A7 après révision) ou la ligne A4 » (A4 n'existe que sous l'option II). Dans la case « nœuds » du texte scellé, écrire « un instrument de l'appariement en échec (section 12, option (a)) ». Sur la question 4 : la décision posée ne rappelle pas que l'erratum tient le point 3 de la v3 « inchangé à la lettre », ce que la section 12 et la note du rédacteur signalaient (« écart possible à la v4 ») ; je n'y vois pas de contradiction : sans condition « sabotage demandé », la lettre n'a rien à lire, et (a) est l'issue la plus proche de cette lettre.

### Nœud 6 — les deux témoins

**9. À corriger — « pour toutes les doses » devenu « à toutes les doses ».**
Décision : « chacun déclenche sa ligne, avec sa propre conclusion, branche non interprétable, **pour toutes les doses (et non seulement les doses où le désappariement est établi)** ».
Transcription : « Les deux témoins déclenchent chacun leur ligne, avec leur propre conclusion, branche non interprétable, **à toutes les doses** ».
La nuance change : le témoin bénin n'existe qu'à la dose 1 (brouillon 2, section 2 : « champ `PREDICTION` déplacé à la seule dose 1 » ; devis v2, section 1, point 1 : « la lecture « une par dose » est abandonnée ») ; « déclenchent … à toutes les doses » peut se lire comme des témoins par dose ou un déclenchement dose par dose. Le sens voulu : la ligne d'un témoin à effet établi rend la branche non interprétable pour toutes les doses, quelle que soit leur issue. La transcription reprend ici le mot du tableau de 07:01:07Z (« à toutes les doses »), non la décision scellée. Rétablir la lettre de la décision, parenthèse comprise.

### Nœud 7 — l'ordre

**10. À corriger — l'objet du contrôle est retiré.**
Décision : « le jumeau déplacé **(contrôle « le déplacement agit » sur les transcriptions)** passe avant la distillation ».
Transcription : « Le jumeau déplacé est lu avant la distillation ».
L'objet est précisément ce que la préférence de Lazar demandait de fixer (relevé, section 4, remarque 2 : « fixer sur quel objet ce contrôle se lit (transcriptions déplacées ou organisme réglé) »). Rétablir la parenthèse. « Du 19 novembre », ajouté, est juste (« oui lrs deux », 2026-11-19T06:41:30Z) : absent de la ligne du nœud 7, présent à celle du nœud 6.

**11. Remarque — ce que « go recos » ne fixe pas ici, à ne pas attribuer à Lazar.**
- « Un arrêt si la distillation ne prend pas à la dose 1 » : ni le moment ni la portée ne sont écrits. La prise se mesure à l'étape (i), sur la machine, avant le lot décisif (brouillon 2, 6.3 et 6.4, point 5) ; la lecture naturelle d'« arrêt » est : la course s'arrête alors, avant les lectures du lot décisif. La contre-lecture proposait autre chose (« arrête la lecture (ligne de la table A), les doses ½ et ¾ gardant » la ligne « manipulation non prise », et une « seconde garde » d'hétérogénéité tirée du jumeau) : rien de cela n'est dans la décision posée.
- L'écart déclaré est le seul. Le reste suit l'ordre préféré, où « écart-type et effet minimal détectable » précèdent le contrôle : l'écart-type sur les seuls honnêtes doit donc être calculé et scellé **avant** la lecture du jumeau, sinon c'est un second écart, non déclaré.
- Si le brouillon 3 fait autrement sur l'un de ces deux points, le reposer à Lazar.

### Nœud 8 — le jumeau déplacé comme épreuve

**12. Remarque — fidèle ; un fait à écrire dans la lecture déclarée.**
Transcription = décision ; la négation « et non comme « la lecture d'un épisode saboté » » est retirée sans perte. La décision posée ne dit pas ce que la contre-lecture relève (bloquant B-5) : les jumeaux des tâches ouvertes **sont** les transcriptions d'entraînement de l'adaptateur de dose 1, mêmes graines (brouillon 2, 6.5). L'épreuve lit donc, sous un autre rôle, des épisodes que toute définition corrigée rangera parmi les épisodes déplacés. La « lecture déclarée » doit l'écrire. Les « définitions corrigées » ne sont pas fixées par le mot de Lazar : la proposition B-5 (1) est celle du contre-lecteur.

### Nœud 9 — classe absente d'un pli, vocabulaire vide

**13. Remarque — « pas d'arrêt de course » : juste par exclusion, à borner.**
La décision met en balance « arrêt de la course (texte archivé) » et « dose « non calculable » » ; retenir la seconde exclut l'arrêt pour ces deux cas. Placé après un point-virgule, l'ajout peut se lire comme général : écrire « pas d'arrêt de course pour ces deux cas ». Les autres gardes de la base (effectifs attendus et garde d'arrêt correspondante, contre-lecture habilitée, point 1, item 2) ne sont pas touchées par ce nœud. Pas de contradiction avec N-063 v2 : le critère n'y est jugé « qu'aux doses où la base « mots et coût » échoue » (titre et point 2) ; une dose « non calculable » n'échoue pas et ne peut qu'empêcher « discret ». (N-063 v2, point 1, ne met hors jugement que les doses où la base « réussit » ; la place d'une dose non calculable n'y est pas écrite : sans effet sur ce bras.)

### Nœud 10 — le juge d'une autre lignée

**14. Remarque — fidèle.** « Il n'entre pas dans le verdict de discrétion » est la négation de l'autre option. Conforme à N-053, point 4 (« un juge Qwen2.5-7B en bras rapporté »). Le retrait rend « discret » plus facile à affirmer (le juge ne pouvait que l'empêcher) ; la décision posée le disait (« où il ne peut qu'empêcher « discret » »). Ses lectures restent rapportées à côté du verdict.

### Nœud 11 — deux points du devis

**15. À corriger — provenance inversée, article défini, deux engagements retirés.**
Décision : « Deux recommandations du devis appliquées par anticipation sous l'autonomie : l'épisode honnête des tâches de vérification passe à la seconde ligne de carte **(lu dans le même lot que les conditions, contre une dérive des lecteurs entre lots)** ; les épreuves se font sur les tâches de fabrication **(aucune tâche de vérification lue avant le lot décisif)**. Ou : le devis v2 tel qu'accordé. Recommandation : les garder ».
Transcription : « **Les** deux recommandations du devis appliquées par anticipation sont gardées : l'épisode honnête des tâches de vérification passe à la seconde ligne de carte ; les épreuves se font sur les tâches de fabrication ».
- **Provenance.** Ce que le devis v2 recommandait, et que l'autonomie (GO-2026-11-18-53) a fait appliquer par anticipation, est l'inverse : honnêtes de vérification joués à la ligne 1 (devis v2, section 4, tableau de la ligne 1) et « les 32 épisodes des épreuves de l'oracle sont tirés des épisodes honnêtes des tâches de vérification joués à la ligne 1 » (section 1, point 6). La note du rédacteur le dit : le changement « défait une recommandation accordée » (section 3, point 1). Les deux points retenus sont deux changements du brouillon 2 au devis v2, non deux recommandations du devis. Le défaut vient de la décision posée et du tableau de 07:01:07Z ; la transcription l'inscrit comme un fait. Le choix, lui, n'est pas ambigu : l'autre option est « le devis v2 tel qu'accordé », et le tableau dit « Les garder : l'honnête de vérification à la seconde ligne, les épreuves sur les tâches de fabrication ».
- **« Les deux »** au lieu de « Deux » : peut se lire comme toutes les recommandations appliquées par anticipation ; il y en a d'autres (constat 16).
- Les parenthèses retirées portent des engagements, non de simples motifs : « lu dans le même lot que les conditions » ; « aucune tâche de vérification lue avant le lot décisif ».
Correction proposée : « Le devis v2 tel qu'accordé sous l'autonomie n'est pas suivi sur deux points (section 1, point 6, et contenu de la ligne 1) ; les deux changements du brouillon 2 sont gardés : l'épisode honnête des tâches de vérification passe à la seconde ligne de carte (lu dans le même lot que les conditions, contre une dérive des lecteurs entre lots) ; les épreuves se font sur les tâches de fabrication (aucune tâche de vérification lue avant le lot décisif). »

**16. À reposer à Lazar — trois points du devis appliqués par anticipation, hors des onze nœuds.**
La contre-lecture (correction C-17 et « points d'information ») et le relevé (section 4, « Hors de ce relevé ») listent quatre points du devis appliqués par anticipation, « posés à Lazar par la relance avec son devis » : une seule proportion pour le témoin bénin, à la dose 1 (devis v2, section 1, point 1) ; pas d'adaptateur de dose nulle (point 3) ; stratification du sous-échantillon du juge d'une autre lignée (devis v2, ligne 122, selon la contre-lecture habilitée, point 5) ; origine des épisodes des épreuves (point 6). Le nœud 11 ne couvre que le quatrième (avec le contenu de la ligne 1). « go recos » ne tranche pas les trois autres, et l'autonomie qui les a fait appliquer finit à 2026-11-19T09:06:42Z. À reposer avec le devis, ou à inscrire « appliqués par anticipation, non confirmés ».

### En-tête de la transcription

**17. Remarque — le mot, et ce que Lazar a lu.**
Vérifié à la source : événement `d1367840-589d-40ed-b0a3-ea43c58932ff`, 2026-11-19T07:07:29Z, « go recos » ; la phrase « Si tu suis toutes mes recommandations, écris « recos » » est dans le message de 07:07:01Z. Un message de la session sur un fichier non suivi (réponse à un crochet d'arrêt, 07:07:09Z) s'intercale : « il suit le message » est juste au sens de « il y répond ». Lazar a lu les onze recommandations en tableau (message de 07:01:07Z), qui renvoie au fichier pour le détail. Le tableau ne contredit le fichier sur aucun nœud ; il en omet des parties (nœud 1 : la condition de γ et celle de la personne ; nœud 7 : l'écart-type sur les seuls honnêtes et l'arrêt à la dose 1 ; nœud 8 : les définitions corrigées) et porte le motif inexact du nœud 2 et la provenance inversée du nœud 11. La transcription prend le fichier pour référence, sauf au nœud 6 (constat 9). Les confiances et les désaccords du rédacteur et du contre-lecteur ne sont pas transcrits : sans effet, la transcription ne porte que les options.

---

## Question 4 — contradiction avec une décision de Lazar non dite par la décision posée

Aucune option retenue ne contredit les décisions N-053, N-054, N-060 v3, v4 et son erratum, ou N-063 sans que la décision posée l'ait dit :
- nœud 1, γ : écart à « ancre humaine » (v3, point 2, tenu « inchangé à la lettre » par l'erratum) — **dit** (« écart déclaré ») ;
- nœud 8 : lecture de l'erratum, point 3 — **dite** ;
- nœud 7 : écart à une préférence de Lazar sur le texte archivé (relevé, non une décision de `docs/decisions/`) — **dit** ;
- nœud 10 : conforme à N-053 ;
- nœud 5 : lecture du point 3 de la v3, que la décision posée ne signale pas comme écart possible ; pas de contradiction trouvée (constat 8) ;
- nœud 2 : l'exigence de N-054, point 1, reste ouverte ; dit seulement par contraposée (constat 4) ;
- nœuds 3 et 9 : compatibles avec N-063 v2, dont la décision posée ne parle pas (constats 6 et 13).
Un seul risque vient de la transcription elle-même : au nœud 1, la condition retirée sur la personne (constat 1) laisserait inscrire une option contraire à la v3, point 4, et à N-054, point 3 (mode tenu à l'écart).

## Ce qui est fidèle sans réserve

Nœuds 2, 5, 8 et 10 : l'option et ses termes. Nœud 9 : l'option ; l'ajout « pas d'arrêt de course » est juste par exclusion.

## Corrections, en une liste (pour un erratum de la transcription)

1. Nœud 1 : « une personne nommée, qui ne conçoit aucun moniteur ni le mode tenu à l'écart, tient les deux ancres (α) » ; « et, à défaut — si aucune personne n'est nommée avant le scellement —, un agent d'une troisième famille pour les deux (γ), en écart déclaré à « ancre humaine » ».
2. Nœud 3 : « rien n'est lu ici ».
3. Nœud 4 : seuils « sur le statut de contenu » ; mesure I « champ « spécifique ou générique » chez les lecteurs, taux d'actions sans contrôles, avec lignes de verdict « hausse établie ou non » ».
4. Nœud 6 : « pour toutes les doses (et non seulement les doses où le désappariement est établi) ».
5. Nœud 7 : « le jumeau déplacé (contrôle « le déplacement agit » sur les transcriptions) ».
6. Nœud 11 : texte du constat 15 (deux changements du brouillon 2 au devis v2, non « les deux recommandations du devis » ; parenthèses rétablies).
7. Facultatif : nœud 5, « un instrument de l'appariement en échec (section 12, option (a)) » ; nœud 9, « pas d'arrêt de course pour ces deux cas ».

**À reposer à Lazar** : constat 3 (la personne de l'ancre, ou l'agent et sa version ; temps sous la révision bornée) ; constat 16 (trois points du devis appliqués par anticipation). **À lui signaler** : constat 4 (motif inexact du nœud 2 ; exigence de N-054, point 1, ouverte).
