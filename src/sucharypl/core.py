from requests import get
from requests import exceptions as reqError
from typing import Literal

Kategoria = Literal["programowanie", "dwuznaczne", "szkolne", "suchary", "wulgarne", "czarnyhumor", "inne"]

class SucharyError(Exception):
     # Bazowy błąd dla biblioteki sucharypl
    pass

class SucharyConnectionError(SucharyError):
    # Błąd połączenia lub timeout
    pass

class SucharyHTTPError(SucharyError):
    # Błąd po stronie serwera (np. 404 lub 500)
    pass

def dajKawal(kategoria: Kategoria | None = None) -> str:
    if kategoria is None:
        adres = "https://sucharyapi.onrender.com"
    else:
        adres = f"https://sucharyapi.onrender.com/{kategoria}"
    try:
        r = get(adres, timeout=6.5)
        r.raise_for_status()
        dane = r.json()
        zart = dane["zart"]
    except reqError.ConnectionError as e:
        raise SucharyConnectionError("Nie udało się połączyć z bazą. Sprawdź swoje połączenie internetowe") from e
    except reqError.Timeout as e:
        raise SucharyConnectionError("Serwer nie odpowiada. Spróbuj ponownie później") from e
    except reqError.HTTPError as e:
        if e.response.status_code == 404:
            raise SucharyHTTPError(f"Nie znaleziono w kategorii {kategoria}") from e
        else:
            raise SucharyHTTPError("Błąd serwera. Spróbuj ponownie później") from e
    except reqError.JSONDecodeError as e:
        raise SucharyError("Otrzymano niepoprawny format danych z serwera") from e
    except Exception as e:
        raise SucharyError(f"Nastąpił błąd :( {e}") from e
    else:
        return zart