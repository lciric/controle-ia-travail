# Décision de Lazar — durée des courses : 2 h pour le second pilote ; reprise par génération d'abord pour les courses longues, Vast seulement à défaut (v1, à inscrire)

- **Mot de Lazar**, 25 octobre 2026, 14:39 (heure de Paris), dans la session de conv-audit : « ok inscris-le dans journal
  et programme », sur la recommandation : « garder 2 h pour ce pilote ; pour les courses longues, étudier d'abord la
  reprise par génération, et Vast seulement si elle n'est pas faisable ».
- **Le fait qui motive la décision** : une course tourne dans une seule commande de fond de la session qui lance ; l'outil
  arrête toute commande de fond au plus tard après 7 200 s, sans réglage ; un processus détaché est arrêté peu après la
  fin du tour de la session. Le second pilote (texte scellé `pilote2-gemini-organisme-v5-2-v2.md`, `d2944654…`) tient
  sous cette borne : 2 400 s par génération, pire cas d'un appel du lanceur ≈ 6 900 s.
- **Ce qui est décidé** :
  1. Le second pilote garde sa borne (2 400 s par génération, une course par commande) ; rien ne change à son texte scellé.
  2. Pour les **courses longues** (rondes de conception, organismes v5.3 et v6, étapes suivantes du programme gradient),
     on étudie d'abord la **reprise par génération** : une commande par génération, le noyau reprenant la course depuis
     son archive, sans changer la mesure.
  3. **Vast** (ou toute machine louée sans cette borne) seulement si la reprise par génération n'est pas faisable ; cela
     demandera alors un GO de dépense, la vérification de `unshare` sur la machine, et une décision sur le passage des
     clés à recharge automatique sur une machine louée.
- **Ce que « étudier » recouvre** (proposition de conv-audit, travail sur processeur, routine) : lire le noyau (relance,
  archive, manifeste, dérivation des graines, plafonds cumulés, bras gelé et juge) pour dire si une reprise entre deux
  générations est déjà possible sans changer la mesure ; sinon, écrire la fonction de reprise avec ses essais — cas sain :
  course coupée entre deux générations puis reprise = course d'une traite (relevés mécaniques identiques en simulation) ;
  artefacts : archive altérée, reprise sous un autre code, reprise d'une course finie, double reprise (R3), plafond total
  dépassé par la somme des reprises. Toute modification du noyau passe par la fusion de session-depot et par le
  préenregistrement des courses qui s'en servent.
- **Ce qui ne change pas** : l'étape 1 scellée (v9) et son lanceur ; le pilote qui part ; les règles R1 à R14.
