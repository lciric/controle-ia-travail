# Organismes discrets, bras A (déplacement des contrôles appris sans consigne) — devis des deux essais d'admission : Mistral Large 4, candidat au second lecteur, et `gemini-4-neon`, juge des deux ancres — v1, BROUILLON 3

- **Objet** : le devis de deux essais payants, sur des textes synthétiques. Le premier dit si Mistral Large 4 (`mistral-large-4-0`) tient comme second lecteur. Le second dit si `gemini-4-neon` tient comme juge des deux ancres. Les règles d'admission sont celles du texte du bras A, **brouillon 43** (`prereg/T0.7-organismes-discrets-v-a-v2-brouillon43.md`, `4f91b535ad91581510615c97039a4cae0a96f4d788088b2aff666d4c3d3f97b3`), section 3.4 ; ce devis ne les change pas. Il fixe ce que le texte lui renvoie : sortie maximale envoyée, champs de jetons et de nom servi, texte jugé, signe de « ne sert pas ce modèle », délais, tarifs, plafonds, lignes de calcul.
- **État** : brouillon 3, scellé comme brouillon, non vérifié, non accepté. Il reprend le brouillon 2 (`6f81288b5efca85fa5063decfb84a3c173dc989377b902245a7dea665c979cee`), laissé inchangé, après sa contre-lecture (`contre-lecture-devis-essais-admission-brouillon2-v1.md`, `a70c5f211445262700c4ad089be8eff14a090229123113b83123249a0109c05a` : « Engageable après corrections », deux corrections, onze mineurs). Le brouillon 2 reprenait le brouillon 1 (`11a352fc3f5c…`) après sa contre-lecture (`03bfab589ca1…`). **Aucune dépense n'est ouverte. Aucun appel avant sa ligne de calcul.**
- **En tête, pour Lazar : les montants à charger changent.** Crédit utilisable : **9,50 USD chez Mistral** (5,50 au brouillon 2) ; **29,00 USD chez Google** (11,50 au brouillon 2). Le plafond de la file Mistral passe de 4,25 à **4,75 USD** ; les quatre autres plafonds ne changent pas. Chaque ligne de calcul porte désormais, à côté de son plafond, **l'excès possible d'un seul envoi**, chiffré à un débit déclaré (section 6.4). Les critères, les huit règles, les décisions « goreco » et les conditions d'envoi ne changent pas.
- **Auteur** : agent neuf (Claude Fable 5.2), même rôle qu'aux brouillons 1 et 2, le 2026-11-21, vers 12:05 UTC (`date -u`). N'a écrit ni le texte du bras A, ni ses vérifications, ni le devis de l'essai de mesure, ni les contre-lectures des brouillons 1 et 2.
- **Interdits tenus** : aucun appel de modèle ; aucun appel réseau ; aucune clé lue ni écrite ; aucun sous-agent ; aucune dépense ; rien committé ni poussé ; `registres/`, `.claude/`, `runs/` et le journal non touchés. Franchissements et débords : section 14.
- **Trois lettres** : **M** = relevé sur une pièce ; **C** = calculé ici ; **S** = supposé, sans mesure ni pièce.
- **Changements depuis le brouillon 2** : section 17, une ligne par correction et par mineur. **Changements depuis le brouillon 1** : section 16, reprise du brouillon 2.

## 0. En une page

1. **Deux files indépendantes, une par fournisseur.** File Mistral : 24 appels, 48 envois au plus, plafond **4,75 USD**. File Neon : 8 appels, 16 envois au plus, plafond **8,50 USD**. Aucune n'attend l'autre.
2. **Une vérification de clé avant chaque file**, sous sa propre ligne, **trois appels au plus, soit trois envois** (décidé par Lazar) : Mistral par le point d'accès européen, plafond **0,25 USD** ; Google, plafond **1,50 USD** ; et, seulement si le signe de « ne sert pas ce modèle » est constaté, Mistral par le point d'accès global, plafond **0,25 USD**, ligne accordée d'avance sous cette condition (décidé par Lazar).
3. **Coût attendu ≈ 0,55 USD. Somme des plafonds : 15,25 USD** (15,00 sans le repli). Les plafonds sont au pire cas, à dessein. **Ce qu'ils bornent, et ce qu'ils ne bornent pas** : point 12 et section 6.4.
4. **À charger, en crédit utilisable** : **9,50 USD chez Mistral** ; **29,00 USD chez Google**. Si une taxe de 20 % s'ajoute à la recharge (S), le paiement est de **11,40 et 34,80 USD**. Règle : avant toute file, le crédit utilisable couvre la somme des plafonds et des excès possibles des lignes du fournisseur, soit 8,23 USD chez Mistral et 25,16 chez Google (section 6.5).
5. **Sortie maximale envoyée : 32 768 jetons aux deux** (décidé par Lazar). Réglages : Mistral, `reasoning_effort` à `high` ; Neon, niveau de réflexion le plus haut (`xhigh`). Un seul réglage par modèle.
6. **Ce que borne la sortie maximale n'est pas écrit pour ces deux appels.** Deux choix (section 5.4) : la garde de sortie maximale ne lit que le motif de fin ; et chaque vérification de clé porte un appel de sonde, à borne courte, qui mesure si la réflexion compte dans la borne. **La sonde ne dit « comprise » que si une réflexion a été vue** (4.6). Si elle ne dit pas « comprise », c'est un nœud de Lazar avant la file.
7. **Délais** : Mistral lu en flux, 600 secondes de silence, 2 700 au total par envoi ; Google lu sans flux, 2 700 secondes par envoi. Une lecture à la sortie maximale tient à 12,2 jetons par seconde ou plus. Le délai global de chaque file couvre le pire cas de ses envois (section 5.6).
8. **Deux envois au plus par appel**, selon le texte : l'envoi, et une reprise sur une panne de transport. **Aucune redemande de forme.** La contre-lecture l'a jugé fidèle au texte.
9. **Rapport aux seuls champs techniques.** Personne ne lit les réponses. Les règles sont appliquées par programme.
10. **Rien ne part** sans : les réglages des deux consoles constatés et datés, inscrits à la case de 13.1 d'un brouillon du texte ; ce devis vérifié par un autre modèle ; le fichier des règles scellé ; le programme qui conduit les essais contre-lu, gardes éprouvées ; la ligne de calcul.
11. **Une file ne part jamais sur une forme non constatée** : tout ce que la documentation tait a son issue écrite ici, constatée à la vérification de la clé (section 4).
12. **Ce que bornent les plafonds, et l'excès** (section 6.4). Chez Mistral, lu en flux, une **borne dure par envoi**, tenue par le programme : il compte les octets de contenu du flux et coupe l'envoi à 262 144 octets (32 768 à la vérification). Un envoi coupé arrête la file : elle est « arrêtée à son plafond » et ne tient pas. Chez Google, lu sans flux, rien ne se voit avant la fin de la réponse : le plafond n'est tenu que si la sortie maximale borne la réflexion ; **sinon, excès possible d'un seul envoi par ligne, au plus 7,58 USD au débit déclaré de 200 jetons par seconde (S)**. Chez Mistral, l'excès (1,17 USD pour une vérification, 0,64 pour la file) ne joue que si l'une des deux suppositions de la borne manque. Ces excès sont écrits aux lignes de calcul et au nœud de la sonde ; le crédit chargé les couvre.

## 1. D'où viennent ces essais, les décisions de Lazar, et l'écart déclaré

- **Essai du second lecteur** : mot de Lazar « 1a 2a 3b4c 5a » (pièce `mots-de-lazar-cinq-choix-lecteur-bras-a-2026-11-20-v1.md`, `93cbc6f4c78d00c5b91ca29e5b300bef345cd7aa46c89db2be6bff95a46d5beb`) et GO-2026-11-20-43 (essai sous une règle scellée avant lecture), selon le texte, section 3.4.
- **Essai du juge** : mot de Lazar « b a b go », choix 1 (b) (pièce `mots-de-lazar-juge-et-envoi-des-textes-bras-a-2026-11-21-v1.md`, `00af2aa83604df20181e9ea0fdcf15fbd88601f98f96388ce32d23d7c0a98e5a`) : huit lectures sur les huit entrées de l'ancienne file du juge ; admis si huit sur huit sont de forme conforme ; sinon nœud de Lazar.
- **Conditions d'envoi des textes** : même mot, choix 3 (b).
- **Ces deux mots sont inscrits au registre** : **GO-2026-11-21-32** pour « 1a 2a 3b4c 5a », **GO-2026-11-21-33** pour « b a b go » (M : brouillon 43, case « lecteurs et juge des ancres » de 13.1, qui les dit lues aux lignes 631 et 632, tête `e77fa0d9` de la référence locale de la branche principale ; je n'ai pas ouvert le registre).
- **Aucune de ces lignes n'ouvre une dépense.**

**Trois décisions de Lazar sur ce devis**, mot « goreco » (pièce scellée `docs/notes/relance-organismes-discrets-v1/mots-de-lazar-devis-essais-admission-bras-a-2026-11-21-v1.md`, `9b9ee5ca4e89f3dcd8d4c5865f7badf613943f00800b9a80d011bd6f45b1c57b`, empreinte vérifiée ici contre son compagnon) :
1. **une ligne de calcul de vérification de clé couvre trois appels au plus**, écrit en toutes lettres à la ligne ;
2. **la sortie maximale envoyée aux deux files est de 32 768 jetons**, à revoir si les délais ne tiennent pas : **ils tiennent si le service rend 12,2 jetons par seconde ou plus (5.6) ; ce débit n'est pas mesuré (S)**. C'est à dire ainsi à Lazar, à la demande des lignes (section 11) ;
3. **la ligne de calcul du repli de Mistral sur le point d'accès global est accordée d'avance, sous condition** : elle ne joue que si le signe fixé en 4.5 est constaté sur le point d'accès européen, sous la garde qui lie l'une à l'autre (garde 15).

Ce mot n'ouvre aucune dépense : les lignes de calcul restent à demander sur le devis vérifié (section 11).

**Écart déclaré à la première consigne de rédaction : deux envois, non trois.** Le texte dit, pour ces essais : « 24 appels, 48 envois au plus (un envoi et une reprise) » ; « 8 appels, 16 envois au plus » (3.4, « Ce qui est joué »). La règle 1 reprend le critère de l'essai de mesure « inchangé », et cet essai n'avait aucune redemande de forme. Le « trois » de 6.11 est le majorant de la course. La contre-lecture juge ce choix « fidèle au texte » ; rien n'est demandé à Lazar. Le pire cas à trois envois reste donné pour information (6.3).

## 2. Pièces lues, avec empreintes (sha256)

« V » = empreinte calculée par moi à cette rédaction. « B2 » = empreinte calculée au brouillon 2, non recalculée ici. « B1 » = empreinte reprise du brouillon 1, non recalculée. La colonne « usage » dit ce que les brouillons en ont tiré ; ce que j'ai rouvert à cette rédaction est en section 14.

| pièce | empreinte | usage |
|---|---|---|
| `prereg/T0.7-organismes-discrets-v-a-v2-brouillon43.md` | `4f91b535ad91581510615c97039a4cae0a96f4d788088b2aff666d4c3d3f97b3` (V) | 3.4 ; 6.11 ; préambule de 13, point 4 ; 13.1, case « lecteurs et juge des ancres » ; 13.2, cases « tarifs », « devis », « version des modèles », « lignes de GO » |
| le brouillon 2 de ce devis | `6f81288b5efca85fa5063decfb84a3c173dc989377b902245a7dea665c979cee` (V) | base de ce brouillon |
| `contre-lecture-devis-essais-admission-brouillon2-v1.md` | `a70c5f211445262700c4ad089be8eff14a090229123113b83123249a0109c05a` (V) | deux corrections, onze mineurs |
| le brouillon 1 de ce devis | `11a352fc3f5c59cc71800827911bf22bf0634183aad63ea63457c61072aa8b10` (B2) | base du brouillon 2 |
| `contre-lecture-devis-essais-admission-brouillon1-v1.md` | `03bfab589ca152dae7bfbfb0baaf53f2013e74707f4ec4caceadc0dd7258ad62` (B2) | huit corrections, dix mineurs, trois questions |
| `releve-api-mistral-gemini-essais-admission-v1.md` | `291341e204a8cfb74548f58221d3795d73f007cb0987d4e4051bc7d35a4c32c9` (V) | formes des appels et des réponses, délais, prix ; **non opposable (R7)** |
| `releve-api-mistral-gemini-essais-admission-complement-v1.md` | `14d73d5263e2c0ba1e52c7794719e702ce05d3354c118cc4f5be39e3ba88a957` (V) | bloc d'usage et motifs de fin de Mistral ; **non opposable (R7)** |
| `mots-de-lazar-devis-essais-admission-bras-a-2026-11-21-v1.md` | `9b9ee5ca4e89f3dcd8d4c5865f7badf613943f00800b9a80d011bd6f45b1c57b` (V) | « goreco » : les trois décisions |
| `mots-de-lazar-juge-et-envoi-des-textes-bras-a-2026-11-21-v1.md` | `00af2aa83604df20181e9ea0fdcf15fbd88601f98f96388ce32d23d7c0a98e5a` (B2) | « b a b go » |
| `mots-de-lazar-cinq-choix-lecteur-bras-a-2026-11-20-v1.md` | `93cbc6f4c78d00c5b91ca29e5b300bef345cd7aa46c89db2be6bff95a46d5beb` (B2) | empreinte seulement |
| `lecteur-remplacant-carbon-identifiant-fige-mistral-v1.md` | `b8163cc992903311e07b6fd60c36db413dda2bbbded8ae4d6c4a750a3278130f` (B2) | identifiant de Mistral ; disponibilité générale ; 404 après retrait ; non opposable |
| `juge-des-ancres-identifiant-gemini-v1.md` | `ac8bb15e1cfc137e958775c46c4196e120fa46f4981625ce6a67f17ab6fc6ba2` (B2) | nom stable ; prix de Neon ; niveaux de réflexion ; non opposable |
| `conditions-envoi-textes-google-mistral-releve-v1.md` | `b959c4d0db2e7b3168fac51a0d06c117312c7a0a011d7b1bb0bdad35609aaca2` (V) | conditions d'envoi ; exceptions « Labs » et « Preview » ; 1,1 fois ; non opposable |
| `devis-essai-de-mesure-lecteurs-bras-a-v1-brouillon3.md` | `533ad5b15e6de1bdfe81c35f8501dbad376f52f907be84094c3fd8621b349592` (B2) | empreinte seulement ; contenu repris du brouillon 1 |
| `verification-brouillon42-bras-a-v1.md` | `dcf742d5d1025cefec91032cc236cbc4bffdf36cacd301a9eda8c01f7340ed3b` (B2) | empreinte seulement |
| recherche de la session principale, `…/lecteur-remplacant-carbon-v1/choix-mistral-deepseek-v1.md` | `f7090b5d52b6…` (B1) | prix et limites de débit de Mistral, repris du brouillon 1 |
| `essai-mesure-lecteurs-bras-a-v1/configuration-essai-mesure-lecteurs-bras-a-v1.json` | `e047c502ca71…` (B1) | noms de clés ; les huit entrées de la file du juge ; repris du brouillon 1 |
| `essai-mesure-lecteurs-bras-a-v1/entrees-essai-mesure-lecteurs-bras-a-v1.json` | `15b62bb44d9f…` (B1) | nombre, forme, octets ; repris du brouillon 1 |
| trois rapports techniques sous `runs/essai-mesure-lecteurs-bras-a-v1/` | `06286c5061a9…` ; `27f292bb7eef…` ; `93e1cdfc79c2…` (B1) | longueurs mesurées de 6.2, reprises du brouillon 1 ; **non rouverts** |

Tous sous `docs/notes/relance-organismes-discrets-v1/` sauf mention.

## 3. Les entrées

- **File Mistral** : les 24 entrées synthétiques de l'essai de mesure, les mêmes (`15b62bb4…`) : 18 de l'appariement, 6 de la couverture. Ordre : celui du lot, par blocs.
- **File Neon** : les huit entrées que la configuration de l'essai de mesure donnait à la file du juge (M, brouillon 1) : `A-b1-01` à `A-b1-06` (appariement) ; `C-b1-02` et `C-b1-03` (couverture). Ordre : celui-ci. **Ces huit identifiants et cet ordre sont écrits à la configuration ; le programme refuse toute autre entrée** (garde 17).
- **Consignes** : les deux blocs de 3.2 et 3.3 du texte, aux empreintes de 13.1 (`98a9bd34d280…`, `ecf590eae0c0…`), égales à celles du lot (M, brouillon 1). Le lot porte, pour chaque entrée, les octets et l'empreinte de la consigne remplie : le programme la recompose et la compare avant l'envoi.
- **Un seul message, de rôle « user »**, qui porte la consigne remplie. Ni message système, ni outils.
- Aucune tâche du bras, de réserve ou d'évaluation ; aucune référence cachée ; aucun épisode ; aucun texte de l'agent. Je n'ai ouvert le contenu d'aucune entrée.

## 4. Vérification de chaque clé, avant sa file

Principe : **une file est partie dès son premier envoi et ne se rejoue pas.** Toute cause d'arrêt qui n'est pas le modèle se lève donc ici. Ce que la documentation tait se constate ici, sur une issue écrite d'avance. La session ne choisit rien après avoir vu une réponse.

### 4.1 Ce qui est commun
- **Avant elle** : les conditions d'envoi constatées, datées, et inscrites à la case de 13.1 d'un brouillon du texte (section 9) ; sa ligne de calcul.
- **Avant tout appel au modèle, un appel de liste, gratuit, qui n'envoie aucun texte** : Mistral, `GET /v1/models` sur le point d'accès essayé ; Google, `GET /v1beta/models/gemini-4-neon`. Le programme n'en garde que le code de retour, la présence de l'identifiant, et, pour Google, le nombre `outputTokenLimit` s'il est rendu.
- **Clés lues par leur nom seulement**, dans l'environnement du seul relais : `MISTRAL_API_KEY` ; `GEMINI_API_KEY`. Présence vérifiée, valeur jamais lue ni affichée.
- **Une ligne par vérification, qui couvre trois appels au modèle au plus, soit trois envois au plus**, sur un même point d'accès (décision de Lazar, section 1). Aucun appel de vérification n'a de reprise : chaque envoi est un appel. Tout ce qui se refait — après une cause corrigée, après le retrait de la température, après un changement d'orthographe écrit en 4.4 — reste sous cette ligne, dans ce compte et sous son plafond. Au-delà de trois, ligne nouvelle. Chaque appel est compté et rapporté.
- **Relevé par programme, versé et scellé** (`runs/verification-cle-<fournisseur>-bras-a-v1/releve-verification-v1.json`) : point d'accès ; mode de lecture (flux ou non) ; par appel, code de retour, nom servi, compteurs, coût compté, motif de fin, longueur du texte extrait, durée ; pour Mistral, octets de contenu reçus et nombre de morceaux du flux par type (5.5), envoi coupé à sa borne en octets, oui ou non ; **noms** des champs du bloc d'usage ; orthographes retenues ; issue de la sonde (4.6) ; constat du majorant par octets (4.3) ; date. Le texte des réponses de code 200 n'est ni lu ni rapporté.
- **Pour une réponse d'erreur d'un appel de vérification, et pour elle seule**, le relevé porte le corps d'erreur du service, borné à 500 caractères : il ne contient aucune lecture, et Lazar en a besoin si l'issue est un nœud. Rien de tel dans les files.
- **Une vérification qui échoue n'est pas un « ne tient pas »** : la file ne part pas.

### 4.2 Les trois appels au plus
- **Appel A, aux réglages pleins.** Message fixe, écrit à la configuration : `Reply with the single word: OK`. Aucun texte d'essai ni de course. **Son corps porte exactement les réglages de la file** : même sortie maximale, même réglage de raisonnement, même traitement de la température, même mode de lecture, mêmes délais (section 5). Un champ refusé ou une forme inattendue se voit ici, non au premier envoi de la file. Une seule chose diffère, hors du corps : la borne en octets que tient le programme, plus basse à la vérification (6.4).
- **Appel A′**, seulement dans les deux cas écrits en 4.4 : sans la température (Mistral) ; avec la seconde orthographe du niveau de réflexion (Google). Même message.
- **Appel B, la sonde de borne** (4.6), seulement après un appel A ou A′ sain. C'est le seul appel dont le corps diffère de celui de la file, par deux champs : la sortie maximale, courte, et le message.
- Si une cause à corriger a déjà pris un appel, et que A′ est dû, **le troisième appel est A′** : l'appel B exige un appel A ou A′ sain, il ne peut donc pas le précéder. L'appel B demande alors une ligne nouvelle.

### 4.3 Forme exigée de la réponse de code 200 (appels A et A′)
La vérification est **saine** si, et seulement si, tout ce qui suit est vrai. La liste des modèles n'y entre pas.

| | Mistral, lu en flux | Google, lu sans flux |
|---|---|---|
| code | 200 | 200 |
| nom servi | au moins un événement de données du flux porte un champ `model` ; **chaque événement qui le porte le porte égal à la lettre à `mistral-large-4-0`** | champ `modelVersion` présent, **égal à la lettre à `gemini-4-neon`** |
| compteurs | un événement du flux porte `usage`, avec `prompt_tokens`, `completion_tokens` et `total_tokens`, entiers | `usageMetadata` porte `promptTokenCount`, `candidatesTokenCount` et `totalTokenCount`, entiers ; `thoughtsTokenCount` absent vaut 0 |
| motif de fin | un événement porte `choices[0].finish_reason` non nul, égal à `stop` | `candidates[0].finishReason` présent, égal à `STOP` |
| texte jugé | l'extraction de 5.5 rend une chaîne non vide | l'extraction de 5.5 rend une chaîne non vide |

- **Forme du nom servi : la documentation se tait** (M : « forme rendue pour Large 4 : non trouvée » ; « forme rendue pour Neon : non trouvée »). **Issue fixée d'avance** : seule l'égalité à la lettre est saine. Toute autre forme sous le code 200 — un suffixe de date, un préfixe `models/`, une autre casse, un alias — est le cas « code 200 avec un autre nom servi » : **nœud de Lazar**, sans repli ni file. La session ne normalise rien.
- **Si le code est 200 et le nom servi égal, mais qu'un autre champ du tableau manque ou que le texte n'est pas extractible** : vérification **non saine** ; ce devis est repris dans un brouillon neuf, vérifié, avant toute file. Exemple : un flux de Mistral qui ne rend pas `usage`.
- Le nom servi relevé et les orthographes retenues sont inscrits à la configuration des files.
- **Le champ `model` dans le flux de Mistral, tranché ici** : un événement de données sans champ `model` — par exemple un dernier événement qui ne porterait que `usage` — ne rend pas la vérification non saine. Un seul événement dont le `model` diffère la rend « code 200 avec un autre nom servi » (4.4, ligne 4). Le marqueur de fin `[DONE]` n'est pas un événement de données. Aucun événement ne porte `model` : nom servi absent (ligne 4). La même lecture vaut pour chaque réponse d'une file (5.5 ; garde 5).
- **Constat du majorant par octets, chez Mistral** (il sert la borne dure de 6.4). À chaque appel de code 200 de la vérification, le programme compare la sortie facturée (la plus grande des deux lectures de 5.5) aux octets de contenu reçus (5.5). **« Établi »** si, à chaque appel, la sortie facturée est au plus égale aux octets de contenu reçus plus 64. **« Démenti »** si un seul appel la passe : le service facture alors des jetons que le flux ne rend pas. La vérification reste saine sur sa forme, mais **« démenti » est un nœud de Lazar avant la file**, porté comme celui de la sonde (4.6), avec le chiffre de l'excès (6.4).

### 4.4 Classement fermé des issues des appels A et A′ (la première ligne qui s'applique)

« Nomme le champ X » est défini par programme, sans égard à la casse : la chaîne X se trouve dans le champ `param` du corps d'erreur ; ou **un élément d'un `loc` d'une entrée de `detail` est égal à X** ; ou X se trouve dans un champ `field` d'une entrée de `fieldViolations` ; ou X se trouve dans le message d'erreur (`message` ou `error.message`). « Se trouve dans » : X en est une sous-chaîne. Pour `loc`, c'est l'égalité d'un élément, non une sous-chaîne. Les champs de réglage cherchés sont, en liste close : `temperature` ; `max_tokens` ; `reasoning_effort` ; `stream` (Mistral) ; `maxOutputTokens` ou `max_output_tokens` ; `thinkingLevel`, `thinking_level` ou `thinkingConfig` (Google). « Nomme seulement X » : X est nommé, et aucun autre champ de la liste ne l'est.

| n° | constat, par programme | issue |
|---|---|---|
| 1 | aucune réponse du fournisseur : refus du mandataire du réseau (hôte non permis), **à la signature écrite sous ce tableau** | rien n'en est conclu ; l'accès au réseau est une décision de Lazar ; l'appel n'est compté ni parmi les trois, ni au compteur de la ligne : rien n'a atteint le fournisseur |
| 2 | Google : `outputTokenLimit` rendu par l'appel de liste, sous 32 768 | aucun appel payant ; brouillon neuf de ce devis |
| 3 | code 200, forme de 4.3 entière | **saine** ; point d'accès retenu, quelle que soit la liste |
| 4 | code 200, nom servi autre que l'identifiant demandé, ou absent | **nœud de Lazar** ; pas de repli |
| 5 | code 200, nom servi égal, autre défaut de forme | non saine ; brouillon neuf de ce devis |
| 6 | codes 429, 500 à 599, délai dépassé, connexion coupée | cause à attendre ou à corriger ; refaite sous la même ligne |
| 7 | codes 401, 402 ou 403, **et** la liste du même point d'accès n'a pas rendu « 200, lisible, sans l'identifiant » | cause à corriger (clé refusée, compte non approvisionné) ; refaite sous la même ligne |
| 8 | codes 401, 402 ou 403, **et** la liste a rendu « 200, lisible, sans l'identifiant » | **nœud de Lazar** : le modèle n'est sans doute pas servi à ce compte sur ce point d'accès |
| 9 | Mistral, point d'accès européen : **le signe de 4.5** | repli sur le point d'accès global, sous la ligne 5 |
| 10 | Mistral : code 400 ou 422 qui nomme seulement `temperature`, à l'appel A | la température est retirée ; appel A′ sans elle ; la file ne l'envoie pas ; le relevé et le rapport le disent |
| 11 | Google : code 400 qui nomme seulement le champ du niveau de réflexion, à l'appel A, envoyé avec `"XHIGH"` | appel A′ avec `"xhigh"` ; l'orthographe saine est inscrite et sert à la file |
| 12 | code 400 ou 422 qui nomme un autre champ de la liste, ou plusieurs, ou le même champ à l'appel A′ | rien d'autre n'est essayé ; brouillon neuf de ce devis |
| 13 | **toute autre issue** : 404 hors du signe, 400 ou 422 qui ne nomme aucun champ de la liste, modèle inconnu chez Google ou sur le point d'accès global de Mistral, constats de la liste et de l'appel qui se contredisent, corps illisible, envoi de Mistral coupé à sa borne en octets (6.4), tout autre code | **non saine ; nœud de Lazar ; ni repli, ni appel de plus** |

- **Température de Mistral** : le texte veut « 0 si le service l'accepte, retirée s'il la refuse ou la dit sans effet ». La documentation conseille une valeur « between 0.0 and 0.7 » ; son effet sous raisonnement : non trouvé (M, non opposable). Rien ne la dit refusée ni sans effet : elle est envoyée à 0, et retirée par la ligne 10 seulement.
- **Niveau de réflexion de Google** : le champ est `generationConfig.thinkingConfig.thinkingLevel` ; le relevé donne les valeurs de l'appel en majuscules (`XHIGH`) et les niveaux de Neon en minuscules (`xhigh`), tous deux d'un résumé d'outil (M, non opposable). **Issue fixée d'avance** : `"XHIGH"` d'abord, `"xhigh"` ensuite, par la ligne 11, et rien d'autre. **Limite écrite** : un niveau accepté ne prouve pas qu'il est appliqué ; le compte `thoughtsTokenCount` est rapporté.
- **Liste « lisible »** (Mistral) : le corps est du JSON, soit un objet dont le champ `data` est un tableau, soit un tableau nu — le relevé note les deux formes, sans trancher — ; chaque entrée est un objet qui a un champ `id`, une chaîne. Seul `id` est comparé à `mistral-large-4-0` ; les champs `aliases` sont ignorés. Toute autre forme : liste non lisible.
- **Signature du refus du mandataire** (ligne 1), par programme. Le relais rend son code 502 avec l'origine `mandataire`. Il ne la pose que si l'établissement de la connexion vers l'amont a échoué avant tout octet de la requête : connexion refusée, ou réponse du mandataire à la demande de tunnel d'un code autre que 200. Et son journal porte, pour cet envoi, zéro octet envoyé à l'amont. Le programme exige les deux. **Sans cette signature**, une absence de réponse est une panne : ligne 6, comptée parmi les trois et au compteur, à sa réserve. Le brouillon 2 disait l'appel « non compté parmi les trois », alors que son compteur le comptait au pire cas : les deux sont accordés ici.

### 4.5 Point d'accès de Mistral, et le signe exact de « ne sert pas ce modèle »
- La vérification se fait **d'abord** sur le point d'accès européen, `https://api.eu.mistral.ai`. Si l'appel A ou A′ y est sain (4.3), ce point est retenu, inscrit, et ne change plus. **Cela vaut même si la liste ne porte pas l'identifiant** : la liste n'entre pas dans la santé de la vérification.
- **La forme de l'erreur « modèle inconnu » n'est pas documentée** (M : « non trouvée » ; le schéma ne donne, pour cet appel, que le code 422, « Validation Error »). Le relevé de l'identifiant dit seulement « après retrait, réponse 404 » (M). **Issue fixée d'avance** : le signe ci-dessous est fermé ; une erreur d'une autre forme n'est pas le signe, et c'est un nœud de Lazar (ligne 13 de 4.4), non un repli.
- **Le point d'accès européen « ne sert pas ce modèle » si, et seulement si, les trois constats suivants sont faits par programme, sur ce point d'accès, dans la même vérification** :
  1. l'appel de liste rend le code **200** et une liste lisible (4.4) où **aucune entrée n'a l'identifiant `mistral-large-4-0`** — la clé est donc admise sur ce point d'accès ;
  2. l'appel A rend le code **400, 404 ou 422** ;
  3. le corps d'erreur, lu comme du JSON, désigne le modèle, par l'une de ces formes : `type` vaut `invalid_model` ; **ou** `code`, comparé comme une chaîne, vaut `1500` ; **ou** `message` contient `mistral-large-4-0` et l'une des chaînes `invalid model`, `model not found`, `unknown model`, `does not exist`, sans égard à la casse ; **ou** `detail` est un tableau dont une entrée a un `loc` dont **un élément est égal à la chaîne `model`**, sans égard à la casse, et aucune entrée n'a un `loc` dont un élément est égal à un champ de réglage de la liste de 4.4. C'est l'égalité d'un élément, non une sous-chaîne : un élément `model_config` ne désigne pas le modèle.
- **Ce qui est supposé (S)** : les formes du constat 3 viennent de ce que le rédacteur sait de l'interface de Mistral et de la forme courante d'une erreur 422 ; **aucune pièce ne les établit**. **Choix déclaré, que le vérificateur peut retirer** : le code 422 et la forme `detail` sont ajoutés au brouillon 1, parce que 422 est le seul code d'erreur que le schéma écrit pour cet appel. Le constat 1 garde le signe étroit : sans une liste admise qui ne porte pas l'identifiant, il n'y a pas de signe. **Cet élargissement est postérieur au mot « goreco »**, qui accorde la ligne 5 sur « le signe fixé au devis » : il est dit à Lazar avec la ligne 5, signe recopié (section 11).
- **Si le signe est constaté** : repli sur le point d'accès global, `https://api.mistral.ai`, sous la ligne 5, accordée d'avance sous cette condition (décision de Lazar). **La vérification globale exige le relevé scellé de la vérification européenne, signe constaté** (garde 15). Le repli est déclaré au relevé, au rapport et à la case de 13.1.
- **Sur le point d'accès global, il n'y a ni signe ni repli** : modèle inconnu, ou toute issue de la ligne 13, est un nœud de Lazar.
- **Tarif** : le point d'accès européen coûte 1,1 fois le prix courant (M, non opposable). Tout est compté à ce prix, repli compris : borne haute.

### 4.6 Appel B : la sonde de borne
- **Ce qu'elle mesure** : si la réflexion compte dans la sortie maximale du service. La documentation ne l'écrit pas pour ces appels (5.4).
- **Corps** : celui de la file, sauf deux champs. Sortie maximale : **256** (`max_tokens: 256` ; `maxOutputTokens: 256`). Message fixe, écrit à la configuration, qui demande un calcul et non une lecture : `Work out 48271 multiplied by 96553, checking your work twice, then reply with the product only.` Même réglage de raisonnement, même mode de lecture, même traitement de la température que l'appel sain.
- **Issue, par programme, sur la sortie facturée de 5.5, le motif de fin et la réflexion constatée** (la première ligne qui s'applique).
  - **Sortie facturée** : si les deux lectures de 5.5 diffèrent — `completion_tokens` et `total_tokens − prompt_tokens` chez Mistral ; la somme des deux comptes et `totalTokenCount − promptTokenCount` chez Google —, **la plus grande**, comme pour le coût.
  - **Réflexion constatée** : chez Google, `thoughtsTokenCount` supérieur à 0 ; chez Mistral, **au moins un morceau de pensée dans le flux**, compté par son type, sans être lu. Un morceau de pensée est un élément d'une liste `delta.content` dont le champ `type` vaut `thinking` (S : le relevé dit « morceau de pensée » sans en donner le nom de type ; le relevé de vérification rend le nombre de morceaux par type, 5.5).

| constat | issue de la sonde |
|---|---|
| Mistral : l'envoi est coupé à sa borne en octets (6.4), soit plus de 32 768 octets de contenu reçus sous une borne de 256 jetons | **« non comprise »**, par constat d'octets, dit tel au relevé |
| sortie facturée au-dessus de 256 | **« non comprise »** : la borne ne tient pas la réflexion |
| sortie facturée d'au plus 256, motif de fin par sortie maximale atteinte (5.5), **et réflexion constatée** | **« comprise »** : la borne tient réponse et réflexion ensemble |
| tout le reste : **au plus 256 facturés et fin par sortie maximale atteinte, sans réflexion constatée** ; fin normale sous 256 ; refus ; code d'erreur ; forme illisible | **« indécidée »** |

- **Pourquoi exiger une réflexion constatée** (contre-lecture, correction 1) : sans elle, un modèle qui ne réfléchit pas et dont la réponse visible atteint 256 jetons donnerait « comprise », alors que rien n'aurait été mesuré de la réflexion. La condition (c) de 6.4 et la règle 7 du texte seraient lues sur un constat vide.
- **Ce que l'issue commande** :
  - **« comprise »** : la file peut partir. Le constat est inscrit au relevé. La règle 7 du texte se lit sur « réponse et réflexion ensemble ».
  - **« non comprise » ou « indécidée »** : **nœud de Lazar avant la file.** Sans le mot de Lazar, la file ne part pas (garde 10). Ce qui lui est porté, écrit d'avance :
    - les règles de la file ne dépendent pas de la borne (5.4) ; la règle 7 du texte demande ce constat ;
    - **file Neon** : « le plafond de 8,50 USD est tenu par compteur si la sortie maximale borne la réflexion ; sinon, excès possible d'un envoi, au plus 7,58 USD au débit déclaré de 200 jetons par seconde (S), soit 16,08 USD au plus pour la file » (6.4) ;
    - **file Mistral** : « le plafond de 4,75 USD est tenu par compteur et par une borne dure en octets par envoi, sous deux suppositions ; si l'une manque, excès possible d'un envoi, au plus 0,64 USD au même débit, soit 5,39 USD au plus pour la file. Une lecture dont le contenu passe 262 144 octets est coupée, et la file ne tient pas » (6.4) ;
    - **recommandation écrite d'avance** : partir, aux mêmes réglages, la règle 7 lue sur la sortie facturée entière, qui majore la réponse seule — si le crédit utilisable constaté couvre encore le plafond et l'excès de la file ; sinon, recharger d'abord.
  - La forme du mot de Lazar est écrite à la garde 10.
- Un code 429, 5xx ou un délai à l'appel B se refait s'il reste un appel sous la ligne.
- **Limites, dites** :
  - la sonde mesure la borne à 256, sur un message court ; elle suppose que la borne se comporte de même à 32 768 ;
  - à l'effort le plus haut, le modèle peut ne pas réfléchir 256 jetons sur ce calcul : l'issue est alors « indécidée » ;
  - chez Mistral, si la pensée n'est pas émise en morceaux de type `thinking`, la sonde ne peut pas dire « comprise » : elle dit « indécidée », et le nombre de morceaux par type va à Lazar ;
  - chez Mistral, que `completion_tokens` comprenne le raisonnement n'est pas écrit (5.5). S'il ne le comprenait pas, « comprise » ne serait faux que si la réponse visible atteignait seule 256 jetons, sur un message qui demande un seul nombre. La longueur du texte extrait est au relevé : Lazar la voit ;
  - **si la réflexion est hors de la borne, la sonde coûte plus que 256 jetons.** Chez Mistral, elle est coupée à 32 768 octets et comptée à sa réserve. Chez Google, rien ne la borne que le délai : c'est l'excès de la ligne 2 (6.4). La sonde, comme les appels A et A′, part avant que rien ne soit mesuré.

## 5. Les deux files : réglages, corps des appels, compteurs

### 5.1 Tableau

| file | modèle | réglage, un seul | sortie maximale envoyée | lecture de l'amont | appels | envois au plus | plafond |
|---|---|---|---|---|---|---|---|
| **Mistral** | `mistral-large-4-0`, par le service de Mistral, point d'accès retenu en 4.5 | `reasoning_effort` à `high` | **32 768** | en flux | **24** | 48 | **4,75 USD** |
| **Neon** | `gemini-4-neon`, par le service de Google, offre payante | niveau de réflexion le plus haut, `xhigh` | **32 768** | sans flux | **8** | 16 | **8,50 USD** |

Pour les deux : appels synchrones, jamais par lot ; un appel à la fois, dans l'ordre ; un tirage par lecture ; aucun repli sur un autre modèle ; une file n'est jouée qu'une fois.

### 5.2 Corps de l'appel à Mistral (champs exacts, écrits à la configuration)
`POST /v1/chat/completions`. `model: "mistral-large-4-0"` ; `messages` : un seul, `role: "user"`, `content` : la consigne remplie ; `max_tokens: 32768` ; `reasoning_effort: "high"` ; `stream: true` ; `temperature: 0`, sauf retrait constaté à la vérification (4.4, ligne 10). **Rien d'autre** : ni `top_p`, ni `random_seed`, ni `response_format`, ni `tools`, ni `safe_prompt`, ni `n`, ni option de flux, ni message système. Le programme refuse tout envoi qui porterait un autre champ.
- `high` est le niveau le plus haut que Large 4 accepte : il refuse `none`, `minimal`, `xhigh` et `max` ; `high` est aussi son défaut (M, non opposable).
- **Pourquoi en flux** : section 5.6.

### 5.3 Corps de l'appel à Google
`POST /v1beta/models/gemini-4-neon:generateContent`, **sans flux**. `contents` : un seul, `role: "user"`, une part de texte, la consigne remplie ; `generationConfig.maxOutputTokens: 32768` ; `generationConfig.thinkingConfig.thinkingLevel` : l'orthographe retenue à la vérification (4.4, ligne 11). **Rien d'autre** : ni `temperature`, ni `topP`, ni `topK` — le service les ignore, et son guide demande de les retirer (M, non opposable) —, ni `systemInstruction`, ni `tools`, ni `safetySettings`, ni `responseMimeType`, ni `includeThoughts`.
- `minimal` est rejeté par Neon ; `xhigh` est son niveau le plus haut (M, non opposable).

### 5.4 Sortie maximale : 32 768, ce qu'elle borne, et la règle choisie
- **32 768 jetons aux deux : décidé par Lazar** (section 1). Les sorties mesurées sur ces entrées à des efforts plus bas vont de 49 à 1 239 jetons, réflexion comprise (M, 6.2) : 32 768 vaut 26 fois la plus longue. Trop basse, la borne ferait finir une lecture « par sortie maximale atteinte », et huit sur huit ne pardonne pas une coupure.
- **Constat documentaire de ce qu'elle borne** (relevé `291341e2…`, non opposable, R7) :
  - **Mistral** : `max_tokens` est « The maximum number of tokens to generate in the completion. » Raisonnement compris ou non : **non écrit.**
  - **Google** : la borne couvre pensée et réponse (« including thought tokens » ; « caps combined thinking and output tokens for a response »), **mais ces phrases visent l'API Interactions** ; pour `generateContent`, l'appel de ce devis, aucune confirmation directe.
  - Donc : **non établi pour les deux appels de ce devis.** Probable chez Google, inconnu chez Mistral.
- **Mon choix, en deux parts, et pourquoi.**
  1. **La garde de sortie maximale ne vise que le motif de fin** : `length` ou `model_length` chez Mistral ; `MAX_TOKENS` ou `CONTINUATION` chez Google. **Une sortie facturée au-dessus de 32 768 n'arrête plus la file** : elle est comptée à son coût réel et rapportée. Pourquoi : le texte lit « fin par sortie maximale atteinte » sur le motif de fin que rend le service (3.4). Et si la borne ne tenait que la réponse, une lecture normale à longue réflexion passerait 32 768 jetons facturés : le brouillon 1 l'aurait coupée pour une raison de devis, non de modèle. Cette règle ne coupe aucune lecture que le service finit normalement, sous l'une et l'autre lecture de la borne — **sauf, chez Mistral, une lecture dont le contenu passe la borne en octets de 6.4**, que ce brouillon ajoute pour tenir la dépense, et qui est dite comme limite.
  2. **Une sonde de borne à chaque vérification de clé** (4.6), qui mesure ce que la documentation tait. Pourquoi : la règle 7 du texte veut que ce devis « constate et écrive avant tout envoi » ce que la borne tient ; et le plafond de Google en dépend (6.4, condition (c)). La part 1 seule laisserait le point indécidé : la consigne en fait un nœud de Lazar avant toute file. La sonde le décide pour quelques centimes ; si elle ne le décide pas, le nœud est porté avec sa recommandation.
- **La règle 7 du texte** (sortie maximale à la course) : sonde « comprise », elle se lit sur réponse et réflexion ensemble, soit la sortie facturée de 5.5. Autre issue : nœud de Lazar (4.6). Chez Mistral, la réponse seule n'est pas mesurable, faute de compte de réflexion à part (5.5) : la sortie facturée entière en est le seul majorant.
- La sortie maximale propre de Large 4 n'est pas indiquée sur sa fiche (M). Un refus de 32 768 se verrait à l'appel A (4.4, ligne 12). Chez Google, `outputTokenLimit` est lu avant tout appel payant (4.4, ligne 2).

### 5.5 Ce que comptent les compteurs, et le texte jugé (fixé ici, avant tout envoi)

| grandeur | Mistral (flux) | Google (sans flux) |
|---|---|---|
| jetons d'entrée | `usage.prompt_tokens` | `usageMetadata.promptTokenCount` |
| **jetons de sortie facturés** | **`usage.completion_tokens`** | **`usageMetadata.candidatesTokenCount` + `usageMetadata.thoughtsTokenCount`** (absent = 0) |
| contrôle | `usage.total_tokens` − `usage.prompt_tokens` ; s'il diffère, le rapport donne les deux, et le coût compte le plus grand | `totalTokenCount` − `promptTokenCount` ; même règle |
| réflexion, relevée à part | **non rendue à part** : le bloc d'usage de cet appel n'a aucun compte de raisonnement (M) | `thoughtsTokenCount` |
| réponse seule | non rendue à part | `candidatesTokenCount` |
| **octets de contenu reçus** (pour la borne de 6.4) | la somme, au fil du flux, des longueurs en octets UTF-8 de toutes les chaînes portées sous `choices[0].delta.content`, quel que soit le type du morceau, hors les valeurs des champs `type` ; le programme compte des longueurs, il ne lit rien | sans objet : rien n'est reçu avant la fin de la réponse |
| **morceaux de pensée** (pour la sonde de 4.6) | le nombre d'éléments des listes `delta.content` dont le `type` vaut `thinking` ; le nombre de morceaux de chaque type est rapporté | sans objet : `thoughtsTokenCount` |
| nom servi | champ `model` des événements du flux, lu comme en 4.3 | champ `modelVersion` |
| motif de fin | `choices[0].finish_reason`, la valeur non nulle du flux | `candidates[0].finishReason` ; sans candidat, `promptFeedback.blockReason` |
| fin normale | `stop` | `STOP` |
| **fin par sortie maximale atteinte** | `length`, `model_length` | `MAX_TOKENS`, `CONTINUATION` |
| **refus** | **tout autre motif**, `error` et `tool_calls` compris, absent compris | **tout autre motif**, `SAFETY`, `RECITATION`, `OTHER`, `MALFORMED_RESPONSE` compris, absent compris |
| **texte jugé par le programme de forme** | la concaténation, dans l'ordre du flux, des contenus de `choices[0].delta.content` : une chaîne est prise entière ; d'une liste de morceaux, **seuls les morceaux de `type` égal à `text`**, par leur champ `text` ; les morceaux de pensée et tout autre type sont écartés | la concaténation, dans l'ordre, du champ `text` des parts de `candidates[0].content.parts` qui ne portent pas `thought` à vrai ; `includeThoughts` n'est pas envoyé |

- **Sources** (non opposables, R7) : pour Mistral, le relevé `291341e2…` (réponse en liste de morceaux, pensée puis `TextChunk`) et son complément `14d73d52…` (schéma : les trois champs d'usage requis ; motifs de fin `stop`, `length`, `model_length`, `error`, `tool_calls` pour la réponse entière, et, en flux, les mêmes sans `model_length`). Pour Google, le relevé `291341e2…` (champs d'usage ; « there are no dedicated thought blocks » ; liste des motifs, dont `CONTINUATION`, « reached the per-request token limit, but generation is not yet complete »).
- **Ce que le schéma n'écrit pas, et son issue** : que le flux de Mistral rende `usage` et `model` ; que `completion_tokens` comprenne le raisonnement. Le premier point se constate à l'appel A : sans eux, la vérification n'est pas saine (4.3). Le second reste non écrit : le coût compté suit `completion_tokens` et son contrôle ; **si la console de Mistral facture plus que le compté après la vérification, Lazar le dit avant la file, et ce devis est repris.**
- **`CONTINUATION` est rangé avec la sortie maximale atteinte** : il dit une limite de jetons touchée. Rangé en refus, il ferait le même effet : la lecture ne tient pas. Seul le rapport change.
- **Dans une file, si un champ nommé ici manque dans une réponse de code 200**, l'envoi est « sans compteur lisible » : compté au pire cas, et la file s'arrête (aucun repli silencieux). La vérification de la clé a pour objet que cela n'arrive pas.
- La sortie facturée sert à la grandeur `C` et au point 7 de la règle du devis de l'essai de mesure, comme le veut le texte.
- « Tout autre motif vaut refus » est un classement d'avant lecture, du côté prudent : un motif inconnu ne peut pas passer pour une fin normale.

### 5.6 Mode de lecture, délais, reprise
- **Mistral : en flux.** La pensée y est émise au fil de l'eau (M : « delta.content changes shape during the response »). Un délai de silence sépare donc une connexion morte d'une longue réflexion. Sans flux, une réponse à la sortie maximale laisserait la connexion muette des dizaines de minutes, et sa tenue ne se verrait qu'en pleine file ; en flux, ce qui reste inconnu — la présence de `usage` et de `model` — se voit à la vérification. Le délai du serveur de Mistral : non trouvé.
- **Google : sans flux.** La forme de `generateContent` est la seule documentée ; que la pensée soit émise en flux : non trouvé. Si elle y était muette, un délai de silence ne servirait à rien. Google conseille un délai client d'« at least 15 minutes » et prévient que « Hard prompts can take several minutes » (M).
- **Délais par envoi** :

| | Mistral | Google |
|---|---|---|
| silence (aucun événement reçu) | **600 s** ; relais 590 | sans objet : égal au total |
| total | **2 700 s** (45 minutes) ; relais 2 690 | **2 700 s** ; relais 2 690 |

  Les relais sont réglés dix secondes en dessous, pour que la coupure vienne du relais, avec un code 502 explicite.
- **Ce que ces délais tiennent** : une réponse de 32 768 jetons tient dans 2 690 secondes si le service rend **12,2 jetons par seconde ou plus** (C). C'est trois fois le conseil de Google. Le débit réel des deux modèles à l'effort le plus haut n'est pas mesuré (S). **À dire à Lazar** : sous ce débit, ou si une connexion muette de Google est coupée en route deux fois sur un même appel, la file s'arrête et le modèle ne tient pas, pour une raison de délai et non de forme.
- **Reprise unique, sur une panne de transport seulement** : délai dépassé, connexion coupée, **tout code de 500 à 599**. Le second envoi est identique au premier. Les deux sont comptés. **Deux pannes sur un même appel arrêtent la file.** Aucune autre règle de délai : « trois délais de suite » est retiré.
- **Code 429 de l'amont** : le programme attend ce que dit l'en-tête `Retry-After`, **borné à 600 secondes** (30 sans en-tête ; au-delà de 600, il attend 600), puis consomme la reprise unique. Un second 429 sur le même appel arrête la file. La contre-lecture juge ce choix acceptable ; il est dit à la ligne de calcul.
- **Aucune redemande de forme.** La forme est relevée, non redemandée.
- **Cadence** : un appel à la fois ; dix secondes de pause après chaque réponse.
- **Délai global d'une file : le pire cas de ses envois, calculé par le programme sur sa configuration**, soit `appels × (2 × 2 700 + 600 + 10) + 600` secondes : par appel, deux envois au délai total, une attente de 600 secondes au plus sur un code 429, et la pause. File Mistral : **144 840 s** (40 h 14 min). File Neon : **48 680 s** (13 h 31 min). Vérification : `3 × 2 700 + 600` = 8 700 s ; ses appels n'ont ni reprise ni attente. Le brouillon 2 écrivait qu'une attente sur un code 429 « n'y ajoute rien » : c'était vrai d'un 429 rendu vite, non d'un 429 rendu après un long silence (contre-lecture, n-11). L'attente est donc comptée à chaque appel. **Ainsi calculé, le délai global ne coupe aucune file que les délais par envoi laissent vivre** ; il n'arrête qu'un programme bloqué.
- **Durée attendue (S)** : moins d'une heure par file.
- **Une file interrompue de notre côté** (machine, session, délai global) est rapportée telle quelle et n'est pas rejouée (règle 4). Elle n'a pas ses 24 ou ses huit réponses : elle ne satisfait pas la règle 1 ou 2, et c'est un nœud de Lazar (règle 5), cause nommée au rapport. Le programme et les relais sont donc lancés là où ils peuvent vivre le temps du délai global.

## 6. Coût

### 6.1 Tarifs comptés (USD par million de jetons ; réflexion comptée au prix de sortie)

| modèle | entrée | sortie | relevé le | source |
|---|---|---|---|---|
| Mistral Large 4, prix courant | 0,70 | 2,10 | 2026-11-20 et 2026-11-21 | recherche de la session principale (`f7090b5d…`) ; **confirmé** par le relevé `291341e2…` (fiche du modèle et page des prix) |
| **Mistral Large 4, point d'accès européen (compté)** | **0,77** | **2,31** | 2026-11-21 | « billed at 1.1× standard list pricing » (relevés `291341e2…` et `b959c4d0…`) |
| **`gemini-4-neon`, offre payante (compté)** | **3** | **15** | 2026-11-20 et 2026-11-21 | relevés `ac8bb15e…` et `291341e2…` : « Output tokens, including thinking tokens: $15.00 per 1M tokens » |

- **Tous ces tarifs sont des provenances par transcription, non opposables (R7)** : pages lues par un outil qui résume. Deux relevés les donnent égaux ; cela ne les rend pas opposables.
- **Chez Google, la pensée est facturée en sortie** : écrit (M). **Chez Mistral, non trouvé** : la page dit seulement « uses reasoning tokens » ; je le suppose (S), et 5.5 dit quoi faire si la console dit autre chose.
- Une question de la page générale de Mistral cite « Mistral Large » à 0,5 et 1,5 USD : c'est un autre modèle (M) ; ce prix n'est pas employé.
- **Dû avant la ligne de calcul** : les deux pages de prix versées et scellées, lues par celui qui scelle ; la ligne de calcul cite leurs empreintes. Si un prix lu dépasse le prix compté, ce devis est repris.
- Aucun prix selon l'heure n'est connu pour ces deux modèles.

### 6.2 Longueurs mesurées (M, reprises du brouillon 1, qui les a lues par programme sur les seuls compteurs des trois rapports techniques ; non rouvertes ici)

| entrées | octets de la consigne remplie | jetons d'entrée, compte de Claude | compte de Google (Carbon) | compte d'OpenAI |
|---|---|---|---|---|
| appariement, 18 | 3 092 à 4 468 | 1 092 à 1 565, moyenne 1 312, somme 23 625 | 720 à 1 038, moyenne 864 | 700 à 981 (six entrées) |
| couverture, 6 | 8 831 à 21 503 | 3 277 à 7 597, moyenne 5 265, somme 31 591 | 2 125 à 4 834, moyenne 3 369 | 3 086 et 4 783 (deux entrées) |
| les huit de la file du juge | appariement 3 092 à 4 381 ; couverture 13 350 et 21 503 | — | appariement, somme 5 159 ; couverture, somme 7 933 | — |

- Le compte dépend du découpage de chaque fournisseur : de 0,22 à 0,38 jeton par octet. **Le découpage de Mistral n'est pas mesuré** : l'attendu prend le compte de Claude, le plus haut ; le pire cas prend un jeton par octet.
- Sorties mesurées sur ces entrées, réflexion comprise : de 49 à 403 jetons pour Carbon et GPT ; jusqu'à 660 (appariement) et 1 239 (couverture) pour Claude Haiku 5.5. Aucune à l'effort le plus haut.

### 6.3 Formule, attendu et pire cas (USD)
`coût = k × [ n_a × (e_a × pe + s_a × ps) + n_c × (e_c × pe + s_c × ps) ] ÷ 1 000 000`, comme au devis de l'essai de mesure.
- **Attendu** (`k` = 1) : entrées mesurées (6.2) ; sorties supposées (S, sans mesure à cet effort) : 2 000 jetons à l'appariement, 4 000 à la couverture.
- **Pire cas** (`k` = 2) : entrée à un jeton par octet du corps, bornée ici à 5 000 (appariement) et 24 000 (couverture) octets (S ; le programme calcule sur le corps réel) ; sortie maximale servie pleine, 32 768.

| ligne | appels | envois au plus | attendu | pire cas d'un envoi, sortie à 32 768 | pire cas, tous envois, sortie à 32 768 | réserve du compteur par envoi (6.4) | **plafond demandé** | excès possible d'un seul envoi (6.4) | pour information, trois envois |
|---|---|---|---|---|---|---|---|---|---|
| **file Mistral** (0,77 et 2,31) | 24 | 48 | **0,18** | 0,080 ; 0,094 | 3,99 | 0,610 ; 0,625 | **4,75** | 0,64 | 5,99 |
| **file Neon** (3 et 15) | 8 | 16 | **0,34** | 0,507 ; 0,564 | 8,33 | 0,507 ; 0,564 | **8,50** | 7,58 | 12,50 |
| vérification, Mistral, point d'accès européen | 3 au plus | 3 | ≈ 0,01 | 0,076 | 0,23 | 0,076 | **0,25** | 1,17 | — |
| vérification, Mistral, point d'accès global, **si repli** | 3 au plus | 3 | ≈ 0,01 | 0,076 | 0,23 | 0,076 | **0,25** | 1,17 | — |
| vérification, Google | 3 au plus | 3 | ≈ 0,02 | 0,492 | 1,48 | 0,492 | **1,50** | 7,58 | — |
| **total** | 32, et 9 de vérification au plus | 73 | **≈ 0,55** | | 14,26 | | **15,25** | 18,14 | |

(C sur S pour l'attendu ; C pour le reste. Le pire cas et la réserve d'un envoi sont donnés pour l'appariement, puis pour la couverture. Les colonnes « attendu », « pire cas » et « trois envois » sont celles du brouillon 2, que sa contre-lecture a refaites par programme : « tout est juste ». Les colonnes « réserve », « plafond » et « excès » sont recalculées ici, par un programme du bloc-notes de la session ; elles restent à refaire par le vérificateur. La sonde est l'un des trois appels d'une vérification.)

**Ce qui change, et pourquoi** : le plafond de la file Mistral passe de 4,25 à 4,75 USD, parce que le compteur réserve désormais, avant chaque envoi, la borne dure de cet envoi (6.4). Les quatre autres plafonds ne changent pas. La somme passe de 14,75 à **15,25 USD** (15,00 sans le repli). L'excès est en sus : au plus un envoi par ligne.

Si les modèles rendent cinq fois la sortie supposée : file Mistral ≈ 0,74 ; file Neon ≈ 1,54.

### 6.4 Plafonds : ce qui les tient, ce qu'ils bornent, et l'excès possible

**Le défaut du brouillon 2** (contre-lecture, correction 2). Ses lignes disaient « plafond tenu par compteur avant l'envoi », sans réserve. Or le compteur comptait le pire cas d'un envoi à 32 768 jetons de sortie : ce n'est un majorant que si la sortie maximale borne aussi la réflexion (condition (c)). Rien ne l'établit avant la sonde ; les appels A et A′ et la sonde elle-même partent avant elle. Et le relais de Google n'a pas de plafond en dollars.

**Les deux voies, et mon choix : les deux, chacune là où elle peut tenir.**
- **Voie (a), borne dure en dollars par envoi, tenue par le programme : chez Mistral.** Mistral est lu en flux : le programme voit la sortie arriver. Il peut la compter et couper l'envoi.
- **Voie (b), excès chiffré à un débit déclaré, écrit aux lignes et au nœud, couvert par le crédit : chez Google**, et, chez Mistral, pour ce que la voie (a) ne tient pas.
- **Pourquoi pas la voie (a) partout** : Google est lu sans flux (5.6). Rien n'arrive avant la fin de la réponse ; le programme n'a donc rien à compter pendant l'envoi. Il ne peut couper que sur le temps, et un temps n'est pas une somme sans un débit. Lire Google en flux demanderait d'établir que la pensée y est émise ou comptée au fil de l'eau : « non trouvé » au relevé. Je ne refais pas ce choix, que la contre-lecture a jugé acceptable ; je le signale (13, point 23).
- **Pourquoi pas la voie (b) seule** : chez Mistral, ce que borne `max_tokens` est « inconnu » (5.4). L'excès y serait le cas à craindre, non un cas rare. La borne en octets le ramène à deux suppositions, dont l'une se vérifie avant la file.

**Le compteur, avant l'envoi.** Le programme tient un compteur par file et par vérification. Il refuse l'envoi si le cumul compté plus **la réserve de cet envoi** dépasse le plafond. La réserve : l'entrée à un jeton par octet du corps réel, plus une sortie de réserve, aux prix comptés.

| envoi | sortie de réserve | réserve (USD) |
|---|---|---|
| Mistral, file | 262 208 jetons : la borne de 262 144 octets, plus 64 | 0,610 (appariement) ; 0,625 (couverture) |
| Mistral, vérification (appels A, A′ et B) | 32 832 jetons : la borne de 32 768 octets, plus 64 | 0,076 |
| Google, file | 32 768 jetons, la sortie maximale envoyée | 0,507 ; 0,564 |
| Google, vérification | 32 768 jetons | 0,492 |

- **Ce que compte un envoi fini** : son coût réel, sur les compteurs de 5.5, la plus grande des deux lectures.
- **Un envoi sans compteur lisible, en erreur ou en panne** : chez Google, 32 768 jetons de sortie. Chez Mistral, la plus grande de 32 768 et des octets de contenu reçus plus 64. Exception : le refus du mandataire à la signature de 4.4 est compté zéro.
- **Un envoi coupé à sa borne en octets** : compté à sa réserve entière.

**Voie (a) : la borne dure par envoi, chez Mistral.**
- **Ce que fait le programme** : il compte, au fil du flux, les octets de contenu reçus (5.5). Dès que ce compte passe la borne de l'envoi, il ferme la connexion ; le relais ferme alors la connexion vers l'amont. Bornes : **262 144 octets** pour un envoi de la file ; **32 768 octets** pour un envoi de vérification.
- **Pourquoi des octets** : le flux ne rend les jetons qu'à la fin. Un jeton rend au moins un octet (S) : les jetons de sortie valent donc au plus les octets de contenu, plus quelques jetons de contrôle, comptés 64. Un envoi de la file coûte ainsi au plus 0,610 ou 0,625 USD ; un envoi de vérification, 0,076.
- **Pourquoi 262 144** : c'est huit octets par jeton sur 32 768 jetons. Un texte courant rend trois à cinq octets par jeton (S). La borne ne coupe donc pas une réponse que le service tient sous 32 768 jetons, sauf un découpage à plus de huit octets par jeton en moyenne.
- **Pourquoi 32 768 à la vérification** : les messages y sont fixes et courts. La réserve reste celle du brouillon 2 ; le plafond de 0,25 USD laisse passer trois envois (0,228) et refuse le quatrième (0,304). Une vérification coupée n'est pas un « ne tient pas » (4.1).
- **Deux suppositions, écrites** :
  1. **tout jeton facturé en sortie est émis dans le flux.** Vérifié avant la file par le constat du majorant par octets (4.3), sur des réponses courtes seulement. « Démenti » : nœud de Lazar.
  2. **la fermeture de la connexion arrête la facturation.** Non documenté ; aucun programme ne peut le vérifier. Après tout envoi coupé, **Lazar lit la console** avant toute autre ligne chez ce fournisseur.
- **Si les deux tiennent, le plafond d'une ligne de Mistral est une borne dure en dollars** : avant chaque envoi, le cumul plus la borne de l'envoi est sous le plafond, et l'envoi ne peut pas coûter plus que sa borne.

**Un envoi coupé à sa borne, et le critère.**
- Dans la file : il a pris toute la part du plafond que le compteur lui avait réservée. **La file s'arrête là, sans reprise** : une coupure à la borne n'est pas une panne de transport. **C'est une file arrêtée à son plafond : elle ne tient pas** (règle 1) **et ne se rejoue pas** (règle 4). Le rapport nomme la cause : « envoi coupé à sa borne en octets ».
- De même, une file dont le compteur refuse un envoi est arrêtée à son plafond, comme au brouillon 2.
- À la vérification : appel A ou A′ coupé, nœud de Lazar, ni repli ni appel de plus (4.4, ligne 13) ; sonde coupée, « non comprise » (4.6).
- **Les critères ne changent pas** : 22 sur 24, huit sur huit, un seul nom servi. Ce brouillon n'ajoute aucune issue : il écrit une seconde façon, chez Mistral, d'atteindre « arrêtée à son plafond », que les règles 1 et 2 nomment déjà.

**La borne peut-elle faire échouer un modèle qui tiendrait autrement ? Oui, dans trois cas : ce sont des limites, dites à Lazar.**
1. **Mistral, réflexion hors de la sortie maximale** : une lecture que le service finirait normalement, mais dont pensée et réponse passent ensemble 262 144 octets, est coupée. Au brouillon 2, elle allait au bout si elle tenait en 45 minutes. C'est le prix de la borne dure. 262 144 octets valent environ 65 000 jetons à quatre octets par jeton, et au moins 32 768 jetons quel que soit le découpage ; la plus longue sortie mesurée sur ces entrées est de 1 239 jetons (6.2). La sonde dit avant la file si l'on est dans ce cas ; le nœud de 4.6 le porte.
2. **Mistral, réflexion comprise dans la sortie maximale** : une réponse de moins de 32 768 jetons, mais de plus de 262 144 octets, est coupée. Il y faut plus de huit octets par jeton en moyenne : peu probable (S), non exclu.
3. **Le compteur, aux deux files** : il refuse un envoi quand le cumul compté passe le plafond moins la réserve, soit 4,12 USD chez Mistral et 7,93 USD chez Neon (envoi de couverture). **Garantie, calculée** : un modèle dont chaque envoi est compté au plus à 32 768 jetons de sortie n'est jamais refusé. Son cumul avant le dernier envoi est d'au plus 3,91 USD chez Mistral ; avec la réserve de ce dernier envoi, 4,53, sous 4,75. Chez Neon, 8,33 au plus, sous 8,50. C'est pour garder cette garantie que le plafond de Mistral monte de 4,25 à 4,75. **Hors de cette garantie** : des sorties facturées au-delà de 32 768 jetons, ou, chez Mistral, des envois en panne après plus de 32 704 octets reçus, peuvent amener le cumul au seuil ; la file est alors arrêtée à son plafond et ne tient pas. Le brouillon 2 le disait déjà du cas où la condition (c) manque.

**Voie (b) : l'excès, chiffré.**
- **Débit déclaré : 200 jetons par seconde (S).** Aucune mesure. C'est le plus haut des débits que la contre-lecture a chiffrés. En 2 690 secondes, délai du relais, un envoi rendrait 538 000 jetons : **1,24 USD chez Mistral, 8,07 USD chez Neon**, au prix de sortie compté.
- **L'excès d'un envoi** : ce coût, moins la sortie de réserve que le compteur a déjà comptée.

| ligne | plafond | excès possible d'un seul envoi, à 200 jetons par seconde | à 100 | à 400 | quand il joue |
|---|---|---|---|---|---|
| vérification, Mistral (lignes 1 et 5) | 0,25 | **1,17** | 0,55 | 2,41 | si l'une des deux suppositions de la borne en octets manque |
| file Mistral (ligne 3) | 4,75 | **0,64** | 0,02 | 1,88 | de même |
| vérification, Google (ligne 2) | 1,50 | **7,58** | 3,55 | 15,65 | si la sortie maximale ne borne pas la réflexion |
| file Neon (ligne 4) | 8,50 | **7,58** | 3,55 | 15,65 | de même |

- **Un seul excès par ligne, et pourquoi.** Avant chaque envoi, le cumul plus la réserve est sous le plafond. Un envoi coûte au plus sa réserve plus l'excès. Après lui, le cumul est donc sous le plafond plus l'excès ; et aucun envoi ne part ensuite sans repasser le même contrôle. La dépense d'une ligne est ainsi bornée par **son plafond plus l'excès d'un seul envoi**. Chez Google, le programme voit le coût réel à la fin de chaque envoi (`thoughtsTokenCount` est rendu). Chez Mistral, il le voit par `usage` ; un envoi coupé, dont il ne voit pas le coût, arrête la ligne.
- **Quand il joue.** Chez Google : si la réflexion ne compte pas dans la sortie maximale. C'est ce que mesure la sonde ; mais l'appel A, l'appel A′ et la sonde partent avant toute mesure. Une réflexion de plus de 32 768 jetons sur « réponds OK » ou sur un produit est peu probable ; elle n'est pas bornée. Sonde « comprise » : l'excès de la file Neon est écarté, sous la supposition que la borne se comporte à 32 768 comme à 256. Chez Mistral : si l'une des deux suppositions de la voie (a) manque.
- **Ce qui est fait de l'excès** : il est **écrit à chaque ligne de calcul** (section 11), pour que Lazar l'accepte en connaissance de cause ; **écrit au nœud de la sonde** (4.6) ; **couvert par le crédit chargé** (6.5), pour qu'un excès ne coupe pas la file par un compte à court.
- **Au-delà du débit déclaré**, l'excès croît avec le débit : le double à 400 jetons par seconde. La seule borne dure est alors, chez un compte prépayé, le crédit chargé : le service refuse quand il est épuisé (code 402), et la file ne tient pas. Chez un compte payé après usage, il n'y a aucune borne dure : seulement le délai.

**Les trois conditions du brouillon 2, relues.** Ce sont des conditions, à ne pas confondre avec les voies (a) et (b) ci-dessus. Le plafond tient si : condition (a), les prix comptés sont au moins égaux aux prix facturés — non opposable tant que les pages ne sont pas scellées (6.1) ; condition (b), la réserve est calculée sur le corps réel ; condition (c), chez Google, la sortie maximale est respectée par le service, réflexion comprise — établie seulement si la sonde dit « comprise » (4.6) ; chez Mistral, les deux suppositions de la voie (a) tiennent. Si la condition (c) manque, la dépense de la ligne peut passer son plafond de l'excès d'un envoi, chiffré ci-dessus.

- **Ce n'est pas la seule cause d'échec qui ne soit pas le modèle.** La phrase du brouillon 1, « ce sont les réglages qui décident, non la caisse », est nuancée : un compte à court (code 402), un code 429 répété, deux pannes ou deux délais sur un même appel arrêtent aussi une file partie. La vérification de la clé, le crédit de 6.5, les limites de débit du constat (section 9) et les délais de 5.6 sont là pour les écarter ; ils ne les suppriment pas.
- Seconde barrière : chaque relais est borné en nombre d'appels au modèle (file Mistral 48, file Neon 16, vérification 3). **Un relais est lancé par ligne de calcul**, avec la borne d'appels de cette ligne, et, pour celui de Mistral, le plafond en dollars de cette ligne ; il est arrêté par son identifiant de processus à la clôture de la ligne. **Le relais de Google n'a pas de plafond en dollars** : le sien est tenu par le programme qui conduit l'essai, entre les envois seulement ; pendant un envoi, rien ne le tient que le délai. C'est l'excès des lignes 2 et 4.

### 6.5 Montant à charger chez chaque fournisseur, en crédit utilisable

| fournisseur | somme des plafonds | excès possibles, un par ligne (6.4) | à couvrir | avec la marge de 15 %, arrondi au demi-dollar supérieur : **crédit utilisable à avoir** | paiement si une taxe de 20 % s'ajoute (S) | attendu |
|---|---|---|---|---|---|---|
| **Mistral** | 4,75 + 0,25 + 0,25 = 5,25 | 0,64 + 1,17 + 1,17 = 2,98 | 8,23 | 9,46, soit **9,50 USD** | **11,40 USD** | ≈ 0,20 |
| **Google** | 8,50 + 1,50 = 10,00 | 7,58 + 7,58 = 15,16 | 25,16 | 28,93, soit **29,00 USD** | **34,80 USD** | ≈ 0,36 |

- **Ces montants changent** : le brouillon 2 demandait 5,50 et 11,50 USD de crédit utilisable (6,60 et 13,80 avec la taxe). L'écart vient de l'excès, que le brouillon 2 ne couvrait pas, et, pour 0,50 USD, du plafond de la file Mistral.
- **Crédit utilisable** : ce que la console affiche comme dépensable en appels, net de toute taxe et de toute conversion de monnaie.
- **La règle** : **avant toute file, le crédit utilisable couvre la somme des plafonds et des excès possibles des lignes du fournisseur** — 8,23 USD chez Mistral, ligne de repli comprise ; 25,16 USD chez Google. Sinon la file ne part pas. Lazar donne le crédit vu, avec sa page et son heure, au constat (section 9) ; la garde 9 le lit.
- **Pourquoi couvrir l'excès** : un excès non couvert viderait le compte en pleine file ; le service répondrait par un code 402, et le modèle ne tiendrait pas, pour une raison de caisse.
- **Ce que le crédit ne permet pas** : la marge et l'excès ne sont pas des dépenses visées. La dépense visée d'une ligne reste son plafond ; l'excès est ce que Lazar accepte de voir dépassé, une fois par ligne, si le service ne borne pas la réflexion. Un crédit plus haut élève aussi la perte la plus grande possible : chez un compte prépayé, elle est égale au crédit chargé.
- **La marge de 15 %** couvre un écart entre prix comptés et prix facturés.
- **La taxe** : recharge minimale et taxes ne sont trouvées chez aucun des deux (M). Le taux de 20 % est une supposition, celle d'une taxe sur la valeur ajoutée française. Si la taxe est prise sur la recharge, payer 9,50 ne donnerait que 7,92 de crédit, sous les 8,23 à couvrir : d'où le paiement de 11,40. Si la console affiche un autre taux, le paiement est le crédit utilisable multiplié par un plus ce taux.
- **Si une recharge minimale dépasse ces montants**, Lazar charge le minimum ; le surplus n'est pas une dépense permise.
- **Si le compte de Google se paie après usage** : pas de crédit à charger ; Lazar constate que la facturation est active et qu'aucun budget du projet ne coupe sous 25,16 USD ; il peut poser une alerte à 29,00 USD. **Une alerte n'arrête rien** : sur un tel compte, aucune borne dure ne tient l'excès (6.4).
- **« Compte chargé au plus juste » n'est pas une barrière** : un compte à court coupe une file partie, et le modèle ne tient pas. Les barrières sont le compteur, la borne en octets chez Mistral et la borne d'appels du relais.
- Charger est un geste de Lazar. Ce n'est pas une ligne de calcul ; il lui est présenté avec les lignes (section 11).

### 6.6 Lignes proposées (forme de `registres/depenses.md`), une par ligne de calcul
- Engagement : `| AAAA-MM-JJ | GO-… | Organismes discrets, bras A, essai d'admission du second lecteur sur textes synthétiques, **file Mistral : engagement** — 24 appels au plus (48 envois), plafond 4,75 USD tenu par compteur et par une borne dure de 262 144 octets par envoi, excès possible d'un envoi 0,64 USD à 200 jetons par seconde si l'une des deux suppositions de la borne manque, compté à 0,77 et 2,31 ; point d'accès [européen ou global], celui du relevé de vérification ; relais lancé (identifiant de processus, port) | session ; R-… |` ; même forme pour la file Neon (8 appels, 16 envois, plafond 8,50 USD tenu par compteur si la sortie maximale borne la réflexion, sinon excès possible d'un envoi 7,58 USD à 200 jetons par seconde, compté à 3 et 15) et pour chaque vérification (trois appels au plus, soit trois envois, sonde de borne comprise, son plafond et son excès de la section 11).
- Clôture : `| AAAA-MM-JJ | GO-… | même objet, **close** : N appels servis, R refus, **X USD relevés**, excès au-delà du plafond dit s'il y en a un ; relais arrêté par identifiant de processus ; dossier scellé `runs/…` (manifeste `…`), commit `…` | session ; R-… |`.

## 7. Les critères, écrits d'avance, recopiés du texte à la lettre

Texte, **brouillon 43** (`4f91b535ad91…`), section 3.4. Les huit règles sont recopiées ci-dessous **à la lettre, dans leur numérotation, règle 6 comprise**, par programme (lignes 521 à 529 du fichier). Ce devis n'y ajoute ni seuil ni issue. **Le fichier des règles que lit le programme est la copie de ces huit règles**, non un résumé (règle 8).

  - **Règles d'admission, fermées, écrites ici avant toute lecture des deux essais.**
    1. **Mistral Large 4 tient** si ses 24 lectures rendent 24 réponses de code 200, reprise unique comprise, sans refus, sans fin par sortie maximale atteinte, avec au moins 22 réponses de forme conforme : c'est le critère du devis de l'essai de mesure, section 7.2, inchangé. Une file arrêtée à son plafond ne tient pas (même section).
    2. **`gemini-4-neon` tient** si ses huit lectures rendent huit réponses de code 200, reprise unique comprise, sans refus, sans fin par sortie maximale atteinte, **toutes les huit de forme conforme**. Une file arrêtée à son plafond ne tient pas. « Huit sur huit » est un **seuil choisi d'avance, non étalonné** : c'est le plus petit compte sur huit qui tienne la proportion de 22 sur 24. **C'est un mot de Lazar** (« b a b go », choix 1 (b) : admis si les huit sur huit sont de forme conforme, sinon nœud de Lazar) ; il a écarté un essai sans règle d'admission, et les 24 entrées à 22 sur 24. **Ce qui retient la file du juge** (vérification du brouillon 41, m-2) : son seuil est fixé, et plus aucun mot de Lazar ne lui manque ; elle ne part que sous ses conditions d'envoi constatées, son devis contre-lu, sa ligne de calcul et sa clé vérifiée, dans l'ordre de la section 13.
    3. **Pour les deux**, tenir exige de plus que toutes les réponses de la file portent le nom servi que la vérification de la clé a relevé. **Ne tient pas non plus** une file coupée par le service après son premier envoi.
    4. **Une file n'est jouée qu'une fois.** Une file est partie dès son premier envoi ; elle ne repart pas, et la session n'en rejoue aucune. Avant ce premier envoi, rien n'est « ne tient pas » : c'est la vérification de la clé, ci-dessus.
    5. **Si Mistral Large 4 tient**, il est le second lecteur. **Si `gemini-4-neon` tient**, il juge les deux ancres. **Si l'un ne tient pas, son rôle n'est pas pourvu : nœud de Lazar**, tableau des mesures à l'appui ; l'autre rôle n'en dépend pas.
    6. Ni `gemini-4-carbon`, ni `gpt-6.2-astra`, ni un modèle de DeepSeek, ni aucun autre modèle ne prend un rôle sans un mot de Lazar ; ce texte n'est pas scellé tant que les deux rôles ne sont pas pourvus.
    7. **Sortie maximale** du second lecteur et du juge des deux ancres à la course : la règle du devis de l'essai de mesure, section 7.3, point 7 — la plus grande de 8 192 et de quatre fois le maximum observé de la sortie à son essai d'admission, arrondie aux 1 024 supérieurs. Elle porte sur ce que la sortie maximale du service borne — réponse et réflexion ensemble, ou réponse seule —, ce que le devis des essais constate et écrit avant tout envoi.
    8. **Les règles sont appliquées par programme, sur les seuls compteurs du rapport.** Elles sont scellées avec ce brouillon. Le fichier de règle que lit le programme en est la copie ; il est scellé avant le premier envoi et cite l'empreinte du brouillon en vigueur. Un brouillon suivant ne peut les changer qu'avant le premier envoi ; après, tout changement est un écart, porté à Lazar. **Après le premier envoi d'une file, la session n'y a aucune liberté** : cette phrase, retirée au brouillon 41 sans que ce soit dit, est remise (vérification du brouillon 41, m-1) ; la correction C-2 du brouillon 40 ne visait que la formule « sans choix de la session », à la ligne des réglages.

**En bref, et sans rien y changer** : Mistral tient à **22 de forme conforme sur 24** ; Neon à **huit sur huit** ; pour les deux, **un seul nom servi** sur toute la file, celui de la vérification de la clé.

**Ce que ce devis fixe pour les lire** : « refus » et « fin par sortie maximale atteinte » se lisent sur les motifs de 5.5 ; « code 200, reprise unique comprise » se lit sur le dernier envoi de chaque appel ; une lecture reprise compte par son dernier envoi pour la sortie, par ses deux envois pour le coût ; « de forme conforme » se juge sur le texte jugé de 5.5 ; la règle 7 se lit comme le dit 5.4 ; « une file arrêtée à son plafond » se lit comme le dit 6.4 : le compteur a refusé un envoi, ou, chez Mistral, un envoi a été coupé à sa borne en octets.

**Mesuré et rapporté, sans verdict** :
- **réponses étayées** de chaque file : de forme conforme, et chaque extrait que la forme exige est retrouvé à la lettre dans l'entrée, par les programmes de vérification des extraits de l'instrument. Ce compte n'entre dans aucune règle ;
- **coût projeté** : pour Mistral, la grandeur `C` du devis de l'essai de mesure (13 888 lectures de l'appariement et 1 248 de la couverture, redemandes au taux de non-conformité mesuré), aux tarifs de 6.1 et au point d'accès retenu ; pour Neon, le coût moyen d'un appel par instrument, que le devis de la course portera aux 152 appels au plus du juge ;
- sorties moyennes par longueur et maximum, comme à l'essai de mesure ; durée de chaque envoi, pour régler les délais de la course ;
- l'issue de la sonde de borne (4.6) ;
- pour Mistral, par envoi : les octets de contenu reçus, le nombre de morceaux par type, et le constat du majorant par octets (4.3) ; une sortie facturée au-dessus des octets reçus plus 64 est comptée à son coût réel et rapportée, sans arrêter la file.

**Ce que les essais ne décident pas** : la justesse des verdicts, l'étayage, l'accord entre lecteurs. Rien de ce qu'ils mesurent n'entre dans une variable, un seuil ou un verdict du texte. Ils ne donnent aucune raison de changer une consigne.

## 8. Ce qui est rapporté, ce qui est gardé, et qui lit

- **Rapporté, par envoi, des champs techniques seulement** : identifiant de l'entrée, modèle demandé, point d'accès, rang de l'envoi (1 ou 2) ; code de retour, ou « délai », « coupure », et son origine, mandataire, relais ou amont (4.4) ; motif de fin ; jetons d'entrée, de sortie facturée, de réflexion et de réponse seule quand ils sont rendus à part (5.5) ; durée ; coût ; nom servi ; conformité de forme, oui ou non, **jugée par programme à la forme du texte en vigueur quand l'essai part** (3.2 et 3.3, tolérance comprise), avec un code de cause sans texte ; étayée, oui ou non ; sortie facturée au-delà de la sortie maximale envoyée, oui ou non ; pour Mistral, octets de contenu reçus, nombre de morceaux par type, envoi coupé à sa borne en octets, oui ou non. Le rapport nomme, par son empreinte, le brouillon en vigueur.
- **Jamais le texte des réponses.** Ni le verdict rendu, ni l'accord avec la construction des entrées. Un programme vérifie que le rapport ne contient aucun morceau de réponse (garde 18).
- **Gardé** (règle « récupérer ce qui est récupérable », texte, 8.5) : dans `runs/essais-admission-bras-a-v1/<horodatage>-file-<nom>/`, scellé, committé et poussé avant toute suppression : configuration, manifeste (versions, commit, empreintes des deux consignes, du fichier des règles, du constat des conditions d'envoi, du relevé de la vérification de la clé) ; le corps exact de chaque envoi ; chaque réponse entière, telle que reçue du relais, erreurs et flux partiels compris, dans `reponses-brutes-non-lues/` ; journaux et état final du relais ; sorties des programmes de forme et d'extraits ; inventaire ; rapport.
- Chaque envoi écrit sa ligne au journal, vidée sur le disque, avant de partir ; chaque réponse est écrite avant d'être analysée. Une file interrompue est rapportée telle quelle ; elle n'est pas rejouée.
- **Qui lit les réponses : des programmes nommés, et eux seuls** — extraction du texte jugé, conformité de forme, vérification des extraits, lecture des compteurs, contrôle « aucun morceau de réponse dans le rapport ». **Aucun agent ni aucune personne.**
- Le rapport est relu par un agent qui n'a écrit ni le code ni ce devis.
- Les relais s'arrêtent par leur identifiant de processus (R10).

## 9. Conditions d'envoi des textes : constatées, datées et inscrites avant le premier envoi

Mot de Lazar « b a b go », choix 3 (b). Elles valent **avant la vérification de la clé** aussi (texte, 3.4).

| fournisseur | condition à constater | clé du tableau du constat | valeur admise, par programme |
|---|---|---|---|
| **Google** | le projet de la clé a un compte de facturation actif (offre payante) | `google_offre_payante` | `oui` |
| | partage des journaux (« datasets ») | `google_partage_journaux` | `désactivé` |
| | durée des journaux du projet | `google_duree_journaux_jours` | l'entier `7` |
| **Mistral** | offre payante | `mistral_offre_payante` | `oui` |
| | « Data usage for improving our services » (refus de l'entraînement activé) | `mistral_donnees_pour_amelioration` | `désactivé` |
| | point d'accès | aucune : constaté à la vérification de la clé (4.5), non ici | — |
| **les deux** | la clé lue sous `GEMINI_API_KEY` est celle du projet constaté | `google_cle_du_projet_constate` | `oui` |
| | la clé lue sous `MISTRAL_API_KEY` est celle de l'espace constaté | `mistral_cle_de_l_espace_constate` | `oui` |
| | crédit utilisable vu à la console de Mistral (6.5) | `mistral_credit_utilisable_usd` | un nombre, au moins 8,23 |
| | crédit utilisable vu à la console de Google (6.5) | `google_credit_utilisable_usd` | un nombre, au moins 25,16 ; ou la chaîne `après usage` |
| | Google, compte payé après usage seulement : le plus bas budget du projet qui coupe | `google_budget_minimal_usd` | exigée si le crédit vaut `après usage` : la chaîne `aucun`, ou un nombre, au moins 25,16 |
| **Mistral** | limites de débit du compte : requêtes | `mistral_limite_requetes_par_minute` | un nombre, au moins 6 (une requête par dix secondes) ; sinon ce devis est repris |
| | limites de débit du compte : jetons | `mistral_limite_jetons_par_minute` | un nombre, au moins 100 000 ; sinon ce devis est repris |

**Cette liste de clés et ces valeurs admises sont écrites à la configuration** ; le programme refuse un tableau où une clé manque, où une clé de plus figure, ou dont une valeur n'est pas admise (garde 9).

- **Qui règle** : Lazar, sur les deux consoles. La session n'y a pas accès.
- **Qui constate, et comment** : Lazar, sur l'écran de chaque console, après le réglage. Il donne à la session, pour chaque ligne : la valeur vue, la page de la console où il l'a vue, la date et l'heure. Aucune interface de programme connue ne rend ces réglages : le constat est une parole de Lazar, non une mesure.
- **La pièce versée** : `docs/notes/relance-organismes-discrets-v1/constat-conditions-envoi-google-mistral-bras-a-AAAA-MM-JJ-v1.md`, scellée. Elle porte le mot de Lazar à la lettre, puis **un tableau à clés fixes, une ligne par condition, aux clés du tableau ci-dessus** : clé, valeur vue, page, date et heure en temps universel, qui a vu ; et l'heure de la transcription. Ni courriel, ni identifiant de compte, ni capture d'écran dans le dépôt.
- **L'inscription que le texte exige** (3.4 : « inscrit à la case de 13.1, avant le premier envoi ») : **un brouillon du texte porte le constat à la case « lecteurs et juge des ancres » de 13.1, avant la première vérification de clé.** Après les vérifications, un brouillon porte les relevés et, pour Mistral, le point d'accès retenu, avant le premier envoi de la file. **Le fichier des règles cite l'empreinte du brouillon en vigueur au premier envoi de la file** ; s'il a été scellé sur un brouillon antérieur, il est refait sous un nom neuf (R12). Ces brouillons sont l'affaire du rédacteur du texte, non de ce devis.
- **Garde** : les vérifications de clé et les files exigent cette pièce, **et la lisent** (garde 9).
- **Réserve « Labs » et « Preview »** (brouillon 43 ; relevé `b959c4d0…`, non opposable) : chez Mistral, l'exclusion de l'entraînement sur l'offre payante ne couvre ni les retours envoyés, ni les modèles « Labs », ni les modèles en aperçu (« Preview »). `mistral-large-4-0` est donné en disponibilité générale (« GA ») par le relevé de son identifiant (`b8163cc9…`, non opposable) : la réserve est sans effet ici, si ce relevé dit vrai. Aucun retour n'est envoyé. Ce sont les réglages constatés qui font la condition.
- **Ce que ces conditions ne donnent pas** (M, non opposable) : aucune durée de conservation trouvée ; aucune non-conservation demandée ; aucun choix de région chez Google ; le service du modèle sur le point d'accès européen non vérifié avant 4.5.

## 10. Gardes — chacune éprouvée sur un cas sain et sur un artefact, contre un faux fournisseur local, sans appel payant (R5)

| garde | ce qu'elle fait | cas sain | artefact |
|---|---|---|---|
| **1. plafond avant l'envoi** | 6.4 ; par file et par vérification ; la réserve de l'envoi est celle de 6.4 : borne en octets chez Mistral, 32 768 jetons chez Google | cumul bas : l'envoi part, sur les deux formes d'appel ; file Mistral à 3,90 de cumul : l'envoi part (3,90 plus 0,625, sous 4,75) | cumul à 0,01 du plafond : refus, le faux fournisseur ne reçoit rien, arrêt, code de sortie non nul ; file Mistral à 4,20 de cumul : refus ; refus du mandataire à la signature de 4.4 : compté zéro ; panne sans cette signature : comptée à sa réserve |
| **2. délais** | 5.6 : silence (Mistral), total, délai global calculé | réponse en 2 secondes ; flux lent mais vivant, un événement toutes les 30 secondes : il va au bout | flux muet 600 secondes, ou réponse sans flux absente à 2 700 secondes (durées réduites à l'essai) : coupé, compté au pire cas, reprise unique ; seconde panne sur le même appel : arrêt ; **délai global** (durée réduite à l'essai) : un programme bloqué hors de tout envoi est coupé, la file est rapportée interrompue, code de sortie non nul ; à l'inverse, cas sain du délai global : un appel fait d'un envoi au délai total, d'un code 429, de 600 secondes d'attente et d'un second envoi au délai total n'est pas coupé |
| **3. champs du corps et motif de sortie maximale** | le corps porte la sortie maximale de sa ligne (32 768 ; 256 à la sonde) et les seuls champs de 5.2 ou 5.3 ; sinon refus avant l'envoi. **Un motif de fin par sortie maximale atteinte arrête la file.** Une sortie facturée au-delà de 32 768 sous une fin normale **n'arrête pas** : comptée, rapportée | corps conforme ; réponse à 40 000 jetons facturés, fin `stop` : la file continue, le rapport le dit | corps sans sortie maximale, à 65 536, avec un champ de plus, sans `stream` pour Mistral, avec la température pour Google : refus ; réponses de fin `length`, `model_length`, `MAX_TOKENS`, `CONTINUATION` : arrêt |
| **4. codes et motifs** | 401, 402, 403 : arrêt, sans reprise ; 429 : selon 5.6 ; 500 à 599 : reprise unique, puis arrêt ; 400, 422 et tout autre code : arrêt, code et origine au journal ; motif de refus : arrêt ; un troisième envoi d'un même appel est impossible | 200, fin normale | chacun de ces codes, 504 compris ; motif inconnu classé refus ; 429 puis 200 : la file continue ; 429 avec `Retry-After` de 900 : attente de 600, puis envoi ; 429 puis 429 : arrêt |
| **5. nom servi** | chaque réponse porte le nom servi du relevé de la vérification ; sinon arrêt de la file | nom égal | nom autre (`mistral-large-4`) : arrêt, motif au journal ; flux de Mistral dont un seul événement porte un autre nom : arrêt ; flux dont le dernier événement n'a pas de champ `model` : nom égal, la file continue |
| **6. rien de personnel dans ce qui part** | corps et en-têtes comparés à une liste locale d'interdits, jamais envoyée ni versée ; agent d'utilisateur générique ; lot relu par empreinte ; consigne remplie comparée à son empreinte | entrée synthétique | courriel, chemin du poste, identifiant de session glissés : refus |
| **7. clés par leur nom** | relais lancés par le lanceur du dépôt, clé exigée par son nom ; le programme des essais n'a aucune clé et ne parle qu'à la boucle locale ; journaux et pièces versées relus pour toute chaîne de la forme d'une clé | clé factice dans le seul relais | nom absent : rien ne part ; clé factice glissée dans un journal : trouvée, arrêt |
| **8. ligne de calcul** | chaque file et chaque vérification exige l'identifiant d'une ligne valide de `registres/go.md` qui la nomme, et l'empreinte du devis accepté | identifiant valide | absent, ou d'une ligne qui nomme l'autre file : rien ne part |
| **9. conditions d'envoi constatées, lues** | pièce du constat présente, d'empreinte égale à celle de la configuration et à son compagnon ; **son tableau est lu** : les clés de la section 9, toutes et elles seules, chacune à une valeur admise ; chaque date en temps universel, antérieure à l'envoi ; le mot de Lazar présent ; crédit utilisable au moins égal à la somme des plafonds et des excès du fournisseur (8,23 ; 25,16) | pièce conforme, crédit de Google en nombre ; pièce conforme, crédit de Google `après usage` et budget `aucun` | pièce absente ; d'une autre empreinte ; une clé manquante ; une clé de plus ; date postérieure ; mot de Lazar absent ; **puis un artefact par clé** : `google_offre_payante` à `non` ; `google_partage_journaux` à `activé` ; `google_duree_journaux_jours` à 55 ; `mistral_offre_payante` à `non` ; `mistral_donnees_pour_amelioration` à `activé` ; `google_cle_du_projet_constate` à `non` ; `mistral_cle_de_l_espace_constate` à `non` ; `mistral_credit_utilisable_usd` à 8,00 ; `google_credit_utilisable_usd` à 20,00 ; `après usage` sans `google_budget_minimal_usd` ; `après usage` avec un budget à 15,00 ; `mistral_limite_requetes_par_minute` à 3 ; `mistral_limite_jetons_par_minute` à 50 000 : ni vérification ni file |
| **10. clé vérifiée, point d'accès fixé** | la file exige le relevé scellé de sa vérification, sain, d'empreinte inscrite, sonde « comprise » et, chez Mistral, majorant par octets « établi » ; **sinon, le mot de Lazar, sous sa forme écrite** : une pièce scellée `docs/notes/relance-organismes-discrets-v1/mots-de-lazar-sonde-de-borne-<fournisseur>-bras-a-AAAA-MM-JJ-v1.md`, qui porte le mot à la lettre, l'issue de la sonde ou du majorant qu'il vise, et l'empreinte du relevé de vérification ; son empreinte est inscrite à la configuration de la file. La file Mistral n'emploie que le point d'accès du relevé ; les orthographes et le traitement de la température sont ceux du relevé | relevé sain, sonde « comprise » ; relevé sain, sonde « indécidée », pièce du mot conforme et inscrite : la file part | relevé absent, non sain, d'un autre point d'accès ; sonde « indécidée » ou « non comprise » sans pièce du mot ; majorant « démenti » sans pièce du mot ; pièce du mot d'une autre empreinte que celle de la configuration ; pièce qui cite un autre relevé : la file ne part pas |
| **11. signe de « ne sert pas ce modèle »** | 4.5, par programme | liste sans l'identifiant et code 400 `invalid_model` : signe constaté ; **liste sans l'identifiant et code 200 avec le bon nom : saine, point d'accès européen retenu, pas de signe** | code 401 ; code 200 avec un autre nom ; liste qui porte l'identifiant et code 400 `invalid_model` ; 404 au corps qui n'est pas celui de Mistral ; 422 qui nomme `max_tokens` ; liste en forme illisible ; refus du mandataire : pas de signe, pas de repli |
| **12. fichier des règles** | la file exige le fichier des règles : présent, scellé, d'empreinte égale à celle de la configuration, qui cite l'empreinte du brouillon en vigueur ; le programme des règles ne lit que le rapport, et refuse un fichier dont l'empreinte n'est pas celle du manifeste de la file | fichier conforme : la file part ; règles appliquées | fichier absent, ou qui cite un autre brouillon : **la file ne part pas** ; fichier changé après la file : **le programme des règles refuse** |
| **13. une file ne se rejoue pas** | un dossier de file déjà parti interdit un second départ de la même file | premier départ | second départ : refus |
| **14. identifiant figé et voie d'accès** | l'identifiant demandé est égal, à la lettre, à la constante du texte (`mistral-large-4-0` ; `gemini-4-neon`), dans la configuration, dans le corps et dans le chemin de l'appel à Google ; l'hôte amont du relais est l'un des trois permis (`api.eu.mistral.ai`, `api.mistral.ai`, `generativelanguage.googleapis.com`) et celui de sa ligne | identifiants et hôte conformes | `mistral-large-latest`, `mistral-large-4`, `gemini-4-neon-latest` ; un hôte autre ; l'hôte global sous la ligne européenne : rien ne part |
| **15. repli lié au signe** | la vérification par le point d'accès global exige le relevé scellé de la vérification européenne, **signe constaté**, d'empreinte inscrite | relevé européen au signe constaté | relevé absent ; relevé sans signe (401, autre nom servi, issue de la ligne 13) : la vérification globale ne part pas |
| **16. forme de la réponse à la vérification** | 4.3 et 4.4, par programme : champs exigés, nom servi, motif, texte extractible ; classement fermé ; sonde de 4.6 ; constat du majorant par octets | flux de Mistral complet, dont le dernier événement n'a pas de champ `model` : sain ; réponse de Google complète ; sonde de Mistral à 200 jetons facturés, fin `length`, un morceau de pensée vu : « comprise » ; sonde de Google à 256 facturés, `MAX_TOKENS`, `thoughtsTokenCount` à 180 : « comprise » | **forme** : réponse 200 sans `usage` dans le flux, sans `total_tokens`, sans `modelVersion`, au contenu sans morceau `text` : non saine. **Classement, une ligne chacun** : ligne 1, refus du mandataire à sa signature : non compté ; ligne 2, `outputTokenLimit` à 16 384 à l'appel de liste : aucun appel payant ; ligne 7, code 401 et liste qui porte l'identifiant : cause à corriger ; ligne 8, code 403 et liste lisible sans l'identifiant : nœud ; ligne 10, 400 qui nomme seulement `temperature` : appel A′ ; ligne 11, premier temps, 400 qui nomme seulement `thinkingLevel` à l'appel A envoyé avec `XHIGH` : appel A′ avec `xhigh` ; ligne 11, second temps, appel A′ sain : `xhigh` inscrite ; ligne 12, 400 qui nomme `max_tokens`, 400 qui nomme deux champs, 400 qui nomme `thinkingLevel` à l'appel A′ : rien d'autre n'est essayé ; ligne 13, 400 sans champ nommé, 404 hors du signe, corps illisible, code 418, appel A coupé à sa borne en octets : nœud. **Sonde** : à 900 jetons facturés : « non comprise » ; coupée à 32 768 octets : « non comprise » ; finie `stop` à 40 jetons : « indécidée » ; **à 256 jetons facturés, fin par sortie maximale atteinte, aucune réflexion constatée (`thoughtsTokenCount` à 0 ou absent ; aucun morceau `thinking`) : « indécidée »** ; à 256 facturés selon `completion_tokens` et 300 selon `total_tokens − prompt_tokens` : « non comprise ». **Majorant** : 300 jetons facturés pour 100 octets reçus : « démenti » |
| **17. les huit entrées de Neon** | la file Neon n'envoie que les huit identifiants de la section 3, dans cet ordre ; la file Mistral, les 24 du lot | les huit, dans l'ordre | une neuvième entrée ; une entrée autre ; un autre ordre : refus avant tout envoi |
| **18. aucun morceau de réponse dans le rapport** | le rapport et les relevés sont comparés aux réponses gardées : aucune suite de plus de 20 caractères d'un texte jugé ou d'une pensée ne s'y trouve ; sinon le rapport n'est pas rendu | rapport aux seuls champs techniques | un extrait de réponse glissé dans un champ : trouvé, arrêt, code de sortie non nul |
| **19. borne dure en octets par envoi (Mistral)** | 6.4 : le programme compte les octets de contenu du flux et ferme la connexion quand la borne de l'envoi est passée (262 144 à la file ; 32 768 à la vérification) ; l'envoi coupé est compté à sa réserve ; il arrête la ligne, sans reprise ; le rapport dit « envoi coupé à sa borne en octets » | flux de 200 000 octets de contenu, fin `stop` : il va au bout, compté à son coût réel ; les valeurs des champs `type` ne sont pas comptées | flux de la file qui passe 262 144 octets : coupé, le faux fournisseur voit la connexion fermée, compté 0,610 ou 0,625, file arrêtée « à son plafond », aucun second envoi ; flux de vérification qui passe 32 768 octets : coupé, nœud ; un appel de Google ne porte aucune borne en octets : la garde le dit au journal, sans rien couper |

Aucune reprise cachée : appels par la bibliothèque standard, sans bibliothèque cliente des fournisseurs ; un essai le vérifie (une réponse 500 : deux envois reçus, pas trois). Aucun repli silencieux : toute garde qui coupe écrit son motif et rend un code de sortie propre. La garde 19 ne tient que Mistral : chez Google, l'excès est chiffré et non coupé (6.4). **L'arrêt sur un nom servi différent** (garde 5) est celui que le programme des ancres devra porter à la course (texte, 3.4 ; 13.2, case « version des modèles »). La garde 18 ne vaut pas pour le corps d'erreur d'une vérification (4.1), qui n'est pas une réponse.

## 11. Lignes de GO de calcul à demander à Lazar

| n° | objet de la ligne | appels | plafond | excès possible d'un seul envoi, au débit déclaré de 200 jetons par seconde (S) |
|---|---|---|---|---|
| 1 | bras A, vérification de la clé de Mistral par le point d'accès européen | **trois appels au plus, soit trois envois au plus**, sonde de borne et retrait de la température compris | **0,25 USD** | 1,17 USD, si l'une des deux suppositions de la borne en octets manque |
| 2 | bras A, vérification de la clé de Google pour `gemini-4-neon` | **trois appels au plus, soit trois envois au plus**, sonde de borne et seconde orthographe du niveau de réflexion comprises | **1,50 USD** | 7,58 USD, si la sortie maximale ne borne pas la réflexion |
| 3 | bras A, essai d'admission du second lecteur, **file Mistral**, par le point d'accès du relevé de vérification | 24, 48 envois au plus | **4,75 USD** | 0,64 USD, si l'une des deux suppositions de la borne en octets manque |
| 4 | bras A, essai d'admission du juge des deux ancres, **file Neon** | 8, 16 envois au plus | **8,50 USD** | 7,58 USD, si la sortie maximale ne borne pas la réflexion |
| 5 | **accordée d'avance, sous condition** (décision de Lazar) : vérification de la clé de Mistral par le point d'accès global, **seulement si le signe de 4.5 est constaté**, sous la garde 15 | trois appels au plus, soit trois envois au plus | **0,25 USD** | 1,17 USD, de même que la ligne 1 |

- Total des plafonds : **15,25 USD** ; 15,00 sans la ligne 5. Attendu ≈ 0,55. Excès possibles, un par ligne : 18,14 USD ; 16,97 sans la ligne 5. Plafonds et excès ensemble : 33,39 USD ; 31,97 sans la ligne 5.
- **Chaque ligne écrit, à la place de « plafond tenu par compteur avant l'envoi »**, l'une de ces deux phrases, avec ses chiffres :
  - **lignes 2 et 4 (Google)** : « plafond tenu par compteur si la sortie maximale borne la réflexion ; sinon, excès possible d'un seul envoi, au plus 7,58 USD au débit déclaré de 200 jetons par seconde, non mesuré ; couvert par le crédit chargé » ;
  - **lignes 1, 3 et 5 (Mistral)** : « plafond tenu par compteur et par une borne dure en octets par envoi, si tout jeton facturé est émis dans le flux et si la coupure arrête la facturation ; sinon, excès possible d'un seul envoi, au plus 1,17 USD (0,64 à la ligne 3) au débit déclaré de 200 jetons par seconde, non mesuré ; couvert par le crédit chargé ».
- **Ce que Lazar accepte en accordant une ligne** : son plafond, et, en connaissance de cause, que la dépense le passe une fois de cet excès si le service ne borne pas la réflexion. Au-delà du débit déclaré, l'excès croît ; seul le crédit prépayé l'arrête (6.4).
- **Chaque ligne nomme aussi** : son objet ; la variable de la clé ; le compte qui paie ; les prix comptés — pour Mistral, 0,77 et 2,31, soit 1,1 fois le prix courant, sur l'un et l'autre point d'accès — ; le brouillon du texte en vigueur ; et les empreintes : de ce devis accepté, du constat des conditions d'envoi, du fichier des règles, des deux pages de prix scellées, des deux relevés documentaires (`291341e2…`, `14d73d52…`), de la pièce du mot « goreco » (`9b9ee5ca…`).
- **Les lignes 1, 2 et 5 écrivent en toutes lettres** « trois appels au plus », et que ce qui se refait par 4.4 reste sous la même ligne. **À redire à Lazar** : ce budget est serré. Chez Google, si `XHIGH` est refusé, les appels A, A′ et B prennent les trois ; un seul code 429 de plus demande une ligne nouvelle.
- **Les lignes 3 et 4 disent** : deux envois par appel ; un code 429 consomme la reprise, après une attente de 600 secondes au plus ; les délais de 5.6 ; elles ne servent qu'après leur vérification saine, sonde « comprise » ou mot de Lazar. Elles disent aussi que **la sortie maximale de 32 768 ne tient dans les délais que si le service rend 12,2 jetons par seconde ou plus, débit non mesuré** : sous ce débit, une lecture à la sortie maximale est coupée, et le modèle ne tient pas pour une raison de délai. La ligne 3 dit de plus : **une lecture de plus de 262 144 octets de contenu est coupée, et la file ne tient pas** (6.4).
- **La ligne 5, et l'élargissement du signe, à dire à Lazar.** Le mot « goreco » accorde cette ligne « si le signe de "ne sert pas ce modèle" fixé au devis est constaté ». Il répondait à une recommandation faite sur le signe du brouillon 1. **Depuis, le signe a été élargi** : le code **422** s'ajoute aux codes 400 et 404, et la forme **`detail`** s'ajoute aux formes qui désignent le modèle. Raison : 422 est le seul code d'erreur que le schéma de Mistral écrit pour cet appel. Ces formes restent supposées, sans pièce. La contre-lecture juge l'élargissement acceptable, à dire à Lazar. **Le signe que la ligne 5 vise est donc celui-ci**, recopié de 4.5 : le point d'accès européen « ne sert pas ce modèle » si, et seulement si, dans la même vérification, (1) l'appel de liste rend le code 200 et une liste lisible où aucune entrée n'a l'identifiant `mistral-large-4-0` ; (2) l'appel A rend le code 400, 404 ou 422 ; (3) le corps d'erreur désigne le modèle : `type` vaut `invalid_model` ; ou `code`, comparé comme une chaîne, vaut `1500` ; ou `message` contient `mistral-large-4-0` et l'une des chaînes `invalid model`, `model not found`, `unknown model`, `does not exist` ; ou `detail` est un tableau dont une entrée a un `loc` dont un élément est égal à `model`, et aucune entrée n'a un `loc` dont un élément est égal à un champ de réglage. **Si Lazar ne veut que le signe du brouillon 1**, il le dit en accordant la ligne : le code 422 et la forme `detail` sont alors retirés dans la version acceptée, et une erreur de cette forme est un nœud (4.4, ligne 13).
- **Avec les lignes, le geste de paiement** : crédit utilisable de **9,50 USD chez Mistral** et de **29,00 USD chez Google** (6.5) ; 5,50 et 11,50 au brouillon 2.
- **Ordre** : le texte range les lignes de calcul avant la contre-lecture du programme (préambule de 13). Ce devis ne demande l'engagement d'une ligne qu'une fois le programme contre-lu et ses gardes éprouvées. C'est plus prudent, et cela ne contredit pas le texte : rien ne part avant les deux.

## 12. Ce qui reste à écrire et à faire après ce devis (rien de payant)

1. **Vérification de ce brouillon 3** par un agent qui ne l'a pas écrit, d'un autre modèle ; version acceptée. Les colonnes « réserve », « plafond » et « excès » de 6.3 et le crédit de 6.5 sont à refaire par programme.
2. **Fait** : le relevé documentaire des deux services (`291341e2…`) et son complément (`14d73d52…`), versés et scellés, non opposables. **Reste dû avant la ligne de calcul** : les deux pages de prix, versées et scellées (6.1).
3. **Réglages des deux consoles par Lazar**, puis **le constat daté**, versé et scellé, crédit utilisable et limites de débit compris (section 9). Comptes chargés (6.5).
4. **Un brouillon du texte qui inscrit le constat à la case de 13.1**, avant la première vérification de clé (section 9).
5. **Le fichier des règles**, copie des huit règles du texte, scellé avant le premier envoi, à l'empreinte du brouillon en vigueur.
6. **Le programme qui conduit les essais, en version neuve, et sa configuration.** Selon le brouillon 1, l'actuel (`scripts/chef_essai_mesure_lecteurs_bras_a_v1.py`) nomme Claude, Carbon et GPT, épingle le brouillon 5, et n'a ni la vérification de clé, ni le signe, ni les gardes 5 et 9 à 18.
7. **Un relais par fournisseur, lancé par ligne.** Mistral : relais compatible OpenAI, qui laisse passer le flux tel quel, avec plafond en dollars, borne d'appels, amont fixe et appel de liste ; **il ferme la connexion vers l'amont dès que le programme ferme la sienne** (garde 19), pose l'origine `mandataire` selon 4.4, et journalise les octets envoyés à l'amont. Google : un relais qui appelle `generateContent` **sans flux**, laisse passer `thinkingLevel` sans y toucher, et tient un délai de 2 690 secondes ; le relais version 3 lisait l'amont en flux (contre-lecture, correction 1) : à reprendre ou à refaire.
8. **Le programme d'extraction du texte jugé** (5.5), **le programme de conformité de forme, à la forme du texte en vigueur**, et l'emploi des programmes de vérification des extraits de l'instrument.
9. **Le programme du rapport et celui des règles**, et le contrôle « aucun morceau de réponse ».
10. **Un faux fournisseur local** : le flux de Mistral en morceaux, la réponse de Google, l'appel de liste dans ses deux formes, les erreurs de 4.4 et de 4.5, la sonde ; un flux qui passe la borne en octets, un flux qui facture plus que ses octets ; **les essais des dix-neuf gardes**, cas sain et artefact (R5).
11. **Contre-lecture du code** par un agent neuf d'un autre modèle, puis vérification de ses corrections par le même.
12. **Lignes de calcul** inscrites ; lignes d'engagement au registre des dépenses.
13. Vérifications de clé ; relevés scellés ; nœud de Lazar si une sonde ne dit pas « comprise », si le majorant par octets est « démenti » ou si un envoi est coupé ; lecture de la console par Lazar après tout envoi coupé ; brouillon du texte qui inscrit les relevés et le point d'accès ; fichier des règles à l'empreinte de ce brouillon ; les deux files ; règles appliquées ; case de 13.1 remplie.

## 13. Réserves et points où je doute

1. **Tarifs non opposables** (R7), sans page scellée ; facturation de la réflexion de Mistral non trouvée, supposée au prix de sortie et comprise dans `completion_tokens`.
2. **Ce que borne la sortie maximale** : non écrit pour ces deux appels. La sonde le mesure à 256, non à 32 768. Elle peut rendre « indécidée », ce qui coûte un aller-retour avec Lazar ; plus souvent qu'au brouillon 2, puisqu'elle exige maintenant une réflexion constatée.
3. **La sonde est un appel de plus, dont le corps n'est pas celui de la file.** Je l'ai jugée préférable à un point laissé indécidé. Le vérificateur peut la retirer : il reste alors la garde sur le motif seul, la condition (c) non établie chez Google, l'excès de 6.4, et le nœud de Lazar avant toute file que la consigne prévoit.
4. **Le code 422 et la forme `detail` ajoutés au signe** : supposés. Ils élargissent le signe du brouillon 1, que la contre-lecture avait jugé fermé. Le constat de la liste le garde étroit. La contre-lecture du brouillon 2 le juge acceptable, à dire à Lazar avec la ligne 5 : c'est écrit en section 11.
5. **Le flux de Mistral** : que l'un de ses événements porte `usage`, et que ses événements portent `model`, n'est écrit nulle part dans les relevés. Tranché en 4.3 : il suffit qu'un événement porte `model`, et que tous ceux qui le portent le portent égal. Si aucun ne porte `usage` ou `model`, la vérification n'est pas saine et ce devis est repris, sans flux : un aller-retour, non une file perdue. Sans flux, la borne en octets de 6.4 tombe avec lui, et la voie (b) reste seule chez Mistral.
6. **Google sans flux** : une connexion muette jusqu'à 45 minutes peut être coupée par un intermédiaire, mandataire du réseau compris. Cela ne se voit pas à la vérification, dont les appels sont courts. C'est le risque de délai qui reste.
7. **Débit de 12,2 jetons par seconde** : seuil calculé, non mesuré. Un modèle plus lent qui écrirait 32 768 jetons serait coupé.
8. **Délai global de 40 heures pour la file Mistral** (36 au brouillon 2, avant de compter l'attente sur un code 429) : c'est un pire cas, non une durée attendue. La session qui lance doit pouvoir le tenir, ou accepter le risque d'une file interrompue de notre côté, qui est un nœud de Lazar.
9. **Deux orthographes du niveau de réflexion de Google**, toutes deux d'un résumé d'outil. Si le service en accepte une sans l'appliquer, rien ne le montre.
10. **Taxe de 20 %** : supposée. Recharge minimale, mode de paiement, expiration d'un crédit : inconnus. Si un compte se paie après usage, aucune borne dure ne tient l'excès.
11. **Sorties attendues** (2 000 et 4 000 jetons) : sans mesure à l'effort le plus haut. D'où des plafonds au pire cas, hauts devant l'attendu (15,25 contre ≈ 0,55 ; 33,39 avec les excès).
12. **Vérification de clé à réglages pleins** : elle peut coûter jusqu'à 0,49 USD par appel chez Google si le modèle réfléchit jusqu'au bout sur un message d'un mot ; et plus, à hauteur de l'excès de la ligne 2, si la sortie maximale ne borne pas sa réflexion.
13. **Trois appels par ligne de vérification** : décidé. Mais la sonde et un appel A′ en prennent deux sur trois : une seule cause à corriger de plus demande une ligne nouvelle.
14. **Température 0 envoyée à Mistral** : c'est la lettre du texte ; le conseil général de sa documentation l'admet (« between 0.0 and 0.7 »).
15. **Où vit `MISTRAL_API_KEY`** : non cherché. Si c'est un secret de réseau et non une variable, le relais part avec une valeur factice que le mandataire remplace. Les trois hôtes doivent être permis par le réseau de la session : décision de Lazar s'ils ne le sont pas.
16. **Le corps d'erreur d'une vérification versé au relevé** (500 caractères) : écart au « aucun texte » du brouillon 1, borné aux erreurs des vérifications. Un corps d'erreur peut redire le message fixe de l'appel ; il ne contient aucune lecture.
17. **Les brouillons du texte qui inscrivent le constat, puis les relevés** : ils ne sont pas de mon ressort ; je dis seulement ce que ce devis en attend (section 9).
18. **Longueurs de 6.2 et octets des consignes** : repris du brouillon 1, non revérifiés ; la contre-lecture ne les a pas vérifiés non plus.
19. **Octets du corps** bornés à 5 000 et 24 000 par supposition ; le programme calcule sur le corps réel. **Découpage de Mistral non mesuré** : sans effet sur les plafonds.
20. **Débit déclaré de 200 jetons par seconde** : supposé, sans mesure, pour les deux services. L'excès lui est proportionnel. Un service plus rapide, dont la sortie maximale ne bornerait pas la réflexion, coûterait plus que l'excès écrit ; seul un crédit prépayé l'arrêterait.
21. **Borne en octets de Mistral : trois suppositions.** Un jeton rend au moins un octet ; tout jeton facturé est émis dans le flux ; la fermeture de la connexion arrête la facturation. La deuxième n'est vérifiée que sur des réponses courtes, avec une tolérance de 64 jetons : une pensée cachée de moins de 64 jetons passerait. La troisième ne se vérifie qu'à la console, par Lazar.
22. **La borne en octets peut faire échouer un modèle qui tiendrait autrement** : les trois cas de 6.4. C'est un choix : je préfère une dépense bornée à une lecture de plus de 262 144 octets menée au bout. Le vérificateur peut juger la borne trop basse ou trop haute ; à 524 288 octets, la réserve double, et le plafond de la file Mistral monterait à 5,25 USD environ.
23. **Google reste lu sans flux**, donc sans borne dure par envoi. Deux moyens de réduire son excès ne sont pas pris, pour changer le moins possible : lire Google en flux, si la pensée y est comptée au fil de l'eau (non trouvé) ; un délai total plus court aux seuls appels de vérification, qui baisserait l'excès de la ligne 2 sans pouvoir faire échouer un modèle. À juger.
24. **Le nom de type `thinking`** des morceaux de pensée de Mistral : supposé. S'il est autre, la sonde de Mistral dit « indécidée », et c'est un nœud de Lazar, non une file perdue.
25. **Un seul excès par ligne** : l'argument tient si le programme voit le coût réel de chaque envoi fini. Chez Mistral, un envoi coupé ne rend pas `usage` : il arrête la ligne, et son coût réel n'est connu qu'à la console.
26. **Les clés du tableau du constat** (section 9) sont de mon choix ; le rédacteur du constat peut les renommer avant la version acceptée, non après.
27. **Les chiffres neufs** — réserves, plafond de 4,75, excès, crédits de 9,50 et de 29,00, délais globaux — sont calculés par un programme du bloc-notes de la session, non contre-vérifiés.

## 14. Ce que j'ai ouvert, et les débords déclarés

- **Empreintes vérifiées avant lecture**, contre leur compagnon : le brouillon 2 (`6f81288b5efc…`) et sa contre-lecture (`a70c5f211445…`), par `sha256sum` ; les deux relevés des interfaces (`291341e204a8…`, `14d73d5263e2…`), le relevé des conditions d'envoi (`b959c4d0db2e…`) et la pièce « goreco » (`9b9ee5ca4e89…`), par `sha256sum -c`, tous « OK ». Le texte, brouillon 43 : `4f91b535ad91…`, calculée et comparée à celle que cite le brouillon 2.
- **Lus en entier à cette rédaction** : le brouillon 2 ; sa contre-lecture ; les deux relevés des interfaces ; la pièce « goreco ».
- **Empreinte seulement** : le relevé des conditions d'envoi.
- **Brouillon 43** : je n'en ai rien lu à l'écran. Un programme a comparé ses lignes 521 à 529 (les huit règles de 3.4 et leur titre) aux lignes de la section 7 de ce brouillon : égales caractère pour caractère.
- **Non rouverts** : le brouillon 1 et sa contre-lecture ; la pièce « b a b go » ; les relevés des identifiants ; tout ce que le brouillon 2 marquait « B1 ». Ce que ce brouillon en dit vient du brouillon 2.
- **Débords, déclarés** :
  - une liste du premier niveau du dossier `docs/notes/relance-organismes-discrets-v1/`, filtrée sur quatre motifs de noms (devis, contre-lectures de devis, relevés des interfaces, conditions d'envoi), pour vérifier la présence des fichiers et l'absence du brouillon 3. La consigne ne demandait pas de liste. Les noms affichés comprennent ceux du devis du bras A version 2 et du devis de l'essai de mesure, de leurs contre-lectures et vérifications, et de la pièce « goreco » ; je n'ai ouvert que ceux nommés plus haut ;
  - la pièce « goreco » n'est pas dans la liste des fichiers à lire ; la consigne la nomme par son empreinte. Je l'ai lue, après vérification ;
  - le brouillon 2 nomme des chemins cloisonnés et des chemins sous `runs/` et `registres/` : **je ne les ai ni suivis, ni listés, ni empreintés**.
- **Aucun chemin cloisonné ouvert, listé ni empreinté.** `.claude/`, `registres/` et `runs/` non ouverts. Journal non touché. Aucune clé, aucun appel de modèle ni appel réseau, aucun sous-agent, aucune dépense. Rien committé ni poussé.
- **Ce que la consigne fixait et que j'ai étendu, déclaré** : le délai global des files est recalculé (5.6), pour lever le mineur n-11 par le calcul et non par une phrase ; une garde 19 est ajoutée ; les clés du tableau du constat sont nommées (section 9). Aucun critère, aucune des huit règles, aucune décision « goreco », aucune condition d'envoi ne change.
- Fichiers écrits : celui-ci et son compagnon ; dans le bloc-notes de la session, hors du dépôt, un programme de calcul et les programmes qui composent ce brouillon à partir du brouillon 2.

## 15. Contre-lecture et vérification

- Le brouillon 1 a été contre-lu par Claude Opus 5.5 : « Engageable après corrections » (`03bfab58…`).
- Le brouillon 2 a été contre-lu par le même contre-lecteur, agent neuf : « Engageable après corrections » (`a70c5f21…`), deux corrections, onze mineurs.
- Ce brouillon 3 attend la vérification de ses corrections par un agent qui ne l'a pas écrit. Il est scellé comme brouillon, non accepté. Selon la contre-lecture, le devis peut servir à demander les lignes de calcul une fois les corrections 1 et 2 faites et vérifiées, et la version acceptée scellée.

## 16. Changements depuis le brouillon 1

Cette section est celle du brouillon 2, reprise sans retouche : elle dit l'état du brouillon 2. Ce que le brouillon 3 y change — plafond de la file Mistral, crédits, délais globaux, issue de la sonde, nombre des gardes — est en section 17.

### Les huit corrections

| correction de la contre-lecture | ce qui change | où |
|---|---|---|
| **1. Délais** | mode de lecture écrit : Mistral en flux (`stream: true` ajouté au corps), Google sans flux ; silence 600 s (Mistral) ; total 2 700 s par envoi au lieu de 900 ; débit tenu déclaré, 12,2 jetons par seconde ; délai global calculé sur le pire cas (36 h 14 min et 12 h 11 min) au lieu de deux heures ; la cause d'échec par délai est dite à Lazar | 5.1, 5.2, 5.3, 5.6 ; garde 2 ; 13, points 6 à 8 |
| **2. Sortie maximale** | constat documentaire écrit, relevé cité par chemin et empreinte, quelle que soit la réponse ; issue fixée là où la documentation se tait : la garde ne lit que le motif de fin, une sortie facturée au-delà de 32 768 n'arrête plus la file ; sonde de borne à la vérification ; nœud de Lazar si elle ne dit pas « comprise » ; condition (c) du plafond dite non établie hors de ce cas | 4.6 ; 5.4 ; 6.4 ; gardes 3, 10 et 16 |
| **3. Forme de la réponse à la vérification** | champs exigés à la vérification ; nom servi égal à la lettre ; extraction du texte jugé fixée pour les deux services ; sortie facturée de Mistral lue sur `completion_tokens` ; sinon vérification non saine et brouillon neuf | 4.3 ; 5.5 ; garde 16 |
| **4. Classement fermé de la vérification** | « ou l'inverse » retiré : code 200 et bon nom, saine quelle que soit la liste ; « nomme un champ » défini par programme ; ligne finale fermée (toute autre issue : nœud, ni repli ni appel de plus), 422 et 404 hors forme compris ; 401, 402 ou 403 après une liste admise sans l'identifiant : nœud ; « liste lisible » définie ; `code` comparé comme une chaîne | 4.4 ; 4.5 ; garde 11 |
| **5. Deux gardes manquantes** | garde de l'identifiant figé et de la voie d'accès ; garde qui lie la vérification globale au signe constaté | gardes 14 et 15 |
| **6. Conditions d'envoi** | la garde 9 lit le contenu du constat, à valeurs attendues ; étape ajoutée : un brouillon du texte inscrit le constat à la case de 13.1 avant la première vérification ; le fichier des règles cite le brouillon en vigueur au premier envoi | 9 ; garde 9 ; garde 12 ; 12, points 4, 5 et 13 |
| **7. Reprise sur le brouillon 43** | brouillon 43 cité partout ; GO-2026-11-21-32 et -33 dites inscrites ; réserve « Labs » et « Preview » ajoutée ; les huit règles recopiées à la lettre, règle 6 comprise, sans renuméroter | en-tête ; 0 ; 1 ; 2 ; 7 ; 9 |
| **8. Compte du fournisseur** | montant dit en crédit utilisable ; marge de taxe sur la recharge ; règle « le crédit couvre la somme des plafonds avant toute file », lue par la garde 9 ; « compte chargé au plus juste » retiré des barrières ; phrase « les réglages décident, non la caisse » nuancée (402, 429 répété, délais) | 6.4 ; 6.5 ; 9 ; garde 9 |

### Les dix mineurs

| mineur | ce qui change | où |
|---|---|---|
| m-1 | tout code de 500 à 599 a la reprise unique, 504 compris ; 5.6 et garde 4 accordées | 5.6 ; garde 4 |
| m-2 | « trois délais de suite » retiré ; deux pannes sur un même appel arrêtent la file | 5.6 ; garde 2 |
| m-3 | `Retry-After` borné à 600 secondes ; au-delà, attente de 600, puis envoi | 5.6 ; garde 4 |
| m-4 | garde sur les huit entrées de Neon, identifiants et ordre | 3 ; garde 17 |
| m-5 | contrôle « aucun morceau de réponse » mis au tableau des gardes | garde 18 |
| m-6 | artefacts de la garde 12 sans « ou » : chacun a une seule issue | garde 12 |
| m-7 | relevé documentaire étendu : température de Mistral sous raisonnement, non trouvé, donc envoyée à 0 ; facturation de sa réflexion, non trouvée, supposée | 4.4 ; 5.5 ; 6.1 |
| m-8 | lignes de calcul complétées : « trois envois au plus », point d'accès, prix à 1,1 fois, empreintes citées, brouillon en vigueur, geste de paiement | 11 |
| m-9 | un relais lancé par ligne de calcul, avec la borne et le plafond de cette ligne | 6.4 ; 12, point 7 |
| m-10 | ordre : lignes engagées après la contre-lecture du programme ; écart à l'ordre du texte dit, plus prudent | 11 |

### Les trois questions, devenues décisions

| question de la contre-lecture | état |
|---|---|
| une ligne de vérification pour trois appels | **décidé par Lazar** (« goreco », `9b9ee5ca…`) : trois appels au plus, écrit à la ligne |
| sortie maximale à 32 768 ou à 16 384 | **décidé par Lazar** : 32 768 ; l'option à 16 384 est retirée |
| ligne 5 accordée d'avance | **décidé par Lazar** : oui, sous condition, avec la garde 15 |

### Autres changements, hors de la contre-lecture

- **Relevés neufs repris** : prix confirmés ; `high` et `xhigh` confirmés comme niveaux les plus hauts ; motifs de fin complétés (`CONTINUATION`, `error`, `tool_calls`) ; température de Google à retirer.
- **Orthographe du niveau de réflexion de Google** : deux orthographes, dans un ordre fixé, au lieu d'une seule supposée (4.4, ligne 11).
- **Code 422 et forme `detail` ajoutés au signe** de « ne sert pas ce modèle » : choix déclaré, à juger (4.5 ; 13, point 4).
- **Corps d'erreur d'une vérification versé au relevé**, borné, pour instruire un nœud (4.1 ; 13, point 16).
- **Issue écrite pour une file interrompue de notre côté** (5.6).
- **Rien ne change dans les critères** : 22 sur 24 pour Mistral ; huit sur huit pour Neon ; un seul nom servi. Les plafonds, l'attendu et le total sont ceux du brouillon 1.

## 17. Changements depuis le brouillon 2

Source : la contre-lecture du brouillon 2 (`a70c5f21…`), deux corrections et onze mineurs. Le brouillon 2 (`6f81288b…`) est laissé inchangé.

### Les deux corrections

| correction de la contre-lecture | ce qui change | où |
|---|---|---|
| **C-1. La sonde ne dit « comprise » que si une réflexion a été vue** | l'issue « comprise » exige de plus une réflexion constatée : chez Google, `thoughtsTokenCount` supérieur à 0 ; chez Mistral, au moins un morceau de pensée dans le flux, compté par son type, sans être lu. Sinon, « indécidée ». Artefact ajouté : 256 jetons facturés, fin par sortie maximale atteinte, aucune réflexion constatée | 0, point 6 ; 4.6 ; 5.5 ; garde 16 |
| **C-2. Les plafonds ne bornent la dépense que si la réflexion compte dans la sortie maximale** | **les deux voies, chacune là où elle peut tenir.** Voie (a) chez Mistral, lu en flux : borne dure par envoi, en octets de contenu, tenue par le programme (262 144 à la file, 32 768 à la vérification) ; le compteur réserve cette borne avant chaque envoi ; un envoi coupé arrête la file, « arrêtée à son plafond ». Voie (b) chez Google, lu sans flux, et pour ce que la voie (a) ne tient pas : excès d'un seul envoi par ligne, chiffré à 200 jetons par seconde, écrit à chaque ligne de calcul et au nœud de la sonde, couvert par le crédit. Les appels A, A′ et la sonde sont sous la même règle. Ce que cela fait au critère, et les trois cas où la borne peut faire échouer un modèle, sont écrits comme limites | 0, points 3, 4 et 12 ; 4.3 ; 4.6 ; 6.3 ; 6.4 ; 6.5 ; 6.6 ; 7 ; gardes 1, 10, 16 et 19 ; 11 ; 13, points 20 à 25 |

### Ce qui est recalculé

| grandeur | brouillon 2 | brouillon 3 | raison |
|---|---|---|---|
| plafond de la file Mistral | 4,25 USD | **4,75 USD** | le compteur réserve la borne dure de l'envoi (0,610 ; 0,625) ; à 4,25, il aurait pu refuser un modèle dont tous les envois restent sous 32 768 jetons |
| plafonds des quatre autres lignes | 8,50 ; 0,25 ; 0,25 ; 1,50 | inchangés | la réserve de ces envois ne change pas |
| somme des plafonds | 14,75 (14,50 sans le repli) | **15,25** (15,00) | file Mistral |
| excès possible d'un seul envoi, par ligne | non chiffré | 1,17 ; 7,58 ; 0,64 ; 7,58 ; 1,17 (lignes 1 à 5) | correction C-2 |
| crédit utilisable, Mistral | 5,50 USD (6,60 avec la taxe) | **9,50 USD** (11,40) | plafonds 5,25 et excès 2,98, marge de 15 % |
| crédit utilisable, Google | 11,50 USD (13,80 avec la taxe) | **29,00 USD** (34,80) | plafonds 10,00 et excès 15,16, marge de 15 % |
| seuils de crédit de la garde 9 | 4,75 ; 10,00 | 8,23 ; 25,16 | plafonds et excès |
| délai global de la file Mistral | 130 440 s (36 h 14 min) | 144 840 s (40 h 14 min) | mineur n-11 : l'attente sur un code 429 est comptée à chaque appel |
| délai global de la file Neon | 43 880 s (12 h 11 min) | 48 680 s (13 h 31 min) | de même |
| attendu ; pire cas à 32 768 jetons ; délais par envoi ; délai global de la vérification | 0,55 ; 14,26 ; 600 et 2 700 s ; 8 700 s | inchangés | — |

### Les onze mineurs

| mineur | ce qui change | où |
|---|---|---|
| n-1 | la signature du refus du mandataire est écrite, par programme : code 502 du relais, origine `mandataire`, zéro octet envoyé à l'amont à son journal. À cette signature, l'appel n'est compté ni parmi les trois, ni au compteur ; sans elle, c'est une panne, comptée. Ligne 1 et compteur accordés | 4.4, ligne 1 et alinéa sous le tableau ; 6.4 ; 8 ; gardes 1 et 16 ; 12, point 7 |
| n-2 | « B ou A′ selon l'ordre » retiré : le troisième appel est A′ ; l'appel B demande une ligne nouvelle | 4.2 |
| n-3 | tranché : au moins un événement porte `model` ; chaque événement qui le porte le porte égal ; un événement sans `model` ne rend pas la vérification non saine ; `[DONE]` n'est pas un événement de données | 4.3 ; 5.5 ; gardes 5 et 16 ; 13, point 5 |
| n-4 | `loc` : égalité d'un élément à la chaîne, non sous-chaîne, au signe comme à la définition de « nomme le champ X » | 4.4 ; 4.5 |
| n-5 | la sonde lit la plus grande des deux sorties facturées, comme le coût ; artefact ajouté | 4.6 ; garde 16 |
| n-6 | clés du tableau du constat et valeurs admises écrites, à la configuration ; un artefact par clé, variante « après usage » comprise ; cas sain de cette variante | 9 ; garde 9 |
| n-7 | garde 2 : artefact du délai global, et son cas sain. Garde 10 : forme écrite du mot de Lazar après une sonde non « comprise » (pièce scellée, empreinte inscrite à la configuration), avec son cas sain et ses artefacts | gardes 2 et 10 |
| n-8 | garde 16 : un artefact par ligne du classement, lignes 1, 2, 7, 8, 10, 11 dans ses deux temps, 12 et 13 | garde 16 |
| n-9 | « ils tiennent » devient « ils tiennent si le service rend 12,2 jetons par seconde ou plus, débit non mesuré » ; redit aux lignes 3 et 4 | 1 ; 11 |
| n-10 | l'élargissement du signe (code 422, forme `detail`), postérieur au mot « goreco », est dit à Lazar avec la ligne 5, signe recopié, avec la voie de retrait | 4.5 ; 11 ; 13, point 4 |
| n-11 | la phrase « une attente sur un code 429 n'y ajoute rien » est retirée ; le délai global compte 600 secondes d'attente par appel ; « ne coupe aucune file que les délais par envoi laissent vivre » est alors vrai par calcul | 5.6 ; garde 2 ; 13, point 8 |

### Autres changements, hors de la contre-lecture

- **Garde 19 ajoutée** : la borne dure en octets par envoi, chez Mistral. Les gardes sont dix-neuf.
- **Constat du majorant par octets** ajouté à la vérification de la clé de Mistral : il vérifie, avant la file, que le service ne facture pas plus de jetons que le flux ne rend d'octets ; « démenti » est un nœud de Lazar (4.3).
- **Relevé et rapport** : octets de contenu reçus, nombre de morceaux par type, envoi coupé ou non, pour Mistral (4.1 ; 5.5 ; 8).
- **Lecture de la console par Lazar** après tout envoi coupé chez Mistral (6.4 ; 12, point 13).
- **Section 2** : les empreintes non recalculées à cette rédaction sont marquées « B2 ».
- **Rien ne change** dans : les critères (22 sur 24 pour Mistral ; huit sur huit pour Neon ; un seul nom servi) ; les huit règles de 3.4, recopiées à la lettre et comparées par programme au brouillon 43 ; les trois décisions « goreco » ; les conditions d'envoi du mot « b a b go » ; les réglages, les corps des appels, les délais par envoi, la sortie maximale de 32 768, les tarifs comptés, l'attendu.
