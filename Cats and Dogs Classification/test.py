def evaluate(image_path, model_path, image_height=150, image_width=150, n_channels=3):
    """Function for a python script to determine if an image is either a cat or a dog.
    Imports the necessary dependencies for the function to work anywhere.
    Args:
        image_path - path to the jpg file of either a cat or a dog.
        model_path - path to the h5 model file
        image_height/width - required shape for image. defaults to 150
        n_channels - 3 for rgb. 1 for black & white
    """
    # import dependencies
    import numpy as np
    import tensorflow as tf
    import matplotlib.pyplot as plt
    from tensorflow import keras
    from keras import models
    from tensorflow.keras.preprocessing.image import load_img, img_to_array

    # load the model
    model = models.load_model(model_path)

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
    predict_proba = model.predict([image])

    # translate for use
    if predict_proba < 0.5:
        print("Model's Prediction: This is a cat.")
    else:
        print("Model's Prediction: This is a dog.")