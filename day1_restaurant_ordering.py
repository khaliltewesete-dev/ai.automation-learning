from groq import Groq

# ضع الـ API Key الحقيقي من Groq هنا
client = Groq(api_key="gsk-proj-YOUR_API_KEY_HERE")

def get_menu(dish):
    return f"Yes, the {dish} is on the menu."

def check_availability(dish):
    return f"Yes, the {dish} is available."

def check_order_limit():
    return "We have reached the limit."

tools = [
    {
        "type": "function",
        "function": {
            "name": "get_menu",
            "description": "get the menu of the restaurant",
            "parameters": {
                "type": "object",
                "properties": {
                    "dish": {
                        "type": "string",
                        "description": "the dish you want to check"
                    }
                },
                "required": ["dish"]
            }
        }
    },
    {
        "type": "function",
        "function": {
            "name": "check_availability",
            "description": "check if the dish is available",
            "parameters": {
                "type": "object",
                "properties": {
                    "dish": {
                        "type": "string",
                        "description": "the dish you want to check"
                    }
                },
                "required": ["dish"]
            }
        }
    },
    {
        "type": "function",
        "function": {
            "name": "check_order_limit",
            "description": "check if the order limit has been reached",
            "parameters": {
                "type": "object",
                "properties": {
                    "limit": {
                        "type": "integer",
                        "description": "the limit of orders"
                    }
                }
            }
        }
    }
]

user_message = "I want to order a tagine"

response = client.chat.completions.create(
    model="mixtral-8x7b-32768",
    messages=[
        {"role": "user", "content": user_message}
    ],
    tools=tools
)

tools_call = response.choices[0].message.tool_calls[0]
function_name = tools_call.function.name
function_args = tools_call.function.arguments

if function_name == "get_menu":
    result = get_menu(**function_args)
    print(result)
    
    response2 = client.chat.completions.create(
        model="mixtral-8x7b-32768",
        messages=[
            {"role": "user", "content": user_message},
            {"role": "assistant", "content": response.choices[0].message.content},
            {
                "role": "user",
                "content": f"function result: {result}"
            }
        ],
        tools=tools
    )
    
    print(response2.choices[0].message.content)
