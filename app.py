import streamlit as st
import random
import datetime

# Custom CSS for Styling
st.markdown("""
    <style>
        body {font-family: 'Arial', sans-serif;}
        .main-title {color: #ff5733; text-align: center; font-size: 3em; margin-bottom: 20px;}
        .subheader {color: #2a9d8f; font-size: 1.5em; margin-bottom: 15px;}
        .goal-box, .quote-box, .challenge-box {
            padding: 15px; 
            border-radius: 12px; 
            margin-bottom: 20px;
            box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
        }
        .goal-box {background: #d4edda; border-left: 6px solid #28a745;}
        .quote-box {background: #fff3cd; border-left: 6px solid #ff9f43; font-size: 20px; font-style: italic;}
        .challenge-box {background: #f8d7da; border-left: 6px solid #dc3545;}
        .footer {text-align: center; margin-top: 40px; font-weight: bold; color: #555;}
    </style>
""", unsafe_allow_html=True)

# Helper Functions

def get_random_quote():
    quotes = [
        "Success is not final, failure is not fatal.",
        "Your only limit is your mind.",
        "Mistakes are proof that you are trying.",
        "Fall seven times, stand up eight.",
        "Great things never come from comfort zones."
    ]
    return random.choice(quotes)


def get_daily_challenge():
    challenges = [
        "Write down 3 things you learned today.",
        "Step outside your comfort zone and try something new.",
        "Help someone who is struggling.",
        "Read for 15 minutes about personal growth.",
        "Practice gratitude by listing 5 things you are grateful for."
    ]
    return random.choice(challenges)

# Title
st.markdown('<h1 class="main-title">🚀 Growth Mindset Tracker</h1>', unsafe_allow_html=True)
st.markdown('<h3 class="subheader">Empower yourself to achieve consistent growth!</h3>', unsafe_allow_html=True)

# Sidebar for Goal Input
st.sidebar.header("🌱 Set Your Growth Goal")
name = st.sidebar.text_input("Your Name:")
goal = st.sidebar.text_input("Your Growth Goal:")

if st.sidebar.button("✅ Submit Goal"):
    if name and goal:
        if "goals" not in st.session_state:
            st.session_state.goals = []
        st.session_state.goals.append({"name": name, "goal": goal, "completed": False})
        st.sidebar.success("🎯 Goal added successfully!")
    else:
        st.sidebar.error("Please enter both your name and goal.")

# Display Goals with Progress
st.markdown('<h2 class="subheader">🎯 Your Goals</h2>', unsafe_allow_html=True)
if "goals" in st.session_state and st.session_state.goals:
    for i, g in enumerate(st.session_state.goals):
        completed = st.checkbox(f"{g['name']}: {g['goal']}", g['completed'], key=f'goal_{i}')
        st.session_state.goals[i]['completed'] = completed
else:
    st.info("No goals set yet. Add your goals from the sidebar!")

# Motivational Quote
st.markdown('<h2 class="subheader">💡 Daily Motivation</h2>', unsafe_allow_html=True)
if "quote" not in st.session_state:
    st.session_state.quote = get_random_quote()
st.markdown(f'<div class="quote-box">{st.session_state.quote}</div>', unsafe_allow_html=True)
if st.button("🔄 Get New Quote"):
    st.session_state.quote = get_random_quote()
    st.experimental_rerun()

# Daily Challenge
st.markdown('<h2 class="subheader">🔥 Daily Challenge</h2>', unsafe_allow_html=True)
if "challenge" not in st.session_state or st.session_state.challenge_date != datetime.date.today():
    st.session_state.challenge = get_daily_challenge()
    st.session_state.challenge_date = datetime.date.today()
st.markdown(f'<div class="challenge-box">{st.session_state.challenge}</div>', unsafe_allow_html=True)

# Reflection Section
st.markdown('<h2 class="subheader">📝 Daily Reflection</h2>', unsafe_allow_html=True)
reflection = st.text_area("Write about your progress today:")
if st.button("💾 Save Reflection"):
    if reflection.strip():
        if "reflections" not in st.session_state:
            st.session_state.reflections = []
        st.session_state.reflections.append(reflection)
        st.success("✅ Reflection saved successfully!")
    else:
        st.warning("⚠️ Please write something before saving!")

# Leaderboard
st.markdown('<h2 class="subheader">🏆 Leaderboard</h2>', unsafe_allow_html=True)
if "goals" in st.session_state:
    completed_goals = [g for g in st.session_state.goals if g['completed']]
    if completed_goals:
        st.markdown("### Top Achievers")
        for g in completed_goals:
            st.markdown(f"✅ **{g['name']}** completed: {g['goal']}")
    else:
        st.info("No goals completed yet! Keep pushing forward!")
else:
    st.info("Start by setting your goals to be featured on the leaderboard!")

# Footer
st.markdown('<p class="footer">🚀 Keep Growing, Keep Thriving!</p>', unsafe_allow_html=True)
