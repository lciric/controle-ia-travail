# Remplit [[CONTRE_LECTURE]] et [[CONTRE_LECTURE_DETAIL]] du texte v4 (contre-lectures 1 à 4 de P4v3, 5 traitée, 6 à venir).
# Aucune ligne « entropie E = » ni « graine de la course … = » n'est écrite ici (le script de scellement les refuserait).
import hashlib, pathlib, sys

p = pathlib.Path("/home/claude/pilote4/essaim-m3-refonte-v1/prereg/pilote4-gemini-organisme-v4.md")
t = p.read_text(encoding="utf-8")
h0 = hashlib.sha256(t.encode("utf-8")).hexdigest()
assert h0.startswith("b38fb3d8"), h0
assert t.count("[[CONTRE_LECTURE]]") == 1 and t.count("[[CONTRE_LECTURE_DETAIL]]") == 1

entete = ("1 à 4 sur P4v3 (son § Contre-lecture : `3dd09acb…`, `7c625fa6…`, `0d95ea8c…`,\n"
          "`e2de1372…`), 5 sur ce texte (`914ac3fb…`, « scellable après corrections mineures », traitée) et 6, courte, sur l'écart\n"
          "depuis la 5 (§ Contre-lecture)")

detail = r"""- **Contre-lectures 1 à 4** : celles de P4v3 (son § Contre-lecture), sur les v1, v2 et v3 du texte ; leurs rapports
  (`pilote4-gemini-organisme-v1-cl1.md`, `3dd09acb…` ; `-v2-cl2.md`, `7c625fa6…` ; `-v3-cl3.md`, `0d95ea8c…` ; `-v3-cl4.md`,
  `e2de1372…`) et leurs pièces sont au fichier d'empreintes de P4v3 et à celui de ce texte. Ce qu'elles ont relu (noyau,
  banque v3, lanceur v6 et batterie v8, règles de P4v3) n'a pas changé ; ce texte n'en modifie que ce que la table de
  correspondance dit.
- **Contre-lecture 5** — sous-agent neuf (`claude-opus-5-5`, lancé par conv-audit, 26 octobre 2026, de 00:29 à 00:55 UTC),
  sur ce texte avant corrections (`efb13feb34f66d9652a194564c0bc9eced2889cbb6305c8dac9e97766246b60e`, 323 lignes ; copie
  gardée dans `contre-lecture-5-v1/`) et P4v3 en entier, avec les pièces v6 (`EMPREINTES-pieces-pilote4-v6.txt`) :
  `prereg/contre-lectures/pilote4-gemini-organisme-v4-cl5.md`
  (`914ac3fbf6b2ba0760ef3dace4dd8c3768909809e441ec0f63e5407c2d138240`), **« scellable après corrections mineures »** :
  objet recalculé conforme (arbres, 26 fichiers, écart 3bbb78c → 7ea3270 réduit à C-14 à C-17), lanceurs v7 à v10,
  batteries v9 à v12 et script de scellement v4 redérivés octet pour octet, série v13 complète (229 sur 229) et relevé
  reproduit, lignes de GO et de dépense passant les `grep` du lanceur, mots de Lazar rendus fidèlement ; deux constats
  mineurs, cinq remarques, une conformité ; pièces `pieces-pilote4-gemini/contre-lecture-5-v1/` (brief, rapport et
  relevés du contre-lecteur, copie du texte relu). **Traitement, par conv-audit, à partir de 01:03 UTC** (sans nouvelle
  relecture complète ; la contre-lecture 6 relit l'écart) :
  - P4C5-01 (mineur : options (2) et (2') de la décision ouverte, applicables sans procédure de lecture) : **sans objet**
    depuis les décisions de Lazar de 01:48 et 01:52 (hypothèses de (b) sans aucun score de ce pilote, (b) sur la banque
    v6 : ces options n'existent plus) et de 01:56 (pilote de conception : le moment et les règles de lecture sont au § Plan,
    point 3, qui remplace celui de P4v3 ; § Décisions).
  - P4C5-02 (mineur : deux énoncés de P4v3 dépendant de l'ordre non transposés) : **corrigé** — ligne de la table de
    correspondance « devis, plafond total » (pour la v6.2, la v5.3 ne part pas ; essai `v62-plafond-total`) et ligne de la
    liste d'arrêt « ronde de la v6.2 hors `OK` ».
  - P4C5-03 (remarque : canal (d) écrit au `LANCEMENT.md` de la seconde course) : **écrit** au § Objet (canal (d)) ; la
    règle des options (2) et (2') ayant disparu, la question de l'échéance est sans objet.
  - P4C5-04 (remarque : (a) défaut de la décision du 25 octobre 23:56 UTC — sans objet, tranchée à 01:48 ; (b) forme de la
    ligne de GO — **écrit** au § Plan, point 1 : le message de départ recopie mot pour mot les lignes, l'empreinte remplie,
    sinon rien ne part ; (c) choix laissés à Lazar sur C-14 et C-16 — **écrits** comme points ouverts dans la table).
  - P4C5-05 (remarque, § Essais : (a) réseau sans clé pour `passerelle-saine` et pour l'essai de moisson réelle sur arXiv —
    **corrigé** ; (b) décalage des numéros de lignes du lanceur v6 au v10 (+12 avant l'étape (0 bis), +13 après) — **écrit**
    dans la table ; (c) gardes de la ligne « course v6.2 hors de la liste close » aux étapes (0 bis), (2) et (4) — **corrigé** ;
    (d) aucune seconde course en segments essayée — **déclaré** comme lacune au § Essais, à combler par le prochain lanceur).
  - P4C5-06 (remarque, traçabilité : (a) pièces des cas sains de la série v13 — **versées** (`simulation-lanceur-v10/`) ;
    (b) relevé v2 jamais servi — **versé** (`releves-serie-v11-v1/`) ; (c) versions de code des essais `v621-a` et `v621-b`
    non gardées — **dit** au § Objet, avec leurs causes et les témoins).
  - P4C5-07 (remarque, petits faits : (a) C-14 « dès deux castes, la délibération s'ouvre » — **corrigé** ; (b) le refus
    d'une clé JSON absente est le point 8 de P4v3, gardé, non C-17 — **corrigé** ; (c) commentaire d'en-tête de
    `sceller_pilote4_v4.py` (l. 17–18 : « v5-3 (première course) ») inexact depuis l'inversion de l'ordre — **laissé tel
    quel** : sans effet sur le code (l'enfant 0 reste la graine de la v5.3, l'enfant 1 celle de la v6.2, comme le § Plan,
    point 2, le dit et comme le lanceur le recalcule), et le script, ses essais (16 sur 16) et son empreinte sont ceux que
    la contre-lecture 5 a redérivés ; (d) tête de la copie de lancement — **écrit** au § Plan, point 1 : elle ne diffère de
    `8e5e2f7b` que par les chemins que `PERMIS_APRES_CODE` permet).
  - P4C5-08 (conforme) : rien à traiter.
- **Contre-lecture 6** — sous-agent neuf, relecture courte de l'écart depuis la version relue par la contre-lecture 5
  (traitement ci-dessus, décisions de Lazar de 01:48 à 02:17 inscrites, § Plan points 3 et 4 bis, liste d'arrêt, § Essais,
  § Pièces), sur la version de ce texte qui porte ce paragraphe sans la ligne qui suit ; sa ligne — empreinte de la version
  relue, rapport `prereg/contre-lectures/pilote4-gemini-organisme-v4-cl6.md` et son empreinte, verdict, constats et leur
  traitement — est inscrite ici avant le script de scellement, avec ses pièces (`contre-lecture-6-v1/`).
- **Ce texte scellé** garde le nom de la v4 ; son empreinte n'est aucune de celles que les contre-lectures ont relues. De la
  version relue par la contre-lecture 6 à lui, il porte en plus : la ligne de la contre-lecture 6 ci-dessus, le traitement
  de ses constats s'il y en a (écrits à la main par conv-audit avant le script), puis l'entropie, les deux graines et
  l'empreinte du fichier d'empreintes des pièces, écrites par `sceller_pilote4_v4.py` ; rien d'autre. Les pièces nouvelles
  depuis la contre-lecture 6 sont ses propres pièces, toutes au fichier d'empreintes."""

t = t.replace("[[CONTRE_LECTURE]]", entete, 1).replace("[[CONTRE_LECTURE_DETAIL]]", detail, 1)
for bad in ("entropie E =", "graine de la course v5-3 =", "graine de la course v6-2 ="):
    assert t.count(bad) == 1, bad  # une seule occurrence : celle du § Plan, point 2, avec son marqueur
p.write_text(t, encoding="utf-8")
h1 = hashlib.sha256(t.encode("utf-8")).hexdigest()
print("appliqué ;", h0[:16], "->", h1)
