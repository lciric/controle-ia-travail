# Contre-lecture : lanceur de l'organisme d'idéation pour la lignée Kimi (v9), sa commande et son enveloppe (v1)

Contre-lecteur neuf (sous-agent, n'a rien écrit de ce qu'il lit), 18 novembre 2026. Lecture seule. Aucun appel réseau, aucune
course, aucun relais lancé. Les fonctions du lanceur ont été appelées en mémoire seulement (`python3 -I -B`, import du module,
aucune écriture) pour recalculer la commande, les sommes et les gardes de taille.

Pièces lues :

- `scripts/lancer_course_ideation_organismes_discrets_v9.py` (sans compagnon `.sha256` à ce jour), comparé au
  `lancer_course_ideation_organismes_discrets_v8.py` (`87fb4fec…`, égal à son compagnon) ;
- `docs/notes/ideation-organisme-v1/relais-kimi-v1/commande_kimi_ideation_v1.py` (`5f6c0f27…`, égal à son compagnon),
  comparée à `commande_astra_v1.py` (`986cf71e…`, égale à son compagnon) ;
- `rapports/organismes-discrets-v1/enveloppes-v1/appel-kimi-v1.sh` (`6f006d03…`, égal à son compagnon), comparée à
  `appel-astra-v1.sh` (`aa2df474…`, égal à son compagnon) ;
- l'orchestrateur cloné `/home/user/lciric/ideation-organism/orchestrator` : tête `a41b7b50…`, arbre de `orchestrator/` égal à
  `ee84d6ec…` (la valeur épinglée par le lanceur) ; `pole/adaptateurs.py`, `demonstrations/ideation_v2.py`,
  `demonstrations/ideation_v8.py`, `pole/ideation_v2.py`, `pole/relais.py` égaux aux empreintes épinglées ;
- `relais_kimi_v4.py` ; `devis-course-2-et-pre-pilote-v4.md` (`03e961d5…`) ligne 36 ;
  `devis-ideation-organismes-discrets-lignee-kimi-v1.md` (`9f8f01c9…`) ; documentation de Moonshot versée le 30 octobre
  (`doc-moonshot-lue-2026-10-30-v1/api_chat.md`) ; `LISEZMOI-relais-kimi-v4.md` ; journaux des relais Kimi déjà joués
  (quatre dossiers `docs/notes/*/relais-v1/journal-relais-kimi*.jsonl`) ; relevés des quatre courses du v8.

## Verdict

**À corriger.** Aucun constat bloquant : les bornes de dépense tiennent, l'orchestrateur épinglé admet la commande produite, le
modèle servi est contrôlé, les prix sont sourcés. Quatre constats significatifs : la garantie du verrou commun annoncée dans
l'en-tête est fausse ; avec les délais actuels, la sortie maximale de 98 304 jetons ne peut pas être atteinte ; une trace
« 34 USD pour trois lignées » serait scellée dans chaque manifeste de pré-départ ; les essais annoncés n'existent pas.

## Constats

### Significatifs

1. **Le verrou n'est pas commun aux deux lanceurs.** Fichier `scripts/lancer_course_ideation_organismes_discrets_v9.py`,
   l. 20 (en-tête), l. 230 et l. 1227. Le nom `NOM_VERROU` est bien celui du v8, mais le fichier de verrou est ouvert dans
   `r.dossier_sorties / NOM_VERROU`, et `DOSSIER_SORTIES` est propre au v9 (l. 227). Le verrou du v9 est donc
   `/home/user/sorties-course-ideation-organismes-discrets-v9/.verrou-lanceur-organismes-discrets-v8`, un autre fichier que
   celui du v8 (`…-v8/.verrou-…-v8`). Même avec un fichier commun, la garantie resterait fausse : le verrou ne couvre que la
   fenêtre allant de la lecture de l'état au manifeste de départ, et la vérification « course en marche » (l. 1250-1255) ne lit
   que la série de runs du v9 (`runs_du_lanceur`, l. 879). Une course du v8 en marche n'empêche donc pas le départ d'une course
   du v9. L'effet est nul aujourd'hui, car le v8 ne peut plus rien lancer : Carbon a ses deux courses (relevés 1,530326 et
   1,530326 USD), Astra et Argon ont produit des fiches (relevés 1,342677 et 1,127553 USD). La somme reste aussi bornée par le
   plafond du relais Claude (22 USD selon le devis Kimi, § 3). Mais l'en-tête affirme une propriété de sécurité qui ne tient
   pas. Correction : retirer l'affirmation et écrire ce qui tient (le v8 est épuisé, avec ses relevés en appui ; le relais
   Claude borne la somme), ou bien lire aussi les runs du v8 et prendre le verrou au chemin du v8, ce qui est plus lourd et
   n'apporte rien tant que le v8 est épuisé.

2. **La sortie maximale de 98 304 jetons est hors de portée avec les délais en place.** Fichiers concernés : l'enveloppe
   `appel-kimi-v1.sh`, l. 15-16 et 24-26 (`--delai-s 1500`, `timeout -k 20 1700`, `--max-sortie-jetons 98304`) ; la commande
   `commande_kimi_ideation_v1.py`, l. 92 et l. 158-177 ; l'orchestrateur (`--delai-commande-s`, 1800 s par défaut,
   `demonstrations/ideation_v2.py` l. 616) ; le relais (`--delai-amont-s`, 1800 s par défaut, `relais_kimi_v4.py` l. 192) ;
   le devis Kimi, § 5, risque 1.
   - Le relais ne renvoie rien à la commande avant la fin de la génération : la connexion locale reste muette, et la commande
     lève `TimeoutError` à 1500 s (code 6, coût compté au pire cas).
   - Débit observé de Kimi sur les 13 appels des journaux versés : de 24 à 35 jetons par seconde. Par exemple, 25 964 jetons
     en 1 016,6 s (`docs/notes/collisionneur-bassins-etroits-v1/relais-v1/journal-relais-kimi-v1.jsonl`, première ligne) et
     16 384 jetons en 463,2 s (`docs/notes/collisionneur-conception-qo1-q1-v1/relais-v1/journal-relais-kimi-v1.jsonl`).
     En 1500 s, cela fait environ 36 000 à 53 000 jetons.
   - Conséquence : un appel qui raisonne au-delà d'environ 1500 s ne finit plus en `finish_reason = length`, qui donnait le
     code 5, environ 0,33 USD à l'usage et un relais qui lit l'usage. Il finit en délai dépassé : code 6, sans texte, coût
     compté au pire cas (environ 1,01 USD par appel avec ces consignes ; le relais continue de lire l'amont jusqu'à 1800 s).
   - Le budget reste borné : le coût compté ne dépasse pas le plafond de session (1,5 et 1,7 USD), et la relance reste
     permise après un arrêt au contrôle (1,7 + 0,2 ≤ 2,1). Ce qui ne tient pas, c'est le but affiché (« le plafond de session
     borne le reste »). En réalité, c'est le temps qui borne, et de façon plus chère.
   - Corrections possibles :
     - (a) ramener la sortie maximale à ce que 1500 s permettent (environ 40 000 jetons), en le disant ;
     - (b) relever les délais de façon cohérente, avec commande < enveloppe < orchestrateur et relais ≥ commande. Par exemple :
       `--delai-s 3300`, `timeout 3500`, `--delai-commande-s 3600` passé par le lanceur (ce drapeau n'est pas interdit), et le
       relais lancé avec `--delai-amont-s 3400`. À 30 jetons par seconde, 98 304 jetons demandent environ 3300 s ;
     - (c) régler `reasoning_effort` (« max » par défaut selon `LISEZMOI-relais-kimi-v4.md` l. 59). Cela demande une commande
       neuve, sous un nouveau nom (R12).
   - Recommandation : (b), ou à défaut (a). Dans les deux cas, corriger le risque 1 du devis.

3. **Trace oubliée, scellée dans chaque manifeste de pré-départ.** Fichier du lanceur v9, l. 1298-1299 : `"decision": "mots de
   Lazar du 18 novembre 2026 (relance, composition A, go dépenses par anticipation) ; ligne de GO trouvée par son contenu ;
   pire cas et borne 34 USD pour trois lignées"`. Ce texte est écrit dans `manifeste-lanceur-pre-depart.json` de chaque course
   Kimi. Il contredit la borne de 11,3 USD et cite une autre base de décision que celle de la lignée Kimi (« oublie pas kimi
   dans les courses », ligne de GO « lignée kimi »). Le diff ne l'annonce pas et l'en-tête ne la couvre pas. À réécrire.

4. **Les essais annoncés n'existent pas, et le lanceur n'est pas scellé.** Fichier du lanceur v9, l. 29 : « Essais :
   `tests/test_lancer_course_ideation_organismes_discrets_v9.py` ». Ce fichier est absent (seul le
   `test_lancer_course_ideation_organismes_discrets_v8.py` existe). Aucun essai non plus pour la commande Kimi, alors que la
   commande Astra a `test_commande_astra_v1.py`. La branche neuve `famille == "kimi"` (l. 711-713) et `plancher_kimi`
   (l. 697-701) ne sont testées nulle part (R5 : chaque garde testée sur un cas sain et sur un artefact). Le v9 n'a pas
   encore de compagnon `.sha256` : `verifier_soi` (l. 400-402) refuse tout lancement, ce qui est sûr, mais le lanceur ne
   pourra être scellé qu'après ces essais. Le contrôle fait ici en mémoire tient : commande recalculée ; sommes 4,2 ≤ 6,
   5,9 < 6,5 et exposition 9,2 ; gardes de taille sur la mesure réelle des courses v8 (consignes 11 560 / 11 085 caractères)
   avec planchers Kimi de 0,0696 / 0,0685 USD sous 1,7 / 1,5. Il ne remplace pas les essais.

### Mineurs

5. **Autres traces « trois lignées »** dans le lanceur v9 :
   - l. 166 (commentaire « devis v3 de cette course : trois lignées ») ;
   - l. 424-425 (docstring de `verifier_go` : périmètre « trois lignées », alors que le code lit `PERIMETRE_GO`, qui est juste) ;
   - l. 1216 (rappel du bilan : « les trois lignées se lisent ensemble ». Ce rappel est scellé dans le manifeste de fin, et il
     y a désormais quatre lignées).

   À réécrire en même temps que le constat 3.

6. **La commande du relais donnée dans l'en-tête est incomplète.** Lanceur v9, l. 26-27 ; commande Kimi, l. 8-9. Il y manque
   `--plafond-usd`, `--prix-entree`, `--prix-sortie` et `--prix-cache`, que `relais_kimi_v4.py` exige (l. 1039-1043 : sans
   eux, il refuse de démarrer avec le code 2, ce qui est sûr). Le devis Kimi (§ 3) donne les valeurs : plafond 5 USD,
   12 appels, prix 2 / 10, cache 2. Les reporter dans l'en-tête, avec `--delai-amont-s` (voir le constat 2). Le plafond de
   5 USD couvre les réservations au pire cas : environ 1,01 USD par appel, soit 4 appels pour une course et sa relance.

7. **Erreur 502 du relais.** Commande Kimi, l. 168-173. Sur un 502, y compris le 502 « modèle servi différent » de la
   barrière du relais, la commande rend le code 5 **sans** clé `modele_servi`. Avec un code non nul, l'orchestrateur appelle
   `controle_modele(…, seulement_si_dit=True)` (`pole/adaptateurs.py` l. 690). La ligne est donc lue comme une erreur
   ordinaire, pas comme un refus : le coût est compté au pire cas, aucun texte n'est servi, et
   `depense_modele_non_autorise_usd` reste à 0, alors que le corps du 502 porte `modele_servi`. Le comportement est identique à
   celui de la commande Astra, déjà jouée. C'est une information, pas un défaut à corriger ici.

8. **Prix.** Les prix 2 / 10 sont sourcés (`devis-course-2-et-pre-pilote-v4.md` l. 36 : page lue le 30 octobre, `c62210a0…`,
   observée conforme à la facture). L'écriture de cache à 5 minutes coûte 2,00 USD par million (`LISEZMOI-relais-kimi-v4.md`
   l. 58-59) : compter toute l'entrée à 2 est donc bien une borne haute. Ces prix ont 19 jours, alors que ceux d'Astra ont
   été relus le 14 novembre. La relecture n'est pas exigée, mais il faut le dire.

9. **Sortie maximale par défaut de la commande.** La commande Kimi garde `--max-sortie-jetons 32768` par défaut (l. 90),
   alors que l'enveloppe impose 98 304 après `"$@"`. C'est cohérent (l'enveloppe l'emporte), mais l'en-tête de la commande
   pourrait le dire.

10. **Estimation du devis Kimi (§ 4).** Le devis attend environ 0,1 USD pour Kimi. Les appels Kimi déjà journalisés coûtent de
    0,20 à 0,29 USD chacun, avec 12 000 à 26 000 jetons dont la majorité en raisonnement. Pour deux appels (contrôle et
    passe 1), il faut plutôt compter de 0,4 à 0,6 USD. La borne de 11,3 n'est pas touchée.

11. **Ligne de GO à venir.** Son périmètre ne doit pas contenir « trois lignées » : sinon le `verifier_go` du v8 trouverait
    deux lignes candidates. Ce serait sans effet tant que le v8 est épuisé, mais c'est une précaution d'écriture.

## Ce qui a été vérifié et tient

- **Diff v8 → v9.** Seuls les changements annoncés, plus les traces des constats 3 et 5 : en-tête, `VERSION`, `LIGNEES`,
  `PERIMETRE_GO`, pire cas et borne 11,3, `COMMANDE_KIMI` et son empreinte, `LIGNEES_EXTERNES` (kimi seul), `PIECES` et
  `PLAFONDS` de référence, prix Kimi, dossier de sortie, série et suffixe de runs v9, `NOM_VERROU` (constat 1), défaut
  `lignee`, `plancher_kimi` et la branche « kimi ». Aucune référence à Carbon, Astra ou Argon ne pèse sur la lignée Kimi :
  `COMMANDE_GEMINI`, `COMMANDE_ASTRA` et les constantes `GEMINI_*` / `ASTRA_*` restent définies sans être servies. La
  formule de taille de la commande Astra (octets × 1,15 + 1024, sortie minimale 4096) est bien la formule de la commande Kimi.
- **Diff de la commande Astra → commande Kimi.** Seulement l'en-tête, `VERSION` et les quatre défauts (port 8789, modèle
  `kimi-k3.1-pro`, prix 2 / 10).
- **Diff de l'enveloppe Astra → enveloppe Kimi.** Seulement l'en-tête, le chemin de la commande, le message d'absence, le port
  8789, le modèle, les prix 2 / 10 et la sortie maximale 98 304. Pas de collision de port avec le relais Gemini (8788) ni avec
  le relais Astra (8790).
- **Garde de cumul et relance** (lanceur v9, l. 1042-1076).
  - Première course : 0 + 9,2 ≤ 11,3.
  - Relance après un arrêt au contrôle : 2,1 + 9,2 = 11,299999999999999, qui passe sous 11,3 + 1e-9.
  - Après une course pleine, la relance est refusée deux fois : par `relance_permise` (relevé au-dessus de 2,1, ou fiches
    produites) et par la garde de cumul (9,2 + 9,2 > 11,3).
  - Au plus deux courses. Le plafond du GO doit être ≥ 11,3 (l. 462).
- **Plafond du proposeur externe face au pire cas de la commande** (commande Kimi, l. 103-154). La commande **réduit** la
  sortie à min(98 304, ce que paie le plafond) et ne **refuse** sans envoi (code 4, `envoye: false`) que si la sortie tombe
  sous 4096 jetons. Avec un plafond de 1,5 USD et un corps d'environ 12,9 ko, la réduction ne mord pas : n = 98 304, pire cas
  d'environ 1,01 USD, sous 1,5 et sous 1,7 pour le contrôle. Le juge externe différé (2,5) est déclaré et jamais joué ; il
  entre dans la somme externe (5,9 < 6,5).
- **Admission par l'orchestrateur épinglé** (`demonstrations/ideation_v2.py` l. 751-790). `--modele-commande-externe
  kimi-k3.1-pro` diffère d'Argon, mais `--commande-externe-lit-modele` est présent, donc il est admis. Le modèle attendu est
  `kimi-k3.1-pro`, et les modèles du proposeur `kimi=kimi-k3.1-pro` et du juge `kimi-juge=kimi-k3.1-pro` lui sont égaux :
  aucun écart. Pas d'expérimentateur. `exiger_modele_servi` est vrai sous le moteur réel (l. 746-748).
- **Modèle demandé et modèle servi** (commande Kimi).
  - `MODELE_DEMANDE_POLE` est lu (l. 130-132 ; écart → code 2, rien envoyé).
  - En cas de succès, `modele_servi` est rendu (l. 193). Un modèle servi différent ou absent donne le code 5 avec
    `modele_servi` (valeur ou `null`), lu comme refus (`commande.modele_servi` ou `commande.modele_servi_absent`).
  - Les journaux montrent `model` = `kimi-k3.1-pro` exactement, et la documentation le confirme (`api_chat.md` l. 236).
- **Relais v4.**
  - Il lit l'amont en flux : il ajoute `stream: true` et `stream_options.include_usage` (l. 720-732) et réassemble le flux
    (`lire_flux`, l. 549-610). Le client reçoit une réponse entière, sans flux.
  - Il accepte `max_completion_tokens`, transmis tel quel et lu pour son pire cas (l. 363-371). La documentation de Moonshot
    donne ce champ comme courant, avec un maximum de 1 048 576 pour `kimi-k3.1-pro` (`api_chat.md` l. 1077-1094).
- **Prix 2 / 10.** Sourcés à la ligne 36 du devis de la course 2, version 4, empreinte égale à son compagnon.
