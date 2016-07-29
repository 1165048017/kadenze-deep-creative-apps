# kadenze-deep-creative-apps
Kandenze creative applications of deep learning in TensorFlow assignments

**Disclaimer:** be aware of the Kadenze code of conduct if you are enrolled in the course. Copying the code from this repository and pretending it to be sure would be bad (evil). Even looking into it may be an infringement. Plagiarism is not tolerated. You are now informed, behave with honor. 

## Installation and setup

You can find the installation instruction on the [CADL repository][cadl-install]. I have a slightly different setup since I use Anaconda.

On OS X, download the Anaconda [installation script][continuum-download] for Python 3.5 and follow the Continuum instructions. Then, install TensorFlow:

````
$ conda create -n tensorflow python=3.5
$ source activate tensorflow
(tensorflow)$ conda install ipykernel
(tensorflow)$ export TF_BINARY_URL=https://storage.googleapis.com/tensorflow/mac/tensorflow-0.9.0-py3-none-any.whl
(tensorflow)$ pip install --upgrade --ignore-installed $TF_BINARY_URL
`````

## Credits

+ all credits go to [Parag Mital][pkmital] and [Kadenze][kadenze] and all materials are distributed under the Apache license v2.0

[cadl-install]: https://github.com/pkmital/CADL#what-is-notebook
[continuum-download]: https://www.continuum.io/downloads#_macosx
[pkmital]: https://github.com/pkmital
[kadenze]: https://www.kadenze.com/
