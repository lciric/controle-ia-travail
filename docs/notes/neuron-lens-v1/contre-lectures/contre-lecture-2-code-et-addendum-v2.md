# Contre-lecture 2 du code de décision v2 (B-α, volet A) et de l'addendum v2 — rapport (résumé fidèle)

Contre-lecteur : sous-agent neuf (« modèle B »), lancé après 10:54:39 UTC, rapport lu avant 11:00 UTC (`date -u`) ; il n'a écrit aucune des
pièces. Pièces relues : `verdicts_b_alpha_v2.py` (`afc9c9d8475fee61506b4de07e33650990fa30fae30a43ddcf884f8210262f0f`), son essai
(`8e639896af6acd8014a4633a536e49bb128b36a75d5236d50f79c1441fb4db7b`), `decisions_volet_a_v2.py`
(`6ea51e462c75d9dd55322b9086fbebe274c90188e7c9a5036fc58c7984525805`), son essai (`7dfc6374f75a641848c88a6defaa2351698f09ef0a49513b2a21dd84d29ba0c3`),
`addendum-empreintes-v2.md` (`4ccf01e3a89b0113afc663f13a4d52dc2f0513ebf71142436562acc7a81f397d`). Résumé remarque par remarque.

## Empreintes et essais
Toutes concordantes ; `kept-qwen3-8b.txt` : 103 830 lignes triées, sans doublon, P et 1879 présents ; 41 essais passés. Non vérifiable
sans réseau : le recalcul de la liste gardée.

## Verdicts
Les cinq pièces : **scellables après corrections mineures**. Les trois lectures déclarées de `verdicts_b_alpha_v2.py` sont **compatibles**
avec le texte gelé ; réserve : l'extension de « en attente d'audit » à B-7 par le haut n'est pas déclarée.

## Remarques
1. **Moyenne** — `valider` ne valide pas `n` (non fini, 1000, −5 acceptés). Exiger des entiers finis dans [0, 64].
2. **Moyenne** — B-7 « par le haut » préfixe le verdict de reproduction, alors que B-7 est hors du verdict de reproduction et que l'audit
   n'est exigé qu'« avant toute lecture » de B-7. Garder le déclencheur sans préfixer, ou déclarer ; dire que « en attente » ne suspend pas B-β.
3. **Mineure** — `n_par_couche` conforme à `score` ; déclarer « motifs exclusifs, priorité à sans contexte ».
4. **Moyenne-mineure** — gardes manquantes de `n_par_couche` : aléatoires hors de `picks`, doublons, couche sans tirés, `nv` > V, couche
   négative ; affirmer `n + écartés == 64`.
5. **Mineure** — `n_depuis_causal` : formes justes (`steer` [P, 2, 2, V], `fired` [P, 2, K]) mais non affirmées ; dériver `aleatoires` comme
   `score` (`random_neurons`, `random.Random(0)`), ou prendre `picks` pour Llama (pas de pôle nommé).
6. **Mineure** — exiger des valeurs à 4 décimales dans `valider` ; `controle_lentille` : une matrice non finie doit être un arrêt.
7. **Mineure** — essais : doses distinguées dans `n_depuis_causal` ; clause B-2 « `r_med` < 0,30 » ; quart exact du témoin (7 sur 28) ;
   effet nul en ablation et cas double ; B-7 par le haut ; gardes des remarques 1 et 4.
8. **Moyenne-mineure** — replis silencieux restants dans le volet A (`verdict_a3` chutes non finies et longueurs ; `s_fait_mieux` à 3 couches ;
   rang non fini ; `qualificatif_texte` non fini et casse ; σ_v = 0 ; `verdict_i` valeurs non reconnues et longueur de `a3_par_contraste`).
9. **Mineure** — bords flottants du volet A (0,05 ; 0,02) : déclarer une lecture et l'essayer.
10. **Mineure** — `audit_volet_a` : « neurones égaux à la sonde partout » non défini ; déclencheur non relié au verdict.
11. **Mineure** — addendum : la révision à laquelle chaque arbre a été demandé n'est portée par aucune pièce ; écrire « selon les requêtes
   de l'autrice, non portées par les fichiers archivés » (sans conséquence pour trois arbres, dont les dates de dernière modification
   précèdent le relevé).
12. **Mineure** — addendum, mécanisme « chat » : `05_act_corpus.py` réécrit la provenance après la passe : l'égalité se fait contre la
   provenance de Qwen3-8B (`a76c6b02…`) ; écrire l'argument `--docs dclm=40000,zh=8000,code=8000,chat=8000` (le défaut est dix fois plus petit).

## Les 19 remarques de la contre-lecture 1
Traitées : 1, 3, 4, 5, 6, 7, 8, 10, 12, 13, 14, 16, 17, 18, 19 ; partiellement : 2 (n et matrices), 9 (dérivation de `rand`, gardes),
11 (restes : remarque 8), 15 (bords 0,05 et 0,02). Toutes les empreintes et révisions de l'addendum concordent.
