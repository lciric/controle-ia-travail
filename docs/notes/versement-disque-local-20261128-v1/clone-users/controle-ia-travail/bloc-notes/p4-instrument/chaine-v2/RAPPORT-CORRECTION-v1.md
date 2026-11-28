# Rapport de correction de la chaîne de P4-instrument (chaîne v2) — v1

Correcteur neuf de la chaîne. 2026-10-20, fin vers 22:23 UTC.
Préfixe `…/` = `/tmp/claude-0/-home-user/50508bff-8fed-5fe9-beef-07f1bdcaf615/scratchpad/p4-instrument`.

## Verdict

Chaîne v2 conforme sur C d'essai, prête pour la vérification neuve et le versement. Toutes les décisions de la session sont appliquées ; sept bancs à 0 cas non conforme ; répétition jouet conforme (cinq passages aux codes attendus, sept récupérations conformes avec destruction, vingt-sept artefacts à un seul KO avec instance gardée et heure limite, deux refus en code 2, lecture jouet : refus sans --prereg du run décisif et L3 sur un run non décisif complet) ; `verifications_p4_v1.py preuves` et `repetition` en code 0 ; empreintes citées égales aux scripts livrés. Trois défauts réels trouvés par les bancs et la répétition, corrigés (lancement.txt décalé par le lanceur ; lecture d'un run arrêté acceptée en silence par la répétition ; artefact compté deux fois). Réserves : C d'essai et module v2 (le module v3 est vérifié depuis, R-295), deux noms de rapports à confirmer au versement, répétition finale à jouer sur le vrai C ; une écriture parasite de ma part dans le dépôt de travail (sans donnée, déplacée hors du dépôt par un autre).

## Ce qui est fait

- Chaîne v2 écrite dans `…/chaine-v2/`, copie de `…/chaine/` (v1 intacte), mêmes noms, vingt et un scripts dont
  quatre neufs (`arreter_p4_v1.sh`, `controler_traces_p4_v1.sh`, `essais_arret_p4_v1.sh`, `essais_traces_p4_v1.sh`).
  Liste CHAINE mise à jour (scellement, lanceur, bancs ; répétition finale : 21 attendus).
- Toutes les décisions de la session appliquées (détail constat par constat : `NOTES-CHAINE-v2.md`, section 2).
- Bancs complétés : chaque correction a son cas sain et ses artefacts ; cas des relecteurs repris (formes voisines
  de révocation, fenêtres décalées, texte échappé, traces seules, étiquette « p4-v1 x », 4 096 colonnes, longueurs
  doublées, motif d'arrêt recopié).
- Sept bancs et la répétition jouet rejoués sur les versions finales : bancs sur le C d'essai
  `8f4814ad54b7c271d30ced6371465eb8e26eaf40`, répétition sur le C d'essai `35f90e41993dd0cffcaaa9e1faba9dd5121454e7`
  (même module v2, chaîne v2 finale), candidat 2 d'essai tiré du candidat 1 réel par `ecrire_candidat2_v1.py` et les
  paires de la chaîne v2. Cinquième passage ajouté (arrêt du module pendant le run).
- `verifications_p4_v1.py preuves` (sept journaux des bancs) : code 0. `verifications_p4_v1.py
  repetition` : code 0.
- Paires exactes du texte : `paires-candidat2-chaine-v2-v1.json` (`2f5a591b8bd7d420509026c6d63e626602648f5d6925a391829ce560b34378fb`).

## Résultats

- `banc-arret-p4-v1.log` : FIN DU BANC DE L'ARRÊT DE P4 ; cas non conformes : 0 (21 lignes « CONFORME »).
- `banc-surveillance-p4-v1.log` : FIN DU BANC DE LA SURVEILLANCE DE P4 ; cas non conformes : 0 (93 lignes « CONFORME »).
- `banc-traces-p4-v1.log` : FIN DU BANC DU CONTRÔLE DES TRACES DE P4 ; cas non conformes : 0 (20 lignes « CONFORME »).
- `banc-verifications-p4-v1.log` : FIN DU BANC DES VÉRIFICATIONS DE P4 ; cas non conformes : 0 (177 lignes « CONFORME »).
- `banc-lanceur-p4-v1.log` : FIN DU BANC DU LANCEUR DE P4 ; cas non conformes : 0 (125 lignes « CONFORME »).
- `banc-controles-p4-v1.log` : FIN DU BANC DES CONTRÔLES DE P4 ; cas non conformes : 0 (86 lignes « CONFORME »).
- `banc-scellement-p4-v1.log` : FIN DU BANC DU SCELLEMENT DE P4 ; cas non conformes : 0 (64 lignes « CONFORME »).
- `repetition-jouet-p4-v1.log` : FIN DE LA RÉPÉTITION (cinq passages aux codes 0, 2, 1, 124, 1 ; sept récupérations
  conformes avec destruction ; vingt-sept artefacts à un seul KO, instance gardée ; deux refus en code 2 ; lecture
  jouet : refus sans --prereg du run décisif, L3 sur le run non décisif ; aucun jeton ni aucune fenêtre affichés).
- Preuves : code 0. Répétition : code 0. C d'essai `35f90e41993dd0cffcaaa9e1faba9dd5121454e7` ; candidat d'essai `P4-instrument-v1-candidat2-essai.md` (`1398e10c4c1c5e0d87baac50fd8bfc2d79567e156ad11e40f0355341538e2e72`).

## Constats du correcteur

- **CV2-01** (majeur (corrigé)) : Lanceur v2 : les arguments du printf qui écrit lancement.txt étaient décalés d'un rang (un argument « création » resté de la v1 après le passage de la surveillance au dossier des traces). Effet : ligne « contrôle à cinq minutes entre … » fausse et second bloc vide répété dans lancement.txt, lu ensuite par la surveillance, le contrôle à cinq minutes et la récupération. Trouvé par le cas sain P00 du banc du lanceur (R5). Corrigé ; le lanceur relit en plus, une fois chacune, les lignes calculées (lanceur, plafond de la surveillance, contrôle à cinq minutes, récupération) avant la création.
- **CV2-10** (majeur (corrigé)) : Répétition jouet (lecture jouet, module v2) : le run jouet non décisif était lancé sans l'entropie du préenregistrement jouet ; le module s'arrêtait (« modèle jouet autre que celui du run source ») et la lecture du run arrêté rendait L2 avec le code 0, ligne acceptée par le module commun : un repli silencieux, contraire à R5. Corrigé dans repetition_jouet_p4_v1.sh : entropie passée, run complet exigé (code 0, résumé sans motif d'arrêt), sinon pas de lecture et la répétition échoue ; la lecture rend L3. Deux autres défauts de la répétition corrigés : ligne __pycache__ comptée parmi les lignes « lecture jouet » ; artefact « jeton dans les traces seules » qui comptait deux KO (jeton de GitHub porté par deux variables).
- **CV2-02** (majeur (écart à la consigne, de mon fait)) : Écriture parasite dans le dépôt de travail, de mon fait : vers 20:07:21 UTC, une commande en arrière-plan mal formée (le cd ne valait que pour la première tâche) a créé /home/user/controle-ia-travail/banc-traces.log (une ligne d'erreur de bash et « code 127 » ; aucun texte, aucun jeton). À 20:07:44 UTC, un autre que moi l'a déplacé hors du dépôt, vers …/chaine-v2-travail/hors-depot/banc-traces-ecrit-a-la-racine-du-depot-2026-10-20-2007.log (66 octets, contenu relu). Aucune commande git, aucun autre fichier, aucun __pycache__. Signalé à la session vers 20:09 UTC ; toutes les commandes suivantes en chemins absolus.
- **CV2-03** (information) : Deux écrivains sur chaine-v2 (R-293) : une copie de ce correcteur, relancée hors de l'orchestration, a écrit de 19:49 à 19:53 UTC (banc du lanceur, adaptation au module v2, passages 1 et 5 en parallèle, outil du C d'essai). Arrêtée par la session. Tout est intégré ; les huit journaux éprouvent les versions finales (empreintes citées = fichiers de chaine-v2).
- **CV2-04** (réserve) : Module : la consigne disait module inchangé (v1) ; la session a retenu le module v2 (R-293). La chaîne v2 est éprouvée avec le module v2 (C d'essai, candidat d'essai, 1 123 tests). Le module v3 de P4 est vérifié (R-295) : s'il est retenu, refaire le C d'essai, le candidat (empreintes et nombre de tests) et la répétition ; la chaîne v2 ne cite aucune empreinte du module.
- **CV2-05** (réserve) : Preuves sur des C d'essai, pas sur le vrai C : bancs sur le commit 8f4814ad… (dépôt de travail à a82dac76…), répétition jouet sur le commit 35f90e41… (dépôt de travail à 98a95de7…), sans les PDF, module v2 et chaîne v2 versés. La répétition finale n'est pas jouée (vrai C, journaux versés et tokeniseur versé exigés). L'ordre de la session rejoue bancs, répétition jouet et répétition finale sur le vrai C après le versement.
- **CV2-06** (réserve) : Rapports attendus (RAPPORTS_NOMS, douze noms exacts) : deux noms restent à confirmer au versement (vérification de la chaîne v2 ; vérification du module retenu ; le module v2 en a deux, contournement et fidélité, nommés ici avec « P4 »). Un nom changé change l'empreinte du module commun : bancs qui le citent et répétition à rejouer (déjà prévu sur le vrai C).
- **CV2-07** (information) : Laissé tel quel, selon la décision : RC-donnees-07 (contrôle des fuites sur l'instance avant la poussée, version suivante) ; RC-fidelite-10 et -11 (rien). La dépense consignée X n'est relue par aucun code (la chaîne relit la forme et la somme) : dit dans le texte, précision 7.
- **CV2-08** (mineur (corrigé)) : Défauts des bancs trouvés en les jouant : sauts de ligne littéraux dans des chaînes Python (fabrication des fenêtres, entrées du filtre), guillemets coupés par le shell (F07), chemin du bloc-notes factice du banc du lanceur, lignes de la lecture jouet (J18 à J20, plus J20b), contrôle de troncature dépendant de la locale (W04, désormais exact), motif de J00, nombre de KO attendus (A44j, A44k, A51 : deux), compte « 11 » écrit en dur. Tous corrigés avant les journaux finaux.
- **CV2-09** (forme) : Banc du lanceur : deux cas partagent le préfixe M01 (M01-fichier-du-module-change, M01-second-lancement-du-meme-s) ; noms complets et verdicts distincts.

## Texte à ajouter au candidat (exact)

Chaque phrase remplace l'ancre indiquée du candidat 1, trouvée une seule fois (fichier `paires-candidat2-chaine-v2-v1.json`).

1. chaîne v2, accord-forme-150 (RC-depense-05, RC-fidelite-05) — ajouter, juste après l'ancre qui finit par « …étape reste sous 150 USD, et l'écrit dans la ligne d'accord. » :

```

    Forme exacte, une fois dans la ligne d'accord : « dépense consignée X USD + borne 5,41 USD = Y USD < 150 USD », où X
    est la dépense de la phase 0 consignée dans `registres/depenses.md` le jour de l'accord et Y = X + 5,41, à deux
    décimales, virgule décimale (par exemple « dépense consignée 47,83 USD + borne 5,41 USD = 53,24 USD < 150 USD »).
    `verifications_p4_v1.py accord` relit la forme, refait la somme au centime et exige Y < 150 ; sinon, aucune
    création. À 120 USD et au-delà, l'alerte de GO-2026-10-04-08 est écrite à l'accord.
```

2. chaîne v2, revocation-voisine (RC-depense-03, RC-depense-08, RC-fidelite-03) — ajouter, juste après l'ancre qui finit par « …R-269** ». L'une ou l'autre : aucune création. » :

```
 Une forme voisine (espaces libres, casse, accents ou tirets autres ;
    type « Révocation », « revocation » ou absent de l'en-tête du registre des GO ; cellule de décision qui commence
    par « Révocation », « révoque », « annulation » ou « retrait » ; plusieurs identifiants dans une même cellule) qui
    nomme l'un de ces cinq identifiants, à frontières de mot, arrête aussi le lancement (code 2, lignes affichées) :
    la chaîne refuse plus que la forme exacte, jamais moins. Les registres sont relus juste avant la création, après
    le choix de l'offre.
```

3. chaîne v2, accord-apres-s (RC-fidelite-08, RC-depense-09, RC-depense-10, RC-depense-04) — ajouter, juste après l'ancre qui finit par « …date du jour après l'échéance de la colonne du GO
    cité). » :

```
 L'accord est consigné après le scellement S : le lanceur refuse un accord dont l'identifiant figure déjà
    dans `registres/decisions.md` au commit S. Le GO cité se lit à frontières de mot (« GO-2026-10-20-071 » ne cite
    pas GO-2026-10-20-07). Un accord, un lancement : juste avant la création, le lanceur écrit un marqueur du commit
    S ; il refuse toute création si un marqueur de S existe déjà ou si la branche `calcul/p4-reel-v1` existe sur le
    dépôt distant. Avant chaque rejeu de la garde de calcul gelée, la chaîne exige `.claude/hooks/garde_calcul.py`
    égal à celui de S et d'empreinte `579f65c8ae3002d8e5c61698d636549b0401da3acff6bce718ae88e93664a6f2` ; sinon,
    aucune création.
```

4. chaîne v2, arret (RC-depense-01, RC-fidelite-06, RC-depense-06) — remplacer l'ancre :

```
     création + 9 600 s, puis arrêt de l'instance par son identifiant (R10) ;
```

par :

```
     création + 9 600 s, puis arrêt de l'instance par son identifiant (R10). L'arrêt est exécuté par
     `arreter_p4_v1.sh <identifiant> <dossier neuf>` : étiquette relue entière (« p4-v1 » exactement, sinon refus),
     `vastai stop instance <identifiant>`, état relu arrêté deux fois de suite en 10 minutes au plus (sinon code non
     nul et nœud de Lazar), heure et ligne prête pour `registres/arrets.md` écrites (le registre reste écrit par la
     session). La surveillance l'appelle d'elle-même à sa sortie (fin de l'amorce, échec d'amorce, redémarrage,
     état terminal, plafond) ; elle lit l'identifiant et la création dans `lancement.txt`, relit l'étiquette au
     départ et interroge l'instance toutes les 10 à 300 s, sans dormir au-delà du plafond ;
```

5. chaîne v2, liste-d-arret (RC-fidelite-04, RC-depense-02) — remplacer l'ancre :

```
- Contrôle à cinq minutes en échec ; dépense au-delà de la borne de l'étape : arrêt de l'instance par son identifiant.
```

par :

```
- Contrôle à cinq minutes en échec (il relit aussi le téléchargement, au plus 0,05 USD par Go, et le stockage, au
  plus 0,03 USD de l'heure) ; dépense au-delà de la borne de l'étape : arrêt de l'instance par son identifiant
  (`arreter_p4_v1.sh`, appelé par le contrôle à cinq minutes en échec).
- Récupération en échec : aucune destruction ; la récupération écrit l'état de l'instance et l'heure limite de
  destruction (création + 9 600 s + 24 heures) ; nœud de Lazar. Elle exige 3 Go libres avant le clonage et relit
  l'instance absente de la liste après la destruction.
```

6. chaîne v2, chaine-traces (RC-donnees-06) — remplacer l'ancre :

```
reste d'utile) ; attente du verdict complété de P3
```

par :

```
reste d'utile) ; contrôle des traces de la session avant tout versement (`controler_traces_p4_v1.sh <dossier>`) ;
attente du verdict complété de P3
```

7. chaîne v2, paragraphes (RC-donnees-01 à -05, -08, -09, RC-fidelite-09) — ajouter, juste après l'ancre qui finit par « …ncement à la fois ; P4, puis les autres lancements de R-262. » :

```


**Fenêtres, activations, traces et lignes de progression** (chaîne v2) :

- « Aucun texte d'action poussé » se contrôle à la récupération par toutes les fenêtres de 48 caractères, au pas de
  16, de chaque texte honnête de P3 d'au moins 48 caractères (fenêtres d'un seul caractère répété ignorées),
  cherchées en brut et sous forme échappée (JSON, Python) dans la forme brute et déséchappée de chaque fichier
  poussé, dans chaque chaîne JSON décodée et dans chaque chaîne des tableaux, aussi sur le chemin des traces seules.
  Aucun motif d'arrêt ni ligne de journal n'est affiché sans masquage des jetons puis recherche des fenêtres ; une
  ligne qui porte une fenêtre n'est affichée que par sa longueur et son empreinte courte.
- « Aucune activation gardée » se contrôle par un schéma fermé des trois tableaux : clés, types et dimensions fermés ;
  noms des sondes de la validation égaux à ceux de `scores-p4.npz` (424, même ordre) ; longueurs par jeton égales
  aux jetons notés de l'action.
- Avant tout versement, les traces de la session (lancement, contrôles, surveillance, contrôle à cinq minutes,
  arrêt, récupération) passent `controler_traces_p4_v1.sh <dossier>` : mêmes fenêtres, et valeurs des jetons ; une
  fenêtre ou un jeton trouvé : rien n'est versé, nœud de Lazar.
- Les lignes de progression du run (préfixe « PROGRES » : « etape=M5 conforme=True », épisodes au niveau 1,
  exclusions sur total), relayées par l'instance et gardées par la surveillance, peuvent être vues avant le verdict
  complété de P3 : elles ne sont pas une lecture. Elles ne donnent ni aire, ni C1, ni M6, et aucune décision n'en
  est tirée avant la lecture.
- Tokeniseur de l'agent : versé par la session sous `donnees/P4-tokeniseur-v1/` (`tokenizer.json`
  `79e3e522635f3171300913bb421464a87de6222182a0570b9b2ccba2a964b2b4`, `tokenizer_config.json`
  `177c7b61e616fecb84c17ce0591acb92c6c4d60e9ac5ababfb940ff23bbcd424`), avec leurs sceaux, zone exclue de la copie
  publique ; les contrôles avant dépense y rejouent les mesures de conception ; absent ou d'empreinte autre : arrêt.
- La liste des chemins gelés est lue dans `7a54d43` (`git show`), aux contrôles et au scellement, jamais dans
  l'arbre contrôlé.
```

8. chaîne v2, tokeniseur-metrique (RC-donnees-09) — remplacer l'ancre :

```
    citée (copie de la session `…/p4-instrument/tokeniseur/tokenizer.json`,
    `79e3e522635f3171300913bb421464a87de6222182a0570b9b2ccba2a964b2b4`, versée avec MC-1)
```

par :

```
    citée (copie de la session, versée avec MC-1 sous `donnees/P4-tokeniseur-v1/tokenizer.json`,
    `79e3e522635f3171300913bb421464a87de6222182a0570b9b2ccba2a964b2b4` ; Chaîne de lancement)
```

9. chaîne v2, precision-5 (RC-depense-03) — remplacer l'ancre :

```
5. Révocation : seules les formes écrites à l'en-tête bloquent ; une mention libre ne bloque pas.
```

par :

```
5. Révocation : les formes écrites à l'en-tête bloquent (code 1) ; une forme voisine qui nomme l'un des cinq
   identifiants bloque aussi (code 2) ; une mention libre, hors de la tête d'une cellule de décision et hors d'une
   ligne de GO de type « révocation » ou inconnu, ne bloque pas.
```

10. chaîne v2, precision-7 (RC-depense-05, RC-fidelite-05) — remplacer l'ancre :

```
7. Plafond de la phase (150 USD) : vérifié par la session à l'accord ; aucun code ne le relit.
```

par :

```
7. Plafond de la phase (150 USD) : vérifié par la session à l'accord et écrit dans la ligne d'accord sous la forme
   exacte de l'en-tête ; `verifications_p4_v1.py accord` la relit (somme refaite au centime, Y < 150 exigé). La
   dépense consignée X elle-même n'est relue par aucun code : elle reste un geste de la session.
```

11. chaîne v2, rapports attendus (RC-fidelite-12) — ajouter, juste après l'ancre qui finit par « …onsignes-v1.md`, le contenu des textes d'action, aucune clé. » :

```

- **Rapports versés** (sous `prereg/contre-lectures/`, avec leurs sceaux ; noms exacts, seuls de leur famille,
  relus par les contrôles et le scellement) :
  `prereg/contre-lectures/contre-lecture-R2-P4-instrument-brouillon1-v1.md` (`108a8d1ffd0a892c123608af237c824e2bc40545d4e54e5e5b7dcb9a37835420`) ;
  `prereg/contre-lectures/verification-corrections-brouillons2-3-P4-v1.md` (`9c94c2205b3f08e522917fd7c078748f8dc583fe4242ed9a26c325af71e7228e`) ;
  `prereg/contre-lectures/contre-lecture-3-P4-instrument-candidat1-v1.md` (`7f947de00aa58b0635fe2b6f0ad3c22eb7dbcb48ed0c8079f65a57abb13b5368`) ;
  `prereg/contre-lectures/relecture-chaine-depense-P4-instrument-v1.md` (`b6e43dd7a981d3dabc214127787ea245f976731763963d8d31a59543794f3c5b`) ;
  `prereg/contre-lectures/relecture-chaine-donnees-P4-instrument-v1.md` (`184b8926fe320f25f31014291fead8cd29b72efed5bd107ee97eacac5d9e7733`) ;
  `prereg/contre-lectures/relecture-chaine-fidelite-P4-instrument-v1.md` (`923c71d87115cf114d16c8079adce4dd79aa3ca112bcf9224ad6b9088cb988c5`) ;
  `prereg/contre-lectures/verification-chaine-v2-P4-instrument-v1.md` (`<empreinte au versement>`) ;
  `prereg/contre-lectures/verification-module-v2-contournement-P4-instrument-v1.md` (`2ce3d0af0a36fbb076d494b59619f4f11ed03fb9172f05e3bdde3087500a335d`) ;
  `prereg/contre-lectures/verification-module-v2-fidelite-P4-instrument-v1.md` (`ea12d4a2ea780e50e465105c29fb53fbe1e6eace5e3bae1ee177ed17426e7196`) ;
  `prereg/contre-lectures/P4-instrument-v1-brouillon1.md` (`41e5f035616e7cd3a233b680af06ba2a97c517a41d92f2042fde746aa85a48fd`) ;
  `prereg/contre-lectures/P4-instrument-v1-brouillon3.md` (`2ec30d6860838f5b9e9c2e637906101a8b0d2ad2a1df2cfdc355bf552374cd4c`) ;
  `prereg/contre-lectures/P4-instrument-v1-candidat1.md` (`6422fb45a1dc2a3b42a5f6adad4ed8ff02cf89b3c09d91474213c5c1f5fe3bc0`).
```


## Fichiers livrés

Chaque fichier a son sceau compagnon `.sha256` (forme « empreinte  nom »).

| fichier | sha256 |
|---|---|
| `NOTES-CHAINE-v2.md` | `1691bf2516ebc675e193482ff19cd4d136d5dda0778f9b56aa739665540e4841` |
| `amorce_instance_p4_v1.sh` | `21b3f447080353741c15d4948e557235dab17201a8d70f4545d1d9f1913c608d` |
| `arreter_p4_v1.sh` | `825701e2847d52e466b228cba46635fdc214cf9bc8fae4ebba8dffb68db85227` |
| `banc-arret-p4-v1.log` | `15c400cb60448a70b818038eeb5ae0fc97a74b95b75bc1292751d338a51d8489` |
| `banc-controles-p4-v1.log` | `55b8fc75d1cee822abff6ba4791e21c31a1d5d4f2e077d1e42caa32d3f0cb627` |
| `banc-lanceur-p4-v1.log` | `b7adeb5ca6bb4b5f7d57089edb7ab59085a85f99da66134e550b3e5de2672742` |
| `banc-scellement-p4-v1.log` | `d933980149ecb96bb84490f582d8a9ea6bed2c80a10b76bced694cf1ccb704a0` |
| `banc-surveillance-p4-v1.log` | `435b92ba64c9d4a24425b1dd81498e985b6926ab3f537ceba5a3e681f1546458` |
| `banc-traces-p4-v1.log` | `b3e5dbcf5a091338564c787a5408f484e6f19701b56406027e3218be6062c2ba` |
| `banc-verifications-p4-v1.log` | `0a5c4f9d0787c4939bbac420d9f14f18eec11e82a0900e3cffc7d673e73c4843` |
| `controle_cinq_minutes_p4_v1.sh` | `c3a63049480f3a526bb53edec6b04f72a532014b2811d5a696280922047af5e6` |
| `controler_traces_p4_v1.sh` | `f2fe40f2c9299af17ec7bbe4843d2e36b45c91904affe98b623057b1375c108e` |
| `controles_avant_depense_p4_v1.sh` | `c44bd6893c3b201ceb9273ce2a8b3a73b99ebf1589e325ee8fab11a61a9ddbeb` |
| `essais_arret_p4_v1.sh` | `d8e4e554c817d3aa8ff6714d657d6313e5d64ec92295f81d29d5331715147891` |
| `essais_controles_p4_v1.sh` | `e348e7eec67b92a4df3a3234143a44a47b416ea2c6a6140a4e7f6e2288d852be` |
| `essais_lanceur_p4_v1.sh` | `1c80fe4b45dc422cac5f8481e53a39cf324cbdd8c3fc238d68fc28e85b852173` |
| `essais_scellement_p4_v1.sh` | `f68d709117da0faac0d939b2ed588c8b47fc72e457cd0315580081acbdf99b87` |
| `essais_surveillance_p4_v1.sh` | `2f51d42dad9aedcf553a9a9e53226ae3eb09baa1a817a2fe1fd111794b38c4a0` |
| `essais_traces_p4_v1.sh` | `12cb9a0de4594a2e42faaad49703e47d15ccce39119b3aebe1fc7e62e25474c2` |
| `essais_verifications_p4_v1.sh` | `d8ab8510be47a8f2cd2fed0ab0cc056cd3baac91e5fbdeba265290e4a308e8b7` |
| `lancer_p4_v1.sh` | `0d2099335ebc31acf643ed275e1cd4789c9e0f78972588cee6a21a2e5d78d2ab` |
| `outils_essais_p4_v1.py` | `9f26389bb4868fda4b98a8e8b378740f7a441eaf5446bfeeba6419ad616d14c5` |
| `p4_instance_v1.sh` | `8801864fd9f2d940ed7ce2eed43c4efac8251484d37c1dcf3d3bea9bf0d8f967` |
| `paires-candidat2-chaine-v2-v1.json` | `2f5a591b8bd7d420509026c6d63e626602648f5d6925a391829ce560b34378fb` |
| `recuperation_p4_v1.sh` | `65477c6d5d1169ca123d9d087af5c8c74c6d2b80aa9f320f785af01de5d08814` |
| `repetition-jouet-p4-v1.log` | `f266f808e745f499458d817c617a27b4df94ed53b2e950820250633806918ffa` |
| `repetition_finale_p4_v1.sh` | `94bb9dcab7639c9aeba2b7d6265aba82d8f19784edf5aeec544a4da5d0a17f27` |
| `repetition_jouet_p4_v1.sh` | `b6cdba62126894c9e85df59b79930dc9007013f4c4c9e8b9da3d34acb8dd5efc` |
| `sceller_p4_v1.sh` | `afd15b53233fc1879faa0c575a2a4762973ec8f9c3d2c7920f07331436fffbf6` |
| `surveiller_p4_v1.sh` | `315ddd7d6141a8c124a9e7e3f1918837c7560a856f1065134506530d94701204` |
| `verifications_p4_v1.py` | `cdb6b90a34eabd549c2624441efae12bc6fa1a44ed245d5103f01738099f8f8e` |
