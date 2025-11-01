import streamlit as st

# 🎮 Page setup
st.set_page_config(page_title="FLAMES Game", page_icon="🔥", layout="centered")

st.title("🔥 FLAMES Game 🔥")
st.markdown("### Let's find out your relationship compatibility!")

# 🧑‍🤝‍🧑 Input fields
col1, col2 = st.columns(2)
with col1:
    name1 = st.text_input("Enter First Name", placeholder="e.g. John")
with col2:
    name2 = st.text_input("Enter Second Name", placeholder="e.g. Emma")

# ❤️ Function to calculate FLAMES result
def flames_game(name1, name2):
    n = list(name1.lower().replace(" ", ""))
    m = list(name2.lower().replace(" ", ""))

    for char in name1:
        if char in m:
            m.remove(char)
            n.remove(char)

    res = len(n + m)
    s = list("flames")

    while len(s) > 1:
        i = (res % len(s)) - 1
        if i >= 0:
            s = s[i + 1:] + s[:i]
        else:
            s = s[:len(s) - 1]
    return s[0]

# 🔤 Meaning dictionary
flames_dict = {
    'f': '💚 Friendship',
    'l': '❤️ Love',
    'a': '💞 Affection',
    'm': '💍 Marriage',
    'e': '💫 Enemies',
    's': '👫 Siblings'
}

# 🎯 Buttons
col3, col4 = st.columns([1, 1])
with col3:
    submit = st.button("🔮 Check Result")
with col4:
    reset = st.button("🔁 Reset")

# 💡 Result section
if submit:
    if name1.strip() == "" or name2.strip() == "":
        st.warning("⚠️ Please enter both names before submitting.")
    else:
        result = flames_game(name1, name2)
        meaning = flames_dict.get(result, "Unknown")
        st.success(f"🎉 The relationship between **{name1}** and **{name2}** is: {meaning}")

if reset:
    st.experimental_rerun()
