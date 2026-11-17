# Addendum 7 au préenregistrement du témoin de Bailey (`prereg/temoin-attaque-publiee-bailey-v1.md`, `fb6c2f34…`) — run de confirmation au régime complet (72 tours), décidé avant la lecture du verdict à 36 tours

16-17 novembre 2026, scellé après contre-lecture (R2). Session « attaquant informé » (`session_01XJ6MgnEhQMZteN9F8a1BST`),
branche `claude/compassionate-meitner-d4ryyk`. Brouillons archivés tels quels (R12) :
`brouillons/temoin-attaque-publiee-bailey-v1-addendum-7-run-de-confirmation-brouillon1.md` et `…-brouillon2.md` (contre-lu). Le préenregistrement et ses
addenda 1 à 6 restent tels quels ; en cas de conflit, le préenregistrement prime et l'écart est un nœud. **Écrit et à
sceller avant toute lecture du verdict à 36 tours** : aucune note de sonde ni de juge n'a été lue, par aucune session.

## 1. Pourquoi
La relance seule (addenda 5 et 6) a fini le 15 novembre vers 11:52Z par la garde de dépense (D = 73,026 USD sur B = 75) :
**36 tours complets**, aucune garde tombée, transfert complet, instance détruite
(`runs/temoin-bailey-v1-20261111/sortie-conduite-v13/bilan-conduite-v5.json`). Dossier de lecture assemblé :
`runs/temoin-bailey-v1-20261111/lecture-assemblee-v1/` (45 fichiers scellés vérifiés le 16 novembre). Le texte lit ce run
comme un run tronqué de K′ = 36 tours, au régime réduit (l. 165, 332, 338). Le verdict n'est pas lancé.

Choix soumis à Lazar avant toute lecture (note `registres/passations/2026-11-16-…-bailey-choix-1-suspendu-question-ordre.md`) ;
mot de Lazar, verbatim : « go 2 puis 1 » (note `…-decision-lazar-bailey-2-puis-1.md`) : (i) cet addendum, scellé ;
(ii) puis le verdict à 36 tours (R13) ; (iii) puis un run neuf de 72 tours, au régime publié.

**Lenteur de la relance** (champs techniques seulement) : tours 0 à 35 de 36,5 à 132,8 min
(`principal-relance/transfert-1/sortie-durees-v3.jsonl`, `6c445f3e…`) : croissance presque régulière des tours 0 à 29
(36,5 à 127,2 min), puis tours 30, 33, 34 et 35 plus courts (72,3 ; 66,8 ; 45,2 ; 46,8 min) ; 48,7 h pour 36 tours ;
tours 0 et 1 : 2 187,1 et 2 365,6 s (moyenne 2 276,4 s). Tours 0 à 7 de la première exécution de la série 3, sur une
autre machine (Texas, offre 59431043), 21,7 à 26,4 min, sans croissance sur ces huit tours (`9ff59e4b…`) ; t du
pilote de la série 3 : 1 315,99 s (`pilote/transfert-1/sortie-durees-v3.jsonl`, `2cac2458…`).
Diagnostic en lecture seule du 15 novembre (`runs/temoin-bailey-v1-20261111/diagnostic-hetzner-v1-sortie.txt`, `9a879463…`) :
processus d'exécution à 576 % de processeur, carte à 0 % ; ≈ 16 min entre la sauvegarde d'une sonde et celle des
paramètres, ≈ 1 h 30 entre ces paramètres et la sonde suivante : la partie lente est sur le processeur (lecture de la session, non établie : l'entraînement de la sonde sur la banque
qui grossit, ou une charge variable de l'hôte — charge moyenne 16,3 au diagnostic ; tours 30 à 35 plus courts). La
machine du Texas (AMD EPYC 7V12, 32 cœurs effectifs, 2,45 GHz) est louable le 16 novembre (offre 59431043,
1,108 USD/h) : relevé `runs/temoin-bailey-v1-20261111/releve-offres-processeur-20261117-0025.txt` (`a902256b…`) : offre 59431043 à 1,2576 USD/h carte et 110 Go de stockage compris (1,108 USD/h la carte seule) ; même processeur sur la machine 154960 (Oregon, offre 57349463, 1,255 USD/h). Les
caractéristiques du processeur de la machine de la relance (Suède, offre 58516569, `offre-choisie-v12.json`,
`972928bb…`) ne sont pas relevées : rien n'établit que le filtre du § 2.4 l'aurait exclue.

## 2. Écarts : principe décidé par Lazar (« go 2 puis 1 ») ; B = 85 par son mot du 17 novembre (ligne de GO) ; plafond de durée, filtre et crédit : calcul de la session, soumis à Lazar avec la demande du mot de lancement (condition 7), dont le mot les accepte
1. **Run de confirmation (écart à R3, [T] l. 69-71, à la liste d'arrêt, et à l'addendum 4, § 2.2, et à l'addendum 5, § 4 : une série nouvelle après la relance, sur nouvelle décision de Lazar et par cet addendum).** Une série neuve,
   **décidée et scellée avant toute lecture** : ce qui la rend compatible avec l'objet de R3 (aucun résultat connu ne
   la motive ; elle est engagée quel que soit le verdict à 36 tours). Tout du texte s'applique sans changement :
   hypothèse, prédictions, métriques, seuils, population, juge, modèle, bras, graines (pilote 1394228342, run principal
   1865327867), critères de lecture gelés, liste d'arrêt (pilote, au plus une reprise ; règle ; run principal ; au plus
   une relance), audit de symétrie. Code : celui de l'addendum 5, plus la garde du point 3.
2. **Poste neuf, B neuf (écart au texte, l. 249-251 et 374).** La série de confirmation est un poste neuf : D compte de
   zéro à sa première instance ; **B = 85 USD**, garde à B − 2. Pourquoi 85 : la règle donne K = 72 dès que
   c ≤ 1,6 USD/h (carte et stockage, borne du § 2.4), t ≤ 1 800 s (garde du § 2.3) et D ≤ 8,7 USD au calcul
   (`analyse_v3.nombre_de_tours(85, 8, 1.6, 1800)` : H = 41,9 h, K = 72 ; K = 71 tant que D ≤ 9,6 USD). La garde B − 2
   laisse ≈ 70 h de run à 1,11 USD/h. Au-delà de 1,6 USD/h, la règle peut donner K < 71 (c = 1,8, D = 5, t = 1 800 :
   K = 67), d'où la borne de coût du § 2.4. Les séries 1 à 3 et la relance gardent leur B = 75 et leur D
   (73,026 USD) ; la dépense cumulée du témoin devient au plus ≈ 73 + 84,5 USD.
3. **Garde neuve : durée de tour du pilote** (code `lanceur_v21`, `Conduite(t_max_pilote_s=1800)`) : après la règle,
   si t (moyenne des durées des tours 0 et 1 du pilote, la même que la règle) dépasse **1 800 s**, arrêt avant le run
   principal, transfert, destruction. Cette garde n'ouvre pas la reprise du pilote du texte (l. 243-245, 366 : elle se
   referait sur le même hôte) ; sa chute met fin à la série de confirmation, rapportée « confirmation non courue
   (garde de durée du pilote) », avec t. Aucune nouvelle tentative sans nouvelle décision de Lazar et nouvel addendum,
   qui diraient qu'ils sont postérieurs à la lecture du verdict à 36 tours. Pourquoi 1 800 : entre le t du pilote de la
   série 3 (1 315,99 s ; 1 800 ≈ 1,368 × t) et le t qu'aurait eu la relance (2 276,4 s), que la garde aurait arrêtée.
   Perte en cas de chute : mise en place, contrôle du juge et trois tours de pilote (≈ 3 h, ≈ 3 à 5 USD sur un hôte
   comme celui de la relance), doublée si le pilote a été repris pour une autre cause ; aucune garde ne la borne avant
   la fin du pilote, hors B − 2.
4. **Filtre d'offre** (paramètre de lancement, déclaré) : celui du poste v12 (`poste-hetzner-v12.sh`, l. 143), plus
   `cpu_cores_effective >= 32`, `cpu_ghz >= 2.4`, et un coût, carte et 110 Go de stockage (grandeur `cout` du choix
   d'offre), d'au plus 1,6 USD/h ; offre la moins chère qui passe. Disque 110 Go. Ce filtre est une préférence : il
   n'est pas établi qu'il exclue la machine de la relance ; le contrôle est la garde du § 2.3. Aucune offre conforme
   en 24 h : rien ne tourne ; « confirmation non lancée », rapportée avec sa cause.
5. **Crédit (comme la condition 9′ de l'addendum 6)** : avant la création, crédit ≥ S = 14 h × (max(1,7 ; c₀) + o) et
   ≥ 25 USD, recharge automatique configurée ; 14 h ≥ mise en place ≤ 0,75 h + pilote ≤ 1,5 h + 20 tours × 1 800 s
   × 1,15 = 11,5 h (total 13,75 h) ; relevé consigné dans l'ordre de lancement. Un hôte à t = 1 800 s qui croîtrait
   comme la relance mettrait ≈ 17,3 h pour ses 20 premiers tours : la recharge automatique couvre l'écart (risque (c)).

## 2 bis. Devis (demandé par le mot de Lazar du 16 novembre ; s'ajoute au devis v4, qu'il ne remplace pas)
Hors poste Hetzner. Hôte comme celui du Texas (pilote t = 1 316 s ; tours 0 à 7 de 1 299 à 1 586 s, moyenne 1 411 s,
sans croissance sur huit tours) : mise en place et contrôle du juge ≤ 0,75 h, pilote ≈ 1,1 h, 72 tours ≈ 28,2 h
(32,5 h avec la marge de 1,15) : ≈ 30 à 34 h, ≈ 33 à 38 USD à 1,108 USD/h (carte seule), ≈ 38 à 43 USD à 1,258 USD/h (carte et
stockage, offre du Texas relevée le 17 novembre). Hôte à t = 1 800 s qui croîtrait comme la
relance (≈ 180 s par tour, mise à l'échelle 1 800/2 276) : arrêt à B − 2 vers 48 tours complets à 1,108 USD/h, vers
39 à 1,6 USD/h (régime réduit). Dépense maximale : B − 0,5 = 84,5 USD (seuil de secours). Dépense cumulée du témoin :
73,03 USD (séries 1 à 3 et relance) plus 33 à 84,5 USD. Tirage sur la carte : la dépense moins le crédit initial, par
recharges de 5 USD (≈ une toutes les 3 à 4,5 h selon le taux).

## 3. Lecture (fixée maintenant, avant toute lecture)
- **Verdict à 36 tours** (étape « 1 » de Lazar) : prononcé d'abord, par un lecteur neuf (R13), sur
  `lecture-assemblee-v1`, avec les critères gelés ; c'est le verdict du texte pour les séries 1 à 3 et la relance
  (K′ = 36, l. 332, 338). Il ne change ni la décision de lancer la confirmation, ni ses pièces, ni sa lecture. Seule
  exception, fixée maintenant : si cette lecture établit un défaut technique d'un code que la confirmation emploie
  (lanceur, instance, exécution, journaliseur, lecture), la confirmation n'est pas lancée avec ce code ; nœud ; toute
  correction passe par un addendum neuf, qui dit qu'il est écrit après cette lecture.
- **Verdict de confirmation** : par un lecteur neuf (R13), qui n'est pas celui du verdict à 36 tours, sur la sortie de
  la conduite de confirmation, avec les mêmes critères gelés (`lecture_v8.valider`, `lire` avec
  `analyse_v3.graines()["reechantillonnage"]`, audit de symétrie). K′ y désigne le nombre de tours complets de
  l'exécution qui porte le verdict de la confirmation (sa relance, s'il y en a une, l. 371).
- **Rapport** : les deux verdicts, côte à côte, chacun avec son K′ et son régime ; leur accord ou leur désaccord est
  rapporté tel quel ; aucune mise en commun des notes. **Verdict retenu pour l'étape 1** (nœud 5, option (c),
  inchangée ; formule publique « attaque publiée reproduite sur le banc des auteurs », au régime publié ou « sur
  K tours ») : si la confirmation compte K′ ≥ 71, son verdict, quel qu'il soit (« effet reproduit », « effet non
  reproduit » ou « non interprétable »), est retenu, au régime publié ; le verdict à 36 tours reste rapporté comme la
  lecture prévue au régime réduit. Dans tous les autres cas (confirmation non lancée ou non courue, pas de run
  principal, pas de verdict, ou K′ ≤ 70, quelle qu'en soit la cause), le verdict retenu est celui à 36 tours ; la
  confirmation est rapportée avec sa cause, selon la table des critères gelés (l. 329-338). Ce que vaut l'étape 1 pour
  le témoin de [Règle] ne change pas (l. 340 ; nœud 5, option (c)).
- Contrôle du juge hors seuil à la mise en place de la confirmation : pas de run, pas de verdict de confirmation
  (l. 365) ; il est rapporté à côté du verdict à 36 tours, comme réserve, sans le changer.
- Aucune autre série sans nouvelle décision de Lazar et nouvel addendum.
- Information, sans effet sur la lecture : le rapport donne le premier tour où les empreintes de suffixe de la
  confirmation diffèrent de celles de la relance (graines identiques).

## 4. Code, essais
`lanceur_v21` (= `lanceur_v20` plus la garde du point 3 ;
`75cf4049c61d81439989ad11f4f8370ef9c7b16a1257c881245f0efbd8dbaf02`), au commit `873ab00ca5eaaaa00c84c9ae9f0bd53fef6435e5` ; instance (`instance_v16`), exécution
(`execution_v4`), lecture (`lecture_v8`), journaliseur, conventions, analyse : inchangés. Manifeste neuf
`manifeste-local-v7.json`, écrit après l'inscription de la ligne de GO (il porte son identifiant) : seules différences avec
le v6 : `B` (85), `commit_code`, `go_id`. Essais :
`tests/test_temoin_bailey_condition6_v21.py` (`36573ae2…`) : les essais v20 rejoués, plus la garde (sous le plafond :
run principal ; plafond atteint : passe ; au-dessus : arrêt avant le run principal, instance détruite ; sans plafond :
rien ne change) ; avec `tests/test_temoin_bailey_reprise_relance_v1.py` : 227 passés, 1 sauté (configurations publiques
non fournies). La valeur par défaut `t_max_pilote_s=None` désarme la garde : la conduite v15 refuse de partir si la valeur n'est pas
exactement 1 800, et l'ordre de lancement la consigne. Si la garde tombe, le manifeste « règle » n'est pas écrit :
B, R, D, c, t, H et K sont au bilan et dans le dossier `regle` transféré.
Essais complémentaires (M-9 de la contre-lecture) : `tests/test_temoin_bailey_condition6_v21_complements.py`
(pilote repris pour une autre cause, puis garde ; t non fini). Pièces de lancement, écrites après l'inscription du GO (elles portent son identifiant), contre-lues (R2)
et scellées avant le lancement : conduite `lancer-conduite-v15.py` = `lancer-conduite-v13.py` sans `relance_seule`,
avec `lanceur_v21`, `t_max_pilote_s=1800`, aucune instance antérieure, le manifeste v7 et le GO neuf ; poste
`poste-hetzner-v13.sh` et son constructeur = le poste v12 avec la conduite v15, le filtre du point 4 et la garde du
commit `873ab00c`.

## 5. Risques déclarés
- (a) l'hypothèse « processeur » n'est pas établie ; la vitesse d'un hôte peut changer après le pilote, par croissance
  (relance, tours 0 à 29) ou par une charge variable de l'hôte (relance, tours 30 à 35 plus courts ; non établi). La
  garde B − 2 tronque alors le run : à t = 1 800 s avec la croissance de la relance, ≈ 48 tours à 1,108 USD/h, ≈ 39 à
  1,6 USD/h (régime réduit, lu si K′ ≥ 20). Inversement, la garde du § 2.3 peut arrêter un hôte lent au seul moment du
  pilote, ou un hôte stable entre 1 800 et ≈ 2 700 s que la règle aurait laissé finir 72 tours : perte du § 2.3,
  confirmation non courue ;
- (b) la machine du Texas peut ne plus être louable ; une autre machine qui passe le filtre n'a pas été éprouvée ;
- (c) ce que l'addendum 6 déclarait pour le crédit et la recharge automatique (carte de Lazar, compte partagé avec
  d'autres chantiers) vaut ici ;
- (d) graines identiques à celles du texte : la confirmation n'est pas un réplicat indépendant de la relance ; elle teste
  le même protocole au régime publié (choix de rester dans le texte : changer les graines serait un écart de plus).

## 6. Conditions de lancement et ordre
Celles du texte et de l'addendum 5, avec :
- condition 2 : une **ligne de GO neuve sur `main`** (mot de Lazar du 17 novembre,
  `registres/passations/2026-11-17-0008-decision-lazar-bailey-ligne-go-main.md`, `546aa0bc…`), de type « calcul »,
  d'identifiant `GO-AAAA-MM-JJ-NN`. Son objet cite le texte (`fb6c2f34`), le devis v4 (`f9c8c66e`) et cet addendum par
  son empreinte, et fixe « (B = 85, garde d'horloge à B − 2) ». Plafond 90 USD ≥ B ; les 5 USD au-delà de B ne sont engagés par aucune conduite : ils couvrent l'écart
  entre le compte prudent et la facture, et une reprise éventuelle (lecture 38) après un arrêt à B − 2 ; toute
  dépense au-delà de B : nœud. Échéance 2026-11-30 : création au plus tard à l'échéance moins ((B − 0,5)/c + 1) h (`verifier_echeance`),
  soit vers le 27 novembre 17:44Z à c = 1,108 USD/h, vers le 28 novembre 02:50Z à c = 1,258 USD/h ; au-delà,
  une ligne neuve ;
- condition 5 : nœud 5, option (c), inchangée ;
- condition 7 : le mot direct de Lazar pour le lancement ;
- condition 9′ : le § 2.5.

Ordre, sans autre étape :
1. cet addendum contre-lu et scellé ;
2. **avant la lecture du verdict à 36 tours** :
   - la ligne de GO inscrite sur `main` ;
   - les pièces de lancement écrites (conduite `lancer-conduite-v15.py`, poste `poste-hetzner-v13.sh` et son
     constructeur, manifeste v7). Elles sont contre-lues (R2) par un lecteur neuf, puis scellées. Ce lecteur vérifie
     qu'elles ne diffèrent de la conduite v13, du poste v12 et du manifeste v6 que par ce que cet addendum nomme :
     `lanceur_v21`, `t_max_pilote_s=1800` exigé, aucune `relance_seule`, aucune instance antérieure, B = 85, filtre
     du § 2.4, garde du commit `873ab00c`, GO neuf et empreinte de cet addendum vérifiée dans son objet ;
   - la demande du mot de lancement (condition 7) envoyée à Lazar, avec le § 2 bis, les risques du § 5 et le tirage
     attendu sur la carte ;
3. le verdict à 36 tours prononcé et scellé (R13) ;
4. crédit relevé (9′), mot de Lazar reçu, création.

Si une pièce de l'étape 2 ne peut être faite avant la lecture, elle est faite après, et le rapport le dit. Si la
confirmation n'est pas lancée (mot non donné, aucune offre, crédit, échéance, défaut du § 3), le rapport du témoin le
dit avec sa cause, et le verdict retenu reste celui à 36 tours.

## Contre-lecture
Rapport (R2) : `docs/notes/reproduction-attaque-publiee-v1/contre-lecture-addendum-7-confirmation-bailey-v1.md`
(`f1c2ca523da96dbeb3e989248ebac21c36f5fad853730613a5d5183513e5372c`), contre-lecteur neuf, sur le brouillon 2 :
« scellable après corrections », aucun bloquant. Textes de remplacement du rapport repris mot pour mot : § 1 (M-5),
§ 2 titre (M-8), § 2.1 à 2.5 (M-2, M-4, M-5, M-7, M-8), § 2 bis (M-6), § 3 (M-3, M-11), § 4 (M-9), § 5 (a) (M-7),
§ 6 (M-1, M-8, M-10). Compléments de la session : pièce du relevé du Texas (`a902256b…`) ; devis au taux carte et
stockage (1,258 USD/h) ; échéance de création à ce taux ; emploi des 5 USD au-delà de B ; information sur les empreintes
de suffixe (M-11, option) ; essais complémentaires (M-9).
