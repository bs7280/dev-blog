---
id: 485mn6o4cjr3bzlpdssfwyz
title: Golf Wind Calculator
desc: ""
created: 1706293718479
updated: 1706293718479
---
Being obsessed with golf, and having unlimited access to several high end golf simulators, i've naturally spent a lot of time thinking how I can use my data-science and development experience to improve my golf game. Foresight golf simulators write all of their shot data to a nice JSON file, every time a shot is hit. This is great for data analytics, but for making some live training aids. 

## Loading and Visualizing Shot Data
To start, I made a [simple streamlit dashboard](https://fsx-golf-shot-viewer.streamlit.app/) that lets me see the dispersion pattern of each of my clubs. The important part here isn't just getting an average distance, which a lot of existing tools can do. Instead, I wanted to see the elliptical miss pattern. For righty golfers, a left shot goes longer and a right shot goes shorter (for the most part). So if I am playing a shot onto a green with water short and right, it means I need a longer club or really commit to a draw.

## Adding Wind 
For most golfers, we accept wind as this mostly unpredictable factor in our shots. A headwind will make the ball fly shorter, but how much? If I play a high ball, it will get knocked down a lot so I need to club up. Someone else map play a lower shot, and not need to club up on some holes. But for the most part, everyone just accepts the random nature of this problem.

But what if I could accurately predict exactly how much a given wind pattern will effect my shots? 

### Initial Work

I found some interesting starting points / projects that are good but intentionally take some shortcuts. Im able to compare a mathematically estimated ball flight vs real world data and have found a large margin of error for balls over ~200 yards. This is due to two factors
- Simple aerodynamic model
- Drag coefficients used on very out dated equipment

### Understanding the math

Helpful links:
- Symbols in air resistance math: https://www.ae.utexas.edu/courses/ase367k/Symbols.pdf

- Force lift
- Force Drag

Areas of model that need improvement
- Coefficient_Lift - Current a discrete mapping, needs to be a polynomial curve
- Reynolds Number - Constant number


### Calibrating to modern equipment

## Result