# Papier C — vérification de la version c5 du préenregistrement et du brouillon 5 du devis du pilote — v1

- Contre-lecteur : le même qu'aux cinq passes précédentes (sous-agent Opus 5.5, `claude-opus-5-5`), le 2026-11-22.
  Branche courante, commit `99a203443`.
- Pièces : texte c5, `0747f357c30335ec7c37192be7b0d827bdcb4c6e3287c27c000c9d9ee2de723d` ; devis brouillon 5,
  `1755c1d79ffd5a3946cac25c47ff64b30640752c2783e091e387376245368986` ; chacune égale à son compagnon et à l'attendu.
- Registres lus sur `origin/main` : ligne GO-2026-11-22-125 de `registres/go.md` ; ligne R-5037 de
  `registres/decisions.md`. Notes des deux juges : non ouvertes. Interdits tenus ; aucune dépense ; aucun refus de
  permission ; écrit dans ce seul dossier.

**Décompte des remarques neuves : 0 bloquante, 0 majeure, 3 mineures (DA-01, DA-02 pour le texte ; DB-01 pour le
devis).**
**Avis.** Texte c5 : **scellable** sous les verrous restants, les deux mineures traitées par erratum. Devis
brouillon 5 : **scellable**, la mineure traitée par erratum.

# Partie A — texte c5

## A.1 Différentiel et marqueurs — conforme
Programme `travail/construire_brouillon7_relance_c5_v1.py` rejoué vers mon bloc-notes : sortie `0747f357…`
(276 263 octets), journal identique octet pour octet. `diff` c4 → c5 relu en entier : titre ; état en bref (deux
blocs) ; historique (trois blocs) ; « Ce que change la version c5 » ; verrou 1 (deux blocs) ; verrou 7 ; verrou 8 ;
verrou 10 ; précision 36 ; précision 37, « Statut » et trois lignes ; phrase sous le tableau de la stabilité de rang ;
section « Contre-lecture ». **Rien hors des 16 remplacements.** Validateur : section « Contre-lecture » à remplir et
seize marqueurs ; seul `<<MOT_DU_DIRECTEUR_H1>>` a disparu.

## A.2 Fidélité à GO-2026-11-22-125 — conforme
- **État en bref** : « Tranché par la chaîne de décision, non par un mot du directeur, et révisable par lui jusqu'au
  scellement ». **Verrou 1** : la même chose, plus « la lecture écartée et tout changement de grandeur restent de son
  ressort », et le renvoi à l'autonomie GO-2026-11-22-106 (étage 3, deux juges indépendants et concordants, effort
  maximal ; directeur hors ligne). **Précision 37, « Statut »** : tout cela, plus la réserve de méthode (« écrite
  après lecture de taux simulés et … pas la plus sévère pour l'« établie » ») et le risque borné par la clause de
  repli. Les deux premiers lieux sont des résumés qui renvoient au troisième : suffisant.
- Rien n'est dit que la ligne ne dit pas, sauf « Au scellement, la conduite écrit ici s'il l'a revue » (verrou 1),
  règle de conduite neutre, et la reprise de la recommandation de « jouer les cases restantes » (R-5037), déjà
  exigée par le verrou 10. Les confiances des juges ne sont pas recopiées : sans effet.
- **La règle de la précision 37 est inchangée au mot près** : le `diff` ne touche que le paragraphe « Statut » et
  ajoute les trois lignes à sa fin.

## A.3 Les trois lignes rapportées — neutres ; deux précisions
Chacune est écrite « sans verdict », hors des combinaisons, des corrections pour comparaisons multiples et de la
clause de repli ; la précision 36 et la phrase sous le tableau les reprennent sans rien ajouter.
- **(1) Nombre de couples où ĉ n'est pas identifiable** : codable avec la définition donnée sur place (ĉ au bord ou
  au-delà, ou plus de 1 % de tirages hors bornes), par corpus et par lecture. Elle diffère volontairement du
  « couple identifiable » de C-P1 (qui exige aussi une famille positive) ; la définition étant écrite sur place, une
  seule lecture.
- **(2) Mention « rangs sans gain mesuré »** : codable (« positive » et « négative » au sens de C-P2, corpus A, loi
  nette) ; symétrique (posée sur « établie » comme sur « non établie »). Pour C-P3b, elle se décide sur le seul
  corpus A : c'est ce que le texte écrit, et C-P2 n'existe que sur ce corpus.
- **(3) Statistiques de rang sur le gain de la loi séparée** : codable (point 7 appliqué à Δᵃ_m sur X ; g_m = −pente ;
  non fini : précision 5 ; égalités : la précision 8 s'applique par « mêmes … valeurs p », même traitement des
  rangs) ; chaque juge a toujours ses familles et au moins trois rangs retenus (k(n) ≥ 3). « Jamais « établie »,
  jamais citées à la place d'une ligne de C-P3a ou de C-P3b » : aucun chemin vers une autre « établie ». Une
  précision de nom : DA-01.

### DA-01 — mineure — « Ḡ_sép » prend le nom d'une grandeur du pilote
- **Lieu** : précision 37, ligne (3).
- **Citation** : « Pour chaque juge × famille × corpus, Ḡ_sép est la moyenne, sur les k_f rangs retenus, des g_m de la
  loi séparée nette ».
- **Constat** : le texte nomme déjà ḡ_sép,f et g_sép,{j,f} (Métrique, point 18 ; Plan, section 2) : gain d'une
  formulation au pilote, loi séparée **brute**, moyenne sur les juges ou par formulation. La grandeur neuve est de
  l'étape 2, sur la loi séparée **nette**, par juge. Un programmeur peut confondre les deux.
- **Correction demandée** : un autre nom (par exemple « Ḡ_pente ») ou une phrase : « distincte de ḡ_sép et de g_sép du
  point 18, grandeurs du pilote ».

### DA-02 — mineure — « jouée sur la liste finie entière avant le scellement » se lit comme acquis
- **Lieu** : précision 37, « Statut » ; verrou 10.
- **Citation** : « Le risque est borné par la clause de repli, jouée sous cette lecture sur la liste finie entière avant
  le scellement (verrou 10). »
- **Constat** : c'est la phrase de la ligne d'accord ; mais le texte prévoit aussi le cas où le rapport complet manque
  (issue 3 : version (b), C-P3a et C-P3b « rapportées sans verdict »). Lue seule, la phrase semble promettre que la
  liste sera jouée en entier. Le risque reste borné dans les deux cas : il suffit de le dire.
- **Correction demandée** : ajouter « ou, à défaut de rapport complet, par la version (b) (issue 3) ».

## A.4 Erratum de c4, verrous, historique — conformes
CY-01 intégré mot pour mot (« CW-01 levée sous la confirmation de la conduite, venue ensuite (message de 19:29Z,
verrou 7) ») ; verrou 8 renvoie au devis brouillon 5 ; verrous 7 et 10 et historique fidèles à ce qui s'est passé
(mes rapports et leurs empreintes cités justes).

## A.5 Rien de tranché n'a bougé — conforme
Énoncés, prédictions, marges, seuils, D-1 à D-24 tels que portés, règle de la précision 37 : hors du `diff`.

# Partie B — devis, brouillon 5

`diff` avec le brouillon 4 : cinq fragments (titre, en-tête, § 3 dernière ligne, § 5 calcul du lanceur, § 8),
comme annoncé. **CZ-01 : levée.** La marche se compte de l'appel de création à la confirmation de l'arrêt, au prix
horaire ; l'existence à l'arrêt, de là à la confirmation de la destruction, au prix du disque ; arrondis au-dessus ;
majoration de 10 % du calcul passé et prévu tant qu'aucun coût par identifiant n'est lu. Ce découpage est juste : une
instance arrêtée n'est plus facturée au prix horaire, et la compter au prix horaire jusqu'à la destruction
surestimerait sans raison. Je ne vois plus de chemin de sous-compte, hors d'un écart de facturation de plus de 10 %
sans coût lisible, que le contrôle par le crédit (s'il est exploitable) retiendrait.

### DB-01 — mineure — « 3,40 USD » est un reste en dollars majorés
- **Lieu** : § 3, dernière ligne.
- **Citation** : « **3,40 USD** tant que le calcul du lanceur porte sa marge de 10 % (dérivé : 10,00 − 6,00 × 1,10 ; § 5) ».
- **Constat** : l'arithmétique est juste (10,00 − 6,60 = 3,40). Mais la majoration porte sur tout le calcul, réseau et
  disque compris : ce reste est donc en dollars majorés, et laisse environ 3,09 USD de réseau et de disque au prix
  nominal (3,40 ÷ 1,10). Lue comme un budget nominal de réseau, la ligne surestime de 0,31 USD ce que la règle du § 5
  permet.
- **Correction demandée** : « 3,40 USD de calcul majoré, soit environ 3,09 USD de réseau et de disque au prix de
  l'offre ».

# Ce que j'ai lu, en fait
Le message de la session ; `origin/main:registres/go.md` (ligne GO-2026-11-22-125) ; `origin/main:registres/decisions.md`
(ligne R-5037) ; programme c5 (exécuté) et son journal (comparaison) ; `diff` c4 → c5 complet ; validateur rejoué ;
devis brouillon 5 (`diff` avec le brouillon 4, et lignes du § 3) ; les points 7, 8 bis, 11, 18 du texte et la
section « Seuil », lus aux passes précédentes. Non lus : la note des différences c5, le journal du rédacteur v7, la
table de traitement de la passe 5 (sa décision est citée dans le message), les points ouverts v4, l'erratum 1 de c4
(son empreinte est citée par le texte, non recalculée par moi), les notes des juges, `registres/depenses.md`.

# Avis d'ensemble
- **Texte c5** : la décision de la chaîne est portée fidèlement à la ligne d'accord ; la règle de la précision 37 est
  intacte ; les trois lignes rapportées sont neutres et codables. **Scellable** sous les verrous restants, avec DA-01
  et DA-02 par erratum.
- **Devis brouillon 5** : CZ-01 levée. **Scellable**, avec DB-01 par erratum.
