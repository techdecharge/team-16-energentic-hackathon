import asyncio
import uuid

from google.adk.agents import LlmAgent
from google.adk.runners import Runner
from google.adk.sessions import InMemorySessionService
from google.genai import types

# --- OpenAPI Tool Imports ---
from google.adk.tools.openapi_tool.openapi_spec_parser.openapi_toolset import OpenAPIToolset
from app import app
from app.schema import generate_schema
import json

# --- Constants ---
APP_NAME_OPENAPI = "openapi_petstore_app"
USER_ID_OPENAPI = "user_openapi_1"
SESSION_ID_OPENAPI = f"session_openapi_{uuid.uuid4()}" # Unique session ID
AGENT_NAME_OPENAPI = "demand_flexible_manager_agent"
GEMINI_MODEL = "gemini-2.0-flash"

openapi_schema = generate_schema(app)
openapi_spec_string = json.dumps(openapi_schema)

# --- Create OpenAPIToolset ---
generated_tools_list = []
try:
    # Instantiate the toolset with the spec string
    petstore_toolset = OpenAPIToolset(
        spec_str=openapi_spec_string,
        spec_str_type="json"
    )
    # Get all tools generated from the spec
    generated_tools_list = petstore_toolset.get_tools()
    print(f"Generated {len(generated_tools_list)} tools from OpenAPI spec:")
    for tool in generated_tools_list:
        # Tool names are snake_case versions of operationId
        print(f"- Tool Name: '{tool.name}', Description: {tool.description[:60]}...")

except ValueError as ve:
    print(f"Validation Error creating OpenAPIToolset: {ve}")
    # Handle error appropriately, maybe exit or skip agent creation
except Exception as e:
    print(f"Unexpected Error creating OpenAPIToolset: {e}")
    # Handle error appropriately

# --- Agent Definition ---
openapi_agent = LlmAgent(
    name=AGENT_NAME_OPENAPI,
    model=GEMINI_MODEL,
    tools=generated_tools_list,
    instruction=f"""You are a Demand Flexibility - DeCharge Procurement Agent assistant managing Demand flexibility via an API.
    Use the available tools to fulfill user requests.
    Available tools: {', '.join([t.name for t in generated_tools_list])}.
    When listing programs, mention any filters used (like program name or search criteria) and ask the user if he is interested.
    show the user his battery details after the program listing and ask the user if he is interested to participate in the program.
    after listing programs, store the company name, program name and its respective provider id and item id to it, so in future when user selects program name get the values from there.
    When confirming  get the provider by ID and item id in the request, state the ID's and program name you requested.
    after confirmation response ask the user to fetch the order detials 
    after order response ask the user consent to start batter discharge.
    while displaying the result instead of json show with appropriate format easy to read. 
    when fetching company details pass the company name and form the response show the consolidated data in numbers - like count of items.
    """,
    description="Manages a demand flexibility using tools generated from an OpenAPI spec."
)

root_agent = openapi_agent
