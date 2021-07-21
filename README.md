# ElSerpiente

<h1> Summary </h1>
This program was inspired by Ted Braun's work to visualize census data on race, income, and education level. Read his thorough write-up on that here:

https://github.com/TedBYanKei/Race_EducationLevel_Income#readme

Elsewhere he pondered how these same educational & salary groups would profile along male/female lines.  So I wrote a python program to do that.

<h1>Details and observations</h1>

Like Ted's R program described above, this program uses the census data as input.

What appears to be a proponderance of the observations (for some educational groups) at $100k is actually the $100k+ bracket. This degree of aggregation on the top end means the fidelity of the udnerlying data is not sufficient to understand the shape of the inequality in higher incomes. I have to wonder if it might be even worse than it looks - where male salaries dominate the ultra-high end of the scale (and have a profound influence on the mean salary as a result). 

I didn't take the time (yet) to subplot the histograms into a single larger plot, so I did that part manually to produce the .png below. But the rest is automated.

It was a fun learning exercise, but at the same time -- as the father of a young lady, a bit disappointing.

![image of histograms](https://github.com/jhstlr/ElSerpiente/blob/main/histograms.png)
