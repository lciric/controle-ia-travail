# Relecture par Claude Fable 5.2 (appel direct à l'interface d'Anthropic)

- Outil : `controle_ia.relecture_fable_api_v5` (empreinte du module 052ea1e2c66f8b80b1724db9f0c5afb27a48cc01eac2e1e5210658ca8423bdb8)
- Modèle demandé : `claude-fable-5-2` ; modèle servi : `claude-fable-5-2` ; identifiant du message : `msg_011ChJ5N33DUvCSwfxE5h354`
- Heure (UTC) : 2026-11-22T13:54:46Z
- Réglages : effort `max`, réflexion adaptative à affichage « omitted » (texte de la réflexion ni demandé ni écrit), `max_tokens` 128000, aucune relance, aucun repli vers un autre modèle, budget de tâche 96000 jetons (bêta `task-budgets-2026-03-13` ; cible indicative vue par le modèle, pas une borne : seul `max_tokens` arrête)
- Entrées :
  - consigne : `docs/notes/mathematiques-nouvelles-v1/brouillon-2-fable-v1/consigne-fable-brouillon-3-et-devis-v3-v2.md` — sha256 cb005fff30d62b176975b3e97d6763b39866abb90503e9ba586cd9ba202a8c09 (compagnon : vérifié)
  - correction : `prereg/mathematiques-nouvelles-v1/preenregistrement-pilote-generation-v1-brouillon-2-en-differences.md` — sha256 ba5ddf70dfd01f20c4f60eccbfef89a6170443b25ee855e1c9572b8ce71f1ce4 (compagnon : vérifié)
  - correction : `prereg/mathematiques-nouvelles-v1/devis-pilote-generation-v2-brouillon.md` — sha256 c857e62c1e921cdfc16f1234e54bff2d8dcf1f68bfdb7d8e3dcb96ee1d555ca6 (compagnon : vérifié)
  - correction : `docs/notes/mathematiques-nouvelles-v1/brouillon-2-fable-v1/notes-au-directeur-fable-v1.md` — sha256 c4c04db5aa990ef80543da43b11fde41a9f271f20cc3a30d7e0bd0ddefbe9fbc (compagnon : vérifié)
  - correction : `prereg/mathematiques-nouvelles-v1/calculs-v2/sortie-calculs-devis-pilote-generation-v2.txt` — sha256 724e2b79adf9fd1eaa1c15941e32bb3ba4ce34a7e9aa3c0f5a590bf4b67cd1c5 (compagnon : vérifié)
  - correction : `docs/notes/mathematiques-nouvelles-v1/brouillon-2-fable-v1/copies-sans-nom-v1/releves-prix-et-source-score-apparie-v1-sans-nom-v1.md` — sha256 3dab36f8d5737c2c79a654af33b11d4032624fc3ee067506e3f28ded34e59623 (compagnon : vérifié)
  - correction : `docs/notes/mathematiques-nouvelles-v1/lot-b1-code-v1/note-choix-implementation-lot-b1-v5.md` — sha256 6c71414bc37b33cb1558021d479cb804f1045ff86fabc4a253159f8b10ea2912 (compagnon : vérifié)
  - correction : `docs/notes/mathematiques-nouvelles-v1/lot-b1-code-v1/rapport-essais-r5-lot-b1-v5.md` — sha256 0923bcc2904542e2942270325a3635f6ea236561410af21846254a3f1f94a3e2 (compagnon : vérifié)
  - correction : `docs/notes/mathematiques-nouvelles-v1/brouillon-2-fable-v1/empreintes-code-lot-b1-v5.md` — sha256 5846b0ac2ff1f896217b922443cd467a9e59307cfb86e8f9c27855ad1c0fca1f (compagnon : vérifié)
  - remarques : `prereg/mathematiques-nouvelles-v1/calculs-v2/ecarts-devis-v2-main-contre-script-v1.md` — sha256 0acdc28b5985bb9a5c8ea4e4f44ddc1dc62f48b5962cc6355f4914475922162a (compagnon : vérifié)
  - remarques : `docs/notes/mathematiques-nouvelles-v1/lot-b1-code-v1/verification-corrections-lot-b1-v4.md` — sha256 01a7258dcb3d80307297cbcb89c6044da05a76ce9a4b44d44410b6f9c05613e0 (compagnon : vérifié)
  - avant : `docs/notes/mathematiques-nouvelles-v1/brouillon-2-fable-v1/copies-sans-nom-v1/preenregistrement-pilote-generation-v1-brouillon-sans-nom-v1.md` — sha256 865a773235f95594d19ff320bc2d917bb8bc99ca094f094efb776127f49c9150 (compagnon : vérifié)
- Empreinte de l'invite envoyée : f84784431e2778e5345b3a1aa0e36559ad2595d914962fdbf6bb8af15596d62a
- Jetons : entrée 67923, sortie 22170 (dont réflexion 3951), écriture de cache 0, lecture de cache 0 ; raison d'arrêt `end_turn`
- Coût compté : 1.430184 USD (base : usage ; tarif 8 / 40 USD par million de jetons d'entrée / de sortie)

---
=== DEBUT PREENREGISTREMENT BROUILLON 3 ===
# Préenregistrement — pilote « oracles plantés » du pilier des mathématiques nouvelles — v1, brouillon 3 (complet ; remplace les brouillons 1 et 2)

Non contre-lu, non scellable tant qu'un blanc « À REMPLIR » reste. Aucune lecture de résultat, aucun appel, aucune dépense.

- Auteur : le concepteur (consigne adressée à Claude Fable 5.2). Date : à porter au scellement par `date -u` (je n'ai pas d'horloge).
- Commit du code : **À REMPLIR : COMMIT-CODE**. Base : version 5 (`src/controle_ia/oracles_plantes_v5/`, commit `b1d60ca09f4178491ce4e9499f32c89e4bfc25cb`, 210 essais passés, empreintes dans `empreintes-code-lot-b1-v5.md`, `5846b0ac…`). Mes décisions exigent une **version 6** (§ Mondes, « Changements de code »). Ses empreintes seront portées ici mot pour mot après vérification par le même contre-lecteur.
- Documents qui font foi :
  - ceux du brouillon 1 : plan d'avancée, note de conception du pilier (`94532165…`), N-058 (`854f2724…`), N-045 v2 (`c7b05e39…`), N-053 (`2204256d…`), brouillon 3 de l'essai « preuve formelle contre suite bon marché » (`717259ed…`, § 3.2 et § 3.6), table des valeurs critiques (`fbd77a23…`), sortie des calculs v1 (`5d6175dd…`) ;
  - l'erratum 1 du plan (`1827b680…`) ;
  - les relevés de prix et de source (`a7d9073f…`) ;
  - la note de choix v5 (`6c71414b…`), le rapport des essais R5 v5 (`0923bcc2…`), la vérification de la v5 (`01a7258d…`) ;
  - la sortie du script du devis v2 (`724e2b79…`), la note des écarts (`0acdc28b…`) ;
  - le devis v3, scellé avec ce texte.

## Hypothèse

**Objet.** Le pilier ne peut rien mesurer avant d'avoir trois instruments étalonnés sur des vérités plantées :
1. des **proposeurs** d'énoncés, jugés sur l'oracle d'un monde planté et sur le coût, jamais sur le verdict d'un juge (N-058 ; N-053) ;
2. des **tests de mort** exacts, dont une proposition tuée reste morte ;
3. un **juge de nouveauté**, dont le taux de faux « neuf » est mesuré sur des connus plantés.

Le pilote étalonne les trois, sans Lean, sur des mondes finis à vérité calculable, miniatures des questions Q4 (détection bornée par la variation totale) et Q3 (agrégation sous dépendance adverse) et des domaines D1 et D5 de l'essai. Toute pièce qui présente le pilier cite POPPER, Dwork et al., « The Ladder » (Blum et Hardt) et Co-Scientist. Aucun chiffre n'en est repris ici (R7 : non vérifié).

- **H1 (primaire) — la chaîne « proposeurs + tests de mort » est utilisable.** Sur douze mondes, les proposeurs à modèle, après tests de mort, rendent des énoncés vrais-bornés, non triviaux et non redits à une précision d'au moins 0,25, et retrouvent en moyenne au moins deux des huit vérités plantées par monde. H1′ : ils n'y arrivent pas à ce coût.
- **H2 (secondaire, N-058) — composition.** Deux familles (`claude-opus-5-5` et `gemini-4-argon`, douze propositions chacune par monde) retrouvent plus de vérités par dollar que le témoin « un modèle, vote à k, coût apparié » (Opus, vingt-quatre propositions par monde ; N-045 v2). Complémentaire : pas plus.
- **H3 (secondaire) — l'expérimentateur contre la lecture nue et contre le calcul exact.** Sur 150 énoncés plantés (75 vrais, 38 faux tôt, 37 pièges), le bras S (agent à outil Python en bac isolé, recherche de contre-exemples, relecture par une autre famille) déclare « faux » plus souvent que le bras N (même modèle, un appel, sans outil) sur les faux, à fausses morts bornées sur les vrais. Ses réfutations déclarées ne se vérifient pas toutes en arithmétique exacte. Complémentaire : S ne fait pas mieux que N.
- **H4 (secondaire) — le juge de nouveauté à modèle seul** (`gpt-6.2-astra`). Sur 40 connus plantés reformulés par une troisième famille, il étiquette « non trouvé dans les pièces lues » au-dessus du seuil d'emploi 0,10. Sur 20 énoncés de mondes, neufs par construction, il n'étiquette presque jamais « connu ». Complémentaire : le juge tient le seuil.

**Hypothèses de travail.**
- Lean est absent. La commande `lake comparator` existe dans les sources de Lean v4.35.0 et n'a pas été exécutée.
- La vérité est **bornée** et se calcule exactement.
- « Vivante » veut dire « non tuée jusqu'à N », jamais « vraie ».
- Aucun énoncé réel du programme n'entre dans ce pilote.
- Aucun score n'entre dans un entraînement ni dans une sélection d'agents.

## Prédiction chiffrée et signe attendu

Toutes supposées, écrites pour être démenties. Le dessin ne les vise pas (R3). Réfutation : sortie de l'intervalle ou signe contraire.

- **P1 (H1)** : précision dans [0,20 ; 0,45], centre 0,30. Retrouvées par monde dans [1 ; 3,5] sur 8, centre 2,0. Confiance 0,5. Réfutation forte : précision < 0,10, ou moins d'une retrouvée par monde.
- **P2** : au moins 5 % des propositions valides coïncident avec un piège planté. Signe +, confiance 0,6.
- **P3** : part des valides tuées dans [0,25 ; 0,55] ; part des vivantes triviales ou redites dans [0,30 ; 0,60] ; part « informe » ≤ 0,15.
- **P4 (H2)** : rapport des rendements par dollar dans [0,9 ; 1,8], centre 1,3. Signe + sur la majorité des mondes, confiance 0,55.
- **P5 (H3)** :
  - Δ = r_S − r_N sur les 75 faux ≥ +0,15, centre +0,25 ;
  - rappel de N sur les pièges dans [0,05 ; 0,40] ;
  - fausses morts de N dans [0,10 ; 0,35], de S dans [0,05 ; 0,20] ;
  - fausses morts de N plus hautes sur les vérités « seuil » que sur les autres (signe +, confiance 0,55) ;
  - contre-exemples vérifiés de S : faux tôt dans [0,60 ; 0,95], pièges dans [0,15 ; 0,50] ;
  - réfutations fausses de S dans [0,10 ; 0,40], au-dessus de 0,10 (signe +) ;
  - confiance 0,6.

  La phrase du brouillon 2 « la forme ne révèle plus la strate » est retirée : elle était inexacte (remarque 20).
- **P6 (H4)** : faux « neuf » dans [0,30 ; 0,70], centre 0,45. Strate « célèbre » sous la strate « obscure ». Faux « connu » sur les énoncés de mondes ≤ 0,10. Confiance 0,65.
- **P7 (coût)** : total des appels dans **[115,39 ; 261,41] USD**. Formule : (120 / 164,28) × 157,97 et (260 / 164,28) × 165,17, soit les rapports du brouillon 1 appliqués aux attendus du devis v3 (sortie du script, bloc 8). Attendu 157,97 si la course finit le 30 novembre 2026 au plus tard, 165,17 dès le 1er décembre.
- **P8 (instrument, par construction)** : la batterie exacte tue 100 % des faux tôt et 0 % des vérités sur la banque entière, avant tout appel. Tout écart est un défaut du code (A1).
- **P9 (par construction)** : la règle « forme seule » (faux si seuil littéral ou résidu évité) donne, sur la banque entière **et dans chaque monde** : rappel 1 sur les pièges, 1/2 sur les faux tôt, fausses morts 1/2 sur les vérités. Tout écart est un défaut de plantation (A1).
- **P10 (par construction, nouvelle)** : la règle « borne non naturelle » (faux si seuil dont le côté clos n'est ni 0, ni 1, ni une constante du monde, ou résidu évité) donne rappel 1 sur les pièges, 1/2 sur les faux tôt, fausses morts 1/4 sur les vérités. Tout écart est un défaut de plantation (A1).

## Métrique

Unités : la proposition (H1, H2), l'énoncé planté (H3), l'item jugé (H4) ; le monde pour les appariements de H2.

- **Valide** : conforme au schéma et à la grammaire. Sinon « informe », comptée, hors dénominateur.
- **Morte** : tuée par T2 ou T3, ou par héritage. L'héritage exige un contre-exemple certifié sur la proposition elle-même, jusqu'à 3N, au témoin d'une morte. « Morte » ne veut donc pas toujours dire « fausse sous N ». Le motif est rapporté. **Vivante** sinon.
- **Indéfini** (division par zéro, indice négatif, argument hors domaine) : **contre-exemple**, T2 tue. Un énoncé universel doit avoir un sens à chaque instance. Les consignes le disent.
- **Hors capacité** : « non décidée », ni morte ni vraie-bornée.
- **Triviale** : close à vrai par le normaliseur, ou instance d'un axiome servi (T4).
- **Redite** : trois étages de T5 contre les vivantes antérieures du même proposeur ou de la même configuration :
  1. même forme normale ;
  2. table de vérité sur les atomes ;
  3. même profil jusqu'à 3N dans le monde et trois mondes perturbés, positions « hors capacité » écartées, profil informatif exigé.

  **Exception** : une proposition retrouvée (ci-dessous) n'est jamais redite par l'étage 3 seul. Raison : deux vérités structurelles distinctes peuvent coïncider par profil (racine d'essai 24). Le compte des redites par l'étage 3 seul et la précision avec « redite = étages 1 et 2 » sont rapportés en sensibilité.
- **Vraie-bornée** : vraie à toute instance jusqu'à N.
- **Retrouvée** : vraie-bornée et égale à une vérité plantée par l'étage 1 ou 2. Le compte par empreinte seule est en sensibilité.
- **Piégée** : égale à un piège planté par l'étage 1 ou 2.
- **Précision** : (vivantes ∧ vraies-bornées ∧ non triviales ∧ non redites) / valides. **Retrouvées par monde** : moyenne des vérités distinctes retrouvées, par monde et par configuration.
- **Rendement par dollar** : retrouvées / dollars mesurés par appel aux prix relevés (devis v3, § 1), Argon au prix du jour de l'appel. Différence par monde Y_multi(w) − Y_témoin(w), à 24 propositions par configuration.
- **H3** :
  - r_b = P(« faux » | faux) et φ_b = P(« faux » | vrai), b ∈ {S, N}, par strate (faux tôt, piège ; seuil, non-seuil) ;
  - Δ = r_S − r_N, apparié ;
  - **contre-exemple vérifié** : instance avancée par S, scellée sur la machine jetable, puis vérifiée exactement par T6 chez le conteneur de confiance (le bac ne vérifie rien) ;
  - **réfutation fausse** : réfutation déclarée sans instance vérifiée, rapportée aux réfutations déclarées.
- **H4** : faux « neuf » par strate (célèbre, obscur) ; faux « connu » ; trois étiquettes, jamais « nouveau ».
- **Fuite de style** : aire sous la courbe du classifieur de style, faux contre vérités. Elle est rapportée par strate, par pli, et **hors textes déjà vus à l'apprentissage**. L'aire qui fait foi est la plus grande des aires par strate, hors textes déjà vus, scores mis en commun. Les aires par pli sont en description.
- **Réserve (remarque 15)** : l'héritage ne couvre que les reformulations de même préfixe. Elle est portée dans toute lecture des retrouvées et des motifs de mort.
- **Intervalles** : Clopper–Pearson exact, unilatéral à 97,5 %, pour les taux. Percentiles à 90 % d'un rééchantillonnage par monde (2 000 tirages) pour la précision et le rendement. Score apparié pour Δ.

## Seuil

Fixés avant toute donnée.

- **H1** :
  - « utilisable » si précision ≥ 0,25, borne basse ≥ 0,15 et retrouvées ≥ 2,0 pour une configuration au moins ;
  - « non utilisable » si borne haute < 0,25, ou retrouvées < 1,0 pour les deux ;
  - sinon non concluant.
- **H2** : test exact des signes. « Deux familles supérieures » si au moins 10 différences positives sur 12 (niveau unilatéral 0,0193) ; « témoin supérieur » si au moins 10 négatives ; sinon non concluant. Moins de 8 mondes sans ex æquo : description seulement.
- **H3** : δ = 0,20. Valeurs critiques à n = 75 : z*(B > 0) = 2,2504 ; z*(H < δ) = 2,2754 ; z*(B ≥ δ) = 2,3099 (`fbd77a23…`), chacune à 0,0125 par queue.
  - « S ajoute » si S(0) ≥ 2,2504 ;
  - « gain d'au moins δ » si S(δ) ≥ 2,3099 ;
  - « S n'ajoute pas δ » si S(δ) ≤ −2,2754.

  Borne haute de φ_S ≤ 0,10 exigée pour « filtre utilisable avec vérification » (au plus 2 événements sur 75). Réfutations fausses : seuil 0,10. Les strates sont lues en description.
- **Seuil de fuite de style (nouveau, convention supposée)** : aire qui fait foi ≤ **0,75**, mesurée au rejeu sur la banque réelle, avant tout appel.
  - Sous le seuil : H3 se lit comme écrit.
  - Au-dessus : la course a lieu, mais H3 n'affirme que sur les contre-exemples vérifiés (critères gelés). La comparaison des verdicts passe en description.
- **H4** : seuil d'emploi 0,10. « Tient » exige 0 événement sur 40 (borne haute 0,088). Faux « connu » > 0,10 sur 20 : rapporté en tête.
- **Multiplicité** : H1 seule primaire, à 0,05 unilatéral. Aucune correction entre hypothèses ; le rapport le dit.

## Plan d'analyse

- **Trois lieux (erratum 1).**
  - *Le bac* : seul le code écrit par le bras S y tourne. Aucun réseau, identité dédiée, dossier neuf par énoncé, détruit ensuite.
  - *La machine jetable* : l'orchestrateur du bras S seulement. Ni clé, ni vérité, ni générateur, ni évaluateur. Elle rend des sorties scellées, jamais un verdict.
  - *Le conteneur de confiance* (la session du chantier) : générateur, clés, évaluateur, normaliseur, registre de lignée, issues, analyse.
- **Clés.** Tirées après le scellement, scellées et versées dans la même commande. Jamais lues par un agent qui sert ou juge, jamais servies, jamais sur la machine jetable. La branche n'en garde que les empreintes.
- **Banque.** 12 mondes, 4 par famille. Par monde : 8 vérités, 4 faux tôt, 4 pièges, 10 témoins (5 triviaux, 5 grossiers). 192 analysables, 312 plantés.
- **Sous-banque servie à S et à N.** 150 analysés ; 48 témoins hors analyse (2 triviaux et 2 grossiers par monde, enfant [2]) ; 10 seconds services (enfant [6]). 208 items par bras, sous identifiants tirés. **Chaque item est jugé dans un contexte neuf, sans voir les autres** (remarque 20).
- **Rôles.**
  - proposeurs : `claude-opus-5-5` et `gemini-4-argon` ;
  - témoin, S et N : `claude-opus-5-5` ;
  - relecteur de S et reformulateur : `kimi-k3.1-pro` ;
  - juge : `gpt-6.2-astra`.

  Un appel de fumée par modèle (quatre) a lieu après le GO, avant tout autre appel.
- **Repli R1, fixé ici.**
  - Astra échoue : juge Kimi, reformulateur Argon en contexte neuf, réserve de famille rapportée.
  - Kimi échoue : relecteur et reformulateur Argon, juge Astra.
  - Les deux échouent : H4 non courue, relecteur Argon.
  - Aucun autre repli.
- **Ordre.**
  1. fumée ;
  2. banque plantée, clés scellées, rejeu sans appel (P8, P9, P10, aire de style) ;
  3. banque de connus, clé scellée ;
  4. script d'analyse scellé ;
  5. course par blocs de mondes (proposeurs, tests de mort à l'arrivée, S et N, juge) ;
  6. sorties scellées ;
  7. clés ouvertes ;
  8. analyse ;
  9. lecture par un agent neuf (R13).

  Ce pilote passe avant le pilote « preuve formelle contre suite bon marché ». La dépense attend le GO sur le devis v3 contre-lu.
- **Aveuglement.** Les proposeurs reçoivent les définitions d'un monde, jamais la clé ni les sorties de l'autre configuration. S et N ne voient ni la clé ni l'autre bras. Le juge ne voit ni l'origine ni la clé.
- **Tests de mort**, chez le conteneur de confiance, par le code figé, sur sorties scellées :
  - T1 forme ;
  - lignée (héritage) ;
  - T2 contre-exemple par énumération jusqu'à N ;
  - T3 vacuité ;
  - T4 trivialité ;
  - T5 redite ;
  - T6 vérification exacte des contre-exemples de S, jusqu'à 3N.

  Toute mort par contre-exemple de S passe par `appliquer_t6`. Le registre de lignée est unique, scellé en fin de course, et sa tête est consignée au manifeste (exigence au lot B3).
- **Score apparié (H3)**, défini par ses principes, sans attribution :
  - q = [√(B² − 4AC) − B] / (2A), avec A = 2n, B = −n₁₀ − n₀₁ + (2n − n₁₀ + n₀₁)Δ₀, C = −n₀₁Δ₀(1 − Δ₀) ;
  - S(Δ₀) = (n₁₀ − n₀₁ − nΔ₀) / √(n(2q + Δ₀(1 − Δ₀))) ;
  - q est le maximum de vraisemblance sous Δ = Δ₀, et S se réduit à McNemar en Δ₀ = 0.

  En appui seulement : le code R `contingencytables` 3.1.1 (`5248271a…`, lignes 83 et 93 à 96) porte la même forme.
- **Méthode commune (décision du directeur).**
  - chaîne de raisonnement écrite pour chaque lecture ;
  - tout mécanisme invoqué est éprouvé sur des objets de contrôle où l'analogue de l'hypothèse est faux (témoins, faux tôt, bases de forme) ;
  - le premier pas non justifié est nommé ;
  - relecteurs hostiles et aveugles, chacun affecté à un mode d'échec (fuite, forme, comptage, statistique) ;
  - re-preuve par un agent qui ne reçoit que l'énoncé ;
  - agents de côté ;
  - le passage d'une table à un théorème général est écrit comme question, non comme résultat.
- **Secondaires rapportées toutes** : parts par famille ; coûts unitaires ; motifs de mort ; stabilité sur les 10 seconds services ; refus ; temps mural ; base « grammaire aléatoire » ; bases « forme seule » et « borne non naturelle » ; collisions de lignée ; comptes par strate de forme ; nombre de textes plantés identiques entre mondes, par strate.
- **Sensibilité** : exclusion appariée des pannes ; Argon à 2 / 10 et 4 / 20 ; H3 avec « S ne tue que par contre-exemple vérifié » ; redite aux étages 1 et 2.
- **Graines (R9).** Racine `numpy.random.SeedSequence(À REMPLIR : GRAINE-RACINE)`. Enfants :
  - [0] mondes, dont (0, w, 0) pour la définition et (0, w, 1) pour les mondes perturbés ;
  - [1] plantation ;
  - [2] sous-banque et témoins servis ;
  - [3] identifiants et ordre ;
  - [4] ordre des mondes et des configurations ;
  - [5] rééchantillonnage ;
  - [6] seconds services ;
  - [7] connus ;
  - [8] audit humain ;
  - [9] base « grammaire aléatoire » ;
  - **[10] scindé (remarque 21)** : (10, 0) plis du classifieur de style, (10, 1) audit de symétrie.
- **Racine refusée à la plantation (règle écrite d'avance).** La même commande retire une racine. Toutes les racines tirées et le motif de chaque refus vont au manifeste. Au plus trois tirages ; au-delà, arrêt et retour au concepteur. Aucun appel n'a lieu avant une plantation conforme : la sélection ne porte que sur la plantabilité, et le rapport le dit.

## Critères de lecture gelés

| issue observée | verdict | lecture écrite d'avance |
|---|---|---|
| H1 : précision ≥ 0,25, borne basse ≥ 0,15, retrouvées ≥ 2,0 (une configuration) | confirmé | chaîne utilisable sur mondes plantés à ce coût ; rien sur des énoncés réels ni sur la nouveauté |
| H1 : borne haute < 0,25, ou retrouvées < 1,0 pour les deux | réfuté | la génération libre sur cibles réelles est prématurée ; reconception des proposeurs |
| H1 : autre | non concluant | effectif nécessaire rapporté ; pas de relance sans devis ni GO |
| H2 : ≥ 10 positives / ≥ 10 négatives / autre | deux familles / témoin / non concluant | composition du pilote 2 sur cet oracle et le coût seulement |
| H3, aire ≤ 0,75 : S(0) ≥ z* et borne haute de φ_S ≤ 0,10 | S ajoute, filtre utilisable avec vérification | S entre comme proposeur de contre-exemples vérifiés ; il ne tue jamais seul si ses réfutations fausses dépassent 0,10 |
| H3 : S(0) ≥ z*, mais rappel sur les pièges non porté par des contre-exemples vérifiés | S ajoute en verdict, pas en preuve | S ne tue que par contre-exemple vérifié |
| **H3, aire > 0,75** | H3 lue sur les contre-exemples vérifiés seulement | affirmable : « S produit des contre-exemples vérifiés sur telle part des faux, N aucun par construction » ; non affirmable : « S discerne mieux que N » |
| H3 : S(δ) ≤ −z*(H < δ) | S n'ajoute pas δ | la lecture nue suffit ici |
| H3 : borne haute de φ_S > 0,10 | S non utilisable comme filtre | rapporté en tête |
| H4 : borne haute du faux « neuf » > 0,10 | juge seul non employable | plancher mécanique exigé au pilote 2 |
| H4 : 0 sur 40 et faux « connu » ≤ 0,10 | juge tient sur cette banque | audit de symétrie avant lecture |
| Fumée en échec | R1 appliqué tel qu'écrit | réserve de famille en tête |
| Symétrie : H1 confirmée avec précision > 0,60, ou H4 tenue, ou rapport de H2 > 2, ou H1 réfutée avec précision < 0,05 | audit avant remise | 20 vivantes relues (enfant [8]) ; contrôle de fuite des clés ; classifieur de style sur les connus reformulés (enfant (10, 1)) |

## Liste d'arrêt

Chaque garde est éprouvée sur un cas sain et sur un artefact (R5). Aucun repli silencieux.

- **A1** : batterie ou plantation non conforme (P8, P9, P10 ; comptes de forme par monde) ⇒ aucun lancement ; correction en version neuve.
- **A2** : modèle servi différent de l'identifiant demandé ⇒ arrêt de la configuration.
- **A3** : refus sur plus de 10 % des 20 premiers appels d'un rôle ⇒ arrêt du rôle.
- **A4** : pour un bras, 3ᵉ alerte sur les 24 témoins triviaux servis, ou 3ᵉ manque sur les 24 grossiers ⇒ arrêt.
- **A5** : plus de 15 % d'informes pour un proposeur sur les trois premiers mondes ⇒ arrêt de ce proposeur.
- **A6** : dépense + appels en vol + prochain appel > plafond ⇒ plus de lancement. Réserve 5,93 USD (devis v3, § 3). Plafond : **À REMPLIR : PLAFOND-GO**.
- **A7** : plafond de 1,50 USD par item pour l'agent S ⇒ verdict « plafond », compté « non tué ».
- **A8** : contrôle par empreinte, chez le conteneur de confiance, des journaux de tout contexte servi et de l'inventaire de la machine jetable. Clé, texte ou instance de clé, générateur ou évaluateur présents ⇒ arrêt, course invalidée.
- **A9** : minuterie de destruction à 48 heures, plafond machine 65 USD, inscription dans `registres/arrets.md`.
- **A10** : **À REMPLIR : ÉCHÉANCE**.
- **A11** : aucun appel facturé sans GO valide dans `registres/go.md`.
- **A12** : sortie invalide ⇒ « informe », jamais corrigée à la main.
- **A13** : appel au juge de plus de 272 000 jetons d'entrée refusé (prix non relevé au-delà).

**À REMPLIR : ESSAIS-R5** pour A2 à A13 (harnais d'appels, lot B3). A1 est éprouvée en version 5 (rapport `0923bcc2…`) et à rejouer en version 6.

## Mondes plantés et tests de mort

- **Familles** (définitions tirées par graine, rationnels exacts).
  - F1, détection finie : K de 4 à 8 issues, lois P et Q à support plein, P ≠ Q, T pas indépendants.
  - F2, agrégation à marges fixées : 2 ou 3 moniteurs binaires, pire et meilleur cas exacts sur les couplages, règles OU, ET, MAJ. L'indice entier est le nombre de tours indépendants (`pfa_t`, `prap_t`).
  - F3, suites récurrentes u, w, v à paramètres tirés.
- **Paramètres gelés** (note v5, § 1) : bornes N avec F1 = 4, F2 = 10, F3 = 15 ; capacités ; profil à 3N ; trois mondes perturbés ; base aléatoire à 24 par monde, profondeur 3.
- **Grammaire** : langage fermé à mots-clés français ASCII. « NAT » n'est admis que dans le préfixe universel de tête ; tout autre quantificateur est borné. Schéma d'un proposeur : `enonce`, `ce_qui_le_tuerait` (texte libre, non analysé), `confiance`. Sortie de S : `verdict` (« vrai », « faux », « indecis »), `contre_exemples`, `raison`.
- **Plantation par monde** : 8 vérités (4 de forme seuil), 4 faux tôt (2 de forme seuil : n₀ tiré dans [1 .. N], c = E(n₀)), 4 pièges (seuil ou résidu évité ; faux à une instance certifiée dans ]N .. 3N]), 10 témoins. Parmi les seuils, 6 sur 10 sont faux.
- **Gabarits « seuil » des vérités (remarque 22) : je les prends à mon compte, un par un.** « k » désigne un indice tiré par monde dans [2 .. N] (enfant [1]) ; le littéral est la valeur exacte à k.
  - F1-a `vt(t) < 1` : approuvé (support plein).
  - F1-b `t >= 1 implique vt(t) > 0` : approuvé (P ≠ Q).
  - F1-c : **remplacé** par `t >= k implique vt(t) >= vt(k)`, en littéral (vt croît en t).
  - F1-d : **remplacé** par `t >= k implique puissance(A, t, 1) >= ` sa valeur à k.
  - F2-a `pfa_t(OU, t) < 1` : approuvé.
  - F2-b `t >= 1 implique prap_t(OU, t) > 0` : approuvé.
  - F2-c : **remplacé** par `t >= k implique pfa_t(ET, t) >= ` sa valeur à k.
  - F2-d : **remplacé** par `t >= k implique pfa_t(OU, t) >= ` sa valeur à k (repli : `prap_t(OU, …)`).
  - F3-a `u(n) > 0` : approuvé.
  - F3-b `n >= 1 implique w(n) >= 1` : approuvé.
  - F3-c, résidu absent d'une période entière (module premier à QU dans [3 .. 40]) : approuvé.
  - F3-d : **remplacé** par `n >= k implique v(n) >= v(k)`, en littéral.

  Raison des cinq remplacements : 1 − (1 − x)^t, vt et v croissent, donc la raison générale tient pour tout k. Le littéral à k est alors un grand rationnel propre au monde, comme celui des pièges, et le texte ne se répète plus d'un monde à l'autre.
- **Autres gabarits, approuvés.**
  - Vérités non seuil : F1 Scheffé, sous-additivité, couplage, Le Cam ; F2 Fréchet (union), Markov, espérance, encadrement par l'indépendance ; F3 Cassini, addition, duplication, période modulaire.
  - Faux tôt non seuil : ceux de la note v5, ligne 52.
  - Pièges : ceux de la note v5, ligne 34.
  - Le retrait des vérités de la version 4 listées à la remarque 22 est approuvé.
- **Certification.**
  - Vérité : vivante, vraie-bornée, non triviale, non tuée jusqu'à 3N, non redite **par les étages 1 et 2** d'une vérité plantée avant elle. L'étage 3 n'est pas appliqué entre vérités plantées. Raison : une vérité structurelle n'est jamais une redite ; l'étage 3 n'y apporte que des coïncidences (racine 24).
  - Faux tôt : tué par T2.
  - Piège : vivant, vrai-borné, non trivial, tué à 3N, revérifié par T6.
  - Un gabarit non certifiable lève l'arrêt et revient au concepteur.
- **Mondes perturbés** : tirés distincts du monde réel et distincts entre eux par leurs paramètres (rejet et nouveau tirage sur le flux (0, w, 1)).
- **Une proposition tuée reste morte.** La mort est héritée sous normalisation, dans la limite de la remarque 15. Aucune résurrection.
- **Changements de code exigés (version 6).**
  1. cinq gabarits à indice k tiré (F1-c, F1-d, F2-c, F2-d, F3-d) ;
  2. étage 3 non appliqué entre vérités plantées à la plantation ;
  3. mondes perturbés distincts ;
  4. exception « retrouvée » dans la redite, et comptes de sensibilité ;
  5. graines (10, 0) et (10, 1) ;
  6. règle « borne non naturelle » contrôlée au rejeu et entrée en A1 (P10) ;
  7. aire par pli et hors textes déjà vus ; compte des textes identiques entre mondes ;
  8. liste « provisoire » du fichier de paramètres vidée, sauf les réglages du classifieur ;
  9. balayage des 42 racines rejoué, racine 24 comprise.

## Bases à battre

- **Grammaire aléatoire** (processeur, enfant [9]) : 24 énoncés par monde. Une configuration qui ne la bat pas d'au moins 0,15 en précision n'est pas « utilisable ».
- **Témoin « vote à k, coût apparié »** : base de H2.
- **Lecture nue** (N) : base de H3.
- **Règles « forme seule » et « borne non naturelle »**, et classifieur de style (processeur, 0 USD) : bases du bras N sur les pièges.
- **Suite bon marché** : mesurée ici ; base que Lean devra battre au pilote 2.
- **Plancher mécanique de normalisation** du juge, rapporté à côté du juge à modèle.

## Antériorité (R8)

Résultat : **À REMPLIR : ANTÉRIORITÉ**.

Questions :
1. La génération de conjectures filtrée par contre-exemples mesure-t-elle son rendement sur des mondes plantés à vérité calculable ?
2. La contamination des bancs de preuve et de conjectures est-elle documentée et stratifiée ?
3. Un juge de nouveauté à modèle a-t-il été mesuré sur des connus reformulés ?
4. Les pièges « vrais jusqu'à N » servent-ils déjà d'épreuve ?
5. La « vérité plantée pour juger un proposeur » est pratiquée dans les bancs de criblage séquentiel : à citer, non à revendiquer.

**Protocole P**, avant le scellement, par un lecteur d'une autre lignée que les proposeurs (ni Opus, ni Argon) :
1. Par question, trois requêtes au moins sur deux index publics. Requêtes, date et nombre de réponses sont consignés.
2. Au plus huit pièces par question, plus les travaux qui les citent. Chaque PDF est versé avec son empreinte.
3. Chaque constat est cité à la page. Sans page, il est « non vérifié ».
4. Sortie par question : « collision datée » (avec la réduction écrite), ou « non trouvé selon le protocole P, à la date D ».

Une absence ne prouve aucune nouveauté. Ce pilote n'en revendique aucune. La lecture par étages du directeur s'appliquera aux pilotes suivants.

## Pièces à remplir

- COMMIT-CODE (version 6, empreintes mot pour mot) ;
- GRAINE-RACINE ;
- PLAFOND-GO ; ÉCHÉANCE ;
- ANTÉRIORITÉ ;
- **CONSIGNES** : écrites par le concepteur après la vérification de la version 6, contre-lues par un Opus 5.5 neuf, scellées avant le tirage de la graine. Elles disent la borne N, la vérité bornée, « indéfini = contre-exemple », le schéma de sortie, « l'énoncé peut être vrai ou faux », un contexte neuf par item. Elles ne disent rien des pièges ni des proportions.
- ESSAIS-R5 (A2 à A13) ;
- SCRIPT-ANALYSE (lot B3, scellé avant la course) ;
- CONTRE-LECTURE.

## Contre-lecture

**À REMPLIR : CONTRE-LECTURE** — Opus 5.5 neuf. Lui donner ce brouillon, le devis v3, l'erratum 1, les relevés, la note v5, la vérification de la v5, la note des écarts. Puis vérification des corrections par le même contre-lecteur.

## Écarts au brouillon 1

- Trois lieux ; clés et tests de mort chez le conteneur de confiance (erratum 1).
- Juge `gpt-6.2-astra` ; identifiants et prix relevés ; R1 fixé avec le cas « Kimi manque » ; fumée.
- Gabarits partagés entre strates ; P9 et P10 ; cinq gabarits à indice k (version 6).
- P1 : retrouvées, centre 2,5 → 2,0. P5 : intervalles ajoutés, phrase sur la forme retirée. P7 : [115,39 ; 261,41].
- Redite à trois étages (profil à 3N, mondes perturbés distincts) ; exception « retrouvée » ; « retrouvée » aux étages 1 et 2.
- Héritage de mort par témoin certifié ; « indéfini = contre-exemple ».
- Plantation : étage 3 non appliqué entre vérités ; règle de retirage d'une racine refusée.
- Seuil de fuite de style 0,75 et lecture conditionnée de H3 ; un contexte neuf par item.
- Sous-banque de 208 items ; A4 réécrite ; A6 à réserve 5,93 ; A8 étendue ; A13 neuve.
- Graines [9] et [10], cette dernière scindée en (10, 0) et (10, 1).
- Score apparié sans attribution ; méthode commune ; protocole P.
- Blancs retirés : BORNES-N, IDENTIFIANTS-MODÈLES, ACCÈS, PRIX-VÉRIFIÉS, source du score, GÉNÉRATEUR-DE-MONDES, CLÉS-SCELLÉES.
=== FIN PREENREGISTREMENT BROUILLON 3 ===

=== DEBUT DEVIS V3 ===
# Devis — pilote « oracles plantés » — v3 (remplace le devis v2, `c857e62c…`)

Aucun GO demandé par ce texte. Montants en USD. Chaque chiffre vient de la sortie du script v2 (`724e2b79…`, bloc cité) ou est nommé « supposé ». La version 6 du code et sa vérification coûtent 0 USD d'appels.

## 1. Prix (entrée / sortie par million de jetons ; relevés du 22 novembre 2026, `a7d9073f…` ; bloc 0)
- `claude-opus-5-5` : 4 / 20.
- `gemini-4-argon` : 2 / 10 jusqu'au 30 novembre 2026, 4 / 20 dès le 1er décembre.
- `kimi-k3.1-pro` : 2 / 10.
- `gpt-6.2-astra` : 8 / 40. Au-delà de 272 000 jetons d'entrée, le prix n'est pas relevé : l'appel est refusé (A13).
- Cache non compté ; raisonnement compté comme sortie. Pages relevées sans compte.
- Machine : 0,28 l'heure observé, borne haute 1,30 (repris du v1, supposés).

## 2. Calcul
Profils de jetons : **supposés**, repris du v1, à remplacer par la mesure.

**Effectifs (bloc 1).** 432 propositions Opus, 144 Argon. 208 items par bras, soit **58 appels neufs** par rapport au v1, dont 48 énoncés neufs (les témoins) et 10 seconds services. 40 reformulations, 60 jugements.

**Coûts unitaires, bas / attendu / pire (bloc 2).**
- Proposition Opus : 0,042 / 0,10 / 0,32. Argon : 0,021 / 0,05 / 0,16 à 2 / 10, comme Opus à 4 / 20.
- Item S : 0,156 / 0,308 / 1,272. Le plafond de 1,50 borne l'agent seul ; il n'est atteint dans aucun scénario (agent au pire 1,20).
- Item N : 0,052 / 0,136 / 0,496.
- Reformulation Kimi : 0,028 / 0,042 / 0,096.
- Jugement Astra : 0,128 / 0,224 / 0,576.

**Fumée (bloc 3).** Un appel par modèle, quatre appels d'au plus 1 000 / 1 000 jetons. Borne haute 0,096 (Argon à 2 / 10) ou 0,108 (à 4 / 20). Les totaux gardent le forfait **supposé** de 0,10, à 0,008 près.

**Postes, bas / attendu / pire (bloc 4).**
- P1 connus : 8,80 / 15,12 / 38,40.
- P2 proposeurs : 21,17 / 50,40 / 161,28 (Argon à 2 / 10) ; 24,19 / 57,60 / 184,32 (à 4 / 20).
- P3 bras S : 32,45 / 64,06 / 264,58. Bras N : 10,82 / 28,29 / 103,17.
- **Total des appels, course finie le 30 novembre au plus tard : 73,33 / 157,97 / 567,52.**
- **Total des appels, dès le 1er décembre : 76,36 / 165,17 / 590,56.**
- Course à cheval sur les deux dates : entre les deux colonnes ; écart maximal 3,02 / 7,20 / 23,04.
- P4 machine : 3,36 / 6,72 / 62,40.
- Appels + machine : 76,69 / 164,69 / 629,92 (30 novembre) ; 79,72 / 171,89 / 652,96 (1er décembre).

**Repli R1, à l'attendu (bloc 5).**
- Astra échoue : juge Kimi, −10,08 ; reformulateur Argon, +0,00 à 2 / 10 et +1,68 à 4 / 20.
- Kimi échoue : +0,00 à 2 / 10, +7,50 à 4 / 20.
- Les deux échouent : total 142,85 (2 / 10) ou 155,88 (4 / 20).

**Lignes conditionnelles, attendu, Argon à 4 / 20 (bloc 7).**
- Banque de connus refaite : 15,12.
- Un monde régénéré et rejoué : 12,50.
- Attendu avec les deux : **192,79** (184,99 à 2 / 10).

## 3. Plafonds proposés (bloc 7)
- **Réserve des appels en vol : 5,93.** C'est la logique v1 : trois agents S au plafond avec leur relecteur au pire, deux propositions au pire, un jugement au pire.
- **Plafond d'appels** : 192,79 × 1,5 + réserve = 294,90 sur valeurs exactes (script), arrondi à la dizaine supérieure : **300**. Le plafond est le même avec l'une ou l'autre réserve (script). La coupure A6 joue avant le pire cas.
- **Plafond machine : 65**, soit 48 h × 1,30 = 62,40, arrondi aux 5 supérieurs (règle désormais écrite).
- Somme des plafonds : 365. Ce n'est pas un attendu.

## 4. Intervalle de P7
[115,39 ; 261,41]. Formule : (120 / 164,28) × 157,97 et (260 / 164,28) × 165,17 (bloc 8). Le bas, le pire et le plafond en sortent. L'attendu, les replis et l'attendu avec conditionnelles y tombent.

## 5. Machine et environnement
- La machine louée ne porte que l'orchestrateur du bras S et le bac (réseau coupé, dossier neuf par énoncé, identité dédiée).
- Ni clé, ni vérité, ni générateur, ni évaluateur n'y montent.
- Générateur, tests de mort, normaliseur, registre et analyse tournent chez le conteneur de confiance, à 0 USD.
- Les 12 / 24 / 48 heures sont l'enveloppe du v1, **non réestimée** alors que ces tâches en sortent : c'est une borne haute supposée.

## 6. Sensibilité, total des appels à l'attendu (bloc 6)
- Juge Astra : 157,97 (Argon à 2 / 10) ; 165,17 (à 4 / 20).
- Juge Kimi (R1) : 147,89 ; 156,77.
- Postes dominants : bras S, puis proposeurs, à l'attendu comme au pire.

## 7. Positions sur les écarts du rejeu
- **+0,84 du § 5 du v2** : accepté. La phrase était fausse ; le surcoût est 0,00.
- **Fumée** : accepté. Quatre modèles, borne 0,108, forfait nommé supposé.
- **Réserve** : accepté. 5,93 remplace 5,72, parce que la formule du v2 oubliait le relecteur.
- **294,91** : accepté. 294,90 sur valeurs exactes, sans effet sur le plafond.
- **Plafond machine** : accepté. La règle d'arrondi est écrite.
- **Arrondis au centime** : acceptés tels quels.
- **Incohérences 1 à 10** : toutes acceptées et corrigées.
  1. P7 a sa formule (§ 4).
  2. « 58 appels neufs », non « 58 énoncés neufs ».
  3. Le plafond par item borne l'agent seul et ne joue dans aucun scénario.
  4. Quatre appels de fumée, un par modèle.
  5. Les trois cas de R1 sont chiffrés.
  6. Les heures de machine ne sont pas réestimées, et c'est dit.
  7. La ligne « appels + machine » est rétablie.
  8. **Le bas prend le juge Astra** : il n'est pas comparable au bas du v1, qui prenait Kimi.
  9. Le profil bas du juge est « repris » du script v1, non « reconstitué ».
  10. La course à cheval est bornée.
- **Refusé : rien.**

## 8. Hors devis, et à vérifier avant le GO
- Hors devis : relecture humaine et temps des agents (comme au v1) ; protocole P, qui demande un devis s'il fait des appels.
- À vérifier avant le GO :
  1. rejeu de ce v3 par script ;
  2. profils de jetons sur un monde témoin ;
  3. le harnais compte les jetons, vérifie l'identifiant servi et applique A13 ;
  4. le plafond retenu.
=== FIN DEVIS V3 ===

=== DEBUT NOTES AU DIRECTEUR ===
**Décisions qui changent une prédiction, un seuil ou le code**

1. **Version 6 du code exigée.** COMMIT-CODE reste un blanc ; la liste des neuf changements est au § Mondes. Une vérification neuve et un rejeu des 42 racines sont à faire.
2. **Racine refusée : option (b), plus une part de (c) et (d) en dernier recours.**
   - (b) : l'étage 3 n'est plus appliqué entre vérités plantées.
   - (c) : les mondes perturbés sont tirés distincts du monde réel.
   - (d) : règle de retirage, trois tirages au plus.
   - J'écarte (a) : la coïncidence vient du test, pas du gabarit.
   - Le constat « la même redite fausse toucherait un proposeur » est traité : une proposition retrouvée n'est jamais redite par l'étage 3 seul.
   - Aucun intervalle de prédiction ne change.
3. **Fuite de style : les deux à la fois.**
   - Les gabarits changent : cinq seuils « valeur à k tiré » donnent aux vérités de grands littéraux propres au monde.
   - Un seuil d'emploi est fixé : aire ≤ 0,75, hors textes déjà vus. C'est une **convention supposée, à valider par vous**. Au-dessus, H3 n'affirme plus que sur les contre-exemples vérifiés.
   - **Je n'ai pas éprouvé que la version 6 passe sous 0,75.** Les pièges n'ont toujours pas de borne naturelle (P10 le mesure : fausses morts 1/4), et les grands modules premiers des résidus évités restent propres aux pièges de F3.
4. **Remarque 22** : sept gabarits seuil approuvés, cinq remplacés. Les autres gabarits et les retraits de la version 4 sont approuvés.
5. **Remarque 20** : acceptée. La phrase de P5 est retirée, P10 est ajoutée, chaque item est jugé en contexte neuf.
6. **Remarque 21** : acceptée, sous-enfants (10, 0) et (10, 1).
7. **Remarque 23** : acceptée, aire par pli et hors textes vus.
8. **Écarts de la note v5, § 9** :
   - P9 monde par monde : adopté dans le texte ;
   - A2 à A13 : restent au lot B3 ;
   - les deux autres sont tranchés aux points 2 et 3.
9. **P7** passe à [115,39 ; 261,41], avec sa formule. **A6** : réserve 5,93.

**Nœuds qui vous reviennent**

- Le seuil 0,75. L'alternative plus dure est une version 7 avec des pièges à borne naturelle ; je ne sais pas si elle est faisable dans les trois familles.
- La faisabilité des cinq gabarits à k tiré n'est pas éprouvée. Si la plantation les refuse, cela me revient, sans repli silencieux.
- La règle de retirage sélectionne les racines plantables. Je la crois sans effet sur les hypothèses (aucun appel avant), mais c'est une sélection : à valider.
- Plafond (300 proposé), échéance, exécutant du protocole P.
- Le devis v3 n'ajoute aucun calcul à la main hors P7, repris du bloc 8 ; il reste à rejouer par script.
=== FIN NOTES AU DIRECTEUR ===
