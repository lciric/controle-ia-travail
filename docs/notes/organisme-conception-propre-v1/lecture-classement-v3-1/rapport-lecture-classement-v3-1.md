# Rapport — outil du lecteur v3.1 (lecteur Astra) et classement v3.1, course « conception propre »

Auteur de la v3 (modèle A), sous-agent de la session mère ; 14 novembre 2026, de 09:01 à 10:20 environ UTC (heures
relevées par `date -u`). Demande de la mère après la contre-lecture `contre-lecture-lecture-classement-v3-v1.md`
(`f5cc9cdb…`, modèle B, R-2678, « non utilisable en l'état pour `envoyer` ») et le prix lu (`prix-astra-v2.md`,
`bf211a07…`, R-2677). **Aucun appel réseau** (essais, bancs et sondes sous doublure ou sur la boucle locale ; bancs et
sondes sous `unshare -n`), **aucune valeur de clé lue** (clés factices ; présence de la vraie vérifiée par son nom seul),
**aucune fiche ni aucun témoin ouvert** (fiches factices ; témoins lus par les programmes seulement, sous une racine
factice). Dossier v3 intact (R12) ; rien commité, rien poussé.

## Verdict

v3.1 écrite, essayée hors réseau et scellée. **B1, B2, M1 à M5 et m1 corrigés ; m3 corrigé ; m2 vérifié et corrigé dans
le devis v2** ; palier Flex en option ; règle inchangée (comparaison d'arbres, essai `test_regle_inchangee_v3_v3_1`).
Essais : **220 passés** (aussi sous `unshare -n`). Bancs, seconde passe : **mes 182 mutants tués sur 182** ; **mutants du
contre-lecteur rejoués : 20 tués sur 21**, le survivant D2 démontré redondant par un essai (§ 5). Sondes du contre-lecteur
rejouées : toutes ses conditions de la ligne C1 tiennent (§ 6). **Reste avant tout appel** : relecture courte du
différentiel par le contre-lecteur (R-2678), attestation qui nomme OpenAI (m5, geste de la mère), et le mot de Lazar sur
le palier, l'effort et la part de la ligne (devis v2 : Flex `medium` ≈ 8,64 USD attendus, condition des 18 appels
9,28 ; standard `medium` 17,28 et 18,57, hors de la ligne).

## 1. Pièces (scellées ; empreintes dans les compagnons `.sha256`)

| Pièce | Rôle |
|---|---|
| `outil_lecteur_conception_propre_v3_1.py` | préparer, envoyer, bilan, vérifier |
| `classer_conception_propre_v3_1.py` | classement (règle inchangée) |
| `differentiel-outil-v3-v3-1.diff`, `differentiel-classer-v3-v3-1.diff` | différentiels entiers |
| `essais_lecture_classement_v3_1.py`, `resultat-essais-lecture-classement-v3-1.txt` | essais hors réseau |
| `mutations_lecture_classement_v3_1.py`, `resultat-mutations-lecture-classement-v3-1.json` | banc de l'auteur |
| `rejeu-contre-lecture/` : mutants et sondes du contre-lecteur adaptés, leurs différentiels avec l'original, leurs résultats | rejeu demandé |
| `devis-lecture-astra-v2.md` | devis au prix lu, deux paliers, deux efforts |

## 2. Constat par constat

| Constat | Issue | Ce qui change |
|---|---|---|
| **B1** clé écrite si elle porte une fin de ligne | **corrigé** | `lire_cle` refuse, sans la montrer, toute clé vide ou hors `[\x21-\x7e]{1,512}`, avant tout journal et tout envoi ; le message d'une exception de transport n'est jamais écrit (seul son type) ; tout ce qu'`envoyer` écrit passe par `expurger` (clé et formes échappées : JSON, `\/`, pourcentage, repr) ; une réponse qui porte la clé est expurgée et bloquante (`cle_dans_la_reponse`). Essais avec le transport réel sur la boucle locale (`\r`, `\n`, `\r\n`, espace, tabulation, non-ASCII), en ligne de commande, exception à message échappé, réponse qui renvoie la clé sous trois formes. |
| **B2** redirection suivie vers un autre hôte | **corrigé** | `SansRedirection` (aucune redirection suivie) ; 3xx → statut rendu, anomalies `statut_non_200` et `redirection_refusee`, arrêt ; adresse finale contrôlée (`ErreurTransport`). Essais sur la boucle locale pour 301, 302, 303, 307, 308 : l'autre hôte ne reçoit rien ; par `envoyer` : arrêt, fichier d'erreur, pire cas, reprise refusée. |
| **M1** réponses lues hors journal | **corrigé** | `verifier_lecture` confronte journal et dossier dans les deux sens (`controler_coherence` : tout fichier nommé existe à la même empreinte, toute réponse ou erreur présente est nommée), et exige pour chaque réponse lue une clôture à son nom, son empreinte, statut 200 ; reçue sans clôture : `reponse_non_analysee` (bloquante). Le classement passe par là. |
| **M2** un dossier neuf remet la dépense à zéro | **corrigé (C6 par programme)** | un seul dossier d'envois, au chemin fixe `docs/notes/organisme-conception-propre-v1/lecture-g1-v3-1/envois` ; tout autre `manifeste-envois-v3*.json` sous `docs/` ou `runs/` fait refuser `preparer`, `envoyer`, `bilan` et `verifier` ; `--depense-anterieure-usd` obligatoire, consignée, et plafond ≤ 14,20 moins elle (C4). Option retenue : « refus d'un second dossier » (la mère en offrait deux) : le journal du seul dossier possible est le journal commun. |
| **M3** réponse payée perdue si l'analyse tombe | **corrigé** | réponse 200 écrite brute (le corps seul), scellée et consignée (`recu`) **avant** l'analyse ; analyse sans exception (chaque champ contrôlé par son type) ; filet déclaré `analyse_en_echec`, pire cas ; corps d'erreur de forme inattendue : fichier d'erreur écrit. |
| **M4** usage sous-déclaré accepté | **corrigé** | `usage_incoherent` (pire cas, bloquant) aussi si total < somme, entrée < octets du corps / 16, sortie visible < octets du contenu / 16 (au moins 1 dès que le contenu n'est pas vide) ; usage absent ou nul : idem. |
| **M5** gardes sans artefact | **corrigé** | un essai par mutant survivant (D4, D5, F1 à F4, M2, C1 à C3, R2, R3, D6, D7) ; D2 démontré redondant (§ 5). Tout écart d'envoi consigné pour un lot devient une anomalie bloquante de la vérification (`anomalie_d_envoi`, nommant les fiches du lot) : réserve r6 de la v3 levée. |
| **m1** plafond non revalidé à l'envoi | **corrigé** | `valider_manifeste` à l'envoi : palier, prix égaux aux prix lus, dépense antérieure, plafond fini et dans les bornes, nombre d'appels, lecteur, ordre, octets et pire cas de chaque corps, paramètres de chaque corps (clés exactes, modèle, plafond de sortie, effort, `store`, `service_tier`) ; refus avant la lecture de la clé. |
| **m2** condition des 18 appels | **vérifiée, corrigée au devis v2** | le 18e appel est un lot de 4 : **0,2988 PE + 0,3116 PS** (`medium`) ; le 0,2978 du contre-lecteur omet la marge de 1 024 octets du pire cas d'entrée (écart 0,01 USD au prix standard). |
| **m3** « contenu non lu » faux | **corrigé** | docstring de `lire_reponse` et précision du classement justes : le contenu d'une réponse à fin autre que `stop` est lu (sans effet sur E2). |
| **m4** N illisible non nulle compte `aucune` | **non changé : nœud** | touche la lecture ; sonde s9 rejouée, résultat identique à la v3. Recommandation pour le nœud : faire de toute valeur de N hors {`aucune`, `C1`…`C12`} une anomalie bloquante (même logique que C1). |
| **m5** attestation écrite pour Kimi | **geste de la mère** | l'outil accepte toute attestation conforme ; recommandé : `attestation-lecture-g1-v2.json` qui nomme OpenAI (Astra, palier, `store: false`). |
| **m6** environnement réduit | **commandes du § 7** | `envoyer` lancé avec un environnement réduit aux noms nécessaires, sans mettre la valeur de la clé dans une ligne de commande. |
| **m7** formulation de R-2675 | sans objet pour le code | le devis v2 dit « la garde borne au plafond donné ». |
| **m8** D2 et R3 redondants | **R3 tué par un essai ; D2 démontré redondant** | § 5. |

## 3. Différentiel v3 → v3.1 (outil ; détail : `differentiel-outil-v3-v3-1.diff`)

- **Identiques** (comparaison d'arbres, docstrings ôtées) : 68 objets, dont toute la règle (`vue_lecteur`,
  `admissibilite`, `construire_pile`, `enfants_ordres`, `ordres_lectures`, `decouper_lots`, `etiquette`, `texte_message`,
  `passage_dans`, `verifier_entree`, `entrees_catalogue`, `extraire_json`, `verifier_attestation`,
  `verifier_fiches_de_run`, `verifier_lot`, `cles_manquantes`, `ORDRE_VUE`, `TABLE_TYPO`, `PIECES`, `ENTROPIE_ORDRES`,
  `TAILLE_LOT`, `MODELE_LECTEUR`, `MAX_APPELS`, `MAX_SORTIE`, `EFFORTS`, `URL_AMONT`, `PLAFOND_ABSOLU_USD`).
- **Changés** : `VERSION`, noms de fichiers (`SUFFIXE` « v3-1 »), `TAILLE_MAX_REPONSE` (4 Mo → 1 Mo),
  `ANOMALIES_BLOQUANTES` (+ `anomalie_d_envoi`, `reponse_non_analysee`, `palier_servi_different`), `preparer`
  (C6, palier, dépense antérieure, prix lus), `corps_requete` (palier), `lire_cle` (B1), `transport_reel` (B2),
  `champ_court` (codes `[a-z_]{1,64}` seulement), `cout_usage` (M3, M4), `analyser_reponse` (M3, M4, B2, palier),
  `lire_journal` (événement `recu`, lignes mal formées refusées), `ajouter_journal` (expurgation), `nom_reponse`,
  `nom_erreur`, `controler_coherence` (deux sens), `bilan` (C3, C5), `envoyer` (B1, M3, revalidation), `lire_reponse`
  (palier, robustesse, m3), `charger_envois` (C6), `verifier_lecture` (M1, écarts d'envoi bloquants), `main`.
- **Retiré** : `masquer` (remplacé par `expurger`).
- **Neufs** : `PIECES_PRIX`, `PRIX_LUS`, `LIGNES_SOURCE_PRIX`, `SOURCE_PRIX`, `PALIERS`, `SERVICE_TIER`,
  `PALIERS_SERVIS_ADMIS`, `DOSSIER_ENVOIS_REL`, `MOTIF_CLE`, `PLANCHER_OCTETS_PAR_JETON`, `nombre_fini`, `prix_du_palier`,
  `racine_du_dossier`, `verifier_unicite`, `lecteur_attendu`, `formes_de_cle`, `contient_cle`, `expurger`,
  `ErreurTransport`, `SansRedirection`, `valider_manifeste`.
- **Ligne de commande** : `preparer` perd `--prix-entree`, `--prix-sortie`, `--prix-cache`, `--source-prix` (prix lus,
  constants) et gagne `--palier standard|flex` (défaut `standard`) et `--depense-anterieure-usd` (obligatoire) ;
  `verifier` refuse une `--racine` autre que celle du dossier.

**Classement** (`differentiel-classer-v3-v3-1.diff`) : chargement de l'outil v3.1, noms en `-v3-1`, refus d'une racine
autre que celle du dossier, une précision ajoutée ; aucune ligne de la règle ne change (essai de comparaison d'arbres).

**Palier.** `--palier flex` : `service_tier: "flex"` dans chaque corps, prix Flex (5 / 0,50 / 25), palier consigné au
manifeste et au relevé ; une réponse dont `service_tier` n'est pas `flex` est bloquante (envoi et vérification). En
standard, aucun champ n'est envoyé ; un palier servi autre que absent, `default` ou `standard` (par exemple `priority`,
facturé plus cher) est aussi bloquant : précaution ajoutée, noms SUPPOSÉ, éprouvés au premier appel (C3). Plafond absolu
inchangé : 14,20 USD.

## 4. Essais (hors réseau)

`essais_lecture_classement_v3_1.py` : **220 passés** (`resultat-essais-lecture-classement-v3-1.txt`), aussi sous
`unshare -n`. Les essais de la v3 sont gardés (adaptés : toutes les réponses passent par `envoyer` et son journal,
puisque `verifier` refuse désormais les autres ; l'aide `deposer_sans_journal` garde la forme v3 pour les artefacts de
M1). Neufs, chacun avec son cas sain et son artefact :

| Garde | Cas sain | Artefact |
|---|---|---|
| B1 clé | clé propre lue, retirée, absente de tout fichier et de toute sortie ; transport réel sur la boucle : un seul POST, bon chemin, bon en-tête | six formes de clé refusées avant tout journal (aussi en ligne de commande) ; exception de transport à message échappé ; réponse qui renvoie la clé (expurgée, bloquante) |
| B2 redirection | réponse 200 directe acceptée | 301, 302, 303, 307, 308 : statut rendu, autre hôte jamais contacté ; par `envoyer` : arrêt ; adresse finale autre : refusée |
| M1 journal | 12 réponses par `envoyer`, lisible | réponses déposées sans journal ; réponse désscellée, effacée, altérée, rescellée ; erreur nommée au journal puis effacée ; réponse reçue non close |
| C6 | une préparation, un dossier | seconde préparation (même dossier, autre dossier), envoi d'une copie, manifeste v3 ailleurs sous `docs/` ou `runs/`, racine neuve où traîne un manifeste |
| M3 | réponse écrite brute, octet pour octet, avant son analyse | détails d'usage et message non objets ; erreurs en chaîne, en liste, corps en liste ; filet de l'analyse ; réponse trop grande |
| M4 | usage cohérent | usage absent, détails non objets, zéros, un jeton, total sous la somme, entrée et sortie visible sous leurs planchers |
| M5 | — | reprise refusée après chacune de seize anomalies ; plusieurs choix, contenu vide, objet inattendu ; fins `content_filter`, `tool_calls`, absente, `length` lisible à la vérification ; nom servi en majuscules ; code d'erreur portant un identifiant ; autre variable de clé ; seize manifestes ou corps rescellés hors des bornes |
| palier | Flex : corps, prix, envoi, classement ; standard sans champ | palier servi `default` sous Flex, `priority` sous Flex et sous standard ; ligne de prix absente |

## 5. Bancs de mutations

Tous deux sous `unshare -n`, environnement réduit (aucune clé, aucun mandataire), un mutant = une chaîne remplacée dans
une copie hors du dépôt, essais v3.1 joués contre elle.

**Mutants du contre-lecteur, rejoués** (`rejeu-contre-lecture/mutations_contre_lecture_v3_rejeu_v3_1.py` ; seize
appliqués mot pour mot, cinq traduits parce que leur ligne a changé — D4, D6, D7, D9, C3 —, différentiel avec l'original
versé) :

- première passe (09:22:49 à 09:37:06 UTC, essais à 217) : **20 tués sur 21** ;
- seconde passe (10:07:56 à 10:16:08 UTC, essais définitifs, 220) : **20 tués sur 21**
  (`resultat-mutations-contre-lecture-rejeu-v3-1.json`). Les quinze survivants de la contre-lecture sont tués, sauf
  **D2**, démontré redondant : `valider_manifeste` refuse avant tout appel un manifeste dont un pire cas diffère de celui
  recalculé sur les octets du corps (essai `test_D6_D7_m1_manifeste_rescelle_revalide_a_l_envoi`, cas
  « pire_cas_abaisse ») ; pour tout manifeste accepté, le pire cas consigné égale l'exact arrondi à 10⁻⁶, donc
  `max(consigné, recalculé)` et « consigné seul » ne diffèrent jamais de plus de 5 × 10⁻⁷ USD (essai
  `test_D2_redondant_avec_la_revalidation_du_manifeste`). R3 est tué (essai `test_R3_envoi_consigne_deux_fois_refuse`).

**Mon banc** (`mutations_lecture_classement_v3_1.py`, 182 mutants : 128 de la v3, dont cinq adaptés aux lignes changées,
« exception de transport non masquée » étant retiré, et 54 neufs — dont son remplaçant « message d'exception de
transport écrit » — sur B1, B2, M1, C6, M3, M4, les écarts d'envoi bloquants, le palier, les prix lus, la revalidation du
manifeste, le bilan, la racine du classement) :

- première passe (09:22:29 à 09:48:26 UTC) : **178 tués sur 182** ; survivants : « réponse non scellée acceptée » (le
  sceau de `lire_reponse` est redoublé par la confrontation journal-dossier), « prix nul admis » (prix constants),
  « chemin du dossier non contrôlé à la préparation » et « racine du dossier non contrôlée » (masqués par la recherche
  d'un second manifeste, dont le refus contenait aussi le mot attendu par l'essai) ; quatre essais ajoutés, qui tuent
  chacun le sien (vérifié un par un) ; code inchangé ;
- seconde passe (09:50:05 à 10:07:56 UTC) : **182 tués sur 182**, aucun inapplicable
  (`resultat-mutations-lecture-classement-v3-1.json` ; la première passe est versée à côté). Après la seconde passe, seule
  la docstring du banc a été corrigée (compte des mutants adaptés) ; sa liste de mutants est celle qui a été jouée.
- R4 : un banc entièrement tué reste « trop propre » ; mes mutants et mes essais sont du même auteur. Deux gardes sont
  des défenses en profondeur sans mutant tuable par un essai de bout en bout (le filet d'expurgation du fichier d'erreur,
  dont le texte ne porte jamais de champ capable de contenir la clé ; la seconde exigence de clôture dans
  `verifier_lecture`, après `controler_coherence`) : elles ne sont pas dans le banc, et c'est dit.

## 6. Sondes du contre-lecteur rejouées sur la v3.1

`rejeu-contre-lecture/sondes_contre_lecture_v3_rejeu_v3_1.py` (copie adaptée, différentiel avec l'original versé ;
adaptations dites en tête : chemins, s1 gardée par `try`, s4 par `deposer_sans_journal`, s7 et s8 au dossier fixe),
jouée sous `unshare -n` (seule interface : `lo`) ; résultat `resultat-sondes-contre-lecture-rejeu-v3-1.json`.

| Sonde | v3 (contre-lecture) | v3.1 |
|---|---|---|
| s1 clé avec fin de ligne | clé écrite dans le fichier d'erreur | **refus avant tout journal, clé dans aucun fichier ni dans le refus, serveur non contacté par cette clé** |
| s2 redirection | autre hôte contacté, sa réponse acceptée | **302 rendu, autre hôte : aucune requête** |
| s3 usage sous-déclaré | aucun écart | **trois `usage_incoherent`, pire cas** |
| s4 réponses sans journal | deux idées désignées | **refus** |
| s5 réponse 200 mal formée | exception, pièce payée perdue | **aucune exception, réponse gardée brute** |
| s6 erreur mal formée | exception | **aucune exception, fichier d'erreur écrit** |
| s7 régénération | tenue | **tenue** (identique à la v2 : ordres, étiquettes, pile, vue servie, préambule, graines) |
| s8 dossier neuf | 12 appels de plus, mêmes corps | **trois refus (même dossier, autre dossier, copie) ; 3 appels en tout** |
| s9 N illisible non nulle | compte `aucune` | inchangé (m4 : nœud) |
| s10 plafond NaN rescellé | 12 appels sans garde puis exception | **refus avant tout appel** |

Note sur s1 : le champ d'origine `serveur_contacte` vaut vrai à la seconde itération parce que la « reprise » de la
première itération, faite par la sonde avec une clé propre, part normalement en v3.1 (rien n'avait été envoyé avant) ;
le champ ajouté `serveur_contacte_avec_cette_cle` est faux dans les deux itérations.

## 7. Commandes exactes de l'emploi, sous les conditions C1 à C7

Depuis la racine du dépôt ; `DOS=docs/notes/organisme-conception-propre-v1` (variable du shell, **non exportée** : le
point 6 retire de l'environnement toute variable exportée hors de sa liste) ; rien de ceci n'est fait.

0. **C1** (avant tout) : relecture courte de la v3.1 par le contre-lecteur ; puis
   `cd $DOS/lecture-classement-v3-1 && sha256sum -c outil_lecteur_conception_propre_v3_1.py.sha256 classer_conception_propre_v3_1.py.sha256 && cd -`.
1. **m5** : attestation neuve qui nomme OpenAI, scellée par la mère (même forme, mêmes champs, empreinte des fiches
   `a9f9594e…`), par exemple `$DOS/attestations/attestation-lecture-g1-v2.json`.
2. **Préparation** (palier et effort selon le mot de Lazar ; ici la recommandation du devis v2) :
   `.venv/bin/python -I -B $DOS/lecture-classement-v3-1/outil_lecteur_conception_propre_v3_1.py preparer --fiches runs/course-ideation-conception-propre-v1/20261113-235541-course-ideation-conception-propre-v1-g1/copies/sortie--fiches-validees.json --attestation $DOS/attestations/attestation-lecture-g1-v2.json --sortie $DOS/lecture-g1-v3-1/envois --effort medium --palier flex --plafond-usd 14.20 --depense-anterieure-usd 0`
3. **C2** : `.venv/bin/python -I -B -c "import json; s=json.load(open('$DOS/lecture-g1-v3-1/envois/manifeste-envois-v3-1.json'))['garde_depense']['prix_usd_par_million']; print(s); print('SUPPOSÉ' not in s['source'] and 'barème' not in s['source'] and 'bf211a07' in s['source'])"` → les prix du palier et `True`.
4. **C4** : le plafond du manifeste (14,20) est ≤ 14,20 moins toute dépense comptée depuis le devis
   (`registres/depenses.md` ; 0 à ce jour) et ≥ la condition des 18 appels au prix lu (Flex `medium` : 9,28).
5. **C6** : `find docs runs -name 'manifeste-envois-v3*.json'` → une seule ligne (le programme le vérifie aussi).
6. **C3 et C7, premier appel seul**, environnement réduit sans mettre la valeur de la clé dans une ligne de commande :
   `( for v in $(compgen -e); do case $v in PATH|HOME|HTTPS_PROXY|https_proxy|SSL_CERT_FILE|OPENAI_API_KEY) ;; *) unset "$v";; esac; done; exec .venv/bin/python -I -B $DOS/lecture-classement-v3-1/outil_lecteur_conception_propre_v3_1.py envoyer --envois $DOS/lecture-g1-v3-1/envois --envois-max 1 )`
   puis `.venv/bin/python -I -B $DOS/lecture-classement-v3-1/outil_lecteur_conception_propre_v3_1.py bilan --envois $DOS/lecture-g1-v3-1/envois`
   → `anomalies` vide, `clotures[0].modele_servi` = `gpt-6-astra`, `palier_servi` = `flex` (ou `default` en standard),
   `reasoning_tokens ≤ completion_tokens ≤ 32768`, `cout_usd ≤ pire_cas_usd` ; la mère recalcule le devis avec ces
   jetons avant les 17 autres.
7. **Les 17 autres** : même commande qu'au point 6, sans `--envois-max` (code 0 fait, 3 arrêt sur anomalie, 4 arrêt au
   plafond, 2 refus).
8. **C5** : `bilan` → `pret_pour_verifier: true`, `clos: 18`, `en_vol: []` (code 0 ; la confrontation journal-dossier
   est faite par le programme).
9. **C7** (après l'envoi, la clé lue par son nom, un booléen seul affiché) :
   `.venv/bin/python -I -B -c "import importlib.util as u, os, pathlib; s=u.spec_from_file_location('o', '$DOS/lecture-classement-v3-1/outil_lecteur_conception_propre_v3_1.py'); o=u.module_from_spec(s); s.loader.exec_module(o); c=os.environ['OPENAI_API_KEY']; print(any(o.contient_cle(p.read_bytes(), c) for p in pathlib.Path('$DOS/lecture-g1-v3-1').rglob('*') if p.is_file()))"` → `False`.
10. **Vérification et classement** : `.venv/bin/python -I -B $DOS/lecture-classement-v3-1/outil_lecteur_conception_propre_v3_1.py verifier --envois $DOS/lecture-g1-v3-1/envois`
    puis `.venv/bin/python -I -B $DOS/lecture-classement-v3-1/classer_conception_propre_v3_1.py --envois $DOS/lecture-g1-v3-1/envois --sortie $DOS/lecture-g1-v3-1/classement`.
    Après l'envoi, les gestes 3 à 10 ne lisent rien d'autre que le dépôt.

## 8. Réserves

- **r1 — documentation d'OpenAI non lue** (inchangé depuis la v3) : forme du corps, `reasoning_effort`, sens de
  `usage` (raisonnement compris dans `completion_tokens`) et noms de `service_tier` servis restent ceux de la pratique du
  dépôt et de ma connaissance ; le premier appel seul (C3) les éprouve. `reasoning_effort` n'a jamais encore été envoyé à
  Astra ; `service_tier: "flex"` non plus.
- **r2 — planchers de M4** : 16 octets par jeton est large (3 à 4 octets attendus) ; un découpeur très différent pourrait
  déclencher un faux `usage_incoherent` (arrêt au premier appel, compté au pire cas) : C3 le dirait.
- **r3 — palier standard** : la vérification du palier servi en standard (absent, `default` ou `standard` admis) est une
  précaution ajoutée hors de la lettre de la consigne ; un autre nom légitime arrêterait la lecture au premier appel.
- **r4 — appel sans flux** (inchangé) : une coupure compte le pire cas et arrête la lecture ; Flex peut être plus lent.
- **r5 — C6** borne la recherche des manifestes à `docs/` et `runs/` de la racine ; une copie hors du dépôt n'est pas
  vue (garde contre l'accident, non contre la malveillance), de même que le journal.
- **r6 — clé** : limite connue (`/proc/<pid>/environ` garde le bloc initial tant que le processus vit) ; l'intermédiaire
  de la session, qui porte son propre certificat, voit l'en-tête (dit par le contre-lecteur).
- **r7 — mutants et essais du même auteur** pour mon banc ; le rejeu des mutants du contre-lecteur n'est qu'une partie
  de la réponse : sa relecture courte reste à faire.
- **r8 — m4** (N illisible non nulle) : nœud, non routine ; recommandation au § 2.
