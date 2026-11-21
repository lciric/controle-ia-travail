# Contre-lecture de l'outil de relecture d'une correction par Fable 5.2 appelé par l'interface d'Anthropic, v1

Contre-lecteur neuf : Claude Opus 5.5 (n'a rien écrit de la pièce), 21 novembre 2026. Pièce d'instrument, classe B
(GO-2026-11-21-84). Aucun appel réel fait ; aucun fichier de la pièce modifié ; mutations et corrections essayées dans une
copie du bloc-notes de la session.

## Verdict : **à corriger**

L'outil est sain sur l'essentiel (garde avant tout envoi, clé jamais écrite, aucun défaut rendu comme une relecture,
réflexion jamais écrite, réglages de l'appel conformes à la compétence « claude-api »). Sept corrections sont demandées
(C1 à C7) : la borne de repli du comptage (C1, celle de la réserve 1), un trou d'essai sur les raisons d'arrêt (C2), un
compagnon `.sha256` qui peut être écrasé (C3), l'ordre « journal avant sortie » non essayé (C4), trois variantes
d'identifiant de session et un terme de chemin qui passent la garde (C5), une interruption pendant l'envoi qui sort sans
ligne au journal (C6), un repli silencieux au journal de refus (C7). Toutes ont été appliquées dans une copie : 76 essais
passés (59 anciens gardés, un remplacé par deux, et 17 neufs en tout) ; chaque mutation correspondante est tuée.

## Pièces vérifiées

| Pièce | Empreinte (vérifiée par son compagnon, `sha256sum -c`) |
|---|---|
| `src/controle_ia/relecture_fable_api_v1.py` | `056bc4ef1f7deb75cacc867701170a87226c316b727dd5b84f09401e1c6f5798` — OK |
| `tests/test_relecture_fable_api_v1.py` | `a3f649cf…` — OK |
| `docs/notes/relecture-fable-api-v1/rapport-developpeur-v1.md` | `be900d1c…` — OK |
| `docs/notes/relecture-fable-api-v1/journal-depense-fumee-v1.jsonl` | OK |
| `fumee-v1/consigne-fumee-v1.md`, `piece-fumee-v1.md`, `remarques-fumee-v1.md` | OK, OK, OK |
| `fumee-v1/sortie/relecture-fable-api.md` (`eb3535b7…`), `compteurs.json` | OK, OK |

Le journal de fumée porte l'empreinte du module `056bc4ef…` (égale à celle du fichier contre-lu) ; modèle demandé et
servi `claude-fable-5-2`, `end_turn`, entrée comptée 273 = facturée 273, sortie 45 dont réflexion 41, coût
(273 × 8 + 45 × 40) / 10⁶ = 0,003984 USD, pire d'avant l'envoi (308 × 8 + 2 200 × 40) / 10⁶ = 0,090464 USD ≤ 0,10 : les
chiffres du rapport (§ 5) se recalculent.

Essais rejoués : `PYTHONPATH=src .venv/bin/python -m pytest -q tests/test_relecture_fable_api_v1.py -p no:cacheprovider
--basetemp=<dossier neuf>` : **60 passés** (kit `anthropic` 2.12.0).

## Jugement de l'appel (compétence « claude-api » chargée ce jour)

- Identifiant `claude-fable-5-2` : exact (table « Current Models », sans suffixe de date). Tarif 8 / 40 USD par million,
  lecture de cache 0,20 : conforme à la table et à `shared/models.md` (qui porte aussi l'écriture de cache d'une heure à
  16 USD, soit 2 × 8 : `FACTEUR_ECRITURE_CACHE = 2.0` est la borne haute, juste). Aucun supplément de long contexte n'est
  porté pour ce modèle. Le tarif vient de la table mise en cache le 2026-11-03, non de la page de prix en ligne : à dire
  si un chiffre de coût entre dans une pièce opposable.
- Flux : `client.messages.stream(**params)` puis `get_final_message()` : forme documentée ; nécessaire à 128 000 jetons.
- Réflexion : `{type: "adaptive", display: "omitted"}` — seul réglage admis avec l'omission ; ni `budget_tokens`
  (refusé, 400) ni `disabled` ; aucun paramètre d'échantillonnage (refusé depuis la version 2026-10-21) : juste.
- Effort : `output_config.effort = "max"`, dans `output_config` et non au premier niveau : juste. La compétence conseille
  de partir de `high` sur Fable 5.2 et réserve `max` au plafond du modèle ; `max` reste un choix de la mère, à garder en
  sachant qu'il pousse la réflexion vers le plafond de 128 000 (défaut `max_tokens` facturé jusqu'à ≈ 5,12 USD).
- Comptage : `messages.count_tokens` avec le même modèle, le même message, la même réflexion et le même effort : juste ;
  `input_tokens` contrôlé (entier strictement positif).
- Raisons d'arrêt : `end_turn` seule admise ; `max_tokens`, `refusal` (catégorie lue dans `stop_details.category`), toute
  autre raison = défaut : juste (mais la dernière branche n'était pas essayée, C2).
- Repli serveur `fallbacks` : absent, contre le défaut de la compétence, à dessein — juste : une relecture servie par un
  autre modèle ne serait pas celle de Fable ; le modèle servi est de plus comparé à celui demandé.
- Client : clé explicite (`api_key=`), donc, d'après le kit 2.12.0 (`_client.py`, « explicit ctor args are total »),
  aucune variable d'identité ni profil n'est lu ; `max_retries=0` (essai : une seule requête après un 500) ;
  `base_url` explicite (la variable `ANTHROPIC_BASE_URL` est ignorée).

## Jugement point par point

**(1) Aucun envoi sans la garde vide — tenu, avec trois trous de variantes (C5).** La garde porte sur l'invite exacte
(consigne, balises avec chemins et empreintes, pièces), avant le comptage, qui envoie lui aussi l'invite : l'ordre est
juste. Les lignes ne peuvent pas chevaucher deux segments (chaque segment finit par un saut de ligne) et le contrôle de
l'invite jointe double la garde. Sondes faites sur `garde_motifs_ligne` : passent aujourd'hui `SESSION_01Qi7…`,
`Session_01Qi7…`, `session-01Qi7…`, un identifiant de session au format UUID (celui du bloc-notes de cette session),
`La​zar` (espace sans chasse), `conception-ii-b1-v1.md`, `conception (ii-b)`. C5 les refuse. Restent refusés à tort
(prudence, sans fuite) : `compte-rendu` avec trait d'union, fréquent en français et dans les noms de fichiers du dépôt,
et « Lazarus » ; la mère doit s'attendre à fournir des copies nettoyées. La lecture « verite / rendu / scores dans un
chemin ou un nom » (réserve 4) me paraît la bonne : refuser ces mots partout rendrait l'outil inutilisable.

**(2) La clé n'est jamais affichée ni écrite — tenu.** Lue par son nom, jamais dans la ligne, les compteurs, l'en-tête ni
les paramètres journalisés ; tout message d'erreur passe par `masquer` (deux fois sur le chemin d'erreur d'envoi) ; essai
sain : le secret n'est dans aucun fichier écrit ni sur la sortie. Le journal de débogage du kit (`ANTHROPIC_LOG=debug`)
n'écrit que les en-têtes propres à la requête, pas l'en-tête d'autorisation (vu dans `_base_client.py`).

**(3) Le plafond de ligne — tenu sauf deux cas (C1, C6).** Erreur au milieu du flux, 5xx, 529, délai dépassé, exception
imprévue de l'envoi, usage absent : comptés au pire, essais à l'appui ; 4xx et connexion impossible avant l'ouverture :
zéro, juste. Deux cas cassent la borne :
- comptage échoué : la borne de 2,5 caractères par jeton sous-compte (1,76 mesuré à la fumée : 480 caractères, 273
  jetons) ; de plus une exception autre que celles du kit au comptage sort sans ligne au journal. **Correction C1
  (recommandée par la mère, retenue) : refus de l'envoi si le comptage échoue, pour quelque raison que ce soit**, code 10,
  ligne `refus_avant_envoi` à coût nul ; la constante et la fonction de borne sont retirées ;
- interruption (Ctrl-C, SIGTERM) pendant le flux : l'envoi est parti et facturé, mais aucune ligne n'est écrite, donc
  le cumul suivant l'ignore. **C6** : la consigner au pire avant de sortir. Reste hors d'atteinte (à déclarer) : SIGKILL
  ou coupure de la machine ; seule une ligne de réservation écrite avant l'envoi les couvrirait (v2, si la mère le veut).
L'entrée facturée peut dépasser la garde ⌈n × 1,01⌉ + 32 (marqué `entree_au_dela_de_la_garde`, non essayé) : écart
négligeable devant la sortie, la borne n'est donc pas une preuve stricte, à savoir. Deux commandes lancées en même temps
sur le même journal peuvent passer toutes deux : lancer une commande à la fois.

**(4) Aucun défaut rendu comme une relecture — tenu.** Erreur, usage absent, `max_tokens`, `refusal`, autre raison,
modèle servi autre, texte vide (y compris blancs seuls) : chaque cas écrit `compteurs.json` en « defaut » et, s'il y a du
texte, le fichier « PAS-UNE-RELECTURE », jamais `relecture-fable-api.md`. Trou d'essai : aucune raison d'arrêt autre que
`end_turn`, `max_tokens` et `refusal` n'était essayée (mutation M2 survivante) : **C2**.

**(5) Rien n'est écrasé, journal avant toute sortie, réflexion jamais écrite — un écart (C3), un trou d'essai (C4).**
Les sorties s'ouvrent en mode « x » ; mais `sceller` ouvre le compagnon en « w » et le contrôle préalable ne regarde pas
les compagnons : un `relecture-fable-api.md.sha256` ou `compteurs.json.sha256` orphelin dans DOSSIER serait écrasé
après un envoi payé. **C3**. L'ordre « journal puis sortie » est juste dans le code (chemins sain et défaut) mais aucun
essai ne le tenait (mutation M3 survivante) : **C4**. La réflexion n'est ni demandée (`omitted`) ni lue (seuls les blocs
`text` sont joints) ; seul le nombre de jetons de réflexion est écrit : juste. Le refus avant envoi qui ne peut écrire
son journal se tait (`except OSError: pass`) : repli silencieux contraire à R5, **C7**.

**(6) Essais — 60 passés ; chaque garde a son cas sain et son artefact, sauf les trous dits en (4) et (5).** Mutations
écrites dans une copie (jamais dans le fichier), essais copiés à côté pour que la configuration du dépôt
(`pythonpath = ["src", "tests"]` dans `pyproject.toml`) ne réimporte pas l'original ; témoin sans mutation : 60 passés.

| Mutation sur la v1 | Résultat | Essai qui la tue |
|---|---|---|
| M1 : « ciric » retiré des noms interdits | tuée | `test_garde_refuse_chaque_motif[M. Ciric a dit]`, `[M. Ćirić a dit]` |
| M2 : branche « autre raison d'arrêt » supprimée | **survit** | aucun (C2) |
| M3 : journal écrit après la relecture | **survit** | aucun (C4) |
| M4 : `max_retries=2` | tuée | `test_chemin_reel_erreur_serveur_sans_relance_comptee_au_pire` |
| M5 : 5xx et erreur de flux comptés zéro | tuée | `…erreur_serveur…`, `…erreur_dans_le_flux…` |
| M6 : réflexion `display: "summarized"` | tuée | `test_cas_sain` |

Après les corrections (copie corrigée, 76 passés ; témoin sans mutation : 76 passés) :

| Mutation sur la copie corrigée | Résultat | Essai qui la tue |
|---|---|---|
| M2 (même) | tuée | `test_autre_raison_arret_est_un_defaut[stop_sequence|pause_turn|tool_use|None]` |
| M3 (même) | tuée | `test_journal_ecrit_avant_toute_sortie` |
| M8 : borne de repli remise au comptage | tuée | `test_comptage_impossible_refuse_sans_envoi[…]`, `test_chemin_reel_comptage_500_refuse_sans_envoi` |
| M9 : compagnons non contrôlés avant l'envoi | tuée | `test_compagnon_orphelin_jamais_ecrase[…]` |
| M10 : identifiant UUID non cherché | tuée | `test_garde_refuse_chaque_motif[dossier 2eb82089-…]` |
| M11 : interruption non consignée | tuée | `test_interruption_pendant_envoi_comptee_au_pire`, `test_sigterm_pendant_envoi_compte_au_pire` |

(Pendant les passes de M9 à M11, le disque de la machine était à quelques mégaoctets libres : des erreurs de
préparation d'essais s'y ajoutent ; les essais nommés ci-dessus échouent sur leur assertion, et le témoin passe.)

## Corrections — texte de remplacement exact

Le texte exact est donné en différence unifiée contre les fichiers contre-lus (`056bc4ef…` et `a3f649cf…`) : les lignes
« - » sont remplacées par les lignes « + », mot pour mot. Une fois appliquées, le module a l'empreinte
`acf9ddd25cdc916f6c74b05d7f2f5462c64102da6b746fd54deaa1d92e3e927c` et les essais
`efa04f0000819010a2294dbcca5caab59a9cb240696762653cbb8aa9a15cc46a` (copie vérifiée : 76 passés). Nouvelle version =
nouveau nom (R12) : l'appliquer en `relecture_fable_api_v2.py` et `test_relecture_fable_api_v2.py` (`VERSION` et
l'importation des essais renommés en conséquence), la v1 gardée.

Correspondance des blocs :
- **C1** (comptage échoué = refus) : docstring point 6 ; `CODE_COMPTAGE = 10` ; retrait de `CAR_PAR_JETON_BORNE` et de
  `borne_entree` ; bloc `try: compte = compter(params)` ; essais `test_comptage_impossible_refuse_sans_envoi` (remplace
  `test_comptage_impossible_borne_declaree`) et `test_chemin_reel_comptage_500_refuse_sans_envoi` ;
- **C2** : essai `test_autre_raison_arret_est_un_defaut` ;
- **C3** (compagnons) : docstring point 4 ; `sceller` en mode « x » ; contrôle préalable des six noms par `lexists` ;
  essai `test_compagnon_orphelin_jamais_ecrase` ;
- **C4** : essai `test_journal_ecrit_avant_toute_sortie` ;
- **C5** (garde) : `MOTIF_SESSION` sans casse, « _ » ou « - » ; `MOTIF_UUID` ; retrait des caractères invisibles
  (catégorie Unicode Cf) en tête de `garde_motifs_ligne` ; `conception-ii-b` sans la garde arrière et avec « . », « ( »,
  « ) » comme séparateurs ; cinq artefacts de plus dans `ARTEFACTS` ;
- **C6** (interruption) : `import signal`, `import threading`, `_sigterm_en_interruption`, bloc de l'envoi avec
  `except BaseException` et `finally` ; essais `test_interruption_pendant_envoi_comptee_au_pire` et
  `test_sigterm_pendant_envoi_compte_au_pire` ;
- **C7** : avertissement au lieu de `pass` dans `refuser`.

Rapport du développeur, § 6, réserve 1 — texte de remplacement : « 1. **Comptage échoué : refus.** L'appel de fumée a
donné 1,76 caractère par jeton (480 caractères, 273 jetons) ; la borne de repli de 2,5 de la v1 sous-comptait l'entrée.
La v2 refuse l'envoi si le comptage échoue, pour quelque raison que ce soit (code 10, ligne `refus_avant_envoi` à coût
nul) ; il n'y a plus de borne de repli. » Et § 2, point 6 : remplacer « si le comptage échoue autrement que par une clé
refusée : borne déclarée de 1 jeton pour 2,5 caractères (avertissement, et source au journal) ; » par « si le comptage
échoue, pour quelque raison que ce soit : refus (code 10), rien n'est envoyé ; ».

### Module

```diff
--- a/src/controle_ia/relecture_fable_api_v1.py
+++ b/src/controle_ia/relecture_fable_api_v1.py
@@ -18,12 +18,14 @@
  3. garde de motifs sur l'invite entière, telle qu'elle partirait : elle doit être vide avant tout envoi (voir
     `garde_motifs`) ; l'outil ne nettoie jamais : une pièce qui cite un motif interdit doit être remplacée par une copie
     nettoyée que l'appelant fournit ;
- 4. refuse si DOSSIER/relecture-fable-api.md ou DOSSIER/compteurs.json existe déjà (on n'écrase jamais, R12) ;
+ 4. refuse si DOSSIER/relecture-fable-api.md, DOSSIER/compteurs.json, le fichier de texte partiel ou l'un de leurs
+    compagnons .sha256 existe déjà (on n'écrase jamais, R12) ;
  5. lit la clé dans la variable dont le NOM est donné (jamais affichée, jamais écrite ; masquée dans tout message) ;
  6. pire coût avant l'envoi : entrée comptée par l'interface de comptage d'Anthropic (`messages.count_tokens`, même
-    modèle, même message, même réglage), garde = ⌈compte × 1,01⌉ + 32 ; si le comptage échoue (hors clé refusée), borne
-    prudente déclarée de 1 jeton pour 2,5 caractères ; sortie comptée au maximum demandé ; refus si le cumul du journal
-    plus ce pire dépasse le plafond de la ligne ;
+    modèle, même message, même réglage), garde = ⌈compte × 1,01⌉ + 32 ; si le comptage échoue, pour quelque raison
+    que ce soit, refus (code 10) : rien n'est envoyé, aucune borne de repli (1,76 caractère par jeton mesuré à la
+    fumée) ; sortie comptée au maximum demandé ; refus si le cumul du journal plus ce pire dépasse le plafond de la
+    ligne ; une interruption (Ctrl-C, SIGTERM) pendant l'envoi est consignée au pire avant la sortie ;
  7. un seul appel en flux à `claude-fable-5-2`, effort « max » (le plus haut admis), réflexion adaptative (seul réglage
     admis par ce modèle, `budget_tokens` y est refusé) à affichage « omitted » (le texte de la réflexion n'est ni demandé
     ni écrit), aucune relance automatique (`max_retries=0`), aucun repli serveur vers un autre modèle (`fallbacks` non
@@ -65,7 +67,9 @@
 import math
 import os
 import re
+import signal
 import sys
+import threading
 import unicodedata
 
 VERSION = "relecture_fable_api_v1"
@@ -81,7 +85,6 @@
 MAX_SORTIE_MIN_RELECTURE = 64000
 MAX_SORTIE_MIN_FUMEE = 1000
 TEXTE_MIN_AU_DELA_REFLEXION = 32000
-CAR_PAR_JETON_BORNE = 2.5
 TOLERANCE_COMPTE = (0.01, 32)
 DELAI_LECTURE_S = 3600.0
 DELAI_CONNEXION_S = 30.0
@@ -101,16 +104,18 @@
 CODE_DEFAUT = 7
 CODE_ENVOI = 8
 CODE_EXISTE = 9
+CODE_COMPTAGE = 10
 
 # ---------- garde de motifs ----------
 
 NOMS_INTERDITS = ("lazar", "ciric")  # comparés sans casse ni accent (« Ćirić » → « ciric »)
-MOTIF_SESSION = re.compile(r"session_[0-9A-Za-z]{20,}")
+MOTIF_SESSION = re.compile(r"session[_\-][0-9A-Za-z]{20,}", re.IGNORECASE)
+MOTIF_UUID = re.compile(r"[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}", re.IGNORECASE)
 MOTIF_COURRIEL = re.compile(r"[A-Za-z0-9._%+\-]+@[A-Za-z0-9\-]+(?:\.[A-Za-z0-9\-]+)*\.[A-Za-z]{2,}")
 # Termes refusés partout (sans casse ni accent ; séparateurs « - », « _ » ou espace admis entre les mots)
 TERMES_PARTOUT = {
     "consigne-privee": re.compile(r"consigne[\s_\-]*privee"),
-    "conception-ii-b": re.compile(r"conception[\s_\-]*ii[\s_\-]*b(?![a-z0-9])"),
+    "conception-ii-b": re.compile(r"conception[\s_\-.()]*ii[\s_\-.()]*b"),
     "donnees/": re.compile(r"donnees\s*[/\\]"),
 }
 # Termes refusés dans un chemin ou un nom : jeton qui contient « / », « \ », « _ », « - » ou finit par une extension,
@@ -133,8 +138,11 @@
 def garde_motifs_ligne(ligne: str) -> list[str]:
     """Motifs interdits trouvés dans une ligne (noms des motifs, jamais le texte trouvé)."""
     trouves = []
+    ligne = "".join(c for c in ligne if unicodedata.category(c) != "Cf")  # caractères invisibles (U+200B…) retirés
     if MOTIF_SESSION.search(ligne):
         trouves.append("identifiant de session")
+    if MOTIF_UUID.search(ligne):
+        trouves.append("identifiant de session (UUID)")
     if MOTIF_COURRIEL.search(ligne):
         trouves.append("adresse de courriel")
     norm = sans_accents(ligne)
@@ -331,11 +339,6 @@
     return -(-compte * 101 // 100) + TOLERANCE_COMPTE[1]
 
 
-def borne_entree(caracteres: int) -> int:
-    """⌈caractères / 2,5⌉, en arithmétique entière."""
-    return -(-caracteres * 2 // 5)
-
-
 def pire_cout(entree: int, max_sortie: int) -> float:
     return (entree * PRIX_ENTREE_USD_PAR_MJ + max_sortie * PRIX_SORTIE_USD_PAR_MJ) / 1e6
 
@@ -440,10 +443,14 @@
 
 # ---------- écriture des sorties ----------
 
+def _sigterm_en_interruption(signum, frame):
+    raise KeyboardInterrupt(f"signal {signum} pendant l'envoi")
+
+
 def sceller(chemin: str) -> str:
     with open(chemin, "rb") as f:
         h = empreinte_octets(f.read())
-    with open(chemin + ".sha256", "w", encoding="utf-8") as f:
+    with open(chemin + ".sha256", "x", encoding="utf-8") as f:
         f.write(f"{h}  {os.path.basename(chemin)}\n")
     return h
 
@@ -511,8 +518,8 @@
         try:
             if journal and os.path.isdir(os.path.dirname(os.path.abspath(journal))):
                 ecrire_journal(journal, ligne)
-        except OSError:
-            pass
+        except OSError as e:
+            print(f"AVERTISSEMENT : refus non consigné au journal ({type(e).__name__})", file=sys.stderr)
         print(f"REFUS (rien n'est envoyé) : {masquer(r.message, cle)}", file=sys.stderr)
         return r.code
 
@@ -551,8 +558,8 @@
         # 4. sorties neuves
         if os.path.exists(args.sortie) and not os.path.isdir(args.sortie):
             raise Refus(CODE_USAGE, f"--sortie n'est pas un dossier : {chemin_affiche(args.sortie)}")
-        for nom in (NOM_RELECTURE, NOM_COMPTEURS, NOM_PARTIEL):
-            if os.path.exists(os.path.join(args.sortie, nom)):
+        for nom in [n + s for n in (NOM_RELECTURE, NOM_COMPTEURS, NOM_PARTIEL) for s in ("", ".sha256")]:
+            if os.path.lexists(os.path.join(args.sortie, nom)):
                 raise Refus(CODE_EXISTE, f"sortie déjà présente, jamais écrasée : "
                                          f"{chemin_affiche(os.path.join(args.sortie, nom))}")
         # 5. clé et espace
@@ -577,15 +584,12 @@
         envoyer = envoyeur or (lambda p: envoyer_par_sdk(client, p, cle))
         try:
             compte = compter(params)
-            entree_garde, source = garde_entree(compte), "count_tokens d'Anthropic, garde ⌈n × 1,01⌉ + 32"
         except CleRefusee as e:
             raise Refus(CODE_ENVOI, f"clé refusée au comptage, rien n'est envoyé : {masquer(e, cle)}")
-        except ComptageImpossible as e:
-            compte = None
-            entree_garde = borne_entree(len(invite))
-            source = f"borne déclarée de 1 jeton pour {CAR_PAR_JETON_BORNE} caractères (comptage impossible : " \
-                     f"{masquer(e, cle)[:200]})"
-            print(f"AVERTISSEMENT : {source}", file=sys.stderr)
+        except Exception as e:  # ComptageImpossible ou imprévu : aucune borne de repli, rien n'est envoyé
+            raise Refus(CODE_COMPTAGE, "comptage de l'entrée impossible, rien n'est envoyé : "
+                                       + masquer(f"{type(e).__name__} : {e}", cle)[:300])
+        entree_garde, source = garde_entree(compte), "count_tokens d'Anthropic, garde ⌈n × 1,01⌉ + 32"
         pire = pire_cout(entree_garde, max_sortie)
         ligne = _ligne_base(args, entrees, max_sortie)
         ligne.update({"sha256_invite": sha_invite, "caracteres_invite": len(invite), "entree_comptee": compte,
@@ -599,10 +603,21 @@
 
     # 7. un seul envoi
     os.makedirs(args.sortie, exist_ok=True)
+    principal = threading.current_thread() is threading.main_thread()
+    sigterm_avant = signal.signal(signal.SIGTERM, _sigterm_en_interruption) if principal else None
     try:
         res = envoyer(params)
     except Exception as e:  # imprévu : on ne sait pas si l'envoi est parti, compté au pire
         res = Resultat(envoye=True, erreur=masquer(f"imprévu : {type(e).__name__} : {e}", cle)[:400], base_cout="pire")
+    except BaseException as e:  # interruption (Ctrl-C, SIGTERM) pendant l'envoi : comptée au pire, consignée, puis on sort
+        ligne.update({"heure_utc": heure_utc(), "envoye": True, "statut": "defaut",
+                      "defaut": f"interruption pendant l'envoi : {type(e).__name__}", "base_cout": "pire",
+                      "cout_compte_usd": round(pire, 6)})
+        ecrire_journal(journal, ligne)
+        raise
+    finally:
+        if principal:
+            signal.signal(signal.SIGTERM, sigterm_avant)
     ligne["heure_utc"] = heure_utc()
     ligne.update({"envoye": res.envoye, "modele_servi": res.modele_servi, "identifiant_message": res.identifiant,
                   "identifiant_requete": res.identifiant_requete, "raison_arret": res.raison_arret,
```

### Essais

```diff
--- a/tests/test_relecture_fable_api_v1.py
+++ b/tests/test_relecture_fable_api_v1.py
@@ -136,6 +136,8 @@
     "lire consigne-privee-v1.md", "la consigne privée", "consigne_privee", "la conception-ii-b",
     "voir docs/verite_dommage/x.md", "la vérité-cachée.md", "fichier rendu-v1.md", "le `rendu`",
     "le fichier scores.json", "dossier `scores`", "lire donnees/brut.csv", "lire données/brut.csv",
+    "voir SESSION_01Qi7Gr3eYmAhDEJzqLgWcv1", "voir session-01Qi7Gr3eYmAhDEJzqLgWcv1",
+    "dossier 2eb82089-3810-5ff8-881f-da5f24b622eb", "lu par La\u200bzar", "lire conception-ii-b1-v1.md",
 ]
 SAINS = [
     "le rendu est bon", "les scores montent", "la vérité du dommage", "session_court", "écrire à a@b",
@@ -273,15 +275,16 @@
     assert envoi.appels == []
 
 
-def test_comptage_impossible_borne_declaree(dossier):
+@pytest.mark.parametrize("exception", [rf.ComptageImpossible("essai"), RuntimeError(f"boum {SECRET}")])
+def test_comptage_impossible_refuse_sans_envoi(dossier, exception):
     def compter(params):
-        raise rf.ComptageImpossible("essai")
+        raise exception
     envoi = FauxEnvoi(sain())
-    assert rf.relire(arguments(), envoyeur=envoi, compteur=compter, environ=ENV) == rf.OK
+    assert rf.relire(arguments(), envoyeur=envoi, compteur=compter, environ=ENV) == rf.CODE_COMPTAGE
+    assert envoi.appels == [] and not os.path.exists("sortie")
     (l,) = lignes_journal()
-    invite = envoi.appels[0]["messages"][0]["content"]
-    assert l["entree_comptee"] is None and l["entree_garde"] == -(-len(invite) * 2 // 5)
-    assert "borne déclarée" in l["source_entree"]
+    assert l["statut"] == "refus_avant_envoi" and l["cout_compte_usd"] == 0 and "comptage" in l["defaut"]
+    assert SECRET not in json.dumps(l)
 
 
 def test_cle_refusee_au_comptage_arrete_avant_envoi(dossier):
@@ -320,6 +323,56 @@
     assert "refus du modèle" in l["defaut"] and l["categorie_refus"] == "reasoning_extraction"
 
 
+@pytest.mark.parametrize("fin", ["stop_sequence", "pause_turn", "tool_use", None])
+def test_autre_raison_arret_est_un_defaut(dossier, fin):
+    envoi = FauxEnvoi(sain(fin=fin))
+    assert rf.relire(arguments(), envoyeur=envoi, compteur=compteur_fixe(), environ=ENV) == rf.CODE_DEFAUT
+    assert not os.path.exists("sortie/relecture-fable-api.md")
+    (l,) = lignes_journal()
+    assert l["statut"] == "defaut" and "raison d'arrêt inattendue" in l["defaut"]
+
+
+def test_journal_ecrit_avant_toute_sortie(dossier, monkeypatch):
+    vus, vrai = [], rf.ecrire_neuf
+
+    def espion(chemin, texte):
+        vus.append((os.path.basename(chemin), len(lignes_journal())))
+        return vrai(chemin, texte)
+    monkeypatch.setattr(rf, "ecrire_neuf", espion)
+    assert rf.relire(arguments(), envoyeur=FauxEnvoi(sain()), compteur=compteur_fixe(), environ=ENV) == rf.OK
+    assert len(vus) == 2 and all(n == 1 for _, n in vus)
+    vus.clear()
+    os.rename("sortie", "sortie-1")
+    assert rf.relire(arguments(), envoyeur=FauxEnvoi(sain(texte="coupé", fin="max_tokens")),
+                     compteur=compteur_fixe(), environ=ENV) == rf.CODE_DEFAUT
+    assert len(vus) == 2 and all(n == 2 for _, n in vus)
+
+
+def test_interruption_pendant_envoi_comptee_au_pire(dossier):
+    with pytest.raises(KeyboardInterrupt):
+        rf.relire(arguments(), envoyeur=FauxEnvoi(exception=KeyboardInterrupt()), compteur=compteur_fixe(),
+                  environ=ENV)
+    (l,) = lignes_journal()
+    assert l["statut"] == "defaut" and l["base_cout"] == "pire" and l["cout_compte_usd"] == l["pire_usd"]
+    assert not os.path.exists("sortie/relecture-fable-api.md")
+
+
+def test_sigterm_pendant_envoi_compte_au_pire(dossier):
+    import signal
+    import time
+    avant = signal.getsignal(signal.SIGTERM)
+
+    def envoyer(params):
+        os.kill(os.getpid(), signal.SIGTERM)
+        time.sleep(5)
+        return sain()
+    with pytest.raises(KeyboardInterrupt):
+        rf.relire(arguments(), envoyeur=envoyer, compteur=compteur_fixe(), environ=ENV)
+    (l,) = lignes_journal()
+    assert l["base_cout"] == "pire" and l["cout_compte_usd"] == l["pire_usd"]
+    assert signal.getsignal(signal.SIGTERM) is avant
+
+
 def test_modele_servi_autre_est_un_defaut(dossier):
     envoi = FauxEnvoi(sain(modele="claude-opus-4-8"))
     assert rf.relire(arguments(), envoyeur=envoi, compteur=compteur_fixe(), environ=ENV) == rf.CODE_DEFAUT
@@ -384,6 +437,16 @@
     assert envoi.appels == [] and open("sortie/relecture-fable-api.md").read() == "ancienne\n"
 
 
+@pytest.mark.parametrize("nom", ["relecture-fable-api.md.sha256", "compteurs.json.sha256"])
+def test_compagnon_orphelin_jamais_ecrase(dossier, nom):
+    os.mkdir("sortie")
+    with open(f"sortie/{nom}", "w") as f:
+        f.write("ancien\n")
+    envoi = FauxEnvoi(sain())
+    assert rf.relire(arguments(), envoyeur=envoi, compteur=compteur_fixe(), environ=ENV) == rf.CODE_EXISTE
+    assert envoi.appels == [] and open(f"sortie/{nom}").read() == "ancien\n"
+
+
 def test_max_sortie_basse_refusee_hors_fumee(dossier):
     envoi = FauxEnvoi(sain())
     assert rf.relire(arguments("--max-sortie", "2000"), envoyeur=envoi, compteur=compteur_fixe(),
@@ -498,6 +561,15 @@
     assert l["base_cout"] == "pire" and l["cout_compte_usd"] == l["pire_usd"]
 
 
+def test_chemin_reel_comptage_500_refuse_sans_envoi(dossier, serveur):
+    serveur["compte"] = (500, {"type": "error", "error": {"type": "api_error", "message": "boum"}})
+    code = rf.relire(arguments("--fumee", "--max-sortie", "2000"), environ=ENV, base_url=serveur["url"])
+    assert code == rf.CODE_COMPTAGE
+    assert len(serveur["requetes"]) == 1  # le comptage seul, aucune relance, aucun envoi
+    (l,) = lignes_journal()
+    assert l["statut"] == "refus_avant_envoi" and l["cout_compte_usd"] == 0
+
+
 def test_chemin_reel_refus_400_compte_zero(dossier, serveur):
     serveur["messages"] = (400, {"type": "error", "error": {"type": "invalid_request_error", "message": "mauvais"}})
     code = rf.relire(arguments("--fumee", "--max-sortie", "2000"), environ=ENV, base_url=serveur["url"])
```

## Remarques sans correction demandée

1. Noms en cyrillique (« Лазар », « Ћирић ») : non cherchés ; si la mère le veut, `NOMS_INTERDITS = ("lazar", "ciric",
   "лазар", "ћирић", "чирич")` (la mise en minuscules suffit, « ћ » ne se décompose pas).
2. Le kit lit `ANTHROPIC_CUSTOM_HEADERS` même avec une clé explicite et ajoute ces en-têtes à chaque requête. Si la mère
   veut l'exclure : au point 5, `if "ANTHROPIC_CUSTOM_HEADERS" in os.environ: raise Refus(CODE_USAGE, "variable
   ANTHROPIC_CUSTOM_HEADERS présente : en-têtes ajoutés par le kit, refus")` (lecture du nom seul, jamais de la valeur).
3. Une écriture du journal qui échoue après un envoi payé (disque plein, cas vu pendant cette contre-lecture) lève une
   exception et perd le texte reçu. Une v2 pourrait, dans ce cas seul, écrire le texte dans le fichier
   « PAS-UNE-RELECTURE » avant de sortir en défaut (récupérer ce qui est récupérable).
4. `entree_au_dela_de_la_garde`, `--max-sortie` au-dessus de 128 000 et `--plafond-ligne` nul ou non fini n'ont pas
   d'essai ; gardes simples, lues justes.
5. Le kit `anthropic` 2.12.0 n'est pas dans `requirements-cpu.txt` (réserve 5 du rapport) : à inscrire par la mère,
   sinon l'outil ne s'installe pas sur une machine neuve.
6. Le journal de fumée et la sortie de fumée gardent l'empreinte `056bc4ef…` : après la v2, ils restent l'appel de fumée
   de la v1 ; refaire un appel de fumée avec la v2 est à décider par la mère (un appel, sous le même GO).
