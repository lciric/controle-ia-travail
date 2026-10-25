# Journal synthétique — v5 — état au 25 octobre 2026, 13:45 UTC (v1 à v4 gardées ; en tête : ce qui a été tranché aujourd'hui)

Écrivain : lignée « conv-audit » ; contre-lecteur : lignée « session-depot » (section « Divergences » à sa main).
Nouvelle version = nouveau nom. Rien d'opposable (R7) : chaque fait renvoie au journal détaillé du jour
(`journal/detaille/2026-10-25-conv-audit.md`, entrées de 09:46 à 13:37) et à sa pièce. Heures : UTC lues sur l'horloge
ou sur les commits ; décisions de Lazar en heure de Paris (UTC + 1 depuis le 25 octobre à 3 h). La section 0 de la v4
(« qu'est-ce qu'apprendre, pour un organisme ? ») vaut toujours, inchangée ; elle n'est pas recopiée.

## 0. En une page : ce qui a changé le 25 octobre

- **Deux pilotes descriptifs de l'organisme de Gemini.** Le premier (objet v4, une question) est parti à 07:49 UTC et
  s'est arrêté sur le crédit épuisé (rapport mécanique v2 et audit de symétrie, canal, `7d1feec5`). Le second est
  **scellé** (13:31 UTC) sur un objet nouveau, la **v5.2.1** : texte `pilote2-gemini-organisme-v5-2-v2.md`
  (`d2944654…`), deux courses, **M** (question « maïeutique contre coercition », v2 épurée) puis **S** (« apprendre sa
  structure »), départ remis à session-depot (canal n° 48). Aucun score n'est lu avant le moment de lecture du texte.
- **L'objet n'est plus « écrit par Gemini seul »** : v5.2.1 = la v5.2 poussée par Gemini (`2d00232`) + la correction
  mécanique C-13 de session-depot (bloc de moisson refermé), comme C-12 l'avait été pour la v5.1 ; déclaré.
- **Trois lignées d'organismes à distinguer** : la v5.2.1 (pilote, conception de Gemini + deux corrections mécaniques) ;
  la **v5.3 « assistée »** (Lazar, 13:54 : Gemini l'écrit à partir des réponses du collisionneur sur les « emprunts » —
  la revendication d'auto-conception est perdue pour elle) ; la **v6** de Gemini (mémoire et récompense écrites par
  l'essaim, moisson déplafonnée, rondes de conception), conçue sur les questions de Lazar, livrée tronquée, et dont
  l'indépendance du brainstorm dépend de la conversation où elle sera finie.
- **Dépenser seulement ce qui rapporte** : les bornes des courses suivantes se décident par un **escalier de coût**
  préenregistré (δ = 0,10, règle gelée), après les indices gratuits du pilote ; le bruit est mesuré gratuitement par les
  générations 0 de M et de S.
- **Défauts trouvés avant de dépenser** : l'environnement vide du lanceur aurait coupé tous les appels Anthropic
  (certificats de la passerelle) ; « M saine » ne lisait aucun statut d'appel ; le temps d'une course dépassait la borne
  de la commande de fond. Tous corrigés avant le scellement, essayés (116 cas).

## 1. Où en est le programme (phase 0, instruments)

- **Étape 1 du programme gradient** : préenregistrement **scellé** par session-depot (v9, `6abcbe61…`, code `4de6544`,
  lanceur v6 ; contre-lectures n° 8 et n° 9 ; R-418) ; attend les clés de moisson visibles (R-420), puis répétition,
  épreuve d'endurance, A1, A2, B1, B2 ; le second pilote passe avant A1/A2 (R-423).
- **Confrontation** : brouillon v7 (`74487a41…`) ; la v8 doit inscrire que les pilotes ne changent ni la table de
  lecture de H-E1, ni ses seuils, ni ses règles (condition du moment de lecture des pilotes) — à la charge de conv-audit.
- **Second pilote** : scellé, prêt à partir (§ 0). **Noyau du pilote** : `b1c7f4b6` = `5d1d4fd` + R-410 (clés OpenAlex et
  Semantic Scholar en en-tête, jamais dans l'adresse) ; 141 essais.
- **Collisionneur** : tours faits aujourd'hui — structure v2, comparaison, espaces inégaux, publication v6 (Opus a
  refusé ; question reformulée pour lui, R-422), format v4, **emprunts v1** (Fable, Argon ; Opus a refusé), **financement
  v1** (trois cellules) ; en file : **escalier de coût v2** (après le départ de M). Dépense des cinq derniers tours ≈ 15
  USD (GO-2026-10-24-07).

## 2. Hypothèses

### En cours
- **H-E1** (confrontation), **H-G1** (étape 1, v9 scellée) : inchangées dans leur énoncé ; aucune donnée.
- **Escalier de coût** (à préenregistrer après la lecture du pilote) : « monter d'un cran de budget (rondes de conception,
  castes, générations) rapporte au moins +0,10 d'exactitude équilibrée sur le test final » — à tester avec une règle
  symétrique, le moins cher l'emportant à égalité.

### Validées
- Aucune hypothèse de recherche. Validations mécaniques nouvelles : v5.2.1 reproductible (relevés identiques sur trois
  graines de hachage), 34 essais en isolation ; lanceur v5 du second pilote (116 cas, dont les nouvelles gardes) ; essai
  à blanc du texte scellé ; clés OpenAlex et Semantic Scholar envoyées en en-tête (essai R-410).

### Réfutées ou retirées (le 25 octobre)
- « Un environnement vide (`env -i`) suffit au noyau » : **réfutée par l'observation** (12:54 UTC, sans clé : `httpx`
  échoue sur les certificats de la passerelle, `urllib` passe) → liste fermée avec les variables d'infrastructure réseau.
- « Deux générations de 3 000 s tiennent sous la borne de 2 h » : **réfutée par le calcul** (attente de 900 s des appels
  en vol : ≈ 8 000 s au pire) → 2 400 s.
- « Une seconde course peut partir sur une première saine sans lire les statuts d'appels » : retirée (P52C1-02).
- « La passerelle se vérifie à la main avant le départ » : retirée → garde automatique du lanceur.
- « La clé Anthropic par défaut du lanceur est celle des runs » : retirée → clés des runs nommées (P52C1-05).
- « L'objet du pilote est écrit par Gemini seul » : retirée (C-12, C-13, déclarées).
- « Lancer le pilote en parallèle sur Vast » : non retenue (recommandation (a) ; R3, clés à recharge sur machine louée,
  `unshare` probablement absent) ; Vast gardé pour les parties graphiques et les courses longues de l'étape 1.

## 3. Conclusions acquises (pièces à l'appui)

- **Second pilote** : texte scellé `d2944654…` ; contre-lecture 1 `e4a7292f…` ; lanceur v5 `83f8b9cf…` ; essais v5
  `1cc9efc1…` (116 sur 116) ; pièces `68306821…` (100 fichiers) ; branche `outils/pilote2-gemini-v5-2-travail`.
- **Objet** : v5.2.1, `ec8e0b6`, arbre `fec005c6…` (21 fichiers) ; vérifié par conv-audit et par session-depot.
- **Questions** : M v2 épurée `8b1c7511…` (aucun outil mathématique nommé) ; S v2 `a54da93e…` (canal).
- **Réseau** : la passerelle de sortie présente ses propres certificats (« Egress Gateway SDS Issuing CA ») ; Anthropic
  répond 401 et Gemini 403 sans clé, sous l'environnement du noyau.
- **Financement** : rapport vérifié (`notes/financement-bourses-france-v1.md`, `68520431…`) et comparaison avec les trois
  réponses du collisionneur (`notes/financement-comparaison-collisionneur-v1.md`, `1c478fe7…`) : le verrou est le
  contrat, pas le doctorat ; le statut d'accueil ouvre l'affiliation et le calcul national, mais sa convention cède souvent
  le logiciel et soumet la publication à un visa ; seuls les philanthropes internationaux de la sécurité de
  l'intelligence artificielle versent à une personne sans poste ; crédits d'accès externe d'Anthropic (1 000 dollars,
  examen le premier lundi du mois).

## 4. Décisions tranchées par Lazar (25 octobre, heure de Paris)

| heure | décision | pièce |
|---|---|---|
| 09:58 | garde avant départ = test de dépense (recharge automatique active) | journal 09:46 |
| 10:17 | plafonds : 30 USD par génération, 60 par course, 120 au pire, 8 192 jetons | idem |
| 11:37 | Brave gardé ; clé OpenAlex demandée ; formulaire Semantic Scholar | journal 11:06 |
| 12:11 | clés OpenAlex et Semantic Scholar intégrées au noyau avant le pilote | noyau `b1c7f4b6` |
| 12:20 | v5.2 de Gemini d'abord | zip `a0dadd85…` |
| 12:27 | attendre la v5.2 (rien ne part pendant le trajet) | — |
| 12:50 | M puis S | canal n° 43 |
| 12:55 | tour « emprunts » du collisionneur | canal n° 43 |
| 12:59 | bourses et affiliations : recherche et collisionneur | notes financement |
| 13:26 | objet = v5.2 poussée par Gemini (`2d00232`) | R-426 |
| 13:27–13:28 | question M v2 épurée | canal `a15809b8` |
| ≈ 13:32 | « corrige tout de suite » (C-13) → objet v5.2.1 | R-429 |
| 13:54 | (a) v5.3 « assistée » écrite par Gemini à partir des emprunts | zip `52dc2d02…` |
| 14:01, 14:12 | bornes selon le budget ; « (c) puis (a) : go » (indices gratuits, puis escalier) | journal 13:20 |
| 14:14, 14:16 | collisionneur sur δ, puis sur la conception de l'escalier | canal n° 46, 47 |
| 14:15 | δ = 0,10 et règle gelée de l'escalier : « excellent go » | journal 13:20 |

**En attente de Lazar** (défaut sous 48 heures) : Vast ou nuage pour le pilote (défaut : nuage) ; vérificateurs en
arrière-plan (défaut : après le pilote, les trois formes) ; v6 dans une conversation de Gemini séparée ou déclarée
« assistée ».

## 5. Idées ouvertes et idées écartées

Ouvertes : vérificateurs automatiques (essais de l'organisme relancés par le noyau ; reçu automatique des livraisons ;
second modèle juge réservé au collisionneur) ; escalier de coût ; plafond de moisson relevé pour la v6 (20 recherches et
10 téléchargements proposés par Gemini : presque gratuit en dollars, coûteux en temps) ; billets publics d'abord sur des
résultats d'objet (hypothèses de l'essaim testées sur processeur graphique), la méta-architecture gardée jusqu'à des
résultats nets ; demande de calcul et bourses (notes financement).
Écartées : les « réfutées ou retirées » de la section 2 ; servir les réponses du collisionneur aux organismes à
l'exécution (toujours exclu ; la v5.3 les reçoit seulement à la conception, déclarée).

## 6. Prochaines étapes (ordre)

1. **Départ de M** au réveil de session-depot (ligne de GO à trois empreintes d'abord), puis S si M est saine.
2. Pendant les courses : reconstitution et vérification de la v5.3 (sous-agent en cours) ; v6 complète à demander à
   Gemini ; tour « escalier » du collisionneur après le départ de M.
3. Après les courses : lecture mécanique (fichiers lisibles), audit de symétrie si un critère gelé le déclenche ; v8 de la
   confrontation (inscription) pour ouvrir le moment de lecture ; lecture des deux réponses comme matériau ;
   comparaison A contre A des générations 0 (sous le préenregistrement de l'escalier).
4. Étape 1 : répétition, épreuve, A1/A2, B1/B2 (session-depot).

## Divergences (à la main de session-depot)

(vide à la v5)
