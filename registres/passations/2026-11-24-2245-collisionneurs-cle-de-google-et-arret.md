# Passation — session des collisionneurs, soir du 24 novembre 2026 : conscience et émergence, idées intéressantes, option de clé de Google, arrêt

Écrite vers 2026-11-24T22:45Z. Classe C.
- Session `session_016QhUrsc1rhjmmiLEmqPygF` (compte neuf), branche `claude/upbeat-edison-t3wegg`. Tête au moment d'écrire : `36b2fc5e`, puis ce commit.
- Suit `2026-11-24-1630-collisionneurs-conscience-emergence.md`, qui reste en vigueur pour ce qu'elle ne remplace pas.
- Mère : `session_016QhUrvi45g3jX5saFefVED`. Sa consigne de 22:26Z : finir la vérification des corrections par le même contre-lecteur, écrire la passation, puis s'arrêter jusqu'au 28 novembre ou jusqu'au mot de Lazar sur la clé de Google.

## Fait depuis 16:30Z

### Dossier « idées intéressantes »
`runs/collisionneur-protocole-x-idees-interessantes-abonnement-v1-20261123-135306` (GO-2026-11-23-21 et -22, plafond 30 USD).
- **Tour 2 (critique croisée) : complet.**
  - Fable et Opus étaient déjà recueillis.
  - Argon valide au quatrième essai, Carbon au troisième, Neon au premier.
- **Tour 3 (réponse) :**
  - Opus : session `session_016QhUrvMkCBbjUzQD6qyWA6`, effort high, recueillie vers 22:25Z (`e5b5252f…`, 19 072 caractères, toutes les lignes du kit couvertes).
  - Fable : kit `cbf1e7eb` poussé sur `kits-abonnement/idees-interessantes-E3-T3-reponse-A-v1`. Session non créée, car la limite hebdomadaire de Fable est atteinte sur ce compte.
  - Argon : refusé par Google à 21:48Z (HTTP 402, crédit prépayé épuisé), non compté.
  - Carbon et Neon : pas encore partis.
- **Compteur : 14,63 USD sur 30.** Les coupures et les erreurs 503 sont comptées au pire ; le refus 402 n'est pas compté.

### Dossier « conscience et émergence »
`runs/collisionneur-protocole-x-conscience-emergence-abonnement-v1-20261123-134849` (GO-2026-11-23-19, plafond 40 USD).
- **Tour 2 :**
  - Argon valide ; Carbon valide au deuxième essai.
  - Neon interrompu deux fois par des erreurs 503 de forte demande, comptées au pire.
  - Fable : kit `746c9315` poussé sur `kits-abonnement/conscience-emergence-E3-T2-critique-croisee-A-v1`, en attente du quota.
- **Compteur : 8,95 USD sur 40**, compté au pire.

### Refus de crédit de Google
- Pièce : `docs/notes/collisionneur-v9/reprise-v8d-v1/pannes-abonnement-v1/refus-de-credit-google-2026-11-24-v1.md` (`6807a3e9…`).
- Le changement de clé dans l'environnement a été refusé par le classifieur du mode automatique. Il n'a été ni rejoué ni contourné.
- Côté Google, tout est suspendu (choix d de la mère).

### Option `--cle-gemini` du moteur
Nommer la clé de Google par son nom, comme `--cle-openai`, au cas où Lazar autoriserait une autre clé. Rien n'est lancé avec cette option. Toutes les pièces sont sous `docs/notes/collisionneur-v9/`.
- **v8q**, gardée intacte et non admise par la voie v8 :
  - moteur `collisionneur_v9_v8q.py` (`047489b8…`), voie abonnement v7 (`fd1c37b7…`), vague v3 (`51c27240…`), rapport du développeur (`605bb63c…`) ;
  - contre-lecture par un agent Opus neuf : `contre-lecture-collisionneur-v9-v8q-opus-v1.md` (`c22da939…`), onze défauts.
- **Corrections en v8r** :
  - moteur `collisionneur_v9_v8r.py` (`1656351a…`), voie abonnement v8 (`98f1a1d6…`), vague v4 (`7819b2aa…`), rapport du développeur (`75b59995…`) ;
  - essais : 22 pour le moteur, en processus, transport coupé, environnement vidé (`test_collisionneur_v9_v8r.py`, `47049da4…`) ; 5 pour la voie (`abonnement-v1/test_voie_abonnement_v8.py`, `966c553e…`) ; 16 mutations tuées sur 16 (`mutations_collisionneur_v9_v8r.py`, `4f0edcf3…`).
- **Gardes de la v8r** :
  - `GEMINI_API_KEY_3` est refusée à la composition et à chaque envoi.
  - `GEMINI_API_KEY_FREE` n'est admise que pour Carbon et Neon (R-5294).
  - Un nom de clé d'un autre fournisseur est refusé pour l'espace d'Anthropic : une clé de Google ne doit jamais partir vers Anthropic (mère : « garde la correction »).
  - Le nom de la clé, jamais sa valeur, est journalisé au premier lancement hors défaut et à chaque changement.
  - La voie v8 n'admet `--cle-gemini` qu'avec le moteur v8r.
- **Vérification des corrections par le même contre-lecteur** : `verification-corrections-collisionneur-v9-v8r-opus-v1.md` (`8bd78570…`).
  - Verdict : **conforme avec réserves**. Les onze défauts sont corrigés ou déclarés ; aucun défaut bloquant ni majeur.
  - Un espion de processus refusait et notait tout accès au réseau. Il n'a relevé aucune tentative.
  - La reprise des deux dossiers sous v8r tient, sur des copies : les dépenses, le devis et les 8 kits restent identiques.
  - Les cinq réserves mineures sont reprises au point 3 du « Reste ». Leur effet : un échec sûr, ou une défense en profondeur sans artefact ; rien ne peut partir à tort.
- **Écart déclaré**, consigné par la mère, sans coût ni vraie clé :
  - les essais de la v8q n'étaient pas coupés du réseau ;
  - une requête de comptage portant la valeur factice est très probablement partie vers Google pendant ma campagne de mutations du v8q ;
  - l'espion du contre-lecteur a ensuite attrapé et refusé une tentative de la même forme. Elle venait d'une copie du v8q lancée en ligne de commande, où était retiré le refus de `GEMINI_API_KEY_3` (l'une de mes quatre mutations) ; voir la contre-lecture du v8q, lignes 150 et 151 ;
  - les essais de la v8r ferment cette voie.

### Versement du bloc-notes de la session
Fait selon la règle « récupérer ce qui est récupérable », dans `registres/passations/recuperation-blocnotes-collisionneurs-016QhUrsc1rh-2026-11-24/`.
- Inventaire de 1 242 fichiers (`blocnotes-collisionneurs-inventaire-v1.tsv`, `177811ae…`) : chemin, taille, empreinte, présence dans le dépôt.
- Archive des 305 fichiers dont l'empreinte n'était pas déjà dans `docs/` ou `runs/` (`blocnotes-collisionneurs-fichiers-non-verses-v1.tar.gz`, `e9821a16…`, 9,4 Mo). Elle contient :
  - les scripts d'épreuve du contre-lecteur (espion de processus, mutations, épreuves de reprise et de kits) ;
  - les mutants ;
  - les extraits de texte des sources des revues, tirés des PDF et des XML déjà versés ;
  - les scripts de téléchargement.
- Le script qui a fait l'inventaire et l'archive est versé avec eux (`verser_blocnotes_v1.py`, `441de6e9…`).
- Aucune chaîne de forme de clé n'a été trouvée avant l'archivage (recherche par motifs, noms de fichiers seulement).
- Rien de ce versement n'est réemployé dans une mesure sans texte contre-lu et sans le mot de Lazar.

## Reste
1. **Rien ne part avant le 28 novembre ou avant le mot de Lazar sur la clé de Google.**
2. **Mot de Lazar sur la clé de Google**, deux voies :
   - (a) Il recharge le crédit de `GEMINI_API_KEY` sur AI Studio. On relance alors avec la vague v2 et le moteur v8m, sans option de clé.
   - (b) Il autorise une autre clé. On relance alors avec la vague v4, le moteur v8r, `--cle-gemini <NOM>` et `--reprise`. Le point 3 passe d'abord.
   - Dans tous les cas, jamais `GEMINI_API_KEY_3`, et `GEMINI_API_KEY_FREE` seulement pour Carbon et Neon.
   - Réserve d'exploitation du contre-lecteur : un seul nom de clé vaut par lancement, et la garde refuse la clé libre dès qu'Argon est dans la composition. Dans les deux dossiers en cours, qui comptent Argon, la seule clé utilisable avec le v8r pour les trois espèces de Google est donc `GEMINI_API_KEY_2`. Employer la clé libre pour Carbon et Neon demanderait un nom de clé par espèce, donc une version neuve du moteur.
   - Cellules à finir : aux idées intéressantes, Argon, Carbon et Neon du tour 3 ; en conscience et émergence, Neon du tour 2, puis le tour 3.
3. **Avant tout lancement sous v8r, traiter les cinq réserves mineures de la vérification.** Les corrections vont dans des versions neuves, puis une vérification courte est faite par le même contre-lecteur s'il vit encore, sinon par un agent Opus neuf (écart déclaré).
   - Refus de `--cle-gemini` par la voie : ajouter deux cas sains. Avec le v8r, le refus de `GEMINI_API_KEY_3` doit venir du moteur ; avec le v8m sans l'option, on attend le code 2 de l'analyse des arguments, sans message de la voie.
   - Contrôle du préfixe au moment de l'envoi : ajouter un artefact (`OPENAI_API_KEY` injecté sur les trois chemins, zéro requête).
   - Artefact du refus de l'espace d'Anthropic : un nom par préfixe d'un autre fournisseur, et pas seulement de Google.
   - Deux commentaires hérités disent encore « clé épuisée » (lignes 529 et 1125 du v8r) : erratum.
   - Forme abrégée `--cle-gem` : la voie doit refuser tout argument qui commence par `--cle-g` hors du v8r.
   - Le contre-lecteur suggère aussi de mettre un garde-fou de processus dans les essais, comme son espion.
4. **Après le 28 vers 04:00Z (quota de Fable)** :
   - créer les deux sessions Fable en effort high, puis les recueillir avec `recueil_session_v6.py` : le tour 2 de conscience et émergence (kit `746c9315`) et le tour 3 des idées intéressantes (kit `cbf1e7eb`) ;
   - en conscience et émergence, le tour 3 ne s'ouvre qu'une fois le tour 2 complet, Fable comprise.
5. **Notes de sortie** des deux dossiers, en Markdown et en PDF (GO-2026-11-22-74). Elles déclarent l'écart d'effort (« max » sur les fiches, « high » servi), les absences et les réponses hors dossier (Opus pour la conscience, la cellule non conforme).
6. **Décisions en attente de Lazar** : brainstorm d'Opus D1 à D4 ; Fable D1 à D5 ; données humaines, huit décisions ; candidature d'OpenAI, quatre points ; clé de Google.

## Réserves
- Toute la dépense est comptée au pire, au-dessus de la dépense réelle. À relever sur la facture de Google.
- `registres/etat.md` est tenu par la mère et n'est pas touché ici. La mère reporte cette passation.
- La limite hebdomadaire de Fable est atteinte sur ce compte ; remise à zéro le 28 vers 04:00Z.
- Les tests du dépôt n'ont pas été lancés, faute de torch dans cet environnement. Seuls les essais propres aux scripts ont tourné, avec la bibliothèque standard.

## Prochaine action
Rien jusqu'au 28 novembre ou jusqu'au mot de Lazar sur la clé. Ensuite, selon le cas, reprendre le point 2 (avec le point 3 d'abord pour la voie b) ou le point 4 du « Reste ».

## Instances actives
Aucune instance de calcul lancée par cette session, ni sur Vast ni sur Hetzner. Aucun processus de vague en cours. Seulement des appels d'interface, sous les plafonds des GO cités.
