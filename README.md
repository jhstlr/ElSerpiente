# ElSerpiente

<h1> Summary </h1>
This program was inspired by Ted Braun's work to visualize census data on race, income, and education level. Read his thorough write-up on that here:

https://github.com/TedBYanKei/Race_EducationLevel_Income#readme

Elsewhere he pondered how these same educational & salary groups would profile along male/female lines.  So I wrote a python program to do that.

<h1>Details and observations</h1>

Like Ted's R program described above, this program uses the census data as input.

I'd echo Ted's comments regarding the inefficient storage format, but the larger issue for me is the data granularity: bucketing the higher incomes into a single $100K bracket means the fidelity is not sufficient to understand the shape of the inequality in higher incomes.

I didn't take the time (yet) to subplot the histograms into a single larger plot, so I did that part manually to produce the .png below. But the rest is automated.

It was a fun learning exercise, but at the same time -- as the father of a young lady, a bit disappointing.

![image of histograms](https://github.com/jhstlr/ElSerpiente/blob/main/histograms.png)
