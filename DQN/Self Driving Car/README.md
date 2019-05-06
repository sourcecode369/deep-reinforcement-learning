# Self Driving Car using Kivy
 
 This is going to be a modelled version of a car (so it won't be driving on the streets of real cities ;) ) but still - it will learn how to drive itself. And the key word here is **learn**, because the car will not be given any rules on how to operate in the environment before hand - it will have to figure everything out on it's own. And to achieve that we will be using Deep Q-Learning.

Deep Q-Learning is the result of combining Q-Learning with an Artificial Neural Network. The states of the environment are encoded by a vector which is passed as input into the Neural Network. Then the Neural Network will try to predict which action should be played, by returning as outputs a Q-value for each of the possible actions. Eventually, the best action to play is chosen by either taking the one that has the highest Q-value, or by overlaying a Softmax function. 

## Installation

 * #### Install NumPy >= 1.15.4
 
      `pip install numpy`
      
 * #### Install Matplotlib >= 3.0.2
 
      `pip install -q matplotlib`
 
 * #### Install PyTorch >= 1.1
      * `conda install pytorch-cpu torchvision-cpu -c pytorch` or,
      
      * `pip3 install https://download.pytorch.org/whl/cpu/torch-1.1.0-cp36-cp36m-win_amd64.whl` and,
      
      * `pip3 install torchvision`
 
 * #### Install Kivy
    It’s advisable to install Kivy with the development version for each OS. The development version can be found within the installation     instructions, for example: https://kivy.org/docs/installation/installation- osx.html. 
    
     
    You can install Kivy with Homebrew and pip using the following steps: 
    * Install the requirements using homebrew: 
    
        `$ brew install pkg-config sdl2 sdl2_image sdl2_ttf sdl2_mixer gstreamer`
        
    * Install Cython and Kivy using pip: 
         
         `$ pip install Cython==0.26.1`
         
    * To install the development version, use this in the second step: 
    
        `$ pip install https://github.com/kivy/kivy/archive/master.zip`
        
## How to Run
  * Activate the conda environment in which your dependencies are installed (optional)
  * Change your directory using `cd` on cmd and hover inside the `Self Driving Car` folder 
  * run `python map.py` 
  * enjoy!

## Results

#### `Before Training`
![before_training](https://github.com/sourcecode369/Deep-RL/blob/master/DQN/Self%20Driving%20Car/assets/before_training%20(2).gif)

#### `After Training`
![after_training](https://github.com/sourcecode369/Deep-RL/blob/master/DQN/Self%20Driving%20Car/assets/before_training%20(1).gif)
