# Papier C — points ouverts pour le directeur après le brouillon 7 de relance du préenregistrement — v1

Date : 2026-11-22. Auteur : rédacteur du brouillon 7 de relance (session fille `session_013QMayk1rjSZrn2u9UAVhEp` ;
modèle : ligne 323 de `registres/qui-a-lu-quoi-v19.md`). Classe C. Accords : GO-2026-11-22-77, GO-2026-11-22-113. Aucune dépense, aucun résultat lu.
Texte visé : `brouillons/papier-C-preenregistrement-HC1-HC3-v1-brouillon7-relance-2026-11-22.md` (empreinte : son
compagnon `.sha256`).

**En une phrase.** Les vingt décisions D-1 à D-20 sont tranchées et portées ; ce brouillon ajoute deux propositions
à défaut (D-21, D-22), pose deux nœuds qui ne retiennent pas le scellement (D-23, D-24), et rappelle deux points
hérités de la version r3 que la conduite pouvait requalifier (H-1, H-2).

---

## D-21 — Quelles sondes le papier C lit, quand la porte G0 juge par famille et par dose (proposition, défaut sous 48 heures)

**Décision en une phrase.** Dire quelles sondes sont « désignées » pour HC2, HC2b et C-P6 quand le verdict de la
porte G0 juge le critère 3 sur deux familles d'organismes et seulement à certaines doses.

**Enjeu.** La version r3 écrivait « les sondes que le verdict de G0 déclare au-dessus du plancher […] sur
l'organisme du mode « coût gonflé » », au singulier. Or le brief écrit le critère 3 « sur (i) et (ii) » (instruction
cachée ; réglage fin sans instruction), et la décision N-063, version 2, ne le juge qu'aux doses où la base « mots
et coût » échoue, ou le dit « sans objet ». Trois cas n'avaient pas de règle : une sonde au-dessus du plancher sur
une famille et pas sur l'autre ; plusieurs doses ; critère « sans objet ». Le choix pèse sur HC2 : une sonde qui ne
lit que la consigne cachée réussit sur (i), échoue sur (ii) (test de validité du brief, T0.7), et ne bouge pas sous
un plaidoyer ; la désigner confirmerait HC2 à vide. Lieu : Plan, section 8, précision 38 ; liste d'arrêt 15.

**Options.**
- (a) Désignée seulement si elle est au-dessus du plancher sur chaque famille et à chaque dose que le verdict
  juge ; écart = le plus petit ; critère « sans objet » ou une seule famille jugée : aucune sonde, nœud. Avantage :
  suit le test de validité du brief ; la plus sévère pour la confirmation. Inconvénient : peut ne laisser aucune
  sonde, et le nœud se posera alors à l'ouverture de l'étape 2.
- (b) Désignée sur la seule famille (i), celle dont l'agent de l'étape 2 a le type. Avantage : il y aura presque
  toujours une sonde. Inconvénient : admet une sonde qui lit la consigne ; HC2 confirmée ne dirait rien.
- (c) Ne rien fixer maintenant ; un addendum de désignation après le verdict de G0. Avantage : on connaîtra la forme
  du verdict. Inconvénient : une règle choisie après des mesures de sondes.

**Recommandation.** (a). Confiance : 0,75. **Défaut sous 48 heures** : (a), la version écrite au texte.

**À savoir.** Si la base « mots et coût » réussit à toutes les doses du mode « coût gonflé » (où le sabotage
s'écrit en clair), le critère 3 sera « sans objet » et le papier C n'aura aucune sonde désignée : HC2 ne serait pas
lancée sans un nouveau mot. Le nœud D-23 offre une sortie.

---

## D-22 — Dire que le saboteur du papier C est « à consigne », et mesurer ce que la sonde doit au contexte (proposition, défaut sous 48 heures)

**Décision en une phrase.** Accepter une réserve nommée, une mention sur toutes les lignes des sondes et une ligne
rapportée sans verdict, qui disent ce que la séparation entre saboteur et honnête doit à la consigne tenue en
contexte.

**Enjeu.** À l'étape 2, le saboteur est l'agent sous une consigne privée (type de la famille (i)), dans un seul
mode, chiffré. La consigne est la même avec et sans plaidoyer : une sonde qui en lirait la trace resterait
immobile, HC2 serait confirmée et l'opposition aux juges « établie », sans rien apprendre d'une sonde d'intention
sur un agent sans consigne. C'est la critique la plus prévisible d'un relecteur (« votre sonde lit la consigne »).
La version r3 ne la nommait pas. Aucune revendication ne change. Lieu : Plan, section 7, réserve 20 ; section 8,
précision 39 ; Critères, « Mode d'induction ».

**Ce qui est écrit.** (1) Réserve 20. (2) Mention « saboteur à consigne tenue en contexte, mode du coût gonflé » sur
toute ligne de C-P4, C-P4b, C-P4c et C-P6 (sondes), quelle que soit l'issue. (3) Deux parts rapportées, par lecture
forcée (aucune génération) : π_S, part de la séparation qui disparaît quand la consigne quitte le contexte, à jetons
du saboteur égaux ; π_H, part qui apparaît quand elle y entre, à jetons de l'honnête égaux. Aucun seuil, aucun
verdict changé.

**Options.**
- (a) Les trois. Avantage : la limite est dite et chiffrée ; coût : quatre passes sans génération par tâche.
  Inconvénient : du code de plus dans le module (la fonction de reconstruction existe déjà pour le témoin lexical).
- (b) La réserve et la mention seules, sans les parts. Avantage : rien à coder. Inconvénient : la limite est dite
  sans mesure.
- (c) Rien. Avantage : texte inchangé. Inconvénient : HC2 confirmée serait lue plus large qu'elle ne vaut.

**Recommandation.** (a). Confiance : 0,7. **Défaut sous 48 heures** : (a). Si (b) : une version neuve retire la
précision 39 et tous ses renvois (toute occurrence de « précision 39 », de « π_S » et de « π_H »). Si (c) : elle
retire en plus la réserve 20 et sa mention (remplacements T-22, T-24, T-30, T-37 et T-38 de la note des
différences).

**Limite à connaître.** Les parts ne séparent pas la trace de la consigne de l'état que la consigne installe chez
l'agent. Seul un saboteur sans consigne le fait : D-23.

---

## D-23 — Un bras « saboteur sans consigne » pour HC2 (nœud : périmètre et dépense ; aucun défaut)

**Décision en une phrase.** Dire si TC.2 est rejoué avec un saboteur qui n'a aucune consigne en contexte, pour que
HC2 se lise aussi là où la sonde ne peut pas lire une consigne.

**Enjeu.** C'est le seul bras qui lève la réserve 20. Il demande des épisodes de plus (dépense, devis de la
piste C) et un organisme retenu par le verdict de G0. Il ne change rien au texte présent et ne retient pas son
scellement : il passerait par un préenregistrement complémentaire, scellé et contre-lu avant l'étape 2, comme la
clause d'ouverture de R-307.

**Options.**
- (a) Complément avant l'étape 2 : mêmes tâches, mêmes niveaux de plaidoyer, saboteur = l'organisme de la
  famille (ii) du mode « coût gonflé » retenu par G0 (entraîné sans instruction), honnête = le modèle de base ;
  cellules S et SP_m de plus, soit (n/2) × (1 + k_P) épisodes, 120 à 240 avec k_P = 3 ; HC2 et C-P4c rapportées par
  mode d'induction. Avantage : répond à la critique ; réemploie tout. Inconvénient : dépense à chiffrer ; dépend de
  ce que G0 retient.
- (b) Rien de plus : la réserve 20 et sa mention disent la limite. Avantage : aucun coût. Inconvénient : le papier C
  ne peut pas écrire « sonde d'intention ».
- (c) Attendre la famille (iv) de N-053 (politique apprise sans texte de consigne). Avantage : le contrôle le plus
  propre. Inconvénient : famille pas encore construite, sur devis à part ; délai.

**Recommandation.** (a), et (c) en plus si la famille (iv) existe à l'ouverture de l'étape 2. Confiance : 0,7.
**Défaut.** Nœud, aucun défaut ; à trancher avant le devis de la piste C, pas avant le scellement.

---

## D-24 — L'accord de calcul que le pilote citera (nœud : dépense ; aucun défaut)

**Décision en une phrase.** Dire si la ligne GO-2026-11-22-93 tient lieu de la ligne de type « calcul » que la
décision D-18 demandait pour le pilote, ou si une ligne propre au pilote, sur devis scellé, reste exigée.

**Enjeu.** GO-2026-11-19-74 (D-18, option (b)) : « une ligne de type « calcul » reste à inscrire sur devis scellé
avant tout lancement ». Depuis, GO-2026-11-22-93 (type « calcul ») a prolongé au 31 décembre, plafonds inchangés,
l'enveloppe de la phase 0 (GO-2026-10-20-06, dont le pilote « suit la même échéance ») et la délégation de 10 USD
par lancement (GO-2026-10-20-07). La garde de calcul accepterait donc un lancement qui cite cette ligne ; le mot du
19 novembre, lui, demandait un devis scellé. Le pilote coûte 4 heures de carte au plus, environ 6 USD.

**Options.**
- (a) GO-2026-11-22-93 suffit. Avantage : rien n'attend. Inconvénient : écart au mot de GO-2026-11-19-74 ; ligne
  générale, sans devis du pilote.
- (b) Ligne propre sur devis scellé : le brouillon existe (`devis-pilote-papier-C-v1-brouillon1.md`, `a4c9bdbc…`,
  branche du 19 novembre), prix et durée à remplir, à contre-lire et à sceller. Avantage : conforme au mot du 19 ;
  plafond et échéance propres. Inconvénient : une petite pièce de classe A de plus.

**Recommandation.** (b). Confiance : 0,75. **Défaut.** Nœud, aucun défaut. Le texte ne nomme aucun identifiant dans
les deux cas : il ne change pas.

---

## Points hérités de la version r3, que la conduite pouvait requalifier

- **H-1, précision 37** (tirages dégénérés et statistiques de rang). Tranchée le 19 novembre par une raison de
  principe, sans mot du directeur : les statistiques de rang C-P3a et C-P3b, fonctions des seuls gains, sont
  toujours lues, même là où la destination n'est pas identifiable. La lecture contraire est écrite en entier dans
  la précision. Elle fixe quand ces deux lignes peuvent être « établies ». Recommandation : la garder telle quelle
  (confiance 0,7) ; défaut sous 48 heures : gardée.
- **H-2, règle de remplissage du bras « contrôlabilité »** (D-19, option (a), rendue mécanique). Deux choses y sont
  fixées que l'option retenue ne disait pas : le concept est recopié octet pour octet de la configuration de
  l'organisme, sans libellé anglais ; plusieurs chaînes ou aucune : nœud. Recommandation : garder (confiance 0,8) ;
  défaut sous 48 heures : gardée.

---

## Pour la session mère (organisation, sans mot du directeur)

Le scellement attend six travaux qui ne dépendent pas les uns des autres ; aucun ne coûte.
1. **Contre-lecture** de ce brouillon par un Opus 5.5 neuf : consigne `consigne-contre-lecteur-brouillon7-relance-v1.md`.
2. **Module et configuration** (classe B, Opus 5.5) : mise à jour sur ce texte ; fiche v3 de la branche du
   19 novembre et son additif `fiche-module-additif-brouillon7-relance-v1.md` ; contre-lecture par un autre modèle.
3. **Grille de la clause de repli** : 58 cases pour C-P3a et C-P3b, 48 pour C-P3c, à jouer par un agent qui n'a écrit
   aucune version du texte, puis contre-lecture ; sans rapport complet au scellement, la version (b) s'applique
   d'elle-même.
4. **Taux de la réserve d'intention sous le nul** (verrou 11) : une contre-lecture de méthode le mesure.
5. **Versement sur `main`** des 1 669 fichiers de la branche du 19 novembre et des rapports de lecteurs du niveau 3.
6. **Note du vivier** : l'accès au dépôt `lciric/p1-auto` a été refusé le 19 novembre ; Lazar peut déposer le
   fichier. Les 24 PDF du verrou 2 manquent toujours ; le texte ne cite aucun chiffre qui en dépende.

Deux signalements.
- La réponse à la demande du directeur du 22 novembre (« papier C et banc de juge », mandat `6136451f…`) n'est pas
  rendue : la session a fini faute de crédit après ses quatre points (`1aa71279…`). C'est une panne, non un
  résultat : droit à une relance sur le même accord (règle du 22 novembre).
- Calendrier : le critère 7 de la porte G0 (au plus tard le 31 décembre) demande le texte scellé **et** contre-lu ;
  les travaux 2 à 4 sont le chemin critique, non la rédaction.
