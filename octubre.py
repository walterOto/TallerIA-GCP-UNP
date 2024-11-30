import google.generativeai as genai

api = "AIzaSyB1PrF3AoScetI7hcB6C5kA9Rh3tbfkdz4"
genai.configure(api)

# Create the model
generation_config = {
  "temperature": 1,
  "top_p": 0.95,
  "top_k": 40,
  "max_output_tokens": 8192,
  "response_mime_type": "text/plain",
}

model = genai.GenerativeModel(
  model_name="gemini-1.5-flash",
  generation_config=generation_config,
)

response = model.generate_content([
  "input: ¿Existe 26 Octubre?",
  "input 2: 26 Octubre pertenece a Piura",
  "input 3: 26 de Octubre es una fecha o distrito en Piura",
  "output: El distrito de Veintiséis de Octubre es uno de los diez distritos que conforman la provincia de Piura, ubicada en el departamento homónimo al norte del Perú. Desde el punto de vista de la jerarquía de la iglesia católica, forma parte de la Arquidiócesis de Piura.​",
  "output 2: Si, es nuevo",
  "input: ¿26 Octubre es de Piura o Lima?",
  "input 2: ",
  "input 3: ",
  "output: Pertenece a Piura pe",
  "output 2: ",
  "input: ",
  "input 2: ",
  "input 3: ",
  "output: ",
])

print(response.text)