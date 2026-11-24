"""Remplissage déterministe et scellement sans édition manuelle de l'additif de commit des diagnostics préalables
des sondes de la boîte blanche (version 2 — v2 avec mode jonction_tardive_ulterieure, R-5209 point 2).

Substitue les marqueurs bornés du brouillon :
- <DATE_SCELLEMENT_UTC>
- <CHEMIN_NOTE_DES_EFFECTIFS>
- <SHA256_NOTE_DES_EFFECTIFS>
- <DOSES_D>
- <ETAT_CONTROLE_DU_CHEMIN>
- <OPTION_REJEUX_NULS>
- <CLAUSE_TABLE_CORRESPONDANCE_BBIS>
et, s'il figure encore dans le brouillon d'entrée, <ENTREE_CONTRE_LECTURE_ADDITIF>.

Gardes strictes sans repli silencieux (règle numéro 5) :
- vérification sur disque des compagnons .sha256 du brouillon, de la note des effectifs (via charger_note_effectifs),
  du rapport de contre-lecture et, le cas échéant, de la table de correspondance et de sa contre-lecture ;
- mode `jonction_tardive_ulterieure` (GO-2026-11-23-36, R-5209 point 2) : exige `--go-correspondance` valide,
  refuse tout fichier de correspondance et inscrit la clause de pièce jointe ultérieure contre-lue en classe B
  avant toute ouverture des données réelles ;
- refus d'écrasement de la sortie ou de son compagnon (règle numéro 12) ;
- refus de tout chemin absolu de machine dans les chemins inscrits au texte scellé ;
- refus du cas mixte du contrôle du chemin sans règle ni autorisation GO explicite ;
- refus de tout marqueur résiduel (<...>, <<...>>, « À REMPLIR ») avant toute écriture finale ;
- validation complète par `controle_ia.prereg.problemes` et scellement par `controle_ia.prereg.sceller_prereg`.
"""
from __future__ import annotations

import argparse
import json
import re
import sys
import tempfile
from pathlib import Path

# Permet l'exécution directe avec PYTHONPATH pointant vers sondes-v2-code/src
from controle_ia.gardes import GardeArret
from controle_ia import prereg
from controle_ia.scellement import verifier
from controle_ia.sondes_v2 import formats_v1 as fm
from controle_ia.sondes_v2 import statistiques_v2 as st

MARQUEURS_OBLIGATOIRES = (
    "<DATE_SCELLEMENT_UTC>",
    "<CHEMIN_NOTE_DES_EFFECTIFS>",
    "<SHA256_NOTE_DES_EFFECTIFS>",
    "<DOSES_D>",
    "<ETAT_CONTROLE_DU_CHEMIN>",
    "<OPTION_REJEUX_NULS>",
    "<CLAUSE_TABLE_CORRESPONDANCE_BBIS>",
)
MARQUEUR_CONTRE_LECTURE = "<ENTREE_CONTRE_LECTURE_ADDITIF>"

RE_DATE_UTC = re.compile(r"^\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}Z$")
RE_HEX64 = re.compile(r"^[0-9a-f]{64}$")
RE_GO = re.compile(r"^GO-\d{4}-\d{2}-\d{2}-\d+$")
RE_MARQUEUR_SIMPLE = re.compile(r"<[A-Za-z0-9_]+>")
RE_MARQUEUR_CHEVRON = re.compile(r"<[^>\n]+>")
RE_MARQUEUR_DOUBLE = re.compile(r"<<[^>\n]+>>")


def _exiger_chemin_relatif_depot(chemin_texte: str, nom_champ: str) -> str:
    if not isinstance(chemin_texte, str) or not chemin_texte.strip():
        raise GardeArret(f"{nom_champ} : chemin relatif dans le dépôt non vide attendu")
    p = Path(chemin_texte)
    if p.is_absolute() or ".." in p.parts:
        raise GardeArret(f"{nom_champ} : chemin relatif propre dans le dépôt attendu, reçu {chemin_texte!r}")
    return chemin_texte.strip()


def _verifier_hex64(valeur: str, nom_champ: str) -> str:
    if not isinstance(valeur, str) or not RE_HEX64.fullmatch(valeur):
        raise GardeArret(f"{nom_champ} : empreinte hexadécimale minuscule de 64 signes attendue, reçu {valeur!r}")
    return valeur


def _verifier_go(valeur: str | None, nom_champ: str) -> str:
    if not isinstance(valeur, str) or not RE_GO.fullmatch(valeur):
        raise GardeArret(f"{nom_champ} : identifiant au format GO-AAAA-MM-JJ-NN attendu, reçu {valeur!r}")
    return valeur


def _clause_option_rejeux(option_rejeux: int) -> str:
    if option_rejeux == 39:
        return (
            "option C retenue (`plan-epreuve-plantee-et-devis-v2.md`, § 5) : `39` rejeux demandés (`--nul 39`) pour "
            "les deux nuls hors des lignes du texte scellé (`contraste` et `texte`), soit à $P = 8$ paires et "
            "$\\alpha = 0,05$ un plafond analytique de puissance sous effet infini de `0,9626` (image retournée "
            "comptée) à `0,9897` (image non comptée), arrondi de `0,96` à `0,99` (contraste non testable à "
            "$\\alpha = 0,01$)."
        )
    if option_rejeux == 199:
        return (
            "option A retenue (`plan-epreuve-plantee-et-devis-v2.md`, § 5) : `199` rejeux demandés (`--nul 199`) pour "
            "les deux nuls hors des lignes du texte scellé (`contraste` et `texte`), soit à $P = 8$ paires et "
            "$\\alpha = 0,05$ un plafond analytique de puissance sous effet infini de `0,999995` à `1,00`, arrondi à "
            "`1,00` (`0,54` à `0,82` à $\\alpha = 0,01$)."
        )
    raise GardeArret(f"option de rejeux des nuls hors lignes : 39 ou 199 attendu, reçu {option_rejeux!r}")


def _verifier_structure_correspondance_json(chemin_correspondance: Path) -> str:
    sha_c = verifier(chemin_correspondance)
    try:
        c = json.loads(chemin_correspondance.read_text(encoding="utf-8"))
    except json.JSONDecodeError as e:
        raise GardeArret(f"table de correspondance illisible ({e})") from None
    cles_attendues = {
        "format", "redigee_par", "date_utc", "attestation", "table_source", "selection", "colonnes", "valeurs"
    }
    if not isinstance(c, dict) or set(c) != cles_attendues:
        raise GardeArret(f"table de correspondance : clés exactes {sorted(cles_attendues)} attendues")
    if c.get("format") != "correspondance-rejeu-croise-v1":
        raise GardeArret(f"table de correspondance : format {c.get('format')!r} invalide")
    if not isinstance(c.get("colonnes"), dict) or set(c["colonnes"]) != set(st.CHAMPS_TABLE):
        raise GardeArret("table de correspondance : les douze champs de CHAMPS_TABLE sont exigés dans colonnes")
    ts = c.get("table_source")
    if not isinstance(ts, dict) or set(ts) != {"chemin", "sha256", "ligne_registre", "format_fichier"}:
        raise GardeArret("table de correspondance : table_source incomplet ou invalide")
    _verifier_hex64(ts["sha256"], "correspondance.table_source.sha256")
    return sha_c


def _clause_correspondance(
    mode_correspondance: str,
    go_correspondance: str | None = None,
    fichier_correspondance: str | Path | None = None,
    chemin_correspondance_depot: str | None = None,
    rapport_cl_correspondance: str | Path | None = None,
    chemin_rapport_cl_correspondance_depot: str | None = None,
) -> str:
    if mode_correspondance == "jonction_tardive":
        go_id = _verifier_go(go_correspondance, "go_correspondance")
        if fichier_correspondance is None or chemin_correspondance_depot is None:
            raise GardeArret("jonction_tardive : fichier_correspondance et chemin_correspondance_depot obligatoires")
        if rapport_cl_correspondance is None or chemin_rapport_cl_correspondance_depot is None:
            raise GardeArret(
                "jonction_tardive : rapport_cl_correspondance et chemin_rapport_cl_correspondance_depot obligatoires "
                "(contre-lecture de classe B exigée)"
            )
        ch_corr = _exiger_chemin_relatif_depot(chemin_correspondance_depot, "chemin_correspondance_depot")
        ch_cl = _exiger_chemin_relatif_depot(
            chemin_rapport_cl_correspondance_depot, "chemin_rapport_cl_correspondance_depot"
        )
        sha_corr = _verifier_structure_correspondance_json(Path(fichier_correspondance))
        sha_cl = verifier(Path(rapport_cl_correspondance))
        return (
            f"jonction tardive accordée par Lazar sous `{go_id}` (écart déclaré à la lettre « jointe avant le "
            f"scellement » du texte scellé `R-5056`, aux trois conditions de la contre-lecture) : table "
            f"`{ch_corr}` (`{sha_corr}`), établie sans lecture d'aucune colonne de score, contre-lue en classe B "
            f"(`{ch_cl}`, `{sha_cl}`), scellée et inscrite avant l'épreuve à vérité plantée et avant le verdict du "
            f"test sur les adaptateurs jumeaux."
        )
    if mode_correspondance == "jonction_tardive_ulterieure":
        if any(x is not None for x in (fichier_correspondance, chemin_correspondance_depot,
                                       rapport_cl_correspondance, chemin_rapport_cl_correspondance_depot)):
            raise GardeArret(
                "jonction_tardive_ulterieure : aucun fichier de correspondance ne doit être fourni"
            )
        go_id = _verifier_go(go_correspondance, "go_correspondance")
        return (
            f"jonction tardive par pièce jointe ultérieure accordée par Lazar sous `{go_id}` et décision `R-5209` "
            f"(point 2, écart déclaré à la lettre « jointe avant le scellement » du texte scellé `R-5056`, aux trois "
            f"conditions de la contre-lecture) : la table de correspondance des champs du rejeu croisé "
            f"(`correspondance-rejeu-croise-v2.json`), établie sans lecture d'aucune colonne de score, contre-lue en "
            f"classe B et scellée par pièce jointe ultérieure avant toute ouverture des données réelles (activations "
            f"ou scores) et avant le verdict du test sur les adaptateurs jumeaux, sera jointe sans bloquer le "
            f"scellement du présent additif ni l'exécution de l'épreuve à vérité plantée (laquelle ne lit jamais la "
            f"table de correspondance)."
        )
    if mode_correspondance == "rejeu_non_calculable":
        if any(x is not None for x in (fichier_correspondance, chemin_correspondance_depot,
                                       rapport_cl_correspondance, chemin_rapport_cl_correspondance_depot)):
            raise GardeArret("rejeu_non_calculable : aucun fichier de correspondance ne doit être fourni")
        mention_go = ""
        if go_correspondance is not None:
            go_id = _verifier_go(go_correspondance, "go_correspondance")
            mention_go = f" (décision `{go_id}`)"
        return (
            f"table non jointe avant le scellement initial (`R-5056`){mention_go} : conformément à la liste d'arrêt "
            f"du texte scellé, la ligne du rejeu croisé (`Q3`) est déclarée d'avance « non calculable », sans arrêt "
            f"des lignes de l'identité des poids (`Q1`) et de l'étalon de transport (`Q2`)."
        )
    if mode_correspondance == "texte_neuf":
        if any(x is not None for x in (fichier_correspondance, chemin_correspondance_depot,
                                       rapport_cl_correspondance, chemin_rapport_cl_correspondance_depot)):
            raise GardeArret("texte_neuf : aucun fichier de correspondance ne doit être fourni")
        go_id = _verifier_go(go_correspondance, "go_correspondance")
        return (
            f"sur décision de Lazar (`{go_id}`, option c de la section 6, point 2, des décisions du concepteur "
            f"version 2), la table n'ayant pas été jointe avant `R-5056`, la ligne du rejeu croisé (`Q3`) est "
            f"« non calculable » sous le présent texte et renvoyée à un préenregistrement neuf contre-lu, sans arrêt "
            f"des lignes `Q1` et `Q2`."
        )
    raise GardeArret(
        f"mode_correspondance {mode_correspondance!r} hors de "
        "('jonction_tardive', 'jonction_tardive_ulterieure', 'rejeu_non_calculable', 'texte_neuf')"
    )


def remplir_et_sceller(
    *,
    brouillon: str | Path,
    sortie: str | Path,
    note_effectifs: str | Path,
    chemin_note_depot: str,
    date_scellement_utc: str,
    option_rejeux_nuls: int,
    mode_correspondance: str,
    attendu_sha256_note: str | None = None,
    attendu_doses_d: int | None = None,
    go_correspondance: str | None = None,
    fichier_correspondance: str | Path | None = None,
    chemin_correspondance_depot: str | None = None,
    rapport_cl_correspondance: str | Path | None = None,
    chemin_rapport_cl_correspondance_depot: str | None = None,
    regle_cas_mixte: str | None = None,
    go_cas_mixte: str | None = None,
    rapport_contre_lecture: str | Path | None = None,
    chemin_rapport_contre_lecture_depot: str | None = None,
    verdict_contre_lecture: str | None = None,
    auteur_contre_lecture: str = "sous-agent neuf séparé du rédacteur (contre-lecture de classe A sous GO-2026-11-23-33)",
    contre_lecture_fichier: str | Path | None = None,
) -> dict:
    brouillon_path = Path(brouillon)
    sortie_path = Path(sortie)
    if sortie_path.exists() or sortie_path.with_name(sortie_path.name + ".sha256").exists():
        raise GardeArret(f"{sortie_path} ou son compagnon .sha256 existe déjà (règle numéro 12)")

    if not isinstance(date_scellement_utc, str) or not RE_DATE_UTC.fullmatch(date_scellement_utc):
        raise GardeArret(
            f"date_scellement_utc : format AAAA-MM-JJTHH:MM:SSZ attendu, reçu {date_scellement_utc!r}"
        )

    ch_note_rel = _exiger_chemin_relatif_depot(chemin_note_depot, "chemin_note_depot")
    sha_brouillon = verifier(brouillon_path)
    texte = brouillon_path.read_text(encoding="utf-8")

    # Vérification préalable des marqueurs obligatoires dans le brouillon
    absents = [m for m in MARQUEURS_OBLIGATOIRES if m not in texte]
    if absents:
        raise GardeArret(f"brouillon incomplet : marqueurs obligatoires absents {absents}")

    # Validation complète de la note des effectifs scellée
    note_lue = fm.charger_note_effectifs(Path(note_effectifs))
    sha_note = _verifier_hex64(note_lue["sha256"], "sha256_note")
    doses_d = int(note_lue["doses_holm"])
    etat_chemin = str(note_lue["cas_mixte"])

    if attendu_sha256_note is not None:
        att_sha = _verifier_hex64(attendu_sha256_note, "attendu_sha256_note")
        if att_sha != sha_note:
            raise GardeArret(
                f"empreinte attendue de la note ({att_sha}) différente de l'empreinte vérifiée ({sha_note})"
            )
    if attendu_doses_d is not None:
        if isinstance(attendu_doses_d, bool) or not isinstance(attendu_doses_d, int) or attendu_doses_d != doses_d:
            raise GardeArret(
                f"nombre de doses D attendu ({attendu_doses_d!r}) différent de la note des effectifs (D = {doses_d})"
            )

    if etat_chemin.startswith("cas mixte"):
        if regle_cas_mixte is None or go_cas_mixte is None:
            raise GardeArret(
                "note des effectifs : cas mixte détecté sur le contrôle du chemin ; scellement refusé sans "
                "regle_cas_mixte et go_cas_mixte (nœud conditionnel pour Lazar)"
            )
        if regle_cas_mixte not in st.REGLES_CAS_MIXTE:
            raise GardeArret(f"regle_cas_mixte {regle_cas_mixte!r} hors de {st.REGLES_CAS_MIXTE}")
        go_cm = _verifier_go(go_cas_mixte, "go_cas_mixte")
        texte_etat_chemin = (
            f"cas mixte tranché par Lazar sous `{go_cm}` : règle retenue `{regle_cas_mixte}` "
            f"(détail par dose : `{json.dumps(note_lue['cas_mixte_par_dose'], ensure_ascii=False, sort_keys=True)}`)"
        )
    else:
        if regle_cas_mixte is not None or go_cas_mixte is not None:
            raise GardeArret(
                f"note des effectifs hors cas mixte ({etat_chemin!r}) : regle_cas_mixte et go_cas_mixte refusés"
            )
        texte_etat_chemin = etat_chemin

    clause_rejeux = _clause_option_rejeux(option_rejeux_nuls)
    clause_corr = _clause_correspondance(
        mode_correspondance=mode_correspondance,
        go_correspondance=go_correspondance,
        fichier_correspondance=fichier_correspondance,
        chemin_correspondance_depot=chemin_correspondance_depot,
        rapport_cl_correspondance=rapport_cl_correspondance,
        chemin_rapport_cl_correspondance_depot=chemin_rapport_cl_correspondance_depot,
    )

    substitutions = {
        "<DATE_SCELLEMENT_UTC>": date_scellement_utc,
        "<CHEMIN_NOTE_DES_EFFECTIFS>": ch_note_rel,
        "<SHA256_NOTE_DES_EFFECTIFS>": sha_note,
        "<DOSES_D>": str(doses_d),
        "<ETAT_CONTROLE_DU_CHEMIN>": texte_etat_chemin,
        "<OPTION_REJEUX_NULS>": clause_rejeux,
        "<CLAUSE_TABLE_CORRESPONDANCE_BBIS>": clause_corr,
    }

    contre_lecture_presente = MARQUEUR_CONTRE_LECTURE in texte
    if contre_lecture_presente:
        if contre_lecture_fichier is not None and rapport_contre_lecture is not None:
            raise GardeArret(
                "fournir soit contre_lecture_fichier, soit rapport_contre_lecture, jamais les deux à la fois"
            )
        if contre_lecture_fichier is not None:
            entree_cl = Path(contre_lecture_fichier).read_text(encoding="utf-8").strip()
            if not entree_cl:
                raise GardeArret("contre_lecture_fichier est vide")
        elif rapport_contre_lecture is not None:
            if not chemin_rapport_contre_lecture_depot or not verdict_contre_lecture:
                raise GardeArret(
                    "rapport_contre_lecture exige chemin_rapport_contre_lecture_depot et verdict_contre_lecture"
                )
            ch_cl_add = _exiger_chemin_relatif_depot(
                chemin_rapport_contre_lecture_depot, "chemin_rapport_contre_lecture_depot"
            )
            sha_cl_add = verifier(Path(rapport_contre_lecture))
            if sha_cl_add == sha_brouillon:
                raise GardeArret("le rapport de contre-lecture ne peut pas avoir la même empreinte que le brouillon")
            entree_cl = (
                f"- **Contre-lecture 1** : {auteur_contre_lecture.strip()}. "
                f"Brouillon relu : `{brouillon_path.name}` (`{sha_brouillon}`). "
                f"Rapport : `{ch_cl_add}` (`{sha_cl_add}`). "
                f"Verdict et traitement : {verdict_contre_lecture.strip()}"
            )
        else:
            raise GardeArret(
                f"le brouillon contient encore {MARQUEUR_CONTRE_LECTURE} : fournir rapport_contre_lecture "
                "ou contre_lecture_fichier"
            )
        substitutions[MARQUEUR_CONTRE_LECTURE] = entree_cl
    else:
        if any(x is not None for x in (contre_lecture_fichier, rapport_contre_lecture,
                                       chemin_rapport_contre_lecture_depot, verdict_contre_lecture)):
            raise GardeArret(
                f"{MARQUEUR_CONTRE_LECTURE} absent du brouillon (déjà rempli) : options de contre-lecture refusées"
            )

    texte_final = texte
    for cle, val in substitutions.items():
        texte_final = texte_final.replace(cle, val)

    # Garde stricte contre tout marqueur résiduel (simple chevron, double chevron, À REMPLIR)
    restes_doubles = sorted(set(RE_MARQUEUR_DOUBLE.findall(texte_final)))
    restes_simples = sorted(set(RE_MARQUEUR_SIMPLE.findall(texte_final)))
    restes_chevrons = sorted(set(RE_MARQUEUR_CHEVRON.findall(texte_final)))
    if restes_doubles or restes_simples or restes_chevrons:
        tous = sorted(set(restes_doubles) | set(restes_simples) | set(restes_chevrons))
        raise GardeArret(f"marqueurs résiduels détectés après substitution : {tous}")
    if prereg.MARQUEUR in texte_final:
        raise GardeArret(f"marqueur prohibé {prereg.MARQUEUR!r} présent dans le texte final")

    # Validation préalable par controle_ia.prereg.problemes sur un fichier temporaire avant d'écrire la cible
    with tempfile.NamedTemporaryFile("w", encoding="utf-8", suffix=".md", delete=True) as tmp:
        tmp.write(texte_final)
        tmp.flush()
        probs = prereg.problemes(tmp.name)
        if probs:
            raise GardeArret("additif non conforme à controle_ia.prereg : " + " ; ".join(probs))

    sortie_path.parent.mkdir(parents=True, exist_ok=True)
    sortie_path.write_text(texte_final, encoding="utf-8")
    sha_sortie = prereg.sceller_prereg(sortie_path)
    return {
        "sortie": str(sortie_path),
        "sha256": sha_sortie,
        "brouillon_sha256": sha_brouillon,
        "note_sha256": sha_note,
        "doses_d": doses_d,
        "etat_controle_du_chemin": texte_etat_chemin,
        "option_rejeux_nuls": option_rejeux_nuls,
        "mode_correspondance": mode_correspondance,
    }


def main(argv: list[str] | None = None) -> int:
    ap = argparse.ArgumentParser(description=__doc__.split("\n\n")[0])
    ap.add_argument("--brouillon", required=True, help="Chemin du brouillon scellé (.sha256 requis)")
    ap.add_argument("--sortie", required=True, help="Chemin de l'additif final à écrire et sceller")
    ap.add_argument("--note-effectifs", required=True, help="Chemin sur disque de la note des effectifs scellée")
    ap.add_argument("--chemin-note-depot", required=True, help="Chemin relatif de la note dans le dépôt")
    ap.add_argument("--date-scellement-utc", required=True, help="Horodatage UTC exact AAAA-MM-JJTHH:MM:SSZ")
    ap.add_argument("--option-rejeux-nuls", type=int, choices=(39, 199), required=True)
    ap.add_argument(
        "--mode-correspondance",
        choices=("jonction_tardive", "jonction_tardive_ulterieure", "rejeu_non_calculable", "texte_neuf"),
        required=True,
    )
    ap.add_argument("--attendu-sha256-note", default=None)
    ap.add_argument("--attendu-doses-d", type=int, default=None)
    ap.add_argument("--go-correspondance", default=None)
    ap.add_argument("--fichier-correspondance", default=None)
    ap.add_argument("--chemin-correspondance-depot", default=None)
    ap.add_argument("--rapport-cl-correspondance", default=None)
    ap.add_argument("--chemin-rapport-cl-correspondance-depot", default=None)
    ap.add_argument("--regle-cas-mixte", default=None)
    ap.add_argument("--go-cas-mixte", default=None)
    ap.add_argument("--rapport-contre-lecture", default=None)
    ap.add_argument("--chemin-rapport-contre-lecture-depot", default=None)
    ap.add_argument("--verdict-contre-lecture", default=None)
    ap.add_argument(
        "--auteur-contre-lecture",
        default="sous-agent neuf séparé du rédacteur (contre-lecture de classe A sous GO-2026-11-23-33)",
    )
    ap.add_argument("--contre-lecture-fichier", default=None)
    a = ap.parse_args(argv)
    res = remplir_et_sceller(
        brouillon=a.brouillon,
        sortie=a.sortie,
        note_effectifs=a.note_effectifs,
        chemin_note_depot=a.chemin_note_depot,
        date_scellement_utc=a.date_scellement_utc,
        option_rejeux_nuls=a.option_rejeux_nuls,
        mode_correspondance=a.mode_correspondance,
        attendu_sha256_note=a.attendu_sha256_note,
        attendu_doses_d=a.attendu_doses_d,
        go_correspondance=a.go_correspondance,
        fichier_correspondance=a.fichier_correspondance,
        chemin_correspondance_depot=a.chemin_correspondance_depot,
        rapport_cl_correspondance=a.rapport_cl_correspondance,
        chemin_rapport_cl_correspondance_depot=a.chemin_rapport_cl_correspondance_depot,
        regle_cas_mixte=a.regle_cas_mixte,
        go_cas_mixte=a.go_cas_mixte,
        rapport_contre_lecture=a.rapport_contre_lecture,
        chemin_rapport_contre_lecture_depot=a.chemin_rapport_contre_lecture_depot,
        verdict_contre_lecture=a.verdict_contre_lecture,
        auteur_contre_lecture=a.auteur_contre_lecture,
        contre_lecture_fichier=a.contre_lecture_fichier,
    )
    print(json.dumps(res, ensure_ascii=False, sort_keys=True))
    return 0


if __name__ == "__main__":
    try:
        sys.exit(main())
    except GardeArret as exc:
        print(f"ARRÊT : {exc}", file=sys.stderr)
        sys.exit(1)
