VERSION DE PYTHON : `python3 --version` ; AUCUN `-c`, AUCUN `-` APRÈS PYTHON3

AUCUNE COMMANDE DE LISTE : NI `ls`, NI `find`, NI `git ls-tree`, NI `git ls-files`, NI `git status`, NI `grep -r`, NI RECHERCHE SUR UN DOSSIER ENTIER, NI JOKER DANS UN CHEMIN. TOUT FICHIER S'OUVRE PAR SON CHEMIN COMPLET. UNE COMMANDE SIMPLE PAR APPEL : NI `&&`, NI `;`, NI BOUCLE. `git show` TOUJOURS REDIRIGÉ VERS UN FICHIER DE TON DOSSIER, JAMAIS À L'ÉCRAN. AUCUNE RECHERCHE DE MOTIF LARGE.

# Mandat du rédacteur — préenregistrement court de la course « nouvelles attaques », version 2 (corrections K1 à K24) — v1

Pièce de travail (classe C). Donné par la session du compte organisme le 2026-11-20. Dossier : `/home/user/controle-ia-travail/docs/notes/ideation-nouvelles-attaques-v1/preenregistrement-court-v1/` (noté P).

## Qui

Un rédacteur neuf, modèle F. Tu signes « rédacteur neuf, modèle F ».

## Ce qui fait foi (vérifie chaque empreinte contre son compagnon)

- La contre-lecture : `P/contre-lecture-preenregistrement-court-nouvelles-attaques-v1.md` (`a9886437aeac1c8aa38c132efcdbc34f8593588194e48e1d2c0d5b8c9a78999b`), **vingt-quatre corrections K1 à K24**, texte exact au § 8 ; son calcul `P/calcul_repartition_cles_v1.py` et sa sortie `P/calcul-repartition-cles-v1.json` (`bf423a5e…`), dont la table des répartitions par clé et le seuil X = 9,28 USD.
- Les pièces v1 : `P/preenregistrement-court-course-nouvelles-attaques-v1.md` (`0f0d8b9b…`), `P/rapport-redacteur-preenregistrement-court-nouvelles-attaques-v1.md` (`057b3a4c…`).
- Sur main (`git -C /home/user/controle-ia-travail fetch origin main`, puis `git show` redirigé) : GO-2026-11-20-14, -15, -16 ; R-4089 à R-4097. La mère a confirmé que séparer proposeur et juge d'une même espèce sur deux clés est permis (« une espèce ou un rôle fixe par clé ») et que le coût rendu à la composition se compte par rôle et par espèce, jamais par clé.
- Le besoin du bras A sur Rigaud, établi par la contre-lecture : au plus **8,35 USD** réservés à l'essai de mesure (devis `docs/notes/relance-organismes-discrets-v1/devis-essai-de-mesure-lecteurs-bras-a-v1-brouillon3.md`, `533ad5b1…`, § 5.1 et § 6.3, GO-2026-11-19-34, moins 0,904 déjà comptés) ; les lectures du bras A elles-mêmes : non trouvées par chemins nommés (ordre de grandeur écrit d'environ 580 USD, § 7.3). X ≤ 9,28 si seul l'essai compte.

## Ce que tu fais

1. K1 à K24 **à la lettre**, par l'outil contre-lu (`python3 -B /home/user/controle-ia-travail/scripts/remplacer_texte_exact_v1.py`, empreinte commençant par `391db990`), un JSON par pièce écrit avec l'outil d'écriture de fichiers, sous les noms neufs `preenregistrement-court-course-nouvelles-attaques-v2.md` et `rapport-redacteur-preenregistrement-court-nouvelles-attaques-v2.md`. Pour K1 à K4 et K9, relis main et recalcule les empreintes de registre comme la contre-lecture le demande.
2. K7 : la répartition par clé suit la table de la contre-lecture ; écris la répartition retenue selon X (au plus 8,35 USD si seul l'essai de mesure compte : la ligne « meilleure si X ≤ 9,28 ») et dis ce qui la ferait basculer (les lectures du bras A pendant la course). N2 récrit selon K22, posé à Lazar sans défaut.
3. K21 (règle de lecture d'une course arrêtée avant la fin) est une proposition de la contre-lecture : porte-la, marquée « à accepter ou refuser par la mère ».
4. Tenue : titres, lignes de version. Aucune autre modification de fond. **Aucune méthode d'attaque, aucun procédé, aucun détail opérant.**
5. Différentiels `diff -u` v1 → v2 et rapport court `rapport-redacteur-corrections-preenregistrement-court-v2-v1.md`.

Ton dossier : `/tmp/claude-0/-home-user-controle-ia-travail/227b647d-2ece-5654-bf04-8493b3ed2f19/scratchpad/redacteur-preenregistrement-court-v2/`. Chaque fichier rendu avec son compagnon (`env -C DOSSIER sha256sum F`, redirigé vers `DOSSIER/F.sha256`). Règle R-4067 pour l'outil ; vérifie chaque ancre par `grep -c -F -e` sur la cible avant l'appel.

## Interdits

Voir en tête. Jamais de heredoc ni de code en ligne passé à un interpréteur. Aucune écriture dans le dépôt, aucun commit. Rien sous `archives-reponses-modeles/`, rien du coffre hormis sa question, rien sous `/root/.claude/`. Jamais le nom d'une commande d'arrêt ou de recherche de processus par motif. Aucun appel à un fournisseur de modèles, aucune dépense, aucune valeur de clé. Aucun identifiant de modèle. Au premier refus de permission, de classifieur ou de garde : arrête-toi et dis-le.
