# Concepts

*For this project, we expect you to look at this concept:*

- [Job Search Resources](https://intranet.alxswe.com/concepts/100)

![Clean Up Your Portfolio Project](cleanup.gif)

## Let’s Clean Up

Of all the things that a potential employer looks at, code is the most important. It is after all, what they are hiring you to do. Also remember, Recruiters and Hiring Managers are busy people. Here is a real-world scenario that may help you understand how important your GitHub is to eventual job placement.

## Top of the Resumé Pile at DreamCo

Imagine this… You’re at a meetup and a friendly recruiter from DreamCo strikes up a conversation with you. He says there’s a software engineering position opening up in a few weeks and it would be great to keep in touch. You let him know you’ll follow up and send him a resume. That night you do a ton of research about DreamCo and tailor your resumé and email followup for the position. You get your resumé reviewed, iterate, and by the end of next day you confidently send him your latest draft. The Recruiter replies immediately – you’re a strong fit for the role.

Your resume is going to the top of the pile he will pass to the Hiring Manager. The Hiring Manager (your potential manager) receives a stack of 20 resumes (filtered down from the 2000 received), and she thinks you are a great candidate. She would love to speak with you. Right before she emails the recruiter to reach out to you, she finds your GitHub profile.

She randomly selects some projects and pokes around. She sees a checkin comment, “one more fix before bed” and thinks it’s not particularly professional, but at least it demonstrates diligence. She opens a random file and there are hardcoded strings being passed between functions to manage state. “That’s pretty poor coding hygiene, but style and standards can be taught. Maybe this is a one-off, ” the Manager thinks. Finally she finds a file where there is some more complex logic. Variables are poorly named, some functionality could have clearly been refactored, and one function named “addThemAllUp” spans 2 screens with 5 while loops and no comments to explain! She then flips to the next resumé on the stack.

## Tasks

### 0. Comment all your code

Go through and add comments to your code. The more, the better. If you’ve already done this, great! You have nothing more to do.

If you’re unclear about the standards for comments, look up what is expected. Here’s an [example from Digital Ocean](https://intranet.alxswe.com/rltoken/NKZdruo-0Mq8obOkarTy_A) detailing the standard commenting practices for Python 3.

### 1. Clean up those commit messages

Look through the history of your commits and view them from the perspective of a potential employer. Would you hire yourself? Are your commit messages clear and informative? Is there a way to edit a commit message on GitHub?

### 2. (Re)Organize your files

Clean up and remove any files that serve no purpose. This includes temp files, unused libraries, pycache, etc.

### 3. Refactor and Simplify

Are your functions/classes too big? Do they have too many responsibilities? Take time to refactor anything that may be unmanageable.

### 4. Spruce up variable names

One letter variables for anything besides temporary counters are unhelpful. Take the time to go through and update variable names to conform to convention and be descriptive.

### 5. Complete your README.md

The required task here is to improve your `README.md` to be complete. It should contain all standard aspects of a traditional `README.md` including:

- Project Name
- Introduction
	- Must include link to your deployed site, final project blog article, author(s) LinkedIn
- Installation
- Usage
- Contributing
- Related projects
- Licensing

A couple resources: * [What your code repository says about you](https://intranet.alxswe.com/rltoken/U9p-ykec7yt-EiAlPa0FhQ) * Here’s an [awesome list of READMEs](https://intranet.alxswe.com/rltoken/28TPP0t9tEUk73CEntOJyA).

At least one screenshot of your app must be included.

### 6. Optional: Include much more technical detail and incorporate your story into your `README.md`

Your portfolio project will **not** be the most technically impressive application that a recruiter or hiring manager sees. Bring context to the application by sharing your inspiration for creating this, or express the technical challenge you set out to solve. Be honest where you struggled and what you envision for a next-iteration. Add the emotion, the timeline, and a reminder of the human behind the keyboard so that your project is seen through the lens of “Wow, I’d like to work with a human who thinks like this!”

Pull from all your planning materials, your blog post, and project screenshots to create a `README.md` that stands out and tells the story of this project. This is a wonderful place to go into more technical depth than you did in your blog post. Really explain the details of the algorithm you chose, or the details of why you chose a specific solution. Add visuals (gifs, screenshots, emoji!) to bring the file to life!

Here are some examples of `README.md`‘s that tell a great story:

- [DeepFakes](https://github.com/deepfakes/faceswap)
- [WikiGraph](https://github.com/erabug/wikigraph)
- [Job Odyssey](https://intranet.alxswe.com/rltoken/oonQKOkl6uzdg0kIvO2vpg)
- [ideadog](https://intranet.alxswe.com/rltoken/CPOu_4-3K9Hs7KtJrccUgg)
