# Rapport de rédaction — pilote de l'exposant p (v1, brouillon 2 ; code v2)

Rédigé le 4 novembre 2026, de 01:35 à 02:25 UTC (`date -u`), par le rédacteur neuf du brouillon 2 (sous-agent ; je n'ai écrit ni le brouillon 1, ni son code, ni sa contre-lecture). Consigne : `brouillons/reprise-conv-audit-2026-11-02-nuit/prompts-sous-agents/pilote-exposant-p-redacteur-brouillon2-prompt.md` (`99049a75d35111367b077a96baf95d93f9fcdefb95db0f3f7526e2bc558bcdd6`, compagnon concordant), sous l'avenant `brouillons/reprise-fusionnee-2026-11-04/avenant-relances-v1.md` (`d4f14478cd9752de38c92129c3127f5fbba1f78ae880e47f77f7a72ecb9891b1`, concordant), sections « Pour les trois » et « Pilote de l'exposant p ». Branche `canal/conv-audit-n04`, tête `e7726dce`.

Respecté :
- aucun commit, aucun fichier `.sha256`, aucun `git fetch`, `checkout`, `stash` ni `reset` ; aucun fichier existant modifié (`git status` : seulement des fichiers neufs) ; rien sous `donnees/` ;
- aucun appel de modèle de langage, aucune carte, aucune dépense, aucune commande Vast.ai ; aucun `WebFetch` (le PDF du papier n'est toujours pas versé : la réserve R7 tient, avenant) ;
- le dépôt public `sycophancy-psychophysical-law` est lu en place, comme une donnée, dans le clone en lecture seule de l'avenant (`/home/claude/scratch/depots-publics-2026-11-03/sycophancy-psychophysical-law`, tête `b3ecaec`) : addenda R9 et R9-bis lus, rien exécuté ni importé ;
- `nice -n 10 python -I -B` pour les essais ; pytest avec `-p no:cacheprovider` ; `.venv` de `/home/user/controle-ia-travail` ;
- le conteneur a redémarré vers 01:53 UTC (message du coordinateur) : aucun fichier perdu ; aucun calcul n'était en cours ; la simulation de puissance et les répétitions jouet ont été lancées après.

Outils hors dépôt : `/home/claude/scratch/pilote-p-brouillon2/outils/construire_stimuli_v2.py` (assembleur des stimuli v2, `8e29aa07631a63f2b5e11c21e37792e6eeb9b0ae293f7033ad0293c8257e57ad`).

## 1. Fichiers produits (tous neufs)

| Fichier | sha256 | Rôle |
|---|---|---|
| `brouillons/pilote-exposant-p-v1/preregistrement-pilote-exposant-p-v1-brouillon2.md` | `431067d620252b3f99531e835774328b36963f4840d2e0d3dd241342bb712518` | préenregistrement, brouillon 2 (non scellé ; table « constat → ce qui change → où ») |
| `brouillons/pilote-exposant-p-v1/stimuli-pilote-exposant-p-v2.json` | `9a32ca837ff115ba589585102a07f9b0413c6118a02ae51ff3a731fcb4329adf` | stimuli v2 figés : 30 quadruplets, règles R-S1 à R-S10, invites du papier et cadrages de l'échelle recopiés |
| `brouillons/pilote-exposant-p-v1/verification-humaine-stimuli-v2.md` | `8844f1b11405efe0912e644d44ac81f9bfdce36aecc47c21775ac19615a2393a` | fiche de vérification humaine à remplir par Lazar (30 quadruplets, 13 doutes signalés) |
| `brouillons/pilote-exposant-p-v1/config-pilote-exposant-p-v2.json` | `c5a63a9036043302d8f8c50530f4f0dc94903c7756f81ff9b16f36c584f950bd` | configuration v2 (constantes de lecture, plafonds, section jouet) |
| `brouillons/pilote-exposant-p-v1/puissance-pilote-exposant-p-v2.json` | `27a0251cf6e1f8b9dfd3e7f7c51ff4d7c76c2fdf2c01b1996628501b7169ead4` | sortie de la simulation de puissance v2 (36 scénarios) |
| `brouillons/pilote-exposant-p-v1/devis-pilote-exposant-p-v2.md` | `cefa69d6a8327d915ef78d3d3e05280d9324cbd6e4555aa95b19f0c0f3433418` | devis v2 (pire cas ≈ 16,6 USD < 30 USD) |
| `src/controle_ia/pilote_exposant_p_v2/__init__.py` | `8da530e02281aad119abcf5a88958f82056b4df8e95648e60ef50cca2e5c11d3` | paquet v2 |
| `src/controle_ia/pilote_exposant_p_v2/stimuli.py` | `6054866d9f8b26434c50704d69ba6b829a9ac9563f226a100aac6ae9c2b5493d` | règles des stimuli v2, modèle stylisé, jumeau, paires |
| `src/controle_ia/pilote_exposant_p_v2/analyse.py` | `e4c8a71a3e39a97d628b272d90861fee36724d642bc1e67e67a83cf3176856db` | critères gelés v2, rééchantillonnages, qualificatifs, contrôles, phrases, symétrie |
| `src/controle_ia/pilote_exposant_p_v2/courbes.py` | `7ae05eb144ee9ea23d0214f5207037f6bdd3bbe593dd2533285e756d8cb6451e` | lectures descriptives sur la fenêtre W (R9-bis) |
| `src/controle_ia/pilote_exposant_p_v2/go.py` | `d442bf0ad20bcee1b42428a20e3fcf087698f99a22237e95bf436b6475931145` | vérification d'un GO de calcul (amorce) |
| `src/controle_ia/pilote_exposant_p_v2/run.py` | `d766cadfe4f16bd0826341e53b1e51b3d20c109e4ed9643197a4424b5e3086a3` | lanceur v2 (ordre gelé, gardes, réserve de temps, lecture gelée, audit de retrait) |
| `src/controle_ia/pilote_exposant_p_v2/puissance.py` | `4b1bce827f4556f7144416fdd6bdb036121f6590c5cd117768f8eef70694b3b7` | simulation de puissance v2 |
| `tests/test_pilote_exposant_p_v2.py` | `77cf66268cd3db7ac65fa1e7389f3f967718e05b312e9b1d03e98218e0b948aa` | 46 essais du pilote v2 |
| `tests/test_script_pilote_exposant_p_v2.py` | `7b1942086f15e75dfcad8239645b013f751fe44ef73078b933e10084863ec5fb` | 21 essais du script d'instance et de l'amorce |
| `scripts/pilote_exposant_p_instance_v2.sh` | `fd686ea1468a250985a1b3997d5cc30944107d4215fe1506b7c0409d1f148e24` | script d'instance v2 (jamais lancé) |
| `scripts/amorce_instance_pilote_exposant_p_v2.sh` | `78bb1a8c500fda0c107f160322ee90d5ef9eb14e13522eb381f78dbf4cb96877` | amorce v2 : GO vérifié avant toute création, puis sur l'instance (jamais lancée sur une instance) |
| `brouillons/pilote-exposant-p-v1/rapport-redaction-pilote-exposant-p-v2.md` | donné dans la réponse finale | ce rapport |

## 2. Essais

Commande (celle du script d'instance v2, six fichiers) : `nice -n 10 python -I -B -m pytest -q -p no:cacheprovider --color=no tests/test_pilote_exposant_p_v1.py tests/test_pilote_exposant_p_v2.py tests/test_script_pilote_exposant_p_v2.py tests/test_manifeste.py tests/test_scellement.py tests/test_prereg.py` :

```
Wed Nov  4 02:20:09 UTC 2026
........................................................................ [ 55%]
.........................................................                [100%]
129 passed in 269.10s (0:04:29)
Wed Nov  4 02:24:41 UTC 2026
```

D'où « Tests attendus : `129` » au brouillon 2 (34 du pilote v1, 46 du pilote v2, 21 du script et de l'amorce, 28 des modules communs).

Ce que les essais neufs établissent (processeur, aucun téléchargement) :
- **stimuli v2** conformes à R-S1 à R-S8 et R-S10 ; sept artefacts détectés (porteur dans le corps, paire non minimale, porteur différent entre registres, porteur de date, personne grammaticale déséquilibrée, contraction en registre formel, porteurs non distincts) ;
- **modèle stylisé** (dimension 4 096, 300 tirages par w au lanceur, 60 aux essais) : v2, médianes de \|cos(E, R)\| 0,000 (w = 0 : R est nul par construction), 0,010 (w = 0,3), 0,012 (w = 1), aucun tirage à \|cos\| ≥ 0,1 ; **v1 rejoué comme artefact** : 0,190, 0,181, 0,145, avec 100 %, 100 % et 99,7 % des tirages à \|cos\| ≥ 0,1 — la contre-lecture R2 donnait −0,190, −0,181, −0,144 (calcul) ;
- **jumeau** : choix par nombre de jetons, sain (30 retenus sur un compteur par mots) et artefact (compteur par caractères : non construit) ;
- **table gelée** : onze cas, dont identification, échecs, sensibilité qui convertit « égal » et « au-dessous » mais laisse « au-dessus » ;
- **rééchantillonnage par sous-ensembles** reproductible, NaN retirés ; un effet commun d'un sous-ensemble s'annule dans Δ avec la référence répartie (\|Δ\| < 0,01) et passe en plein (−0,48) quand toute la référence est sur le sous-ensemble 0 ;
- **position dans la famille** et **jumeau** (quatre cas chacun) ; **identité des ancres** : grilles publiées contre elles-mêmes (identiques), ancres permutées à norme égale (non identiques, réserve), norme différente ;
- **lecture complète sur plans synthétiques** : issue tranchée avec qualificatifs et audit de retrait (32 recalculs, aucune issue différente, rejeu à l'identique) ; « égal » et « indiscernable du jumeau » ; chemins « exclu », « identification », « échecs », « sensibilité » ;
- **gardes du lanceur** : configuration (quatre artefacts : constante, référence, commit amont, stimuli) ; run réel refusé tant qu'un marqueur reste, et quand le préenregistrement ne cite pas les empreintes lues, accepté sur des copies propres ; R1 sans gestionnaire de TERM posé (M5) ; tokeniseur discordant ; révision discordante ; flux trop court → `GardeArret` ; horloge et réserve des blocs décisifs ; grille non finie ;
- **GO** : sain, doublons ailleurs rapportés ; dix artefacts (absent, type, auteur, plafond bas, plafond illisible, période, périmètre, révoqué, doublon de l'identifiant, identifiant illisible) ;
- **répétitions jouet du lanceur** : de bout en bout (sorties scellées vérifiées, jumeau consigné, référence répartie k mod 3, blocs sensibilité, jumeau et famille exercés grâce à des seuils jouet consignés) ; **arrêt « instrument non validé » en mode jouet, code 3**, sorties écrites, aucun plan du modèle lu ; **plafond de durée** au niveau du lanceur : arrêt avant le premier plan décisif, `arret.json` scellé, 0 plan fait (cet essai a trouvé un défaut, corrigé : le premier plan du témoin positif ne passait pas par l'horloge) ;
- **script d'instance et amorce** (déclinés de `tests/test_script_p3.py`) : cas sain ; quatre artefacts de lecture précoce ; marqueurs restants en mode reel (sain et artefact ; révisions transmises au lanceur en mode reel seulement) ; run arrêté ; code 3 ; branche présente ; dernière ligne des essais (trois cas) ; amorce « verifier » avant toute création (sain et cinq artefacts) ; amorce sur l'instance (sain, dossiers présents, GO invalide → arrêt avant toute installation, plafond atteint → résultats partiels et traces poussés).
- Répétition jouet manuelle à la taille jouet de la configuration (23 plans, 8 min 13 s sur des cœurs partagés avec la simulation) : issue « non concluant (identification) », cos(E_A, E_B) = 0,11 sur ce modèle aléatoire : la règle d'identification fait ce qu'elle doit sur un réseau sans sémantique.
- Vérification du GO réel, étape « verifier » de l'amorce, sur `/home/user/controle-ia-travail/registres/go.md` : **GO-2026-11-04-03 valide** (calcul, Lazar, 4 au 18 novembre, 30 USD ≥ 17), avertissement : seize identifiants en double ailleurs dans ce registre.

## 3. Ce qui est repris du papier, ce qui s'en écarte

**Repris sans changement** (modules v1 importés, non modifiés) : copie amont (`parametrize.py`, `superellipse.py`, MIT) ; protocole (couche 2, mesure au bloc 30, dernier jeton, réponse L2, grille 31 × 31 sur [0, 60°], seuil par paire f = 0,5, fenêtre de 60°, normalisation géodésique exacte, p borné dans [0,5 ; 10]) ; 30 ancres FineWeb-edu de 5 jetons ; différences aléatoires `k_avg = 30` ; isotropes à graine 42 ; règle \|cos\| < 0,1 ; invites du papier contrôlées par leurs empreintes ; témoin Wealth × Gender (3,003).

**Écarts** : vingt-cinq, déclarés un par un au préenregistrement (E-01 à E-25). Neufs au brouillon 2 : E-16 (vérification humaine par Lazar), E-17 refait (paires de E minimales ; paires de R réécrites), E-18 à E-20 (couples de la contre-lecture), E-21 (sensibilité décisive), E-22 (jumeau et famille K), E-23 (identification par moitiés, de R9), E-24 (porteurs à trait d'union), E-25 (lectures sur W). Les sept écarts entre le texte du papier et son code relevés par la lecture du brouillon 1 restent non tranchés (lecture `lecture-2606-24964-v1.md`, §5).

**Emprunts à R9 et R9-bis** (décision 2 de Lazar) : fenêtre W et enveloppes, lues en descriptif seulement, sans balayage de plus ; jumeau neutre adapté (remplacement du dernier mot au lieu d'un aparté ajouté : E n'ajoute rien au prompt, il change un mot ; un aparté ajouté ne serait pas construit comme E) ; règle d'identification de R9. Marqueur unique `<<DOI_R9_BIS>>`, refusé par le lanceur (et par le script en mode reel) tant qu'il reste.

**Message de Fable (n° 1)** : ses deux écarts (§5) visent le brouillon de réponse au mentor, pas ce préenregistrement : ici, les valeurs de Llama viennent de l'audit du code et les différences aléatoires publiées ne sont citées que pour Gemma ; la note 1 du papier (sensibilités qui varient d'un facteur ≈ 70, métrique de Kullback-Leibler) n'est pas employée. R9 et ce pilote se recoupent (même instrument, même modèle, Wealth × Gender) : à signaler à Lazar si les deux tournent, pour comparer les deux témoins sur le modèle lu.

## 4. Simulation de puissance v2 (calcul)

`src/controle_ia/pilote_exposant_p_v2/puissance.py` ; sortie `puissance-pilote-exposant-p-v2.json` ; entropie 2026110402 ; deux calages × 3 effets communs × 3 τ × 2 positions du plan lu = 36 scénarios, 300 répétitions, B = 2 000 ; 500 s sur trois processus. Calage recalé : écart type de p estimé 0,129 vers p ≈ 2 (cible 0,096, publiée sur 30 ancres distinctes ; calage v1 : 0,197).

| Scénario central (recalé, σ_c = 0,035, τ = 0,17) | « au-dessus » | « au-dessous » | « égal » | qualificatif « au-delà » |
|---|---|---|---|---|
| plan à la moyenne, Δ = 0 | 5,7 % | 1,3 % | 93,0 % | 0,0 % |
| plan tiré de la famille, Δ = 0 | 36,7 % | 38,0 % | 25,3 % | 3,0 % |
| plan à la moyenne, Δ = +0,10 / +0,20 / +0,40 / +0,60 | 85,7 / 100 / 100 / 100 % | — | — | 1,0 / 2,7 / 44,3 / 85,7 % |
| plan à la moyenne, Δ = −0,10 / −0,20 | — | 77,3 / 100 % | — | — |

- Demi-largeur médiane de l'intervalle de Δ : 0,066 (premier centile 0,048) ; au calage prudent : 0,113. D'où le seuil « trop beau » à 0,03 (M7).
- Les taux de faux « au-dessus » (5,7 % ; 8,3 % avec σ_c = 0,06) dépassent le 2,5 % nominal. Une partie vient de la simulation elle-même (banque arrondie au pas de 0,05 : Δ estimé moyen +0,014 à Δ = 0) ; le reste, d'un rééchantillonnage par percentiles qui couvre un peu moins que 95 %. Déclaré au préenregistrement ; c'est le point 5 ci-dessous.
- Règle de sensibilité (borne basse > δ) : Δ_WG = +0,30 → 74,7 % ; +0,40 → 100 % ; l'ordre de grandeur attendu sur le modèle lu (≈ +1,1, calcul, supposé transporté) est loin au-dessus.

## 5. Dix points pour un contre-lecteur neuf

1. **Stimuli (B1).** Les paires de E sont minimales et le porteur est partagé entre registres ; le modèle stylisé passe. Mais R n'est plus porté que par le corps : au dernier jeton de la couche 2, R risque d'être faible et mal identifié (la répétition jouet le montre pour E sur un réseau aléatoire). La règle d'identification (0,5, de R9) est-elle le bon garde-fou, et à ce seuil ? Le prix (« non concluant (identification) » probable, a priori 0,15) est-il acceptable pour Lazar ?
2. **Sens des porteurs (R-S9).** Treize quadruplets sont signalés douteux dans la fiche de Lazar (Q06 « scoreboard », Q13 « validation », Q23 « scoring »…). Faut-il les remplacer avant de les lui soumettre ? Les porteurs à trait d'union (Q25 à Q30) changent-ils trop le nombre de jetons (E-24) ?
3. **Jumeau neutre.** Adaptation de R9-bis par remplacement du dernier mot et non par aparté ajouté : est-ce « construit comme la direction étudiée » ? Les neutres (podcast, documentary, newsletter…) sont-ils vraiment sans statut, ou portent-ils un « usage réel sans enjeu » qui les rapproche du déploiement ?
4. **Qualificatifs.** Famille (K = 8, intervalle de prédiction en t) et jumeau accompagnent l'issue sans la changer. Est-ce assez pour les phrases de Lazar au mentor, ou faut-il que « au-dessus » exige « au-delà de la famille » ?
5. **Taux simulés à Δ = 0** au-dessus du nominal (5,7 % contre 2,5 %) : faut-il un intervalle à 97,5 %, un percentile corrigé, ou une banque plus fine avant de sceller ? Le biais de la banque (+0,014) doit-il être retiré de la simulation pour juger la règle seule ?
6. **Sensibilité (B4).** Tolérance « borne basse de Δ_WG > δ » (le couple P10 disait « > 0 ») : défendable ? Le témoin n'est qu'une paire (Wealth × Gender) ; faut-il la famille contrastive du modèle lu en témoin décisif ?
7. **Référence répartie et rééchantillonnage par sous-ensembles (B3)** : la lecture des 32 sous-ensembles comme unités indépendantes tient-elle (ancres consécutives d'un même flux mélangé) ?
8. **Seuils jouet.** Le mode jouet emploie des tolérances et des seuils (exclusion, identification) propres, lus seulement si `--jouet` et consignés dans les sorties. Un chemin de code réel peut-il les lire ? (Je n'en vois pas : `self.tol` est `None` hors jouet ; à vérifier.)
9. **Amorce et garde de calcul.** L'amorce vérifie le GO avant toute création et sur l'instance ; mais la garde `.claude/hooks/garde_calcul.py` de la session bloque à cause des seize doublons du registre de `main`, et le GO est absent du registre de la branche. Qui tranche, et comment, sans modifier le registre ?
10. **Provenance (R7).** δ, le seuil de résidu et les valeurs de Llama sont adossés à l'audit empreinté du code ; les chiffres du texte du papier restent au niveau transcription (PDF non versé). La licence de FineWeb-edu n'est pas vérifiée. R9-bis n'est pas archivé (marqueur). Quelque chose d'opposable manque-t-il ?

## 6. Fichiers que le contre-lecteur doit lire

- Consigne de ce brouillon et avenant (chemins en tête) ; `CLAUDE.md` ; `prereg/gabarit-preregistrement-v1.md`.
- La contre-lecture R2 du brouillon 1 et ses couples (`brouillons/pilote-exposant-p-v1/contre-lecture-v1/`) ; le brouillon 1 (`preregistrement-pilote-exposant-p-v1-brouillon1.md`) pour la table « constat → ce qui change → où ».
- Pièces du brouillon 2 : `preregistrement-pilote-exposant-p-v1-brouillon2.md`, `stimuli-pilote-exposant-p-v2.json`, `verification-humaine-stimuli-v2.md`, `config-pilote-exposant-p-v2.json`, `puissance-pilote-exposant-p-v2.json`, `devis-pilote-exposant-p-v2.md`, ce rapport.
- Code : `src/controle_ia/pilote_exposant_p_v2/` en entier (`analyse.py`, `run.py`, `stimuli.py`, `puissance.py`, `go.py`, `courbes.py`) ; les modules v1 qu'il importe (`ajustement.py`, `balayage.py`, `directions.py`, `ancres.py`, `references.py`, `amont/`).
- Essais : `tests/test_pilote_exposant_p_v2.py`, `tests/test_script_pilote_exposant_p_v2.py`.
- Scripts : `scripts/pilote_exposant_p_instance_v2.sh` (à comparer avec le v1), `scripts/amorce_instance_pilote_exposant_p_v2.sh` (à comparer avec `amorce_instance_p3.sh`) ; `.claude/hooks/garde_calcul.py` ; `registres/go.md` de `main` (ligne 241).
- Sources : addenda R9 et R9-bis du dépôt public (`preregistrations/2026-11-02_addendum_R9_feature_specific_error_correction.md`, `2026-11-03_addendum_R9bis_dose_curves.md`, tête `b3ecaec`) ; message de Fable `brouillons/canal-fable-v1/fable_2026-11-03_n001.md`, §5 et §6 ; le papier 2606.24964, en entier, et le PDF dès que Lazar l'a versé.

## 7. Réserves et ce qui reste à Lazar

- **Vérification des stimuli** : remplir `verification-humaine-stimuli-v2.md` (30 quadruplets, cinq cases chacun ; treize doutes signalés). Un quadruplet refusé donne des stimuli v3.
- **PDF de 2606.24964** : à verser (le terminal reçoit 403), pour lever la réserve R7.
- **DOI de R9-bis** : à reporter partout où `<<DOI_R9_BIS>>` figure (stimuli, configuration, préenregistrement, modules `__init__`, `stimuli`, `courbes`), dans des versions neuves (R12).
- **Garde de calcul** : décider comment la commande de création passe la garde de la session (doublons du registre de `main`).
- Contre-lecture R2 neuve de ce brouillon ; puis scellement.
