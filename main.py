# main.py
# This is a Streamlit application for a progressive, ER-focused diagnostic tool.

import streamlit as st
from er_symptoms import ER_PRESENTATIONS
# The file er_treatments.py is assumed to be in the same directory.
# If you don't have it, you can create a placeholder file to prevent errors.
# For example:
#
# # er_treatments.py
# ER_TREATMENTS = {}
#
# import er_treatments 
#
# or simply remove the import and the section that uses it.
#from er_treatments import ER_TREATMENTS

def initialize_session_state():
    """Initializes session state variables if they don't exist."""
    if "step" not in st.session_state:
        st.session_state.step = "start"
    if "chief_complaint" not in st.session_state:
        st.session_state.chief_complaint = None
    if "answers" not in st.session_state:
        st.session_state.answers = {}
    if "diagnosis" not in st.session_state:
        st.session_state.diagnosis = None

def reset_app():
    """Resets the application to the initial state."""
    st.session_state.step = "start"
    st.st.session_state.chief_complaint = None
    st.session_state.answers = {}
    st.session_state.diagnosis = None

def get_next_question(presentation, answers):
    """
    Determines the next question to ask based on the current answers.
    Returns the question key and a list of options.
    """
    for question_key in ER_PRESENTATIONS[presentation]["questions"]:
        if question_key not in answers:
            return question_key, ER_PRESENTATIONS[presentation]["questions"][question_key]
    return None, None

def match_diagnosis(presentation, answers):
    """
    Matches the user's answers to a possible diagnosis based on the ER_PRESENTATIONS data.
    """
    diagnoses = ER_PRESENTATIONS[presentation]["diagnoses"]
    for diagnosis in diagnoses:
        match_criteria = diagnosis["match"]
        is_match = True
        for key, value in match_criteria.items():
            user_answer = answers.get(key)
            if isinstance(value, list):
                if user_answer not in value:
                    is_match = False
                    break
            else:
                if user_answer != value:
                    is_match = False
                    break
        if is_match:
            return diagnosis
    return None

def main():
    initialize_session_state()

    st.set_page_config(
        page_title="ER Diagnostic Tree",
        page_icon="🏥",
        layout="centered",
    )

    st.title("🏥 ER Diagnostic Tree")
    st.markdown("A progressive tool to practice differential diagnosis for common ER presentations.")
    
    if st.session_state.step == "start":
        st.subheader("Select a Chief Complaint")
        complaints = list(ER_PRESENTATIONS.keys())
        
        # Split the complaints into two columns for better display
        cols = st.columns(2)
        for i, complaint in enumerate(complaints):
            with cols[i % 2]:
                if st.button(complaint, use_container_width=True, key=f"btn_{i}"):
                    st.session_state.chief_complaint = complaint
                    st.session_state.step = "questions"
                    st.experimental_rerun()

    elif st.session_state.step == "questions":
        presentation = st.session_state.chief_complaint
        st.subheader(f"Chief Complaint: {presentation}")
        
        question_key, options = get_next_question(presentation, st.session_state.answers)
        
        if question_key:
            # Dynamically display the question based on the key
            question_text = f"**Question:** What is the {question_key}?"
            # Special case for "type" as it can be ambiguous
            if question_key == "type":
                 question_text = "**Question:** What is the type of the symptom?"
            # Special case for "associated_symptoms"
            elif question_key == "associated_symptoms":
                question_text = "**Question:** What are the associated symptoms?"
            
            st.markdown(question_text)
            
            # Create buttons for each option
            cols = st.columns(len(options))
            for i, option in enumerate(options):
                with cols[i]:
                    if st.button(option, key=f"{question_key}_{option}"):
                        st.session_state.answers[question_key] = option
                        st.experimental_rerun()
        else:
            # All questions have been answered, now find the diagnosis
            st.session_state.diagnosis = match_diagnosis(presentation, st.session_state.answers)
            st.session_state.step = "results"
            st.experimental_rerun()

    elif st.session_state.step == "results":
        st.subheader("Your Analysis")
        st.markdown(f"**Chief Complaint:** {st.session_state.chief_complaint}")
        st.markdown("**Your Findings:**")
        for key, value in st.session_state.answers.items():
            st.markdown(f"- {key.capitalize()}: {value}")
        
        st.markdown("---")
        
        diagnosis = st.session_state.diagnosis
        if diagnosis:
            st.success(f"**Most Probable Diagnosis:** {diagnosis['name']}")
            st.info(f"**Differentiating Factors:** {diagnosis['differentiating_factors']}")
            
            # This part assumes er_treatments.py exists
            try:
                if diagnosis['name'] in ER_TREATMENTS:
                    treatment_data = ER_TREATMENTS[diagnosis['name']]
                    st.markdown("#### **Initial Management (ER)**")
                    st.markdown("**First-Line Therapy:**")
                    for item in treatment_data['first_line']:
                        st.markdown(f"- {item}")
                    st.markdown("**Supportive Care:**")
                    for item in treatment_data['supportive_care']:
                        st.markdown(f"- {item}")
                else:
                    st.warning("Treatment protocol not found for this diagnosis.")
            except NameError:
                st.warning("Could not find `er_treatments.py`. Please make sure the file exists and is in the same directory.")
        else:
            st.warning("Could not match a specific diagnosis with these findings.")
        
        st.markdown("---")
        st.button("Start Over", on_click=reset_app)

if __name__ == "__main__":
    main()
