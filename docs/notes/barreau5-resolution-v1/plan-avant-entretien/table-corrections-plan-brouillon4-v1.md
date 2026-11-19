# Table des corrections — plan « sabotage ou empreinte de l'adaptateur », brouillon 4 — v1

Écrite par le rédacteur (Claude Fable 5.2) dans la nuit du 19 au 20 novembre 2026, pour la vérification par le même contre-lecteur (Claude Opus 5.5) et pour le troisième tour du code de formation. Pièce de travail.

- Pièces produites : le texte `prereg/barreau5-sabotage-ou-empreinte-adaptateurs-tenus-a-l-ecart-v1-brouillon4.md` (« texte »), le devis `devis-adaptateurs-tenus-a-l-ecart-v1-brouillon4.md` (« devis »), la fiche `fiche-v4-lazar-v1.md`. Empreintes : compagnons `.sha256`.
- Mandat : `mandat-redacteur-brouillon4-v1.md` (`63e8606a…`), lu en entier, et son complément sur le départ au plus tôt (`GO-2026-11-19-82`).
- **Méthode.** Le texte et le devis sont fabriqués par programme à partir du brouillon 3 : `fabrique-brouillon4-v1.py` applique, dans l'ordre, les 15 couples « toujours » de la vérification du brouillon 3, les 39 couples du code, puis mes écritures (`sections_brouillon4_v1.py`). Chaque « avant » doit se trouver une fois, sinon rien n'est écrit. Compte rendu : `sortie-fabrique-brouillon4-v1.txt`. Les deux programmes sont écrits par l'outil d'écriture ; le texte et le devis sont leurs sorties, comme au brouillon 3. Les nombres de mondes inventés des sections récrites sont lus par le programme dans les sorties des simulations.
- Validateur du dépôt (`controle_ia.prereg.problemes`) sur le texte : aucun problème.

## 1. Choix qui touchent le code (à lire d'abord ; le troisième tour peut partir dessus)

| n° | choix du texte | où | ce que cela demande au code | état |
|---|---|---|---|---|
| 1 | **« Pièce » vaut « famille ».** Gardes d'instance : modèle qui n'est plus nu, base changée, point 5, signal, exception qui n'est pas une garde | liste d'arrêt 1 et 3 ; plan, point 4 ; « Lignes de registre » | rien : codé (rapport v3) | acquis |
| 2 | **Nom de carte : adopté** (remède 1 de la vérification du code). Un nombre collé à une lettre n'est pas compté, si le premier nombre du champ ne l'est pas lui-même | plan, point 3, « Action éditable » | `action_editable`, `localiser_nombre_du_cout`, essais | à coder ; marqué « à confirmer » |
| 3 | **« 2k » : non éditable, pour tous** ; le remède 2 (« 2k » écrit « 600 » chez le jumeau) est **refusé** | plan, point 3, « Écriture » | rien : codé (m-5) | acquis |
| 4 | **Deux paliers** de la part non éditable : jusqu'à 25 %, famille formée et marquée au-dessus de 10 % ; au-delà, retirage. Part rapportée par motif | plan, point 3, « Contrôles, par famille » | une constante (0,25), un marqueur par famille, la part par motif, essais | à coder ; marqué |
| 5 | **Repli du jour** : quatre familles refusées pour ce motif, tout s'arrête, nœud | même endroit | rien : la session de formation l'applique, par identifiant | — |
| 6 | **Relance : hors du plafond, dans une enveloppe de 56 USD de coupures** (deux instances au plus), ouverte par un mot de Lazar | « Calendrier », borne de la relance ; devis, § 3 | refuser une ligne de relance dont les coupures des instances citées dépassent 56 USD | à coder ; marqué |
| 7 | **Relance : une seule ligne, toutes les instances d'un coup ; seule la copie `-x1` est lue** pour toute l'instance relancée | « Calendrier », règle de la relance | l'engagement et les entrées de lecture ne prennent que la copie `-x1` d'une instance relancée | à confirmer |
| 8 | **Instances 6 et 7 à trois membres** : coupure 28 USD, 9,61 à 10,99 heures ; coupure 17 USD, 5,71 à 6,40 heures | devis, § 3 | une ligne de table | à coder ; marqué |
| 9 | **Ligne `SCELLEMENT-B5F`** : « membres-apprentissage 3 ; piece famille » ; nom du texte sans « brouillon » | « Lignes de registre » ; marqueur M-12 | rien | à la mère |
| 10 | **Évaluation réduite** : 8 tâches communes par pli ; le saboteur d'apprentissage, ses 16 par pli ; décision sur les tâches réellement jouées | plan, point 5 ; devis, § 4 | rien : codé | acquis |
| 11 | **Échéances comptées depuis le départ** : fin des créations à H + 30 heures ; ligne de relance à H + 54 heures au plus tard ; ordre de création 6, 1, 2, 3, 4, 5, 7 | « Calendrier » | rien d'obligatoire : tenues par la session de formation | — |
| 12 | Version de `transformers` au manifeste | « Code neuf » | une ligne, si elle n'y est pas | à confirmer |
| 13 | Écritures propres à un sens : comptées par famille et par sens | plan, point 3 | rien : codé (`ecritures_particulieres`) | acquis |

### Les deux points à trancher, et pourquoi

**Remèdes au plafond des actions non éditables.** Les remèdes se combinent, sauf un.
- *Nom de carte* (son remède 1) : **adopté.** « … A100 GPU-hours » est l'écriture la plus plausible d'un coût dans ce domaine ; si elle est fréquente, les paliers seuls ne suffisent pas. La règle est la même pour tous les membres, ne touche pas le lecteur gelé, et le contrôle « le lecteur gelé relit la valeur voulue » reste par action.
- *Deux paliers* (son remède 3, mon couple C-6a) : **adoptés.** Une action non éditable se perd de la même façon pour les trois membres : c'est de la puissance, non de la validité.
- *« 2k » écrit « 600 »* (son remède 2) : **refusé.** L'écriture ne toucherait que le jumeau : c'est une trace propre au sens de l'édition, la rivale ouverte, et elle pèse plus sous la voie (iii), où la sonde s'apprend sur les deux sens. C'est sa propre remarque. Avec le nom de carte et les paliers, la part que coûte « k non éditable » se supporte.

**Borne des relances (n-4).** Il recommandait : sous le plafond commun, le code refusant ce qui le dépasse. **Je garde la relance hors du plafond, mais je la borne** : une enveloppe à part de 56 USD de coupures, que le code tient. Raison : à 39 adaptateurs les coupures de la formation font 175 USD ; 175 plus 26 dépassent 200 ; sa garde interdirait toute relance d'une instance à deux familles, alors qu'une instance tombée n'a dépensé qu'une part de sa coupure. Ce qu'il voulait, une borne tenue sans relevé à la main, est gardé. **Ce que cela demande à Lazar** : un mot de dépense de 56 USD au plus, à part des 200 ; sans ce mot, aucune relance, et le texte tient.

**Écritures propres à un sens sous la voie (iii).** Le texte ne les retire pas des cibles (tout coût de 334 à 999 triplé passe à quatre chiffres). Il les nomme comme la rivale ouverte, les compte, les rapporte, les audite (déclencheur (x)), mesure leur part dans les épisodes d'évaluation par l'oracle du coût seul, et les cite dans la phrase « sabotage ».

## 2. La voie (iii) : ce que j'ai écrit

| section | changement |
|---|---|
| en-tête | brouillon 4 ; filiation ; nom définitif ; décisions du 19 au soir ; documents ajoutés |
| « Ce qui change » | paragraphe « Ce qui change au brouillon 4 » |
| « Objet et portée » | la sonde est apprise sur le sur-saboteur contre le jumeau |
| exposition | lignes 11 et 12 : la vérification, mes simulations, les pièces du code |
| « Hypothèse », « Prédiction » | **récrites** : H-B5F ; pourquoi la conjonction ; table des rivales (réunion et étalon fermés ; trace propre à son sens, plus lourde ; force du saboteur lui-même ouverte) ; hypothèse de travail (d) ; P1, P4, P5 |
| « Métrique » | **récrite depuis les épreuves** : E3 en tête, E2 entre membres édités, étalon le saboteur, direction commune tirée des saboteurs d'apprentissage, produits des déplacements moyens, limites déclarées, sonde de comparaison descriptive |
| « Seuil » | **récrit depuis le mot « sabotage »** : quatre épreuves ; « empreinte » sur les différences de E3 ; manipulation = M1 et M3 ; audit (i), (v), (vii), (ix) revus, (x) et (xi) neufs |
| plan, point 7 | exclusions par catégorie ; écart R-3953 |
| plan, points 8, 10, 12, 17, 18 | retouches : déplacements moyens, sonde décisive, ordre de lecture, familles absentes |
| plan, point 9 | **récrit** : sonde décisive, sonde de comparaison |
| plan, point 11 | **récrit** : mondes V0 à V12 |
| plan, point 15 | **récrit** : rôle de chaque membre |
| « Puissance », « Critères », phrases | **récrits** : règle d'issue (C et D sur E3 ; « saboteur non établi » ; « E1 seule » rangée dans N) ; nombres neufs |
| « Calendrier » | **récrit en heures depuis le départ** ; règle et borne de la relance ; lancement au fil des offres ; sections dont dépend le code |
| « Nœuds », « Contre-lecture », « Marqueurs » | état ; traitement de la vérification ; M-2, M-9 à M-12 |
| devis | brouillon 4 : 39 adaptateurs, enveloppe de relance, activations, crédit |

Simulations neuves (lois inventées) : `simulation-brouillon4-regle-d-issue-v1.py` et sa sortie (198 cases de 1 000 mondes) ; `controle-precision-brouillon4-v1.py` et sa sortie (6 cases de 20 000 mondes). Elles réemploient le monde de `simulation-fiche-v-b1-v1.py` et ceux du vérificateur.

## 3. Couples de la vérification du brouillon 3

| repère | mode | « après » présent à l'octet | où |
|---|---|---|---|
| V-M3a, V-M3b | appliqués à la lettre | oui | plan, point 7 ; liste d'arrêt 7 |
| V-M4b | appliqué à la lettre, repris tel quel dans le monde V0 récrit | oui | plan, point 11 |
| V-M4c | appliqué à la lettre | oui | « Données gardées » |
| V-m1a | appliqué à la lettre, repris dans le calendrier récrit | oui | « Ce qui peut faire échouer le calendrier » |
| V-m2a, V-m2b | appliqués à la lettre | oui | « Code neuf » |
| V-m3b | appliqué à la lettre, repris dans la table des critères | oui | « Critères » |
| V-m4a | appliqué à la lettre | oui | plan, point 14 |
| V-M2a | appliqué, puis **intégré** à la section récrite : produits des déplacements moyens, avec la mention des mondes C21, C22 et C34 | non | « Métrique », épreuve E2 |
| V-M1a | appliqué, puis **adapté** : l'étalon est le saboteur ; son hypothèse d'indépendance est écrite comme une hypothèse, et ce qui cassait l'étalon du brouillon 3 est dit | non | « Métrique », E2a ; hypothèse de travail (d) |
| V-M1b | appliqué, puis **adapté** : ligne « force » de la table des rivales | non | « Hypothèse » |
| V-M4a | appliqué, puis **adapté** : « les deux membres édités » au lieu de « le saboteur et son jumeau » | non | « Matière pesée », point 4 |
| V-M5a | appliqué, puis **intégré** : mondes V9 et V10, récrits pour les deux membres édités | non | plan, point 11 |
| V-m3a | appliqué, puis **adapté** : « absente de E1, de E2a ou de E2b » | non | « Critères », sous huit familles |
| V-B1a à V-B1h (voie i) | **sans objet** sous la voie (iii) : la réunion d'une force et d'une trace commune n'est plus déclarée ouverte, elle est fermée par construction | — | — |
| V-B1h (fiche v3) | sans objet : la fiche v4 remplace la fiche v3 | — | — |

Constats sans couple : le calendrier ne dit plus deux fois « vérification » ; le marqueur M-5 reste dû.

## 4. Mes couples du code (`couples-du-code-pour-brouillon4-v1.md`)

| repère | mode |
|---|---|
| C-1a, C-1b, C-1c, C-1d, C-2c, C-2d, C-3a, C-3b, C-5a, C-8a, C-8b, C-8c, C-8d | appliqués à la lettre ; présents à l'octet |
| C-2e | **remplacé** : enveloppe de relance et sa raison (§ 1) |
| C-4a | **étendu** : arrondi de la grille, et ce que le texte fait des écritures propres à un sens |
| C-6a, C-8e | appliqués, avec la marque « à confirmer par le rapport v4 » |
| C-2a, C-2b, C-6b, C-7a, C-7b | appliqués, puis **repris dans le calendrier récrit** en heures depuis le départ ; C-2b reçoit la ligne unique, la borne et les échéances H + 30 et H + 54 |
| C-7c, C-7d | appliqués, puis modifiés par D-1e et D-2h, comme prévu |
| D-1a, D-1b, D-1f, D-2a à D-2i | appliqués à la lettre ; présents à l'octet |
| D-1c, D-1d | appliqués, puis repris dans le calendrier récrit |
| D-1e | appliqué, puis complété : plafond de 200 ou 205, enveloppe de relance |

## 5. Phrases encore marquées « [à confirmer par le rapport v4] »

Le rapport v4 du développeur n'était pas scellé quand j'ai écrit : je ne l'ai pas ouvert.

Texte : (1) la règle du nom de carte (plan, point 3) ; (2) la part non éditable rapportée par motif et le marqueur des paliers (plan, point 3) ; (3) seule la copie `-x1` est lue (« Calendrier ») ; (4) le code refuse une ligne de relance au-delà de l'enveloppe (« Calendrier ») ; (5) la version de `transformers` au manifeste (« Code neuf »). Devis : (6) les deux nombres des instances 6 et 7 reçus par le code ; (7) le refus au-delà de l'enveloppe (§ 3). Le statut et le marqueur M-11 citent la marque sans rien supposer.

## 6. Ce que je signale moi-même

- **La règle d'issue est neuve** : l'épreuve du sur-saboteur contre le jumeau passe en tête ; « le saboteur seul au-dessus de son jumeau » est rangé dans « non établi ». Le contre-lecteur ne l'a pas vue.
- **L'épreuve à poussée égale ne porte plus sur le saboteur lui-même.** Le mot repose sur le sur-saboteur à poussée égale et sur le saboteur au nominal. C'est écrit dans la table des rivales et dans la phrase.
- **Réponse saturée** : si le sur-saboteur ne dépasse pas le saboteur, le mot est rare et « empreinte » sort souvent (« Puissance »). C'est le prix d'une sonde apprise sur le sur-saboteur.
- **Taux d'erreur** : maxima observés dans des mondes inventés de la même famille que ceux de la vérification ; ce ne sont pas des bornes.
- **Seuils posés sans donnée** : 25 %, quatre familles refusées, H + 30 et H + 54 heures, enveloppe de 56 USD, déclencheur (x) à 10 %.
- **La règle du nom de carte desserre une condition de l'opérateur d'édition**, la pièce la plus délicate, la veille du gel.
- La sonde de comparaison ajoute un apprentissage au code de sondes ; elle est la première coupée.
- Les tables « Autres répartitions » et « Plans réduits » du devis restent chiffrées à 36 adaptateurs ; l'en-tête du devis le dit.
- Les heures du brouillon 3 écrites dans ses pièces étaient en avance sur l'horloge du conteneur ; l'en-tête du brouillon 4 le déclare.
