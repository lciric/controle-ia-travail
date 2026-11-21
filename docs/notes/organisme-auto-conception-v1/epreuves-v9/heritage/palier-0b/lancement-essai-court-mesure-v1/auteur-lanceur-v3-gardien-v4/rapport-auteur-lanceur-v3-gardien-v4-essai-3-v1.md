# Rapport de l'auteur — lanceur v3 et gardien v4 de l'essai 3 du palier 0b — v1

Auteur neuf (modèle O). Je n'ai écrit ni le lanceur v2 ni le gardien v3.

**Ce qui fait foi :**
- le devis inscrit, GO-2026-11-21-73 : `devis-serveur-loue-palier-0b-essai-3-v5.md`, empreinte `452e7bcf…47fb`, relevée par `sha256sum` et égale à l'attendue, § 3 et § 4 ;
- le complément 1 v3 : extraction `pieces-v2/…-v2.md` lue sur origin/main par `git show` redirigé, copiée dans D/`complement.md`, empreinte `56ed20f8…b867`. Elle est égale à `auteur-v2/complement-1-v3-extraction-v2.md`.

**Pièces de départ :** lanceur v2, départ v2, vérificateur v2, gardien v3 (`d8fd650b…`), départ du gardien v3. Je les ai copiées à l'octet dans D/essais/copies/pieces-anciennes/.

**Lectures faites :** les rapports v1 à v3 de l'auteur, la contre-lecture v1, les vérifications v2 et v3.

**Dossier de travail (D) :** `/tmp/claude-0/-home-user-controle-ia-travail/d90e22c7-b755-5554-90ae-faa848d18eef/scratchpad/auteur-lanceur-v3-gardien-v4/`.

**Ce que je n'ai pas fait :**
- Je n'ai lancé que des factices, jamais le vrai programme. Le vrai fichier du programme a été copié depuis le dépôt de travail dans des copies factices, pour son empreinte seulement. Un interprète factice prend sa place à l'exécution.
- Je n'ai rien écrit sous `/home/user/palier-0b-racine/` ni sous `/home/user/journaux-palier-0b-essai-court-v1/`.
- Aucun appel à un fournisseur, aucune clé, aucune dépense.
- Aucun commit dans un dépôt du programme. Seuls des dépôts git factices, jetables, ont été créés sous D/essais et ont reçu un commit factice chacun. Ils servent aux essais de la forme « racine avec .git ».
- Je n'ai arrêté que mes factices, par leur identifiant.
- Aucun refus de permission, de classifieur ou de garde.

## Fichiers et empreintes (sha256 ; compagnon `.sha256` à côté de chacun)

| Pièce | Empreinte |
|---|---|
| `lancer-essai-3-v3.sh` | 9ba097c711537fe5f74c62370e377fed2b1e14e2d3714280e4ae091d5588b8f5 |
| `demarrer-essai-3-v3.sh` | 8473af508c8740ac13cbf4842873f92b3579e5db9f11992d9dc855033b17d806 |
| `verifier-commande-v3.py` | ca93ea3a4cc3daab764c6af423e2067a2af9cfe1dd0731c1a6a67593288a051e |
| `gardien-essai-3-v4.py` | ba39fe9be5d6fbf760e409d7677ed60662f6118103cb7bd75b93a6786d6246ed |
| `demarrer-gardien-essai-3-v4.sh` | b333b2eb4bac58c567e0a2efa479ae424dccc6fa9d88fe5a4d95011cb2ce6232 |
| `complement.md` (extraction lue) | 56ed20f89c3b9d9237350aeda092c815b6faee54b9048ba948659328d75bb867 |
| `consigne.md` (extraction lue) | d327b3fcbee59f37f833e83812a66ba8b28af72cdd5475772870612a2c9d23d8 |

Les essais sont dans D/essais/ (scripts, un compagnon chacun). Les sorties sont dans `essais/resultats/final-*.txt`, et leurs empreintes dans `essais/empreintes-resultats-v4.txt`. Rejeu : `bash essais/rejouer-tout-v4.sh SUF PARTIE`, parties 1 à 5. Chaque rejeu écrit d'abord les empreintes des pièces ; elles sont égales à celles de la table ci-dessus.

## Mode d'emploi sur le serveur

1. **Préparer la copie.** Copier la racine (copie de l'arbre du commit, sans `.git`), avec `COMMIT-DE-LA-COPIE.txt` et `EMPREINTES-DE-LA-COPIE.txt`. Ces deux fichiers sont fabriqués sur le poste par la commande écrite dans l'en-tête du lanceur.
2. **Contrôler avant le départ.** Lancer `lancer-essai-3-v3.sh TENUE_D_ESSAI RACINE INTERPRETE SORTIES --verifier-seulement`. **Le dossier de tenue doit être à part** : ce mode écrit `code-de-sortie.txt`, et un départ dans le même dossier serait ensuite refusé (code 4).
3. **Départ du programme.** Lancer `demarrer-essai-3-v3.sh TENUE RACINE INTERPRETE SORTIES`.
4. **Départ du gardien, aussitôt après.** Lancer `demarrer-gardien-essai-3-v4.sh TENUE INTERPRETE --sorties SORTIES --heure-arret-duree <H0 + 94 h>`. L'heure se calcule par `date -u -d "@$(( $(date -u -d H0 +%s) + 94 * 3600 ))" +%Y-%m-%dT%H:%M:%SZ` : cette commande est éprouvée, elle rend 2026-11-25T17:00:00Z pour H0 = 2026-11-21T19:00:00Z.

## Ce qui change

**Lanceur v3** (`lancer-essai-3-v3.sh`) :
- **Racine, interpréteur et sorties en paramètres**, chemins absolus exigés (code 2 sinon). La ligne `env -C` est celle du complément, où seuls les trois chemins deviennent `"$RACINE"`, `"$INTERPRETE"` et `"$SORTIES"`.
- **Refus de la v2 gardés** : 10, 11, 12 et 13, ainsi que 2, 3 et 4, avec les mêmes valeurs attendues `d7f949ac…` et `1f04cb46…`.
- **Racine sans `.git`** : le code 11 contrôle `COMMIT-DE-LA-COPIE.txt`. Le fichier doit être régulier, sur une ligne, et porter exactement le commit. Le code 12 contrôle `EMPREINTES-DE-LA-COPIE.txt` par `sha256sum --check --strict`, puis compare les comptes : lignes, chemins distincts, fichiers réguliers de la copie.
- **Racine avec `.git`** : contrôles de la v2, à l'identique.
- **Nouveau refus 14** : interpréteur absent, non régulier ou non exécutable.
- **Mode `--verifier-seulement`** : les valeurs d'emploi sont gardées par défaut. TETE et EMPREINTE ne peuvent être remplacées que dans ce mode, et la commande n'y est jamais exécutée.

**Départ v3** (`demarrer-essai-3-v3.sh`) :
- La forme d'emploi prend exactement 4 arguments ; la forme d'essai est `--lanceur L TENUE …`.
- Les fichiers sont suffixés `essai-3`. Le reste est identique à la v2.

**Vérificateur v3** (`verifier-commande-v3.py`) :
- Il lit les trois chemins dans la ligne du complément : 9e, 5e et 11e mots.
- Il construit la ligne attendue du lanceur et la compare à l'octet.
- Il refuse aussi qu'un des trois chemins du complément reste écrit tel quel dans la ligne du lanceur.

**Gardien v4** (`gardien-essai-3-v4.py`) : trois changements, et rien d'autre (diff relu en entier).
- (A) **Arrêt de durée**, `--heure-arret-duree`, obligatoire :
  - format strict AAAA-MM-JJTHH:MM:SSZ, puis date réelle ;
  - contrôlé après l'arrêt de place, sur l'heure murale relue ;
  - même voie que les autres arrêts (`arreter`), raison « arrêt de durée » écrite avec l'heure lue et l'heure visée ;
  - refus de départ (code 2) si l'heure est mal formée, ou située plus de 94 h 10 min après la prise de garde.
- (B) **Arrêt de mesure** : `--arret-mesure desarme|arme`, désarmé par défaut.
- (C) **Noms et chemins de l'essai 3** :
  - suffixe `essai-3` pour le journal de tenue, les fichiers pid, pgid, boot-id et depart-processus, le fichier de mesure et les inventaires, comme dans le complément 1 v3 ;
  - `--tenue` et `--sorties` obligatoires.
- Ajout : `--verifier-seulement`, qui contrôle les paramètres sans rien lire ni écrire.
- L'arrêt de place est inchangé.

**Départ du gardien v4** (`demarrer-gardien-essai-3-v4.sh`) :
- l'interpréteur passe en paramètre ;
- les paramètres sont contrôlés au premier plan avant le départ détaché ;
- les noms suivent l'essai 3.

## Table des essais (rejeu `final`, de 18:34:16Z à 18:44:55Z, pièces aux empreintes ci-dessus)

| Partie | Essai | Objet | Attendu | Rendu |
|---|---|---|---|---|
| Lanceur, vérification | 36 cas (`final-1-refus.txt`) | Racine `.git` factice : sain, sorties existantes, tête fausse, tête d'emploi, empreinte fausse, fichier suivi modifié, non suivi seul, racine absente. Copie sans `.git`, valeurs d'emploi : saine ; sans fichier de commit ; commit faux, abrégé, sur deux lignes, sans fin de ligne, en lien ; liste absente ou vide ; fichier modifié, manquant, ajouté ; programme altéré (liste refaite) ; `.git` parasite. Interpréteur absent, non exécutable, dossier. Chemins relatifs, usages, code déjà présent, tenue absente | 0 / 10 / 11 / 12 / 13 / 14 / 2 / 3 / 4 selon le cas ; sorties jamais créées | **36/36 TENU** |
| Lanceur, emploi | 6 cas (`final-1-emploi.txt`), vrai départ v3 détaché | Sain ; sans fichier de commit ; commit faux ; interpréteur absent ; sorties existantes ; fichier de la copie modifié | Codes 0, 11, 11, 14, 10, 12 ; interprète appelé dans le seul cas sain | **6/6 TENU** |
| Commande, dynamique | `final-1-argv.txt` : vrai lanceur en emploi, interprète factice qui enregistre | Deux copies, l'une à un chemin avec espace, sorties avec apostrophe | Dossier courant, PYTHONPATH et arguments égaux à l'attendu calculé de la seule ligne du complément (`argv-attendu-v4.py`) | **ÉGAL** (2/2) |
| Commande, statique | `verifier-commande-v3.py` | Lanceur v3 ; altérés (un octet d'option, un octet de chemin, argument en trop, deux lignes, chemin codé, guillemets ôtés, variable renommée) ; ligne du complément prise pour un lanceur | 0 ; 1 pour chaque altéré | **0 ; 1 × 8** ; aucune altération nulle |
| Gardien, heure | `final-1-lire-heure.txt`, 19 cas | Quatre acceptés, valeurs calculées à la main (0 ; 1 795 219 200 ; 1 795 626 000 ; 29 février 2028) ; 15 refus (format `date -u` par défaut, sans Z, espace, 31 novembre, 24 h, 29 février 2027, vide, fraction, décalage, minuscules, espace en tête, fin de ligne, chiffres pleine chasse, 60 min, mois 13) | Valeurs exactes ; ValueError | **19/19 TENU** |
| Gardien, départ | `final-1-heure-depart.txt`, 15 cas, vrai départ v4 | Acceptés : +1 h, +94 h, +94 h 09 min, heure passée. Refus : +94 h 11 min, +31 jours, format par défaut, sans Z, espace, 31 novembre, vide, absente, décalage, `--arret-mesure oui`. Commande H0 + 94 h | Code 0 ; ou code 2 sans pid, sans sortie, sans journal ; témoin intact | **15/15 TENU** ; témoin vivant jusqu'à son arrêt par moi |
| Gardien, rejoué | Projections v1 (5) et v2 (5) | Valeurs à la main | Égales | **0 échec** |
| Gardien, rejoué | Colonne d'arrêt (`essai-arret.py`) | Lien brisé, profondeur 6, dossier ; noms voisins | Comptés ; voisins non comptés | Conforme (lien, profondeur 6, dossier) |
| Auteur v1 rejoué (arrêt de mesure **armé**) | s1 à s9 (`final-2-*.txt`) | s1, s3, s5 sains ; s2 place ; s4 n ; s6 durée de l'étape 4 ; s7 sourd (seuil n 2, délai 60 s) ; s8 n = 1 ; s9 groupe faux | Sains : aucun arrêt. Artefacts : arrêt, mesure, arrêt forcé, « projection impossible », aucun signal | s1, s3, s5 : code 0, aucun arrêt. s2 : arrêt de place (143). s4 : n = 13, figé. s6 : durée, n = 6. s7 : arrêt forcé du groupe à 60 s, tous absents. s8 : « projection impossible ». s9 : « aucun signal… groupe écrit 3999999 ». |
| Contre-lecture rejouée | h1, h3, h4, c2-sain | Enfant hors groupe avec témoin ; rapide ; sourd dans le groupe ; docile | Arrêt par identifiant, figé ; arrêt forcé (h4) ; témoin intact | Conforme : h1, descendant 14111 par identifiant, témoin vivant ; h3, n 774 figé ; h4, arrêt forcé du groupe ; c2, pas d'arrêt forcé |
| Identité rejouée et étendue | decoy ABSENT, −7, 0 (place, et **durée** : nouveauté) ; fichiers périmés | Faux : heure absente, décalée, périmée. Vrai : heure exacte | Faux : aucun signal, témoin vivant. Vrai : signal | Conforme pour les deux déclencheurs : ABSENT et −7, aucun signal, témoin vivant ; 0, signal, témoin arrêté par le gardien ; périmés, aucun signal |
| Auteur v2 rejoué | c5 sain et artefact ; c6 sain et artefact | Contenu du manifeste ; colonne d'arrêt | Mêmes décisions ; empreinte de l'inventaire égale à `sha256sum` ; « aucun » contre « oui » | Conforme : 345d7a…a277 = `sha256sum` (artefact), 041964…061d (sain) ; c6, « aucun » contre « oui (1 : …/arret-factice.txt) » |
| Vérification v2 rejouée | sourd-groupe, sourd-hors, docile-hors, chef-tue, orphelin, rapide | — | Comme en v3 | Conforme. Orphelin : « NON figé » (n 55 puis 60), orphelin arrêté ensuite par moi |
| Erratum 2 rejoué | e2c1 sain, place (témoin), mesure, sourd ; écrivain externe | — | Comme en v3 | Conforme. Place : seuil factice ; descendants par groupe porteur ; témoin vivant. Écrivain : « NON figé », projection préfixée |
| **Nouveauté A, cas sains** | d1 (heure +1 h), d1b (heure +25 s, programme fini à environ 6 s), avec témoin | Heure non atteinte pendant la vie du programme | Aucun arrêt, code 0, aucun `arret-gardien.txt` | **Conforme** |
| **Nouveauté A, artefacts** | d2 (+8 s, sans fin, témoin) ; d2b (sourd) ; d2c (chef tué à 3 s, descendant vivant) ; d2d (heure passée de 60 s) ; d2e (enfant hors groupe sourd) ; d2f (enfant sourd dans le groupe) | Heure atteinte | « arrêt de durée » écrit avec l'heure ; arrêt par la voie commune ; témoin intact | **Conforme partout** : d2, signal au groupe, 143, tous absents, témoin vivant ; d2b, arrêt forcé du groupe à 5 s ; d2c, mode descendants, groupe porteur ; d2d, arrêt au premier tour ; d2e, SIGTERM puis SIGKILL par identifiant ; d2f, arrêt forcé du groupe. Écart de l'arrêt à l'heure visée : moins d'un intervalle (d2 : 46,658 s pour 46 s) |
| **Nouveauté B, sans arrêt (désarmé)** | m1 (défaut), m1b (`desarme` explicite) : seuil n 5, durée de l'étape 4 2 s, n jusqu'à 30 ; m1c : valeurs d'emploi, n jusqu'à 40 > 13 | n au-delà du seuil, durée dépassée | Aucun arrêt, aucune mesure, code 0 | **Conforme** : journal vivant à n = 27 > 5 pendant environ 9 s ; aucun arrêt |
| **Nouveauté B, témoin armé** | m2 : mêmes réglages, `--arret-mesure arme` | Même objet, mécanisme armé | Arrêt de mesure et fichier de mesure | **Conforme** : n = 7, figé, `mesure-essai-3.txt` écrit |
| **Arrêt de place gardé** (désarmé) | p1, seuil impossible, témoin ; p1b, valeurs d'emploi (8 Go) | — | p1 : arrêt de place ; p1b : aucun arrêt | **Conforme** |

## Écarts

1. **Noms de l'essai 3.** C'est hors de la lettre « tout le reste inchangé ».
   - Changé : les fichiers de tenue passent de « essai-court » à « essai-3 », et `--tenue` et `--sorties` deviennent obligatoires.
   - Raison : le complément 1 v3 nomme `journal-essai-3.txt` et `journal-de-tenue-essai-3.txt`, et les chemins d'emploi codés en v3 n'existent pas sur le serveur.
   - Ce n'est qu'un changement de nom, par la constante `SUFFIXE` ; le diff est lisible en entier.
2. **Contrôle « sans modification » sur la copie.** Le devis ne nomme que le fichier du commit. Pour garder le refus 12 sans `.git`, j'ajoute `EMPREINTES-DE-LA-COPIE.txt`.
   - Conséquence : la **préparation du serveur** (devis § 4.3, à écrire) doit fabriquer ces deux fichiers par la commande de l'en-tête, depuis la copie extraite du commit sur le poste.
   - Les deux noms sont de mon choix : à confirmer ou à renommer par la session.
3. **Interpréteur du gardien en paramètre** du script de départ. En v3, il était codé pour ce conteneur.
4. **Refus 14 et chemins absolus** : ce sont des refus nouveaux (codes 14 et 2).
5. **Borne de 94 h 10 min** sur l'heure d'arrêt, garde contre une faute de frappe. Une heure passée est acceptée et arrête au premier tour : ne pas laisser le programme sans gardien m'a paru plus sûr.
6. **Format unique de l'heure.** Seul AAAA-MM-JJTHH:MM:SSZ est reçu, c'est-à-dire `date -u +%Y-%m-%dT%H:%M:%SZ`, l'usage du programme. La sortie par défaut de `date -u` est refusée, et ce refus est éprouvé (h3).
7. **Essais non rejoués.**
   - `orphelin-lent` de la vérification v3 : sa pièce lente n'est pas archivée. La réserve qu'il démontre porte sur la partie inchangée (preuve de gel en une seconde) ; elle reste entière.
   - Les essais v1 de `fabriquer-lanceur-factice` : le lanceur v3 n'a plus de constantes de racine. Je les ai remplacés par le vrai lanceur, sans modification, sur une copie factice qui porte le vrai programme.
8. **Commits factices.** Des commits ont été faits dans des dépôts git jetables sous D/essais : `a-refus-1/racine-git` et `a-final-1/refus/racine-git`. Ils servent aux refus de la forme « racine avec .git ». Ce ne sont pas des commits du programme.

## Limites

- **Forme `.git` jamais éprouvée en emploi.** Une tête `d7f949ac` ne se fabrique pas. Les refus de cette forme sont éprouvés en vérification seulement, avec une tête factice.
- **Granularité de l'arrêt de durée.** Il part au premier tour après l'heure, donc au plus un intervalle (60 s) plus la durée d'un relevé après H0 + 94 h. Si l'identité n'est pas confirmée, aucun signal ne part (comme pour les autres arrêts) ; la destruction à H0 + 98 h par le poste reste le seul arrêt.
- **Arrêt de durée et heure murale.** Il dépend de l'heure murale du serveur : un saut d'horloge le décale.
- **Faiblesses des comptes de la copie.** Ils comptent par `wc -l`, si bien qu'un nom de fichier qui contient un saut de ligne fausse les comptes. Le chemin est lu à la colonne 67, ce qui décale les lignes échappées par `sha256sum` (noms avec barre oblique inverse) ; cela ne touche que le contrôle des doublons.
- **Ce qui reste supposé.** Le vrai programme, le code v6 et l'orchestrateur n'ont pas été exécutés. Leur conduite au signal de fin et l'absence d'appel à git sans `.git` sont supposées. Le programme ne contient aucun appel à git (recherche faite) ; dans le code v6, ma recherche n'a rien trouvé ; l'orchestrateur n'a pas été lu.
- Factices écrits par moi ou par mes prédécesseurs ; intervalle d'essai d'une seconde.

## Relevé de méthode

**Chaîne de raisonnement.**
1. La commande exigée est la ligne 40 de `complement.md` (`56ed20f8…b867`) ; sa partie variable se limite aux trois chemins (devis v5 `452e7bcf…`, § 4.1).
2. La ligne du lanceur v3 est cette ligne, où seuls les trois chemins sont remplacés : `verifier-commande-v3.py` rend 0. Ce vérificateur rend 1 sur huit altérations, dont une d'un octet (`final-1-argv.txt`).
3. Ce que la ligne exécute vraiment, une fois les variables développées, est égal à l'attendu calculé du complément seul, y compris pour des chemins avec espace et apostrophe : interprète factice, essai dynamique.
4. Les refus de départ de la v2 sont rejoués (10 à 13, 2 à 4). Les refus de la copie sans `.git` et le refus 14 rendent leurs codes, en vérification (36 cas) et en emploi (6 cas, l'interprète n'étant appelé que dans le cas sain).
5. Le gardien v4 ne diffère du v3 que par (A), (B) et (C) : lecture du diff entier (`diff essais/copies/pieces-anciennes/gardien-essai-court-v3.py gardien-essai-3-v4.py`). Un arrêt déjà fait, de place, de durée ou de mesure, clôt les contrôles comme en v3 : un arrêt de place sans signal, faute d'identité, empêche donc aussi l'arrêt de durée.
6. L'arrêt de durée passe par `arreter`, comme les autres arrêts (lecture de `controles`). Les essais d2 à d2f montrent la même conduite qu'en v3 :
   - groupe, et arrêt forcé ;
   - hors groupe, par identifiant ;
   - mode descendants ;
   - identité non confirmée : aucun signal (decoy « duree »).
7. Désarmé, l'arrêt de mesure ne décide rien (m1, m1b, m1c). Armé, il décide comme en v3 (m2, s4, s6, et toutes les parties 3 et 4).
8. L'arrêt de place est inchangé (p1, p1b, s2, e2c1-place).
9. Le reste du gardien v3, inchangé, est rejoué sur la v4 (parties 1 à 4), avec les mêmes rendus que le rapport v3. Les noms changent seuls.
10. Supposé : la conduite du vrai programme au signal de fin, et sans `.git`.

**Objets de contrôle.**
- *Arrêt de durée.*
  - Faux par construction : heure non atteinte, ou atteinte après la fin du programme (d1, d1b). Prédit : aucun arrêt. Rendu : aucun arrêt.
  - Vrai par construction : heure atteinte (d2 à d2f). Prédit : arrêt, raison écrite. Rendu : arrêt.
  - Identité : témoin sans lien, heure absente ou décalée. Prédit : aucun signal. Rendu : aucun signal. Heure exacte : signal.
- *Refus de l'heure.*
  - Vrai : heures mal formées ou trop lointaines. Prédit : code 2, rien d'écrit. Rendu : conforme.
  - Faux : heures bien formées, bord de 94 h compris. Prédit : départ. Rendu : départ.
- *Arrêt de mesure désarmé.*
  - Objet où un arrêt serait faux : n au-delà du seuil, désarmé. Prédit : rien. Rendu : rien.
  - Même objet armé (m2). Prédit : arrêt. Rendu : arrêt.
  - Le témoin armé montre que le cas désarmé pouvait échouer.
- *Lanceur.*
  - Copie saine (vraie). Prédit : 0. Rendu : 0.
  - Copie sans commit, avec commit faux, interpréteur absent, fichier modifié (fausses). Prédit : refus. Rendu : refus.
- *Vérificateur.*
  - Lanceur exact. Prédit : 0. Rendu : 0.
  - Huit altérations. Prédit : 1. Rendu : 1.
  - Aucun mécanisme n'a réussi là où la conclusion était fausse.

**Premier pas non justifié.** Pas 10. Deux choses ne sont pas éprouvées : la conduite du vrai programme au signal de fin, et sa marche sans `.git` (code v6 et orchestrateur non exécutés, orchestrateur non lu). Ce qui le justifierait : un départ du vrai programme sur la copie, dans un dossier jetable, arrêté par le gardien au bout de quelques minutes. Cela sort de mon mandat.

**Mode d'échec affecté.** Sans objet : je suis l'auteur, non un relecteur.

**Dérivation de l'énoncé seul.** Sans objet : je ne suis pas un agent de re-dérivation.

**Trouvaille de côté.**
- (a) En mode `--verifier-seulement`, le lanceur écrit `code-de-sortie.txt`, ce qui bloque un départ ultérieur dans le même dossier de tenue (code 4). Le contrôle préalable sur le serveur doit donc se faire dans un dossier de tenue à part (c'était déjà vrai en v2).
- (b) Dans le vérificateur v3, la garde « chemin resté codé » double l'égalité à l'octet : je n'ai trouvé aucun cas où elle seule échoue.
- (c) Un gardien arrêté par mon signal de fin reste visible environ 0,3 s dans `/proc` (essai de départ) : c'est un effet de délai, il était absent ensuite.

**Évaluateur et conseil.** Ce qui jugera ce produit : le vérificateur S, puis la session. Mes témoins sont les objets vrais et faux ci-dessus, construits et nommés avant chaque rejeu `final`.

Le produit pourrait recevoir un bon jugement sans le mériter, par quatre voies :
- les factices et l'interprète factice sont écrits par moi ;
- la forme `.git` n'est éprouvée qu'en vérification ;
- l'arrêt de durée n'est éprouvé qu'à des heures proches, à quelques secondes, et non à 94 h ;
- le seuil de place factice de `e2c1-place` dépend de la place libre au moment de l'essai.

Conseil au vérificateur : lire le diff du gardien v3 contre le v4, et chercher un chemin où l'heure atteinte ne déclenche pas d'arrêt.
