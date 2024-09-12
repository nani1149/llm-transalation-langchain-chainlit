import openai
from google.auth import default, transport
from langchain import PromptTemplate
# Build
from langchain_openai import ChatOpenAI
from vertexai.preview import rag

credentials, _ = default(scopes=['https://www.googleapis.com/auth/cloud-platform'])
auth_request = transport.requests.Request()
credentials.refresh(auth_request)


MODEL_LOCATION = "us-central1"
PROJECT_ID='sacred-alliance-433217-e3'
MODEL_ID = "meta/llama3-405b-instruct-maas"  # @param {type:"string"} ["meta/llama3-405b-instruct-maas"]

llm = ChatOpenAI(
    model=MODEL_ID,
    base_url=f"https://{MODEL_LOCATION}-aiplatform.googleapis.com/v1beta1/projects/{PROJECT_ID}/locations/{MODEL_LOCATION}/endpoints/openapi/chat/completions?",
    api_key=credentials.token,
)
