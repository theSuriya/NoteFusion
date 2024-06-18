import streamlit as st
from model import AllModels
from html_pdf import Pdf
from pdf_process import PdfExtract
from PIL import Image
model = AllModels()
roadmap_generator = Pdf()


st.title('NoteFusion')
st.markdown("""
    <style>
    .justified-text {
        text-align: justify;
    }
    </style>
    """, unsafe_allow_html=True)

# Sidebar Section
st.sidebar.title("About")

st.sidebar.caption("""
        <div class="justified-text">
           NoteFusion is an AI-powered educational assistant helps students by providing summarizing textbook content, and generating personalized study plans roadmap Pdf and converts image to Notes. Powered by the Gemini API and built with Streamlit.
        </div>
        """, unsafe_allow_html=True)

for _ in range(3):
        st.sidebar.write("") 

menu = ["Image To Notes", "Summarize Textbook", "Generate Roadmap PDF","Generate own book"]
choice = st.sidebar.selectbox("Choose an option", menu)

for _ in range(3):
        st.sidebar.write("") 

if choice == 'Generate Roadmap PDF':
    st.subheader('Generate Roadmap PDF')
    subjects = st.text_input("Enter the subjects you need help with (comma-separated)")
    if subjects:
        button = st.button("Generate RoadMap")
    if subjects and button:
        with st.spinner('creating...'):
            response = model.road_map_model(subjects)
            print(response)
            response = response.replace("```html", "")
            response = response.replace("```", "")
            pdf_bytes = roadmap_generator.pdf_creator(response)
            st.success("PDF generated successfully!")

            st.download_button("Download PDF", data=pdf_bytes, file_name="output.pdf", mime="application/pdf")

elif choice == "Summarize Textbook":
    st.subheader("Summarize Textbook")
    uploaded_file = st.file_uploader("Upload a textbook pdf", type=["pdf",'png','jpg','jpeg'])
    if uploaded_file:
        button = st.button("Generate Summary")
        type = uploaded_file.name.split('.')[-1]
        if type!='pdf':
            st.image(uploaded_file,caption='uploaded image')
        else:
             pdf_text = PdfExtract(uploaded_file)
    if uploaded_file and button:
        with st.spinner('creating...'):
            if type == 'pdf':
                response = model.summary_model(input_doc = pdf_text.extracted_text)
                st.write(response)
            else:
                img = Image.open(uploaded_file)
                response = model.summary_model(image=img)
                st.write(response)
                 

elif choice == "Generate own book":
    st.subheader("Create your own book")
    st.caption('Give the book name and pages our AI will create book for you')
    book_name = st.text_input("textbook Naame")
    if book_name:
        button = st.button("Generate Book")
    if book_name and button:
        with st.spinner('creating...'):
            response = model.book_creator(book_name)
            st.write(response)
            response = response.replace("```html", "")
            response = response.replace("```", "")
           
            pdf_bytes = roadmap_generator.pdf_creator(response)
            st.success("PDF generated successfully!")

            st.download_button("Download PDF", data=pdf_bytes, file_name="output.pdf", mime="application/pdf")

elif choice == "Image To Notes":
    st.subheader("Image To Notes")
    uploaded_file = st.file_uploader("Upload a image or screenshot", type=['png','jpg','jpeg'])
    if uploaded_file:
        st.image(uploaded_file,caption='uploaded image')
        
        button = st.button("Generate Notes")

    if uploaded_file and button:
        with st.spinner('creating...'):
            img = Image.open(uploaded_file)
            response = model.note_model(img)
            st.write(response)

        

     

   


