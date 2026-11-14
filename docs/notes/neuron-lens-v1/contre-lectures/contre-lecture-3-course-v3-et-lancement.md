# Contre-lecture 3 du volet A (assemblage v3, chargement, lanceur, garde de dépense, commande) — rapport (résumé fidèle)

Contre-lecteur : sous-agent neuf, « modèle D », lancé après le commit 9ea1b78d, rapport lu avant 12:14 UTC ; il n'a écrit aucune des
pièces ; lecture seule (essais du chargement, du lanceur et de la garde : 18 passés ; fumée de la course non relancée). Empreintes
conformes (texte gelé, quatre pièces, commande, liste des versions, essais).

**Verdicts** : `volet_a_course_v3.py` après corrections mineures ; `volet_a_chargement_v1.py` **scellable en l'état** ;
`volet_a_lancer_v1.py` après corrections mineures ; `garde_depense_v1.py` après corrections (une moyenne) ; `commande-volet-a-v1.md`
après corrections (plusieurs moyennes ; non exécutable telle quelle).

**A.** Remarques de la contre-lecture 2 : 2, 4, 5, 6, 7, 8, 10 traitées ; 1 à moitié (devis non refait) ; 3 par déclaration (pic
transitoire) ; 9 en partie (pas d'essai NaN de A3). **B.** Audit R4 : déclencheur conforme ; sixième découpe `spawn(6)[5]` conforme
(clé « enfant suivant », même ramification, C3 d'abord) ; retrait vérifié conforme (couche 14, découpe 0, déclaré) ; lecture (c)
défendable quant au but, mais « permutée » non rendu et aucune règle de lecture écrite. **C.** Chargement conforme à l'addendum et aux
formats du code voisin archivé (clés J et K, 2f lignes « + » puis « − », ligne f+11672, c = +b̂ sur lobe négatif, colonne 344 de
`down_proj`) ; `catalog.kept` recalculé ; garde du rendu sur tous les textes. **D.** Lanceur : ordre et liste d'arrêt respectés, rien de
silencieux. **E.** Garde : seuils, destruction par identifiant, crédit relevé, R5 essayé.

**Remarques**
1. Moyenne — devis périmé : sans cache, ≈ 960 000 séquences pour A3 (C1 ≈ 242 000, C2 ≈ 719 000), 4 à 7 h, 2 à 6 USD, plus la sixième
   découpe ; refaire le devis, mesurer le débit réel avant la course.
2. Moyenne — économies sans changer les résultats : réutiliser le score d'origine si l'invite n'est pas modifiée ; ne pas calculer
   la tête de langage ; arrêter la propagation à la couche lue (module d'extraction).
3. Moyenne — `destroy` qui échoue fait mourir la garde : réessayer, vérifier, journaliser, code non nul.
4. Moyenne — minuterie : option absente du `main` ; durée à compter de la création ; rappel indépendant (`send_later`) à 80 %.
5. Moyenne — audit (c) : ajouter la variante « étiquettes permutées et P retiré » ; écrire la règle de lecture (rang comparé à celui de
   la course, information rapportée, verdict inchangé).
6. Mineure — essais : égalité des 5 premières graines de `spawn(6)` avec l'arbre ; NaN de A3 → arrêt, bruts déjà écrits.
7. Moyenne — commande : `git` absent de l'image ; filtre `cuda_max_good>=12.8` ; `cpu_cores_effective>=8` ; paquet sans HEAD
   (cloner par `--branch`) ; contrôler `torch.cuda.is_available()`.
8. Mineure — pic mémoire des cas sains (deux copies de 5 Go) : travailler sur les gardés.
9. Mineure — `pos_v0` sans garde d'indice.
10. Mineure — `_retirer_dans_invite` peut rendre `None` dans l'audit (c) : garde explicite.
11. Mineure — fumée de 22 min non comptée au devis ; frais de téléchargement non déclarés.
12. Info — rapatriement périodique des `diag/<run_id>/` (une destruction à 90 % perdrait les bruts) ; licence et empreintes de
    `manifeste.py`, `scellement.py` non vérifiées par le lanceur ; partie 2 de l'addendum lue comme relevé scellé avant la première
    passe : à confirmer par la mère.
