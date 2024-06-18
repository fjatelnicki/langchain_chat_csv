# Chat with CSV

This project enables users to interact with data stored in CSV files through natural language queries. It leverages the power of OpenAI's GPT-3.5 model to understand and respond to user queries by searching the CSV file for relevant information.

## Features

- **Upload CSV**: Users can upload their own CSV files.
- **Query CSV**: After uploading, users can ask questions related to the data in the CSV file.
- **Immediate Responses**: The system uses a language model to provide answers directly from the CSV content.

## How to Use

1. **Start the Application**: Run the Streamlit application.
2. **Upload a CSV File**: Use the file uploader to upload your CSV file.
3. **Ask Questions**: Enter your questions in the text area provided.
4. **Get Answers**: Press submit to see the answers extracted from the CSV.

## Setup

1. **Clone the Repository**: Clone this repository to your local machine.
2. **Install Dependencies**: Run `pip install -r requirements.txt` to install the required Python packages.
3. **Set Up Environment Variables**: Ensure your `.env` file contains the necessary API keys.
4. **Run the App**: Execute `streamlit run app.py` to start the application.

## Technologies Used

- Python
- Streamlit
- OpenAI GPT-3.5
- LangChain

## Configuration

Ensure that the `.env` file is set up with the following variable:
- `OPENAI_API_KEY`: Your OpenAI API key.
