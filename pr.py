class GeneticDisease:
    def __init__(self, name, inheritance_pattern, gene=None, prevalence=None):
        self.name = name
        self.inheritance_pattern = inheritance_pattern
        self.gene = gene
        self.prevalence = prevalence

# Comprehensive disease database
GENETIC_DISEASES = {
    "x_linked_recessive": [
        GeneticDisease("Duchenne muscular dystrophy (DMD)", "x_linked_recessive", "DMD"),
        GeneticDisease("Becker muscular dystrophy", "x_linked_recessive", "DMD"),
        GeneticDisease("Hemophilia A", "x_linked_recessive", "F8"),
        GeneticDisease("Hemophilia B", "x_linked_recessive", "F9"),
        GeneticDisease("G6PD deficiency", "x_linked_recessive", "G6PD"),
        GeneticDisease("Hunter syndrome", "x_linked_recessive", "IDS"),
        GeneticDisease("Red-green color blindness", "x_linked_recessive", "OPN1LW/OPN1MW"),
        GeneticDisease("X-linked agammaglobulinemia", "x_linked_recessive", "BTK"),
        GeneticDisease("Chronic granulomatous disease", "x_linked_recessive", "CYBB"),
        GeneticDisease("Lesch-Nyhan syndrome", "x_linked_recessive", "HPRT1"),
        GeneticDisease("Ornithine transcarbamylase deficiency", "x_linked_recessive", "OTC"),
        GeneticDisease("Wiskott-Aldrich syndrome", "x_linked_recessive", "WAS"),
        GeneticDisease("Menkes disease", "x_linked_recessive", "ATP7A"),
        GeneticDisease("Fabry disease", "x_linked_recessive", "GLA"),
        GeneticDisease("X-linked adrenoleukodystrophy", "x_linked_recessive", "ABCD1"),
        GeneticDisease("X-linked SCID", "x_linked_recessive", "IL2RG"),
        GeneticDisease("X-linked sideroblastic anemia", "x_linked_recessive", "ALAS2"),
        GeneticDisease("X-linked hypohidrotic ectodermal dysplasia", "x_linked_recessive", "EDA"),
        GeneticDisease("Dyskeratosis congenita", "x_linked_recessive", "DKC1"),
        GeneticDisease("Alport syndrome (X-linked type)", "x_linked_recessive", "COL4A5"),
        GeneticDisease("Charcot-Marie-Tooth disease (CMTX1)", "x_linked_recessive", "GJB1")
    ],
    
    "x_linked_dominant": [
        GeneticDisease("Rett syndrome", "x_linked_dominant", "MECP2"),
        GeneticDisease("X-linked hypophosphatemic rickets", "x_linked_dominant", "PHEX"),
        GeneticDisease("Incontinentia pigmenti", "x_linked_dominant", "IKBKG"),
        GeneticDisease("Aicardi syndrome", "x_linked_dominant", "Unknown"),
        GeneticDisease("Fragile X syndrome", "x_linked_dominant", "FMR1")
    ],
    
    "autosomal_dominant": [
        GeneticDisease("Achondroplasia", "autosomal_dominant", "FGFR3"),
        GeneticDisease("Osteogenesis imperfecta", "autosomal_dominant", "COL1A1/COL1A2"),
        GeneticDisease("Marfan syndrome", "autosomal_dominant", "FBN1"),
        GeneticDisease("Ehlers-Danlos syndrome (AD type IV)", "autosomal_dominant", "COL3A1"),
        GeneticDisease("Hereditary multiple exostoses", "autosomal_dominant", "EXT1/EXT2"),
        GeneticDisease("Neurofibromatosis type 1", "autosomal_dominant", "NF1"),
        GeneticDisease("Neurofibromatosis type 2", "autosomal_dominant", "NF2"),
        GeneticDisease("Tuberous sclerosis", "autosomal_dominant", "TSC1/TSC2"),
        GeneticDisease("Huntington disease", "autosomal_dominant", "HTT"),
        GeneticDisease("Myotonic dystrophy type 1", "autosomal_dominant", "DMPK"),
        GeneticDisease("Spinocerebellar ataxias", "autosomal_dominant", "Various"),
        GeneticDisease("Familial hemiplegic migraine", "autosomal_dominant", "CACNA1A"),
        GeneticDisease("CADASIL", "autosomal_dominant", "NOTCH3"),
        GeneticDisease("Familial hypercholesterolemia", "autosomal_dominant", "LDLR"),
        GeneticDisease("Hypertrophic cardiomyopathy", "autosomal_dominant", "MYH7"),
        GeneticDisease("Long QT syndrome (AD forms)", "autosomal_dominant", "KCNQ1/KCNH2"),
        GeneticDisease("Hereditary hemorrhagic telangiectasia", "autosomal_dominant", "ENG/ACVRL1"),
        GeneticDisease("Familial adenomatous polyposis", "autosomal_dominant", "APC"),
        GeneticDisease("Adult polycystic kidney disease", "autosomal_dominant", "PKD1/PKD2"),
        GeneticDisease("Alport syndrome (rare AD form)", "autosomal_dominant", "COL4A3/COL4A4"),
        GeneticDisease("Porphyria (AD forms)", "autosomal_dominant", "Various"),
        GeneticDisease("Familial hypocalciuric hypercalcemia", "autosomal_dominant", "CASR"),
        GeneticDisease("Li-Fraumeni syndrome", "autosomal_dominant", "TP53"),
        GeneticDisease("Hereditary breast & ovarian cancer (BRCA1/2)", "autosomal_dominant", "BRCA1/BRCA2"),
        GeneticDisease("Lynch syndrome (HNPCC)", "autosomal_dominant", "MLH1/MSH2"),
        GeneticDisease("Retinoblastoma (AD predisposition)", "autosomal_dominant", "RB1"),
        GeneticDisease("Von Hippel-Lindau disease", "autosomal_dominant", "VHL"),
        GeneticDisease("MEN type 1", "autosomal_dominant", "MEN1"),
        GeneticDisease("MEN type 2A & 2B", "autosomal_dominant", "RET"),
        GeneticDisease("Cowden syndrome", "autosomal_dominant", "PTEN")
    ],
    
    "autosomal_recessive": [
        GeneticDisease("Cystic fibrosis", "autosomal_recessive", "CFTR"),
        GeneticDisease("Sickle cell anemia", "autosomal_recessive", "HBB"),
        GeneticDisease("Thalassemia", "autosomal_recessive", "HBA1/HBA2/HBB"),
        GeneticDisease("Phenylketonuria (PKU)", "autosomal_recessive", "PAH"),
        GeneticDisease("Tay-Sachs disease", "autosomal_recessive", "HEXA"),
        GeneticDisease("Albinism", "autosomal_recessive", "TYR"),
        GeneticDisease("Wilson disease", "autosomal_recessive", "ATP7B"),
        GeneticDisease("Spinal muscular atrophy", "autosomal_recessive", "SMN1")
    ],
    
    "y_linked": [
        GeneticDisease("Y chromosome infertility", "y_linked", "AZF regions"),
        GeneticDisease("Swyer syndrome", "y_linked", "SRY"),
        GeneticDisease("Hypertrichosis of the pinna", "y_linked", "Unknown")
    ]
}

class FamilyMember:
    def __init__(self, relation, gender, is_affected=False, disease=None, is_carrier=False):
        self.relation = relation
        self.gender = gender  # 'M' or 'F'
        self.is_affected = is_affected
        self.disease = disease
        self.is_carrier = is_carrier

class FamilyTree:
    def __init__(self, parent_number):
        self.parent_number = parent_number
        self.members = {}
        self.carrier_status = {}  # Store carrier analysis results
        
    def add_member(self, relation, gender, is_affected=False, disease=None, is_carrier=False):
        self.members[relation] = FamilyMember(relation, gender, is_affected, disease, is_carrier)

def display_inheritance_patterns():
    print("\nAvailable Inheritance Patterns:")
    print("1. Autosomal Dominant")
    print("2. Autosomal Recessive") 
    print("3. X-Linked Recessive")
    print("4. X-Linked Dominant")
    print("5. Y-Linked")

def get_inheritance_pattern_choice():
    while True:
        try:
            choice = int(input("Enter your choice (1-5): "))
            if 1 <= choice <= 5:
                patterns = ["autosomal_dominant", "autosomal_recessive", 
                           "x_linked_recessive", "x_linked_dominant", "y_linked"]
                return patterns[choice - 1]
            else:
                print("Please enter a number between 1 and 5")
        except ValueError:
            print("Please enter a valid number")

def display_diseases(pattern):
    print(f"\nDiseases under {pattern.replace('_', ' ').title()}:")
    diseases = GENETIC_DISEASES[pattern]
    for i, disease in enumerate(diseases, 1):
        print(f"{i}. {disease.name}")

def get_disease_choice(pattern):
    diseases = GENETIC_DISEASES[pattern]
    while True:
        try:
            choice = int(input(f"Select a disease (1-{len(diseases)}): "))
            if 1 <= choice <= len(diseases):
                return diseases[choice - 1]
            else:
                print(f"Please enter a number between 1 and {len(diseases)}")
        except ValueError:
            print("Please enter a valid number")

def collect_parent_info(parent_type, parent_num):
    print(f"\n=== Parent {parent_num}'s {parent_type} Information ===")
    
    has_disease = input(f"Did your {parent_type} have any genetic disease? (yes/no): ").lower().strip()
    
    if has_disease in ['yes', 'y']:
        display_inheritance_patterns()
        pattern = get_inheritance_pattern_choice()
        display_diseases(pattern)
        disease = get_disease_choice(pattern)
        return True, disease
    else:
        return False, None

def collect_siblings_info(parent_num):
    print(f"\n=== Parent {parent_num}'s Siblings Information ===")
    
    siblings = []
    try:
        num_siblings = int(input("How many siblings do you have (including yourself)? "))
        
        for i in range(num_siblings):
            print(f"\n--- Sibling {i+1} ---")
            gender = input(f"Gender of sibling {i+1} (M/F): ").upper().strip()
            
            if i == 0:
                relation = "You"
                is_self = True
            else:
                relation = f"Sibling {i+1}"
                is_self = False
            
            has_disease = input(f"Was {relation} affected by genetic disease? (yes/no): ").lower().strip()
            
            if has_disease in ['yes', 'y']:
                display_inheritance_patterns()
                pattern = get_inheritance_pattern_choice()
                display_diseases(pattern)
                disease = get_disease_choice(pattern)
                siblings.append((relation, gender, True, disease, is_self))
            else:
                siblings.append((relation, gender, False, None, is_self))
                
        return siblings
    except ValueError:
        print("Please enter a valid number")
        return []

def build_family_tree(parent_number):
    print(f"\n{'='*50}")
    print(f"Building Family Tree for Parent {parent_number}")
    print(f"{'='*50}")
    
    tree = FamilyTree(parent_number)
    
    # Collect father's information
    father_affected, father_disease = collect_parent_info("Father", parent_number)
    tree.add_member("Father", "M", father_affected, father_disease)
    
    # Collect mother's information  
    mother_affected, mother_disease = collect_parent_info("Mother", parent_number)
    tree.add_member("Mother", "F", mother_affected, mother_disease)
    
    # Collect siblings information
    siblings_info = collect_siblings_info(parent_number)
    
    for relation, gender, affected, disease, is_self in siblings_info:
        tree.add_member(relation, gender, affected, disease)
    
    return tree

def analyze_carrier_status(tree, parent_num):
    """Advanced carrier analysis using pedigree chart analysis"""
    print(f"\n{'='*60}")
    print(f"CARRIER ANALYSIS FOR PARENT {parent_num}")
    print(f"{'='*60}")
    
    # Get all diseases in the family
    family_diseases = set()
    for member in tree.members.values():
        if member.disease:
            family_diseases.add(member.disease)
    
    carrier_results = {}
    
    for disease in family_diseases:
        carrier_prob = calculate_carrier_probability(tree, disease)
        carrier_results[disease] = carrier_prob
        
        status = "HIGH CARRIER RISK" if carrier_prob >= 0.5 else "LOW CARRIER RISK"
        print(f"● {disease.name}: {status} ({carrier_prob*100:.1f}% probability)")
        
        # Update carrier status for the parent (You)
        if "You" in tree.members:
            if carrier_prob >= 0.5:
                tree.members["You"].is_carrier = True
                tree.carrier_status[disease.name] = "High probability carrier"
            else:
                tree.carrier_status[disease.name] = "Low probability carrier"
    
    return carrier_results

def calculate_carrier_probability(tree, disease):
    """Calculate carrier probability based on pedigree analysis"""
    pattern = disease.inheritance_pattern
    carrier_prob = 0.0
    
    if pattern == "autosomal_recessive":
        # For autosomal recessive: check if parents are carriers/affected
        father = tree.members.get("Father")
        mother = tree.members.get("Mother")
        
        # If both parents are carriers/affected, high probability
        if father and (father.is_affected or father.disease == disease):
            carrier_prob += 0.5
        if mother and (mother.is_affected or mother.disease == disease):
            carrier_prob += 0.5
            
        # If siblings are affected, increase probability
        affected_siblings = 0
        total_siblings = 0
        
        for rel, member in tree.members.items():
            if rel.startswith("Sibling") and rel != "You":
                total_siblings += 1
                if member.is_affected and member.disease == disease:
                    affected_siblings += 1
        
        if total_siblings > 0:
            carrier_prob += (affected_siblings / total_siblings) * 0.5
            
        carrier_prob = min(carrier_prob, 1.0)
        
    elif pattern in ["x_linked_recessive", "x_linked_dominant"]:
        # For X-linked: different calculation based on gender
        you = tree.members.get("You")
        if you and you.gender == 'F':
            # Female: check father and brothers
            father = tree.members.get("Father")
            if father and father.is_affected and father.disease == disease:
                carrier_prob = 1.0  # Daughter of affected father is always carrier
            else:
                # Check brothers
                affected_brothers = 0
                total_brothers = 0
                
                for rel, member in tree.members.items():
                    if rel.startswith("Sibling") and member.gender == 'M':
                        total_brothers += 1
                        if member.is_affected and member.disease == disease:
                            affected_brothers += 1
                
                if total_brothers > 0:
                    carrier_prob = (affected_brothers / total_brothers) * 0.7
        else:
            # Male: typically not carriers for X-linked (they're either affected or not)
            you = tree.members.get("You")
            if you and you.is_affected and you.disease == disease:
                carrier_prob = 1.0  # Affected males pass to daughters
            else:
                carrier_prob = 0.0
                
    elif pattern == "autosomal_dominant":
        # For dominant disorders, carrier status is different
        you = tree.members.get("You")
        if you and you.is_affected and you.disease == disease:
            carrier_prob = 1.0  # Affected individuals have 50% chance to pass
        else:
            # Check parents
            father = tree.members.get("Father")
            mother = tree.members.get("Mother")
            if (father and father.is_affected and father.disease == disease) or \
               (mother and mother.is_affected and mother.disease == disease):
                carrier_prob = 0.5  # 50% chance of inheriting dominant mutation
    
    return carrier_prob

def calculate_fetus_risk(tree1, tree2, disease, child_gender):
    """Calculate risk for unborn fetus based on carrier status and inheritance pattern"""
    risk_info = {}
    pattern = disease.inheritance_pattern
    
    # Get carrier probabilities for both parents
    carrier_prob1 = calculate_carrier_probability(tree1, disease)
    carrier_prob2 = calculate_carrier_probability(tree2, disease)
    
    if pattern == "autosomal_recessive":
        risk_info["description"] = "Autosomal Recessive Disorder"
        # Both parents need to be carriers
        risk = carrier_prob1 * carrier_prob2 * 0.25
        risk_info["risk"] = risk
        risk_info["explanation"] = f"Based on carrier probabilities: Parent 1 ({carrier_prob1*100:.1f}%), Parent 2 ({carrier_prob2*100:.1f}%)"
        
    elif pattern == "autosomal_dominant":
        risk_info["description"] = "Autosomal Dominant Disorder"
        # Only one parent needs to be affected/carrier
        risk = max(carrier_prob1, carrier_prob2) * 0.5
        risk_info["risk"] = risk
        risk_info["explanation"] = f"Based on carrier probabilities: Parent 1 ({carrier_prob1*100:.1f}%), Parent 2 ({carrier_prob2*100:.1f}%)"
        
    elif pattern == "x_linked_recessive":
        risk_info["description"] = "X-Linked Recessive Disorder"
        if child_gender == 'M':
            # Male child: risk depends on mother being carrier
            risk = carrier_prob1 if tree1.members["You"].gender == 'F' else carrier_prob2
            risk_info["risk"] = risk * 0.5
            risk_info["explanation"] = f"Male child risk based on mother's carrier probability"
        else:
            # Female child: typically carriers, low risk of being affected
            risk_info["risk"] = 0.0
            risk_info["explanation"] = "Female children are typically carriers, not affected"
            
    elif pattern == "x_linked_dominant":
        risk_info["description"] = "X-Linked Dominant Disorder"
        risk = max(carrier_prob1, carrier_prob2) * 0.5
        risk_info["risk"] = risk
        risk_info["explanation"] = f"Based on carrier probabilities of both parents"
        
    elif pattern == "y_linked":
        risk_info["description"] = "Y-Linked Disorder"
        if child_gender == 'M':
            # Only males can be affected, passed from father
            father_carrier = carrier_prob1 if tree1.members["You"].gender == 'M' else carrier_prob2
            risk_info["risk"] = father_carrier
            risk_info["explanation"] = "Y-linked disorders passed from father to son"
        else:
            risk_info["risk"] = 0.0
            risk_info["explanation"] = "Y-linked disorders only affect males"
    
    return risk_info

def perform_comprehensive_fetus_analysis(tree1, tree2):
    """Main analysis function for unborn fetus"""
    print(f"\n{'='*70}")
    print("COMPREHENSIVE FETUS GENETIC RISK ANALYSIS")
    print(f"{'='*70}")
    
    # Perform carrier analysis for both parents
    carrier_results1 = analyze_carrier_status(tree1, 1)
    carrier_results2 = analyze_carrier_status(tree2, 2)
    
    # Combine diseases from both families
    all_diseases = set()
    for disease in carrier_results1.keys():
        all_diseases.add(disease)
    for disease in carrier_results2.keys():
        all_diseases.add(disease)
    
    if not all_diseases:
        print("\n✓ No significant genetic risks identified in either family")
        print("✓ Fetus appears to have low genetic risk")
        return
    
    print(f"\n{'='*70}")
    print("FETUS RISK PREDICTION FOR MALE CHILD")
    print(f"{'='*70}")
    analyze_fetus_risks_by_gender(tree1, tree2, all_diseases, 'M')
    
    print(f"\n{'='*70}")
    print("FETUS RISK PREDICTION FOR FEMALE CHILD")
    print(f"{'='*70}")
    analyze_fetus_risks_by_gender(tree1, tree2, all_diseases, 'F')

def analyze_fetus_risks_by_gender(tree1, tree2, all_diseases, child_gender):
    """Analyze fetus risks for a specific gender"""
    high_risk_conditions = []
    moderate_risk_conditions = []
    low_risk_conditions = []
    
    for disease in all_diseases:
        risk_info = calculate_fetus_risk(tree1, tree2, disease, child_gender)
        risk_info['disease'] = disease
        
        if risk_info['risk'] >= 0.25:
            high_risk_conditions.append(risk_info)
        elif risk_info['risk'] > 0.05:
            moderate_risk_conditions.append(risk_info)
        else:
            low_risk_conditions.append(risk_info)
    
    gender_name = "MALE" if child_gender == 'M' else "FEMALE"
    
    if high_risk_conditions:
        print(f"\n🚨 HIGH RISK CONDITIONS FOR {gender_name} FETUS:")
        for condition in high_risk_conditions:
            print(f"\n● {condition['disease'].name}")
            print(f"  Pattern: {condition['description']}")
            print(f"  Risk: {condition['risk']*100:.1f}%")
            print(f"  Explanation: {condition['explanation']}")
    
    if moderate_risk_conditions:
        print(f"\n⚠️ MODERATE RISK CONDITIONS FOR {gender_name} FETUS:")
        for condition in moderate_risk_conditions:
            print(f"\n● {condition['disease'].name}")
            print(f"  Pattern: {condition['description']}")
            print(f"  Risk: {condition['risk']*100:.1f}%")
            print(f"  Explanation: {condition['explanation']}")
    
    if low_risk_conditions:
        print(f"\n✅ LOW RISK CONDITIONS FOR {gender_name} FETUS:")
        for condition in low_risk_conditions:
            print(f"\n● {condition['disease'].name}")
            print(f"  Pattern: {condition['description']}")
            print(f"  Risk: {condition['risk']*100:.1f}%")
            print(f"  Explanation: {condition['explanation']}")
    
    if not high_risk_conditions and not moderate_risk_conditions and not low_risk_conditions:
        print(f"\n✓ No significant genetic risks identified for {gender_name.lower()} fetus")

def display_family_summary(tree, parent_num):
    """Display a summary of the collected family information"""
    print(f"\nParent {parent_num}'s Family Summary:")
    print("-" * 40)
    
    affected_count = 0
    diseases_found = set()
    
    for relation, member in tree.members.items():
        status = "Affected" if member.is_affected else "Not Affected"
        carrier_status = " (Carrier)" if member.is_carrier else ""
        disease_info = f" - {member.disease.name}" if member.disease else ""
        print(f"{relation}: {status}{carrier_status}{disease_info}")
        
        if member.is_affected and member.disease:
            affected_count += 1
            diseases_found.add(member.disease.name)
    
    print(f"\nTotal affected family members: {affected_count}")
    print(f"Genetic diseases in family: {', '.join(diseases_found) if diseases_found else 'None'}")

def main():
    print("=== ADVANCED GENETIC DISEASE RISK PREDICTOR ===")
    print("This tool performs carrier analysis and predicts risks for unborn fetus")
    print("Uses pedigree chart analysis from both parents' family histories")
    print("\nDISCLAIMER: This is for educational purposes only.")
    print("Always consult with a genetic counselor for medical advice.")
    
    # Collect information for first parent
    print("\n" + "="*50)
    print("PARENT 1 FAMILY HISTORY")
    print("="*50)
    tree1 = build_family_tree(1)
    
    # Collect information for second parent
    print("\n" + "="*50)
    print("PARENT 2 FAMILY HISTORY")
    print("="*50)
    tree2 = build_family_tree(2)
    
    # Display family summaries
    display_family_summary(tree1, 1)
    display_family_summary(tree2, 2)
    
    # Perform comprehensive fetus risk analysis
    perform_comprehensive_fetus_analysis(tree1, tree2)
    
    # Final recommendations
    print(f"\n{'='*70}")
    print("RECOMMENDATIONS FOR PROSPECTIVE PARENTS")
    print(f"{'='*70}")
    print("1. Consider prenatal genetic testing based on identified risks")
    print("2. Discuss carrier screening with a genetic counselor")
    print("3. Consider preimplantation genetic diagnosis (PGD) for high-risk conditions")
    print("4. Maintain regular prenatal care and ultrasound monitoring")
    print("5. Early intervention can improve outcomes for many genetic conditions")
    print("6. Remember that carrier status does not guarantee affected offspring")
    print("\nThank you for using the Advanced Genetic Disease Risk Predictor!")

if __name__ == "__main__":
    main()