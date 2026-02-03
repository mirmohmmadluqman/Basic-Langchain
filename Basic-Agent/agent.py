from google import genai
from google.genai import types
import os

os.environ["GEMINI_API_KEY"] = "YOUR_API_KEY"

client = genai.Client()

def get_eth_balance(address: str) -> str:
    return f"Fake balance for {address}: 2.4 ETH"

tools = [
    types.Tool(
        function_declarations=[
            types.FunctionDeclaration(
                name="get_eth_balance",
                description="Get ETH balance for a wallet",
                parameters={
                    "type": "object",
                    "properties": {
                        "address": {"type": "string"}
                    },
                    "required": ["address"]
                }
            )
        ]
    )
]

config = types.GenerateContentConfig(
    tools=tools
)

prompt = "Check balance of 0x742d35Cc6634C0532925a3b8D7cDa223A56b8B04"

response = client.models.generate_content(
    model="gemini-3-flash-preview",
    contents=prompt,
    config=config
)

part = response.candidates[0].content.parts[0]

if part.function_call:
    args = part.function_call.args
    result = get_eth_balance(args["address"])
    print("Tool result:", result)
else:
    print(response.text)
