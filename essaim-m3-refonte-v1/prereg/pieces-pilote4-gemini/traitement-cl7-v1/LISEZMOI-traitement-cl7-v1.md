# Traitement des constats de la contre-lecture 7 du pilote 4 — pièces — v1 (26 octobre 2026, à partir de 02:57 UTC)

Écrit par l'instance nouvelle de la lignée conv-audit. Heures lues sur `date -u`.

- **Texte traité** : `prereg/pilote4-gemini-organisme-v4.md`, de la version relue par la contre-lecture 7
  (`4c20ca317b496feb2893cb4a6f7ff2403a394d945dd5295e6639c2c743a697d8`, 576 lignes ; copie dans `contre-lecture-7-v1/`) à la
  version donnée au script des graines (`8d0fa7237d6047e5445ccda770d7f22a0423be90f47c9e8706e2c839fd8ec428`, 643 lignes).
- **Rapport traité** : `prereg/contre-lectures/pilote4-gemini-organisme-v4-cl7.md`
  (`68daac567230edcdeded204e55243a92b3046f8fee2c135af7063ba36a461725`), « scellable après corrections mineures » ; deux
  mineurs (P4C7-01, P4C7-02), trois remarques (P4C7-03 à P4C7-05), une conformité.
- **Écart complet** : `diff-texte-4c20ca31-vers-8d0fa723-v1.txt` (`diff -u`).
- **Relevé v7 des mots de Lazar** : `objet-v6-2-1-v1/mots-de-lazar-2026-10-25-26-v7.md`
  (`a99eb30607fee9b13a7cd35e1bf5ce69d7f24352122ff72da39f2eb21f3f0234`), construit par `outils/faire_releve_v7_v1.py` à partir
  de la v6 (`2e6387b9…`, empreinte vérifiée par le script ; script exécuté depuis une copie hors du dossier des pièces) :
  titre, phrase d'en-tête et en-tête de la section session-depot changés ; six lignes ajoutées à la fin de la table
  (03:01 à 03:48, verbatim) ; R-479 à R-484 ajoutées à la fin (`main` `162418c` ; R-479 recopiée sans les mots de Lazar
  qui touchent une candidature, la question correspondante n'étant pas versée) ; `diff` : 3 lignes ôtées, les trois
  remplacées, 29 ajoutées.
- **Ce qui est fait de chaque constat** : § Contre-lecture du texte, paragraphe « Contre-lecture 7 ». Les deux mineurs
  sont corrigés dans les mots du rapport ; le choix (a) du point 4 bis est gardé, comme le rapport le recommande ; les
  chiffres de P4C7-01 ont été refaits à part (z = 2,2414 au niveau 97,5 % bilatéral ; 18 / 23,0239 = 0,7818 ;
  12 / 17,0239 = 0,7049 ; McNemar à huit paires discordantes de même sens : p = 0,0078, sous 0,0125).
- **Ajouts hors des constats, déclarés au texte** : les mots de Lazar de 03:01 à 03:48 (§ Décisions), dont la décision
  « graines » toujours pendante et la retenue de lecture qui la protège (conv-audit ne lit aucun score de ce pilote, et
  la sortie du script de lecture est poussée sans être affichée, jusqu'à la décision de Lazar), et « ni
  préenregistrement ni scellement au sens de R1 » (03:46 ; statut ; le paragraphe « Ce texte scellé » devient « Ce
  texte, à ses graines », même sens, aucun script ne lit ce titre) ; ce que l'instance nouvelle a lu depuis la
  contre-lecture 7 (« Ce qui a été lu »). Aucune de ces modifications ne touche une règle de lecture, une garde du
  lanceur, la ligne de GO, les lignes de dépense, les graines ou l'objet.
- **Répétition du script des graines**, à déclarer : à 02:50 UTC environ, pour essayer l'outil de vérification du départ
  (canal, `envois/verification-depart-pilote4-v1/`), `sceller_pilote4_v4.py` a tourné une fois sur une **copie de
  travail jetable** de la branche à `672d47b` (texte `4c20ca31…`) ; l'entropie et les graines tirées ont été masquées à
  l'affichage et détruites avec la copie ; elles ne servent à rien et n'ont été choisies ni comparées à rien. Le texte
  réel n'a reçu ses graines qu'une fois, après ce traitement.
- **Ce qui ne change pas** : noyau `8e5e2f7b`, lanceur v10, batterie v12 et série v13, objet v6.2.1 (`7ea3270`, arbre
  `4f13647a…`), ligne de GO et lignes de dépense (§ Plan, point 1), liste d'arrêt, marqueurs des graines, script des
  graines v4. Aucun score lu.
