import streamlit as st

# Page config
st.set_page_config(page_title="Philosophy Quiz - Personal Identity", page_icon="🧠", layout="wide")

# Initialize session state
if 'answers' not in st.session_state:
    st.session_state.answers = {}
if 'submitted' not in st.session_state:
    st.session_state.submitted = False

# Questions data
questions = [
    {
        "id": 1,
        "question": "According to Plato's theory of Forms, what are the visible objects in our world?",
        "options": [
            "Perfect examples of ideal Forms",
            "Imperfect replicas of ideal Forms that exist in another world",
            "The only real things that exist",
            "Mental constructions with no reality"
        ],
        "correct": 1,
        "explanation": "Plato held that physical objects are imperfect replicas of perfect ideal Forms that exist in a separate, unchanging world knowable only by the mind."
    },
    {
        "id": 2,
        "question": "What is the relationship between the soul and body according to Plato in the Phaedo?",
        "options": [
            "They are equal partners working together",
            "The pure soul should rule over the impure body",
            "The body should control the soul",
            "They are identical and inseparable"
        ],
        "correct": 1,
        "explanation": "Plato argues the 'pure' soul should rule over the 'impure' body, turning away from bodily desires and wild passions."
    },
    {
        "id": 3,
        "question": "According to Plato, what happens to a soul that becomes 'polluted' by bodily desires?",
        "options": [
            "It becomes stronger and wiser",
            "It is dragged down to the visible world and wanders after death",
            "It immediately ceases to exist",
            "It gains immortality"
        ],
        "correct": 1,
        "explanation": "Plato argues that a soul polluted by bodily desires becomes heavy and is dragged down to wander among tombs and sepulchers after death."
    },
    {
        "id": 4,
        "question": "How did Aristotle's view of Forms differ from Plato's?",
        "options": [
            "Aristotle rejected the existence of Forms entirely",
            "Aristotle believed Forms exist in the visible things themselves, not in a separate world",
            "Aristotle thought Forms were created by God",
            "Aristotle agreed completely with Plato"
        ],
        "correct": 1,
        "explanation": "Unlike Plato, Aristotle believed forms exist in the visible things themselves rather than in a separate world. Forms are real because objects in our visible world embody these forms."
    },
    {
        "id": 5,
        "question": "According to Aristotle, what is the 'highest end' that humans seek?",
        "options": [
            "Pleasure and wealth",
            "Fame and recognition",
            "Happiness achieved through virtue and reason",
            "Knowledge of the Forms in another world"
        ],
        "correct": 2,
        "explanation": "Aristotle argued that happiness is our ultimate end and is achieved by living according to virtue, which means carrying out the activities of reason with excellence."
    },
    {
        "id": 6,
        "question": "What is the key to overcoming political strife according to Confucius?",
        "options": [
            "Strict laws and harsh punishments",
            "Military force and control",
            "Virtue in both rulers and citizens",
            "Economic prosperity alone"
        ],
        "correct": 2,
        "explanation": "Confucius held that virtue should be the primary concern of individuals and the basis of political authority. When rulers and citizens behave virtuously, political strife ends."
    },
    {
        "id": 7,
        "question": "According to Confucius, what is 'li' (the rules of propriety)?",
        "options": [
            "Universal laws that apply equally to all people",
            "Specific moral customs that provide concrete guidance for behavior in one's society",
            "Religious commandments from heaven",
            "Personal preferences about behavior"
        ],
        "correct": 1,
        "explanation": "Li refers to the rules of propriety or moral customs of one's society, which provide specific and concrete guidance for proper behavior in various situations."
    },
    {
        "id": 8,
        "question": "What basic assumption do most people make about personal identity according to the text?",
        "options": [
            "That we are constantly changing into different people",
            "That we remain the same person from day to day throughout our lives",
            "That personal identity doesn't matter",
            "That only our bodies define who we are"
        ],
        "correct": 1,
        "explanation": "Most people assume they remain the same person throughout their lives, which is why promises, relationships, and life projects make sense."
    },
    {
        "id": 9,
        "question": "According to the Traditional Western view, what makes a person remain the same over time?",
        "options": [
            "The continuity of the physical body",
            "Memory of past experiences",
            "An immaterial soul or mind",
            "Social recognition by others"
        ],
        "correct": 2,
        "explanation": "The Traditional view holds that an immaterial soul or mind makes a person remain the same person as the body changes over time."
    },
    {
        "id": 10,
        "question": "What was Descartes' famous conclusion on November 10, 1619?",
        "options": [
            "God exists and controls everything",
            "The body and mind are one substance",
            "I think, therefore I am",
            "All knowledge comes from the senses"
        ],
        "correct": 2,
        "explanation": "Descartes concluded 'I think, therefore I am' was so certain and assured that even the most extravagant suppositions of skeptics were incapable of shaking it."
    },
    {
        "id": 11,
        "question": "According to Descartes, can you conceive of yourself without a body?",
        "options": [
            "No, it's impossible to imagine",
            "Yes, but you cannot conceive of yourself without a thinking mind",
            "Only in dreams can this be conceived",
            "Only after death is this possible"
        ],
        "correct": 1,
        "explanation": "Descartes argues he can conceive of himself without a body, but cannot conceive of himself without a thinking mind. Therefore, he is essentially a thinking mind, not a body."
    },
    {
        "id": 12,
        "question": "What crucial assumption does Descartes make about conceivability?",
        "options": [
            "If you can conceive of one thing without another, they must be different",
            "Conceiving something makes it physically real",
            "What you cannot conceive doesn't exist",
            "Conceivability has no relationship to reality"
        ],
        "correct": 0,
        "explanation": "Descartes assumes that if we can conceive of one thing without the other, then those two things are different; if we can't, then one must be an essential part of the other."
    },
    {
        "id": 13,
        "question": "What is the main objection to Descartes' view about the continuity of the mind?",
        "options": [
            "The mind doesn't exist at all",
            "We cannot observe our own minds to verify they remain the same over time",
            "The mind is identical to the brain",
            "Everyone's mind is actually the same"
        ],
        "correct": 1,
        "explanation": "Critics point out that we cannot observe our own minds or souls to verify they remain the same over time, which seems necessary to know we are the same person."
    },
    {
        "id": 14,
        "question": "According to John Locke, what makes a person the same over time?",
        "options": [
            "The immaterial soul",
            "The physical body",
            "Memory or consciousness of being that earlier person",
            "Social relationships with others"
        ],
        "correct": 2,
        "explanation": "Locke argues that what makes me the same person I was earlier is my memory or consciousness of being that earlier person, not the soul or body."
    },
    {
        "id": 15,
        "question": "In Locke's view, if someone has no memory of being a person from the past, what follows?",
        "options": [
            "They are still the same person due to their soul",
            "They are not the same person as that earlier person",
            "Memory is irrelevant to identity",
            "They must have the same body to be the same person"
        ],
        "correct": 1,
        "explanation": "Locke concludes that if someone has no memory or consciousness of being an earlier person, they are not the same person, even if they have the same soul or body."
    },
    {
        "id": 16,
        "question": "What problem does Thomas Reid identify with Locke's memory theory?",
        "options": [
            "Memory is too reliable",
            "Locke's view produces contradictions about identity",
            "Memory never changes over time",
            "Consciousness is not important"
        ],
        "correct": 1,
        "explanation": "Reid showed that Locke's view produces contradictions. If a 30-year-old remembers being 20, and the 20-year-old remembered being 10, but the 30-year-old doesn't remember being 10, then contradictory conclusions follow."
    },
    {
        "id": 17,
        "question": "According to Buddhist philosophy, what is the self?",
        "options": [
            "An eternal, unchanging soul",
            "A fleeting, momentary composite that dissolves and changes constantly",
            "Identical to the physical body",
            "A creation of society"
        ],
        "correct": 1,
        "explanation": "Buddhism holds that the self is a fleeting momentary composite of constantly changing elements. There is no enduring self that continues through time."
    },
    {
        "id": 18,
        "question": "What is the Buddha's argument about control and the self?",
        "options": [
            "If we could control the body or mind, we could prevent aging and suffering, so neither can be the self",
            "The self exists because we can control our thoughts",
            "Control is irrelevant to questions about the self",
            "Only the body can be controlled, so it is the self"
        ],
        "correct": 0,
        "explanation": "The Buddha argues that if the body or mind were the self, we could control them to prevent aging and suffering. Since we cannot, neither the body nor mind can be the self."
    },
    {
        "id": 19,
        "question": "According to Buddhist teaching, what is the cause of human suffering?",
        "options": [
            "Physical pain and disease",
            "Lack of wealth and power",
            "Clinging to things (including the idea of self) when nothing is permanent",
            "Evil actions by others"
        ],
        "correct": 2,
        "explanation": "Buddhism teaches that suffering comes from clinging to things we want, including our self and those we love, when nothing is permanent. The illusion of self is the source of suffering."
    },
    {
        "id": 20,
        "question": "What is David Hume's view about the self?",
        "options": [
            "The self is an immortal soul",
            "The self is identical to the physical body",
            "There is no enduring self, only a bundle of changing perceptions",
            "The self is created by God"
        ],
        "correct": 2,
        "explanation": "Hume argues we are nothing but a bundle of constantly changing perceptions. There is no enduring unified self—it is a fiction philosophers have created."
    },
    {
        "id": 21,
        "question": "According to Hume, why do we have no knowledge of the self?",
        "options": [
            "The self is too complex to understand",
            "We never perceive an enduring thing we can call the self, only changing perceptions",
            "The self exists but is invisible",
            "Science hasn't discovered the self yet"
        ],
        "correct": 1,
        "explanation": "Hume argues that genuine knowledge depends on experience. Since we never experience a permanent, enduring self (only changing perceptions), we have no real knowledge of a self."
    },
    {
        "id": 22,
        "question": "What similarity exists between Hume's and Buddhist views on the self?",
        "options": [
            "Both believe in an eternal soul",
            "Both argue that experience shows constant change without permanence, so there is no enduring self",
            "Both think the body is the self",
            "Both believe the self is created by society"
        ],
        "correct": 1,
        "explanation": "Both Hume and Buddhism argue that our experience is one of constant change without permanence. Therefore, there can be no continuous enduring self."
    },
    {
        "id": 23,
        "question": "According to Hegel, how do we become free and independent?",
        "options": [
            "By isolating ourselves from others",
            "Through recognition from others who see us as free and independent",
            "By accumulating wealth and power",
            "Through meditation and inner reflection alone"
        ],
        "correct": 1,
        "explanation": "Hegel argues we become free and independent only when others recognize us as such. We need others to acknowledge our freedom to truly be free."
    },
    {
        "id": 24,
        "question": "What does Hegel's master-servant dialectic illustrate?",
        "options": [
            "Masters are truly free while servants are not",
            "Both master and servant become dependent on each other in their struggle for recognition",
            "Freedom comes from dominating others",
            "Independence requires no relationship with others"
        ],
        "correct": 1,
        "explanation": "Hegel shows that the independent master becomes dependent on the servant's skills, while the servant, through work, develops independence. Each needs the other's recognition."
    },
    {
        "id": 25,
        "question": "According to Charles Taylor, how is our identity formed?",
        "options": [
            "Through our genes and biology alone",
            "By our own independent choices without influence",
            "Through dialogue and recognition from others, including our culture",
            "Randomly without any pattern"
        ],
        "correct": 2,
        "explanation": "Taylor argues our identity is shaped by recognition from others. We learn languages of expression and define ourselves through interaction with others who matter to us."
    },
    {
        "id": 26,
        "question": "What does Taylor mean by saying identity is formed 'dialogically'?",
        "options": [
            "Identity comes from internal dialogue with ourselves",
            "We define ourselves through exchanges and interactions with others",
            "Identity is formed through reading dialogues in books",
            "Dialogue has no role in identity formation"
        ],
        "correct": 1,
        "explanation": "Taylor argues we become full human agents through dialogue with others. We are introduced to languages of expression through interaction with others who matter to us."
    },
    {
        "id": 27,
        "question": "According to Hegel and Taylor, can subordinate social classes be created through misrecognition?",
        "options": [
            "No, social classes are biologically determined",
            "Yes, when groups internalize inferior images that others project onto them",
            "Social classes don't exist",
            "Only economic factors create social classes"
        ],
        "correct": 1,
        "explanation": "Both argue that misrecognition can create subordinate classes when groups internalize demeaning images projected onto them by dominant groups."
    },
    {
        "id": 28,
        "question": "How does Taylor's view of self-identity relate to culture?",
        "options": [
            "Culture has no influence on identity",
            "Culture determines everything about identity",
            "A person's culture provides the language, symbols, and ideas through which they understand themselves",
            "Only Western culture shapes identity"
        ],
        "correct": 2,
        "explanation": "Taylor argues that culture provides the traditions, symbols, language, and ideas through which society shows a person who they are and can be."
    },
    {
        "id": 29,
        "question": "What does the 'atomistic view of the self' claim?",
        "options": [
            "The self is made of atoms",
            "The self is self-contained and independent of others, like an atom",
            "The self doesn't exist",
            "The self is constantly splitting apart"
        ],
        "correct": 1,
        "explanation": "The atomistic view holds that the self is like an atom—self-contained and independent of other atoms. The real core of self can rise above and remain independent."
    },
    {
        "id": 30,
        "question": "According to the text, which qualities might NOT depend on relationships with others?",
        "options": [
            "All qualities depend on others",
            "Basic physical qualities like height, weight, and some personality traits",
            "One's name and language",
            "One's cultural identity"
        ],
        "correct": 1,
        "explanation": "The text suggests basic physical qualities and possibly some personality traits may not depend on relationships with others, though abilities to feel, think, and choose might."
    }
]

# Header
st.title("🧠 Philosophy Quiz: Personal Identity & the Self")
st.markdown("**By Xavier Honablue M.Ed for CognitiveCloud.ai**")

# Resources Section
with st.expander("📚 Additional Resources"):
    st.markdown("""
    ### External Philosophy Resources
    
    For deeper exploration of the topics covered in this quiz, visit:
    
    - **[Stanford Encyclopedia of Philosophy](https://plato.stanford.edu/)** - Comprehensive, peer-reviewed articles on philosophy topics
    - [Plato](https://plato.stanford.edu/entries/plato/)
    - [Aristotle](https://plato.stanford.edu/entries/aristotle/)
    - [Personal Identity](https://plato.stanford.edu/entries/identity-personal/)
    - [Descartes](https://plato.stanford.edu/entries/descartes/)
    - [John Locke](https://plato.stanford.edu/entries/locke/)
    - [David Hume](https://plato.stanford.edu/entries/hume/)
    
    *Links open in a new tab and won't affect your quiz progress*
    """, unsafe_allow_html=True)

st.info("📋 **Instructions:** Answer all questions before submitting. You can review explanations after completing the entire quiz.")

# Display questions
if not st.session_state.submitted:
    st.markdown("---")
    
    for idx, q in enumerate(questions):
        st.markdown(f"### Question {idx + 1}")
        st.write(q["question"])
        
        answer = st.radio(
            "Select your answer:",
            options=range(len(q["options"])),
            format_func=lambda x: q["options"][x],
            key=f"q_{q['id']}",
            index=st.session_state.answers.get(q['id'], None)
        )
        
        st.session_state.answers[q['id']] = answer
        st.markdown("---")
    
    # Progress tracking
    answered = len([a for a in st.session_state.answers.values() if a is not None])
    st.progress(answered / len(questions))
    st.write(f"Questions answered: {answered} / {len(questions)}")
    
    # Submit button
    if answered == len(questions):
        if st.button("Submit Quiz", type="primary", use_container_width=True):
            st.session_state.submitted = True
            st.rerun()
    else:
        st.warning("Please answer all questions before submitting.")

# Results page
else:
    # Calculate score
    score = sum(1 for q in questions if st.session_state.answers.get(q['id']) == q['correct'])
    percentage = round((score / len(questions)) * 100)
    
    # Display score
    st.success(f"## 🎯 Quiz Results: {score} / {len(questions)} ({percentage}%)")
    
    # Show answers with explanations
    st.markdown("---")
    st.markdown("## 📝 Answer Review")
    
    for idx, q in enumerate(questions):
        user_answer = st.session_state.answers.get(q['id'])
        is_correct = user_answer == q['correct']
        
        if is_correct:
            st.success(f"### ✅ Question {idx + 1}")
        else:
            st.error(f"### ❌ Question {idx + 1}")
        
        st.write(f"**{q['question']}**")
        
        st.write(f"**Your answer:** {q['options'][user_answer]}")
        
        if not is_correct:
            st.write(f"**Correct answer:** {q['options'][q['correct']]}")
        
        st.info(f"**Explanation:** {q['explanation']}")
        st.markdown("---")
    
    # Retake button
    if st.button("🔄 Retake Quiz", type="primary", use_container_width=True):
        st.session_state.answers = {}
        st.session_state.submitted = False
        st.rerun()
