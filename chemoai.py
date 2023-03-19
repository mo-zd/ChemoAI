from flask import Flask, render_template, request
import openai
import json
import os

app = Flask(__name__)

# Set up OpenAI API credentials
openai.api_key = os.environ.get("OPENAI_API_KEY")

# Define function to generate drug properties
def get_drug_properties(input_molecule):
    try:
        # Call OpenAI API to generate drug properties
        response = openai.Completion.create(
            engine="text-davinci-002",
            prompt="Get drug properties for " + input_molecule + ".",
            max_tokens=1024,
            n=1,
            stop=None,
            temperature=0.5,
        )

        # Parse response and extract drug properties
        output_text = response.choices[0].text
        drug_properties = json.loads(output_text)

        # Return drug properties
        return drug_properties
    except Exception as e:
        print(f"Error: {e}")
        return None

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/drug_properties', methods=['POST'])
def drug_properties():
    molecule_name = request.form['molecule_name']
    drug_properties = get_drug_properties(molecule_name)

    if drug_properties is None:
        return render_template('error.html', error_message="Failed to get drug properties.")
    else:
        return render_template('drug_properties.html', drug_properties=drug_properties)

if __name__ == '__main__':
    app.run(debug=True)
