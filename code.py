import streamlit as st
import json
import re

# -------------------------------------------------
# Page Configuration
# -------------------------------------------------

st.set_page_config(
    page_title="AI Flashcard Generator",
    page_icon="🧠",
    layout="wide"
)

# -------------------------------------------------
# Title
# -------------------------------------------------

st.title("🧠 AI Flashcard Generator")
st.write(
    "Generate flashcards from your study material "
    "and test your knowledge."
)

st.divider()

# -------------------------------------------------
# Sidebar
# -------------------------------------------------

with st.sidebar:
    st.header("⚙️ Flashcard Settings")

    number_of_cards = st.slider(
        "Number of flashcards",
        min_value=5,
        max_value=30,
        value=10
    )

    difficulty = st.selectbox(
        "Difficulty",
        ["Easy", "Medium", "Hard"]
    )

# -------------------------------------------------
# Study Material
# -------------------------------------------------

st.subheader("📚 Study Material")

text = st.text_area(
    "Paste your study material below:",
    height=300,
    placeholder=(
        "Example:\n\n"
        "Machine learning is a branch of artificial intelligence "
        "that allows computers to learn from data..."
    )
)

# -------------------------------------------------
# Generate Flashcards
# -------------------------------------------------

if st.button("✨ Generate Flashcards", use_container_width=True):

    if not text.strip():
        st.warning("⚠️ Please enter some study material first.")
        st.stop()

    # Split text into sentences
    sentences = re.split(r"(?<=[.!?])\s+", text.strip())

    # Remove very short sentences
    sentences = [
        sentence.strip()
        for sentence in sentences
        if len(sentence.split()) >= 5
    ]

    if not sentences:
        st.error(
            "❌ Not enough content to generate flashcards."
        )
        st.stop()

    cards = []

    for index, sentence in enumerate(
        sentences[:number_of_cards],
        start=1
    ):

        card = {
            "id": index,
            "question": "What is the main idea of this statement?",
            "answer": sentence,
            "difficulty": difficulty
        }

        cards.append(card)

    # -------------------------------------------------
    # Success Message
    # -------------------------------------------------

    st.success(
        f"✅ Generated {len(cards)} flashcards!"
    )

    st.divider()

    # -------------------------------------------------
    # Display Flashcards
    # -------------------------------------------------

    st.subheader("🃏 Your Flashcards")

    for card in cards:

        with st.expander(
            f"Flashcard {card['id']} — "
            f"{card['difficulty']}"
        ):

            st.markdown("### ❓ Question")

            st.write(card["question"])

            st.markdown("### ✅ Answer")

            st.write(card["answer"])

    # -------------------------------------------------
    # Download Flashcards
    # -------------------------------------------------

    st.divider()

    json_data = json.dumps(
        cards,
        indent=4,
        ensure_ascii=False
    )

    st.download_button(
        label="📥 Download Flashcards",
        data=json_data,
        file_name="flashcards.json",
        mime="application/json"
    )

# -------------------------------------------------
# Footer
# -------------------------------------------------

st.divider()

st.caption(
    "AI Flashcard Generator | Python + Streamlit"
)