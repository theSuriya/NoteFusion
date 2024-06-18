# NoteFusion

NoteFusion is an AI-powered educational assistant built with Streamlit. It helps students by summarizing textbooks, generating personalized study plans and roadmaps, converting images to notes, and creating personalized books. Perfect for enhancing your learning experience!

## Features

- **Summarize Textbook**: Upload a textbook PDF or an image, and NoteFusion will generate a concise summary of the content.
- **Generate Roadmap PDF**: Enter subjects you need help with, and NoteFusion will create a personalized study plan and generate a PDF roadmap.
- **Generate Your Own Book**: Provide the name of your book, and NoteFusion's AI will create a personalized book for you.
- **Image to Notes**: Upload an image or screenshot, and NoteFusion will convert it to detailed notes.

## Installation

1. Clone the repository:

    ```sh
    git clone https://github.com/theSuriya/NoteFusion.git
    cd NoteFusion
    ```

2. Create a virtual environment and activate it:

    ```bash
   python -m venv ./venv
   cd venv\Scripts
   activate
    ```
    
3. Google API KEY:
Go to this site to generate api key [HERE](https://aistudio.google.com) You can see left side generate api thn click and copy. Once you have the api key, locate the .env file in your project directory. Open it and paste your api key like this:
  ```bash
  GOOGLE_API_KEY = "paste the api key here"
  ```
4. Install the required packages:

    ```sh
    pip install -r requirements.txt
    ```

5. Run the Streamlit app:

    ```sh
    streamlit run app.py
    ```

## Usage

Once the app is running, you can access it in your web browser. Use the sidebar to select the desired functionality:

- **Summarize Textbook**: Upload a textbook PDF or image to get a summary.
- **Generate Roadmap PDF**: Enter subjects to get a personalized study plan in PDF format.
- **Generate Your Own Book**: Provide the name of the book you want to create.
- **Image to Notes**: Upload an image or screenshot to convert it to notes.

## File Structure

```plaintext
NoteFusion/
├── app.py                  # Main application file
├── model.py                # Contains all AI model classes
├── html_pdf.py             # Module for PDF generation
├── pdf_process.py          # Module for PDF processing
├── requirements.txt        # Python packages required
└── README.md               # Readme file
```

## Contributing
Contributions are welcome! Please fork the repository and create a pull request with your changes.

## License
This project is licensed under the MIT License.

## Contact
For any inquiries or issues, please open an issue in the repository or contact thesuriya3@gmail.com.
