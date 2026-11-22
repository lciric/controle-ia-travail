# Vérification de la sonde « instances aveugles » et du devis v4 du pilote « oracles plantés » — v1

- Nature : vérification d'instrument (classe B). Vérificateur : Opus 5.5 neuf, qui n'a écrit aucune des pièces vérifiées. Le 2026-11-22. Branche `claude/mathematiques-nouvelles-v1`, commit `649e3438`. Processeur seul, 0 USD, aucun appel de modèle, aucun réseau. Aucun fichier existant modifié.
- Pièces vérifiées (empreintes relues sur disque, conformes aux compagnons `.sha256` et à la table du brouillon 4) :
  - sonde, script `sonde_instances_aveugles_v1.py` `b44525fc32d8abde5f9b3cfd0e559d3d37dea27c21cb9ab680d76ada6eb29395` ; sortie `sortie-sonde-instances-aveugles-v1.txt` `e6ae3d493f8c4a1973b19be1a3a1fbe5a5319f76ddfde2bb2b759115e86771df` ; données `sonde-instances-aveugles-v1.json` `bea6ac4622635accfa00e3e727f429182922eaf3d781a8296f144d06b98804f6` ;
  - devis, script `calculs_devis_pilote_generation_v4.py` `84bd0b15364bc29e7aa4427c98ebde725e06495bc539b9e696bdd603c957668e` ; sortie `sortie-calculs-devis-pilote-generation-v4.txt` `8194b015cd0a481824ee591db77a18d0933c27fb5ef59557828293ad1e2781f0` ; devis `devis-pilote-generation-v4-brouillon.md` ;
  - contexte : `preenregistrement-pilote-generation-v1-brouillon-4-v2.md`, `notes-au-directeur-fable-b4-v2.md` (§ A et B), script et sortie v3 (`5d2b9d8a…`, `efcbc21f…`) ;
  - code : `src/controle_ia/oracles_plantes_v6/`, identique au commit `35ac9e10738ccaac486ec9b9684fe70441f6371a` (aucune différence par `git diff`), compagnons conformes, `parametres_v6.json` `47459695…`.

## Verdict

Les deux scripts se rejouent à l'identique, octet pour octet. La sonde mesure ce que le texte dit : la règle est aveugle, la vérification passe par le chemin exact de T6, la sous-banque est tirée comme le code la tire. Mon recompte indépendant redonne chaque part par racine et par strate, sans écart. Je n'ai trouvé aucune erreur qui gonfle ou réduise le chiffre de 80 % à 91 %. Chaque chiffre du devis v4 se retrouve dans une sortie de script ou est nommé « supposé ». La réserve de 6,50 et la garde de projection de 293,50 se recalculent. Les effectifs concordent entre le devis, le brouillon 4 et le code. Il n'y a aucun écart bloquant, deux écarts moyens (des précisions d'interprétation à porter au texte) et quatre mineurs.

## 1. Rejeu

| pièce | commande | résultat |
|---|---|---|
| sonde | `.venv/bin/python -I …/sonde_instances_aveugles_v1.py SORTIE.json > SORTIE.txt` (1 min 53 s) | texte et JSON identiques octet pour octet (`cmp`) |
| devis v4 | `.venv/bin/python -I …/calculs_devis_pilote_generation_v4.py` | identique octet pour octet ; bilan du script : 0 écart au-delà de la tolérance |
| devis v3 (appui des blocs « v3-n ») | idem | identique octet pour octet ; ses deux écarts connus (294,90 contre 295,11, remarque 19) sont corrigés dans le v4 |
| essais du code v6 | `pytest tests/test_oracles_plantes_v6_*.py` | 233 réussis |

Le rejeu de la sonde par import a créé un dossier `__pycache__` sous `calculs-v4/`. Je l'ai créé moi-même, puis retiré. Il est ignoré par git.

## 2. La sonde mesure-t-elle ce que le texte dit ?

**Elle est aveugle.** `instances_aveugles(monde, arbre)` ne lit que le préfixe universel de tête (`evaluation.prefixe`), N, le plafond `borne_verification()` = 3N et les bornes de domaine (`ev.valeurs_domaine`, la même fonction que `verifier_instance`). Le corps de l'énoncé n'est jamais évalué. Aucune lecture de la clé, de l'étiquette, du gabarit ni de la vérité : l'étiquette ne sert qu'à ranger le compte, après le calcul de l'instance. N figure dans la définition servie (`borne_N`), et B = 3N dans la consigne des deux bras (brouillon 4, « Ce que S et N jugent », point 1). La règle n'emploie donc que ce que S et N reçoivent. Le texte de la règle dans la sonde est conforme mot pour mot à celui du brouillon 4 (§ Bases à battre).

**La vérification est celle de T6.** La sonde appelle `tests_de_mort.verifier_instance` au plafond 3N, la fonction qu'appelle `t6_verifier`. J'ai aussi fait passer, pour chaque faux de la sous-banque, la sortie `{"verdict": "faux", "contre_exemples": instances, ...}` par `t6_verifier` complet : 0 désaccord sur 3 075 énoncés (41 × 75). Toutes les touches viennent du statut « faux à cette instance ». Aucune ne vient du statut « indéfini », que T6 compte aussi comme vérifié : aucun gonflement par ce chemin. Chaque instance porte au plus trois éléments, ce qui est la borne que lit T6.

**La sous-banque est tirée comme le code la tire.** Les identifiants de monde viennent de `identifiants_opaques(generateur(racine, 3, 0), …)`, puis vient `tirer_sous_banque(banque, ids, racine, params["sous_banque"])` : ce sont les lignes 125 et 149 de `rejeu.py`. Seuls les items de rôle « analyse » sont comptés (les seconds services et les témoins en sont exclus). J'ai vérifié 75 vrais, 38 faux tôt et 37 pièges sur chaque racine. La sonde appelle `construire_banque` et non `construire_banque_avec_retirage`. Pour une racine acceptée, la banque est la même, car le retirage appelle `construire_banque`.

**Les racines déclarées sont les bonnes.** 0 à 39 et 20261122, soit 41 racines distinctes. `v6-aires.json` porte 42 lignes, dont la racine 11 deux fois : c'est conforme à l'en-tête et à la note A4.

**Recompte indépendant** (script à part, qui n'appelle que les fonctions du code v6).

- Par racine, les nombres de faux tôt et de pièges touchés dans la sous-banque égalent ceux du JSON : 0 écart sur 41 racines.
- Synthèse sur les 75 faux de la sous-banque : 60 à 68 touchés, médiane 63, soit 0,800 à 0,907, médiane 0,840. Pour les faux tôt : 0,789 à 0,921. Pour les pièges : 0,784 à 0,919. Le cumul est de 0,847 pour les faux tôt et 0,846 pour les pièges.
- Banque entière : 20 gabarits touchés 164 fois sur 164, et 4 gabarits qui résistent (F1 « puissance majorée à un pas », 0/164 ; F3 « résidu atteint tôt », 20/164 ; « résidu évité », 15/164 ; « rang d'apparition », 9/164). Vérités touchées : 0.
- Les affirmations du brouillon 4 (§ Bases à battre, P11) et des notes (A1, A4, A5, A6) se retrouvent toutes : 80 % à 91 %, médiane 84 % ; 20 gabarits sur 24 ; 7 à 15 faux hors de portée ; textes de vérités répétés 16, 17 ou 18 (sur 24, 13 et 4 racines) ; un texte de piège répété sur 10 racines (8, 10, 19, 21, 22, 23, 29, 31, 32, 37) ; base « grammaire aléatoire » de 0,052 à 0,125, médiane 0,076. P11, « 58 à 70 sur 75, v_A dans [0,77 ; 0,93] », est cohérente : 58/75 = 0,773 et 70/75 = 0,933.

**Dépendance au plafond 3N et à la borne de trois instances** (cumul sur la sous-banque, 41 racines, 3 075 faux) :

| variante | faux tôt | pièges | ensemble |
|---|---|---|---|
| règle (3N, 1, N + 1), plafond 3N | 0,847 | 0,846 | 0,846 |
| une seule instance, à 3N | 0,836 | 0,838 | 0,837 |
| (1, N + 1) seulement | 0,847 | 0,067 | 0,462 |
| (2N, 1, N + 1), plafond 2N | 0,847 | 0,425 | 0,638 |
| (N, 1), plafond 3N | 0,851 | 0,000 | 0,431 |

La borne « trois instances » ne pèse presque rien : l'instance au plafond fait seule 0,837, et les deux autres ajoutent 0,9 point. Le chiffre des pièges tient entièrement au fait que l'instance avancée soit le plafond 3N. Les pièges sont plantés avec n0 dans ]N .. 3N] (`mondes.py`, outil des pièges), leur expression croît, et la vérification va jusqu'à 3N. Une instance au plafond est donc un contre-exemple par construction. Avec un plafond 2N, les pièges tombent à 0,425 ; à N, à 0. Les faux tôt ne dépendent pas du plafond.

## 3. Le devis v4

**Chaque chiffre est tracé.** Les chiffres des § 1 à 9 se trouvent dans la sortie v4 (blocs 0, 1, 2, 4, 5, 7 à 12) ou dans la sortie v3 (blocs cités « v3-2, 3, 5, 6, 7, 8 » : agent au pire 1,20 ; fumée 0,096 et 0,108 ; repli R1 −10,08, +1,68, +7,50, 172,68, 142,85, 155,88 ; 184,99 ; 147,89 et 156,77 ; intervalle de P7). Les autres sont nommés « supposés » : profils de jetons, forfait de fumée 0,10, prix de la machine 0,28 et 1,30, enveloppe de 12, 24 et 48 heures, profils du protocole P, 0, 10 ou 50 pièces relues. Le seuil de 272 000 jetons est une règle de prix (A13), non un calcul. Les arrondis vont au centime, et ceux des rapports (1,8163 → 1,82 ; 3,5754 → 3,58 ; 1,7774 → 1,78) sont justes.

**La réserve de 6,50 se recalcule.**
- Un item S : agent au plafond 1,50, plus le relecteur au pire sous le repli R1 (Argon à 4 / 20 : 6 000 × 4 + 6 000 × 20 par million = 0,144, plus que Kimi à 0,072), soit 1,644.
- Un autre appel : le plus cher au pire est l'item N, 4 000 × 4 + 24 000 × 20 = 0,496, devant une proposition (0,32) et une reformulation par Argon (0,192).
- Un jugement : Astra au pire, 0,576 (Kimi en repli, 0,144).
- 3 × 1,644 + 2 × 0,496 + 0,576 = 6,500.

Les créneaux répondent au texte de A6 du brouillon 4 (trois items S, deux autres appels, un jugement), et les replis répondent au repli R1 du brouillon 4. Le plafond vaut 192,79 × 1,5 + 6,50 = 295,68, arrondi à 300. Les options (b) et (c) se recalculent aussi : réserves de 6,148 et 1,216.

**La garde de projection de 293,50 se recalcule** : 300 − 6,50. La dépense à la fin du premier bloc (7,62 / 15,69 / 54,00) se recalcule avec la fumée, 40 reformulations, 36 propositions d'Opus, 12 d'Argon à 4 / 20, 18 items de chaque bras et 5 jugements. Au profil « pire », la projection est de 590,56, au-dessus de 293,50 : la garde arrête la course avant le deuxième bloc.

## 4. Effectifs : devis, brouillon 4, code

| effectif | devis v4 | brouillon 4 | code v6 (`parametres_v6.json`, `sous_banque.py`) |
|---|---|---|---|
| mondes | 12 | 12, 4 par famille | 3 familles × 4 mondes |
| par monde | — | 8 vérités, 4 faux tôt, 4 pièges, 5 + 5 témoins ; 192 analysables, 312 plantés | 8, 4, 4, 5, 5 |
| faux de la banque | — | 96 (tirage des 20 faux de mondes) | 48 + 48 (sonde) |
| sous-banque analysée | — | 150 = 75 + 38 + 37 | 75, 38, 37 ; quotas vérifiés sur 41 racines |
| items par bras | 208 | 150 + 48 témoins + 10 seconds services | 2 + 2 témoins par monde, `servis_deux_fois` = 10 |
| items par bloc | 18 au premier bloc | 18 pour les quatre premiers blocs, 17 ensuite (4 × 18 + 8 × 17 = 208) | — |
| propositions | 432 Opus, 144 Argon | 12 + 24 Opus et 12 Argon par monde | — |
| base aléatoire | — | 24 par monde | `par_monde` = 24 (288 par racine dans la sonde) |
| jugements | 60 = 40 + 20 | 40 connus, 20 faux de mondes (10 + 10) | — |

Aucune discordance.

## 5. Écarts, par gravité

**Bloquant : aucun.**

**Moyen 1. Deux des vingt gabarits « tombés » ne sont pas des seuils monotones, et la règle n'y a rien à choisir.** F2 « intersection produit » est un énoncé clos : la seule instance est l'instance vide, et T6 y évalue l'énoncé lui-même. F2 « pire cas indépendant » n'a que des variables à domaine borné : la seule instance prend les plus petites valeurs. Ces deux gabarits font 328 des 1 968 faux tôt, soit 16,7 % des faux tôt de la banque. Sans eux, les faux tôt à variable naturelle sont touchés à 1 332 / 1 640 = 0,812. Ce n'est pas une erreur de mesure : S et N ont le même droit à l'instance vide, et la consigne le dit. Mais l'explication de la note A1 (« un seuil monotone dépassé est faux à toute instance assez grande ») ne couvre ni ces deux gabarits ni les faux tôt qui ne sont pas des seuils (« additive », « Cassini signe », « addition décalée »). Ces derniers sont faux à l'instance au plafond (164 / 164 chacun), et « Cassini signe » comme « addition décalée » le sont dès l'instance 1 (164 / 164) : ils sont faux à presque toute instance. Comptes par instance tirés du JSON de la sonde. À préciser dans le texte : le plancher mêle trois mécanismes (énoncé clos ou sans choix ; seuil dépassé au plafond ; énoncé faux à presque toute instance).

**Moyen 2. Le plancher des pièges est un fait de construction du couple plantation et plafond, non une propriété de la règle.** Il vaut 0,846 au plafond 3N, 0,425 si le plafond servi était 2N, et 0 à N (tableau du § 2). La borne de trois instances n'y joue presque pas. Le brouillon 4 dit bien que A est un plancher et que la version 7 doit fermer la « fuite d'instance ». Il gagnerait à écrire en clair que les pièges plantés dans ]N .. 3N] et croissants sont pris par la seule instance au plafond, et que tout changement du plafond servi ou de la plage de plantation change P11.

**Mineur 1.** Note A1 : « toutes les variables au plafond 3N » ; seules les variables naturelles y sont, celles à domaine borné prennent leur plus petite valeur. Le brouillon 4 l'écrit juste.

**Mineur 2.** L'en-tête du script du devis v4 cite `preenregistrement-pilote-generation-v1-brouillon-4.md`. Le fichier est `…-brouillon-4-v2.md`, R12. Aucun chiffre n'en dépend.

**Mineur 3.** Le facteur de 1,78 que tolère la garde de projection est calculé sur l'attendu simple (165,17). Si les deux lignes conditionnelles se réalisaient (attendu 192,79), la tolérance tomberait à (293,50 − 0,10) / (192,79 − 0,10) = 1,52. À dire au § 3 du devis, ou à préciser : la projection compte-t-elle les unités d'un monde régénéré ?

**Mineur 4.** Le contrôle « vérités touchées = 0 » est attendu par construction : une vérité n'a pas de contre-exemple jusqu'à 3N. Il éprouve T6, non la cécité de la règle. La cécité est établie par lecture du code (§ 2).

## 6. Ce qui n'a pas été vérifié

Les prix relevés (hors mandat : réseau interdit) ; les profils de jetons (supposés) ; les valeurs critiques de la table calibrée et les bornes de Clopper–Pearson du bloc 12, au-delà du rejeu (je n'ai recalculé à la main que les seuils du score apparié en Δ0 = 0 : 6, 8 et 10) ; le texte des notes hors des § A et B.
