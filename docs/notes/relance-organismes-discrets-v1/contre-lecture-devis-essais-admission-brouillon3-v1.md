# Contre-lecture du devis des deux essais d'admission (Mistral Large 4, second lecteur ; `gemini-4-neon`, juge des deux ancres), brouillon 3 — bras A — v1

- **Pièce contre-lue** : `docs/notes/relance-organismes-discrets-v1/devis-essais-admission-mistral-neon-bras-a-v1-brouillon3.md`, `657d996cede3d9a5…` (empreinte vérifiée « OK » contre son compagnon), 675 lignes, écrit par Claude Fable 5.2.
- **Point de départ** : le brouillon 2, `6f81288b5efca85f…` (vérifié), et sa contre-lecture, `a70c5f211445…` (vérifiée) : deux corrections, onze mineurs.
- **Contre-lecteur** : Claude Opus 5.5, agent neuf, le 2026-11-21. Je n'ai écrit ni ce devis, ni ses brouillons, ni leurs contre-lectures, ni le texte du bras A.
- **Ce que j'ai fait** : lecture ; comparaison des huit règles et calculs par trois programmes du bloc-notes de la session. Je juge ; je ne corrige rien. Aucun appel de modèle, aucun appel réseau, aucune clé, aucun sous-agent, aucune dépense. Rien scellé, rien committé.
- **Texte en vigueur** : `prereg/T0.7-organismes-discrets-v-a-v2-brouillon43.md`, `4f91b535ad915815…` (vérifié).

## Verdict

**Engageable après corrections.** Deux corrections, toutes deux sur l'excès possible. Elles changent ce qui est dit à Lazar et le crédit de Google. Elles sont à faire avant la demande des lignes de calcul.

La correction 1 du brouillon 2 (sonde) est levée. La correction 2 (plafonds) est levée sur le fond chez Mistral, où la borne en octets est saine sous ses suppositions. Elle ne l'est qu'en partie chez Google : l'argument « un seul excès par ligne » est faux dans le cas même qui fixe le chiffre de l'excès. Les onze mineurs sont levés. Les critères, les huit règles (vérifiées par programme), les décisions « goreco » et les conditions d'envoi sont inchangés. L'arithmétique est juste, et elle suit bien la marge de 64 jetons.

1. **C-1. « Un seul excès par ligne » est faux quand un envoi finit sans compteur lisible.** Un envoi coupé par le délai est compté à sa réserve, puis la ligne continue (appel suivant, ou reprise). Chez Google, la réserve ne borne rien si la réflexion échappe à la sortie maximale. La ligne de vérification de Google peut alors porter trois excès : 24,21 USD réels, au débit déclaré, contre 9,08 écrits. Une file Neon partie sur un mot de Lazar après une sonde non « comprise » peut en porter neuf : environ 73 USD, contre 16,08 écrits.
2. **C-2. L'excès chiffré suppose que la coupure arrête la génération et la facturation. Ce n'est écrit nulle part pour Google.** Lu sans flux, Google n'a pas d'autre borne que cette coupure. Chez Mistral, si la troisième supposition manque, le chiffre de 0,64 ou de 1,17 n'est plus une borne : le délai ne borne rien une fois la connexion fermée.

Le reste est mineur (huit points, question 6).

## 1. Les deux corrections et les onze mineurs du brouillon 2

### Les deux corrections

| correction | traitée fidèlement ? | levée ? | constat |
|---|---|---|---|
| **C-1. Sonde « comprise » seulement sur une réflexion vue** | oui | **levée** | 4.6 : « comprise » exige `thoughtsTokenCount` supérieur à 0 chez Google, au moins un morceau `thinking` chez Mistral ; sinon « indécidée ». 0, point 6 ; 5.5 (compte des morceaux par type) ; garde 16, artefact « 256 facturés, fin par sortie maximale, aucune réflexion : indécidée ». Le nom de type `thinking` est supposé (13, point 24) : s'il est autre, la sonde dit « indécidée », et c'est un nœud, non une file perdue. Réserve : mineur n-1 (un plafond d'octets fermerait le dernier cas faux). |
| **C-2. Borne de la dépense** | oui | **levée chez Mistral ; en partie chez Google** | Voie (a), Mistral : borne dure en octets lus en flux, réserve égale à la borne plus 64 jetons, garde 19, coupure qui arrête la ligne. Saine sous ses suppositions (question 2). Voie (b), Google : excès chiffré à 200 jetons par seconde, écrit aux lignes de 11, au nœud de 4.6, couvert par le crédit de 6.5. Mais l'argument « un seul excès par ligne » (6.4) ne vaut pas pour un envoi coupé par le délai : corrections C-1 et C-2 ci-dessus. |

### Les onze mineurs

| mineur | levé ? | constat |
|---|---|---|
| n-1 | levé | Signature du refus du mandataire écrite par programme : code 502 du relais, origine `mandataire`, zéro octet envoyé à l'amont. Non compté parmi les trois ni au compteur ; sans elle, panne comptée. 4.4, alinéa ; 6.4 ; gardes 1 et 16. |
| n-2 | levé | 4.2 : le troisième appel est A′ ; B demande alors une ligne nouvelle. |
| n-3 | levé | 4.3 : au moins un événement porte `model` ; chacun qui le porte le porte égal ; `[DONE]` n'est pas un événement de données. Gardes 5 et 16. |
| n-4 | levé | « Égalité d'un élément, non sous-chaîne » pour `loc`, en 4.4 et en 4.5. |
| n-5 | levé | La sonde lit la plus grande des deux sorties facturées ; artefact 256 contre 300. |
| n-6 | levé | Douze clés et leurs valeurs admises, à la configuration ; un artefact par clé ; cas sain « après usage, budget aucun ». |
| n-7 | levé | Garde 2 : artefact et cas sain du délai global. Garde 10 : forme écrite du mot de Lazar (pièce scellée, empreinte inscrite), cas sain et artefacts. |
| n-8 | levé | Garde 16 : lignes 1, 2, 7, 8, 10, 11 (deux temps), 12 et 13. |
| n-9 | levé | Section 1, décision 2, et lignes 3 et 4 : « ils tiennent si le service rend 12,2 jetons par seconde ou plus, débit non mesuré ». |
| n-10 | levé | Section 11, ligne 5 : élargissement dit, signe recopié, voie de retrait. Réserve : mineur n-6 (recopie non littérale). |
| n-11 | levé | Délai global recalculé avec 600 s d'attente par appel : 144 840 s et 48 680 s. Vrai par calcul (question 4). |

## 2. La borne en octets chez Mistral

### Est-elle sûre ?

**Oui, sous ses trois suppositions, comme borne par envoi.** Le compte d'octets est un majorant des jetons émis si chaque jeton rend au moins un octet. Il est un majorant des jetons facturés si tout jeton facturé est émis. La réserve (borne plus 64 jetons) est alors le coût maximal d'un envoi, si la coupure arrête la facturation. Le compteur réserve cette borne avant chaque envoi. Le plafond de la ligne est donc une borne dure. Le raisonnement est juste.

Les trois suppositions, une par une :
1. **Un jeton rend au moins un octet.** Vrai des jetons de texte. Les jetons de contrôle (marques de début et de fin de pensée, fin de réponse) peuvent ne rien rendre ; la marge de 64 les couvre s'ils sont peu nombreux. Le constat du majorant par octets (4.3) éprouve cette supposition avec la deuxième. Elle n'est pas nommée aux lignes de 11, qui ne citent que « deux suppositions » (mineur n-3).
2. **Tout jeton facturé est émis dans le flux.** Éprouvée avant la file, par le constat du majorant. L'épreuve est bonne si elle porte sur la sonde : un calcul « vérifié deux fois » fait réfléchir bien plus de 64 jetons, et une pensée cachée s'y verrait. Le devis ne dit pas clairement si la sonde entre dans le constat (titre de 4.3 « appels A et A′ » ; texte « chaque appel de code 200 de la vérification ») : mineur n-2. Une pensée émise sous un autre champ que `delta.content` donnerait « démenti » : c'est le bon sens.
3. **La coupure arrête la facturation.** Non documentée, non vérifiable avant. La lecture de la console par Lazar après un envoi coupé est la bonne parade. Mais deux limites : la lecture ne vise que l'envoi « coupé à sa borne », non l'envoi coupé par le délai ; et si cette supposition manque, l'excès n'est plus borné par le délai (correction C-2).

**Ce qui rend la borne presque toujours sans objet** : si la sonde dit « comprise », la sortie maximale de 32 768 jetons borne déjà tout envoi, sous la supposition que la borne se comporte à 32 768 comme à 256. Chaque envoi coûte alors au plus 0,094 USD, loin sous la réserve. La borne en octets ne joue vraiment qu'aux appels de vérification, partis avant la sonde, et dans une file partie sur un mot de Lazar après une sonde non « comprise ». Le devis gagnerait à le dire ; ce n'est pas une correction.

### Les trois cas où la borne peut faire échouer un modèle

**Acceptables, sans mot de Lazar de plus que l'accord de la ligne 3**, pourvu qu'ils soient dits à la demande des lignes. Ils le sont (11, ligne 3 ; 4.6, nœud). Raisons :
- **cas 1, réflexion hors de la sortie maximale, plus de 262 144 octets** : impossible si la sonde dit « comprise ». Sinon, la sonde dit « non comprise » ou « indécidée », et la file ne part que sur un mot de Lazar, qui lit au nœud : « une lecture dont le contenu passe 262 144 octets est coupée, et la file ne tient pas ». Lazar décide donc en connaissance de cause ;
- **cas 2, plus de huit octets par jeton en moyenne** : très improbable sur des réponses à forme fixe, au lexique inventé ;
- **cas 3, refus du compteur** : hors de la garantie seulement. La garantie est juste par calcul (question 4).

Ce n'est pas un changement de critère : le devis fixe la sortie maximale et les délais, qui peuvent eux aussi faire échouer un modèle ; la borne en octets est de même nature. Mais le nom donné à l'issue force la lettre de la règle 1 (mineur n-4).

### Le plafond de 4,75 USD

**Justifié.** Un modèle dont chaque envoi reste sous 32 768 jetons de sortie atteint au plus 4,5237 USD de cumul plus réserve, au dernier envoi, quel que soit l'ordre (calcul de la question 4). À 4,25, le compteur pouvait refuser un tel modèle. À 4,50 aussi (4,5237 > 4,50). 4,75 est le plus petit quart de dollar qui tienne. Le seuil de refus est de 4,1258 USD (envoi de couverture).

## 3. Google : flux, délai court, crédit

### Ce que le crédit de 29,00 USD ne couvre pas (correction C-1)

Le devis compte un envoi de Google « sans compteur lisible, en erreur ou en panne » à 32 768 jetons de sortie (6.4). Il écrit aussi : « Chez Google, le programme voit le coût réel à la fin de chaque envoi ». Or l'excès au débit déclaré naît justement d'un envoi qui dure jusqu'au délai : il n'a pas de fin, le programme ne voit pas son coût, et le compte à la réserve. La ligne continue :
- **vérification de Google** : un délai dépassé est « refait sous la même ligne » (4.4, ligne 6). Trois envois coupés à 2 690 s : le compteur voit 1,476 USD, sous 1,50. Le coût réel, à 200 jetons par seconde, est de **24,21 USD** (programme `google3.py`). Le devis écrit 1,50 plus 7,58, soit 9,08 ;
- **file Neon, partie sur un mot de Lazar après une sonde non « comprise »** : chaque appel garde sa reprise. Sept appels avec un envoi coupé et une reprise courte, puis un huitième avec deux envois coupés : neuf envois coupés. Le compteur voit 4,94 USD. Le coût réel est d'environ **73,15 USD**. Le devis écrit 16,08 au nœud de 4.6 ;
- **chez Mistral**, le même trou existe pour les délais (silence ou total), mais seulement si une supposition manque : sous les trois, l'envoi coupé coûte au plus ses octets plus 64.

Le cas est improbable : il faut des centaines de milliers de jetons de réflexion. Mais le devis le chiffre, et il dit à Lazar qu'il accepte « que la dépense le passe **une fois** de cet excès ». C'est faux dans le cas même qui donne ce chiffre.

**Deux façons de lever C-1** (au rédacteur de choisir, et de le dire) :
- **(i) compter un envoi de Google sans compteur lisible à 200 jetons par seconde de sa durée, au moins 32 768**, aux appels de vérification et dans une file partie après une sonde non « comprise ». Un envoi coupé au délai fait alors passer le cumul au-dessus du plafond, et la ligne s'arrête : un seul excès, comme le dit le devis. Une coupure brève par un intermédiaire reste comptée bas et garde sa reprise. Après une sonde « comprise », la réserve est une vraie borne : rien ne change. Coût : dans une file partie après une sonde non « comprise », un envoi coupé au délai arrête la file ; c'est à dire à Lazar au nœud ;
- **(ii) garder le compte, et écrire les vrais chiffres** : jusqu'à trois excès à la vérification de Google, jusqu'à neuf dans la file Neon, et le crédit qui va avec. Peu praticable.

### Le flux chez Google (`streamGenerateContent`)

**Non, pas dans ce devis.** Raisons :
- la pensée n'est pas rendue en `generateContent` sans `includeThoughts` (« there are no dedicated thought blocks », relevé `291341e2…`). Avec `includeThoughts`, ce qui revient est un résumé de la pensée, non la pensée. Un compte d'octets sur un résumé ne majore pas les jetons de pensée facturés : l'analogue de la deuxième supposition de Mistral est faux par construction ;
- reste le compteur d'usage au fil du flux. Qu'il arrive pendant la pensée, et non avec le premier morceau de réponse ou à la fin, n'est écrit dans aucune pièce (« flux de la pensée en `generateContent` : non trouvé »). S'il n'arrive qu'après la pensée, le flux reste muet pendant la seule phase qui coûte, et ne borne rien ;
- passer Google en flux rouvre le relais, que la première contre-lecture a fait passer sans flux, et les gardes 2 et 3. Il faudrait un relevé neuf et une issue écrite d'avance, constatée à la vérification (« compteur de pensée vu pendant la pensée : borne ; sinon rien »). Aucun montant ne peut être promis d'avance.

### Un délai plus court aux seuls appels de vérification

**Oui, et le devis peut le prendre lui-même.** C'est un choix de procédure. Il ne touche aucun critère. Il ne peut faire échouer aucun modèle : une vérification qui échoue n'est pas un « ne tient pas » (4.1). Son prix : un appel de plus sous la ligne, ou une ligne nouvelle, si Neon réfléchit plus longtemps que le délai sur « Reply with the single word: OK » ou sur la sonde bornée à 256 ; c'est improbable. Il faut alors retirer « mêmes délais » de l'appel A (4.2) : l'appel A n'éprouve de toute façon pas un délai de 45 minutes. 900 s suit le conseil de Google (« at least 15 minutes ») ; 600 s est le délai de silence de Mistral.

| délai de vérification (relais 10 s en dessous) | excès d'un envoi de vérification | trois envois coupés, au-delà du plafond (compte actuel) |
|---|---|---|
| 2 700 s (devis) | 7,58 USD | 22,72 USD |
| 900 s | 2,18 USD | 6,52 USD |
| 600 s | 1,28 USD | 3,82 USD |

### Le crédit de Google selon la voie

Avec C-1 levée par la voie (i), un seul excès par ligne ; marge de 15 %, arrondi au demi-dollar supérieur (programme `google3.py`) :

| voie | à couvrir | crédit utilisable | avec une taxe de 20 % |
|---|---|---|---|
| devis, délai de 2 700 s partout | 25,16 | **29,00 USD** | 34,80 |
| délai de vérification à 900 s | 19,76 | **23,00 USD** | 27,60 |
| délai de vérification à 600 s | 18,86 | **22,00 USD** | 26,40 |
| recharge en deux temps, délai de 2 700 s : l'excès de la file Neon n'est chargé que si Lazar fait partir la file après une sonde non « comprise » | 17,58 | **20,50 USD** | 24,60 |
| deux temps, 900 s | 12,18 | **14,50 USD** | 17,40 |
| deux temps, 600 s | 11,28 | **13,00 USD** | 15,60 |

**Mon avis** : le devis prend le délai court de vérification (900 s, selon le conseil de Google) et lève C-1 par la voie (i). La recharge en deux temps revient à Lazar : charger est son geste, et il tranche de toute façon au nœud de la sonde. Le devis la lui présente avec les montants. Elle est cohérente avec le devis lui-même, qui dit l'excès de la file Neon « écarté » après une sonde « comprise » (6.4), mais exige quand même de le couvrir avant toute file (6.5 ; mineur n-5).

## 4. Arithmétique

Refaite par programme (`arith3.py` ; `google3.py`, bloc-notes de la session), sur les prix comptés (0,77 et 2,31 ; 3 et 15 USD par million), entrées bornées à 5 000 et 24 000 jetons, corps de vérification à 200 octets.

| grandeur | devis | recalculé |
|---|---|---|
| réserve, file Mistral (appariement ; couverture) | 0,610 ; 0,625 | 0,60955 ; 0,62418 (arrondi supérieur) |
| réserve, vérification Mistral ; trois ; quatre | 0,076 ; 0,228 ; 0,304 | 0,07600 ; 0,2280 ; 0,3040 |
| réserve, file Neon ; vérification Google | 0,507 ; 0,564 ; 0,492 | 0,50652 ; 0,56352 ; 0,49212 |
| **marge de 64, non de 1 024** | — | avec 1 024 : 0,612 ; 0,626 ; 0,078 ; trois 0,235 ; quatre 0,313. **Tous les chiffres du devis suivent 64.** La correction à la main est complète. |
| garantie : cumul avant le dernier envoi ; plus la réserve | 3,91 ; 4,53 | 3,9141 (dernier d'appariement) ou 3,8995 (dernier de couverture) ; plus la réserve : 4,5237 dans les deux cas ; sous 4,75, au-dessus de 4,25 et de 4,50 |
| seuils de refus, Mistral ; Neon | 4,12 ; 7,93 | 4,1258 ; 7,9365 |
| Neon, seize envois à 32 768 | 8,33 | 8,3323 |
| excès à 200 jetons par seconde (538 000 jetons) : vérification Mistral ; file Mistral ; Google | 1,17 ; 0,64 ; 7,58 | 1,1669 ; 0,6371 ; 7,5785 |
| à 100 : mêmes lignes | 0,55 ; 0,02 ; 3,55 | 0,5455 ; 0,0157 ; 3,5435 (le devis arrondit au centime supérieur, partout : prudent) |
| à 400 : mêmes lignes | 2,41 ; 1,88 ; 15,65 | 2,4097 ; 1,8799 ; 15,6485 |
| somme des excès ; sans la ligne 5 | 18,14 ; 16,97 | 18,14 ; 16,97 |
| plafonds et excès ; sans la ligne 5 | 33,39 ; 31,97 | 33,39 ; 31,97 |
| crédit Mistral | 8,23 → 9,46 → 9,50 ; 11,40 | 8,23 × 1,15 = 9,4645 → 9,50 ; 11,40 ; 9,50 ÷ 1,2 = 7,92 |
| crédit Google | 25,16 → 28,93 → 29,00 ; 34,80 | 25,16 × 1,15 = 28,934 → 29,00 ; 34,80 |
| délai global, file Mistral | 144 840 s, 40 h 14 min | 24 × (5 400 + 600 + 10) + 600 = 144 840 s = 40 h 14 min 0 s |
| délai global, file Neon | 48 680 s, 13 h 31 min | 48 680 s = 13 h 31 min 20 s |
| délai global, vérification | 8 700 s | 8 700 s |
| débit minimal | 12,2 | 32 768 ÷ 2 690 = 12,18 |

**Tout est juste.** Une remarque sans effet : la pause de dix secondes vient « après chaque réponse », donc deux fois par appel quand il y a une reprise ; la formule n'en compte qu'une. Le pire cas avec deux pauses (144 480 s et 48 160 s) reste sous le délai global, avec 360 s et 520 s de marge.

**Ce que l'arithmétique ne couvre pas** : les cas de C-1 (24,21 et environ 73,15 USD au débit déclaré), qui sortent de l'argument « un seul excès ».

## 5. Fidélité

- **Critères inchangés** : 22 sur 24 pour Mistral ; huit sur huit pour Neon ; un seul nom servi. Oui.
- **Huit règles de 3.4** : comparées par programme (`regles3.py`) — lignes 399 à 407 du devis contre lignes 521 à 529 du brouillon 43 : neuf lignes égales caractère pour caractère (longueurs 85, 337, 879, 223, 240, 248, 207, 452, 685), règle 6 comprise ; égales aussi aux lignes du brouillon 2. Le renvoi « lignes 521 à 529 » est exact.
- **Décisions « goreco »** : respectées. Trois appels au plus par vérification, écrit aux lignes 1, 2 et 5. Sortie maximale de 32 768, dite conditionnelle au débit de 12,2. Ligne 5 accordée d'avance, sous la garde 15.
- **Plafond de la file Mistral à 4,75** : compatible. Le mot « goreco » ne fixe aucun plafond (pièce `9b9ee5ca…`). Le changement est dit en tête (ligne 5), au tableau de 6.3, en 17 et aux lignes de 11. À la demande des lignes, il faut le redire : 4,25 → 4,75 ; somme 14,75 → 15,25 ; crédits 5,50 et 11,50 → 9,50 et 29,00 (ou le montant qui sortira de C-1).
- **Élargissement du signe dit à la ligne 5** : oui (11, ligne 5 ; 4.5), avec la voie de retrait si Lazar ne veut que le signe du brouillon 1.
- **Écarts au texte, déjà jugés acceptables** : trois appels de vérification au lieu d'« un appel minimal » (3.4 ; 6.11), sur mot de Lazar ; lignes engagées après le programme contre-lu, plus prudent.

## 6. Verdict, corrections et mineurs

**Engageable après corrections.**

### Corrections (avant la demande des lignes de calcul)

**C-1. Rendre vrai « un seul excès par ligne », ou écrire les vrais chiffres.** Un envoi coupé par le délai est compté à sa réserve, et la ligne continue. Chez Google, si la réflexion échappe à la sortie maximale, la vérification peut porter trois excès (24,21 USD au débit déclaré) et une file Neon partie après une sonde non « comprise » neuf (environ 73,15 USD). Chez Mistral, de même si une supposition manque. Lever : compter un envoi sans compteur lisible à 200 jetons par seconde de sa durée, au moins sa réserve, aux vérifications et dans une file partie après une sonde non « comprise » (question 3, voie (i)) ; ou écrire les vrais chiffres et le crédit. Avec l'artefact à la garde 1 : trois délais à la vérification de Google, la ligne s'arrête au premier.

**C-2. Écrire que l'excès chiffré suppose que la coupure arrête la génération et la facturation.** Chez Google, lu sans flux, c'est la seule borne, et rien ne la documente. Chez Mistral, si la troisième supposition manque, 0,64 et 1,17 ne bornent plus rien. À écrire aux lignes de 11, au nœud de 4.6 et en 6.4. Et étendre la lecture de la console par Lazar à tout envoi coupé par le délai, chez les deux fournisseurs, avant toute autre ligne chez ce fournisseur.

### Mineurs

- **n-1** : sonde de Mistral. Si `completion_tokens` ne compte pas la pensée (non écrit, 5.5), « comprise » reste faux dans un cas (pensée hors de la borne, réponse visible à 256). Le devis a déjà le compte d'octets : « comprise » pourrait exiger aussi au plus 256 × 8 octets de contenu reçus, plus une marge. Au-delà, « non comprise ».
- **n-2** : 4.3. Dire que le constat du majorant porte sur la sonde aussi. C'est l'appel où une pensée cachée se verrait le mieux.
- **n-3** : lignes de 11 et 6.4 : « deux suppositions » ; 13, point 21 : trois. Nommer la troisième (un jeton, au moins un octet), ou dire que le constat du majorant l'éprouve avec la deuxième.
- **n-4** : un envoi coupé à sa borne en octets n'est pas une file « arrêtée à son plafond » : le cumul en est loin. Le dire « arrêtée par sa borne de dépense ». La règle 1 la lit « ne tient pas » de toute façon : la file n'a pas 24 réponses de code 200. Et écrire « aucune issue nouvelle ; une cause nouvelle », au lieu de « aucune issue ».
- **n-5** : 6.4 dit l'excès de la file Neon « écarté » après une sonde « comprise » ; 6.5 et la garde 9 exigent pourtant de le couvrir avant toute file. Accorder les deux, ou proposer à Lazar la recharge en deux temps (question 3).
- **n-6** : 11, ligne 5. Le signe « recopié de 4.5 » ne l'est pas à la lettre : il perd « lu comme du JSON », deux « sans égard à la casse » et « de la liste de 4.4 ». Recopier à la lettre, ou écrire que 4.5 fait foi.
- **n-7** : 7, « mesuré et rapporté ». Un majorant « démenti » en pleine file est compté et rapporté, « sans arrêter la file ». Dire qu'alors la borne dure ne tient plus pour la suite de la file ; avec C-1 levée, le compteur reste sûr.
- **n-8** : 5.6. « Ses appels n'ont ni reprise ni attente » (vérification) contre la ligne 6 de 4.4, « cause à attendre ». Dire qu'attendre se fait par un nouveau lancement sous la même ligne, hors du délai global de 8 700 s.

### Le devis peut-il servir maintenant à demander les lignes de GO ?

**Pas encore.** Les lignes 2 et 4 diraient à Lazar « dépassé une fois de 7,58 USD au plus », ce qui est faux au débit déclaré, et le crédit de Google en dépend. Il le pourra après un brouillon 4 qui fait C-1 et C-2, et tranche le délai de vérification de Google, vérifié par un agent qui ne l'a pas écrit, puis scellé comme version acceptée. Le reste des lignes est en place : objet, appels, plafonds, prix comptés, empreintes, élargissement du signe, débit de 12,2.

### Ce qui doit être dit à Lazar avec les lignes

- Le plafond de la file Mistral passe de 4,25 à 4,75 USD (somme 15,25), pour que le compteur réserve la borne dure de chaque envoi.
- Le crédit à charger : 9,50 USD chez Mistral ; chez Google, selon la voie retenue après C-1 (de 13,00 à 29,00 USD, tableau de la question 3), et 20 % de plus si une taxe s'ajoute.
- La borne en octets peut faire échouer Mistral dans trois cas, tous dits ; le premier ne peut arriver qu'après une sonde non « comprise », donc après son mot.
- L'excès est chiffré sous deux suppositions : un débit de 200 jetons par seconde, et une coupure qui arrête la facturation. Aucune n'est mesurée. Au-delà, seul un crédit prépayé arrête la dépense.
- Le signe de « ne sert pas ce modèle » a été élargi après son mot (code 422, forme `detail`) ; il peut le refuser en accordant la ligne 5.
- La sortie maximale de 32 768 ne tient dans les délais qu'à 12,2 jetons par seconde ou plus, débit non mesuré.

## Fichiers ouverts

Empreintes vérifiées par `python -m controle_ia.scellement verifier`, toutes « OK » :
- le brouillon 3, `657d996cede3…`, lu en entier ;
- le brouillon 2, `6f81288b5efc…` : comparé au brouillon 3 par programme, section par section ; lignes changées affichées en partie (sections 4.5, 5.1, 5.6, 7, 8) ; non relu en entier ;
- `contre-lecture-devis-essais-admission-brouillon2-v1.md`, `a70c5f211445…`, lu en entier ;
- `releve-api-mistral-gemini-essais-admission-v1.md`, `291341e204a8…` ; `releve-api-mistral-gemini-essais-admission-complement-v1.md`, `14d73d5263e2…` ; `conditions-envoi-textes-google-mistral-releve-v1.md`, `b959c4d0db2e…` : lus en entier ;
- `mots-de-lazar-juge-et-envoi-des-textes-bras-a-2026-11-21-v1.md`, `00af2aa83604…` ; `mots-de-lazar-devis-essais-admission-bras-a-2026-11-21-v1.md`, `9b9ee5ca4e89…` : lus en entier ;
- `prereg/T0.7-organismes-discrets-v-a-v2-brouillon43.md`, `4f91b535ad91…` : section 3.4 en entier ; 6.11, ses lignes qui contiennent « admission », « neon », « mistral », « trois » ou « envoi » ; 13.2, les lignes « tarifs », « devis », « version des modèles » et « lignes de GO », leurs 1 600 premiers caractères.

Tous sous `docs/notes/relance-organismes-discrets-v1/` sauf le texte.

## Écarts

- **Titres du brouillon 43** : pour repérer les sections, j'ai listé ses titres, filtrés sur 3.4, 3.5, 6.11, 6.12, 13, 13.1, 13.2. Les titres de 3.5 et 6.12 se sont affichés ; je n'ai pas lu ces sections.
- **Chemins cloisonnés nommés dans le texte lu** : 3.4 et 6.11 nomment `docs/notes/bras-a-contre-lecture-habilitee-v1/…`, `prereg/T0.6-organismes-v0-v1.md` et des chemins sous `runs/`. **Je ne les ai ni suivis, ni listés, ni empreintés.**
- **Sorties longues** (le brouillon 3, la contre-lecture du brouillon 2, la section 3.4) gardées d'office par le harnais, hors du dépôt, sous `/root/.claude/projects/…/tool-results/`, puis relues de là pour les afficher en entier.
- **Chiffres mesurés du devis** (longueurs de 6.2, octets des consignes) : non vérifiés ; ils viennent de pièces sous `runs/`, non ouvertes. L'arithmétique part des valeurs déclarées.
- **Ce que je dis du flux de Google** au-delà des relevés (pensée rendue en résumé avec `includeThoughts`, compteur d'usage peut-être absent pendant la pensée) vient de ce que je sais de ce service, **sans pièce** (S). Cela ne fonde aucune correction : seulement l'avis de ne pas prendre cette voie maintenant.
- **Aucune liste de dossier.** Le rapport a été vérifié absent avant écriture par un `ls` sur son chemin exact.
- **Fichiers écrits** : celui-ci. Dans le bloc-notes de la session, hors du dépôt : `regles3.py` (comparaison des huit règles), `arith3.py` (calculs du devis), `google3.py` (cas de C-1 et voies de Google). Rien scellé, rien committé, aucun compagnon.
- **Aucun chemin cloisonné ouvert, listé ni empreinté.** `.claude/`, `registres/`, `runs/` et le journal non touchés. Aucun appel de modèle ni appel réseau, aucune clé, aucun sous-agent, aucune dépense.
