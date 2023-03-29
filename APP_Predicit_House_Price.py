import gradio as gr
import joblib as jb
import numpy as np
import tensorflow as tf


def predict01(sqft_living, sqft_lot, waterfront, view, grade, sqft_above, yr_built,
              zipcode, lat, long, sqft_living15, sqft_lot15):
    # load model
    model = tf.keras.models.load_model('/content/modelo_house_price.h5') # specify  to way for model

    # load scaler
    scaler_1 = joblib.load('/content/scaler.pkl') # specify to way for scaler

    X_test_scaled_1 = np.array([[sqft_living, sqft_lot, waterfront,
                                 view, grade, sqft_above, yr_built,
                                 zipcode, lat, long, sqft_living15,
                                 sqft_lot15]])

    # normalization
    # scaler_1 = MinMaxScaler()
    X_test_scaled_1 = scaler_1.transform(X_test_scaled_1)

    y_predict_1 = model.predict(X_test_scaled_1)

    p = scaler.inverse_transform(y_predict_1)[0]

    return {"Predicted House price is $": p[0]}


# inputs objects
sqft_living = gr.inputs.Number(label="Living area square feet - range (290 - 13540)")
sqft_lot = gr.inputs.Slider(minimum=1,
                            maximum=100000.0,
                            label="Lot area square feet")
waterfront = gr.inputs.Radio(['1', '0'],
                             label="Whether the property has a view to river, lake or sea")
view = gr.inputs.Slider(minimum=0,
                        maximum=4,
                        label="Overall view rating of the property ")
grade = gr.Dropdown(choices=['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13'],
                    type="value", label="Overall grade given to the housing unit")
sqft_above = gr.inputs.Slider(minimum=1,
                              maximum=10000,
                              label="Square feet of living area above ground level ")
yr_built = gr.inputs.Slider(minimum=1900,
                            maximum=2015,
                            label="Year the property was built")
zipcode = gr.inputs.Number(label="Zipcode - range (98001 - 98199)")
lat = gr.inputs.Textbox(label="Latitude - range (47.1559 - 47.7776)")
long = gr.inputs.Textbox(label=" Longitude - range (-122.515 - -121.315)")
sqft_living15 = gr.inputs.Slider(minimum=399,
                                 maximum=10000,
                                 label="Average living area square footage of the 15 nearest neighbors")
sqft_lot15 = gr.inputs.Slider(minimum=651,
                              maximum=10000,
                              label=" Average lot square footage of the 15 nearest neighbors")

# output object
Output = gr.outputs.Textbox()
# create interface
gui = gr.Interface(fn=predict01, inputs=[sqft_living, sqft_lot,
                                         waterfront, view, grade,
                                         sqft_above, yr_built, zipcode, lat, long,
                                         sqft_living15, sqft_lot15], outputs=[Output]);
# gui.launch(share=True) #debug = True
gui.launch(debug=True)



