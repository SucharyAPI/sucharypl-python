# SucharyPL - oficjalna biblioteka bazy SucharyAPI
Pythonowa biblioteka do pobierania kawałów z ogólnopolskiej bazy SucharyAPI

[![Python Version](https://img.shields.io/badge/python-3.8%2B-blue)](https://www.python.org/)
[![License](https://img.shields.io/badge/license-MIT-green)](LICENSE)

---

## 🚀 Instalacja
### Za pomocą pip

```bash
pip install sucharypl
```

### Za pomocą uv (w projekcie)

```bash
uv add sucharypl
```

---

## ⚡ Szybki start
### Pobranie losowego suchara
```python
from sucharypl import dajKawal

# Pobierz losowy suchar z dowolnej kategorii
suchar = dajKawal()
print(suchar)
```

### Pobranie suchara z konkretnej kategorii
```python
from sucharypl import dajKawal

# Pobierz suchar z kategorii "programowanie"
suchar = dajKawal(kategoria="programowanie")
print(suchar)
```

---

## Kategorie
- `"programowanie"` - Suchary o programowaniu
- `"dwuznaczne"` - Suchary dwuznaczne
- `"szkolne"` - Suchary szkolne
- `"suchary"` - Ogólne suchary
- `"wulgarne"` - Suchary wulgarne
- `"czarnyhumor"` - Czarny humor
- `"inne"` - Inne kategorie

---

## 🛡️ Obsługa błędów

Biblioteka rzuca sformalizowane wyjątki, które możesz łatwo obsługiwać:

### Dostępne wyjątki

- `SucharyError` - Bazowy wyjątek, rodzic wszystkich błędów z biblioteki
- `SucharyConnectionError` - Problemy z połączeniem (brak internetu, timeout)
- `SucharyHTTPError` - Błędy serwera (np. 404 dla nieistniejącej kategorii)

### Przykład obsługi błędów

```python
from sucharypl import dajKawal, SucharyError, SucharyConnectionError, SucharyHTTPError

try:
    suchar = dajKawal(kategoria="programowanie")
    print(suchar)
except SucharyConnectionError:
    print("❌ Błąd połączenia - sprawdź połączenie internetowe!")
except SucharyHTTPError as e:
    print(f"❌ Błąd serwera: {e}")
except SucharyError as e:
    print(f"❌ Nieoczekiwany błąd: {e}")
```

---

## 📡 API

Biblioteka jest produktem oraz korzysta z oficjalnej bazy SucharyAPI:  
🔗 [https://sucharyapi.onrender.com](https://sucharyapi.onrender.com)

---

## 📝 Licencja

MIT

---