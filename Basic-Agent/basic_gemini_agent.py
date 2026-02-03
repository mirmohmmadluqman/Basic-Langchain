from google import genai

# The client gets the API key from the environment variable `GEMINI_API_KEY`.
client = genai.Client()

response = client.models.generate_content(
    model="gemini-3-flash-preview", contents="Hello, my name is Mir Mohmmad Luqman"
)
print("Here's your response:")
print(response.text)