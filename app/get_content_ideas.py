from langchain_core.tools import tool

@tool
def get_content_ideas(niche: str) -> str:
    """Get content format ideas for a given niche or topic.
    Use this when the user asks for content ideas, formats, or creative suggestions."""
    return (
        f"Content ideas for {niche}: "
        "1) Carousel post — break down a common myth in your niche into 5 slides. "
        "2) Reel — show a before and after transformation in 30 seconds. "
        "3) Story series — share 3 quick tips over 3 consecutive days. "
        "4) Long-form video — do a full tutorial or deep dive on a topic your audience keeps asking about."
    )