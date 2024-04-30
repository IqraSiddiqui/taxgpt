from django.shortcuts import render
from django.http import JsonResponse
from ..models import W2Data
from django.core.files import File
from pdf2image import convert_from_bytes
import requests
from rest_framework import generics
from io import BytesIO


class FileUploadView(generics.GenericAPIView):

    def extract_text_from_pdf(self, uploaded_file):
    # Read the contents of the uploaded file
        pdf_bytes = uploaded_file.read()

        # Convert the PDF bytes to images
        images = convert_from_bytes(pdf_bytes)

        label_ocr_dict = {}
        for i, image in enumerate(images):
            # Save each image to a file-like object (BytesIO)
            image_bytes = BytesIO()
            image.save(image_bytes, 'JPEG')

            # Send the image for OCR
            url = 'https://app.nanonets.com/api/v2/OCR/Model/b5450fc0-75d9-4771-af71-568850babc35/LabelFile/'
            data = {'file': image_bytes.getvalue()}  # Pass image bytes directly
            response = requests.post(url, auth=requests.auth.HTTPBasicAuth('d06c1a67-04df-11ef-837e-7a4a94e44568', ''), files=data)

            # Extract labels and OCR text
            for item in response.json()['result'][0]['prediction']:
                label_ocr_dict[item['label']] = item['ocr_text'].replace(',', '')

        return label_ocr_dict

    def post(self, request):
        if request.FILES.get('file'):
            uploaded_file = request.FILES['file']
            text = self.extract_text_from_pdf(uploaded_file)
            
            # Create a W2Data object and save it to the database
            w2_data = W2Data.objects.create(
                Employee_SSA_number=text.get("Employee's_SSA_number", ""),
                Employee_address=text.get("Employee's_address", ""),
                Employee_name=text.get("Employee's_name", ""),
                Employer_FED_ID=text.get("Employer's_FED_ID_number", ""),
                Gross_Pay=float(text.get('GROSS_PAY', 0)),
                Local_income_tax=float(text.get('LOCAL_INCOME_TAX', 0)),
                Medicare_tax=float(text.get('MEDICARE_TAX', 0)),
                Social_Security=float(text.get('SOCIAL_SECURITY', 0)),
                State_income_tax=float(text.get('STATE_INCOME_TAX', 0)),
                State_employer_state_id=int(text.get("State_Employer's_state_ID_no.", 0)),
                State_wages=float(text.get("State_wages,_tips,_etc.", 0)),
                Tax_withheld=float(text.get("TAX_WITHHELD_BOX_04_OF_W_-_2", 0))
            )
            
            # Return a JSON response indicating success
            return JsonResponse({'message': 'File uploaded and data stored successfully'})
        
        # If no file was uploaded
        return JsonResponse({'error': 'No file uploaded'}, status=400)
