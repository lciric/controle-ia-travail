# Extrait à l'octet de la liste d'arrêt du texte scellé du barreau 5, et deux renvois de lignes — v1

Conducteur de la lecture du barreau 5 (session_016QhUrrG5GmnzyjK8E1CZCB), 2026-11-23 18:24Z. Demandé par la mère (session_016QhUrvi45g3jX5saFefVED) pour la conception des sondes, qui écrit la table de correspondance. Ce fichier ne contient aucun résultat : aucun score, aucune issue observée, rien de la table de l'ouvreur. Seul le texte scellé est cité.

Source : `prereg/barreau5-sabotage-ou-empreinte-adaptateurs-tenus-a-l-ecart-v1.md`, sha256 bdff244f1377e795b84f71518bb5e58fb1600fff8afee383d8f70c10d3f5d935. Lignes 345 à 361, recopiées par `sed -n 345,361p` sans aucun changement.
sha256 du bloc recopié (octets des lignes 345 à 361, saut de ligne final compris) : a1be71bd894aacb4be6beee8fded003ed3cb16ba47fbe87ae496d5a12bbd431f

## (b) Deux renvois

- **Où le verdict écrit le nombre de familles de chaque épreuve.** Le texte scellé ne fixe pas de champ du verdict pour cela. Ce qu'il fixe :
  - les familles se comptent épreuve par épreuve, et chaque demi-épreuve de E2 compte les siennes (l. 323) ;
  - une issue porte le niveau le plus faible des épreuves qui la fondent (l. 323) ;
  - sous six familles, l'issue est N, motif « niveau non atteignable » (l. 323 et liste d'arrêt, point 13, l. 359).

  L'écriture elle-même revient au mandat du lecteur du verdict : `docs/notes/barreau5-resolution-v1/plan-avant-entretien/lecture/mandat-juge-verdict-b5f-v2.md` (sha256 17aafef2…), § « Effectifs », point 3, ligne 57. Pour chaque épreuve (M1, M3, E3, E2a, E2b, E1), il relève le nombre de familles présentes K, son niveau (99, 95 ou aucun), « séparé » ou « contraire », et les familles absentes avec leur motif.
- **Niveau de l'issue « empreinte » sous huit familles.**
  - La règle d'ensemble est celle de la l. 323 : une issue porte le niveau le plus faible des épreuves qui la fondent. Mais l'interdit nommé du niveau de 99 % sous huit familles ne vise que les issues S, D et C, et la lecture au niveau déclaré de 95 % y est décrite pour « les mêmes épreuves ».
  - L'issue « empreinte » ne se décide pas par une épreuve des rangs à un niveau. Elle se décide par une condition sur toutes les familles (l. 195), d'erreur au plus 2^−K : 0,0039 à huit familles, 0,0078 à sept, 0,0156 à six (table du « Seuil », l. 185 à 191). Son étendue a une confiance de 1 − 2^(1−K) : 99,2 % à huit (l. 195).
  - Le texte ne dit pas en toutes lettres quel niveau porte le nom de l'issue « empreinte » à six ou sept familles. Le nœud 6 (l. 459, tranché par GO-2026-11-19-88) parle des issues en général. C'est un point à faire trancher, pas à déduire.

## (a) Bloc recopié (lignes 345 à 361)

## Liste d'arrêt

1. Empreinte d'une entrée, d'une consigne, d'un fichier de tâches, de la base avant et après distillation, d'un adaptateur ou d'un fichier de scores différente de celle consignée. Pendant la formation : si l'empreinte est celle d'un adaptateur ou d'une sortie d'une famille, cette famille n'est pas formée et compte absente, pour raison technique écrite, et la famille suivante de l'instance est formée ; si c'est celle de la base, ou d'une entrée commune à l'instance (consigne, fichier de tâches, configuration), l'instance entière s'arrête. Hors de la formation, l'instance s'arrête.
2. Tâche de réserve dans une évaluation, ou tâche d'évaluation dans une distillation : aucune création.
3. Contrôle d'identité à dose 0 en échec, artefact non vu à dose 1, état d'adaptateur d'un lot différent de celui de sa phase : pendant la formation, la famille en cours n'est pas formée et compte absente, pour raison technique écrite ; la famille suivante de l'instance est formée, après la garde du modèle nu (point 4 du plan). Hors de la formation, l'instance s'arrête.
4. Contrôle de l'opérateur d'édition manqué pour une famille (point 3), ou transcriptions de deux membres différentes hors des jetons du nombre : la famille n'est pas formée ; un seul retirage.
5. **Tout score de sonde sur une instance de formation ; toute activation écrite sur disque, gardée ou sortie d'une instance de formation (la garde d'équivalence de la génération de la course de confirmation n'est pas jouée ici : elle demanderait des crochets en mémoire, que cette garde refuse ; « mêmes réglages que la course de confirmation », au point 2, ne la couvre donc pas : écart déclaré) ; tout score de sonde dans l'entraînement, le choix, l'arrêt ou l'exclusion d'un adaptateur** (invariant de N-053) : arrêt ; la famille est invalide.
6. Toute moyenne ou médiane sur les jetons dans un score de sonde : arrêt.
7. Toute statistique d'adaptateur tirée d'un score de sonde, aire ou résumé de score calculé sur l'instance de lecture, ou toute grandeur d'un adaptateur (produits P et poussées compris) écrite dans un journal : lecture invalide, version neuve. Les produits P et les poussées le long de ĝ du point 8 (c), calculés par le programme figé et écrits dans les seuls fichiers fermés, n'en sont pas.
8. Table des étiquettes, branche de la formation ou coût d'un adaptateur tenu à l'écart présents dans l'arbre de la session de lecture : refus, nœud.
9. Engagement absent ou postérieur à la création de l'instance de lecture ; scores non scellés avant l'ouverture ; empreinte de la table différente de l'engagement : refus de la lecture, nœud.
10. Épreuve à vérité plantée non passée, ou programme de lecture d'empreinte différente de celle de `CODE-LECTURE-B5F` : aucune ouverture.
11. Chemin de relecture en échec (cas sain différent, ou artefact égal) : arrêt avant toute notation.
12. Décision sur une pièce (lancer, relancer, abandonner, changer un réglage) prise sur la foi d'une sortie de ce plan, de la répétition générale ou d'un résultat antérieur : pièce invalide. Les coupes de la section « Calendrier », le retirage du point 4, la relance unique d'une instance tombée, le lancement au fil des offres, les deux paliers de la part d'actions non éditables (point 3 du plan), l'évaluation réduite et l'abandon d'une famille à l'approche de la coupure (devis, § 4) sont des règles mécaniques ; elles n'en sont pas.
13. Moins de six familles présentes : issue N, motif « niveau non atteignable », nœud.
14. Dépense : chaque instance s'arrête dès que son cumul relevé plus un quart d'heure atteint sa coupure ; les pièces du devis s'arrêtent toutes à son plafond, que leur seule dépense compte ; une relance, hors de ce plafond, ne compte que dans son enveloppe (« Calendrier », borne de la relance) ; arrêt et destruction par identifiant (R10), après versement de ce qui est récupérable.
15. Clé de ce texte écrite au registre partagé des scellements : arrêt de l'écriture.
