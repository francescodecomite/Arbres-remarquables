import csv
from pyproj import Transformer

# Lambert 72 -> WGS84
transformer = Transformer.from_crs(
    "EPSG:31370",
    "EPSG:4326",
    always_xy=True
)

fichier_entree = "coordonnees.csv"
fichier_sortie = "coordonnees_wgs84.csv"

with open(fichier_entree, "r", encoding="utf-8-sig", newline="") as f_in:
    lecteur = csv.DictReader(f_in, delimiter=";")

    # Conserver les colonnes existantes
    fieldnames = lecteur.fieldnames + ["longitude", "latitude"]

    with open(fichier_sortie, "w", encoding="utf-8", newline="") as f_out:
        ecrivain = csv.DictWriter(
            f_out,
            fieldnames=fieldnames,
            delimiter=";"
        )

        ecrivain.writeheader()

        for ligne in lecteur:
            x = float(ligne["X"])
            y = float(ligne["Y"])

            longitude, latitude = transformer.transform(x, y)

            ligne["longitude"] = f"{longitude:.8f}"
            ligne["latitude"] = f"{latitude:.8f}"

            ecrivain.writerow(ligne)

print(f"Conversion terminée : {fichier_sortie}")
