# Flask issue on GitHub

**Behaviour experiencing**

User is running a Python Flask application and has implemented Raygun4Py. When the user tries to set the Raygun config, they get the following error:

`TypeError: Provider.__init__() got an unexpected keyword argument 'config'`

**Expected behaviour**

When this works, we are expecting the programme to run without error, and the config items set to take effect.

**Steps to reproduce**

You can pull down this repo that includes a Python test app set up with Flask and Raygun.

This test app has been set up with the `'filtered_keys'` config item being passed through the config object to the provider, but you could use any config item. This is what triggers the error.

You can follow the steps below to set up and run the test app.

## Python test app

**Project set up**

1. Pull down this repo.

3. Open a terminal in the route directory, install Flask by running `python -m pip install flask`.

4. _(Optional)_ Install python-dotenv by running `py -m pip install python-dotenv`.

2. _(Optional)_ Add `.env` file that contains your Raygun application API key.

5. Pull down the Raygun4Py repo to your computer. Checkout the branch that has the bugfix `ob/worm-51/update-python-middlewear`.

6. From the Raygun4Py route directory, run the command `python setup.py sdist` to build the Raygun4Py package.

7. Also from this route directory, you can run `python setup.py install`. This will install the local Raygun4Py package so that you can use it in your test app.

8. To check that the package has installed correctly, and is available to your project, got to the terminal in the route directory of your project, and run `python -m pip show raygun4py`.

9. To run your project, run `python app.py` from the route directory.

You can keep making local changes in the Raygun4Py repo and running the build/install steps to implement and test your changes. I'd recommend changing the version number each time just so you can keep track of which changes you're running. Can always switch back to the correct version before pushing up.