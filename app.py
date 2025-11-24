import streamlit as st
import pandas as pd
import random

# --- CONFIGURATION ---
st.set_page_config(
    page_title="多拉A夢日語百寶袋",
    page_icon="🔔",
    layout="centered",
    initial_sidebar_state="collapsed"
)

# --- THEME & CSS (Doraemon Style) ---
# Blue: #0096E1, Red: #D80F28, Bell Gold: #F4D03F
doraemon_css = """
<style>
    .stApp {
        background-color: #E0F7FA;
    }
    h1, h2, h3 {
        color: #0096E1;
        font-family: 'Gen Jyuu Gothic', sans-serif;
    }
    .stButton>button {
        background-color: #0096E1;
        color: white;
        border-radius: 20px;
        border: 2px solid #0078B5;
    }
    .stButton>button:hover {
        background-color: #D80F28;
        border-color: #B00C20;
    }
    .css-1d391kg {
        background-color: #FFFFFF;
        border-radius: 15px;
        padding: 20px;
        box-shadow: 0 4px 6px rgba(0,0,0,0.1);
    }
    .metric-card {
        background-color: white;
        padding: 10px;
        border-radius: 10px;
        border-left: 5px solid #D80F28;
    }
</style>
"""
st.markdown(doraemon_css, unsafe_allow_html=True)

# --- INITIALIZE DATA (SESSION STATE) ---
if 'vocab_df' not in st.session_state:
    # Initial Seed Data
    data = {
        '日文': ['猫', '銅鑼焼き', '竹蜻蜓', '任意門'],
        '假名': ['ねこ', 'どらやき', 'たけこぷたー', 'どこでもどあ'],
        '中文': ['貓', '銅鑼燒', '竹蜻蜓', '任意門']
    }
    st.session_state.vocab_df = pd.DataFrame(data)

# --- HELPER FUNCTIONS ---
def get_hiragana_chart():
    # Simplified rows for demo
    return pd.DataFrame([
        ['あ (a)', 'い (i)', 'う (u)', 'え (e)', 'お (o)'],
        ['か (ka)', 'き (ki)', 'く (ku)', 'け (ke)', 'こ (ko)'],
        ['さ (sa)', 'し (shi)', 'す (su)', 'せ (se)', 'そ (so)'],
        ['た (ta)', 'ち (chi)', 'つ (tsu)', 'て (te)', 'と (to)'],
        ['な (na)', 'に (ni)', 'ぬ (nu)', 'ね (ne)', 'の (no)'],
    ])

def get_katakana_chart():
    return pd.DataFrame([
        ['ア (a)', 'イ (i)', 'ウ (u)', 'エ (e)', 'オ (o)'],
        ['カ (ka)', 'キ (ki)', 'ク (ku)', 'ケ (ke)', 'コ (ko)'],
        ['サ (sa)', 'シ (shi)', 'ス (su)', 'セ (se)', 'ソ (so)'],
    ])

# --- SIDEBAR NAVIGATION ---
st.sidebar.image("https://upload.wikimedia.org/wikipedia/en/c/c8/Doraemon_volume_1_cover.jpg", width=100)
st.sidebar.title("🔔 百寶袋選單")
menu = st.sidebar.radio(
    "選擇道具 functionality:",
    ["🏠 主頁面", "📓 五十音記憶吐司", "🚪 每日一句任意門", "🍞 單字記憶吐司 (Input)"]
)

# --- PAGE LOGIC ---

if menu == "🏠 主頁面":
    st.title("🔔 多拉A夢日語百寶袋")
    st.markdown("### 歡迎來到 Antigravity 日語教室！")
    st.markdown("這是一個專門為了幫助你記憶日語而開發的應用程式。請從左側選單選擇你要使用的道具。")
    
    col1, col2 = st.columns(2)
    with col1:
        st.info(f"📚 目前累積單字: {len(st.session_state.vocab_df)} 個")
    with col2:
        st.success("⚡ 學習狀態: 充滿活力")
        
    st.image("https://i.imgur.com/3v1R5tZ.png", caption="一起努力學習吧！", use_column_width=True)

elif menu == "📓 五十音記憶吐司":
    st.title("📓 五十音圖表")
    tab1, tab2 = st.tabs(["平假名 (Hiragana)", "片假名 (Katakana)"])
    
    with tab1:
        st.table(get_hiragana_chart())
    with tab2:
        st.table(get_katakana_chart())

elif menu == "🚪 每日一句任意門":
    st.title("🚪 任意門：每日短句")
    
    phrases = [
        {"jp": "こんにちは", "reading": "Konnichiwa", "cn": "你好"},
        {"jp": "ありがとう", "reading": "Arigatou", "cn": "謝謝"},
        {"jp": "頑張って！", "reading": "Ganbatte", "cn": "加油！"},
        {"jp": "お腹すいた", "reading": "Onaka suita", "cn": "肚子餓了"},
        {"jp": "何をしているの？", "reading": "Nani o shite iru no?", "cn": "你在做什麼？"}
    ]
    
    if st.button("✨ 打開任意門 (隨機抽取)"):
        phrase = random.choice(phrases)
        st.markdown("---")
        st.header(phrase['jp'])
        st.subheader(phrase['reading'])
        st.info(f"中文意思: {phrase['cn']}")
        st.balloons()

elif menu == "🍞 單字記憶吐司 (Input)":
    st.title("🍞 記憶吐司：單字庫")
    st.markdown("在這裡吃下（輸入）新的單字，才不會忘記喔！")

    # Input Form
    with st.form("vocab_form", clear_on_submit=True):
        col1, col2, col3 = st.columns(3)
        new_jp = col1.text_input("日文 (例如: 猫)")
        new_kana = col2.text_input("假名 (例如: ねこ)")
        new_cn = col3.text_input("中文 (例如: 貓)")
        
        submitted = st.form_submit_button("📥 印在吐司上 (儲存)")
        
        if submitted and new_jp and new_cn:
            new_entry = pd.DataFrame([{'日文': new_jp, '假名': new_kana, '中文': new_cn}])
            st.session_state.vocab_df = pd.concat([st.session_state.vocab_df, new_entry], ignore_index=True)
            st.success(f"成功儲存單字: {new_jp}")

    st.markdown("---")
    st.subheader("📖 你的單字筆記本")
    
    # Display Dataframe
    st.dataframe(st.session_state.vocab_df, use_container_width=True)
    
    # Simple Quiz Mechanism
    st.markdown("---")
    st.subheader("🧠 隨堂小考")
    if not st.session_state.vocab_df.empty:
        if st.button("❓ 抽考一個單字"):
            target = st.session_state.vocab_df.sample(1).iloc[0]
            st.write(f"請問 **{target['中文']}** 的日文是什麼？")
            with st.expander("點擊查看答案"):
                st.write(f"**{target['日文']}** ({target['假名']})")
