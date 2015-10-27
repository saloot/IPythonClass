<h1>Getting Started With IPython Notebooks<br></h1><br>
This tutorial is a shorter version of the more complete one <a href="https://github.com/LCAV/SignalsOfTheDay/blob/master/Tutorial/Tutorial.ipynb"> here</a>, 
which was provided by <a href="http://lcav.epfl.ch">LCAV</a>.

<ul>


<li><a href="#python" title="Link: #python">Introduction</a><br></li>

<li><a href="#ana" title="Link: #ana">Anaconda</a><br></li>

<li><a href="#insana" title="Link: #ana">Installing Python and IPython Notebooks</a><br></li>

<ol>
<li><a href="#dl" title="Link: #dl">Downloading Anaconda</a><br></li>


<li><a href="#linux">Installation on Linux</a><br></li>


<li><a href="#win" title="Link: #win">Installation on Windows</a><br></li>

<li><a href="#mac" title="Link: #mac">Installation on Mac</a><br></li>

</ol>

<li><a href="#ipynb" title="Link: #ipynb">IPython Notebooks</a></li>
<li><a href="#github" title="Link: #ipynb">Working with Github</a></li>
<li><a href="#coursdownload" title="Link: #ipynb">Downloading Course Material</a></li>
<li><a href="#contatcs" title="Link: #ipynb">Contact Us</a></li>
</ul>

<a name="python" title="Link: null"></a>
<h1>Introduction<br></h1> Python is a very popular general-purpose language, with all the modern and classic constructs of a programming language that every software developer appreciates. This is what makes Python beneficial over MATLAB, besides the fact that it is not proprietary and various open source python distributions are freely and publicly available.


However, the very fact that Python is a general purpose language and not a software specific to scientific computing may be considered a drawback of it, too. To address this problem, several scientific computing packages (i.e. sets of function,classes,...) have been developed and released for it&nbsp;so far. These packages contain a large variety of functions which can solve everyday computational problems of researchers in many fields of&nbsp;engineering and science.


But the remaining problem is to find, install, maintain, manage updates and retain the consistency among all such packages as well as the Python system itself. This is&nbsp;where Anaconda comes in.




<a name="ana" title="Link: null"></a><h2>Anaconda</h2> Anaconda is a completely free Python distribution (i.e. set of packages) for scientific purposes, as stated in their website. It contains more than 125 Python packages for science, mathematics, engineering and data analysis.

Installing Anaconda will not only give you an out-of-the-box ready python system as well as a fully-featured IDE (Integrated Development Environment), but also it will release you from the burden of manually installing and taking care of dependency and consistency requirements between various packages.


<a name="insana" title="Link: null"></a><h1>Installing Python and IPython Notebooks</h1>
<a name="dl" title="Link: null"></a><h2>Downloading Anaconda</h2> To download the Anaconda, you can simply go to the link <a href="http://continuum.io/downloads" title="Link: http://continuum.io/downloads">http://continuum.io/downloads</a> and download the zip file compatible with your system. The download page looks like this:


<img title="Image: https://d396qusza40orc.cloudfront.net/dsp/img/dl.png" alt="window" src="https://d396qusza40orc.cloudfront.net/dsp/img/dl.png" width="600">


It may ask for your e-mail as well.&nbsp;Please note that the Python version Anaconda uses is Python 2.7.<br>


<a name="linux"></a><h2>Installation on Linux</h2> Installing Anaconda is pretty simple. On Linux-based systems, all you need to do is running the following command.



`$ bash Anaconda-1.x.x-Linux-x86[ 64].sh`

No root access is required. However, you will need to manually add Python executable files to your Path environment if you want to run them from every folder. This can be done by adding the following line of code to your ~/.bashrc file:


`export PATH= /anaconda:$PATH`

<a name="win" title="Link: null"></a><h2>Installation on Windows</h2> Installing Anaconda on Windows should be easy. It is automatically added to Path. In case of any prospective problem, disabling your anti-virus can be a potential solution.

<img title="Image: https://d396qusza40orc.cloudfront.net/dsp/img/win.png" alt="window" src="https://d396qusza40orc.cloudfront.net/dsp/img/win.png" width="600">


<a name="mac" title="Link: null"></a><h2>Installation on Mac</h2> On MacOS, &nbsp;all you need to do is running the graphical installer. Anaconda will be automatically added to your path. However, in some cases an error message may appear at the installation time which is not a big deal. You can simply click <i>Install for me only&nbsp;</i>and go on.

<img title="Image: https://d396qusza40orc.cloudfront.net/dsp/img/osx.png" alt="window" src="https://d396qusza40orc.cloudfront.net/dsp/img/osx.png" width="600">

It seems to happens for older versions of OS X that the following error is generated when launching the&nbsp;ipython notebook (see </span><a href="#ipynb" title="Link: #ipynb">section 12</a>)
<div class="code">ValueError: unknown locale: UTF-8</div>

In that case, run the command <strong>locale</strong> in the terminal and inspect the value of the environment variable <code>LC_CTYPE</code>. It is probably just <code>UTF-8</code>.

Now open the file ~/.profile and add the following line

`export LC_CTYPE='us_EN.UTF-8'`


Then close the terminal session and try again. You might need to replace <code>us_EN</code> by a different value matching your system configuration.

<a name="readmoreIPy" title="Link: null"></a><h2>Reading more about Python basics</h2>
If you are new to Python, you can start with some introdcutory online courses (such as [this one](https://www.udacity.com/course/programming-foundations-with-python--ud036)).

Alternatively, you might be interested in taking a look at [this tutorial](https://github.com/LCAV/SignalsOfTheDay/blob/master/Tutorial/Tutorial.ipynb), which was procided by [LCAV](http://lcav.epfl.ch) here at EPFL.


<a name="ipynb" title="Link: null"></a><h1>IPython Notebooks</h1>
IPython notebooks are very interesting novel features added to recent versions of IPython. Notebooks are interactive documents that allow running Python code and reading (or writing) notes and documentations <i>in the same place</i>. Therefore, one can not only see the results he is reading&nbsp;about, but also can produce different results by changing the documented code. <br><br>A notebook is actually an extended HTML file which contains specific markup to distinguish Python codes inside the page. When displayed using a custom web server, it allows interactive execution and editing of the code inside the document. However, it can also be viewed as a usual, nicely-formatted HTML page. The document you are currently reading is itself an IPython notebook.

The command to run the IPython Notebooks web server is the following:

`$ ipython notebook`

When you execute the command above, a new browser window is opened which shows the notebooks in the current folder. The IPython notebook files have the ".ipynb" extension.

<a name="readmoreIPy" title="Link: null"></a><h2>Reading more about IPython Notebooks</h2> 
There are a lot of notebooks available on the web which you can see and read. The GitHub repository available in <a href="https://github.com/ipython/ipython/wiki/A-gallery-of-interesting-IPython-Notebooks" title="Link: https://github.com/ipython/ipython/wiki/A-gallery-of-interesting-IPython-Notebooks">here</a>&nbsp;contains many useful and interesting ones. The source code of these notebooks is also available through the GitHub version control system.  
 
Another interesting source is the book "Python For Signal Processing" which is publicly available as a series of IPython notebooks available <a href="https://github.com/unpingco/Python-for-Signal-Processing" title="Link: https://github.com/unpingco/Python-for-Signal-Processing">at this address.<br>


<a name="github" title="Link: null"></a><h1>Working with Github</h1>
In this workshop, we are going to show you how you can publish the IPython Notebook for your paper onto *Github* and share it with your colleagues.
For those of you who are not familiar with how Github works, we have summarized a few helpful commands to get you started.

<a name="githubRepCreate" title="Link: null"></a><h2>Creating a Repository</h2>
A repository is a collection of files/folders where you store/share your code, data and paper body.
To create a repository, you can simply
<ol>
<li> <a href="https://github.com/login?return_to=%2Fjoin">Sign in</a> to your Github account (or <a href="https://github.com/join">signup</a> by creating an account)
<li> Once signed in, click on the "+" sign on top right of your screen (see the figure below) and select "New Reprository".
<img alt="Create a new repository on Github" src="https://documents.epfl.ch/users/s/sa/salavati/public/IPythonClassPhotos/CreateRepGithub.png" width="600">
</li>
<li> Select a name for your repository and click on "Create reprository".
<img alt="Create a new repository on Github" src="https://documents.epfl.ch/users/s/sa/salavati/public/IPythonClassPhotos/CreateRepGithubStep2.png" width="600">
</li>
<li>Congratulations! Once you see a screen like the one below you are done :) <b>Make sure to keep the URL specified in the figure below somewhere handy</b>.
We will need it shortly. Also, <b>do not close this window for now!</b>.
<img alt="Create a new repository on Github- Final step" src="https://documents.epfl.ch/users/s/sa/salavati/public/IPythonClassPhotos/CreateRepGithubStep3.png" width="600">
</ol>


<a name="githubRepPush" title="Link: null"></a><h2>Submitting Files to the Repository</h2>
<a name="githubRepPushMac" title="Link: null"></a><h4>Mac and Linux Users</h4>
Users that use Mac OS or Linux could use simple commands using terminal to submit your code.
<ul>
<li> Open a "Terminal" and navigate to the folder containg your codes (make sure you have some files in the folder). </li>
<li> Execute the following commands </li>
</ul>
    $ git init

    $ git add *

    $ git commit -m "first commit"

    $ git remote add origin the_url_to_your_repository

    $ git push -u origin master

Note that the "the_url_to_your_repository" is the same URL that you have "kept somewhere handy". Here's when we need it ;)

</ul>
<li> Congratulations! You have successfully submitted your code. To verify, go back to your web browser and navigate to your Github repository on the web. You should see a page like the one below.
<br>
<img alt="Create a new repository on Github- Final step" src="https://documents.epfl.ch/users/s/sa/salavati/public/IPythonClassPhotos/CreateRepGithubStep10.png" width="600">
</li>
</ul>

<a name="githubRepPushWin" title="Link: null"></a><h4>Windows Users</h4>
<ol>
<li> Donwload the Github client for Windows <a href="https://desktop.github.com/">from here</a> and install it.</li>
<li> After installation, in your browser, navigate to the Github page you saw in the <i>Step 4</i> above. Then, select <b>Setup in Dekstop (see figure below)</b>
<img alt="Create a new repository on Github- Final step" src="https://documents.epfl.ch/users/s/sa/salavati/public/IPythonClassPhotos/CreateRepGithubStep4.png" width="600">
</li>
<li> The browser will ask for permission to launch the Github application. Please allow it ;) 
<img alt="Create a new repository on Github- Final step" src="https://documents.epfl.ch/users/s/sa/salavati/public/IPythonClassPhotos/CreateRepGithubStep5.png" width="600">
</li>
<li> Once opened, navigate to the place you want your repository be on your hard drive and clik on <b>Clone</b>.
<img alt="Create a new repository on Github- Final step" src="https://documents.epfl.ch/users/s/sa/salavati/public/IPythonClassPhotos/CreateRepGithubStep6.png" width="600">
</li>
<li> You should now see a repository on the left panel in your Github application.
<img alt="Create a new repository on Github- Final step" src="https://documents.epfl.ch/users/s/sa/salavati/public/IPythonClassPhotos/CreateRepGithubStep7.png" width="600">
</li>
<li> On your hard drive, add your codes to the repository folder. Then, go back to the Github application and you should see that new changes have been found in your repository.
<img alt="Create a new repository on Github- Final step" src="https://documents.epfl.ch/users/s/sa/salavati/public/IPythonClassPhotos/CreateRepGithubStep8.png" width="600">
</li>
<li> At this point, add some comment to the "Summary" filed about what you changed and then click on <b>Commit and Sync master</b>.
<img alt="Create a new repository on Github- Final step" src="https://documents.epfl.ch/users/s/sa/salavati/public/IPythonClassPhotos/CreateRepGithubStep9.png" width="600">
</li>
<li> Congratulations! You have successfully submitted your code. To verify, go back to your web browser and navigate to your Github repository on the web. You should see a page like the one below.

<img alt="Create a new repository on Github- Final step" src="https://documents.epfl.ch/users/s/sa/salavati/public/IPythonClassPhotos/CreateRepGithubStep10.png" width="600">
</li>
<li>
Now, you can edit the code on your hard drive and submit it regularly (to backup and do version control) just like what we did above. Once finished, you can share the URL
of your repository with your colleagues and let them to enjoy your magnificent work as well :) Happy coding!
</li>
</ol>

<a name="githubRepPush" title="Link: null"></a><h2>Reading More About Using Git and Github</h2>

<a name="githubRepPush" title="Link: null"></a><h2>Reading More About Using Git and Github</h2>
Git and Github are twopowerful tools for backing up your code, do proper version control and share the code with your colleagues.
There are lots of very good tutorials on the web, from beginner to advanced.
<ul>
<li> <a href="https://help.github.com/articles/good-resources-for-learning-git-and-github/">A list of good resources</a> for learning Git and Github from Github website.</li>
<li> A simple <a href="https://guides.github.com/activities/hello-world/">Github "Hello World" Example</a></li>
<li> Nice introductory <a href="https://www.udacity.com/course/how-to-use-git-and-github--ud775">course on using Git and Github</a></li>
</ul>


<a name="coursdownload" title="Link: null"></a><h1>Downloading Course Material</h1>
You can simply click on the <b>Download ZIP</b> button on the right side of your screen, as shown in the figure below (of course there is the "Github way" as well but for now, this simpler solution should do the job ;) ).
<br>
<img alt="Download Course Materials" src="https://documents.epfl.ch/users/s/sa/salavati/public/IPythonClassPhotos/DownloadCourseMaterial.png" width="600">


<a name="contatcs" title="Link: null"></a><h1>Contacts</h1>
In case you had any trouble in the above steps or ANY questions or suggestions regarding the workshop, logistics, IPython, etc.
please do not hesitate to contact us (<a href="mailto:robin.scheibler@epfl.ch">Robin</a> or <a href="mailto:hesam.salavati@epfl.ch">Hesam</a>). We will be happy to help :) 