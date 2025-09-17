from typing import Any, Text, Dict, List
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher


class ActionRecommendCareer(Action):

    def name(self) -> Text:
        return "action_recommend_career"

    def run(
        self,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any]
    ) -> List[Dict[Text, Any]]:

        # Get user message
        msg = tracker.latest_message.get("text", "").lower()
        rec = ""

        # Creative / design careers
        if "photoshop" in msg or "design" in msg or "figma" in msg:
            rec = (
                "You mentioned design/creative tools.\n"
                "- Graphic Designer\n"
                "- UI/UX Designer\n"
                "- Visual Designer / Motion Graphics\n"
                "👉 Build a portfolio and practice real-world briefs."
            )

        # Technical / coding careers
        elif "python" in msg or "coding" in msg or "programming" in msg:
            rec = (
                "Looks like you’re interested in coding.\n"
                "- Software Developer\n"
                "- Data Analyst\n"
                "- Machine Learning Engineer\n"
                "👉 Start with projects, GitHub contributions, and coding challenges."
            )

        # Default fallback
        else:
            rec = (
                "I am not sure from that message. "
                "Tell me briefly: do you prefer technical, creative (arts), "
                "or commerce roles? Or mention 1–2 skills you have."
            )

        # Send response back to user
        dispatcher.utter_message(text=rec)
        return []
