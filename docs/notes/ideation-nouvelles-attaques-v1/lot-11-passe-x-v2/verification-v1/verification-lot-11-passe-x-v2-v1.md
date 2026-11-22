# Vérification neuve du lot 11 v2 — passe X (NA-1) — v1

Aucune requête réseau hors 127.0.0.1, aucune clé lue, aucune dépense. Rejeu : 73 essais passés ; 39 mutations (38 tuées, T0 survit, `conforme: true`). Empreinte de la configuration = son compagnon (4f83d3af…). Mes essais : `/tmp/claude-0/-home-user-controle-ia-travail/e2c3ce0b-40f3-55d3-a6bf-333c05f6ccd1/scratchpad/v2_artefacts_x.py` (V1 à V9 rejoués contre la v2, plus W1 à W4).

## Verdict : CONFORME AVEC RÉSERVES (aucun point bloquant ; envoi réel possible si Lazar accepte les réserves)

## Points B1 à B4, R1 à R8
| point | état | preuve |
|---|---|---|
| B1 garde de départ liée à la configuration | porté | V3 : plan partiel → `REFUS G4 : couple non éprouvé…`, 0 envoi. Plan de lancement = les 8 couples (clé, modèle) de la configuration (W4) ; chaque couple doit être « prêt » |
| B2 coût au pire si erreur ou fin absente | porté | V1, V1b : 6,05 = pire, `cout_inconnu` vrai |
| B3 `fin` et modèle servi en liste fermée | porté | V2 : texte absent du journal ; `fin` → liste `FINS`, sinon « autre » / « absente » ; modèle → « autre » / « absent » |
| B4 toute exception de transport | porté | V4 (coupure chunked réelle) : classe « injoignable », exception `IncompleteRead` (nom seul), ligne écrite, flux et compagnon présents, coût au pire |
| R1 crédit sur le corps brut | porté | W1, transport réel local : corps texte brut 403, JSON `{"error":"…"}` 429, `{"message":…}` 403, « prepayment … depleted » 429 : crédit reconnu ; 502 : non. Indicateur `credit` cumulé (`or`). (V6 d'origine passe par le faux transport, qui contourne la correction : sans objet.) |
| R2 suffixe du modèle | porté | V7 : `gpt-6-astra-mini` → « modèle substitué » (suffixe date ou numéro seulement) |
| R3 ligne « envoi » avant l'envoi | porté | diff : ligne `type_ligne: envoi` (empreinte de la requête, réglages) écrite avant `transport` ; ligne d'ouverture avec l'écart Google |
| R4 quarantaine neuve hors des dépôts ; journal de garde | porté | refus si la quarantaine existe ou est sous le dépôt de travail ou `main-lecture` ; trois journaux (principal, garde, réglages) vérifiés absents avant tout envoi |
| R5 réservation à 6,05 ; coût brut | porté | V8 : huit fils, une clé à 13,00 : 2 envois, 1,07 compté ; `cout` ne borne plus au pire, `max(c, pire)` si sortie hors plafond |
| R6 arrêt n° 13 sous le verrou | porté | `_reserver` relit le drapeau sous le verrou |
| R7 aucune redirection | porté | `_SansRedirection` pour les envois de la passe (voir réserve 1) |
| R8 usage Kimi aux deux emplacements | porté | lecture de `choices[].usage` ajoutée |

## G4b (essai de réglages)
- **Dépense** : bornée. Corps fixe : une invite « ok » (`GD.INVITE`), `max_tokens` / `max_completion_tokens` = 16, sans flux ; au plus 3 essais (Claude) ou 2 (OpenAI) par maillon ; arrêt au premier 200 ; un 400 passe au niveau suivant, tout autre statut ou une exception refuse (W2 : corps vérifiés, 3 essais Anthropic max/xhigh/high, journal une ligne par essai). Coût d'un essai de l'ordre de 10⁻³ USD ; hors P_X, comme la garde de départ.
- **Texte autre que « ok »** : non ; le corps est construit de `GD.INVITE` seul, plus le modèle, les extras fermés et l'effort.
- **Niveau retenu sans 200** : non ; `retenu` n'est posé que sur le statut 200 (W3 : 400 puis 200 retient `high`, `efforts` retiré) ; aucun niveau admis : refus. Le journal des essais ne contient aucun texte.
- Une configuration qui fixe déjà un effort et en demande l'essai est refusée ; l'ordre décroissant et la liste fermée sont contrôlés.

## Configuration de lancement
- Chaînes conformes au devis v3 : espèce 3 = Opus 5.5, Opus 4.6, Sonnet 4.6 ; espèce 4 = Fable 5.1, Opus 4.6, Sonnet 4.6 ; ajout Opus 4.6 = Opus 4.6, Sonnet 4.6 (saut) ; ajout Sonnet 4.6 = Sonnet 4.6 (saut) ; Kimi, Astra, Argon, Carbon : un maillon.
- Sous-parts : 72,60 + 12,10 + 6,05 + 6,05 = 96,80 (somme vérifiée). Luc : 9 tentatives au plus × 6,05 = 54,45 ≤ 72,60.
- Pires par tentative (`pire`, tarifs de la configuration, 21 413 octets) : Argon 1,40 ; Astra 5,01 ; Opus 5.5 2,01 ; Opus 4.6 2,51 ; Fable 5,01 ; Sonnet 4.6 1,50 ; Carbon 2,90 ; Kimi 1,00 : tous sous 6,05 ; `Passe` construite sans refus (G5, G6 : Argon et Carbon à 65 536 avec réflexion 49 152, niveau high, sous la garde v3).
- Les modèles de l'orchestrateur (opus-5-5, fable-5-1, argon, astra, carbon) sont tous présents. Les numéros d'espèce suivent le devis, non l'ordre de ce fichier (espèce 1 = Argon, 2 = Astra, 3 = Opus 5.5, 4 = Fable, 5 = Carbon) : conforme au LISEZMOI (devis de l'héritage v5), non recoupé ici.
- Plan = configuration : les 8 couples sont égaux (W4). Les tarifs de Kimi et des bornes d'Astra et Carbon restent « TK » / bornes du devis, comme dit au LISEZMOI.

## Réserves restantes (non bloquantes)
1. La garde de départ et G4b utilisent `GD.transport_reel` (`urlopen`, redirections suivies) : R7 ne couvre que les envois de la passe. Risque très faible (hôtes fixes) ; à consigner.
2. Google : la garde de départ prouve l'accès seul (`countTokens`), jamais le crédit ; un défaut de crédit Google apparaîtra à la passe elle-même (classe « erreur de requête » ou « crédit épuisé », n° 13 levé si le motif y est).
3. G4b : un 400 dû au crédit (Anthropic le rend en 400) fait parcourir les niveaux puis refuse ; sûr, mais le message dit « aucun niveau admis ».
4. Le coût réel peut dépasser la réservation de 6,05 sans que le n° 12 l'arrête en cours de tentative (tarifs de configuration à tenir justes ; pire calculé le plus haut : 5,01).
5. Le suffixe numérique `-v?\d{1,3}` du modèle servi reste large (ex. `…-4`) : à relire à l'essai réel.
6. Écarts du LISEZMOI v2 : tous déclarés (Google 65 536, huit proposeurs, noms de classes, A5, transport propre, Neon). Pas d'écart non déclaré trouvé.
