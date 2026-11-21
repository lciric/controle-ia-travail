# Contre-lecture du programme des deux essais d'admission du bras A — livraison 4 (fichiers `_v3`) — v1

- **Contre-lecteur** : Claude Opus 5.5, auteur des contre-lectures des livraisons 1 à 3 et de la confrontation à la règle Google, le 2026-11-21. N'a écrit ni le devis, ni l'avenant, ni le programme.
- **Objet** : le commit `616fb1504` et sa note `note-programme-essais-admission-bras-a-v3.md`. Les six fichiers `_v3` (chef d'essai, relais de Mistral, relais de Google, faux fournisseur, essais, gabarit v3) répondent « OK » à leur compagnon.
- **Essais** :
  - la commande imposée, trois fois : **177 passés à chaque fois** (89 à 99 s) ;
  - sous charge (huit boucles de calcul, deux suites en parallèle), l'essai de la garde 19 qui coupe une file à sa borne en octets (20 rejeux) et l'essai de la file du juge à deux relais (6 rejeux) : 52 sur 52 ;
  - deux essais jetables neufs, hors du dépôt, qui confirment C-1 et C-2.
- **Interdits tenus** : aucun réseau, aucun `git fetch`, aucune clé, `GO_ID` jamais fixé, rien écrit hors ce rapport, rien scellé.
- **Débord, à déclarer** : un `ls scripts/*_v3.py tests/*_v3.py`, lancé pour trouver les fichiers livrés, a **affiché les noms** de fichiers d'autres chantiers, dont des noms sous les motifs interdits (`scripts/mots_et_cout_*`, des noms qui portent `t07`). Aucun de ces fichiers n'a été ouvert, cherché ni empreinté.

## Verdict

**Engageable après corrections : deux corrections, sept mineurs.** Le partage par rang ne fait partir aucun envoi en double, ne dépasse pas le plafond partagé et ne fausse aucun compte. G-1 à G-9 et les trois voies de la vérification 3 sont fermées. Restent deux trous :
- le retrait de la plus grande des deux dépenses, au lieu de leur somme, n'est sûr que si l'on sait quelle clé paie quel projet ; or ce lien peut être levé (C-1) ;
- la garde « réflexion plus 16 000 » ne relit jamais la réflexion réellement facturée : la borne déclarée ou le budget n'est jamais démenti par la réponse (C-2).

## 1. Partage par rang : deux clés, deux relais, un seul compteur

- **Un compteur, un plafond** pour toute la file (`chef:2600`), en série : chaque envoi repasse le contrôle de la réserve, quelle que soit sa clé (`chef:2626-2631`). Aucun dépassement du plafond partagé n'est possible par le partage.
- **La clé du rang** : elle vient du tableau écrit à la configuration, égal à la règle de l'avenant, sinon rien ne part (`chef:337-372`). La reprise reste sur la clé du premier envoi (`chef:2618-2621`). `controler_la_voie` refuse avant l'envoi toute autre adresse (`chef:2565-2575`).
- **Panne d'une clé au milieu de la file** :
  - 401, 402 ou 403 : arrêt sans reprise ; la file ne tient pas, ce qui est conforme au devis (règles 1 à 3) ;
  - coupure ou délai : reprise unique sur la même clé ;
  - 429 : attente, puis reprise sur la même clé.
  La signature du mandataire est lue dans le journal du relais de l'envoi (`chef:2645`). Un départ sans réponse porte sa variable de clé au journal (`chef:2637`), et la dépense reconstituée est attribuée par clé (`chef:920-924`). Je n'ai trouvé ni envoi en double ni compte faux.
- **Deux relais**, bornés chacun à huit envois (`chef:2921-2925`) ; chacun refuse de partir si l'autre variable de Google est dans son environnement. L'amorce les arrête tous deux par leur identifiant de processus, et additionne les alertes de clé des deux (`chef:3338-3361`).
- **Verrous** : un verrou par fournisseur, et un verrou « des vivants », tenu par l'amorce, l'ouvrier (`pass_fds`) et chaque relais. Un ouvrier ou un relais orphelin retient toute ligne du fournisseur, avec un motif écrit qui dit de l'arrêter par son identifiant (`chef:3240-3249`). C'est un blocage voulu, non silencieux.

## 2. Dépense retirée à chaque solde, constat à vingt-huit clés

- Le constat est **lu** : vingt-huit clés, toutes et elles seules (`chef:635-733`). Une clé levée ne passe que si elle est levable, nommée à `cles_levees`, sous le GO de la configuration, avec la valeur et la source exactes. Aucune clé de Mistral n'est levable. Rien de silencieux de ce côté.

### C-1 — Le retrait de la plus grande des deux dépenses alors que le lien entre clé et projet est levé

- **Où** : `chef:778-807` (`controler_credit_de_google`) ; la levée vient de `CLES_LEVABLES` (`chef:122-124`), au gabarit `cles_levees`.
- **Ce qui se passe** (éprouvé par `test_p1_deux_projets_distincts_avec_cles_levees_retire_le_max`) : avec `google_deux_projets_distincts` à « oui », la dépense retirée de **chaque** projet est la plus grande des deux dépenses comptées. Ce n'est sûr que si chaque clé paie un projet différent. Or `google_cle_du_projet_constate_cle_1` et `…_cle_2`, les seules clés qui disent quelle clé appartient à quel projet, font partie des six levées par GO-2026-11-21-68. Prenons 5 USD dépensés sous chaque clé et 25 USD vus sur chaque projet : le programme retire 5 et trouve 20, au-dessus de 19,76 ; la ligne part. Mais si les deux clés paient le projet a, il y reste 15, sous le seuil.
- **Correction** : retirer la plus grande des deux dépenses seulement si `google_deux_projets_distincts` vaut « oui » **et** si les deux clés du projet constaté sont constatées (non levées). Sinon, retirer la somme. Le relevé et le manifeste disent la règle employée. Un essai par cas.

### Mineur sur ce point

- **m-1** (`chef:978-981`) : la ligne « recharges survenues : nombre N ; montant M » de la lecture de la console est exigée par sa forme, puis **ignorée**. Avec la recharge automatique active et non comptée, une recharge survenue est un paiement que personne ne voit au relevé. La recopier au relevé et au manifeste, et la dire à Lazar si N vaut plus que 0.

## 3. G-1 à G-9

| | fermée ? | appui |
|---|---|---|
| G-1 garde commune | **fermée par reproduction** : la règle dit « l'emploie ou la reproduit » ; reproduite au chef (`chef:1361-1488`) et au relais (`relais_google:193-218`) ; aucun module commun sous `src/controle_ia/`. Réserve m-2 sur les mutations | lecture |
| G-2 plafond ≥ réflexion + 16 000 | **fermée avant l'envoi**, sous les deux formes (`chef:1389-1411`, `:1431-1469`) ; **non fermée après la réponse** : C-2 | `test_regle_google_g2_…` |
| G-3 limite de mots | fermée (`chef:1415-1428`, `:1466-1469`) ; les limites restent à inscrire par quelqu'un d'habilité | `test_regle_google_g3_…` |
| G-4, G-5 zéro pensée, texte vide | **fermées** : « défaut journalisé, jamais une réponse », la file s'arrête sans jugement de forme (`chef:2550-2553`, `defaut_de_reponse_google` `:1472-1488`). `thoughtsTokenCount` absent vaut 0, donc défaut. Réserve m-3 | `test_regle_google_g4_g5_…` |
| G-6 vérification sans pensée | fermée : ligne 13 du classement, nœud de Lazar (`chef:2040-2044`) | `test_regle_google_g6_…` |
| G-7 sonde | fermée : envoyée seulement sous une exemption inscrite avec son GO, et pour son seul corps exact (`chef:2353-2358`, `:1453-1463`) ; réserve m-4 | `test_regle_google_g7_…` |
| G-8 relais | fermée : le relais refuse un corps sans réflexion explicite ou sous le plafond ; l'exemption ne vaut qu'au plafond de la sonde, et seulement sur une ligne de vérification | `test_regle_google_g8_…` |
| G-9 gabarit | fermée : les champs nuls arrêtent tout | `test_gabarit_…` |

### C-2 — La borne de la réflexion n'est jamais confrontée à la réflexion facturée

- **Où** : `chef:1472-1488` (`defaut_de_reponse_google`) et `decider_dans_la_file` (`chef:2525-2560`).
- **Ce qui se passe** (éprouvé par `test_p2_reflexion_au_dela_de_la_borne_declaree_n_est_pas_un_defaut`) : sous la forme « niveau », la borne de 16 768 jetons n'est qu'une déclaration. Sous la forme « budget », rien n'établit que le service tient le budget. Une réponse dont `thoughtsTokenCount` passe la borne, finie en `STOP`, est jugée comme les autres. La garantie « réflexion plus 16 000 » devient purement déclarative, et la course héritera d'une borne démentie sans que personne le sache.
- **Correction** : à chaque réponse de Google (vérification, file, et sonde comme mesure), comparer `thoughtsTokenCount` à la borne. Au-dessus, c'est « borne de réflexion démentie » :
  - dans la file, un défaut journalisé qui arrête la file, ou au moins un constat porté au rapport et au nœud de Lazar ; c'est à trancher par Lazar, à défaut le défaut ;
  - à la vérification, la ligne n'est pas saine.
  Un essai par forme.

## 4. Les trois voies de la vérification 3

| voie | fermée ? |
|---|---|
| numéro de processus de l'amorce repris après un redémarrage | **oui** : identité du processus (numéro, heure de départ, identifiant de démarrage de la machine) comparée (`chef:3455-3489`) |
| fausse alerte de clé qui ne se lève qu'en révoquant la clé | **oui** : levée « faux positif », admise seulement si aucun relais n'a vu la valeur exacte de sa clé (`chef:1030-1068`) |
| verrou tenu par l'amorce seule ; ouvrier orphelin | **oui** : verrou par fournisseur passé à l'ouvrier, verrou des vivants partagé avec les relais (`chef:3229-3249`, `:3321-3322`) |

## 5. L'écart sur la recharge, et le taux admis 6 heures après la pièce

- **`recharge_comptee` à faux** : **accepté**. L'écart à l'avenant (4.4) va du côté prudent : chaque projet ne compte que son solde vu, et le chemin de l'avenant reste dans le code, inatteignable en configuration définitive. Il faut le dire à Lazar : avec la recharge automatique active et non comptée, les seuils de 19,76 et de 16,08 USD peuvent retenir une ligne que la recharge aurait couverte. Et ils ne bornent plus la perte : seuls le compteur et la lecture de la console la bornent.
- **Taux jusqu'à 6 heures après l'heure de la pièce, jamais après l'envoi** (`chef:538-567`) : **accepté**, c'était ma proposition. Au constat, l'heure de référence est la plus tardive des heures des valeurs vues. Un montant vu tôt peut donc être converti à un taux relevé jusqu'à 30 heures plus tard : à dire dans la note, ou à borner par l'heure de chaque valeur (m-5).

## 6. Mineurs

- **m-1** : les recharges survenues sont ignorées (section 2).
- **m-2** : la règle Google demande « essais et mutations à l'appui ». Les mutations se limitent aux bornes déplacées d'un jeton dans les essais. Une campagne de mutations par outil, même courte, sur `garde_google_avant_envoi`, `defaut_de_reponse_google` et `defaut_du_corps`, est due.
- **m-3** : un défaut de Google (G-4 ou G-5) reste compté parmi les « réponses de code 200 » du rapport (`chef:` `faire_rapport`, compteur `reponses_de_code_200`). Le verdict n'en change pas, la file étant non complète, mais le rapport doit compter ces défauts à part, puisque la règle dit « jamais une réponse ».
- **m-4** : sous la forme « budget », le corps de la sonde porte `thinkingBudget` égal au budget de la file (par exemple 16 384) avec `maxOutputTokens` 256. Que le service l'admette n'est pas relevé. Un refus classerait l'issue ligne 12 (« brouillon neuf »). À dire avec la décision de Lazar sur la forme.
- **m-5** : l'heure de référence du taux au constat (section 5).
- **m-6** : le seuil de crédit de Mistral (8,23 USD) arrête aussi les lignes de Google (écart 5 de la note) ; c'est un couplage à dire à Lazar, sans risque de dépense.
- **m-7** : deux fichiers suivis et scellés hors du périmètre (`scripts/epreuve_temoins_seuls_v3.py`, `scripts/lancer_course_affinage_mentors_v3.py`) restent modifiés par le `sed` du rédacteur (`git status`). Ils ne répondent plus à leur compagnon : à rendre par `git checkout` avant tout lancement de ces chantiers, sur décision de Lazar.

## 7. Ce que j'ai ouvert

- La note de livraison 4, en entier.
- Le chef `_v3`, aux lignes 99 à 163, 337 à 372, 506 à 586, 622 à 810, 884 à 1003, 1340 à 1505, 1731 à 1768, 2013 à 2050, 2340 à 2365, 2525 à 2700, 2921 à 2960 et 3190 à 3388, plus un index des fonctions et des recherches de lignes.
- Le relais de Google `_v3`, `defaut_du_corps` et des recherches de lignes.
- Le gabarit v3, par programme : `constat_cles`, `cles_levees`, `recharge_comptee`, la marge, les réglages de Google, les bornes des relais.
- `git log` et `git status`, empreintes par `sha256sum -c`, et le `ls` du débord déclaré en tête.
- Lus par programme pendant les essais : le lot des entrées nommé par le devis, les consignes et les règles par empreinte, les modules du programme de forme.
- Bloc-notes, hors du dépôt : `essais_jetables_l4/test_l4_jetable.py` et `test_charge_v3_jetable.py`.
