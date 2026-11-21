# Relevé du lot 0 — véhicule NA-1, course « nouvelles attaques » — v1

- Développeur neuf, modèle O. Je n'ai écrit ni la conception, ni sa contre-lecture, ni aucun orchestrateur, ni aucun lanceur.
- Date (UTC) : 2026-11-21 ; relevé de `date -u` : 07:19:51Z, après la lecture, avant l'écriture.
- Mandat : lot 0 accordé par la mère (06:58Z). Lecture seule : aucun programme exécuté, aucun essai, aucun import, aucune écriture dans un dépôt, aucun appel, aucune clé lue. Rien ouvert sous `archives-reponses-modeles/` ni sous `/root/.claude/`. Aucun refus rencontré.
- Pièces : conception `675f8d39dc64548f34e36763b3a523277d9c1daa1c208e3b2b678dd9f79ace9b` (égale à son compagnon) ; contre-lecture `f5b7aacc9d96dfd3bb10eaa80a6f451d646b3b7c06844dbb4da6837182cf36db` (égale à son compagnon). Code : table d'empreintes jointe (`table-empreintes-lot-0-vehicule-na-v1.md`) ; chaque fichier de code lu égale l'empreinte que L9, L10 ou le manifeste v68 épinglent, sauf `noyau_v55.py`, `caviardage.py`, `outils.py`, `graines_v53.py` et `suivi_roles_v54.py` qu'aucune de ces listes n'épingle (le dernier égale l'empreinte que cite CL, l. 28).
- Orchestrateur : `/home/user/lciric/ideation-organism`, tête `a41b7b50f7c64ce488c120bb89ad3d25fb1dd1cb`, arbre propre (`git status --short` vide). Paquet v68 : manifeste `4ed9fd8e…`, ses huit fichiers égaux au manifeste. Dépôt de l'organisme : branche `lot/compte-organisme-v1`, tête `0def0643…` (la conception citait `9555d8b6…` ; les fichiers lus égalent leurs empreintes épinglées).
- Un écart de méthode : le chemin des fichiers du paquet ne figurant dans aucune pièce, je l'ai lu dans la liste des noms du commit de versement `61987a3a…` de `verse/vehicule-na-v1` (`git show --name-only`, restreint au dossier `orchestrateur-v68`). La commande d'une espèce compatible OpenAI n'existe que sur `origin/main` (`a5f06087…`) : je l'ai copiée par `git cat-file blob` dans un dossier à part du bloc-notes (`lot-0-copie-astra/`) pour l'empreinter ; son empreinte égale celle que L9 épingle.

Sigles : ORC = `/home/user/lciric/ideation-organism/orchestrator/` ; PQ = `…/epreuves-v9/orchestrateur-v68/paquet/orchestrator/` ; ORG = `/home/user/controle-ia-travail-organisme/` ; L9, L10, E9 comme à la conception ; CO = la conception ; CL = sa contre-lecture.

## Les quatorze réponses

### Q1 — Ce que chaque type d'adaptateur ajoute au texte remis, octet par octet

**Réponse fermée : oui pour le type `claude_sdk` (un texte système fixe, par rôle) ; non pour les trois autres types (`commande_externe` Gemini, `commande_externe` compatible OpenAI, `kimi_protocole`) : la consigne part seule dans un message utilisateur, entourée de réglages non textuels.**

**A. Avant l'adaptateur, le noyau assemble lui-même du texte** (ce n'est pas l'adaptateur, mais c'est ce que CO, § 5.3 appelle « la forme servie par l'orchestrateur ») :

| rôle | octets ajoutés à la pièce | preuve |
|---|---|---|
| proposeur (v68) | la pièce passée par `rstrip()` (fin de ligne retirée), puis `"\n\n## Case\nTexte : " + case[0] + " ; bras : " + case[1] + "\n"`, puis, s'il y a un héritage, `"\n## " + titre + "\n" + corps + "\n"` | PQ `pole/course2_v68.py`, l. 190-194 : « `consigne = consigne.rstrip() + f"\n\n## Case\nTexte : {case[0]} ; bras : {case[1]}\n"` » |
| portier (aiguilleur) | `consigne.rstrip() + "\n\n## La fiche\n```json\n" + json.dumps(contenu, ensure_ascii=False, indent=1) + "\n```\n"` ; aucun identifiant | ORC `pole/fiches_v54.py`, l. 57-59 : « `entree = consigne_figee.rstrip() + "\n\n## La fiche\n```json\n" + corps + "\n```\n"` » ; ORC `pole/noyau_v54.py`, l. 232 |
| juge | la même chose, avec en dernière clé de l'objet `"identifiant": "F" + 10 caractères hexadécimaux` | ORC `pole/noyau_v56.py`, l. 198-199 : « `ident_servi = "F" + self.graines.jeton_opaque(…, 5)` » ; `fiches_v54.py`, l. 50-51 ; ORC `pole/graines_v53.py`, l. 65-67 : « `…integers(0, 256, size=octets)).hex()` » |

**B. Ce que l'adaptateur ajoute, type par type.**

| type | texte ajouté | réglages ajoutés (non textuels) | preuve |
|---|---|---|---|
| `claude_sdk` (`AdaptateurClaudeSDK`) | **un texte système fixe**, choisi par `role_kit` : pour `proposeur_ideation`, le texte des l. 101-107 ; pour `juge_ideation`, celui des l. 108-111. **Le portier reçoit le texte du juge** : il est appelé avec `role_kit="juge_ideation"`. La consigne elle-même part inchangée comme invite (`sdk.query(prompt=consigne, …)`) | `model`, `effort` (« high » pour le proposeur, « medium » pour le juge et le portier), `tools=[]`, `max_turns=1`, `max_budget_usd` = plafond de l'appel, `permission_mode`, `disallowed_tools`, `setting_sources=[]`, `verbatim_prompts=True`, `fallback_model=None`, bac à sable, variables d'environnement du relais et deux variables sans repli | ORC `pole/adaptateurs.py`, l. 338-339 : « `"system_prompt": (… else CONSIGNES_SYSTEME[role])` » ; l. 101-111 (les deux textes) ; l. 494 ; l. 55 ; l. 325-350 ; ORC `pole/noyau_v54.py`, l. 235 : « `role_kit="juge_ideation"` » (portier) ; ORC `pole/noyau_v56.py`, l. 165 (`max_tours` = 1) |
| `commande_externe`, commande Gemini (`commande_argon_v3d.py`, sous ses enveloppes) | **aucun** : `contents = [{"role": "user", "parts": [{"text": consigne}]}]`, la consigne décodée UTF-8 telle que lue sur l'entrée standard ; aucune consigne système | `generationConfig.maxOutputTokens` ; `generationConfig.thinkingConfig.thinkingBudget` sauf avec `--sans-config-pensee` (la branche proposeur de l'enveloppe v9 le porte, la branche juge non) ; `tools: [{"google_search": {}}]` seulement avec `--recherche-web`, absent des deux enveloppes v9 ; un appel `countTokens` préalable porte les mêmes `contents` | ORG `docs/notes/ideation-organisme-v1/argon-recherche-v1/commande_argon_v3d.py`, l. 818 ; l. 857-862 : « `corps = {"contents": contenus, "generationConfig": config}  # ni outil, ni fonction` » ; l. 824 ; l. 713 ; ORG `rapports/fille-ideation-1-v1/appel-argon-sans-troncature-v1.sh`, l. 37 et 40 ; `appel-carbon-synchrone-v1.sh`, l. 42 |
| `commande_externe`, commande compatible OpenAI | **aucun** : `{"model": …, "messages": [{"role": "user", "content": consigne}], "max_completion_tokens": n}` | `max_completion_tokens` ; le relais `relais_kimi_v4.py` ajoute `"stream": true` et `"stream_options": {"include_usage": true}` et resérialise le JSON | copie de `commande_astra_v1.py` (`origin/main`), l. 131 ; ORG `docs/notes/ideation-organisme-v1/relais-kimi-v1/relais_kimi_v4.py`, l. 720-721 : « `json.dumps(dict(demande, stream=True, stream_options={"include_usage": True}), …)` » |
| `kimi_protocole` | **aucun** : `{"model": modele, "messages": [{"role": "user", "content": consigne}], "max_tokens": n}` | `max_tokens` ; le même relais ajoute `stream` et `stream_options` | ORC `pole/adaptateur_kimi_v53.py`, l. 98 ; `relais_kimi_v4.py`, l. 720 |
| enveloppes du lanceur (garde de crédit, conservation) | **aucun** : l'entrée standard est passée à l'identique | — | ORG `scripts/garde_credit_relais_v5.py`, l. 142-143 ; ORG `scripts/enveloppe_conservation_reponses_v1.py`, l. 166-169 : « `p = subprocess.run(commande, input=consigne, capture_output=True)` » |
| variables d'environnement de la commande | hors de la requête : `PLAFOND_SESSION_USD`, `ROLE_POLE`, `MODELE_DEMANDE_POLE`, `ETAPE_POLE`, `PLAFOND_ETAPE_USD` | — | ORC `pole/adaptateurs.py`, l. 658-663 ; ORC `pole/adaptateurs_v56.py`, l. 69-70 |
| relais Claude, relais Gemini | **aucun** : le corps est transmis tel quel, seuls des en-têtes changent | — | ORC `pole/relais_reel_v2.py`, l. 300-309 ; ORG `…/relais_gemini_v2.py`, l. 286-305 |

Texte système du proposeur, exact aux l. 101-107 (les espaces qui encadrent les guillemets français sont à vérifier à l'octet par programme au lot 3 : la lecture à l'écran ne les distingue pas) : « Tu es un proposeur du pôle en prise « idéation ». Tu lis les pièces fournies dans la consigne et tu proposes des questions de recherche et des approches, chacune au gabarit d'une fiche d'idéation, au niveau méthode seulement : aucune technique d'attaque, aucune recette, aucune séquence opérationnelle, aucun exemple de mode de sabotage ; les travaux côté attaque sont nommés par classe et protocole d'évaluation. Aucun réseau, aucune clé, aucune recherche ; tu n'inventes aucune référence (marque RAPPORTÉ ou SUPPOSÉ). Tu réponds par un bloc JSON {fiches}. »

Texte système du juge et du portier, l. 108-111 : « Tu es le juge figé du tournoi d'idéation du pôle : aveugle aux auteurs, tu n'as écrit aucune fiche. Tu notes chaque fiche sur la grille fixée dans la consigne, une ligne de justification par critère, sans rien ajouter aux fiches et sans rien proposer toi-même. Aucun réseau, aucune recherche. Tu réponds par un bloc JSON {notes}. »

**Non établi par lecture** : ce que l'outil du kit ajoute lui-même au corps de la requête qu'il envoie au relais Claude (texte propre de l'outil, borne de sortie, réflexion, définitions d'outils). C'est dans le binaire de l'outil, hors de ce code. Seul le faux fournisseur de l'essai à blanc peut le relever (CO, § 6.3, point 2).

**Ce que cela change.**
- Lot 4 et § 2.3, l. 116 de CO : la réponse est **oui**, donc la branche « l'additif le déclare comme enveloppe » ne vaut pas sous D2 (CL, 2.3 et 6.4). Phrase à écrire : « le texte système fixe de `claude_sdk` est retiré ».
- **Aucun réglage ne le retire** : `construire_options` pose toujours un texte système (l. 338-339), les seules variantes étant deux autres textes fixes (étage de tests, dossier fermé). CL, 2.3 demande un retrait « par un réglage déclaré et sans modifier l'adaptateur » : **ce n'est pas possible**. Il faut un fichier neuf (un adaptateur Claude du véhicule qui construit ses options sans texte système), et le comportement de l'outil sans texte système (texte par défaut de l'outil ou rien) n'est pas lisible ici : il doit être relevé au faux fournisseur **avant** l'écriture de l'additif.
- Asymétrie à dire à la mère : aujourd'hui seules les espèces servies par `claude_sdk` reçoivent « Tu réponds par un bloc JSON {fiches} ». Une fois ce texte retiré, aucune espèce ne reçoit plus de syntaxe de sortie : le point 2 du § 9 de CO devient bloquant pour le lecteur de fiches (lot 5, voir Q6).
- Portier : le texte du juge (« bloc JSON {notes} ») partirait vers le portier ; sous D2 il est retiré avec l'autre.
- Lot 3 : les octets du noyau (tableau A) sont du texte ajouté à la pièce. Pour le proposeur, le module `requete` les remplace (CO, § 2.9). Pour le portier et les juges, « la fiche, dans la forme servie par l'orchestrateur » (CO, § 5.3) **est** ce texte (`## La fiche`, clôture de bloc JSON, indentation d'un espace, clé `identifiant` du juge) : l'additif doit le déclarer octet pour octet, ou le lot 3 doit écrire sa propre forme. Le `rstrip()` du noyau change aussi le dernier octet de la pièce : le module `requete` doit dire s'il le fait.
- Lot 4 et § 6.3 : le relais compatible OpenAI resérialise le JSON. L'égalité « texte reçu, transport retiré » doit porter sur la chaîne de la consigne extraite du corps, jamais sur les octets du corps HTTP.

### Q2 — Où les noms de fournisseurs sont fixés ; deux adaptateurs du même type sur deux relais

**Réponse fermée : dans l'orchestrateur, nulle part (noms libres, clés de `conf["fournisseurs"]`) ; dans les lanceurs, à cinq noms fixes, un type par nom. Deux adaptateurs du même type : rien à changer dans l'orchestrateur ; à changer dans le lanceur.**

- ORC `demonstrations/ideation_v8.py`, l. 67-80 : « `for nom, f in sorted((conf.get("fournisseurs") or {}).items()):` » ; un adaptateur par nom, son type lu dans `f["type"]`, une porte par nom (l. 80). Chaque rôle désigne son adaptateur par le champ `fournisseur` (configuration v5, l. 180-232), et le noyau l'atteint par ce nom (ORC `pole/noyau_v56.py`, l. 165 : « `self.ad[fournisseur].lancer(…)` »).
- L9, l. 539-540 (L10, l. 641-642) : « `TYPES_PERMIS = {"claude": "claude_sdk", "argon": "commande_externe", "kimi": …, "astra": …, "carbon": …}` » ; L9, l. 1817-1822 refuse tout autre nom et exige `claude` et `argon` ; traitements propres à un nom : l. 1845-1848, 1862-1865, 1866-1887, 1797-1800 (`modeles_claude_de_la_configuration` filtre `fournisseur == "claude"`), 2054-2057, 2229 (`FOURNISSEURS_DISPENSABLES`).
- Ce qu'il faut pour deux `claude_sdk` sur Minuit et Luc : deux noms neufs dans `conf["fournisseurs"]`, chacun avec son `url_relais` et sa porte « commande » ; le lanceur doit les admettre (table neuve à la place de `TYPES_PERMIS`) et réécrire les contrôles nommés ci-dessus.

**Deux faits de plus, qui touchent la table des rôles et des clés :**
1. Le noyau exige un adaptateur pour des rôles **jamais appelés** : les deux lecteurs d'étiquettes et le metteur en fusion (ORC `pole/course2_v54.py`, l. 88-91 et 97-99 : « `raise ConfigurationRefusee("adaptateur absent pour : " …)` » ; configuration v5, l. 200-211 et 228-232). La table du § 2.3 de CO doit leur donner un nom d'adaptateur présent, ou la classe neuve doit surcharger `fournisseurs_requis`.
2. À chaque étape jouée, le plafond est transmis à la porte de **chaque** adaptateur (ORC `pole/noyau_v56.py`, l. 237-249) : quatre relais, quatre portes par étape.

**Ce que cela change** : lot 8 (table des noms et contrôles réécrits) ; lot 4 ou 6 (rôles jamais appelés dans la table). Et surtout le point qui suit, qui contredit CO, § 2.3, l. 103.

**Le routage par rôle n'est pas faisable dans `lancer` tel qu'il est appelé.** L'adaptateur reçoit `(role_kit, consigne, dossier, plafond, 1, modele=…)` (ORC `pole/noyau_v56.py`, l. 165) : ni l'étiquette du rôle, ni la génération, ni la case. Le portier et les juges partagent `role_kit="juge_ideation"` (`noyau_v54.py`, l. 235 ; `noyau_v56.py`, l. 202). Le dossier de session est un nom opaque (empreinte du chemin logique, ORC `pole/noyau_v55.py`, l. 77-81), dont la correspondance n'est gardée que dans `self.sessions` de la génération. Le pas 1 (rôle, clé) et la ligne de journal du pas 4 (rôle, identifiant de la case, génération) ne peuvent donc pas être tenus par un adaptateur gardé qui ne lit que ses arguments. Il faut : soit une classe de génération neuve qui surcharge `appel` (fichier neuf) et pose le contexte avant chaque envoi, soit donner à l'adaptateur gardé la génération pour qu'il lise `sessions[basename(dossier)]`. Phrase de CO à changer : « L'appel du noyau (…) ne change pas : il atteint l'adaptateur gardé ».

### Q3 — Comment la configuration v5 ne joue pas la passe « tableau », les étiquettes et les fusions ; trois étapes seulement ?

**Réponse fermée : non, une génération ne peut pas ne déclarer que trois étapes. La configuration v5 déclare les six et en neutralise trois par leurs valeurs.**

- Six étapes exigées : ORC `pole/course2_v53.py`, l. 73-76 : « `absentes = [e for e in ETAPES if e not in noms]` … `"budget.etapes : étapes de la génération absentes du plan : "` » ; la v56 joue les six, par la liste du module et non par un attribut de la classe : ORC `pole/course2_v56.py`, l. 346 : « `for nom in ETAPES:` ».
- `passe_tableau` et `fusions` : sacrifiables, plafond de relais 151 au-dessus de S17 150 (configuration v5, l. 93-112), donc retirées au point 3 de la règle d'A1 : ORC `pole/budget_v56.py`, l. 177-180 : « `if e["role"] == "sacrifiable": self._appliquer(e, …) ; return RETIREE` ». L9 l'exige : l. 2267-2270.
- `etiquettes` : protégée, plafond de relais 0, attendu 0, aucun bras (`"bras": []`, configuration v5, l. 100-104 et 222-224) : l'étape est **jouée**, sans appel (ORC `pole/course2_v54.py`, l. 257-265), mais elle écrit `accords.json` et des dépôts au coffre (l. 273-277) et reçoit la transmission du plafond (ORC `pole/noyau_v56.py`, l. 254-258).
- Champs exigés par la vérification même quand rien ne les sert : `lecteurs_etiquettes` (deux, distincts), `tableau.consigne_passe`, `memoire.methode`, plafonds de session `fusion` et `lecteur` (ORC `pole/course2_v53.py`, l. 43-44, 86-90, 97-99).

**Ce que cela change** : lot 6. CO, § 2.9 : « ses étapes sont « proposition », « aiguillage », « juges », et aucune autre » ne se tient qu'en surchargeant `verifier_configuration` **et** `executer` (qui lit la liste du module). La plus petite différence est de garder les six étapes neutralisées comme en v5 et de l'écrire ainsi : « trois étapes jouées avec appels ; `etiquettes` jouée sans appel ; `passe_tableau` et `fusions` retirées par construction ».

### Q4 — Rien d'autre que la boucle des cases ne suppose les mêmes cases à chaque génération ?

**Réponse fermée : oui pour la lecture en course (seule la boucle de `_proposer` lit les cases, la passe « tableau » étant retirée) ; mais l'objet `conf` est le même pour toutes les générations et sa forme des cases est vérifiée à chaque génération.**

- PQ `pole/course2_v68.py`, l. 186 : « `for ic, case in enumerate(self.conf["cases"]):` » ; l. 329 : chaque `GenerationV68` reçoit le même `conf`. Autre lecture : ORC `pole/course2_v54.py`, l. 205 (passe « tableau », retirée).
- Forme exigée à chaque construction de génération : ORC `pole/course2_v53.py`, l. 94-96 : « `if not (isinstance(c, list) and len(c) == 2 …): manques.append("cases : [texte, bras] attendu")` » ; non vide : l. 43 et 71.
- La case entre dans les métadonnées de la fiche : ORC `pole/fiches_v53.py`, l. 46.
- Les identifiants de fiche ne se répètent pas d'une génération à l'autre (préfixe de tâche par génération) : ORC `pole/course2_v54.py`, l. 102.

**Ce que cela change** : lot 6. La classe neuve lit ses cases au tirage scellé ; `conf["cases"]` doit rester non vide et de la forme `[texte, bras]`, ou la vérification être surchargée. De plus, la mémoire anti-redite, que CO, § 1.2 dit « retirée de ce régime », tourne encore dans `executer` (ORC `pole/course2_v56.py`, l. 355 et 368) et passe d'une génération à l'autre (PQ `course2_v68.py`, l. 344) : la retirer demande de surcharger `executer`.

### Q5 — Statuts de retour ; refus de classifieur, refus pour crédit, erreur d'accès, réponse coupée

**Réponse fermée : six statuts ; le refus de classifieur se distingue (statut « refus » et champ `refus`) ; le refus pour crédit, l'erreur d'accès et la réponse coupée ne se distinguent pas par le statut (tous « erreur », sauf deux cas), seulement par le texte libre `erreur`, que le noyau ne garde pas.**

- Statuts : ORC `pole/adaptateurs.py`, l. 27 : « `STATUTS_RESULTAT = ("ok", "erreur", "budget_depasse", "tours_epuises", "refuse", "refus")` ».
- Le noyau ne note que le statut : ORC `pole/noyau_v56.py`, l. 172-175 (aucun champ `erreur`).

| issue | `claude_sdk` | commande Gemini | compatible OpenAI et `kimi_protocole` |
|---|---|---|---|
| refus de classifieur | « refus », `refus.evenement` = `assistant.stop_reason` ou `result.stop_reason` (`adaptateurs.py`, l. 505-507, 523-525, 545-548) | « refus », `commande.refus` si la commande dit `refus` ou `stop_reason` (l. 688-689) ; une consigne bloquée par l'interface est un code non conforme, donc « erreur » (commande, l. 664) | « refus », `kimi.content_filter` (`adaptateur_kimi_v53.py`, l. 170-173) |
| même statut, autre cause | « refus » aussi pour un modèle servi différent (l. 500-504) : lire `refus.evenement` | idem (`commande.modele_servi`) | idem ; et HTTP 403 du relais = « refus » `relais.modele_non_permis` (l. 131-132) |
| refus pour crédit | « erreur » ; `erreur` peut rester vide quand le message de résultat est en erreur (l. 518-520) ; le 402 du relais Claude (plafond du relais) n'est vu qu'au journal du relais (`relais_reel_v2.py`, l. 275-279) | « erreur » ; la garde de crédit du lanceur lit la sortie de la commande et écrit l'arrêt (`garde_credit_relais_v5.py`, l. 46-53) | 402 → « budget_depasse » (`adaptateur_kimi_v53.py`, l. 131) |
| erreur d'accès | « erreur » (`ClaudeSDKError`, l. 538-539) | « erreur » (code d'interface) | « erreur » (l. 144-150) |
| réponse coupée | délai : « erreur » (l. 543-544) ; tours : « tours_epuises » ; budget : « budget_depasse » | « erreur » (MAX_TOKENS, commande l. 682) | `length` : « erreur » (l. 176-177) |

**Ce que cela change** : lot 4, pas 6 du § 2.3 (« statut lu pour les arrêts n° 1 et n° 13 ») : le statut ne suffit pas. L'adaptateur gardé doit lire `statut`, `refus["evenement"]` et `erreur` du résultat ; pour les deux clés Claude, l'arrêt n° 13 demande de lire l'état ou le journal du relais, car l'adaptateur du kit ne dit pas un refus pour crédit. La garde de crédit du lanceur ne couvre que les commandes externes (L9, l. 2229-2235).

### Q6 — Ce que lisent `fiches_du_texte` et `preparer` ; ce que `champs_fiche` peut porter

**Réponse fermée : `fiches_du_texte` ne lit qu'un objet JSON qui porte la clé `fiches` (une liste) ; `preparer` exige un dictionnaire, refuse dix noms de champ réservés, exige les champs obligatoires non vides, accepte tout champ de plus, et caviarde les chaînes. `champs_fiche` est une liste de noms quelconques, dont seule la présence non vide est vérifiée.**

- ORC `pole/fiches_v53.py`, l. 49-54 : « `bloc = extraire_bloc_json(texte, cle)` … `raise FicheRefusee(f"bloc JSON {{{cle}: [...]}} absent")` » ; ORC `pole/outils.py`, l. 106-129 : le dernier objet qui porte la clé, bloc clôturé `json` d'abord, objet nu sinon. Les lignes « champ : valeur » ne sont pas lues.
- `{"fiches": []}` rend une liste vide, donc « exploitable » pour le noyau ; une réponse sans bloc rend `None`, donc un échec compté (ORC `pole/course2_v54.py`, l. 470-474 ; voir Q12).
- ORC `pole/fiches_v53.py`, l. 19 : « `CLES_META = ("ident", "meta", "empreinte", "case", "fournisseur", "passe", "origine", "bras", "classe", "temoin")` » ; l. 33-35 : refus de ces champs ; l. 36-38 : obligatoires non vides ; aucun refus d'un champ en trop ; valeurs de tout type JSON ; l. 39 : `caviarder_objet` (motifs de secrets, ORC `pole/caviardage.py`, l. 12-22) ; l'empreinte est prise sur le contenu caviardé (l. 45).

**Ce que cela change** (lot 5 ; CO, § 2.4, § 5.4) :
- **Si le contrat de fiche porte un champ nommé `case`** (le gabarit des témoins, repris par CO, § 5.2, parle de « leur champ `case` »), **chaque fiche est refusée par `preparer`**. Le lot 5 ne doit pas appeler `fv.preparer`, ou le champ doit changer de nom, ce qui touche la partie servie, donc la lettre (nœud). Je n'ai pas ouvert la partie servie : à vérifier par le concepteur.
- « Un champ de plus envoie la fiche au coffre » (CO, § 2.4, (i)) : `preparer` l'accepte ; contrôle neuf au lot 5.
- Le lecteur à deux syntaxes de CO, § 9, point 2 est du code neuf : rien n'existe pour « champ : valeur ».
- Le caviardage peut changer un champ fermé : la comparaison à l'octet de l'arrêt n° 4 doit dire si elle lit le texte brut ou le contenu caviardé.

### Q7 — Relais factices et faux fournisseur dans l'essai à blanc de L9

**Réponse fermée : aucun relais n'est lancé et aucun faux fournisseur n'existe dans l'essai à blanc de L9 : il tourne en moteur simulé, sur une déclaration de relais qu'aucun programme ne contacte.**

- L9, l. 2903 : « `r.moteur, r.exiger_bac_a_sable, r.verifier_go = "simule", False, False` » ; déclaration d'essai, adresse `http://127.0.0.1:18999`, porte `["/bin/false"]`, noms de clés factices : l. 2874-2888 ; en moteur simulé, procédure des relais, relevé de prix et porte à blanc ne sont pas joués : l. 2630-2632 et 2672.
- L'orchestrateur, en simulé, prend `AdaptateurSimuleV56` pour chaque fournisseur : ORC `demonstrations/ideation_v8.py`, l. 50-56 et 135-136.
- Ailleurs : E9 a un juge et un aiguilleur factices hors ligne (ORG `scripts/epreuve_temoins_auto_conception_v9.py`, l. 344-379) ; les essais de l'orchestrateur lancent le relais Claude contre un amont factice (`relais_reel_v2.py`, l. 35-36 ; fichier d'essai non lu) ; l'adaptateur du protocole compatible OpenAI accepte un ouvreur injecté (`adaptateur_kimi_v53.py`, l. 74-75).

**Ce que cela change** : aucun changement de fond (CO, § 2.12 compte déjà le faux fournisseur comme neuf). Précision pour les lots 6 et 9 : rien n'est à reprendre de L9 pour lui ; seuls les factices de E9 et l'amont factice des essais du relais servent de modèle.

### Q8 — Où le coût par espèce et par rôle est écrit pour une génération ; pour plusieurs ?

**Réponse fermée : pour une génération, oui (une ligne par appel, rôle et fournisseur, dans `consommations.json` de la génération ; L9 en fait la somme par rôle et par fournisseur pour la génération 1) ; pour plusieurs, non : seuls des totaux par génération sont écrits.**

- ORC `pole/noyau_v56.py`, l. 172-175 (étape, rôle, coût, fournisseur, statut) ; ORC `pole/course2_v56.py`, l. 325-328 (`consommations.json`).
- L9, l. 2418 : « `chemin = sortie / "generation-1" / "consommations.json"` » ; l. 2430-2433 (`par_relais`, `par_role`).
- PQ `pole/course2_v68.py`, l. 338 : « `"cout_generation_usd": round(gen.budget.cumul, 6)` » (total) ; L10, l. 2843-2851 : `couts_generation` rend `total_usd` et le nombre de lignes, rien par rôle.

**Ce que cela change** : lots 7 et 8. CO, § 1.2 reprend de L10 « la lecture des coûts génération par génération » : elle ne donne que des totaux. Le lot 8 doit faire passer `couts_reels` de L9 sur chaque `generation-k` ; l'espèce d'un proposeur se lit par son étiquette de rôle, la clé par le nom du fournisseur et la table des rôles et des clés.

### Q9 — Les relais tiennent-ils un plafond cumulé sur trois générations et un compte d'appels suffisant ?

**Réponse fermée : plafond cumulé, oui (un compteur unique pour la vie du relais, lancé une fois pour la ligne entière) ; compte d'appels suffisant pour trois générations, non (les bornes sont calculées pour une génération).**

- ORC `pole/relais_reel_v2.py`, l. 153-183 : « `if self.depense + self.engage + self.reserve > self.plafond …: return False` » (cumul jamais remis à zéro) ; aucun compte d'appels borné dans ce relais. ORG `scripts/porte_plafond_relais_v1.py`, l. 9-14 : « le relais est lancé une fois … au plafond de la ligne … Elle ne relance rien ».
- L9, l. 1955-1956 : le plafond du relais Claude doit **égaler** le plafond d'arrêt de la course (« Claude : égal, relais de ligne entière »).
- L9, l. 2628-2630 : `appels_argon_au_pire(fixe, len(lots["lots"]), …)`, `appels_externes=len(lots["lots"])` (une génération) ; l. 1965-1967 et 2025-2030 (`--max-appels`, `max_lots`) ; l. 420-422 (deux appels de relais par appel Gemini, plus deux).

**Ce que cela change** : aucun changement de fond (CO, § 1.2 et § 2.11, point 7 le disent déjà). Précisions pour le lot 8 : remplacer l'égalité de L9, l. 1955-1956 par « égal à la part de sa clé » ; compter les bornes pour trois générations, juges compris.

### Q10 — Les réponses brutes du premier relais sont-elles conservées comme celles des commandes externes ?

**Réponse fermée : non.**

- L9, l. 2229 et 328 : l'enveloppe de conservation n'entoure que les commandes externes nommées dans `FOURNISSEURS_DISPENSABLES` ; les adaptateurs `claude_sdk` n'ont pas de commande à envelopper.
- ORC `pole/relais_reel_v2.py`, l. 30 : « Journal des appels en JSON par ligne : jamais la clé, jamais le corps des messages » ; l. 352-355.
- Le noyau ne garde de la réponse que les fiches lues (ORC `pole/course2_v56.py`, l. 366-367). Seule trace possible : les transcriptions de l'outil sous `.claude` du dossier maison, inventoriées par L9 (l. 2690, 2785), si l'outil les écrit (non établi par lecture).

**Ce que cela change** : lot 4 ou 8, et CO, § 1.2 (« l'enveloppe de conservation des réponses brutes », gardée de L9) : elle ne couvre ni Minuit ni Luc. Il faut un chemin neuf pour ces deux clés, par exemple l'adaptateur gardé qui écrit le texte brut dans le dossier de sortie avant de rendre la main (V9, l. 396, citée par CL, 2.4).

### Q11 — Les appels d'une étape sont-ils lancés l'un après l'autre ?

**Réponse fermée : oui.**

- PQ `pole/course2_v68.py`, l. 186-199 (boucle des cases et des proposeurs, appel synchrone) ; ORC `pole/course2_v54.py`, l. 168-169 (aiguillage) ; ORC `pole/noyau_v56.py`, l. 197-204 (juges).
- Adaptateurs bloquants : ORC `pole/adaptateurs.py`, l. 439 (`asyncio.run`), l. 735 (`communicate`) ; `adaptateur_kimi_v53.py`, l. 126.

**Ce que cela change** : aucun changement. Le terme « appels en vol » de l'arrêt n° 12 vaut zéro et reste écrit.

### Q12 — Les gardes héritées du noyau ; ce qu'elles font à une « réponse vide motivée » ; un rôle arrêté sans bruit ?

**Réponse fermée : oui, un proposeur peut être arrêté sans arrêt nommé de la course (A3), et une part de réponses vides au-dessus de 34 % arrête toute la course (A14 → nœud). Une « réponse vide motivée » est comptée comme échec dès qu'elle ne porte pas de bloc `{"fiches": …}`.**

Valeurs de la configuration v5 (l. 246-253) : `a3_echecs_consecutifs` 3 ; `a3_delai_s` 1800 ; `a14_part_max` 0,34 ; `a11_modeles` vide. Le suivi est neuf à chaque génération (ORC `pole/noyau_v54.py`, l. 54 ; PQ `course2_v68.py`, l. 329).

| garde | où | effet sur une réponse vide motivée | bruit |
|---|---|---|---|
| échec compté | ORC `pole/noyau_v56.py`, l. 178-181 ; `suivi_roles_v54.py`, l. 72-77 : « `elif not exploitable: motif = f"sortie inexploitable (statut {statut})"` » | sans bloc `fiches` : `lu = None`, échec ; avec `{"fiches": []}` : liste vide, **exploitable**, pas d'échec (Q6) | événement « appel-inexploitable » |
| A3, échecs consécutifs | `suivi_roles_v54.py`, l. 82-83 : « `elif r["consecutifs"] >= self.echecs_max: r["arrete"] = …` » ; `noyau_v56.py`, l. 155-160 | trois réponses vides de suite (sur trois cases, la boucle étant case par case) : le proposeur est arrêté pour le reste de la génération ; ses appels suivants sont sautés | **aucun arrêt nommé** : un événement « appel-saute-role-arrete », le compte `appels_sautes`, l'état du suivi au manifeste de fin ; la course continue ; les 55 appels ne sont pas joués |
| A3, délai | `suivi_roles_v54.py`, l. 61 et 69-71 | un appel de plus de 1 800 s est un échec et sa réponse n'est pas lue, même complète ; le délai d'une session `claude_sdk` est 3 600 s (`adaptateurs.py`, l. 57) | idem |
| A14, part d'inexploitables | `noyau_v56.py`, l. 272-278 : « `res = self.budget.marquer_technique(nom, motif)` » ; `suivi_roles_v54.py`, l. 86-89 | au-delà de 34 % d'appels inexploitables d'un rôle sur la génération, l'étape devient « non mesurée (technique) » | **bruyant et total** : C13 fausse, nœud (`noyau_v54.py`, l. 146-154), la génération n'ouvre rien (`course2_v56.py`, l. 348-353), la course s'arrête (PQ `course2_v68.py`, l. 341-343 et 379-380) |
| A11 | `suivi_roles_v54.py`, l. 63-67, 80-81 | inactive : liste vide | — |
| A2, modèle servi absent ou changé | `noyau_v56.py`, l. 176-185 et 205-211 | ne touche pas la réponse vide ; une réponse « ok » sans modèle servi arrête le rôle | arrêt du rôle seulement, événement « arret-role-a2 » ; course continue |
| coupure au plafond du relais | `noyau_v56.py`, l. 150-154 | ne touche pas la réponse vide ; reste nul : appel non lancé, étape coupée | protégée coupée → « non mesurée (budget) » → nœud |
| 11a | `noyau_v56.py`, l. 228-236 et 280-282 | ne la touche pas | arrêt de l'exécution |
| garde « Kimi » (S12) | ORC `pole/course2_v54.py`, l. 172-183 ; `noyau_v54.py`, l. 275-300 | ne la touche pas ; mais elle s'applique à tout fournisseur nommé `kimi` : plus d'un quart de ses fiches classées « concret » par le portier arrête son rôle de proposeur | arrêt du rôle, événement marqué nœud |
| portier qui ne rend pas de classe | `noyau_v54.py`, l. 237-246 | la fiche est classée « concret », sans passeport ; l'appel du portier compte comme échec (A3, A14 sur le rôle du portier) | A14 sur le portier → nœud |

**Ce que cela change** : lot 6 (classe de génération) et additif. A3 et A14 contredisent V9, l. 97 et 101 et les 55 appels figés (CL, 2.1). Chaque garde doit être rattachée à un arrêt de la V9 ou rendue inerte par une valeur déclarée (par exemple A3 au-delà de 55, A14 à 1), ou la réponse vide motivée doit être lue comme exploitable par le lecteur de fiches neuf. La garde « Kimi » se neutralise en ne nommant aucun fournisseur `kimi` ou par `debordement_max` déclaré. Le délai A3 (1 800 s) est sous le délai de session du kit (3 600 s) : à aligner.

### Q13 — Un envoi refusé par l'adaptateur gardé est-il compté au plafond de l'appel ? Où ce coût entre-t-il ?

**Réponse fermée : oui, s'il est refusé par une exception levée dans `lancer` : le plafond entier de l'appel est compté, marqué « coût inconnu », statut « exception ».**

- ORC `pole/noyau_v56.py`, l. 161 (`plafond = min(float(self.ps[plafond_role]), reste)`) ; l. 163-175 : « `finally: … cout = plafond if cout is None else cout ; etat["cout"] += cout ; self.coffre.noter_consommation(…)` ». Il n'y a pas de `except` : l'exception remonte ensuite.
- Cumuls où il entre, dans l'ordre :
  1. `etat["cout"]` de l'étape (l. 171) ;
  2. `BudgetV56.cumul` par `apres_etape` (`noyau_v56.py`, l. 271 ; `budget_v56.py`, l. 206) ; s'il dépasse le plafond dur, l'étape est coupée (`budget_v56.py`, l. 209-217) ;
  3. le coffre, puis `consommations.json` (`course2_v56.py`, l. 325-328), que relit le second programme de 11a (`budget_v56.py`, l. 258-261) ;
  4. `GardeBudgetCourseV68` par `noter_arret` (PQ `course2_v68.py`, l. 333-335 ; PQ `budget_course_v68.py`, l. 96-108), puis le bilan de course ;
  5. la lecture des coûts du lanceur (L9, l. 2421-2433), et M4 si M4 lit ces consommations.
- Et l'exception arrête la génération puis la course (`course2_v56.py`, l. 369-371 ; PQ `course2_v68.py`, l. 371-373).
- Si l'adaptateur gardé rend plutôt un résultat non « ok » à coût nul, le coût compté est nul, mais le suivi compte un échec (A3, A14 : `noyau_v56.py`, l. 180-181).

**Ce que cela change** : lot 4 et CO, § 2.3 (CL, 2.2). Aucune des deux voies n'est neutre dans le noyau tel qu'il est. La voie propre est de refuser **avant** l'appel du noyau, dans la surcharge d'`appel` de la classe neuve (voir Q2), avec la ligne de journal « non envoyé » et aucune consommation notée. Phrase à écrire au § 2.3 : « un refus des pas 1 à 5 ne passe pas par `lancer` ».

### Q14 — Le lanceur v9 : structure, points d'entrée, ce qui est propre à la v9, ce qui serait repris

**Réponse fermée : un seul fichier de 2 944 lignes, bibliothèque standard, trois points d'entrée ; une large part est propre à la course v9 (liste ci-dessous, par plages de lignes).**

- Lecture : corps lus aux l. 1-120, 300-569, 1797-2075, 2223-2944 ; les autres plages ci-dessous viennent de la liste des fonctions (`grep -n "^def \|^class "`), non de leur corps.
- Points d'entrée : L9, l. 2920-2940 : sans argument, `executer(Reglages.production())` ; `--a-blanc DOSSIER` (`reglages_a_blanc`, l. 2821-2904) ; `--decouper MATIERE DOSSIER` (l. 2907-2917). Codes : 0 ; 2 refus ou erreur ; 3 alerte de crédit ; 4 plafond d'arrêt dépassé ; 5 arrêt au premier refus pour crédit (l. 2809-2815, 2932-2940).
- Déroulé de `executer` (l. 2575-2815) : pièce de départ → une seule course → clé présente → ligne d'accord → mot de reprise → préenregistrement, pièces, additif, contre-lecture → configuration fixe et seuils → matière et lots → épreuve des témoins → sondes → déclaration des relais → réglages des enveloppes Gemini → pire cas → parts et crédits → procédure des relais → relevé de prix → orchestrateur → environnement filtré, bac à sable → dossier du run → enveloppes → acte de gel → configuration assemblée → vérification par l'orchestrateur (`--verifier-seulement`) → porte à blanc → sortie créée → manifeste de départ → lancement de l'orchestrateur, relais des signaux, arrêt par identifiant de processus au premier refus pour crédit (l. 2754-2756) → coûts, relevé après, inventaire de fin, alertes, manifeste de fin.
- **Propre à la v9, à retirer** : matière et lots (l. 651-825, 1448-1473, 1699-1707, 2907-2917) ; courses closes admises et mot de reprise (l. 356-362, 905-966) ; clé Claude unique et ses refus (l. 446-452, 1843-1847) ; sondes et réglages Gemini et OpenAI (l. 1242-1698) ; épreuve v9 et ses pièces (l. 1708-1776) ; Kimi (l. 1906-1917, 2104-2111) ; devis v2 et écart au devis (l. 519-528, 2441-2453) ; seuils au haut du devis (l. 2293-2340) ; acte de gel de cette course (l. 2368-2380) ; `--generations 1` et « une seule génération » (l. 2656, 2264) ; lectures de la seule `generation-1` (l. 2418, 2478, 2484, 2498).
- **Repris** : `verifier_go`, registre dérivé (l. 967-1045) ; préenregistrement, additif, contre-lecture, pièces (l. 1046-1165) ; `verifier_orchestrateur` (l. 2242-2257) ; `environnement_filtre`, `sonder_bac_a_sable` (l. 2386-2411) ; `envelopper_commandes` (l. 2223-2236) ; `controler_relais_vivant`, procédure des relais, porte à blanc (l. 1919-2103, à adapter aux noms neufs et aux parts) ; `verifier_credits`, `releve_apres` (l. 2134-2207, 2456-2472, à adapter à l'arrêt n° 11) ; `inventorier`, `base_des_sessions` (l. 2496-2553) ; `_depot_git`, `_versions` ; le squelette de `executer` (manifestes, signaux, arrêt par identifiant).
- **Lieu de fuite dans L9 même** : l. 2667-2669 : « `raise Refus(f"vérification de l'orchestrateur refusée (code {verif.returncode}) : " f"{(verif.stderr or verif.stdout).strip()[-800:]!r}")` », imprimé sur la sortie d'erreur par `principal` (l. 2935-2937). C'est le lieu que CO, § 2 situe en L10, l. 2998-2999 ; il est en L9 aux mêmes octets.

**Ce que cela change** : lot 8, comme CL, 3.1 le demande : un différentiel lisible contre L9. La liste « retirée, gardée, ajoutée » ci-dessus en est la base. Le lieu de fuite à fermer est L9, l. 2667-2669 (et non seulement L10). Les `Reglages` (l. 826-879) portent les chemins de production et doivent être réécrits.

## Ce qui contredit la conception

1. **§ 2.3, l. 103 (lot 4)** : l'adaptateur gardé ne reçoit ni le rôle, ni la génération, ni la case ; le portier et les juges partagent le même `role_kit`. Le routage par rôle et la ligne de journal ne se tiennent pas « sans changer l'appel du noyau » : il faut une surcharge d'`appel` dans une classe neuve (Q2).
2. **§ 2.3, l. 116 et § 9, point 2 ; CL, 2.3 (lots 3 et 4)** : le texte fixe de rôle existe (`claude_sdk` seul), le portier reçoit celui du juge, et aucun réglage ne le retire : il faut un adaptateur Claude neuf. Ce que l'outil du kit ajoute n'est pas lisible ici (Q1).
3. **§ 2.3, pas 6 ; § 6.1, n° 13 (lot 4)** : le statut ne distingue pas le refus pour crédit, l'erreur d'accès et la réponse coupée ; pour les clés Claude, le refus pour crédit ne se lit qu'au relais (Q5).
4. **§ 2.3 ; CL, 2.2 (lot 4)** : un refus levé dans `lancer` est compté au plafond entier et arrête la course ; rendu à coût nul, il compte un échec A3 et A14 (Q13).
5. **§ 1.2 (lot 8)** : l'enveloppe de conservation de L9 ne couvre pas les deux clés Claude (Q10).
6. **§ 2.9 (lot 6)** : « trois étapes et aucune autre » demande de surcharger `verifier_configuration` et `executer` ; la v5 garde six étapes neutralisées (Q3). **§ 1.2** : la mémoire anti-redite tourne encore dans `executer` (Q4).
7. **§ 2.4, § 5.4 (lot 5)** : `preparer` refuse un champ nommé `case` (et neuf autres noms), accepte un champ en trop, caviarde ; `fiches_du_texte` ne lit qu'un bloc JSON `{"fiches": …}` (Q6).
8. **Q12, contre V9, l. 97 et 101** : A3 arrête un proposeur sans arrêt nommé après trois réponses vides sans bloc ; A14 au-delà de 34 % arrête toute la course.
9. **§ 1.2, reprise de L10 (lots 7 et 8)** : `couts_generation` ne lit que des totaux, rien par espèce ni par rôle (Q8).
10. **§ 2.3, table des rôles et des clés (lots 4 et 6)** : le noyau exige des adaptateurs pour les lecteurs d'étiquettes et le metteur en fusion, jamais appelés (Q2).
11. **À trancher, § 9, point 3 (lot 5)** : l'identifiant de fiche du noyau est `f` suivi de 12 caractères hexadécimaux (PQ `course2_v68.py`, l. 203 ; `graines_v53.py`, l. 65-67), et l'identifiant servi au juge `F` suivi de 10. Servi comme « nom » au registre, il porte une suite de plus de huit caractères hexadécimaux : si la contrainte de V9, l. 75 vaut pour tout texte servi, le registre servi ne peut pas reprendre cet identifiant.
12. **§ 2, règle commune** : le lieu de fuite à fermer est aussi dans L9, l. 2667-2669 (Q14).

## D2 : ce qu'il faut retirer pour que rien ne soit ajouté à l'enveloppe

1. **À retirer** : le texte système de `claude_sdk` (`adaptateurs.py`, l. 101-111, posé l. 338-339), pour les proposeurs des deux clés Claude, le portier et le juge. Moyen : un adaptateur Claude neuf (fichier neuf) qui ne pose aucun texte système. Puis établir au faux fournisseur ce que l'outil du kit envoie alors, et le déclarer à l'additif comme transport, ou le refuser.
2. **À ne pas reprendre du noyau** pour le proposeur : `rstrip()`, la section `## Case`, la section d'héritage de la v68 (PQ `course2_v68.py`, l. 190-194). Le module `requete` du lot 3 les remplace.
3. **À déclarer octet pour octet, ou à remplacer par du code neuf**, pour le portier et les juges : `## La fiche`, la clôture de bloc JSON, l'indentation d'un espace et la clé `identifiant` (`fiches_v54.py`, l. 48-61 ; `noyau_v56.py`, l. 198-199). Sous D2 au sens strict, ils sont à retirer : la fiche doit alors suivre la consigne dans la forme que l'additif fixe.
4. **Rien à retirer** pour les commandes externes et pour `kimi_protocole` : aucun texte n'est ajouté ; les réglages (`generationConfig`, `max_tokens`, `max_completion_tokens`, `stream`) sont du transport non textuel, à nommer à l'additif. La seule condition : ne jamais passer `--recherche-web` (commande Gemini, l. 713, 861-862).

— développeur du lot 0, modèle O
