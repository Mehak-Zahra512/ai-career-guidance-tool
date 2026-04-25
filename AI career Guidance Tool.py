# 🎓 AI Career Advisor System (Clean Final Version)

print("\n==============================")
print(" CAREER COMPASS AI SYSTEM")
print("==============================\n")

# ---------------- INPUT ----------------
marks_input = input("Enter your FSC/Intermediate percentage (e.g. 78 or 78%): ")
interest_input = input("Enter your interest (CS / Medical / Business / Engineering): ")

# ---------------- CLEAN INPUT ----------------
try:
    marks = float(marks_input.replace("%", "").strip())
except:
    print("\n Invalid marks input! Please enter a number like 78 or 78%")
    exit()

interest = interest_input.strip().lower()

print("\nAnalyzing your profile...\n")

# ---------------- CAREER DATA ----------------
careers = [
    {
        "field": "cs",
        "career": "Software Engineer / AI Engineer",
        "min_marks": 70,
        "reason": "High demand in AI, software, and tech industry"
    },
    {
        "field": "engineering",
        "career": "Civil / Electrical Engineer",
        "min_marks": 65,
        "reason": "Strong infrastructure and development opportunities"
    },
    {
        "field": "medical",
        "career": "Doctor / Pharmacist",
        "min_marks": 80,
        "reason": "Stable and respected healthcare profession"
    },
    {
        "field": "business",
        "career": "Business Analyst / Entrepreneur",
        "min_marks": 60,
        "reason": "Flexible career with startup and corporate growth"
    }
]

# ---------------- LOGIC ----------------
results = []

for c in careers:
    score = 0
    notes = []

    # Field match
    if interest == c["field"]:
        score += 60
    else:
        score += 25
        notes.append("Partial interest match")

    # Marks check
    gap = marks - c["min_marks"]

    if gap >= 0:
        score += 40
    elif gap >= -5:
        score += 25
        notes.append("Slightly below requirement")
    elif gap >= -10:
        score += 10
        notes.append("Below requirement")
    else:
        score += 0
        notes.append("Far below requirement")

    results.append({
        "career": c["career"],
        "score": score,
        "reason": c["reason"],
        "notes": notes
    })

# ---------------- SORT ----------------
results = sorted(results, key=lambda x: x["score"], reverse=True)

# ---------------- OUTPUT ----------------
print(" BEST CAREER MATCHES FOR YOU:\n")

for r in results:
    print(f"{r['career']}")
    print(f"Match Score: {r['score']}/100")
    print(f"Insight: {r['reason']}")

    if r["notes"]:
        for n in r["notes"]:
            print(" -", n)

    print("-" * 40)

print("\n Analysis Complete!")