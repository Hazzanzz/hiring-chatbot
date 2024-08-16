def provide_feedback(response):
    """AI-driven feedback based on candidate's response."""
    prompt = f"Analyze this interview response and suggest improvements: {response}"
    feedback = openai.Completion.create(engine="text-davinci-003", prompt=prompt, max_tokens=150)
    return feedback.choices[0].text.strip()
