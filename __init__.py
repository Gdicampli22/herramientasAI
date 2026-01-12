# Script to populate the database with sample hypotheses
from db.database import SessionLocal, Base, engine
from db.models import Hypothesis
from datetime import datetime

# Create tables if they don't exist
Base.metadata.create_all(bind=engine)

db = SessionLocal()

samples = [
    {
        "title": "Growth: Invite-a-friend feature",
        "problem": "Low organic user growth",
        "metric": "Invites per active user",
        "impact": 4.5,
        "confidence": 0.7,
        "effort": 3,
        "reach": 500,
        "stage": "Idea",
    },
    {
        "title": "Retention: Email reactivation campaign",
        "problem": "Users churn after 7 days",
        "metric": "DAU 7-day retention",
        "impact": 3.8,
        "confidence": 0.8,
        "effort": 2,
        "reach": 1000,
        "stage": "Research",
    },
    {
        "title": "Conversion: Simplify checkout flow",
        "problem": "High drop-off at payment stage",
        "metric": "Checkout completion rate",
        "impact": 5,
        "confidence": 0.9,
        "effort": 4,
        "reach": 2000,
        "stage": "Test",
    },
    {
        "title": "UX: Dark mode for dashboard",
        "problem": "Users request theme customization",
        "metric": "User satisfaction (CSAT)",
        "impact": 2.5,
        "confidence": 0.6,
        "effort": 1.5,
        "reach": 1500,
        "stage": "Learn",
    },
    {
        "title": "Performance: Optimize database queries",
        "problem": "Slow load times on large datasets",
        "metric": "Avg dashboard load time",
        "impact": 4.0,
        "confidence": 0.85,
        "effort": 3.5,
        "reach": 800,
        "stage": "Scale",
    },
]

for s in samples:
    h = Hypothesis(
        **s,
        priority_score=round((s["impact"] * s["confidence"]) / s["effort"], 2),
        success_probability=round(0.5 + (s["confidence"] - 0.3) * 0.5, 2),
        created_at=datetime.utcnow(),
    )
    db.add(h)

db.commit()
db.close()

print("✅ Sample hypotheses successfully added!")
