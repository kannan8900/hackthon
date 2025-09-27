import datetime
import json

NORMAL_RANGES = {
    "weight_kg": (45, 120),  
    "blood_pressure_systolic": (90, 120),  
    "blood_pressure_diastolic": (60, 80),  
    "fetal_heart_rate": (110, 160), 
    "maternal_heart_rate": (60, 100), 
    "blood_sugar": (70, 140),  
    "hemoglobin": (11, 16), 
}


DATA_FILE = "prenatal_care_log.json"

def load_data():
    """Load logged data from file."""
    try:
        with open(DATA_FILE, "r") as file:
            return json.load(file)
    except FileNotFoundError:
        return {}

def save_data(data):
    """Save logged data to file."""
    with open(DATA_FILE, "w") as file:
        json.dump(data, file, indent=4)

def input_patient_info():
    """Input patient information from the user."""
    info = {}
    print("Enter patient information:")
    info["name"] = input("Full Name: ")
    info["age"] = int(input("Age: "))
    info["gestational_age_weeks"] = int(input("Gestational Age (weeks): "))
    info["contact_number"] = input("Contact Number: ")
    info["medical_history"] = input("Medical History: ")
    info["risk_factors"] = input("Risk Factors (e.g., smoking, alcohol): ")
    info["medications"] = input("Current Medications: ")
    return info

def input_health_metrics():
    """Input health metrics from the user."""
    metrics = {}
    print("Enter health metrics for the visit:")
    metrics["weight_kg"] = float(input("Weight (kg): "))
    metrics["blood_pressure_systolic"] = int(input("Blood Pressure (Systolic, mmHg): "))
    metrics["blood_pressure_diastolic"] = int(input("Blood Pressure (Diastolic, mmHg): "))
    metrics["fetal_heart_rate"] = int(input("Fetal Heart Rate (bpm): "))
    metrics["maternal_heart_rate"] = int(input("Maternal Heart Rate (bpm): "))
    metrics["blood_sugar"] = int(input("Blood Sugar (mg/dL): "))
    metrics["hemoglobin"] = float(input("Hemoglobin (g/dL): "))
    metrics["symptoms"] = input("Symptoms: ")
    metrics["notes"] = input("Additional notes: ")
    return metrics

def check_metrics(metrics):
    """Check if metrics are within normal ranges and provide advice."""
    flags = []
    for metric, value in metrics.items():
        if metric in NORMAL_RANGES:
            lower, upper = NORMAL_RANGES[metric]
            if not (lower <= value <= upper):
                flags.append(f"{metric} is out of range ({value}). Normal range: {lower}-{upper}")
    return flags

def schedule_next_visit(last_visit_date):
    """Schedule the next prenatal visit."""
    visit_interval = datetime.timedelta(weeks=4)  
    next_visit_date = last_visit_date + visit_interval
    return next_visit_date

def main():
    """Main function to run the prenatal care monitoring system."""
    data = load_data()
    print("Welcome to the Prenatal Care Monitoring System!")


    patient_id = input("Enter patient ID or name: ")
    if patient_id not in data:
        data[patient_id] = {"info": {}, "visits": [], "next_visit": None}
        data[patient_id]["info"] = input_patient_info()


    visit_date = datetime.date.today()
    print(f"\nRecording visit for {visit_date}")
    metrics = input_health_metrics()
    flags = check_metrics(metrics)


    visit_data = {
        "date": visit_date.isoformat(),
        "metrics": metrics,
        "flags": flags,
    }
    data[patient_id]["visits"].append(visit_data)


    next_visit_date = schedule_next_visit(visit_date)
    data[patient_id]["next_visit"] = next_visit_date.isoformat()
    print(f"\nNext prenatal visit scheduled for: {next_visit_date}")

    
    save_data(data)

    if flags:
        print("\nWarning: The following metrics are out of range:")
        for flag in flags:
            print(f"- {flag}")
        print("Please consult your healthcare provider.")
    else:
        print("\nAll metrics are within normal ranges. Keep up the good work!")

main()