# Organismes discrets, bras A — vérification du brouillon 3 du devis de l'essai de mesure des lecteurs — v1

- **Pièce vérifiée** : `docs/notes/relance-organismes-discrets-v1/devis-essai-de-mesure-lecteurs-bras-a-v1-brouillon3.md`, branche `claude/pensive-bardeen-1fv7hw` (tête `de052f27e`), empreinte `533ad5b15e6de1bdfe81c35f8501dbad376f52f907be84094c3fd8621b349592`, recalculée et conforme. Comparé au brouillon 2, `ae9e75bba8b8…`.
- **Vérification de référence** : `verification-devis-essai-de-mesure-brouillon2-v1.md` (`f2180d176673…`), points D1 à D4, recommandations E1 et E2.
- **Vérificateur** : le même contre-lecteur (Claude Opus 5.5), le 2026-11-19, vers 10:15 UTC. Périmètre limité aux trois questions posées.
- **Interdits tenus** : rien lu dans `diag/`, `runs/`, `donnees/` ni `docs/verdicts/`. Le relevé de vérification de la clé Claude n'a pas été ouvert, et son empreinte (`7ce262ba…`) n'est pas recalculée ici : la garde G8 la contrôle au lancement. Aucun appel payant ; réseau : `git fetch` seulement ; aucun fichier existant modifié ; rien committé.

## Conclusion

**Engageable.**

## 1. Le diff du brouillon 2 au brouillon 3

Méthode : comparaison mot à mot des deux fichiers (`git diff --no-index --word-diff`), 29 passages changés.

**Le plan et le plafond ne bougent pas.** Les tableaux des entrées (4.3), des files (5.1) et des coûts (6.3), ainsi que la règle de choix (7.3), sont intacts. Les mentions de 17,75, 9,25, 6,00 et 2,50 sont en même nombre dans les deux brouillons.

Chaque passage changé relève de l'une de ces catégories :

| catégorie | passages |
|---|---|
| **D1** (clé Claude) | 0, point 3 ; 5.6 (Claude) ; 6.4 (ligne de la file Claude) ; garde G6 ; garde G8 ; 11, point 7 ; configuration (empreinte de l'attestation) ; doute 10 |
| **D2** (pages de prix scellées) | en-tête ; pièces lues ; 6.1 (trois lignes du tableau et règle du repli) ; 11, point 3 |
| **D3** (codes non listés) | garde G4, deux colonnes |
| **D4** (refus de code 400 compté au pire cas) | 5.5 ; paragraphe sous 6.3 ; garde G1 ; doute 4 |
| **E1** (délais des relais) | 5.3 ; 5.4 ; garde G2 ; doute 12 ; configuration (« options et délais des relais ») |
| **E2** (clé partagée) | 5.6, puce « Clé partagée » |
| **phrases proposées pour les doutes 1 et 2** de la vérification du brouillon 2 (relais de GPT et secret du réseau ; budget de réflexion de Carbon) | 5.6 (GPT) ; garde G6, artefact ; 6.3, condition (c) ; 8.1 (relevé par envoi de Carbon) ; doute 1 |
| **tenue du dossier** | en-tête (état, auteur, interdits) ; pièces lues (trois lignes ajoutées) ; 10 (contre-lecture) ; 11, point 2 ; 12.4 (table de traitement) ; 14 |

**Un seul ajout hors de cette liste** : la puce « Règle de permission » en 5.6, et le point 8 de la section 11. Ils viennent du journal (OD-104, OD-105) : un appel Claude a été refusé une fois par le classifieur de permissions de la session. Le devis exige donc une règle de permission étroite pour la seule commande du chef d'essai, posée sur un mot de Lazar, et dit que rien ne sera tenté pour la contourner. C'est une condition de départ de plus pour la seule file Claude. Elle restreint, ne touche ni au plan ni au plafond, et ne demande aucune correction. Mais c'est un écart au « remplacements exacts, rien d'autre » annoncé par l'auteur : il faut le dire.

## 2. D1 et D3 à la lettre

**D3 : fait à la lettre.** La phrase « **Tout autre code que 200 et ceux nommés ici** (404, 413, 422, …) : arrêt de la file, sans reprise, code et origine (relais ou amont) au journal. » est insérée à la place demandée, avant « Les autres files continuent ». L'artefact « réponse 404 : arrêt de la file, sans reprise » est ajouté.

**D1 : fait à la lettre, avec des ajouts de fait.**
- La garde G6 (« pour Claude, `RR_ANTHROPIC_API_KEY_RIGAUD` ») et la section 11, point 7, reprennent mot pour mot les textes « après ».
- En 5.6, le texte « après » est repris entier, avec quatre ajouts :
  - la citation de la lettre « par le formulaire sécurisé » ;
  - le passage entre crochets, rempli : « Cet emploi est couvert par le mot de Lazar « go reco a », donné dans la session de relance (événement `e27e9fdd…`, 09:57:23Z ; journal, OD-105) » ;
  - les compteurs de l'appel (10 jetons d'entrée et 1 de sortie, 1,5e-6 dollar) ;
  - l'empreinte de l'attestation, `7ce262baf640…`.
- **Sur le passage entre crochets** : selon le journal (OD-105), ce mot de Lazar a permis la seule commande qui lit la clé par le nom `RR_ANTHROPIC_API_KEY_RIGAUD`, et la ligne GO-2026-11-19-31 met la part Claude sur la clé Rigaud. L'emploi de cette variable pour l'essai en découle. Je ne l'ai pas relu à la source (événement `e27e9fdd…`). Ce n'est pas bloquant.

## 3. La clé Rigaud n'a été vérifiée que sur Haiku 5.5

**Sans risque pour le plafond : oui.**
- Un refus d'accès à un modèle rend un code 403 ou 404 chez Anthropic. Une erreur de cette classe n'est pas facturée.
- Le relais Claude compte zéro pour une réponse sans compteur d'usage (`relais_reel.py`, ligne 321, `cout = … if usage else 0.0`). Le chef d'essai compte zéro ou, au plus, le pire cas d'un envoi. Les deux compteurs ne peuvent donc que monter plus vite que la dépense réelle.
- La garde G4 arrête la file au premier refus, sans reprise : 403 comme refus de compte, 404 par la règle ajoutée en D3. Aucun envoi ne suit.

**Bien dit : presque.** La phrase de 5.6, « un refus de la clé pour Opus 5.5 ou Sonnet 5.5 se lirait au premier envoi de la file (garde G4) », est juste pour Opus 5.5, joué en premier, mais pas pour Sonnet 5.5 : son premier envoi vient après les 24 lectures d'Opus 5.5 à l'effort bas. Et la phrase ne dit pas la conséquence. Un 403 est un refus de compte : il arrête toute la file Claude, donc les modèles pas encore joués ne sont pas mesurés, même s'ils sont accessibles. C'est sûr pour le plafond, mais cela coûte la mesure. Précision proposée, non bloquante, à faire au prochain passage ou dans la configuration :
- Avant (5.6) : « L'appel n'a vérifié que Haiku 5.5 : un refus de la clé pour Opus 5.5 ou Sonnet 5.5 se lirait au premier envoi de la file (garde G4). »
- Après : « L'appel n'a vérifié que Haiku 5.5. Un refus de la clé pour Opus 5.5 ou Sonnet 5.5 (code 403 ou 404, non facturé) se lirait au premier envoi de ce modèle : Opus 5.5 au premier envoi de la file, Sonnet 5.5 après les 24 lectures d'Opus 5.5 à l'effort bas. Il arrête toute la file Claude, sans reprise (garde G4). Les modèles pas encore joués ne sont alors pas mesurés, et la file ne se reprend que sous une ligne nouvelle. Aucune dépense ne s'ajoute à celle des envois déjà servis. »

## 4. Pièces lues

| pièce | empreinte |
|---|---|
| devis, brouillon 3 | `533ad5b15e6d…` |
| devis, brouillon 2 | `ae9e75bba8b8…` |
| vérification du brouillon 2 | `f2180d176673…` |
| `docs/notes/ideation-organisme-v1/orchestrateur-v52b/pole/relais_reel.py`, lignes 255 à 330 | `1b90b020287e…` |
| journal de la relance, entrées OD-104 à OD-106 (lu pour la vérification du brouillon 2) | registre vivant |
