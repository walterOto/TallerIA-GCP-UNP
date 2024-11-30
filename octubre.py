import os
import google.generativeai as genai

genai.configure(api_key="AIzaSyBWydmHuDJjc5K4q7TH85lmHPtrrqfmzlY")

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
  "input: ¿existe 26 de octubre?",
  "input 2: 26 de octubre pertenece a Piura",
  "input 3: ¿26 de octubre es una fecha o un distrito de Piura?",
  "output: El distrito de Veintiséis de Octubre es uno de los diez distritos que conforman la provincia de Piura, ubicada en el departamento homónimo al norte del Perú. Desde el punto de vista de la jerarquía de la iglesia católica, forma parte de la Arquidiócesis de Piura.1​",
  "input: 26 de octubre es de piura o lima?",
  "input 2: 26 de octubre es de piura o lima?",
  "input 3: 26 de octubre es de piura o lima?",
  "output: ",
])

print(response.text)
