# Rapport : collisionneur v9 v6 (corrections de la contre-lecture) et consultation v6

Écrit le 21 novembre 2026 par le développeur du v9-v5 (Claude Opus 5.5). Pièce de classe B : le même contre-lecteur, Fable, vérifie les corrections.

Ce que je n'ai pas fait :
- aucun appel à un modèle, aucun comptage, aucune requête réseau, aucune dépense ;
- aucune valeur de clé lue ni affichée ;
- aucun commit ;
- rien sous runs/, archives-reponses-modeles/ ou docs/notes/bras-attaque/ ;
- aucune suppression.

Le v9-v5 et la consultation v5 ne sont pas touchés : sceaux vérifiés avant la copie, `697f0151…` et `4c44b89e…`.

## 1. Corrections obligatoires, au code exact de la contre-lecture

Contre-lecture : `contre-lecture-collisionneur-v9-v5-v1.md`, `77041a13…`.

| correction | ce qui est fait | essais |
|---|---|---|
| **CO-1** : un défaut de réglage n'est jamais renvoyé au même réglage | Fonction `reglage_en_defaut(dossier, cid, m)`, placée après `STATUT_REGLAGE`. Branche ajoutée dans `lancer_etage`, juste après celle du refus : la cellule n'est pas renvoyée, elle est comptée bloquée, et la porte se ferme. Code repris à la lettre. | `test_v6_defaut_de_reglage_jamais_renvoye_au_meme_reglage` : premier lancement au code 9 ; la même commande n'envoie rien à Carbon et ferme la porte au code 2 ; l'absence acceptée laisse finir l'étage. `test_v6_defaut_de_reglage_renvoye_si_le_reglage_a_change` : une autre provision ou un plafond plus haut libèrent la cellule. |
| **CO-2** : aucun repli dormant sur la clé par défaut | `appeler_openai` et `compter_openai` refusent un nom absent de la composition : échec à l'envoi, `COMPTE_IMPOSSIBLE` au comptage. `OPENAI_API_KEY` n'est plus lue à sa place. | `test_v6_cle_openai_sans_nom_dans_la_composition_aucun_repli` |
| **CO-3** : essai témoin contre la mutation « code 9 étendu à toute sortie vide » | Essai seul, sans changement de code. | `test_v6_sortie_vide_fin_stop_relancee_comme_la_v3`, pour Carbon et Neon : une sortie vide terminée par « STOP » est relancée comme dans le v3. |
| **CO-4** : erratum du rapport du v5 | `rapport-collisionneur-v9-v5-et-consultation-v5-v1-erratum-1.md`. Le texte de la contre-lecture y est repris tel quel. Une puce ajoutée dit la suite donnée : la v6. | — |

## 2. Décisions de routine de la mère

**Provisions de Carbon.** Carbon reprend les réglages du v9-v4 :
- provision 49 152 (`PROVISION_CARBON_V6`), plafonds 65 536 ;
- il reste donc 16 384 jetons de texte, au-dessus du plancher de 16 000 de la règle du plafond large ;
- le budget envoyé reste égal au seuil de la garde : ils ne sont pas séparés dans cette version ;
- Argon et Neon gardent leurs réglages du v9-v5 ;
- la ligne de Carbon est identique à celle du v9-v4 (vérifié par un essai) ;
- le délai de 5 400 s couvre 114 688 jetons comptés à 25 jetons par seconde (4 588 s).

**Pire cas de Carbon.** Même formule qu'avant. Le pire cas « avec relance », demandé par la contre-lecture pour tout devis, est le double du pire cas simple.

| garde d'entrée | Carbon, v9-v6 | Carbon, avec relance | Neon, inchangé | Neon, avec relance |
|---|---|---|---|---|
| 0 jeton | 2,2938 USD | 4,5875 USD | 1,4746 USD | 2,9491 USD |
| 29 800 jetons | 2,4130 USD | 4,8259 USD | 1,5640 USD | 3,1279 USD |
| 70 004 jetons | 2,5738 USD | 5,1476 USD | 1,6846 USD | 3,3691 USD |

Rejouée sur la v6, la critique de Carbon du 20 novembre est gardée (`OK`) : 27 122 jetons d'entrée, 39 953 jetons de pensées, 10 298 visibles. Une réflexion de 49 153 jetons donne le code 6.

**`--cle-openai`.** Le nom doit commencer par `OPENAI_API_KEY` (constante `PREFIXE_CLE_OPENAI`).
- Sinon, refus au code 1 : à la composition, ou par la ligne de commande avant toute écriture, sans aucun appel et sans répéter le nom.
- Refusés à l'essai : `GEMINI_API_KEY`, `TYPESAFE_API_KEY`, `MA_CLE`, `CLE_OPENAI_API_KEY`, `OPENAI_KEY`.
- Acceptés à l'essai : `OPENAI_API_KEY`, `OPENAI_API_KEY_2`, `OPENAI_API_KEY2`.
- La consultation v5 avait le même défaut : la **consultation v6** porte la même garde, et ne change rien d'autre.

**Réponse coupée.** La relance au même plafond est gardée.

## 3. Essais

Lancés avec `--basetemp` et `TMPDIR` sous mon bloc-notes, et COPIE_RUN_DOPAMINE non posée.

| suite | sur | résultat |
|---|---|---|
| `test_collisionneur_v9_v6.py` | v9-v6 | **201 passés, 1 sauté** (la copie du run, non désignée) |
| `test_collisionneur_v9_v5.py`, non-régression | v9-v5 | 186 passés, 1 sauté |
| essais v3 et complément, copie sans run | v9-v3 | 156 passés, 1 sauté |
| `essais_appel_modeles_externes_v6.py` | consultation v6 | **23 passés**, avec pytest et avec le lanceur du fichier |
| `essais_appel_modeles_externes_v5.py`, non-régression | consultation v5 | 21 passés |
| `essais_appel_modeles_externes_v4.py`, non-régression | consultation v4 | 10 passés |

**Écarts voulus dans les essais repris du v5.**

Collisionneur, trois essais adaptés à la provision de Carbon :
- `test_garde_a_sain_budget_pose_et_reflexion_dans_la_provision` : 49 152 de pensées et de budget ;
- `test_garde_a_provision_comptee_avant_l_envoi` : pire cas sur 65 536 + 49 152 ;
- `test_v5_neon_au_catalogue_seule_difference_avec_la_v3` : provision de Carbon à 49 152, version « v9-v6 ».

Consultation, deux écarts :
- la version du script attendue est « v6 » ;
- l'essai qui vérifie que la ligne de commande transmet l'option nomme maintenant une variable absente au préfixe imposé, `OPENAI_API_KEY_ABSENTE_ESSAI_V6`.

**Essais neufs.**
- Collisionneur, 15 :
  - CO-1, deux essais ;
  - CO-2, un ;
  - CO-3, deux ;
  - préfixe de la clé : 5 refusés et 3 acceptés ;
  - réglages de Carbon : deux.
- Consultation, 2 : préfixe refusé, préfixe accepté.

## 4. Mutations

Faites sur des copies dans le bloc-notes, par `outils/mutations_v6.py`, chaque copie avec son `--basetemp` et son `TMPDIR`. Les copies non mutées passent toutes : 201 essais du collisionneur, 23 de la consultation. **Les 25 mutations (19 du collisionneur, 6 de la consultation) sont toutes prises.**

| mutation | essais en échec |
|---|---|
| collisionneur : CO-1 retirée, renvoi au même réglage | 1 |
| collisionneur : CO-1, provision ignorée dans la comparaison | 1 |
| collisionneur : CO-1, plafond ignoré dans la comparaison | 1 |
| collisionneur : CO-2, repli sur la clé par défaut à l'envoi | 1 |
| collisionneur : CO-2, repli sur la clé par défaut au comptage | 1 |
| collisionneur : **code 9 étendu à toute sortie vide, fin « STOP » comprise** (la mutation que le v9-v5 ne prenait pas) | **2** |
| collisionneur : préfixe de `--cle-openai` retiré | 5 |
| collisionneur : préfixe réduit à `OPENAI` | 8 |
| collisionneur : nom refusé répété dans le message | 5 |
| collisionneur : provision de Carbon ramenée à 32 768 | 5 |
| collisionneur : provision de Carbon à 49 537, soit 15 999 jetons de texte | 48 |
| collisionneur : code 9 retiré | 4 |
| collisionneur : règle retirée avant le comptage | 2 |
| collisionneur : règle retirée à la composition | 4 |
| collisionneur : plancher à 15 000 | 7 |
| collisionneur : nom de clé ignoré à la composition | 7 |
| collisionneur : `--cle-openai` non transmise | 9 |
| collisionneur : prix de Neon à 2 et 10 | 5 |
| collisionneur : Neon avant Carbon dans l'ordre | 4 |
| consultation : préfixe retiré | 1 |
| consultation : préfixe réduit à `OPENAI` | 1 |
| consultation : nom refusé répété dans le message | 1 |
| consultation : option ignorée à l'exécution | 4 |
| consultation : option non transmise par `main` | 1 |
| consultation : Neon hors du plancher de texte | 2 |

À la première passe, la mutation « nom répété » de la consultation n'était pas prise. J'ai ajouté une assertion « nom non répété » à l'essai du préfixe, dans les deux scripts, et ajouté la même mutation au collisionneur. Les chiffres ci-dessus sont ceux de la seconde passe.

## 5. Réserves

1. **Budget et seuil non séparés.** Si la réflexion de Carbon dépasse le budget de 22 %, comme le 20 novembre, la garde l'arrête au code 6. Si Google coupe à 65 536, pensées comprises, avant ce dépassement, il ne reste qu'environ 5 600 jetons au texte. C'était la réserve 1 de la contre-lecture de la v4 et la section 7 de celle du v9-v5. Un tel cas finirait en `TRONQUE`, ou au code 9 s'il n'y a aucun texte.
2. **Le préfixe ne prouve pas que la variable porte une clé d'OpenAI.** Il empêche seulement de nommer `GEMINI_API_KEY` ou une autre variable connue.
3. **Remarques non bloquantes de la contre-lecture, non traitées dans cette version :**
   - `--reflexion 0` est encore accepté pour Carbon et Neon dans la consultation (remarque 2) ;
   - essai de la consultation pour un budget refusé chez Neon (remarque 7) ;
   - garde « coupure sous le plafond envoyé » (réserve 3).
4. **Avant tout appel**, la contre-lecture demande encore deux choses : un envoi d'essai à Neon par la consultation, qui est une dépense et attend ton accord, et une commande de lancement contre-lue.

## 6. Pièces

| fichier | empreinte |
|---|---|
| `docs/notes/collisionneur-v9/collisionneur_v9_v6.py` | `3c6a4cfb49ad22014285be73744e4fa619b08c55069e0ae19d699b5b138b61a7` |
| `docs/notes/collisionneur-v9/test_collisionneur_v9_v6.py` | `cd4c1337beb01a376bff6a616906ccdfba95cb97e485c208a9409f80db975b21` |
| `docs/notes/collisionneur-v9/rapport-collisionneur-v9-v5-et-consultation-v5-v1-erratum-1.md` | `4519f20331c5252e258690b2d2353c954e23072b37020a3b121f4e6c06325fd9` |
| `docs/notes/papier-dopamine-moniteur-v1/approfondissement-v1/appel_modeles_externes_v6.py` | `e2095843da99754b7e9e1908a51d84ad2b50ee87b4376b562e35489a6f893cb1` |
| `docs/notes/papier-dopamine-moniteur-v1/approfondissement-v1/essais_appel_modeles_externes_v6.py` | `58738dca543e93838b44448ead4ffee103b28b6e61973a96708860c260dcc302` |

Chacune a son compagnon `.sha256`.

## 7. Différentiels, v5 vers v6

### 7.1 Collisionneur : v9-v5 (`697f0151…`) vers v9-v6 (`3c6a4cfb…`), différentiel unifié complet

```diff
--- collisionneur_v9_v5.py
+++ collisionneur_v9_v6.py
@@ -44,6 +44,15 @@
 #   (défaut OPENAI_API_KEY) : nom de la variable qui porte la clé d'OpenAI, lue pour l'envoi et pour le comptage, jamais
 #   affichée.
 #   Détail : rapport-collisionneur-v9-v5-et-consultation-v5-v1.md, même dossier.
+# v9-v6 (même développeur, 21 novembre 2026) : copie du v9-v5 (697f0151…, inchangé, R12), corrigée après la contre-lecture
+#   contre-lecture-collisionneur-v9-v5-v1.md (77041a13…), et sur les décisions de routine de la mère. Changements, et
+#   seulement ceux-là : (CO-1) une cellule arrêtée au code 9 n'est jamais renvoyée au même réglage, pas même par une
+#   nouvelle commande (reglage_en_defaut, lu dans lancer_etage) ; (CO-2) aucun repli sur la clé d'OpenAI par défaut dans
+#   appeler_openai et compter_openai : un nom absent de la composition est refusé ; (décision de la mère) --cle-openai
+#   n'accepte qu'un nom qui commence par OPENAI_API_KEY (la clé d'un autre fournisseur ne part jamais vers OpenAI) ;
+#   (décision de la mère) Carbon reprend les réglages du v9-v4 : provision 49 152, plafonds 65 536, soit 16 384 jetons de
+#   texte ; le budget envoyé reste égal au seuil de la garde. La relance d'une réponse coupée au même plafond est gardée.
+#   Détail : rapport-collisionneur-v9-v6-v1.md, même dossier.
 """Collisionneur épistémique N×3 (N = nombre d'espèces activées, de deux à sept), protocole v2 : orchestration déterministe,
 sans agent.
 
@@ -62,17 +71,17 @@
 cette question ; c'est pourquoi il reste séparé des étages I et II, qui gardent leur émission à l'aveugle (règle B2).
 
 Usage (ESPÈCES : au moins deux options parmi --fable --opus --argon --kimi --astra --carbon --neon, toujours écrites) :
-  python collisionneur_v9_v5.py devis   ESPÈCES --faits FAITS.md [--question QUESTION.md]
-  python collisionneur_v9_v5.py etage1  ESPÈCES [--cle-anthropic NOM] [--cle-openai NOM] --faits FAITS.md --sortie DOSSIER
+  python collisionneur_v9_v6.py devis   ESPÈCES --faits FAITS.md [--question QUESTION.md]
+  python collisionneur_v9_v6.py etage1  ESPÈCES [--cle-anthropic NOM] [--cle-openai NOM] --faits FAITS.md --sortie DOSSIER
                                         [--plafond-usd 40] [--ligne-usd MONTANT] [--reprise] [--accepter-absence ID]
-  python collisionneur_v9_v5.py etage2  ESPÈCES [--cle-anthropic NOM] [--cle-openai NOM] --sortie DOSSIER
+  python collisionneur_v9_v6.py etage2  ESPÈCES [--cle-anthropic NOM] [--cle-openai NOM] --sortie DOSSIER
                                         --arbitrage ARBITRAGE.md [...]
-  python collisionneur_v9_v5.py etage3  ESPÈCES [--cle-anthropic NOM] [--cle-openai NOM] --sortie DOSSIER
+  python collisionneur_v9_v6.py etage3  ESPÈCES [--cle-anthropic NOM] [--cle-openai NOM] --sortie DOSSIER
                                         --question QUESTION.md [--faits FAITS.md] [--plafond-usd 40] [--ligne-usd MONTANT]
                                         [--reprise]
-  python collisionneur_v9_v5.py devis-reprise DOSSIER --ligne-usd MONTANT [--max-fable N]   (sans réseau)
-  python collisionneur_v9_v5.py verifier DOSSIER
-  python collisionneur_v9_v5.py jev-test
+  python collisionneur_v9_v6.py devis-reprise DOSSIER --ligne-usd MONTANT [--max-fable N]   (sans réseau)
+  python collisionneur_v9_v6.py verifier DOSSIER
+  python collisionneur_v9_v6.py jev-test
 --ligne-usd MONTANT (v9-v3) : ligne de dépense ouverte au premier lancement qui la donne, consignée au journal ; tout envoi
 dont le pire cas ferait dépasser la ligne (dépense depuis son ouverture) est refusé avant l'envoi.
 --reprise (v9-v3) : déclare au journal qu'un run commencé par un autre script est repris par celui-ci ; sans elle, le
@@ -80,7 +89,8 @@
 --cle-anthropic NOM : nom de la variable d'environnement qui porte la clé d'Anthropic (obligatoire avec --fable ou --opus) ;
 --nom-espace-anthropic NOM : nom de la variable de l'espace de travail, s'il en faut un (défaut ANTHROPIC_WORKSPACE_ID).
 --cle-openai NOM (v9-v5) : nom de la variable d'environnement qui porte la clé d'OpenAI (défaut OPENAI_API_KEY), lue pour
-l'envoi et pour le comptage d'Astra ; la valeur n'est jamais affichée ni écrite.
+l'envoi et pour le comptage d'Astra ; la valeur n'est jamais affichée ni écrite. v9-v6 : le nom doit commencer par
+OPENAI_API_KEY (par exemple OPENAI_API_KEY_2) ; tout autre nom est refusé (code 1).
 Option --jev (étages et devis) : Jev, de TypeSafe AI, audite chaque cellule valide, seule : il ne lit jamais deux
 propositions ensemble, ni les attaques d'une autre. Ses notes vont à l'arbitre, dans jev/notes-jev.md, à lire après les
 cellules, et n'entrent jamais dans un prompt des modèles. Aucun classement n'est produit. Un échec de Jev est consigné
@@ -93,7 +103,8 @@
 de la provision, total de jetons au-delà des champs lus, entrée au-delà de l'entrée gardée, usage absent), 7 refus de la garde
 de motifs (rien n'est envoyé), 8 (v9-v3) comptage des jetons d'entrée impossible ou invraisemblable (rien n'est envoyé),
 9 (v9-v5) défaut de réglage chez une espèce sous la règle du plafond large (Carbon, Neon) : arrêt en MAX_TOKENS sans texte
-(coût réel compté, aucune relance au même réglage, aucune cellule écrite).
+(coût réel compté, aucune relance au même réglage, aucune cellule écrite ; v9-v6 : une commande suivante ne la renvoie
+pas non plus tant que le réglage du script est le même, il faut --accepter-absence ou un script au réglage corrigé).
 Le code 4 couvre aussi (v9-v3) la ligne de dépense : refus avant l'envoi, rien n'est envoyé. Le code 1 couvre aussi (v9-v5)
 un réglage hors de la règle du plafond large (moins de 16 000 jetons de texte au-delà de la provision) : refus à la
 composition, ou avant l'envoi (consigné), rien n'est envoyé.
@@ -116,7 +127,7 @@
 from dataclasses import dataclass, field
 from pathlib import Path
 
-VERSION = "collisionneur-v9-v5"
+VERSION = "collisionneur-v9-v6"
 
 # ---------- table des espèces ----------
 # Prix en USD par million de jetons (entrée, sortie), avec leur source :
@@ -146,6 +157,14 @@
 #   Page du modèle (docs/sources/prix/page-modele-gemini-4-neon-20261121T134943Z.html, 2eadc192…) : « Max output 65,536
 #   (default synchronous) », réflexion « Supported (low, medium, high, xhigh) ». Aucun budget de réflexion n'y est documenté.
 # Plafonds de sortie, relance et provision de réflexion : devis v3, section 3 (Carbon : « réglages supposés »).
+# v9-v6 (décision de la mère, sur la recommandation de la contre-lecture du v9-v5, section 7) : Carbon reprend les réglages
+# du v9-v4 (46f1d917…, rapport-developpeur-collisionneur-v9-v4.md) : provision 49 152 (= 65 536 − 16 384), plafonds 65 536.
+# Raison : sous 32 768, la critique de Carbon du tour 2 du 20 novembre a été arrêtée, payée et sans cellule (39 953 jetons
+# de pensées, garde de réflexion) ; la demande du directeur du 20 novembre (« plus de provision de réflexion à Carbon et
+# Argon ») ; la règle du plafond large tient : 65 536 − 49 152 = 16 384 ≥ 16 000. Le budget envoyé reste la provision
+# (seuil de la garde = budget) ; leur séparation n'est pas faite dans cette version. Argon garde les réglages du v9-v3.
+# Délai de Carbon inchangé : 65 536 + 49 152 = 114 688 jetons comptés, à 25 jetons par seconde 4 588 s < 5 400 s.
+PROVISION_CARBON_V6 = 49152
 # Neon (v9-v5) : sortie et relance 65 536 (plafond synchrone de la page du modèle et de la liste) ; provision 32 768, comme
 # Carbon, soit 32 768 jetons de texte au-delà, au-dessus du plancher de 16 000 de la règle (REGLE_TEXTE_MIN) ; délai 5 400 s,
 # comme Carbon (même compte : 65 536 + 32 768 jetons à 25 jetons par seconde, 3 932 s). Réglages SUPPOSÉS : aucun envoi à
@@ -171,7 +190,8 @@
     "astra": {"id": "gpt-6.2-astra", "fournisseur": "openai", "prix": (10.0, 50.0),
               "max": 8000, "max_relance": 32000, "provision": 0, "car_par_jeton": 2.5, "delai_s": 3600},
     "carbon": {"id": "gemini-4-carbon", "fournisseur": "gemini", "prix": (4.0, 20.0),
-               "max": 65536, "max_relance": 65536, "provision": 32768, "car_par_jeton": 2.5, "delai_s": 5400},
+               "max": 65536, "max_relance": 65536, "provision": PROVISION_CARBON_V6, "car_par_jeton": 2.5,
+               "delai_s": 5400},
     "neon": {"id": "gemini-4-neon", "fournisseur": "gemini", "prix": (3.0, 15.0),
              "max": 65536, "max_relance": 65536, "provision": 32768, "car_par_jeton": 2.5, "delai_s": 5400},
 }
@@ -185,6 +205,9 @@
 # de texte au-delà de la provision. Un arrêt en MAX_TOKENS sans texte chez ces espèces est un défaut de réglage, pas une
 # réponse (code 9, sans relance au même réglage).
 REGLE_TEXTE_MIN = {"carbon": 16000, "neon": 16000}
+# v9-v6 (décision de la mère) : tout nom donné à --cle-openai commence par ce préfixe ; GEMINI_API_KEY, TYPESAFE_API_KEY ou
+# la variable d'Anthropic sont donc refusés.
+PREFIXE_CLE_OPENAI = "OPENAI_API_KEY"
 
 # Composition du run : fixée par fixer_composition, à partir des options (ou du dossier, pour `verifier`). Vide au départ :
 # aucune espèce n'est implicite.
@@ -546,6 +569,9 @@
     for nom in (nom_cle_anthropic, nom_espace_anthropic, nom_cle_openai):
         if nom is not None and not MOTIF_NOM_VARIABLE.match(nom):
             raise Arret(CODE_USAGE, "nom de variable d'environnement mal formé (lettres majuscules, chiffres, « _ »)")
+    if not nom_cle_openai.startswith(PREFIXE_CLE_OPENAI):  # v9-v6 : la clé d'un autre fournisseur ne part jamais vers OpenAI
+        raise Arret(CODE_USAGE, f"--cle-openai : le nom doit commencer par {PREFIXE_CLE_OPENAI} (une clé ne part jamais "
+                                f"vers un autre fournisseur que le sien)")
     modeles = {}
     for i, espece in enumerate(choisies):
         m = dict(CATALOGUE[espece], espece=espece)
@@ -996,7 +1022,9 @@
     les INTERVALLE_RELEVE_S secondes, jusqu'au délai de l'espèce. La création n'est jamais renvoyée (sauf 429) ; un relevé
     manqué n'est pas un renvoi et se refait. Délai dépassé : annulation demandée, envoi compté au pire. Clé lue dans la
     variable nommée par --cle-openai (v9-v5 ; défaut OPENAI_API_KEY), jamais affichée."""
-    nom_cle = m.get("nom_cle") or NOMS_CLES["openai"]  # v9-v5
+    nom_cle = m.get("nom_cle")  # v9-v6 : le nom vient de la composition ; jamais de repli sur la clé par défaut
+    if not nom_cle:
+        return Reponse(echec="nom de la variable de la clé d'OpenAI absent de la composition (--cle-openai)")
     cle = os.environ.get(nom_cle)
     if not cle:
         return Reponse(echec=f"{nom_cle} absente (variable nommée par --cle-openai)")
@@ -1216,7 +1244,10 @@
 def compter_openai(m, prompt):
     """POST /responses/input_tokens (interface Responses) : même modèle et même entrée que l'envoi ; même restriction
     d'adresse que l'envoi (base_openai). v9-v5 : clé lue dans la variable nommée par --cle-openai."""
-    nom_cle = m.get("nom_cle") or NOMS_CLES["openai"]  # v9-v5
+    nom_cle = m.get("nom_cle")  # v9-v6 : le nom vient de la composition ; jamais de repli sur la clé par défaut
+    if not nom_cle:
+        raise RefusCompte("COMPTE_IMPOSSIBLE", "nom de la variable de la clé d'OpenAI absent de la composition "
+                                               "(--cle-openai)")
     cle = os.environ.get(nom_cle)
     if not cle:
         raise RefusCompte("COMPTE_IMPOSSIBLE", f"{nom_cle} absente (variable nommée par --cle-openai)")
@@ -1328,6 +1359,18 @@
 STATUT_REGLAGE = "MAX_TOKENS_SANS_TEXTE"
 
 
+def reglage_en_defaut(dossier, cid, m):
+    """v9-v6 (CO-1) : vrai si le dernier essai de la cellule s'est arrêté en MAX_TOKENS sans texte (STATUT_REGLAGE) sous le
+    réglage que le script enverrait de nouveau : même provision, et aucun plafond de sortie au-dessus de celui de cet
+    essai. Une telle cellule n'est jamais renvoyée : il faut une absence acceptée, ou un script au réglage corrigé."""
+    essais = essais_journal(dossier, cid)
+    if not essais or essais[-1]["statut"] != STATUT_REGLAGE:
+        return False
+    dernier = essais[-1]
+    return (dernier.get("provision_reflexion") == m["provision"]
+            and max(m["max"], m["max_relance"]) <= dernier.get("max_tokens", 0))
+
+
 def juger(m, rep, prompt, pire, garde=None):
     """v9 : statut et coût compté d'un envoi. Envoi interrompu ou usage absent : pire cas. Sinon, coût réel sur l'usage
     (écart de Google compris), puis les gardes : réflexion au-delà de la provision, écart de total (Google), entrée au-delà
@@ -1550,6 +1593,12 @@
             elif statut_courant(dossier, cid) == "REFUS":
                 bloquees.append(cid)  # un refus est définitif dans un run
                 continue
+            elif reglage_en_defaut(dossier, cid, MODELES[lettre]):  # v9-v6 (CO-1) : jamais de renvoi au même réglage
+                print(f"{cid} : arrêt en MAX_TOKENS sans texte au dernier essai, réglage inchangé (plafond et "
+                      f"provision) : non renvoyée ; il faut --accepter-absence, ou un script au réglage corrigé "
+                      f"(--reprise)", flush=True)
+                bloquees.append(cid)
+                continue
             else:
                 prompt, pieces = construire_prompt(dossier, tour, lettre, retenues, absences)
                 if executer_cellule(dossier, tour, lettre, prompt, pieces, plafond, appelants) != "OK":
@@ -1879,7 +1928,8 @@
         s.add_argument("--cle-anthropic", help="NOM de la variable d'environnement qui porte la clé d'Anthropic")
         s.add_argument("--nom-espace-anthropic", default="ANTHROPIC_WORKSPACE_ID")
         s.add_argument("--cle-openai", default=NOMS_CLES["openai"],  # v9-v5
-                       help="NOM de la variable d'environnement qui porte la clé d'OpenAI (défaut OPENAI_API_KEY)")
+                       help="NOM de la variable d'environnement qui porte la clé d'OpenAI (défaut OPENAI_API_KEY ; "
+                            "v9-v6 : commence par OPENAI_API_KEY)")
         s.add_argument("--sortie", required=True)
         s.add_argument("--plafond-usd", type=float, default=PLAFOND_DEFAUT_USD)
         s.add_argument("--accepter-absence", action="append", default=[])
```

### 7.2 Consultation : v5 (`4c44b89e…`) vers v6 (`e2095843…`), différentiel unifié complet

```diff
--- appel_modeles_externes_v5.py
+++ appel_modeles_externes_v6.py
@@ -1,4 +1,11 @@
-"""Version 5 (21 novembre, GO-2026-11-21-57) de l'appel aux modèles externes : Neon, et clé d'OpenAI nommée.
+"""Version 6 (21 novembre) de l'appel aux modèles externes : nom de la clé d'OpenAI restreint à OPENAI_API_KEY….
+Remplace le v5 (4c44b89e…, gardé sans modification, R12). Un seul changement, décidé par la mère après la contre-lecture
+contre-lecture-collisionneur-v9-v5-v1.md (77041a13…, remarque 1) : --cle-openai n'accepte qu'un nom qui commence par
+OPENAI_API_KEY (par exemple OPENAI_API_KEY_2) ; tout autre nom (GEMINI_API_KEY, par exemple) est refusé sans être répété,
+pour qu'une clé ne parte jamais vers un autre fournisseur que le sien. Essais : essais_appel_modeles_externes_v6.py.
+
+Ce qui suit est l'en-tête du v5, inchangé.
+Version 5 (21 novembre, GO-2026-11-21-57) de l'appel aux modèles externes : Neon, et clé d'OpenAI nommée.
 Remplace le v4 (b31fecf2…, gardé sans modification, R12). Changements, et seulement ceux-là :
 - espèce Neon (gemini-4-neon, flux continu Gemini, clé GEMINI_API_KEY par son nom) : prix 3 / 15 USD par million (palier
   « Standard » de la page publique de Google lue le 21 novembre 2026 à 13:49Z, versée :
@@ -30,7 +37,7 @@
 - aucun renvoi silencieux : tout échec est écrit dans le JSON et rend un code non nul (1 échec ou refus, 3 réponse
   tronquée ou incomplète — texte partiel écrit à part, en `.partiel.md`, jamais sous le nom de la réponse) ;
 - essais hors réseau : `essais_appel_modeles_externes_v4.py` (transport simulé).
-Usage (v5) : python -I appel_modeles_externes_v5.py {argon|astra|carbon|neon} ENONCE SORTIE_MD SORTIE_JSON
+Usage (v6) : python -I appel_modeles_externes_v6.py {argon|astra|carbon|neon} ENONCE SORTIE_MD SORTIE_JSON
         [--reflexion N] [--texte N] [--efforts xhigh,high] [--plafond-usd X] [--cle-openai NOM]
 Clés lues par leur nom seulement (celle d'OpenAI dans la variable nommée par --cle-openai, défaut OPENAI_API_KEY ;
 GEMINI_API_KEY) ; jamais affichées ni écrites.
@@ -55,6 +62,7 @@
 ESPECES_GEMINI = ("carbon", "argon", "neon")  # v5 : espèces servies par le flux Gemini, sous le plancher de texte
 REGLE_PLAFOND_LARGE = ("carbon", "neon")  # v5 : règle de CLAUDE.md (GO-2026-11-21-47), étendue à Neon (GO-2026-11-21-57)
 MOTIF_NOM_VARIABLE = re.compile(r"^[A-Z_][A-Z0-9_]{0,99}$")  # v5 : --cle-openai, comme le collisionneur
+PREFIXE_CLE_OPENAI = "OPENAI_API_KEY"  # v6 : tout nom donné à --cle-openai commence par ce préfixe
 URL_OPENAI = "https://api.openai.com/v1/responses"
 URL_GEMINI = "https://generativelanguage.googleapis.com/v1beta/models/{}:streamGenerateContent?alt=sse"
 RELEVE_S = 20
@@ -282,6 +290,9 @@
         print("ARRET : --cle-openai : nom de variable d'environnement mal formé (lettres majuscules, chiffres, « _ »)",
               file=sys.stderr)
         return CODE_ECHEC
+    if not nom_cle_openai.startswith(PREFIXE_CLE_OPENAI):  # v6 : une clé ne part jamais vers un autre fournisseur
+        print(f"ARRET : --cle-openai : le nom doit commencer par {PREFIXE_CLE_OPENAI}", file=sys.stderr)
+        return CODE_ECHEC
     for chemin in (sortie_md, sortie_json, sortie_md + ".partiel.md"):
         if os.path.exists(chemin):
             print(f"ARRET : {chemin} existe déjà (on n'écrase jamais, R12)", file=sys.stderr)
@@ -309,7 +320,7 @@
         res = appeler_gemini(enonce, cle, reglage, journal, espece, transport_flux)
     code, motif = verdict(espece, res)
     pe, ps = PRIX[espece]
-    meta = {"version_script": "v5", "espece": espece, "modele_demande": MODELE[espece], "variable_cle": nom_cle,
+    meta = {"version_script": "v6", "espece": espece, "modele_demande": MODELE[espece], "variable_cle": nom_cle,
             "modele_servi": res["modele_servi"], "id_reponse": res["id_reponse"], "fin": res["statut"],
             "verdict": "ok" if code == CODE_OK else ("tronque" if code == CODE_TRONQUE else "echec"),
             "motif": motif, "erreur_fournisseur": res["erreur_fournisseur"],
@@ -349,7 +360,8 @@
     p.add_argument("--efforts", default=None, help="Astra : efforts essayés dans l'ordre sur refus 400, ex. xhigh,high")
     p.add_argument("--plafond-usd", type=float, default=PLAFOND_APPEL_USD)
     p.add_argument("--cle-openai", default=CLE["astra"],  # v5
-                   help="NOM de la variable d'environnement qui porte la clé d'OpenAI (défaut OPENAI_API_KEY)")
+                   help="NOM de la variable d'environnement qui porte la clé d'OpenAI (défaut OPENAI_API_KEY ; v6 : "
+                        "commence par OPENAI_API_KEY)")
     a = p.parse_args(argv)
     efforts = tuple(x.strip() for x in a.efforts.split(",") if x.strip()) if a.efforts else None
     return executer(a.espece, a.enonce, a.sortie_md, a.sortie_json, a.reflexion, a.texte, efforts, a.plafond_usd,
```

### 7.3 Essais du collisionneur : v9-v5 (`624b5229…`) vers v9-v6 (`cd4c1337…`), différentiel unifié complet

```diff
--- test_collisionneur_v9_v5.py
+++ test_collisionneur_v9_v6.py
@@ -1,4 +1,8 @@
-"""Essais du collisionneur v9-v5 (GO-2026-11-21-57). Partie reprise : les essais v9-v3 (8c38dc2f…) et leur complément 1
+"""Essais du collisionneur v9-v6 : copie des essais v9-v5 (624b5229…), rejoués sur le v9-v6, adaptés là où le v9-v6 change
+(provision de Carbon à 49 152, marqués « v9-v6 »), plus la section v9-v6 en fin de fichier (CO-1 à CO-3 de la contre-lecture
+du v9-v5, préfixe de --cle-openai, réglages de Carbon). En-tête des essais v9-v5, inchangé :
+
+Essais du collisionneur v9-v5 (GO-2026-11-21-57). Partie reprise : les essais v9-v3 (8c38dc2f…) et leur complément 1
 (58ddaa24…), rejoués sur le v9-v5, avec trois écarts seulement : (1) le chemin du script (collisionneur_v9_v5.py) et le nom
 du module chargé ; (2) l'essai qui lisait le run réel sous runs/ ne lit plus qu'une copie désignée par COPIE_RUN_DOPAMINE
 (absente : essai sauté), comme dans les essais v9-v4 ; (3) test_identifiants_et_table_des_prix attend Neon (écart voulu).
@@ -6,7 +10,7 @@
 transport des comptages, horloge et sommeil remplacés par des doublures ; toute ouverture de connexion lève une erreur.
 Chaque garde a un cas sain et un artefact (R5) ; chaque motif de la garde de motifs a son témoin positif.
 
-Lancement : PYTHONPATH=src .venv/bin/python -B -m pytest -q docs/notes/collisionneur-v9/test_collisionneur_v9_v5.py
+Lancement : PYTHONPATH=src .venv/bin/python -B -m pytest -q docs/notes/collisionneur-v9/test_collisionneur_v9_v6.py
 """
 import importlib.util
 import io
@@ -18,14 +22,14 @@
 
 import pytest
 
-CHEMIN = Path(__file__).with_name("collisionneur_v9_v5.py")
+CHEMIN = Path(__file__).with_name("collisionneur_v9_v6.py")
 CLE_GEMINI, CLE_OPENAI, CLE_ANTHROPIC = "cle-gemini-secrete-123", "cle-openai-secrete-456", "cle-anthropic-secrete-789"
 SAIN = "mot " * 1000  # 4 000 caractères, aucun motif
 TEXTE_JEV = "mot " * 1000  # v9-v2 (C3, point 4) : pire cas de Jev non nul
 
 
 def charger():
-    spec = importlib.util.spec_from_file_location("collisionneur_v9_v5_essai", CHEMIN)
+    spec = importlib.util.spec_from_file_location("collisionneur_v9_v6_essai", CHEMIN)
     module = importlib.util.module_from_spec(spec)
     spec.loader.exec_module(module)
     return module
@@ -274,15 +278,15 @@
 # ---------- 2a. budget et provision de réflexion ----------
 
 def test_garde_a_sain_budget_pose_et_reflexion_dans_la_provision(c, tmp_path):
-    t = FauxTransport(flux_gemini(pensees=32768))
+    t = FauxTransport(flux_gemini(pensees=49152))  # v9-v6 : provision de Carbon 49 152 (v9-v5 : 32 768)
     c.TRANSPORT = t
     assert executer(c, tmp_path, "carbon") == "OK"
     corps = t.appels[0]["corps"]
-    assert corps["generationConfig"]["thinkingConfig"] == {"thinkingBudget": 32768, "includeThoughts": True}
+    assert corps["generationConfig"]["thinkingConfig"] == {"thinkingBudget": 49152, "includeThoughts": True}
     assert corps["generationConfig"]["maxOutputTokens"] == 65536
     assert t.appels[0]["url"].endswith("gemini-4-carbon:streamGenerateContent?alt=sse")
     e = journal(c, tmp_path)[-1]
-    assert e["statut"] == "OK" and e["cout_usd"] == round(500 * 4 / 1e6 + (50 + 32768) * 20 / 1e6, 4)
+    assert e["statut"] == "OK" and e["cout_usd"] == round(500 * 4 / 1e6 + (50 + 49152) * 20 / 1e6, 4)  # v9-v6
 
 
 def test_garde_a_artefact_reflexion_au_dela_de_la_provision(c, tmp_path):
@@ -299,7 +303,7 @@
 def test_garde_a_provision_comptee_avant_l_envoi(c, tmp_path):
     c.fixer_composition(["carbon", "kimi"])
     m = c.MODELES["B"]
-    assert c.cout_pire_cas(m, 0, 65536) == pytest.approx((65536 + 32768) * 20 / 1e6)
+    assert c.cout_pire_cas(m, 0, 65536) == pytest.approx((65536 + 49152) * 20 / 1e6)  # v9-v6
     pire = c.cout_pire_cas(m, len(SAIN), 65536)
     c.TRANSPORT = FauxTransport()  # artefact : plafond juste sous le pire cas, provision comprise → aucun envoi
     with pytest.raises(c.Arret) as e:
@@ -1238,10 +1242,11 @@
     assert c.CATALOGUE["neon"] == {"id": "gemini-4-neon", "fournisseur": "gemini", "prix": (3.0, 15.0), "max": 65536,
                                    "max_relance": 65536, "provision": 32768, "car_par_jeton": 2.5, "delai_s": 5400}
     assert set(c.CATALOGUE) == set(v3.CATALOGUE) | {"neon"}
-    for espece in v3.CATALOGUE:  # aucune autre espèce ne change
-        assert c.CATALOGUE[espece] == v3.CATALOGUE[espece]
+    for espece in v3.CATALOGUE:  # aucune autre espèce ne change ; v9-v6 : sauf la provision de Carbon (section v9-v6)
+        attendu = dict(v3.CATALOGUE[espece], provision=49152) if espece == "carbon" else v3.CATALOGUE[espece]
+        assert c.CATALOGUE[espece] == attendu
     assert c.ORDRE_CATALOGUE == v3.ORDRE_CATALOGUE + ("neon",)  # Neon en fin d'ordre
-    assert c.NOMS_CLES == v3.NOMS_CLES and c.VERSION == "collisionneur-v9-v5"
+    assert c.NOMS_CLES == v3.NOMS_CLES and c.VERSION == "collisionneur-v9-v6"  # v9-v6
     for nom in ("TOLERANCE_COMPTE", "CAR_PAR_JETON_MAX", "ATTENTES_429", "PLAFOND_DEFAUT_USD", "RATIO_PROJECTION_ENTREE",
                 "CAR_SORTIE_MAX", "MAX_FABLE_V3", "CODE_GARDE", "CODE_COMPTE", "STATUTS_GARDE", "REFUS_GEMINI"):
         assert getattr(c, nom) == getattr(v3, nom), nom
@@ -1541,3 +1546,130 @@
     c.fixer_composition(["astra", "neon"], nom_cle_openai="OPENAI_API_KEY_2")
     c.sceller_composition(tmp_path)  # même composition : aucun arrêt
     assert "OPENAI_API_KEY" not in (tmp_path / "especes.json").read_text(encoding="utf-8")
+
+
+# ======================================================================================================================
+# v9-v6 : corrections de la contre-lecture du v9-v5 (contre-lecture-collisionneur-v9-v5-v1.md, 77041a13…), au code exact
+# qu'elle donne (CO-1, CO-2, CO-3), puis les décisions de la mère : préfixe de --cle-openai, réglages de Carbon du v9-v4.
+# ======================================================================================================================
+
+def _vide_max(modele):
+    return flux_gemini(texte="", modele=modele, fin="MAX_TOKENS", candidats=0, pensees=32768)
+
+
+# ---------- CO-1 : un défaut de réglage n'est jamais renvoyé au même réglage ----------
+
+def test_v6_defaut_de_reglage_jamais_renvoye_au_meme_reglage(c, tmp_path, monkeypatch, capsys):
+    faits = tmp_path / "faits.md"
+    faits.write_text("Fait 1 (HYPOTHÈSE) : texte sain.\n", encoding="utf-8")
+    sortie = tmp_path / "run"
+    argv = ["etage1", "--carbon", "--neon", "--faits", str(faits), "--sortie", str(sortie)]
+    c.TRANSPORT = FauxTransport(_vide_max("gemini-4-carbon"))
+    assert c.principal(argv) == c.CODE_REGLAGE  # premier lancement : arrêt au code 9, un envoi
+    # Artefact : la même commande ne renvoie rien à Carbon ; Neon part ; porte fermée après le tour.
+    c.TRANSPORT = FauxTransport(flux_gemini(modele="gemini-4-neon"))
+    assert c.principal(argv) == c.CODE_PORTE
+    assert [a["url"].split("/")[-1].split(":")[0] for a in c.TRANSPORT.appels] == ["gemini-4-neon"]
+    assert [e["statut"] for e in c.essais_journal(sortie, "E1-T1-meta-A")] == ["MAX_TOKENS_SANS_TEXTE"]
+    assert "non renvoyée" in capsys.readouterr().out
+    # Sain 1 : l'absence acceptée par l'arbitre laisse l'étage finir, sans envoi à Carbon au tour 1.
+    c.TRANSPORT = FauxTransport(flux_gemini(modele="gemini-4-carbon"), flux_gemini(modele="gemini-4-neon"))
+    assert c.principal(argv + ["--accepter-absence", "E1-T1-meta-A"]) == c.CODE_FINI
+    assert [e["statut"] for e in c.essais_journal(sortie, "E1-T1-meta-A")] == ["MAX_TOKENS_SANS_TEXTE"]
+
+
+def test_v6_defaut_de_reglage_renvoye_si_le_reglage_a_change(c, tmp_path, monkeypatch):
+    """Sain 2 : sous un réglage différent, la cellule repart."""
+    c.TRANSPORT = FauxTransport(_vide_max("gemini-4-carbon"))
+    with pytest.raises(c.Arret) as e:
+        executer(c, tmp_path, "carbon")
+    assert e.value.code == c.CODE_REGLAGE
+    l = lettre_de(c, "carbon")
+    cid = c.id_cellule("E1-T1", l)
+    assert c.reglage_en_defaut(tmp_path, cid, c.MODELES[l]) is True
+    assert c.reglage_en_defaut(tmp_path, cid, dict(c.MODELES[l], provision=24576)) is False
+    assert c.reglage_en_defaut(tmp_path, cid, dict(c.MODELES[l], max_relance=131072)) is False
+    assert c.reglage_en_defaut(tmp_path, c.id_cellule("E1-T2", l), c.MODELES[l]) is False  # cellule jamais lancée
+
+
+# ---------- CO-2 : aucun repli sur la clé par défaut, même sans nom dans la composition ----------
+
+def test_v6_cle_openai_sans_nom_dans_la_composition_aucun_repli(c):
+    c.fixer_composition(["astra", "kimi"], nom_cle_openai="OPENAI_API_KEY_2")
+    m = dict(c.MODELES[lettre_de(c, "astra")], nom_cle=None)  # OPENAI_API_KEY est présente : elle n'est pas lue
+    c.TRANSPORT = FauxTransport()
+    rep = c.appeler_openai(m, SAIN, 100)
+    assert rep.echec and "absent de la composition" in rep.echec and c.TRANSPORT.appels == []
+    with pytest.raises(c.RefusCompte) as e:
+        c.compter_openai(m, SAIN)
+    assert e.value.motif == "COMPTE_IMPOSSIBLE" and c.TRANSPORT_COMPTE.appels == []
+
+
+# ---------- CO-3 : une sortie vide dont la fin est « STOP » n'est pas le défaut de réglage ----------
+
+@pytest.mark.parametrize("espece", ["carbon", "neon"])
+def test_v6_sortie_vide_fin_stop_relancee_comme_la_v3(c, tmp_path, espece):
+    modele = c.CATALOGUE[espece]["id"]
+    c.TRANSPORT = FauxTransport(flux_gemini(texte="", modele=modele, fin="STOP", candidats=0, pensees=100),
+                                flux_gemini(modele=modele))
+    assert executer(c, tmp_path, espece) == "OK"
+    assert [e["statut"] for e in journal(c, tmp_path)] == ["VIDE", "OK"] and len(c.TRANSPORT.appels) == 2
+
+
+# ---------- décision de la mère : --cle-openai commence par OPENAI_API_KEY ----------
+
+@pytest.mark.parametrize("nom", ["GEMINI_API_KEY", "TYPESAFE_API_KEY", "MA_CLE", "CLE_OPENAI_API_KEY", "OPENAI_KEY"])
+def test_v6_cle_openai_hors_prefixe_refusee(c, tmp_path, capsys, monkeypatch, nom):
+    """Artefact : la clé d'un autre fournisseur (présente dans l'environnement) ne part jamais vers OpenAI ; refus au code 1,
+    avant toute écriture et tout appel, à la composition comme par la ligne de commande."""
+    monkeypatch.setenv("OPENAI_KEY", "cle-quelconque-0000")
+    monkeypatch.setenv("CLE_OPENAI_API_KEY", "cle-quelconque-0001")
+    with pytest.raises(c.Arret) as e:
+        c.fixer_composition(["astra", "kimi"], nom_cle_anthropic="MA_CLE", nom_cle_openai=nom)
+    assert e.value.code == c.CODE_USAGE and "OPENAI_API_KEY" in str(e.value) and c.LETTRES == ()
+    faits = tmp_path / "faits.md"
+    faits.write_text("Fait sain.\n", encoding="utf-8")
+    sortie = tmp_path / "run"
+    c.TRANSPORT = FauxTransport()
+    assert c.principal(["etage1", "--astra", "--kimi", "--cle-openai", nom, "--faits", str(faits), "--sortie",
+                        str(sortie)]) == c.CODE_USAGE
+    err = capsys.readouterr().err
+    assert CLE_GEMINI not in err and CLE_ANTHROPIC not in err and "doit commencer par OPENAI_API_KEY" in err
+    assert nom not in err  # le nom refusé n'est pas répété
+    assert not sortie.exists() and c.TRANSPORT.appels == [] and c.TRANSPORT_COMPTE.appels == []
+
+
+@pytest.mark.parametrize("nom", ["OPENAI_API_KEY", "OPENAI_API_KEY_2", "OPENAI_API_KEY2"])
+def test_v6_cle_openai_prefixe_accepte(c, nom):
+    c.fixer_composition(["astra", "kimi"], nom_cle_openai=nom)
+    assert c.MODELES[lettre_de(c, "astra")]["nom_cle"] == nom and c.PREFIXE_CLE_OPENAI == "OPENAI_API_KEY"
+
+
+# ---------- décision de la mère : réglages de Carbon du v9-v4 ----------
+
+def test_v6_carbon_reprend_les_reglages_du_v4_et_tient_la_regle(c):
+    spec = importlib.util.spec_from_file_location("collisionneur_v9_v4_reference", CHEMIN.with_name("collisionneur_v9_v4.py"))
+    v4 = importlib.util.module_from_spec(spec)
+    spec.loader.exec_module(v4)
+    assert c.CATALOGUE["carbon"] == v4.CATALOGUE["carbon"]  # même ligne que le v9-v4
+    assert (c.CATALOGUE["carbon"]["max"], c.CATALOGUE["carbon"]["max_relance"], c.CATALOGUE["carbon"]["provision"]) \
+        == (65536, 65536, 49152)
+    assert c.CATALOGUE["argon"] == charger_v3().CATALOGUE["argon"]  # Argon garde les réglages du v9-v3
+    c.fixer_composition(["carbon", "kimi"])
+    m = c.MODELES[lettre_de(c, "carbon")]
+    for plafond in (m["max"], m["max_relance"]):
+        assert c.ecart_regle_texte(m, plafond) is None and plafond - m["provision"] == 16384
+
+
+def test_v6_carbon_reponse_du_20_novembre_gardee_et_artefact_au_dela(c, tmp_path):
+    """Sain : la critique de Carbon du 20 novembre (39 953 jetons de pensées, arrêtée sous 32 768) est gardée sous 49 152 ;
+    budget envoyé 49 152. Artefact : 49 153 jetons de pensées → garde de réflexion, code 6, un seul envoi."""
+    t = FauxTransport(flux_gemini(entree=27122, pensees=39953, candidats=10298))
+    c.TRANSPORT = t
+    assert executer(c, tmp_path / "sain", "carbon", prompt="mot " * 20000) == "OK"
+    assert t.appels[0]["corps"]["generationConfig"]["thinkingConfig"]["thinkingBudget"] == 49152
+    c.TRANSPORT = FauxTransport(flux_gemini(pensees=49153))
+    with pytest.raises(c.Arret) as e:
+        executer(c, tmp_path / "artefact", "carbon")
+    assert e.value.code == c.CODE_GARDE and len(c.TRANSPORT.appels) == 1
+    assert c.essais_journal(tmp_path / "artefact")[-1]["statut"] == "REFLEXION_HORS_PROVISION"
```
