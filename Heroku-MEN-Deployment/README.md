# [Heroku](https://www.heroku.com/) MEN deployment Guide

## Heroku Setup
Before starting, make sure you have your Heroku Set up from the previous [guide]().

## Deploying an app:

### Create the App in your Heroku Dashboard

1. Go to your [Heroku Dashboard](https://dashboard.heroku.com/apps), and you'll see a list of all apps you have deployed with Heroku. Befor you can deploy a new app, you have to create the app in an initialized git repository. Let's do this with the CLI!
   - ```heroku create <optional-preferred-name-of-your-app>```

2. If you don't enter a specified name, Heroku will assign a randomly generated aoo name automatically (this can be changed later).

3. Remember that there are thousands of thousands of apps deployed with/through heroku, so you might have to get a little creative with your desired app name as it has to be unique to Heroku. (Pro tip: you can use hyphens ``-`` to help get your desired app name)

4. So if we run the command ``heroku create sei-students`` then we should see the following output:
   - ``` Creating ⬢ sei-students... done``` 
     ```https://sei-students.herokuapp.com/ | https://git.heroku.com/mongoose-flights\.git```
5. Verify that the command ran successfully with:
   - ``git remote -v``
6. The output should list should have a remote name ``heroku`` in the response. If not, repeat the steps with a different name that's not taken.

### Making sure the code is Commited to ``main``
1. Deploying to Heroku is super straightforward. You simply have to push the ``main`` branch to the remote named ``heroku``. So let's make sure our code is committed:
   ``git add .`` 
   ``git commit -m "deploy to heroku"``
2. Then push the repo to Heroku (NOT TO GITHUB):
   - ``git push heroku main``
   - This command will start the deployment on Heroku. 
3. The build and deploy process will take a few minutes for heroku to complete. While the app is deploying, you'll see messages from Heroku's servers prefaced by ``remote:`` and a successful deployment looks like this:
   - ``remote: -----> Build succeeded!1``
   - Then towards the end of the deployment:
   - ``remote: Verifying deploy... done.``
   - IF DEPLOYMENT FAILS: There will be error messages to help us track down how and why.

### Set your App's Environment Variables (if you're using a ``.env`` file)
1. You have to set each of your ``KEY=value`` pairs in your app's ``.env`` file on Heroku. So let's go to your [Heroku dashboard](https://dashboard.heroku.com/apps).
2. Click on the application that you need to add the ``.env`` ``KEY=value`` pairs to.

<img src="https://i.imgur.com/VGjSpLO.jpg">

3. When you're in the application's page, open "Settings", then click on the "Reveal Config Vars" button.

<img src="https://i.imgur.com/mDRQg2m.jpg">

4. Copy all of the Key=Value pairs from your local ``.env`` file to Heroku. If you're deploying an app with Google OAuth, make sure you change the ``GOOGLE_CALLBACK`` value on Heroku to:

``https://<your-app-name-here>.herokuapp.com/auth/google/oauth2callback``

<img src="https://i.imgur.com/1eEtdIK.jpg">

- AS A HEADS UP: The value of GOOGLE_CALLBACK in your local .env file should remain as ``https://localhost:3000/auth/google/oauth2callback``. If you were to change it to match your Heroku deployment, you would be redirected to your Heroku deployment every time you login while you're developing. This is NOT what you want.
- Also head over to your [Google Cloud Platform](https://console.cloud.google.com/apis/dashboard) dashboard and select "Credentials from the left side bar, choose the Client ID you're working with (the one linked to your project), and add the heroku OAuth callback url:

<img src="https://i.imgur.com/9UPUteH.jpg">

1. Add a new key/value pair in your ``.env`` at the top:
   - ``DATABASE_URL=............``
2. Go to your [MongoDB](https://www.mongodb.com/) page and click on the "Connect" button next to your database, choose the option of "Connect your Application".
3. Copy the string that displays, which should look like:
   - ``mongodb+srv://<username>:<password>@yourname-cluster.lr7ci.mongodb.net/myFirstDatabase?retryWrites=true&w=majority``
4. Add this code to your ``.env`` as the value to DATABASE_URL and change the username and password to your mongodb username and password for the database(not your login info) ``DATABASE_URL=mongodb+srv://<username>:<password>@nathan-cluster.lr7ci.mongodb.net/myFirstDatabase?retryWrites=true&w=majority``


5.  After adding the configuration, click on the button dropdown "More" in the top right, and click on "Restart all dynos"

<img src="https://i.imgur.com/hmODWGe.jpg">

### Final step
1. Browse to your app in the CLI, and once in the app's directory we can test our deployment! Enter this command in your terminal:
``heroku open``

### CONGRATS!
You have a deployed app to Heroku!

</br>

## Troubleshooting steps:
1. You can look at deployment messages, error messages, and the output in your terminal when running your app in development by using this command:
``heroku logs --tail``
2. More often than not, the biggest error is setting environment variables incorrectly. Run this command to log out a list of the variables set on HEROKU (not local):
``heroku config``
