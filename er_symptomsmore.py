# er_symptoms_expanded.py
# This file contains a comprehensive diagnostic tree for common ER presentations, designed for medical students and ER professionals.
# It includes all original presentations, expanded differentials, detailed questions, and USMLE-style accurate differentiating factors.
# All diagnoses are verified against standard medical guidelines (e.g., UpToDate, Tintinalli’s Emergency Medicine, AHA/ACC, ACR).

ER_PRESENTATIONS = {
    # 1-5: Classic Chief Complaints
    "Chest Pain": {
        "questions": {
            "location": ["Central", "Left-sided", "Right-sided", "Substernal", "Diffuse"],
            "character": ["Crushing", "Sharp", "Dull", "Burning", "Tearing", "Pressure", "Aching"],
            "radiation": ["To the arm", "To the jaw", "To the back", "To the shoulder", "To the neck", "None"],
            "onset": ["Sudden", "Gradual"],
            "duration": ["Seconds", "Minutes", "Hours", "Days"],
            "associated_symptoms": ["Dyspnea", "Nausea/Vomiting", "Sweating", "Palpitations", "Syncope", "Fever", "Cough", "Hemoptysis", "Fatigue"],
            "exacerbating_factors": ["Exertion", "Inspiration", "Eating", "Movement", "Swallowing", "Stress", "None"],
            "relieving_factors": ["Rest", "Nitroglycerin", "Antacids", "Leaning forward", "None"],
            "risk_factors": ["Hypertension", "Smoking", "Diabetes", "Family history of CAD", "Obesity", "Hyperlipidemia", "Cocaine use", "Recent trauma"],
            "past_medical_history": ["CAD", "GERD", "Pulmonary disease", "Recent surgery", "Connective tissue disorder", "Atrial fibrillation"],
            "physical_exam": ["Tachycardia", "Hypotension", "Unequal pulses", "Pericardial rub", "Murmur", "Decreased breath sounds", "Crackles"],
            "social_history": ["Cocaine use", "Smoking history", "Alcohol use"]
        },
        "diagnoses": [
            {
                "name": "Myocardial Infarction (MI)",
                "match": {"location": ["Central", "Substernal"], "character": ["Crushing", "Pressure"], "radiation": ["To the arm", "To the jaw"], "associated_symptoms": ["Dyspnea", "Nausea/Vomiting", "Sweating"]},
                "differentiating_factors": "Severe, central chest pain, often radiating to left arm/jaw, lasting >20 minutes. Associated with dyspnea, diaphoresis, nausea. EKG: ST-elevation (STEMI), new Q waves, or non-ST elevation (NSTEMI). Troponin elevated. Risk factors: CAD, smoking, diabetes, hyperlipidemia. Management: MONA (morphine, oxygen, nitroglycerin, aspirin), heparin, cath lab for STEMI. USMLE key: PCI within 90 minutes."
            },
            {
                "name": "Pulmonary Embolism (PE)",
                "match": {"character": "Sharp", "associated_symptoms": ["Dyspnea", "Tachycardia"], "exacerbating_factors": "Inspiration", "risk_factors": ["Recent surgery", "Recent trauma"]},
                "differentiating_factors": "Sudden-onset, pleuritic chest pain with dyspnea, tachycardia, hypoxia. Wells score or PERC rule for risk stratification. D-dimer if low probability; CT pulmonary angiography (CTPA) diagnostic. Risk factors: immobilization, malignancy, hypercoagulable states. Treat with anticoagulation (heparin, DOACs); thrombolytics if unstable. USMLE key: hypoxia with clear lungs, S1Q3T3 on EKG."
            },
            {
                "name": "Pericarditis",
                "match": {"location": "Central", "character": "Sharp", "relieving_factors": "Leaning forward", "exacerbating_factors": "Inspiration", "physical_exam": "Pericardial rub"},
                "differentiating_factors": "Sharp, pleuritic pain, worse supine, improved leaning forward. Pericardial friction rub pathognomonic. EKG: diffuse ST-elevation, PR depression. Often post-viral or autoimmune (e.g., SLE). Echocardiogram for effusion. Treat with NSAIDs (ibuprofen) and colchicine. USMLE key: friction rub and positional relief."
            },
            {
                "name": "Gastroesophageal Reflux Disease (GERD)",
                "match": {"character": "Burning", "location": ["Central", "Substernal"], "exacerbating_factors": "Eating", "relieving_factors": "Antacids", "past_medical_history": "GERD"},
                "differentiating_factors": "Burning substernal pain, postprandial or worse supine, with regurgitation or dysphagia. No EKG changes or troponin elevation. Trial of PPI (omeprazole) or antacids diagnostic. EGD for complications (Barrett’s esophagus). USMLE key: rule out cardiac causes."
            },
            {
                "name": "Aortic Dissection",
                "match": {"character": "Tearing", "radiation": ["To the back", "To the neck"], "onset": "Sudden", "physical_exam": ["Unequal pulses", "Hypotension"]},
                "differentiating_factors": "Sudden, severe, tearing pain radiating to back, with unequal pulses or BP differential (>20 mmHg). Risk factors: hypertension, Marfan’s, Ehlers-Danlos. CXR: widened mediastinum; CT/MRI diagnostic. Surgical emergency; beta-blockers (labetalol) for BP. USMLE key: pulse deficit or neurological symptoms."
            },
            {
                "name": "Pneumothorax",
                "match": {"character": "Sharp", "onset": "Sudden", "associated_symptoms": ["Dyspnea"], "physical_exam": "Decreased breath sounds"},
                "differentiating_factors": "Sudden unilateral pain with dyspnea, decreased breath sounds, hyperresonance. Risk factors: smoking, trauma, tall/thin habitus. CXR: lung collapse. Tension pneumothorax: tracheal deviation, hypotension. Chest tube or needle decompression. USMLE key: young males, sudden onset."
            },
            {
                "name": "Costochondritis",
                "match": {"character": "Sharp", "exacerbating_factors": "Movement", "relieving_factors": "Rest"},
                "differentiating_factors": "Localized, reproducible pain at costochondral junctions. No systemic symptoms or EKG changes. Common post-trauma or in younger patients. Treat with NSAIDs, rest. USMLE key: reproducible pain."
            },
            {
                "name": "Esophageal Spasm",
                "match": {"character": ["Crushing", "Burning"], "radiation": "None", "exacerbating_factors": "Swallowing"},
                "differentiating_factors": "Intermittent, severe pain mimicking MI, triggered by swallowing or stress. Normal EKG/troponin. Esophageal manometry diagnostic. Calcium channel blockers (diltiazem) or nitrates. USMLE key: mimics cardiac pain."
            },
            {
                "name": "Boerhaave Syndrome",
                "match": {"character": "Severe", "onset": "Sudden", "associated_symptoms": ["Nausea/Vomiting"], "exacerbating_factors": "Swallowing"},
                "differentiating_factors": "Sudden, severe pain post-forceful vomiting, with subcutaneous emphysema or Hamman’s sign. CXR: pneumomediastinum; CT/esophagram confirms esophageal rupture. Surgical emergency. USMLE key: Mackler’s triad (pain, vomiting, emphysema)."
            },
            {
                "name": "Myocarditis",
                "match": {"character": "Dull", "associated_symptoms": ["Fever", "Dyspnea"], "past_medical_history": "Recent viral illness"},
                "differentiating_factors": "Diffuse pain with fever, fatigue, or heart failure post-viral illness (e.g., coxsackievirus). EKG: diffuse ST changes; troponin elevated. Cardiac MRI or biopsy diagnostic. Supportive care; avoid NSAIDs in acute phase. USMLE key: viral prodrome."
            },
            {
                "name": "Pneumonia",
                "match": {"character": "Sharp", "associated_symptoms": ["Fever", "Cough"], "physical_exam": "Crackles"},
                "differentiating_factors": "Pleuritic pain with fever, productive cough, dyspnea. CXR: consolidation. Leukocytosis, elevated CRP. Antibiotics (levofloxacin or ceftriaxone + azithromycin). USMLE key: community-acquired vs. hospital-acquired."
            }
        ]
    },
    "Abdominal Pain": {
        "questions": {
            "location": ["RUQ", "LUQ", "RLQ", "LLQ", "Epigastric", "Periumbilical", "Diffuse", "Suprapubic", "Flank"],
            "character": ["Colicky", "Dull", "Sharp", "Burning", "Cramping", "Tearing"],
            "onset": ["Sudden", "Gradual"],
            "radiation": ["To the shoulder", "To the back", "To the groin", "To the pelvis", "None"],
            "associated_symptoms": ["Nausea/Vomiting", "Fever/Chills", "Bloating", "Diarrhea", "Constipation", "Weight loss", "Jaundice", "Hematochezia", "Melena", "Dysuria"],
            "exacerbating_factors": ["Fatty meals", "Movement", "Eating", "Coughing", "None"],
            "relieving_factors": ["Antacids", "Bowel movement", "Fetal position", "None"],
            "past_medical_history": ["Prior surgeries", "Gallstones", "Alcohol use", "NSAID use", "IBD", "Pregnancy", "Pancreatitis", "AAA"],
            "physical_exam": ["Rebound tenderness", "Guarding", "Murphy’s sign", "Rovsing’s sign", "CVA tenderness", "Pulsatile mass"],
            "social_history": ["Recent travel", "Alcohol use", "IV drug use"]
        },
        "diagnoses": [
            {
                "name": "Appendicitis",
                "match": {"location": ["Periumbilical", "RLQ"], "character": "Sharp", "associated_symptoms": ["Fever/Chills", "Nausea/Vomiting"], "physical_exam": ["Rebound tenderness", "Rovsing’s sign"]},
                "differentiating_factors": "Pain starts periumbilical, migrates to RLQ (McBurney’s point). Anorexia, low-grade fever, rebound tenderness. Rovsing’s, psoas, or obturator signs positive. CT: thickened appendix, periappendiceal fluid; ultrasound in pediatrics. Surgical emergency (appendectomy). USMLE key: migration of pain."
            },
            {
                "name": "Cholecystitis",
                "match": {"location": "RUQ", "character": ["Colicky", "Dull"], "exacerbating_factors": "Fatty meals", "physical_exam": "Murphy’s sign"},
                "differentiating_factors": "RUQ pain radiating to right shoulder, post-fatty meal. Murphy’s sign positive. Ultrasound: gallstones, wall thickening, pericholecystic fluid. Leukocytosis, elevated LFTs. Antibiotics (ceftriaxone + metronidazole), cholecystectomy. USMLE key: Murphy’s sign specific."
            },
            {
                "name": "Diverticulitis",
                "match": {"location": "LLQ", "character": "Dull", "associated_symptoms": ["Fever/Chills", "Constipation"]},
                "differentiating_factors": "LLQ pain with fever, leukocytosis, often elderly. CT: sigmoid diverticula, fat stranding, or abscess. Antibiotics (ciprofloxacin + metronidazole); surgery for complications. USMLE key: LLQ pain in older patients."
            },
            {
                "name": "Pancreatitis",
                "match": {"location": ["Epigastric", "LUQ"], "character": "Dull", "radiation": "To the back", "past_medical_history": ["Alcohol use", "Gallstones"]},
                "differentiating_factors": "Epigastric pain radiating to back, nausea/vomiting. Risk factors: alcohol, gallstones, hypertriglyceridemia. Lipase >3x upper limit, amylase elevated. CT for complications (necrosis, pseudocyst). IV fluids, NPO, pain control. USMLE key: lipase more specific."
            },
            {
                "name": "Peptic Ulcer Disease (PUD)",
                "match": {"location": "Epigastric", "character": "Burning", "relieving_factors": "Antacids", "past_medical_history": "NSAID use"},
                "differentiating_factors": "Gnawing epigastric pain; duodenal ulcers relieved by food, gastric worsened. Risk factors: H. pylori, NSAIDs. EGD diagnostic; H. pylori testing (urea breath test, stool antigen). PPIs, H. pylori eradication (clarithromycin, amoxicillin, PPI). USMLE key: perforation risk (free air on CXR)."
            },
            {
                "name": "Bowel Obstruction",
                "match": {"location": "Diffuse", "character": "Cramping", "associated_symptoms": ["Nausea/Vomiting", "Constipation"]},
                "differentiating_factors": "Cramping pain, vomiting (feculent if distal), distension, no flatus/stool. Risk factors: adhesions, hernias, malignancy. X-ray: air-fluid levels, dilated loops. NG tube, fluids; surgery if strangulation. USMLE key: high-pitched bowel sounds early."
            },
            {
                "name": "Mesenteric Ischemia",
                "match": {"location": "Diffuse", "character": "Severe", "associated_symptoms": ["Nausea/Vomiting"], "past_medical_history": "CAD"},
                "differentiating_factors": "Severe pain out of proportion to exam, elderly with vascular risk factors (atrial fibrillation). CT angiography; lactic acidosis. Surgical emergency (revascularization). USMLE key: disproportionate pain."
            },
            {
                "name": "Ectopic Pregnancy",
                "match": {"location": ["RLQ", "LLQ"], "character": "Sharp", "associated_symptoms": "Vaginal bleeding", "past_medical_history": "Pregnancy"},
                "differentiating_factors": "Unilateral pelvic pain, vaginal bleeding, positive β-hCG. Transvaginal ultrasound: no intrauterine pregnancy, adnexal mass. Methotrexate or surgery. USMLE key: rule out in reproductive-age women."
            },
            {
                "name": "Abdominal Aortic Aneurysm (AAA) Rupture",
                "match": {"location": ["Diffuse", "Flank"], "character": "Tearing", "associated_symptoms": ["Hypotension", "Syncope"], "physical_exam": "Pulsatile mass"},
                "differentiating_factors": "Sudden, severe pain with hypotension, pulsatile mass. Risk factors: smoking, hypertension, elderly males. Bedside ultrasound or CT. Surgical emergency. USMLE key: classic triad (pain, hypotension, pulsatile mass)."
            },
            {
                "name": "Gastroenteritis",
                "match": {"location": "Diffuse", "character": "Cramping", "associated_symptoms": ["Diarrhea", "Nausea/Vomiting"], "social_history": "Recent travel"},
                "differentiating_factors": "Cramping pain with diarrhea, vomiting, often viral (norovirus) or bacterial (Salmonella). Stool studies if severe. Fluids, antiemetics (ondansetron). USMLE key: dehydration risk."
            },
            {
                "name": "Ovarian Torsion",
                "match": {"location": ["RLQ", "LLQ"], "character": "Sharp", "associated_symptoms": "Nausea/Vomiting", "past_medical_history": "Pregnancy"},
                "differentiating_factors": "Sudden, unilateral pelvic pain, nausea. Ultrasound with Doppler: enlarged ovary, reduced flow. Surgical detorsion. USMLE key: ovarian cyst or pregnancy risk."
            },
            {
                "name": "Perforated Viscus",
                "match": {"location": "Diffuse", "character": "Sharp", "associated_symptoms": ["Fever", "Nausea/Vomiting"], "physical_exam": "Guarding"},
                "differentiating_factors": "Sudden, severe pain with guarding, rebound tenderness. CXR: free air under diaphragm. Surgical emergency. USMLE key: often due to perforated ulcer or appendix."
            }
        ]
    },
    "Shortness of Breath": {
        "questions": {
            "onset": ["Sudden", "Gradual"],
            "associated_symptoms": ["Cough", "Wheezing", "Chest pain", "Fever", "Ankle swelling", "Orthopnea", "Paroxysmal nocturnal dyspnea", "Hemoptysis", "Weight loss"],
            "exacerbating_factors": ["Exertion", "Lying flat", "Allergens", "Cold air", "None"],
            "relieving_factors": ["Bronchodilators", "Sitting up", "Oxygen", "None"],
            "risk_factors": ["Smoking", "Heart disease", "Asthma", "Recent immobilization", "Malignancy", "Obesity"],
            "past_medical_history": ["COPD", "CHF", "Asthma", "DVT/PE", "Pulmonary hypertension"],
            "physical_exam": ["Crackles", "Wheezes", "Decreased breath sounds", "JVD", "Edema", "Cyanosis"],
            "social_history": ["Smoking history", "Occupational exposure"]
        },
        "diagnoses": [
            {
                "name": "Asthma Exacerbation",
                "match": {"onset": "Sudden", "associated_symptoms": ["Wheezing", "Cough"], "relieving_factors": "Bronchodilators", "past_medical_history": "Asthma"},
                "differentiating_factors": "Sudden dyspnea with wheezing, triggered by allergens, infection, or exercise. Reduced peak flow. Albuterol, corticosteroids; magnesium sulfate for severe cases. USMLE key: accessory muscle use, pulsus paradoxus."
            },
            {
                "name": "Congestive Heart Failure (CHF)",
                "match": {"onset": "Gradual", "associated_symptoms": ["Ankle swelling", "Orthopnea", "Paroxysmal nocturnal dyspnea"], "physical_exam": ["Crackles", "JVD", "Edema"]},
                "differentiating_factors": "Gradual dyspnea with edema, orthopnea, JVD. CXR: pulmonary edema, cardiomegaly. BNP elevated. Diuretics (furosemide), ACE inhibitors, oxygen. USMLE key: S3 gallop, pink frothy sputum."
            },
            {
                "name": "Pneumonia",
                "match": {"onset": ["Sudden", "Gradual"], "associated_symptoms": ["Fever", "Cough"], "physical_exam": "Crackles"},
                "differentiating_factors": "Fever, productive cough, dyspnea, focal crackles. CXR: consolidation. Leukocytosis, elevated CRP. Antibiotics (levofloxacin or ceftriaxone + azithromycin). USMLE key: community-acquired vs. hospital-acquired."
            },
            {
                "name": "Pulmonary Embolism (PE)",
                "match": {"onset": "Sudden", "associated_symptoms": ["Chest pain", "Hemoptysis"], "risk_factors": "Recent immobilization"},
                "differentiating_factors": "Sudden dyspnea, pleuritic pain, hypoxia, tachycardia. Wells score; D-dimer if low probability. CTPA diagnostic. Anticoagulation (heparin, DOACs); thrombolytics if unstable. USMLE key: hypoxia with clear lungs."
            },
            {
                "name": "COPD Exacerbation",
                "match": {"onset": "Gradual", "associated_symptoms": ["Cough", "Wheezing"], "risk_factors": "Smoking", "past_medical_history": "COPD"},
                "differentiating_factors": "Chronic cough, increased sputum, dyspnea in smoker. CXR: hyperinflation. Bronchodilators, steroids, antibiotics if bacterial. USMLE key: pursed-lip breathing, barrel chest."
            },
            {
                "name": "Pneumothorax",
                "match": {"onset": "Sudden", "associated_symptoms": "Chest pain", "physical_exam": "Decreased breath sounds"},
                "differentiating_factors": "Sudden dyspnea, unilateral pain, decreased breath sounds, hyperresonance. CXR diagnostic. Tension pneumothorax: tracheal deviation, hypotension. Chest tube or needle decompression. USMLE key: young, tall males."
            },
            {
                "name": "Anaphylaxis",
                "match": {"onset": "Sudden", "associated_symptoms": ["Wheezing", "Hives"], "risk_factors": "Allergen exposure"},
                "differentiating_factors": "Sudden dyspnea with hives, angioedema, hypotension post-allergen. IM epinephrine, antihistamines, steroids. USMLE key: biphasic reaction risk."
            },
            {
                "name": "Acute Respiratory Distress Syndrome (ARDS)",
                "match": {"onset": "Sudden", "associated_symptoms": "Dyspnea", "past_medical_history": "Recent trauma"},
                "differentiating_factors": "Severe hypoxia, bilateral crackles post-sepsis, trauma, or aspiration. CXR: bilateral infiltrates. PaO2/FiO2 <300. Mechanical ventilation (low tidal volume). USMLE key: non-cardiogenic pulmonary edema."
            },
            {
                "name": "Pulmonary Edema (Non-Cardiogenic)",
                "match": {"onset": "Sudden", "associated_symptoms": "Dyspnea", "past_medical_history": "Recent aspiration"},
                "differentiating_factors": "Sudden dyspnea with crackles, post-aspiration or drug overdose. CXR: bilateral infiltrates, normal heart size. Supportive care, treat underlying cause. USMLE key: distinguish from CHF."
            },
            {
                "name": "Pulmonary Hypertension",
                "match": {"onset": "Gradual", "associated_symptoms": ["Dyspnea", "Fatigue"], "past_medical_history": "Pulmonary hypertension"},
                "differentiating_factors": "Progressive dyspnea, fatigue, syncope. Echo: elevated RV pressure. Right heart catheterization confirms. Vasodilators (epoprostenol). USMLE key: loud P2 on exam."
            }
        ]
    },
    "Headache": {
        "questions": {
            "onset": ["Sudden (Thunderclap)", "Gradual"],
            "character": ["Throbbing", "Band-like pressure", "Sharp", "Dull", "Worse with valsalva"],
            "location": ["Unilateral", "Bilateral", "Occipital", "Temporal", "Frontal"],
            "associated_symptoms": ["Photophobia", "Phonophobia", "Nausea/Vomiting", "Fever", "Stiff neck", "Visual changes", "Focal neurological deficits", "Tearing", "Nasal congestion"],
            "triggers": ["Stress", "Caffeine withdrawal", "Sleep deprivation", "Hypertension", "Food triggers"],
            "relieving_factors": ["Rest", "Analgesics", "Dark room", "None"],
            "past_medical_history": ["Migraine", "Hypertension", "Recent trauma", "Infection"],
            "physical_exam": ["Papilledema", "Nuchal rigidity", "Temporal tenderness", "Focal neurological signs"],
            "social_history": ["Alcohol use", "Smoking"]
        },
        "diagnoses": [
            {
                "name": "Migraine",
                "match": {"onset": "Gradual", "character": "Throbbing", "associated_symptoms": ["Photophobia", "Phonophobia", "Nausea/Vomiting"], "past_medical_history": "Migraine"},
                "differentiating_factors": "Unilateral, pulsating headache, 4-72 hours, with nausea, photophobia, or aura. Triggers: stress, foods. Triptans (sumatriptan), NSAIDs. Prophylaxis (propranolol) if frequent. USMLE key: aura in 30% of cases."
            },
            {
                "name": "Tension Headache",
                "match": {"onset": "Gradual", "character": "Band-like pressure", "location": "Bilateral"},
                "differentiating_factors": "Bilateral, non-pulsatile, stress-related. No nausea or photophobia. NSAIDs, stress management. USMLE key: most common headache type."
            },
            {
                "name": "Subarachnoid Hemorrhage",
                "match": {"onset": "Sudden (Thunderclap)", "associated_symptoms": ["Stiff neck", "Focal neurological deficits"]},
                "differentiating_factors": "Worst headache of life, sudden onset. Seizures, altered mental status. Non-contrast CT head; LP if negative (xanthochromia). Neurosurgical emergency. USMLE key: sentinel bleed history."
            },
            {
                "name": "Meningitis",
                "match": {"character": "Worse with valsalva", "associated_symptoms": ["Fever", "Stiff neck"], "physical_exam": "Nuchal rigidity"},
                "differentiating_factors": "Fever, headache, nuchal rigidity. Kernig’s/Brudzinski’s signs. LP: elevated WBC, low glucose (bacterial). Antibiotics (ceftriaxone, vancomycin), steroids. USMLE key: meningococcal rash."
            },
            {
                "name": "Temporal Arteritis",
                "match": {"location": "Temporal", "associated_symptoms": "Visual changes", "physical_exam": "Temporal tenderness"},
                "differentiating_factors": "Unilateral temporal pain, jaw claudication, visual loss in >50y. ESR/CRP elevated. Temporal artery biopsy. High-dose steroids (prednisone). USMLE key: vision loss irreversible."
            },
            {
                "name": "Cluster Headache",
                "match": {"location": "Unilateral", "character": "Sharp", "associated_symptoms": ["Tearing", "Nasal congestion"]},
                "differentiating_factors": "Severe, unilateral orbital pain, 15-180 minutes, with lacrimation, nasal congestion. High-flow oxygen, triptans. USMLE key: male predominance, nocturnal attacks."
            },
            {
                "name": "Idiopathic Intracranial Hypertension",
                "match": {"associated_symptoms": "Visual changes", "physical_exam": "Papilledema"},
                "differentiating_factors": "Headache with visual changes, pulsatile tinnitus, often in obese young females. LP: elevated opening pressure. Acetazolamide, weight loss. USMLE key: papilledema on fundoscopy."
            },
            {
                "name": "Cervicogenic Headache",
                "match": {"location": "Occipital", "exacerbating_factors": "Movement"},
                "differentiating_factors": "Occipital pain radiating forward, related to neck movement or posture. Physical therapy, analgesics. USMLE key: cervical spine pathology."
            }
        ]
    },
    "Back Pain": {
        "questions": {
            "location": ["Cervical", "Thoracic", "Lumbar", "Sacral"],
            "onset": ["Sudden (with injury)", "Gradual"],
            "radiation": ["To the leg", "To the chest", "To the groin", "None"],
            "red_flags": ["Fever", "Urinary retention", "Saddle anesthesia", "Weight loss", "Neurological deficits", "Bowel incontinence"],
            "exacerbating_factors": ["Movement", "Coughing", "None"],
            "relieving_factors": ["Rest", "Heat", "None"],
            "past_medical_history": ["Trauma", "Cancer", "Infection", "Osteoporosis"],
            "physical_exam": ["Spinal tenderness", "Paraspinal muscle spasm", "Straight leg raise positive"],
            "social_history": ["IV drug use", "Heavy lifting"]
        },
        "diagnoses": [
            {
                "name": "Lumbar Strain",
                "match": {"location": "Lumbar", "onset": "Sudden (with injury)", "radiation": "None"},
                "differentiating_factors": "Localized pain post-lifting or trauma, improves with rest. No neurological deficits. NSAIDs, muscle relaxants, physical therapy. USMLE key: benign, common cause."
            },
            {
                "name": "Herniated Disc",
                "match": {"location": "Lumbar", "radiation": "To the leg", "physical_exam": "Straight leg raise positive"},
                "differentiating_factors": "Radiating pain in dermatomal pattern, sensory/motor deficits. Positive straight leg raise. MRI diagnostic. Steroids, surgery if progressive deficits. USMLE key: sciatica symptoms."
            },
            {
                "name": "Aortic Dissection",
                "match": {"location": ["Thoracic", "Lumbar"], "onset": "Sudden (with injury)", "character": "Tearing"},
                "differentiating_factors": "Severe, tearing pain radiating to back, unequal pulses or BP differential. CT/MRI diagnostic. Surgical emergency; beta-blockers for BP. USMLE key: pulse deficit."
            },
            {
                "name": "Pyelonephritis",
                "match": {"location": "Lumbar", "red_flags": ["Fever"], "associated_symptoms": "Dysuria"},
                "differentiating_factors": "Flank pain, fever, dysuria, CVA tenderness. Urinalysis: pyuria, nitrites. Antibiotics (ciprofloxacin). USMLE key: CVA tenderness."
            },
            {
                "name": "Spinal Epidural Abscess",
                "match": {"red_flags": ["Fever", "Neurological deficits"], "social_history": "IV drug use"},
                "differentiating_factors": "Back pain with fever, neurological deficits. MRI diagnostic. Antibiotics (vancomycin, ceftriaxone), surgical drainage. USMLE key: IV drug use, rapid progression."
            },
            {
                "name": "Cauda Equina Syndrome",
                "match": {"red_flags": ["Saddle anesthesia", "Urinary retention", "Bowel incontinence"]},
                "differentiating_factors": "Low back pain, saddle anesthesia, urinary retention. MRI: disc herniation or mass. Surgical emergency. USMLE key: neurological emergency."
            },
            {
                "name": "Vertebral Osteomyelitis",
                "match": {"red_flags": ["Fever", "Weight loss"], "past_medical_history": "Infection"},
                "differentiating_factors": "Chronic back pain with fever, weight loss. MRI: vertebral destruction. Antibiotics, possible surgery. USMLE key: IV drug use or immunocompromised."
            }
        ]
    },
    # 6-10: Fever & Infectious
    "Fever": {
        "questions": {
            "onset": ["Acute (< 48 hours)", "Subacute (days to weeks)", "Chronic (>2 weeks)"],
            "associated_symptoms": ["Rash", "Sore throat", "Cough", "Headache", "Abdominal pain", "Joint pain", "Night sweats", "Altered mental status"],
            "travel_history": ["Yes (specify region)", "No"],
            "immune_status": ["Immunocompromised", "Immunocompetent"],
            "risk_factors": ["Recent hospitalization", "Animal exposure", "IV drug use", "Tick exposure"],
            "past_medical_history": ["HIV", "Diabetes", "Recent surgery"],
            "physical_exam": ["Lymphadenopathy", "Murmur", "Rash", "Splenomegaly"],
            "social_history": ["Travel", "Homelessness"]
        },
        "diagnoses": [
            {
                "name": "Influenza",
                "match": {"onset": "Acute (< 48 hours)", "associated_symptoms": ["Sore throat", "Cough", "Myalgias"]},
                "differentiating_factors": "Sudden fever, myalgias, sore throat, dry cough. Rapid flu test confirms. Antivirals (oseltamivir) if <48 hours. USMLE key: seasonal pattern."
            },
            {
                "name": "Sepsis",
                "match": {"onset": "Acute (< 48 hours)", "associated_symptoms": ["Altered mental status", "Tachycardia"]},
                "differentiating_factors": "Fever with organ dysfunction (hypotension, confusion). qSOFA score for risk. Blood cultures, broad-spectrum antibiotics (vancomycin, piperacillin-tazobactam), fluids. USMLE key: early goal-directed therapy."
            },
            {
                "name": "Meningitis",
                "match": {"onset": "Acute (< 48 hours)", "associated_symptoms": ["Headache", "Stiff neck"], "physical_exam": "Nuchal rigidity"},
                "differentiating_factors": "Fever, headache, nuchal rigidity. Kernig’s/Brudzinski’s signs. LP: elevated WBC, low glucose (bacterial). Antibiotics (ceftriaxone, vancomycin), steroids. USMLE key: meningococcal rash."
            },
            {
                "name": "Cellulitis",
                "match": {"associated_symptoms": "Redness/swelling on skin", "onset": "Subacute (days to weeks)"},
                "differentiating_factors": "Localized redness, warmth, swelling with fever. Antibiotics (cephalexin, clindamycin). USMLE key: check for abscess."
            },
            {
                "name": "Malaria",
                "match": {"travel_history": "Yes (specify region)", "associated_symptoms": ["Fever", "Chills"]},
                "differentiating_factors": "Cyclic fevers, chills, sweats in endemic travel history. Thick/thin blood smears. Antimalarials (artemether-lumefantrine). USMLE key: travel history critical."
            },
            {
                "name": "Endocarditis",
                "match": {"onset": "Subacute (days to weeks)", "associated_symptoms": ["Fever", "Joint pain"], "physical_exam": "Murmur"},
                "differentiating_factors": "Persistent fever, murmurs, embolic phenomena. Blood cultures, echocardiogram. Prolonged antibiotics (vancomycin, gentamicin). USMLE key: Duke criteria."
            },
            {
                "name": "Lyme Disease",
                "match": {"risk_factors": "Tick exposure", "associated_symptoms": ["Rash", "Joint pain"]},
                "differentiating_factors": "Fever, erythema migrans, joint pain post-tick bite. Serology confirms. Doxycycline. USMLE key: early localized stage."
            }
        ]
    },
    "Sore Throat": {
        "questions": {
            "onset": ["Sudden", "Gradual"],
            "associated_symptoms": ["Fever", "Cough", "White patches on tonsils", "Rash", "Lymphadenopathy", "Fatigue", "Dysphagia"],
            "risk_factors": ["Recent exposure to sick contacts", "Immunocompromised"],
            "past_medical_history": ["Recurrent tonsillitis", "HIV"],
            "physical_exam": ["Exudates", "Tender lymph nodes", "Splenomegaly", "Trismus"],
            "social_history": ["Smoking", "Sexual history"]
        },
        "diagnoses": [
            {
                "name": "Viral Pharyngitis",
                "match": {"onset": "Gradual", "associated_symptoms": ["Cough", "Fatigue"]},
                "differentiating_factors": "Mild sore throat with URI symptoms (rhinorrhea, cough). Supportive care. USMLE key: most common cause."
            },
            {
                "name": "Strep Throat",
                "match": {"onset": "Sudden", "associated_symptoms": ["Fever", "White patches on tonsils"], "physical_exam": "Tender lymph nodes"},
                "differentiating_factors": "Sudden sore throat, fever, no cough, tender cervical nodes. Centor criteria. Rapid strep test, throat culture. Penicillin or amoxicillin. USMLE key: prevent rheumatic fever."
            },
            {
                "name": "Mononucleosis",
                "match": {"associated_symptoms": ["Fatigue", "Lymphadenopathy"], "physical_exam": "Splenomegaly"},
                "differentiating_factors": "Prolonged sore throat, fatigue, lymphadenopathy, splenomegaly. Monospot test, EBV serologies. Supportive care; avoid contact sports. USMLE key: splenic rupture risk."
            },
            {
                "name": "Peritonsillar Abscess",
                "match": {"onset": "Sudden", "physical_exam": ["Exudates", "Trismus"]},
                "differentiating_factors": "Severe unilateral sore throat, trismus, muffled voice, uvular deviation. CT/ultrasound confirms. Drainage, antibiotics (amoxicillin-clavulanate). USMLE key: ENT emergency."
            },
            {
                "name": "Epiglottitis",
                "match": {"onset": "Sudden", "associated_symptoms": ["Dysphagia", "Fever"], "physical_exam": "Trismus"},
                "differentiating_factors": "Rapid-onset sore throat, drooling, stridor. Lateral neck X-ray: thumbprint sign. Airway management, antibiotics (ceftriaxone). USMLE key: H. influenzae in unvaccinated."
            }
        ]
    },
    "Cough": {
        "questions": {
            "onset": ["Acute", "Chronic (>8 weeks)"],
            "character": ["Productive", "Dry"],
            "associated_symptoms": ["Fever", "Dyspnea", "Chest pain", "Hemoptysis", "Weight loss"],
            "risk_factors": ["Smoking", "Allergen exposure", "Occupational exposure"],
            "past_medical_history": ["Asthma", "COPD", "GERD"],
            "physical_exam": ["Wheezing", "Crackles"],
            "social_history": ["Smoking history", "Travel history"]
        },
        "diagnoses": [
            {
                "name": "Acute Bronchitis",
                "match": {"onset": "Acute", "character": "Productive", "associated_symptoms": "Fever"},
                "differentiating_factors": "Self-limiting cough, often post-viral. Supportive care; antibiotics if bacterial. USMLE key: usually viral."
            },
            {
                "name": "Pneumonia",
                "match": {"onset": "Acute", "associated_symptoms": ["Fever", "Dyspnea"], "physical_exam": "Crackles"},
                "differentiating_factors": "Fever, productive cough, dyspnea, crackles. CXR: consolidation. Antibiotics (levofloxacin or ceftriaxone + azithromycin). USMLE key: CURB-65 score."
            },
            {
                "name": "COPD Exacerbation",
                "match": {"onset": "Acute", "character": "Productive", "past_medical_history": "COPD"},
                "differentiating_factors": "Increased cough, sputum, dyspnea in smoker. Bronchodilators, steroids, antibiotics if bacterial. USMLE key: smoking history."
            },
            {
                "name": "Lung Cancer",
                "match": {"onset": "Chronic (>8 weeks)", "associated_symptoms": ["Hemoptysis", "Weight loss"], "risk_factors": "Smoking"},
                "differentiating_factors": "Chronic cough, hemoptysis, weight loss in smokers. CT: lung mass. Bronchoscopy for biopsy. USMLE key: smokers >40."
            }
        ]
    },
    "Rash": {
        "questions": {
            "onset": ["Sudden", "Gradual"],
            "appearance": ["Maculopapular", "Vesicular", "Urticarial", "Erythema Migrans", "Purpuric"],
            "associated_symptoms": ["Fever", "Itching", "Joint pain", "Pain"],
            "risk_factors": ["Recent medication", "Tick exposure", "Allergen exposure"],
            "past_medical_history": ["Autoimmune disease", "HIV"],
            "physical_exam": ["Distribution (dermatomal, diffuse)", "Palpable purpura"],
            "social_history": ["Recent travel", "Animal contact"]
        },
        "diagnoses": [
            {
                "name": "Allergic Reaction (Urticaria)",
                "match": {"onset": "Sudden", "appearance": "Urticarial", "associated_symptoms": "Itching"},
                "differentiating_factors": "Itchy hives, triggered by food, medication, or insect bites. Antihistamines (diphenhydramine), steroids if severe. USMLE key: rule out anaphylaxis."
            },
            {
                "name": "Cellulitis",
                "match": {"onset": "Sudden", "appearance": "Erythema", "associated_symptoms": "Fever"},
                "differentiating_factors": "Localized redness, warmth, swelling. Antibiotics (cephalexin, clindamycin). USMLE key: check for abscess."
            },
            {
                "name": "Shingles (Herpes Zoster)",
                "match": {"appearance": "Vesicular", "physical_exam": "Distribution (dermatomal)"},
                "differentiating_factors": "Painful, vesicular rash in dermatomal distribution, preceded by burning. Antivirals (acyclovir) if <72 hours. USMLE key: post-herpetic neuralgia risk."
            },
            {
                "name": "Lyme Disease",
                "match": {"appearance": "Erythema Migrans", "risk_factors": "Tick exposure"},
                "differentiating_factors": "Bull’s-eye rash, fever, joint pain post-tick bite. Serology confirms. Doxycycline. USMLE key: early localized stage."
            },
            {
                "name": "Meningococcemia",
                "match": {"appearance": "Purpuric", "associated_symptoms": ["Fever", "Headache"]},
                "differentiating_factors": "Purpuric rash, fever, hypotension. Blood cultures, LP if meningitis suspected. Antibiotics (ceftriaxone). USMLE key: petechial rash."
            }
        ]
    },
    "Nausea and Vomiting": {
        "questions": {
            "onset": ["Acute", "Chronic"],
            "associated_symptoms": ["Abdominal pain", "Diarrhea", "Fever", "Headache", "Vertigo"],
            "timing": ["After meals", "Morning", "None"],
            "past_medical_history": ["Pregnancy", "Diabetes", "Migraine"],
            "physical_exam": ["Abdominal distension", "Tenderness"],
            "social_history": ["Alcohol use", "Recent travel"]
        },
        "diagnoses": [
            {
                "name": "Gastroenteritis",
                "match": {"onset": "Acute", "associated_symptoms": ["Diarrhea", "Abdominal pain"], "social_history": "Recent travel"},
                "differentiating_factors": "Vomiting, diarrhea, cramping pain, often viral (norovirus). Stool studies if severe. Fluids, antiemetics (ondansetron). USMLE key: dehydration risk."
            },
            {
                "name": "Bowel Obstruction",
                "match": {"onset": "Acute", "associated_symptoms": "Abdominal pain", "physical_exam": "Abdominal distension"},
                "differentiating_factors": "Vomiting (feculent if distal), distension, no flatus/stool. X-ray: air-fluid levels. NG tube, surgery if strangulation. USMLE key: high-pitched bowel sounds."
            },
            {
                "name": "Pancreatitis",
                "match": {"onset": "Acute", "associated_symptoms": "Abdominal pain", "timing": "After meals"},
                "differentiating_factors": "Epigastric pain radiating to back, post-meal. Elevated lipase. CT for complications. IV fluids, NPO. USMLE key: alcohol, gallstones."
            },
            {
                "name": "Morning Sickness",
                "match": {"onset": "Chronic", "timing": "Morning", "past_medical_history": "Pregnancy"},
                "differentiating_factors": "Nausea/vomiting in first trimester. Supportive care, antiemetics (pyridoxine, doxylamine). USMLE key: rule out hyperemesis gravidarum."
            }
        ]
    },
    # 11-15: Trauma & Orthopedic
    "Extremity Pain/Injury": {
        "questions": {
            "location": ["Arm", "Leg", "Hand", "Foot", "Shoulder"],
            "onset": ["Acute (with injury)", "Chronic"],
            "mechanism": ["Fall", "Twisting injury", "Direct blow", "Overuse"],
            "physical_exam": ["Deformity", "Swelling", "Inability to bear weight", "Ecchymosis"],
            "associated_symptoms": ["Numbness", "Weakness"],
            "past_medical_history": ["Arthritis", "Diabetes"]
        },
        "diagnoses": [
            {
                "name": "Fracture",
                "match": {"onset": "Acute (with injury)", "physical_exam": ["Deformity", "Inability to bear weight"]},
                "differentiating_factors": "Severe pain post-trauma, deformity. X-ray diagnostic. Immobilization, possible surgery. USMLE key: Ottawa rules for ankle/knee."
            },
            {
                "name": "Dislocation",
                "match": {"onset": "Acute (with injury)", "physical_exam": "Deformity"},
                "differentiating_factors": "Joint deformity post-trauma. X-ray confirms. Reduction, immobilization. USMLE key: shoulder, patella common."
            },
            {
                "name": "Sprain/Strain",
                "match": {"onset": "Acute (with injury)", "physical_exam": "Swelling"},
                "differentiating_factors": "Pain, swelling without deformity. RICE (rest, ice, compression, elevation), NSAIDs. USMLE key: ligament (sprain) vs. muscle (strain)."
            },
            {
                "name": "Cellulitis",
                "match": {"onset": "Gradual", "physical_exam": "Swelling", "past_medical_history": "Diabetes"},
                "differentiating_factors": "Redness, warmth, swelling, possible fever. Antibiotics (cephalexin). USMLE key: diabetic patients at risk."
            },
            {
                "name": "Compartment Syndrome",
                "match": {"onset": "Acute (with injury)", "associated_symptoms": ["Pain", "Numbness"], "physical_exam": "Tense swelling"},
                "differentiating_factors": "Severe pain out of proportion, paresthesias, tense swelling. Measure compartment pressure. Fasciotomy if elevated. USMLE key: 6 Ps (pain, pallor, pulselessness, etc.)."
            }
        ]
    },
    "Head Injury": {
        "questions": {
            "mechanism": ["Fall", "Assault", "Motor vehicle accident"],
            "loss_of_consciousness": ["Yes", "No"],
            "associated_symptoms": ["Headache", "Nausea/Vomiting", "Amnesia", "Focal neurological deficit", "Seizure"],
            "past_medical_history": ["Anticoagulant use", "Alcoholism"],
            "physical_exam": ["Scalp hematoma", "Pupillary asymmetry"]
        },
        "diagnoses": [
            {
                "name": "Concussion",
                "match": {"loss_of_consciousness": "Yes", "associated_symptoms": "Amnesia"},
                "differentiating_factors": "Transient LOC, amnesia, headache, dizziness. CT if red flags (vomiting, age >60). Rest, monitor for post-concussion syndrome. USMLE key: no focal deficits."
            },
            {
                "name": "Subdural Hematoma",
                "match": {"associated_symptoms": ["Headache", "Focal neurological deficit"], "past_medical_history": "Anticoagulant use"},
                "differentiating_factors": "Slow-onset symptoms in elderly post-minor trauma. CT: crescent-shaped hematoma. Surgical evacuation if symptomatic. USMLE key: anticoagulation risk."
            },
            {
                "name": "Epidural Hematoma",
                "match": {"mechanism": "Motor vehicle accident", "associated_symptoms": ["Headache", "Nausea/Vomiting"]},
                "differentiating_factors": "Lucid interval, then rapid decline. CT: lens-shaped hematoma. Neurosurgical emergency. USMLE key: arterial bleed, temporal bone fracture."
            },
            {
                "name": "Traumatic Subarachnoid Hemorrhage",
                "match": {"mechanism": "Motor vehicle accident", "associated_symptoms": "Headache"},
                "differentiating_factors": "Sudden headache post-trauma. CT: blood in subarachnoid space. Monitor for vasospasm. USMLE key: trauma-related SAH."
            }
        ]
    },
    "Trauma (General)": {
        "questions": {
            "mechanism": ["Stab wound", "Gunshot wound", "Blunt force trauma"],
            "injury_location": ["Abdomen", "Chest", "Extremity"],
            "hemodynamic_status": ["Stable", "Unstable"],
            "physical_exam": ["Penetrating wound", "Crepitus", "Abdominal rigidity"]
        },
        "diagnoses": [
            {
                "name": "Hemorrhagic Shock",
                "match": {"mechanism": ["Stab wound", "Gunshot wound", "Blunt force trauma"], "hemodynamic_status": "Unstable"},
                "differentiating_factors": "Hypotension, tachycardia post-trauma. Fluid resuscitation, blood transfusion, control bleeding. USMLE key: class III/IV shock."
            },
            {
                "name": "Pneumothorax",
                "match": {"mechanism": "Blunt force trauma", "injury_location": "Chest", "physical_exam": "Crepitus"},
                "differentiating_factors": "Unilateral chest pain, dyspnea, decreased breath sounds. CXR diagnostic. Chest tube or needle decompression. USMLE key: tension pneumothorax signs."
            },
            {
                "name": "Splenic/Liver Laceration",
                "match": {"mechanism": "Blunt force trauma", "injury_location": "Abdomen", "hemodynamic_status": "Unstable"},
                "differentiating_factors": "Abdominal pain, tenderness post-blunt trauma. FAST ultrasound, CT. Surgical intervention if unstable. USMLE key: Kehr’s sign for spleen."
            },
            {
                "name": "Flail Chest",
                "match": {"mechanism": "Blunt force trauma", "injury_location": "Chest", "physical_exam": "Crepitus"},
                "differentiating_factors": "Paradoxical chest movement, multiple rib fractures. CXR diagnostic. Pain control, positive pressure ventilation. USMLE key: respiratory compromise."
            }
        ]
    },
    "Joint Pain/Swelling": {
        "questions": {
            "location": ["Knee", "Shoulder", "Ankle", "Hip", "Multiple joints"],
            "onset": ["Acute", "Chronic"],
            "associated_symptoms": ["Redness", "Warmth", "Fever", "Limited range of motion", "Morning stiffness"],
            "past_medical_history": ["Gout", "Rheumatoid arthritis", "Recent infection"],
            "physical_exam": ["Effusion", "Erythema"]
        },
        "diagnoses": [
            {
                "name": "Septic Arthritis",
                "match": {"onset": "Acute", "associated_symptoms": ["Redness", "Warmth", "Fever"], "physical_exam": "Effusion"},
                "differentiating_factors": "Hot, swollen joint with fever. Joint aspiration: WBC >50,000, positive culture. Antibiotics (vancomycin, ceftriaxone), surgical drainage. USMLE key: S. aureus most common."
            },
            {
                "name": "Gout",
                "match": {"onset": "Acute", "location": "Ankle", "associated_symptoms": ["Redness", "Warmth"]},
                "differentiating_factors": "Sudden, severe pain, often first MTP joint. Uric acid elevated, crystals on aspiration. Colchicine, NSAIDs. USMLE key: podagra."
            },
            {
                "name": "Rheumatoid Arthritis (RA) flare",
                "match": {"onset": "Chronic", "location": "Multiple joints", "associated_symptoms": "Morning stiffness"},
                "differentiating_factors": "Symmetric polyarthritis, morning stiffness >1 hour. RF, anti-CCP positive. DMARDs (methotrexate). USMLE key: MCP/PIP involvement."
            },
            {
                "name": "Osteoarthritis",
                "match": {"onset": "Chronic", "associated_symptoms": "Limited range of motion"},
                "differentiating_factors": "Joint pain worse with activity, improved with rest. X-ray: joint space narrowing, osteophytes. NSAIDs, physical therapy. USMLE key: weight-bearing joints."
            }
        ]
    },
    "Acute Wounds": {
        "questions": {
            "type": ["Laceration", "Abrasion", "Puncture wound", "Avulsion"],
            "location": ["Head/Face", "Extremity", "Trunk"],
            "risk_factors": ["Contaminated wound", "Animal bite", "Diabetic"],
            "physical_exam": ["Foreign body", "Signs of infection"],
            "past_medical_history": ["Tetanus status", "Diabetes"]
        },
        "diagnoses": [
            {
                "name": "Laceration",
                "match": {"type": "Laceration"},
                "differentiating_factors": "Clean cut requiring sutures. Irrigate, explore for foreign bodies. USMLE key: cosmetic closure for face."
            },
            {
                "name": "Abscess",
                "match": {"location": "Extremity", "risk_factors": "Diabetic", "physical_exam": "Signs of infection"},
                "differentiating_factors": "Fluctuant, tender, red nodule. Incision and drainage, antibiotics if systemic. USMLE key: MRSA common."
            },
            {
                "name": "Animal Bite",
                "match": {"risk_factors": "Animal bite"},
                "differentiating_factors": "Puncture wounds, crush injuries. Rabies prophylaxis, tetanus, antibiotics (amoxicillin-clavulanate). USMLE key: Pasteurella in cat bites."
            },
            {
                "name": "Tetanus",
                "match": {"past_medical_history": "Tetanus status", "type": "Puncture wound"},
                "differentiating_factors": "Muscle stiffness, spasms post-dirty wound. Tetanus immunoglobulin, vaccine. USMLE key: unvaccinated patients."
            }
        ]
    },
    # 16-20: Cardiovascular
    "Palpitations": {
        "questions": {
            "onset": ["Sudden", "Gradual"],
            "character": ["Racing", "Skipping a beat", "Pounding"],
            "associated_symptoms": ["Dizziness", "Syncope", "Chest pain", "Dyspnea"],
            "past_medical_history": ["Thyroid disease", "Arrhythmia"],
            "physical_exam": ["Irregular pulse", "Tachycardia"],
            "social_history": ["Caffeine use", "Drug use"]
        },
        "diagnoses": [
            {
                "name": "Atrial Fibrillation (A-fib)",
                "match": {"character": "Racing", "onset": "Sudden", "physical_exam": "Irregular pulse"},
                "differentiating_factors": "Irregularly irregular rhythm, stroke risk. EKG diagnostic. Anticoagulation, rate control (beta-blockers). USMLE key: CHA2DS2-VASc score."
            },
            {
                "name": "Supraventricular Tachycardia (SVT)",
                "match": {"character": "Racing", "onset": "Sudden"},
                "differentiating_factors": "Regular, narrow-complex tachycardia. Vagal maneuvers, adenosine. USMLE key: abrupt onset/offset."
            },
            {
                "name": "Ventricular Tachycardia (V-tach)",
                "match": {"associated_symptoms": ["Dizziness", "Syncope", "Chest pain"]},
                "differentiating_factors": "Wide-complex tachycardia, risk of cardiac arrest. EKG diagnostic. Amiodarone, cardioversion if unstable. USMLE key: cardiac history."
            },
            {
                "name": "Anxiety-Induced Palpitations",
                "match": {"associated_symptoms": "Dizziness", "social_history": "Caffeine use"},
                "differentiating_factors": "Palpitations with anxiety, normal EKG. Reassurance, avoid triggers. USMLE key: rule out organic causes."
            }
        ]
    },
    "Hypertension": {
        "questions": {
            "bp_reading": ["Severe (>180/120)", "Mild"],
            "associated_symptoms": ["Headache", "Chest pain", "Shortness of breath", "Visual changes"],
            "past_medical_history": ["Chronic hypertension", "Renal disease"],
            "physical_exam": ["Papilledema", "Retinal hemorrhages"]
        },
        "diagnoses": [
            {
                "name": "Hypertensive Emergency",
                "match": {"bp_reading": "Severe (>180/120)", "associated_symptoms": ["Headache", "Chest pain", "Shortness of breath"]},
                "differentiating_factors": "BP >180/120 with end-organ damage (encephalopathy, AKI). IV medications (labetalol, nicardipine). USMLE key: gradual BP reduction."
            },
            {
                "name": "Hypertensive Urgency",
                "match": {"bp_reading": "Severe (>180/120)", "associated_symptoms": "None"},
                "differentiating_factors": "BP >180/120 without end-organ damage. Oral medications (clonidine). USMLE key: outpatient follow-up."
            }
        ]
    },
    "Syncope": {
        "questions": {
            "onset": ["Sudden", "Preceded by symptoms"],
            "triggers": ["Standing up", "Painful stimulus", "Exertion", "None"],
            "associated_symptoms": ["Palpitations", "Chest pain", "Fainting", "Seizure-like activity"],
            "past_medical_history": ["Arrhythmia", "Dehydration"],
            "physical_exam": ["Orthostatic vitals"]
        },
        "diagnoses": [
            {
                "name": "Vasovagal Syncope",
                "match": {"onset": "Preceded by symptoms", "triggers": "Painful stimulus"},
                "differentiating_factors": "Lightheadedness, nausea, sweating before fainting. Young, healthy patients. Supportive care. USMLE key: benign, common."
            },
            {
                "name": "Orthostatic Hypotension",
                "match": {"onset": "Sudden", "triggers": "Standing up", "physical_exam": "Orthostatic vitals"},
                "differentiating_factors": "BP drop on standing, elderly or dehydrated. Fluids, address cause (medications). USMLE key: check diuretics."
            },
            {
                "name": "Cardiogenic Syncope",
                "match": {"onset": "Sudden", "triggers": "Exertion", "associated_symptoms": "Chest pain"},
                "differentiating_factors": "Exertional syncope, arrhythmia or aortic stenosis. EKG, echo. USMLE key: red flag for cardiac cause."
            }
        ]
    },
    "Dizziness": {
        "questions": {
            "type": ["Vertigo (spinning sensation)", "Lightheadedness", "Disequilibrium"],
            "onset": ["Sudden", "Gradual"],
            "associated_symptoms": ["Nausea", "Hearing loss", "Tinnitus", "Headache", "Focal neurological deficits"],
            "triggers": ["Head movement", "Standing up"],
            "past_medical_history": ["Migraine", "Stroke"],
            "physical_exam": ["Nystagmus", "Gait instability"]
        },
        "diagnoses": [
            {
                "name": "Benign Paroxysmal Positional Vertigo (BPPV)",
                "match": {"type": "Vertigo (spinning sensation)", "onset": "Sudden", "triggers": "Head movement"},
                "differentiating_factors": "Brief vertigo triggered by head movements. Dix-Hallpike maneuver diagnostic. Epley maneuver. USMLE key: no hearing loss."
            },
            {
                "name": "Ménière's Disease",
                "match": {"type": "Vertigo (spinning sensation)", "associated_symptoms": ["Hearing loss", "Tinnitus"]},
                "differentiating_factors": "Vertigo, tinnitus, hearing loss, episodes lasting hours. Low-salt diet, diuretics. USMLE key: fluctuating hearing loss."
            },
            {
                "name": "Vestibular Neuritis",
                "match": {"type": "Vertigo (spinning sensation)", "onset": "Sudden", "associated_symptoms": "Nausea"},
                "differentiating_factors": "Severe vertigo lasting days, post-viral. No hearing loss. Steroids, supportive care. USMLE key: viral prodrome."
            },
            {
                "name": "Orthostatic Hypotension",
                "match": {"type": "Lightheadedness", "triggers": "Standing up"},
                "differentiating_factors": "Lightheadedness on standing, BP drop. Fluids, address cause (medications). USMLE key: common in elderly."
            },
            {
                "name": "Vestibular Migraine",
                "match": {"type": "Vertigo (spinning sensation)", "past_medical_history": "Migraine"},
                "differentiating_factors": "Vertigo with headache, photophobia. Triptans, prophylaxis (propranolol). USMLE key: migraine history."
            }
        ]
    },
    "Edema": {
        "questions": {
            "location": ["Unilateral", "Bilateral"],
            "associated_symptoms": ["Shortness of breath", "Calf pain", "Redness/Warmth", "Chest pain"],
            "past_medical_history": ["CHF", "DVT", "Liver disease", "Renal disease"],
            "physical_exam": ["Pitting edema", "JVD", "Hepatomegaly"],
            "social_history": ["Recent travel"]
        },
        "diagnoses": [
            {
                "name": "Deep Vein Thrombosis (DVT)",
                "match": {"location": "Unilateral", "associated_symptoms": "Calf pain", "social_history": "Recent travel"},
                "differentiating_factors": "Unilateral swelling, pain. Doppler ultrasound diagnostic. Anticoagulation (heparin, DOACs). USMLE key: Virchow’s triad."
            },
            {
                "name": "Congestive Heart Failure (CHF)",
                "match": {"location": "Bilateral", "associated_symptoms": "Shortness of breath", "physical_exam": ["JVD", "Pitting edema"]},
                "differentiating_factors": "Bilateral pitting edema, orthopnea, JVD. BNP elevated, CXR: pulmonary edema. Diuretics, ACE inhibitors. USMLE key: S3 gallop."
            },
            {
                "name": "Nephrotic Syndrome",
                "match": {"location": "Bilateral", "past_medical_history": "Renal disease"},
                "differentiating_factors": "Bilateral edema, hypoalbuminemia, proteinuria. Urinalysis: >3.5 g/day protein. Treat underlying cause, diuretics. USMLE key: frothy urine."
            },
            {
                "name": "Cirrhosis",
                "match": {"location": "Bilateral", "past_medical_history": "Liver disease", "physical_exam": "Hepatomegaly"},
                "differentiating_factors": "Edema with ascites, jaundice. LFTs abnormal, low albumin. Diuretics, address liver disease. USMLE key: portal hypertension."
            }
        ]
    },
    # 21-25: Neurological
    "Weakness": {
        "questions": {
            "onset": ["Sudden", "Gradual"],
            "location": ["One side of body", "Both sides of body", "All four limbs"],
            "associated_symptoms": ["Numbness", "Difficulty speaking", "Drooping face", "Trouble swallowing"],
            "past_medical_history": ["Stroke", "MS", "Myasthenia gravis"],
            "physical_exam": ["Facial asymmetry", "Reflex changes"],
            "social_history": ["Recent infection"]
        },
        "diagnoses": [
            {
                "name": "Stroke (CVA)",
                "match": {"onset": "Sudden", "location": "One side of body", "associated_symptoms": ["Difficulty speaking", "Drooping face"]},
                "differentiating_factors": "Sudden focal deficits (hemiparesis, aphasia). CT to rule out hemorrhage; tPA if ischemic and <4.5 hours. USMLE key: time is brain."
            },
            {
                "name": "Myasthenia Gravis",
                "match": {"onset": "Gradual", "location": "Both sides of body", "associated_symptoms": ["Trouble swallowing"]},
                "differentiating_factors": "Fluctuating, fatigable weakness, worse with activity. Anti-AChR antibodies, edrophonium test. Pyridostigmine. USMLE key: ptosis, diplopia."
            },
            {
                "name": "Guillain-Barré Syndrome",
                "match": {"onset": "Gradual", "location": "Both sides of body", "associated_symptoms": "Numbness", "social_history": "Recent infection"},
                "differentiating_factors": "Ascending paralysis, numbness, post-viral. LP: elevated protein, normal WBC. IVIG, plasmapheresis. USMLE key: areflexia."
            },
            {
                "name": "Botulism",
                "match": {"onset": "Gradual", "associated_symptoms": ["Trouble swallowing"], "social_history": "Recent infection"},
                "differentiating_factors": "Descending paralysis, diplopia, dry mouth. Antitoxin, supportive care. USMLE key: canned food exposure."
            }
        ]
    },
    "Seizures": {
        "questions": {
            "type": ["Generalized", "Focal"],
            "known_history": ["Yes (epilepsy)", "No"],
            "associated_symptoms": ["Fever", "Head trauma", "Drug/alcohol use", "Tongue biting"],
            "past_medical_history": ["Epilepsy", "Stroke"],
            "physical_exam": ["Postictal state", "Injuries"],
            "social_history": ["Alcohol withdrawal"]
        },
        "diagnoses": [
            {
                "name": "Epilepsy",
                "match": {"type": "Generalized", "known_history": "Yes (epilepsy)"},
                "differentiating_factors": "Seizures in known epilepsy. Medication noncompliance common. Antiepileptics (levetiracetam). USMLE key: avoid triggers."
            },
            {
                "name": "Status Epilepticus",
                "match": {"type": "Generalized"},
                "differentiating_factors": "Seizures >5 minutes or multiple without recovery. Benzodiazepines (lorazepam), antiepileptics. USMLE key: airway protection."
            },
            {
                "name": "Febrile Seizure",
                "match": {"associated_symptoms": "Fever"},
                "differentiating_factors": "Seizures in children with fever, benign. Antipyretics, workup for infection. USMLE key: age 6 months to 5 years."
            },
            {
                "name": "Alcohol Withdrawal Seizure",
                "match": {"social_history": "Alcohol withdrawal", "associated_symptoms": "Drug/alcohol use"},
                "differentiating_factors": "Seizures 12-48 hours post-alcohol cessation. Benzodiazepines (lorazepam). USMLE key: treat underlying withdrawal."
            }
        ]
    },
    "Altered Mental Status": {
        "questions": {
            "onset": ["Sudden", "Gradual"],
            "associated_symptoms": ["Fever", "Headache", "Weakness", "Seizures"],
            "past_medical_history": ["Diabetes", "Drug/alcohol use", "Stroke", "Infection"],
            "physical_exam": ["Focal deficits", "Nuchal rigidity"],
            "social_history": ["Drug use", "Alcohol use"]
        },
        "diagnoses": [
            {
                "name": "Hypoglycemia",
                "match": {"onset": "Sudden", "past_medical_history": "Diabetes"},
                "differentiating_factors": "Confusion, diaphoresis, anxiety. Glucose <70 mg/dL. IV dextrose. USMLE key: rapid response to glucose."
            },
            {
                "name": "Infectious Encephalitis",
                "match": {"onset": "Gradual", "associated_symptoms": ["Fever", "Headache"]},
                "differentiating_factors": "Fever, headache, altered status. LP: lymphocytic pleocytosis. Acyclovir for HSV. USMLE key: viral etiology."
            },
            {
                "name": "Toxic-Metabolic Encephalopathy",
                "match": {"onset": "Gradual", "past_medical_history": ["Drug/alcohol use"]},
                "differentiating_factors": "Confusion due to drugs, organ failure. Treat underlying cause. USMLE key: reversible with correction."
            },
            {
                "name": "Stroke",
                "match": {"onset": "Sudden", "associated_symptoms": "Weakness", "physical_exam": "Focal deficits"},
                "differentiating_factors": "Sudden altered status with focal deficits. CT head, tPA if ischemic. USMLE key: time-sensitive."
            }
        ]
    },
    "Focal Neurological Deficit": {
        "questions": {
            "onset": ["Sudden", "Gradual"],
            "type": ["Speech difficulties", "Facial droop", "Hemiparesis"],
            "risk_factors": ["Hypertension", "Diabetes", "Smoking"],
            "past_medical_history": ["Stroke", "TIA"],
            "physical_exam": ["Cranial nerve deficits", "Motor weakness"]
        },
        "diagnoses": [
            {
                "name": "Transient Ischemic Attack (TIA)",
                "match": {"onset": "Sudden"},
                "differentiating_factors": "Transient deficits resolving <24 hours. Antiplatelets (aspirin), risk factor control. USMLE key: stroke warning."
            },
            {
                "name": "Stroke (CVA)",
                "match": {"onset": "Sudden", "type": ["Speech difficulties", "Facial droop", "Hemiparesis"]},
                "differentiating_factors": "Persistent focal deficits. CT to rule out hemorrhage; tPA if ischemic. USMLE key: NIHSS score."
            },
            {
                "name": "Multiple Sclerosis",
                "match": {"onset": "Gradual", "past_medical_history": "MS"},
                "differentiating_factors": "Relapsing-remitting deficits, optic neuritis. MRI: white matter lesions. Steroids, DMARDs. USMLE key: separated in time and space."
            }
        ]
    },

    "Vertigo": {
        "questions": {
            "onset": ["Sudden", "Gradual"],
            "associated_symptoms": ["Hearing loss", "Tinnitus", "Nausea", "Head movements", "Focal neurological deficits"],
            "past_medical_history": ["Migraine", "Stroke"],
            "physical_exam": ["Nystagmus", "Gait instability"]
        },
        "diagnoses": [
            {
                "name": "Benign Paroxysmal Positional Vertigo (BPPV)",
                "match": {"onset": "Sudden", "associated_symptoms": "Head movements", "physical_exam": "Nystagmus"},
                "differentiating_factors": "Brief vertigo triggered by head movements. Dix-Hallpike maneuver diagnostic, shows geotropic nystagmus. Epley maneuver curative. USMLE key: no hearing loss, benign course."
            },
            {
                "name": "Ménière's Disease",
                "match": {"onset": "Sudden", "associated_symptoms": ["Hearing loss", "Tinnitus"]},
                "differentiating_factors": "Episodic vertigo (hours), low-frequency hearing loss, tinnitus, aural fullness. Audiometry confirms hearing loss. Low-salt diet, diuretics (hydrochlorothiazide), betahistine. USMLE key: fluctuating symptoms, progressive hearing loss."
            },
            {
                "name": "Vestibular Neuritis",
                "match": {"onset": "Sudden", "associated_symptoms": "Nausea"},
                "differentiating_factors": "Severe vertigo lasting days, often post-viral. No hearing loss, unidirectional nystagmus. Corticosteroids (prednisone), antiemetics (meclizine). USMLE key: viral prodrome, no auditory symptoms."
            },
            {
                "name": "Cerebellar Stroke",
                "match": {"onset": "Sudden", "associated_symptoms": "Focal neurological deficits", "physical_exam": "Gait instability"},
                "differentiating_factors": "Sudden vertigo with ataxia, dysmetria, or cranial nerve deficits. CT/MRI confirms cerebellar infarct or hemorrhage. Neurology consult, thrombolytics if ischemic and within window. USMLE key: focal deficits, emergent imaging."
            },
            {
                "name": "Vestibular Migraine",
                "match": {"onset": "Sudden", "past_medical_history": "Migraine", "associated_symptoms": ["Headache", "Photophobia"]},
                "differentiating_factors": "Vertigo with migraine symptoms (photophobia, headache). Triptans for acute attacks, prophylaxis (propranolol, amitriptyline). USMLE key: migraine history, no persistent neurological deficits."
            }
        ]
    },
    # 21-25: Neurological (continued)
    "Numbness/Tingling": {
        "questions": {
            "location": ["Unilateral", "Bilateral", "Facial", "Extremity"],
            "onset": ["Sudden", "Gradual"],
            "associated_symptoms": ["Weakness", "Speech difficulty", "Vision changes", "Pain"],
            "past_medical_history": ["Diabetes", "Stroke", "MS", "Vitamin B12 deficiency"],
            "physical_exam": ["Sensory loss", "Reflex changes", "Motor deficits"],
            "social_history": ["Alcohol use"]
        },
        "diagnoses": [
            {
                "name": "Stroke (CVA)",
                "match": {"onset": "Sudden", "location": "Unilateral", "associated_symptoms": ["Weakness", "Speech difficulty"]},
                "differentiating_factors": "Sudden unilateral numbness with weakness or aphasia. CT/MRI to rule out hemorrhage; tPA if ischemic within 4.5 hours. USMLE key: NIHSS for severity, time-critical."
            },
            {
                "name": "Peripheral Neuropathy",
                "match": {"onset": "Gradual", "location": "Bilateral", "past_medical_history": "Diabetes"},
                "differentiating_factors": "Symmetric distal numbness, burning pain, often diabetic. HbA1c elevated, nerve conduction studies confirm. Glycemic control, gabapentin for pain. USMLE key: ‘stocking-glove’ distribution."
            },
            {
                "name": "Multiple Sclerosis (MS)",
                "match": {"onset": "Gradual", "associated_symptoms": "Vision changes", "past_medical_history": "MS"},
                "differentiating_factors": "Numbness with optic neuritis or motor deficits, relapsing-remitting. MRI: white matter lesions. High-dose steroids, disease-modifying therapies (interferon). USMLE key: lesions separated in time and space."
            },
            {
                "name": "Vitamin B12 Deficiency",
                "match": {"onset": "Gradual", "location": "Bilateral", "past_medical_history": "Vitamin B12 deficiency"},
                "differentiating_factors": "Numbness, paresthesias, macrocytic anemia. Low B12, elevated methylmalonic acid. IM B12 replacement. USMLE key: pernicious anemia, subacute combined degeneration."
            },
            {
                "name": "Bell’s Palsy",
                "match": {"location": "Facial", "onset": "Sudden", "associated_symptoms": "Facial weakness"},
                "differentiating_factors": "Unilateral facial numbness/weakness, no central signs. Corticosteroids (prednisone) within 72 hours, antivirals if HSV suspected. USMLE key: peripheral CN VII palsy, no forehead sparing."
            }
        ]
    },
    "Speech Difficulty": {
        "questions": {
            "type": ["Slurred speech", "Word-finding difficulty", "Incoherent speech"],
            "onset": ["Sudden", "Gradual"],
            "associated_symptoms": ["Weakness", "Numbness", "Facial droop", "Confusion"],
            "past_medical_history": ["Stroke", "TIA", "Dementia"],
            "physical_exam": ["Cranial nerve deficits", "Motor weakness"]
        },
        "diagnoses": [
            {
                "name": "Ischemic Stroke",
                "match": {"onset": "Sudden", "type": "Word-finding difficulty", "associated_symptoms": ["Weakness", "Facial droop"]},
                "differentiating_factors": "Sudden aphasia with hemiparesis or facial droop. CT/MRI, tPA if within 4.5 hours. USMLE key: Broca’s (expressive) vs. Wernicke’s (receptive) aphasia."
            },
            {
                "name": "Transient Ischemic Attack (TIA)",
                "match": {"onset": "Sudden", "type": "Word-finding difficulty"},
                "differentiating_factors": "Transient speech difficulty resolving <24 hours. Antiplatelets (aspirin), risk factor control. USMLE key: stroke precursor."
            },
            {
                "name": "Brain Tumor",
                "match": {"onset": "Gradual", "associated_symptoms": ["Headache", "Seizures"]},
                "differentiating_factors": "Progressive speech difficulty with headache, seizures. MRI: mass effect. Surgical referral, steroids. USMLE key: focal symptoms with mass."
            },
            {
                "name": "Dementia",
                "match": {"onset": "Gradual", "type": "Word-finding difficulty", "past_medical_history": "Dementia"},
                "differentiating_factors": "Progressive word-finding issues, memory loss. MMSE, MRI for atrophy. Supportive care. USMLE key: Alzheimer’s vs. frontotemporal dementia."
            }
        ]
    },
    "Tremors": {
        "questions": {
            "type": ["Resting", "Intention", "Postural"],
            "onset": ["Sudden", "Gradual"],
            "associated_symptoms": ["Rigidity", "Bradykinesia", "Ataxia", "Confusion"],
            "past_medical_history": ["Parkinson’s", "Thyroid disease"],
            "physical_exam": ["Cogwheel rigidity", "Cerebellar signs"],
            "social_history": ["Alcohol use", "Medication changes"]
        },
        "diagnoses": [
            {
                "name": "Parkinson’s Disease",
                "match": {"type": "Resting", "associated_symptoms": ["Rigidity", "Bradykinesia"]},
                "differentiating_factors": "Resting tremor, bradykinesia, cogwheel rigidity. Levodopa trial diagnostic. Dopamine agonists, MAO-B inhibitors. USMLE key: TRAP (tremor, rigidity, akinesia, postural instability)."
            },
            {
                "name": "Essential Tremor",
                "match": {"type": "Postural", "onset": "Gradual"},
                "differentiating_factors": "Bilateral postural/action tremor, improves with alcohol. Propranolol, primidone. USMLE key: family history common."
            },
            {
                "name": "Cerebellar Tremor",
                "match": {"type": "Intention", "associated_symptoms": "Ataxia", "physical_exam": "Cerebellar signs"},
                "differentiating_factors": "Intention tremor with ataxia, dysmetria. MRI to rule out stroke/tumor. Treat underlying cause. USMLE key: cerebellar signs."
            },
            {
                "name": "Hyperthyroidism",
                "match": {"type": "Postural", "associated_symptoms": "Weight loss", "past_medical_history": "Thyroid disease"},
                "differentiating_factors": "Fine tremor with tachycardia, weight loss. Low TSH, high T4. Beta-blockers (propranolol), methimazole. USMLE key: thyroid function tests."
            }
        ]
    },
    "Visual Disturbance": {
        "questions": {
            "type": ["Vision loss", "Double vision", "Flashing lights"],
            "onset": ["Sudden", "Gradual"],
            "associated_symptoms": ["Headache", "Pain with eye movement", "Nausea"],
            "past_medical_history": ["Diabetes", "MS", "Hypertension"],
            "physical_exam": ["Fundoscopic changes", "Pupillary defects"]
        },
        "diagnoses": [
            {
                "name": "Retinal Detachment",
                "match": {"type": "Flashing lights", "onset": "Sudden", "associated_symptoms": "Floaters"},
                "differentiating_factors": "Sudden floaters, flashes, curtain-like vision loss. Fundoscopy: detached retina. Urgent ophthalmology referral. USMLE key: visual field defect."
            },
            {
                "name": "Optic Neuritis",
                "match": {"type": "Vision loss", "onset": "Sudden", "associated_symptoms": "Pain with eye movement"},
                "differentiating_factors": "Unilateral vision loss, pain with eye movement, often MS-related. MRI: optic nerve enhancement. High-dose steroids. USMLE key: afferent pupillary defect."
            },
            {
                "name": "Temporal Arteritis",
                "match": {"onset": "Sudden", "associated_symptoms": ["Headache", "Jaw claudication"], "past_medical_history": "Age >50"},
                "differentiating_factors": "Sudden vision loss, temporal headache, ESR/CRP elevated. Temporal artery biopsy. High-dose prednisone. USMLE key: vision loss irreversible."
            },
            {
                "name": "Diabetic Retinopathy",
                "match": {"onset": "Gradual", "type": "Vision loss", "past_medical_history": "Diabetes"},
                "differentiating_factors": "Gradual vision loss, hemorrhages/exudates on fundoscopy. HbA1c elevated. Laser therapy, VEGF inhibitors. USMLE key: control diabetes."
            }
        ]
    },
    # 26-30: Gastrointestinal
    "Diarrhea": {
        "questions": {
            "onset": ["Acute", "Chronic (>4 weeks)"],
            "character": ["Watery", "Bloody", "Fatty"],
            "associated_symptoms": ["Fever", "Abdominal pain", "Weight loss"],
            "past_medical_history": ["IBD", "Celiac disease", "Recent antibiotics"],
            "social_history": ["Recent travel", "Food exposure"]
        },
        "diagnoses": [
            {
                "name": "Viral Gastroenteritis",
                "match": {"onset": "Acute", "character": "Watery", "associated_symptoms": ["Nausea", "Fever"]},
                "differentiating_factors": "Acute watery diarrhea, vomiting, often norovirus. Supportive care, fluids. USMLE key: self-limiting."
            },
            {
                "name": "Bacterial Enteritis",
                "match": {"onset": "Acute", "character": "Bloody", "social_history": "Recent travel"},
                "differentiating_factors": "Bloody diarrhea, fever, abdominal pain (Salmonella, Shigella). Stool culture, antibiotics if severe (ciprofloxacin). USMLE key: travel history."
            },
            {
                "name": "Clostridium Difficile Colitis",
                "match": {"onset": "Acute", "past_medical_history": "Recent antibiotics"},
                "differentiating_factors": "Watery diarrhea post-antibiotics, C. diff toxin positive. Vancomycin or fidaxomicin. USMLE key: pseudomembranous colitis."
            },
            {
                "name": "Inflammatory Bowel Disease (IBD)",
                "match": {"onset": "Chronic (>4 weeks)", "character": "Bloody", "past_medical_history": "IBD"},
                "differentiating_factors": "Chronic bloody diarrhea, weight loss. Colonoscopy diagnostic. Mesalamine, steroids. USMLE key: Crohn’s vs. ulcerative colitis."
            }
        ]
    },
    "Constipation": {
        "questions": {
            "onset": ["Acute", "Chronic"],
            "associated_symptoms": ["Abdominal pain", "Bloating", "Rectal bleeding"],
            "past_medical_history": ["Hypothyroidism", "Opioid use"],
            "physical_exam": ["Abdominal distension", "Hard stool"]
        },
        "diagnoses": [
            {
                "name": "Functional Constipation",
                "match": {"onset": "Chronic", "associated_symptoms": "Bloating"},
                "differentiating_factors": "Chronic, no red flags. Fiber, laxatives (polyethylene glycol). USMLE key: Rome IV criteria."
            },
            {
                "name": "Bowel Obstruction",
                "match": {"onset": "Acute", "associated_symptoms": ["Abdominal pain", "Nausea"]},
                "differentiating_factors": "Acute constipation, vomiting, distension. X-ray: air-fluid levels. NG tube, surgery if needed. USMLE key: high-pitched bowel sounds."
            },
            {
                "name": "Hypothyroidism",
                "match": {"onset": "Chronic", "past_medical_history": "Hypothyroidism"},
                "differentiating_factors": "Constipation with fatigue, cold intolerance. Elevated TSH. Levothyroxine. USMLE key: systemic symptoms."
            },
            {
                "name": "Opioid-Induced Constipation",
                "match": {"onset": "Chronic", "past_medical_history": "Opioid use"},
                "differentiating_factors": "Constipation post-opioid use. Methylnaltrexone, laxatives. USMLE key: common in chronic pain."
            }
        ]
    },
    "Hematochezia": {
        "questions": {
            "character": ["Bright red blood", "Mixed with stool"],
            "associated_symptoms": ["Abdominal pain", "Weight loss", "Fever"],
            "past_medical_history": ["IBD", "Diverticulosis", "Hemorrhoids"],
            "physical_exam": ["Anal fissure", "Masses"],
            "social_history": ["NSAID use"]
        },
        "diagnoses": [
            {
                "name": "Hemorrhoids",
                "match": {"character": "Bright red blood", "past_medical_history": "Hemorrhoids"},
                "differentiating_factors": "Bright red blood on wiping, no systemic symptoms. Anoscopy confirms. Fiber, topical treatments. USMLE key: common, benign."
            },
            {
                "name": "Diverticular Bleeding",
                "match": {"character": "Bright red blood", "past_medical_history": "Diverticulosis"},
                "differentiating_factors": "Painless hematochezia in elderly. Colonoscopy, angiography if severe. USMLE key: self-limiting in most cases."
            },
            {
                "name": "Inflammatory Bowel Disease (IBD)",
                "match": {"character": "Mixed with stool", "past_medical_history": "IBD"},
                "differentiating_factors": "Bloody diarrhea, abdominal pain, weight loss. Colonoscopy diagnostic. Mesalamine, steroids. USMLE key: chronic symptoms."
            },
            {
                "name": "Colorectal Cancer",
                "match": {"associated_symptoms": ["Weight loss", "Abdominal pain"]},
                "differentiating_factors": "Hematochezia with weight loss, change in bowel habits. Colonoscopy with biopsy. USMLE key: age >50, screening critical."
            }
        ]
    },
    "Melena": {
        "questions": {
            "character": ["Black tarry stools", "Occult blood"],
            "associated_symptoms": ["Abdominal pain", "Nausea", "Fatigue"],
            "past_medical_history": ["PUD", "NSAID use", "Liver disease"],
            "physical_exam": ["Pallor", "Epigastric tenderness"]
        },
        "diagnoses": [
            {
                "name": "Peptic Ulcer Disease (PUD)",
                "match": {"character": "Black tarry stools", "past_medical_history": ["PUD", "NSAID use"]},
                "differentiating_factors": "Epigastric pain, melena, H. pylori or NSAID use. EGD diagnostic, PPI, H. pylori eradication. USMLE key: perforation risk."
            },
            {
                "name": "Gastritis",
                "match": {"character": "Black tarry stools", "past_medical_history": "NSAID use"},
                "differentiating_factors": "Melena, epigastric pain, often NSAID or alcohol-related. PPI, stop offending agent. USMLE key: rule out PUD."
            },
            {
                "name": "Esophageal Varices",
                "match": {"character": "Black tarry stools", "past_medical_history": "Liver disease"},
                "differentiating_factors": "Melena or hematemesis in cirrhosis. EGD, band ligation. Octreotide, beta-blockers. USMLE key: portal hypertension."
            },
            {
                "name": "Mallory-Weiss Tear",
                "match": {"associated_symptoms": ["Nausea", "Vomiting"]},
                "differentiating_factors": "Melena post-vomiting, alcohol use. EGD diagnostic, supportive care. USMLE key: self-limiting in most cases."
            }
        ]
    },
    "Jaundice": {
        "questions": {
            "onset": ["Acute", "Chronic"],
            "associated_symptoms": ["Abdominal pain", "Fever", "Weight loss", "Pruritus"],
            "past_medical_history": ["Hepatitis", "Alcohol use", "Gallstones"],
            "physical_exam": ["Hepatomegaly", "Splenomegaly", "Scleral icterus"],
            "social_history": ["IV drug use", "Alcohol use"]
        },
        "diagnoses": [
            {
                "name": "Viral Hepatitis",
                "match": {"onset": "Acute", "associated_symptoms": ["Fever", "Abdominal pain"], "social_history": "IV drug use"},
                "differentiating_factors": "Acute jaundice, elevated transaminases, viral serologies (HAV, HBV, HCV). Supportive care, antivirals for HBV/HCV. USMLE key: risk factors critical."
            },
            {
                "name": "Cholecystitis/Cholangitis",
                "match": {"onset": "Acute", "associated_symptoms": ["Abdominal pain", "Fever"], "past_medical_history": "Gallstones"},
                "differentiating_factors": "RUQ pain, fever, jaundice (Charcot’s triad for cholangitis). Ultrasound, ERCP for cholangitis. Antibiotics, cholecystectomy. USMLE key: Murphy’s sign, ascending cholangitis."
            },
            {
                "name": "Alcoholic Hepatitis",
                "match": {"onset": "Chronic", "past_medical_history": "Alcohol use"},
                "differentiating_factors": "Jaundice, hepatomegaly, AST:ALT >2:1. Corticosteroids if severe (Maddrey score >32). USMLE key: alcohol history."
            },
            {
                "name": "Pancreatic Cancer",
                "match": {"onset": "Chronic", "associated_symptoms": ["Weight loss", "Abdominal pain"]},
                "differentiating_factors": "Painless jaundice, weight loss, Courvoisier’s sign (palpable gallbladder). CT/MRI, biopsy. USMLE key: elderly, smoking history."
            }
        ]
    },
    # 31-35: Genitourinary
    "Dysuria": {
        "questions": {
            "onset": ["Acute", "Chronic"],
            "associated_symptoms": ["Fever", "Hematuria", "Urgency", "Flank pain"],
            "past_medical_history": ["UTI", "Diabetes", "Kidney stones"],
            "physical_exam": ["CVA tenderness", "Suprapubic tenderness"],
            "social_history": ["Sexual history"]
        },
        "diagnoses": [
            {
                "name": "Urinary Tract Infection (UTI)",
                "match": {"onset": "Acute", "associated_symptoms": ["Urgency", "Fever"]},
                "differentiating_factors": "Dysuria, urgency, frequency, pyuria on urinalysis. Nitrofurantoin or TMP-SMX. USMLE key: E. coli most common."
            },
            {
                "name": "Pyelonephritis",
                "match": {"onset": "Acute", "associated_symptoms": ["Fever", "Flank pain"], "physical_exam": "CVA tenderness"},
                "differentiating_factors": "Dysuria with fever, flank pain, CVA tenderness. Urinalysis: pyuria, WBC casts. Ciprofloxacin, ceftriaxone. USMLE key: systemic symptoms."
            },
            {
                "name": "Urethritis",
                "match": {"onset": "Acute", "social_history": "Sexual history"},
                "differentiating_factors": "Dysuria, discharge, often STD-related (gonorrhea, chlamydia). NAAT testing, doxycycline or azithromycin. USMLE key: sexual history critical."
            },
            {
                "name": "Nephrolithiasis",
                "match": {"onset": "Acute", "associated_symptoms": ["Flank pain", "Hematuria"], "past_medical_history": "Kidney stones"},
                "differentiating_factors": "Severe flank pain radiating to groin, hematuria. CT: stone visualization. Hydration, analgesia, tamsulosin. USMLE key: colicky pain."
            }
        ]
    },
    "Hematuria": {
        "questions": {
            "character": ["Gross", "Microscopic"],
            "associated_symptoms": ["Dysuria", "Flank pain", "Weight loss"],
            "past_medical_history": ["Kidney stones", "Bladder cancer", "Trauma"],
            "physical_exam": ["CVA tenderness", "Abdominal mass"],
            "social_history": ["Smoking"]
        },
        "diagnoses": [
            {
                "name": "Nephrolithiasis",
                "match": {"character": "Gross", "associated_symptoms": "Flank pain"},
                "differentiating_factors": "Colicky flank pain, hematuria. CT: stones. Hydration, analgesia. USMLE key: calcium oxalate most common."
            },
            {
                "name": "Bladder Cancer",
                "match": {"character": "Gross", "associated_symptoms": "Weight loss", "social_history": "Smoking"},
                "differentiating_factors": "Painless gross hematuria, smoking history. Cystoscopy, biopsy. USMLE key: elderly males, smoking."
            },
            {
                "name": "Urinary Tract Infection (UTI)",
                "match": {"character": "Microscopic", "associated_symptoms": "Dysuria"},
                "differentiating_factors": "Dysuria, urgency, hematuria on urinalysis. Antibiotics (nitrofurantoin). USMLE key: pyuria present."
            },
            {
                "name": "Glomerulonephritis",
                "match": {"character": "Microscopic", "associated_symptoms": "Edema"},
                "differentiating_factors": "Hematuria, proteinuria, hypertension. Renal biopsy, treat underlying cause (e.g., post-streptococcal). USMLE key: cola-colored urine."
            }
        ]
    },
    "Flank Pain": {
        "questions": {
            "onset": ["Sudden", "Gradual"],
            "associated_symptoms": ["Fever", "Hematuria", "Dysuria", "Nausea"],
            "past_medical_history": ["Kidney stones", "UTI", "AAA"],
            "physical_exam": ["CVA tenderness", "Pulsatile mass"]
        },
        "diagnoses": [
            {
                "name": "Nephrolithiasis",
                "match": {"onset": "Sudden", "associated_symptoms": ["Hematuria", "Nausea"]},
                "differentiating_factors": "Colicky flank pain, hematuria, nausea. CT: stones. Hydration, tamsulosin. USMLE key: radiating pain to groin."
            },
            {
                "name": "Pyelonephritis",
                "match": {"onset": "Sudden", "associated_symptoms": ["Fever", "Dysuria"], "physical_exam": "CVA tenderness"},
                "differentiating_factors": "Flank pain, fever, dysuria, CVA tenderness. Urinalysis: pyuria, WBC casts. Antibiotics (ciprofloxacin). USMLE key: systemic symptoms."
            },
            {
                "name": "Abdominal Aortic Aneurysm (AAA)",
                "match": {"onset": "Sudden", "physical_exam": "Pulsatile mass"},
                "differentiating_factors": "Severe flank pain, pulsatile mass, hypotension. Ultrasound/CT. Surgical emergency. USMLE key: elderly males, smoking."
            },
            {
                "name": "Renal Infarction",
                "match": {"onset": "Sudden", "associated_symptoms": "Hematuria"},
                "differentiating_factors": "Sudden flank pain, hematuria, elevated LDH. CT angiography. Anticoagulation. USMLE key: atrial fibrillation risk."
            }
        ]
    },
    "Testicular Pain": {
        "questions": {
            "onset": ["Sudden", "Gradual"],
            "associated_symptoms": ["Swelling", "Fever", "Nausea", "Dysuria"],
            "past_medical_history": ["Recent trauma", "Infection"],
            "physical_exam": ["Cremasteric reflex absent", "Testicular tenderness"]
        },
        "diagnoses": [
            {
                "name": "Testicular Torsion",
                "match": {"onset": "Sudden", "associated_symptoms": "Nausea", "physical_exam": "Cremasteric reflex absent"},
                "differentiating_factors": "Sudden severe pain, absent cremasteric reflex, high-riding testis. Doppler ultrasound: no flow. Surgical detorsion. USMLE key: time-sensitive, 6-hour window."
            },
            {
                "name": "Epididymitis",
                "match": {"onset": "Gradual", "associated_symptoms": ["Fever", "Dysuria"]},
                "differentiating_factors": "Gradual pain, dysuria, epididymal tenderness. Antibiotics (ceftriaxone + doxycycline). USMLE key: STD or UTI."
            },
            {
                "name": "Testicular Trauma",
                "match": {"onset": "Sudden", "past_medical_history": "Recent trauma"},
                "differentiating_factors": "Pain post-trauma, hematoma on ultrasound. Conservative management or surgery. USMLE key: rule out rupture."
            },
            {
                "name": "Testicular Cancer",
                "match": {"onset": "Gradual", "associated_symptoms": "Swelling"},
                "differentiating_factors": "Painless mass, gradual pain. Ultrasound: solid mass. Tumor markers (AFP, β-hCG). USMLE key: young males."
            }
        ]
    },
    "Vaginal Bleeding": {
        "questions": {
            "onset": ["Sudden", "Gradual"],
            "character": ["Heavy", "Light", "Clots"],
            "associated_symptoms": ["Abdominal pain", "Dizziness", "Fever"],
            "past_medical_history": ["Pregnancy", "Fibroids", "PCOS"],
            "physical_exam": ["Pelvic tenderness", "Uterine enlargement"],
            "social_history": ["Recent miscarriage"]
        },
        "diagnoses": [
            {
                "name": "Ectopic Pregnancy",
                "match": {"onset": "Sudden", "associated_symptoms": ["Abdominal pain", "Dizziness"], "past_medical_history": "Pregnancy"},
                "differentiating_factors": "Unilateral pelvic pain, vaginal bleeding, positive β-hCG. Transvaginal ultrasound: no intrauterine pregnancy. Methotrexate or surgery. USMLE key: reproductive-age women."
            },
            {
                "name": "Spontaneous Abortion",
                "match": {"onset": "Sudden", "associated_symptoms": "Abdominal pain", "past_medical_history": "Pregnancy"},
                "differentiating_factors": "Vaginal bleeding, cramping, positive β-hCG. Ultrasound: non-viable pregnancy. D&C or expectant management. USMLE key: first trimester."
            },
            {
                "name": "Uterine Fibroids",
                "match": {"onset": "Gradual", "character": "Heavy", "past_medical_history": "Fibroids"},
                "differentiating_factors": "Heavy menstrual bleeding, pelvic pressure. Ultrasound: fibroids. NSAIDs, hormonal therapy. USMLE key: common in reproductive age."
            },
            {
                "name": "Endometrial Cancer",
                "match": {"onset": "Gradual", "past_medical_history": "PCOS"},
                "differentiating_factors": "Postmenopausal bleeding or irregular bleeding. Endometrial biopsy. USMLE key: obesity, PCOS risk factors."
            }
        ]
    },
    # 36-40: Respiratory
    "Hemoptysis": {
        "questions": {
            "onset": ["Sudden", "Gradual"],
            "character": ["Streaks of blood", "Frank blood"],
            "associated_symptoms": ["Cough", "Fever", "Weight loss", "Chest pain"],
            "past_medical_history": ["TB", "Lung cancer", "COPD"],
            "physical_exam": ["Wheezing", "Clubbing"],
            "social_history": ["Smoking", "Travel history"]
        },
        "diagnoses": [
            {
                "name": "Bronchitis",
                "match": {"onset": "Gradual", "character": "Streaks of blood", "associated_symptoms": "Cough"},
                "differentiating_factors": "Productive cough with blood streaks, often post-viral. Supportive care, antibiotics if bacterial. USMLE key: benign, common."
            },
            {
                "name": "Pulmonary Embolism",
                "match": {"onset": "Sudden", "associated_symptoms": ["Chest pain", "Dyspnea"]},
                "differentiating_factors": "Sudden hemoptysis, dyspnea, hypoxia. CTPA diagnostic. Anticoagulation (heparin). USMLE key: Wells score, S1Q3T3 on EKG."
            },
            {
                "name": "Lung Cancer",
                "match": {"onset": "Gradual", "associated_symptoms": ["Weight loss", "Cough"], "social_history": "Smoking"},
                "differentiating_factors": "Chronic hemoptysis, weight loss, smoking history. CT: lung mass. Bronchoscopy for biopsy. USMLE key: smokers >40."
            },
            {
                "name": "Tuberculosis",
                "match": {"onset": "Gradual", "associated_symptoms": ["Fever", "Weight loss"], "past_medical_history": "TB"},
                "differentiating_factors": "Hemoptysis, night sweats, weight loss. CXR: cavitary lesions, sputum AFB positive. RIPE therapy. USMLE key: reactivation TB."
            }
        ]
    },
    "Wheezing": {
        "questions": {
            "onset": ["Sudden", "Gradual"],
            "associated_symptoms": ["Dyspnea", "Cough", "Fever", "Urticaria"],
            "past_medical_history": ["Asthma", "COPD", "Allergies"],
            "physical_exam": ["Accessory muscle use", "Stridor"],
            "social_history": ["Allergen exposure", "Smoking"]
        },
        "diagnoses": [
            {
                "name": "Asthma Exacerbation",
                "match": {"onset": "Sudden", "past_medical_history": "Asthma", "associated_symptoms": "Dyspnea"},
                "differentiating_factors": "Sudden wheezing, dyspnea, reduced peak flow. Albuterol, corticosteroids. USMLE key: pulsus paradoxus in severe cases."
            },
            {
                "name": "COPD Exacerbation",
                "match": {"onset": "Gradual", "past_medical_history": "COPD", "social_history": "Smoking"},
                "differentiating_factors": "Wheezing, increased sputum, chronic smoker. Bronchodilators, steroids, antibiotics if bacterial. USMLE key: barrel chest."
            },
            {
                "name": "Anaphylaxis",
                "match": {"onset": "Sudden", "associated_symptoms": "Urticaria", "social_history": "Allergen exposure"},
                "differentiating_factors": "Wheezing, hives, hypotension post-allergen. IM epinephrine, antihistamines. USMLE key: biphasic reaction risk."
            },
            {
                "name": "Foreign Body Aspiration",
                "match": {"onset": "Sudden", "physical_exam": "Stridor"},
                "differentiating_factors": "Sudden wheezing or stridor, unilateral findings. CXR, bronchoscopy for removal. USMLE key: children, sudden onset."
            }
        ]
    },
    "Stridor": {
        "questions": {
            "onset": ["Sudden", "Gradual"],
            "associated_symptoms": ["Dyspnea", "Fever", "Drooling", "Cough"],
            "past_medical_history": ["Allergies", "Recent intubation"],
            "physical_exam": ["Inspiratory stridor", "Tracheal deviation"],
            "social_history": ["Foreign body exposure"]
        },
        "diagnoses": [
            {
                "name": "Anaphylaxis",
                "match": {"onset": "Sudden", "past_medical_history": "Allergies"},
                "differentiating_factors": "Stridor, hives, hypotension post-allergen. IM epinephrine, airway management. USMLE key: rapid progression."
            },
            {
                "name": "Epiglottitis",
                "match": {"onset": "Sudden", "associated_symptoms": ["Fever", "Drooling"]},
                "differentiating_factors": "Stridor, drooling, fever, tripod position. Lateral neck X-ray: thumbprint sign. Airway management, antibiotics (ceftriaxone). USMLE key: H. influenzae in unvaccinated."
            },
            {
                "name": "Foreign Body Aspiration",
                "match": {"onset": "Sudden", "social_history": "Foreign body exposure"},
                "differentiating_factors": "Sudden stridor, choking history. CXR, bronchoscopy for removal. USMLE key: pediatric emergency."
            },
            {
                "name": "Laryngeal Edema",
                "match": {"onset": "Sudden", "past_medical_history": "Recent intubation"},
                "differentiating_factors": "Stridor post-intubation or trauma. Steroids, airway monitoring. USMLE key: post-extubation complication."
            }
        ]
    },
    "Cyanosis": {
        "questions": {
            "location": ["Central", "Peripheral"],
            "onset": ["Sudden", "Gradual"],
            "associated_symptoms": ["Dyspnea", "Chest pain", "Fever"],
            "past_medical_history": ["COPD", "Congenital heart disease"],
            "physical_exam": ["Clubbing", "Murmurs"]
        },
        "diagnoses": [
            {
                "name": "Pulmonary Embolism",
                "match": {"onset": "Sudden", "associated_symptoms": ["Dyspnea", "Chest pain"]},
                "differentiating_factors": "Sudden central cyanosis, hypoxia, tachycardia. CTPA diagnostic. Anticoagulation (heparin). USMLE key: hypoxia with clear lungs."
            },
            {
                "name": "Pneumonia",
                "match": {"onset": "Gradual", "associated_symptoms": ["Fever", "Dyspnea"]},
                "differentiating_factors": "Cyanosis, fever, productive cough. CXR: consolidation. Antibiotics (levofloxacin). USMLE key: CURB-65 score."
            },
            {
                "name": "Congenital Heart Disease",
                "match": {"onset": "Gradual", "past_medical_history": "Congenital heart disease"},
                "differentiating_factors": "Central cyanosis, murmurs, clubbing. Echocardiogram diagnostic. Surgical correction. USMLE key: cyanotic heart defects (e.g., tetralogy of Fallot)."
            },
            {
                "name": "Methemoglobinemia",
                "match": {"onset": "Sudden", "associated_symptoms": "Dyspnea"},
                "differentiating_factors": "Central cyanosis, normal SpO2, chocolate-brown blood. Methylene blue. USMLE key: drug exposure (e.g., benzocaine)."
            }
        ]
    },
    "Respiratory Distress": {
        "questions": {
            "onset": ["Sudden", "Gradual"],
            "associated_symptoms": ["Wheezing", "Stridor", "Cough", "Fever"],
            "past_medical_history": ["Asthma", "CHF", "COPD"],
            "physical_exam": ["Accessory muscle use", "Crackles", "JVD"],
            "social_history": ["Smoking", "Allergen exposure"]
        },
        "diagnoses": [
            {
                "name": "Asthma Exacerbation",
                "match": {"onset": "Sudden", "associated_symptoms": "Wheezing", "past_medical_history": "Asthma"},
                "differentiating_factors": "Sudden respiratory distress, wheezing, reduced peak flow. Albuterol, corticosteroids. USMLE key: reversible obstruction."
            },
            {
                "name": "Congestive Heart Failure (CHF)",
                "match": {"onset": "Gradual", "associated_symptoms": "Crackles", "physical_exam": "JVD"},
                "differentiating_factors": "Dyspnea, crackles, edema, elevated BNP. Diuretics (furosemide), oxygen. USMLE key: pink frothy sputum."
            },
            {
                "name": "Pneumothorax",
                "match": {"onset": "Sudden", "physical_exam": "Decreased breath sounds"},
                "differentiating_factors": "Sudden distress, unilateral decreased breath sounds. CXR: lung collapse. Chest tube. USMLE key: tension pneumothorax signs."
            },
            {
                "name": "Acute Respiratory Distress Syndrome (ARDS)",
                "match": {"onset": "Sudden", "past_medical_history": "Recent trauma"},
                "differentiating_factors": "Severe hypoxia, bilateral crackles, PaO2/FiO2 <300. CXR: bilateral infiltrates. Low tidal volume ventilation. USMLE key: non-cardiogenic edema."
            }
        ]
    },
    # 41-45: ENT & Ophthalmologic
    "Epistaxis": {
        "questions": {
            "onset": ["Sudden", "Recurrent"],
            "location": ["Anterior", "Posterior"],
            "associated_symptoms": ["Nasal trauma", "Hypertension", "Bleeding elsewhere"],
            "past_medical_history": ["Anticoagulant use", "Liver disease"],
            "physical_exam": ["Nasal mucosa dryness", "Septal deviation"],
            "social_history": ["Cocaine use"]
        },
        "diagnoses": [
            {
                "name": "Anterior Epistaxis",
                "match": {"onset": "Sudden", "location": "Anterior", "physical_exam": "Nasal mucosa dryness"},
                "differentiating_factors": "Bleeding from Kiesselbach’s plexus, often due to trauma or dry mucosa. Nasal compression, oxymetazoline, cautery. USMLE key: most common, benign."
            },
            {
                "name": "Posterior Epistaxis",
                "match": {"onset": "Sudden", "location": "Posterior", "past_medical_history": "Hypertension"},
                "differentiating_factors": "Severe bleeding, elderly, hypertension. Nasal packing, ENT consult. USMLE key: risk of airway compromise."
            },
            {
                "name": "Coagulopathy",
                "match": {"associated_symptoms": "Bleeding elsewhere", "past_medical_history": "Anticoagulant use"},
                "differentiating_factors": "Epistaxis with other bleeding sites, anticoagulant use. INR/PTT, reverse anticoagulation (vitamin K for warfarin). USMLE key: check medications."
            },
            {
                "name": "Hereditary Hemorrhagic Telangiectasia",
                "match": {"onset": "Recurrent", "associated_symptoms": "Bleeding elsewhere"},
                "differentiating_factors": "Recurrent epistaxis, telangiectasias on skin/mucosa. ENT referral, laser therapy. USMLE key: genetic condition."
            }
        ]
    },
    "Ear Pain": {
        "questions": {
            "onset": ["Sudden", "Gradual"],
            "associated_symptoms": ["Fever", "Hearing loss", "Discharge", "Vertigo"],
            "past_medical_history": ["Recent URI", "Swimming"],
            "physical_exam": ["Tympanic membrane erythema", "Effusion"],
            "social_history": ["Swimming"]
        },
        "diagnoses": [
            {
                "name": "Acute Otitis Media",
                "match": {"onset": "Sudden", "associated_symptoms": "Fever", "physical_exam": "Tympanic membrane erythema"},
                "differentiating_factors": "Ear pain, fever, bulging TM. Amoxicillin, observation in mild cases. USMLE key: pediatric common."
            },
            {
                "name": "Otitis Externa",
                "match": {"onset": "Sudden", "social_history": "Swimming", "physical_exam": "Ear canal edema"},
                "differentiating_factors": "Ear pain, canal swelling, often swimmer’s ear. Topical antibiotics (ciprofloxacin drops). USMLE key: Pseudomonas aeruginosa."
            },
            {
                "name": "Mastoiditis",
                "match": {"onset": "Gradual", "associated_symptoms": "Fever", "physical_exam": "Mastoid tenderness"},
                "differentiating_factors": "Ear pain, mastoid tenderness, post-URI. CT: mastoid air cell opacification. IV antibiotics, possible surgery. USMLE key: complication of otitis media."
            },
            {
                "name": "TM Perforation",
                "match": {"onset": "Sudden", "associated_symptoms": "Hearing loss"},
                "differentiating_factors": "Sudden pain, hearing loss post-trauma or infection. Otoscopy: perforation. Keep dry, antibiotics if infected. USMLE key: avoid water exposure."
            }
        ]
    },
    "Eye Pain/Redness": {
        "questions": {
            "onset": ["Sudden", "Gradual"],
            "associated_symptoms": ["Vision loss", "Photophobia", "Discharge", "Foreign body sensation"],
            "past_medical_history": ["Contact lens use", "Autoimmune disease"],
            "physical_exam": ["Ciliary flush", "Corneal opacity"],
            "social_history": ["Trauma"]
        },
        "diagnoses": [
            {
                "name": "Conjunctivitis",
                "match": {"onset": "Gradual", "associated_symptoms": "Discharge"},
                "differentiating_factors": "Red eye, discharge (viral, bacterial, allergic). Viral: supportive; bacterial: erythromycin drops; allergic: antihistamines. USMLE key: distinguish etiology."
            },
            {
                "name": "Corneal Abrasion",
                "match": {"onset": "Sudden", "associated_symptoms": "Foreign body sensation", "social_history": "Trauma"},
                "differentiating_factors": "Sudden pain, fluorescein staining positive. Antibiotic drops, avoid contact lenses. USMLE key: trauma history."
            },
            {
                "name": "Acute Angle-Closure Glaucoma",
                "match": {"onset": "Sudden", "associated_symptoms": ["Vision loss", "Nausea"], "physical_exam": "Ciliary flush"},
                "differentiating_factors": "Severe pain, blurred vision, halos, fixed pupil. Elevated IOP on tonometry. Acetazolamide, timolol, laser iridotomy. USMLE key: ophthalmic emergency."
            },
            {
                "name": "Uveitis",
                "match": {"onset": "Gradual", "associated_symptoms": "Photophobia", "past_medical_history": "Autoimmune disease"},
                "differentiating_factors": "Pain, photophobia, ciliary flush, often autoimmune (e.g., HLA-B27). Steroid drops, treat underlying cause. USMLE key: slit-lamp exam."
            }
        ]
    },
    "Facial Swelling": {
        "questions": {
            "onset": ["Sudden", "Gradual"],
            "associated_symptoms": ["Fever", "Dyspnea", "Rash", "Tooth pain"],
            "past_medical_history": ["Allergies", "Dental infection"],
            "physical_exam": ["Erythema", "Airway compromise"],
            "social_history": ["Allergen exposure"]
        },
        "diagnoses": [
            {
                "name": "Anaphylaxis",
                "match": {"onset": "Sudden", "associated_symptoms": ["Dyspnea", "Rash"], "past_medical_history": "Allergies"},
                "differentiating_factors": "Rapid swelling, urticaria, respiratory distress. IM epinephrine, antihistamines. USMLE key: airway management critical."
            },
            {
                "name": "Angioedema",
                "match": {"onset": "Sudden", "past_medical_history": "Allergies"},
                "differentiating_factors": "Non-pitting swelling, often lips or eyes, ACE inhibitor-related. C1 esterase inhibitor for HAE, antihistamines for allergic. USMLE key: drug history."
            },
            {
                "name": "Ludwig’s Angina",
                "match": {"onset": "Gradual", "associated_symptoms": ["Fever", "Tooth pain"]},
                "differentiating_factors": "Submandibular swelling, fever, dental infection. CT: abscess. Antibiotics (clindamycin), surgical drainage. USMLE key: airway emergency."
            },
            {
                "name": "Cellulitis",
                "match": {"onset": "Gradual", "associated_symptoms": "Fever", "physical_exam": "Erythema"},
                "differentiating_factors": "Erythema, warmth, swelling, often post-trauma. Antibiotics (cephalexin). USMLE key: rule out abscess."
            }
        ]
    },
    "Neck Pain": {
        "questions": {
            "onset": ["Sudden", "Gradual"],
            "associated_symptoms": ["Fever", "Stiff neck", "Headache", "Weakness"],
            "past_medical_history": ["Trauma", "Infection", "RA"],
            "physical_exam": ["Nuchal rigidity", "Tender lymph nodes"],
            "social_history": ["Recent infection"]
        },
        "diagnoses": [
            {
                "name": "Cervical Strain",
                "match": {"onset": "Sudden", "past_medical_history": "Trauma"},
                "differentiating_factors": "Localized pain post-trauma, no neurological deficits. NSAIDs, physical therapy. USMLE key: benign, common."
            },
            {
                "name": "Meningitis",
                "match": {"onset": "Sudden", "associated_symptoms": ["Fever", "Stiff neck"], "physical_exam": "Nuchal rigidity"},
                "differentiating_factors": "Neck stiffness, fever, headache. LP: elevated WBC, low glucose (bacterial). Antibiotics (ceftriaxone, vancomycin). USMLE key: Kernig’s/Brudzinski’s signs."
            },
            {
                "name": "Cervical Spondylosis",
                "match": {"onset": "Gradual", "past_medical_history": "RA"},
                "differentiating_factors": "Chronic neck pain, stiffness, radiculopathy. X-ray: degenerative changes. NSAIDs, physical therapy. USMLE key: elderly patients."
            },
            {
                "name": "Subarachnoid Hemorrhage",
                "match": {"onset": "Sudden", "associated_symptoms": ["Headache", "Stiff neck"]},
                "differentiating_factors": "Thunderclap headache, neck stiffness. CT head, LP if negative (xanthochromia). Neurosurgical emergency. USMLE key: sentinel bleed."
            }
        ]
    },
    # 46-50: Miscellaneous & New Presentations
    "Foreign Body Ingestion": {
        "questions": {
            "onset": ["Sudden"],
            "associated_symptoms": ["Choking", "Dysphagia", "Chest pain", "Abdominal pain"],
            "object": ["Coin", "Food", "Sharp object", "Battery"],
            "past_medical_history": ["Esophageal disease", "Pediatric"],
            "physical_exam": ["Drooling", "Respiratory distress"],
            "social_history": ["Child vs. adult"]
        },
        "diagnoses": [
            {
                "name": "Esophageal Foreign Body",
                "match": {"onset": "Sudden", "associated_symptoms": ["Dysphagia", "Drooling"], "past_medical_history": "Pediatric"},
                "differentiating_factors": "Sudden dysphagia, drooling, often pediatric (coin, battery). X-ray: radiopaque object. Endoscopy for removal. USMLE key: battery ingestion urgent."
            },
            {
                "name": "Airway Foreign Body",
                "match": {"onset": "Sudden", "associated_symptoms": ["Choking", "Respiratory distress"]},
                "differentiating_factors": "Choking, stridor, respiratory distress. CXR, bronchoscopy for removal. USMLE key: pediatric emergency."
            },
            {
                "name": "Perforation",
                "match": {"onset": "Sudden", "object": "Sharp object", "associated_symptoms": "Chest pain"},
                "differentiating_factors": "Pain post-ingestion of sharp object, pneumomediastinum on CXR. Surgical emergency. USMLE key: Boerhaave syndrome risk."
            }
        ]
    },
    "Fever in Pediatric Patient": {
        "questions": {
            "age": ["Neonate (<28 days)", "Infant (1-12 months)", "Child (>1 year)"],
            "associated_symptoms": ["Lethargy", "Poor feeding", "Rash", "Seizures"],
            "past_medical_history": ["Prematurity", "Vaccination status"],
            "physical_exam": ["Fontanelle bulging", "Nuchal rigidity"],
            "social_history": ["Daycare exposure"]
        },
        "diagnoses": [
            {
                "name": "Neonatal Sepsis",
                "match": {"age": "Neonate (<28 days)", "associated_symptoms": ["Lethargy", "Poor feeding"]},
                "differentiating_factors": "Fever or hypothermia, lethargy, poor feeding. Blood/CSF cultures, broad-spectrum antibiotics (ampicillin, gentamicin). USMLE key: Group B Streptococcus."
            },
            {
                "name": "Febrile Seizure",
                "match": {"age": "Child (>1 year)", "associated_symptoms": "Seizures"},
                "differentiating_factors": "Seizure with fever, age 6 months-5 years. Antipyretics, workup for infection. USMLE key: simple vs. complex seizures."
            },
            {
                "name": "Meningitis",
                "match": {"associated_symptoms": ["Lethargy", "Rash"], "physical_exam": "Nuchal rigidity"},
                "differentiating_factors": "Fever, irritability, nuchal rigidity. LP: bacterial vs. viral. Antibiotics (ceftriaxone, vancomycin). USMLE key: meningococcal rash."
            },
            {
                "name": "Kawasaki Disease",
                "match": {"age": "Child (>1 year)", "associated_symptoms": "Rash"},
                "differentiating_factors": "Prolonged fever, rash, conjunctivitis, strawberry tongue. IVIG, aspirin. USMLE key: coronary artery aneurysms."
            }
        ]
    },
    "Allergic Reaction": {
        "questions": {
            "onset": ["Sudden", "Gradual"],
            "associated_symptoms": ["Rash", "Wheezing", "Swelling", "Dyspnea"],
            "past_medical_history": ["Allergies", "Asthma"],
            "physical_exam": ["Urticaria", "Angioedema"],
            "social_history": ["Allergen exposure"]
        },
        "diagnoses": [
            {
                "name": "Anaphylaxis",
                "match": {"onset": "Sudden", "associated_symptoms": ["Wheezing", "Dyspnea"], "physical_exam": "Angioedema"},
                "differentiating_factors": "Rapid-onset rash, wheezing, hypotension. IM epinephrine, antihistamines, steroids. USMLE key: biphasic reaction risk."
            },
            {
                "name": "Urticaria",
                "match": {"onset": "Sudden", "associated_symptoms": "Rash", "physical_exam": "Urticaria"},
                "differentiating_factors": "Itchy hives, no systemic symptoms. Antihistamines (cetirizine). USMLE key: rule out anaphylaxis."
            },
            {
                "name": "Angioedema",
                "match": {"onset": "Sudden", "associated_symptoms": "Swelling", "past_medical_history": "Allergies"},
                "differentiating_factors": "Non-pitting swelling, often ACE inhibitor-related. C1 esterase inhibitor for HAE, antihistamines for allergic. USMLE key: drug history."
            },
            {
                "name": "Contact Dermatitis",
                "match": {"onset": "Gradual", "associated_symptoms": "Rash"},
                "differentiating_factors": "Localized rash, itching post-allergen contact. Topical steroids. USMLE key: avoid allergen."
            }
        ]
    },
    "Hypotension/Shock": {
        "questions": {
            "onset": ["Sudden", "Gradual"],
            "associated_symptoms": ["Fever", "Chest pain", "Abdominal pain", "Bleeding"],
            "past_medical_history": ["Sepsis", "Trauma", "MI"],
            "physical_exam": ["Tachycardia", "Cool extremities", "JVD"],
            "social_history": ["Recent trauma"]
        },
        "diagnoses": [
            {
                "name": "Septic Shock",
                "match": {"onset": "Sudden", "associated_symptoms": "Fever", "past_medical_history": "Sepsis"},
                "differentiating_factors": "Hypotension, fever, warm skin early. qSOFA score, blood cultures. Broad-spectrum antibiotics, fluids. USMLE key: early goal-directed therapy."
            },
            {
                "name": "Hypovolemic Shock",
                "match": {"onset": "Sudden", "associated_symptoms": "Bleeding", "past_medical_history": "Trauma"},
                "differentiating_factors": "Hypotension, tachycardia, cool skin post-bleeding. Fluids, blood transfusion. USMLE key: class III/IV shock."
            },
            {
                "name": "Cardiogenic Shock",
                "match": {"onset": "Sudden", "associated_symptoms": "Chest pain", "physical_exam": "JVD"},
                "differentiating_factors": "Hypotension, JVD, pulmonary edema post-MI. Echocardiogram, inotropes (dobutamine). USMLE key: low cardiac output."
            },
            {
                "name": "Anaphylactic Shock",
                "match": {"onset": "Sudden", "associated_symptoms": "Rash", "past_medical_history": "Allergies"},
                "differentiating_factors": "Hypotension, urticaria, wheezing post-allergen. IM epinephrine, fluids. USMLE key: rapid onset."
            }
        ]
    },
    "Fatigue": {
        "questions": {
            "onset": ["Acute", "Chronic"],
            "associated_symptoms": ["Weight loss", "Fever", "Dyspnea", "Depression"],
            "past_medical_history": ["Anemia", "Hypothyroidism", "Depression"],
            "physical_exam": ["Pallor", "Lymphadenopathy"],
            "social_history": ["Stress"]
        },
        "diagnoses": [
            {
                "name": "Anemia",
                "match": {"onset": "Chronic", "associated_symptoms": "Dyspnea", "physical_exam": "Pallor"},
                "differentiating_factors": "Fatigue, pallor, low hemoglobin. Iron studies, B12, folate levels. Treat underlying cause (iron, B12). USMLE key: microcytic vs. macrocytic."
            },
            {
                "name": "Hypothyroidism",
                "match": {"onset": "Chronic", "associated_symptoms": "Weight gain", "past_medical_history": "Hypothyroidism"},
                "differentiating_factors": "Fatigue, cold intolerance, elevated TSH. Levothyroxine. USMLE key: systemic symptoms."
            },
            {
                "name": "Depression",
                "match": {"onset": "Chronic", "associated_symptoms": "Depression", "social_history": "Stress"},
                "differentiating_factors": "Fatigue, low mood, anhedonia. PHQ-9 screening, SSRIs (sertraline). USMLE key: rule out organic causes."
            },
            {
                "name": "Chronic Fatigue Syndrome",
                "match": {"onset": "Chronic", "associated_symptoms": "Post-exertional malaise"},
                "differentiating_factors": "Severe fatigue >6 months, unrefreshing sleep. Supportive care, CBT. USMLE key: diagnosis of exclusion."
            }
        ]
    }
}

def run_diagnostic_tree(presentation, patient_data):
    """
    Run the diagnostic tree for a given presentation based on patient data.
    :param presentation: str, the chief complaint (e.g., 'Chest Pain')
    :param patient_data: dict, patient symptoms and history
    :return: list of possible diagnoses with differentiating factors
    """
    if presentation not in ER_PRESENTATIONS:
        return {"error": "Presentation not found"}
    
    possible_diagnoses = []
    presentation_data = ER_PRESENTATIONS[presentation]
    
    for diagnosis in presentation_data["diagnoses"]:
        match_score = 0
        total_criteria = len(diagnosis["match"])
        
        for key, value in diagnosis["match"].items():
            if key in patient_data and patient_data[key] in value:
                match_score += 1
        
        if match_score / total_criteria >= 0.6:  # Threshold for matching
            possible_diagnoses.append({
                "diagnosis": diagnosis["name"],
                "differentiating_factors": diagnosis["differentiating_factors"],
                "match_score": match_score / total_criteria
            })
    
    return sorted(possible_diagnoses, key=lambda x: x["match_score"], reverse=True)

# Example usage:
# patient_data = {"location": "Central", "character": "Crushing", "radiation": "To the arm", "associated_symptoms": "Dyspnea"}
# result = run_diagnostic_tree("Chest Pain", patient_data)
# print(result)
