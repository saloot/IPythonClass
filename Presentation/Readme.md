How to Make Slideshows Using IPython Notebooks
===================

IPython Notebooks can also be used to make slide shows. All you have to do is to follow a few simple steps and then render the presentation in your browser. Here's how it works.


Creating the Slides
--------
The slides are created in the same way that each block of code is created: using *cells*. To create a slide, simply select *slideshow* in the *Cell Toolbar* (see the figure below).


Then, select the appropriate cell type from the corresponding dropdown menu (we selected *Markdown* for the example below).


The result should like this



If you select *Markdown*, you can style your slides according to Markdown conventions or even use **HTML**.




Selected results from the paper
--------
Our analysis shows that the increase in the amount of CO2 in the atmosphere is correlated with the increase in oceans' heat content. See the figure below.

<img src="https://documents.epfl.ch/users/s/sa/salavati/public/IPythonClassPhotos/AtmosphericCO2.png" width=600>
<br>

Executing the Code
---------

1. First, download the IPython notebook, either from this [GitHub link](https://github.com/saloot/IPythonClass/blob/master/Sample%20Paper/Paper%20Code/CO2Example.ipynb)
or directly from [this link](http://some_links) (we recommend the GitHub method).
2. Open a terminal/command line window and move to the directory the IPython Notebook is located. 
3. In the command line, type

    ```ipython notebook```
4. Consequently, a browser window pops up. Navigate to the browser window and select the IPython Notebook. 
5. You can then adjust parameters of the code and run different decoders.


### Required Packages
* A working distribution of [Python 2.7](https://www.python.org/downloads/).
* The code relies heavily on [Numpy](http://www.numpy.org/), and [matplotlib](http://matplotlib.org).
* It also depends on several other standard Python packages, such as [os](https://docs.python.org/3/library/os.html), [sys](https://docs.python.org/3/library/sys.html), [getopt](https://docs.python.org/3/library/getopt.html), [pdb](https://docs.python.org/3/library/pdb.html) and [random](https://docs.python.org/3/library/random.html).

### Tested on...
The code has been tested on Mac OS X 10.7, 10.8, 10.9, and on Ubuntu linux.



License
-------

2013-2015 (c) Author 1 and Author 2.

This work is licensed under the Creative Commons
Attribution-NonCommercial-ShareAlike 4.0 International License. To view a copy
of this license, visit [this link](http://creativecommons.org/licenses/by-nc-sa/4.0/).

The code is free to reuse for non-commercial and academic purposes. However,
please acknowledge its use with the following citation.

    @article{EPFL-JOUR-204991,
       author      = {Author 1 and Author 2},
       title       = {Paper Title},
       journal     = {Some journal}
       volume      = 1,
       year        = 2016,
       ee          = {http://link_to_paper.ch}
    }


Contact
-------
For any other purposes, please contact the authors.

Author 1
([email](mailto:first[dot]last[at]epfl[dot]ch))
([homepage](http://google.com))

Author 2
([email](mailto:first2[dot]last2[at]epfl[dot]ch))
([homepage](http://google.com))

Please do not hesitate to contact us. We would be happy to help you run the code.

