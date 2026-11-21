# La livraison 3 face à la règle des appels aux modèles de Google (GO-2026-11-21-71) — v1

- **Lecteur** : Claude Opus 5.5, contre-lecteur des livraisons 1 à 3, le 2026-11-21. Travail en lecture seule.
- **Règle lue** : `git show origin/main:CLAUDE.md`, section « Appels aux modèles de Google », extraite par la commande donnée (commit `bbb20d37d`).
- **Confronté** : `scripts/chef_essais_admission_bras_a_v2.py` (le chef), `scripts/relais_google_essais_admission_v2.py` (le relais de Google), et le gabarit `…/essais-admission-bras-a-v1/configuration-essais-admission-bras-a-v2-gabarit.json` (le gabarit), tous du commit `70715d3b0`. Trois envois sont visés : la vérification de la clé de Google (appels A et A′), la sonde de borne (appel B), et la file du juge `gemini-4-neon`.
- **Interdits tenus** : aucun réseau, aucun `git fetch`, aucune clé, aucun chemin interdit ; rien écrit hors ce rapport ; rien scellé.

## Verdict

**Corrections pour la livraison 4.** Le réglage de réflexion est explicite et contrôlé avant l'envoi. Mais rien ne vérifie par programme que le plafond atteint « réflexion plus 16 000 jetons de texte », ni que la limite de mots de l'invite tient dans le plafond de texte. Après la réponse, une réponse sans aucun jeton de pensée, ou au texte vide, est encore comptée comme une réponse jugée. Enfin, la garde commune exigée par la règle n'est ni employée ni reproduite. Ce sont les corrections G-1 à G-9.

### Les corrections

- **G-1 — garde commune.** Le chef et le relais de Google emploient la garde commune de `src/controle_ia/`, ou la reproduisent, avec ses essais et ses mutations. Je n'ai trouvé dans `origin/main` aucun module dont le nom la désigne (recherche par nom de fichier ; aucun contenu lu). Si elle n'existe pas encore, l'écrire d'abord.
- **G-2 — plafond de sortie.** Contrôle avant l'envoi : plafond de sortie ≥ borne de la réflexion + 16 000. La forme dépend du choix de la question 2 (budget explicite, ou plafond relevé) ; c'est un nœud de Lazar.
- **G-3 — limite de mots.** Contrôle avant l'envoi : la limite de mots de chaque consigne, inscrite à la configuration avec un rapport de jetons par mot écrit d'avance, tient dans le plafond de texte.
- **G-4 — zéro jeton de pensée.** Dans la file, une réponse sans aucun jeton de pensée est un défaut journalisé, jamais une réponse jugée. `thoughtsTokenCount` absent ne vaut plus 0 mais défaut.
- **G-5 — texte vide.** Dans la file, un texte jugé vide est un défaut journalisé, jamais une lecture « non conforme » comptée parmi les réponses.
- **G-6 — appels A et A′.** La vérification n'est saine que si au moins un jeton de pensée est constaté ; sinon, nœud de Lazar. C'est le cas de l'erreur d'Argon : un niveau accepté mais non appliqué.
- **G-7 — sonde de borne.** Elle reçoit une exemption nommée, à accorder par Lazar, pour le seul contrôle du plafond avant l'envoi (question 5). Les contrôles après la réponse s'y appliquent comme mesure, jamais comme réponse.
- **G-8 — relais de Google.** Il refuse, en dernière barrière, un corps `generateContent` sans réglage de réflexion explicite ou sous le plafond exigé.
- **G-9 — gabarit.** Il inscrit la borne de la réflexion (ou le budget), la marge de 16 000 jetons de texte, et la limite de mots par consigne ; la garde 3 les relit.

## 1. Réglage de réflexion explicite, au niveau le plus haut admis

**Conforme en forme ; le « plus haut admis » n'est pas établi.**

- **Le corps porte le réglage** : `generationConfig.thinkingConfig.thinkingLevel` est posé à chaque envoi de Google (`chef:1068-1069`). Le contrôle avant l'envoi refuse un corps sans ce champ, ou avec une autre orthographe que celle retenue (`chef:1112-1115`). Les trois envois passent par là : file (`chef:2122-2124`), vérification (`chef:1909-1914`), contrôle de tous les corps (`chef:2621-2623`). L'appel B reprend l'orthographe de l'appel sain (`chef:1907`).
- **Les orthographes du gabarit** : `["XHIGH", "xhigh"]` (`gabarit:302-305`). Elles viennent d'un relevé non opposable (devis, 4.4 ; R7). Que `xhigh` soit le niveau le plus haut que Neon admet n'est attesté par aucune pièce scellée. L'appel A prouve seulement que le niveau est **accepté**, non qu'il est **appliqué** (devis, 4.4 : « un niveau accepté ne prouve pas qu'il est appliqué »).
- **Le relais ne contrôle rien du corps** : un objet JSON lui suffit (`relais_google:249-253`). La règle dit « par tout script » : correction G-8.

## 2. Le plafond atteint-il « réflexion plus 16 000 jetons de texte » ?

**Non conforme : rien ne le vérifie, et rien ne peut le vérifier tant que la réflexion se règle par un niveau.**

- `maxOutputTokens` vaut 32 768 (`gabarit:299` ; `chef:1069`), décision de Lazar dans « goreco ». Avec un niveau, la réflexion n'a pas de borne connue : la règle demande une inégalité que le programme ne peut pas écrire.
- Si `maxOutputTokens` borne la réflexion et la réponse ensemble (probable chez Google, non établi pour `generateContent` ; devis, 5.4), il reste 16 768 jetons à la réflexion avant que le texte passe sous 16 000. Une réflexion plus longue mange le texte et finit en `MAX_TOKENS`, ce qui arrête la file (`chef:2088`).

**Les options** :

| | (a) budget de réflexion explicite : `thinkingBudget` 16 384, plafond 32 768 | (b) plafond relevé à 65 536, niveau `xhigh` gardé | (c) autre |
|---|---|---|---|
| la règle | **vérifiable par programme** : 16 384 + 16 000 = 32 384 ≤ 32 768 | non vérifiable : il faut supposer une borne de la réflexion (≤ 49 536), qu'aucune pièce ne donne | une borne de la réflexion relevée et scellée (documentation de Google pour `xhigh`), puis un plafond égal à cette borne plus 16 000 : vérifiable si la pièce existe (R7) |
| devis, corps de 5.3 | `thinkingConfig.thinkingBudget` au lieu, ou en plus, de `thinkingLevel` ; que l'interface admette les deux ensemble n'est pas relevé : la vérification doit le constater, avec une ligne neuve au classement de 4.4 | `maxOutputTokens: 65536` ; la ligne 2 de 4.4 (`outputTokenLimit` ≥ la sortie maximale) se relit d'elle-même | comme (b), à la borne relevée |
| plafonds en dollars | inchangés : la réserve reste 0,507 et 0,564 USD par envoi de la file, 0,492 par vérification | **changés** (calcul fait ici, à refaire par le vérificateur du devis) : réserve d'un envoi de la file d'environ 1,00 à 1,06 USD ; pire cas des seize envois d'environ 16,2 USD, d'où un plafond de la file d'environ 16,50 au lieu de 8,50 ; vérification : trois envois à 0,98 environ, d'où un plafond d'environ 3,00 au lieu de 1,50 (à 1,50, le second envoi serait refusé). Excès d'un envoi au débit déclaré : environ 7,09 USD au lieu de 7,58. L'avenant (recharge gardée) doit le reprendre | selon la borne |
| délais | inchangés | 65 536 jetons en 2 690 secondes demandent 24,4 jetons par seconde (au lieu de 12,2) : relever le délai ou l'écrire comme limite | selon la borne |
| sonde de borne | elle perd une part de son objet : la réflexion est bornée par le budget ; elle doit plutôt constater que `thoughtsTokenCount` reste sous le budget ; à 256 de plafond, un budget de 16 384 peut être refusé ou rogné : forme non relevée | inchangée | inchangée |
| ce que juge « huit sur huit » | **un autre réglage** que `xhigh` : le juge est admis sous une réflexion bornée à 16 384, et la course doit garder ce réglage. Cela change une décision de Lazar (un seul réglage, le plus haut) | le même réglage ; moins de fins en `MAX_TOKENS`. Cela change la décision « goreco » (32 768) | selon le cas |

**Ma recommandation** : (a) si l'interface admet le budget avec Neon. C'est la seule option que la règle laisse vérifier par programme avant l'envoi, et elle ne touche à aucun plafond en dollars. Sinon (c), si une pièce scellée donne une borne. (b) seulement comme repli, en connaissance du doublement des plafonds. Les trois options sont des nœuds de Lazar : elles changent soit le réglage décidé, soit la sortie maximale de « goreco ».

## 3. La limite de mots de l'invite tient-elle dans le plafond de texte ?

**Je ne peux pas le dire.** Les deux consignes sont des blocs du préenregistrement (lignes 398 à 423 et 445 à 479), lus par le programme et contrôlés par empreinte (`gabarit:` clés `consignes` ; `chef:312-322`). Je n'ai le droit d'en lire que les lignes 521 à 529 : la limite de mots m'est hors d'atteinte sans franchir le cloisonnement.

**Non conforme de toute façon** : le programme n'a aucun contrôle de ce genre. Correction G-3 : quelqu'un d'habilité à lire les consignes inscrit au gabarit la limite de mots de chacune et un rapport de jetons par mot fixé d'avance ; le programme refuse l'envoi si la limite × ce rapport dépasse le plafond de texte (le plafond moins la borne de la réflexion).

## 4. Après la réponse (file du juge)

| cas | ce que fait la livraison 3 | conforme ? |
|---|---|---|
| **zéro jeton de pensée**, fin `STOP`, texte de forme conforme | décision « ok » (`chef:2081-2091`), lecture jugée et comptée parmi les conformes (`chef:2170-2174`, `:2273`) ; `thoughtsTokenCount` absent vaut 0 sans alerte (`chef:1303`) | **non** : G-4 |
| fin `MAX_TOKENS` (et `CONTINUATION`) | arrêt de la file, `garde 3 : fin par sortie maximale atteinte` (`chef:2088`), compté dans `fins_par_sortie_maximale` (`:2272`), non jugé (pas d'événement « forme ») | **oui**, défaut journalisé, jamais une réponse |
| `SAFETY`, `RECITATION`, tout autre motif | classe « refus » (`chef:1334-1340`, `MOTIFS` `:115-116`) : arrêt, `garde 4 : motif de fin de refus` (`:2090`), compté dans `refus` (`:2271`), non jugé | **oui** |
| `promptFeedback.blockReason` sans candidat | lu comme motif (`chef:1318-1319`), donc classe « refus » : arrêt, non jugé | **oui** |
| **texte vide**, fin `STOP` | décision « ok », puis `juger_la_forme` rend « non conforme, cause vide » (`chef:1687-1688`) : compté parmi les réponses de code 200 et les lectures finies | **non** : G-5. Le verdict ne change pas (la file ne tient pas), mais la règle veut un défaut, non une réponse jugée |

- **La classe « refus »** : tout motif autre que `STOP` ou la sortie maximale, motif absent compris, arrête la file sans jugement de forme. C'est conforme à la règle, et plus large qu'elle.
- **`reflexion_constatee` faux** (`chef:1329`) : il ne sert qu'à la sonde, où il donne « indécidée » (`chef:1650-1656`). Il n'a aucun effet dans la file, ni aux appels A et A′ : `forme_de_verification` (`chef:1579-1585`) ne demande ni pensée ni compte de pensée. Une vérification peut donc être saine avec zéro pensée, et la file partir ensuite sur un mot de Lazar après une sonde « indécidée », avec la recommandation écrite d'avance du devis de partir. C'est exactement le cas d'Argon : corrections G-4 et G-6.
- **Un défaut arrête la file entière**, conformément au devis (huit sur huit). La règle ne demande pas plus.

## 5. La sonde et la vérification sont-elles des envois à un modèle de Google ?

**Oui, les deux** : ce sont des `generateContent` à `gemini-4-neon`, par le même relais.

- **Appels A et A′** (`maxOutputTokens` 32 768) : ils sont dans la même situation que la file pour le plafond (G-2). Après la réponse, une réponse sans pensée doit être un défaut : G-6. Prix à dire à Lazar : sur « Reply with the single word: OK », un modèle peut ne pas réfléchir même au niveau le plus haut ; l'issue est alors un nœud de Lazar, non une vérification saine.
- **Sonde** (`maxOutputTokens` 256, `gabarit:300` ; `chef:1909-1913`) : elle viole **par construction** l'exigence de plafond (256 < 16 000). Son objet est de mesurer une borne : la fin en `MAX_TOKENS` y est le résultat attendu de « comprise » (`chef:1653`). Il faut une **exemption nommée de la règle**, accordée par Lazar : c'est un écart à une règle permanente, donc un nœud. Elle porte sur le seul contrôle de plafond d'avant l'envoi, et la garde commune la reconnaît par une marque explicite du corps de la sonde (message fixe, plafond 256), éprouvée par un essai. Les contrôles d'après la réponse s'appliquent à la sonde comme **mesure, jamais comme réponse** : c'est déjà le cas, puisqu'aucun texte de sonde n'est jugé, et « comprise » exige `thoughtsTokenCount` supérieur à 0. Sous l'option (a), la sonde change d'objet (section 2).

## Ce que j'ai ouvert

- La section « Appels aux modèles de Google » de `CLAUDE.md` à `origin/main`, par la commande donnée.
- `git show origin/main --stat`, `git log origin/main` (trois lignes), et la liste des noms de fichiers sous `src/controle_ia` à `origin/main`, filtrée des motifs interdits ; aucun contenu lu.
- Le chef `_v2`, aux lignes 113 à 117, 1059 à 1069, 1105 à 1124, 1297 à 1342, 1579 à 1585, 1632 à 1656, 1683 à 1691 et 2066 à 2100, plus des recherches de lignes ; le relais de Google `_v2`, son `do_POST` ; le gabarit `_v2`, lignes 296 à 312.
- Les consignes du préenregistrement : **non lues** (hors du cloisonnement).
