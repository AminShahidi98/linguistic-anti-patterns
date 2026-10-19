# Linguistic anti-patterns in Java

Finds Java methods whose name promises one thing while the code does another
(for example a `get` method that returns nothing), and rewrites them so the
name and the behaviour agree.

## Files

| file | what it is |
|---|---|
| `app.py` | the web page (Streamlit) |
| `lap_engine.py` | runs the detectors and fixers on one piece of code; used by `app.py` |
| `Core.py` | the original command-line version; edits `Demo.java` in place |
| `Detectors.py`, `Actuators.py`, `Utils.py`, `Models.py` | detection, fixes, helpers, LAP types |
| `Demo-backup.txt` | the example code the web page starts with |

## Run it on your computer

```
pip install -r requirements.txt
streamlit run app.py
```

It opens at http://localhost:8501.

## Put it online (Streamlit Community Cloud)

1. Push this folder to GitHub.
2. Go to https://share.streamlit.io, sign in with GitHub, and choose
   **Create app** -> this repository -> branch `main` -> file `app.py`.
3. Under **Advanced settings**, choose Python **3.12**. Deploy.
