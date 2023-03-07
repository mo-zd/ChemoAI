# ChemoAI

ChemoAI is a virtual drug design assistant that allows users to input a molecule name or SMILES/MOL2 format and retrieve drug properties, such as target disease, molecular weight, pharmacokinetic profile, and toxicity. The app uses the OpenAI API to generate drug properties based on user input and provides a user-friendly interface for accessing this information.

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

    python app.py

This will start the app and open a web interface that allows users to input a molecule name or SMILES/MOL2 format and retrieve drug properties. The app will call the OpenAI API to generate additional drug-related information based on user input and display this information on the web page.

## Contributing

Contributions to ChemoAI are welcome! If you find a bug or have a suggestion for a new feature, please open an issue on the GitHub repository. If you would like to contribute code, please fork the repository, create a new branch, and submit a pull request with your changes.

## License

ChemoAI is licensed under the MIT License. See LICENSE for more information.

## Acknowledgements

ChemoAI was created using the OpenAI API and the Flask web framework. Thanks to the developers of these tools for their contributions to the open-source community.
