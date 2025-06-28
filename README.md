# 💖 Emilies Ønskeliste

En hyggelig og sikker ønskeliste-app for Emilie, hvor hun kan administrere sine ønsker og familie kan se hva hun ønsker seg.

## Funksjoner

- **Emilies grensesnitt**: Legg til og fjern ønsker med navn, beskrivelse og lenke
- **Familie grensesnitt**: Se ønskelisten, marker ting som kjøpt og legg til hvem som kjøpte det
- **Sikker innlogging**: Passord-basert autentisering for to brukertyper
- **Pen design**: Rosa, koselig tema som passer for en 13-åring
- **Statistikk**: Oversikt over kjøpte og ikke-kjøpte ønsker

## Brukere

- **Emilie** (`princess123`): Kan legge til/fjerne ønsker, men ikke se kjøpsstatus
- **Familie** (`family456`): Kan se alle ønsker og markere dem som kjøpt

## Teknologier

- Python 3.x
- Streamlit - Web app framework
- Pandas - Data manipulation
- UUID - Unique identifiers

## Installation

1. Clone or download this repository
2. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## Running the App

To start the Streamlit application:

```bash
streamlit run app.py
```

The app will open in your default web browser at `http://localhost:8501`

## App Structure

```
├── app.py              # Main Streamlit application
├── requirements.txt    # Python dependencies
└── README.md          # This file
```

## Bruk

1. **Som Emilie**: 
   - Logg inn med passord `princess123`
   - Legg til nye ønsker med navn, beskrivelse og lenke
   - Fjern ønsker du ikke lenger vil ha
   - Se oversikt over alle dine ønsker

2. **Som familie**: 
   - Logg inn med passord `family456`
   - Se alle Emilies ønsker med statistikk
   - Marker ønsker som kjøpt og legg til ditt navn
   - Se hvem som har kjøpt hva og når

## Tilpasning

Du kan lett utvide denne appen ved å:
- Legge til flere brukere eller brukertyper
- Implementere database lagring (f.eks. SQLite eller Firebase)
- Legge til e-post notifikasjoner når noe kjøpes
- Integrere med nettbutikker for prissjekk
- Legge til kategorisering av ønsker

## Contributing

Feel free to fork this project and submit pull requests for any improvements!
