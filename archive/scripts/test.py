from scripts.data_service import DataService
from scripts.openai_service import OpenAIService

service = OpenAIService()
#response = service.get_completion(prompt_guc1)
#print(response)

data_service = DataService()

# Load context
context = data_service.get_context()

# Load ideas
json_ideen = data_service.get_ideen()
service.client.files.create()
print("Anazahl Zeichen:", len(str(json_ideen)))
print("Anzahl an Ideen:", len(json_ideen))
print(json_ideen)
