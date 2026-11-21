# Vérification du programme des deux essais d'admission du bras A — livraison 5 (fichiers `_v4`) — v1

- **Vérificateur** : Claude Opus 5.5, contre-lecteur des livraisons 1 à 4, le 2026-11-21. N'a écrit ni le programme, ni le devis, ni l'avenant.
- **Objet** : le commit `64789043c` et sa note `note-programme-essais-admission-bras-a-v4.md`. Les six fichiers `_v4` (chef d'essai, deux relais, faux fournisseur, essais, gabarit v4) répondent « OK » à leur compagnon.
- **Essais** :
  - la commande imposée, deux fois : **188 passés à chaque fois** (92 et 95 s) ;
  - six essais jetables, hors du dépôt (`…/scratchpad/essais_jetables_l5/test_l5_jetable.py`) ; cinq confirment, le sixième a corrigé ma propre hypothèse (section 4).
- **Interdits tenus** : aucun réseau, aucun `git fetch`, aucune clé, `GO_ID` jamais fixé, **aucune commande de liste par motif**, rien écrit hors ce rapport, rien scellé.

## Verdict

**Engageable pour la ligne de calcul qui sera ouverte, une fois les décisions de Lazar inscrites. Une correction est due avant de lancer Mistral sans Google : D-1, le découplage.** C-1 et C-2 sont fermées, les mineurs codés sont fermés, et la campagne de mutations tient (91 mutants tués sur 91). Mais le constat est une seule pièce, lue en entier pour toute ligne : une ligne de Mistral ne peut pas partir tant que les clés de Google ne sont pas prêtes, et l'inverse est vrai aussi. Le passage à 65 536 se fait par la seule configuration, mais les plafonds en dollars de la configuration et du registre devront suivre l'avenant 2 (section 4).

## 1. C-1 et C-2

- **C-1 est fermée** : mon essai, rejoué (`test_p1_rejoue_c1`), voit la somme retirée et la ligne refusée quand le lien entre clé et projet est levé, même avec « deux projets distincts : oui » (`chef:783-825`). La règle employée est dite au contrôle du crédit et recopiée.
- **C-2 est fermée** : mon essai, rejoué (`test_p2_rejoue_c2`), voit « borne de réflexion démentie » dès qu'un jeton passe la borne (`borne_dementie`, `chef:1506-1512`). Le défaut joue dans la file (`defaut_de_reponse_google`, `chef:1515-1535`), à la vérification (ligne 13, `chef:2090-2092`) et à la sonde, où il est porté comme mesure (`chef:2249`).
- **Le choix de l'arrêt de la file, pris à défaut : accepté.** C'est la lecture prudente : au-delà de la borne, la garantie « réflexion plus 16 000 » ne tient plus pour ce qui suit. L'arrêt ne fait pas « ne pas tenir » un modèle qui aurait tenu sous une borne honnête, puisque la borne est une déclaration de notre côté. Il faut donc dire à Lazar que la borne doit être choisie haute : sous le niveau gardé à 65 536, la plus haute admise est 49 536. Une borne basse ferait échouer le juge pour un chiffre de configuration.

## 2. Les mineurs codés, et les mutations

| | fermé ? | appui |
|---|---|---|
| m-1 recharges survenues | **oui** : lues, contrôlées, recopiées au manifeste, au relevé et au rapport, et dites (« À DIRE À LAZAR ») | essai du dépôt `test_m1_l5_…` |
| m-3 défauts comptés à part | **oui** : `nombre_de_defauts_google` et `codes_200_recus` au rapport. La lecture du rédacteur est acceptée : un même envoi peut figurer comme défaut et comme refus, car les compteurs `refus` et `fins_par_sortie_maximale` sont ceux des règles du devis ; le verdict n'en change pas | `test_m3_l5_…` |
| m-5 taux borné par chaque montant | **oui** : au plus 24 heures avant le montant le plus tardif, au plus 6 heures après le plus ancien (`chef:722-723`) | `test_m5_l5_…` |
| m-2 mutations | **oui, avec une réserve** : 91 tués sur 91, sur les six gardes de la règle de Google. Les outils vivent dans le bloc-notes de la session (`…/scratchpad/mut/`), qui peut être effacé : à verser au dépôt, sous un nom versionné, pour que la campagne puisse se rejouer | note, section 4 |

## 3. Les mineurs non codés

- **m-4, sonde sous la forme « budget »** : sans objet si Lazar garde le niveau (décision du 21 novembre, section 4). À rouvrir seulement si la forme « budget » revient.
- **m-7, deux fichiers hors du périmètre modifiés** : `git status` les montre toujours (` M`). Il faut les rendre par `git checkout`, sur le mot de Lazar, avant tout lancement de ces chantiers ; sans effet sur ces essais.
- **m-6, découplage de Mistral et de Google : bloquant pour l'objectif dit.** Deux essais le montrent :
  - `test_p3_constat_sans_les_cles_de_google_ne_sert_pas_mistral` : un constat qui ne porte que les clés de Mistral est refusé (« clé manquante ») pour toute ligne, Mistral comprise. `lire_constat` exige les vingt-huit clés, chacune à une valeur admise (`chef:640-700`), et `gardes_avant_depart` le lit pour toute ligne (`chef:3201`). Une clé de Google non prête ne peut pas être levée : seules six le sont, et aucune ne porte sur l'offre payante, les crédits ou la devise.
  - `test_p3b_credit_de_mistral_bas_arrete_google` : l'inverse, un crédit de Mistral sous 8,23 USD, arrête une ligne de Google (`chef:727-731`).
  - De plus, la ligne de taux est exigée dès qu'**un** montant du constat est en euros (`chef:723`) : un compte Google en euros impose un taux, daté de 24 heures, à une ligne de Mistral en dollars.

### D-1 — Découpler le constat par fournisseur

- **Correction** : une ligne de Mistral ne lit, ne contrôle et n'exige que les clés de Mistral, et la ligne de taux seulement si un montant de Mistral est en euros. Une ligne de Google fait de même pour les clés de Google.
- **Deux formes possibles** : deux pièces de constat (une par fournisseur, chacune à son empreinte dans la configuration de ses lignes), ou une pièce dont les clés de l'autre fournisseur sont absentes ou à « non prêt », tant que ses lignes ne partent pas.
- **Le reste est déjà découplé** : les verrous, la garde 20 et les seuils de Google sont par fournisseur ; les vérifications et les files sont des lignes distinctes. Seule la garde 9 couple.
- **Essais à écrire** : constat Mistral seul, ligne de Mistral : part ; même constat, ligne de Google : refusée.

## 4. Plafond de Google à 65 536, niveau gardé, sonde exemptée : la configuration suffit-elle ?

**Oui, sans code neuf**, à quatre valeurs de configuration près :
- `fournisseurs.google.sortie_max` : 65 536 ;
- `reflexion` : `{"forme": "niveau", "borne_declaree": N}`, avec N ≤ 49 536 (sinon `controler_la_configuration_de_google` refuse, `chef:1434`) ;
- `exemption_de_la_sonde` : vrai, avec son GO ;
- les limites de mots.

Le reste suit seul :
- la réserve de chaque ligne de Google se déduit de `sortie_max` (`reserve_de_la_ligne`) ;
- le relais reçoit `--borne-reflexion` ;
- le contrôle `outputTokenLimit` de la liste suit la sortie maximale ;
- aucun 32 768 n'est écrit en dur dans le chef ; l'essai du dépôt `chef:…` `test_…` de la ligne 3105 l'éprouve déjà sur le contrôle d'avant l'envoi.

**Ce que la configuration doit changer aussi, par l'avenant 2, et que le programme ne fera pas de lui-même** :
- **Plafonds en dollars** (`plafond_usd` et `plafond_registre` de chaque ligne, et les lignes du registre) :
  - à 65 536, la réserve d'un envoi de Neon monte à environ 1,00 à 1,06 USD. Sous le plafond de 8,50 USD de la file, la garantie du devis (6.4 : un modèle dont chaque envoi reste sous la sortie maximale n'est jamais refusé) tombe. Une file de longues lectures peut être arrêtée à son plafond et ne pas tenir pour une raison de caisse ;
  - à la vérification, mon essai `test_p4_…` a d'abord échoué, et c'est mon hypothèse qui était fausse. Un appel A fini à son coût réel laisse partir la sonde sous 1,50 USD : rien n'est bloqué tant que les envois finissent. Mais trois envois comptés à leur réserve ne tiennent plus sous 1,50 (2,95 USD) ; `test_p4b_…` passe avec un plafond de 3,00.
- **Délais** : 65 536 jetons en 2 690 secondes demandent 24,4 jetons par seconde (devis 5.6 : 12,2 à 32 768). Il faut relever `delais.total_s` et `relais_total_s` de la file Neon, ou écrire cette limite. Le délai global se recalcule seul.
- **Seuils de crédit** (19,76 et 16,08 USD) : ils dérivent des plafonds et des excès du devis, et sont à recalculer dans l'avenant 2.

## 5. Ce que j'ai ouvert

- La note de livraison 5, en entier.
- Le chef `_v4`, aux lignes 640 à 745, 783 à 830 et 1506 à 1535, plus des recherches de lignes ; les essais `_v4`, aux lignes 60 à 110, 178 à 198, 395 à 401 et 3105 à 3107, plus des recherches de lignes.
- `git log`, `git status`, et les empreintes par `sha256sum -c` sur six chemins nommés un à un.
- Lus par programme pendant les essais : le lot des entrées nommé par le devis, les consignes et les règles par empreinte, les modules du programme de forme.
- Aucun chemin interdit ouvert, listé ni empreinté ; aucune liste par motif.
