VIOLATION_PENALTIES = {
    "Dresscode": ["Memorize Mission-Vision", "Community Service", "Suspension"],
    "No Motor Sticker": ["Warning", "Parent Conference", "Suspension"],
    "Late Submission": ["Warning", "Extra Assignment", "Suspension"],
    "Absent without Leave": ["Warning", "Detention", "Suspension"]
}

def calculate_penalty(violation_type, offense_count):
    if violation_type in VIOLATION_PENALTIES:
        penalties = VIOLATION_PENALTIES[violation_type]
        return penalties[offense_count-1] if offense_count <= len(penalties) else penalties[-1]
    return "Warning"