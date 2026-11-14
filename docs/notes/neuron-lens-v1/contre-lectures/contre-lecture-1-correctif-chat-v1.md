# Contre-lecture 1 du correctif (4) « provenance chat de Llama » et des contrôles de B0 — rapport recopié (résumé fidèle)

Contre-lecteur : sous-agent neuf, « modèle D », lancé après 11:09 UTC ; il n'a écrit aucune des pièces. Pièces relues : note
`correctif-provenance-chat-llama-v1.md` (`ce671ab1b8056d4884dbb79952f50f26f5bb5198a96c301f4ad7b536a2660145`), différence
`provenance-chat-llama-v1.diff` (`fec2c0a7f298ea8b786ccfe9e7b406c6406549caab740d8cfe18f54689b9b73f`), code `controles_b0_v1.py`
(`d06db4e095d3c9b47a02fdc402f9b514380de9d66477a3d41ce1906437e2e2e0`), essais `test_neuron_lens_controles_b0_v1.py`
(`41368ae7c191de094263fee0f35723a73317f4028fa30c12aa6cc9d6b294de8b`).

1) Empreintes conformes ; 4 essais passés ; `git apply --check` réussi ; 8 011 lignes ajoutées ; le corps déposé, clé `file` remise à
`act-chat.jsonl`, est identique octet pour octet à `act-chat-qwen3-8b.provenance.json` (`a76c6b02…`) ; fichier déposé `777aa068…`.

2) Verdicts : note **scellable après corrections mineures** (1 à 3) ; différence **scellable en l'état** ; code **scellable après corrections
mineures** (4) ; essais **scellables après corrections mineures** (5).

3) Remarques
- (1) Réponses : le nom `act-chat-llama-3.1-8b-instruct` est bien celui de `act_file("chat")` pour `NEURON_LENS_MODEL=meta-llama/Llama-3.1-8B-Instruct`
  (variable lue à l'import, à poser avant le lancement) ; le script n'en lit que `revision` ; contenu = provenance de Qwen3-8B à la clé `file`
  près (identifiants de Qwen3-8B et de Gemma identiques entre eux) ; `verifier_provenances` compare ce qu'il faut, contre la bonne référence ;
  égalité des identifiants raisonnable (premières lignes de `test_sft`, `skip` 0, seul `text.strip()` filtre, `prompt_id` uniques) ; rien de
  bloquant ailleurs (`strip_header`, « code » et le filtrage ne dépendent pas du modèle).
- (1 bis) Moyenne — le script réécrit sur place `act-dclm`, `act-zh`, `act-code` et la provenance « chat » de Llama : les références doivent
  être lues **avant** la passe, ou par `git show 849bfe16:<chemin>`, jamais dans l'arbre après la passe. À écrire dans la note et le code.
- (2) Mineure — pour dclm, zh et code des textes vides sont possibles et écartés, mais la référence a subi le même filtre à la même révision :
  le dire.
- (3) Moyenne — deux angles morts : le gabarit de Llama 3.1 peut insérer la date du jour dans l'en-tête système (texte « chat », donc son
  empreinte, non reproductible d'un jour à l'autre ; relever à B0 le texte rendu d'une ligne et la date) ; l'en-tête consomme une part du
  plafond de caractères des documents (corpus différent par construction de celui de Qwen ; à mentionner, pas un critère d'arrêt).
- (4) Mineure — `verifier_provenances` : une clé absente des deux côtés passe (`None == None`) ; traiter l'absence dans `produites` comme un
  problème ; essai.
- (5) Mineure — essais : `compter_debuts` (document vide, triple jeton, `bos_id` absent) ; `empreinte_liste_gardee` (doublon, jeton ajouté) ;
  le test du correctif ne compare pas aux identifiants de Qwen3-8B (référence absente du dépôt) : citer `a76c6b02…` et l'égalité établie par
  lecture.
