# cat-vs-dog-classifier-CNN-

A binary image classifier that determines whether an image contains a dog or a cat.The train folder contains images of cat and dogs 20,000 images of dogs and cats.There are no duplicate images.
The test folder contains 5000 images of cats and dogs.
Each image has been preprocessed to 256x356 pixels with a batch size of 32.


Model Architecture:<br>
Input Data Shape: 256x256x3
Layer 1:<br>
Convolutional Layer 32 filter Filter shape: 3x3
Activation Function: ReLu
Max Pooling Pool shape: 2x2
Strides=2

Layer 2:<br>
Convolutional Layer 64, filter Filter shape: 3x3
Activation Function: ReLu
Max Pooling Pool shape: 2x2
Strides=2

Layer 3:<br>
Convolutional Layer 128, filter Filter shape: 3x3
Activation Function: ReLu
Max Pooling Pool shape: 2x2
Strides=2


Dense layer:
Flatten
Dense Size: 128
Activation Function: ReLu

Dense Size: 64
Activation Function: ReLu

Dense Size: 1
Activation Function: Sigmoid

Optimizer: Adam
Loss: binary_crossentropy
