# Contre-lecture du devis des deux essais d'admission (Mistral Large 4, second lecteur ; `gemini-4-neon`, juge des deux ancres), brouillon 4 — bras A — v1

- **Pièce contre-lue** : `docs/notes/relance-organismes-discrets-v1/devis-essais-admission-mistral-neon-bras-a-v1-brouillon4.md`, `31189b57dcacd6b3…` (empreinte vérifiée « OK » contre son compagnon), 809 lignes, écrit par Claude Fable 5.2.
- **Point de départ** : le brouillon 3, `657d996cede3d9a5…` (vérifié), et sa contre-lecture, `b0318fb02c85…` (vérifiée) : deux corrections, huit mineurs.
- **Contre-lecteur** : Claude Opus 5.5, agent neuf, le 2026-11-21. Je n'ai écrit ni ce devis, ni ses brouillons, ni leurs contre-lectures, ni le texte du bras A.
- **Ce que j'ai fait** : lecture entière du brouillon 4 ; comparaison au brouillon 3 par `diff` ; huit règles et signe comparés par programme (`regles5.py`) ; tous les chiffres refaits par programme (`calc5.py`), dans le bloc-notes de la session. Je juge ; je ne corrige rien. Aucun appel de modèle, aucun appel réseau, aucune clé, aucun sous-agent, aucune dépense. Rien scellé, rien committé.
- **Texte en vigueur** : `prereg/T0.7-organismes-discrets-v-a-v2-brouillon43.md`, `4f91b535ad915815…` (vérifié).

## Verdict

**Engageable après corrections.** Deux corrections, toutes deux de rédaction, sur ce qui est dit à Lazar aux lignes. Aucun chiffre n'est à refaire. Le reste est mineur (sept points).

Les deux corrections et les huit mineurs du brouillon 3 sont levés. L'arithmétique est juste, à chaque chiffre neuf. Les critères, les huit règles (vérifiées par programme), les décisions « goreco » et les conditions du mot « b a b go » sont inchangés.

1. **C-1. Au régime courant, « un seul excès » repose sur une supposition de plus, que les lignes ne disent pas.** Après une sonde « comprise », un envoi coupé est compté à sa réserve et garde sa reprise. Si la borne ne se comporte pas à 32 768 comme à 256, jusqu'à neuf envois de la file Neon peuvent porter un excès (72,77 USD au débit déclaré). Le devis l'écrit en 6.4 et en 13, point 28. Mais la ligne 4 et l'alinéa « Ce que Lazar accepte » de la section 11 disent « une fois ». Et ce même cas est le prix caché de la recharge en deux temps : le solde laissé peut couper une file qui tiendrait.
2. **C-2. « La dépense ne peut pas passer le solde prépayé » est plus fort que le relevé.** Le relevé cité dit lui-même que des crédits Google Cloud admissibles peuvent s'appliquer à l'API Gemini une fois le prépaiement acheté. Ce que fait le service au solde nul (arrêt, ou bascule sur le moyen de paiement du compte) n'est pas relevé. La phrase est écrite aux lignes 2 et 4.

## 1. Les deux corrections et les huit mineurs du brouillon 3

### Les deux corrections

| correction | levée ? | constat |
|---|---|---|
| **C-1. « Un seul excès par ligne »** | **levée au régime prudent** ; reste un cas au régime courant (C-1 ci-dessus) | Voie (i) prise. 6.4 : un envoi sans compteur lisible est compté à 200 jetons par seconde de sa durée, au moins sa réserve, aux vérifications, dans une file partie sur un mot de Lazar, et après un majorant démenti en file. Recalculé : une vérification de Google coupée à 890 s est comptée 2,6706 USD, au-dessus de 1,50 : la ligne s'arrête au premier envoi. Une vérification de Mistral coupée au silence (590 s) : 0,2727 USD, au-dessus de 0,25 : de même. Un envoi Neon coupé à 2 690 s : 8,085 ou 8,142 USD ; avec la réserve suivante, 8,5915 : la file s'arrête. L'argument de 6.4 est juste : avant chaque envoi, cumul plus réserve sous le plafond ; après, cumul compté qui majore la dépense au débit déclaré ; donc plafond plus un excès. Garde 1 : l'artefact « trois délais à la vérification de Google, la ligne s'arrête au premier » est écrit. 4.4, ligne 6 ; 5.6 ; 4.6 ; 11 accordés. |
| **C-2. L'excès suppose que la coupure arrête la génération et la facturation** | **levée** | Écrit en 0, point 12 ; 4.6 (nœud, les deux files) ; 6.4 (trois suppositions de l'excès) ; 6.6 ; 11 (les deux phrases des lignes). Chez Mistral : « si la troisième manque, ni la borne ni ce chiffre ne bornent plus rien ». Lecture de la console après tout envoi coupé, par un délai ou à sa borne en octets, chez les deux fournisseurs, avant toute autre ligne chez ce fournisseur : 4.1, 6.4, garde 20, 11, 12 point 13. Réserve : mineur m-1 (connexion coupée). |

### Les huit mineurs

| mineur | levé ? | constat |
|---|---|---|
| n-1 | levé | 4.6 : « comprise » exige au plus 2 048 octets de contenu reçus chez Mistral ; « plus de 2 048 » : « non comprise ». Garde 16 : 5 000 octets « non comprise », 2 048 « comprise ». Bornes cohérentes (au plus / plus de). 13, point 32 : sans marge, dit. |
| n-2 | levé | 4.3 : « appels A, A′ et B : la sonde y entre ». Artefact de la garde 16 à la sonde. |
| n-3 | levé | Trois suppositions nommées en 6.4, au nœud de 4.6, aux lignes 1, 3 et 5, en 13 point 21. |
| n-4 | levé | « arrêtée par sa borne de dépense » ; « aucune issue nouvelle ; une cause nouvelle » (6.4, 7, garde 19). |
| n-5 | levé | 6.4 et 6.5 accordés par la recharge en deux temps. Réserve : C-1 (son prix n'est pas tout dit). |
| n-6 | levé | Signe de la ligne 5 égal à celui de 4.5, quatre lignes égales caractère pour caractère, espaces de tête ôtés (programme) ; égal aussi au 4.5 du brouillon 3. « 4.5 fait foi » écrit. |
| n-7 | levé | Section 7 et 6.4 : majorant démenti en file, borne dure perdue pour la suite, compteur au régime prudent. |
| n-8 | levé | 5.6 : « ni reprise ni attente dans un même lancement » ; une cause à attendre se refait par un lancement nouveau, sous la même ligne, hors du délai global. |

## 2. Le prépaiement de Google

### Est-il bien porté ?

**Oui, sur trois des quatre points ; le quatrième est trop fort (C-2).**
- **Solde à court qui coupe une file** : dit en 6.4 (« C'est alors la caisse qui décide »), en 6.5 (conséquence 2), en 0 point 4. La règle « le crédit couvre plafonds et excès avant toute file » est gardée. Bien.
- **Constat par le crédit visible** : clé `google_offre_payante` (« un crédit prépayé est visible à la console ») et `google_credit_utilisable_usd`, nombre seul, au moins 12,18 ; « après usage » refusé ; artefacts à la garde 9. Bien. Mineur m-5 : garder aussi la lettre du mot « b a b go » (« un compte de facturation actif »).
- **Recharge automatique désactivée** : clé `google_recharge_automatique`, `désactivée` ou `non proposée` ; artefact `activée`. Bien. Son existence n'est pas relevée : dit (13, point 33).
- **Borne dure** : 6.4 écrit « La dépense chez Google ne peut donc pas passer le solde prépayé, quels que soient le débit, la réflexion et ce que fait la coupure ». Deux limites seulement sont dites (arrêt exact au solde nul ; recharge automatique). **Il en manque deux.** (a) Le relevé `26ba69ee…` porte : « Prepay users must first purchase Prepaid credits before any eligible Google Cloud credits can be applied to Gemini API usage. » Une fois le prépaiement acheté, d'autres crédits admissibles du compte de facturation peuvent donc payer l'API. La borne est alors le solde prépayé plus ces crédits. (b) Ce que fait le service au solde nul — refus, ou bascule sur le moyen de paiement du compte de facturation — n'est pas relevé. La phrase passe aux lignes 2 et 4 (« La dépense ne peut pas passer le solde prépayé »). D'où C-2.

### La recharge en deux temps est-elle sûre ?

**Sûre dans le cas pour lequel elle est faite ; non dans un cas que le devis ne lui impute pas.**
- **Sonde non « comprise » et mot de Lazar** : le complément porte le solde vu à 18,50 USD ; la garde 10 exige au moins 16,08 vus. Au régime prudent, la dépense de la file est bornée à 8,50 + 7,58 = 16,08 au débit déclaré. Le solde couvre. Sûre.
- **Sonde « comprise »** : aucun complément ; l'excès de la file est « écarté » sous la supposition que la borne se comporte à 32 768 comme à 256. Solde au départ de la file (programme) : 14,48 USD si la vérification a coûté l'attendu ; 10,82 si elle a pris plafond et excès ; 8,50 au plus bas que la garde 9 admet (crédit vu de 12,18). **Si la supposition manque, la recharge en deux temps peut couper une file qui tiendrait.** Exemple : une lecture finie normalement au-delà de 32 768 jetons facturés n'arrête pas la file (5.4, part 1) ; elle est comptée à son coût réel. Si c'est le dernier envoi, la file tient avec une dépense jusqu'à 16,08 au débit déclaré. Le solde de 10,82 à 14,48 peut manquer avant : refus du service, une réponse de moins, la file ne tient pas, pour une raison de caisse. De même d'un envoi coupé dont la reprise trouve le solde vide. En une fois (23,00), le solde au départ de la file est de 19,32 à 22,98 : il couvre un excès.
- **Le devis écrit le prix des deux temps** (6.5) : un second geste de paiement et le délai d'apparition du crédit. Il n'écrit pas ce prix-là. C'est la seconde moitié de C-1.
- **Le cas est improbable** : il faut que la borne tienne la réflexion à 256 et non à 32 768. Mais c'est exactement le cas que le devis veut éviter (« la caisse qui décide, non le modèle »), et Lazar choisit entre 14,50 et 23,00 sur ce qui lui est dit.
- Deux points plus petits : le solde vu après la vérification peut ne pas encore porter sa dépense (délai d'affichage non connu, S) : mineur m-3. Une seconde ligne de vérification de Google, après un envoi coupé, exige de nouveau 12,18 vus ; avec 14,50 au départ et 3,68 pris, il en reste 10,82 : une recharge est alors due, non dite : mineur m-4.

### Le minimum de 5 USD vaut-il pour un complément ?

**Non relevé. Il faut le dire, et le devis le dit à moitié.** Le relevé ne vise que le premier prépaiement (« Upgrading from the Free Tier to the Paid Tier means … prepaying to add a minimum of $5 »). Le devis le dit bien en 6.5, au montant du complément (« porté à 5,00 si le minimum de 5 USD vaut aussi pour un complément (S) ») et en 13, point 10 (« minimum d'un complément : inconnu »). Mais 6.5, alinéa « Recharge minimale », écrit « 5 USD chez Google (M, non opposable) », sans borner au premier prépaiement. Et le geste de paiement de la section 11 ne parle pas du minimum. Mineur m-2. Sans effet sur la dépense : un complément porté à 5 USD donne un solde plus haut, et « le surplus n'est pas une dépense permise » est écrit.

## 3. Les deux régimes du compteur (réserve 1 du rédacteur)

**Acceptable, comme choix déclaré, à condition de le dire aux lignes (C-1).**
- **Pourquoi c'est acceptable.** Le régime prudent partout ferait échouer Neon sur un seul délai de 45 minutes après une sonde « comprise », contre la « reprise unique comprise » de la règle 2 : une règle de compte du devis déciderait. Le cas laissé ouvert exige une borne qui tient la réflexion à 256 et non à 32 768. La contre-lecture du brouillon 3 avait proposé cette coupe (voie (i)). Le rédacteur l'écrit lui-même (6.4, « Au régime courant » ; 13, point 28) et laisse le choix au vérificateur. Je le garde.
- **Chez Google, le cas restant est-il borné par le solde ?** **Oui, sous trois réserves.** Neuf envois coupés coûteraient 72,77 USD au débit déclaré (programme), contre 4,56 comptés au régime courant. Le solde au départ de la file, de 8,50 à 14,48 en deux temps, arrête la dépense avant. Réserves : le solde n'est une borne que sans autre crédit admissible et sans bascule au solde nul (C-2) ; l'arrêt exact au solde nul n'est pas écrit (S) ; la source est une transcription (R7). Et borner la perte coupe la file : c'est la caisse qui décide (C-1).
- **Chez Mistral, l'est-il par la borne en octets ?** **Oui, sous les trois suppositions, et mieux qu'à Google.** Au régime courant, un envoi coupé de Mistral est compté à la plus grande de 32 768 et des octets reçus plus 64. Sous les suppositions 1 et 2, ce compte majore son coût ; la garde 19 coupe à 262 144 octets dans les deux régimes. Le compteur reste donc un majorant : pas d'excès multiple. Reste un trou étroit : les suppositions 1 ou 2 manquent seulement sur des envois coupés, sans qu'aucun envoi fini ne démente le majorant avant (un envoi fini qui le dément fait passer au régime prudent, section 7). Et si la supposition 3 manque, rien ne borne, le crédit de Mistral seulement s'il est prépayé, ce qui n'est pas relevé (6.4 ; 13, point 10). C'est écrit.
- **Ce qui manque** : la ligne 4 et « Ce que Lazar accepte » (section 11) disent « une fois » sans condition ; la ligne 3 aussi, plus faiblement. Le crochet « [ligne 3 : si la file part sur un mot de Lazar] » omet « ou après un majorant démenti » (mineur m-6). Voir le texte proposé des lignes, question 6.

## 4. Arithmétique

Refaite par programme (`calc5.py`), sur les prix comptés (0,77 et 2,31 ; 3 et 15 USD par million), entrées bornées à 5 000 et 24 000 octets, corps de vérification à 200 octets, débit de 200 jetons par seconde, arrondi supérieur au centime comme le devis.

| grandeur | devis | recalculé |
|---|---|---|
| excès, vérification de Google, 890 s | 2,18 | 178 000 jetons × 15 − 32 768 × 15 = 2,17848 → 2,18 |
| à 100 et à 400 jetons par seconde | 0,85 ; 4,85 | 0,8435 ; 4,8485 |
| excès des autres lignes (1, 3, 4, 5) | 1,17 ; 0,64 ; 7,58 ; 1,17 | 1,16694 ; 0,63708 ; 7,57848 ; 1,16694 |
| somme des excès ; sans la ligne 5 | 12,74 ; 11,57 | 12,74 ; 11,57 |
| plafonds et excès ; sans la ligne 5 | 27,99 ; 26,57 | 27,99 ; 26,57 |
| seuils : Mistral ; Google avant vérification ; avant une file Neon sur mot de Lazar | 8,23 ; 12,18 ; 16,08 | 5,25 + 2,98 = 8,23 ; 10,00 + 2,18 = 12,18 ; 8,50 + 7,58 = 16,08 |
| crédits, marge de 15 %, demi-dollar supérieur | 9,50 ; 14,50 ; 18,50 ; 23,00 | 9,4645 → 9,50 ; 14,007 → 14,50 ; 18,492 → 18,50 ; 19,76 × 1,15 = 22,724 → 23,00 |
| avec une taxe de 20 % | 11,40 ; 17,40 ; 27,60 | 11,40 ; 17,40 ; 27,60 (et 22,20 pour un solde de 18,50) |
| complément | 4,02 à 7,68 | 18,50 − 14,48 = 4,02 ; 18,50 − 10,82 = 7,68 |
| dépense la plus grande, lignes 2 ; 4 ; 1 et 5 ; 3 | 3,68 ; 16,08 ; 1,42 ; 5,39 | 3,68 ; 16,08 ; 1,42 ; 5,39 |
| régime prudent : durées sous lesquelles un envoi est compté à sa réserve | 164 ; 1 311 ; 164 s | 163,84 ; 1 311,04 ; 164,16 s |
| comptes du régime prudent | 2,68 ; 0,28 ; 8,09 ou 8,15 ; 0,61 ou 0,63, 1,25 ou 1,27 | 2,6706 ; 0,2727 ; 8,085 ou 8,142 (plus 0,50652 : 8,5915) ; 0,60955 ou 0,62418, 1,2466 ou 1,2613 |
| délai global, vérification de Google | 3 300 s | 3 × 900 + 600 = 3 300 s ; Mistral 8 700 ; files 144 840 et 48 680 |
| débit minimal | 12,2 | 32 768 ÷ 2 690 = 12,181 |
| réserves (reprises) | 0,610 ; 0,625 ; 0,076 ; 0,507 ; 0,564 ; 0,492 | 0,60955 ; 0,62418 ; 0,07600 ; 0,50652 ; 0,56352 ; 0,49212 |
| cas résiduel du régime courant, neuf envois Neon coupés | environ 73 | 72,77 réels ; 4,56 comptés |

**Tout est juste.** Le délai de 3 300 s ne compte pas les pauses de dix secondes (30 s pour trois appels) : les 600 s ajoutées les couvrent, comme chez Mistral.

## 5. Fidélité

- **Critères inchangés** : 22 sur 24 pour Mistral ; huit sur huit pour Neon ; un seul nom servi. Oui (0 ; 7 ; 18).
- **Huit règles de 3.4** : comparées par programme (`regles5.py`) — lignes 446 à 454 du brouillon 4 contre lignes 521 à 529 du brouillon 43 : neuf lignes égales caractère pour caractère (longueurs 85, 337, 879, 223, 240, 248, 207, 452, 685), règle 6 comprise. Égales aussi aux lignes 399 à 407 du brouillon 3. Le renvoi « lignes 521 à 529 » est exact.
- **« goreco »** (pièce `9b9ee5ca…`, lue) : trois appels au plus par vérification, écrit aux lignes 1, 2 et 5 ; sortie maximale de 32 768, dite conditionnelle au débit de 12,2, non mesuré ; ligne 5 accordée d'avance, sous la garde 15, avec l'élargissement du signe dit et la voie de retrait. Respecté.
- **« b a b go »** (pièce `00af2aa8…`, lue) : choix 1 (b), huit sur huit, règle 2 inchangée ; choix 3 (b), conditions constatées avant la vérification de la clé, section 9. Seul écart de lettre : « projet avec un compte de facturation actif » se constate désormais par « un crédit prépayé visible ». C'est un affinement, que le relevé fonde (payer = lier un compte de facturation et prépayer) ; le devis le dit. Mineur m-5.
- **Délai court de Google aux vérifications** : procédure, sans effet sur un critère ; une vérification coupée n'est pas un « ne tient pas » (4.1). Fidèle.
- **Changements depuis le brouillon 3** (`diff`) : tous dans les endroits que la section 18 annonce. Rien de silencieux sur les réglages, les corps, les tarifs, les plafonds, les délais des files.

## 6. Verdict, corrections et mineurs

**Engageable après corrections.**

### Corrections (avant de sceller la version acceptée et de demander les lignes)

**C-1. Dire, aux lignes 3 et 4 et à « Ce que Lazar accepte », ce que suppose « une fois » au régime courant, et l'imputer à la recharge en deux temps.** Écrire : après une sonde « comprise » (et, chez Mistral, un majorant « établi »), un envoi coupé est compté à sa réserve et garde sa reprise ; « un seul excès » suppose alors que la borne se comporte à 32 768 comme à 256. Si elle ne le fait pas, plus d'un envoi peut porter un excès, jusqu'à neuf dans la file Neon (72,77 USD au débit déclaré). Seul le solde prépayé borne alors la perte chez Google, et il peut couper une file qui tiendrait. Le même cas va au « prix » de la recharge en deux temps (6.5) : le solde au départ de la file Neon, de 10,82 à 14,48, ne couvre pas un excès de 7,58 ; en une fois (23,00), il le couvre. Lazar choisit entre 14,50 et 23,00 en le sachant.

**C-2. Ramener « la dépense ne peut pas passer le solde prépayé » à ce que le relevé porte.** Aux lignes 2 et 4, en 6.4, en 6.5 et en 13 point 29 : « la dépense chez Google est bornée par le solde prépayé, plus tout crédit Google Cloud admissible du compte de facturation (relevé `26ba69ee…` : « before any eligible Google Cloud credits can be applied ») ; ce que fait le service au solde nul n'est pas relevé ». Deux voies, au choix du rédacteur : une clé de plus au constat (autres crédits admissibles appliqués à l'API Gemini, `aucun` ou un montant ; et, si la console le dit, ce qui se passe au solde nul) ; ou la seule phrase réduite, et la limite à 13, point 29.

### Mineurs

- **m-1** : la lecture de la console (4.1, 6.4, garde 20) vise l'envoi coupé « par un délai ou à sa borne en octets ». La supposition 2 de l'excès vise aussi « une connexion fermée ». Une connexion coupée en route après que la demande a atteint le fournisseur peut laisser générer et facturer. L'ajouter à la garde 20, ou dire pourquoi non.
- **m-2** : 6.5, « Recharge minimale : 5 USD chez Google (M) » : borner au premier prépaiement ; pour un complément, non relevé (S). Le redire au geste de paiement de la section 11.
- **m-3** : garde 10 : le solde vu après la vérification peut ne pas encore porter sa dépense (délai d'affichage non connu). Exiger aussi que le crédit du constat, moins la dépense comptée de la vérification, plus le complément versé, atteigne 16,08 ; ou que Lazar attende que la vérification figure à la console.
- **m-4** : une seconde ligne de vérification de Google, après un envoi coupé, exige de nouveau 12,18 vus (6.5) : avec 14,50 au départ, une recharge est alors due. Le dire en 6.5 et à la ligne 2.
- **m-5** : section 9 : écrire la condition de Google à la lettre du mot « b a b go » (« projet avec un compte de facturation actif »), puis sa forme constatée (« crédit prépayé visible »).
- **m-6** : 0, point 12, et le crochet de la ligne 3 en section 11 : le régime prudent vaut aussi après un majorant démenti en file (6.4). L'ajouter.
- **m-7** : 13, point 28, écrit « le solde prépayé de 14,50 USD borne alors la perte » : au départ de la file, c'est le solde restant (de 8,50 à 14,48 en deux temps), non 14,50.

### Le devis peut-il être scellé comme version acceptée et servir à demander les cinq lignes ?

**Pas en l'état ; après un brouillon 5 qui fait C-1 et C-2, oui.** Les deux corrections sont des phrases ; aucun chiffre ne bouge. Le brouillon 5 peut être vérifié sur ses seuls changements, puis scellé comme version acceptée. Tout le reste des lignes est en place : objet, appels, plafonds, excès, prix comptés, suppositions, empreintes, élargissement du signe, débit de 12,2, lecture de la console.

### Texte proposé des cinq lignes, une phrase chacune (après C-1 et C-2)

1. **Vérification de la clé de Mistral, point d'accès européen** : bras A, vérification de la clé de `mistral-large-4-0` sur `api.eu.mistral.ai`, trois appels au plus, soit trois envois au plus, sonde de borne et retrait de la température compris, plafond 0,25 USD tenu par compteur et par une borne dure de 32 768 octets par envoi, excès possible d'un seul envoi de 1,17 USD au débit déclaré de 200 jetons par seconde si un jeton rend moins d'un octet ou si un jeton facturé n'est pas émis dans le flux, sous la supposition, non documentée, que la coupure arrête la génération et la facturation, compté à 0,77 et 2,31 USD par million.
2. **Vérification de la clé de Google** : bras A, vérification de la clé de `gemini-4-neon`, trois appels au plus, soit trois envois au plus, sonde de borne et seconde orthographe du niveau de réflexion comprises, délai de 900 secondes par appel, plafond 1,50 USD tenu par compteur si la sortie maximale borne la réflexion, sinon excès possible d'un seul envoi de 2,18 USD au débit déclaré de 200 jetons par seconde, tout envoi sans compteur lisible étant compté à ce débit sur sa durée, ce qui arrête la ligne au premier délai, sous la supposition, non documentée, que la coupure arrête la génération et la facturation, compté à 3 et 15 USD par million, payé sur le crédit prépayé, qui borne la perte avec tout crédit admissible du compte.
3. **File Mistral** : bras A, essai d'admission du second lecteur, 24 appels, 48 envois au plus, par le point d'accès du relevé de vérification, plafond 4,75 USD tenu par compteur et par une borne dure de 262 144 octets par envoi, excès possible d'un seul envoi de 0,64 USD au débit déclaré si l'une des deux premières suppositions de la borne manque, compteur au régime prudent si la file part sur un mot de Lazar ou après un majorant démenti, sous la supposition, non documentée, que la coupure arrête la génération et la facturation, faute de quoi rien ne borne la dépense ; une lecture de plus de 262 144 octets est coupée et la file ne tient pas.
4. **File Neon** : bras A, essai d'admission du juge des deux ancres, 8 appels, 16 envois au plus, plafond 8,50 USD tenu par compteur si la sortie maximale borne la réflexion, sinon excès possible d'un seul envoi de 7,58 USD au débit déclaré quand la file part sur un mot de Lazar, au régime prudent, où un envoi coupé à 45 minutes arrête la file, et, après une sonde « comprise », sous la supposition que la borne se comporte à 32 768 comme à 256, faute de quoi jusqu'à neuf envois peuvent porter un excès (72,77 USD au débit déclaré), que seul le solde prépayé borne, au risque de couper la file ; le tout sous la supposition, non documentée, que la coupure arrête la génération et la facturation.
5. **Repli de Mistral, point d'accès global** : bras A, vérification de la clé de `mistral-large-4-0` sur `api.mistral.ai`, accordée d'avance par « goreco », seulement si le signe de 4.5 est constaté sur le point d'accès européen (signe élargi au code 422 et à la forme `detail`, que Lazar peut refuser), sous la garde 15, trois appels au plus, soit trois envois au plus, plafond 0,25 USD et excès de 1,17 USD sous les mêmes suppositions que la ligne 1.

Chaque ligne ajoute, comme l'écrit la section 11 : « après tout envoi coupé, par un délai ou à sa borne en octets, Lazar lit la console avant toute autre ligne chez ce fournisseur » ; les empreintes du devis accepté, du constat, du fichier des règles (lignes 3 et 4), des deux pages de prix, des deux relevés, de la pièce « goreco ». Avec les lignes, le geste de paiement : 9,50 USD chez Mistral ; chez Google, 14,50 USD prépayés puis un complément jusqu'à un solde de 18,50 si la file Neon part sur un mot de Lazar, ou 23,00 en une fois ; 20 % de plus si une taxe s'ajoute.

### Ce qui sépare encore de la première vérification de clé

1. Un brouillon 5 qui fait C-1 et C-2 ; sa vérification par un agent qui ne l'a pas écrit ; le scellement comme version acceptée.
2. Les deux pages de prix versées et scellées (6.1) ; la ligne de calcul cite leurs empreintes.
3. Les réglages des deux consoles par Lazar ; le crédit de Mistral chargé ; le crédit de Google prépayé, recharge automatique désactivée ; le constat daté, versé et scellé, avec ses treize clés (section 9).
4. Un brouillon du texte qui inscrit le constat à la case « lecteurs et juge des ancres » de 13.1 (section 9).
5. Le programme qui conduit les essais, en version neuve, sa configuration, les deux relais (Mistral : flux, fermeture vers l'amont, origine `mandataire` ; Google : sans flux, 890 et 2 690 s), les programmes d'extraction, de forme, du rapport, le faux fournisseur local, et les vingt gardes éprouvées sur un cas sain et un artefact (R5).
6. La contre-lecture de ce code par un agent neuf d'un autre modèle, puis la vérification de ses corrections.
7. Les cinq lignes de GO accordées par Lazar, inscrites à `registres/go.md`, et la ligne d'engagement de chaque vérification au registre des dépenses.
8. Les trois hôtes permis par le réseau de la session, et les deux clés présentes par leur nom (13, point 15) : décision de Lazar s'ils ne le sont pas.

Le fichier des règles n'est dû qu'avant le premier envoi d'une file, non avant la vérification.

## Fichiers ouverts

Empreintes vérifiées par `python -m controle_ia.scellement verifier`, toutes « OK » :
- le brouillon 4, `31189b57dcac…`, lu en entier ;
- le brouillon 3, `657d996cede3…` : comparé au brouillon 4 par `diff` ; hunks lus en partie (4.1, 4.2, 4.3, 4.4 ligne 6, 5.6, 7, 9) ; non relu en entier ;
- `contre-lecture-devis-essais-admission-brouillon3-v1.md`, `b0318fb02c85…`, lu en entier ;
- `credits-essai-google-et-gemini-releve-v1.md`, `26ba69eeae69…`, lu en entier ;
- `releve-api-mistral-gemini-essais-admission-v1.md`, `291341e204a8…` ; `releve-api-mistral-gemini-essais-admission-complement-v1.md`, `14d73d5263e2…` ; `conditions-envoi-textes-google-mistral-releve-v1.md`, `b959c4d0db2e…` : lus en entier ;
- `mots-de-lazar-juge-et-envoi-des-textes-bras-a-2026-11-21-v1.md`, `00af2aa83604…` ; `mots-de-lazar-devis-essais-admission-bras-a-2026-11-21-v1.md`, `9b9ee5ca4e89…` : lus en entier ;
- `prereg/T0.7-organismes-discrets-v-a-v2-brouillon43.md`, `4f91b535ad91…` : section 3.4 en entier (lignes 495 à 535).

Tous sous `docs/notes/relance-organismes-discrets-v1/` sauf le texte.

## Écarts

- **Titres du brouillon 43** : pour trouver 3.4, j'ai listé ses titres, filtrés sur 3.4 et 3.5. Le titre de 3.5 s'est affiché ; je n'ai pas lu cette section.
- **Sortie longue** : la section 3.4 a été gardée d'office par le harnais, hors du dépôt, sous `/root/.claude/projects/…/tool-results/`, puis relue de là pour l'afficher en entier.
- **Chemins cloisonnés nommés dans le texte lu** : 3.4 nomme `docs/notes/bras-a-contre-lecture-habilitee-v1/…`, et des chemins sous `runs/` ; le devis nomme `scripts/chef_essai_mesure_lecteurs_bras_a_v1.py` et des chemins sous `runs/` et `registres/`. **Je ne les ai ni suivis, ni listés, ni empreintés.**
- **Recherches de chaînes** : sur le brouillon 4 et le brouillon 43, fichiers nommés seulement.
- **Aucune liste de dossier.** Le rapport a été vérifié absent avant écriture par un `ls` sur son chemin exact.
- **Chiffres mesurés du devis** (longueurs de 6.2, octets des consignes) : non vérifiés ; ils viennent de pièces sous `runs/`, non ouvertes. L'arithmétique part des valeurs déclarées.
- **Fichiers écrits** : celui-ci. Dans le bloc-notes de la session, hors du dépôt : `regles5.py` (huit règles et signe), `calc5.py` (tous les chiffres). Rien scellé, rien committé, aucun compagnon.
- **Aucun chemin cloisonné ouvert, listé ni empreinté.** `.claude/`, `registres/`, `runs/` et le journal non touchés. Aucun appel de modèle ni appel réseau, aucune clé, aucun sous-agent, aucune dépense.
