from flask import Flask, request, jsonify, send_from_directory
from flask_cors import CORS

app = Flask(__name__, static_folder=None)
CORS(app)


@app.route('/')
def home():
    return send_from_directory(app.root_path, 'index.html')


@app.route('/style.css')
def stylesheet():
    return send_from_directory(app.root_path, 'style.css')


@app.route('/script.js')
def frontend_script():
    return send_from_directory(app.root_path, 'script.js')


@app.route('/Whats.jpg')
def avatar():
    return send_from_directory(app.root_path, 'Whats.jpg')


@app.route('/Whats1.jpg')
def background_image():
    return send_from_directory(app.root_path, 'Whats1.jpg')


medicines = {
    'asthma': 'Salbutamol',
    'fever': 'Paracetamol',
    'headache': 'Ibuprofen',
    'cough': 'Cough syrup',
    'cold': 'Antihistamines',
    'sore throat': 'Strepsils',
    'body pain': 'Diclofenac',
    'diarrhea': 'Loperamide',
    'constipation': 'Lactulose',
    'acidity': 'Pantoprazole',
    'stomach ache': 'Dicyclomine',
    'high blood pressure': 'Amlodipine',
    'diabetes': 'Metformin',
    'allergy': 'Levocetirizine',
    'infection': 'Amoxicillin',
    'skin rash': 'Hydrocortisone',
    'vomiting': 'Ondansetron',
    'migraine': 'Sumatriptan',
    'anxiety': 'Alprazolam',
    'insomnia': 'Zolpidem',
    'nausea': 'Domperidone',
    'ear pain': 'Ciprofloxacin ear drops',
    'eye irritation': 'Lubricant eye drops',
    'dizziness': 'Betahistine',
    'arthritis': 'Naproxen',
    'heartburn': 'Ranitidine',
    'urinary tract infection': 'Nitrofurantoin',
    'acid reflux': 'Esomeprazole',
    'back pain': 'Tramadol',
    'toothache': 'Mefenamic acid',
    'flu': 'Oseltamivir',
    'eczema': 'Clobetasol cream',
    'psoriasis': 'Calcipotriol',
    'hair loss': 'Minoxidil',
    'obesity': 'Orlistat',
    'thyroid issues': 'Levothyroxine',
    'depression': 'Fluoxetine',
    'panic disorder': 'Clonazepam',
    'gout': 'Allopurinol',
    'osteoporosis': 'Alendronate',
    'chest pain': 'Nitroglycerin',
    'irritable bowel syndrome': 'Hyoscine',
    'hyperlipidemia': 'Atorvastatin',
    'anemia': 'Ferrous sulfate',
    'menstrual pain': 'Mefenamic acid',
    'polycystic ovary syndrome (PCOS)': 'Spironolactone',
    'bloating': 'Simethicone',
    'motion sickness': 'Dimenhydrinate',
    'sunburn': 'Aloe vera gel',
    'acne': 'Benzoyl peroxide',
    'pneumonia': 'Azithromycin',
    'bronchitis': 'Doxycycline',
    'sinusitis': 'Pseudoephedrine',
    'ringworm': 'Terbinafine',
    'scabies': 'Permethrin cream',
    'cold sores': 'Acyclovir',
    'warts': 'Salicylic acid',
    'yeast infection': 'Fluconazole',
    'high cholesterol': 'Rosuvastatin',
    'low blood pressure': 'Midodrine',
    'seizures': 'Phenytoin',
    'Parkinson’s disease': 'Levodopa',
    'Alzheimer’s disease': 'Donepezil',
    'chronic pain': 'Gabapentin',
    'ADD/ADHD': 'Methylphenidate',
    'smoking cessation': 'Bupropion',
    'dry skin': 'Urea cream',
    'hyperhidrosis': 'Aluminum chloride solution',
    'muscle spasms': 'Cyclobenzaprine',
    'hemorrhoids': 'Lidocaine cream',
    'prostate enlargement': 'Tamsulosin',
    'varicose veins': 'Diosmin',
    'vitamin D deficiency': 'Cholecalciferol',
    'kidney stones': 'Potassium citrate',
    'liver disease': 'Ursodeoxycholic acid',
    'stroke prevention': 'Clopidogrel',
    'blood clot prevention': 'Warfarin',
    'post-surgery pain': 'Ketorolac',
    'allergic rhinitis': 'Fluticasone nasal spray',
    'vertigo': 'Meclizine',
    'hay fever': 'Cetirizine',
    'chronic cough': 'Codeine syrup',
    'fatigue': 'Vitamin B12',
    'tennis elbow': 'Diclofenac gel',
    'plantar fasciitis': 'Ibuprofen gel',
    'fibromyalgia': 'Pregabalin',
    'itches': 'Levocetirizine',
    'cramp': 'Thiocolchicoside',
    'malaria': 'Falcigo Plus',
    'skin burn': 'Burnol',
    'appendicitis': 'Ceftriaxone',
    'angina': 'Isosorbide dinitrate',
    'hives': 'Loratadine',
    'pelvic pain': 'Buscopan',
    'UTI in pregnancy': 'Nitrofurantoin',
    'piles': 'Daflon',
    'oral thrush': 'Nystatin',
    'anaphylaxis': 'Adrenaline injection',
    'nerve pain': 'Amitriptyline',
    'herpes': 'Valacyclovir',
    'conjunctivitis': 'Ofloxacin drops',
    'gas': 'Activated charcoal',
    'dehydration': 'Oral rehydration salts',
    'bee sting': 'Antihistamine cream',
    'chapped lips': 'Petroleum jelly',
    'hyperkalemia': 'Sodium polystyrene sulfonate',
    'hypokalemia': 'Potassium chloride',
    'frostbite': 'Silver sulfadiazine',
    'fractures': 'Paracetamol + codeine',
    'shingles': 'Acyclovir',
    'eczema flare-ups': 'Tacrolimus ointment',
    'overactive bladder': 'Oxybutynin',
    'hormonal imbalance': 'Dydrogesterone',
    'alopecia areata': 'Topical corticosteroids',
    'bronchial asthma': 'Montelukast',
    'pre-diabetes': 'Metformin',
    'gestational diabetes': 'Insulin',
    'dental abscess': 'Clindamycin',
    'smelly feet': 'Antifungal powder',
    'stomach ulcers': 'Omeprazole',
    'bedsores': 'Hydrocolloid dressing',
    'Celiac disease': 'Gluten-free diet',
    'rosacea': 'Metronidazole gel',
    'chronic sinusitis': 'Fluticasone nasal spray',
    'cystic acne': 'Isotretinoin',
    'pink eye': 'Chloramphenicol drops',
    'food poisoning': 'Ciprofloxacin',
    'inguinal hernia': 'Painkillers',
    'gastritis': 'Rabeprazole',
    'vaginal dryness': 'Estradiol cream',
    'hot flashes': 'Black cohosh supplements',
    'bacterial vaginosis': 'Metronidazole tablets',
    'oral ulcers': 'Chlorhexidine gel',
    'rheumatic fever': 'Benzathine penicillin',
    'chronic fatigue syndrome': 'Methylphenidate',
    'Raynaud’s disease': 'Nifedipine',
    'premenstrual syndrome': 'Evening primrose oil',
    'adhesion pain': 'NSAIDs',
    'carpal tunnel syndrome': 'Wrist splints',
    'muscle weakness': 'Vitamin D3',
    'poor appetite': 'Cyproheptadine',
    'head congestion': 'Phenylephrine',
    'severe acne': 'Tretinoin',
    'sports injury': 'Ice packs + Ibuprofen',
    'viral fever': 'Paracetamol',
    'bleeding gums': 'Vitamin C',
    'cellulitis': 'Cephalexin',
    'measles': 'Vitamin A supplements',
    'chickenpox': 'Calamine lotion',
    'whooping cough': 'Azithromycin',
    'hiccups': 'Chlorpromazine',
    'head lice': 'Permethrin lotion',
    'nosebleeds': 'Oxymetazoline spray',
    'phantom pain': 'Gabapentin',
    'heart palpitations': 'Beta-blockers',
    'menopause': 'Hormone replacement therapy',
    'bacterial endocarditis': 'Gentamicin',
    'sepsis': 'Meropenem',
    'thyroiditis': 'Levothyroxine',
    'allergic conjunctivitis': 'Olopatadine drops',
    'autoimmune diseases': 'Methotrexate',
    'gastric reflux': 'Lansoprazole',
    'pelvic inflammatory disease': 'Doxycycline',
    'prostatitis': 'Ciprofloxacin',
    'erectile dysfunction': 'Sildenafil',
    'varicella': 'Acyclovir',
    'rashes': 'Hydrocortisone',
    'oral cavity ulcers': 'B-complex supplements',
    'tinnitus': 'Betahistine',
    'skin burn':'burnol',
    'cancer':'Temmozolomide',

}

@app.route('/chat', methods=['POST'])
def chat():
    try:
        user_message = request.json.get('message', '').lower()  
        if not user_message:
            return jsonify({"response": "Please provide a valid message."}), 400

        bot_response = "I'm here to assist you with any queries. Please describe your symptoms."

        
        for symptom, medicine in medicines.items():
            if symptom in user_message:
                bot_response = f"You seem to have {symptom}. I recommend taking {medicine}."
                break

        return jsonify({"response": bot_response})
    except Exception as e:
        return jsonify({"error": f"An error occurred: {str(e)}"}), 500

if __name__ == '__main__':
    app.run(debug=True, port=5000)  
