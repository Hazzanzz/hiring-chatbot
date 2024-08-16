import openai

openai.api_key = "YOUR_API_KEY"

def generate_questions(cv_data, previous_response):
    """Dynamically generate questions based on the candidate's CV and previous responses."""
    prompt = f"Based on the following CV data: {cv_data}, and previous response: {previous_response}, generate relevant interview questions."
    response = openai.Completion.create(engine="text-davinci-003", prompt=prompt, max_tokens=150)
    return response.choices[0].text.strip()
