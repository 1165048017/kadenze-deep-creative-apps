# Overview

Few guidance is given for the project, especially compared to the sessions. This is good, since it pushes me to develop my creative skills. It could also be overwhelming, so I have decided to take few working assumptions.

The main one is to use a pre-designed net, and ideally even a pre-trained one, and to work around it. Designing an advanced NN requires a lot of effort, training it involves a lot of computing power (not mentioning the iterations). On the contrary, importing a net with the trained parameters is super easy. It has been done several times in the course, like with the Google inception v5 to generate deep dream pictures.

Before joining the course, I have been following the generative artist [Anders Hoff](https://twitter.com/inconvergent) for a couple of months, and I remember to have been amazed by the [Sand Glyphs](http://inconvergent.net/generative/sand-glyphs/) and the powerful effect of this asemic writing. Note that this algorithm is not based on neural nets. Then I have discovered [Hardmaru](https://twitter.com/hardmaru) by the impressive [large images generation from latent vectors](http://blog.otoro.net/2016/04/01/generating-large-images-from-latent-vectors/). It happens that Hardmaru has implemented with TensorFlow a random handwriting generation based on the Alex Graves' [paper](http://arxiv.org/abs/1308.0850). Handwriting is highly personal and unique, so having an algorithm generating it is just AWESOME. It looks like a perfect playground for exploration.

The implementation of  Hardmaru is available on [GitHub](https://github.com/hardmaru/write-rnn-tensorflow). It was based on Python 2 and TensorFlow r0.5. The first step has been to upgrade to Python 3 and TensorFlow r0.11. Hardmaru has been nice enough to merge my push requests into the main repository. The network had to be trained again, but since there is no change of design, and I knew that the training would last a couple of hours on a CPU, it was OK.

**Note:** the content of this repository heavily relies on the Hardmaru' implementation of the random handwriting generation.
