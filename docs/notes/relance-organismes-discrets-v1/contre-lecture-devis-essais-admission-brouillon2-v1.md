# Contre-lecture du devis des deux essais d'admission (Mistral Large 4, second lecteur ; `gemini-4-neon`, juge des deux ancres), brouillon 2 — bras A — v1

- **Pièce contre-lue** : `docs/notes/relance-organismes-discrets-v1/devis-essais-admission-mistral-neon-bras-a-v1-brouillon2.md`, `6f81288b5efca85f…` (empreinte vérifiée « OK » contre son compagnon), 515 lignes, écrit par Claude Fable 5.2.
- **Point de départ** : le brouillon 1, `11a352fc3f5c59cc…` (vérifié), et sa contre-lecture, `03bfab589ca152da…` (vérifiée) : huit corrections, dix mineurs, trois questions.
- **Contre-lecteur** : Claude Opus 5.5, agent neuf, le 2026-11-21. Je n'ai écrit ni ce devis, ni le brouillon 1, ni sa première contre-lecture, ni le texte du bras A.
- **Ce que j'ai fait** : lecture ; recherches de chaînes sur des fichiers nommés ; comparaison des huit règles et calcul des montants par deux programmes du bloc-notes de la session. Je juge ; je ne corrige rien. Aucun appel de modèle, aucun appel réseau, aucune clé, aucun sous-agent, aucune dépense. Rien scellé, rien committé.
- **Texte en vigueur** : `prereg/T0.7-organismes-discrets-v-a-v2-brouillon43.md`, `4f91b535ad915815…` (vérifié).

## Verdict

**Engageable après corrections.** Deux corrections, toutes deux à faire avant la demande des lignes de calcul.

Les huit corrections et les dix mineurs de la première contre-lecture sont traités fidèlement, et chacun est levé. Les trois décisions « goreco » sont portées telles quelles. Les critères sont inchangés : 22 sur 24, huit sur huit, un seul nom servi. Les huit règles de 3.4 sont recopiées à la lettre, règle 6 comprise : je l'ai vérifié par programme, caractère pour caractère. L'arithmétique est juste.

Les deux corrections viennent de la réponse du brouillon 2 à la correction 2 (sortie maximale) :
1. **La sonde peut dire « comprise » sans avoir vu de réflexion.** L'issue doit exiger une réflexion constatée.
2. **Le plafond n'est pas une borne en dollars tant que la sonde n'a pas dit « comprise ».** Cela vaut aussi pour les appels de vérification, faits avant la sonde. Une ligne de calcul ne peut pas dire « plafond tenu par compteur » sans le dire, ni sans chiffrer l'excès possible.

Le reste est mineur (onze points, section 6).

## 1. Les corrections et les mineurs de la première contre-lecture

### Les huit corrections

| correction | traitée fidèlement ? | levée ? | où, et réserve |
|---|---|---|---|
| **1. Délais** | oui | **levée** | Mode de chaque amont écrit : Mistral en flux (`stream: true` au corps, 5.2), Google sans flux (5.3). Silence 600 s, total 2 700 s, relais dix secondes en dessous. Débit tenu déclaré : 12,2 jetons par seconde. Délai global calculé sur le pire cas. La cause d'échec par délai est dite à Lazar (5.6 ; 13, points 6 à 8). Réserve mineure : n-11. |
| **2. Sortie maximale** | oui | **levée sur le fond** | Constat documentaire écrit, relevé cité par chemin et empreinte (5.4). Issue écrite là où la documentation se tait. Condition (c) dite non établie hors du cas « comprise » (6.4). Mais la sonde ajoutée porte deux défauts neufs : corrections C-1 et C-2. |
| **3. Forme de la réponse à la vérification** | oui | **levée** | Tous les champs de 5.5 exigés (4.3), `thoughtsTokenCount` absent vaut 0. Extraction du texte jugé fixée pour les deux services (5.5). Sinon, vérification non saine et brouillon neuf (4.3 ; 4.4, ligne 5). Réserve mineure : n-3. |
| **4. Classement fermé** | oui | **levée** | « Ou l'inverse » retiré : code 200 et bon nom, saine quelle que soit la liste (4.4, ligne 3 ; 4.5 ; garde 11, cas sain). « Nomme le champ X » défini par programme, sur une liste close de champs. Ligne finale fermée (ligne 13). 401, 402 ou 403 après une liste admise sans l'identifiant : nœud (ligne 8). « Liste lisible » définie, sous ses deux formes. `code` comparé comme une chaîne. Réserves mineures : n-1, n-2, n-4. |
| **5. Deux gardes manquantes** | oui | **levée** | Garde 14 : identifiant demandé égal à la lettre, dans la configuration, le corps et le chemin de Google ; hôte parmi les trois permis et celui de sa ligne ; artefacts sur les trois alias, un hôte autre, l'hôte global sous la ligne européenne. Garde 15 : la vérification globale exige le relevé européen scellé, signe constaté ; artefacts : relevé absent, relevé sans signe. |
| **6. Conditions d'envoi** | oui | **levée** | Garde 9 : le tableau du constat est lu, une ligne par condition, à sa valeur attendue, date en temps universel antérieure, mot de Lazar présent, crédit suffisant. Étape ajoutée : un brouillon du texte inscrit le constat à la case de 13.1 avant la première vérification (9 ; 12, point 4). Le fichier des règles cite le brouillon en vigueur au premier envoi, refait sous un nom neuf sinon (9). Réserve mineure : n-6. |
| **7. Reprise sur le brouillon 43** | oui | **levée** | Brouillon 43 cité partout ; plus aucune mention du 42 hors des empreintes lues (section 14). GO-2026-11-21-32 et -33 dites inscrites ; je l'ai retrouvé à la case de 13.1 du brouillon 43 (lignes 631 et 632, tête `e77fa0d9`). Réserve « Labs » et « Preview » ajoutée (9). Les huit règles recopiées à la lettre (question 3). |
| **8. Compte du fournisseur** | oui | **levée** | Montant dit en crédit utilisable (6.5). Taxe de 20 % sur la recharge prise en compte, supposée (S). Règle « le crédit couvre la somme des plafonds avant toute file », lue par la garde 9. « Compte chargé au plus juste » retiré des barrières. Phrase « les réglages décident, non la caisse » nuancée : 402, 429 répété, deux pannes (6.4). |

### Les dix mineurs

| mineur | levé ? | constat |
|---|---|---|
| m-1 | levé | « tout code de 500 à 599 » en 5.6 et à la garde 4 ; 504 à l'artefact. |
| m-2 | levé | « trois délais de suite » retiré ; deux pannes sur un même appel arrêtent (5.6 ; garde 2). |
| m-3 | levé | `Retry-After` borné à 600 s, au-delà attente de 600 puis envoi ; artefact à 900 (garde 4). La borne passe de 60 à 600 s : choix neuf, sans effet sur la forme, couvert par la marge du délai global. Acceptable. |
| m-4 | levé | Garde 17 : huit identifiants, cet ordre ; artefacts : une neuvième entrée, une autre, un autre ordre. |
| m-5 | levé | Garde 18 au tableau, cas sain et artefact. |
| m-6 | levé | Garde 12 : chaque artefact a une seule issue. |
| m-7 | levé | Relevé `291341e2…` : température sous raisonnement « non trouvé », facturation de la réflexion « non trouvée » ; repris en 4.4, 5.5 et 6.1. |
| m-8 | levé | Lignes de 11 : « trois appels au plus, soit trois envois au plus » ; point d'accès du relevé ; prix à 1,1 fois ; empreintes ; brouillon en vigueur ; geste de paiement. |
| m-9 | levé | Un relais par ligne, avec la borne et le plafond de la ligne ; le relais de Google n'a pas de plafond en dollars, dit (6.4). |
| m-10 | levé | Ordre dit, plus prudent que celui du texte (11, dernier tiret). |

**Les trois questions** sont devenues décisions (16) : voir la question 2.

## 2. Les trois décisions « goreco »

Pièce `mots-de-lazar-devis-essais-admission-bras-a-2026-11-21-v1.md`, `9b9ee5ca4e89f3dc…`, vérifiée.

| décision | portée telle quelle ? | constat |
|---|---|---|
| 1. Une ligne de vérification couvre trois appels au plus, écrit en toutes lettres | **oui** | 4.1 ; lignes 1, 2 et 5 de 11 : « trois appels au plus, soit trois envois au plus ». « Soit trois envois » ne dit rien de plus : aucun appel de vérification n'a de reprise (4.1). Le devis loge la sonde dans ces trois appels : c'est un emploi du budget, non un budget de plus. Il est dit à la ligne (« sonde de borne comprise »). Réserve mineure : la ligne 1 de 4.4 dit le refus du mandataire « non compté parmi les trois », mais le compteur le compte au pire cas (n-1). |
| 2. Sortie maximale de 32 768 aux deux files | **oui** | 0, point 5 ; 5.1 à 5.4 ; garde 3. L'option à 16 384 est retirée. « À revoir si les délais ne tiennent pas » : le devis répond « ils tiennent, au débit déclaré en 5.6 ». C'est conditionnel à un débit non mesuré (S). À dire ainsi à Lazar (n-9). |
| 3. Ligne du repli global accordée d'avance, sous condition | **oui** | Ligne 5 de 11, sous le signe de 4.5 et la garde 15. Le mot dit « le signe … fixé au devis » : il suit donc le signe du devis accepté. Mais ce signe a été élargi (code 422, forme `detail`) après le mot, qui répondait à la recommandation faite sur le signe du brouillon 1. Rien n'est demandé de plus, mais la demande de la ligne 5 doit le dire (n-10). |

Ni plus ni moins, aux deux réserves mineures près.

## 3. Fidélité au texte

**Comparaison par programme** (`regles.py`, bloc-notes de la session) : les lignes 314 à 322 du devis contre les lignes 521 à 529 du brouillon 43, section 3.4.
- Neuf lignes (le titre et les huit règles) : **identiques caractère pour caractère**, longueurs 85, 337, 879, 223, 240, 248, 207, 452 et 685.
- **Règle 6 comprise**, à son rang : « Ni `gemini-4-carbon`, ni `gpt-6.2-astra`, ni un modèle de DeepSeek, ni aucun autre modèle ne prend un rôle sans un mot de Lazar ; … ».
- Le renvoi « lignes 521 à 529 du fichier » du devis est exact.

**Critères inchangés** :
- Mistral : « au moins 22 réponses de forme conforme » sur 24, règle 1 ;
- Neon : « toutes les huit de forme conforme », règle 2, conforme à la pièce « b a b go », choix 1 (b) ;
- un seul nom servi : « toutes les réponses de la file portent le nom servi que la vérification de la clé a relevé », règle 3.

Le résumé « En bref » et « Ce que ce devis fixe pour les lire » n'ajoutent ni seuil ni issue. La lecture des motifs (5.5) suit le texte : « fin par sortie maximale atteinte se lit sur le motif de fin que rend le service » (3.4, « Ce que les essais envoient »).

**Autres points du texte, vérifiés** :
- 24 appels, 48 envois ; 8 appels, 16 envois ; un seul réglage ; un message « user » : conforme (3.4, « Ce qui est joué »).
- Repli borné : « seul ce signe déclenche le repli » ; code 200 avec un autre nom servi : nœud, sans repli (3.4, « Deux précisions » et « L'exception est bornée ») : conforme (4.3 ; 4.4, ligne 4 ; garde 11).
- Conditions d'envoi « constatées et datées avant le premier envoi, essais d'admission compris », et « vérification de la clé comprise » : conforme (4.1 ; 9 ; garde 9).
- Ordre du préambule de 13 : constat, devis contre-lu, fichier des règles, lignes de calcul, programme contre-lu, vérification de la clé. Le devis engage les lignes après le programme : plus prudent, dit (11).
- La vérification du texte est « un appel minimal ». Le devis en fait jusqu'à trois, aux réglages pleins, sonde comprise. Les trois appels sont un mot de Lazar ; les réglages pleins avaient été jugés acceptables par la première contre-lecture. La sonde est un appel à message de calcul, non lu. Je le juge compatible, puisque la ligne le nomme.

## 4. Choix faits là où la documentation se tait

| choix | jugement | raison |
|---|---|---|
| **Garde de sortie qui ne lit que le motif de fin** | **procédure acceptable**, fidèle au texte ; mais elle ouvre la correction C-2 | Le texte lit « fin par sortie maximale atteinte » sur le motif de fin. Le brouillon 1 arrêtait une file sur une sortie facturée au-delà de 32 768, ce qui pouvait couper une lecture normale pour une raison de devis. La règle neuve ne coupe aucune lecture que le service finit normalement. Contrepartie : si la réflexion est hors de la borne, ni le compteur ni le relais ne bornent plus la dépense en dollars (C-2). |
| **Appel de sonde de la borne, trois issues** | **procédure acceptable sur le principe ; défaut dans l'issue « comprise »** (C-1) | Mesurer pour quelques centimes ce que la documentation tait vaut mieux qu'un point laissé indécidé ; « non comprise » et « indécidée » vont à Lazar, avec une recommandation écrite d'avance. Défaut : « comprise » ne demande que « au plus 256 facturés et fin par sortie maximale ». Un modèle qui ne réfléchit pas et dont la réponse visible atteint 256 jetons donne « comprise », alors que rien n'a été mesuré de la réflexion. Il faut une réflexion constatée. Mineur : quelle sortie facturée lire quand `completion_tokens` et `total_tokens − prompt_tokens` diffèrent (n-5). |
| **Nom servi égal à la lettre** | **procédure acceptable**, fidèle au texte | Le texte veut « le nom servi est l'identifiant demandé ». Toute autre forme (suffixe de date, préfixe `models/`, casse, alias) va à Lazar, sans normalisation. C'est prudent. Le prix : un aller-retour avec Lazar si Google rend un nom suffixé. C'est un nœud à la vérification, non une file perdue. |
| **Signe élargi au code 422 et à la forme `detail`** | **procédure acceptable**, à dire à Lazar avec la ligne 5 (n-10) | Le schéma ne donne que 422 pour cet appel : l'ajouter est raisonnable. Le constat 1 (liste admise sans l'identifiant) garde le signe étroit. Un faux signe ferait passer au point d'accès global alors que l'européen sert le modèle, contre la condition de « b a b go ». Il exigerait un refus qui désigne le modèle et une liste sans l'identifiant : c'est peu probable. Les formes restent supposées (S), sans pièce : déclaré. Précision manquante : « un `loc` qui contient la chaîne `model` », élément égal ou sous-chaîne (n-4). |
| **« XHIGH » puis « xhigh »** | **procédure acceptable** | Les deux orthographes viennent d'un résumé d'outil. L'ordre est fixé d'avance ; une seule bascule, sur un 400 qui ne nomme que le champ du niveau ; rien d'autre n'est essayé. La limite est dite : un niveau accepté n'est pas prouvé appliqué ; `thoughtsTokenCount` est rapporté. Manque au tableau des gardes l'artefact de cette ligne (n-8). |
| **Flux de Mistral** | **procédure acceptable** | Il permet un délai de silence qui distingue une connexion morte d'une longue réflexion (la pensée est émise au fil de l'eau, M). Ce qui reste inconnu (`usage` et `model` dans le flux) se constate à l'appel A, sinon brouillon neuf : un aller-retour, non une file perdue. L'extraction ne garde que les morceaux de premier niveau de type `text` : un morceau de pensée, même s'il contient du texte, est écarté. Précision : « `model` … le même dans tous » (n-3). |
| **Délais** : 600 s de silence, 2 700 s par envoi, 36 h au pire pour la file Mistral | **procédure acceptable**, déclarée | 2 700 s, c'est trois fois les 15 minutes conseillées par Google. Le délai global est au-dessus du pire cas des envois, avec une marge de 600 s ; il n'arrête qu'un programme bloqué. 36 h est un majorant, non une durée attendue. La session qui lance doit tenir ce temps : une file interrompue de notre côté est un nœud (5.6 ; 13, point 8). Le risque résiduel est réel et dit : une connexion muette de Google coupée par un intermédiaire, que la vérification ne voit pas (13, point 6). Réserve mineure sur la phrase « ne peut couper aucune file » (n-11). |
| **Budget de trois appels jugé serré** | **procédure acceptable** ; le budget est le mot de Lazar | Chez Google, si « XHIGH » est refusé : A, A′, puis B prennent les trois appels ; un seul 429 de plus demande une ligne nouvelle. Ce n'est pas une file perdue : un nœud et une ligne de plus. Le devis le dit (13, point 13). Il faut le redire à la demande des lignes. Mineur : 4.2, dernier tiret, « B ou A′ selon l'ordre » ; seul A′ est possible, puisque B exige un appel sain (n-2). |

## 5. Arithmétique

Refaite par programme (`arith2.py`, bloc-notes de la session), sur les seuls tarifs et volumes que le devis déclare. Prix comptés : 0,77 et 2,31 USD par million pour Mistral ; 3 et 15 pour Neon. Entrées bornées à 5 000 et 24 000 jetons. Sortie pleine de 32 768. Corps de vérification à 200 octets.

| grandeur | devis | recalculé |
|---|---|---|
| un envoi, Mistral (appariement ; couverture) | 0,080 ; 0,094 | 0,0795 ; 0,0942 |
| un envoi, Neon | 0,507 ; 0,564 | 0,5065 ; 0,5635 |
| file Mistral, deux envois (trois) | 3,99 (5,99) | 3,9937 (5,9905) |
| file Neon, deux envois (trois) | 8,33 (12,50) | 8,3323 (12,4985) |
| vérification Mistral, un envoi ; trois | 0,076 ; 0,23 | 0,0758 ; 0,2275 |
| vérification Google, un envoi ; trois | 0,492 ; 1,48 | 0,4921 ; 1,4764 |
| compteur : trois envois passent, pas quatre | (implicite) | Mistral 0,2275 ≤ 0,25, 0,3034 > 0,25 ; Google 1,4764 ≤ 1,50, 1,9685 > 1,50 |
| pire cas total ; somme des plafonds ; sans repli | 14,26 ; 14,75 ; 14,50 | 14,2574 ; 14,75 ; 14,50 |
| attendu Mistral ; Neon ; total | 0,18 ; 0,34 ; ≈ 0,55 | 0,1811 ; 0,3393 ; 0,5604 avec les trois vérifications (0,55 sans le repli) |
| cinq fois la sortie supposée | 0,74 ; 1,54 | 0,7355 ; 1,5393 |
| crédit utilisable : Mistral ; Google | 5,50 ; 11,50 | 4,75 × 1,15 = 5,4625, arrondi au demi-dollar supérieur 5,50 ; 10,00 × 1,15 = 11,50 |
| paiement avec une taxe de 20 % | 6,60 ; 13,80 | 6,60 ; 13,80 ; sans ce surplus, 5,50 ne donnerait que 4,583 de crédit |
| délai global, file Mistral | 130 440 s, 36 h 14 min | 24 × 2 × 2 700 + 24 × 10 + 600 = 130 440 s = 36 h 14 min 0 s |
| délai global, file Neon | 43 880 s, 12 h 11 min | 43 880 s = 12 h 11 min 20 s |
| délai global, vérification | 8 700 s | 3 × 2 700 + 600 = 8 700 s ; 8 730 s avec trois pauses (sans effet) |
| débit minimal | 12,2 jetons par seconde | 32 768 ÷ 2 690 = 12,18, arrondi à 12,2 ; 12,14 sur 2 700 s |
| « trois fois le conseil de Google » | 3 | 2 700 ÷ 900 = 3 |

**Tout est juste.** Le « ≈ 0,55 » du total omet le centime du repli : sans effet.

**Ce qui n'est pas chiffré, et devrait l'être** (correction C-2). Si la réflexion est hors de la borne, un envoi n'est borné que par 2 690 secondes :

| débit (S) | jetons en 2 690 s | Mistral, au prix de sortie compté | Neon |
|---|---|---|---|
| 12,2 par seconde | 32 818 | 0,08 USD | 0,49 USD |
| 50 | 134 500 | 0,31 USD | 2,02 USD |
| 100 | 269 000 | 0,62 USD | 4,04 USD |
| 200 | 538 000 | 1,24 USD | 8,07 USD |

À 100 jetons par seconde, un seul envoi de Neon passe le plafond de la vérification de Google (1,50 USD) et la marge du crédit (1,50 USD).

## 6. Gardes

**Les dix-huit gardes ont chacune un cas sain et un artefact**, contre un faux fournisseur local, sans appel payant (R5). Il n'y a pas d'artefact flou comme au brouillon 1 (gardes 2 et 12).

**Les deux gardes demandées sont là** :
- **garde 14**, identifiant exact et hôte permis : identifiant égal à la lettre dans la configuration, le corps et le chemin de Google ; hôte parmi les trois permis et celui de sa ligne ; artefacts `mistral-large-latest`, `mistral-large-4`, `gemini-4-neon-latest`, un hôte autre, l'hôte global sous la ligne européenne ;
- **garde 15**, repli lié au signe constaté : la vérification globale exige le relevé européen scellé, signe constaté, d'empreinte inscrite ; artefacts : relevé absent, relevé sans signe (401, autre nom servi, ligne 13).

**La garde des conditions d'envoi (garde 9) lit chaque condition**, sur le principe : « une ligne par condition de la section 9, à la valeur attendue », dates antérieures, mot de Lazar présent, crédit suffisant. Ses artefacts n'en éprouvent que certaines : condition manquante, partage « activé », journaux à 55 jours, date postérieure, crédit de 4,00. Ne sont pas éprouvés : le refus de l'entraînement de Mistral « activé » ; l'offre gratuite ; la clé d'un autre projet ; des limites de débit sous le seuil ; la variante de Google « après usage, aucun budget sous 10,00 » (n-6).

Autres manques d'artefacts, mineurs :
- garde 2 : le délai global, qui coupe un programme bloqué, n'a pas d'artefact (n-7) ;
- garde 10 : le chemin « sonde non comprise ou indécidée, avec mot de Lazar » n'a ni forme écrite du mot (pièce scellée, empreinte inscrite) ni cas sain (n-7) ;
- garde 16 : les lignes 2, 7, 8, 11 (dans ses deux temps), 12 et 13 de 4.4 n'ont pas d'artefact au tableau, bien que le faux fournisseur doive les porter (12, point 10) (n-8) ;
- garde 16 : une fois la correction C-1 faite, artefact « 256 facturés, fin par sortie maximale, aucune réflexion constatée : indécidée ».

## 7. Verdict, et ce qui reste avant la première vérification de clé

**Engageable après corrections.**

### Corrections (avant la demande des lignes de calcul)

**C-1. Issue « comprise » de la sonde : exiger une réflexion constatée.** Aujourd'hui : « au plus 256 facturés, et fin par sortie maximale atteinte ». Sans réflexion, une réponse visible de 256 jetons donne « comprise », et la condition (c) et la règle 7 seraient lues sur un constat qui ne mesure rien de la réflexion. À écrire : « comprise » exige aussi une réflexion constatée. Chez Google, `thoughtsTokenCount` supérieur à 0. Chez Mistral, au moins un morceau de pensée dans le flux, compté par son type, sans lecture. On peut ajouter, ou mettre à la place, une longueur courte du texte extrait, déjà relevée : la coupure est alors tombée dans la réflexion. Sinon, « indécidée ». Avec l'artefact de la garde 16.

**C-2. Plafonds : dire, dans les lignes et au nœud, qu'ils ne bornent la dépense que sous la condition (c), et chiffrer l'excès possible.** Le devis l'écrit en 6.4 (« le cumul peut alors passer le plafond de l'excès de cet envoi, borné en pratique par le délai total »). Mais :
- les lignes 1 à 5 de 11 disent « plafond, tenu par compteur avant l'envoi », sans réserve ;
- les appels A et A′ des vérifications partent aux réglages pleins, **avant** que la sonde ait rien mesuré ; la sonde elle-même aussi ;
- le relais de Google n'a pas de plafond en dollars ;
- l'excès n'est borné qu'en temps : à 100 jetons par seconde, un envoi de Neon coûte 4,04 USD, plus que le plafond de la vérification de Google et que la marge du crédit (section 5).

Une dépense au-delà du plafond d'une ligne est une dépense sans ligne. À écrire : à chaque ligne, « plafond tenu par compteur si la sortie maximale borne la réflexion ; sinon, excès possible d'un envoi, au plus X USD à un débit déclaré Y » ; même phrase au nœud de 4.6, avec la recommandation. Sinon, une borne dure en dollars par un autre moyen. C'est à Lazar d'accepter l'excès en connaissance de cause, au moment des lignes.

### Mineurs

- **n-1** : ligne 1 de 4.4, refus du mandataire. La signature par programme n'est pas écrite (origine « relais » ou « amont », section 8). Et le compteur compte au pire cas tout envoi en erreur, donc un quatrième envoi ne passe plus sous 0,25 : le refus « non compté parmi les trois » l'est en fait par le compteur. À accorder.
- **n-2** : 4.2, dernier tiret, « le troisième appel est B ou A′ selon l'ordre ci-dessus ». Seul A′ est possible, puisque B exige un appel A ou A′ sain. À écrire.
- **n-3** : 4.3, « un champ `model` présent dans les événements du flux, … le même dans tous ». Chaque événement de données, ou ceux qui le portent ? Un dernier événement d'usage sans `model` rend-il la vérification non saine ? À trancher par écrit, avec la réserve 5.
- **n-4** : 4.5, constat 3, forme `detail` : « un `loc` qui contient la chaîne `model` », élément égal ou sous-chaîne d'un élément. À écrire.
- **n-5** : la sonde lit « la sortie facturée de 5.5 ». Si `completion_tokens` et `total_tokens − prompt_tokens` diffèrent, laquelle ? La plus grande, comme pour le coût, à écrire.
- **n-6** : garde 9. La liste des clés du tableau et la forme des valeurs admises sont à la configuration. Un artefact par clé : refus de l'entraînement « activé », offre gratuite, clé d'un autre projet, limites de débit sous le seuil, variante « après usage ».
- **n-7** : garde 2, artefact du délai global. Garde 10, forme du mot de Lazar après une sonde non « comprise » (pièce scellée, empreinte inscrite à la configuration), avec son cas sain.
- **n-8** : garde 16, artefacts au tableau pour les lignes 2, 7, 8, 11 (dans ses deux temps), 12 et 13 de 4.4.
- **n-9** : section 1, décision 2. « Ils tiennent » se lit « ils tiennent si le service rend 12,2 jetons par seconde ou plus, débit non mesuré ». À dire ainsi à la demande des lignes.
- **n-10** : ligne 5. Le signe a été élargi (422, `detail`) après le mot « goreco », qui accorde la ligne sur « le signe fixé au devis ». À dire à Lazar avec la ligne, signe de 4.5 recopié.
- **n-11** : 5.6, « une attente sur un code 429 n'y ajoute rien ». C'est vrai si le 429 revient vite. Un 429 rendu après un long silence, plus 600 s d'attente, passe le créneau de l'appel ; la marge de 600 s en couvre un seul. « Ne peut donc couper aucune file » est à tempérer.

### Le devis peut-il servir à demander les lignes de GO ?

**Pas en l'état.** Les lignes reprendraient la phrase « plafond tenu par compteur » sans la réserve de C-2. Elles le pourront après un brouillon 3 qui fait C-1 et C-2, vérifié par un agent qui ne l'a pas écrit, puis scellé comme version acceptée. Les mineurs peuvent y être pris au passage. Rien d'autre dans les lignes n'est à reprendre : objet, nombre d'appels, prix comptés, empreintes citées, geste de paiement sont en place.

### Ce qui sépare encore de la première vérification de clé

Dans l'ordre que donnent le texte (préambule de 13) et le devis (0, point 10 ; 12) :
1. **Le devis** : brouillon 3 avec C-1 et C-2, vérifié, version acceptée scellée.
2. **Le constat** : réglages des deux consoles par Lazar ; constat daté, crédit utilisable et limites de débit compris, versé et scellé (`constat-conditions-envoi-google-mistral-bras-a-AAAA-MM-JJ-v1.md`) ; comptes chargés en crédit utilisable (5,50 et 11,50 USD, ou plus avec la taxe).
3. **Le brouillon du texte qui inscrit le constat** à la case « lecteurs et juge des ancres » de 13.1, avant la première vérification. C'est l'affaire du rédacteur du texte.
4. **Les pages de prix** des deux services, versées et scellées, lues par celui qui scelle. Elles sont dues avant la ligne de calcul ; si un prix lu dépasse le prix compté, le devis est repris.
5. **Le fichier des règles**, copie des huit règles, scellé. Le texte le range avant les lignes de calcul. Le devis ne l'exige qu'au premier envoi d'une file (garde 12) et le fait refaire si le brouillon change. Il est à faire avant les lignes, selon l'ordre du texte.
6. **Le programme qui conduit les essais**, en version neuve, avec ses relais (un par ligne) et un faux fournisseur local. Les dix-huit gardes doivent être éprouvées, cas sain et artefact. Contre-lecture du code par un agent neuf d'un autre modèle, puis vérification de ses corrections. La vérification de clé passe par ce programme (gardes 1, 8, 9, 14, 16).
7. **Les lignes de calcul 1 et 2**, et la ligne 5 sous condition : inscrites sur le devis accepté, avec leurs empreintes. Lignes d'engagement au registre des dépenses.
8. **Le réseau** : les trois hôtes permis au réseau de la session, et les deux clés présentes par leur nom (13, point 15). Si les hôtes ne sont pas permis, c'est une décision de Lazar.

## Fichiers ouverts

Empreintes vérifiées par `python -m controle_ia.scellement verifier`, toutes « OK » :
- le brouillon 2 contre-lu, `6f81288b5efc…`, lu en entier ;
- le brouillon 1, `11a352fc3f5c…` : sections 4 à 5.6 et 6.1 lues ; tableau des gardes, par recherche de chaînes ; le reste n'est pas relu ;
- la première contre-lecture, `03bfab589ca1…`, lue en entier ;
- `releve-api-mistral-gemini-essais-admission-v1.md`, `291341e204a8…` ; `releve-api-mistral-gemini-essais-admission-complement-v1.md`, `14d73d5263e2…` ; `conditions-envoi-textes-google-mistral-releve-v1.md`, `b959c4d0db2e…` ; `lecteur-remplacant-carbon-identifiant-fige-mistral-v1.md`, `b8163cc99290…` ; `juge-des-ancres-identifiant-gemini-v1.md`, `ac8bb15e1cfc…` : lus en entier ;
- `mots-de-lazar-juge-et-envoi-des-textes-bras-a-2026-11-21-v1.md`, `00af2aa83604…` ; `mots-de-lazar-devis-essais-admission-bras-a-2026-11-21-v1.md`, `9b9ee5ca4e89…` : lus en entier ;
- `prereg/T0.7-organismes-discrets-v-a-v2-brouillon43.md`, `4f91b535ad91…` : section 3.4 en entier ; 6.11 par recherche de chaînes (« admission », « neon », « mistral », « trois », « envoi ») ; 13.1, case « lecteurs et juge des ancres », ses 7 000 premiers caractères ; 13.2, cases « tarifs », « devis », « version des modèles », « lignes de GO », leurs 2 200 premiers caractères.

Tous sous `docs/notes/relance-organismes-discrets-v1/` sauf le texte.

## Écarts

- **Titres du brouillon 43** : pour repérer les sections, j'ai listé les titres et filtré ceux de 3.4, 3.5, 6.11, 6.12, 7.x, 13, 13.1, 13.2. Les titres de 3.5, 6.12 et 7.x se sont affichés ; je n'ai pas lu ces sections.
- **Hors des sections nommées** : dans le préambule de 13, les deux alinéas qui contiennent « admission » (point 4 et son sous-point sur les essais d'admission). Je les ai lus pour juger l'ordre des étapes.
- **Chemins cloisonnés nommés dans le texte lu** : 3.4, 6.11 et la case de 13.1 nomment `docs/notes/bras-a-contre-lecture-habilitee-v1/…`, `prereg/T0.6-organismes-v0-v1.md` et des chemins sous `runs/`. **Je ne les ai ni suivis, ni listés, ni empreintés.**
- **Une sortie longue** (la section 3.4 affichée en entier) a été gardée d'office par le harnais, hors du dépôt, sous `/root/.claude/projects/…/tool-results/`. Je ne l'ai pas rouverte.
- **Chiffres mesurés du devis** (longueurs de 6.2, octets des consignes) : non vérifiés. Ils viennent de pièces sous `runs/` et des entrées de l'essai de mesure, que je n'ai pas ouvertes. L'arithmétique part des valeurs déclarées.
- **La pièce « 1a 2a 3b4c 5a »**, le devis de l'essai de mesure et la vérification du brouillon 42 ne sont pas ouverts. Je n'en ai pas pris l'empreinte.
- **Aucune liste de dossier.** Le rapport a été vérifié absent avant écriture par un `ls` sur son chemin exact.
- **Fichiers écrits** : celui-ci. Dans le bloc-notes de la session, hors du dépôt : `regles.py` (comparaison des huit règles) et `arith2.py` (calculs). Rien scellé, rien committé, aucun compagnon.
- **Aucun chemin cloisonné ouvert, listé ni empreinté.** `.claude/`, `registres/`, `runs/` et le journal non touchés. Aucun appel de modèle ni appel réseau, aucune clé, aucun sous-agent, aucune dépense.
