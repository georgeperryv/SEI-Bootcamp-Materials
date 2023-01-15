# [Heroku](https://www.heroku.com/) Install Guide

## Introduction: What is Heroku?

Heroku is another free and easy to use deployment method for web developement that supports a massive amount of features and tech stacks.

## Setup: Creating an account

1. Go to [The Heroku signup page](https://signup.heroku.com/). Fill out the signup with these fields, and add your email and name.
  <img src="https://i.imgur.com/Kyzf3lU.jpg">
2. OPTIONAL STEP: You can verify your account using a credit card, so that you get 1000 free dyno hours instead of 550, 100 free apps instead of 5, and the ability to use custom domain names. Heroku will NOT charge your card without your approval. If you're concerened but still want to verify, I would recommend using [Privacy](https://privacy.com/) to make a virtual card and set a limit of zero dollars on it or the minimum amount.

## Installing Heroku and running it from the CLI

#### Installation
1. The Heroku CLI makes it easy to create and manage apps in your Heroku account. Check to see if you have the Heroku cli installed with this command:
   1. `` heroku --version ``
2. If it's not installed, run these commands:
   1. Mac OSX: ``` brew tap heroku/brew && brew install heroku ```
   2. WSL for windows or Linux: ``` curl https://cli-assets.heroku.com/install.sh | sh ```

#### Log In
Once you've installed the Heroku CLI, type in ``` heroku login ``` in the terminal and follow the instructions. Use your Heroku account credentials to log in.

## Next Steps: 
[MEN stack deployment with Heroku](https://git.generalassemb.ly/SEI-Rancho-Cordova-3-21/Heroku-MEN-Deployment)
