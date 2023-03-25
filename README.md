# ChemoAI

![logo](https://user-images.githubusercontent.com/91246296/227485787-44eaadd4-3a78-4cc9-b881-e49920537866.jpg)


ChemoAI is a virtual drug design assistant that allows users to input a molecule name or SMILES format and retrieve drug properties, such as target disease, molecular weight, pharmacokinetic profile, and toxicity. The app uses the OpenAI API to generate drug properties based on user input and provides a user-friendly interface for accessing this information.

### Follow-Up Prompts
ChemoAI now includes a new feature of follow-up prompts, which provides users with additional information and options based on their input. For example, if a user searches for a particular drug, the app may suggest follow-up prompts related to managing common side effects, learning about clinical trials, or exploring alternative treatments.

## Installation

To install ChemoAI, follow these steps:

    Clone the repository to your local machine.



    git clone https://github.com/USERNAME/ChemoAI.git

Install the required Python packages using pip.

    pip install -r requirements.txt

Set up your OpenAI API credentials by creating a file named .env in the root directory of the repository and adding the following lines with your API key:

    OPENAI_API_KEY=YOUR_API_KEY_HERE

## Usage

To use ChemoAI, run the app.py script from the command line.

    python chemoai.py

This will start the app and open a web interface that allows users to input a molecule name or SMILES format and retrieve drug properties. The app will call the OpenAI API to generate additional drug-related information based on user input and display this information on the web page.
![index](https://user-images.githubusercontent.com/91246296/227491711-c799be3f-94c8-419a-bff6-eed53fd041f0.JPG)

## Setting Up ChemoAI
ChemoAI is currently under development and is not yet ready for deployment. However, you can clone the repository to your local machine and explore the codebase to learn more about the app's functionality and architecture.

## Examples
Valid molecule names or SMILES strings that can be input into the app include:

    Aspirin: C9H8O4
    Ibuprofen: CC(C)CC1=CC=C(C=C1)C(C)C(=O)O
    Caffeine: CN1C=NC2=C1C(=O)N(C(=O)N2C)C

## Contributing

Contributions to ChemoAI are welcome! If you find a bug or have a suggestion for a new feature, please open an issue on the GitHub repository. If you would like to contribute code, please fork the repository, create a new branch, and submit a pull request with your changes.

## License

ChemoAI is licensed under the MIT License. See LICENSE for more information.

## Acknowledgements

ChemoAI was created using the OpenAI API and the Flask web framework. Thanks to the developers of these tools for their contributions to the open-source community.
