# Proposition B — Vérification non circulaire des artefacts produits en bac à sable

## (a) Ce que la question suppose sans que ce soit établi

| # | Supposition implicite | Statut | Commentaire |
|---|---|---|---|
| S1 | Un optimiseur qui « apprend à satisfaire le vérificateur » est un risque réel dans le contexte de l'organisme (agents LLM exécutant du code, pas un agent RL entraîné en boucle sur un signal de récompense). | HYPOTHÈSE | Avalon (p. 76, 79–80, VÉRIFIÉ dans la pièce 4) décrit des agents RL entraînés sur des récompenses collectives dans 25 environnements. L'organisme d'idéation n'entraîne pas d'agent en boucle sur le verdict du vérificateur : l'expérimentateur a 3 exécutions par fiche, un lecteur neuf rend un verdict, et les résultats ne nourrissent jamais les juges de la même course (pièce 1, « résultats »). Le transfert du risque Avalon au contexte de l'organisme n'est pas établi ; il est raisonnable comme garde, mais la question le traite comme un fait. |
| S2 | La circularité réside dans le fait que « la vérification tourne dans le même bac que la production ». | RAPPORTÉ (pièce 3, l. 166–187 ; pièce 4, l. 199–204) | Le texte d'Avalon dit : « Hashing the check tools is circular, because the hash is computed by tools in the same sandbox » (p. 76). Mais dans l'architecture v48, le vérificateur (lecteur_test) est déjà une session neuve distincte du producteur (expérimentateur) — pièce 1, table « rôle lecteur_test ». Le hachage des résultats est fait par le noyau, pas par le script du bac. La circularité visée par Avalon (un agent qui contrôle à la fois la production et la vérification) ne s'applique pas directement au protocole v48 tel que décrit. La question suppose que la circularité existe ; elle est partielle au mieux. |
| S3 | Une machine virtuelle légère (Firecracker, Kata) « change la classe du problème » par rapport à un bac dans l'hôte. | HYPOTHÈSE | Aucune pièce ne compare les surfaces d'attaque. La question l'offre comme option mais ne cite aucune mesure. Le passage de `bwrap` (filtrage d'appels système en espace utilisateur) à Firecracker (VMM avec un noyau invité séparé) réduit la surface d'appels système exposée à l'hôte (HYPOTHÈSE illustrative : ~30 appels système pour Firecracker contre ~300+ pour un conteneur), mais cela ne change la « classe » du problème que si l'on définit ce que « classe » signifie en termes de taux de fuite mesurable. |
| S4 | Deux bacs d'implémentations différentes avec accord exigé fournissent un « gain réel » contre un optimiseur. | HYPOTHÈSE | La question cite Wheeler (double compilation diverse) et Thompson (« Reflections on Trusting Trust »). Wheeler traite de la compilation, pas de l'exécution en bac à sable. Thompson montre qu'un compilateur compromis peut reproduire sa compromission — le parallèle avec deux bacs est une analogie, pas un résultat. Aucune pièce ne donne de taux de détection pour une redondance diverse de bacs. |
| S5 | Les canaris journalisés mesurent « le sondage de la plate-forme ». | HYPOTHÈSE | Les canaris (fichiers, clés et chemins factices) mesurent un type de sondage : l'accès à des ressources nommées placées délibérément. Ils ne mesurent pas le sondage par canaux latéraux (temps, consommation mémoire, contention de cache). La pièce 1 mentionne l'écouteur sur la boucle locale et l'écriture hors dossier comme sondes, mais pas de canaris au sens de fichiers factices. La question les suppose valides sans définir leur couverture. |
| S6 | Des « suites publiques d'étanchéité » existent pour `bwrap`, gVisor et Firecracker et sont applicables telles quelles. | HYPOTHÈSE | La pièce « Faits servis » dit explicitement : « Aucune suite publique d'étanchéité n'est nommée dans les pièces (c'est précisément ce que la question demande aux espèces, Q6). » Le fait que de telles suites existent est une supposition — elles peuvent exister sous forme de suites de conformité OCI, de tests d'appels système, ou de fuzzing noyau, mais leur adéquation pour valider `bwrap` spécifiquement n'est pas établie. |
| S7 | L'attestation matérielle (TPM, Confidential Computing) est disponible et pertinente sur une machine louée jetable à 0,06 EUR/h. | HYPOTHÈSE | La pièce 2 ne mentionne pas de TPM sur les gabarits Hetzner CPX. Les machines Cloud CPX sont des instances partagées (pièce 2, § 1.2 : « AMD partagés »). L'accès à un TPM virtuel ou à une attestation matérielle sur ces gabarits est SUPPOSÉ indisponible sans vérification. |
| S8 | La « reproduction des empreintes par un tiers » (point (h)) est faisable à coût raisonnable. | HYPOTHÈSE | La reproductibilité des empreintes exige des constructions déterministes. La pièce 1 décrit un `tar --sort=name --mtime=@0 --owner=0 --group=0 --numeric-owner` déterministe (pièce 2, § 2.3), mais la reproductibilité de l'exécution du script Python dans le bac (même sortie pour les mêmes entrées) n'est pas établie — elle dépend du déterminisme du code exécuté, du planificateur, des horodatages, etc. |

---

## (b) Expériences décisives

### Expérience 1 — La circularité d'Avalon s'applique-t-elle au protocole v48 ?

**H_A** : Un expérimentateur (LLM avec 3 exécutions, sans accès au vérificateur) peut, dans le protocole v48, produire un artefact qui satisfait la lecture mécanique du noyau tout en étant incorrect (faux positif de l'étage).

**H_B** : La séparation noyau/expérimentateur/lecteur du protocole v48 empêche structurellement cette attaque — le verdict ne dépend que de la dernière ligne `RESULTAT:` de la dernière exécution réussie, lue mécaniquement par le noyau, et le lecteur neuf ne peut que confirmer ou contredire cette lecture sans la modifier.

**Métrique** : Taux de faux positifs de l'étage. On soumet N fiches avec des hypothèses délibérément fausses (effet nul planté dans les données), et on mesure combien passent le seuil gelé malgré l'absence d'effet.

**Seuil** : Si > 0 fiche sur 50 passe avec un effet nul planté et un seuil raisonnable (p < 0.05 bilatéral), H_B est falsifiée. Si 0 sur 50, H_A n'est pas prouvée impossible mais la borne supérieure du taux est < 7 % (IC 95 %, illustratif).

**Contrôle négatif** : Fiches avec un effet réel (planté à 2σ dans les données), qui doivent passer. Si elles ne passent pas, l'étage est dysfonctionnel et l'expérience est non concluante.

**Falsification** :
- Issue A (au moins un faux positif) : falsifie H_B — la séparation structurelle est insuffisante.
- Issue B (zéro faux positif, et les contrôles positifs passent) : falsifie H_A dans les limites de la puissance — la circularité d'Avalon ne se manifeste pas à cette échelle.

**Note critique** : Cette expérience teste la robustesse du protocole, pas la capacité d'un optimiseur à apprendre à le tromper. L'expérience 2 ci-dessous est nécessaire pour tester l'optimisation.

---

### Expérience 2 — Un agent peut-il sonder la plate-forme à travers le bac ?

**H_A** : Un script exécuté dans le bac `bwrap` (drapeaux de la pièce 1 : `--unshare-all --unshare-net --clearenv --die-with-parent`, système en lecture seule, un dossier inscriptible) peut distinguer un environnement de production d'un environnement de test par des observations accessibles (temps d'exécution, contenu du dossier inscriptible, erreurs retournées par des appels système bloqués).

**H_B** : Le bac est opaque — aucune observation accessible dans le bac ne permet de distinguer production et test avec un taux supérieur au hasard.

**Métrique** : Précision d'un classificateur binaire (production vs test) entraîné sur des caractéristiques extraites de l'intérieur du bac (temps, codes d'erreur, contenu de `/proc` disponible, latences de syscall).

**Seuil** : Précision > 60 % sur 100 essais (50 production, 50 test) falsifie H_B. Précision ≤ 55 % ne falsifie pas H_A mais la rend peu exploitable (illustratif : gain informationnel < 0,02 bit).

**Contrôle négatif** : Un script qui ne fait que du calcul pur (pas d'appel système au-delà de read/write sur le dossier inscriptible) doit rendre 50 % ± bruit. Si ce script distingue déjà les environnements, le protocole expérimental est vicié.

**Falsification** :
- Issue A (précision > 60 %) : falsifie H_B — le bac fuit de l'information. La nature de la fuite (quel trait est discriminant) oriente la correction.
- Issue B (précision ≤ 55 %) : falsifie H_A dans les limites — le sondage par canaux accessibles n'est pas viable.

**Contrainte** : Cet essai ne doit utiliser aucune technique d'évasion (règle de la question). On mesure uniquement ce que le script peut *observer*, pas ce qu'il peut *exploiter*. Les traits sont des lectures passives (horloge, codes d'erreur, `/proc/self/status`).

---

### Expérience 3 — La redondance diverse (deux bacs) détecte-t-elle les écarts ?

**H_A** : Deux bacs d'implémentations différentes (`bwrap` et gVisor, ou `bwrap` et un `chroot` durci) exécutant le même script produisent des sorties identiques octet pour octet pour des scripts honnêtes, et des sorties divergentes pour des scripts qui exploitent un comportement spécifique à une implémentation.

**H_B** : Les deux bacs divergent déjà sur des scripts honnêtes (différences d'environnement, de temporisation, de bibliothèques), rendant la comparaison inutilisable sans tolérance.

**Métrique** : Taux de divergence = (scripts avec sortie différente) / (scripts totaux), mesuré séparément sur un corpus honnête et un corpus adversariel.

**Seuil** :
- Sur le corpus honnête (50 scripts de calcul numérique Python) : taux de divergence > 10 % falsifie H_A — la redondance produit trop de fausses alertes.
- Sur le corpus adversariel (50 scripts qui lisent des chemins spécifiques à l'implémentation, mesurent des timings, interrogent `/proc`) : taux de divergence < 50 % falsifie l'utilité de la redondance — elle ne détecte pas assez.

**Contrôle négatif** : Un script `print(2+2)` doit rendre la même sortie partout. S'il ne le fait pas, la comparaison octet-pour-octet n'est pas le bon niveau.

**Falsification** :
- Issue A (divergence honnête ≤ 10 %, divergence adversarielle ≥ 50 %) : la redondance diverse est utile et praticable.
- Issue B (divergence honnête > 10 %) : falsifie H_A — il faut une comparaison sémantique ou tolérant les écarts, ce qui réintroduit de la complexité dans le vérificateur.

---

### Expérience 4 — Les canaris détectent-ils le sondage, et à quel taux de fausses alertes ?

**H_A** : Des fichiers canaris (clés factices, chemins piégés, fichiers sentinelles avec inotify ou horodatage d'accès) détectent un script qui explore le système de fichiers au-delà de son dossier de travail, avec un taux de fausses alertes < 5 % sur des scripts honnêtes.

**H_B** : Le taux de fausses alertes des canaris est ≥ 5 % sur des scripts honnêtes (un script Python normal touche des chemins inattendus via l'importation de bibliothèques, la résolution de liens symboliques, etc.), ou bien les canaris sont contournables sans accès direct (lecture de métadonnées, pas d'ouverture du fichier).

**Métrique** : Taux de fausses alertes = (scripts honnêtes qui déclenchent un canari) / (scripts honnêtes totaux). Taux de détection = (scripts sondeurs qui déclenchent un canari) / (scripts sondeurs totaux).

**Seuil** : Fausses alertes < 5 % **et** détection > 80 % pour que le mécanisme soit retenu. L'un ou l'autre hors seuil falsifie l'utilité des canaris tels que conçus.

**Contrôle négatif** : Un script qui n'importe rien et ne lit que `stdin` ne doit déclencher aucun canari. Un script qui fait `import numpy; import pandas` représente le cas honnête typique.

**Falsification** :
- Issue A (fausses alertes < 5 %, détection > 80 %) : les canaris fonctionnent.
- Issue B (fausses alertes ≥ 5 %) : falsifie H_A — les canaris génèrent trop de bruit ; il faut un mécanisme plus fin (par exemple, ne surveiller que les chemins hors de `/usr/lib/python*`).
- Issue C (détection < 80 %) : falsifie que les canaris mesurent le sondage — un sondeur peut éviter les pièges.

---

## (c) Mesure minimale pour chaque instrument nommé

### Instrument 1 : Vérificateur hors du bac (point (b) de la question)

**Ce qu'il doit faire** : Recevoir un artefact (script exécuté + sortie + empreinte) par un canal étroit, et rendre un verdict « conforme / non conforme » sans accéder au bac de production.

**Mesure minimale** :
- **Taux de détection** : Proportion d'artefacts altérés (empreinte modifiée, sortie injectée, script substitué) correctement rejetés.
- **Taux de fausses alertes** : Proportion d'artefacts honnêtes incorrectement rejetés.
- **Cas honnêtes appariés** : 100 paires (artefact honnête, artefact altéré d'un bit dans le script, d'un octet dans la sortie, ou avec une empreinte recalculée après modification). Les deux membres de chaque paire sont produits par le même script de base.
- **Vérification mécanique à battre** : Comparaison naïve `sha256(script) == empreinte_attendue && sha256(sortie) == empreinte_sortie_attendue`. C'est la baseline. Le vérificateur doit au minimum l'égaler (il ne peut pas faire pire que le hachage) et détecter en plus les cas où l'empreinte elle-même a été recalculée par le producteur.
- **Seuil** : Détection ≥ 99 % et fausses alertes < 1 %. Le protocole v48 atteint déjà ces seuils pour le hachage simple (le noyau scelle script, sortie et résultat par exécution — pièce 1). La question est de savoir si le vérificateur résiste quand le producteur contrôle le contenu de la sortie et choisit quoi imprimer sur `RESULTAT:`.

### Instrument 2 : Attestation par journal d'appels système (point (c))

**Ce qu'il doit faire** : Prouver que le binaire exécuté dans le bac est celui qui a été relu, et que l'exécution n'a pas été interrompue ou détournée.

**Mesure minimale** :
- **Taux de détection** : Proportion de substitutions de binaire détectées (le script exécuté diffère du script relu par le lecteur).
- **Taux de fausses alertes** : Proportion d'exécutions honnêtes où le journal signale une anomalie (appel système inattendu dû au runtime Python, au ramasse-miettes, etc.).
- **Cas honnêtes appariés** : 50 exécutions du même script, dont 25 avec substitution (un second script est `exec`-é par le premier à la place du calcul prévu — dans les limites du bac, ce qui est probablement impossible avec `--ro-bind` et `--no-new-privs`, mais c'est ce qu'il faut vérifier).
- **Vérification mécanique à battre** : L'empreinte du script avant exécution, comparée au script scellé. Le journal d'appels système doit détecter en plus les substitutions à l'exécution (par exemple via `execve` dans le bac).
- **Seuil** : Détection = 100 % pour les substitutions de binaire (c'est binaire : le bon fichier ou non). Fausses alertes < 2 %. Le coût du journal (surcharge de `strace` ou `seccomp` en mode log) doit être < 20 % du temps d'exécution (illustratif) pour rester viable sur des exécutions de 120 s.

### Instrument 3 : Canaris journalisés (point (e))

**Ce qu'il doit faire** : Détecter qu'un script explore le bac au-delà de son dossier de travail.

**Mesure minimale** : Définie dans l'expérience 4 ci-dessus. Résumé :
- Détection ≥ 80 %, fausses alertes < 5 %.
- Cas honnêtes : 50 scripts Python typiques (calcul numérique, manipulation de fichiers dans le dossier de travail, avec imports standards).
- Vérification mécanique à battre : `bwrap` lui-même avec `--ro-bind` empêche l'écriture hors du dossier de travail. Le canari doit détecter les *lectures* exploratoires, pas les écritures (déjà bloquées). Le taux de base est donc le taux de détection de `--ro-bind` pour les écritures (attendu : ~100 %) ; les canaris doivent ajouter la détection des lectures non autorisées.

### Instrument 4 : Suites publiques d'étanchéité (point (f))

**Ce qu'il doit faire** : Confirmer que le bac empêche les fuites attendues (réseau, système de fichiers hors montage, élévation de privilèges).

**Mesure minimale** :
- **Taux de détection** : Proportion de classes de fuites couvertes par la suite. Classes minimales : (1) accès réseau, (2) écriture hors dossier inscriptible, (3) lecture de fichiers sensibles de l'hôte (`/etc/shadow`, `/proc/1/environ`), (4) élévation de privilèges via appel système, (5) accès à d'autres espaces de noms.
- **Taux de fausses alertes** : Nombre de tests qui échouent sur une configuration correcte (régressions de la suite elle-même).
- **Cas honnêtes** : Le bac configuré selon la pièce 1 (`--unshare-all --unshare-net --clearenv --die-with-parent --ro-bind / / --dev /dev --proc /proc`, dossier inscriptible unique), avec un programme trivial.
- **Vérification mécanique à battre** : Les sondes internes de la v48 (pièce 1 : « écouteur sur la boucle locale, écriture hors dossier : un exécuteur qui laisse passer est refusé »). La suite publique doit couvrir au minimum ces deux cas et ajouter les classes 3 à 5.

### Instrument 5 : Redondance diverse (point (d))

**Mesure minimale** : Définie dans l'expérience 3 ci-dessus.

---

## (d) Ancrage matériel

### Modèles

L'organisme utilise déjà Claude (via le kit) et Argon (protocole externe) comme expérimentateurs (pièce 1). Le lecteur est un modèle neuf. Pour les expériences proposées :

- **Expérience 1** (faux positifs de l'étage) : aucun modèle supplémentaire nécessaire. On utilise l'orchestrateur v48 existant avec des fiches plantées. Le modèle expérimentateur est celui du protocole (Claude ou Argon).
- **Expérience 2** (sondage par le bac) : pas de modèle LLM. Scripts Python écrits à la main (ou générés une fois, puis fixés). Le classificateur est un Random Forest ou une régression logistique scikit-learn, entraîné sur les traits extraits.
- **Expérience 3** (redondance diverse) : pas de modèle LLM. Exécution mécanique de scripts dans deux bacs.
- **Expérience 4** (canaris) : pas de modèle LLM. Scripts pré-écrits.

Pour le vérificateur hors du bac (instrument 1), si l'on veut un vérificateur LLM (comme le rôle `lecteur_test`), un modèle ouvert de taille raisonnable suffirait pour la relecture de code : **Llama 3.1 70B** ou **Qwen 2.5 72B** (référence à vérifier pour les versions exactes disponibles en novembre 2026). L'avantage d'un modèle ouvert pour le vérificateur est que son comportement est auditable (poids fixes, pas de mise à jour silencieuse côté fournisseur).

### Calcul nécessaire

| Composante | Machine | Durée estimée | Coût estimé (illustratif) |
|---|---|---|---|
| **Expérience 1** : 50 fiches × 3 exécutions × 120 s dans le bac | CPX32 Hetzner | ~5 h | ~0,40 USD (TTC, au prix de la pièce 2) + coût modèle ~30 USD (50 fiches × 0,6 USD/fiche, illustratif) |
| **Expérience 2** : 100 exécutions × 2 conditions (prod/test) × 120 s | CPX32 Hetzner | ~7 h | ~0,56 USD machine |
| **Expérience 3** : 100 scripts × 2 bacs × 120 s | CPX32 + une seconde machine avec gVisor | ~7 h × 2 | ~1,12 USD machine. gVisor tourne en espace utilisateur, pas de coût supplémentaire au-delà de la machine |
| **Expérience 4** : 100 scripts × 120 s, avec instrumentation inotify | CPX32 Hetzner | ~3,5 h | ~0,28 USD machine |
| **Suite d'étanchéité** (instrument 4) : dépend de la suite, estimé 30 min à 2 h | CPX32 Hetzner | 2 h | ~0,16 USD machine |
| **Vérificateur LLM ouvert** (instrument 1, si retenu) : Llama 3.1 70B, une GPU A100 louée | ~50 fiches × ~2 min inférence | ~2 h GPU | ~4–8 USD (illustratif, au prix d'une A100 à 2–4 USD/h chez un fournisseur GPU) |

**Coût total illustratif** : ~35–42 USD, dominé par le coût du modèle expérimentateur (exp. 1) et du modèle vérificateur ouvert. Le calcul machine est négligeable (< 3 USD).

### Ordre recommandé (Q7, reformulé en termes d'expériences falsifiantes)

1. **Avant tout** : Expérience 2 (sondage par le bac). Si H_B est falsifiée (le bac fuit de l'information), tout le reste est compromis. Coût : < 1 USD machine. Aucune dépense modèle. Se joue sur la machine S0 de la pièce 2, avant même S1.

2. **Ensuite** : Expérience 4 (canaris). Établit si le mécanisme de mesure fonctionne. Coût : < 1 USD. Se joue sur S0 également.

3. **En parallèle de S1** : Évaluation de la suite d'étanchéité (instrument 4). Identifier une suite — candidates (noms à vérifier, je ne dispose pas de liens confirmés dans les pièces) : les tests d'intégration de `bubblewrap` eux-mêmes dans le dépôt `containers/bubblewrap` sur GitHub ; les tests OCI de `opencontainers/runtime-tools` ; pour gVisor, sa propre suite de conformité POSIX ; pour Firecracker, les tests de sa suite `integration_tests/`. **Aucune de ces suites n'est nommée dans les pièces ; ces noms sont des hypothèses à vérifier.** La suite se joue pendant S1 pour ne pas allonger le calendrier.

4. **Après S1 réussie** : Expérience 1 (faux positifs). Nécessite un modèle expérimentateur fonctionnel et l'`ExecuteurDistantParLots` (pièce 2, § 2.7). Se joue en série P ou dans une série de validation dédiée.

5. **Expérience 3** (redondance diverse) : **peut attendre**. Elle n'est utile que si les expériences 1 et 2 montrent que le bac unique est insuffisant. Coût modeste mais complexité élevée (second bac à configurer et maintenir). Ne pas la faire avant d'avoir montré qu'elle résout un problème avéré.

6. **L'attestation matérielle** (Q3) : **peut attendre indéfiniment**. Les machines CPX32 partagées ne fournissent vraisemblablement pas de TPM (HYPOTHÈSE). L'attestation logicielle (empreintes du script et de la sortie scellées par le noyau, comme dans la v48) suffit tant que le noyau lui-même n'est pas compromis — et s'il l'est, le TPM de la machine louée ne protège pas non plus (il atteste le démarrage de la VM, pas l'intégrité du bac à l'intérieur). Le gain marginal est proche de zéro pour le coût.

### Ce que la question ne pose pas et qu'il faudrait poser

La question demande comment vérifier les artefacts de façon non circulaire, mais ne demande pas **quel est le modèle de menace précis**. Il y a trois scénarios très différents :

1. **Un agent LLM qui, par hasard ou par instruction-following, écrit un script qui sonde le bac** : les gardes existantes (G8, G9, sondes internes) et le bac `bwrap` suffisent probablement. L'expérience 2 le tranche.

2. **Un agent LLM qui optimise délibérément sa sortie pour tromper le lecteur** : c'est un problème d'alignement du modèle, pas de bac à sable. Le vérificateur hors du bac ne le résout pas si le script produit une sortie `RESULTAT:` numériquement correcte mais scientifiquement trompeuse (par exemple, p-hacking par choix du sous-ensemble de données). Ce problème relève du préenregistrement et du seuil gelé, pas de la plomberie du bac.

3. **Un modèle qui a été entraîné à exploiter l'infrastructure de vérification** (le cas Avalon) : cela suppose un entraînement en boucle sur le signal du vérificateur, ce que le protocole v48 ne fait pas (les résultats ne nourrissent pas la génération courante). Si l'organisme évolue vers un tel entraînement, la question devient pertinente mais les gardes actuelles sont insuffisantes — il faut alors un vérificateur qui ne partage aucune information avec le processus d'entraînement, ce qui va bien au-delà d'un « bac séparé ».

La question mélange ces trois scénarios. Les réponses seront plus utiles si le scénario est fixé.

FIN-DE-CELLULE