#!/usr/bin/env python3
"""Agrega cotizaciones a price_history.csv y regenera data.json.
Uso: python3 actualizar.py --viaje mar19|ene31 --tipologia directo|rapido|economico \
     --precio-clp N --aerolinea X --duracion 13h25m --escalas 0 --fuente "Google Flights" --url "https://..."
Sin argumentos: solo regenera data.json."""
import argparse, csv, json, datetime, pathlib
ROOT = pathlib.Path(__file__).resolve().parent
CSV = ROOT / "price_history.csv"
OUT = ROOT / "data.json"
def regenerar():
    rows = list(csv.DictReader(open(CSV, encoding="utf-8")))
    OUT.write_text(json.dumps({"actualizado": datetime.datetime.utcnow().isoformat() + "Z",
                               "registros": rows}, ensure_ascii=False, indent=1), encoding="utf-8")
    print(f"data.json regenerado: {len(rows)} registros")
if __name__ == "__main__":
    p = argparse.ArgumentParser()
    for a in ["--viaje", "--tipologia", "--aerolinea", "--precio-clp", "--precio-usd",
              "--duracion", "--escalas", "--fuente", "--url", "--notas"]:
        p.add_argument(a, default="")
    args = p.parse_args()
    if args.tipologia:
        now = datetime.datetime.now()
        with open(CSV, "a", newline="", encoding="utf-8") as f:
            csv.writer(f).writerow([datetime.datetime.utcnow().isoformat() + "Z",
                now.strftime("%Y-%m-%d"), now.strftime("%H:%M"), args.viaje or "mar19",
                args.tipologia, args.aerolinea, args.precio_clp, args.precio_usd,
                args.duracion, args.escalas, args.fuente, args.url, args.notas])
    regenerar()
