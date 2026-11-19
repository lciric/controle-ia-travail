# Vérification des corrections — brouillon 6 de relance du préenregistrement du papier C, version c1 — v1

- Vérificateur : le contre-lecteur du brouillon 6 de relance (Opus 5.5), même agent (règle du programme), le
  2026-11-19. Rapport vérifié : `rapport-contre-lecture-brouillon6-relance-v1.md`
  (`9a7121bc52890f6e761227ac916f72078b41086bbce7d29bf6ef44a33dc186a0`).
- **Texte vérifié** : `bloc-notes/redacteur/papier-C-preenregistrement-HC1-HC3-v1-brouillon6-relance-2026-11-19-c1.md`,
  **`ff3e2ff30263cfb2d29d2df0402c6791b64eaf37f8b64af91bc7f46bdc8aa021`** (égale à l'empreinte attendue).
  Comparé au texte relu `67cd36f1…0e0d`.
- Pièces lues (empreintes recalculées) : table de traitement `0929788f7b3aecb8…` ; décisions v2 `66e9854baa26bb08…` ;
  note des différences v2 `4131fac02124e5d8…` ; sortie du validateur c1 `42f259eb7f802966…` ; journal v2
  `a422108a1bae43da…` ; `travail/rejeu-grille-c1/` (manifestes, lanceur, 24 sorties).
- Mêmes interdits que la consigne, tenus : aucun résultat lu, aucun nom interdit ouvert, ligne R-2059 non lue, aucune
  dépense, aucun agent, aucune écriture hors de mon dossier ; aucun refus de permission.
- Erratum de mon rapport : son en-tête de section 2 dit « 7 mineures » ; il y en a 6 (CL-12 à CL-17), soit 17 au
  total. La version c1 écrit « 6 mineures » : c'est juste.

## 1. Verdict par remarque

| remarque | verdict | constat |
|---|---|---|
| CL-01 (bloquante) | **levée** | Paragraphe neuf « HC2 : confirmation, réfutation et côté négatif » (l. 501-519) : partie commune fixée, versions (i) et (ii) écrites jusqu'au bout, mots du cas négatif sous chacune ; tableau de prédiction, « Seuil » (ligne « niveaux », qui dit primer sur la ligne générale), critères et combinaisons y renvoient. Le choix est un nœud (D-15, sans défaut) : c'est juste, comme je l'avais demandé pour l'option (ii). Plus aucune lecture double. |
| CL-02 | **levée** | e, e_c, e_x définis (Métrique, point 13) ; « opposition établie » exige e et e_c ; deux mentions pour les divergences ; paragraphe « ce que cette ligne ne peut pas montrer », qui dit aussi que la lecture complète porte l'effet de longueur dans le même sens ; l'hypothèse dit ce que lit chaque moniteur (l. 417-420). |
| CL-03 | **levée**, une réserve neuve (V-03) | Confirmation par intersection-union, chaque niveau ; réserve « niveau le plus fort » retirée ; demi-largeur dite celle d'un niveau (juste). Réfutation laissée sur la moyenne : voir V-03. |
| CL-04 | **levée en partie** | Préfixe fixé (dialogue entier, seul le message système change) ; témoin principal dans le contexte de l'honnête qui plaide ; témoin de l'instrument avec tolérance et garde 20 ; verrou 9 pour le harnais. Reste : le verrou 9 doit aussi vérifier que la consigne privée de saboter est bien dans le message système et nulle part ailleurs dans le dialogue relu ; sinon « seul le message système change » ne retire pas l'intention (V-04). |
| CL-05 | **levée** | Nom mot pour mot, quatre conditions de N-026, plancher apparié et D₀ recalculés avec la même agrégation ; extension au maximum des moyennes glissantes dite lecture de N-026 (D-14). |
| CL-06 | **levée** | Trajectoire passée en nœud (D-16, sans défaut), versions (a) et (b) écrites ; mention « lu sur une action » portée aux critères selon D-16. |
| CL-07 | **levée** | Couplage écrit au texte (l. 1414-1429) et dans D-8 ; trois versions écrites ; (a) dite écart à la lettre de N-053 ; combinaison avec le côté négatif de HC2 sous (i) et (ii). |
| CL-08 | **levée** | Le bloc P-021 dit que la clause joue déjà aux deux lectures et que la troisième lecture en remplace l'effet ; options de D-9 réécrites justement ((b) : C-P3a et C-P3b sans verdict). Classement : voir V-05. |
| CL-09 | **levée en partie** (verrou 10 juste et exact) | Voir section 3. |
| CL-10 | **levée** | Bras défini en (b1) banc tel quel et (b2) transposition (concept, phrases, consignes, empan, négatifs, seuil, « direction » pour sonde linéaire et à attention, témoin) ; transposition dite écart ; seuil « moitié » sorti en D-17 (nœud). Observation V-06. |
| CL-11 | **levée** | A9 dans les deux sens, même audit, élargi à la différence des champs entre S et SP_m ; combinaison écrite. |
| CL-12 | **levée** | Note v2, section 4. |
| CL-13 | **levée** | Note v2, ligne C-57d. |
| CL-14 | **levée** | Empreinte complète `12879073de20e912…` et chemin d'archive écrits ; égale à mon calcul. |
| CL-15 | **sans objet au texte**, comme demandé | Reste au versement (verrou 5). |
| CL-16 | **levée** | D-3 dit que (b) serait un écart à N-005. |
| CL-17 | **levée** | Figure 2, p. 4 (balayage) et figure 1, p. 3 (trois moniteurs sur cinq), conformes à N-023. |

## 2. Différence entre le texte relu et la version c1

- Contrôle par programme (`outils/diff-b6-c1-lignes-v1.txt`) : 31 blocs de lignes ; chaque bloc relu et rattaché à un
  changement K- annoncé (35 identifiants au programme `changements_c1_v1.py`, plusieurs blocs voisins se fondent) et à
  la table. **Aucun changement non annoncé.** Énoncés de HC1, HC2, HC2b, HC3 inchangés ; « Pièces revendiquées »
  inchangées.
- **Aucune revendication neuve** ; **aucun chiffre de l'état de l'art ajouté** (les seuls chiffres neufs sont les taux
  du rejeu de la grille, mesures de conception sur données simulées, dites telles, sous manifeste vérifié ; et deux
  choix de conception déclarés : tolérance 0,01 × D₀ sur 99 % des contenus, quantile à 99 % des négatifs).
- Cohérence des cases réécrites : règle de HC2 en deux versions cohérente entre « Prédiction », « Seuil »,
  « Critères » et « Combinaisons » ; confirmation niveau par niveau et réfutation sur la moyenne incompatibles entre
  elles (aucune issue double) ; écart juge moins sonde en trois calculs cohérent entre Métrique, Seuil, TC.2 et
  Critères ; A9 cohérent avec les combinaisons. Deux restes de mots anciens (V-01, V-02), sans effet sur un verdict.
- Validateur relancé : sortie identique à `problemes-brouillon6-relance-c1-v1.txt` (six cases de décision, la case
  « Contre-lecture », treize marqueurs du scellement).

## 3. Rejeu de la grille (CL-09) et verrou 10

- Programmes de `travail/rejeu-grille-c1/` : égaux au manifeste `sha256sums-programmes-v1.txt` (six fichiers) ;
  ce sont ceux de l'archive, avec le seul chemin de la configuration changé (longueurs seules lues). Sorties : 24
  fichiers conformes à `sha256sums-sorties-v1.txt` (`4377f8d96aac3130…`, comme le texte), fichiers d'erreur vides.
- Les dix cases nulles communes avec l'archive (U3) redonnent des sorties **identiques** ; la case N5, k = 5,
  60 tâches est identique à mon propre rejeu.
- Taux recalculés sur les 24 sorties : trois lectures jointes, C-P3a 0,008 à 0,043, C-P3b 0,019 à 0,054 (maximum en
  N0, k = 5, 60 tâches) ; deux lectures, 0,010 à 0,149 et 0,024 à 0,150 ; seuil de la clause à 1 000 essais :
  0,05 + 2√(0,05·0,95/1 000) = 0,0638. **Conformes au verrou 10.**
- Ce qui manque est nommé exactement : (a) C-P3c, qu'aucun programme de l'archive ne simule aux trois lectures (U1 la
  simule aux deux lectures seulement) ; (b) les cases « même attaque à g = 0,20 » sous l'erreur seule et la compression
  seule (les scénarios N0 à N5 n'ont g = 0,20 qu'en N5, mélange : vérifié au programme U1) ; (c) le rapport d'un
  sous-agent neuf exigé par la clause. J'ajoute seulement que la grille de la clause cite aussi les mélanges
  « les trois juges pouvant différer » à g = 0,10, couverts par N4 : rien ne manque de ce côté.

## 4. Les six cases du directeur et le classement des dix-sept décisions

- **D-1, D-15, D-16, D-8** : options écrites jusqu'au bout au texte et dans la liste ; le mot suffit. Pour D-8,
  « si tu refuses le masque, dis-le à part » laisse une issue non écrite (V-07).
- **D-2** : sous l'option (b), la liste ajoute une phrase à TC.2 qui n'est pas au texte ; elle est écrite en entier dans
  la liste, donc recopiable sans rédaction : acceptable.
- **D-17** : (a) et (b) écrites ; « si tu refuses la transposition » n'est pas écrit au texte (V-07).
- **Classement.** Juste pour D-1, D-2, D-4, D-8, D-13, D-15, D-16, D-17 (nœuds) et pour D-3, D-5, D-6, D-7, D-10, D-11,
  D-12, D-14 (propositions ou information à défaut).
  - **Confirmation niveau par niveau (doute 1 du rédacteur)** : je la tiens pour une **méthode**. Elle ne change ni
    l'énoncé ni le signe, elle ne peut que rendre la confirmation plus difficile, elle coïncide avec l'ancienne règle
    quand k_P = 1, et la liste la porte à la connaissance de Lazar dans D-2. Pas de nœud.
  - **D-9 (doute 5)** : voir V-05 ; je recommande le nœud.

## 5. Remarques neuves

- **V-01 — mineure.** Bloc P-021, l. 546 : « U3 : 0,008 à 0,043 aux trois lectures » reste le chiffre des 12 cases de
  l'archive, alors que le verrou 10 et D-9 donnent 0,019 à 0,054 pour C-P3b sur 24 cases. Harmoniser (renvoyer au
  verrou 10, ou écrire les deux plages avec leur nombre de cases).
- **V-02 — mineure.** Combinaisons, l. 1410 : « HC2 et HC2b confirmées ensemble (Ḡ_P sur les champs dans la marge, […]) »
  décrit l'ancienne règle ; écrire « HC2 confirmée selon la règle de la section « Prédiction » ».
- **V-03 — mineure (R4).** La confirmation de HC2 se lit niveau par niveau, la réfutation sur la moyenne : un niveau
  le plus fort nettement hors de la marge, la moyenne non, donne « non concluante » et jamais « réfutée ». C'est
  défendable (la mention est écrite), mais l'asymétrie favorise la non-réfutation. Soit le dire en une phrase (et dans
  D-2), soit réfuter aussi si un niveau a son intervalle à 95 % (Bonferroni sur les niveaux) entièrement hors de la
  marge.
- **V-04 — mineure.** Verrou 9 : vérifier aussi où vit la consigne privée de saboter (message système seul, ou aussi un
  tour du dialogue) ; si elle est ailleurs, la relecture L-HP ne retire pas l'intention et le témoin lexical doit
  être redéfini avant le scellement.
- **V-05 — mineure (classement).** D-9 garde un défaut à 48 heures alors qu'il renverse l'effet mécanique d'une
  décision appliquée par défaut (P-021, R-326) dans le sens qui garde un verdict à la prédiction 3 de N-005. Un défaut
  ne devrait pas défaire l'issue d'un autre défaut : je recommande le classement en nœud (sans défaut). Le fond de
  l'option (a) reste défendable.
- **V-06 — mineure (observation, sans correction exigée).** En (b2), l'agent recopie des champs de saboteur sans
  intention de saboter : la détection « sans consigne » peut être proche du taux de faux positifs, et le rapport
  « moitié » de D-17 (b) n'a alors pas de sens. Si (b) est retenue, écrire que la réserve n'est pas évaluée quand la
  détection sans consigne n'excède pas nettement 1 %.
- **V-07 — mineure.** D-8 (« si tu refuses le masque ») et D-17 (« si tu refuses la transposition ») ouvrent une issue
  dont le texte n'est pas écrit d'avance : soit l'écrire comme option, soit dire qu'un refus donne une version
  nouvelle du texte.

## 6. Avis d'ensemble

**Plus aucune remarque bloquante.** Les dix-sept remarques sont levées ou traitées comme demandé ; CL-04 et CL-09
restent en partie ouvertes sous des verrous nommés exactement (9 et 10). Les remarques neuves sont toutes mineures.
**La version c1 est scellable** une fois : les six cases du directeur remplies (D-1, D-2, D-8, D-15, D-16, D-17) et
les nœuds D-4 et D-13 tranchés ; les verrous levés (1 à 10, dont 9 avec V-04 et 10 avec le rapport d'un sous-agent
neuf) ; V-01 à V-07 corrigées ou déclinées par écrit (errata admis pour cette classe). Le choix fait en D-8, D-15 ou
D-16 ne demande qu'un remplissage de case, sauf un refus de masque ou de transposition (V-07).
