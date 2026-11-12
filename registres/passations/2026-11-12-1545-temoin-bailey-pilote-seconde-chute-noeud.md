# Témoin de Bailey — run v6 : seconde chute du pilote ; pas de run principal, pas de verdict ; nœud — 12 novembre 2026, 15:45 UTC

Session `session_01XJ6MgnEhQMZteN9F8a1BST`, branche `claude/compassionate-meitner-d4ryyk`. Ne se réécrit pas (R12).

## Verdict (liste d'arrêt du préenregistrement `fb6c2f34…`)
**« Seconde chute du pilote : pas de run principal, pas de verdict ; nœud. »** Aucune relance sans version nouvelle
(préenregistrement : « Seconde chute du pilote : pas de run principal, pas de verdict ; nœud »).

## Déroulé (journal `sortie-conduite-v6/conduite-v5.jsonl`, bilan `bilan-conduite-v5.json`, poussés par le poste)
- Mots de Lazar : « abaisse le filtre à 129 Go maintenant ; non on ne va pas attendre 24h pour louer, on loue ce qu'il y
  a now ». Filtre de mémoire allouée à 128,9 Go (les offres « 129 Go » ont 128 980 Mo), disque demandé à 110 Go (valeur
  par défaut du code, 200 Go, absente du préenregistrement et du devis ; aucune A100 80 Go à 200 Go louable à 14:57Z) :
  conduite v6 (`99a31ae7…`), poste v5 (`9ff5077d…`).
- Poste v5 (Hetzner 175841505) : offre 59858182 (New Jersey, 1,2547 USD/h) choisie à 15:02:49Z ; conduite PID 7800 ;
  instance 60370363 créée à 15:02:56Z, c = 1,2839 USD/h, prête en 23 s.
- Amorce finie ; auto-arrêt disponible (API, chien de garde, identifiant, variables) ; **mise en place : huit gardes
  passées** (commits, dépôt public, empreintes, graines, mémoire vive, Python, révisions, versions) ; pas par tour 1 600 ;
  longueur de suffixe 13 (écart 10 : vrai, différente des 16 jetons de l'article) ; **contrôle du juge : garde passée,
  contrôles tenus**.
- **Pilote** (graine 1394228342) : code de retour 1 après ≈ 71 s ; 0 tour complet ; journaux `gardes-v3.jsonl` et
  `technique-v3.jsonl` absents ; « configuration effective : non décidée » (le script public n'a pas imprimé sa
  configuration) ; aucune ligne de durée. **Reprise du pilote** : identique.
- La conduite a transféré (transfert complet), posé la marque, détruit l'instance. Poste fini à 15:33:32Z, détruit par son
  identifiant à 15:44:10Z.

## Cause : non établie
Le message d'erreur du script public n'est pas sorti de l'instance : la liste fermée « Ce qui sort de l'instance »
(texte l. 316-319 ; lecture 12) ne garde que les lignes de durée et l'état des gardes, et l'instance est détruite. Le
préenregistrement permet un « diagnostic borné au nom de la garde, au message d'erreur, aux durées et à la mémoire » :
ici, le message d'erreur manque. Hypothèses, aucune vérifiée : import de `sparsify` (« à surveiller » sur l'instance,
addendum 2, § 2) ; surcharge de configuration refusée par Hydra ; dépendance manquante ; disque (110 Go).

## Dépense
Instance 60370363 ≈ 0,44 USD ; **D du poste = 1,976 USD** (quatre instances, toutes détruites) ; B = 75 USD. Postes
Hetzner ≈ 0,02 EUR.

## Nœud — ce qu'il faut pour aller plus loin (décision de Lazar)
Une version nouvelle du code (v14) qui fait sortir de l'instance le message d'erreur d'une exécution sortie sans journal
(dernières lignes de la sortie d'erreur, filtrées : ni note, ni texte, ni suffixe), contre-lue, éprouvée, et un
addendum 3 qui l'acte ; puis un essai à blanc de l'exécution publique sur une petite carte avant de relouer une A100.

## Restes
Clé de déploiement GitHub à retirer par Lazar ; clé `ssh` Vast 1864483 à retirer. Aucune instance ni poste actif créé par
cette session. Notes du pilote : aucune n'existe (zéro tour).
