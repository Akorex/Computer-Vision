def evaluate(image_path, model_path, dict_path, image_height=128, image_width=128, n_channels=3):
    """Function for a python script to determine the specie of a given bird input
    Imports the necessary dependencies for the function to work anywhere.
    Args:
        image_path - path to the jpg file of the bird specie
        model_path - path to the h5 model file
        dict_path - path to the pickle dictionary for classes
        image_height/width - required shape for image. defaults to 150
        n_channels - 3 for rgb. 1 for black & white
    """
    # import dependencies
    import os
    os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3'  # suppress tensorflow warnings
    import numpy as np
    import tensorflow as tf
    import matplotlib.pyplot as plt
    from tensorflow import keras
    from keras import models
    import pickle
    from tensorflow.keras.preprocessing.image import load_img, img_to_array

    # load the model
    model = models.load_model(model_path)
    
    # load the dict
    with open(dict_path, 'rb') as handle:
        class_dict = pickle.load(handle)
    
    # preprocess the image
    image = load_img(image_path, target_size=(image_height, image_width))

    # plot the image
    plt.imshow(image)
    plt.xticks([])
    plt.yticks([])

    # convert image to array & clip to 0-1 range
    image = img_to_array(image)
    image = np.array(image)
    image = image[:]/255
    image = np.expand_dims(image, axis=0)

    # feed image to model & predict
    pred = model.predict(image)
    pred = np.argmax(pred, axis=1)
    
    for key, value in class_dict.items():
        if pred == key:
            predicted_bird_specie = class_dict[key]
            print(f"Model Predicted: {predicted_bird_specie}")
    plt.title(predicted_bird_specie)
    plt.show()