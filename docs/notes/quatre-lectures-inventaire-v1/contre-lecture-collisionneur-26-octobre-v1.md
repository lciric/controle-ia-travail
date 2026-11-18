# Contre-lecture de la note sur les deux tours du collisionneur du 26 octobre (intégration de l'explorateur de neurones, et « déjà propre ») (v1)

- **Écrit** le 18 novembre 2026 vers 05:10 UTC (`date -u` : 2026-11-18T05:06:37Z en cours de rédaction) par un sous-agent contre-lecteur neuf (Claude Opus 5.5), qui n'a pas écrit la note (règle R2), sur une consigne calculée par le script de la mère, sous l'autonomie GO-2026-11-18-05 et le « go » de Lazar aux quatre lectures sans dépense de l'inventaire (R-3168, R-3170).
- **Note contre-lue** : `docs/notes/quatre-lectures-inventaire-v1/collisionneur-26-octobre-v1.md`, sha256 `dac5edd116f43af0fb2b8980059999b6b11314ddce1428640464a69c98a7bbfe` (recalculé, égal au compagnon `.sha256`). Non modifiée.
- **Cadre tenu** : aucune dépense, aucun appel de modèle, aucune clé lue ni affichée, aucun commit, aucune poussée, aucun `git fetch` ; rien sous `diag/` ; aucune branche `calcul/` ni `donnees/` ouverte ; seuls les extraits préparés par la mère ont été lus, sous `…/scratchpad/quatre-lectures/extrait/collisionneur-neuron-explorer-v1/` (branche `donnees/collisionneur-neuron-explorer-v1`, commit `191a658`) et `…/extrait/collisionneur-already-clean-v1/` (branche `donnees/collisionneur-already-clean-v1`, commit `08e6b31`). Au dépôt : `docs/notes/lecture-voisin-neuron-lens-v1.md` (`12c8f673e4141168…`), `docs/notes/weight-space-programming-v1/piece-3-lecture-factuelle.md` (`fff05896def645d0…`), `docs/notes/inventaire-collisionneurs-organismes-v1/inventaire-v1.md` (`b49dc2462382206d…`), `registres/decisions.md` lignes 701, 702 et 707.
- **Cloisonnement du contre-lecteur** : aucune des 66 plages exclues par la note n'a été affichée ; leurs tailles ont été recalculées par un script qui compte les octets sans rien imprimer (`/tmp/claude-0/-home-user-controle-ia-travail/8282ab93-0983-5813-b791-a7a522157dcd/scratchpad/taille_excl.py`, hors du dépôt). Je n'ai donc pas pu juger si ces plages relèvent bien de la famille 2 ; je juge seulement que la note n'en reprend rien.

## Verdict : à corriger

La note est solide : ses empreintes, ses coûts, ses espèces et l'immense majorité de ses renvois (fichier, ligne, espèce) sont exacts ; aucun avis n'est présenté comme un fait, aucun chiffre de l'état de l'art comme vérifié, aucune zone vierge comme un trou ; rien d'une famille exclue n'y est résumé. Six corrections de fait, toutes mineures, et une réserve de cloisonnement. Comme toutes sont de fait, j'ai écrit la version 2 : `docs/notes/quatre-lectures-inventaire-v1/collisionneur-26-octobre-v2.md`.

## Corrections (liste exacte)

1. **Attribution trop large, section 5.1, question 7.** « Les trois espèces pensent que la différence des moyennes écrit mieux » ; seuls C (explorateur T1-C l. 113) et B (explorateur T1-B l. 68) le disent, tous deux en renvoyant à Marks et Tegmark « à vérifier ». A ne le dit dans aucune de ses cellules (recherche de « moyennes » dans les trois cellules de A du tour « explorateur » : seulement T3-A l. 17, 27, 111, sur un autre point). → « B et C ».
2. **Attribution trop large, section 5.2.** « Les trois espèces le rappellent » (la poussée reste une mesure au sens de N-015) avec deux renvois seulement (explorateur T1-B l. 80, qui est B ; déjà propre T1-A l. 49, qui est A). C cite N-015 dans un autre sens : abandonner toute intervention par poussée de sonde (déjà propre T1-C l. 136 ; T3-C l. 177). → « A et B ».
3. **Proportion fausse, réserve d'honnêteté des exclusions.** « La famille 2 y occupe environ un dixième du texte des cellules » (« déjà propre »). Recalcul sur les plages de la note : 43 371 octets sur 231 068, soit environ 19 % ; pour l'explorateur 33 015 sur 232 416, environ 14 %. Les 66 tailles de passage annoncées sont, elles, toutes exactes.
4. **Plage qui englobe une ligne exclue, section 2.** Riposte de A au tour « explorateur », « l. 17-47 », alors que la ligne 35 est exclue par la note elle-même. Le résumé (« elle accepte presque tout ») ne décrit pas cette ligne ; la plage devient « l. 17-34 et 36-47 ».
5. **Coût de C compressé, section 6.** « 125 à 1 200 USD selon C (T1-C l. 128-129) » fond deux scénarios distincts de C : environ 125 USD sur amorces courtes (l. 128), 600 à 1 200 USD sur transcriptions longues (l. 129), tous deux « illustratifs ».
6. **Oubli mineur, sources.** `LISEZMOI-v1.md` du tour « explorateur » décrit quatre lanceurs ; la note ne cite que le départ v1. Le lanceur v2 a échoué sans dépense, le v3 n'a jamais été lancé. La réponse du départ v1 est un fichier de 0 octet (« n'a rien produit » est donc exact).

## Réserve de cloisonnement (non corrigée sur le fond, signalée dans la version 2)

- **Déjà propre, conception de B, ligne 314**, utilisée par la section 5.3 (troisième leçon pour le papier B : « rapporter la distribution entière des tirages »). Cette ligne est un élément de liste qui suit immédiatement la ligne 312, exclue, et se trouve dans la section « Point 5 » de B, dont les lignes 295-301 sont exclues. Le passage exclu est, selon la note, la réponse à l'option « maximum à l'aveugle comme opération de la primitive ». La ligne 314 énonce une règle de statistique générale (sélection sur le bruit) et ne décrit aucun mécanisme d'évasion ; je ne l'ai pas classée comme exclue, mais je n'ai pas pu confirmer, sans lire les lignes exclues, qu'elle n'appartient pas à la même réponse. La mère peut préférer appuyer la leçon sur les seules autres sources citées (explorateur T1-A l. 72 ; T1-B l. 112-114).
- Deux autres lignes voisines de passages exclus ont été rouvertes et me semblent sans contenu exclu dans ce que la note en tire : déjà propre T1-C l. 22 (C : un épiphénomène reste un signal d'alerte valide ; la suite de la ligne, que je n'ai pas lue en entier, jouxte la ligne 23 exclue) ; explorateur T3-C l. 71 (agent explorateur et vrais neurones dans l'épreuve en aveugle, jouxte 72-74). Le « couple minimal » de C (explorateur T1-C l. 150) sert, chez C, à valider une explication dans la boucle extérieure ; je ne le classe pas en famille 2.

## Ce que j'ai vérifié, et comment

### (1) Citations

- **Empreintes** : les dix-huit cellules ont été recalculées ; chacune est égale à son `essais/*.essai1.reponse.md` et à son compagnon `.sha256`, et les seize premiers caractères sont ceux de la note. Questions : `2ba899ddef82d21e…` (identique dans les deux dossiers de course) et `252f4922920defad…` (égale à celle citée par R-483, ligne 707). Lecture par lentille neuronale : `12c8f673e41411683…`, exact.
- **Espèces et coûts** : `LISEZMOI-v1.md`, `etat.md`, `journal-etage3-v4.txt` et `journal-etage3-v1.txt` donnent A = `claude-fable-5-1`, B = `claude-opus-5-5`, C = `gemini-4-argon`, 9 cellules sur 9, 6,25 USD (02:38:27 à 03:05:38 UTC) et 6,31 USD (02:43:07 à 03:10:51 UTC). Exact.
- **Renvois aux cellules, rouverts un par un (95)**. Tous exacts sur le fond, sauf les numéros 1, 2 et 5 ci-dessus :
  - explorateur T1-A l. 25, 72, 134-137 ; T1-B l. 14-29 (quatorze présupposés a1 à a14), 22 (1/257, environ 56 faux positifs pour 14 336 neurones), 51, 60, 68, 80, 155, 169, 184 ; T1-C l. 112-113, 128-129, 150 ; T1-A, structure des sept duels E1 à E7 (titres l. 39 à 89).
  - explorateur T2-A l. 17, 44-45, 57, 59, 98-99, 113 ; T2-B l. 20-24, 80-83, 145 ; T2-C l. 17-18, 69-71.
  - explorateur T3-A l. 17, 19, 29, 117 ; T3-B l. 19, 20, 21, 24, 28, 32, 40, 41, 43, 50, 88, 116, 143-151, 161-162, 213-216 ; T3-C l. 10-12, 23, 26, 58, 71, 84, 85, 102-104, 106-108, 145.
  - déjà propre T1-A l. 13, 19, 49, 111, 119 ; T1-B l. 26, 71, 75, 97-100, 109, 119-123, 204, 284, 314 ; T1-C l. 22, 117, 133-134, 167 ; T2-A l. 63, 114 ; T2-B l. 7-11, 19-24, 77, 108, 189 ; T2-C l. 75-76 ; T3-A l. 25, 65, 77-82 (rappel exigé d'au moins 80 %, l. 81), 123 ; T3-B l. 47, 104-106, 219-220 ; T3-C l. 101-104, 177.
- **Renvois aux questions** : explorateur, demandes l. 57-79, licence non trouvée l. 37 ; déjà propre, organisme et question M l. 48-55, demandes l. 65-87, chiffres de l'essai l. 16-18, 28-31, 32-35 (183 neurones, 76 %, 11 %, « < 2 % », « −0,004 nats »). Exacts.
- **Renvois au dépôt** : lecture par lentille neuronale l. 89, 111 (« 200 neurones », « 5 % nets », pages du PDF), 130, 149, 156, 158, 172, 175, 181, 197, 199 (ligne « H6 », sans l'explorateur ; aucune occurrence de « explorer » ni de « collisionneur » dans tout le fichier), 201 ; `piece-3-lecture-factuelle.md` l. 199 cite bien le dépôt `neuron-explorer` ; inventaire lignes 40-41 (tableau A.1), 133 (section B, point 1), 160 (section E, nœud 1). Exacts. L'observation de la note sur le renvoi « l. 199 » de l'inventaire est juste.
- **Chevauchements** : j'ai confronté par programme chaque renvoi de la note aux 66 plages exclues. Le seul chevauchement est la plage large de la correction 4.

### (2) Statut des affirmations

- **Avis contre faits** : chaque proposition des sections 2 à 4 est attribuée à une espèce, avec cellule et ligne ; les jugements « neuf / partiel / raffinement » sont présentés comme ceux du rédacteur et comme des questions pour la mère (section 4, préambule). Les seuls écarts sont les deux attributions trop larges (corrections 1 et 2), qui prêtent un avis à une espèce qui ne l'a pas donné.
- **Règle R7** : les références de littérature (Elazar et al., Ravichander et al., Heap et al. 2025, Paulo et al. 2024) sont dites « non vérifiées » ou « à vérifier » ; les chiffres de l'essai sont « non vérifiés », avec le PDF empreinté à consulter ; les dimensions de Llama sont « non vérifiées » ; les chiffres de l'explorateur sont « de l'auteur, transcrits à vérifier ». Aucun chiffre de l'état de l'art n'est présenté comme vérifié.
- **Règle R8** : aucune zone vierge revendiquée ; la note le dit (section 6) et traite chaque « neuf » comme une question.
- **Résultats sous embargo** : les cellules ne citent aucun résultat du programme (recherche de T0.x, P3, 7a, 7b, étape B, `diag/` : seules deux occurrences de « P3 » en riposte de A au tour « explorateur », l. 47 et 74, qui désignent des positions de poussée, pas l'expérience P3). La note n'en cite aucun.

### (3) Cloisonnement

- **Famille 1** : aucune pièce ne relève de la conception d'organismes saboteurs discrets ; l'organisme des deux questions classe des tâches (question « déjà propre », l. 48-55). Je souscris.
- **Famille 2** : 66 passages exclus, chemin, lignes et taille ; les 66 tailles sont exactes au octet près. La note ne résume ni ne reformule aucun de ces passages. Le passage « Pour mémoire » sur l'opération « pousser » de l'organisme (explorateur T3-B l. 143-151 ; T3-C l. 106-114) a été rouvert : trois bras de budget égal et étalonnage de la variance, sans contenu d'évasion. Réserve unique : la ligne 314 ci-dessus.
- **Réserve d'honnêteté du rédacteur** : il dit que des passages exclus ont défilé à l'écran avant classement. Je ne trouve dans la note aucune trace de leur contenu.

### (4) Oublis

- Les dix-huit cellules, les trois espèces, les deux questions, les deux `LISEZMOI`, les journaux et les fichiers de faits sont tous présents dans la note. Aucune cellule ni espèce absente.
- Oubli mineur : les lanceurs v2 et v3 (correction 6).
- Observation pour la mère, hors de la note : l'inventaire range ces deux tours sous « Collisionneur v2.5 » (section A.1, l. 17) ; les questions s'adressent au « collisionneur v2.5 », mais `LISEZMOI-v1.md` des deux tours dit que l'outil employé est la v2.6 (`0e63febd…`, R-481). Sans effet sur le fond.

## Limites

- Les plages exclues n'ont pas été lues : leur classement en famille 2 et leur exhaustivité ne sont pas contre-lus, seulement leurs tailles et l'absence de reprise dans la note.
- 95 renvois rouverts sur environ trois cents ; les autres n'ont été confrontés qu'aux plages exclues, par programme.
- Les « neuf » de la section 4 n'ont pas été confrontés au programme ni aux préenregistrements ; comme la note, je les tiens pour des questions.
