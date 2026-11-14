# Vérification courte du différentiel candidat 2 → candidat 3 — préenregistrement du pilote MR-2 (v1)

**Lecteur** : modèle E, lecteur neuf, autre modèle que le rédacteur (modèle A). Je n'ai écrit aucun des textes lus.
**Texte relu** : `preenregistrement-pilote-conditionnelles-v1-candidat3-compte-organisme.md`, sha256
`539cf171739ee9649719c7c851ebbf8e721e8f225b71ef5ec57ac44e0f8755a6` (égal à son compagnon `.sha256`). Base : candidat 2,
`640b2f556108647d4af362ac4d1aae652d0453b4c7fa7455987038cd2ed5c797` (conforme à l'attendu).
**Heures** (`date -u`) : début 2026-11-14 13:44:56 UTC ; fin 2026-11-14 13:47:00 UTC.

## Verdict

**Scellable après la phrase de Lazar sur les prix** : aucun constat bloquant ni majeur ; quatre constats mineurs, dont deux
corrections de mots recommandées avant le scellement (constats 1 et 2) ; rien ne touche la lecture du pilote (issue, seuil, règle
P-0/P-1/P-2). Le seul marqueur restant est [PRIX-CONSOLE], qui attend la phrase de Lazar.

## Points a à h

**a. Hors des passages réécrits, le candidat 3 reprend le candidat 2 mot pour mot : conforme.** J'ai regénéré le différentiel
(`diff -u`, deux premières lignes d'en-tête exclues) : il est identique au fichier `differentiel-candidat2-candidat3.patch`
(empreinte `6889c487…`, 14 blocs). Tout ce qui diffère est dans le patch ; je l'ai lu en entier. Les blocs touchent : titre et statut ;
nouvelle table « Changements depuis le candidat 2 » ; « Documents qui font foi » (lignes ajoutées, relevé v72 « à jouer » remplacé) ;
« En dix lignes » 9 et 10 ; Dessin (identifiants, bornes) ; Ordre ; Métrique (réflexion et coût) ; Plan d'analyse (lanceur v74) ;
Liste d'arrêt (sonde v74, ligne « sans réflexion », phrase R-2727) ; Code (v74, bloc) ; Préalables ; Devis ; Lignes de GO ;
Contre-lecture ; Marqueurs ; heures. Aucune modification des sections non annoncées au fond. Écart de forme : la table
d'historique n'annonce pas Ordre, Plan d'analyse, « En dix lignes », Contre-lecture ni les heures (constat 4, mineur).

**b. Bloc gelé : conforme.** Par programme : le texte entre `<!-- empreintes-du-code-pilote-v74 : début -->` et `… : fin -->`
inclus, plus un saut de ligne, est égal octet pour octet au fichier `bloc-releve-sonde-complete-v74.txt` (5 320 octets de part et
d'autre ; un seul début, une seule fin). Empreinte du fichier : `8b5dcfe7a9f8e382469fc4638a2cbf18a99e1a9d8f449ffe5bf02e543f6618ec`
(conforme). Il porte l'empreinte du relevé `f56d9c0e…` et ne porte aucun identifiant de modèle.

**c. Lignes de GO de la sonde : conforme.** Les lignes 329 et 330 du fichier `go-main-6db34425.md` (empreinte
`809e6a0b27cb76adffb21de79fdd0a2299e5407761b1ee1ea1820524a7e08d4b`, conforme) sont chacune présentes une fois, mot pour mot, dans le
candidat 3 (l. 616 et 617), et égales aux deux lignes de `lignes-sonde-v74-inscrites.txt`.

**d. Chiffres neufs : conforme.**
- Dépenses recalculées depuis les `cout_usd` des huit appels : `fable52` 0,008104 + 0,010624 = 0,018728 ; `opus55` 0,004192 +
  0,005312 = 0,009504 ; `argon` 0,04039 + 0,01341 = 0,0538 ; `astra` 0,00398 + 0,01312 = 0,0171 ; lignes s1 0,028232 et s2 0,0709 ;
  total 0,099132 = `depense_usd` du relevé. Le total est mot pour mot celui du journal (PO-033). Le pire cas 8,052896 et les lignes
  4,39 / 3,68 sont ceux du devis ; « ≈ 15,00 » = 14,90 + 0,099, cohérent. 0,079262 (sonde v73) et 0,0167 viennent du journal (PO-024) : non
  recalculables ici (relevé v73 hors de ma liste).
- Heures : `debut_utc` 13:38:30, `fin_utc` 13:39:09 : conformes ; code 0 et registre des lancements : journal PO-033.
- Jetons de `argon` : borne gelée, réflexion (`thoughtsTokenCount`) 786, sortie visible 8, entrée 69, total 863 = 69 + 8 + 786 ;
  borne courte, entrée 61, sortie 256, total 317, aucun champ de réflexion : conformes. `astra` : réflexion 61 sur 72 (appel à la
  borne gelée), 256 sur 256 (borne courte) : conformes.
- Empreintes entières recalculées par `sha256sum` : relevé `f56d9c0e…` ; bloc `8b5dcfe7…` ; paquet `1cda2feb…` ; rapport du développeur
  `59d4db3d…` ; contre-lecture `d82de053…` ; relecture courte `895e776c…` ; devis `0426930a…` ; candidat 2 `640b2f55…` : toutes égales
  à celles du candidat 3. Non recalculables (fichiers hors de ma liste) : `35afab77…`, `40eb7b32…`, `2b4017c7…`.
- Conclusions : pour les quatre relais, `statut`, `usage_entier`, `modele_servi_conforme`, `borne_gelee_admise`,
  `borne_courte_tronquee`, `borne_tenue`, `raison_arret_normale`, `verdict_egal_a_la_regle` sont vraies ;
  `reflexion_observee` vraie pour `argon` et `astra` ; `au_dessus_du_pire_cas` fausse pour les quatre ; `reflexion_sans_effet`
  fausse pour `argon` et absente des trois autres : aucun proposeur « sans réflexion ». `partiel` faux, `arret` nul. Les deux
  verdicts de réflexion dits (`argon` « non comprise », `astra` « comprise ») sont ceux du relevé ; `fable52`, `opus55` « sans champ ».
  Observation : `regle_configuree` est fausse pour `argon` ; c'est l'écho de sa règle configurée (« non comprise »), pas une
  exigence (le code l'a admis, bloc rendu avec le code 0, journal PO-033) ; je n'ai pas lu le module de la sonde pour le confirmer.

**e. Marqueurs : conforme.** Hors de la table « Changements depuis le candidat 1 » (ligne 54 : [DATE-GO], [MOT-LAZAR-GO], histoire),
les seuls marqueurs entre crochets sont [PRIX-CONSOLE] (Devis l. 599, table des marqueurs l. 687). Les marqueurs levés (BLOC-GELE-V73,
RELEVE-SONDE-V72, GO-S1, GO-S2, DATE-GO, MOT-LAZAR-GO) n'ont laissé aucun trou : bloc, empreinte du relevé et lignes sont en place.

**f. Cohérence interne : conforme, avec un reste (constat 1).** Plus aucun « lanceur v73 gelé », « sonde v72 » à jouer ni « code v73 »
gelé hors des tables d'historique et de la table « Documents » (qui garde le paquet v73 comme pièce, à côté de la ligne v74). Les
sections Ordre (l. 314, 321), Plan d'analyse (l. 391), Liste d'arrêt, Code (l. 470 à 489), Préalables, Lignes de GO (π1, l. 623) et
Devis nomment le lanceur ou le module v74. Reste : l'en-tête de la table des proposeurs (l. 273) dit encore « règle gelée, à confirmer
par la sonde ».

**g. Décisions citées : conforme, sans ajout qui touche la lecture.** R-2727 option (a) : message PO-023 (« la phrase de fin de
liste d'arrêt est gardée, option (a) ») ; fidèle. R-2731 : PO-025 (relevé et réponses brutes restent sur la branche, jamais recopiés
tels quels dans `main`) ; fidèle. R-2738 : PO-026 (état « aucune réflexion cachée » = aucun champ de réflexion aux deux appels et
total égal à entrée plus sortie ; pilote arrêté si un champ apparaît ; ajouts seuls) et mot de Lazar PO-025 « Option (a) : code v74,
réflexion absente sans effet » ; fidèles. Le verbatim de la ligne -10 (« Recommandation : (a), confiance 0,7. : go ») est celui de
PO-031. La réserve de variabilité d'`argon` est celle de PO-034. Rien dans les ajouts ne touche l'issue, le seuil ni la règle
P-0/P-1/P-2 : ils portent sur le comptage de la réflexion, le coût, la liste d'arrêt et les marqueurs. Seule précision : constat 3.

**h. Identifiants de modèle : conforme, avec une réserve de mot (constat 2).** Aucun identifiant de modèle (aucun « claude- »,
« gemini- », « gpt- » ni numéro de version) dans le candidat 3 ; les proposeurs sont nommés par leurs clés. Le texte contient « le
modèle Fable » (l. 675), nom de famille, non un identifiant.

## Constats

Bloquant : 0. Majeur : 0. Mineur : 4.

1. **Mineur — mot périmé, l. 273.** L'en-tête « réflexion comptée dans la sortie (règle gelée, à confirmer par la sonde) » est dit
   avant la sonde ; elle est jouée et a confirmé les règles. Correction : « (règle gelée, confirmée par la sonde v74) ».
2. **Mineur — nom de famille de modèle, l. 675.** « jamais sur le modèle Fable avant le 20 novembre 15:00 UTC » nomme une famille, ce
   que le candidat dit éviter (« aucun identifiant de modèle dans ce texte »). Correction : « jamais sur le modèle du proposeur
   `fable52` » (clé de configuration) ou « jamais sur la lignée de `fable52` avant … ».
3. **Mineur — précision, l. 444 à 447.** La ligne « sans réflexion » arrête le pilote pour trois causes : champ de réflexion, réflexion
   comptée non nulle, total d'`argon` différent de entrée + sortie. Le message R-2738 ne cite que le champ de réflexion ; les deux
   autres viennent du code v74 (rapport du développeur, §2 : jalon 3). Elles ne touchent pas la lecture (arrêt sans issue, liste de
   proposeurs vide à ce relevé). Correction : ajouter « (conditions du code v74, rapport du développeur §2 ; R-2738 ne nomme que le
   champ) », ou laisser tel quel et le dire à la mère.
4. **Mineur — table d'historique incomplète.** La table « Changements depuis le candidat 2 » n'annonce pas Ordre, Plan d'analyse,
   « En dix lignes » 9 et 10, la section Contre-lecture, ni l'heure de rédaction ; le patch les montre, tous cohérents avec le reste.
   Correction : une ligne « autres mots : lanceur v74, état fait/à faire, heures » ; non nécessaire au scellement.

Observation sans classe : les heures de rédaction début et fin sont identiques (13:44:01) ; le fichier a été écrit à 13:44:16.
