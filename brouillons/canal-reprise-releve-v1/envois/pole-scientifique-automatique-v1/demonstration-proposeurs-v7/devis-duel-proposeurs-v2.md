# Duel des proposeurs — devis v2 (après les contre-lectures du code et les versions 10 à 17 de v7)

Lignée conv-audit (instance du 27 octobre 2026 ; servie par Opus 5.5), écrit après le relevé `date -u` de 20:35:05 UTC.
**Remplace le devis v1** (`7687bcc6…`, gardé, R12) : même question, même dépense, mais la plomberie a changé sur six points
qui touchaient la lecture ou la sûreté. **Rien n'est dépensé ici** : c'est un nœud de décision (GO de Lazar, lancement chez
session-depot). Exploratoire (R-546).

## Verdict

1. **Question inchangée** : un proposeur à modèle (Opus 5.5, avec ou sans la partie de développement) retrouve-t-il des
   structures qu'aucune référence gratuite ne retrouve, sur des mondes hors de l'espace du chercheur mécanique (grammaire v2,
   « trois traits », « seuil décalé ») ?
2. **Dépense inchangée** : 80 sessions de proposeur ; **attendu 30 à 60 USD, plafond 100 USD**.
3. **Ce que le devis v1 aurait mesuré à tort, et qui est corrigé** (v7 versions 10 à 17, 224 essais, `7f1646b`) : les bras à
   modèle jugeaient **une** fiche non témoin par génération (réservation aux plafonds pour des rôles simulés) — corrigé ; les
   quatre bras n'avaient **pas le même juge** — corrigé et vérifié sur les manifestes (`meme_juge_dans_tous_les_bras`) ;
   l'héritage de la preuve multipliait des e-valeurs lues sur les **mêmes issues** — corrigé (trois tranches de 150) ; la
   mémoire refusait 21 propositions sur 26 comme « déjà éprouvées » — corrigé (seuil de fusion au gabarit : 1 sur 50) ; le
   bac à sable laissait l'agent **lire** la banque et les mesures des fiches voisines — corrigé (lectures bornées à son
   dossier, échec dur sans bac à sable) ; la **clé** du relais restait lisible dans `/proc` — corrigé (fichier à lecture
   unique, contrôle `verification_cle_proc_v7.py`).
4. **Trois conditions avant le GO** : (i) la **rotation de la clé** recommandée par session-depot (R-589) ; (ii) le relais
   lancé **par fichier à lecture unique**, contrôle `/proc` versé avec la course (cas sain : « aucune variable de clé ») ;
   (iii) dans le conteneur de session-depot, le bac à sable des agents doit pouvoir monter un `/proc` neuf — sinon la
   course s'arrête d'elle-même, et il faut des agents sous un utilisateur non root distinct de celui du relais.

## 1. Plan (v1, avec les réglages fixés)

- Mondes : grammaire v2, structures « trois_traits » et « seuil_decale », graines 20261201 à 20261220 ; parties calibrage
  150, développement 300, épreuve 450 (**trois tranches de 150**, une par génération).
- Bras (mêmes mondes, mêmes témoins, **même juge** : v1 sans urne, nul informé, nul d'archive ajusté, règle e-BH avec
  témoins vrais hors famille et m fixé avant les issues, témoins sans agents ; réglages `REGLAGES_JUGE` du script :
  plans de 150, 6 instants de lecture des filles, 12 de calibrage, 4 filles et 2 paires par recombinaison, 12 propositions
  par génération, 3 générations) : M-expl (Opus 5.5 avec développement), M-aveugle (Opus 5.5 sans), mécanique (avec
  développement), aléatoire — ces deux derniers gratuits.
- Script : `orchestrateur-pole-v7/demonstrations/duel_proposeurs_v7.py DOSSIER --moteur claude-sdk --url-relais
  http://127.0.0.1:<port>/v1 [--arret-apres 10] [--budget-par-monde 6]` ; seul le proposeur passe par le relais
  (adaptateur mixte ; les rôles simulés ne réservent ni ne dépensent rien) ; répétition sans dépense :
  `--moteur simule` (vérifiée : même juge dans les quatre bras, aucune fiche hors budget).

## 2. Lecture (fixée avant la course ; v1, avec les précisions des versions 10 et 11)

- **L1** : témoins faux promus ≤ α dans chaque bras ; promues sans lien et **promues partielles** (traits en commun sans
  être exactement ceux de la structure) rapportées ; `meme_juge_dans_tous_les_bras` doit être vrai, sinon la lecture
  s'arrête.
- **L2 à L4** : contraste par monde v = [structures(bras 1) − structures(bras 2)] / 3 ; **pari apparié borné en forme
  « parts » seule** (conception v2 à v5), mélange sur Λ = {0,1 ; 0,3 ; 0,6 ; 0,9}, α = 0,05 : L2 M-expl contre mécanique
  (la question principale), L3 M-aveugle contre aléatoire, L4 M-expl contre M-aveugle. « Structure retrouvée » = au moins
  une fiche non témoin promue dont la loi emploie **exactement** les traits de la structure.
- **L5** : USD par structure retrouvée, rapporté, jamais un critère.
- Arrêt : après 10 mondes, si M-expl n'a rien retrouvé, la suite est annulée (moitié de la dépense économisée).
- Prédiction (inchangée, à contester) : L2 promu (0,4) ; L3 non promu (0,7) ; L4 promu (0,6).

## 3. Devis (inchangé)

| poste | nombre | plafond unitaire | plafond |
|---|---|---|---|
| sessions de proposeur, M-expl (2 par monde) | 40 | 1,5 USD | 60 |
| sessions de proposeur, M-aveugle | 40 | 1,0 USD | 40 |
| **total** | 80 | | **100 USD** (attendu 30 à 60) |

Relais à 100 USD, réserve 0,40 par appel ; budget par monde 6 USD, par génération 2 USD (explicite, v11) ; proposeur
`plafond_proposeur_usd` 1,5, 15 tours ; durée 2 à 4 heures.

## 4. Ce que le duel ne dira pas (inchangé)

Rien sur un chercheur de la littérature ; rien sur une banque réelle (la couche 1 bis vient de montrer que la banque T0.5 ne
porte pas de structure dans ses quatre traits : `../couche1bis-lecture-v1/lecture-couche1bis-v1.md`) ; rien de décisif.
