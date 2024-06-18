import google.generativeai as genai
import os
from dotenv import load_dotenv

load_dotenv()
os.environ["GOOGLE_API_KEY"] = os.getenv("GOOGLE_API_KEY")
genai.configure(api_key="AIzaSyDA6zE16NjMSYefmnIo74aJ8cacoDxJsrE")


class AllModels:
    def __init__(self):
       self.model = genai.GenerativeModel('gemini-1.5-flash-latest')


    def road_map_model(self,subjects):
        prompt = f"""Create an HTML format roadmap for learning {subjects} with proving week task . The roadmap should include the following sections:

        Introduction: Brief overview of the subject and its importance.

        Foundation: Fundamental concepts and theories to grasp before diving deeper.

        Intermediate Level: More advanced topics building upon the foundation.

        Advanced Level: Complex concepts, techniques, or applications within the subject.

        Resources: List of recommended books, online courses, tutorials, and websites for further learning using hyperlink tag.

        Projects: Hands-on projects or exercises to reinforce learning and apply knowledge.

        Conclusion: Summary of key takeaways and encouragement for further exploration.

        The HTML format should be visually appealing with appropriate headings, subheadings, bullet points, and hyperlinks where necessary. Ensure clarity and logical progression in the roadmap.
        NOTE: The roadmap should be provided in pure HTML format without any Markdown or other formatting styles and In the html format dont need style tags and title tags"""

        response = self.model.generate_content([prompt.format(subjects=subjects)]) 
        return response.text
    

    def summary_model(self,input_doc=None,image=None):
        if input_doc:
            prompt = """you are an intelligent assistant using the giving document summarize it shortly
            document:
            {document}
            """
            response = self.model.generate_content([prompt.format(document=input_doc)]) 
            return response.text
        elif image:
             prompt = """you are an intelligent assistant using the giving image summarize it and its content."""
             response = self.model.generate_content([prompt,image]) 
             return response.text


    

    def book_creator(self,book_name):
        prompt = """"Generate a detailed and extensive book titled '{book_title}'.
        Please provide the content in HTML format with appropriate tags for headings, paragraphs,
        NOTE: The book should be provided in pure "HTML" format without any "Markdown" or other formatting styles and In the html format dont need style tags and title tags
        Ensure the HTML is well-structured and valid. Here is the beginning of the book in HTML:\n\n
        <html>\n<head>\n<title>'{book_title}'</title>\n</head>\n<body>\n"
        <h1>'{book_title}'</h1>\n"
        <div>\n"""

        response = self.model.generate_content([prompt.format(book_title=book_name)]) 
        return response.text
    
    def note_model(self,img):
        prompt = """You are an intelligent Notes creator.create a notes using given screenshot
        important note: if the screenshot not contain any text means you must say 'please upload a valid screenshot."""

        response = self.model.generate_content([prompt,img]) 
        return response.text

