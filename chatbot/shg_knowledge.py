"""
Thanjavur-focused SHG knowledge base.
Every scheme has answers in 3 languages: tamil, english, tanglish.
"""

SHG_SCHEMES = [
    # ---------------- 1. SHG Bank Linkage ----------------
    {
        "name": "SHG Bank Linkage Programme",
        "keywords": [
            "shg bank", "bank linkage", "shg loan", "group loan",
            "kadan", "bank kadan", "கடன்", "வங்கி கடன்"
        ],
        "answers": {
            "english": (
                "**SHG Bank Linkage Programme (SBLP)**\n\n"
                "• **What:** Banks provide loans to SHGs after 6 months of savings.\n"
                "• **Eligibility:** Group of 10-20 women, saving for 6 months.\n"
                "• **Loan:** 1-4x of group savings (first cycle up to Rs.1 lakh).\n"
                "• **Interest:** ~7% under DAY-NRLM.\n"
                "• **In Thanjavur:** Apply at IOB, Indian Bank, SBI, or Thanjavur DRDA."
            ),
            "tamil": (
                "**SHG வங்கி இணைப்பு திட்டம் (SBLP)**\n\n"
                "• **என்ன:** 6 மாதம் சேமிப்புக்கு பிறகு வங்கிகள் SHG-க்கு கடன் தரும்.\n"
                "• **தகுதி:** 10-20 பெண்கள் கொண்ட குழு, 6 மாதம் சேமிப்பு.\n"
                "• **கடன்:** குழு சேமிப்பின் 1-4 மடங்கு (முதல் சுற்று ரூ.1 லட்சம் வரை).\n"
                "• **வட்டி:** DAY-NRLM கீழ் ~7%.\n"
                "• **தஞ்சாவூரில்:** IOB, இந்தியன் வங்கி, SBI அல்லது DRDA அலுவலகத்தில்."
            ),
            "tanglish": (
                "**SHG Bank Linkage Programme (SBLP)**\n\n"
                "• **Enna:** 6 maasam savings panna appuram bank loan kudukkum.\n"
                "• **Eligibility:** 10-20 ponnunga group, 6 maasam save pannanum.\n"
                "• **Loan:** Group savings la 1-4 madangu (first cycle Rs.1 lakh varai).\n"
                "• **Interest:** DAY-NRLM la ~7%.\n"
                "• **Thanjavur la:** IOB, Indian Bank, SBI illa DRDA office la apply pannunga."
            ),
        },
    },

    # ---------------- 2. DAY-NRLM ----------------
    {
        "name": "DAY-NRLM",
        "keywords": [
            "nrlm", "day nrlm", "aajeevika", "rural livelihood",
            "தேசிய ஊரக", "deendayal"
        ],
        "answers": {
            "english": (
                "**Deendayal Antyodaya Yojana - NRLM**\n\n"
                "• **Goal:** Organize rural women into SHGs.\n"
                "• **Benefits:** Revolving Fund Rs.15,000, Community Investment Fund, "
                "interest subvention, skill training.\n"
                "• **Thanjavur:** Contact Thanjavur DRDA or BDO in your block."
            ),
            "tamil": (
                "**தீனதயாள் அந்த்யோதய யோஜனா - NRLM**\n\n"
                "• **நோக்கம்:** ஊரக பெண்களை SHG-களாக ஒழுங்கமைத்தல்.\n"
                "• **பயன்கள்:** சுழல் நிதி ரூ.15,000, CIF, வட்டி மானியம், திறன் பயிற்சி.\n"
                "• **தஞ்சாவூர்:** DRDA அலுவலகம் அல்லது வட்டார BDO-வை அணுகவும்."
            ),
            "tanglish": (
                "**DAY-NRLM Scheme**\n\n"
                "• **Nokkam:** Ooraga ponnungala SHG-a organize panna.\n"
                "• **Benefits:** Revolving fund Rs.15,000, CIF, interest subsidy, training.\n"
                "• **Thanjavur:** DRDA office illa unga block BDO-vai approach pannunga."
            ),
        },
    },

    # ---------------- 3. Mudra Yojana ----------------
    {
        "name": "Mudra Yojana",
        "keywords": [
            "mudra", "pmmy", "shishu", "kishor", "tarun",
            "முத்ரா", "business loan"
        ],
        "answers": {
            "english": (
                "**Pradhan Mantri Mudra Yojana**\n\n"
                "• **Shishu:** Up to Rs.50,000\n"
                "• **Kishor:** Rs.50,001 - Rs.5 lakh\n"
                "• **Tarun:** Rs.5 lakh - Rs.10 lakh\n"
                "• **Eligibility:** Any Indian citizen with a business plan.\n"
                "• **Thanjavur:** Apply at SBI, IOB, Indian Bank, City Union Bank."
            ),
            "tamil": (
                "**பிரதான் மந்திரி முத்ரா யோஜனா**\n\n"
                "• **ஷிஷு:** ரூ.50,000 வரை\n"
                "• **கிஷோர்:** ரூ.50,001 - ரூ.5 லட்சம்\n"
                "• **தருண்:** ரூ.5 லட்சம் - ரூ.10 லட்சம்\n"
                "• **தகுதி:** வணிக திட்டம் உள்ள எந்த இந்திய குடிமகனும்.\n"
                "• **தஞ்சாவூர்:** SBI, IOB, இந்தியன் வங்கி, CUB-ல் விண்ணப்பிக்கலாம்."
            ),
            "tanglish": (
                "**PM Mudra Yojana**\n\n"
                "• **Shishu:** Rs.50,000 varai\n"
                "• **Kishor:** Rs.50,001 - Rs.5 lakh\n"
                "• **Tarun:** Rs.5 lakh - Rs.10 lakh\n"
                "• **Eligibility:** Business plan irundha apply pannalam.\n"
                "• **Thanjavur:** SBI, IOB, Indian Bank, CUB la apply pannunga."
            ),
        },
    },

    # ---------------- 4. Stand-Up India ----------------
    {
        "name": "Stand-Up India",
        "keywords": [
            "stand up india", "standup", "women entrepreneur",
            "startup loan", "ஸ்டாண்ட் அப்"
        ],
        "answers": {
            "english": (
                "**Stand-Up India Scheme**\n\n"
                "• **What:** Loans for SC/ST & women entrepreneurs.\n"
                "• **Loan:** Rs.10 lakh - Rs.1 crore.\n"
                "• **Eligibility:** Women 18+, greenfield enterprise.\n"
                "• **Thanjavur:** Visit any scheduled bank branch. Website: www.standupmitra.in"
            ),
            "tamil": (
                "**ஸ்டாண்ட்-அப் இந்தியா திட்டம்**\n\n"
                "• **என்ன:** SC/ST மற்றும் பெண் தொழில்முனைவோருக்கு கடன்.\n"
                "• **கடன்:** ரூ.10 லட்சம் - ரூ.1 கோடி.\n"
                "• **தகுதி:** 18+ பெண்கள், புதிய நிறுவனம்.\n"
                "• **தஞ்சாவூர்:** SBI, இந்தியன் வங்கி, IOB கிளைகளில்."
            ),
            "tanglish": (
                "**Stand-Up India Loan**\n\n"
                "• **Enna:** SC/ST & ponnunga entrepreneurs-ku loan.\n"
                "• **Loan:** Rs.10 lakh - Rs.1 crore.\n"
                "• **Eligibility:** 18+ ponnu, puthu business.\n"
                "• **Thanjavur:** SBI, IOB, Indian Bank branch la apply pannunga."
            ),
        },
    },

    # ---------------- 5. Business Ideas ----------------
    {
        "name": "SHG Business Ideas - Thanjavur",
        "keywords": [
            "business idea", "small business", "income", "shg business",
            "thozhil", "வணிகம்", "தொழில்"
        ],
        "answers": {
            "english": (
                "**Top SHG Business Ideas for Thanjavur Women**\n\n"
                "1. Thanjavur Painting (Classical) - famous worldwide\n"
                "2. Thanjavur Dolls (Thalaiyatti Bommai)\n"
                "3. Handloom Sarees - cotton & silk\n"
                "4. Papad & Pickle Units\n"
                "5. Dairy & Poultry - delta region ideal\n"
                "6. Banana Chips & Snacks\n"
                "7. Coconut-based products\n"
                "8. Tailoring & Boutique\n"
                "9. Flower Cultivation\n"
                "10. Tiffin / Catering Services"
            ),
            "tamil": (
                "**தஞ்சாவூர் பெண்களுக்கு சிறந்த SHG வணிக யோசனைகள்**\n\n"
                "1. தஞ்சாவூர் ஓவியம் - உலகப் புகழ்பெற்றது\n"
                "2. தஞ்சாவூர் தலையாட்டி பொம்மை\n"
                "3. கைத்தறி புடவைகள்\n"
                "4. அப்பளம் & ஊறுகாய் தயாரிப்பு\n"
                "5. பால் & கோழி வளர்ப்பு\n"
                "6. வாழைக்காய் சிப்ஸ்\n"
                "7. தேங்காய் பொருட்கள்\n"
                "8. தையல் & பூட்டிக்\n"
                "9. மலர் சாகுபடி\n"
                "10. டிபன் / கேட்டரிங் சேவை"
            ),
            "tanglish": (
                "**Thanjavur Ponnunga-ku Best SHG Business Ideas**\n\n"
                "1. Thanjavur Painting - worldwide famous\n"
                "2. Thalaiyatti Bommai - traditional craft\n"
                "3. Handloom Sarees\n"
                "4. Papad & Pickle\n"
                "5. Dairy & Poultry\n"
                "6. Banana Chips\n"
                "7. Coconut products\n"
                "8. Tailoring / Boutique\n"
                "9. Flower Cultivation\n"
                "10. Tiffin / Catering"
            ),
        },
    },

    # ---------------- 6. How to Form SHG ----------------
    {
        "name": "SHG Formation",
        "keywords": [
            "form shg", "start shg", "create shg", "how to start",
            "shg epdi", "shg start", "குழு அமைக்க"
        ],
        "answers": {
            "english": (
                "**How to Form an SHG in Thanjavur**\n\n"
                "1. Gather 10-20 women from your village.\n"
                "2. Elect a leader, secretary, treasurer.\n"
                "3. Register with Thanjavur DRDA / Block office.\n"
                "4. Open a group savings account.\n"
                "5. Meet weekly, save fixed amount (Rs.50-Rs.200).\n"
                "6. Maintain records: minutes, ledger, passbook.\n"
                "7. After 6 months, apply for bank loan.\n\n"
                "Thanjavur DRDA: Near Collectorate, Thanjavur - 613001"
            ),
            "tamil": (
                "**தஞ்சாவூரில் SHG எப்படி அமைப்பது**\n\n"
                "1. உங்கள் கிராமத்தில் 10-20 பெண்களை சேர்க்கவும்.\n"
                "2. தலைவர், செயலாளர், பொருளாளர் தேர்ந்தெடுக்கவும்.\n"
                "3. DRDA / வட்டார அலுவலகத்தில் பதிவு செய்யவும்.\n"
                "4. குழு சேமிப்பு கணக்கு தொடங்கவும்.\n"
                "5. வாரந்தோறும் சந்தித்து சேமிக்கவும் (ரூ.50-ரூ.200).\n"
                "6. பதிவேடுகள் பராமரிக்கவும்.\n"
                "7. 6 மாதம் பின் வங்கி கடனுக்கு விண்ணப்பிக்கவும்.\n\n"
                "தஞ்சாவூர் DRDA: ஆட்சியர் அலுவலகம் அருகில், 613001"
            ),
            "tanglish": (
                "**Thanjavur la SHG Epdi Form Pannanum**\n\n"
                "1. Unga village la 10-20 ponnunga gather pannunga.\n"
                "2. Leader, Secretary, Treasurer select pannunga.\n"
                "3. DRDA / Block office la register pannunga.\n"
                "4. Group savings account open pannunga.\n"
                "5. Weekly meet panni save pannunga (Rs.50-Rs.200).\n"
                "6. Records maintain pannunga.\n"
                "7. 6 maasam savings panna appuram loan apply pannunga.\n\n"
                "DRDA Office: Collectorate pakkathula, Thanjavur - 613001"
            ),
        },
    },

    # ---------------- 7. Mahalir Thittam ----------------
    {
        "name": "Mahalir Thittam (TN)",
        "keywords": [
            "mahalir thittam", "tamil nadu shg",
            "மகளிர் திட்டம்", "magalir thittam"
        ],
        "answers": {
            "english": (
                "**Mahalir Thittam - Tamil Nadu Government**\n\n"
                "• **What:** TN govt's flagship SHG program (since 1989).\n"
                "• **Benefits:** Revolving fund, credit linkage, training.\n"
                "• **Thanjavur:** Over 12,000 active SHGs.\n"
                "  - Project Officer, Mahalir Thittam, Thanjavur\n"
                "  - Or your Panchayat President / VLW"
            ),
            "tamil": (
                "**மகளிர் திட்டம் - தமிழ்நாடு அரசு**\n\n"
                "• **என்ன:** தமிழ்நாடு அரசின் முக்கிய SHG திட்டம் (1989 முதல்).\n"
                "• **பயன்கள்:** சுழல் நிதி, கடன் இணைப்பு, பயிற்சி.\n"
                "• **தஞ்சாவூர்:** 12,000+ செயலில் உள்ள SHG-கள்.\n"
                "  - திட்ட அதிகாரி, மகளிர் திட்டம், தஞ்சாவூர்"
            ),
            "tanglish": (
                "**Mahalir Thittam (TN Govt)**\n\n"
                "• **Enna:** TN govt-oda main SHG program (1989 la start).\n"
                "• **Benefits:** Revolving fund, credit linkage, training.\n"
                "• **Thanjavur:** 12,000+ active SHGs.\n"
                "  - Project Officer, Mahalir Thittam, Thanjavur"
            ),
        },
    },

    # ---------------- 8. DRDA Contact ----------------
    {
        "name": "Thanjavur DRDA Contact",
        "keywords": [
            "drda", "contact", "office", "address", "phone",
            "தொடர்பு", "அலுவலகம்"
        ],
        "answers": {
            "english": (
                "**Thanjavur DRDA - Contact Details**\n\n"
                "Address: District Rural Development Agency,\n"
                "Collectorate Campus, Thanjavur - 613001\n\n"
                "Phone: 04362-230122\n"
                "Website: www.thanjavur.nic.in\n"
                "Email: drda.tnj@nic.in\n\n"
                "Blocks: Thanjavur, Orathanadu, Kumbakonam, Papanasam, "
                "Thiruvaiyaru, Budalur, Pattukkottai, Peravurani, Madukkur, "
                "Sethubhavachatram, Ammapettai, Thiruppanandal, Thiruvidaimarudur."
            ),
            "tamil": (
                "**தஞ்சாவூர் DRDA - தொடர்பு**\n\n"
                "முகவரி: மாவட்ட ஊரக வளர்ச்சி முகமை,\n"
                "ஆட்சியர் அலுவலக வளாகம், தஞ்சாவூர் - 613001\n\n"
                "தொலைபேசி: 04362-230122\n"
                "இணையம்: www.thanjavur.nic.in"
            ),
            "tanglish": (
                "**Thanjavur DRDA Contact**\n\n"
                "Address: DRDA, Collectorate Campus, Thanjavur - 613001\n"
                "Phone: 04362-230122\n"
                "Website: www.thanjavur.nic.in\n"
                "Email: drda.tnj@nic.in"
            ),
        },
    },

    # ---------------- 9. Kumbakonam ----------------
    {
        "name": "Kumbakonam SHG",
        "keywords": ["kumbakonam", "கும்பகோணம்"],
        "answers": {
            "english": (
                "**SHG Support in Kumbakonam**\n\n"
                "• Block Office: Kumbakonam BDO\n"
                "• Popular SHG: Brass lamp making, sarees, temple flower, dairy.\n"
                "• Banks: IOB, City Union Bank, Indian Bank\n"
                "• Special: Mahamaham festival - flower & catering SHGs get huge income."
            ),
            "tamil": (
                "**கும்பகோணத்தில் SHG**\n\n"
                "• வட்டார அலுவலகம்: கும்பகோணம் BDO\n"
                "• SHG செயல்பாடுகள்: பித்தளை விளக்கு, புடவை, கோயில் மாலை, பால்.\n"
                "• வங்கிகள்: IOB, CUB, இந்தியன் வங்கி\n"
                "• சிறப்பு: மகாமகம் திருவிழா"
            ),
            "tanglish": (
                "**Kumbakonam SHG Support**\n\n"
                "• Block Office: Kumbakonam BDO\n"
                "• Famous SHG work: Brass lamp, sarees, kovil malai, dairy.\n"
                "• Banks: IOB, CUB, Indian Bank\n"
                "• Special: Mahamaham festival la nalla income."
            ),
        },
    },

    # ---------------- 10. General Schemes ----------------
    {
        "name": "General Schemes",
        "keywords": [
            "government scheme", "govt scheme", "scheme",
            "அரசு திட்டம்", "schemes"
        ],
        "answers": {
            "english": (
                "**Key Government Schemes for SHG Women**\n\n"
                "1. DAY-NRLM - Revolving fund, CIF, training\n"
                "2. Mudra Yojana - Business loan up to Rs.10 lakh\n"
                "3. Stand-Up India - Rs.10 lakh - Rs.1 crore\n"
                "4. Mahalir Thittam (TN)\n"
                "5. PMEGP - Up to Rs.25 lakh\n"
                "6. Annapurna Scheme\n"
                "7. Mahila Samridhi Yojana\n"
                "8. Atal Pension Yojana\n"
                "9. PM Suraksha Bima Yojana\n\n"
                "Which scheme?"
            ),
            "tamil": (
                "**SHG பெண்களுக்கான முக்கிய அரசு திட்டங்கள்**\n\n"
                "1. DAY-NRLM\n"
                "2. முத்ரா யோஜனா\n"
                "3. ஸ்டாண்ட்-அப் இந்தியா\n"
                "4. மகளிர் திட்டம்\n"
                "5. PMEGP\n"
                "6. அன்னபூர்ணா திட்டம்\n"
                "7. மகிளா சம்ரித்தி யோஜனா\n"
                "8. அடல் பென்ஷன் யோஜனா\n"
                "9. PM சுரக்ஷா பீமா"
            ),
            "tanglish": (
                "**SHG Ponnunga-ku Important Govt Schemes**\n\n"
                "1. DAY-NRLM\n"
                "2. Mudra Yojana\n"
                "3. Stand-Up India\n"
                "4. Mahalir Thittam\n"
                "5. PMEGP\n"
                "6. Annapurna Scheme\n"
                "7. Mahila Samridhi Yojana\n"
                "8. Atal Pension Yojana\n"
                "9. PM Suraksha Bima\n\n"
                "Edhu pathi theriyanum?"
            ),
        },
    },
]


def get_shg_answer(user_message: str, language: str = "english"):
    """Return matching SHG answer in the requested language."""
    msg = user_message.lower()
    best_match = None
    best_score = 0

    for scheme in SHG_SCHEMES:
        score = sum(1 for kw in scheme["keywords"] if kw.lower() in msg)
        if score > best_score:
            best_score = score
            best_match = scheme

    if best_match:
        return best_match["answers"].get(language, best_match["answers"]["english"])
    return None