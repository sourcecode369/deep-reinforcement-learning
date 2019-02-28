[//]: # (Image References)

[image1]: https://user-images.githubusercontent.com/10624937/42135602-b0335606-7d12-11e8-8689-dd1cf9fa11a9.gif "Trained Agents"
[image2]: https://user-images.githubusercontent.com/10624937/42386929-76f671f0-8106-11e8-9376-f17da2ae852e.png "Kernel"
[image3]: https://spinningup.openai.com/en/latest/_images/spinning-up-in-rl.png "Spinning Up in Deep RL"
# Deep Reinforcement Learning 

![Trained Agents][image1]  

## Table of Contents

### Tutorials

The notebooks helps through implementing various algorithms in reinforcement learning. All of the codes are in PyTorch (v0.4) or TensorFlow(v1.7) and Python 3.

* [Dynamic Programming](https://github.com/udacity/deep-reinforcement-learning/tree/master/dynamic-programming): Dynamic Programming algorithms such as Policy Evaluation, Policy Improvement, Policy Iteration, and Value Iteration. 


### Labs / Projects

The labs and projects can be found below.  All of the projects use simulation environments from [Unity ML-Agents](https://github.com/Unity-Technologies/ml-agents). They are btter documented and requires good knowledge of the implemented algorithms to completely understand re-build.


### Resources

* [Cheatsheet](https://github.com/udacity/deep-reinforcement-learning/blob/master/cheatsheet): It is encouraged to use [this PDF file](https://github.com/udacity/deep-reinforcement-learning/blob/master/cheatsheet/cheatsheet.pdf) to better understand the reinforcement learning algorithms. 

## Dependencies

To set up the python environment to run the code in this repository, follow the instructions below.

1. Create (and activate) a new environment with Python 3.6.

	- __Linux__ or __Mac__: 
	```bash
	conda create --name drlnd python=3.6
	source activate drlnd
	```
	- __Windows__: 
	```bash
	conda create --name drlnd python=3.6 
	activate drlnd
	```
	
2. Follow the instructions in [this repository](https://github.com/openai/gym) to perform a minimal install of OpenAI gym.  
	- Next, install the **classic control** environment group by following the instructions [here](https://github.com/openai/gym#classic-control).
	- Then, install the **box2d** environment group by following the instructions [here](https://github.com/openai/gym#box2d).
	
3. Clone the repository (if you haven't already!), and navigate to the `python/` folder.  Then, install several dependencies.
```bash
git clone https://github.com/udacity/deep-reinforcement-learning.git
cd deep-reinforcement-learning/python
pip install .
```

4. Create an [IPython kernel](http://ipython.readthedocs.io/en/stable/install/kernel_install.html) for the `drlnd` environment.  
```bash
python -m ipykernel install --user --name drlnd --display-name "drlnd"
```

5. Before running code in a notebook, change the kernel to match the `drlnd` environment by using the drop-down `Kernel` menu. 

![Kernel][image2]

## Bibliography
 * [Spinning up in Deep RL](https://spinningup.openai.com/en/latest/index.html)an educational resource produced by OpenAI that makes it easier to learn about deep reinforcement learning (deep RL).
 
 * __David Silver's__ course on [Reinforcement Learning](https://www.youtube.com/watch?v=2pWv7GOvuf0&list=PLqYmG7hTraZDM-OYHWgPebj2MfCFzFObQ).
 
 * __UC Berkley and OpenAI's__ [Deep RL Bootcamp](https://sites.google.com/view/deep-rl-bootcamp/lectures).
 
 * Udacity's [Deep Reinforcement Learning Nanodegree](https://www.udacity.com/course/deep-reinforcement-learning-nanodegree--nd893) program helped me getting started and implementing algorithms and clearing the concepts within Deep Reinforcement learning. (__Highly Recommend__)
 <p align="center"><a href="https://www.udacity.com/course/deep-reinforcement-learning-nanodegree--nd893">
 <img width="503" height="133" src="https://user-images.githubusercontent.com/10624937/42135812-1829637e-7d16-11e8-9aa1-88056f23f51e.png"></a>
 </p>
 
  
