import streamlit as st
import random

# --- Configurazione pagina ---
st.set_page_config(
    page_title="Risolvi e Vinci",
    page_icon="🎯",
    layout="centered"
)

# --- CSS personalizzato ---
st.markdown("""
    <style>
        body, .stApp {
            background-color: #000000;
            color: #FFD700;
        }
        .stButton>button {
            background-color: #FFD700;
            color: #000000;
            font-weight: bold;
        }
        .big-font {
            font-size:30px !important;
            font-weight:bold;
        }
        .med-font {
            font-size:18px !important;
        }
    </style>
""", unsafe_allow_html=True)

# --- Titolo e indizio iniziale ---
st.markdown('<div class="big-font">RISOLVI E VINCI</div>', unsafe_allow_html=True)
st.markdown('<div class="med-font"><em>"Nel buio non vince chi ha più coraggio, ma chi sa osservare. La luce, a volte, è più utile di un’arma. La vita si salva con la mente, non con il cuore. E chi non tradisce, sarà ricompensato."</em></div>', unsafe_allow_html=True)
st.write("")

# --- Sequenza vincente segreta ---
sequenza_vincente = [
    'Città abbandonata',
    'Accendino',
    'Donna misteriosa',
    'Non sacrifico'
]

# --- STEP 1: Scelta del luogo ---
scelta1 = st.radio(
    "1. Dove vuoi iniziare il tuo viaggio?",
    ('Bosco oscuro', 'Città abbandonata', 'Galleria sotterranea', 'Isola deserta'),
    key="step1"
)
st.write("")

# --- STEP 2: Scelta dell’oggetto ---
scelta2 = st.radio(
    "2. Scegli un oggetto da portare con te:",
    ('Coltello arrugginito', 'Accendino', 'Specchio rotto', 'Corda consumata'),
    key="step2"
)
st.write("")

# --- STEP 3: Scelta dell’alleato ---
scelta3 = st.radio(
    "3. Chi vuoi che ti accompagni?",
    ('Il bambino muto', 'Il vecchio cieco', 'La donna misteriosa', 'Il cane ferito'),
    key="step3"
)
st.write("")

# --- STEP 4: Scelta finale ---
scelta4 = st.radio(
    "4. Alla fine, cosa decidi di fare?",
    ('Sacrifico l’altro', 'Non sacrifico', 'Provo a scappare', 'Mi sacrifico io'),
    key="step4"
)
st.write("")

# --- Bottone di verifica ---
if st.button("Scopri il tuo destino"):
    scelte = [scelta1, scelta2, scelta3, scelta4]
    # Controllo sequenza
    if scelte == sequenza_vincente:
        codice = "BTC-" + str(random.randint(1000, 9999))
        st.success(f"🎉 Complimenti! Hai risolto l'enigma e il tuo codice vincente è: **{codice}** 🎉")
        st.write("")
        email = st.text_input("Inserisci la tua email per essere contattato:", "")
        wallet = st.text_input("Inserisci il tuo indirizzo wallet (es. Bitcoin):", "")
        if st.button("Salva i miei dati"):
            # Salvataggio su file locale (su Streamlit Cloud persisterà durante la sessione)
            with open("vincitori.csv", "a") as f:
                f.write(f"{email},{wallet},{codice}\n")
            st.info("Grazie! I tuoi dati sono stati salvati correttamente.")
    else:
        st.error("❌ Il tuo viaggio si è concluso... ma non nel modo giusto. Riprova o lascia che il destino decida per te.")

# --- Footer / Istruzioni ---
st.markdown("---")
st.markdown("Dopo aver ricevuto il codice vincente, se hai risolto, verrai contattato via email per ricevere il premio. Buona fortuna!")

