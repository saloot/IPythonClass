<h1>Getting Started With Python and Anaconda<br></h1><br>



<ol>


<li><a href="#python" title="Link: #python">Introduction</a><br></li>

<li><a href="#ana" title="Link: #ana">Anaconda</a><br></li>

<li><a href="#insana" title="Link: #ana">Installing Anaconda</a><br></li>

<ol>
<li><a href="#dl" title="Link: #dl">Downloading Anaconda</a><br></li>


<li><a href="#linux">Installation on Linux</a><br></li>


<li><a href="#win" title="Link: #win">Installation on Windows</a><br></li>


<li><a href="#mac" title="Link: #mac">Installation on Mac</a><br></li>


<li><a href="#spyder">Spyder</a><br></li>
</ol>

<li><a href="#start" title="Link: #start">Getting Started: Variables and Arrays</a><br></li>


<li><a href="#opera" title="Link: #opera">Matrix Operations</a><br></li>


<li><a href="#import" title="Link: #import">Importing Data</a><br></li>


<li><a href="#ipy">IPython</a><br></li>


<li><a href="#ipynb" title="Link: #ipynb">IPython Notebooks</a><br></li>

<li><a href="#func" title="Link: #func">Functions and Scripts</a><br></li>

<li><a href="#refe" title="Link: #refe">References</a></li>

</ol><br>



<a name="python" title="Link: null"></a>
<h1>1. Introduction<br></h1> Python is a very popular general-purpose language, with all the modern and classic constructs of a programming language that every software developer appreciates. This is what makes Python beneficial over MATLAB, besides the fact that it is not proprietary and various open source python distributions are freely and publicly available.


However, the very fact that Python is a general purpose language and not a software specific to scientific computing may be considered a drawback of it, too. To address this problem, several scientific computing packages (i.e. sets of function,classes,...) have been developed and released for it&nbsp;so far. These packages contain a large variety of functions which can solve everyday computational problems of researchers in many fields of&nbsp;engineering and science.


But the remaining problem is to find, install, maintain, manage updates and retain the consistency among all such packages as well as the Python system itself. This is&nbsp;where Anaconda comes in.




<a name="ana" title="Link: null"></a><h2>2. Anaconda</h2> Anaconda is a completely free Python distribution (i.e. set of packages) for scientific purposes, as stated in their website. It contains more than 125 Python packages for science, mathematics, engineering and data analysis.

Installing Anaconda will not only give you an out-of-the-box ready python system as well as a fully-featured IDE (Integrated Development Environment), but also it will release you from the burden of manually installing and taking care of dependency and consistency requirements between various packages.


<a name="insana" title="Link: null"></a><h1>Installing Anaconda</h1>
<a name="dl" title="Link: null"></a><h2>3. Downloading Anaconda</h2> To download the Anaconda, you can simply go to the link <a href="http://continuum.io/downloads" title="Link: http://continuum.io/downloads">http://continuum.io/downloads</a> and download the zip file compatible with your system. The download page looks like this:


<img title="Image: https://d396qusza40orc.cloudfront.net/dsp/img/dl.png" alt="window" src="https://d396qusza40orc.cloudfront.net/dsp/img/dl.png" width="600">


It may ask for your e-mail as well.&nbsp;Please note that the Python version Anaconda uses is Python 2.7.<br>


<a name="linux"></a><h2>4. Installation on Linux</h2> Installing Anaconda is pretty simple. On Linux-based systems, all you need to do is running the following command.



<div class="code"> bash Anaconda-1.x.x-Linux-x86[ 64].sh</div>

<br> No root access is required. However, you will need to manually add Python executable files to your Path environment if you want to run them from every folder. This can be done by adding the following line of code to your ~/.bashrc file:




<div class="code"> export PATH= /anaconda:$PATH</div>

<a name="win" title="Link: null"></a><h2>5. Installation on Windows</h2> Installing Anaconda on Windows should be easy. It is automatically added to Path. In case of any prospective problem, disabling your anti-virus can be a potential solution.

<img title="Image: https://d396qusza40orc.cloudfront.net/dsp/img/win.png" alt="window" src="https://d396qusza40orc.cloudfront.net/dsp/img/win.png" width="600">


<a name="mac" title="Link: null"></a><h2>6. Installation on Mac</h2> On MacOS, &nbsp;all you need to do is running the graphical installer. Anaconda will be automatically added to your path. However, in some cases an error message may appear at the installation time which is not a big deal. You can simply click <i>Install for me only&nbsp;</i>and go on.

<img title="Image: https://d396qusza40orc.cloudfront.net/dsp/img/osx.png" alt="window" src="https://d396qusza40orc.cloudfront.net/dsp/img/osx.png" width="600">

It seems to happens for older versions of OS X that the following error is generated when launching the&nbsp;ipython notebook (see </span><a href="#ipynb" title="Link: #ipynb">section 12</a>)
<div class="code">ValueError: unknown locale: UTF-8</div>

In that case, run the command <strong>locale</strong> in the terminal and inspect the value of the environment variable <code>LC_CTYPE</code>. It is probably just <code>UTF-8</code>.

Now open the file ~/.profile and add the following line
<div class="code">export LC_CTYPE='us_EN.UTF-8'
</div>

Then close the terminal session and try again. You might need to replace <code>us_EN</code> by a different value matching your system configuration.


<a name="spyder" title="Link: null"></a><h2>7. Spyder</h2>Spyder is a popular and very handy GUI for Python which is integrated in Anaconda by default. It is very similar to MATLAB's GUI meaning that&nbsp;if you have already worked with MATLB, you will not get lost in spyder. You can run the spyder using the following command in your command line:.
<div class="code">spyder</div><br/>




When you run the command above, the following screen appears.

<img title="Image: https://d396qusza40orc.cloudfront.net/dsp/img/spyder.png" alt="window" src="https://d396qusza40orc.cloudfront.net/dsp/img/spyder.png" width="600">

The <i>Console</i> window on the bottom right is where you type your commands and view possible results. The Object inspector window in top right shows the help manual available for functions you type in the console window. In the top bar of the application you can see and change your working directory. This is the default location in which spyder expects to find the files you read, the scripts you run,... &nbsp;.<br>

Finally, the <i>Editor</i> window in the left is where you create and edit your own functions. &nbsp;We will talk about functions later in this tutorial.<br>



<a name="start" title="Link: null"></a><h2>8. Getting Started: Variables and Arrays</h2> Variables are where you store your values and results of your operations. Despite some other programming languages, in Anaconda there is no need to define a variable or its type&nbsp;prior to using it. The most important variable type you will be working

with is the array type. Please note the very important fact that in Python, indices of an array start from zero. This is in contrast to some other systems (the most notable of them is MATLAB) in which arrays and matrices are indexed starting from one.

Initializing arrays is simple and can be done using the following commands, for example:
