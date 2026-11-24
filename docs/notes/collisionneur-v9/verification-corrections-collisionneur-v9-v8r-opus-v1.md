# Vérification des corrections du v8q : moteur v9-v8r, voie abonnement v8, script de vague v4 — Opus 5.5 (v1)

- 24 novembre 2026, vers 22:40Z. Même contre-lecteur que la contre-lecture du v8q (`contre-lecture-collisionneur-v9-v8q-opus-v1.md`, `c22da939…`). Classe B, vérification des corrections.
- Pièces vérifiées, commit `1222fcf6` :
  - `collisionneur_v9_v8r.py` (`1656351a…`) ;
  - `test_collisionneur_v9_v8r.py` (`47049da4…`) ;
  - `mutations_collisionneur_v9_v8r.py` (`4f0edcf3…`) ;
  - `abonnement-v1/voie_abonnement_v8.py` (`98f1a1d6…`) et `abonnement-v1/test_voie_abonnement_v8.py` (`966c553e…`) ;
  - `reprise-v8d-v1/vague_abonnement_v4.sh` (`7819b2aa…`) ;
  - le rapport `rapport-developpeur-collisionneur-v9-v8r-v1.md` (`75b59995…`).
- Rien n'est parti vers un fournisseur. Je n'ai lancé ni vague, ni étage hors des essais. Aucune valeur de clé n'a été lue ni affichée.
- Toutes mes exécutions ont tourné sous un espion de processus, décrit en section 3. Il n'a relevé aucune tentative de réseau. Les dossiers des vagues n'ont été touchés qu'en copie ; les originaux sont intacts (empreintes de tous leurs fichiers comparées).

## Verdict : conforme avec réserves

- Les onze défauts sont corrigés, ou déclarés là où le rapport le dit.
- Les trois différences se limitent à ce que le rapport annonce.
- Les essais sont étanches au réseau : aucune tentative relevée, ni dans les 22 et 5 essais, ni dans la campagne du développeur (16 mutations sur 16 tuées), ni dans la mienne.
- Ils tuent toutes mes mutations du v8q, y compris deux formes qui échappent à la lecture de l'arbre syntaxique.
- Restent cinq réserves mineures, sans défaut majeur :
  - deux gardes neuves éprouvées d'un seul côté (le refus de la voie n'a pas de cas sain ; le contrôle du préfixe au moment de l'envoi n'a pas d'artefact) ;
  - un artefact trop étroit pour le refus de l'espace d'Anthropic ;
  - deux commentaires hérités qui disent encore « clé épuisée » ;
  - la forme abrégée `--cle-gem`, qui échappe au refus de la voie.
- Une réserve d'exploitation, pour la mère (section 5).

## 1. Empreintes et différences

- **Empreintes.** Les sept pièces neuves et le rapport ont des compagnons conformes.
  - Les pièces précédentes sont intactes : v8q `047489b8…`, voie v7 `fd1c37b7…`, script v3 `51c27240…`, ainsi que le v8m, la voie v6 et le script v2.
  - Ma contre-lecture a été versée sans changement (`c22da939…`).
  - La table `MOTEURS` de la voie v8 porte l'empreinte entière du v8r (`1656351ace2a…`), et le v8q n'y figure plus.
- **v8q → v8r** : exactement les points (1), (4), (5), (6) et (7) de l'en-tête et du rapport, rien d'autre :
  - `cle_gemini` et les trois lectures qui l'emploient ;
  - `NOMS_CLE_GEMINI_RESTREINTS` et son refus ;
  - le refus de préfixe pour `--nom-espace-anthropic` ;
  - le motif du refus de `GEMINI_API_KEY_3` ;
  - l'en-tête et la docstring du journal ;
  - `VERSION`.
- **Voie v7 → v8** : l'en-tête, `VERSION`, le v8r à la place du v8q, les deux listes de commandes, et le refus de `--cle-gemini` hors du v8r (l. 426-429). Rien d'autre.
- **Script v2 → v4** (et v3 → v4) : l'en-tête refait et l'appel de la voie v8. Rien d'autre.
  - Le fichier est en mode 644, comme l'était déjà la v3 dans git. C'est sans effet avec `bash …`.

## 2. Les onze défauts

| défaut | réponse | constat |
|---|---|---|
| 1. Repli silencieux | corrigé | `cle_gemini` (l. 1826-1831) passe par `cle_par_son_nom`, sans repli ; les trois lectures l'emploient. Sans nom dans la composition, rien ne part (essai et mutations C2, C2b tuées). |
| 2. Essais non étanches | corrigé, question éclaircie | Tout tourne dans le même processus, les deux transports coupés, et les essais de refus exigent zéro requête. Le rapport déclare qu'une requête de comptage avec la valeur factice est très probablement partie pendant la campagne du v8q. |
| 3. Couverture | corrigé | Les essais (a) à (f) existent. L'ancien contrôle textuel est remplacé par une lecture de l'arbre syntaxique. Toutes mes mutations du v8q sont tuées (section 3). |
| 4. Clé libre | corrigé | Cas sain et artefact (section 4). R-5294 est confirmé dans la copie locale de `origin/main`, `registres/decisions.md` l. 5438 : « GEMINI_API_KEY_FREE pour Carbon et Neon (protocole X, bancs plantés, dossiers suivants) ». |
| 5. Espace d'Anthropic | corrigé, choix déclaré | Cas sain et artefact ; l'artefact est étroit (section 4). |
| 6. Motif « épuisée » | corrigé en partie | Le message, l'en-tête et le commentaire de la constante sont corrigés. Deux commentaires hérités disent encore « clé épuisée » : l. 529 et l. 1125 (réserve 4). |
| 7. Journal mal décrit | corrigé | L'en-tête (l. 17-19) et la docstring (l. 3358-3360) sont alignés sur le code. |
| 8. Script v3 et code 2 | corrigé pour les formes écrites | L'en-tête du v4 est juste. La voie v8 refuse `--cle-gemini` et `--cle-gemini=…` hors du v8r au code 1, avant tout chargement : l'essai passe même pour le v8p et l'essaim, absents de cette branche. La forme abrégée échappe au refus (réserve 5). |
| 9. Voie sans essais | corrigé | 5 essais. Les essais de la v6 ne sont pas recopiés ; c'est déclaré. |
| 10. Nom fixe hors du v8r | déclaré | Dans l'en-tête de la voie v8 et dans celui du script v4. |
| 11. Docstring des essais | corrigé | Par la commande documentée, chaque script se relance dans un environnement vidé ; aucune valeur réelle n'est lue. |

## 3. Essais, étanchéité, mutations

- **Espion de processus.**
  - Un `usercustomize.py`, placé en tête de `PYTHONPATH`, remplace `socket.connect`, `connect_ex` et `getaddrinfo`. Il note toute connexion et toute résolution de nom, puis les refuse.
  - Il ne masque pas le `sitecustomize` du système, et `PYTHONPATH` survit à la relance des essais.
  - Il était chargé dans chaque processus (une ligne « espion chargé » par processus).
  - Éprouvé avant usage, il attrape les deux voies de sortie : le mandataire de la session, qui écoute en local (d'où le refus de la boucle locale aussi), et la résolution directe dans un environnement vidé.
- **Commandes du rapport**, lancées telles quelles, espion en tête de `PYTHONPATH` :
  - essais du moteur : 22 sur 22 ;
  - essais de la voie : 5 sur 5 ;
  - campagne du développeur, sous `env -i` : 16 mutations tuées sur 16.
  - L'espion était chargé dans 5 processus (4 pour les deux scripts et leurs relances, 1 pour la campagne) et n'a relevé **aucune tentative**.
- **Mes mutations, rejouées contre les essais du v8r** : sous `env -i`, avec un mutant au transport coupé en plus des essais, un témoin non muté (aucun échec) et l'espion (aucune tentative).

| mutation | issue |
|---|---|
| C1 nom hors du contrôle de forme | tuée (`test_refus_nom_mal_forme`) |
| C2 comptage : repli sur `NOMS_CLES["gemini"]` | tuée (trois essais) |
| C2b comptage : repli par `PREFIXE_CLE_GEMINI`, invisible à la lecture syntaxique | tuée (deux essais de comportement) |
| C3 relevé : `os.environ["GEMINI_API_KEY"]` | tuée (lecture syntaxique et lot complet) |
| C4 création : `NOMS_CLES["gemini"]` dans l'en-tête | tuée (lecture syntaxique et lot complet) |
| C4b création : `PREFIXE_CLE_GEMINI`, invisible à la lecture syntaxique | tuée (lot complet) |
| C10 annulation : `os.environ["GEMINI_API_KEY"]` | tuée (lecture syntaxique et lot complet) |
| C5 valeur au journal ; C6 valeur à l'écran | tuées (`test_journal_et_ecran_ne_montrent_jamais_la_valeur`) |
| C7 défaut de la ligne de commande changé | tuée (nom exact du défaut) |
| C8 option lue mais non transmise | tuée (trois essais en ligne de commande, zéro requête) |
| C9 nom journalisé avant `--reprise` | tuée (`test_reprise_exigee_avant_tout_journal_du_nom`) |
| N3 préfixe non contrôlé au moment de l'envoi (`cle_gemini`, l. 1831) | **survit** (réserve 2) |
| N8 refus de l'espace d'Anthropic limité aux noms de Google (l. 1109) | **survit** (réserve 3) |
| V1 voie : `--cle-gemini` refusée même avec le v8r | **survit** (réserve 1) |
| V2 voie : v8m, v8p et essaim refusés même sans `--cle-gemini` | **survit** (réserve 1) |
| V3 voie : forme `--cle-gemini=NOM` non vue | tuée |

- **Reprise sous v8r**, rejouée sur des copies neuves des deux dossiers des vagues :
  - sans `--reprise`, arrêt au code 1 ;
  - ensuite, `verifier` rend 0 problème, sous v8r comme sous v8m ;
  - dépenses inchangées (14,6296 et 8,9492 USD) ;
  - devis de reprise identique, hors de sa ligne de version ;
  - les 8 kits déjà écrits sont reconstruits à l'identique.

## 4. Gardes neuves : un cas sain et un artefact chacune ?

- **Clé restreinte** (`GEMINI_API_KEY_FREE`) : oui.
  - Cas sain : Carbon et Neon, avec ou sans Fable.
  - Artefact : Argon et Carbon, refus qui nomme Argon.
  - La mutation qui retire la garde est tuée.
- **Espace d'Anthropic** : oui.
  - Cas sain : le défaut `ANTHROPIC_WORKSPACE_ID`.
  - Artefact : `GEMINI_API_KEY_2`.
  - La mutation qui retire la garde est tuée. L'artefact ne couvre cependant qu'un nom de Google, pas les autres préfixes de `PREFIXES_AUTRES_FOURNISSEURS` : N8 survit.
- **Les autres gardes nouvelles**, hors de la question posée :
  - le refus d'un nom interdit au moment de l'envoi a son cas sain et son artefact (mutation tuée) ;
  - le contrôle du préfixe au moment de l'envoi n'a pas d'artefact (N3) ;
  - le refus de `--cle-gemini` par la voie n'a pas de cas sain (V1, V2).
  - J'ai constaté à la main, en m'arrêtant à l'analyse des arguments, que le code de la voie est juste : le v8r avec `--cle-gemini` et le v8m sans l'option passent son contrôle.

## 5. Réserves et défauts nouveaux

Aucun défaut bloquant ni majeur. Tous les défauts ci-dessous sont mineurs.

**1. Mineur : le refus de la voie n'a pas de cas sain (R5).**
- Lieu : `voie_abonnement_v8.py` l. 426-429 ; `test_cle_gemini_refusee_hors_du_v8r` l. 115-121.
- Effet : une régression qui bloquerait la vague prévue (v8r avec `--cle-gemini`, V1), ou toute vague v8m, v8p ou essaim (V2), ne ferait tomber aucun essai. L'échec serait sûr (code 1, rien ne part), mais il ne serait vu qu'au lancement.
- Correction, deux cas sains par `v8.principal` :
  - v8r avec `--cle-gemini GEMINI_API_KEY_3` : le refus doit venir du moteur (« est refusée ») et non de la voie (« n'est admise qu'avec »), sans aucune requête ;
  - v8m sans l'option, arguments incomplets : code 2 de l'analyse du moteur, sans message de la voie.

**2. Mineur : le contrôle du préfixe au moment de l'envoi n'a pas d'artefact.**
- Lieu : `cle_gemini` l. 1831.
- Correction : injecter `m["nom_cle"] = "OPENAI_API_KEY"` sur les trois chemins, et vérifier « hors préfixe » et zéro requête.

**3. Mineur : l'artefact du refus de l'espace d'Anthropic est étroit.**
- Lieu : `test_espace_anthropic_ne_nomme_pas_une_cle_de_google` l. 162-167.
- Correction : parcourir un nom par préfixe de `PREFIXES_AUTRES_FOURNISSEURS` (OpenAI, Mistral, Kimi, Moonshot, Jev, en plus de Google).

**4. Mineur, reste du défaut 6 : deux commentaires hérités disent encore « clé épuisée ».**
- Lieu : l. 529 et l. 1125, juste au-dessus du message corrigé.
- Correction : un erratum, ou la prochaine version.

**5. Mineur, reste du défaut 8 : la forme abrégée échappe au refus de la voie.**
- La forme `--cle-gem`, qu'acceptent les analyseurs d'arguments, n'est pas refusée par la voie : le v8m rend alors de nouveau le code 2, confondu avec « porte fermée ». Je l'ai éprouvé en m'arrêtant à l'analyse des arguments.
- Lieu : `voie_abonnement_v8.py` l. 426.
- Correction : refuser tout argument qui commence par `--cle-g`. Aucune option du v8m, du v8p ni de l'essaim ne commence ainsi.

**Réserve d'exploitation, pour la mère.**
- R-5294 demande d'employer `GEMINI_API_KEY_FREE` pour Carbon et Neon. Or un seul nom vaut par lancement, et la garde refuse ce nom dès qu'Argon est dans la composition : c'est le cas des deux dossiers en cours.
- Pour ces dossiers, la seule clé de Google utilisable avec le v8r est donc `GEMINI_API_KEY_2`, pour les trois espèces. C'est conforme à la consigne de la mère du 24 novembre (`GEMINI_API_KEY_2`, ou la clé libre pour Carbon et Neon), mais la clé libre y reste inemployable.
- L'employer demanderait un nom par espèce, donc une version neuve.
- L'incident de la campagne du v8q (une requête de comptage partie, avec la valeur factice) est déclaré au rapport du développeur. Le consigner aux registres revient à la mère.

**Remarques sans défaut.**
- L'étanchéité tient par le remplacement des deux transports du moteur. Aucun chemin du moteur ne les contourne : je l'ai vérifié à la lecture, et l'espion le confirme. Une garde de processus dans les essais, comme mon espion, la rendrait vraie par construction.
- Lancés par pytest plutôt que par la commande documentée, les essais ne se relancent pas dans un environnement vidé. `Environnement` lit alors les valeurs réelles de Google pour les rétablir, sans les afficher ni les envoyer.
- La campagne du développeur ne joue pas de témoin non muté. La mienne en joue un, sans échec.

## 6. Ce que j'ai lancé (tout sans réseau, sous l'espion)

- Les trois commandes du rapport ; les différences ; les empreintes.
- Les fichiers du bloc-notes de la session, qui est temporaire :
  - l'espion : `/tmp/claude-0/-home-user-controle-ia-travail/12f6e278-4ba7-598c-9d00-941c25a1615c/scratchpad/espion-v8r/usercustomize.py` ;
  - mes mutations : `/tmp/claude-0/-home-user-controle-ia-travail/12f6e278-4ba7-598c-9d00-941c25a1615c/scratchpad/mutations_contre_lecteur_v8r.py` ;
  - la reprise et les kits sous v8r : `/tmp/claude-0/-home-user-controle-ia-travail/12f6e278-4ba7-598c-9d00-941c25a1615c/scratchpad/epreuve_reprise_v8m_v8r.py` et `/tmp/claude-0/-home-user-controle-ia-travail/12f6e278-4ba7-598c-9d00-941c25a1615c/scratchpad/epreuve_kits_v8m_v8r.py`.
- Deux sondes de la voie, arrêtées à l'analyse des arguments : la forme abrégée, puis les deux cas sains.
