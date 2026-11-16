# Préenregistrement — crible (iii) de l'organisme d'idéation : deux passes, traits choisis par un proposeur bon marché, loi écrite par un proposeur cher — brouillon 1

- Auteur : sous-agent neuf de la session mère, rédacteur de cette pièce (« modèle A » de cette pièce au sens de R-2598 ;
  identité dite en conversation seulement) ; auteur aussi du brouillon 1 du crible (v), même dossier. Je n'ai écrit ni la note
  des idées originales, ni le relevé, ni les fiches, ni le pilote MR-2, ni son code, ni sa procédure, ni aucune contre-lecture
  citée.
- Date (UTC) : 2026-11-16, rédaction de 11:47 à 12:27 (`date -u`), après celle du crible (v) ; dépôt lu sur `main` (tête
  `91f9ddd9`, puis `377a2a0c`) ; branches lues par `git show`, sans clone ; aucun commit, aucune poussée.
- Commit du code d'analyse : **aucun à ce jour**. Le code s'écrit après la contre-lecture de ce texte et son scellement ; ses
  empreintes entrent dans un addendum d'empreintes scellé avant tout jeu, qui ne change rien d'autre.
- Documents qui font foi (chemin, empreinte entière) :
  - note des idées originales, § 0 à 7 et annexe A : `docs/notes/organisme-idees-juge-v1/conception-idees-originales-v1.md`
    (`2f6a69dd480a079fa385846c8aca06ff53c8d40b0cf36be1fd61cf8e1e0537a3`) — ci-dessous **[NOTE]** ;
  - relevé des idées, § 3.1, § 4.2, § 5 et § 6 : `docs/notes/organisme-conception-propre-v1/relecture-exploratoire-v2/releve-idees-reutilisables-v1.md`
    (`bd253b6c68f6baada0e61b5381f029b52838ca34aa092502e55253c662451c6c`) — **[RELEVÉ]** ; fiches argon-p1-04 (n° 3, empreinte
    de fiche `428ae07c…`) et argon-p2-04 (n° 17, `aef7787e…`) du fichier `runs/course-ideation-conception-propre-v1/20261113-235541-course-ideation-conception-propre-v1-g1/copies/sortie--fiches-validees.json`
    (`a9f9594e2dc3a7a553c54577202817758e3f7ef231445f1a48d500fc647389d5`) : **non relues par moi** (pièce sous `runs/`), citées à
    travers [RELEVÉ] et [NOTE] ;
  - recoupement des méthodes, V3 (plan combinatoire de focalisations) et C2 (arbres de continuation) :
    `docs/notes/organisme-bassins-etroits-v1/recoupement-methodes-v1.md`
    (`eecd98fab0beff8c99414380a5d12b18feafd1581d38c7fe54b94491327ab172`) — **[REC]** ;
  - registre des GO, ligne GO-2026-11-15-06 (l. 339) : `registres/go.md` au commit `377a2a0c`
    (`4bcec4a0408499477babb133f7184a159928ca2f35c5bc3188666e5a81264568`) ; registre des décisions : R-2851, R-2873, R-2875,
    R-2883, R-2968 à R-2970 (registre vivant) ;
  - texte scellé du pilote MR-2, candidat 6 (branche `prep/pilote-mr2-compte-organisme-v1`) :
    `docs/notes/organisme-multi-generations-v1/pilote-v1/preenregistrement-pilote-conditionnelles-v1-candidat6-compte-organisme.md`
    (`8aa33014667da569ec934459d7bc1b1f6b54efa5c2145a6e5bdce5f7fa74603e`) — **[PILOTE]** ;
  - procédure v14 du pilote (branche `lot/compte-organisme-v1`) :
    `docs/notes/organisme-multi-generations-v1/pilote-v1/procedure-pilote-v74-compte-organisme/procedure-pilote-mr2-v74-machine-v14.md`
    (`2035562740efe1e87db9ffa2f0494705bb5117c56069309ece2279d351bde18a`) — **[PROC-14]** ;
  - devis du pilote : `docs/notes/organisme-multi-generations-v1/pilote-v1/sorties/devis-pilote-v2.json`
    (`dba76367488ca0b7c66fbf66f03e44357cf5ad02d99b267d522ab2489542c350`) ; lecture des prix publics v2 (branche
    `lot/compte-organisme-v1`) `…/pilote-v1/prix-publics-sonde-v74-compte-organisme/lecture-prix-publics-sonde-v74-v2.md`
    (`b88253b841d5f41ec83d7be86c9f62402b429a13b6ed2a63a6984641f735643d`), citée à travers [PILOTE], préalable 3 ;
  - famille MR-2 : conception v4 `docs/notes/organisme-multi-generations-v1/conception-monde-riche-doublons-v4.md`
    (`47e38ec0663320e8c68011130c3f1b8e1017969cbb740d30c83a78eb5db0a6dc`) — **[MR2]** ; conception v3, § 4.1 (couverture)
    `…/conception-monde-riche-doublons-v3.md` (`386d48bacd6c487d88846d0991d83bd4ad95122f70500d6fbeb7859cde56659c`) — **[V3]** ;
    sorties des 12 mondes de développement `…/sorties-v4/partie-v4-monde-{0…11}.json` (résumé `…/sorties-v4/resume-v4.json`,
    `c4c55f010bed7e28d0e87c72a8702cabd4f0807a7023309f4c62c238829dfbd5`) ;
  - outils : `…/outils-v4/monde_riche_v4.py` (`4b1658477811fb87360dda44a65b0af96e87ae1d2ca4a32bdabbd3ce6cc19eb8`) ;
    `…/outils-v1/complements_synthese_v1.py` (`89eb7ba8c8cf8633541a6de8090767f74619e3f3968ebed8f894b1f8d593e9ba`) ;
    `…/outils-v1/monde_riche_outils_v1.py` (`1825b956eed638fe4daf3d7395a169fdbdf7c9679076d9ba3fb4a15cfd7ec85e`) ;
    `…/pilote-v1/outils/mesure_pilote_v4.py` (`676d5f37f21cf5d512f92d2029991fa8795a77076c285ea9bd83c43841748365`) ;
  - décisions : `docs/decisions/decision-N-058-v1.md` (`854f2724864f1e45394e001f4aca7b0248753e5d2b0a66991e2ee8a7be87de9d`),
    `docs/decisions/decision-N-045-v2.md` (`c7b05e39de381cee1d5ec2276745a0310bd3cc0857a6be0e0fb14eeb5042261d`),
    `docs/decisions/decision-N-044-v1.md` (`2b70bdac014d366d058a530680d016663b35ed73b8ca0cae9f2369206f5004bf`),
    `docs/decisions/decision-N-067-v1.md` (`966dd9dc3fae61cbe1f10ee2a54f401ddf7af5041eeaacd81ad9f8b264661589`) ; question de la
    course « conception propre » (QO1, QO4) : `docs/notes/organisme-conception-propre-v1/question-organisme-conception-propre-v1.md`
    (`77c524f3c591e43ec1b14e261bd4667cf0e085b6c94afe7e7b37f72816c6feb4`) ;
  - catalogue des conceptions publiées : `docs/notes/organisme-conception-propre-v1/catalogue-conceptions-publiees-v1.md`
    (`ddfb2522be0fe5095926405b8761d0e4be0065a29679585051a287349114fe9d`) — **[CAT]** ;
  - brouillon 1 du crible (v), même dossier, `crible-v-brouillon1.md` (son empreinte est dans son compagnon) — **[CRIBLE-V]** ;
  - modèles de forme : `prereg/organisme-idee-1-2-tirages-repartis-arret-anticipe-v4.md`
    (`bdabf2bc9b2c9b78939660f7f7053576a145e165927cafd23e14a798d07d790e`), `prereg/organisme-idee-1-1-poids-du-nul-v2.md`
    (`3ffe1739aa83ea8de613d07855db52d16c82ad6247fca22e833ee7f6ff8305ff`) ; gabarit `prereg/gabarit-preregistrement-v1.md`
    (`8cad43714b562e28238a92200d6315b1769d8bdf7e9f0a8d72dfe2bc9b37700e`) ; validateur `src/controle_ia/prereg.py`
    (`3b2e3ee56463f30ffd3c549e7fe480fea574c707581bcf30098bf38f4980c306`).

**Statut.** Brouillon 1, **non scellé, non contre-lu** (R1, R2). Aucune dépense, aucun appel de modèle, aucun monde tiré.
L'accord GO-2026-11-15-06 (enveloppe des cinq cribles, crédits de Claude employés au maximum) **n'autorise encore aucun
appel** : la ligne « calcul » propre à ce crible s'inscrit par la mère sur un devis refait d'après le coût mesuré du pilote MR-2
et contre-lu (lecture de la mère, l. 339). Prédictions et devis sont écrits **avant** toute lecture du pilote (qui génère ses
mondes ce jour, machine 60918148) ; la version qui fera foi les refera sur ses coûts et taux mesurés, en déclarant ce qui en a
été lu. **Les gabarits des deux passes sont neufs** : le pilote ne les éprouve pas (section « Devis », sonde des gabarits).
Validateur `controle_ia.prereg.problemes` : un seul défaut attendu à ce stade, la section « Contre-lecture » sans les deux
empreintes (aucune contre-lecture n'existe) ; rien d'autre.

## 0. En dix lignes

1. **Question** ([NOTE] § 3 (iii) ; [RELEVÉ] § 3.1) : une passe bon marché qui propose vingt ensembles de 1 à 3 traits, un
   filtre déterministe sans juge qui en garde six, puis une passe chère qui écrit une carte par ensemble, couvrent-ils plus de
   composantes **par dollar** qu'un appel cher seul ? La passe chère est-elle nécessaire (QO1) ?
2. **Quatre bras** sur les mêmes 20 mondes MR-2, archive {K1}, une génération : S standard (Pr-2) ; D deux passes (Pr-1 choisit,
   Pr-2 écrit) ; H ensembles au hasard (programme, puis Pr-2) ; B tout bon marché (Pr-2 remplacé par Pr-1 **sur les ensembles
   mêmes de D**). 100 appels ; aucun juge, aucun test de mort (N-058).
3. **Filtre** : ensembles valides, doublons et ensembles de l'archive retirés, puis six choisis par une règle gloutonne de
   distance de Jaccard (le plus éloigné des déjà choisis, égalités par l'ordre des noms) ; aucun modèle, aucun juge, aucune issue.
4. **Mesure** : composantes certifiées couvertes par les cartes brutes (oracle du pilote), hors l'effet de K1 ; dollars par appel
   au prix public ; exécution (la carte k emploie-t-elle les traits de l'ensemble k ?) ; traits de pur bruit.
5. **Deux principales** (Bonferroni, intervalles à 97,5 %) : P1 efficacité Δ_R = R_D − R_S (composantes par dollar de D moins
   celles de S ; le rapport ρ_DS est rapporté) ;
   P2 nécessité de la frontière δ_DB = couverture de D moins celle de B, mêmes ensembles.
6. **Secondaires** : choix bon marché contre hasard (D − H), effet du format (H − S), conditionnelles, bruit, coûts.
7. **Prédiction de l'auteur** : P1 « non tranché », Δ_R ≤ 0 en estimation et ρ_DS ≤ 1,1 (confiance 0,5) ; P2 : la passe chère couvre au moins une
   demi-composante de plus par monde (0,45) ; D ≈ H (0,5).
8. **Devis (brouillon, estimé)** : 58,30 USD attendus aux prix de [NOTE] (48 sur crédits de Claude, 10,30 hors crédits ; mes
   fourchettes : 48 à 62) ; **216,60 au pire**
   (120 sur crédits, 96,60 hors crédits), sous les 243 de [NOTE] : B réemploie la passe 1 de D (− 40), les plafonds de Pr-1 sont
   2,34 et non 2,00 (+ 13,60) ; variante « crédits de
   Claude au maximum » (Pr-2 choisit, Pr-4 écrit) : ≈ 128,30 attendus, 263 au pire, dont 3 hors crédits.
9. **Durée** : passe 1 puis passe 2 dans chaque monde : ≈ 12 à 15 h de machine si les mondes passent l'un après l'autre, trop près
   de la minuterie de 17 h : mondes en parallèle à prévoir.
10. **Préalable conseillé** : une sonde des deux gabarits neufs (trois appels sur un monde de développement, ≈ 1,05 à 1,40 USD
    au prix public, 6,68 au pire), avant les 100 appels.

## Hypothèse

**Contexte.** Les fiches argon-p1-04 et argon-p2-04 (un seul proposeur ; [RELEVÉ] § 3.1) proposent de séparer le **choix des
traits**, confié à une passe légère, de **l'écriture de la loi**, confiée à la frontière ; la partie propre, selon [RELEVÉ], est
le **filtre déterministe sans juge** entre les deux passes ; le piège nommé par la fiche : forcer des traits de pur bruit. C'est
une forme de « le bon marché d'abord » (convergence de trois proposeurs, [RELEVÉ] § 4.2 et § 6) et une mesure de la nécessité de
la frontière pour le rôle d'écriture (N-045 points 1, 3 et 7 ; QO1, QO4).

**H-iii** (énoncé de [NOTE] § 3 (iii)). Dans une génération partie de {K1}, sur la famille MR-2, les deux passes (Pr-1 propose
vingt ensembles de 1 à 3 traits ; filtre ; Pr-2 écrit une carte par ensemble retenu) couvrent **davantage de composantes
certifiées par dollar** qu'un appel standard de Pr-2.

**H-iii-a** (mesure, sans sens attendu par le programme ; QO1, N-045 point 3) : sur les mêmes ensembles, ce que perd l'écriture
quand Pr-1 remplace Pr-2 (B contre D).

**H-iii-b** (contrôle, N-045 point 7, « espaces de conception égaux ») : ce que le choix de Pr-1 apporte au-delà du seul
format « une carte par ensemble » (D contre H) ; et ce que le format seul fait (H contre S).

**Hypothèses de travail.** (i) Sessions neuves et indépendantes, sans historique ; la passe 2 ne reçoit de la passe 1 que les
ensembles retenus, jamais sa réponse brute. (ii) **Génération 1 seulement**, archive {K1}. (iii) Le filtre ne lit ni issue, ni
oracle, ni monde : la réponse brute de la passe 1 et les traits des lois de l'archive. (iv) La couverture d'une carte libre peut
porter plusieurs composantes à la fois (un arbre jusqu'à 48 feuilles, [MR2] § 2.2) : la forme « une carte par ensemble » peut
donc couvrir **moins** que six cartes libres, même avec de bons ensembles.

## Prédiction chiffrée et signe attendu

Écrites avant le pilote, sans donnée de proposeur sur MR-2 ; confiance faible. Notations : section « Métrique ».

| # | prédiction | signe | chiffre | ce qui la réfute | confiance |
|---|---|---|---|---|---|
| III-1 | **principale P1** : efficacité Δ_R = R_D − R_S | ≤ 0 | estimation ≤ 0 (ρ_DS entre 0,8 et 1,1) ; issue « non tranché » | borne basse à 97,5 % de Δ_R > 0 | 0,5 |
| III-2 | **principale P2** : δ_DB (mêmes ensembles, écrivain cher contre bon marché) | + | ≥ + 0,5 composante par monde ; « perte établie sans la frontière » | borne haute à 97,5 % < 0 | 0,45 |
| III-3 | choix bon marché contre hasard : δ_DH | ≈ 0 | entre − 0,5 et + 0,5 | borne basse à 95 % > 0 | 0,5 |
| III-4 | exécution E_D | — | ≥ 0,8 | < 0,5 | 0,6 |
| III-5 | piège du bruit : part des ensembles retenus qui contiennent un trait distracteur | D < H | N_D ≤ 0,25 ; N_H ≈ 0,45 à 0,61 | N_D ≥ N_H | 0,55 |
| III-6 | première conditionnelle couverte (mondes) | D, H ≥ S | D − S ≥ 2 mondes | S − D ≥ 2 mondes | 0,3 |
| III-7 | coût relatif $_D / $_S (prix publics) | > 1 | 1,05 à 1,6 | < 1 | 0,6 |

**Raisons.** Dans les 12 mondes de développement de [MR2], 4 à 6 composantes sont certifiées par monde (2 fortes, 1 à 3 moyennes,
1 ou 2 conditionnelles, une faible certifiée en tout ; annexe A, point 10) : hors l'effet de K1, **3 à 5 composantes à couvrir**
par monde ; les nombres sont petits, les écarts entre bras aussi. III-1 : six cartes libres d'un proposeur cher peuvent chacune
porter toutes les composantes visibles à la marge (l'autre forte, les moyennes) ; la forme par ensemble disperse les cartes,
ce qui aide seulement si les ensembles tombent sur les bons traits ; D paie en plus l'appel de Pr-1 (III-7). III-2 : rien ne
mesure encore Pr-1 comme écrivain sur MR-2 ; je parie sur l'écart de prix. III-3 : vingt ensembles proposés au vu de 400
épisodes devraient éviter des distracteurs (III-5) mais la règle de Jaccard pousse vers la dispersion, que le hasard donne aussi.
III-5 : au hasard (tailles 1, 2 ou 3), un ensemble contient un distracteur avec la probabilité 0,45 si le monde en a 2, 0,61 s'il
en a 3 (annexe A, point 7 ; au moins 2 distracteurs par monde, [MR2] § 2.2). III-6 : six ensembles au hasard contiennent la paire
(trait de condition, trait de la conditionnelle) avec une probabilité d'environ 0,25 (annexe A, point 8, filtre ignoré) ; un
écrivain qui reçoit cette paire peut essayer une condition ; une carte libre, presque jamais (hypothèse de masquage de [MR2] :
0,02 par carte, estimée, que le pilote mesure).

**Ce que serait chaque issue (R3).** P1 « plus efficaces » : H-iii non réfutée au crible ; lue avec Q : si D ≈ H, le gain vient du
**format** (cartes dispersées par ensemble), non du choix bon marché ; si D > H, du choix. P1 « moins efficaces » : H-iii réfutée
au crible. P1 « non tranché » : rien sur l'efficacité à 20 mondes. P2 « perte établie » : la frontière sert à l'écriture (pour
ce rôle, ce moment, cette famille) ; P2 « sans perte notable » : Pr-1 écrit presque aussi bien sur les mêmes ensembles, et B est
alors le bras le moins cher (efficacité ρ_BD rapportée). III-4 fausse (E_D < 0,5) : la consigne n'est pas suivie ; le format
n'a pas été joué ; P1 et P2 sont lus sous réserve. III-6 vraie : la forme par ensemble trouve des conditionnelles qu'une carte
libre ne trouve pas, information pour le pilote et la course (aucune adoption).

## Métrique

Programme de mesure neuf, `mesure_crible_iii_v1.py` (nom réservé ; dérivé de `mesure_pilote_v4.py`, `676d5f37…`), lancé une seule
fois sur la machine du crible.

- **Appels et cartes** : définitions de [PILOTE] et de [CRIBLE-V] (« Métrique ») : appel complet, tronqué, en échec ; carte
  valide = admise au gardien, évaluable, emplacement ≤ 6, d'un appel complet ; appel répondu = complet avec au moins une carte
  valide. Les cartes refusées, au-delà de six, non évaluables ou d'appels tronqués comptent dans les dollars, jamais dans une
  couverture.
- **Passe 1** (gabarit G1, neuf) : la réponse brute est scellée, puis lue par un analyseur gelé : un **ensemble valide** est une
  liste de 1 à 3 entiers distincts de 0 à 7 (dimension 8) ; forme canonique : tuple trié ; les 20 premiers ensembles valides sont
  gardés, les suivants ignorés et comptés ; ensembles invalides comptés.
- **Filtre** (programme gelé, sans modèle, sans juge, sans issue) : (1) doublons retirés (première occurrence gardée) ; (2) retrait
  des ensembles **inclus dans les traits d'une loi de l'archive** (avec {K1} : l'ensemble réduit au trait de K1) ; (3) ordre des
  noms = ordre lexicographique des tuples triés ; premier choisi = le premier dans cet ordre ; puis, tant que moins de six sont
  choisis, l'ensemble restant qui **maximise sa plus petite distance de Jaccard** (1 − |A ∩ B| / |A ∪ B|) aux ensembles déjà
  choisis, égalités par l'ordre des noms ; (4) s'il en reste moins de six, la passe 2 reçoit tous ceux qui restent (k < 6 cartes
  demandées), compté.
- **Bras** (même monde, même archive, mêmes épisodes servis) : **S** : un appel de Pr-2, gabarit du pilote (`e77d3041…`),
  inchangé. **D** : passe 1 de Pr-1, filtre, puis passe 2 de Pr-2 (gabarit G2, neuf, portant les k ensembles). **H** : vingt
  ensembles tirés par le programme (taille uniforme sur {1, 2, 3}, traits uniformes sans remise parmi 8), même filtre, puis passe 2
  de Pr-2. **B** : passe 2 de **Pr-1**, sur **les ensembles mêmes de D** (texte servi égal à l'octet à celui de D).
- **Monde complet** : S, D (passe 1 avec au moins un ensemble après filtre, et passe 2), H et B répondus. **Format tenu** dans un
  monde : D a six ensembles.
- **Composantes comptées et couverture** : comme [CRIBLE-V] : composantes **certifiées** (étiquette C8 de `verifier_v4`, latente
  exclue), moins l'effet de K1 et ce que K1 servie porte à elle seule ; porte si Δ_i ≥ max(0,005 ; 0,75·I_i) (oracle de
  12 000 instances). C_X(w) = composantes comptées portées par au moins une carte valide du bras X dans le monde w.
- **Dollars** (prix publics de la note des prix v2 en principal ; prix de la configuration v12 en sensibilité, voir [CRIBLE-V]) :
  $_S = appel S ; **$_D = passe 1 + passe 2 de D** ; $_H = passe 2 de H (les ensembles du programme ne coûtent rien) ;
  **$_B = passe 1 + passe 2 de B** (la passe 1 commune compte dans chacun des deux bras qui l'emploient). Machine à part.
- **Efficacité** R_X = Σ_w C_X(w) / Σ_w $_X(w) (composantes par dollar, mondes complets) ; **Δ_R = R_D − R_S** (statistique
  de P1) ; **ρ_XY = R_X / R_Y** (rapporté, défini si Σ C_Y > 0).
  **Écart de couverture** δ_XY = moyenne sur les mondes complets de C_X(w) − C_Y(w).
- **Intervalles** : rééchantillonnage apparié des mondes complets, 10 000 rééchantillons, percentile ; **97,5 % pour P1 et P2**
  (Bonferroni sur deux principales), 95 % ailleurs ; test exact des signes rapporté pour δ (accords non nuls ; seuils de
  l'annexe A, point 2).
- **Exécution** (bras D, H, B) : la carte d'emplacement k répond à l'ensemble k. **Traits employés** par une loi : le trait j est
  employé si un nœud `softmax` a des poids de colonne j non tous égaux entre issues (écart > 10⁻⁶), ou si un nœud `si_sinon`
  conditionne sur z_j, ou si une `transformee` oscille sur z_j. **E_X** = part des cartes valides k qui emploient tous les traits
  de l'ensemble k ; **E′_X** = part qui n'emploient que des traits de l'ensemble k et le trait de K1.
- **Bruit** : N_X = part des ensembles retenus (D, H) qui contiennent au moins un trait distracteur (`distracteurs` du devis du
  monde) ; part des cartes de chaque bras qui emploient un distracteur ; couverture des cartes dont l'ensemble n'a que des
  distracteurs.
- **Qualité du choix de la passe 1** (sans écriture) : part des ensembles valides de Pr-1 et des ensembles retenus de D, H qui
  contiennent au moins un trait d'une composante comptée (traits de `traits_v4`, trait de condition compris pour une
  conditionnelle).
- **Conditionnelle** : nombre de mondes complets où la première conditionnelle comptée est couverte, par bras.
- **Sensibilités, rapportées sans verdict** : τ' = 0,25·I ; toutes les composantes ; prix de la configuration ; mondes non
  complets réintégrés bras par bras. **Rapportés aussi** : appels répondus, tronqués, en échec, par proposeur et par passe ;
  ensembles invalides et ignorés ; jetons et dollars par passe. Pertes et couvertures **par classe sommées sur les mondes**,
  jamais monde par monde. Information sur la composition, jamais un classement de proposeurs (N-058). Aucune moyenne ni médiane
  sur des jetons dans une sonde (il n'y en a pas).

## Seuil

- **Minimum** : n_c ≥ 16 mondes complets sur 20, aucun fournisseur perdu en entier ; sinon « non concluant ».
- **Format** : format tenu dans au moins 14 mondes complets ; sinon réserve « format non tenu ». **Consigne** : E_D ≥ 0,5 ; sinon
  réserve « consigne non suivie ».
- **Zone utile** : au moins 10 mondes complets où l'un des bras couvre au moins une composante comptée ; sinon « hors de la zone
  utile ».
- **P1** : « **deux passes plus efficaces par dollar** » si la borne basse à 97,5 % de Δ_R = R_D − R_S dépasse 0 ; « **moins
  efficaces** » si la borne haute est sous 0 ; sinon « non tranché ». La décision porte sur la différence, toujours définie (les
  dollars ne sont jamais nuls) ; le rapport ρ_DS, indéfini si Σ C_S = 0, est rapporté avec son intervalle quand il est défini.
- **P2** : « **perte établie sans la frontière** » si la borne basse à 97,5 % de δ_DB dépasse 0 (qualifiée « petite » si la borne
  haute est sous 0,5) ; sinon « **sans perte notable** » si la borne haute est sous + 0,5 composante par monde ; sinon « non
  tranché ». Marge de 0,5 : choix de ce texte (une demi-composante par monde, soit 10 à 17 % des 3 à 5 composantes comptées),
  à contre-lire.
- **Q** (secondaire, 95 %) : « le choix bon marché aide » si la borne basse de δ_DH dépasse 0 ; « pas mieux que le hasard au
  crible » si la borne haute est sous + 0,5 ; sinon « non tranché ». **F** (format, δ_HS) : rapporté avec son intervalle.

## Plan d'analyse

### Proposeurs (configuration v12 du pilote, inchangée)

| poste | clé de configuration | crédits | rôle ici | attendu par appel ([NOTE] § 1) | plafond de session (bloc gelé de [PILOTE]) | borne de sortie | prix de la configuration (entrée / sortie) |
|---|---|---|---|---|---|---|---|
| Pr-1 | `argon` | hors crédits | passe 1 (D, B) ; écrivain de B | 0,25 | 2,34 | 36 000 | 10 / 50 (public : 2 / 10 jusqu'au 30 novembre) |
| Pr-2 | `opus55` | crédits de Claude | S ; écrivain de D et H | 0,80 | 2,00 | 89 000 | 4 / 20 |

Identités : celles de la configuration v12 (`f69503dd…`, bloc gelé de [PILOTE]) ; aucun identifiant de modèle ici (R-2598).
Pr-3 et Pr-4 ne servent pas dans la forme fidèle à [NOTE] (voir la variante « crédits de Claude au maximum », « Devis »).

### Gabarits

- **G0** (S) : celui du pilote, inchangé (`e77d3041…`) : 400 épisodes de développement, archive {K1}, grammaire servie, « au
  plus 3 conditions emboîtées », rien sur les conditions ni sur les sortes d'effets (R-2504).
- **G1** (passe 1) : les mêmes pièces servies, puis la consigne de rendre **vingt ensembles distincts de 1 à 3 traits** (indices
  0 à 7) qui « semblent porter de l'information au-delà de l'archive », sous une forme fixe (liste JSON de listes d'entiers), **sans
  loi** ; rien sur les conditions, les interactions ou les sortes d'effets ; empreinte gelée au code.
- **G2** (passe 2) : G0, puis le bloc des k ensembles numérotés (entiers seuls, reconstruits depuis les formes canoniques : aucun
  texte de la passe 1) et la consigne : « écris exactement une carte par ensemble, dans l'ordre ; la carte k emploie les traits de
  l'ensemble k ; elle peut employer aussi le trait de la loi de l'archive ; aucun autre trait » ; **consigne, non garde** : le
  gardien est celui du pilote, inchangé ; l'exécution est mesurée (E, E′). Même G2 pour D, H et B.
- Rédaction exacte de G1 et G2 à figer au code et à contre-lire (aucun mot qui annonce une condition, R-2504).

### Partie A — plafond du format (processeur seul, avant tout appel ; descriptive)

Sur les 12 mondes de développement de [MR2] (régénérés par `generer_v4` à leurs graines publiques ; étiquettes C8 reprises de
leurs sorties scellées, contrôlées par empreinte), **écrivain parfait** : la carte de l'ensemble k est le monde restreint
(`monde_restreint`) aux composantes dont tous les traits sont dans l'ensemble k ou sont le trait de K1. Pour 1 000 tirages
d'ensembles au hasard par monde (loi de H, filtre compris ; graines `(12, r, t)`), couverture des six cartes parfaites : sa
distribution est le **plafond du format** pour H ; le plafond de S est le nombre de composantes comptées (une carte libre peut
être le monde entier). Rapporté sans critère ; ne change rien à la partie B. Coût : ≈ 1 à 1,5 h d'un cœur, **quand la machine
n'est plus chargée** (jamais pendant un chronométrage d'une autre session).

### Partie B — le crible

- **Mondes** : 20 mondes MR-2 du **secret du crible**, procédure de la machine comme [PROC-14] (secret engagé et poussé, phrase de
  Lazar, mondes et empreintes inscrits avant tout appel) ; jamais publiés, jamais réutilisés, jamais hors de la machine.
  (Variante « témoin commun » avec (v) : mêmes mondes et appels S pris à (v) ; section « Choix et doutes », point 7.)
- **Ordre dans un monde** : S, passe 1 et H partent ensemble ; à la réponse de la passe 1 : analyse, filtre, puis D et B partent
  ensemble ; une passe 1 en échec, tronquée ou sans ensemble valide : **ni D ni B** dans ce monde (aucune dépense de plus), monde
  non complet.
- **Appels** : 5 par monde, 100 en tout (Pr-2 : 60 ; Pr-1 : 40) ; aucune reprise, aucune bascule ; réponses brutes et témoins
  d'isolement scellés avant extraction ; empreinte de chaque texte servi au journal ; `CARTES.json` et `ENSEMBLES.json` scellés.
- **Mesure** : `mesure_crible_iii_v1.py`, une seule fois, sur la machine ; sortie scellée avant toute lecture, sans devis de monde ;
  rapatriement comme [PROC-14] § 9 (jamais les mondes) ; réponses brutes sur une branche de travail, jamais sur `main` (R-2731).

### Graines (R9)

Racine : l'entier de l'empreinte sha256 du texte qui fera foi. `numpy.random.SeedSequence(entropy=racine, spawn_key=…)`, numpy
≥ 1.25 (2.5.3 sur la machine) : ensembles au hasard de H dans le monde r `(r, 40)` ; partie A `(12, r, t)` ; rééchantillonnage
`(99, b)` ; essais et mutations `(97, k)`, liste à l'addendum. **Graine du monde r** : fonction `graine_monde_pilote` de [PILOTE]
avec l'étiquette neuve « crible-iii-v1 » (secret du crible, phrase de Lazar, empreinte du texte scellé, r) ; tirages de
`generer_v4` ; épisodes de développement : règle du bloc gelé, étiquette « crible-iii-v1 » ; oracle `cle("oracle-crible-iii",
empreinte du devis du monde)`. Manifeste du run : `src/controle_ia/manifeste.py`.

### Étapes

0. **Code** sous des noms neufs : lanceur du crible (dérivé du lanceur v74 du pilote ; deux passes, ordre par monde, filtre,
   tirage de H), gabarits G1 et G2, analyseur de la passe 1, `mesure_crible_iii_v1.py`, `lire_crible_iii_v1.py` (lecture gelée),
   programme de la partie A. **Essais** : cas sain et artefact pour chaque ligne de la liste d'arrêt (R5) ; filtre éprouvé sur des
   cas écrits à la main (égalités, moins de six, doublons, ensemble de l'archive, ensembles invalides). **Banc de mutations**, au
   moins : le filtre lit le monde ou l'oracle ; égalités rompues par le proposeur ou au hasard ; ensemble de l'archive gardé ; H
   tiré des ensembles de D ou du secret ; B servi d'autres ensembles que D ; réponse brute de la passe 1 servie à la passe 2 ; passe
   1 comptée hors de $_D ou de $_B ; carte refusée ou au-delà de six comptée ; effet de K1 compté ; intervalles à 95 % au lieu de
   97,5 % pour les principales. Toutes tuées pour la raison attendue. Contre-lecture du code par un sous-agent neuf d'un autre
   modèle ; addendum d'empreintes scellé.
1. **Partie A** sur processeur (quand la charge le permet), sortie scellée, lue sans critère.
2. **Sonde des gabarits neufs** (conseillée, sur devis et ligne propre) : sur un monde de développement à graine publique, un
   appel de Pr-1 sous G1, un de Pr-2 et un de Pr-1 sous G2 ; vérifie l'analyse des ensembles, la forme des cartes, les jetons ; ne
   lit aucune couverture.
3. **Avant toute dépense du crible** : pilote MR-2 joué, coûts et durées mesurés ; version qui fera foi (devis, prédictions,
   puissance), contre-lue, scellée par `sceller_prereg`, recopiée sous `prereg/` ; lignes « calcul » inscrites par la mère.
4. **Machine** (procédure dérivée de [PROC-14], noms neufs, trois barrières), essai à blanc avec proposeurs scriptés et vraies
   pièces servies (les deux passes comprises), puis les 100 appels.
5. **Mesure** une seule fois, sortie scellée, rapatriement, destruction par identifiant (R10), preuve d'absence.
6. **Lecture** gelée, puis sous-agent neuf (R13) ; audit de symétrie (R4) écrit avant le prononcé ; rapport ; **aucune adoption**.

### Comparaisons et corrections

Deux principales, P1 (Δ_R = R_D − R_S) et P2 (δ_DB), à 97,5 % chacune (Bonferroni). Secondaires à 95 %, sans correction : Q (δ_DH), F (δ_HS),
ρ_BD, ρ_BS, ρ_HS, conditionnelles. Tout est apparié par monde.

### Taille

20 mondes, comme [NOTE] (annexe A de [NOTE] : 0,80 de puissance pour une part passant de 0,05 à 0,40 à 20 mondes). Pour δ, le test
exact des signes au niveau unilatéral 0,0125 demande au moins 16 accords sur 20 ; sa puissance est 0,05 si un bras gagne dans 60 %
des mondes non égaux, 0,24 à 70 %, 0,63 à 80 %, 0,96 à 90 % (annexe A, points 2 et 3). **Crible d'un grand effet** : P1 et P2
ne voient qu'un écart net dans une large majorité de mondes ; un « non tranché » ne dit rien d'un petit effet. Le pilote ne mesure
pas la couverture par appel (sa sortie ne rend que la conditionnelle, le témoin et la condition, [PILOTE] « Métrique ») : la
puissance de P1 se recalculera, avant le scellement, par simulation sur processeur sous le modèle de proposeurs synthétiques de
[MR2] et la partie A, quand la machine n'est plus chargée ; 24 ou 30 mondes si la mère le décide (devis + 20 % à + 50 %).

## Critères de lecture gelés

Lecture dans cet ordre ; un étage 0, 1 ou 3 arrête la lecture.

| étage | observé | verdict |
|---|---|---|
| 0 | une ligne d'arrêt déclenchée ; la mesure en erreur | « **non jugeable (arrêt)** » : aucune issue lue |
| 1 | n_c < 16 ; un fournisseur perdu en entier | « **non concluant** » ; causes rapportées |
| 2 | format non tenu ; E_D < 0,5 | réserve « **format non tenu** » ou « **consigne non suivie** » : P1 et P2 lus et rapportés sous cette réserve ; aucune conclusion sur l'idée |
| 3 | zone utile manquée | « **hors de la zone utile** » |
| 4 | P1 | « deux passes plus efficaces par dollar » / « moins efficaces » / « non tranché » |
| 5 | P2 (QO1, rôle d'écriture) | « perte établie sans la frontière » (« petite » si borne haute < 0,5) / « sans perte notable » / « non tranché » |
| 6 | Q et F | « le choix bon marché aide » / « pas mieux que le hasard au crible » / « non tranché » ; F avec son intervalle |
| 7 | exécution, bruit, choix de la passe 1, conditionnelles, sensibilités, coûts | rapportés, sans verdict |

**Lecture de H-iii.** Étage 4 « plus efficaces » : « H-iii non réfutée au crible », **qualifiée par l'étage 6** (gain du choix si
Q « aide », du format si Q « pas mieux que le hasard ») ; « moins efficaces » : « H-iii réfutée au crible » ; « non tranché » :
« non tranchée ». **Rien n'est adopté** : changer la composition de l'organisme (un rôle au bon marché) est un nœud de Lazar
(N-045 point 1 : la composition est apprise, non fixée par un crible ; N-058).

**Audit de symétrie (R4)**, écrit avant le prononcé pour toute issue : textes servis de D et de B égaux à l'octet, monde par
monde ; ensembles reconstruits depuis les réponses brutes scellées de la passe 1 (contrôle indépendant de l'analyseur) ; filtre
rejoué à la main sur trois mondes (graine dérivée de l'empreinte de `ENSEMBLES.json`) ; attribution relue sur trois cartes par
bras et par monde ; dollars rapprochés des journaux des relais. **« Trop propre »** : ρ_DS ≥ 2 (quand il est défini) ; δ_DB ≥ 2 ; E_D = 1 avec toutes
les prédictions vraies. **« Tout négatif »** : un bras à couverture nulle partout ; E_D < 0,2 ; cartes de passe 2 identiques d'un
ensemble à l'autre ; couvertures égales dans les quatre bras partout. Même relecture écrite, par un sous-agent neuf.

## Liste d'arrêt

Chaque ligne a son essai sain et son artefact, écrits et passés avant l'addendum d'empreintes (R5) ; aucun repli silencieux.

| condition | action | essai sain | artefact |
|---|---|---|---|
| empreinte différente : texte, monde, gabarit G0, G1 ou G2, configuration, programme, module importé | arrêt avant tout appel | pièces conformes | un octet changé dans G2 : refus nommé |
| configuration autre que v12 | arrêt avant tout appel | v12 acceptée | borne de Pr-1 changée : refus |
| relevé de sonde absent ou invalide (si le lanceur l'exige) | refus avant tout dossier | relevé conforme | relevé d'une autre configuration : refus |
| monde sans tirage conforme en 8 ; C-16 ou C-17 en défaut | arrêt avant tout appel | mondes conformes | monde forcé non conforme : arrêt |
| texte servi d'une passe 2 différent de G2 et du bloc d'ensembles reconstruit | arrêt avant cet appel | texte égal | un mot de la réponse de passe 1 dans le bloc : arrêt |
| texte servi de B différent de celui de D (mêmes ensembles) | arrêt avant l'appel de B | égalité à l'octet | un ensemble permuté pour B : arrêt |
| le filtre reçoit autre chose que la réponse brute de la passe 1 et les traits des lois de l'archive | arrêt ; défaut | signature conforme | objet oracle ou devis du monde passé : refus nommé |
| ensembles de H tirés d'une graine qui dépend du monde, du secret ou de la passe 1 | arrêt ; défaut | graine `(r, 40)` | graine du secret : refus |
| passe 1 sans ensemble valide, tronquée ou en échec | pas de passe 2 pour D et B dans ce monde ; monde non complet ; compté | passe 1 conforme : D et B partent | réponse sans liste : aucune passe 2, compte juste |
| réponse brute ou témoin d'isolement absent | arrêt (code 3), pièces versées | pièces présentes | témoin supprimé : arrêt |
| coût d'un appel au-dessus de son pire cas | arrêt (code 3), dépense comptée | coût sous le pire | relevé gonflé : arrêt |
| dépense d'un fournisseur atteignant sa part | arrêt ; jamais de ligne d'extension | part non atteinte | part atteinte en essai : arrêt |
| fournisseur abandonné alors que 16 mondes complets ne sont plus possibles | arrêt du crible ; « non concluant » | panne d'un appel : continue | panne de Pr-1 à tous les appels dès le monde 3 : arrêt |
| couverture comptant une carte refusée, tronquée, au-delà de six, non évaluable, ou l'effet de K1 | arrêt ; défaut | cartes valides seules | carte au-delà de six injectée : refus |
| exception de la mesure (pas un refus nommé) | rien n'est lu ; correction sous un nom neuf, contre-lue, scellée ; mêmes entrées | mesure conforme | division par zéro forcée : arrêt sans sortie |
| lecture avant le scellement de la sortie ; mesure lancée deux fois | run invalide | une sortie scellée | seconde mesure : refus |
| toute dépense sans ligne « calcul » inscrite citant GO-2026-11-15-06 | interdit | ligne présente | ligne absente : la commande refuse |
| minuterie : moins de la durée bornée des appels restante avant l'échéance | arrêt (A) sans appel | marge suffisante | échéance proche simulée : arrêt |

## Devis (brouillon ; tout est estimé sauf les plafonds ; à refaire sur le coût mesuré du pilote)

**Hypothèses de coût** (comme [CRIBLE-V], « Devis ») : attendus de [NOTE] § 1 (devis du pilote, `dba76367…`, estimés) ; mes
fourchettes au prix public : entrée ≈ 15 000 à 18 000 jetons par appel (≤ 52 000 octets servis, ≈ 3 octets par jeton supposés ;
G2 ajoute moins de 1 000 octets), sortie ≈ 30 000 jetons pour six cartes ([PILOTE]), **passe 1 : ≈ 2 000 à 10 000 jetons** (vingt
ensembles et la réflexion, supposé) ; pires cas : plafonds de session du bloc gelé ; Pr-1 compté par le code à 10 / 50 (cinq fois
son prix public).

**Forme fidèle à [NOTE]** (Pr-1 choisit, Pr-2 écrit), 20 mondes, 100 appels :

| ligne | appels | jetons d'entrée (attendu ; compté au pire) | jetons de sortie (attendu ; borne) | crédits | attendu [NOTE] | fourchette (prix public) | pire (plafonds) |
|---|---|---|---|---|---|---|---|
| Pr-2, S standard | 20 | 0,30 à 0,36 M ; 1,06 M | 0,60 M ; 1,78 M | Claude | 16,00 | 13,20 à 16,40 | 40,00 |
| Pr-2, D passe 2 | 20 | 0,30 à 0,37 M ; 1,08 M | 0,60 M ; 1,78 M | Claude | 16,00 | 13,20 à 16,40 | 40,00 |
| Pr-2, H passe 2 | 20 | 0,30 à 0,37 M ; 1,08 M | 0,60 M ; 1,78 M | Claude | 16,00 | 13,20 à 16,40 | 40,00 |
| Pr-1, passe 1 (commune à D et B) | 20 | 0,30 à 0,36 M ; 1,06 M | 0,04 à 0,20 M ; 0,72 M (+ réflexion ajoutée) | hors | 5,00 | 1,00 à 2,80 (code : 5 à 14) | 46,80 |
| Pr-1, B passe 2 | 20 | 0,30 à 0,37 M ; 1,08 M | 0,60 M ; 0,72 M (+ réflexion ajoutée) | hors | 5,00 | 7,00 à 9,00 (code : 34 à 42) | 46,80 |
| machine (≤ 0,15 USD/h ; 0,0522 relue le 16 novembre) | — | — | — | hors | 0,30 | 0,50 à 0,80 | 3,00 |
| **crédits de Claude** (Pr-2) | 60 | | | | **48,00** | 39,60 à 49,20 | **120,00** |
| **hors crédits** (Pr-1, machine) | 40 | | | | **10,30** | 8,50 à 12,60 | **96,60** |
| **total** | 100 | ≈ 1,5 à 1,85 M ; 5,36 M | ≈ 2,45 à 2,6 M ; 6,78 M | | **58,30** | 48,10 à 61,80 | **216,60** |
| conditionnel : sonde des gabarits neufs (G1 par Pr-1, G2 par Pr-2 et par Pr-1, un monde de développement) | 3 | — | — | Claude 1, hors 2 | — | 1,05 à 1,40 | 6,68 (2,00 sur crédits ; 4,68 hors crédits) |
| conditionnel : sonde neuve des relais (si le lanceur l'exige ; lignes de la sonde v74) | 8 | — | — | les deux | 0,10 | — | 8,07 |
| partie A | 0 | — | — | — | 0 | 0 | 0 |

- **Écart à [NOTE]** : 100 appels au lieu de 120 (B réemploie la passe 1 de D : section « Choix et doutes », point 1) ; plafonds de
  Pr-1 à 2,34 (bloc gelé, R-2542) au lieu de 2,00 ; pire 216,60 au lieu de 243,00.
- **Témoin commun avec (v)** ([NOTE] § 4) : S pris aux appels de Pr-2 de (v) : − 20 appels, attendu ≈ 42,30 (32 sur crédits),
  pire 176,60 (80 sur crédits ; 173,60 si la machine est celle de (v)) ; mêmes mondes, donc une seule machine pour les deux cribles.
- **Variante « crédits de Claude au maximum »** (Pr-2 choisit, Pr-4 `fable52` écrit ; S = un appel de Pr-4) : Pr-4, 60 appels :
  96,00 attendus (79,20 à 98,40), 180,00 au pire ; Pr-2, 40 appels (passe 1 et écriture de B) : 32,00 attendus (passe 1 comptée
  comme un appel entier ; 15,20 à 21,80 au prix public), 80,00 au pire ; machine 0,30 / 3,00 : **≈ 128,30 attendus, 263,00 au
  pire, dont 3,00 hors crédits**. Elle change la question (écart de prix 2 au lieu de 3,2 ; deux modèles d'une même maison) : section
  « Choix et doutes », point 4.
- **Plafond de 0,75 pour Pr-1** ([NOTE] § 4) : impossible sous la configuration v12 ([CRIBLE-V], « Devis »).
- **Durée** (estimée) : mondes ≈ 1 h ; dans un monde, la passe 1 (≈ 5 à 15 min) puis la passe 2 (≈ 15 à 20 min), S et H en
  parallèle de la passe 1 : ≈ 30 à 40 min par monde, **≈ 10 à 13 h pour 20 mondes l'un après l'autre**, plus mesure et barrières :
  ≈ 12 à 15 h de machine, trop près de la minuterie de 17 h (et de la règle de [PROC-14] : 12 h 30 au moins avant l'échéance au
  départ du réel) : **deux mondes au moins en parallèle**, ou une minuterie plus longue (procédure neuve) ; concurrence des relais
  (plusieurs sessions de Pr-2 à la fois) non éprouvée. Temps d'agents : code, gabarits, essais, contre-lectures (deux jours).

**Points à remesurer d'après le coût réel du pilote MR-2** : ceux de [CRIBLE-V] (jetons, dollars aux deux prix, durées, taux de
réponse par fournisseur, réflexion de Pr-1, cartes admises, taille du texte servi, durée des mondes) ; et, **non mesurés par le
pilote**, à prendre à la sonde des gabarits : sortie et réflexion de la passe 1, analyse des ensembles, longueur et forme des cartes
sous G2.

## Lignes de GO proposées, non inscrites (inscription par la mère, dans l'enveloppe de GO-2026-11-15-06)

```
| GO-AAAA-MM-JJ-NN (κiii1) | AAAA-MM-JJ | calcul | Organisme d'idéation, crible (iii) « deux passes » (traits choisis par un proposeur bon marché, loi écrite par un proposeur cher), part sur crédits de Claude : proposeur `opus55` (Pr-2, plafond de session 2 USD, part 120), 60 appels (bras standard, passe 2 des bras « deux passes » et « ensembles au hasard ») ; 20 mondes MR-2 du secret du crible, jamais publiés ni réutilisés ; archive {K1}, une génération ; gardien mécanique seul, aucun juge, aucun test de mort ; filtre déterministe sans modèle ni juge ; mesure gelée une seule fois ; conditions toutes exigées : coûts du pilote MR-2 mesurés et devis refait, préenregistrement du crible contre-lu et scellé, code et gabarits contre-lus et gelés, essai à blanc réussi, mondes vérifiés et leurs empreintes inscrites ; coût au-dessus du pire cas = arrêt ; essayé, non adopté ; jamais de ligne d'extension ; arrêt par identifiant (R10) | 120 USD (sur crédits) | 2026-11-30 | Lazar | GO-2026-11-15-06 ; R-2851 ; R-2875 ; ce texte |
| GO-AAAA-MM-JJ-NN (κiii2) | AAAA-MM-JJ | calcul | Même crible, part hors crédits : `argon` (Pr-1, 2,34 USD par session, part 93,60), 40 appels (passe 1 commune, écriture du bras « tout bon marché »), aucun réglage envoyé, machine jetable 3 USD ; plafond de chaque relais égal à sa part ; mêmes conditions que la ligne κiii1 | 96.60 USD | 2026-11-30 | Lazar | GO-2026-11-15-06 ; R-2851 ; R-2875 ; ce texte |
| GO-AAAA-MM-JJ-NN (κiii0, conditionnelle) | AAAA-MM-JJ | calcul | Sonde des gabarits neufs du crible (iii) : un appel de `argon` sous le gabarit de passe 1, un de `opus55` et un de `argon` sous le gabarit de passe 2, sur un monde de développement à graine publique ; aucune couverture lue ; relevé versé ; une seule exécution | 6.68 USD (2 sur crédits, 4,68 hors crédits) | 2026-11-30 | Lazar | GO-2026-11-15-06 ; ce texte |
```

Mots exigés par le lecteur gelé des lignes : à fixer avec le code ; montants à refaire sur le devis mesuré.

## Écarts, nœuds et ce que le crible ne décide pas

- **B réemploie la passe 1 de D** (écart à [NOTE], qui prévoyait 40 appels de Pr-1 pour le bras 4) : la comparaison des écrivains se
  fait sur les **mêmes** ensembles (appariement plus net), 20 appels de moins ; prix : B et D ne sont plus indépendants (dit).
- **Gabarits neufs** G1 et G2 : la « vue » des proposeurs change pour D, H et B ; [NOTE] ne le compte pas comme dessin neuf (« nœud :
  la dépense seulement ») ; je le signale : la consigne « une carte par ensemble » est une vue neuve, **essayée, non adoptée**.
- **Égalités du filtre** rompues par l'ordre des noms ([NOTE] § 3 (iii)) plutôt que par l'ordre de proposition de Pr-1 : le choix de
  Pr-1 n'entre que par l'ensemble des vingt ; choix à contre-lire (point 2).
- **Consigne, non garde** : une carte qui emploie d'autres traits reste valide ; l'exécution est mesurée, non imposée.
- **N-045 point 3** : l'ablation (B) est ici aux critères gelés (étage 5), non « rapportée hors des critères » comme dans une course ;
  à confirmer par la mère. **N-045 point 7** : H sépare l'effet du format de celui du choix.
- **N-044** : famille de conception MR-2 ; aucune conclusion hors de MR-2. **N-058** : aucun proposeur n'est choisi ni classé sur ce
  crible ; la composition reste un nœud.
- **Variante d'instrument local** pour la passe 1 ([NOTE] : carte graphique louée 1 à 2 heures) : **non jouée** ici (aucun modèle
  local désigné) ; à proposer à part.
- **Ne décide pas** : la qualité des idées ; les générations suivantes ; les autres rôles ; la profondeur en chaîne ; l'effet sur le
  juge ; toute revendication publique (N-067).

## Antériorités à chercher (R8 : zone vierge = question)

[RELEVÉ] § 3.1 dit la partie propre : le **filtre déterministe sans juge** entre une passe bon marché et une passe chère ; zone
séduisante, à vérifier plus durement. À lire sur PDF empreinté avant toute phrase de nouveauté ; **aucun chiffre** n'en est tiré
ici (R7) :
- voisins dans le dépôt : [REC] V3 (« plan combinatoire qui répartit des focalisations entre les appels ou entre les cartes d'un
  appel », « une paire de traits à examiner par emplacement de carte » : survivante) et [REC] C2 (préfixes puis continuations ; « un
  préfixe partagé peut ancrer toutes les branches dans la même erreur ») — H est proche d'un plan de focalisations tiré au hasard ;
- génération en deux temps (esquisse ou plan, puis rédaction) par des modèles de langue, et cascades « petit modèle pour planifier,
  grand pour exécuter » — **à chercher** (références non relevées par moi) ;
- sélection de variables par un modèle de langue avant l'ajustement d'un modèle (par exemple « LLM-Select », 2024) et régression
  symbolique guidée par un modèle de langue (par exemple « LLM-SR », 2024) — **à vérifier** ;
- sélection gloutonne « le plus éloigné d'abord » et pertinence marginale maximale (classiques de la dispersion et de la recherche
  d'information) — **à vérifier** pour la citation exacte ;
- boucles évolutives à proposeurs de coûts différents (FunSearch, Nature, 2024 ; AlphaEvolve, 2025) — **à vérifier** ;
- Co-Scientist ([CAT] C1, agents de génération) et The AI Scientist ([CAT] C3) ; CADS (arXiv 2610.24597 ; N-067, § 6 ; PDF sur une
  autre branche, non lu par moi) pour la contribution d'un proposeur à un rôle.

## Choix et doutes soumis à la mère

1. **B sur les ensembles de D** (écart à [NOTE]) : recommandation : oui (appariement, − 20 appels) ; confiance 0,7.
2. **Égalités du filtre** : ordre des noms ([NOTE]) ou ordre de proposition de Pr-1 (plus de « choix bon marché » dans D) ?
   Recommandation : ordre des noms, fidèle et indépendant du proposeur ; confiance 0,55.
3. **Consigne de G2** : « les traits de l'ensemble k, et le trait de l'archive, aucun autre » ; consigne, non garde. À contre-lire.
4. **Crédits de Claude au maximum** : forme fidèle (Pr-1, hors crédits, 10,30 attendus hors crédits) ou variante Pr-2 / Pr-4
   (tout sur crédits sauf la machine ; ≈ 128,30 attendus). Recommandation : forme fidèle, parce que la question est celle du proposeur
   **le moins cher** (QO1, QO4) et que l'écart de prix 3,2 est le contraste visé ; confiance 0,55 ; la variante est préférable si la
   part hors crédits doit être nulle.
5. **Marge de 0,5 composante par monde** pour P2 et Q.
6. **Dollars au prix public** en principal (Pr-1 cinq fois moins cher qu'au prix de la configuration).
7. **Témoin commun avec (v)** : recommandation : non (indépendance ; une seule machine porterait 160 appels, au-delà de la minuterie
   sans parallélisme) ; confiance 0,6.
8. **Sonde des gabarits neufs** avant le crible (≈ 1,05 à 1,40 USD au prix public, 6,68 au pire) : recommandation : oui ;
   confiance 0,7.
9. **Durée** : mondes en parallèle (changement du lanceur) ou minuterie plus longue (procédure neuve).
10. **Loi des ensembles de H** (taille uniforme sur 1 à 3, traits uniformes) : à contre-lire.
11. **Partie A** (plafond du format) : utile pour lire F et Q ; à jouer seulement quand la machine n'est plus chargée.

## Contre-lecture

Aucune à ce jour : ce texte est le brouillon 1, soumis à la contre-lecture (R2) d'un sous-agent neuf d'un **autre modèle** que le
rédacteur (modèle B ≠ A), qui n'a écrit ni ce texte, ni [CRIBLE-V], ni [NOTE], ni [PILOTE]. **Fichiers à lui donner
explicitement** : ce texte ; [CRIBLE-V] (« Métrique », « Devis ») ; [NOTE] (`2f6a69dd…`), § 1, § 2, § 3 (iii), § 4, § 6 et
annexe A ; [RELEVÉ] (`bd253b6c…`), § 3.1, § 4.2, § 5, § 6 ; [REC] (`eecd98fa…`), V3 et C2 ; [PILOTE] (`8aa33014…`), « Dessin »,
« Métrique », « Devis », bloc gelé ; [PROC-14] (`20355627…`), § 0, § 6, § 7 ; [MR2] (`47e38ec0…`), § 2 et § 3 ; [V3]
(`386d48ba…`), § 4.1 ; `mesure_pilote_v4.py` (`676d5f37…`) ; `monde_riche_outils_v1.py` (`1825b956…`) ; N-045 v2 (`c7b05e39…`) ;
N-058 (`854f2724…`) ; la ligne GO-2026-11-15-06 ; l'annexe A et ses deux programmes. **À trancher en priorité** : le filtre (ordre,
égalités, archive) ; le partage de la passe 1 ; la définition des traits employés ; la rédaction de G1 et G2 (rien sur les
conditions) ; les marges et les deux principales ; la comptabilité des dollars de D et B ; la faisabilité de la durée ; les onze
choix ci-dessus.

## Annexe A — comptes exacts (sans donnée de crible, sans tirage, sans appel)

**Programme 1** : `comptes_cribles_v2.py` (`f06bcfe7219a22d9b2c117be141739fe21c878d99b8f233725523072088e0f59`), dossier de travail de la
session, lancé le 16 novembre à 12:10:52 UTC (heure du fichier de sortie) par `nice -n 19 python3 -I` (Python 3.13.18,
bibliothèque standard seule) ; recopié en entier :

```python
"""Comptes exacts pour les brouillons 1 des cribles (v) et (iii) — v2 (la v1 reste en place, R12 ; la v2 la contient et ajoute
les points 5 à 9). Aucune donnée, aucun appel, aucun tirage ; bibliothèque standard seule ; quelques millisecondes.
1. Intervalles de Clopper-Pearson à 95 % bilatéraux pour x mondes sur 20.
2. Test des signes, n accords non nuls de 10 à 20 : plus petit c tel que P(X >= c | 1/2) <= niveau, niveaux 0,0125 et 0,025.
3. Puissance exacte du test des signes à n = 20 (niveau unilatéral 0,0125) pour p = 0,6 ; 0,7 ; 0,8 ; 0,9.
4. Part épargnée attendue par la règle de (v) selon le nombre k de mondes où elle appelle les chers, aux prix centraux.
5. Pour n mondes complets de 16 à 20 : plus petit W dont la borne basse de Clopper-Pearson (95 % bilatéral) dépasse 0,05.
6. Probabilité d'une « perte établie » (W >= seuil du point 5, n = 20) si chaque monde perd avec la probabilité p.
7. Part attendue d'ensembles tirés au hasard (taille uniforme sur 1, 2, 3 ; traits uniformes sans remise parmi 8) qui
   contiennent au moins un trait distracteur, pour d = 2, 3, 4 distracteurs.
8. Probabilité qu'au moins un de six ensembles tirés au hasard (indépendants, filtre ignoré) contienne une paire donnée.
9. Modèle de proposeurs synthétiques de la conception v4 (probabilité par carte de proposer une composante inconnue :
   forte 0,5 ; moyenne 0,25 ; faible 0,1 ; conditionnelle sans sa condition 0,02 ; cartes indépendantes) : probabilité que
   douze cartes de la moitié chère couvrent une composante que les douze de la moitié bon marché ont manquée."""
from math import comb


def queue_haute(n, c, p):
    return sum(comb(n, k) * p ** k * (1 - p) ** (n - k) for k in range(c, n + 1))


def cdf(n, x, p):
    return sum(comb(n, k) * p ** k * (1 - p) ** (n - k) for k in range(0, x + 1))


def bissection(f, lo=0.0, hi=1.0, tours=200):
    for _ in range(tours):
        mi = 0.5 * (lo + hi)
        if f(mi):
            hi = mi
        else:
            lo = mi
    return 0.5 * (lo + hi)


def clopper_pearson(x, n, a=0.05):
    bas = 0.0 if x == 0 else bissection(lambda p: queue_haute(n, x, p) >= a / 2)
    haut = 1.0 if x == n else bissection(lambda p: cdf(n, x, p) <= a / 2)
    return bas, haut


print("1. Clopper-Pearson 95 % bilatéral, x sur 20")
for x in range(0, 11):
    b, h = clopper_pearson(x, 20)
    print(f"  x = {x:2d} : [{b:.4f} ; {h:.4f}]")

print("2. Test des signes : plus petit c avec P(X >= c | n, 1/2) <= niveau")
for n in range(10, 21):
    out = []
    for niv in (0.0125, 0.025):
        c = min(c for c in range(n + 2) if queue_haute(n, c, 0.5) <= niv) if queue_haute(n, n, 0.5) <= niv else None
        out.append(f"niveau {niv} : c = {c}" + (f" (P = {queue_haute(n, c, 0.5):.4f})" if c is not None else " (impossible)"))
    print(f"  n = {n:2d} : " + " ; ".join(out))

print("3. Puissance du test des signes, n = 20, niveau unilatéral 0,0125 (c = 16)")
for p in (0.6, 0.7, 0.8, 0.9):
    print(f"  p = {p} : puissance {queue_haute(20, 16, p):.4f}")

print("4. Part épargnée attendue par la règle de (v), prix centraux (0,25 ; 0,80 ; 1,00 ; 1,60 USD par appel)")
bm, ch = 0.25 + 0.80, 1.00 + 1.60
for k in (0, 1, 2, 3, 4, 5, 10, 15, 20):
    tout = 20 * (bm + ch)
    regle = 20 * bm + k * ch
    print(f"  k = {k:2d} mondes appelés : épargne {1 - regle / tout:.4f} du coût des proposeurs")

print("5. Plus petit W dont la borne basse de Clopper-Pearson dépasse 0,05")
seuils = {}
for n in range(16, 21):
    w = min(x for x in range(n + 1) if clopper_pearson(x, n)[0] > 0.05)
    seuils[n] = w
    print(f"  n = {n} : W >= {w} (borne basse {clopper_pearson(w, n)[0]:.4f} ; à W - 1 : {clopper_pearson(w - 1, n)[0]:.4f})")

print("6. Probabilité d'une perte établie à n = 20 (W >= %d) si chaque monde perd avec la probabilité p" % seuils[20])
for p in (0.05, 0.10, 0.15, 0.20, 0.26, 0.35, 0.47):
    print(f"  p = {p:.2f} : {queue_haute(20, seuils[20], p):.4f}")

print("7. Part attendue d'ensembles au hasard (taille 1, 2 ou 3, uniforme) contenant au moins un distracteur, 8 traits")
for d in (2, 3, 4):
    parts = [1 - comb(8 - d, s) / comb(8, s) for s in (1, 2, 3)]
    print(f"  d = {d} : tailles 1, 2, 3 : " + ", ".join(f"{v:.4f}" for v in parts) + f" ; moyenne {sum(parts) / 3:.4f}")

print("8. Six ensembles au hasard, indépendants : probabilité qu'au moins un contienne une paire donnée de traits")
p_paire = (0 + 1 / comb(8, 2) + comb(6, 1) / comb(8, 3)) / 3
print(f"  par ensemble : {p_paire:.4f} ; sur six : {1 - (1 - p_paire) ** 6:.4f}")

print("9. Modèle synthétique : probabilité que la moitié chère (12 cartes) couvre ce que la moitié bon marché (12) a manqué")
for nom, p in (("forte", 0.5), ("moyenne", 0.25), ("faible", 0.1), ("conditionnelle sans condition", 0.02)):
    q12 = (1 - p) ** 12
    print(f"  {nom} (p = {p}) : manquée par les 12 premières {q12:.4f} ; ajoutée par les 12 autres {q12 * (1 - q12):.4f}")
for nom, compte in (("1 conditionnelle et 2 moyennes", {0.02: 1, 0.25: 2}),
                    ("1 conditionnelle et 3 moyennes", {0.02: 1, 0.25: 3}),
                    ("2 conditionnelles et 2 moyennes", {0.02: 2, 0.25: 2}),
                    ("1 conditionnelle, 2 moyennes et 2 faibles certifiées", {0.02: 1, 0.25: 2, 0.1: 2})):
    survie = 1.0
    for p, k in compte.items():
        q12 = (1 - p) ** 12
        survie *= (1 - q12 * (1 - q12)) ** k
    print(f"  monde à {nom} : probabilité d'au moins une composante ajoutée {1 - survie:.4f}")
```

Sortie (`5d53092e5fc4a6ef087a894035db490536cb9312936cc72dfacf5b6e0eab0cf8`), recopiée en entier :

```
1. Clopper-Pearson 95 % bilatéral, x sur 20
  x =  0 : [0.0000 ; 0.1684]
  x =  1 : [0.0013 ; 0.2487]
  x =  2 : [0.0123 ; 0.3170]
  x =  3 : [0.0321 ; 0.3789]
  x =  4 : [0.0573 ; 0.4366]
  x =  5 : [0.0866 ; 0.4910]
  x =  6 : [0.1189 ; 0.5428]
  x =  7 : [0.1539 ; 0.5922]
  x =  8 : [0.1912 ; 0.6395]
  x =  9 : [0.2306 ; 0.6847]
  x = 10 : [0.2720 ; 0.7280]
2. Test des signes : plus petit c avec P(X >= c | n, 1/2) <= niveau
  n = 10 : niveau 0.0125 : c = 9 (P = 0.0107) ; niveau 0.025 : c = 9 (P = 0.0107)
  n = 11 : niveau 0.0125 : c = 10 (P = 0.0059) ; niveau 0.025 : c = 10 (P = 0.0059)
  n = 12 : niveau 0.0125 : c = 11 (P = 0.0032) ; niveau 0.025 : c = 10 (P = 0.0193)
  n = 13 : niveau 0.0125 : c = 11 (P = 0.0112) ; niveau 0.025 : c = 11 (P = 0.0112)
  n = 14 : niveau 0.0125 : c = 12 (P = 0.0065) ; niveau 0.025 : c = 12 (P = 0.0065)
  n = 15 : niveau 0.0125 : c = 13 (P = 0.0037) ; niveau 0.025 : c = 12 (P = 0.0176)
  n = 16 : niveau 0.0125 : c = 13 (P = 0.0106) ; niveau 0.025 : c = 13 (P = 0.0106)
  n = 17 : niveau 0.0125 : c = 14 (P = 0.0064) ; niveau 0.025 : c = 13 (P = 0.0245)
  n = 18 : niveau 0.0125 : c = 15 (P = 0.0038) ; niveau 0.025 : c = 14 (P = 0.0154)
  n = 19 : niveau 0.0125 : c = 15 (P = 0.0096) ; niveau 0.025 : c = 15 (P = 0.0096)
  n = 20 : niveau 0.0125 : c = 16 (P = 0.0059) ; niveau 0.025 : c = 15 (P = 0.0207)
3. Puissance du test des signes, n = 20, niveau unilatéral 0,0125 (c = 16)
  p = 0.6 : puissance 0.0510
  p = 0.7 : puissance 0.2375
  p = 0.8 : puissance 0.6296
  p = 0.9 : puissance 0.9568
4. Part épargnée attendue par la règle de (v), prix centraux (0,25 ; 0,80 ; 1,00 ; 1,60 USD par appel)
  k =  0 mondes appelés : épargne 0.7123 du coût des proposeurs
  k =  1 mondes appelés : épargne 0.6767 du coût des proposeurs
  k =  2 mondes appelés : épargne 0.6411 du coût des proposeurs
  k =  3 mondes appelés : épargne 0.6055 du coût des proposeurs
  k =  4 mondes appelés : épargne 0.5699 du coût des proposeurs
  k =  5 mondes appelés : épargne 0.5342 du coût des proposeurs
  k = 10 mondes appelés : épargne 0.3562 du coût des proposeurs
  k = 15 mondes appelés : épargne 0.1781 du coût des proposeurs
  k = 20 mondes appelés : épargne 0.0000 du coût des proposeurs
5. Plus petit W dont la borne basse de Clopper-Pearson dépasse 0,05
  n = 16 : W >= 4 (borne basse 0.0727 ; à W - 1 : 0.0405)
  n = 17 : W >= 4 (borne basse 0.0681 ; à W - 1 : 0.0380)
  n = 18 : W >= 4 (borne basse 0.0641 ; à W - 1 : 0.0358)
  n = 19 : W >= 4 (borne basse 0.0605 ; à W - 1 : 0.0338)
  n = 20 : W >= 4 (borne basse 0.0573 ; à W - 1 : 0.0321)
6. Probabilité d'une perte établie à n = 20 (W >= 4) si chaque monde perd avec la probabilité p
  p = 0.05 : 0.0159
  p = 0.10 : 0.1330
  p = 0.15 : 0.3523
  p = 0.20 : 0.5886
  p = 0.26 : 0.8038
  p = 0.35 : 0.9556
  p = 0.47 : 0.9971
7. Part attendue d'ensembles au hasard (taille 1, 2 ou 3, uniforme) contenant au moins un distracteur, 8 traits
  d = 2 : tailles 1, 2, 3 : 0.2500, 0.4643, 0.6429 ; moyenne 0.4524
  d = 3 : tailles 1, 2, 3 : 0.3750, 0.6429, 0.8214 ; moyenne 0.6131
  d = 4 : tailles 1, 2, 3 : 0.5000, 0.7857, 0.9286 ; moyenne 0.7381
8. Six ensembles au hasard, indépendants : probabilité qu'au moins un contienne une paire donnée de traits
  par ensemble : 0.0476 ; sur six : 0.2538
9. Modèle synthétique : probabilité que la moitié chère (12 cartes) couvre ce que la moitié bon marché (12) a manqué
  forte (p = 0.5) : manquée par les 12 premières 0.0002 ; ajoutée par les 12 autres 0.0002
  moyenne (p = 0.25) : manquée par les 12 premières 0.0317 ; ajoutée par les 12 autres 0.0307
  faible (p = 0.1) : manquée par les 12 premières 0.2824 ; ajoutée par les 12 autres 0.2027
  conditionnelle sans condition (p = 0.02) : manquée par les 12 premières 0.7847 ; ajoutée par les 12 autres 0.1689
  monde à 1 conditionnelle et 2 moyennes : probabilité d'au moins une composante ajoutée 0.2191
  monde à 1 conditionnelle et 3 moyennes : probabilité d'au moins une composante ajoutée 0.2431
  monde à 2 conditionnelles et 2 moyennes : probabilité d'au moins une composante ajoutée 0.3511
  monde à 1 conditionnelle, 2 moyennes et 2 faibles certifiées : probabilité d'au moins une composante ajoutée 0.5036
```

**Programme 2 (point 10)** : `compte_certifiees_mr2_v1.py` (`8c0432df23cb78270c851d2c8f81e40b069a41ffefb8f3ddce03fa72804d9e39`),
lecture seule des 12 sorties scellées de [MR2] (chacune vérifiée contre son compagnon), lancé le 16 novembre à 12:18:19 UTC (heure
du fichier de sortie) par `nice -n 19 python3 -I compte_certifiees_mr2_v1.py docs/notes/organisme-multi-generations-v1/sorties-v4` ;
recopié en entier ; sa sortie (`319fa358d6ab8b70e32aba60d553d723a169d7a2ace6418549f8f6ef9d112ea0`) est recopiée à l'annexe A de
[CRIBLE-V] (point 10) :

```python
"""Compte des composantes certifiées (étiquette C8) par classe dans les 12 mondes de développement de la conception v4
(famille MR-2), lu dans les sorties scellées `sorties-v4/partie-v4-monde-{0…11}.json` ; lecture seule, aucun calcul de monde.
Usage : python3 -I compte_certifiees_mr2_v1.py DOSSIER_SORTIES_V4"""
import hashlib
import json
import os
import sys
from collections import Counter

d = sys.argv[1]
total = Counter()
for w in range(12):
    p = os.path.join(d, f"partie-v4-monde-{w}.json")
    sha = hashlib.sha256(open(p, "rb").read()).hexdigest()
    attendu = open(p + ".sha256", encoding="utf-8").read().split()[0]
    assert sha == attendu, f"empreinte différente : {p}"
    r = json.load(open(p, encoding="utf-8"))["resultat"]
    c = Counter(r["c8"][k]["classe"] for k in r["certifiees"])
    tous = Counter(v["classe"] for v in r["c8"].values())
    print(f"monde {w:2d} ({sha[:8]}) : certifiées {len(r['certifiees'])} {dict(sorted(c.items()))} ; toutes {dict(sorted(tous.items()))}")
    total += c
print("total des certifiées sur 12 mondes :", dict(sorted(total.items())))
```

Résumé de sa sortie : 4 à 6 composantes certifiées par monde ; total sur 12 mondes : 24 fortes, 23 moyennes, 14 conditionnelles,
1 faible. Ce sont des mondes de **développement** (graines publiques), jamais servis ; même générateur que les mondes du crible.

## Citations obligatoires (N-064, N-067)

POPPER (Huang et al., ICML 2025 ; `docs/sources/pdf/huang-2025-icml-pmlr-267-popper-automated-hypothesis-validation-agentic-sequential-falsifications.pdf`,
`a3c4b3701543a84a74602ae46a624b955e201bb83baeea2c219213a0e65b4998`) ; Dwork et al., arXiv 1506.02629
(`docs/sources/pdf/anteriorite-P-041-v2/c8/1506.02629.pdf`, `dcfbb9aa401c62949123be2d74787c4f9cca48597f18860760ef1580ddb4bc71`) ;
Blum et Hardt, « The Ladder », arXiv 1502.04585 (`…/c8/1502.04585.pdf`, `957ef4739df371a0a778360f0db4252a62f7c85abcd8343f581cd6250b1d31fe`) ;
Co-Scientist (Gottweis et al., Nature 655, p. 487-496, 2026 ;
`docs/sources/co-scientist-v1/gottweis-2026-nature-655-487-accelerating-scientific-discovery-with-co-scientist.pdf`,
`351f49d89d2f4f4ed84eed4225c09cc95470c41aa3becd0aa3e06b3bd8ba54c3`) ; liste de `docs/decisions/decision-N-067-v1.md`, section 6
(dont CADS, PACE, Qu, Chen et Wang, Hegazy, Jordan et Dieuleveut). Aucune revendication n'est faite ici.
