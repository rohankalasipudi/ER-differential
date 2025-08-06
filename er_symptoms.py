# er_symptoms.py
# This file contains a diagnostic tree for the 50 most common ER presentations.
# It is structured to support a progressive, question-and-answer flow.

ER_PRESENTATIONS = {
    # 1-5: Classic Chief Complaints
    "Chest Pain": {
        "questions": {
            "location": ["Central", "Left-sided", "Right-sided"],
            "character": ["Crushing", "Sharp", "Dull", "Burning"],
            "radiation": ["To the arm", "To the jaw", "To the back", "None"],
        },
        "diagnoses": [
            {
                "name": "Myocardial Infarction (MI)",
                "match": {"location": "Central", "character": "Crushing", "radiation": ["To the arm", "To the jaw"]},
                "differentiating_factors": "Often associated with shortness of breath, sweating, and nausea. EKG changes are key."
            },
            {
                "name": "Pulmonary Embolism (PE)",
                "match": {"character": "Sharp", "radiation": "None"},
                "differentiating_factors": "Sudden onset, often with dyspnea, tachypnea, and risk factors for DVT."
            },
            {
                "name": "Pericarditis",
                "match": {"location": "Central", "character": "Sharp"},
                "differentiating_factors": "Pain is often pleuritic (worse with inspiration) and improves with leaning forward."
            },
            {
                "name": "Gastroesophageal Reflux Disease (GERD)",
                "match": {"character": "Burning", "location": ["Central", "Right-sided", "Left-sided"]},
                "differentiating_factors": "Pain is often postprandial, worse when lying down, and may be relieved by antacids. Look for dysphagia."
            },
            {
                "name": "Aortic Dissection",
                "match": {"character": "Sharp", "radiation": "To the back"},
                "differentiating_factors": "Sudden, severe, tearing pain. Associated with hypertension. A medical emergency."
            }
        ]
    },
    "Abdominal Pain": {
        "questions": {
            "location": ["RUQ", "LUQ", "RLQ", "LLQ", "Epigastric", "Periumbilical", "Diffuse"],
            "character": ["Colicky", "Dull", "Sharp", "Burning"],
            "associated_symptoms": ["Nausea/Vomiting", "Fever/Chills", "Bloating", "Diarrhea", "Constipation"],
        },
        "diagnoses": [
            {
                "name": "Appendicitis",
                "match": {"location": "RLQ", "character": "Sharp"},
                "differentiating_factors": "Pain often starts periumbilical and migrates to the RLQ. Associated with anorexia and low-grade fever."
            },
            {
                "name": "Cholecystitis",
                "match": {"location": "RUQ", "character": ["Colicky", "Dull"]},
                "differentiating_factors": "Pain radiates to the right shoulder/scapula. Often follows a fatty meal. Look for Murphy's sign."
            },
            {
                "name": "Diverticulitis",
                "match": {"location": "LLQ", "character": "Dull"},
                "differentiating_factors": "Associated with fever, leukocytosis, and constipation. Common in older patients."
            },
            {
                "name": "Pancreatitis",
                "match": {"location": ["LUQ", "Epigastric"], "character": "Dull"},
                "differentiating_factors": "Pain radiates to the back. Often associated with alcohol use or gallstones. Nausea and vomiting are common."
            },
            {
                "name": "Peptic Ulcer Disease (PUD)",
                "match": {"location": "Epigastric", "character": "Burning"},
                "differentiating_factors": "Pain is often gnawing or burning. May be relieved by food (duodenal ulcer) or worsened by food (gastric ulcer)."
            }
        ]
    },
    "Shortness of Breath": {
        "questions": {
            "onset": ["Sudden", "Gradual"],
            "associated_symptoms": ["Cough", "Wheezing", "Chest pain", "Fever", "Ankle swelling"],
        },
        "diagnoses": [
            {
                "name": "Asthma Exacerbation",
                "match": {"onset": "Sudden", "associated_symptoms": ["Wheezing", "Cough"]},
                "differentiating_factors": "Patient has a history of asthma. Relieved by bronchodilators."
            },
            {
                "name": "Congestive Heart Failure (CHF)",
                "match": {"onset": "Gradual", "associated_symptoms": ["Ankle swelling"]},
                "differentiating_factors": "Look for orthopnea, paroxysmal nocturnal dyspnea, and bilateral lower extremity edema."
            },
            {
                "name": "Pneumonia",
                "match": {"onset": ["Gradual", "Sudden"], "associated_symptoms": ["Fever", "Cough"]},
                "differentiating_factors": "Often with productive cough, fever, chills, and tachypnea. Chest X-ray is diagnostic."
            },
            {
                "name": "Pulmonary Embolism (PE)",
                "match": {"onset": "Sudden", "associated_symptoms": ["Chest pain"]},
                "differentiating_factors": "Sudden onset of dyspnea with pleuritic chest pain. Check for risk factors for DVT."
            },
            {
                "name": "COPD Exacerbation",
                "match": {"onset": "Gradual", "associated_symptoms": "Cough"},
                "differentiating_factors": "History of smoking and chronic cough. May present with increased sputum production and wheezing."
            }
        ]
    },
    "Headache": {
        "questions": {
            "onset": ["Sudden (Thunderclap)", "Gradual"],
            "character": ["Throbbing", "Band-like pressure", "Sharp", "Worse with valsalva"],
            "associated_symptoms": ["Photophobia", "Phonophobia", "Nausea/Vomiting", "Fever", "Stiff neck"]
        },
        "diagnoses": [
            {
                "name": "Migraine",
                "match": {"onset": "Gradual", "character": "Throbbing", "associated_symptoms": ["Photophobia", "Phonophobia", "Nausea/Vomiting"]},
                "differentiating_factors": "Often unilateral and associated with auras. Can be debilitating."
            },
            {
                "name": "Tension Headache",
                "match": {"onset": "Gradual", "character": "Band-like pressure"},
                "differentiating_factors": "Often bilateral and not associated with photophobia or nausea."
            },
            {
                "name": "Subarachnoid Hemorrhage",
                "match": {"onset": "Sudden (Thunderclap)"},
                "differentiating_factors": "The worst headache of their life. Often associated with altered mental status and stiff neck."
            },
            {
                "name": "Meningitis",
                "match": {"character": "Worse with valsalva", "associated_symptoms": ["Fever", "Stiff neck"]},
                "differentiating_factors": "Headache with fever, stiff neck, and photophobia. Look for rash."
            }
        ]
    },
    "Back Pain": {
        "questions": {
            "location": ["Cervical", "Thoracic", "Lumbar"],
            "onset": ["Sudden (with injury)", "Gradual"],
            "radiation": ["To the leg", "To the chest", "None"],
            "red_flags": ["Fever", "Urinary retention", "Saddle anesthesia"]
        },
        "diagnoses": [
            {
                "name": "Lumbar Strain",
                "match": {"location": "Lumbar", "onset": "Sudden (with injury)", "radiation": "None"},
                "differentiating_factors": "Pain is typically localized and improves with rest. No neurological deficits."
            },
            {
                "name": "Herniated Disc",
                "match": {"location": "Lumbar", "radiation": "To the leg"},
                "differentiating_factors": "Radiating pain in a dermatomal pattern. Can be associated with motor or sensory deficits."
            },
            {
                "name": "Aortic Dissection",
                "match": {"location": ["Thoracic", "Lumbar"], "onset": "Sudden (with injury)"},
                "differentiating_factors": "Severe, tearing pain that radiates to the back. A medical emergency."
            },
            {
                "name": "Pyelonephritis",
                "match": {"location": "Lumbar", "red_flags": ["Fever"]},
                "differentiating_factors": "Flank pain with fever, chills, and dysuria. CVA tenderness is a key sign."
            }
        ]
    },
    # 6-10: Fever & Infectious
    "Fever": {
        "questions": {
            "onset": ["Acute (< 48 hours)", "Subacute (days to weeks)"],
            "associated_symptoms": ["Rash", "Sore throat", "Cough", "Headache", "Abdominal pain"],
            "travel_history": ["Yes", "No"],
        },
        "diagnoses": [
            {
                "name": "Influenza",
                "match": {"onset": "Acute (< 48 hours)", "associated_symptoms": ["Sore throat", "Cough"]},
                "differentiating_factors": "Often accompanied by myalgias and fatigue. Can be diagnosed with a rapid flu test."
            },
            {
                "name": "Sepsis",
                "match": {"onset": "Acute (< 48 hours)", "associated_symptoms": ["Altered mental status", "Tachycardia"]},
                "differentiating_factors": "Look for a source of infection and signs of organ dysfunction. Requires prompt fluid resuscitation and antibiotics."
            },
            {
                "name": "Meningitis",
                "match": {"onset": "Acute (< 48 hours)", "associated_symptoms": ["Headache", "Stiff neck"]},
                "differentiating_factors": "Fever, headache, and nuchal rigidity. Requires a lumbar puncture for definitive diagnosis."
            },
            {
                "name": "Cellulitis",
                "match": {"associated_symptoms": "Redness/swelling on skin"},
                "differentiating_factors": "Fever with localized skin redness, warmth, and swelling. Look for a portal of entry."
            }
        ]
    },
    "Sore Throat": {
        "questions": {
            "onset": ["Sudden", "Gradual"],
            "associated_symptoms": ["Fever", "Cough", "White patches on tonsils", "Rash"],
        },
        "diagnoses": [
            {
                "name": "Viral Pharyngitis",
                "match": {"onset": "Gradual", "associated_symptoms": "Cough"},
                "differentiating_factors": "Often accompanied by other URI symptoms like runny nose and cough. Most common cause of sore throat."
            },
            {
                "name": "Strep Throat",
                "match": {"onset": "Sudden", "associated_symptoms": "White patches on tonsils"},
                "differentiating_factors": "Sudden onset of fever and sore throat without a cough. Look for tender anterior cervical lymph nodes."
            },
            {
                "name": "Mononucleosis",
                "match": {"associated_symptoms": ["White patches on tonsils", "Fever"]},
                "differentiating_factors": "Fever, pharyngitis, and lymphadenopathy. Often prolonged course with fatigue. Splenomegaly is common."
            }
        ]
    },
    "Urinary Symptoms": {
        "questions": {
            "symptoms": ["Pain on urination", "Increased frequency", "Blood in urine", "Flank pain"],
            "associated_symptoms": ["Fever", "Back pain", "Nausea/Vomiting"],
        },
        "diagnoses": [
            {
                "name": "Urinary Tract Infection (UTI)",
                "match": {"symptoms": ["Pain on urination", "Increased frequency"]},
                "differentiating_factors": "Dysuria and frequency are classic symptoms. A urinalysis will show nitrites and leukocyte esterase."
            },
            {
                "name": "Pyelonephritis",
                "match": {"symptoms": "Flank pain", "associated_symptoms": ["Fever", "Back pain"]},
                "differentiating_factors": "Flank pain with fever, chills, and dysuria. CVA tenderness is a key sign."
            },
            {
                "name": "Kidney Stones (Nephrolithiasis)",
                "match": {"symptoms": "Flank pain", "associated_symptoms": "Nausea/Vomiting"},
                "differentiating_factors": "Sudden, severe, colicky flank pain that radiates to the groin. Hematuria is common."
            }
        ]
    },
    "Rash": {
        "questions": {
            "onset": ["Sudden", "Gradual"],
            "appearance": ["Maculopapular", "Vesicular", "Urticarial", "Erythema Migrans"],
            "associated_symptoms": ["Fever", "Itching", "Joint pain"],
        },
        "diagnoses": [
            {
                "name": "Allergic Reaction (Urticaria)",
                "match": {"onset": "Sudden", "appearance": "Urticarial"},
                "differentiating_factors": "Hives that are intensely itchy. Often triggered by food, medication, or insect bites. May be associated with angioedema."
            },
            {
                "name": "Cellulitis",
                "match": {"onset": "Sudden", "appearance": "Erythema"},
                "differentiating_factors": "Localized area of redness, warmth, and swelling. Look for a history of skin injury."
            },
            {
                "name": "Shingles (Herpes Zoster)",
                "match": {"appearance": "Vesicular"},
                "differentiating_factors": "Painful rash of vesicles in a dermatomal distribution. Preceded by a burning sensation."
            }
        ]
    },
    "Nausea and Vomiting": {
        "questions": {
            "onset": ["Acute", "Chronic"],
            "associated_symptoms": ["Abdominal pain", "Diarrhea", "Fever", "Headache"],
            "timing": ["After meals", "Morning", "None"],
        },
        "diagnoses": [
            {
                "name": "Gastroenteritis",
                "match": {"onset": "Acute", "associated_symptoms": ["Diarrhea", "Abdominal pain"]},
                "differentiating_factors": "Often viral or bacterial in origin. Self-limited in most cases. Dehydration is a concern."
            },
            {
                "name": "Bowel Obstruction",
                "match": {"onset": "Acute", "associated_symptoms": "Abdominal pain"},
                "differentiating_factors": "Vomiting may become feculent. Abdominal distention and inability to pass gas or stool are key."
            },
            {
                "name": "Pancreatitis",
                "match": {"onset": "Acute", "associated_symptoms": "Abdominal pain", "timing": "After meals"},
                "differentiating_factors": "Abdominal pain that radiates to the back after a meal is a classic presentation. Look for elevated lipase."
            }
        ]
    },
    # 11-15: Trauma & Orthopedic
    "Extremity Pain/Injury": {
        "questions": {
            "location": ["Arm", "Leg", "Hand", "Foot"],
            "onset": ["Acute (with injury)", "Chronic"],
            "mechanism": ["Fall", "Twisting injury", "Direct blow", "Overuse"],
            "physical_exam": ["Deformity", "Swelling", "Inability to bear weight"],
        },
        "diagnoses": [
            {
                "name": "Fracture",
                "match": {"onset": "Acute (with injury)", "physical_exam": ["Deformity", "Inability to bear weight"]},
                "differentiating_factors": "Immediate, severe pain after trauma. Requires an X-ray for diagnosis."
            },
            {
                "name": "Dislocation",
                "match": {"onset": "Acute (with injury)", "physical_exam": "Deformity"},
                "differentiating_factors": "Visible deformity of a joint after trauma. Requires reduction in the ER."
            },
            {
                "name": "Sprain/Strain",
                "match": {"onset": "Acute (with injury)", "physical_exam": "Swelling"},
                "differentiating_factors": "Pain and swelling after an injury, but without a visible deformity or inability to bear weight."
            },
            {
                "name": "Cellulitis",
                "match": {"onset": "Gradual", "physical_exam": "Swelling"},
                "differentiating_factors": "Localized redness, warmth, and swelling with a possible fever. Not due to trauma."
            }
        ]
    },
    "Head Injury": {
        "questions": {
            "mechanism": ["Fall", "Assault", "Motor vehicle accident"],
            "loss_of_consciousness": ["Yes", "No"],
            "associated_symptoms": ["Headache", "Nausea/Vomiting", "Amnesia", "Focal neurological deficit"],
        },
        "diagnoses": [
            {
                "name": "Concussion",
                "match": {"loss_of_consciousness": "Yes", "associated_symptoms": "Amnesia"},
                "differentiating_factors": "Transient loss of consciousness after trauma with amnesia. Symptoms may include headache, dizziness, and confusion."
            },
            {
                "name": "Subdural Hematoma",
                "match": {"associated_symptoms": ["Headache", "Focal neurological deficit"]},
                "differentiating_factors": "Slow onset of symptoms in an elderly patient after a minor fall. Requires a head CT."
            },
            {
                "name": "Epidural Hematoma",
                "match": {"mechanism": "Motor vehicle accident", "associated_symptoms": ["Headache", "Nausea/Vomiting"]},
                "differentiating_factors": "A classic 'lucid interval' after a head injury, followed by rapid neurological decline. Requires urgent neurosurgical intervention."
            }
        ]
    },
    "Trauma (General)": {
        "questions": {
            "mechanism": ["Stab wound", "Gunshot wound", "Blunt force trauma"],
            "injury_location": ["Abdomen", "Chest", "Extremity"],
            "hemodynamic_status": ["Stable", "Unstable"],
        },
        "diagnoses": [
            {
                "name": "Hemorrhagic Shock",
                "match": {"mechanism": ["Stab wound", "Gunshot wound", "Blunt force trauma"], "hemodynamic_status": "Unstable"},
                "differentiating_factors": "Hypotension and tachycardia after significant trauma. Requires immediate fluid resuscitation and control of bleeding."
            },
            {
                "name": "Pneumothorax",
                "match": {"mechanism": "Blunt force trauma", "injury_location": "Chest"},
                "differentiating_factors": "Unilateral chest pain and shortness of breath after trauma. Look for decreased breath sounds on the affected side."
            },
            {
                "name": "Splenic/Liver Laceration",
                "match": {"mechanism": "Blunt force trauma", "injury_location": "Abdomen", "hemodynamic_status": "Unstable"},
                "differentiating_factors": "Abdominal pain and tenderness after blunt trauma. Requires a FAST exam or CT scan."
            }
        ]
    },
    "Joint Pain/Swelling": {
        "questions": {
            "location": ["Knee", "Shoulder", "Ankle", "Hip", "Multiple joints"],
            "onset": ["Acute", "Chronic"],
            "associated_symptoms": ["Redness", "Warmth", "Fever", "Limited range of motion"],
        },
        "diagnoses": [
            {
                "name": "Septic Arthritis",
                "match": {"onset": "Acute", "associated_symptoms": ["Redness", "Warmth", "Fever", "Limited range of motion"]},
                "differentiating_factors": "Sudden onset of a single, hot, swollen joint with fever. A medical emergency requiring joint aspiration."
            },
            {
                "name": "Gout",
                "match": {"onset": "Acute", "location": "Ankle", "associated_symptoms": ["Redness", "Warmth"]},
                "differentiating_factors": "Sudden, excruciating pain in a single joint (often the big toe). Associated with hyperuricemia."
            },
            {
                "name": "Rheumatoid Arthritis (RA) flare",
                "match": {"onset": "Chronic", "location": "Multiple joints"},
                "differentiating_factors": "Symmetric, polyarticular joint pain and swelling. Morning stiffness is a classic feature."
            }
        ]
    },
    "Acute Wounds": {
        "questions": {
            "type": ["Laceration", "Abrasion", "Puncture wound", "Avulsion"],
            "location": ["Head/Face", "Extremity", "Trunk"],
            "risk_factors": ["Contaminated wound", "Animal bite", "Diabetic"],
        },
        "diagnoses": [
            {
                "name": "Laceration",
                "match": {"type": "Laceration"},
                "differentiating_factors": "A clean cut to the skin that may require sutures."
            },
            {
                "name": "Abscess",
                "match": {"location": "Extremity", "risk_factors": "Diabetic"},
                "differentiating_factors": "A collection of pus under the skin. Presents as a fluctuant, tender, red nodule. Often requires incision and drainage."
            },
            {
                "name": "Animal Bite",
                "match": {"risk_factors": "Animal bite"},
                "differentiating_factors": "Consider rabies prophylaxis, tetanus, and antibiotics. Look for puncture wounds and crush injuries."
            }
        ]
    },
    # 16-20: Cardiovascular
    "Palpitations": {
        "questions": {
            "onset": ["Sudden", "Gradual"],
            "character": ["Racing", "Skipping a beat", "Pounding"],
            "associated_symptoms": ["Dizziness", "Syncope", "Chest pain"],
        },
        "diagnoses": [
            {
                "name": "Atrial Fibrillation (A-fib)",
                "match": {"character": "Racing", "onset": "Sudden"},
                "differentiating_factors": "Irregularly irregular rhythm. Risk of stroke is a key concern. Patient may be asymptomatic or present with shortness of breath."
            },
            {
                "name": "Supraventricular Tachycardia (SVT)",
                "match": {"character": "Racing", "onset": "Sudden"},
                "differentiating_factors": "Regular, narrow-complex tachycardia. Can be treated with vagal maneuvers or adenosine."
            },
            {
                "name": "Ventricular Tachycardia (V-tach)",
                "match": {"associated_symptoms": ["Dizziness", "Syncope", "Chest pain"]},
                "differentiating_factors": "A wide-complex tachycardia. Can lead to cardiac arrest. A medical emergency."
            }
        ]
    },
    "Hypertension": {
        "questions": {
            "bp_reading": ["Severe (>180/120)", "Mild"],
            "associated_symptoms": ["Headache", "Chest pain", "Shortness of breath"],
        },
        "diagnoses": [
            {
                "name": "Hypertensive Emergency",
                "match": {"bp_reading": "Severe (>180/120)", "associated_symptoms": ["Headache", "Chest pain", "Shortness of breath"]},
                "differentiating_factors": "Elevated blood pressure with evidence of end-organ damage. Requires immediate IV medication to lower BP."
            },
            {
                "name": "Hypertensive Urgency",
                "match": {"bp_reading": "Severe (>180/120)", "associated_symptoms": "None"},
                "differentiating_factors": "Elevated blood pressure without evidence of end-organ damage. Can be treated with oral medication over hours to days."
            }
        ]
    },
    "Syncope": {
        "questions": {
            "onset": ["Sudden", "Preceded by symptoms"],
            "triggers": ["Standing up", "Painful stimulus", "Exertion", "None"],
            "associated_symptoms": ["Palpitations", "Chest pain", "Fainting"]
        },
        "diagnoses": [
            {
                "name": "Vasovagal Syncope",
                "match": {"onset": "Preceded by symptoms", "triggers": "Painful stimulus"},
                "differentiating_factors": "Often preceded by lightheadedness, nausea, or sweating. Patient is often young and healthy."
            },
            {
                "name": "Orthostatic Hypotension",
                "match": {"onset": "Sudden", "triggers": "Standing up"},
                "differentiating_factors": "Associated with a drop in blood pressure upon standing. Common in older patients or those on certain medications."
            },
            {
                "name": "Cardiogenic Syncope",
                "match": {"onset": "Sudden", "triggers": "Exertion", "associated_symptoms": "Chest pain"},
                "differentiating_factors": "Loss of consciousness during exertion is a red flag for a cardiac cause (e.g., arrhythmia, aortic stenosis)."
            }
        ]
    },
    "Dizziness": {
        "questions": {
            "type": ["Vertigo (spinning sensation)", "Lightheadedness", "Disequilibrium"],
            "onset": ["Sudden", "Gradual"],
            "associated_symptoms": ["Nausea", "Hearing loss", "Tinnitus", "Headache"],
        },
        "diagnoses": [
            {
                "name": "Benign Paroxysmal Positional Vertigo (BPPV)",
                "match": {"type": "Vertigo (spinning sensation)", "onset": "Sudden"},
                "differentiating_factors": "Brief episodes of vertigo triggered by head movements (e.g., rolling over in bed)."
            },
            {
                "name": "Ménière's Disease",
                "match": {"type": "Vertigo (spinning sensation)", "associated_symptoms": ["Hearing loss", "Tinnitus"]},
                "differentiating_factors": "Classic triad of vertigo, tinnitus, and hearing loss. Episodes last for hours."
            },
            {
                "name": "Vestibular Neuritis",
                "match": {"type": "Vertigo (spinning sensation)", "onset": "Sudden"},
                "differentiating_factors": "A single, severe episode of vertigo lasting days. Often preceded by a viral illness. No hearing loss."
            },
            {
                "name": "Orthostatic Hypotension",
                "match": {"type": "Lightheadedness"},
                "differentiating_factors": "Lightheadedness when standing up from a sitting or lying position. Check for a drop in blood pressure."
            }
        ]
    },
    "Edema": {
        "questions": {
            "location": ["Unilateral", "Bilateral"],
            "associated_symptoms": ["Shortness of breath", "Calf pain", "Redness/Warmth"],
        },
        "diagnoses": [
            {
                "name": "Deep Vein Thrombosis (DVT)",
                "match": {"location": "Unilateral", "associated_symptoms": "Calf pain"},
                "differentiating_factors": "Unilateral leg swelling and pain. Associated with risk factors for hypercoagulability. Requires a Doppler ultrasound."
            },
            {
                "name": "Congestive Heart Failure (CHF)",
                "match": {"location": "Bilateral", "associated_symptoms": "Shortness of breath"},
                "differentiating_factors": "Bilateral pitting edema with signs of fluid overload, such as orthopnea and jugular venous distention."
            }
        ]
    },
    # 21-25: Neurological
    "Weakness": {
        "questions": {
            "onset": ["Sudden", "Gradual"],
            "location": ["One side of body", "Both sides of body", "All four limbs"],
            "associated_symptoms": ["Numbness", "Difficulty speaking", "Drooping face", "Trouble swallowing"],
        },
        "diagnoses": [
            {
                "name": "Stroke (CVA)",
                "match": {"onset": "Sudden", "location": "One side of body", "associated_symptoms": ["Difficulty speaking", "Drooping face"]},
                "differentiating_factors": "Sudden onset of focal neurological deficits. Time is brain. Rule out hemorrhagic vs. ischemic."
            },
            {
                "name": "Myasthenia Gravis",
                "match": {"onset": "Gradual", "location": "Both sides of body", "associated_symptoms": ["Trouble swallowing"]},
                "differentiating_factors": "Classic finding is fluctuating, fatigable weakness that worsens with activity and improves with rest."
            },
            {
                "name": "Guillain-Barré Syndrome",
                "match": {"onset": "Gradual", "location": "Both sides of body", "associated_symptoms": "Numbness"},
                "differentiating_factors": "Ascending paralysis and numbness, often following a viral illness."
            }
        ]
    },
    "Seizures": {
        "questions": {
            "type": ["Generalized", "Focal"],
            "known_history": ["Yes (epilepsy)", "No"],
            "associated_symptoms": ["Fever", "Head trauma", "Drug/alcohol use"],
        },
        "diagnoses": [
            {
                "name": "Epilepsy",
                "match": {"type": "Generalized", "known_history": "Yes (epilepsy)"},
                "differentiating_factors": "Seizures in a patient with a known history of a seizure disorder. Medication noncompliance is a common trigger."
            },
            {
                "name": "Status Epilepticus",
                "match": {"type": "Generalized"},
                "differentiating_factors": "A medical emergency. Seizures lasting longer than 5 minutes or multiple seizures without a return to consciousness."
            },
            {
                "name": "Febrile Seizure",
                "match": {"associated_symptoms": "Fever"},
                "differentiating_factors": "Seizures that occur in children with a fever. Often benign but requires workup to rule out a source of infection."
            }
        ]
    },
    "Altered Mental Status": {
        "questions": {
            "onset": ["Sudden", "Gradual"],
            "associated_symptoms": ["Fever", "Headache", "Weakness", "Seizures"],
            "medical_history": ["Diabetes", "Drug/alcohol use", "Stroke", "Infection"],
        },
        "diagnoses": [
            {
                "name": "Hypoglycemia",
                "match": {"onset": "Sudden", "medical_history": "Diabetes"},
                "differentiating_factors": "Rapid onset of confusion, anxiety, and diaphoresis. Easily treated with glucose."
            },
            {
                "name": "Infectious Encephalitis",
                "match": {"onset": "Gradual", "associated_symptoms": ["Fever", "Headache"]},
                "differentiating_factors": "Fever, headache, and altered mental status. Often requires CSF analysis for diagnosis."
            },
            {
                "name": "Toxic-Metabolic Encephalopathy",
                "match": {"onset": "Gradual", "medical_history": ["Drug/alcohol use"]},
                "differentiating_factors": "Altered mental status due to systemic illness, drug overdose, or organ failure."
            }
        ]
    },
    "Focal Neurological Deficit": {
        "questions": {
            "onset": ["Sudden", "Gradual"],
            "type": ["Speech difficulties", "Facial droop", "Hemiparesis"],
            "risk_factors": ["Hypertension", "Diabetes", "Smoking"],
        },
        "diagnoses": [
            {
                "name": "Transient Ischemic Attack (TIA)",
                "match": {"onset": "Sudden"},
                "differentiating_factors": "Transient neurological symptoms that resolve completely within 24 hours. A warning sign of impending stroke."
            },
            {
                "name": "Stroke (CVA)",
                "match": {"onset": "Sudden", "type": ["Speech difficulties", "Facial droop", "Hemiparesis"]},
                "differentiating_factors": "Symptoms persist and are a true medical emergency. Requires a CT scan to rule out hemorrhage."
            }
        ]
    },
    "Vertigo": {
        "questions": {
            "onset": ["Sudden", "Gradual"],
            "associated_symptoms": ["Hearing loss", "Tinnitus", "Nausea", "Head movements"],
        },
        "diagnoses": [
            {
                "name": "Benign Paroxysmal Positional Vertigo (BPPV)",
                "match": {"onset": "Sudden", "associated_symptoms": "Head movements"},
                "differentiating_factors": "Brief episodes of vertigo triggered by head movements. No hearing loss or tinnitus."
            },
            {
                "name": "Ménière's Disease",
                "match": {"onset": "Sudden", "associated_symptoms": ["Hearing loss", "Tinnitus"]},
                "differentiating_factors": "Classic triad of vertigo, tinnitus, and hearing loss. Episodes last for hours."
            },
            {
                "name": "Vestibular Neuritis",
                "match": {"onset": "Sudden", "associated_symptoms": "Nausea"},
                "differentiating_factors": "A single, severe episode of vertigo lasting days. Often preceded by a viral illness. No hearing loss."
            }
        ]
    },
    # 26-30: Genitourinary & Pelvic
    "Flank Pain": {
        "questions": {
            "onset": ["Sudden", "Gradual"],
            "character": ["Colicky", "Dull"],
            "associated_symptoms": ["Nausea/Vomiting", "Fever", "Dysuria"],
        },
        "diagnoses": [
            {
                "name": "Kidney Stones (Nephrolithiasis)",
                "match": {"onset": "Sudden", "character": "Colicky", "associated_symptoms": "Nausea/Vomiting"},
                "differentiating_factors": "Sudden, severe, colicky flank pain that radiates to the groin. Hematuria is common."
            },
            {
                "name": "Pyelonephritis",
                "match": {"onset": "Gradual", "character": "Dull", "associated_symptoms": ["Fever", "Dysuria"]},
                "differentiating_factors": "Flank pain with fever, chills, and dysuria. CVA tenderness is a key sign."
            }
        ]
    },
    "Pelvic Pain (Female)": {
        "questions": {
            "onset": ["Sudden", "Gradual"],
            "location": ["Lower quadrant", "Midline"],
            "associated_symptoms": ["Vaginal bleeding", "Fever", "Nausea/Vomiting"],
        },
        "diagnoses": [
            {
                "name": "Ectopic Pregnancy",
                "match": {"onset": "Sudden", "associated_symptoms": ["Vaginal bleeding", "Nausea/Vomiting"]},
                "differentiating_factors": "Pelvic pain and vaginal bleeding in a pregnant patient. A medical emergency. Requires a transvaginal ultrasound."
            },
            {
                "name": "Ovarian Torsion",
                "match": {"onset": "Sudden", "location": "Lower quadrant"},
                "differentiating_factors": "Sudden, severe, unilateral pelvic pain. Often associated with nausea and vomiting. Requires an ultrasound with Doppler."
            },
            {
                "name": "Pelvic Inflammatory Disease (PID)",
                "match": {"onset": "Gradual", "associated_symptoms": "Fever"},
                "differentiating_factors": "Fever, chills, and lower abdominal pain. Associated with vaginal discharge and a positive cervical motion tenderness on exam."
            }
        ]
    },
    "Testicular Pain": {
        "questions": {
            "onset": ["Sudden", "Gradual"],
            "associated_symptoms": ["Nausea/Vomiting", "Swelling", "Fever"],
            "physical_exam": ["Absent cremasteric reflex", "Prehn's sign negative"],
        },
        "diagnoses": [
            {
                "name": "Testicular Torsion",
                "match": {"onset": "Sudden", "associated_symptoms": "Nausea/Vomiting", "physical_exam": "Absent cremasteric reflex"},
                "differentiating_factors": "Sudden, severe testicular pain. A surgical emergency. The cremasteric reflex is typically absent."
            },
            {
                "name": "Epididymitis",
                "match": {"onset": "Gradual", "associated_symptoms": "Fever", "physical_exam": "Prehn's sign positive"},
                "differentiating_factors": "Gradual onset of testicular pain and swelling. Prehn's sign (relief of pain with elevation of the testicle) is typically positive."
            }
        ]
    },
    "Vaginal Bleeding": {
        "questions": {
            "pregnancy_status": ["Pregnant", "Not pregnant"],
            "amount": ["Spotting", "Heavy"],
            "associated_symptoms": ["Pelvic pain", "Abdominal pain"],
        },
        "diagnoses": [
            {
                "name": "Threatened Miscarriage",
                "match": {"pregnancy_status": "Pregnant", "amount": "Spotting"},
                "differentiating_factors": "Vaginal bleeding with a closed cervix in a pregnant patient. Fetal viability is still a possibility."
            },
            {
                "name": "Ectopic Pregnancy",
                "match": {"pregnancy_status": "Pregnant", "amount": ["Spotting", "Heavy"], "associated_symptoms": "Pelvic pain"},
                "differentiating_factors": "Vaginal bleeding and pelvic pain. A medical emergency. Requires an ultrasound."
            },
            {
                "name": "Abnormal Uterine Bleeding",
                "match": {"pregnancy_status": "Not pregnant"},
                "differentiating_factors": "Bleeding outside of a normal menstrual cycle. Rule out other causes first, such as polyps or fibroids."
            }
        ]
    },
    "Pregnancy Complications": {
        "questions": {
            "trimester": ["First", "Second", "Third"],
            "symptoms": ["Vaginal bleeding", "Abdominal pain", "Decreased fetal movement"],
        },
        "diagnoses": [
            {
                "name": "Ectopic Pregnancy",
                "match": {"trimester": "First", "symptoms": ["Vaginal bleeding", "Abdominal pain"]},
                "differentiating_factors": "A medical emergency. A fertilized egg implants outside the uterus. Requires a transvaginal ultrasound."
            },
            {
                "name": "Placenta Previa",
                "match": {"trimester": "Third", "symptoms": "Vaginal bleeding"},
                "differentiating_factors": "Painless vaginal bleeding in the third trimester. The placenta covers the cervix."
            },
            {
                "name": "Placental Abruption",
                "match": {"trimester": "Third", "symptoms": ["Vaginal bleeding", "Abdominal pain"]},
                "differentiating_factors": "Painful vaginal bleeding in the third trimester with a firm, tender uterus. A medical emergency."
            }
        ]
    },
    # 31-35: Endocrine & Metabolic
    "Diabetic Crisis": {
        "questions": {
            "type": ["Hyperglycemia", "Hypoglycemia"],
            "associated_symptoms": ["Nausea/Vomiting", "Altered mental status", "Fruity breath"],
        },
        "diagnoses": [
            {
                "name": "Diabetic Ketoacidosis (DKA)",
                "match": {"type": "Hyperglycemia", "associated_symptoms": ["Nausea/Vomiting", "Fruity breath"]},
                "differentiating_factors": "Hyperglycemia with ketosis and acidosis. Patient is often young with Type 1 diabetes. Requires aggressive fluid and insulin therapy."
            },
            {
                "name": "Hyperosmolar Hyperglycemic State (HHS)",
                "match": {"type": "Hyperglycemia", "associated_symptoms": "Altered mental status"},
                "differentiating_factors": "Extreme hyperglycemia without ketosis. Patient is often older with Type 2 diabetes. Requires aggressive fluid resuscitation."
            },
            {
                "name": "Hypoglycemia",
                "match": {"type": "Hypoglycemia", "associated_symptoms": "Altered mental status"},
                "differentiating_factors": "Low blood glucose. Rapid onset of confusion, anxiety, and diaphoresis. Easily treated with glucose."
            }
        ]
    },
    "Thyroid Storm": {
        "questions": {
            "symptoms": ["Fever", "Tachycardia", "Altered mental status"],
            "medical_history": ["Hyperthyroidism"],
        },
        "diagnoses": [
            {
                "name": "Thyroid Storm",
                "match": {"symptoms": ["Fever", "Tachycardia", "Altered mental status"], "medical_history": "Hyperthyroidism"},
                "differentiating_factors": "A life-threatening complication of hyperthyroidism. Requires aggressive supportive care and medication to block thyroid hormone synthesis."
            }
        ]
    },
    "Adrenal Crisis": {
        "questions": {
            "symptoms": ["Hypotension", "Abdominal pain", "Weakness"],
            "medical_history": ["Adrenal insufficiency"],
        },
        "diagnoses": [
            {
                "name": "Adrenal Crisis",
                "match": {"symptoms": ["Hypotension", "Abdominal pain", "Weakness"], "medical_history": "Adrenal insufficiency"},
                "differentiating_factors": "A life-threatening condition caused by a lack of cortisol. Requires immediate IV fluids and steroids."
            }
        ]
    },
    "Electrolyte Abnormalities": {
        "questions": {
            "symptoms": ["Weakness", "Arrhythmia", "Nausea/Vomiting"],
            "triggers": ["Diarrhea/Vomiting", "Diuretics"],
        },
        "diagnoses": [
            {
                "name": "Hypokalemia",
                "match": {"symptoms": ["Weakness", "Arrhythmia"], "triggers": "Diuretics"},
                "differentiating_factors": "Low potassium can cause muscle weakness, cramps, and EKG changes. Requires potassium replacement."
            },
            {
                "name": "Hyponatremia",
                "match": {"symptoms": ["Nausea/Vomiting", "Altered mental status"]},
                "differentiating_factors": "Low sodium can cause confusion, seizures, and cerebral edema. Requires careful fluid management."
            }
        ]
    },
    # 36-40: Psychiatric & Social
    "Suicidal Ideation": {
        "questions": {
            "plan": ["Yes", "No"],
            "intent": ["High", "Low"],
            "risk_factors": ["Previous attempts", "Substance abuse", "Lack of support"],
        },
        "diagnoses": [
            {
                "name": "Depression with Suicidal Ideation",
                "match": {"plan": "Yes", "intent": "High"},
                "differentiating_factors": "A mental health emergency. Requires immediate psychiatric evaluation and inpatient admission for safety."
            },
            {
                "name": "Depression",
                "match": {"plan": "No", "intent": "Low"},
                "differentiating_factors": "Patient feels sad and hopeless but has no plan or intent to act on suicidal thoughts. Requires outpatient psychiatric follow-up."
            }
        ]
    },
    "Anxiety Attack": {
        "questions": {
            "symptoms": ["Shortness of breath", "Chest pain", "Palpitations"],
            "triggers": ["Stress", "Panic attack"],
            "onset": ["Sudden"],
        },
        "diagnoses": [
            {
                "name": "Panic Attack",
                "match": {"symptoms": ["Shortness of breath", "Chest pain", "Palpitations"], "onset": "Sudden"},
                "differentiating_factors": "A sudden episode of intense fear that triggers severe physical reactions. Requires ruling out cardiac causes first."
            }
        ]
    },
    "Substance Abuse/Overdose": {
        "questions": {
            "substance": ["Opioids", "Alcohol", "Benzodiazepines", "Stimulants"],
            "associated_symptoms": ["Altered mental status", "Respiratory depression", "Tachycardia"],
        },
        "diagnoses": [
            {
                "name": "Opioid Overdose",
                "match": {"substance": "Opioids", "associated_symptoms": ["Altered mental status", "Respiratory depression"]},
                "differentiating_factors": "Pinpoint pupils, respiratory depression, and altered mental status. Treat with naloxone."
            },
            {
                "name": "Alcohol Intoxication",
                "match": {"substance": "Alcohol", "associated_symptoms": "Altered mental status"},
                "differentiating_factors": "Slurred speech, ataxia, and confusion. Requires supportive care and monitoring."
            },
            {
                "name": "Benzodiazepine Overdose",
                "match": {"substance": "Benzodiazepines", "associated_symptoms": "Respiratory depression"},
                "differentiating_factors": "Similar to alcohol intoxication but can cause profound respiratory depression. Can be treated with flumazenil."
            }
        ]
    },
    # 41-45: Pediatric
    "Pediatric Fever": {
        "questions": {
            "age": ["< 3 months", "3-36 months", "> 36 months"],
            "symptoms": ["Lethargy", "Irritability", "Poor feeding"],
        },
        "diagnoses": [
            {
                "name": "Sepsis (infant)",
                "match": {"age": "< 3 months", "symptoms": "Lethargy"},
                "differentiating_factors": "A fever in an infant less than 3 months old is a medical emergency until proven otherwise. Requires a full septic workup."
            },
            {
                "name": "Viral illness",
                "match": {"age": "> 36 months", "symptoms": "Irritability"},
                "differentiating_factors": "Fever with other URI symptoms. Most common cause of fever in children."
            }
        ]
    },
    "Pediatric Respiratory Distress": {
        "questions": {
            "age": ["< 2 years", "> 2 years"],
            "symptoms": ["Stridor", "Wheezing", "Cough"],
        },
        "diagnoses": [
            {
                "name": "Croup",
                "match": {"age": "> 2 years", "symptoms": "Stridor"},
                "differentiating_factors": "A barking cough and inspiratory stridor. Often caused by a viral infection."
            },
            {
                "name": "Bronchiolitis",
                "match": {"age": "< 2 years", "symptoms": "Wheezing"},
                "differentiating_factors": "Common in infants. Wheezing and respiratory distress often caused by RSV. Requires supportive care."
            },
            {
                "name": "Foreign Body Aspiration",
                "match": {"onset": "Sudden", "symptoms": ["Stridor", "Wheezing"]},
                "differentiating_factors": "Sudden onset of stridor or wheezing in a child who was previously well. Requires chest X-ray and possible bronchoscopy."
            }
        ]
    },
    # 46-50: Other Common Presentations
    "Eye Pain/Red Eye": {
        "questions": {
            "onset": ["Sudden", "Gradual"],
            "type": ["Painful", "Painless"],
            "vision_changes": ["Yes", "No"],
        },
        "diagnoses": [
            {
                "name": "Conjunctivitis",
                "match": {"onset": "Gradual", "type": "Painless", "vision_changes": "No"},
                "differentiating_factors": "Itching, redness, and discharge. Vision is typically unaffected."
            },
            {
                "name": "Acute Angle-Closure Glaucoma",
                "match": {"onset": "Sudden", "type": "Painful", "vision_changes": "Yes"},
                "differentiating_factors": "Sudden, severe eye pain with blurred vision, halos around lights, and a firm globe on exam. A medical emergency."
            },
            {
                "name": "Corneal Abrasion",
                "match": {"onset": "Sudden", "type": "Painful", "vision_changes": "No"},
                "differentiating_factors": "Sudden eye pain after a foreign body sensation or trauma. Diagnosis with fluorescein stain."
            }
        ]
    },
    "Allergic Reaction": {
        "questions": {
            "symptoms": ["Hives/rash", "Angioedema", "Shortness of breath", "Hypotension"],
            "triggers": ["Food", "Medication", "Insect bite"],
        },
        "diagnoses": [
            {
                "name": "Anaphylaxis",
                "match": {"symptoms": ["Angioedema", "Shortness of breath", "Hypotension"]},
                "differentiating_factors": "A life-threatening, systemic allergic reaction. Requires immediate epinephrine."
            },
            {
                "name": "Urticaria",
                "match": {"symptoms": "Hives/rash"},
                "differentiating_factors": "Hives (urticaria) that are intensely itchy. Not associated with angioedema or shortness of breath."
            }
        ]
    },
    "Poisoning/Toxicity": {
        "questions": {
            "substance": ["Acetaminophen", "Salicylates", "Carbon monoxide"],
            "symptoms": ["Nausea/Vomiting", "Altered mental status", "Tinnitus"],
        },
        "diagnoses": [
            {
                "name": "Acetaminophen Overdose",
                "match": {"substance": "Acetaminophen", "symptoms": "Nausea/Vomiting"},
                "differentiating_factors": "Initially asymptomatic, then presents with nausea and vomiting. Can lead to fatal liver failure. Requires N-acetylcysteine."
            },
            {
                "name": "Salicylate Toxicity",
                "match": {"substance": "Salicylates", "symptoms": "Tinnitus"},
                "differentiating_factors": "Associated with tinnitus, fever, and tachypnea. Can cause a mixed respiratory alkalosis and metabolic acidosis."
            }
        ]
    },
    "Burn": {
        "questions": {
            "severity": ["First-degree", "Second-degree", "Third-degree"],
            "location": ["Hand", "Face", "Genitals", "Torso"],
            "associated_symptoms": ["Pain", "Blisters"],
        },
        "diagnoses": [
            {
                "name": "First-degree Burn",
                "match": {"severity": "First-degree"},
                "differentiating_factors": "Red, painful, and dry skin. No blisters. Heals within a few days."
            },
            {
                "name": "Second-degree Burn",
                "match": {"severity": "Second-degree", "associated_symptoms": "Blisters"},
                "differentiating_factors": "Red, painful, and blistered skin. Can be a partial-thickness burn."
            },
            {
                "name": "Third-degree Burn",
                "match": {"severity": "Third-degree", "associated_symptoms": "None"},
                "differentiating_factors": "Waxy, leathery, and painless. Requires immediate surgical intervention."
            }
        ]
    },
    "Gastrointestinal Bleeding": {
        "questions": {
            "type": ["Hematemesis", "Melena", "Hematochezia"],
            "hemodynamic_status": ["Stable", "Unstable"],
        },
        "diagnoses": [
            {
                "name": "Upper GI Bleed",
                "match": {"type": ["Hematemesis", "Melena"]},
                "differentiating_factors": "Bleeding from a source proximal to the ligament of Treitz. Presents as vomiting blood (hematemesis) or black, tarry stools (melena)."
            },
            {
                "name": "Lower GI Bleed",
                "match": {"type": "Hematochezia"},
                "differentiating_factors": "Bleeding from a source distal to the ligament of Treitz. Presents as bright red blood per rectum."
            }
        ]
    }
}
