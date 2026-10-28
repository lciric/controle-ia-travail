# Premier lancement réel du pôle, option (a) — lecture dans les deux sens — v1

Lignée conv-audit (instance du 27 octobre 2026), écrit à partir de 15:04 UTC (heure lue sur `date -u` : 15:04:13). Source :
branche `donnees/pole-lancement-reel-a-v1`, commit `3fe792f`, versée par session-depot (lancement sous GO-2026-10-27-05,
orchestrateur v6 au commit `0b9efe2`, sans modification). Empreintes de la sortie vérifiées : `EMPREINTES-v1.txt`
(`500f8a96…`), aucun écart. Fichiers lus : `course/bilan.json` (`f6fd36fb…`), `course/journal/generation-00.json`
(`c2905dc9…`) et `generation-01.json` (`b1ad740f…`), `RELAIS.jsonl` (`7228f9f5…`), les leçons de la génération 0
(`course/archive/generations/generation-00/synthese/lecons.json`, `06c17bac…`), les dossiers d'expérience et de
vérification, `LISEZMOI-v1.md` de session-depot (`045b18ba…`). Les « questions à lire » sont celles fixées avant la
dépense, section 5 du devis (`devis-premier-lancement-reel-v1.md`).

## Verdict

1. **La plomberie réelle tient** : 140 appels, 6,24 USD, aucun refus du relais, coûts déclarés par rôle égaux aux coûts
   du relais au cent près ; génération 0 : 8 fiches traitées sur 8, ordre imposé suivi 8 sur 8 (issues identiques aux
   dépôts du noyau), le vérificateur a rejoué et confirmé 5 fois sur 8, le témoin faux jugé a été éliminé.
2. **La course n'a pas éprouvé la méthode.** La génération 1 est perdue entière : 5 fiches sur 5 en « erreur de
   l'orchestrateur ». Cause, que le LISEZMOI ne relève pas : une **leçon écrite par l'agent de synthèse** (« toujours
   écrire reponse.txt ») a fait écrire aux expérimentateurs le fichier que l'orchestrateur se réserve ; l'écriture de
   l'orchestrateur a alors buté sur l'interdiction d'écraser. **Aucun témoin vrai n'a été jugé** (0 sur 3) : les dents ne
   sont pas mesurées. Le bilan affiche pourtant « témoins vrais testés 3, éliminés 0 » : chiffre flatteur (R4).
3. **Huit défauts, tous de mon code, aucun de fond, tous corrigeables sans dépense.** Je les corrige dans v7 (version 5)
   avant toute couche avec de vrais agents. La condition (i) de la porte P3 (« (a) passé sans incident de plomberie »)
   **n'est pas remplie** : je propose une course de contrôle « (a) bis » sur v7 corrigé (≈ 6 à 8 USD, plafond 15).

## 1. Les questions fixées avant la dépense (devis, section 5)

| question | réponse |
|---|---|
| fiches traitées sans erreur | génération 0 : 8 sur 8 ; génération 1 : **0 sur 5** (`EcrasementInterdit` sur `experience/reponse.txt`) |
| ordre imposé suivi | 8 sur 8 : issues déclarées identiques aux issues déposées par le noyau ; empreinte d'ordre recalculée par le vérificateur dans 4 des 5 vérifications confirmées (la cinquième la dit « cohérente ») |
| accords et désaccords | 5 confirmations après rejeu (`python3 -I`), 3 désaccords, **tous de plomberie** : rejeu bloqué par la garde des outils (2), vérification interrompue sans conclusion (1) ; aucun désaccord de fond |
| témoins | faux : S-F4 jugé et éliminé ; S-F1 en erreur. Vrais : **aucun jugé** ; S-V1 indécis en génération 0 faute de rejeu, en erreur en génération 1, puis **retiré** ; S-V4 en erreur |
| coût réel par rôle | expérimentateurs (Opus 5.5) 1,33 USD pour 8 fiches (0,17 par fiche) ; vérificateurs (Fable 5.1) 4,06 USD pour 8 (0,51 par fiche) ; recombinaison et synthèse 0,11 ; génération 1 : 0,74 USD sans aucun verdict |
| temps par génération | génération 0 : 14:34:34 à 14:38:23 UTC (≈ 3 min 50 s, concurrence 4) ; génération 1 : ≈ 1 min 50 s |
| incidents de la garde des outils | deux vérifications bloquées par des faux positifs (« /len », « /120 », « ~ », puis « set ») ; une écriture hors du dossier refusée à juste titre |

Rien de scientifique n'était attendu (monde tautologique) : les deux survivantes (G0-F05, G0-F07, log W 74,6 et 77,7)
disent seulement que le calcul de la richesse tourne.

## 2. Dans l'autre sens : ce que la sortie montre et que le bilan ne dit pas

1. **Génération 1 perdue, par la mémoire.** En génération 0, le vérificateur de G0-F08 s'est plaint que `reponse.txt`
   manquait dans son dossier (c'est voulu : il ne voit pas la réponse de l'expérimentateur). L'agent de synthèse en a tiré
   la leçon « toujours écrire reponse.txt », injectée dans la consigne de chaque expérimentateur de la génération 1. Les
   cinq l'ont suivie ; l'orchestrateur, qui écrit sa propre trace sous ce nom sans jamais écraser, a levé l'erreur après
   chaque expérience. **Défaut 1** : l'orchestrateur partage ses noms de fichiers avec l'agent ; ses invariants dépendent de
   l'obéissance de l'agent. C'est exactement le risque des canaux de texte de la pièce 6 (une leçon est un texte d'agent
   qui devient une consigne).
2. **Défaut 2 — une erreur de l'orchestrateur compte comme un essai.** G0-F02, G0-F03 (le témoin vrai S-V1) et G0-F08
   sont **retirées** après deux « essais », dont le second est l'erreur. Une fiche ne doit jamais perdre sa chance par la
   plomberie.
3. **Défaut 3 — la mesure de qualité flatte.** Elle compte comme « testé » un témoin indécis ou en erreur, et ne mesure que
   les vraies éliminées, jamais les vraies promues. S-V1 est compté deux fois (génération 0 et sa remise en jeu). Le signal
   « pas de dents » de v7 a le même trou : il ne s'allume que si tous les témoins vrais sont **éliminés**, pas s'ils ne
   sont jamais jugés.
4. **Défaut 4 — double règlement du budget.** Quand l'erreur survient après l'expérimentateur, sa réservation est libérée
   deux fois (le coût était réglé, la trace de coût est perdue avec l'issue). En génération 1 : environ 5 USD de marge
   fantôme. Aucun dépassement réel (le plafond du relais tient), mais le plafond de génération n'est plus sûr après une
   erreur ; le coût par fiche de la génération 1 est perdu du journal.
5. **Défaut 5 — la consigne du vérificateur est ambiguë sous la sélection par pari.** Deux vérificateurs ont refusé de
   confirmer faute de « verdict chiffré » (la richesse), que le noyau calcule après eux par construction. Et le dossier de
   vérification reçoit des empreintes orphelines (`consigne.txt.sha256`, `reponse.txt.sha256` de l'expérimentateur) : les
   compagnons des fichiers exclus du rejeu ne sont pas exclus ; le vérificateur de G0-F08 l'écrit (« seules leurs
   empreintes sont fournies »).
6. **Défaut 6 — faux positifs de la garde des outils.** Le code Python passé par une redirection `<<EOF` est lu comme du
   shell : `sum(t)/len(t)` y devient le chemin `/len`, `(k+1)/120` le chemin `/120`, `set(x)` la commande `set` sans
   argument, `(~m)` le dossier personnel ; et `python3 -c "… / …"` (division entourée d'espaces) devient la racine `/`. Les
   commandes réelles des vérificateurs ne sont pas dans la sortie ; ces quatre motifs, et le cinquième, sont reproduits à
   l'identique par la garde v7 sur des commandes typiques. Les vérificateurs ont dépensé leur budget à la contourner.
7. **Défaut 7 — bac à sable inactif, et c'est plus grave qu'une réserve.** Le chemin `/tmp/claude-0/…` indique que la
   session tourne sous l'utilisateur 0 (root) ; les agents, lancés par l'orchestrateur, aussi. Sans bac à sable, un agent
   peut en principe lire l'environnement d'un autre processus du même utilisateur, donc la clé du relais ; la garde des
   outils n'est qu'une barrière par motifs (une commande obscurcie la franchit). **Aucune course réelle de plus sans bac à
   sable actif** : v7 refusera de partir si `bwrap` et `socat` manquent ou si `bwrap` ne s'exécute pas.
8. **Défaut 8 — réserve du relais par appel inférieure au coût maximal d'un appel** (0,266 USD contre 0,25) : le plafond
   peut être dépassé d'au plus (coût maximal − réserve) × concurrence, ici moins de 0,07 USD. Correction : réserve calculée
   depuis la requête (`max_tokens` × prix de sortie, plus une borne d'entrée).

Deux constats qui ne sont pas des défauts :
- **La mémoire a refusé la seule fille** (G0-F05 × G0-F07, trop proche de G0-F07 : divergence 0,287, « réplication, jamais
  une découverte ») ; puis la recombinaison s'est abstenue (paire déjà fusionnée). Sans proposeur, la population s'épuise
  en une génération : c'est la raison d'être du proposeur de v7.
- **Le vérificateur coûte trois fois l'expérimentateur** alors que, dans un monde tenu par le noyau, il ne fait que
  rejouer une copie. Les témoins jugés sans agents (v7) suppriment ce coût pour les témoins ; pour les autres fiches d'un
  tel monde, un vérificateur Opus 5.5 suffirait (à décider ; ce n'est pas une correction).

## 3. Corrections (v7, version 5 ; sans dépense)

| défaut | correction | essai |
|---|---|---|
| 1 | traces de l'orchestrateur (consignes, réponses) dans un dossier voisin que l'agent ne peut pas écrire ; consigne : « ta réponse est ton dernier message » | un agent simulé qui écrit `reponse.txt` ne casse plus rien |
| 2 | une erreur de l'orchestrateur ne compte pas comme un essai ; la fiche reste rejouable, motif écrit | erreur forcée deux fois : jamais « retirée » |
| 3 | qualité : témoins jugés par le pari, vraies promues (puissance), témoins en erreur à part ; trois états « dents », « pas de dents », « dents non mesurées » | témoins indécis : « dents non mesurées » |
| 4 | l'issue garde ses coûts même en erreur ; un seul règlement par réservation | erreur après l'expérimentateur : budget exact |
| 5 | consigne du vérificateur : pas de verdict chiffré à confirmer sous le pari ; compagnons exclus du rejeu | dossier de vérification sans empreinte orpheline |
| 6 | la garde sépare le code (redirections `<<EOF`, `python -c`) du shell ; dans le code, seuls les littéraux de chaîne sont lus comme des chemins | les commandes fautives de (a) passent ; `open('/etc/passwd')` dans le code reste refusé |
| 7 | refus de partir en moteur réel sans `bwrap` et `socat` qui fonctionnent | sain et artefact |
| 8 | réserve du relais calculée depuis la requête | appel à `max_tokens` élevé : réserve suffisante |

**Course de contrôle proposée, « (a) bis »** : v7 corrigé, même monde tautologique, deux générations, témoins avec agents
(pour éprouver le vérificateur), bac à sable actif ; lecture : les huit questions ci-dessus, plus « aucune erreur de
l'orchestrateur » et « au moins un témoin vrai jugé ». Dépense attendue 6 à 8 USD, plafond 15. C'est la condition (i) de
P3. Décision chez session-depot, sur le go anticipatoire de Lazar.
