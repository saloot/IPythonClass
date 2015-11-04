How to Make Slideshows Using IPython Notebooks
===================

IPython Notebooks can also be used to make slide shows. All you have to do is to follow a few simple steps and then render the presentation in your browser. Here's how it works.


Creating the Slides
--------
The slides are created in the same way that each block of code is created: using *cells*. To create a slide, simply select *slideshow* in the *Cell Toolbar* (see the figure below).
<br>
<img src="https://raw.githubusercontent.com/saloot/IPythonClass/master/Presentation/Figures/IPythonSlides1.png" style="border:2px solid #7C8082;width:450px;">
<br>
<br>

Then, select the appropriate cell type from the corresponding dropdown menu (we selected *Markdown* for the example below).
<br>
<img src="https://raw.githubusercontent.com/saloot/IPythonClass/master/Presentation/Figures/IPythonSlides2.png" style="border:2px solid #7C8082;width:450px;">
<br>
<br>

The result should like this
<br>
<img src="https://raw.githubusercontent.com/saloot/IPythonClass/master/Presentation/Figures/IPythonSlides3.png" style="border:2px solid #7C8082;width:500px;">
<br>
<br>

If you select *Markdown*, you can style your slides according to Markdown conventions or even use **HTML**.
<br>
<img src="https://raw.githubusercontent.com/saloot/IPythonClass/master/Presentation/Figures/IPythonSlides4.png" style="border:2px solid #7C8082;width:400px;">


Selecting Different Slide Types
----
Choosing

Rendering the Slides
--------
To render the slides, please open a "terminal" (in MAC OS/Linux) or "command prompt" (in Windows) and use *nbconvert* command as follows

  1. Go to the folder that contain your IPython Notebook (using the "cd" command)
  2. In the command line, type

`$ ipython nbconvert --to --to slides --post serve your_notebook_name`

This will open a browser with your slideshow running (as a result of the `--post serve` command option).

<br>

Custom Styling Using CSS
--------
If you are familiar with CSS (Cascading Style Sheets), you can easily change the style of your slides according to your own will.

To so so, simply add your styles to the file `custom.css` and put it in the same folder as the one your slides are in.


Learn More
--------
If you are curious to learn more about using IPython Notebooks for slideshows, please check out [this article](http://www.damian.oquanta.info/posts/make-your-slides-with-ipython.html) by Damian Avila.
Specifically, there is a slideshow embeded within the page which introduces different features of the slideshows with IPython Notebooks.

Also, you might be interested to see a [youtube video](https://www.youtube.com/embed/rBS6hmiK-H8) where he talks about preparing slides with IPython Notebooks.
<div>
<iframe width="600" height="400" src="https://www.youtube.com/embed/rBS6hmiK-H8" frameborder="0" allowfullscreen></iframe>
</div>

[![ScreenShot](https://raw.githubusercontent.com/saloot/IPythonClass/master/Presentation/Figures/IPYSlideYoutube.png)](https://www.youtube.com/embed/rBS6hmiK-H8)

Contact
-------
If you had any questions or problems, please do not hesitate to contact us!

Robin Scheible
([email](mailto:robin.scheibler@epfl.ch))
([homepage](http://lcav.epfl.ch/Robin_Scheibler))


Amir Hesam Salavati
([email](mailto:saloot@gmail.com))
([homepage](http://rr.epfl.ch/author/AmirHesamSalavati))

We would be happy to help!

