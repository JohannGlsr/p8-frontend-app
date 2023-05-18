import requests
import streamlit as st
from PIL import Image
from io import BytesIO

def main():
    st.title("Application de segmentation d'images")

    image_file = st.file_uploader("Sélectionnez une image", type=['jpg', 'jpeg', 'png'])
    if image_file is not None:
        files = {'image': image_file}
        response = requests.post('https://azure-p8-api.azurewebsites.net/predict', files=files)
        if response.status_code == 200:
            st.success('Image segmentée avec succès.')
            flipped_image_bytes = response.content
            flipped_image = Image.open(BytesIO(flipped_image_bytes))
            st.image(flipped_image, use_column_width=True)
        else:
            st.error('Une erreur s\'est produite lors de la segmentation de l\'image.')

if __name__ == '__main__':
    main()
