"""Écrit les couples du brouillon 8 (candidat) de T0.8 sur le brouillon 7 (R12 : refuse d'écraser).

Usage : python3 -I faire-couples-t08-brouillon8-v1.py DATE_UTC HEURE_UTC SORTIE_JSON   (relevées par `date -u`)
- vérifie l'empreinte du brouillon 7 et du journal du compte 4 qui recopie le mot de Lazar (v16, C4-0054) ;
- couples de l'auteur (session du compte 4, modèle A) : la phrase T5-19 du point 1 du plan est **gardée** (option (a), mot de
  Lazar « go a pour T5-19 ») ; le marqueur `MOT_LAZAR_T5_19` est rempli par ce mot et remplacé, pour ce qui reste à la session
  mère (ligne du registre où elle inscrit ce mot ; confirmation des trois points gardés), par `LIGNE_MOT_LAZAR_T5_19` ; liste des
  marqueurs de l'en-tête complétée ; déclaration de vue de l'auteur bornée au brouillon 8 ; relecture suivante ; titre, statut,
  « Auteurs », « Date ».
"""
import hashlib, json, re, sys
from pathlib import Path

B7 = Path("brouillons/T0.8-bases-boite-noire-v0-v1-brouillon7.md")
SHA_B7 = "1877e384cc639cd627b92af87f8c72775db160034d85ebf701dcc3256da4c017"
J16 = ("registres-provisoires/compte-4-2026-11-14-v16.md", "190fb7ed632c52c36f3ece7d837b84d9f9529f830553bf46c1ae10021cec9288")
MOT = "go a pour T5-19"
ANCIEN_MK = "<<" + "MOT_LAZAR_T5_19" + ">>"
NOUVEAU_MK = "<<" + "LIGNE_MOT_LAZAR_T5_19" + ">>"
SCRIPT = "brouillons/t08-code-compte4-v1/faire-couples-t08-brouillon8-v1.py"
COUPLES = "brouillons/t08-code-compte4-v1/couples-t08-brouillon8-v1.json"


def controles():
    for ch, s in ((B7, SHA_B7), (Path(J16[0]), J16[1])):
        if hashlib.sha256(Path(ch).read_bytes()).hexdigest() != s:
            sys.exit(f"ARRÊT : empreinte de {ch} différente")
    j = Path(J16[0]).read_text(encoding="utf-8")
    if f"> {MOT}\n" not in j or "## C4-0054" not in j:
        sys.exit("ARRÊT : le mot de Lazar n'est pas recopié tel quel au journal v16 (C4-0054)")
    t = B7.read_text(encoding="utf-8")
    lignes = [l for l in t.splitlines() if l.startswith("| `MOT_LAZAR_T5_19` |")]
    if len(lignes) != 1:
        sys.exit("ARRÊT : ligne `MOT_LAZAR_T5_19` de la table des marqueurs absente ou multiple")
    return lignes[0]


def couples_auteur(d, h, ligne_table):
    c = []
    def a(i, ancien, nouveau): c.append({"id": i, "ancien": ancien, "nouveau": nouveau})
    renvoi = f"journal du compte 4, C4-0054, `{J16[0]}`, `{J16[1]}`"
    a("T8-01", "— v1 — brouillon 7 (candidat)", "— v1 — brouillon 8 (candidat)")
    a("T8-02", "- **Statut** : **brouillon 7 (candidat)**, **non scellé** ; il ne vaut pas préenregistrement (R1). Le brouillon 7 applique",
      "- **Statut** : **brouillon 8 (candidat)**, **non scellé** ; il ne vaut pas préenregistrement (R1). Le brouillon 8 applique par "
      "programme les couples de son auteur sur le brouillon 7 : **la phrase T5-19 du point 1 du plan est gardée** (option (a) ; mot de "
      f"Lazar « {MOT} », tapé dans la session du compte 4 et recopié tel quel, {renvoi}) ; le marqueur `MOT_LAZAR_T5_19` est rempli par "
      "ce mot et remplacé, pour ce qui reste à la session mère, par `LIGNE_MOT_LAZAR_T5_19` (ligne du registre où elle inscrit ce mot, "
      "et sa confirmation des trois points gardés plus stricts que ce texte) ; liste des marqueurs de l'en-tête complétée ; déclaration "
      "de vue bornée au brouillon 8 ; relecture suivante ; titre, « Auteurs », « Date » ; script "
      f"`{SCRIPT}`, couples `{COUPLES}` ; aucune autre ligne ne change ; **non scellable avant la vérification courte du différentiel "
      "du brouillon 6 au brouillon 8, le marqueur `LIGNE_MOT_LAZAR_T5_19` et les six autres marqueurs**. Le brouillon 7 applique")
    a("T8-03", "`MOT_LAZAR_T5_19` ajouté au brouillon 7 ; section « Marqueurs à remplir avant le scellement ») : `CODE_MOTS_ET_COUT_T06`, "
      "`RUN_7B`, `EMPREINTES_ENTREES_7B`, `ENTROPIE_T08`, `GO_T08`, `LIGNE_DEPENSE_T08`.",
      "`MOT_LAZAR_T5_19` ajouté au brouillon 7, rempli au brouillon 8 par le mot de Lazar et remplacé par `LIGNE_MOT_LAZAR_T5_19` "
      "pour l'inscription par la session mère ; section « Marqueurs à remplir avant le scellement ») : `CODE_MOTS_ET_COUT_T06`, "
      "`RUN_7B`, `EMPREINTES_ENTREES_7B`, `ENTROPIE_T08`, `GO_T08`, `LIGNE_DEPENSE_T08`, `LIGNE_MOT_LAZAR_T5_19`.")
    a("T8-04", f"(phrase ajoutée au brouillon 5, VCT8B-01 ; nœud de Lazar, VT5-03 : `{ANCIEN_MK}`) ;",
      f"(phrase ajoutée au brouillon 5, VCT8B-01 ; nœud de Lazar, VT5-03 : **gardée**, option (a), mot de Lazar « {MOT} » ({renvoi}) ; "
      f"ligne du registre et confirmation de la session mère : `{NOUVEAU_MK}`) ;")
    a("T8-05", "à confirmer par elle au remplissage du marqueur `MOT_LAZAR_T5_19`",
      "à confirmer par elle au remplissage du marqueur `LIGNE_MOT_LAZAR_T5_19`")
    a("T8-06", ligne_table,
      "| `LIGNE_MOT_LAZAR_T5_19` | la ligne du registre où la session mère inscrit le mot de Lazar sur la phrase T5-19 du point 1 du "
      f"plan (« {MOT} » : option (a), phrase gardée ; {renvoi} ; marqueur `MOT_LAZAR_T5_19` du brouillon 7, rempli au brouillon 8 par "
      "ce mot) ; avec la confirmation de la session mère sur les trois points gardés plus stricts que ce texte (contre-lecture du code, "
      "traitement) | avant le scellement, avant `GEL-T08` | session mère |")
    a("T8-07", "**Relecture suivante, prévue avant le scellement** : au mot de Lazar sur T5-19, le texte qui remplit `MOT_LAZAR_T5_19` "
      "(et, si la phrase est refusée, la retire) ;",
      "**Relecture du brouillon 7**, prévue alors : au mot de Lazar sur T5-19, le texte qui remplit `MOT_LAZAR_T5_19` "
      "(et, si la phrase est refusée, la retire ; fait : brouillon 8, phrase gardée) ;")
    a("T8-08", "son entrée s'ajoute au texte qui suit ; puis les six autres marqueurs.",
      "son entrée s'ajoute au texte qui suit ; puis les six autres marqueurs.\n\n"
      "**Relecture suivante, prévue avant le scellement** : vérification courte du différentiel du brouillon 6 au brouillon 8 "
      "(couples du brouillon 7 et du brouillon 8), par un sous-agent neuf d'un autre modèle que l'auteur (modèle A), qui n'a écrit ni "
      "ce texte, ni la base (A), ni le code de T0.8, ni les relectures précédentes, et n'a vu aucun résultat de 7b, de la pièce HD ni "
      "de sonde ; son entrée s'ajoute au texte qui suit ; puis `LIGNE_MOT_LAZAR_T5_19` et les six autres marqueurs, par la session mère.")
    a("T8-09", "(déclaration de vue, VT5-04 ; bornée au brouillon 7, VT6-03)",
      "(déclaration de vue, VT5-04 ; bornée au brouillon 7, VT6-03, puis au brouillon 8)")
    a("T8-10", "les messages de commit de `main`, et les seules sorties **factices** des essais jouets du code de T0.8.",
      "les messages de commit de `main`, les seules sorties **factices** des essais jouets du code de T0.8 et de celui de (ii-b), et, "
      "pour (ii-b), des extraits de sa conception, les rapports de son développeur et de la contre-lecture 1 de son code, et les suites "
      "de six mots que la consigne privée de son maître partage avec ce dernier rapport (chemins de fichiers et phrases de sa conception).")
    a("T8-11", "**brouillons 5 à 7 (candidats)**, la session du compte 4", "**brouillons 5 à 8 (candidats)**, la session du compte 4")
    a("T8-12", "- **Date (UTC)** : brouillon 7 écrit le ",
      f"- **Date (UTC)** : brouillon 8 écrit le {d} à partir de {h} UTC (heure relevée par `date -u`) ; brouillon 7 écrit le ")
    return c


def principal():
    if len(sys.argv) != 4:
        sys.exit(__doc__)
    d, h, sortie = sys.argv[1], sys.argv[2], Path(sys.argv[3])
    if not re.fullmatch(r"\d{4}-\d{2}-\d{2}", d) or not re.fullmatch(r"\d{2}:\d{2}", h):
        sys.exit("ARRÊT : date AAAA-MM-JJ et heure HH:MM attendues")
    if sortie.exists():
        sys.exit(f"ARRÊT : {sortie} existe déjà (R12)")
    tout = couples_auteur(d, h, controles())
    sortie.write_text(json.dumps(tout, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
    print(f"{len(tout)} couples écrits dans {sortie} ; sha256 {hashlib.sha256(sortie.read_bytes()).hexdigest()}")


principal()
