# Vérification du devis v3 « serveur loué, palier 0b, essai 3 » — v1

**Verdict : À corriger** (corrections de forme, pas de reprise de fond). Cinq de mes six corrections sont portées, une l'est à moitié (« relevé le plus pessimiste »). La v3 introduit une contradiction nouvelle entre le repli à H0 + 98 h et la règle « destruction après versement prouvé ».

Pièce vérifiée : `docs/notes/organisme-auto-conception-v1/epreuves-v9/heritage/palier-0b/lancement-essai-court-mesure-v1/devis-serveur-loue-palier-0b-essai-3-v3.md`, sha256 `9446eba4f374c63964f46d546ac13c5a4905c9930cf50daf6a7257c107db5c44`. Bases : journal de tenue `bbfb4473…a8`, mesure `7605afc3…6d34` (inchangés).

Ce que je ne peux pas faire : (1) vérifier les prix Hetzner (aucun appel permis) ; le prix de la cpx42 n'a toujours aucune pièce, la v3 le dit ; (2) **vérifier les chemins `…/bras-1-a-3/sourd-egal/0.0/0` à `…/19`** : ils sont dans le dossier des sorties hors de mon périmètre de liste, que la session a listé et pas moi. Je n'ai pu contrôler que la cohérence de leur nombre : 0 à 19 font 20 dossiers, égal à n = 20 de la mesure (ligne 6). (3) Vérifier « préenregistrement v19, l. 208 » : le chemin que j'ai tenté `…/palier-0b/preenregistrement-heritage-palier-0b-etage-processeur-v19.md` n'existe pas (je n'ai pas cherché ailleurs, la liste m'étant interdite) ; les doses 0, 0,25 et 0,5 restent non vérifiées de mon côté. Je n'ai pas relu `registres/go.md`.

## Six corrections demandées

| # | correction | état | ligne de la v3 |
|---|---|---|---|
| 1 | 94,6 h | **Portée** | § 1 : « 94,6 h à n = 2 (Δt = 525,8 s …) » ; recalcul : 525,8 × 648 = 340 718,4 s = 94,64 h |
| 2 | place par s4 × 648 / (n − 1), choix 464 / 218,6 Go dit, 320 Go justifiés | **Portée, une réserve** | § 1 « Place » : formule exacte, 337 301 504 × 648 = 218 571 374 592 (recalculé), choix de 218,6 Go dit ; 320 − 218,6 − 3,4 = 98,0 Go. Réserve au pas 3 |
| 3 | « relevé le plus pessimiste » | **À moitié portée** | § 1 oui ; § 2 (« borne haute grossière de la place »), § 3 (« borne haute de l'étape 4 », « la borne de 96 h ») et § 6 (c) (« à la borne haute ») gardent l'ancien mot |
| 4 | repli daté | **Portée, une contradiction nouvelle** | § 5 : H0 + 98 h ; 98 × 0,11436 = 11,207 EUR = 14,009 USD (recalculé, 11,21 et 14,01 exacts) ; plafond 12 / 0,11436 = 104,9 h. Contradiction au pas 5 |
| 5 | lecture du journal | **Portée, une réserve** | § 6 (a) : le poste lit les dernières lignes, les verse, la session refait la projection. Réserve au pas 6 |
| 6 | voie de la racine | **Portée** | § 6 (a) : clone avec accès en lecture temporaire ou copie de l'arbre, contrôle de la tête et de l'empreinte `1f04cb46…` avant départ |

## Relevé de méthode

### Chaîne de raisonnement

1. Durée : 17:49:47,219 − 17:41:01,419 = 525,8 s ; × 648 = 340 718,4 ; /3600 = 94,644 h. La v3 écrit 94,6 h. Pièce : journal ligne 22, mesure ligne 3. Portée (correction 1).
2. Place : 337 301 504 × 648 = 218 571 374 592 octets, /1 = 218,6 Go (journal ligne 22). La v3 emploie le s4 du même instant que n (et non celui de n = 20 : le mélange qui donnait 464 Go est écarté). Disque : 320 − 218,6 − 3,4 = 98,0 Go, comme écrit. Pièce : § 1 de la v3.
3. Réserve de la correction 2 : les « environ 98 Go pour les étapes 5 et 6 et les archives » n'ont aucune mesure (la mesure ne porte que sur l'étape 4) ; c'est un reste, pas une estimation. Il faut l'écrire comme reste ; la gardien v4 (arrêt de place) protège de toute façon. Supposé : taille des étapes 5 et 6 et des archives sous 98 Go.
4. Correction 3. Occurrences de « borne haute » dans la v3 : § 2 « Le disque couvre la borne haute grossière de la place » (ligne 15), § 3 « soit la borne haute de l'étape 4, arrondie » (ligne 20) et « la borne de 96 h » (ligne 23), § 6 (c) « à la borne haute » (ligne 42). Elles contredisent la phrase du § 1 (« non une borne établie »). Le § 3, ligne 23, peut se lire comme borne de durée du gardien, ce qui est licite ; les lignes 15, 20 et 42 ne le sont pas.
5. Repli. § 5 : « À H0 + 98 h … le poste local le détruit … sans attendre ». Même § : « Destruction … après versement prouvé ». Le gardien arrête à 96 h de marche (§ 3, § 4 point 2) ; la marche commence après la mise en place du serveur (clone ou copie de 3,4 Go, environnement, contrôle : plusieurs dizaines de minutes à plusieurs heures, supposé). Si la mise en place dure ≥ 2 h, l'arrêt du gardien tombe à H0 + 98 h ou après : le repli détruit « sans attendre » avant tout versement des sorties. Deux règles qui peuvent se contredire ; la v3 ne dit pas laquelle prime. Il faut écrire : repli = détruire seulement après versement des inventaires et compagnons, ou un seuil de coût qui prime (plafond de 15 USD atteint à 104,9 h), et dater le versement final avant H0 + 98 h.
6. Lecture du journal (§ 6 (a)). Le poste lit « les dernières lignes … (noms, comptes et tailles) », la session refait la projection. La formule exige t3 (heure de dernière modification du manifeste de l'étape 3) ; les dernières lignes du journal de tenue ne le portent pas (journal lignes 13 et 14 : t3 apparaît seulement comme première ligne « manifestes=3 » et dans l'inventaire de l'étape 3). Il faut ajouter au relevé la ligne d'inventaire de l'étape 3 ou la mention de t3. Réserve mineure.
7. Voie de la racine. Deux options non départagées (clone avec accès temporaire, ou copie) : acceptable, le choix revient à la mère. Point d'attention nouveau : le clone dépose sur un serveur loué un accès en lecture au dépôt privé ; la v3 dit qu'il est retiré ensuite, sans dire par qui ni comment le retrait est prouvé. Écrire « retrait constaté, consigné ». Le plus sûr est la copie par la connexion chiffrée, qui ne dépose aucun accès.
8. Repli : « le poste local … l'a déjà fait (registre des dépenses, 11, 12 et 21 novembre) » : le registre montre la destruction par l'identifiant (ligne du 11 novembre : « détruite par l'identifiant 2026-11-11T00:02:17Z »). Pièce suffisante ; la v3 renonce à compter sur la mère pour détruire : correction de mon pas 10 de la v2.
9. Autres chiffres inchangés par rapport à la v2, relus : 0,11436 EUR/h ; 96 h = 10,97856 EUR = 13,7232 USD ; plafond de 15 USD = 104,9 h de vie.
10. Chemins `sourd-egal/0.0/0` à `…/19` : 20 chemins, égaux en nombre à n = 20 ; non listés par moi (voir ci-dessus). La phrase « portent tous le même proposeur et la dose 0 » passe de supposé (v2) à sourcé par la session, sans que j'aie pu le contrôler.

### Objets de contrôle

Mécanisme : le recalcul de la place et de la durée par la formule de la mesure. Objet où la conclusion est fausse par construction : le calcul de la v2 (diviseur n) ; prédiction avant : la v3 doit rendre 218,6 Go et non 232 Go ; résultat : 218 571 374 592 octets, la v3 le rend. Objet vrai par construction : la mesure figée (mesure ligne 9, 24 436 175 495 octets à n = 20) ; la v3 écrit 24,4 Go ; concorde. Pour la contradiction du pas 5, l'objet est un scénario : mise en place de 2 h, gardien à 96 h de marche : le repli tombe avant le versement ; je ne l'ai pas rejoué, il se lit sur les deux phrases.

### Premier pas non justifié

Le pas 5 : la durée de la mise en place du serveur (supposée). Ce qui la justifierait : une mesure de la préparation du serveur (copie de 3,4 Go, création de l'environnement) ou une marge écrite entre l'arrêt du gardien et le repli.

### Mode d'échec affecté

Mes six corrections demandées, plus « la v3 casse-t-elle autre chose ». Réponse : une contradiction (pas 5) et un reste de vocabulaire (pas 4).

### Trouvaille de côté

- Le plafond de 15 USD, atteint à 104,9 h de vie, laisse 6,9 h au-delà du repli de 98 h : la marge est réelle mais dépend d'une mise en place courte.
- Les 98 Go « pour les étapes 5 et 6 » ne sont qu'un reste (pas 3). Non poursuivi.

### Évaluateur et conseil

Ce qui me juge : la session mère. Mes témoins : recalculs à la main, concordants (pas 1, 2, 9). Je pourrais être jugé bon sans le mériter en ne vérifiant que les chiffres, qui sont justes, alors que le défaut est dans l'articulation de deux règles.

Corrections demandées : (a) remplacer « borne haute » aux lignes 15, 20 et 42 par « relevé le plus pessimiste » ou « borne de gardien » ; (b) § 5 : dire que le repli à H0 + 98 h ne détruit qu'après versement des inventaires et compagnons, ou ce qui prime, et fixer le délai entre l'arrêt du gardien et le repli (compte tenu de la mise en place) ; (c) § 6 (a) : ajouter t3 au relevé de 6 h ; (d) § 6 (a) : dire comment le retrait de l'accès en lecture est constaté, ou retenir la copie sans accès déposé ; (e) écrire « reste » pour les 98 Go.
