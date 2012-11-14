ForestWatchers: deforestation application
=========================================

This application will use the cleaned images by the volunteers from the
ForestWatchers project: timeline. 

The goal of this application is to allow actually the users to mark in the
cleaned tiles the deforested areas that they have found.

Requirements
============

In order to use this application you need to install **pybossa-client**:

```bash
    $ virtualenv env
    $ pip install pybossa-client
```

Usage
=====

In order to use this application you need to configure first the **timeline**
application and complete some tasks in a PyBossa server, otherwise this application 
will not create any task.

Once you have some tasks where you need to find deforestation, all you have to
do is to run this command:

```bash
    $ . env/bin/active
    $ python createTasks.py -k API-KEY -s YOURSERVER -c
```

Now you should have the application registered in your PyBossa server.

License
=======
GPLv3 see COPYING file.
