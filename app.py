import streamlit as st

st.set_page_config(page_title="NCLEX/PNLE Review", page_icon="🩺", layout="wide")

# Custom CSS to make it look clean on mobile
st.markdown("""
    <style>
    .stRadio [role=radiogroup]{padding: 20px; background-color: #f0f2f6; border-radius: 10px;}
    .stButton>button {width: 100%; border-radius: 5px; height: 3em; background-color: #007bff; color: white;}
    </style>
    """, unsafe_allow_html=True)

# THE DATA
quiz_data = [
    {"q": "Coughs that are 5 to 10 short, rapid coughs, followed by a rapid inspiration, which causes the hallmark 'whoop' appears in what stage in Pertussis?", "o": ["Catarrhal stage", "Paroxysmal stage", "Convalescent stage", "Performance stage"], "a": "Paroxysmal stage", "r": "The hallmark 'whoop' appears in the Paroxysmal stage."},
    {"q": "A child with Pertussis will be placed at what precaution?", "o": ["Droplet precautions", "Airborne Precaution", "Fomite Precaution", "Vector Precaution"], "a": "Droplet precautions", "r": "Pertussis is transmitted via large respiratory droplets."},
    {"q": "Education on the importance of completing the full course of prescribed antibiotics for streptococcal pharyngitis is necessary to prevent which complication?", "o": ["Epiglottitis", "Dental abscesses", "Rheumatic fever", "Emphysema"], "a": "Rheumatic fever", "r": "Untreated strep can lead to Rheumatic Fever or Glomerulonephritis."},
    {"q": "Which of the following would be appropriate food after a tonsillectomy?", "o": ["Grilled cheese and applesauce", "Lemonade and soft pretzels", "Carrots and dip", "An ice pop and gelatin"], "a": "An ice pop and gelatin", "r": "Soft, cold foods are best. Avoid citrus and red-colored dyes (to not mistake for blood)."},
    {"q": "What is the safest way to assess a 2-year-old's sore throat (croup/epiglottitis suspected)?", "o": ["Use a tongue depressor", "Press down on tongue with finger", "Elicit a gag reflex", "Visually inspect without instruments"], "a": "Visually inspect without instruments", "r": "Using a tongue depressor can trigger laryngospasm/airway obstruction in suspected epiglottitis."},
    {"q": "The most sensitive test for Pertussis in children is:", "o": ["Sputum culture", "Serology test", "Direct fluorescent antibody (DFA)", "Polymerase chain reaction (PCR)"], "a": "Polymerase chain reaction (PCR)", "r": "PCR is currently the most sensitive and rapid test."},
    {"q": "In listening to pediatric heart sounds, which is correct?", "o": ["Use the diaphragm", "Use the bell", "Diaphragm first then bell", "Bell first then diaphragm"], "a": "Diaphragm first then bell", "r": "Standard assessment starts with the diaphragm for high-pitched sounds, then the bell for low-pitched murmurs."},
    {"q": "Which statement about Digoxin requires MORE education?", "o": ["Helps the heart pump better", "I give the exact dose every time", "I will not double the dose if missed", "Nausea and vomiting are expected side effects"], "a": "Nausea and vomiting are expected side effects", "r": "Nausea/Vomiting are signs of Digoxin toxicity, not normal side effects."},
    {"q": "A 5-year-old with 'scarlatiniform rash', fever and refusal to eat likely has:", "o": ["Kawasaki disease", "Rheumatic Fever", "Dengue Fever", "Sore Throat (Strep)"], "a": "Sore Throat (Strep)", "r": "Scarlet fever rash is a hallmark of Group A Strep pharyngitis."},
    {"q": "Tetralogy of Fallot is defined by (SATA):", "o": ["VSD, Overriding Aorta, RV Hypertrophy, RV Outflow Obstruction", "VSD, ASD, PDA, CoAo", "TOGA, VSD, ASD", "RVH, LVH, VSD"], "a": "VSD, Overriding Aorta, RV Hypertrophy, RV Outflow Obstruction", "r": "Remember 'DROP': Defect (VSD), Right Ventricular Hypertrophy, Overriding Aorta, Pulmonary Stenosis."},
    {"q": "Elevated BP in right arm and unequal pulses in extremities indicates:", "o": ["CoAo", "VSD", "ASD", "PDA"], "a": "CoAo", "r": "Coarctation of the Aorta causes high pressure in upper body and low pressure/pulses in lower body."},
    {"q": "Which is NOT included in AVSD management?", "o": ["ACE inhibitors", "Pulmonary artery band", "Surgical closure", "Calcium Channel blockers"], "a": "Calcium Channel blockers", "r": "CCBs are not standard for primary AVSD management; focus is on HF control and surgery."},
    {"q": "Kawasaki IVIG/Aspirin therapy aims to prevent:", "o": ["Coronary artery aneurysms", "Polymorphous exanthema", "Bilateral conjunctivitis", "Embolism"], "a": "Coronary artery aneurysms", "r": "The primary goal is preventing permanent cardiac vessel damage."},
    {"q": "Kawasaki diagnosis includes prolonged fever EXCEPT:", "o": ["Hand/foot changes", "Contained rash of head/face", "Bilateral conjunctivitis", "Lips/mouth changes"], "a": "Contained rash of head/face", "r": "The rash in Kawasaki is typically polymorphous (varied) and trunk-focused, not just the face."},
    {"q": "The virtually definitive sign of Rheumatic Fever is:", "o": ["Erythema marginatum", "Polyarthritis", "Carditis", "Sydenham chorea"], "a": "Erythema marginatum", "r": "Erythema marginatum is a classic Major Jones Criterion."},
    {"q": "Management of HF includes all BUT ONE:", "o": ["Digoxin", "Alpha adrenergic agonist", "ACE inhibitors", "Beta-blockers"], "a": "Alpha adrenergic agonist", "r": "Alpha agonists (like phenylephrine) increase afterload, which is bad for heart failure."},
    {"q": "Expected heart sound in ASD?", "o": ["Harsh holosystolic murmur", "Machinery-like murmur", "Loud systolic murmur", "Fixed split S2 sound"], "a": "Fixed split S2 sound", "r": "A fixed split S2 is the hallmark of Atrial Septal Defect."},
    {"q": "Most common CHD in Trisomy 21?", "o": ["AVSD", "TOF", "TOGA", "CoAo"], "a": "AVSD", "r": "Atrioventricular Septal Defect is highly associated with Down Syndrome."},
    {"q": "Which CHD needs Prostaglandin infusion to keep Ductus Arteriosus open?", "o": ["TOF", "TOGA", "CoAo", "AVSD"], "a": "TOGA", "r": "Transposition of Great Arteries requires mixing of blood via the DA to survive until surgery."},
    {"q": "When is the Jatene procedure (Arterial Switch) performed in TOGA?", "o": ["5-15 years", "6-15 years", "First 3-6 months", "First 2 weeks of life"], "a": "First 2 weeks of life", "r": "Corrective surgery is ideally done very early in the neonatal period."},
    {"q": "Causative agent for bacterial pharyngitis:", "o": ["E.coli", "Group B Strep", "Group A beta hemolytic strep", "Staph Aureus"], "a": "Group A beta hemolytic strep", "r": "GABHS is the most common bacterial cause (Strep Throat)."},
    {"q": "In severe diarrhea, before adding Potassium to IV fluids, ensure:", "o": ["Hemoglobin check", "Infant has voided", "Rectal temp check", "Heart rate taken"], "a": "Infant has voided", "r": "Never add Potassium to IV if there is no urine output (risk of hyperkalemia)."},
    {"q": "Persistent vomiting typically leads to which acid-base imbalance?", "o": ["Respiratory acidosis", "Fluid volume excess", "Metabolic alkalosis", "Hyperchlorosis"], "a": "Metabolic alkalosis", "r": "Loss of gastric HCl causes a rise in blood pH (alkalosis)."},
    {"q": "In Pyloric Stenosis, which assessment is UNRELATED?", "o": ["Sour smelling vomitus", "Bile present in vomitus", "Projectile vomiting", "Olive-size lump"], "a": "Bile present in vomitus", "r": "In pyloric stenosis, the obstruction is above the bile duct, so vomitus is non-biliary."},
    {"q": "When does vomiting occur in Pyloric Stenosis?", "o": ["Immediately after feeding", "An hour after feeding", "In the morning", "When crying"], "a": "Immediately after feeding", "r": "Vomiting is usually projectile and happens right after the infant eats."},
    {"q": "Post-pyloromyotomy, all are correct EXCEPT:", "o": ["Keep NPO/IVF", "Dumping syndrome is normal", "Place on left side when feeding", "Report vomiting immediately"], "a": "Dumping syndrome is normal", "r": "Dumping syndrome is NOT expected after this surgery; it usually happens after stomach removals."},
    {"q": "In Intussusception, which is INCORRECT?", "o": ["Pain repeats q15-20 mins", "Red currant jelly stools", "Stomach feels full", "Immune response to gluten"], "a": "Immune response to gluten", "r": "Gluten response is Celiac Disease, not Intussusception."},
    {"q": "Hirschsprung disease description EXCEPT:", "o": ["Chronic constipation", "More common in females", "Gene on Chromosome 10", "Confirmed by rectal exam"], "a": "More common in females", "r": "Hirschsprung is actually more common in males."},
    {"q": "Food encouraged post-tonsillectomy?", "o": ["Strawberry popsicle", "Vanilla ice cream", "Orange juice", "Guyabano juice"], "a": "Vanilla ice cream", "r": "Dairy is allowed after clear liquids; avoid red colors and acidic juices."}
]

if 'score' not in st.session_state: st.session_state.score = 0
if 'current_q' not in st.session_state: st.session_state.current_q = 0
if 'submitted' not in st.session_state: st.session_state.submitted = False

st.title("👨‍⚕️ PNLE Pediatric Nursing Review")

if st.session_state.current_q < len(quiz_data):
    item = quiz_data[st.session_state.current_q]
    st.progress((st.session_state.current_q) / len(quiz_data))
    
    st.write(f"### Question {st.session_state.current_q + 1}")
    st.info(item["q"])
    
    choice = st.radio("Pick your answer:", item["o"], key=f"choice_{st.session_state.current_q}")
    
    if not st.session_state.submitted:
        if st.button("Check Answer"):
            st.session_state.submitted = True
            st.rerun()
    else:
        if choice == item["a"]:
            st.success(f"✅ Correct! \n\n **Rationale:** {item['r']}")
            if st.session_state.current_q == st.session_state.current_q: # logic gate
                 pass 
        else:
            st.error(f"❌ Incorrect. The answer is **{item['a']}**. \n\n **Rationale:** {item['r']}")
        
        if st.button("Next Question ➡️"):
            if choice == item["a"]:
                st.session_state.score += 1
            st.session_state.current_q += 1
            st.session_state.submitted = False
            st.rerun()
else:
    st.balloons()
    st.header("🏁 Quiz Finished!")
    st.metric("Your Score", f"{st.session_state.score} / {len(quiz_data)}")
    if st.button("Restart"):
        st.session_state.score = 0
        st.session_state.current_q = 0
        st.session_state.submitted = False
        st.rerun()
