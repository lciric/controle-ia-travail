# Contre-lecture du code v72 du pilote MR-2 (configuration v12, lecture v72, sonde v72, lanceur v72) — v1

**Verdict : autorisable après corrections** (le code n'admet aucun relevé qu'il devrait refuser ; mais une condition hors code rend aujourd'hui la sonde payante perdue d'avance, un motif de refus ment dans le cas le plus probable, et le banc ne peut pas finir à 66 sur 66).

- Développeur : modèle A ; contre-lecteur : modèle B ; A ≠ B. Je n'ai écrit aucun des fichiers lus.
- Début : `Sat Nov 14 09:15:19 UTC 2026` (sortie de `date -u` à mon premier geste, recopiée) ; fin : `Sat Nov 14 09:23:27 UTC 2026` (`date -u` de la commande qui écrit cette ligne).
- Objet lu : arbre `/home/user/arbre-organisme-co/organisme`, tête `85167d3`, contre `e7daf32` ; pièces de `/home/user/arbre-organisme-co/pieces-v72/`.
- Ce que je n'ai **pas** fait : ni pytest ni le banc (un banc tournait) ; aucun réseau, aucune clé, aucune sonde ; aucune commande git d'écriture. Les preuves sont des lectures et de courts essais `python3 -I -B -c` sur des fonctions pures, depuis `orchestrator/`. Le constat 3 est donc une **prédiction** (assertions rejouées une à une), à confronter au résultat du banc.
- Dans les commandes ci-dessous, `O` = `/home/user/arbre-organisme-co/organisme/orchestrator` et `R71` = `/home/user/controle-ia-travail/docs/notes/organisme-multi-generations-v1/pilote-v1/sonde-v71-releve-v1/sonde-pilote-v71/releve-sonde-pilote-v71.json`.

## Réponses courtes aux huit questions

1. **Ajouts seuls : oui.** `git -C /home/user/arbre-organisme-co/organisme diff --name-status e7daf32` rend six lignes « A » (lanceur v72, banc v72, essais v72, configuration v12, lecture v72, sonde v72) ; `git status --porcelain` est vide ; le patch `organisme-v72-contre-e7daf32.patch` porte six « new file mode », et ses six empreintes d'objet (`0a1ba87`, `739417a`, `8278be8`, `c19d6c5`, `edfb9e0`, `a7b2c1e`) sont celles de `git hash-object` sur les fichiers du disque. Les empreintes sha256 de `EMPREINTES-code-pilote-v72.txt` égalent celles du disque pour les quatre fichiers neufs gelés et pour `sonde_pilote_v71.py`, `proposeurs_pilote_v70.py`, la commande et le relais.
2. **Lecture v72 = lecture v70 hors version : oui.** Comparaison des deux fonctions par `ast` + `difflib` : deux écarts seulement (la version exigée, passée en constante ; l'appel qualifié `_V70.verifier_section_sonde`). Refus croisés rejoués : `PC.lire_configuration(v11)` → « version « configuration-pilote-mr2-v12 » exigée » ; `PR.lire_configuration(v12)` → « version « configuration-pilote-mr2-v11 » exigée ». Aucune autre fonction de `proposeurs_pilote_v70.py`, `pilote_mr2_v70.py`, `audit_pilote_v70.py` ne relit la configuration par son chemin (`grep -n lire_configuration` : la seule définition, ligne 81). Configuration v12 contre v11, clé par clé : seuls `_lisez_moi`, `version` et les deux consignes diffèrent. Sûr.
3. **`reflexion_observee`** : définition juste (champ brut, entier non booléen, > 0, à l'un des deux appels ; 0, absent, booléen, flottant, texte, négatif refusés). Mais elle est **logiquement impliquée** par `verdict_egal_a_la_regle` (constat 4) : elle ne refuse rien que la v71 ne refusait déjà ; elle ne fait que nommer le refus. Un champ présent et > 0 sans verdict tranché reste refusé par le motif général (cas « argon E » et « astra C » ci-dessous). Relevé forgé : les conclusions sont recalculées des faits, les faits relus des pièces ; rien de neuf n'affaiblit la v71 (la limite reste celle de la v71 : un compagnon sha256 n'est pas une signature — qui réécrit pièces, compagnons et relevé d'un même geste passe). Les trois votes suffisent quand la réflexion est observée (aucun contre-exemple sur 4 800 usages énumérés ; les cas non tranchés tombent du côté du refus). Le refus nommé arrive bien avant le motif général — **trop tôt** (constat 2). Mode réel et bloc exigent la v72 : `exiger_mode_reel` et `bloc_gele` appellent `S.exiger_releve` avec `S` = sonde v72 (version de relevé v72, empreinte de la configuration v12, empreintes du code dont les deux modules de sonde et la lecture v72) ; le lanceur v71, resté en place, exige un relevé v71 sous la configuration v11, qu'aucun relevé ne satisfait.
4. **Consignes v12** : constat 5 (confiance et risques). Pire cas borné par la borne gelée **si** le plafond de sortie du fournisseur couvre la réflexion ; sinon le code ne borne pas, il constate après coup.
5. **Essais** : chaque garde neuve a un cas sain et un artefact, sauf deux manques (constats 2 et 3). Les essais portés visent bien le code v72 : `S` = `sonde_pilote_v72`, `PC` = `proposeurs_pilote_v72` (17 appels), `L` = lanceur v72 chargé par son chemin, `CONF` = `L.CONFIGURATION` ; les seuls usages restants de la v71 et de la v11 sont voulus (refus croisés, comparaison des textes). 127 fonctions `test_` contre 115.
6. **Banc** : 19 des 20 mutations neuves visent la bonne garde et leur essai attendu les tue (lecture assertion par assertion) ; **N18 survit** (constat 3) ; N09 est tuée par un essai d'unité mais est sans effet sur ce qui est admis (constat 4). Gardes neuves sans mutation : constat 6.
7. **Commande et essai à sec** : suffisants pour l'analyse des options, la lecture des lignes au montant exact et le registre ; insuffisants sur trois points (constat 7).
8. **Autre, bloquant** : le quota d'Astra (constat 1).

## Constats

### 1. BLOQUANT (hors code) — Astra n'a jamais répondu à la sonde v71 : HTTP 429 « insufficient_quota » aux deux appels ; le rapport v72 n'en dit rien

- Fichier : `R71` (appels d'`astra`) ; rapport `rapport-developpeur-code-pilote-v72-v1.md`, sections 2 et 6 (aucune occurrence de « 429 » ni de « quota » : `grep -n '429\|quota'` vide).
- Preuve : `cd O && python3 -I -c "import json;r=json.load(open('R71'));print([(f['appel'],f['statut_amont'],f['type_erreur'],f['cout_usd']) for f in r['appels'] if f['proposeur']=='astra'])"` → `[('borne_gelee', 429, 'insufficient_quota', 1.81052), ('borne_courte', 429, 'insufficient_quota', 0.02395)]`. Toutes les conclusions d'`astra` y sont fausses (`statut`, `usage_entier`, etc.).
- Conséquences : (a) la sonde v71 n'a pas échoué sur le seul Argon : Astra n'a pas été sondé du tout, la forme réelle de son usage (`completion_tokens_details.reasoning_tokens` présent ?) est **inconnue** ; (b) tant que le compte hors crédits d'Astra n'a pas de quota, toute sonde v72 est refusée d'avance, quelle que soit la consigne, et consomme les deux lignes de GO neuves (une seule exécution par ligne) ; (c) la « dépense » 1,865848 USD du relevé v71 est pour 1,83447 USD un pire cas comptable d'appels refusés par l'amont, pas une dépense.
- Correction : avant toute sonde v72, Lazar vérifie à la console que le compte d'Astra a du quota (ou la mère tranche : sonder sans Astra n'est pas possible avec ce code, le relevé exige les quatre proposeurs). L'écrire au rapport v72 et à l'ordre de lancement.

### 2. MAJEUR — le refus nommé « la consigne ne l'a pas fait réfléchir » est rendu aussi quand l'appel a échoué en amont

- Fichier : `pole/sonde_pilote_v72.py`, lignes 132 à 134 (avant le motif général, lignes 135 à 138).
- Preuve (rejouable, aucun réseau ; le script écrit un relevé d'essai dans un dossier provisoire à donner) :

```
cd O && python3 -I -B - . R71 /tmp/preuve-c2 <<'PY'
import json, os, sys
arbre, releve71, d = sys.argv[1:4]
sys.path.insert(0, arbre)
from pole import proposeurs_pilote_v72 as PC, proposeurs_pilote_v70 as PR, sonde_pilote_v72 as S, pilote_mr2_v70 as P
conf, _ = PC.lire_configuration(os.path.join(arbre, "exemples", "pilote-mr2-v70", "configuration-pilote-mr2-v12.json"))
faits = json.load(open(releve71, encoding="utf-8"))["appels"]
for f in faits:  # Argon rendu réfléchissant ; Astra laissé tel que relevé (429)
    if f["proposeur"] == "argon":
        f["usage_brut"] = ({"promptTokenCount": 35, "candidatesTokenCount": 4, "thoughtsTokenCount": 900, "totalTokenCount": 939}
                           if f["appel"] == "borne_gelee" else
                           {"promptTokenCount": 40, "candidatesTokenCount": 6, "thoughtsTokenCount": 250, "totalTokenCount": 296})
attendu = {"configuration_sha256": PR.empreinte_configuration(conf), "code_sha256": {"x": "y"}}
os.makedirs(d)
c = os.path.join(d, S.RELEVE)
PR.ecrire_scelle_json(c, S.releve(conf, faits, True, "debut", "fin", False, None, dict(attendu)))
try:
    S.exiger_releve(conf, c, attendu); print("ADMIS (défaut)")
except P.Refus as e:
    print("refus :", e)
PY
```

  Résultat obtenu : `refus : relevé de la sonde : astra : champ de réflexion absent ou nul aux deux appels (la consigne ne l'a pas fait réfléchir) : la règle de comptage gelée (True) n'est pas confirmée` — alors qu'Astra a rendu 429 aux deux appels (`statut` faux). Le diagnostic est faux, et il pousse vers la « troisième voie » du rapport (réglage de réflexion, nœud Q-4) pour une panne de quota.
- Correction (texte exact, une occurrence) — avant :
  `        if p["dialecte"] != "claude" and recalculees.get("reflexion_observee") is not True:`
  après :
  `        if p["dialecte"] != "claude" and recalculees.get("statut") is True and recalculees.get("usage_entier") is True \`
  `                and recalculees.get("reflexion_observee") is not True:`
  Vérifié en mémoire (module recompilé avec ce remplacement) : Astra 429 → « astra ne confirme pas ['statut', …, 'reflexion_observee'] » ; relevé v71 tel quel → « argon : champ de réflexion absent ou nul… ». Le motif nommé reste premier dans le cas qu'il nomme.
- Essai R5 manquant : l'artefact réel d'Astra de la v71 (amont 429 aux deux appels, usage absent) n'est rejoué nulle part (`grep -n '429\|insufficient' essais/test_pilote_mr2_v72.py` : une seule ligne, 1023, le 429 du relais lui-même au cinquième appel, pas un 429 d'amont ; la doublure ne rend que 200, ou 401 sur clé fausse). À ajouter : une sonde sur la doublure où Astra rend 429, motif attendu « astra ne confirme pas », et **pas** « champ de réflexion ».

### 3. MAJEUR — la mutation N18 survit (prédiction) : l'essai attendu ne fixe pas le texte des consignes

- Fichiers : `essais/mutations_pilote_mr2_v72.py` (N18, lignes 171-172) ; `essais/test_pilote_mr2_v72.py`, `V72.test_configuration_v12_seules_les_consignes_changent` (lignes 2513 à 2526).
- Preuve : N18 remet la seule consigne `borne_gelee` de la v11 ; l'essai attendu vérifie que les consignes v12 **diffèrent** de celles de la v11 (vrai : `borne_courte` diffère encore), que le reste est égal, que chaque consigne tient en 100 octets, que le pire cas vaut 8,052896. Rejoué assertion par assertion sur la configuration mutée (`cd O && python3 -I -B -c` : remplacement du texte de N18, une occurrence, puis les quatre assertions) : versions `True`, consignes différentes `True`, reste égal `True`, longueurs `True`. L'essai passe ; le banc resserre la sélection sur l'essai attendu (`selection_effective`) ; issue attendue : « survit », code du banc 1.
- Portée : la consigne est tenue par l'empreinte de la configuration (bloc gelé, relevé), pas par un essai ; un retour silencieux à « Réponds par le seul mot OK. » dans la configuration ne ferait échouer aucun essai de la classe `V72`.
- Correction : dans l'essai, fixer les deux textes mot pour mot (ou leurs sha256), par exemple après `conf, _ = PC.lire_configuration(CONF)` :
  `        self.assertEqual(conf["sonde"]["consignes"], {"borne_gelee": "Combien d'entiers de 1 à 10000 sont divisibles par 7 ou 11, mais pas par 13 ? Le seul nombre.", "borne_courte": "Énumère un à un les nombres premiers entre 1000 et 1200, en justifiant chacun par ses divisions."})`
  et ajouter la mutation jumelle sur `borne_courte` (N21 ci-dessous).

### 4. MINEUR (à dire au rapport) — `reflexion_observee` n'ajoute aucun refus : elle est impliquée par `verdict_egal_a_la_regle`

- Fichiers : `pole/sonde_pilote_v71.py`, `verdict_reflexion` (lignes 153 à 178 : `t == 0` ou non entier → « indetermine ») ; `pole/sonde_pilote_v72.py`, lignes 59 à 61 et 73 à 76.
- Preuve : énumération de 4 800 usages (Argon et Astra ; sortie, réflexion, total, octets pris dans `None, 0, 1, 5, 40, 256, 300, True, 2.0, '3'` et voisins) : aucun cas où le verdict d'un appel est tranché et `reflexion_observee` fausse (« cas 4800 contre-exemples 0 »). Donc pour Argon et Astra, `verdict_egal_a_la_regle` vraie ⇒ `reflexion_observee` vraie.
- Conséquence : la phrase du rapport « interdit qu'un relevé sans réflexion soit admis par une autre voie » décrit une voie qui n'existait pas ; la mutation N09 (retirer la conclusion de la liste exigée) ne change aucun relevé admis ou refusé (elle n'est tuée que par l'essai d'unité sur le tuple). Sans danger ; à écrire tel quel : la v72 nomme un refus, elle ne durcit rien.

### 5. MAJEUR (risque de la sonde, pas défaut du code) — consignes v12 : confiance moyenne ; trois issues à prévoir avant de payer

Simulation des conclusions v72 sur des réponses plausibles (`S.conclusions` sur des faits construits ; coûts par les prix de la configuration) :

| cas | verdict | conclusions manquantes | coût > pire cas de l'appel |
|---|---|---|---|
| argon A : réflexion 900 puis 250, comptée **dans** la borne | non_comprise | aucune | non |
| argon B : à 256 jetons, 256 candidats **plus** 1 200 de réflexion hors borne | non_comprise | `borne_tenue` | **oui** (0,0732 > 0,0240) |
| argon C : aucune réflexion (comme la v71) | indetermine | verdict, `reflexion_observee` | non |
| argon D : réflexion au seul appel court (toute la borne) | non_comprise | aucune | non |
| argon E : réponse longue malgré « Le seul nombre », total absent | indetermine | verdict | non |
| astra A : un nombre, réflexion comprise | comprise | aucune | non |
| astra B : aucune réflexion | indetermine | verdict, `reflexion_observee` | non |
| astra C : réponse expliquée (300 octets), réflexion 64 | indetermine | verdict | non |

- **Vont-elles faire réfléchir ?** Astra : confiance assez haute (environ 85 %) *si le quota est rétabli* — mais jamais observé (constat 1). Argon : **confiance moyenne, environ 60 %**. Le relevé v71 montre l'absence du champ même sur un texte long, et des totaux sans reste (45 = 40 + 5 ; 308 = 52 + 256) : aucune réflexion cachée. Deux lectures : réflexion décidée par le modèle selon la tâche (alors un dénombrement la déclenche, cas A ou D) ; ou réflexion éteinte tant qu'aucun réglage n'est envoyé (alors aucune consigne n'y fera rien, cas C, et la sonde est perdue). Rien dans le dépôt ne tranche ; la consigne est bien choisie pour la première lecture (calcul réel, réponse 2039, texte visible de quelques octets : le vote « réflexion > sortie » tranche).
- **Coût** : pire cas inchangé (rejoué : 2,588224 ; 1,794112 ; 1,835280 ; 1,835280 ; parts 2,59 ; 1,8 ; 1,84 ; 1,84 ; consignes 94 et 99 octets ≤ 100). Il borne la dépense **si** le plafond de sortie envoyé couvre la réflexion. Pour Argon, règle « ajoutée » : si la réflexion sort du plafond (cas B), le code ne l'empêche pas, il le constate (`cout_excessif` → arrêt, relais verrouillé, relevé partiel, **Astra pas sondé** car il vient après dans `PROPOSEURS`). C'est précisément ce que l'appel à 256 jetons éprouve ; le dépassement plausible reste de l'ordre de centimes à dizaines de centimes (consigne courte), mais il n'est pas borné par la borne gelée. À écrire au devis : « borné si le plafond du fournisseur couvre la réflexion ; sinon constaté après coup ».
- **Troncature à la borne gelée** : très improbable (36 000 jetons et plus pour un nombre) ; si elle arrivait, `raison_arret_normale` fausse → refus, du bon côté.
- **Borne courte « tronquée »** : tenue dans tous les cas plausibles (énumération justifiée > 256 jetons ; ou toute la borne en réflexion, texte vide, cas rejoué par l'essai A-2 et vu au relevé v71 pour les deux proposeurs de Claude : 256 jetons, 0 octet visible, « tronque »).
- Note utile à la mère (non demandée) : pour Argon, la règle gelée « ajoutée » est le choix prudent pour le coût (elle compte candidats + réflexion) ; une règle non confirmée faute de réflexion ne met pas la dépense en danger, elle risque seulement un faux arrêt.

### 6. MINEUR — gardes neuves sans mutation

`any` (un appel sur deux suffit), la garde « détails non objet » de `reflexion_brute`, le champ d'Argon, la configuration v12 dans la liste gelée, la lecture v72 dans `jouer`, l'ordre du refus nommé : mutations proposées ci-dessous.

### 7. MINEUR — commande exacte et essai à sec

- L'essai à sec part d'un registre des lancements **vide** ; le registre réel (`/home/user/hors-depot/lancements-sonde-pilote-mr2.jsonl`) porte déjà la ligne de la v71. La lecture du code dit que des identifiants neufs passent (`exiger_premier_lancement` : intersection vide) ; l'essai à sec devrait le montrer avec une ligne antérieure sous d'autres identifiants.
- La commande passe de `python3 …` (v71, qui a marché) à `env -i … NOM="$NOM"` : une variable absente de la session qui lance arrive **vide** au lanceur. Sans effet pour le proxy (urllib ignore une valeur vide) ni pour `SSL_CERT_FILE` vide (le relais teste `if ca`) ; pour une clé vide, le relais n'est pas « prêt » et la sonde refuse avant tout appel et avant la consignation — mais `os.makedirs(args.sortie)` a déjà eu lieu : le dossier de sortie est à retirer à la main avant de relancer. Dans la session de cette contre-lecture, `HTTP_PROXY` est absent (présence testée par nom, aucune valeur lue). L'essai à sec ne couvre ni le passage des noms, ni l'interpréteur (`/usr/local/bin/python3` avec numpy sous `-I`).
- Le journal `essais-pilote-v72.txt` ne porte ni la commande ni l'empreinte de l'arbre ; le rapport v72 porte encore `@@VERDICT@@`, `@@ESSAIS@@`, `@@BANC@@`.

### 8. MINEUR — textes

- `pole/sonde_pilote_v72.py`, ligne 10, et la configuration (`sources`) : « Claude … n'a aucun compte séparé ». Le relevé v71 porte `output_tokens_details.thinking_tokens` (26 sur 30 ; 256 sur 256) : un compte séparé existe, et il confirme « comprise ». Sans effet sur le code (verdict « sans_champ ») ; à corriger au texte, ou à employer un jour.
- `pole/proposeurs_pilote_v72.py`, ligne 26 : docstring « Configuration v10 » (recopié) ; configuration v12, `sources` : « sous-commande « sonde » du lanceur v70 ».
- Hérité de la v71 : un relevé dont `conclusions` n'est pas un objet lève `AttributeError` (trace, code 1) au lieu d'un `Refus` (ligne 130).

## Mutations proposées (texte exact ; chacune présente une seule fois, vérifié par `str.count`)

| id | fichier | avant | après | essai attendu |
|---|---|---|---|---|
| N21-consigne-courte-de-la-v11 | configuration v12 | `"borne_courte": "Énumère un à un les nombres premiers entre 1000 et 1200, en justifiant chacun par ses divisions."` | `"borne_courte": "Écris un très long texte, de plusieurs milliers de mots, sur l'histoire de la navigation."` | `test_configuration_v12_seules_les_consignes_changent` (après la correction du constat 3 ; N18 y est alors tuée aussi) |
| N22-reflexion-aux-deux-appels | `pole/sonde_pilote_v72.py` | `    return any(_entier_positif(reflexion_brute(dialecte, f.get("usage_brut"))) for f in faits)` | `    return all(_entier_positif(reflexion_brute(dialecte, f.get("usage_brut"))) for f in faits)` | `test_reflexion_observee` |
| N23-details-non-objet | `pole/sonde_pilote_v72.py` | `        x = x.get(b) if isinstance(x, dict) else None` | `        x = x.get(b)` | `test_reflexion_observee` (« astra sans détails ») |
| N24-argon-candidats-pris-pour-reflexion | `pole/sonde_pilote_v72.py` | `CHAMP_DE_REFLEXION = {"gemini": ("thoughtsTokenCount", None),` | `CHAMP_DE_REFLEXION = {"gemini": ("candidatesTokenCount", None),` | `test_reflexion_observee` |
| N25-configuration-v12-hors-du-bloc | `demonstrations/pilote_mr2_v72.py` | `    "exemples/pilote-mr2-v70/configuration-pilote-mr2-v12.json",` | `    "exemples/pilote-mr2-v70/configuration-pilote-mr2-v11.json",` | `test_lanceur_v72` |
| N26-jouer-lit-par-la-v70 | `demonstrations/pilote_mr2_v72.py` | `    conf, _ = PC.lire_configuration(args.configuration)` | `    conf, _ = PR.lire_configuration(args.configuration)` | `test_sain_bout_en_bout` |
| N27-refus-nomme-sur-appel-en-echec (après la correction du constat 2) | `pole/sonde_pilote_v72.py` | ` and recalculees.get("statut") is True and recalculees.get("usage_entier") is True \` | ` \` | l'essai neuf « Astra 429 » du constat 2 |

## Avant la sonde payante, dans l'ordre

1. Quota d'Astra vérifié à la console (constat 1) — sans cela, ne pas lancer.
2. Correction du motif nommé et son essai (constat 2) ; consignes fixées à l'essai (constat 3) ; mutations ci-dessus ; banc entier relu (attendu : toutes tuées, N18 comprise après correction). Toute retouche du code gelé change ses empreintes : la faire **avant** la sonde, le relevé liant le code.
3. Décision de la mère dite d'avance pour l'issue « Argon sans réflexion une seconde fois » (probabilité estimée 40 %) : ne pas écrire une troisième consigne.
4. Devis corrigé d'une phrase (constat 5, coût).
