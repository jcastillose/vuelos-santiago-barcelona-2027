# vuelos-santiago-barcelona-2027

Monitor de precios de vuelos Santiago de Chile (SCL) → Barcelona (BCN).
- Itinerario A: ida 2027-01-09 · retorno 2027-03-19 (69 días)
- Itinerario B: ida 2027-01-09 · retorno 2027-01-31 (22 días)
- Tipologías: (1) directo, (2) económico de menor duración, (3) económico
- Consultas programadas: 06:00, 10:00 y 16:00 (hora local)
- Base histórica: `price_history.csv`
- Sitio: `index.html` (GitHub Pages, rama main raíz)

## Criterios de tipología
1. **Directo**: vuelo sin escalas más barato (LEVEL / Iberia, ~13h25 por trayecto).
2. **Económico de menor duración**: itinerario más corto entre las opciones económicas (precio < CLP 2.000.000), excluyendo el directo.
3. **Económico**: precio más bajo de toda la búsqueda, sin restricciones.

Precios ida y vuelta en CLP, 1 adulto, turista, tomados de Google Flights (moneda CLP forzada). Cada corrida registra las tres tipologías para ambos itinerarios; la columna `viaje` (mar19 / ene31) los distingue.
