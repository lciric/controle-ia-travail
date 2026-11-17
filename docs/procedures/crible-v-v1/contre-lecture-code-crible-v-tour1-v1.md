# Contre-lecture du code du crible (v), tour 1 — v1

- **Contre-lecteur** : sous-agent neuf, modèle C ; il n'a écrit aucune des pièces (code écrit par le modèle A ; corrections à venir
  par le modèle A, sous des noms neufs, R12). Première contre-lecture : lecture entière de `lanceur_crible_v_v1.py`, puis de toutes
  les pièces du dossier `docs/procedures/crible-v-v1/` (code, essais, banc, répétition, procédure, devis, gabarits, rapport, sorties
  gardées), contre le texte `docs/notes/organisme-idees-juge-v1/cribles-v1/crible-v-version-foi-v2.md` lu pour ses sections
  « Métrique », « Seuil », « Plan d'analyse », « Étapes », « Critères de lecture gelés », « Liste d'arrêt », « Devis », « Lignes de GO
  proposées ».
- **Heures** (`date -u`) : lecture et rejeux du 2026-11-17 de 01:39 à 01:57 UTC ; rédaction à 01:57 UTC.
- **Non ouverts** : l'issue du pilote MR-2 v14 (seule la section « Pour les cribles » de la consigne est connue), toute branche
  `calcul/pilote-mr2-v74-entree-*`, la pièce de dépense du pilote, la branche de sortie du pilote, le relevé de v67, rien sous `diag/`,
  `runs/`, `donnees/`, rien de 7a, 7b, T0.6, T0.7, P3-bis, du bras d'attaque. Aucune machine, aucun appel au loueur ni à aucun
  fournisseur, aucune clé employée, aucune dépense, aucun commit, aucune pièce du dossier modifiée.

## 0. Verdict : **corrections**

La conception tient (files de mondes, borne par appel, abandon d'un fournisseur, mesure jouée une fois, lecture gelée, machine
sans ssh) et tout ce que le rapport annonce se rejoue à l'identique. **Mais** quatre défauts majeurs, que les essais et le banc ne
voyaient pas, sont démontrés par programme ci-dessous ; chacun est corrigé par un couple « ancien → nouveau » **que j'ai appliqué à
une copie de travail et rejoué** (copie hors du dépôt, détruite ensuite). Ils touchent le lanceur (deux), l'outil de la session (un) et
les essais et le banc (un). Rien ne touche une prédiction, un seuil ou un étage : **les prédictions gelées (R-2993) ne changent pas.**

**Réponse à la question de Lazar (« peut-on les lancer avant le 21 ? »)** : du côté du code, **oui**, rien n'attend le 21 novembre ;
mais pas **avant** les quatre corrections, leur tour différentiel et les pièces de la mère (§ 5). Le goulot n'est pas le code : ce sont
D (non relevée), le scellement du texte sous `prereg/`, l'addendum, les lignes κv1 et κv2, le mot de Lazar sur les clés et sa phrase.
L'accord échoit le 30 novembre.

## 1. Ce que j'ai rejoué (contre le code scellé, sur mon poste, ports décalés, relais factices, mondes d'essai publics)

| contrôle | rejoué | résultat |
|---|---|---|
| empreintes (`sha256sum -c` des 21 compagnons du dossier) | oui | toutes `OK` ; les empreintes du rapport § 1 égales à celles des fichiers |
| essais unitaires | oui (`essais … unitaire`) | **40 essais, 0 échec** |
| essai à blanc complet et scénarios (`jouer`) | oui | **9 essais, 0 échec** ; M = 1 : 80 appels, une coupure à 20 s ; M = 2 : deux files, deux coupures ; pannes, coût, corps, témoin, garde, mode réel refusé |
| reproductibilité | oui | `CARTES.json` et `DOLLARS.json` de mon essai à blanc M = 1 **égaux octet pour octet** aux pièces gardées (`5dbe2f6d…`, `5bf1a69e…`) ; les coupures ne diffèrent que par la durée mesurée |
| mesure (5 essais) | oui | **5 essais, 0 échec** (k_R = 5, S_R = 0,6449, W_R = 15, W_B = 20, p_choix = 0,0036, égaux au recalcul ; division par zéro forcée : code 1, aucune sortie) |
| banc de mutations | oui, entier | **52 mutations tuées sur 52, 3 témoins conformes**, chacune par l'essai qu'elle nomme |
| répétition de la machine | oui, entière | **37 cas, 0 écart** (nominal jusqu'à « fini », phrase absente, feu d'arrêt par PID, minuterie, branche présente, outil de la session) |
| mes mutations en plus (11, hors banc) | oui | 8 tuées ; X7 (`>` → `>=` dans la part) est équivalente à cause de la tolérance 1e-9 ; **X9 et X10 survivent** (voir M4) |

Les mutations exigées par l'étape 0 du texte sont toutes présentes au banc. Le contrôle de « dollars des appels tronqués omis » n'a pas
de mutation nommée, mais je l'ai jouée (X11, `tronque` omis dans `dol`) : tuée par `m_recalcul`.

## 2. Corrections majeures (exigées)

### M1. L'outil de la session refuse la ligne κv1 telle que le texte la propose

**Démonstration.** J'ai pris les deux lignes du bloc « Lignes de GO proposées » du texte (identifiants et dates remplacés) et je les ai
données à `lire_go`, `exiger_kappa` et `exiger_enveloppe` : le plafond de κv1 est écrit **« 104.39 USD (sur crédits) »** (forme du
registre : cf. « 235 USD (sur crédits) » de GO-2026-11-12-01) ; `PLAFOND.fullmatch` n'accepte que « 104.39 USD ».
Sortie : `REFUS kv1 … plafond '104.39 USD (sur crédits)' ≠ 104.39 USD (kv1)` et `REFUS enveloppe : ligne sous l'enveloppe au plafond
illisible`. Le lecteur v66 du lanceur (`lire_go_du_crible`) **accepte** la même ligne : les deux lecteurs divergent. Conséquence :
`creation` et `commande` refusent la création (aucune dépense, mais le feu est bloqué), ou la mère doit écrire une ligne différente de
celle que le texte propose. La répétition n'a pas vu l'écart : son registre d'essai écrit « 104.39 USD » sans la parenthèse.

**Correction** (`session_crible_v_v1.py`, ancien présent une fois) :

ancien :
```
PLAFOND = re.compile(r"([0-9]+(?:\.[0-9]+)?) USD", re.ASCII)
```
nouveau :
```
PLAFOND = re.compile(r"([0-9]+(?:\.[0-9]+)?) USD(?: \((?:sur crédits|hors crédits)\))?", re.ASCII)
```
Rejoué sur la copie : κv1 → 104.39, κv2 → 100.28, enveloppe → 204.67 (= 104.39 + 100.28), lecteur v66 → 104.39 et 100.28.
**À ajouter à la répétition (cas « session »)** : les deux lignes du texte, **telles quelles** (lues dans le bloc du texte), comme cas sain
de `creation` ; et un artefact : « 104.39 USD (sur crédits) » avec un montant différent → refus.

### M2. À M = 2, l'arrêt d'une file n'arrête pas l'autre : jusqu'à 40 appels payants de plus

**Démonstration.** Essai à blanc M = 2, corps du monde 2 (première file « 1 ») altéré, soit « corps servi différent entre les quatre
appels d'un monde : arrêt avant les appels du monde » : le lanceur sort en code 3 **mais les dix mondes de l'autre file ont tous été
joués** (mondes dont des appels sont partis : 1, 3, 5, …, 19 ; 40 appels). Cause : une exception levée **dans** `file()` (corps altéré,
part atteinte, exception imprévue) ne positionne `E.arret` qu'au moment où la boucle de `jouer` lit le résultat de cette file ; or elle
lit les files **dans l'ordre**, donc après la fin de la file 0. Les arrêts qui passent par la liste `erreurs` (coût, témoin, pièces)
positionnent bien `E.arret` aussitôt : le défaut ne touche que les arrêts levés avant les appels du monde. La liste d'arrêt dit
« arrêt avant les appels du monde » et « aucune dépense de plus » ; le crible réel est à M = 1 ou 2 selon D, qui n'est pas encore connue.
Les essais ne jouent ces arrêts qu'à M = 1.

**Correction** (`lanceur_crible_v_v1.py`, ancien présent une fois) :

ancien :
```
            fs = [ex.submit(file, k, mk) for k, mk in enumerate(files)]
```
nouveau :
```
            def file_gardee(k, mk):
                try:
                    file(k, mk)
                except Exception as e:  # noqa: BLE001 — l'arrêt d'une file arrête aussitôt l'autre (aucune dépense de plus)
                    with E.verrou:
                        if not E.arret:
                            E.arret, E.arret_classe = f"{type(e).__name__} : {e}", "arret"
                    raise

            fs = [ex.submit(file_gardee, k, mk) for k, mk in enumerate(files)]
```
Rejoué sur la copie : mondes partis : **[1]** seulement (le monde 1 était déjà en vol à l'instant de l'arrêt) ; les paliers unitaire (40) et
jouer (9) passent encore, 0 échec. **À ajouter** : un essai `j_arret_file_m2` (artefact : corps altéré au monde 2 à M = 2, aucun appel
parti au-delà des mondes déjà en vol) et au banc la mutation « `file_gardee` retirée » tuée par lui.

### M3. La règle d'abandon dépend de l'ordre de traitement des quatre appels d'un monde

**Démonstration.** Mêmes conditions, deux scénarios symétriques, M = 1, appels à blanc : au monde 1, **une** des deux voies de la clé
commune (Pr-2, Pr-4) tombe en panne de relais, l'autre répond.
- `fable52 = panne` : arrêt du crible **au monde 1**, « fournisseur claude abandonné sans aucun appel répondu (perdu en entier) »,
  77 appels « échec » sur 80, alors que l'appel de `opus55` du même monde, parti en même temps, **a répondu** ;
- `opus55 = panne` : le crible **continue** (arrêt nul), 39 appels « échec » (appels restants de la voie « claude »).
Cause : `file()` traite les résultats dans l'ordre `fable52, opus55, argon, astra` ; `traiter_resultat` juge « perdu en entier » sur
`E.repondus_f`, pas encore mis à jour pour les appels du même monde non traités. Le texte dit « perdu en entier = aucun appel répondu
parmi tous les appels du crible de ses proposeurs » : le résultat ne peut pas dépendre de l'ordre des noms. Et Pr-4 est à la fois le
plus cher, le plus lent et le premier de l'ordre.

**Correction** (`lanceur_crible_v_v1.py` ; deux couples, chaque ancien présent une fois) :

ancien 1 :
```
                erreurs = []
                for nom in lancer:
```
nouveau 1 :
```
                erreurs, rendus = [], {}
                for nom in lancer:
```
ancien 2 :
```
                    cs, info = ([], None) if r["etat"] == "echec" else P.cartes_d_un_appel(w, nom, r["texte"])
                    with E.verrou:
                        traiter_resultat(E, w, nom, lignes[nom], r, cs, info)
```
nouveau 2 :
```
                    cs, info = ([], None) if r["etat"] == "echec" else P.cartes_d_un_appel(w, nom, r["texte"])
                    rendus[nom] = (r, cs, info)
                for nom in sorted(rendus, key=lambda n: not repondu_au_lanceur(rendus[n][0], rendus[n][1])):  # répondus d'abord
                    r, cs, info = rendus[nom]
                    with E.verrou:
                        traiter_resultat(E, w, nom, lignes[nom], r, cs, info)
```
Rejoué sur la copie : `fable52 = panne` donne maintenant arrêt nul, 41 appels complets, 39 « échec », comme `opus55 = panne` ; unitaire 40 et
jouer 9 : 0 échec. **À ajouter** : l'essai sain « panne de Pr-4 au monde 1, Pr-2 répond : le crible continue », et la mutation « les
répondus ne passent plus d'abord ».

### M4. Les dollars lus aux journaux des relais et la dépense d'un appel coupé ne sont vérifiés par aucun essai ; deux mutations y survivent

**Démonstration.** Deux mutations de mon banc de contrôle survivent aux trois paliers. X9 : le coût donné à un appel coupé à B_a (le plafond de session)
remplacé par 0,0 : la dépense du fournisseur (`depense_usd`, qui nourrit la garde de la part) perd l'appel coupé, aucun essai ne le voit. X10 : dans `dollars_depuis_les_journaux`, `j = lignes.get((nom, a.get("texte_servi_sha256")), [])`
remplacé par `j = []` : **tous** les dollars des appels non coupés tombent à 0,0 avec la source « journal_relais ». Les trois paliers
passent (`j_blanc_m1` ne vérifie que la source, jamais le montant) ; le banc n'a aucune mutation sur ce chemin (M22 et M23 portent sur
les coupés et sur les échecs de la mesure). Or ce chemin porte **tous** les dollars de S_R, de S_B, de l'étage 3 (a) et de l'audit R4 :
une rupture silencieuse donnerait S_R = 0 et le verdict « pas d'épargne notable ». L'étape 0 du texte demande des mutations qui
touchent les dollars et « toutes tuées pour la raison attendue ».

**Correction** (`essais_crible_v_v1.py`, ancien présent une fois, dans `j_blanc_m1`) :

ancien :
```
    assert all(v["source"] == "journal_relais" for k_, v in dol.items() if k_ != (3, "astra"))
```
nouveau :
```
    assert all(v["source"] == "journal_relais" for k_, v in dol.items() if k_ != (3, "astra"))
    for (w_, n_), v_ in dol.items():  # les dollars d'un appel non coupé sont ceux du journal de son relais (jamais un zéro silencieux)
        if (w_, n_) == (3, "astra"):
            continue
        h_ = [x_ for x_ in rel["appels"] if (x_["monde"], x_["proposeur"]) == (w_, n_)][0]["texte_servi_sha256"]
        j_ = [json.loads(z_) for z_ in open(os.path.join(s, f"journal-relais-f0-{n_}.jsonl")) if z_.strip()]
        att_ = sum(z_["cout_usd"] for z_ in j_ if z_["consigne_recue_sha256"] == h_)
        assert att_ > 0 and abs(v_["cout_config_usd"] - att_) < 1e-9, (w_, n_, v_["cout_config_usd"], att_)
    attendu_ = {n_: sum(v_["cout_config_usd"] for (w_, m_), v_ in dol.items() if m_ == n_) for n_ in c.K.PROPOSEURS}  # coupure comprise (plafond)
    assert all(abs(rel["depense_usd"][n_] - attendu_[n_]) < 1e-6 for n_ in c.K.PROPOSEURS), (rel["depense_usd"], attendu_)
```
et au banc (`banc_mutations_crible_v_v1.py`, ancien présent une fois) :

ancien :
```
    # gardes de la liste d'arrêt
```
nouveau :
```
    ("M29", "dollars lus aux journaux des relais ignorés (lanceur)", L,
     'j = lignes.get((nom, a.get("texte_servi_sha256")), [])', "j = []", "jouer", ["j_blanc_m1"]),
    ("M30", "coût d'un appel coupé à B_a mis à zéro (dépense du fournisseur)", L,
     '"cout_usd": float(p["plafond_session_usd"]), "cout_origine": "plafond_de_session"})',
     '"cout_usd": 0.0, "cout_origine": "plafond_de_session"})', "jouer", ["j_blanc_m1"]),
    # gardes de la liste d'arrêt
```
Rejoué : l'essai corrigé **passe** sur le code sain et **échoue** sur X9 et sur X10 ; M29 et M30 sont **tuées** par `j_blanc_m1`, le témoin T02
reste conforme.

## 3. Corrections mineures (exigées)

**m1. Repli silencieux à zéro dans les dollars** (R5 : « aucun repli silencieux »). `dollars_depuis_les_journaux`, branche finale : un appel
lancé, non coupé, sans aucune ligne au journal est écrit à 0,0 avec la source « journal_relais ». Un appel rendu (complet ou tronqué)
a toujours une ligne ; l'absence signale un écart de rattachement. Le coût que la commande a rendu (`cout_usd` de l'appel) est connu
du lanceur : l'employer évite la perte, sans nouvelle source.

ancien :
```
                out.append({"monde": w, "proposeur": nom, "cout_config_usd": 0.0, "source": "journal_relais"})
```
nouveau :
```
                out.append({"monde": w, "proposeur": nom, "cout_config_usd": float(a.get("cout_usd") or 0.0), "source": "journal_relais"})
```

**m2. Le mode réel n'a d'essai que sur « options absentes ».** `exiger_mode_reel`, `lire_go_du_crible`, `lire_engagement_crible` et le refus du
second lancement ne sont joués par aucun essai (le texte : « chaque ligne a son essai sain et son artefact »). J'ai joué moi-même les
portes qui précèdent le relevé de sonde ; elles refusent bien : options de l'essai à blanc, texte à empreinte différente, addendum à
empreinte différente, D non lançable (16 000 s), M ≠ M de la règle, garde de départ ; les suivantes (GO, engagements, second lancement)
ne sont pas atteignables sans relevé de sonde conforme (voir point 5 de la mère). **À ajouter** à la répétition ou aux essais : un
artefact par porte, et pour `lire_go_du_crible` un cas sain (les deux lignes du texte, M1) et un artefact (même identifiant pour κv1 et κv2 ;
montant différent).

**m3. Procédure et amorce : cadence de la minuterie.** La procédure dit « DELETE chaque minute » ; l'amorce redemande toutes les
**30 s** (`PAS=30`), la cinquième demande tombe donc à 2 minutes.

ancien (procédure, § 0) :
```
(DELETE chaque minute, « stopped » à la cinquième)
```
nouveau :
```
(DELETE toutes les 30 secondes, « stopped » à la cinquième)
```
(Le commentaire d'en-tête de l'amorce dit aussi « chaque minute » : à aligner à l'occasion d'une version neuve de l'amorce ; sans effet
sur le comportement.)

**m4. `--configuration` accepté en mode réel.** Le lanceur du pilote refusait toute configuration autre que celle de l'arbre ; ici le contrôle
d'empreinte (`f69503dd…`) protège, mais l'option devrait être refusée comme les autres options d'essai (la machine ne la passe jamais).

ancien :
```
CHAMPS_A_BLANC = ("scenarios", "lent", "borne_essai_s", "decalage_ports")
```
nouveau :
```
CHAMPS_A_BLANC = ("scenarios", "lent", "borne_essai_s", "decalage_ports", "configuration")
```
(Les essais passent `configuration=None` ; rien d'autre ne change.)

## 4. Remarques facultatives (aucune n'exige de correction)

- **f1.** `tau_0_25` et `toutes_les_composantes` sont deux sensibilités séparées ; le texte les juxtapose (« τ'_i = … ; toutes les composantes (non seulement les
  certifiées, latente comprise) ») : lecture permise, sans verdict.
- **f2.** `exiger_part` ne compte pas l'appel en vol de l'autre file à M = 2 ; borné par le plafond de chaque relais (mondes de la file × plafond de session) : pas de
  dépassement possible, mais l'arrêt par la part peut venir un monde plus tard.
- **f3.** Le banc n'a pas de mutation nommée pour « dollars des appels tronqués omis » (l'essai `m_recalcul` la tue : joué).
- **f4.** `rapatrier` de la machine rend « vrai » sans rien faire si la destination existe déjà : sans effet dans le déroulé prévu.
- **f5.** Un état du journal de la machine du crible (`sonde reelle`, `jouer reel en cours`) n'entre dans aucune durée de D ; c'est la réserve (2) du texte, déjà dite.

## 5. Points pour la mère (à trancher ou à savoir)

1. **Les corrections font de nouvelles versions** (R12) par le modèle A : `lanceur`, `session`, `essais`, `banc`, procédure ; l'addendum
   d'empreintes (§ 1 des gabarits) prendra les nouvelles ; le rapport § 1 est à refaire ; **banc entier, essais, répétition à rejouer**
   (la session a changé) ; **tour différentiel 2** de ce code sur les seuls couples. Rien n'est à changer au texte ni aux prédictions.
2. **Ligne κv1 (M1).** Avant la correction, la forme proposée par le texte, « 104.39 USD (sur crédits) », est refusée par l'outil de la
   session. Contournement sans changer le code : inscrire le plafond « 104.39 USD » (les deux lecteurs l'acceptent) ; c'est à toi de dire si
   la ligne du texte et la ligne inscrite peuvent différer d'une parenthèse. Je recommande la correction du code.
3. **D non relevée** : les quatre durées sont sur la branche de sortie du pilote (journal d'états) que je n'ai pas ouverte ; sans elles le
   budget reste « non lançable » (règle écrite). **Garde de départ** : lue à la lettre, elle compte les barrières déjà passées ; si D sort
   au-dessus d'environ 9 à 10 ks, elle refusera au départ de `jouer`, **après** la sonde payante (≈ 8 USD) : tu peux faire juger la
   garde par la machine avant la sonde (changement de code, donc tour 2) ou vérifier D avant le feu 3.
4. **R5, relevé de sonde** : aucun cas sain du refus « relevé de sonde absent, invalide ou d'un autre code » n'existe hors d'un appel réel
   (réserve 14 du rapport) ; le texte dit « aucune ligne sans ses deux essais » : c'est un écart déclaré, à accepter ou à lever (un
   relevé conforme fabriqué par le module de la sonde sur des faits d'essai). Le premier relevé conforme n'apparaîtra qu'au feu : si
   `exiger_releve_sonde` le refuse, la sonde payée est perdue et le crible ne part pas.
5. **Coupure à B_a comptée au plafond de session** (réserve 3) : le texte est muet sur le coût d'un appel coupé sans ligne de journal ;
   le choix est prudent (borne haute), rapporté (`dollars_sources`) ; à confirmer comme lecture du texte (il gonfle les dollars de la moitié
   concernée, donc S_R).
6. **Archive fictive** (réserve 5) : trois archives (K1 ; K1 et chaque composante forte ou moyenne ; K1 et toutes ensemble) pour « K1 et
   les composantes fortes et moyennes du monde » ; sensibilité sans verdict : acceptable, dire que c'est une lecture.
7. **Partie A** : jamais jouée, forme du relevé de v67 non vérifiée ; le premier lecteur du relevé doit relire l'adaptateur avant l'essai
   sain ; sans effet sur la partie B.
8. **Mot de Lazar** : clés et jeton passés à la machine du crible (GO-2026-11-15-04 ne portait que sur le pilote), présence et phrase ;
   enveloppe : ce crible 204,67 USD seul, avec (iii) 474,67, les cinq ensemble au-dessus de 1 275 (nœud de Lazar, déjà écrit au texte).
9. **Poste** : disque presque plein (1,6 Go libres pendant mes rejeux) et ports 8811 à 8824 pris par une autre session : mes rejeux sont à
   ports décalés ; la machine louée est isolée, sans objet là.

## 6. Les cinq vérifications demandées

1. **Le code fait ce que la pièce fixe et rien d'autre** : oui, sauf M2 (arrêt entre files) et M3 (ordre) ; files (k + 1, k + 1 + M, …), ports
   + 10 k, plafond de relais = mondes de la file × plafond de session, quatre appels d'un monde ensemble, B_a = 900 s, gabarit
   `e77d3041…`, corps égaux, garde de départ (6 000 + 3 D + ⌈20/M⌉ × 900), règle de M (12 400 / 15 400), part = 20 × plafond, parts de κ
   (somme exacte 104,39 et 100,28), copie au sens dirigé, `>` strict, couvertures hors K1, placebo exact, rééchantillonnage `(99, b)`,
   jeu public `(r, 30)`, étages 0 à 6 et V1 à V7 : tous relus contre le texte, conformes.
2. **Essai à blanc et banc rejoués** : oui (§ 1) ; chaque mutation du banc détectée ; un trou (M4) et une absence nommée (f3).
3. **Gardes R5** : chaque ligne de la liste d'arrêt a son essai, sauf le relevé de sonde (sain, point 4) et les portes du mode réel
   après le relevé (m2) ; un repli silencieux (m1).
4. **Procédure tapable ; leçons de l'idée 1.1** : arguments de chaque geste égaux aux sous-commandes de l'outil (compte des arguments
   relu geste par geste) ; reprise de la poussée (toutes les 5 minutes jusqu'à l'échéance), minuterie armée avant toute passe,
   destruction par l'identifiant lu et preuve d'absence par témoin, garde jouée sur chaque offre, ligne contrôlée par programme, prix
   relu, garde de dépense : repris et rejoués en répétition (37 cas) ; seules m3 et M1 gênent ; D (non relevée) bloque le feu.
5. **Aucune clé, aucun appel réel, aucun identifiant de modèle** : recherche de motifs de clés et de noms de modèles dans tous les fichiers
   du dossier : aucun ; seuls les noms de clés de configuration (`opus55`, `fable52`, `argon`, `astra`) et les noms de variables. Les
   essais n'emploient que des relais factices ; la sonde et le mode réel n'ont d'essai qu'en refus.

## 7. Incidents de ma main

- Premier lancement des essais avec un chemin d'arbre faux (le dossier racine au lieu de `orchestrator`) : refus nommé du lanceur, relancé
  correctement ; premier appel manuel du lanceur avec un chemin relatif : refus nommé ; une commande avec attente a été bloquée par l'outil
  (aucun effet).
- J'ai lu le registre `registres/go.md` (lecture seule) pour comparer la forme des plafonds des lignes « calcul » ; j'y ai affiché quelques
  colonnes de lignes de GO sans lien avec ce crible. Je n'ai ouvert que mon dossier de travail dans le scratchpad (copie de l'arbre
  de l'organisme à la tête 605e0f6 et mondes d'essai publics déjà présents) ; une recherche de fichiers par nom a listé des chemins
  d'autres tâches du scratchpad, sans les ouvrir.
- Aucun commit, aucune pièce existante modifiée (`git status` : seules les pièces neuves non suivies du dossier) ; aucune machine ni
  aucun appel ; mes copies mutées et mes sorties sont dans le scratchpad, nettoyées en grande partie.
