# Weather ETL Pipeline (Python + MSSQL)

Detta projekt är ett enkelt **ETL-flöde** i Python som:
1. **Extraherar** väderdata från OpenWeatherAPI.
2. **Transformar** datan (plockar ut temperatur, beskrivning och timestamp).
3. **Laddar** in datan i en MSSQL-databas.
4. **Loggar** alla händelser till både terminal och loggfil (med rotation).
5. **Testas** automatiskt med `pytest`.

---

## Installation

### 1. Klona projektet
```bash
git clone <repo-url>
cd projektmapp
