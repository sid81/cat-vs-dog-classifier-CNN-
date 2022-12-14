# cat vs dog classifier-CNN



A binary image classifier that determines whether an image contains a dog or a cat.The train folder contains images of cat and dogs 20,000 images of dogs and cats.There are no duplicate images.
The test folder contains 5000 images of cats and dogs.
Each image has been preprocessed to 256x356 pixels with a batch size of 32.


### <b>Model Architecture:</b>
Input Data Shape: 256x256x3<br>
Layer 1:<br>
- Convolutional Layer 32 filter Filter shape: 3x3<br>
- Activation Function: ReLu<br>
- Max Pooling Pool shape: 2x2<br>
- Strides=2<br>

Layer 2:<br>
- Convolutional Layer 64, filter Filter shape: 3x3<br>
- Activation Function: ReLu<br>
- Max Pooling Pool shape: 2x2<br>
- Strides=2<br>

Layer 3:<br>
- Convolutional Layer 128, filter Filter shape: 3x3<br>
- Activation Function: ReLu<br>
- Max Pooling Pool shape: 2x2<br>
- Strides=2<br>


Dense layer:<br>
- Flatten<br>
- Dense Size: 128<br>
- Activation Function: ReLu<br>
- Dense Size: 64<br>
- Activation Function: ReLu<br>
- Dense Size: 1<br>
- Activation Function: Sigmoid<br>
- Optimizer: Adam<br>
- Loss: binary_crossentropy

## Model summary
![image](https://user-images.githubusercontent.com/68815179/198990662-873563bc-6568-46c5-b22d-fb4e776d1eb4.png)

## Conclusion
The Architecture and parameter used in this CNN network are capable of producing accuracy of 95.56% on Training data,85% on validation data,on which can be further improved.<br> 
After i have applied model using flask app which is shown below.

![image](https://user-images.githubusercontent.com/68815179/198992834-95610fa0-1212-4695-b36a-f70fc95ae491.png)

![image](https://user-images.githubusercontent.com/68815179/198992996-df991ab9-8af7-43a1-957d-1293fdd6c6c4.png)

![image](https://user-images.githubusercontent.com/68815179/198993051-419caa48-2961-49e7-b6e0-df2b20fc6bc0.png)


