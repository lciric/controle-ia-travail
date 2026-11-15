# Vérification courte de la procédure pas à pas du pilote MR-2 sur la machine jetable — v6 (passage v5 → v6) — v1

- **Lecteur** : instance neuve, qui n'a écrit aucune version de la procédure ni aucune de ses contre-lectures. Ce rapport n'écrit
  aucun nom de modèle (auteur de la procédure : modèle A ; lecteurs précédents : modèle B et un autre modèle).
- **Pièce vérifiée** : `procedure-pilote-mr2-v74-machine-v6.md`, empreinte
  `6eb3a1cf273e6c132b903132921f04d4c72a09650496ba7e9cf1c1ae1d5343ff`, égale à son compagnon et à l'empreinte attendue.
  Comparée à la v5 (`a5719e264f4d6e319f58a44445ae7df5b92803972e0b419dc6e4b462f1b80b3d`) et à la v4 (`3c0e6627…`) ; contre-lecture de
  la v4 relue (`f403f89f12569f7328e477ff0cefafffa3bbddf22b00369f310720ca5103f345`). Les 18 compagnons du dossier sont égaux.
- **Copie** : `/home/user/verif-pilote-v6`, tête détachée `341db2c2` (égale à `origin/lot/compte-organisme-v1`), arbre propre avant écriture.
- **Fin** : 2026-11-15T07:37:48Z (sortie de `date -u` de la commande qui écrit ce fichier).
- **Aucune commande de la procédure n'a été jouée** : aucun appel au loueur, aucune machine, aucun modèle, aucune clé lue.

## Verdict : jouable après corrections

0 bloquant, **2 majeurs**, 14 mineurs.

Le différentiel v5 → v6 ne porte aucun changement non déclaré. Le danger du majeur N1 (un code périmé du premier essai lu pendant le
pilote réel, d'où une destruction en plein appel) est **fermé**, par deux barrières indépendantes. Les quatre majeurs de la
contre-lecture de la v4 restent fermés. Toutes les sous-commandes et options du lanceur citées existent, à la lettre. Les deux
lignes de GO sont lues au montant exact par le lecteur gelé. Les deux majeurs neufs sont dans les chemins d'échec : (M1) le
paragraphe de la relance se contredit sur le nom du dossier quand le refus tombe avant la création de `reel/`, cas qui couvre la plupart
des refus possibles ; (M2) entre un `jouer` réussi et la mesure faite, un code inattendu n'a aucune conduite écrite, alors que l'arrêt
commun (A) y rend la mesure impossible à jamais. Chacun se corrige par deux ou trois phrases, sans toucher ni au code ni au texte.

## Limites

- Texte scellé non lu (il vit sur une autre branche, interdite à ce lecteur) : l'ordre du texte et l'égalité du bloc gelé reposent sur
  les contre-lectures précédentes.
- Outil du loueur : lu **dans son code source installé ici**, sans l'exécuter (`/home/user/vastai-env/lib/python3.13/site-packages/vastai/`,
  version 1.8.3 d'après ses métadonnées). La procédure cite la version 1.11.0 (l. 323) : l'écart de version reste à lever par l'aide
  de l'outil dans la session qui lance.
- Code du lanceur : lu dans le paquet dépaqueté hors de tout dépôt (empreinte du paquet `e3d83e47a06b2941c54240b96612cb17880fe4162e7822a2eb02ebac64c785b1`,
  tête `605e0f60f3eed0948948e6a4eb15cb73de1d03de`). Seule exécution : le lecteur gelé des GO (`pole/registre_go_v66.py`), en lecture
  seule, sur `registres/go.md` du dépôt de travail.
- Essais de forme sur données factices seulement (garde de l'identifiant, programmes proposés en m3).
- Aucun refus d'outil, de crochet ni de classifieur rencontré jusqu'à l'écriture de ce rapport.

## 1. Différentiel exact v5 → v6

`diff` des deux fichiers : 20 blocs. Chacun est rattaché à un point déclaré de la section 12 ter.

| lignes de la v6 | changement | point déclaré |
|---|---|---|
| 1 | titre « v6 » | version (R12) |
| 6-9 | paragraphe des versions : verdict rendu en réponse, refus du classifieur dit | en-tête, 12 ter |
| 28-31 | `etiquette.txt`, `identifiant.txt`, session sous bash | n2, n5 |
| 54-55 | contenu du nœud du point (6), machine louée jusqu'au mot de la mère | n8 |
| 90 | « prix horaire total » (stockage compris) | n4 |
| 92-93 | ≈ 2 h de mise en place, pire cas ≈ 14 h, ≈ 2,80 USD, heure limite à + 14 h | n4 |
| 98-99 | identifiant exigé entier, écrit dans `identifiant.txt` | n1, n2, n3 |
| 101 | repli : comparaison des deux listes brutes, écrit dans `identifiant.txt` | n2, n3 |
| 165-166 | `generer` à lancer détaché | n11 |
| 194 | aucun `blanc-2` | n9 |
| 257 | suivi : nom du code après une relance | N1 |
| 266-272 | relance : cas « `reel/` non créé », cinq étapes | n7, N1 |
| 279-281 | `REEL` ; `mesurer` détachée ; `sortie-lire-non-ouverte.txt` | N1, n11, n6 |
| 286-288 | sortie de `lire` non ouverte, rapatriée à part ; `REEL` | n6, N1 |
| 296 | `rapatrier --source /root/pilote/REEL` | N1 |
| 298 | dossier `retour-sous-agent` | n6 |
| 302-303 | `code-*.txt` au lieu de `code-09-reel.txt` ; copie à part de la sortie de `lire` | N1, n11, n6 |
| 312 | destruction : identifiant relu dans `identifiant.txt` | n2 |
| 315-316 | garde entière de l'identifiant, étiquette relue du fichier | n1, n2 |
| 378-397 | section 12 ter et refus dit tel quel | déclaré |

**Aucun changement non déclaré.** n10 est déclaré « inchangé » et l'est. Deux remarques : n3 n'est porté **qu'en partie** (seule la
lecture de `new_contract` est écrite ; la v6 le dit elle-même, « dite » : voir m3) ; des restes de la v5 contredisent la v6 (voir m5).
Le journal provisoire v18 (PO-052 à PO-056) confirme le verdict de la vérification v4 → v5 (1 majeur N1, 11 mineurs) et l'empreinte
de la v6, mais ne liste pas les onze mineurs un à un : leur seule liste est la section 12 ter de la v6.

## 2. Le majeur N1 : chemin d'une relance après un code 2, pas à pas

Premier essai : `lancer-reel.sh` écrit `journal-09-reel.txt`, puis `code-09-reel.txt` (2), puis efface les clés (l. 242-248).

1. Cas A — `reel/` existe, `lancements.jsonl` absent (refus de `lancer_relais` ou de `exiger_relais_prets`, lanceur l. 311-315, relancé
   en code 2 l. 349-352 ; le registre des lancements n'est écrit qu'après, l. 316-319). Étape (1) : les deux pièces du premier essai
   sont renommées ; `code-09-reel.txt` n'existe plus. Étape (2) : script neuf, sortie `reel-2`, code écrit dans `code-09-reel-2.txt`.
   Étape (3) : contrôles rejoués sur `reel-2`, clés renvoyées (le premier script les a effacées). Étape (4) : le suivi lit
   `code-09-reel-2.txt`, absent tant que le pilote tourne (« en cours »), et un code ne compte qu'avec « clés effacées » ; or les clés
   ne sont effacées qu'après la fin du processus (l. 246-247). **Un code périmé ne peut donc plus être pris pour celui du pilote en
   cours** : le fichier lu est neuf, et la seconde condition écarte un code lu pendant que les clés sont encore là. Étape (5) : les
   sections 10 et 11 suivent `reel-2`. Chemin cohérent de bout en bout. **N1 est fermé.**
2. Même si l'étape (1) échoue (les deux `mv` sont écrits sans dossier ni `ssh` : m1), le nom neuf du code protège encore. Il faut deux
   fautes de l'exécutant (renommage manqué **et** ancienne commande de suivi) pour lire, une fois le pilote fini, le « 2 » du premier
   essai : reste de forme, traité en m1.
3. Cas B — `reel/` n'a pas été créé (refus de `exiger_mode_reel`, l. 227-252 ; dossier existant, l. 291-292 ; préparation des mondes,
   l. 294 ; ou code 2 de l'interprète lui-même : erreur d'usage, fichier introuvable). La ligne 266-267 dit « la seule relance garde
   `reel` », mais les étapes (2), (3) et (5) nomment `reel-2` sans condition. Le danger de N1 reste fermé dans ce cas aussi (pièces
   renommées, aucun code périmé sous aucun des deux noms) ; mais les noms se contredisent : c'est le majeur M1 ci-dessous.

## 3. Les quatre majeurs de la contre-lecture de la v4, en v6

| majeur de la v4 | état en v6 | lignes | reste |
|---|---|---|---|
| M1 identifiant, commande de création, repli | **fermé** | 95-101, 312-316 | forme sans le GO (m2) ; programme du repli non écrit (m3) |
| M2 reprise après un code 2 | **fermé** pour le cas « `reel/` créé » | 265-272 | contradiction sur le cas « `reel/` non créé » (M1) |
| M3 durée et part de 3 USD | **fermé** | 90-94, 258-259 | 14 h × 0,20 = 2,80 USD ; rien d'écrit pour l'heure limite elle-même (m8) |
| M4 refus d'outil après la location | **fermé** | 53-56 | fichier des clés pendant l'attente (m9) |

Mineurs de la v4 portés en v5 et tenus en v6 : (A) aux sections 8, 10 (`lire`) et 11 ; rapatriement en commandes séparées ; pièces de
la séquence `lire --ecrire` puis `rapatrier` versées (les deux noms `lecture-pilote-v70.json` et son compagnon figurent bien parmi les
copies, `"aucun_monde": true`) ; ports contrôlés en Python ; `printf '%q'` ; seuil du crédit ; validité des clés dite. Restent
ouverts, déclarés « non repris » (l. 374) : `cd … || exit` et garde des marques avant le `sed` (m10 de la v4, repris ici en m11),
pièces remises au sous-agent (m11 de la v4), mise en place de ssh (m12 de la v4, repris ici en m13).

## 4. Argent et arrêt

- **GO cité** : GO-2026-11-14-13 et GO-2026-11-14-14, `registres/go.md` de `main`, lignes 332 et 333 (fichier inchangé depuis `20f66b0b`,
  empreinte `e80c6d15b139b502aa577e0f35094cea05088e08af5fa301eab01c3abce1f969`). Lus par le lecteur gelé du paquet : « montant seul »
  20 et 21.72 USD, exactement ceux de la configuration v12 ; type calcul, accordés par Lazar, échéance 2026-11-30, aucune ligne
  d'extension ; mots du périmètre exigés présents. Parts : 12 + 8 = 20 ; 9,36 + 9,36 + 3 = 21,72.
- **Plafond des fournisseurs** : mécanique. Chaque relais est lancé avec sa part comme plafond (`lancer_relais`, valeur par défaut
  `part_usd`) ; le lanceur arrête (code 3) si le pire cas de l'appel suivant dépasserait la part (l. 330-331). Conforme à la l. 259-260.
- **Plafond de la machine** : 3 USD, prix total au plus 0,20 USD par heure, pire cas 14 h (12 h = 4 × 10 800 s, égal aux délais de la
  configuration v12). Cette garde n'est **pas mécanique** : elle repose sur l'horloge de la session (m8).
- **Garde de dépense** : le crochet de garde de calcul `garde_calcul.py` (même empreinte dans la copie et dans le dépôt de travail,
  `73be0638…`) bloque toute commande de création sans identifiant de GO valide. La forme écrite de la commande ne le porte pas (m2).
- **Arrêt et destruction** : par identifiant relu d'un fichier, jamais retapé, exigé entier ; `-y` ; absence prouvée par la liste
  relue, avec témoin ; jamais par le code de sortie ; aucune seconde création avant la preuve (l. 104-105, 312-326). Les sept
  identifiants intouchables n'apparaissent qu'à la ligne 19. La relecture de l'étiquette avant `destroy` n'est qu'un commentaire entre
  deux commandes du même bloc (m3, m4).
- **Clés** : jamais en argument ni à l'écran (commande interne `printf` vers l'entrée standard de ssh ; fichier privé sous `umask 077` ;
  lu sous `env -i` ; effacé par le script et par (A)) ; `${NOM:?}` n'affiche que le nom. Aucune commande n'affiche l'environnement.

## 5. Commandes et scripts

- **Lanceur** (`demonstrations/pilote_mr2_v74.py`, analyseur l. 643-699) : `secret CHEMIN` ; `generer --secret --phrase-fichier --texte
  --texte-sha256 --sortie` ; `preparer --mondes --mondes-sha256` ; `jouer --mode --mondes --mondes-sha256 --sortie` et, en mode réel,
  les huit options de la l. 245 ; `mesurer --sortie --mondes --mondes-sha256` ; `lire --sortie --ecrire` ; `rapatrier --source
  --destination --mondes --mondes-sha256` ; `bloc --releve-sonde`. Toutes existent, noms exacts. Codes : 0 ; 2 sur `Refus` (l. 737-739) ;
  3 sur arrêt (l. 740-742). Clés de sortie de `preparer` égales à la l. 180.
- **Rapatriement** (`pole/audit_pilote_v70.py`) : `lecture-pilote-v70.json` et `CARTES-partiel.json` sont dans la liste permise
  (l. 35-37) ; destination existante refusée ; `sortie-lire-non-ouverte.txt` vit hors de `REEL` et hors des motifs `journal-*.txt` et
  `code-*.txt` : il ne sort que par la commande de la l. 303.
- **Configuration v12** : ports 8811 à 8814, délais 3600, 3600, 1800, 1800 s, parts, trois noms de clés et trois hôtes d'amont : égaux
  aux l. 91, 205, 211, 226, 259-260.
- **Section 1** : la tête de la copie est `origin/lot/compte-organisme-v1` ; le paquet et le dossier de la sonde y sont ; le relevé a
  l'empreinte `f56d9c0e…`, égale à son compagnon ; `--strip-components=6` compte juste. Dépaquetage rejoué hors dépôt : tête `605e0f60…`.
- **Outil du loueur** (code de la version installée ici) : `create instance ID --image --disk --label` et l'option générale `--raw`
  existent ; la sortie brute de la création est `{"success": …, "new_contract": N}` ; type de lancement par défaut : ssh ;
  `destroy instance ID -y` existe ; `show instances --raw`, sans `--limit`, rend une liste plate de lignes portant `id` et `label`.
- **Crochet** : son motif prend aussi `vastai create instance --help` (m2).

## 6. Ce qui se passe sur chaque échec

Aucun repli silencieux trouvé : chaque écart écrit mène à l'arrêt (rien de loué), à l'arrêt commun (A) ou à un nœud. Sections 1 à 8
et 11 : conduite écrite. Manques : codes hors de la liste à la section 9 et code non nul hors 3 de `mesurer` (M2) ; noms contraires
à la relance (M1) ; second code 2 après la relance (m1) ; nom de clé absent à l'étape 9 (m6) ; heure limite atteinte (m8).
Deux faits du code à connaître : un `Refus` levé **après** les appels (contrôle du manifeste, l. 376) sort en code 2 — la règle
« `lancements.jsonl` existe : aucune relance, arrêt (A) » le couvre bien ; l'interprète rend lui-même 2 sur une erreur d'usage ou un
fichier introuvable, sans ligne « refus : … » au journal — rien n'est appelé, `reel/` n'est pas créé.

## 7. Constats classés

### Bloquant

Aucun.

### Majeurs

**M1 — Relance quand `reel/` n'a pas été créé : deux consignes contraires dans le même paragraphe** (l. 266-267 contre l. 269-272).
La ligne 266-267 dit « si `reel/` n'a pas été créé (refus avant), la seule relance garde `reel` » ; l'étape (2) fait écrire un script
qui nomme `--sortie /root/pilote/reel-2` ; l'étape (3) contrôle « dossier `reel-2` absent » ; l'étape (5) dit que les sections 10 et 11
suivent `reel-2` « après une relance ». Ce cas couvre la plupart des refus possibles (toutes les gardes de `exiger_mode_reel` et la
préparation des mondes tombent avant `os.makedirs`, l. 295). L'exécutant doit choisir seul, machine louée et mondes générés. S'il
garde `reel` au script puis suit l'étape (5) à la lettre, `mesurer --sortie /root/pilote/reel-2` ouvre un manifeste absent : erreur
non rattrapée, code 1 (l. 555-556), sans conduite écrite (M2). S'il garde l'ancien script, le code s'écrit sous un nom que le suivi
de l'étape (4) ne lit pas : attente jusqu'au nœud d'avant l'heure limite.
Correction — ancien : « si `reel/` n'a pas été créé (refus avant), la seule relance garde `reel` ; » ; nouveau : « si `reel/` n'a pas
été créé (refus avant), la seule relance se fait aussi sous `--sortie /root/pilote/reel-2` (le lanceur n'exige qu'un dossier
absent) : après une relance, tous les noms sont ceux en `-2`, sans exception ; ». La ligne n7 de la section 12 ter suit.

**M2 — Entre un `jouer` réussi et la mesure faite, un code inattendu n'a aucune conduite écrite, et l'arrêt commun (A) y détruit le
seul lieu où la mesure est possible** (l. 262-274, 279-280, 285 ; (A), l. 49-52 ; l. 307). Seuls sont écrits : pour `jouer`, les codes
0, 2, 3 ; pour `mesurer`, « attendu 0 » et le code 3. Or `mesurer` rend 2 sur chacun de ses refus, tous **avant** le lancement du programme de
mesure (l. 558-569 : rien n'est mesuré, aucune sortie écrite), et 1 sur une erreur non rattrapée (dossier mal nommé, l. 556). Les
sections 4, 7 et 8 disent « arrêt (A) sur tout écart » : par analogie, l'exécutant détruit. Les mondes ne quittent jamais la machine
(l. 307) et la mesure les exige (l. 569, 572) : après la destruction, le pilote payé (jusqu'à 38,72 USD de parts) n'a plus d'issue,
pour une cause qui peut être une empreinte mal recopiée. De même `jouer` peut sortir par 1, 126, 127 ou 137, ou ne jamais écrire
son code (machine arrêtée par son hôte) : rien n'est écrit.
Correction 1 — ancien (l. 285) : « Après un code 3 de `mesurer`, ne pas relancer : arrêt commun (A). » ; nouveau : « Après un code 3 de
`mesurer`, ne pas relancer : arrêt commun (A). Tout autre code non nul de `mesurer` (2 : refus nommé ; 1 : erreur non rattrapée) :
cause écrite ; constater par `ls /root/pilote/REEL` qu'aucun fichier `sortie-mesure*` ni `mesure-pilote-v70*` n'existe ; puis **nœud à
la mère, machine gardée** (au plus jusqu'à l'heure limite) ; ni relance ni arrêt (A) sans son mot : la destruction rend la mesure
impossible. »
Correction 2 — ancien (l. 273-274) : « toute reprise demande un texte neuf et des mondes neufs. » ; nouveau : « toute reprise demande
un texte neuf et des mondes neufs. **Tout autre code** (1, 126, 127, 137…), ou un code jamais écrit alors que le processus a disparu
ou que la machine ne répond plus : aucune relance ; si `lancements.jsonl` existe ou ne peut pas être lu, arrêt commun (A) ; s'il est
absent, nœud à la mère, machine gardée. »

### Mineurs

- **m1 — Relance décrite, non écrite en commandes** (l. 249-250, 257, 267-272). Les `mv` n'ont ni dossier ni `ssh` ; le `sed` et le
  lancement écrits nomment `lancer-reel.sh` ; la commande de suivi écrite nomme `code-09-reel.txt` ; un second code 2 n'a pas de
  suite écrite. Nouveau, à écrire en toutes lettres : `ssh M 'cd /root/pilote && mv journal-09-reel.txt journal-09-reel-essai1.txt &&
  mv code-09-reel.txt code-09-reel-essai1.txt && test ! -e reel-2 && test ! -e lancements.jsonl && echo prêt'` ; le script
  `lancer-reel-2.sh` entier ; le `sed` et le `setsid nohup` sur `lancer-reel-2.sh` ; le suivi sur `code-09-reel-2.txt` ; « "en cours"
  avec "clés effacées" : nœud » ; « second code 2 : arrêt (A) ».
- **m2 — La forme écrite de la création ne cite pas le GO, et l'aide de l'outil est prise par le crochet** (l. 95-96). Le crochet
  bloque toute commande qui porte `vastai create` sans identifiant de GO (motif l. 38, blocage l. 192-194), y compris
  `vastai create instance --help` ; un refus du crochet ne se rejoue pas (l. 22-23). Ancien : « `vastai create instance OFFRE --image
  IMAGE --disk 20 --label "$ETIQ" --raw > "$ENV/creation.json"` » ; nouveau : « `GO_ID=GO-2026-11-14-14 vastai create instance OFFRE
  --image IMAGE --disk 20 --label "$ETIQ" --raw > "$ENV/creation.json"` », et dire comment l'aide se lit (même préfixe, ou lecture du
  code de l'outil).
- **m3 — Des preuves « par programme », seule la lecture de `new_contract` est écrite** (l. 100-103, 317-319, 324-325) : manquent
  le repli, l'étiquette avant `destroy`, l'absence après. Éprouvés ici sur des listes factices, forme de la liste brute lue dans le code de l'outil
  (liste plate, champs `id` et `label`), à confirmer sur la version de la session :
  repli — `python3 -c 'import json,sys;a={str(i["id"]) for i in json.load(open(sys.argv[1]))};n=[str(i["id"]) for i in json.load(open(sys.argv[2])) if str(i["id"]) not in a and i.get("label")==sys.argv[3]];assert len(n)==1,n;print(n[0])' "$ENV/instances-avant.json" "$ENV/instances-apres-creation.json" "$ETIQ" > "$ENV/identifiant.txt"` ;
  avant — `python3 -c 'import json,sys;m=[i for i in json.load(open(sys.argv[1])) if str(i["id"])==sys.argv[2]];assert len(m)==1 and m[0].get("label")==sys.argv[3],m;print("présent, étiquette juste")' "$ENV/instances-avant-destruction.json" "$ID" "$ETIQ"` ;
  après — `python3 -c 'import json,sys;av={str(i["id"]) for i in json.load(open(sys.argv[1]))};ap={str(i["id"]) for i in json.load(open(sys.argv[2]))};t=av-{sys.argv[3]};assert sys.argv[3] not in ap and t and t<=ap;print("absent ; témoins toujours listés :",len(t))' "$ENV/instances-avant-destruction.json" "$ENV/instances-apres-destruction.json" "$ID"`.
  Le témoin y est « toute autre instance listée avant l'est encore après », sans nommer aucun identifiant intouchable. Si le compte
  n'a plus aucune autre instance, le témoin est vide : à dire (nœud, ou preuve par la console).
- **m4 — La garde de l'identifiant n'arrête pas le bloc de destruction** (l. 315-318). Après `|| { echo …; false; }`, les lignes
  suivantes s'exécutent (éprouvé). Sans dommage direct (l'outil refuse un identifiant vide ou non entier), mais la garde est
  décorative. Nouveau : enchaîner les l. 315 à 318 par `&&`, le programme « avant » de m3 placé juste devant `vastai destroy`.
- **m5 — Restes de la v5 qui contredisent la v6.** l. 31-32, ancien : « ; `ID` = son identifiant, **lu dans le fichier
  `$ENV/creation.json`, jamais retapé** (section 2) » ; nouveau : à supprimer (la l. 30 le définit par `identifiant.txt`). l. 28-29,
  ancien : « une location de 13 h » ; nouveau : « 14 h ». l. 307, ancien : « `reel/prive/` » ; nouveau : « `REEL/prive/`, et
  `reel/prive/` d'un premier essai ». l. 6-9 : dire que la version nouvelle remplace la précédente pour l'usage.
- **m6 — Noms des clés et lignes de GO contrôlés seulement à l'étape 9**, après la location, le secret, la phrase et les mondes
  (l. 219, 222-226) ; ce que fait l'exécutant si un nom manque n'est pas écrit. Les deux contrôles ne coûtent rien à la section 1 :
  la ligne 226 telle quelle, et le lecteur gelé sur `"$ENV/go-main.md"` (fait ici : les deux lignes passent).
- **m7 — Python et numpy contrôlés hors du chemin réduit de `O`** (l. 45, 112-113, 125 ; image non nommée, l. 89-90). `O` tourne sous
  `env -i PATH=/usr/local/bin:/usr/bin:/bin` et `-I` ; le contrôle de la section 3 tourne dans le chemin de la connexion. Sur une
  image dont l'interprète est ailleurs, la section 3 passe et la section 4 échoue : arrêt (A), création unique consommée. Nouveau :
  `ssh M 'env -i PATH=/usr/local/bin:/usr/bin:/bin HOME=/root python3 -I -c "import sys,numpy;print(sys.version_info[:2],numpy.__version__)" && git --version'`
  (attendu `(3, 13) 2.5.3`), et nommer l'image.
- **m8 — Rien n'est écrit pour l'heure limite elle-même** (l. 55, 93, 258-259). Nœud une heure avant ; ensuite, sans mot de la mère,
  aucune consigne ; aucune garde mécanique ; à 0,20 USD par heure la part est atteinte à 15 h. L'heure limite n'est écrite dans aucun
  fichier. Nouveau : `date -u -d '+14 hours' +%Y-%m-%dT%H:%M:%SZ > "$ENV/heure-limite.txt"` dans la commande qui suit la création ;
  une phrase de la mère sur l'heure limite (par exemple : aucun processus du pilote en cours → arrêt (A) ; un processus en cours →
  nœud à Lazar, la part de 3 USD n'étant jamais dépassée sans son mot).
- **m9 — Sous le point (6), le fichier des clés peut rester sur la machine louée pendant toute l'attente** (l. 50, 53-56). Nouveau :
  « si le refus ne frappe pas cette commande et qu'aucun `jouer` ne tourne, l'étape (2) est faite avant le nœud ».
- **m10 — Scripts détachés de `generer` et de `mesurer` non écrits ; le bloc garde la forme au premier plan** (l. 162-166, 279-280).
  Deux formes coexistent ; la « forme de la section 9 » lit et efface le fichier des clés, ce qui ne les concerne pas. Les écrire
  (sans les deux lignes des clés, avec `cd … || exit 97`), et dire qu'un `mesurer` lancé deux fois rend 2 la seconde fois.
- **m11 — Variables de la session non gardées** (l. 27-32, 249, 253). Dans une session d'agent, l'état de l'interpréteur de commandes
  ne survit pas d'une commande à l'autre : `W`, `ENV`, `M`, `H`, `S1` à `S4` sont à reposer à chaque commande. Un `$H` vide à la l. 249
  donne une erreur d'usage, code 2, qui consomme la seule relance ; un `$ENV` vide écrit à la racine. Nouveau : `: "${ENV:?}"` en tête
  de chaque commande de la session ; `: "${H:?}" "${S1:?}" "${S2:?}" "${S3:?}" "${S4:?}"` avant le `sed` ; `H` et `S1` à `S4` tirés
  par programme d'une copie de l'engagement (déjà rapatrié, l. 302).
- **m12 — Relevé du crédit sans commande nommée** (l. 84-86). Dire laquelle, et n'en lire que le solde par programme (la commande de
  compte de l'outil retire la clé du loueur mais affiche des champs personnels) ; dire qui constate le moyen de paiement.
- **m13 — Mise en place de ssh non écrite** (l. 31, 112-116). Commande qui donne `M`, port, acceptation de la clé d'hôte sans
  dialogue (une session d'agent ne peut pas répondre à la question), option de port de `scp`. Un fichier de configuration ssh dans
  `"$ENV"` et `ssh -F` règlent les quatre.
- **m14 — La commande de la l. 304 ne compare pas au compagnon.** Ancien : « `sha256sum "$ENV"/retour/rapatrie-reel/lecture-pilote-v70.json` » ;
  nouveau : « `(cd "$ENV/retour/rapatrie-reel" && sha256sum -c lecture-pilote-v70.json.sha256)` » (le fichier n'est pas ouvert).

## Pièces

- Paquet dépaqueté pour la lecture du code et essais de forme sur données factices : dans le dossier temporaire de la session du
  lecteur, hors de tout dépôt (dossiers `arbre-v6/` et `essais-forme/` ; chemins entiers donnés dans la réponse au demandeur).
- Rien d'autre n'a été écrit dans la copie que ce rapport et son compagnon ; aucun commit, aucune poussée.
