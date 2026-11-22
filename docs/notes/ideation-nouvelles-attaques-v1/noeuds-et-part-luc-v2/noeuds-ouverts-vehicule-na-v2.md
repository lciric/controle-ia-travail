# Nœuds ouverts du véhicule NA-1 et règle de repli de GO-2026-11-22-35 — v2

Pièce de travail (classe C), auteur Opus (celui de la v1), 2026-11-22. Processeur seul : aucun appel de modèle, aucun réseau, aucune clé lue, aucune dépense, aucune écriture dans un dépôt.

- **Version.** La v2 remplace la v1 (`noeuds-ouverts-vehicule-na-v1.md`, `c77536e8c4372ffe…`, non scellée, archivée sans changement), après la contre-lecture `B/noeuds-et-part-luc-v1/contre-lecture-v1/contre-lecture-noeuds-et-part-luc-v1.md` (`23e774f901624bb8…`, verdict « À corriger »). Elle porte aussi les décisions de la mère transmises avec la contre-lecture. Ce qui change est écrit au dernier paragraphe, « Différence avec la v1 ».
- **Décisions de la mère portées ici** (transmises par la coordinatrice, à inscrire au registre des décisions par la mère ; je ne les ai pas lues au registre) :
  - N1 et N2 : adaptateur Claude direct ;
  - N3 : contrôle d'empreinte du code chargé, plus la réserve déclarée ;
  - N4 : la garde commune de `main` ;
  - repli (i) : une fiche servie par repli s'attribue au **modèle servi**, est rapportée à part, et n'est jamais confondue avec l'espèce demandée ;
  - repli (ii) : le repli vaut aux lignes à part ;
  - repli (iii) : le pire est retenu **par tentative**.

Abréviations de chemins : **B** = `/home/user/controle-ia-travail/docs/notes/ideation-nouvelles-attaques-v1/` (branche `lot/compte-organisme-v1`) ; **M** = `/home/user/main-lecture/` (copie de `main`, HEAD `e5c0cb99`) ; **P** = `M/prereg/ideation-nouvelles-attaques-v1/`.

| pièce lue | empreinte |
|---|---|
| B/inventaire-depart-v1/inventaire-depart-course-nouvelles-attaques-v1.md | `5f647ceeeb47e86d…` |
| P/preenregistrement-court-course-nouvelles-attaques-v9.md (« V9 », scellé) | `864f39a7ecd41a61…` |
| P/additif-1-preenregistrement-court-v9-mode-tenu-a-l-ecart-et-retrait-espece-6-v5.md (« additif 1 », scellé) | `9f731795cd8b9166…` |
| P/complement-valeurs-preenregistrement-court-v9-lot-1-v3.md (« complément », scellé) | `b4ef87dc6d5cce13…` |
| P/additif-1-complement-valeurs-…-espece-3-sur-minuit-v2.md (« additif au complément », scellé) | `ce76e0d6a0a6e65f…` |
| P/devis-course-nouvelles-attaques-v11.md (« devis », scellé) | `205e08f23ef9ced9…` |
| B/conception-vehicule-v5/conception-vehicule-course-nouvelles-attaques-v5.md (non scellée) | `1b7f6822af20417e…` |
| B/lot-4-vehicule-na-v1/rapport-developpeur-lot-4-na-v1.md ; …/verification-v1/verification-lot-4-na-v1.md | `1b16fabb3f84b6d2…` ; `3c8d1aa2d67b45c2…` |
| B/lot-4-…/pole/appel_garde_na_v1.py ; …/pole/adaptateur_claude_na_v1.py | `d16d07bf9b10ea82…` ; `38baa2061d07f674…` |
| B/lot-6-vehicule-na-v3/reserve-modele-de-menace-lot-6-v3-v1.md ; …/pole/configuration_course_na_v1.py | `a92d3d4a9ef862bb…` ; `0264479234576b3b…` |
| B/audit-regle-appels-google-v1/ (deux audits) | `97c510f06b3e128d…` ; `c21b13d3c64f5665…` |
| B/noeuds-et-part-luc-v1/contre-lecture-v1/contre-lecture-noeuds-et-part-luc-v1.md | `23e774f901624bb8…` |
| M/src/controle_ia/garde_google_v3.py (compagnon OK) ; M/registres/go.md ; M/registres/decisions.md | — ; `49d801d0…` ; `518ff6fa…` |

## Verdict

Les quatre nœuds sont tranchés par la mère. Il reste à les écrire à l'additif du véhicule et à les construire.

Les nœuds 1 et 2 touchent des lignes scellées de la V9 : l. 73, 77 et 387 pour le premier, l. 384 pour le deuxième. Le troisième n'en touche aucune. Le quatrième touche le pire par appel (V9 l. 383 ; complément l. 166) pour les rôles servis par Google.

La règle de repli contredit la V9 l. 372. Avec la décision (i), elle touche aussi la composition et les mesures. La table R1 à R16 du § 5 dit chaque écart. **Avant l'additif, il faut deux mesures** :
- le pire d'un appel d'aiguilleur et de juge, par modèle (le modèle du rôle et chacun des deux modèles de repli) ;
- le pire d'un appel servi par Google sous la garde commune.

---

## 1. Règle « rien n'est ajouté à l'enveloppe » (D2) — décision N1 : adaptateur direct

**Énoncé et sources.**
- D2 : conception v5, l. 87 et l. 603. Le mot 5 de 07:46Z est à la conception l. 228 (« déclaré à l'additif comme transport, octet pour octet, ou refusé »).
- Constat : rapport du lot 4, l. 112 à 118. Un bloc « # Environment » de 1 052 à 1 080 octets, qui varie (dossier, budget, date) et qui porte des motifs de la garde. Un en-tête de facturation de 73 octets et une phrase d'identité de 62 octets.
- Vérification du lot 4, l. 57 à 63 : « D2 n'est pas tenue par l'adaptateur neuf seul ».

**Lignes scellées en jeu.**
- V9 l. 73 (« ni un renvoi interne (… chemin) »).
- V9 l. 77 (la requête assemblée est ce qui part, journalisée avant l'envoi).
- V9 l. 387 (« après elle, plus aucun octet ne change »).
- V9 l. 254 (l'enveloppe est une valeur de l'additif).

**Décision N1.** Un adaptateur neuf appelle l'interface des messages par le relais. Le relais n'admet que ce chemin : audit de l'orchestrateur, l. 21, sur `relais_reel_v2.py` l. 75. La consigne part seule, dans un message « user », sans champ système. Avec elle, les lignes 73, 77 et 387 tiennent sans écart. L'écart porte sur la conception v5, l. 225 (« adaptateur du même type »), qui n'est pas scellée ; il se déclare à l'additif. L'égalité porte sur la consigne extraite du corps reçu, comme le veut la conception l. 230.

**Les sept exigences du mandat du lot 4 v2** (contre-lecture, § 5.1 à 5.7). Chacune a son épreuve sur un cas sain et sur un artefact.

| n° | exigence | épreuve (artefact) |
|---|---|---|
| A1 | **Aucune relance cachée** : le client de l'interface est construit avec `max_retries=0`, écrit et vérifié au départ. Toute relance est une tentative du véhicule, journalisée. | Une erreur 529 simulée ne produit qu'**une** requête au faux fournisseur. |
| A2 | **Aucun repli du fournisseur** : ni le paramètre de repli côté serveur ni son en-tête bêta ne sont jamais envoyés. Le champ `model` de la réponse est comparé au modèle demandé de la tentative (contrôle A2). L'additif dit que GO-35 (« le repli que prévoit le fournisseur ») est rejoué côté client, visible et consigné. | Une requête qui porterait ce paramètre est refusée avant l'envoi ; une réponse dont le modèle diffère lève A2. |
| A3 | **Coût d'un refus compté** : une tentative refusée est comptée au cumul de la clé par son usage déclaré. Si l'usage manque, elle est comptée au pire réservé, jamais à zéro. Le relais v2 compte le refus comme un appel, au barème des deux modèles de repli. | Un refus avec usage non nul accroît le cumul ; un refus sans usage accroît le cumul du pire. |
| A4 | **Réponses brutes conservées par tentative**, refus compris : corps brut, raison d'arrêt, catégorie, modèle servi, usage. C'est la règle de la V9 l. 396 et de la conception l. 227, reprise de l'adaptateur v1 (docstring l. 16-20). | Conservation impossible : rien n'est rendu (comme v1) ; une chaîne de trois tentatives donne trois réponses conservées. |
| A5 | **Catégorie** lue au champ de détail de la raison d'arrêt. Sur les modèles de repli, elle peut manquer : l'issue attendue est alors « catégorie non lue », consignée. | Refus sans détail : ligne « catégorie non lue », jamais un vide. |
| A6 | **Liste fermée** : le repli ne s'ouvre **que** sur une raison d'arrêt lue égale à « refusal ». Un statut inconnu est une « réponse illisible », jamais rejouée. Cela remplace « tout autre refus » de `appel_garde_na_v1.py` l. 74. | Une raison d'arrêt inconnue ne déclenche aucun repli. |
| A7 | **Réglages non textuels par modèle**, écrits à l'additif : effort admis, réflexion, plafond de sortie. Le flux est obligatoire pour 128 000 jetons de sortie (rapport du lot 4, l. 120). Un réglage refusé par un modèle de repli serait une erreur 400 lue « cause non établie » : la configuration est contrôlée au départ. | Un réglage non admis pour un modèle de repli refuse le départ, avec son nom. |

## 2. Refus pour crédit d'amont invisible — décision N2 : adaptateur direct

**Énoncé et sources.**
- Rapport du lot 4, l. 134 (« Un refus pour crédit du compte en amont n'y paraît pas »), l. 125 (crédit, accès et réponse coupée rendus « `<synthetic>` ») et l. 126 (dix relances de l'outil).
- Code : `appel_garde_na_v1.py` l. 160-171 (`relais_montre_refus_credit`) et l. 430-441 (« cause non établie »).
- Vérification du lot 4, l. 79.

**Ligne scellée en jeu.** V9 l. 384, arrêt n° 13 : il est aujourd'hui impossible à lever.

**Décision N2.** L'adaptateur direct reçoit l'erreur d'amont telle quelle, avec son code et le type d'erreur de facturation, et la lève en arrêt n° 13, qui dit la clé. Il n'y a plus de message fabriqué par l'outil. L'additif écrit que le n° 13 garde sa lettre. Une erreur d'amont d'un autre type reste « cause non établie », comme le veut la conception l. 232 (mot 4). Épreuve : un refus pour crédit d'amont simulé par le faux fournisseur v2 lève le n° 13 ; une erreur d'accès simulée ne le lève pas.

## 3. Séparation par processus du lot 6 — décision N3 : empreinte du code chargé, plus la réserve déclarée

**Énoncé et sources.** Réserve du lot 6 v3, l. 5 à 11 : quatre contournements par modification du programme en marche ; « séparation par processus […] prévue au lot suivant » (l. 11). La vérification du lot 6 v3 (l. 24 et 65) propose le contrôle d'empreinte.

**Lignes scellées en jeu.** Aucune parmi les textes lus. L'additif de la matière première n'a pas été lu : la consigne l'interdit.

**Décision N3.**
- Au départ et à chaque génération, le lanceur (lot 8) calcule l'empreinte du fichier source de chaque module chargé, pris dans `sys.modules`, et la compare à la table d'empreintes du paquet. Il refuse tout import hors table après le départ.
- La réserve est déclarée à l'additif : ce contrôle ne voit pas une modification en mémoire. C'est le cas du `__code__` échangé et de la méthode de la colonne vidée, soit les cas 3 et 4 de la réserve.
- C'est un **écart à la décision antérieure de la mère** (« prévue au lot suivant »), à consigner comme tel.
- **Ce qu'il faut écrire comme constat, non comme citation** (contre-lecture, 1.4) : l'arrêt n° 21 (V9 l. 392) vise un « procédé exécuté hors du banc », pas le code d'un modèle. Que cette course n'exécute aucun code rendu par un modèle est un constat du lanceur : aucun import hors table, et aucun appel d'exécution de texte rendu. L'épreuve R5 le vérifie : un module planté hors table refuse le départ.

## 4. Règle d'appels Google — décision N4 : la garde commune de `main`

**Énoncé et sources.**
- La règle : `M/CLAUDE.md` l. 66-67 (GO-2026-11-21-71).
- La décision de faire un lot neuf : R-4655 (decisions.md l. 4794).
- Les deux audits concluent « non tenue ». Celui de l'orchestrateur relève à la l. 30 que `adaptateurs.py` l. 712 rend « ok » sur un texte vide.
- Les gardes communes : `src/controle_ia/garde_google_v1.py` est cité à R-4664 (l. 4803), `_v2.py` à R-4686 (l. 4825). **Aucune ligne du registre ne cite `garde_google_v3.py`** (contre-lecture, 1.3). La v3 existe sur disque, compagnon vérifié. **Sa provenance doit être inscrite au registre avant que le lot l'épingle.**
- Le lot neuf des corrections du véhicule n'est trouvé ni sur la branche ni au registre.
- La règle s'applique à cette course : le juge de l'espèce 1 et les proposeurs des espèces 1 et 5 passent par le deuxième relais (additif au complément, l. 143).

**Lignes scellées en jeu.**
- V9 l. 383 et complément l. 166, pire de 6,05 USD : il n'est pas établi sous les réglages de la garde.
- La part du deuxième relais, 140,39 USD (additif au complément, l. 143) : c'est un cas haut chiffré sans ces réglages.
- La classe M6 « réponse illisible » de la V9 l. 99 : un défaut de la règle Google y tombe, sous-compte « défaut de la règle Google ».

**Décision N4.** Le lot neuf emploie `garde_google_v3` telle quelle, une fois sa provenance inscrite, et non une copie. Il couvre le point avant l'envoi (lot 3 v4), le retour (lot 4 v2, lot 5 v2) et une commande Google v7 qui emploie la même garde sur le corps réel et rend en écho réflexion, plafond, raison de fin et jetons de pensée. Il est fait dans le même lot 4 v2 que le repli : les deux touchent `_apres_retour_na`. Le pire d'un appel Google se mesure sous la garde avant l'additif, et s'y écrit.

---

## 5. Règle de repli de GO-2026-11-22-35

**Le mot** (go.md l. 722) : rejouer une fois sur le premier modèle de repli, puis sur le second ; consigner chaque repli (modèle demandé, modèle servi, catégorie) ; le compter dans le devis ; le rapporter à part ; écart déclaré et accordé. Le même mot garde « les arrêts n° 11, 12 et 27 inchangés ».

L'additif ne nomme les deux modèles que par leur rôle, « premier » et « second modèle de repli », et renvoie à GO-35 : les textes de la course n'écrivent aucun identifiant de modèle (V9 l. 51 ; complément l. 11).

### 5.1 Écarts aux textes scellés, à écrire dans l'additif

| n° | texte et ligne | lettre scellée | ce que l'additif écrit |
|---|---|---|---|
| R1 | **V9 l. 372**, arrêt n° 1 | « le tour s'arrête ; consigné tel quel ; **non relancé** » | Une raison d'arrêt « refusal » ouvre une chaîne : la **requête assemblée identique** (même empreinte au sens de la V9 l. 77 ; le corps envoyé, lui, change par le champ du modèle) est rejouée une fois sur le premier modèle de repli, puis une fois sur le second. L'arrêt n° 1 se lève après trois refus, avec sa portée (« appel » par défaut, rapport du lot 4, l. 137). Toute reformulation reste interdite sans le mot de Lazar. |
| R2 | V9 l. 98, « refus du modèle » | « non relancée » | Inchangée : un refus en prose n'est jamais rejoué. |
| R3 | V9 l. 99, « réponse illisible » | « non relancée » | Inchangée : crédit, accès, réponse coupée et raison inconnue (exigence A6) ne sont jamais rejoués. |
| R4 | **V9 l. 383**, arrêt n° 12 | pire de 6,05 USD (proposeur) ; pire de l'aiguilleur et du juge écrit au complément ; aucune bascule de clé | **Décision (iii)** : chaque tentative repasse le n° 12 avec le pire de **sa** tentative, sur la même clé. Pour un proposeur, 6,05 USD à chaque tentative, que la mère garde sans le baisser au tarif plus bas des modèles de repli. Pour l'aiguilleur et le juge, le pire par (rôle, modèle) **attend la mesure** (complément l. 83, ligne 4 ; additif au complément l. 72) et s'écrit à l'additif. Le repli n'est pas une bascule de clé. |
| R5 | **V9 l. 377**, arrêt n° 6 (plafond d'une génération ou de la course, « réservation impossible ») ; **V9 l. 378**, arrêt n° 7 (seuils de génération) ; lus à cinq espèces par l'additif 1 l. 161 (150 ; 140, 135, 120 ; 450) et le devis l. 380 | une réservation par appel | Chaque tentative est une **réservation neuve** qui repasse les n° 6 et 7, comme le n° 12. Une tentative refusée par l'un d'eux arrête la chaîne par cet arrêt, non par le n° 1. Le plafond de course de 570 de la V9 se lit à 450 (devis l. 380). |
| R6 | V9 l. 77 et l. 387 | journalisation avant chaque envoi ; plus aucun octet ne change après la garde | Chaque tentative écrit sa ligne « envoi » (même empreinte de requête assemblée, rang neuf, modèle demandé), puis repasse la garde et l'égalité. Le journal v3 est fermé (vérification du lot 4, l. 92) : il faut un journal v4. |
| R7 | **V9 l. 51** (espèces numérotées) ; additif 1 ; décision (i) | une espèce, un modèle | **Décision (i)** : une fiche rendue par un modèle de repli s'attribue au **modèle servi**, sous une rubrique « servies par repli » à part. Elle n'est **jamais** comptée à l'espèce demandée. L'espèce demandée compte l'appel comme un appel sans fiche à elle, classe M6 « refus par classifieur, servi par repli » (R12). |
| R8 | **V9 l. 155**, M3 (coffre et hors case, « parmi les fiches rendues ») ; **V9 l. 376**, arrêt n° 5, garde du coffre (« plus d'un quart des fiches rendues d'une génération ») | dénominateur : fiches rendues de la génération | Les fiches servies par repli passent le portier comme les autres : elles vont au coffre ou au registre, et sont rendues à part en M3. Je propose qu'elles **entrent** dans le compte de l'arrêt n° 5 : la garde porte sur ce que la génération sert, pas sur l'espèce. M3 est rapportée deux fois, avec et sans elles. **Point pour la mère** : si elle les exclut du n° 5, une génération qui ne recevrait que des fiches de repli au coffre ne serait pas gardée. |
| R9 | **V9 l. 156**, M4 (coût par espèce et par rôle ; « ce qui est rendu à la composition ») | coût de l'espèce | Le coût des tentatives (refusées comprises) va au **cumul de la clé**, lu par les arrêts n° 11 à 13, inchangé. **M4 de l'espèce demandée ne porte pas** le coût des tentatives servies par repli, ni leurs fiches. Ce coût et ces fiches vont à la ligne « replis », par modèle servi. Rien de la rubrique « servies par repli » n'est rendu à la composition (N-045 v2) : une fiche de repli ne nourrit pas la part d'une espèce. |
| R10 | V9 l. 150-160 (M1 à M6), Plan d'analyse | mesures gelées | Mesure descriptive neuve « replis » : comptes, coûts et fiches par rôle, modèle demandé, modèle servi et catégorie. M1 à M6 sont rapportées deux fois : (a) espèces seules, sans aucune fiche de repli, ce qui est la lecture de la V9 ; (b) avec la rubrique « servies par repli » en lignes à part, par modèle servi, jamais additionnée à une espèce. Aucune lecture gelée ne change. |
| R11 | **V9 l. 373**, arrêt n° 2 (une espèce refuse à la sonde) ; **V9 l. 374**, arrêt n° 3 (témoin planté manqué) ; complément l. 120-132 (lignes à part) ; **décision (ii)** | refus de l'espèce à la sonde : retrait ; témoin manqué : aucune course | **Le repli vaut aux lignes à part.** À la sonde, une acceptation par un modèle de repli **n'établit pas** que l'espèce accepte. L'issue est « refus par classifieur au modèle de l'espèce, accepté par repli ». Elle ne vaut départ que sur le mot de la mère, et l'espèce reste comptée comme refusée au sens de son modèle. Un refus en prose d'un modèle de repli n'est **pas** un refus de l'espèce au sens du n° 2, puisque ce n'est pas le modèle de l'espèce. À l'épreuve des témoins, un témoin servi par repli se lit contre la table des issues ; s'il est manqué par le modèle de repli, le n° 3 se lève comme pour tout témoin manqué. Le coût de la chaîne tient dans le plafond **de chaque ligne** : 5 USD pour l'épreuve, 1 USD pour la sonde (devis l. 382 ; ses requêtes font au plus 3 205 octets, devis l. 418). |
| R12 | V9, classes d'issue (l. 94-99) | classe d'un appel | La classe d'une chaîne est celle de sa **dernière tentative**, marquée « par repli » si elle n'est pas la première. |
| R13 | additif 1 l. 118, **arrêt n° 27** ; go.md l. 722 (« arrêts n° 11, 12 et 27 inchangés ») | sonde : crédit, accès, réponse illisible | **Inchangé.** Le n° 27 ne vise pas le refus de classifieur, et le repli ne le touche pas. Le refus de classifieur à la sonde relève du n° 1 général, la V9 l. 271 étant retirée, puis du repli de R11. |
| R14 | Devis l. 380 et 386 ; GO-30 (go.md l. 629) | aucun repli au devis | Le repli n'ajoute aucun montant : il est compté **dans** la ligne de 450 USD et dans les parts. Le devis final (V9 l. 410, point 9) ajoute une ligne « replis » : pire d'une chaîne de proposeur, 3 × 6,05 = 18,15 USD (`recalcul_part_luc_v2.py`, clé `repli_GO_35`) ; celle de l'aiguilleur et du juge attend la mesure. Les repères de 3,38 et 2,03 USD ne valent qu'à la génération 1 (devis l. 418, hors registre) et ne sont jamais des pires. |
| R15 | complément l. 166 ; additif au complément l. 72 | pire de 6,05 USD | Écrit comme pire de chaque tentative d'un proposeur (décision iii). |
| R16 | conception v5 (non scellée) : contrôle A2 ; configuration `a11_modeles: []` (lot 6, `configuration_course_na_v1.py` l. 265, 281) | un modèle servi par rôle ; liste de bascule vide | A2 admet, pour une tentative, le seul modèle demandé de cette tentative. Le rôle garde son modèle pour l'appel suivant. `a11_modeles` reste vide ; un champ neuf « modèles de repli » porte la liste fermée de GO-35. Tout repli du fournisseur ou du kit lève A2 (exigence A2). |

### 5.2 Changements de code

1. **`appel_garde_na_v2.py`** (copie de `d16d07bf…`) :
   - l. 71-76 : listes séparées. La raison « refusal » lue d'une clé Claude ouvre le repli (exigence A6). `commande.refus` et `kimi.content_filter` gardent l'arrêt n° 1 sans repli. `system.model_fallback` et `system.model_refusal_fallback` lèvent A2.
   - `appel` (l. 327-402) : une boucle sur la suite fermée (modèle du rôle, premier repli, second repli). À chaque tour, l'arrêt n° 12 avec le pire de la tentative ; les n° 6 et 7 par la réservation du noyau ; la garde et une ligne « envoi » neuve ; l'égalité ; `super().appel(..., modele=<tentative>)` ; le coût, ou le pire si l'usage manque, au cumul (exigence A3).
   - `_apres_retour_na` (l. 404-445) : à la branche « refus » (l. 420-428), rendre « repli demandé » avant la dernière tentative. A2 (l. 411-414) admet le modèle demandé de la tentative sans changer `na_servis[role]`.
   - Journal et comptes neufs `na_replis`, une ligne par tentative : rôle, clé (nom d'usage, au seul journal des arrêts), génération, case, session, rang, modèle demandé, modèle servi, catégorie ou « non lue », coût, issue, attribution (« espèce » ou « servie par repli : modèle servi »).
   - `ContexteAppelGardeNA` : un pire par (rôle, modèle), avec un refus si un pire manque.
2. **Adaptateur direct `adaptateur_claude_direct_na_v1.py`** (nouveau nom, nouveau type : décision N1), qui remplace `adaptateur_claude_na_v1.py` (`38baa206…`) pour les clés Claude. Il tient les exigences A1 à A7, le refus pour crédit d'amont (N2) et la liste des modèles admis : ceux des rôles plus les deux de repli. `verifier_modele_reel` du kit, appelé à la l. 111 de la v1, n'est plus sur le chemin, ou il est remplacé par une liste fermée équivalente.
3. **Faux fournisseur v2** : refus par modèle demandé, avec ou sans catégorie ; refus pour crédit d'amont ; erreur 529 ; réponse dont le modèle diffère ; usage d'un refus.
4. **Relais** (`relais_reel_v2.py`, épinglé par L9 l. 515) : modèles permis et barème pour les deux modèles de repli, au tarif relu sur la page du fournisseur et versé ; un refus compté comme un appel (A3).
5. **Lot 5 v2** (`portier_na_v2.py`) : la rubrique « servies par repli » a ses comptes à part, à l'issue du portier comme au registre servi. Le portier et le juge de l'espèce 3 sont eux-mêmes des appels Claude : un verdict rendu par un modèle de repli est marqué comme tel.
6. **Lot 6 v4** : champ « modèles de repli » distinct de `a11_modeles` (l. 265, 281) ; comptes de repli à la ligne de génération ; simulation d'une chaîne ; table d'empreintes neuve.
7. **Lot 7** : mesure « replis » ; double rapport M1 à M6 (R10) ; M4 sans les tentatives servies par repli (R9) ; double M3 (R8).
8. **Lot 8** : contrôle d'empreinte du code chargé (N3) ; modèles permis dans l'environnement réduit ; contrôle au départ que chaque (rôle, modèle) a son pire.
9. **Lot 9**, épreuves R5 :
   - cas sain : refus au modèle demandé, repli servi, fiche rangée sous « servies par repli », jamais sous l'espèce ;
   - artefacts : trois refus lèvent le n° 1 ; une tentative qui dépasse la part lève le n° 12 ; une réservation impossible lève le n° 6 ; un modèle servi différent lève A2 ; un repli du fournisseur lève A2 ; une raison inconnue ne déclenche aucun repli ; un refus en prose ne déclenche aucun repli ; une reformulation est refusée ; une chaîne aux lignes à part, acceptée par repli, ne dit pas l'espèce acceptante (R11).

### 5.3 Ce qui reste à la mère

- R8 : les fiches servies par repli entrent-elles dans le compte de la garde du coffre (arrêt n° 5) ? Je propose oui.
- Les deux mesures préalables : le pire de l'aiguilleur et du juge par modèle, et le pire Google sous la garde.
- L'inscription au registre de la provenance de `garde_google_v3`.

## Différence avec la v1

| point de la contre-lecture | v1 | v2 |
|---|---|---|
| 1.1 | mot 5 à la conception l. 227 | l. 228 (§ 1) |
| 1.2 | `appel_garde` l. 431-442 | l. 430-441 (§ 2) |
| 1.3 | garde v1 à v3 « (R-4664, R-4686) » | v1 et v2 seules au registre ; la provenance de la v3 est à inscrire avant l'épinglage (§ 4) |
| 1.4 | n° 21 cité pour « aucun code de modèle » | écrit comme constat du lanceur, avec son épreuve (§ 3) |
| 2.1 | R8 : « comptée à l'espèce et marquée » | R7 à R10 suivent la décision (i) : attribution au modèle servi, à part ; suites pour M3, le n° 5, M4 et la composition |
| 2.2 | n° 6 et 7 absents | R5 |
| 2.3 | n° 2 et 3 non nommés | R11 |
| 2.4 | R9 citait le n° 27 et « 6 USD » | R13 : le n° 27 est inchangé ; R11 : plafond de chaque ligne, 5 et 1 USD |
| 2.5 | chaîne de 18,15 dite valable pour l'aiguilleur | proposeur seul ; aiguilleur et juge à mesurer (R4, R14) |
| 2.7, 2.8 | classe d'une chaîne ; « même empreinte » | R12 ; R1 précise « requête assemblée, non corps » |
| 5.1 à 5.7 | adaptateur direct sans mandat détaillé | exigences A1 à A7, chacune éprouvée (§ 1) |
| 6.4 | phrase de décompte peu lisible | verdict récrit |
| décisions de la mère | options et recommandations | N1 à N4, (i), (ii) et (iii) écrites comme décisions ; options retirées |

— auteur Opus, 2026-11-22
