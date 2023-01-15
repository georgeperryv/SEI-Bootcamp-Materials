#!/bin/bash

repos=("10-3-HW""3rd-party-apis" "7-26-HW" "7-27-A-LAB" "7-27-B-LAB" "7-28-A-HW" "7-29-HW" "8-1-HW" "8-15-HW" "8-16-HW" "8-17-HW" "8-19-HW" "8-22-HW" "8-23-HW" "8-4-HW" "9-15-HW" "9-16-HW" "9-26-HW" "9-26-m" "9-27-HW" "9-30-HW-react-movies-submission" "9-6-HW" "9-7-HW" "9-8-A-HW" "9-9-in-class-lab" "capstone-issues" "class-work" "containers-and-functions" "daily-code-challenges" "dev-skills-lab-node-express" "django-code-along-day-01" "git-teams" "Heroku-MEN-Deployment" "Heroku-Signup" "into-to-express" "intro-dom-code-along" "Intro-to-DOM-events-code-along" "js-promises" "largest-number-js" "merge-conflicts" "mern-infrastructure" "mern-shopping-cart-complete" "MERN-Shopping-Cart-Part-1" "mongoose-embedding-related-data" "mongoose-movies-codealong" "mongoose-movies-oauth" "mongoose-referencing-related-data" "Netlify-Deploy" "p2-issues" "project-1-issues" "project-2" "project-3" "project-3-issue-tickets" "project-4" "python-classes" "python-intro" "react-intro" "react-shopping-cart" "rscc")

for repo in "${repos[@]}"; do
 git clone "git@git.generalassemb.ly:SEIR-7-25/${repo}.git"

done
