import streamlit as st
import pandas as pd
import random

# Page Configuration
st.set_page_config(
    page_title="Antigravity - Learn Japanese",
    page_icon="🔔",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS for Doraemon Theme
st.markdown("""
    <style>
    /* Doraemon Colors */
    :root {
        --dora-blue: #0096E1;
        --dora-red: #D80F28;
        --dora-white: #FFFFFF;
        --dora-bell: #F1C40F;
    }
    
    .stApp {
        background-color: #F0F8FF;
    }
    
    /* Sidebar styling */
    [data-testid="stSidebar"] {
        background-color: var(--dora-blue);
    }
    [data-testid="stSidebar"] * {
        color: white !important;
    }
    
    /* Headers */
    h1, h2, h3 {
        color: var(--dora-blue);
        font-family: 'Comic Sans MS', 'Chalkboard SE', sans-serif;
    }
    
    /* Custom Buttons */
    .stButton>button {
        background-color: var(--dora-red);
        color: white;
        border-radius: 20px;
        border: 2px solid white;
    }
    .stButton>button:hover {
        background-color: #ff4b4b;
        border-color: var(--dora-bell);
    }
    
    </style>
""", unsafe_allow_html=True)

# Session State Initialization
if 'vocab_list' not in st.session_state:
    st.session_state['vocab_list'] = []

def main():
    st.title("🔔 Antigravity (Japanese Learning)")

    # Sidebar Navigation
    st.sidebar.image("https://upload.wikimedia.org/wikipedia/en/b/bd/Doraemon_character.png", width=100) # Placeholder or remove if not allowed
    st.sidebar.title("Gadget Menu 🚪")
    
    menu = st.sidebar.radio(
        "Choose a Gadget:",
        ["50-Sound Chart", "Anywhere Door", "Memory Bread", "Quiz Mode"]
    )

    if menu == "50-Sound Chart":
        show_50_sound_chart()
    elif menu == "Anywhere Door":
        show_anywhere_door()
    elif menu == "Memory Bread":
        show_memory_bread()
    elif menu == "Quiz Mode":
        show_quiz_mode()

def show_50_sound_chart():
    st.header("50-Sound Chart (五十音圖)")
    
    tabs = st.tabs(["Hiragana (平假名)", "Katakana (片假名)"])
    
    hiragana = [
        ['あ', 'い', 'う', 'え', 'お'],
        ['か', 'き', 'く', 'け', 'こ'],
        ['さ', 'し', 'す', 'せ', 'そ'],
        ['た', 'ち', 'つ', 'て', 'と'],
        ['な', 'に', 'ぬ', 'ね', 'の'],
        ['は', 'ひ', 'ふ', 'へ', 'ほ'],
        ['ま', 'み', 'む', 'め', 'も'],
        ['や', '', 'ゆ', '', 'よ'],
        ['ら', 'り', 'る', 'れ', 'ろ'],
        ['わ', '', '', '', 'を'],
        ['ん', '', '', '', '']
    ]
    
    katakana = [
        ['ア', 'イ', 'ウ', 'エ', 'オ'],
        ['カ', 'キ', 'ク', 'ケ', 'コ'],
        ['サ', 'シ', 'ス', 'セ', 'ソ'],
        ['タ', 'チ', 'ツ', 'テ', 'ト'],
        ['ナ', 'ニ', 'ヌ', 'ネ', 'ノ'],
        ['ハ', 'ヒ', 'フ', 'ヘ', 'ホ'],
        ['マ', 'ミ', 'ム', 'メ', 'モ'],
        ['ヤ', '', 'ユ', '', 'ヨ'],
        ['ラ', 'リ', 'ル', 'レ', 'ロ'],
        ['ワ', '', '', '', 'ヲ'],
        ['ン', '', '', '', '']
    ]
    
    with tabs[0]:
        st.subheader("Hiragana")
        for row in hiragana:
            cols = st.columns(5)
            for i, char in enumerate(row):
                with cols[i]:
                    if char:
                        st.button(char, key=f"h_{char}", use_container_width=True)
    
    with tabs[1]:
        st.subheader("Katakana")
        for row in katakana:
            cols = st.columns(5)
            for i, char in enumerate(row):
                with cols[i]:
                    if char:
                        st.button(char, key=f"k_{char}", use_container_width=True)

def show_anywhere_door():
    st.header("Anywhere Door (隨意門) 🚪")
    
    phrases = [
        {"jp": "こんにちは", "reading": "Konnichiwa", "meaning": "你好 (Hello)"},
        {"jp": "ありがとう", "reading": "Arigatou", "meaning": "謝謝 (Thank you)"},
        {"jp": "さようなら", "reading": "Sayounara", "meaning": "再見 (Goodbye)"},
        {"jp": "おはよう", "reading": "Ohayou", "meaning": "早安 (Good morning)"},
        {"jp": "こんばんは", "reading": "Konbanwa", "meaning": "晚安 (Good evening)"},
        {"jp": "すみません", "reading": "Sumimasen", "meaning": "不好意思 (Excuse me)"},
        {"jp": "お元気ですか", "reading": "Ogenki desu ka", "meaning": "你好嗎? (How are you?)"},
        {"jp": "いただきます", "reading": "Itadakimasu", "meaning": "我要開動了 (Let's eat)"},
    ]
    
    if st.button("Open the Door! 🚪", use_container_width=True):
        phrase = random.choice(phrases)
        st.success(f"**{phrase['jp']}**")
        st.info(f"Reading: {phrase['reading']}")
        st.warning(f"Meaning: {phrase['meaning']}")
    else:
        st.info("Click the button to learn a new phrase!")

def show_memory_bread():
    st.header("Memory Bread (記憶麵包) 🍞")
    
    # Input Form
    with st.form("vocab_form", clear_on_submit=True):
        col1, col2, col3 = st.columns(3)
        with col1:
            word = st.text_input("Word (日文)")
        with col2:
            reading = st.text_input("Reading (讀音)")
        with col3:
            meaning = st.text_input("Meaning (意思)")
            
        submitted = st.form_submit_button("Eat Bread! (Add Word)")
        
        if submitted and word and meaning:
            st.session_state['vocab_list'].append({
                "Word": word,
                "Reading": reading,
                "Meaning": meaning
            })
            st.success(f"Added: {word}")
        elif submitted:
            st.error("Please fill in at least Word and Meaning!")

    # Display List
    if st.session_state['vocab_list']:
        st.subheader("Your Vocabulary List")
        df = pd.DataFrame(st.session_state['vocab_list'])
        edited_df = st.data_editor(df, num_rows="dynamic", use_container_width=True)
        
        # Update session state if edited (optional, but good for UX)
        # Note: st.data_editor returns the edited dataframe. 
        # Syncing back to list is a bit complex with simple lists, 
        # so for this simple app, we might just display it or use the return value if needed later.
        # For now, let's just display. To make it truly editable and persistent in session, 
        # we'd need to convert df back to list.
        
        if not df.equals(edited_df):
             st.session_state['vocab_list'] = edited_df.to_dict('records')
    else:
        st.info("No words yet. Eat some bread to remember words!")

def show_quiz_mode():
    st.header("Quiz Mode 🎯")
    
    if not st.session_state['vocab_list']:
        st.warning("You haven't eaten any Memory Bread yet! Go add some words first.")
        return

    if 'current_quiz' not in st.session_state:
        st.session_state['current_quiz'] = random.choice(st.session_state['vocab_list'])
        st.session_state['quiz_revealed'] = False

    quiz = st.session_state['current_quiz']
    
    st.markdown(f"### What is the meaning of: **{quiz['Word']}**?")
    
    if st.session_state['quiz_revealed']:
        st.info(f"Reading: {quiz['Reading']}")
        st.success(f"Meaning: {quiz['Meaning']}")
        
        if st.button("Next Question ➡️"):
            st.session_state['current_quiz'] = random.choice(st.session_state['vocab_list'])
            st.session_state['quiz_revealed'] = False
            st.rerun()
    else:
        if st.button("Reveal Answer 👁️"):
            st.session_state['quiz_revealed'] = True
            st.rerun()

if __name__ == "__main__":
    main()
