from azure.identity import DefaultAzureCredential
from azure.ai.projects import AIProjectClient

project_endpoint = "https://{resource-name}.services.ai.azure.com/api/projects/<project-name>"
project_client = AIProjectClient(
    credential=DefaultAzureCredential(),
    endpoint=project_endpoint
)
openai_client = project_client.get_openai_client(api_version="2024-10-21")

response = client.responses.create(
    model="gpt-4.1",
    instructions="You are a helpful AI assistant that answers questions clearly and concisely.",
    input="Explain neural networks."
)

print(response.output_text)

# Track responses
last_response_id = None

# Loop until the user wants to quit
print("Assistant: Enter a prompt (or type 'quit' to exit)")
while True:
    input_text = input('\nYou: ')
    if input_text.lower() == "quit":
        print("Assistant: Goodbye!")
        break

    # Get a response
    response = openai_client.responses.create(
                model=model_name,
                instructions="You are a helpful AI assistant that explains technology concepts clearly.",
                input=input_text,
                previous_response_id=last_response_id
    )
    assistant_text = response.output_text
    print("\nAssistant:", assistant_text)
    last_response_id = response.id

    try:
        # Start with initial message
        conversation_history = [
            {
                "type": "message",
                "role": "user",
                "content": "What is machine learning?"
            }
        ]

        # First response
        response1 = openai_client.responses.create(
            model="gpt-4.1",
            input=conversation_history
        )

        print("Assistant:", response1.output_text)

        # Add assistant response to history
        conversation_history += response1.output

        # Add new user message
        conversation_history.append({
            "type": "message",
            "role": "user",
            "content": "Can you give me an example?"
        })

        # Second response with full history
        response2 = openai_client.responses.create(
            model="gpt-4.1",
            input=conversation_history
        )

        print("Assistant:", response2.output_text)

    except Exception as ex:
        print(f"Error: {ex}")