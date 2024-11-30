import os
import google.generativeai as genai

genai.configure(api_key="AIzaSyAEQ67KTAMFL4G-Q6DItcJROHGPnh-Xm7k")

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
  "input: Existe 26 de Octubre en Piura?",
  "input 2: 26 de Octubre es un distrito de Piura?",
  "input 3: Cuántos distritos existen en la ciudad de Piura, 26 de Octubre es uno de ellos?",
  "output: El distrito de Veintiséis de Octubre es uno de los diez distritos que conforman la provincia de Piura, ubicada en el departamento homónimo al norte del Perú. Desde el punto de vista de la jerarquía de la iglesia católica, forma parte de la Arquidiócesis de Piura.1​",
  "output 2: La ciudad de Piura tiene 3 distritos: 26 de Octubre, Castilla y Piura.",
  "output 3: 26 de Octubre se encuentra al oeste de la ciudad.",
  "input: Existe 26 de Octubre en Piura",
  "input 2: Es 26 de Octubre una ciudad?",
  "input 3: Dónde se ubica 26 de Octubre?",
  "output: ",
])

print(response.text)