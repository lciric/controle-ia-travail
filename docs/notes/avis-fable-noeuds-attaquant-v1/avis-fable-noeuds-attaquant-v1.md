# Avis de Claude Fable 5.2 — cinq nœuds restés ouverts côté attaquant informé (v1)

21 novembre 2026, vers 16:25 UTC. Classe C (note d'avis). Demandé par le mot de Lazar « demande a fable pour tout ca »
(GO-2026-11-21-64). **Aucun geste n'a été fait** : ni révocation, ni effacement, ni poussée, ni appel payant, ni commande
vers le loueur de cartes, GitHub, Hetzner ou une messagerie. Ne se réécrit pas (R12).

## Verdict

1. **Ordre conseillé** : les clés d'abord (à un moment calme pour celle du compte du loueur), les instantanés ensuite
   (après un contrôle de couverture gratuit), **pas de purge de l'historique**, le courriel **gelé** jusqu'au gel des
   moniteurs, et pour la revue de sécurité externe **un mot écrit** qui dit ce qu'elle garde comme porte pour le bras
   d'attaque, avec un périmètre et une échéance.
2. **Deux oublis dans la liste des clés** : le jeton Hugging Face des postes, présent dans les instantanés, n'y figure
   pas ; et la clé du compte du loueur collée en clair est très probablement celle qui sert aux courses en cours : il
   faut la **remplacer**, pas seulement la retirer.
3. **Une confusion à écarter** : le nœud « quatre instantanés » vise quatre images de disque chez Hetzner, pas les
   quatre machines arrêtées chez le loueur de cartes que la passation de 16:45Z met sous le même mot.

## Pièces lues (chemin, empreinte abrégée)

Branche `claude/compassionate-meitner-d4ryyk` (tête `d2d9381e`), sous `registres/passations/` :
`2026-11-20-0832-passation-cloture-session-attaquant-informe.md` (`a3728bd5…`) ;
`2026-11-19-1005-incident-cle-instance-versee.md` (`3cff0a89…`) ; `2026-11-19-1029-bailey-instantanes-des-postes.md`
(`bc6342d7…`) ; `2026-11-19-1226-bailey-inventaires-et-destructions.md` (`b624e84c…`) ;
`2026-11-19-1530-attaquant-informe-reprise-sauvegarde-detruite.md` (`f16b5d02…`) ;
`2026-11-19-1648-attaquant-informe-lecture-reserves-bailey.md` (`43301c3f…`) ;
`2026-11-18-0122-brouillon-relais-bailey-depot-tiers-et-cles.md` (`00ac4ed0…`). Même branche, sous
`docs/notes/verification-externe-bras-v1/` : `projet-courriel-replication-externe-v4.md` (`3f1121f5…`, compagnon
conforme) et `plan-verification-externe-bras-v1.md` (`d3991222…`), sections 4.2, 7 et 8.

Branche `claude/loving-lamport-7ol5ws` (tête `271fb4d2`), sous `registres/passations/` :
`2026-11-21-0102-attaquant-informe-fin-autonomie.md` (`bc1e7fe5…`) et son erratum 1 ;
`2026-11-21-1545-attaquant-informe-passation-releve-fille.md` (`8679f6ce…`) ;
`2026-11-21-1645-attaquant-informe-fille-reprise-et-mandat-scellement-2.md` (`f8487d8e…`).

Sur `main` (`0fef5f95`) : `registres/go.md`, lignes GO-2026-10-28-04, GO-2026-11-19-96, GO-2026-11-20-46, -50, -62, -63,
GO-2026-11-21-17, -19, -64 ; fin de `registres/arrets.md` ; `docs/decisions/decision-N-057-v1.md` (`42180088…`) ; mon
avis du 20 novembre, `docs/notes/ideation-nouvelles-attaques-v1/avis-fable-5-2-procede-et-revue-securite-v1.md`
(`ee3e04b3…`) ; l'en-tête de `scripts/depot_expurge.py`.

**Précautions de lecture.** Toute suite de 28 signes ou plus a été masquée à l'affichage des passations : aucune valeur
de clé n'a pu être vue, et quelques noms de fichiers longs non plus. Le commit `2a1c0ff9` n'a pas été ouvert : seuls sa
date, son titre et les branches qui le portent ont été lus. Rien du coffre, aucun mode.

---

## Nœud 1 — Effacement des quatre instantanés

**Décision.** Effacer ou garder, et quand, les quatre images de disque protégées des postes du témoin de Bailey chez
Hetzner : 458234516 (5,05 Go), 458234528 (4,80 Go), 458234531 (7,00 Go), 458341216 (5,67 Go), soit 22,52 Go.

**Ce que disent les pièces.**
- Chaque image porte les clés du poste : clé de déploiement, clé du loueur, jeton Hugging Face (`bc6342d7…`).
- L'inventaire est fait : noms, tailles, empreintes, versés et scellés (`b624e84c…`, `f16b5d02…`).
- Des **contenus** n'existent, d'après ces pièces, que dans les images : le dossier de passe (562 fichiers sur le
  premier poste d'inventaire, 22 sur le second), le versement local du second (738 fichiers, environ 1,2 Gio de copies
  de l'instance), et les 74 fichiers de la sauvegarde des sondes et paramètres de la course à 36 tours. Pour ces 74
  fichiers, la passation prouve que l'image les contient avec la bonne empreinte ; je n'ai pas trouvé la preuve qu'ils
  vivent aussi sur une branche.

**Enjeu.**
- Si on efface : geste **irréversible** ; on perd la seule copie de tout contenu non versé.
- Si on n'efface pas : des clés dorment dans les images (sans effet une fois révoquées) ; un coût de stockage faible,
  que je ne chiffre pas faute de l'avoir lu sur la console ; du matériel d'attaque au repos dans un projet privé.

**Options.**
- (a) Effacer maintenant. Avantage : nœud fermé, clés des images détruites. Inconvénient : contraire à « récupérer ce
  qui est récupérable » tant que la couverture des contenus n'est pas prouvée.
- (b) Révoquer les clés d'abord, prouver la couverture, verser ce qui manque, puis effacer. Avantage : rien de perdu,
  et l'urgence tombe dès la révocation. Inconvénient : deux à trois jours de plus, peut-être un petit serveur à payer.
- (c) Garder sans date. Avantage : aucun risque de perte. Inconvénient : nœud qui traîne de passation en passation.

**Recommandation : (b). Confiance : moyenne-haute.** Si le contrôle de couverture rend une liste vide, effacer aussitôt.

**Qui, dans quel ordre.**
1. Lazar : les clés (nœud 2). Une fois révoquées, les images ne donnent plus aucun accès.
2. La session fille de l'attaquant informé : contrôle de couverture par programme, **sans rien lire** — à partir des
   index scellés des quatre inventaires, pour chaque fichier hors des classes reconstituables (environnement Python,
   système), chercher un fichier de même empreinte sur une branche du dépôt. Sortie : la liste des fichiers sans copie,
   noms et empreintes seulement, chemins cloisonnés filtrés d'abord. Aucune dépense.
3. Si la liste n'est pas vide et vaut d'être gardée : un serveur monté depuis l'image, versement scellé sur la branche
   de l'attaquant (jamais `main`, mot « go a » du 21 novembre), secrets exclus par le filtre de l'inventaire v6. C'est
   une dépense : mot de Lazar et ligne de GO avant.
4. **Lazar seul** : son mot, puis, image par image et par identifiant, retrait de la protection, effacement, absence
   relue (404), ligne au registre des arrêts.

**À ne pas confondre.** La passation de 16:45Z (`f8487d8e…`) écrit que « l'effacement » de quatre machines arrêtées chez
le loueur de cartes (58936096, 58936099, 58936100, 60988826) est ce nœud. Ce n'est pas le même objet : trois de ces
machines sont notées « intouchables » dans la passation `43301c3f…`. Ce nœud ne les vise pas.

---

## Nœud 2 — Révocation des clés

**Décision.** Révoquer les cinq clés listées, plus le jeton Hugging Face des postes, en **remplaçant** celles qui
servent encore.

| Clé | Où elle traîne | Sert encore ? | Geste | Précaution avant |
|---|---|---|---|---|
| Clé de déploiement du témoin (écriture sur le dépôt) | quatre images ; données de démarrage des serveurs détruits | non, depuis le 19 novembre 15:28Z (`f16b5d02…`) | la supprimer dans les réglages du dépôt sur GitHub | lire son nom et sa date de dernière utilisation ; s'assurer que les machines de la formation du barreau 5 ne poussent pas avec elle |
| Clé SSH 1864483 du compte du loueur | compte du loueur ; images | non (postes détruits) | la supprimer dans la console du loueur | même contrôle : aucun lanceur en cours ne l'emploie |
| Jeton GitHub du témoin | images ; données de démarrage | non (témoin clos) | le révoquer sur GitHub | date de dernière utilisation |
| Clé restreinte de l'instance 61170458 | historique de la branche (commit `2a1c0ff9`) | l'instance est détruite depuis le 19 novembre 10:09:26Z | regarder la liste des clés du compte ; la supprimer si elle y est encore | aucune ; consigner ce qui est vu |
| Clé du compte du loueur, collée en clair deux fois dans une conversation (19 novembre vers 16:40Z) | transcription de cette conversation ; secret réseau d'un environnement | **très probablement oui** | **remplacement** : en créer une neuve, la saisir par le formulaire sécurisé dans chaque environnement qui loue des cartes, vérifier un inventaire, puis supprimer l'ancienne | aucune machine en marche, aucune course lancée |
| **Oubli** : jeton Hugging Face des postes | images (`bc6342d7…`) | à vérifier | le remplacer | savoir quelles courses le lisent |

**Enjeu.**
- Si on n'agit pas : la clé du compte permet de louer et de dépenser ; la clé de déploiement et le jeton permettent
  d'écrire sur le dépôt privé, branches du bras comprises. Les pièces scellées restent vérifiables par leurs empreintes
  déposées chez le tiers, mais une écriture non voulue coûterait des heures de contrôle.
- Si on agit mal : couper une clé partagée pendant une course, c'est une machine payée qui ne peut plus verser ses
  sorties, ou un orchestrateur qui ne peut plus détruire sa machine.
- Réversibilité : une clé révoquée ne revient pas, mais une neuve se crée en quelques minutes.

**Options.**
- (a) Tout en une séance, maintenant. Avantage : exposition fermée ce soir. Inconvénient : risque de casser la
  formation du barreau 5, la relecture ou la répétition générale si une clé est partagée.
- (b) En deux temps : les quatre clés qui ne servent plus maintenant ; la clé du compte du loueur (et le jeton Hugging
  Face s'il sert) à la première fenêtre sans machine en marche. Avantage : rien de cassé. Inconvénient : la clé la plus
  grave reste exposée quelques heures ou jours de plus.
- (c) Tout attendre jusqu'à la fin de la formation du barreau 5. Avantage : aucun risque pour la course. Inconvénient :
  exposition prolongée sans raison pour quatre clés que plus rien n'emploie.

**Recommandation : (b). Confiance : haute.** Pour la clé du compte : à la première fenêtre calme, et d'ici là garder la
recharge automatique coupée et relire l'historique de facturation depuis le 19 novembre pour toute machine inconnue.

**Qui, dans quel ordre.** **Lazar seul**, dans les consoles ; aucune session ne voit une valeur. Ordre : (1) les quatre
clés sans usage, dix minutes ; (2) le constat sur la clé restreinte ; (3) le remplacement de la clé du compte à la
fenêtre calme ; (4) une session relit un inventaire en lecture seule pour prouver que la clé neuve marche, et la mère
consigne une ligne par clé : nom, identifiant, heure, jamais de valeur. Pour compléter la liste, la session fille peut
tirer des index d'inventaire les **noms** des fichiers de secrets de chaque image, sans les ouvrir.

---

## Nœud 3 — Purge de l'historique (commit `2a1c0ff9`)

**Décision.** Réécrire ou non l'historique de la branche `claude/compassionate-meitner-d4ryyk` pour en retirer le commit
qui a versé la clé restreinte de l'instance.

**Ce que j'ai vérifié, sans ouvrir le commit.**
- Commit du 19 novembre 09:42:55Z, « poste d'inventaire de l'instance : passe 1 ». Dans ma copie locale, **une seule**
  branche distante le porte ; il n'est pas dans `main` ni dans `claude/loving-lamport-7ol5ws`. À relire sur le dépôt
  distant le jour d'un geste.
- Aucun fichier de ce nom en tête des trois branches : il a été retiré le jour même (`3cff0a89…`).
- Ce n'est pas la clé du compte : empreinte comparée par la session du témoin, sans affichage (`3cff0a89…`).
- La copie publique est faite d'un seul commit tiré d'un commit cité (en-tête de `scripts/depot_expurge.py`) : par
  construction, l'historique ne sort pas.

**Enjeu.**
- Si on purge : poussée forcée sur une branche qui porte les pièces scellées du bras et du témoin. Tous les commits
  postérieurs changent d'identifiant ; ceux que citent des passations scellées et le registre des arrêts (`c04d6a35`,
  `351a6d16`, `7dfda0cf`, `8344310a`) ne se résolvent plus. Et la purge reste incomplète : chaque copie locale garde le
  commit (la mienne aussi), et GitHub le garde tant que son assistance ne l'a pas retiré, ce qui est un contact externe.
- Si on ne purge pas : une clé morte reste lisible par qui lit le dépôt privé, sans dommage possible si sa mort est
  constatée ; environ 308 Mio de bibliothèques Python alourdissent cette branche.

**Options.**
- (a) Ne pas purger. Constater la mort de la clé (nœud 2), le consigner, garder la branche comme archive : jamais
  fusionnée, jamais source de la copie publique. Avantage : provenance intacte, aucun geste destructeur. Inconvénient :
  la trace reste.
- (b) Purger : branche réécrite sous un nom neuf, ancienne supprimée, demande à l'assistance de GitHub. Avantage :
  trace réduite. Inconvénient : provenance cassée, contact externe, résultat incomplet.
- (c) Ne purger que si la console montre la clé encore vivante. Inconvénient : dans ce cas la révocation suffit, et la
  purge n'ajoute rien.

**Recommandation : (a). Confiance : haute**, sous la condition que la mort de la clé soit constatée. La révocation rend
la purge inutile ; la purge sans révocation ne protège pas.

**Qui, dans quel ordre.** Aucun geste destructeur. Lazar : le constat en console. La mère, si elle le veut : ajouter au
programme d'expurgation le retrait `runs/**/versement-instance-*/**` demandé par la note d'incident (je ne l'y ai pas
trouvé), comme ceinture ; c'est une pièce d'instrument, contre-lue par un autre modèle.

---

## Nœud 4 — Pièce 4 : projet de courriel de réplication extérieure, v4

**Décision.** Que faire du projet de courriel qui invite une équipe extérieure à attaquer nos moniteurs gelés.

**Ce que disent les pièces.** Le courriel v4 (`3f1121f5…`) se dit lui-même « non envoyable tel quel » : 18 points « À
décider », 11 points « À remplir », des crochets. La réplication vient après le gel des moniteurs (troisième scellement
du bras), qui n'est pas fait ; le deuxième non plus. Sa phrase sur la revue de sécurité externe est à retirer tant
qu'aucune pièce écrite n'existe (point 13). Depuis le 18 novembre, le terrain a bougé : les six garde-fous
(GO-2026-11-20-50), la porte G0 reportée à fin décembre, l'équipe de Bailey en contact avec toi (condition
d'indépendance du plan, section 3.2), trois chantiers actifs au plus.

**Enjeu.**
- Si on envoie : contact externe, irréversible ; le courriel annonce une dépense (accès en requêtes) et un calendrier
  qui dépend de portes non franchies.
- Si on n'agit pas : rien n'est perdu, il n'y a encore rien à attaquer. Seul coût : trouver une équipe prend des
  semaines, et ce délai ne commence pas.

**Options.**
- (a) Geler : la v4 reste archivée comme projet non envoyable ; une v5 est écrite au gel des moniteurs, avec les
  décisions des 20 et 21 novembre. Avantage : aucune de tes heures dépensée sur 18 points qui peuvent changer.
  Inconvénient : le délai de recherche d'une équipe court plus tard.
- (b) Trancher maintenant les 18 points pour tenir un courriel prêt. Avantage : envoi le jour du gel. Inconvénient : une
  à deux heures de toi, sur un texte que le nœud 5 et la porte G1 peuvent encore déplacer.
- (c) Une version courte, « contexte seul », envoyée autour de l'entretien du 1er décembre. Avantage : sonde l'intérêt
  d'une équipe. Inconvénient : contact externe avant que la règle de sortie soit fixée.

**Recommandation : (a). Confiance : haute.** À l'entretien, tu peux demander de vive voix qui serait une bonne équipe
indépendante, sans rien remettre : c'est ton contact, et cela fait courir le délai sans engager de texte.

**Qui, dans quel ordre.** Aucun geste. La session fille inscrit une ligne : « pièce 4 gelée jusqu'au troisième
scellement ». À la réouverture : rédaction de la v5 par Fable, contre-lecture par Opus, envoi par Lazar seul.

---

## Nœud 5 — Revue de sécurité externe, encore notée « ouverte »

**Décision.** Dire par écrit ce que la revue de sécurité externe garde comme porte pour le bras d'attaque, et lui
donner un périmètre et une échéance.

**Ce que disent les pièces.** Deux régimes coexistent.
- Pour le bras d'attaque : GO-2026-10-28-04 fait attendre la revue à « tout pipeline opérationnel », construction et
  exécution d'organismes évadeurs comprises ; N-057 (point 4) ne la lève pas ; GO-2026-11-19-96 la dit inchangée.
- Pour la course « nouvelles attaques » : ton « non » du 20 novembre (GO-2026-11-20-46, point 8), puis six garde-fous
  internes à la place de la revue pour la mesure interne, la revue restant fixée avant toute sortie hors quarantaine
  (GO-2026-11-20-50, repris par GO-2026-11-21-17 et -19).
- Aucune pièce écrite de cette revue n'existe : ni relecteur, ni périmètre, ni date (plan `d3991222…`, section 4.2).

« Ouverte » cache donc une contradiction : à la lettre, la mesure du bras contre les moniteurs gelés, dont la porte G1 a
besoin, attend un relecteur que personne n'a désigné.

**Enjeu.**
- Si rien n'est dit : soit le bras est bloqué sans fin, soit il est mesuré en écart silencieux à une porte inscrite, ce
  qui est le pire des deux.
- Si la revue est levée partout : plus aucun regard hors de toi et de Claude sur le travail offensif, alors que les
  modes inédits sont justement ce qui ajoute du risque.
- Réversibilité : un mot écrit se reprend ; un procédé sorti ne se reprend pas.

**Options.**
- (a) Garder la porte du 28 octobre telle quelle pour le bras : revue avant toute exécution. Avantage : le plus sûr.
  Inconvénient : bloque la mesure de G1 pendant des semaines ; contact externe à ouvrir.
- (b) Étendre au bras les six garde-fous : mesure interne en quarantaine, sur banc scellé, sans revue ; revue avant toute
  sortie. Avantage : un seul régime, cohérent avec ton non du 20 novembre. Inconvénient : la revue reste un mot sans
  objet.
- (c) L'option (b), plus une existence donnée à la revue : un périmètre d'une page (ce que le relecteur lit : règle de
  quarantaine, journal des accès, réponses du lecteur « sert-il à autre chose que mesurer ? », liste des sorties prévues ;
  jamais un procédé, sauf lecture sur place sous le séquestre du plan) ; la liste des déclencheurs (papier, billet, dépôt
  public, partage, courriel de la pièce 4 s'il porte plus que du contexte, matière d'entretien) ; une date pour désigner
  le relecteur, au plus tard avant la soumission du verdict de G1. Et un fil d'alarme : un procédé qui marche hors du
  banc, sur une surveillance réelle, remet la revue avant tout nouvel usage.

**Recommandation : (c). Confiance : moyenne-haute.** C'est mon avis du 20 novembre (`ee3e04b3…`), étendu au bras.

**Qui, dans quel ordre.** Lazar dit le mot (c'est la modification d'une porte, donc un nœud) ; la mère inscrit la ligne
de GO et remplace « ouverte » dans les registres par le statut exact ; Fable rédige le périmètre d'une page, Opus le
contre-lit ; **Lazar seul** choisit et contacte le relecteur.

---

## Ordre d'ensemble

1. Lazar : les quatre clés sans usage et le constat sur la clé restreinte (dix minutes, ce soir ou demain).
2. Lazar : trois mots — pas de purge (nœud 3), courriel gelé (nœud 4), option (c) pour la revue (nœud 5).
3. La session fille : le contrôle de couverture des images, gratuit.
4. Lazar : remplacement de la clé du compte du loueur et du jeton Hugging Face, à la première fenêtre sans machine.
5. Lazar : effacement des quatre images, après les points 1, 3 et 4.

## Ce que je n'ai pas vérifié

- Aucune console lue : ni l'état réel des clés, ni le prix du stockage, ni la protection des images.
- Que la clé de déploiement et la clé SSH du témoin ne servent à aucune course en cours : à lire par Lazar sur leur date
  de dernière utilisation.
- Que les 74 fichiers de la sauvegarde vivent, ou non, sur une branche : c'est l'objet du contrôle de couverture.
- Que le commit `2a1c0ff9` n'est porté par aucune autre branche du dépôt distant : vu sur ma copie locale seulement.
- Les textes du bras d'attaque (règle, témoin, mandat du deuxième scellement) : non lus, par cloisonnement.
