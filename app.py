# -*- coding: utf-8 -*-
# """GRADIO.ipynb

# Automatically generated by Colaboratory.

# Original file is located at
#     https://colab.research.google.com/drive/1qoaxiKRdz3AeEq52UvMqIssT3ys4EOBa
# """

# pip install --quiet gradio

import numpy as np
import gradio as gr

from urllib.request import urlretrieve
urlretrieve("https://github.com/PRAMODVENKATESH/hugging-face-Similarity/blob/main/1682878_botinki_officine_creative_marshall_025_chernyy_kozha_natural_naya.JPG2.jpg?raw=true","image_1.jpg")
urlretrieve("https://github.com/PRAMODVENKATESH/hugging-face-Similarity/blob/main/1683465_sapogi_giovanni_fabiani_g3583_chernyy_zamsha_natural_naya.JPG2.jpg?raw=true","image_2.jpg")
urlretrieve("https://github.com/PRAMODVENKATESH/hugging-face-Similarity/blob/main/2283128_tufli_nero_giardini_e012011de_rozovyy_zamsha_natural_naya.JPG2.jpg?raw=true","image_3.jpg")
urlretrieve("https://github.com/PRAMODVENKATESH/hugging-face-Similarity/blob/main/636858_botinki_thierry_rabotin_9170m_chernyy_zamsha_natural_naya.JPG2.jpg?raw=true","image_4.jpg")
urlretrieve("https://github.com/PRAMODVENKATESH/hugging-face-Similarity/blob/main/758141_tufli_calvin_klein_twiggy_chernyy_kozha_natural_naya.JPG2.jpg?raw=true","image_5.jpg")
urlretrieve("https://github.com/PRAMODVENKATESH/hugging-face-Similarity/blob/main/778124_botinki_giovanni_fabiani_2135mo_chernyy_kozha_natural_naya.JPG2.jpg?raw=true","image_6.jpg")
urlretrieve("https://github.com/PRAMODVENKATESH/hugging-face-Similarity/blob/main/882830_botinki_thierry_rabotin_9171t_chernyy_kozha_natural_naya.JPG2.jpg?raw=true","image_7.jpg")
urlretrieve("https://github.com/PRAMODVENKATESH/hugging-face-Similarity/blob/main/883554_bosonozhki_calvin_klein_yusra_chernyy_tekstil_.JPG2.jpg?raw=true","image_8.jpg")
urlretrieve("https://github.com/PRAMODVENKATESH/hugging-face-Similarity/blob/main/884170_polubotinki_thierry_rabotin_1435mr_chernyy_zamsha_natural_naya.JPG2.jpg?raw=true", "image_9.jpg")
urlretrieve("https://github.com/PRAMODVENKATESH/hugging-face-Similarity/blob/main/968821_tufli_loriblu_wsj14_chernyy_zamsha_natural_naya.JPG2.jpg?raw=true","image_10.jpg")

demo = gr.Blocks()

def do_nothing(example: list) -> dict:
    return gr.Image.update(value=example[0])

def flip_text(x):
    return x[::-1]

def flip_image(x):
    return [np.fliplr(x),np.fliplr(x),np.fliplr(x),np.fliplr(x),np.fliplr(x)
    ,np.fliplr(x),np.fliplr(x),np.fliplr(x),np.fliplr(x),np.fliplr(x),
    np.fliplr(x),np.fliplr(x),np.fliplr(x),np.fliplr(x),np.fliplr(x),
    np.fliplr(x),np.fliplr(x),np.fliplr(x),np.fliplr(x),np.fliplr(x)]

with demo:
    gr.Markdown("Hybrid Search Demo.")
    with gr.Tabs():
        with gr.TabItem("Most Similar"):
            with gr.Row():
                image_input = gr.Image()
                image_output_1 = gr.Image()
                image_output_2 = gr.Image()
                image_output_3 = gr.Image()
                image_output_4 = gr.Image()
                image_output_5 = gr.Image()
            image_button = gr.Button("Hybrid Search")
        
        with gr.Row():
                inp = gr.Label("Attribute: +zip Probability > 0.85%")
                image_output_6 = gr.Image()
                image_output_7 = gr.Image()
                image_output_8 = gr.Image()
                image_output_9 = gr.Image()
                image_output_10 = gr.Image()

        with gr.Row():
                inp = gr.Label("Attribute: +velcro Probability > 0.85%")
                image_output_11 = gr.Image()
                image_output_12 = gr.Image()
                image_output_13 = gr.Image()
                image_output_14 = gr.Image()
                image_output_15 = gr.Image()

        with gr.Row():
                inp = gr.Label("Attribute: +High Heel Probability > 0.85%")
                image_output_16 = gr.Image()
                image_output_17 = gr.Image()
                image_output_18 = gr.Image()
                image_output_19 = gr.Image()
                image_output_20 = gr.Image()

        with gr.Row():
                inp = gr.Label("Attribute: +High Heel Probability > 0.85%")
                image_output_16 = gr.Image()
                image_output_17 = gr.Image()
                image_output_18 = gr.Image()
                image_output_19 = gr.Image()
                image_output_20 = gr.Image()
        
        with gr.Row():
                #input_image = gr.Image(label='Input Pose Image',
                                           #type='pil',
                                           #elem_id='input-image')
                example_images = gr.Dataset(components=[image_input],
                                                samples= [["image_1.jpg"], 
                                                ["image_2.jpg"],
                                                ["image_3.jpg"],
                                                ["image_4.jpg"],
                                                ["image_5.jpg"],
                                                ["image_6.jpg"],
                                                ["image_7.jpg"],
                                                ["image_8.jpg"],
                                                ["image_9.jpg"],
                                                ["image_10.jpg"]])

        
                

    #text_button.click(flip_text, inputs=text_input, outputs=text_output)
    image_button.click(flip_image, inputs=image_input, outputs=[image_output_1, image_output_2, image_output_3, 
                                                                image_output_4, image_output_5, image_output_6
                                                                , image_output_7, image_output_8, image_output_9
                                                                , image_output_10, image_output_11, image_output_12
                                                                ,image_output_13, image_output_14, image_output_15
                                                                ,image_output_16, image_output_17, image_output_18
                                                                ,image_output_19, image_output_20])
    example_images.click(fn=do_nothing,
                             inputs=example_images,
                             outputs=example_images.components)

demo.launch()