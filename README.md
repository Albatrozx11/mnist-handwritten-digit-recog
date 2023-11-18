# MNIST Handwritten Digit Recognition Project

This repository contains the code for a Handwritten Digit Recognition model using the MNIST dataset. The model is trained using a Jupyter Notebook (`Digit_recognition_using_mnist.ipynb`), and the final model is saved as `final_model.h5`. Additionally, there is a Python file (`main.py`) with a function to predict images using the trained model. It also includes a Gradio interface for easy testing.

## Project Structure

- `Digit_recognition_using_mnist.ipynb`: Jupyter Notebook for training the MNIST digit recognition model.
- `final_model.h5`: The saved model after training.
- `main.py`: Python file with a function for predicting digit images using the trained model.
- `gradio_interface`: Gradio interface for testing the model interactively.
- `sample_image.png`: A sample digit image for testing purposes.

## Usage

1. **Training the Model:** Open and run the `Digit_recognition_using_mnist.ipynb` notebook to train the model. The final model will be saved as `final_model.h5`.

2. **Prediction:** Use the `main.py` file to make predictions on new digit images. Modify the file to input your image and get the prediction.

3. **Gradio Interface:** Run the `main.py` script to start a web interface for testing the model interactively. Open the provided URL in your browser to test the model with the sample image or your custom images.

## Dependencies

- Python 3.x
- Dependencies listed in the Jupyter Notebook (`Digit_recognition_using_mnist.ipynb`).
- Gradio library (`pip install gradio`)

## License

This project is licensed under the [MIT License](LICENSE).

Feel free to explore and contribute to this project. If you have any questions or suggestions, please open an issue or reach out to [Your Name].

Happy coding!
