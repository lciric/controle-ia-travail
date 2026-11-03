# Pièce servie au collisionneur — l'organisme en fonctionnement réel : faits mesurés, étages non joués, mesures absentes — v1

Écrite par la session conv-audit (Claude), 3 novembre 2026, vers 10:35 UTC (`date -u`), pour le tour du collisionneur sur la conception de l'organisme. **Faits internes non encore publiés** (aucune donnée personnelle, aucune clé) ; chacun renvoie à sa source : registre de décisions de session-depot (« SD R-n »), registre de conv-audit (« CA R-n »), dossier factuel de l'organisme (« DF § n », `docs/notes/ideation-organisme-v1/explication-organisme-v1/dossier-factuel-organisme-v1.md`, `0751fc8c…`), message n° 312 de session-depot, README public (`bdd6516f…`). Ce qui est public est dans la pièce « nos résultats » et dans le README, servis à part ; rien n'est répété ici. **Aucune recommandation** : cette pièce dit ce qui est, pas ce qu'il faut faire.

## 1. Course 1 (29 et 30 octobre 2026), sur une question du programme de contrôle
- Tentative 1 (29 octobre) : arrêtée ; refus du proposeur Opus 5.5, puis **bascule automatique non autorisée** du kit d'agent vers Opus 4.8 (sortie mise à l'écart, jamais lue) ; aucune fiche (SD R-764).
- Tentative 2 (30 octobre) : proposeurs Fable 5.1 et Argon, deux passes ; **29 fiches validées**, 3 en quarantaine ; le juge Fable 5.1 refuse (arrêt propre, sans bascule) (SD R-804).
- Rejugement par Opus 5.5 et Argon : 27 fiches éligibles sur 29 (15 de Fable, 14 d'Argon ; 5 et 5 dans les dix premières) ; **accord de rang entre les deux juges 0,12** ; totaux serrés (12,0 à 12,5 sur 15 dans les dix premières) ; les 6 témoins sont tenus, mais tous plus courts que toutes les fiches (épreuve plus faible qu'annoncé) (SD R-811).
- **12 paires de doublons**, toutes entre la passe 1 et la passe 2 du même proposeur : **17 idées distinctes sur 29 fiches** (SD R-820).
- Troisième juge, Kimi : **auto-préférence d'Argon ≈ 1,8 point sur 15** (écart Argon − Fable : −0,55 chez Kimi, −0,73 chez Opus, +1,21 chez Argon) ; Kimi échoue à un témoin (SD R-827).
- Coût ≈ 37 USD (SD R-811). **Aucune fiche de la course 1 n'est devenue une hypothèse ou une expérience du programme** (DF § 10).
- Corrections tirées de la course 1 : mémoire anti-redite (passe 2 nourrie des fiches de la passe 1, bardeaux de mots), témoins de longueur comparable, notation croisée, aiguillage (DF § 5.1, § 10).

## 2. Course du 3 novembre 2026 (organisme complet), sur une question de pilotage des activations
- Cinq espèces (Fable 5.1, Opus 5.5, Astra, Argon, Kimi), une génération, deux bras du bisociateur (basique et substitut de Gu et Krenn) ; **57 min 52 s, code 0, 10,03 USD** pour un devis attendu de 23,61 (n° 312).
- **46 fiches classées** (Fable 7, les autres 8), dont **7 fusions** du bisociateur ; 1 fusion inachevée ; mariages : 4 par bras ; 3 fiches « notables » selon les juges (n° 312).
- Mémoire anti-redite : **46 idées distinctes sur 46, 0 redite** (bardeaux de 3 mots, seuil 0,6, version v53 ; `memoire.json` de la sortie).
- Une fiche de proposeur classée « à corriger » par l'aiguilleur : **son contenu n'est conservé nulle part dans la sortie** (le journal de l'aiguilleur ne garde que l'identifiant et l'empreinte) (CA R-1346).

## 3. Étages et mécanismes jamais joués pour de vrai
- **Tests de mort** : codés et essayés hors ligne ; bac à sable jugé non sûr par deux contre-lectures (voie vers le superutilisateur de l'hôte), durci ensuite ; jamais joués en course réelle (DF § 9.2 ; README, section 4).
- **Boucle entre générations** : codée et essayée hors ligne, jamais jouée pour de vrai (README, section 4).
- **Duel des proposeurs** (proposeur de la littérature contre le nôtre, même juge) : devis écrits, aucun lancement (DF § 9.4).

## 4. Essais et tranches déjà faits sur les mécanismes de diversité et de mémoire
- **Tirage par déterminant** (diversité de domaine entre deux parents, « volume du parallélépipède ») : codé, puis **réfuté** par préenregistrement scellé le 26 octobre sur mondes à ponts plantés (−4,8 et −2,2 points contre le tirage stratifié ; part de paires éloignées 0,532 contre 0,525) ; marche de Swanson par étiquette rare +3,5 et +3,8, sous le seuil de +12 ; tirage stratifié gardé par défaut (CA R-497).
- **Bisociation à deux espaces v2** (volume des domaines × proximité des concepts) : préenregistrée, validation non concluante (DF § 10).
- **Mémoire du pôle** (simulation) : signature prédictive plutôt que texte, redites manquées 0 à 3,5 % contre 100 % ; proposeur qui lit la mémoire 24,0 vraies associations par course contre 12,8 (placebo) et 11,8 (sans mémoire), avantage nul dans un monde sans structure (DF § 5.2).
- **Marchepieds** (simulation, cycle v5) : 282 contre 212 vraies filles dans un monde fécond, 236 contre 245 dans un monde plat (DF § 10).
- Mémoire « spectrale » d'un organisme antérieur : rappel 0,000 sur textes réels (DF § 5.2).

## 5. Mesures absentes du code aujourd'hui
- Aucune mesure de **diversité** ni de **richesse** des fiches entre passes, entre bras ou entre générations (entropie, couverture, distance à une archive) ; la seule garde est la redite par bardeaux (CA R-1350).
- Aucune **règle d'arrêt** d'une lecture ou d'une course autre que les plafonds de dépense et la durée. Une question sur une règle d'arrêt (entropie de Shannon, critère de Cauchy, richesse et nouveauté de l'information tour après tour) a été écrite le 29 octobre pour le collisionneur et n'a jamais été lancée (CA R-443, R-447, R-1350).

## 6. Exploitation
- Le relais d'Argon sert **un seul appel à la fois** : deux usages simultanés sont exclus.
- Une course longue suppose une session gardée vivante : la première course d'A1-v3 a été arrêtée après environ 5 minutes par la reprise du conteneur qui l'hébergeait (41 appels, 4,25 USD, aucun résultat) (CA R-1345).

