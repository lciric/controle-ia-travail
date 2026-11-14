# Consigne du contre-lecteur de la commande du compte 3 (lecture de 7b et étape B de T0.7) — v1

- **Pour la mère** : à donner telle quelle, comme seul message, à **un sous-agent neuf du modèle C** (jamais le modèle B,
  indisponible jusqu'au 2026-11-20 15:00Z, R-2718 ; jamais le rédacteur ; identité du modèle dite en conversation, jamais
  écrite). Écrite le 2026-11-14 par le préparateur (modèle A), qui n'a pas pu lancer lui-même ce sous-agent : son outillage ne
  crée pas de sous-agent (rapport, réserve 1).
- **Règle R2** : le contre-lecteur n'a écrit aucune des pièces lues ; il reçoit ici la liste explicite des fichiers à lire.

---

Tu es le contre-lecteur neuf (règle R2) d'une commande écrite que Lazar collera comme premier message d'une session neuve du
« compte 3 », qui hébergera deux lecteurs de verdict : la table A de T0.6 sur la course 7b, puis l'étape B de T0.7. Français ;
aucun sigle non développé ; aucune heure écrite à la main (`date -u`).

**Interdits** (permanents) : aucune dépense ni machine ; aucune valeur de clé (jamais `env`, `printenv`, `set` sans argument,
`export -p`, `/proc/*/environ`) ; **aucune sortie de 7a, 7b ou T0.7 ouverte** (ni `diag/`, ni `runs/`, ni `donnees/` de ces runs,
ni les branches `calcul/t06-confirmation-7b-v1`, `donnees/t07-etape-a-v1`, `calcul/p3bis-reel-v2`) ; jamais
`diag/*/lecture-sondes-t06.json`, la lecture B de 7a, `donnees/lecture-b-7a-quarantaine-v1`, `donnees/mesure-unanime-v15-sortie-v1`,
`essai/t06-explo-v3`, l'étiqueteur, `donnees/bras-attaque*`, `donnees/mode-tenu-a-l-ecart*`, `docs/notes/bras-attaque/`,
`registres/index-bras-attaque*`, `anteriorite-bras-informe*`, la branche `claude/compassionate-meitner-d4ryyk` ; aucune recherche
récursive large (fichiers nommés seulement) ; aucun commit, aucune poussée ; un refus de permission ou d'un classifieur :
arrêt, tu le rapportes tel quel.

**À lire, et seulement cela** (dépôt `/home/user/controle-ia-travail`, empreintes à vérifier par `sha256sum` contre les
compagnons avant lecture) :
1. `docs/procedures/lecture-7b-etape-b-compte-3-v1/commande-compte-3-v1.md` (l'objet) ;
2. `docs/procedures/lecture-7b-etape-b-compte-3-v1/prealables-v1.md` ;
3. `docs/procedures/lecture-7b-etape-b-compte-3-v1/controle_a_blanc_etape_b_compte_3_v1.py`,
   `attestation_qui_a_lu_quoi_compte_3_v1.py`, leurs essais (`essai_*.sh`) et sorties (`essai-*-sortie-v1.txt`),
   `controle-a-blanc-etat-actuel-sortie-v1.txt` ;
4. le modèle suivi : `docs/procedures/P3-bis-commande-compte-2-v1/commande-ouverture-verdict-p3bis-compte-2-v2.md` ;
5. le code que la commande appelle : `src/controle_ia/t07/registre_v1.py`, `lecture_v4.py` (docstring, `etape_b`, `main`),
   `lecture_v2.py` (`ouvrir`, l. 395-600), `lecture_v1.py` (`lire_table_A`, `lire_fuites`, `lire_episodes_t06`,
   `lire_issue_mots_et_cout`), `code_t07_v1.py` (`controler_code`), `garde_adaptee_v1.py` (`garde_etape_b`) ;
6. les passages des textes scellés cités par la commande et les préalables : `prereg/T0.6-organismes-v0-v1.md` l. 467-588
   et 763-771 ; `prereg/T0.7-sondes-v0-v1.md` l. 1413-1480 et 2091-2215 ; `prereg/T0.8-base-A-mots-et-cout-v1.md` l. 113-170 ;
   `prereg/T0.7-consigne-audit-fuites-v1.md` § 3 et § 4 ;
7. `docs/notes/plan-paquet-multi-comptes-v1/brief-compte-3-v1.md` ; `registres/qui-a-lu-quoi-v1.md` (en-tête et ligne 77) ;
   `registres/scellements-v1.md` ; `docs/procedures/ordre-execution-etape-a-t07-v2.md` § 5 bis et § 9 ;
   `docs/procedures/ordre-fille-course-confirmation-7b-v1.md` l. 25-40 et 374 ; `scripts/extraire_mesures_epreuve_t06_v1.py`
   (en-tête et fonction `mesures`) ; registre des décisions, lignes R-2704, R-2711, R-2714 à R-2716, R-2718 (par
   `grep -n '^| R-27xx '`).

**Questions, dans l'ordre** (réponds à chacune ; « rien à redire » est une réponse) :
- Q1. La commande peut-elle faire lire à la session hôte, ou remettre à un lecteur, un fichier fermé (`lecture-sondes-t06.json`,
  `resume.json` de 7b, activations, adaptateurs, scores bruts de T0.7, une pièce de l'étape B bis) ? Cite le bloc et la ligne.
- Q2. Les blocs A1 à A5 suffisent-ils à un verdict R13 de la table A (pièces du lecteur au regard de T0.6 l. 510-570 :
  effectifs, réserves, audit R4, réserve de mémoire de `run.err`) ? Manque-t-il un fichier, ou en remet-on un de trop ?
- Q3. La règle des préalables sur l'extracteur (constat 1 : T0.6 l. 771 ferme `lecture-sondes-t06.json` jusqu'au contrôle
  d'ouverture v2) est-elle juste ? La commande l'applique-t-elle partout ?
- Q4. Phase C : la garde du module (`lecture_v4 etape-b` depuis l'arborescence détachée à C7, racine = la branche, registre =
  `registres/scellements-v1.md` de la branche) recevra-t-elle tout ce qu'elle exige (clés, `lecture-cout-t06.json`,
  `episodes-t06.json` avec mesures et textes, manifestes, `sondes-t07.json`, scores recomposés, audit, fichier « mots et coût »,
  journal de P3-bis) ? `CODE-T07` passera-t-elle (`controler_code` dans une arborescence détachée) ?
- Q5. La condition d'ordre (plan de B bis scellé avant l'étape B) est-elle contrôlée par programme sans faire refuser le
  lecteur de T0.7 ? Le cloisonnement B / B bis est-il tenu dans les deux sens ?
- Q6. Irréversibles : chaque poussée, chaque remise et l'unique appel de l'étape B sont-ils précédés d'un contrôle à blanc ?
  Que se passe-t-il si l'outil rend la main au milieu du bloc C4 ?
- Q7. Le contrôle à blanc (script et essais) prouve-t-il ce qu'il dit ? Un cas sain ou un artefact manque-t-il (règle R5) ?
  Lis-t-il un contenu de résultat ?
- Q8. L'attestation « qui a lu quoi » (règle adaptée à la ligne 77 de la liste v1) est-elle juste et suffisante ?
- Q9. Le bloc C2 (recomposition des morceaux par programme, empreinte comparée à `SCORES-T07`) est-il correct ?
- Q10. Bash : erreurs de logique dans les blocs (variables, `arret` dans les fonctions, `&&`/`||`, relance d'un bloc) ?
- Q11. Le brief du compte 3 (lot NARCBench, bras descriptif de T0.7) devrait-il exclure ce compte comme hôte ? Lignes à l'appui.
- Q12. Toute autre faute : contradiction avec un texte scellé, identifiant de modèle écrit, heure écrite à la main, chiffre
  sans source.

**Ce que tu rends** : un fichier `docs/procedures/lecture-7b-etape-b-compte-3-v1/contre-lecture-commande-compte-3-v1.md`,
scellé (`PYTHONPATH=src .venv/bin/python -m controle_ia.scellement sceller <fichier>`), non commité : en tête, ton modèle
(« modèle C », sans identifiant), la déclaration que tu n'as écrit aucune pièce lue et n'as ouvert aucune sortie de 7a, 7b ou
T0.7, les heures de début et de fin (`date -u`) ; puis le **verdict** en une ligne parmi « remettable », « remettable après
corrections », « non remettable » (pour la phase A et pour la phase C séparément) ; puis les constats numérotés CL3-01, …,
chacun avec sa gravité (bloquant, majeur, mineur), le lieu (bloc, ligne), la preuve (fichier et ligne) et, si possible, le
couple « ancien » / « nouveau » exact à appliquer ; enfin les réponses Q1 à Q12. Ton rapport final à la mère : le chemin et
l'empreinte du fichier, le verdict, le nombre de constats par gravité.
