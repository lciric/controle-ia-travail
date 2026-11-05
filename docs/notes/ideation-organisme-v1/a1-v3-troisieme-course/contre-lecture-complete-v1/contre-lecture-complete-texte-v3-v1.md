# Contre-lecture complète du texte — préenregistrement A1-v3, version 3 scellée (R2, lecteur neuf)

Contre-lecteur neuf : je n'ai écrit ni le texte (v1, v2, v3 et leurs brouillons), ni le code v3 ou v3.1, ni le lanceur durable, ni
les sondes, ni aucune contre-lecture ou audit précédent. 5 novembre 2026, à partir de 09:36:59 UTC (heures relevées par `date -u`).
Consigne : `consigne-contre-lecture-complete-texte-v3-v1.md`, sha256 `f03f78df69b7abbb4b99d0d45aff1de179b7e5ea8aa5276290e51f9a8758b983`
(compagnon égal). Interdits tenus : aucun commit, aucun `.sha256` rendu, aucun fichier existant modifié, rien sous `donnees/` ni
`/home/claude/coffre-*`, aucun réseau, aucune location, aucune clé lue, aucune dépense ; commandes sous `timeout 600 nice -n 10`,
épreuves en `python3 -I -B` sur des copies du bloc-notes, hors de tout dépôt.

**Verdict : lançable après couples, version v4 du texte.**
La v3 scellée (`c697d0df…`) n'est pas lançable : elle garde le marqueur `<<AUDIT_A9_SECONDE>>`, que le lanceur gelé refuse (B1, éprouvé).
La v4 = la v3 + les 14 couples joints (marqueur rempli par l'audit A9 rendu, faits de la seconde course alignés sur cet audit, risques complétés), un lanceur durable v4 qui nomme `…-v4.md`, et le mot de Lazar sur « texte v3 » du périmètre de GO-2026-11-04-06 ; rien d'autre de bloquant.

## Pièces lues et empreintes vérifiées

- Texte scellé v3 : `/home/user/ideation-organism/orchestrator/prereg/preenregistrement-attaque-goodhart-v3-v3.md`, sha256
  `c697d0dfb7956cd3bc0297af613746eafacf9d9f68ca39befa0d12c4daad5baa` (recalculé ; égal au compagnon et à la consigne ; 2 153 lignes,
  296 390 octets ; commit public `08ad8f35`) — **lu en entier**, sections 0 à 14, annexes et empreintes.
- v2 scellée, même dossier : `2a29f59353ce776f92d17799de25f8b75741f1c60dcc5edfbc427bf0ae3a8bb1` (compagnon égal) ; différence complète
  v2 → v3 relue bloc par bloc.
- Brouillons 1 à 3 de la v3 (`6e65136a…`, `86ad379b…`, `a92166b8…`, compagnons égaux) ; couples `couples-brouillon2-v3-v1.json`
  (`e1be43e2…`), `contre-lecture-n4-v1/couples-contre-lecture-n4-v1.json` (`462a8ea2…`), `couples-brouillon3-v3-v1.json` (`2e0f742a…`),
  compagnons égaux ; contre-lecture n° 4 (`b524b41c…`) ; rapports `rapport-redaction-v3-v2.md` et son additif 1 (sections 2, 4 à 8) ;
  audit A9 de la seconde course `audit-A9-a1-v3-seconde-course-v1.md` (`a0577b8b…`, compagnon égal) en entier.
- Registres (copie de travail du dépôt privé, lecture seule) : `registres/go.md` lignes 244, 247, 250 à 253 ; `registres/decisions.md`
  R-1478, R-1534, R-1538 à R-1554 ; `registres/depenses.md` (aucune dépense sous GO-2026-11-04-06, -04-09 ni -05-03).
- Lanceur durable v3 au commit `bb35e87f` : `src/controle_ia/hote_durable_a1_v3_v3.py` `916a3c85…`, `scripts/amorce_hote_durable_a1_v3_v3.sh`
  `e37bfde5…`, `tests/test_hote_durable_a1_v3_v3.py` `2f7e9291…` (égaux à l'arbre et aux compagnons ; lu seulement aux lignes qui
  touchent le texte : ordre des contrôles sur la machine, `NOM_TEXTE`, `GO_MACHINE`, numpy) ; ordre `docs/procedures/ordre-fille-a1-v3-troisieme-course-v1.md`
  (recherche de mots seulement).

## Épreuves (bloc-notes `/tmp/claude-0/-home-user/4a4722d4-e39d-57bd-bde3-e6a99e2eecdf/scratchpad/cl/`, hors dépôt)

- Arbre `git archive 08ad8f35 orchestrator` ; les 73 fichiers du bloc `empreintes-du-code` y sont ceux de `9776ed0` (`git diff --stat
  9776ed0 08ad8f35` vide sur ces 73 chemins ; `9776ed0` ancêtre de `08ad8f35`).
- `scripts/epreuve_marqueur.py` (`940cab64…`) : texte v3 scellé et son compagnon réel → `verifier_scelle` vrai, puis **« REFUS
  PreenregistrementRefuse marqueur(s) non rempli(s) : ['<<AUDIT_A9_SECONDE>>'] »**.
- `scripts/epreuve_v4_simulee.py` (`d0b6c387…`) : même texte, marqueur remplacé par un texte quelconque, renommé `…-v4.md`, compagnon
  factice → **accepté** (73 empreintes, plan : GO-2026-11-04-06, 400 USD, 259 200 s, « aucun », Argon un fil, configuration `e5306c47…`,
  devis maximum 190,46 USD).
- `scripts/epreuve_go.py` : `verifier_go_v55` gelé, GO-2026-11-04-06 à 400 USD : registre du canal à `740f49e2` accepté le 5 et le
  18 novembre, refusé le 19 (validité) ; registre de `main` à `a364e947` refusé (« identifiant GO-2026-10-24-07 en double ») ;
  ligne 244 de `main` = ligne 82 du canal à `740f49e2` et à `0aa04b5c`, à l'octet ; 74 identifiants sans doublon au canal, 17
  doublons sur `main` — comme le texte l'écrit (section 4).
- `scripts/rejouer_couples.py` : brouillon 1 + 10 couples = brouillon 2 (`86ad379b…`) ; brouillon 2 + 9 + 10 couples = brouillon 3
  (`a92166b8…`), à l'octet ; brouillon 3 → v3 : seuls le paragraphe de scellement et deux remplacements de `<<COMMIT_LANCEUR_DURABLE>>`.
- `scripts/hunks_sections.py` : les 24 blocs du diff v2 → v3 rattachés à leur section (question 4).
- Couples joints appliqués à la v3, résultat relu par le lanceur gelé : voir la fin de ce rapport.

## Points (gravité : bloquant / à corriger / note)

### Bloquant

- **B1 — bloquant (questions 1 et 6) : le texte scellé garde le marqueur `<<AUDIT_A9_SECONDE>>` (ligne 533, section 0.5 bis) ; le lanceur gelé refuse donc ce texte.** Le paragraphe de scellement (ligne 3) dit « brouillon 3 … avec, et seulement : le marqueur du commit du lanceur durable remplacé (deux fois) » ; l'annexe B (lignes 2061 à 2066) annonce deux marqueurs, dont celui de l'audit A9 de la seconde course ; R-1543 décrit le texte comme « brouillon 3 + commit du lanceur rempli + paragraphe de scellement ». Le motif gelé `<<[A-Z0-9_]+>>` (`demonstrations/attaque_goodhart_v3.py:97`) le voit et `lire_preenregistrement` refuse (`:271-273`) : épreuve ci-dessus. Sur l'hôte durable v3, l'ordre est : GO, registre, signe de vie poussé, sources, clone public, relais lancé, puis `--verifier-seulement` exigé en code 0 (`hote_durable_a1_v3.py:689-694`, hérité, appelé `hote_durable_a1_v3_v3.py:647`) : la machine aurait été louée, la branche du signe de vie prise (R12), et rien ne serait parti (aucune dépense d'Argon). La section 0.5 bis le dit elle-même (ligne 536 : « Tant que ce marqueur reste, le lanceur refuse ce texte »). Contre-épreuve : marqueur rempli, la copie renommée `…-v4.md` est acceptée — aucun autre refus de lecture. **Levée** : version v4 du texte (nom neuf, R12 ; texte neuf, graine neuve), marqueur rempli par l'audit A9 de la seconde course (`docs/notes/ideation-organisme-v1/a1-v3-troisieme-course/audit-A9-a1-v3-seconde-course-v1.md`, sha256 `a0577b8b0c6e0487b090d064f0872034f66024357ece95d2b14152b130e90a41`, compagnon égal), rendu par R-1478 (fichier entré par l'instantané `c0243d37`, compagnon par `cbaf76a9496aa90bf23a57e5926be08878fb95bd`, « R-1478 : audit A9 de la seconde course d'A1-v3 », qui porte les deux et descend dans `main` ; vérifié par `git show`), conclusion « cause d'infrastructure établie » (audit, section 6, « Conclusion pour le marqueur AUDIT_A9_SECONDE de la v3 ») — couple C1. **Conséquence hors du texte** : le lanceur durable fige le nom du texte (`NOM_TEXTE = "orchestrator/prereg/preenregistrement-attaque-goodhart-v3-v3.md"`, `src/controle_ia/hote_durable_a1_v3.py:56`, repris par la v3 via `h.NOM_TEXTE`) ; une v4 du texte (`…-v4.md`, seul nom libre) demande donc un lanceur durable v4 (noms neufs, R12, essais rejoués), et la v4 du texte doit nommer ce lanceur (paragraphe de tête, section 0.5 bis l. 572, section 8 « Troisième course (v3) », section 13 point 7 quater, section 14) — couples à écrire quand ce commit existera (marqueur de commit, comme en v3), non joints ici.

### Question 1 — cohérence interne du texte entier

1. À corriger (couple C6) — section 13, point 4, « **Marqueurs (aucun ne reste)** » n'a pas été mis à jour pour la v3 : il ne nomme que les marqueurs de la v1 et de la v2, alors que l'annexe B en annonce deux pour la v3 ; aucune étape de la section 13 n'exige, sur le fichier final, la recherche des marqueurs au motif du lanceur avant l'écriture du compagnon — l'étape qui aurait arrêté B1.
2. À corriger (couples C2 à C5, C3 bis) — section 0.5 bis, faits de la seconde course non alignés sur l'audit A9 rendu (réserves R3, R4 et R7 de l'audit ; R-1478 : « à reporter dans la section 0.5 bis ») : limite d'usage bloquante dès 03:04:53 UTC (le texte : « vers 03:46 ») ; 03:46:39–40 = redémarrage du processus de travail, garde arrêtée « worker_restart » (absent) ; ≈ 1 h 42 (le texte : 1 h 43, aussi en section 12) ; lien limite → redémarrage vraisemblable, non prouvé (le texte l'affirme) ; dépense 48,49583 à ≈ 50,30 USD avec un appel en vol (le texte : 48,49583) ; « son audit A9 ne lit que ce que l'audit A9 de la première a lu (journaux, registre de dépense, manifeste de départ) » : l'audit n'a lu aucun fichier de l'état scellé (noms et empreintes seulement).
3. À corriger (couple C1) — les cinq points que le texte assigne à l'audit comprennent « dépense appariée au registre » ; l'audit l'établit sur le journal du relais seulement, non appariée au registre de dépense de la sortie (lecture interdite par sa consigne ; audit, section 6, point 3) : la v4 doit l'écrire en remplissant le marqueur ; ce n'est pas une condition d'admission (la règle de la section 8 demande la cause), c'est une réserve (R4).
4. À corriger (couple C7, C7 bis, C7 ter) — section 14 : le n° 4 y est encore « à faire » ; sa liste de pièces dit « ce brouillon (`…-brouillon1.md`) » et « le lanceur durable v3 … et son additif 1 », alors que le n° 4 a lu le brouillon 2 et le lanceur durable v2 (son titre ; le couple 9 du brouillon 3 a réécrit la liste après coup) ; les 10 couples du rédacteur appliqués au brouillon 3 (C1 à C3 du code, noms v2 → v3) n'ont été contre-lus par personne avant le scellement (R2 non tenue pour eux, contrairement à R-1543 « R2 tenue ») — ils le sont par cette lecture et par la lecture parallèle du lanceur.
5. Note — section 8, « Création » : la puce garde « **aucune carte** (`num_gpus` = 0) … 8 Go de mémoire » et le préambule dit « ces critères remplacent “aucune carte (`num_gpus` = 0)” dans la liste ci-dessous » (une carte, au moins 8 000 Mo de mémoire) : juste par la phrase de remplacement, contradictoire à la lecture ; la v4 gagnerait à écrire l'offre une fois (et à dire si « 8 Go » est la mémoire vive et « 8 000 Mo » celle de la carte).
6. Note — section 8, « Plafonds de la machine » : « 80 h de vie et 32 USD (0,40 USD × 80 h) » ; sections 12 et 13 : « au plus 32,57 USD (minuterie : création + 10 min + 80 h + 1 h, plus 15 min) » : les deux sont vrais (80 h et 32 USD = garde de l'hôte qui arrête la course ; 32,57 USD = borne de la minuterie de destruction ; rapport `rapport-redaction-v3-v2.md`, section 2, (C)) mais le texte ne relie jamais les deux ; « 80 h de vie » est inexact (la machine vit jusqu'à ≈ 81 h 25).
7. Note — section 0.5 bis : « la session qui lance (la fille) ne fait que louer, puis n'a plus de rôle » contredit le point 7 quater (contrôles du pilote à T0 + 40 min et après l'échéance finale, inventaire R14) ; le couple 9 du n° 4 n'a corrigé que le point 7 quater.
8. Note — renvois faux : section 0.7, point 23, « sections 4, 8, 13 point 7 quater et 14 » : le renommage dit « section 4 » est en section 0.5 bis (ligne 572 ; le couple 3 du brouillon 3 le dit « section 4 (ligne 570) ») ; la phrase « Brouillon 3 » du paragraphe de tête omet 0.5 bis. Tous les autres renvois neufs de la v3 que j'ai suivis (0.5 bis, 0.7, 4 « GO » et « Registre », 8 « Troisième course (v3) », 9 L18, 11, 12, 13 points 3, 7, 7 quater et 9, 14, annexe B, rapport v3-v2 section 2 (C) et section 5 conduite (b), audit A9 de la première sections 2 et 8) existent et disent ce qui est cité.
9. Note — section 4, « GO » : sous la convention du paragraphe de tête, la puce commence par « **GO-2026-11-03-01** (bloc `plan-gele`) » alors que le bloc porte GO-2026-11-04-06 (dit plus bas, « Troisième course (v3) ») ; juste par la convention, trompeur pour un lecteur ; même effet pour le registre hors du clone (`/home/user/hors-clone-a1-v3-seconde-v1/…`) et le dossier de sortie. Titre « version 3, brouillon 1 » d'un texte scellé : convention de la v2 (n° 4, point 6), sans effet.
10. Note — hypothèses, prédictions, métriques, seuils, plan d'analyse, critères gelés (ordre 2, 6, 1, 3, 4, 5), audits A1 à A9 et liste d'arrêt : chacun défini une fois (sections 2, 3, 5, 6, 7, 8), sans contradiction entre sections ; table des comptes à u unités jouées recoupée par sondage (Wilson : 0/11 → 0,259 ; 0/12 → 0,2425 ; 2/11 → 0,051 ; 1/4 → 0,045 ; 2/12 → 0,047), cohérente avec « sous 19 », « sous 21 », « de 4 à 11 », « de 1 à 3 ».

### Question 2 — prédictions et critères

11. Note (conforme) — P1 à P6 reconduites de T sans changement, avec signe attendu, seuils en comptes à u unités jouées et valeurs d'A1 « pour information » ; « réplication à valeurs antérieures connues » déclarée ; issues ouvertes dans les deux sens (brèche, bras perdu, sans dents, résiste, instrument, précision) ; aucune course ne vise un signe (R3).
12. Note (conforme, R7) — aucun chiffre de l'état de l'art ; chiffres d'A1 renvoyés à A, V et AD par section et empreinte ; ceux de la seconde course au rapport de la fille et à l'audit ; le chemin du 402 est dit « non relu » sur la commande.
13. À corriger (couple C1) — la règle de lecture des trois courses est écrite d'avance (0.5 bis ; 13, point 9), mais la règle qui **admet** la troisième (« cause d'infrastructure établie par l'audit A9 ») n'est pas écrite dans le texte scellé : sa citation est le marqueur (B1).
14. À corriger (texte de tête de la v4, non joint) — la v4 doit dire qu'aucune course n'a tourné sous la v3 (rien loué ni lancé : R-1545, R-1553 ; la v3 est refusée par le lanceur), donc que sa course est encore la troisième (et non une quatrième, qui demanderait un GO neuf, section 8), et ajouter « aucune relance de la v3 ».
15. À corriger (procédure, nœud de Lazar) — GO-2026-11-04-06 (ligne 244) et GO-2026-11-05-04 (ligne 252) disent « texte v3 neuf, contre-lu …, scellé, committé et poussé avant la course » : une v4 sort de la lettre du périmètre ; ni le lanceur gelé ni le lanceur durable ne lisent le périmètre ; la v4 doit citer le mot de Lazar qui la couvre (R-1553, « A1-v3 complet, puis lancer », relayé avec « texte v4 … s'il le faut ») ou une extension du GO. Les trois GO échoient le 2026-11-18 (vérifié une fois, au départ).
16. Note — section 12, « pour information » : ≈ 0,078 USD par appel de la seconde course (48,49583 / 620) compte les 5 échecs, comptés au pire cas réservé si la table de la section 4 vaut pour eux (≈ 1,6 USD chacun), et se compare au 0,062 d'A1 calculé sans l'échec ((34,35943 − 1,61417)/526) : pas à périmètre égal ; sans effet sur le plan.

### Question 3 — ce qui peut fausser la course ou sa lecture

17. Note (conforme) — instrument : Argon seul, relais 8805 à un fil (410 USD, 9 000 appels, aucune reprise), code `9776ed0` (73 empreintes égales sur `08ad8f35`, épreuve), configuration `e5306c47…` (absente de ce conteneur : vérifié par empreinte sur tout le disque, R11), plan gelé lu et accepté par le lanceur gelé (épreuve v4 simulée) ; graine neuve à la v4 (celle de la v3, publique depuis 07:35 UTC, n'a servi à rien : aucune carte calculée, L18).
18. Note (conforme) — plafonds : 400 USD (la garde du registre mord la première, ≈ 398,39 USD) ; relais 410 USD et 9 000 appels (≥ 400 et ≥ 8 000 exigés, section 13, point 7 (a) : 6 144 + 247 + 1 584 = 7 975) ; 72 h (≥ 35,78 h) ; garde de l'hôte 80 h et 32 USD ; minuterie 32,57 USD sous GO-2026-11-05-03 (35 USD : il reste 2,43 USD pour tout autre usage de ce GO, sonde ou essai, ce que le texte ne dit pas).
19. Note (conforme) — codes 2 à 6, commande muette, 402 et 429 : table de la section 4, règles, choix (e), section 8 et section 12 concordent ; un 402 de l'interface → code 3 au pire cas (déduit de n° 294, déclaré non relu) ; si le relais rendait ce 402 tel quel (son propre HTTP 402), la commande sortirait en code 4 et la course s'arrêterait aussitôt (« refus_de_budget »), plus tôt et moins cher : les deux chemins sont des arrêts d'infrastructure sans résultat, sous la même règle.
20. À corriger (couple C9) — **disparition de la machine** (hôte de Vast perdu, instance détruite par un tiers) : rien n'est versé, car manifeste, registre de dépense, journaux et relevés de la garde ne vivent que sur la machine ; le texte dit seulement « une mort brutale perd les réponses en mémoire, comme en v2 », alors qu'en v2 le disque survivait : la dépense d'Argon n'est alors connue que par la facturation du fournisseur (≤ 400 USD), la machine par celle de Vast (≤ 32,57 USD), et l'audit A9 n'a que la branche du signe de vie, le journal de la location et les relevés de Vast — à écrire.
21. À corriger (couple C10) — **poussée finale manquée ou secret trouvé** : « la machine s'arrête … données gardées sur son disque, et la session qui reprend décide » ; aucune voie de récupération n'est éprouvée (point d'entrée = amorce, pas de coquille ; `vastai copy` non éprouvé, R-1549 ; jeton non remplaçable sur la machine, R-1551) ; C3 ne couvre qu'une panne passagère suivie d'une relance : une telle fin peut perdre la course et sa dépense — à déclarer (R4).
22. À corriger (couple C11) — **échéance du jeton GitHub** absente du texte, alors qu'elle a arrêté le départ (R-1545) et qu'un jeton échu rend le versement final impossible : contrôle à écrire avant la location (point 7 quater : échéance après T0 + 82 h, lue sans l'afficher ; sinon rien n'est loué).
23. Note — plus aucune alerte en direct : l'« alerte écrite d'avance » du point 7 devient une lecture d'après coup par l'audit A9 (7 quater) ; une cause durable (402, clé révoquée, quota quotidien) va jusqu'à l'arrêt au plafond (≤ ≈ 12 h, sans résultat) sans décision de Lazar ; c'est dit par morceaux (section 8, 402 ; 7 quater), cohérent avec « l'hôte n'envoie aucun message ».
24. Note — reprise et versement : C3 (copie de nom neuf), signe de vie exigé (C2), destruction par identifiant, branches neuves (R12) et « sortie scellée avant lecture » sont écrits et cohérents ; ce qui est rapporté si la course meurt est écrit pour la reprise du conteneur (état versé sur `…-troisieme-interrompue-v1`), non pour la disparition (point 20).

### Question 4 — écart à la v2 scellée

25. Note (conforme) — différence complète v2 → v3 : 24 blocs, tous dans des sections que la section 0.7 et le paragraphe de scellement nomment (tête, 0.4, 0.5 bis, 0.7, section 4 dont la ligne `go:` du bloc `plan-gele` et ses notes, sections 8, 9 L18, 11, 12, 13, 14, annexe B, empreintes) ; aucun dans les sections 1, 2, 3, 5, 6, 7 et 10 ; bloc `empreintes-du-code` et bloc `plan-gele` hors `go:` inchangés ; chaîne des brouillons et passage brouillon 3 → v3 rejoués à l'octet.
26. Note — seuls écarts de déclaration : les deux renvois du point 8 ; et le paragraphe de scellement, juste dans ce qu'il dit, tait le second marqueur.

### Question 5 — risques déclarés

27. Note (conforme) — clé d'Argon : métadonnées de la machine chez Vast, clé d'instance qui voit tout le compte, exploitant de la machine, transcription d'une session (R-1540), usure du crédit commun ; conduite écrite (nom de variable, jamais affichée, rotation après la course, risque au rapport de la course).
28. Note (conforme) — jeton GitHub : exposition à l'exploitant et écriture possible sur `main` (dont `registres/go.md`, lu par les gardes) déclarées, rotation après la course ; manque l'échéance (point 22).
29. À corriger (couple C8) — crédit d'Argon : le texte écrit une précaution (Lazar confirme au moins 400 USD ou une recharge automatique, la fille l'écrit au journal), absente de l'ordre de la fille (recherche de « crédit », « solde », « 402 » : rien) et abandonnée par R-1543 (« risque accepté pour aller vite ») ; texte, ordre et registre doivent dire la même chose, avec le prix : un solde épuisé en cours de course perd, sans résultat, tout ce qui a été dépensé avant le premier 402 (jusqu'à ≈ 131 USD à l'attendu haut du code).
30. Note — interpréteur Python : C1 écrit et cohérent (3.13 par chemin absolu, lien de `/usr/bin/python3`, versions au journal, sinon rien ne part) ; le texte affirme que la configuration gelée écrit `/usr/bin/python3` pour la commande d'Argon, ce que le rédacteur n'a pas relu (additif 1, section 6, point 2) et que je ne peux pas relire (configuration absente) : les deux cas sont couverts par C1.
31. Note — versement : épreuve « partie de `main` » contre GitHub déclarée réussie (07:31:40 UTC, `19d2b119`) — non vérifiable ici (branche et objet absents des références locales, aucun réseau) ; échecs : points 21 et 22.

### Question 6 — autre point pour une course à 400 USD au plus

32. Bloquant — B1 (ci-dessus), avec ses deux suites hors du texte : lanceur durable v4 (`NOM_TEXTE`) et mot de Lazar sur le périmètre (point 15).
33. Note — intégrité des sorties sur une machine tierce : l'exploitant, déclaré maître du disque et de la mémoire pour les secrets, l'est aussi des sorties avant leur scellement sur la machine ; non exclu, non déclaré ; réserve à écrire au rapport de la course (R4).

## Couples (`couples-contre-lecture-complete-texte-v3-v1.json`, 14 ; chaque « ancien » unique dans la v3 scellée et encore unique au moment de son application, dans l'ordre)

C1. Section 0.5 bis : marqueur `<<AUDIT_A9_SECONDE>>` et ses quatre lignes → chemin, commits, empreinte, conclusion de l'audit A9 rendu, ses cinq points (dont la dépense non appariée au registre) et ses réserves (B1, points 3 et 13).
C2. Section 0.5 bis : « coupée par la limite d'usage … vers 03:46 » → bloquée dès 03:04:53, redémarrage du processus de travail à 03:46:39–40, garde arrêtée « worker_restart » (point 2).
C3. Section 0.5 bis : « ≈ 1 h 43 » → « ≈ 1 h 42 » (point 2) ; C3 bis, même chiffre en section 12.
C4. Section 0.5 bis : dépense bornée par un appel en vol, ≈ 50,30 USD au plus (point 2).
C5. Section 0.5 bis : « cette fois par la limite d'usage de la session » → sous la limite du compte, lien vraisemblable non prouvé (point 2) ; C5 bis : ce que l'audit a lu (point 2).
C6. Section 13, point 4 : marqueurs de la v3, celui resté (B1), contrôle par programme sur le fichier final avant le compagnon (point 1).
C7. Section 14 : titre ; C7 bis, n° 4 rendu, ce qu'il a lu, couples du brouillon 3 non contre-lus ; C7 ter, sa liste de pièces (point 4).
C8. Section 8 : précaution du crédit d'Argon et son abandon de R-1543, avec le prix (point 29).
C9. Section 8 : disparition de la machine (point 20).
C10. Section 8 : poussée finale manquée ou secret trouvé (point 21).
C11. Section 13, point 7 quater : échéance du jeton GitHub (point 22).

Restent à écrire par le rédacteur de la v4, hors de ces couples (ils dépendent du commit du lanceur durable v4 ou sont l'en-tête
d'une version) : paragraphe de tête de la v4 et section 0.8 ; nom `…-v4.md` dans la commande exacte (section 4) ; « texte v3 » là où il
désigne le texte de la course (section 4, commande exacte ; section 8, « Préparation » ; section 13, point 7 quater) ; noms, essais et
commit du lanceur durable v4 (tête, 0.5 bis l. 572, section 8, 13 point 7 quater, 14) ; les points 14 et 15 ; à la discrétion du
rédacteur, les notes 5 à 9.
