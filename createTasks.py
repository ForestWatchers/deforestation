#!/usr/bin/env python 
# -*- coding: utf-8 -*-

# Copyright (C) 2012 Citizen Cyberscience Centre
# 
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
# 
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
# 
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

from optparse import OptionParser
import pbclient
if __name__ == "__main__":
    # Arguments for the application
    usage = "usage: %prog [options]"
    parser = OptionParser(usage)
    
    parser.add_option("-s", "--url", dest="api_url", help="PyBossa URL http://domain.com/", metavar="URL")
    parser.add_option("-k", "--api-key", dest="api_key", help="PyBossa User API-KEY to interact with PyBossa", metavar="API-KEY")
    parser.add_option("-p", "--template", dest="template", help="PyBossa HTML+JS template for application presenter", metavar="TEMPLATE")
    parser.add_option("-b", "--tutorial", dest="tutorial", help="HTML tutorial for application", metavar="TUTORIAL")
    parser.add_option("-c", "--create", dest="create", action="store_true", 
                      help="Create the application",
                      metavar="CREATE-APP")

    parser.add_option("-u", "--update", dest="update", action="store_true", 
                      help="Update the templates of the application",
                      metavar="UPDATE-APP")

    parser.add_option("-v", "--verbose", action="store_true", dest="verbose")
    
    (options, args) = parser.parse_args()

    if not options.update:
        fw_client = pbclient
        fw_client.set('endpoint','http://forestwatchers.net/pybossa')
        fw_client.set('api_key', options.api_key)
        besttile = pbclient.find_app(short_name='besttile')[0]
        offset = 0
        limit = 100
        completed_tasks = pbclient.find_tasks(besttile.id, state="completed", offset=0,limit=200)


    if not options.api_url:
        options.api_url = 'http://localhost:5000'

    pbclient.set('endpoint', options.api_url)

    if not options.api_key:
        parser.error("You must supply an API-KEY to create an applicationa and tasks in PyBossa")
    else:
        pbclient.set('api_key', options.api_key)

    if not options.template:
        print("Using default template: template.html")
        options.template = "template.html"

    if not options.tutorial:
        print("Using default tutorial template: tutorial.html")
        options.tutorial= "tutorial.html"

    if (options.verbose):
       print('Running against PyBosssa instance at: %s' % options.api_url)
       print('Using API-KEY: %s' % options.api_key)

    if (options.create):
        app = pbclient.find_app(short_name='deforestedareas')
        if len(app)!=0 :
            pbclient.delete_app(app[0].id)
        pbclient.create_app('Deforestation', 'deforestedareas',
                            'Help us to find deforested areas in the forest')
        app = pbclient.find_app(short_name='deforestedareas')[0]
        print app.id
        app.long_description = open('long_description.html').read()
        app.info['task_presenter'] = open(options.template).read()
        app.info['thumbnail'] = "http://img204.imageshack.us/img204/6598/deforestation.png"
        app.info['tutorial'] = open(options.tutorial).read()
        pbclient.update_app(app)

        # Now add some tasks
        i = 0
        for t in completed_tasks:
            #maxVert, maxHor, minVert, minHor = map(float, tile.split(" "))
            #data = [minHor, minVert, maxHor, maxVert]
            #t = dict(question="Mark deforested areas in this tile",
            #        name=str(i),
            #        restrictedExtent=data,
            #        bounds=data,
            #        )
            t = dict(question="Mark deforested areas in this tile",
                    name=str(i),
                    restrictedExtent=t.info['tile']['restrictedExtent'],
                    bounds=t.info['tile']['bounds'])
            task_info=dict(tile=t)
            print task_info
            print app.id
            pbclient.create_task(app.id, task_info)

    if (options.update):
        app = pbclient.find_app(short_name='deforestedareas')[0]
        app.long_description = open('long_description.html').read()
        app.info['task_presenter'] = open(options.template).read()
        app.info['thumbnail'] = "http://img204.imageshack.us/img204/6598/deforestation.png"
        app.info['tutorial'] = open(options.tutorial).read()
        pbclient.update_app(app)

