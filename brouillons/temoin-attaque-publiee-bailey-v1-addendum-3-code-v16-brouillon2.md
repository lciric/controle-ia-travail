# Addendum 3 au préenregistrement du témoin de Bailey (`prereg/temoin-attaque-publiee-bailey-v1.md`, `fb6c2f34…`) — code v16 : message d'erreur d'une exécution morte avant tout tour ; nouvelle série après la seconde chute du pilote — brouillon 2

12 novembre 2026. Session « attaquant informé » (`session_01XJ6MgnEhQMZteN9F8a1BST`), branche
`claude/compassionate-meitner-d4ryyk`. **Brouillon 2 : non contre-lu (R2), non scellé** ; il remplace le brouillon 1
(`brouillons/temoin-attaque-publiee-bailey-v1-addendum-3-code-v14-brouillon1.md`, `f5e40842…`, gardé tel quel, R12), qui
décrivait le code v14 (D-9 de la relecture différentielle). Le préenregistrement et ses addenda 1 et 2 restent tels quels ;
en cas de conflit, le préenregistrement prime et l'écart est un nœud. Cet addendum ne contient aucun résultat : aucune
note de sonde ni de juge n'existe (zéro tour complet) et aucune n'a été lue.

## 1. Pourquoi
Run du 12 novembre (conduite v6, code v13 au commit `4988f3f4`, instance 60370363) : mise en place (huit gardes) et
contrôle du juge tenus ; **pilote et reprise du pilote sortis en code 1 en ≈ 71 s, sans journal, configuration effective
« non décidée »** ; issue de la liste d'arrêt : « seconde chute du pilote : pas de run principal, pas de verdict ; nœud »
(`registres/passations/2026-11-12-1545-temoin-bailey-pilote-seconde-chute-noeud.md`, `21f0fc4d…`). Le message d'erreur
n'est pas sorti de l'instance (liste fermée, texte l. 316-319) : cause non établie. Décision de Lazar sur ce nœud :
« go (a) » (`registres/passations/2026-11-12-1720-decision-lazar-bailey-option-a-v14.md`, `df3833a9…`).

## 2. Écarts actés par cet addendum
1. **Liste « Ce qui sort de l'instance » (texte l. 316-319 ; lecture 12) : s'y ajoute un seul fichier**,
   `erreur-demarrage-v1.txt`.
   - **Condition** (toutes requises) : code de retour non nul ; garde de démarrage non décidée ; zéro tour complet ;
     sortie standard reçue égale à un début exact de la configuration attendue ; aucun arrêt décidé par l'instance (ni
     garde de démarrage, ni dépense, ni échéance) : l'enfant est mort de lui-même ; journal des notes (là où l'écrit le
     journaliseur) absent ou vide ; dossiers des sondes et des suffixes (écart 9) absents ou vides, sans lien symbolique
     ni entrée spéciale. Dans ce cas, `train_harmful.py` n'a commencé aucun tour : aucune note, aucun texte produit par le
     modèle sous attaque, aucun suffixe ni aucune sonde n'existe.
   - **Contenu** : les 60 dernières lignes de la sortie d'erreur de l'enfant ; valeurs remplacées sur place (nombre
     décimal ou à exposant : `<nombre>` ; suite de plus de 12 chiffres : `<chiffres>` ; jeton Hugging Face : `<jeton>` ;
     suite alphanumérique de 32 caractères ou plus : `<suite>`) ; ligne qui contient `tensor(` retirée entière ; 300
     caractères par ligne après le filtre ; 20 000 octets au plus. Le filtre ne retire ni les entiers ni les mots : c'est
     une défense en profondeur ; **la garantie vient de la condition**.
   - Le fichier est empreinté, transféré et scellé comme les autres ; il ne sert qu'au diagnostic borné de la liste
     d'arrêt (« nom de la garde, message d'erreur, durées, mémoire »).
2. **Portée (R-3, D-6).** Le message ne sort pas pour une mort après l'impression complète de la configuration, ni quand
   la garde de démarrage tombe, ni quand l'instance arrête l'enfant (dépense, échéance), même avant toute sortie. Dans ces
   cas, le diagnostic de la liste d'arrêt (texte l. 370) se borne au nom de la garde, aux durées et à la mémoire, sans
   message d'erreur. L'étendre serait un nouvel élargissement de la liste fermée : nœud, décision de Lazar.
3. **Écart à la lettre (R-4).** Le message peut contenir la ligne de Hydra des surcharges (graine, nombre de tours,
   chemins) et des morceaux de la configuration ; c'est un écart au texte l. 316-317 (« la configuration … n'en sort pas,
   seule son empreinte »), acté ici. Il ne contient aucune note : aucune n'existe dans ce cas.
4. **Nouvelle série.** La seconde chute du pilote est due à un défaut survenu avant tout tour et avant toute donnée. Une
   **nouvelle série** est permise, une seule : pilote, au plus une reprise, puis la règle et le run principal selon le
   texte, inchangés. Mêmes graines (pilote 1394228342, run principal 1865327867), même B (75 USD), même D (cumulé depuis
   la première instance du poste : 1,976 USD au 12 novembre, 15:33Z, quatre instances détruites). Les exécutions du
   12 novembre sont rapportées comme interrompues ; elles n'ont produit aucune note. Une nouvelle seconde chute du
   pilote : pas de run principal, pas de verdict ; nœud.
5. **Paramètres de lancement** (hors du texte, déclarés) : disque demandé 110 Go (valeur par défaut du code : 200 Go ;
   le devis chiffre 1 à 2 Go de sondes et suffixes) ; offres filtrées à 128,9 Go de mémoire allouée au moins ; la garde
   de mémoire vive du texte (128 × 10⁹ octets, à la mise en place) est inchangée et a passé le 12 novembre ; pilotage par
   un poste Hetzner autonome (« go c » de Lazar).

## 3. Commit et code
**Commit du code : `91238a735a2127a0879fb4533a6cde5baccb4efa`.** Seuls changent, par rapport à l'addendum 2 :

| Rôle | Module | SHA-256 |
|---|---|---|
| Lanceur local | `lanceur_v16.py` | `03df34aabc5146d4136d0ffe61a0df450362cb1c2a50c2030cd612f7cc57a6a0` |
| Lanceur côté instance | `instance_v15.py` | `39725c4c190f73262861ea1fee6f8e4360cca3712c271349b1b44eeff2fd100f` |

Les autres modules sont ceux de l'addendum 2, inchangés (`lecture_v8`, `execution_v3`, `journaliseur_v3`,
`conventions_v3`, `analyse_v3`). Manifeste neuf (R12) : `runs/temoin-bailey-v1-20261111/manifeste-local-v4.json`, écrit
par `lanceur_v16.manifeste_depuis_versions_figees` avec ce `commit_code` (l'archive envoyée sur l'instance est tirée de ce
commit ; le manifeste v3 citait `4988f3f4`) ; versions figées et graines inchangées.

**Défaut corrigé (règle R4).** Dans `executer`, une liste locale nommée `signal` masquait le module `signal` depuis la
v7 : les trois arrêts internes d'une exécution (garde de démarrage tombée, dépense B − 2, échéance) levaient
`UnboundLocalError` et laissaient l'enfant vivre ; les relectures du code v7 à v12 ne l'ont pas vu. Trouvé par l'essai v14,
confirmé par la relecture du code v14 ; corrigé (`signaux`), et un essai vérifie qu'aucune fonction de l'instance ne lie
un nom local `signal`.

**Essais (R5)** : `tests/test_temoin_bailey_condition6_v16.py` (`f5b71cad…`) : 161 passés (les 139 essais v13 rejoués,
les essais du message d'erreur v14 et v15, ceux de la relecture différentielle : filtre, enfant muet arrêté par la
dépense et par l'échéance, vacuité, lecture d'un dossier d'étape qui porte le fichier) ; `test_temoin_bailey_analyse_v3`
(36 passés). L'essai instable `test_v13_P2_…` est corrigé dans l'essai (attente bornée ; cause établie : bénigne en
production).

**Contre-lectures du code (R2)** : `docs/notes/reproduction-attaque-publiee-v1/relecture-code-condition6-v14-bailey-v1.md`
(`0e7c96ca…`, conforme après corrections) ; `…/relecture-differentiel-code-condition6-v15-bailey-v1.md` (`0d7cc2a1…`,
conforme après corrections) ; les corrections D-1 à D-8 sont dans le commit ci-dessus.

## 4. Ce qui ne change pas
Hypothèse, prédictions, métriques, seuils, population, juge, modèle, bras, graines, B, critères de lecture gelés, liste
d'arrêt (hors les écarts du § 2), lectures 1 à 38 actées, risques déclarés de l'addendum 2.

## 5. Points ouverts pour Lazar (à trancher avant le scellement)
1. **Essai à blanc.** Le « go (a) » prévoyait un essai à blanc sur une petite carte avant de relouer une A100. La garde de
   mémoire vive (128 × 10⁹ octets) exclut la plupart des hôtes de petites cartes, et un essai hors conduite serait un code
   de plus. La première exécution v16 sur A100 joue le même rôle (si le pilote meurt encore, le message sort ; coût
   observé : ≈ 0,44 USD). Recommandation : remplacer l'essai à blanc par cette exécution.
2. **Délai de la garde de démarrage (R-10).** Une garde de démarrage jamais décidée n'a pas de délai : un enfant bloqué
   avant l'impression n'est arrêté que par la dépense B − 2, l'échéance ou le chien de garde, et ne laisse pas de message
   (§ 2.2). Coût borné par B. Options : (a) garder ainsi pour cette série, avec une alerte de la session à Lazar si le
   pilote n'a pas fini 4 heures après son lancement (devis : 2 h attendues, 3,8 h au pire) ; (b) délai borné dans une
   version suivante, avec un nouvel addendum. Recommandation : (a).
