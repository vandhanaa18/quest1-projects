import os
from google import genai
from dotenv import load_dotenv


def get_nearby_restaurants(location: str):
    """
    Suggest popular restaurants for a given location.
    Uses Gemini to generate restaurant names dynamically.
    """

    # Lazy initialization
    load_dotenv()

    client = genai.Client(
        api_key=os.getenv("GOOGLE_API_KEY")
    )

    prompt = f"""
    You are a restaurant recommendation assistant.

    Suggest 5 popular restaurants in {location}, India.

    For each restaurant provide:
    - Restaurant name
    - Cuisine type
    - Approximate price range

    Use real and commonly known restaurants whenever possible.

    Return the response in this format:

    1. Restaurant Name
       Cuisine: ...
       Price Range: ...

    2. Restaurant Name
       Cuisine: ...
       Price Range: ...
    """

    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=prompt
    )

    return response.text