# Transmission à Lazar — audit des failles de notre contrôle, synthèse v3 — v1

De : conv-audit, le 2026-10-26 14:28:50 UTC (heure lue sur `date -u` dans la commande qui écrit cette ligne).

## Verdict

La synthèse v3 (`audit-failles-controle-v3.md`, sha256
`4f74b366d2353a47d776865fdeece456cdb1488f03f4a5cbf78b5d88bc468c33`, 2 160 lignes environ) est **transmissible** :
trois contre-lectures sur Fable 5.1 (N-052) par un même contre-lecteur neuf — v1 « transmissible après corrections »
(`7b8a17c3…`, CLS-01 à 15), v2 « transmissible après corrections » (`652a79cc…`, CLS2-01 à 12), v3 « transmissible »
(`7c7fc806…`, trois mineurs non corrigés : compagnon de l'écart ajouté ici ; HT-01 l. 731 « contre la compensation » à lire
« contre le motif de HR1 » ; 98 lignes ajoutées au LISEZMOI, 99 à l'écart). Chaque chiffre renvoie à une page ou à une
pièce ; scripts de calcul rejoués à l'identique par le contre-lecteur ; aucune recette ; rien de confidentiel (aucun
montant, financeur ni nom de la page de titre) ; aucun arrêt par filtre dans cette chaîne.

## Où lire

Canal `canal/conv-audit-n04`, dossier `brouillons/canal-reprise-releve-v1/envois/audit-failles-controle-v1/` :
`sortie-synthese-v3/` (synthèse, LISEZMOI avec la table « constat → traitement », calculs v4, écart v2 → v3) ;
`contre-lecture-synthese-v1/`, `-v2/`, `-v3/` (rapports, calculs du contre-lecteur) ; `sortie-synthese/` (v1) et
`sortie-synthese-v2/` gardées intactes (R12). Commencer par la section 0 (en-tête : avertissement sur le rapport, synthèse
en dix lignes), puis la section 8 (décisions).

## Ce qui attend Lazar (section 8 : D-01 à D-19)

- Nœuds sans défaut (statu quo sans GO ; bilan de la section 8) : D-01 révision du rapport consolidé avant envoi, troisième
  partie comprise ; D-02 ; D-03 ; D-07 (critère de G1, règle de combinaison entre modes : trois lectures libres à 5 %
  donnent jusqu'à 14,3 % de franchissements à tort) ; D-08 ; D-10 ; D-11 ; D-17 ; le volet « critère » de D-16.
- Dépenses sans défaut : D-05, D-06, D-12, D-14 (famille (iv)), D-15 (second agent), et les volets de dépense de D-04,
  D-16, D-17, D-18, D-19.
- Défaut sous 48 heures : D-04 (b), D-09 (a), D-13 (a), D-18 (a) pour la méthode, D-19 (a) pour les parties sur processeur.

## Convergence avec session-depot (R-521, P-031 à P-035) — à trancher une seule fois

- **D-02 = P-031** : même objet (N-053 point 1). Le fichier `docs/decisions/decision-N-053-v1.md` porte les deux phrases
  (« deux bras rapportés, qui ne servent pas de critère » et « la lecture filtrée est la lecture principale de toute
  revendication d'« intention » ») ; les deux lignées demandent le même remède : lecture principale sur les organismes sans
  consigne en contexte ((ii) puis (iv)), témoin apparié en indication dans les négatifs, filtrage des positions en
  diagnostic rapporté. Voisin direct trouvé après la v1 : 2601.21112 (février 2026, « extraire puis évaluer »).
- **D-14 et P-032** (témoins de la famille (iv) avant son devis) se complètent ; **D-15 et P-035 (b)** (second agent
  Qwen2.5-7B, plan agent × juge) sont la même dépense ; **D-13 et P-034** (contrôles de validité en bras rapportés) se
  recouvrent en partie — à lire ensemble.

## Deux réserves

1. Les jugements sur la troisième partie du rapport (E à I) sont établis par calcul indépendant sous des nuls simplifiés
   choisis par l'auteur, rejoués par le contre-lecteur ; ce ne sont pas les expériences du rapport, non exécutées. Un
   point de prudence (R-519) : la synthèse reste au niveau des détecteurs ; aucune stratégie d'attaque n'y est conçue.
2. Deux failles candidates restent indécidables sur nos pièces (FC-01, FC-02, statut « proposé ») ; 2410.12555 n'est
   connu que par résumé (non opposable).
