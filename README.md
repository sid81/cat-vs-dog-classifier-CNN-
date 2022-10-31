# cat vs dog classifier-CNN



A binary image classifier that determines whether an image contains a dog or a cat.The train folder contains images of cat and dogs 20,000 images of dogs and cats.There are no duplicate images.
The test folder contains 5000 images of cats and dogs.
Each image has been preprocessed to 256x356 pixels with a batch size of 32.


### <b>Model Architecture:</b><br>
Input Data Shape: 256x256x3<br>
Layer 1:<br>
Convolutional Layer 32 filter Filter shape: 3x3<br>
Activation Function: ReLu<br>
Max Pooling Pool shape: 2x2<br>
Strides=2<br>

Layer 2:<br>
Convolutional Layer 64, filter Filter shape: 3x3<br>
Activation Function: ReLu<br>
Max Pooling Pool shape: 2x2<br>
Strides=2<br>

Layer 3:<br>
Convolutional Layer 128, filter Filter shape: 3x3<br>
Activation Function: ReLu<br>
Max Pooling Pool shape: 2x2<br>
Strides=2<br>


Dense layer:<br>
Flatten<br>
Dense Size: 128<br>
Activation Function: ReLu<br>

Dense Size: 64<br>
Activation Function: ReLu<br>

Dense Size: 1<br>
Activation Function: Sigmoid<br>

Optimizer: Adam<br>
Loss: binary_crossentropy
