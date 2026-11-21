# Règle pour le lanceur du lot 8, « maison de l'agent dans le dossier de sortie » — extraction v1

- Source : `docs/notes/organisme-noeuds-2026-11-21-v1/reponses-fable-noeuds-organisme-v1.md` (sha256 `dd4e1ccc53dbe142a4a64ae054114dd17feec20f07eb9d050d9de714ac3ed587`), sur main.
- Section : § 4 (règle à écrire au mandat du lot 8).
- Retenu par la mère, décision de routine, R-4573.
- Extrait à l'octet par programme le 2026-11-21T14:48:35Z (`date -u`), sans aucun changement ; conçu par Claude Fable 5.2.

<!-- lignes 286 à 293 de la source : règle, points 1 à 8, à l'octet -->

1. **Deux dossiers neufs par appel.** Pour tout rôle dont l'adaptateur lance l'outil, le lanceur crée avant l'appel, sous `<dossier de sortie>/maisons/<identifiant neutre de l'appel>/`, un dossier `maison/` et un dossier `travail/`, neufs et vides.
2. **Environnement réduit à une liste de noms**, sans héritage : la variable de la maison (`HOME`), la variable du dossier de configuration de l'outil si l'outil en a une (son nom se relève, il ne se suppose pas), les quatre variables de dossiers d'utilisateur (`XDG_CONFIG_HOME`, `XDG_CACHE_HOME`, `XDG_DATA_HOME`, `XDG_STATE_HOME`) et celle du dossier temporaire (`TMPDIR`) pointent toutes sous `maison/` ; le dossier courant est `travail/`.
3. **Bac à sable** : la maison réelle et le dossier de configuration réel de l'outil ne sont pas montés. Sans bac à sable : départ refusé.
4. **Garde au départ, arrêt nommé « maison de l'agent hors du dossier de sortie »** : le chemin réel de chacune de ces variables est sous le chemin réel du dossier de sortie ; aucun lien symbolique ; `maison/` et `travail/` sont vides (un fichier de consignes ou de mémoire y serait ajouté à la requête par l'outil : voir le § 5).
5. **Nom neutre** : l'identifiant de l'appel est le rang du journal réencodé ; le chemin ne porte ni génération, ni case, ni rôle, ni espèce, ni nom de la course, parce que l'outil peut servir ce chemin au modèle.
6. **Après l'appel** : inventaire (noms, tailles, empreintes) de `maison/` et de `travail/` dans un fichier à part du dossier de sortie ; **rien n'est supprimé**. La transcription est classée « réponse brute, copie de l'outil » : elle suit le dossier de sortie en quarantaine ; la mère ne la lit jamais ; aucune mesure ne la lit, la source des mesures restant la conservation à l'empreinte faite par l'adaptateur.
7. **Épreuves (règle R5)** : cas sain, un appel au faux fournisseur laisse une transcription sous `maison/` et une fausse maison témoin reste intacte ; artefacts, chacun refusé au départ : maison hors du dossier de sortie, variable de configuration hors du dossier de sortie, `maison/` non vide, lien symbolique.
8. Une option de l'outil qui couperait la transcription peut s'ajouter ; elle ne remplace pas la règle, qui porte sur le lieu.
