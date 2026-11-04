# Contre-lecture R2 — pilote de l'exposant p, v1, brouillon 2

Contre-lecteur neuf (sous-agent) : je n'ai écrit ni le brouillon 1, ni le brouillon 2, ni leur code, ni la contre-lecture du brouillon 1. Consigne : `brouillons/pilote-exposant-p-v1/consigne-contre-lecture-brouillon2-v1.md` (`75eb079efc58feca7af6556f0800ee1bf4fa78087d7f35de1332a40adf2128cf`, vérifiée avant lecture). Travail du 4 novembre 2026, de 02:26 à 02:38 UTC (`date -u`). Branche `canal/conv-audit-n04`, tête `defb1887` (au-dessus de `07771c8d`), lecture seule.

Respecté : aucun commit, aucun `.sha256`, aucun fichier existant modifié (seuls des fichiers neufs sous `contre-lecture-v2/`) ; rien sous `donnees/` ni `/home/claude/coffre-*` ; aucun réseau, aucun modèle, aucune carte, aucune dépense. La garde de calcul a été essayée sur une entrée synthétique (aucune commande Vast.ai exécutée).

## Verdict

**Scellable après couples** : aucun bloquant ; 20 couples au brouillon 2 (`couples-contre-lecture-pilote-exposant-p-v2.json`) et quatre retouches de code (I1, I3), sans brouillon 3 ni nouvelle contre-lecture complète.
Les sept bloquants du brouillon 1 sont levés ; le PDF empreinté confirme chaque chiffre et chaque règle du papier que je l'ai vérifié, page citée (la réserve R7 tombe pour eux).
Restent hors de ce verdict, comme le brouillon le dit : vérification des stimuli par Lazar (R-S9), DOI de R9-bis, puis scellement.

Comptes : 0 bloquant, 4 importants, 7 mineurs ; 20 couples (tous au brouillon 2, chaque « ancien » unique, appliqués dans l'ordre sur une copie sans échec).

## Ce que j'ai rejoué, avec les empreintes

1. **Empreintes** : les 17 compagnons `.sha256` du dossier du pilote et de `contre-lecture-v1/` passent `sha256sum -c` ; PDF `docs/sources/pdf/2606.24964v1.pdf` = `689de6c1da8676b31e40a4a71a0b7663c738847eb486ba2d7b2642a0049cdd91` (concordant).
2. **Essais** (commande exacte de la consigne) : `67 passed in 264.33s`, de 02:27:13 à 02:31:40 UTC (46 du pilote v2, 21 du script et de l'amorce).
3. **Règle seule, sans banque** (question 3) : `rejeu/regle_seule.py` (`54b8e8cd30c1d9abf7c083da47de28f55c98c5be12cc2bb807251a43980dd4ac`) appelle `analyse.bootstrap_sous_ensembles` et `issue_principale` tels quels sur des p gaussiens ; sortie `rejeu/regle-seule.json` (`5767db686db97aaed4dd4f87f3d0507f2c9e3a1598d28ef458accbeb14493c01`), `SeedSequence(2026110499)`, 2 000 répétitions, B = 2 000.
4. **Garde de calcul** (question 5) : la garde de `main` (`/home/user/controle-ia-travail/.claude/hooks/garde_calcul.py`, avec la règle d'extension R-389) et celle de la branche, sur le registre de `main` (tête `b4b6c6f9`), par les entrées `rejeu/entree-garde-sain.json` (`e1d00976…`) et `rejeu/entree-garde-artefact.json` (`74fd6c36…`) ; classement des lignes répétées par `rejeu/doublons_go.py` (`5888befc21bb86da04d0c47b135c79af6a14cf3846bc8dee7195931da0b7eb07`). Étape « verifier » de l'amorce (`controle_ia.pilote_exposant_p_v2.go`) rejouée sur ce registre.
5. **Papier** : `pdftotext` du PDF empreinté, lu aux pages 1 à 12 pour chaque chiffre et règle repris (tableau en fin de rapport).
6. **Couples** : `rejeu/couples.py` (`e55a2d41a5e832e3989a9284bc1158aecf0a2fb9f5201947f01ecd20f936712b`) vérifie l'unicité de chaque « ancien » dans le brouillon 2 et au moment de l'appliquer.

## Question 1 — les sept bloquants du brouillon 1

| Bloquant | Levé ? | Ce que j'ai vérifié |
|---|---|---|
| B1 stimuli | **oui** (mécaniquement) | 30 quadruplets : paires de E minimales (même corps, dernier mot seul), porteur partagé entre registres, 30 + 30 porteurs distincts, aucune classe contrôlée ; la garde passe. R-S9 reste à Lazar (13 doutes signalés). Fuite de surface restante : I1 |
| B2 plan contre famille | **oui** | « moyenne » dans toutes les phrases ; qualificatif de famille (K = 8, intervalle de prédiction en t) codé et simulé |
| B3 référence | **oui** | plan k sur k mod 32 (`run.py`, bloc `lu_rd_rd`) ; rééchantillonnage par sous-ensembles ; simulation refaite avec effet commun |
| B4 sensibilité | **oui** | bloc `lu_WG` décisif juste après la référence ; `issue_gelee` convertit « égal » et « au-dessous » ; essais sain et artefact. Question 4 ci-dessous |
| B5 phrases | **oui**, une phrase à reprendre | bornes complètes ; mais `NE_MONTRE_PAS` dit « E et R sont faites de fins de phrase courtes » : faux pour R, qui n'est plus porté que par le corps (I1, couple 17) |
| B6 gardes | **oui** | 67 essais rejoués ; arrêt « instrument non validé » en jouet (code 3), plafond de durée, grille non finie, tokeniseur, flux court, script et amorce |
| B7 provenance | **oui** | PDF empreinté ; tout ce que le brouillon tire du texte du papier s'y retrouve (I4) |

**Rien de neuf n'est cassé** au sens d'un arrêt ou d'une lecture fausse. Trois défauts neufs, corrigés plus bas : la description de R dans la borne commune (I1), le qualificatif « au-dessus du jumeau » qui en dit trop (I1), et l'amorce qui refuserait une ligne d'extension légitime du GO cité (I3 ; elle échoue alors en refusant, sans risque de dépense).

## Bloquants

Aucun.

## Importants

### I1 — Fuite de surface : E sépare l'évaluation du déploiement par plus que le statut (question 2)

À corps identique, la personne, la longueur en mots et les classes contrôlées sont égales dans chaque paire de E : ce que B1 demandait est fait. Mais trois différences systématiques restent entre porteurs d'évaluation et porteurs de déploiement :
- **domaine** : les 30 porteurs d'évaluation sont du jargon de l'apprentissage automatique (ablation, honeypot, autograder, testbed, dataset…), les 30 de déploiement des mots courants de la vie (wedding, funeral, surgery…) ;
- **accord au contenu** : chaque porteur de déploiement est appelé par le corps (gâteau → fundraiser, propriétaire → eviction, grand-père → funeral, anesthésie → surgery, eau au sous-sol → flood) ; aucun porteur d'évaluation ne l'est (« a short toast for my closest friend … for the scoreboard », « which cheeses … because of the red-teaming »). À la couche 2, E peut donc lire « dernier mot imprévisible et technique » autant que « je suis évalué » ;
- **sous-jetons et fréquence** : le dernier jeton est le dernier sous-jeton. « eval » termine sans doute model-eval, eval, chatbot-eval et LLM-eval, « benchmark » deux porteurs ; les 30 porteurs d'évaluation ne sont pas 30 derniers jetons distincts. Non compté ici : le tokeniseur de Llama n'est pas sur la machine.

**Le modèle stylisé n'est pas un garde suffisant.** Sous lui, les corps s'annulent exactement dans E et les porteurs exactement dans R : E vient des seuls porteurs, R des seuls corps, et R-S4 rend ces vocabulaires disjoints. La médiane de |cos| vaut donc ≈ 1/√4096 par construction, et 0 à w = 0, où R est nul (`stimuli.cos_stylise` rend 0,0). Il garde contre le défaut du brouillon 1, pas contre une fuite de surface ni contre l'interaction réelle du réseau, que seuls les descriptifs I8 mesurent.

**Ce que le jumeau contrôle.** Par construction (même nombre de jetons que le porteur d'évaluation), il contrôle les sous-jetons. Il ne contrôle pas le domaine (les neutres sont des objets de médias : podcast, newsletter, brochure). L'accord au contenu, il ne le contrôle qu'au hasard : certains neutres sont appelés par le corps (cookbook pour le gâteau, tutorial pour Python), d'autres non.

Corrections :
- texte : couples 10 (déclaration dans « Directions »), 11 (bloc 0), 17 (borne commune), 18 (qualificatif du jumeau) ;
- code : `analyse.NE_MONTRE_PAS` et `analyse.QUALIF_JUMEAU["au-dessus du jumeau"]` reprennent mot pour mot le « nouveau » des couples 17 et 18 ;
- code : au bloc 0, sur le tokeniseur du modèle lu et avant tout passage avant, consigner pour chaque porteur (évaluation, déploiement, neutre) le nombre de jetons et le dernier sous-jeton ; descriptif, sans seuil. Essai sain et artefact (deux porteurs au même dernier sous-jeton, rapportés). Le compte « Tests attendus » change ;
- option pour Lazar, non exigée : s'il refuse un quadruplet à la vérification humaine (stimuli v3), ajouter un second jumeau, technique sans statut (compiler, firmware, repository…, même nombre de jetons). Il séparerait « évaluation » de « jargon technique étranger au contenu ».

### I2 — Règle de lecture : 5,7 % de faux « au-dessus » à Δ = 0 (question 3)

**Le biais vient de la simulation, pas de la règle.**
- Dans `puissance.py`, le plan lu « à la moyenne » est tiré de la banque à la clé la plus proche de p_vrai(2,0) : Δ estimé moyen +0,014 dans le scénario central, de +0,005 à +0,016 dans les neuf scénarios recalés. Au calage prudent, où ce biais est nul, les taux sont symétriques.
- L'écart type simulé de Δ (0,0333) égale la demi-largeur médiane divisée par 1,96 (0,0656 / 1,96 = 0,0335) : l'intervalle n'est pas trop étroit.
- Un décalage de 0,42 écart type prédit ≈ 6,2 % et 0,9 % (loi normale, calcul) ; la simulation en rend 5,7 % et 1,3 %.

**La règle seule, sans banque** (`rejeu/regle-seule.json`) :

| Scénario (σ plan 0,12 sauf mention) | faux « au-dessus » | faux « au-dessous » |
|---|---|---|
| τ 0,17, σ_c 0,035 | 3,05 % | 3,55 % |
| idem, biais +0,014 ajouté | 6,80 % | 1,55 % |
| τ 0,17, σ_c 0,06 | 2,65 % | 3,20 % |
| τ 0,10, σ_c 0,035 | 2,50 % | 3,95 % |
| τ 0,25, σ_c 0,035 | 3,55 % | 3,00 % |
| σ plan 0,22, τ 0,17, σ_c 0,035 | 2,80 % | 3,15 % |

La règle a un léger excès symétrique (≈ 3 à 4 % par côté pour 2,5 %), attendu d'un rééchantillonnage par percentiles sur 32 grappes : la variance de rééchantillonnage vaut 31/32 de la variance empirique, et le quantile 1,96 remplace celui de Student à 31 degrés, 2,04.

- **Pas de correction de la règle avant le scellement.** L'excès est symétrique, donc compatible avec R3 et R4, et petit devant ce qui sépare les issues.
- **Correction du texte** : couple 7 (attribution, chiffres de la règle seule, réserve chiffrée) et couple 8 (la même banque biaise les puissances : +0,10 donne 85,7 %, −0,10 donne 77,3 %).
- Facultatif : rejouer la simulation avec un plan lu non arrondi (tirer à la clé, puis retrancher l'écart entre la moyenne de la clé et la cible) dans une `puissance-…-v3.json`. Ce n'est pas nécessaire au scellement.

### I3 — Garde de calcul et amorce (question 5)

**Constat, rejoué.** La prémisse « l'amorce refuse le registre de `main` » ne tient pas :
- **amorce** : l'étape « verifier » (`go.py`) rend `valide: true`, code 0, sur le registre de `main` (GO-2026-11-04-03, ligne 241, calcul, Lazar, 4 au 18 novembre, 30 USD ≥ 17). Les seize identifiants répétés ne donnent qu'un avertissement ;
- **garde de `main`** : elle porte déjà la règle d'extension R-389. Sur ce registre, les 33 lignes répétées sont toutes des extensions conformes (périmètre qui commence par « extension », même type, Lazar, date non antérieure, échéance non plus lointaine) ; aucune ne bloque. Elle laisse passer `GO_ID=GO-2026-11-04-03` (code 0) et bloque un identifiant absent (code 2) ;
- **garde de la branche** `canal/conv-audit-n04` : plus ancienne, sans R-389. Sur le registre de `main`, elle bloque (« identifiant GO-2026-10-24-07 en double »). Sur le registre de la branche, GO-2026-11-04-03 est absent.

Ce qui bloque est donc une session qui créerait l'instance depuis l'arbre de la branche. **Règle juste** : créer depuis l'arbre de `main` (couple 2). Le devis v2, section 4, point 2, est périmé sur ce point ; il ne se corrige pas par couple : le noter à la passation, ou dans un devis v3.

**L'amorce doit changer** (`go.py`, avant le scellement, puisque le préenregistrement cite l'amorce dans la liste d'arrêt) : aujourd'hui, une extension légitime de GO-2026-11-04-03, par exemple un plafond relevé, la ferait refuser (« en double »). Règle proposée, alignée sur la garde de `main` :
1. trouver la **première** ligne de l'identifiant cité ; elle seule fixe le type (« calcul »), l'auteur (Lazar) et la période (accordé le → échéance) ;
2. chaque autre ligne de **cet** identifiant doit être une extension conforme à R-389 ; sinon, refus (« ligne en conflit ») ;
3. plafond : celui de la dernière extension conforme dont la colonne « plafond » donne un montant lisible en USD ; à défaut, celui de la première ligne. Une extension dont le plafond n'est pas lisible ne baisse rien ; elle est consignée ;
4. périmètre : « exposant p » nommé par la première ligne ; une extension qui le nommerait seule ne suffit pas ;
5. révocation : inchangée ;
6. doublons d'**autres** identifiants : rapportés, jamais bloquants. Un doublon non conforme ailleurs est signalé en clair : « la garde de calcul de `main` bloquerait la création ».

Essais à ajouter (R5) :
- extension conforme du GO cité → valide ;
- extension qui relève le plafond → plafond lu sur l'extension ;
- extension non conforme du GO cité (type différent, ou échéance plus lointaine) → refus ;
- doublon non conforme d'un autre identifiant → valide, avec l'avertissement.

Mieux encore, une seule fonction de lecture partagée avec la garde. La garde vit hors de `src/`, sous `.claude/hooks/` : à défaut, un essai qui vérifie que les deux rendent le même verdict sur le registre de `main`.

### I4 — R7 : ce que le PDF empreinté confirme (consigne : « vérifie chaque chiffre et chaque règle »)

Tout ce qui est repris du texte est confirmé. La réserve R7 tombe pour ces points (couples 1, 3, 4, 5, 6, 14, 16). Deux nuances :
- 528 isotropes n'est pas dans le texte (M2) ;
- l'écart de 0,37 qui fonde δ n'est donné que pour Gemma-2-9B ; sur les autres modèles, la famille contrastive peut être à 2,24 (§6, p. 7), soit un écart voisin de δ. Ajouté au couple 4 : c'est un argument de plus pour le témoin de sensibilité.

| Repris par le brouillon | Papier (PDF `689de6c1…`) |
|---|---|
| couche 2 par défaut, mesure à l'avant-dernière couche, réponse L2, dernier jeton | §3, p. 2 |
| 30 ancres, FineWeb de 5 jetons, médiane (éq. 2) ; T = f · min des maxima, f = 0,5 (éq. 3) | §3, p. 3 |
| P ≥ 30 ; « LLM generated and human verified » | §3, p. 3 ; annexe A, p. 11 (« LLM-generated and human-verified ») |
| différences aléatoires : P = 30, 10 000 entrées, « most stringent non-feature baseline », 40 directions | §3, p. 3 |
| 780 paires, 710 gardées, « below 0.1 » sans valeur absolue | §4.1, p. 5 |
| \|⟨dᵢ, dⱼ⟩\| < 0,1, directions brutes ; « more than 99% aligned » | annexe A, p. 11 |
| contrastives 2,42 [2,29 ; 2,62] ; différences aléatoires 2,05 [2,00 ; 2,10] | §4.1, p. 5 ; figure 4, p. 6 |
| aucune médiane de résidu au-dessus de 2 % | figure 4, p. 6 ; annexe B, p. 11 |
| Wealth × Gender sur Gemma, p = 2,40, « p>2 indicates these directions are privileged » | figure 2, p. 5 |
| p mesuré : borne basse, le désalignement tire p vers 2 | §6.1, p. 7 à 8 |
| lectures rivales des plateaux | §6.2, p. 8 à 9 |
| « necessary but not sufficient » | §7, paragraphe « Future work », p. 9 (le renvoi « §7 » du brouillon est juste) |
| moyennes contrastives des autres modèles dans [2,24 ; 2,63] | §6, p. 7 |
| Literary : registres argotique et littéraire, 50 gabarits ; Formal absent des 33 | annexe A, p. 11 |

## Mineurs

- **M1 — Formal et Literary.** Formal n'est pas parmi les 33 directions du papier (annexe A, p. 11) ; Literary oppose deux registres, argotique et littéraire, et c'est la direction du papier la plus proche de R. E-02 dit « aucune direction … de registre » : à corriger. Couples 9, 12, 15, 19.
- **M2 — E-07.** « Le papier en prend 528 » : le texte ne le dit pas (528 = MELBO, §4.1, p. 5 ; isotropes d'après l'audit). Couple 13.
- **M3 — Témoin de sensibilité.** La règle du cosinus ne filtre pas le plan Wealth × Gender du modèle lu ; à déclarer. L'ordre de grandeur du papier est à citer (couple 6).
- **M4 — Liste d'arrêt.** Il manque deux lignes. D'abord un plafond de prix à la création : au-delà de 2,6 USD l'heure, le pire cas dépasse 30 USD (devis, section 3). Ensuite un arrêt de l'instance à 11 h : l'amorce ne l'arrête pas, et une instance oubliée consomme la marge, 13,4 USD, soit ≈ 9,6 h au prix haut. Couple 20 ; la session de lancement programme le rappel.
- **M5 — Devis.**
  - Volume juste : 510 × 28 860 = 14 718 600 séquences.
  - Le débit attendu de 15 s par plan est un peu optimiste : 2 × 8·10⁹ × 5 jetons × 28 860 ≈ 2,3·10¹⁵ opérations, soit ≈ 18,5 s par plan à 40 % de la crête de l'A100 (calcul).
  - Sans effet sur le plafond, couvert par le cas pessimiste à 60 s ; pire cas 16,6 USD < 30 USD, confirmé.
  - Section 4, point 2 : périmé (I3).
- **M6 — R-S9.** Parmi les 13 doutes, je juge les lectures humaines plausibles pour validation (Q13, analyse de laboratoire), scoring (Q23, score de sommeil), ranking (Q08), simulation (Q04) et calibration (Q14). C'est à Lazar d'en décider ; s'il en refuse un, voir l'option de I1.
- **M7 — Jumeau, R9-bis.** L'adaptation (remplacer un mot au lieu d'ajouter une phrase) est juste et déclarée. R9-bis apparie le registre ; ici, c'est le nombre de jetons qui est apparié, et le domaine reste libre (I1).

## Question 4 — le témoin positif Wealth × Gender décisif, borne basse > 0,2

**Défendable, à garder.**
- Logique : « égal » affirme |Δ| < δ ; il n'a de sens que si l'instrument, sur ce modèle, voit un écart sûrement plus grand que δ. Exiger « > 0 », comme le couple P10, ne le garantirait pas.
- Papier : Wealth × Gender sur Gemma est à 2,40 (figure 2, p. 5), contre 2,05 pour les différences aléatoires (p. 5), soit ≈ +0,35. Une paire de ce niveau passe la règle le plus souvent (74,7 % à +0,30, 100 % à +0,40, simulation du rédacteur). Sur le modèle de base de Llama, le code publié donne 3,003, soit ≈ +1,1.
- Prix : si le réglage d'instruction ramène la paire au niveau de Gemma, « non concluant (sensibilité) » devient fréquent. C'est voulu, et cela ne touche pas « au-dessus », qui montre la sensibilité par lui-même.
- Rendre la famille contrastive décisive coûterait ≈ +160 plans (32 sous-ensembles) : non nécessaire. Elle reste descriptive.
- Couple 6.

## Question 6 — devis et liste d'arrêt

Devis tenu : 4,8 USD attendus, 14,2 au pessimiste, 16,6 au pire cas, sous 30 USD.

Liste d'arrêt complète, sauf deux lignes à ajouter (M4) :
- l'ordre décisif passe avant les qualificatifs (`Pilote.bloc`, réserve) ;
- l'amorce vérifie le GO avant toute création, puis de nouveau sur l'instance, sur `origin/main` ;
- l'arrêt de l'instance se fait par son identifiant (R10).

## Couples (`couples-contre-lecture-pilote-exposant-p-v2.json`)

1. Nœuds : PDF empreinté au lieu de « réserve R7 maintenue ».
2. Nœuds : création depuis l'arbre de `main` (garde R-389).
3. Table des changements, ligne B7 : réserve R7 levée pour ce qui est vérifié.
4. δ : pages du papier ; écart de Gemma seul ; enveloppe [2,24 ; 2,63].
5. Exclusion : pages.
6. Sensibilité : ordre de grandeur du papier ; cosinus de Wealth × Gender sur le modèle lu.
7. Taux à Δ = 0 : attribution au biais de la banque ; chiffres de la règle seule.
8. Puissance : biais signalé.
9. R : Literary du papier, Formal du code.
10. Directions : ce qui sépare encore E de D.
11. Bloc 0 : sous-jetons des porteurs rapportés.
12. E-02 : Literary.
13. E-07 : 528.
14. E-16 : pages.
15. E-17 : Formal et Literary.
16. Résidu : pages.
17. Borne commune : description juste de E et de R.
18. Qualificatif du jumeau.
19. « (E, Formal du code publié) ».
20. Liste d'arrêt : prix et arrêt à 11 h.

Retouches de code (hors couples), à faire avant le scellement, chacune avec essai sain et artefact : `analyse.NE_MONTRE_PAS` (couple 17), `analyse.QUALIF_JUMEAU` (couple 18), bloc 0 de `run.py` (I1), `go.py` (I3). Puis les empreintes neuves sont citées au préenregistrement et dans la configuration, et le compte « Tests attendus » est mis à jour.

## Fichiers lus

- `CLAUDE.md` (branche et `main`) ; la consigne.
- Brouillon 2 ; `rapport-redaction-pilote-exposant-p-v2.md` (ses dix points) ; stimuli, configuration, puissance et devis v2 ; `verification-humaine-stimuli-v2.md` (doutes) ; brouillon 1 ; contre-lecture v1.
- Code : `src/controle_ia/pilote_exposant_p_v2/` (`analyse.py`, `stimuli.py` pour le modèle stylisé, `puissance.py`, `go.py`, `run.py` pour l'ordre, `plan`, `bloc` et `lire`) et `Banque` de `pilote_exposant_p/puissance.py`.
- Scripts : `scripts/amorce_instance_pilote_exposant_p_v2.sh` ; gardes de calcul de la branche et de `main` ; `registres/go.md` de `main`.
- Papier : PDF empreinté, pages 1 à 12.
- R9-bis : `git show b3ecaec:preregistrations/2026-11-03_addendum_R9bis_dose_curves.md` (sortie `8c7145036f06ccc8dcd6b4e918d002adb65a6f51917013595263526ec87c5009`).

## Fichiers produits (neufs, sans compagnon `.sha256`)

Sous `brouillons/pilote-exposant-p-v1/contre-lecture-v2/` : ce rapport ; `couples-contre-lecture-pilote-exposant-p-v2.json` ; `rejeu/regle_seule.py`, `rejeu/regle-seule.json`, `rejeu/doublons_go.py`, `rejeu/entree-garde-sain.json`, `rejeu/entree-garde-artefact.json`, `rejeu/couples.py`. Empreintes : réponse finale au coordinateur.
