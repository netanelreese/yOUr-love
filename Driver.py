# Copyright 2021 Google LLC
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#    http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import flask
import google.auth

app = Flask(__name__)
_, PROJECT_ID = google.auth.default()
PARENT = 'projects/{}'.format(PROJECT_ID)

@app.route('/', methods=['GET', 'POST'])
def survey():
    return render_template('index.html', 
    """
    main handler - show form and possibly previous translation
    """

    # Flask Request object passed in for Cloud Functions
    # (use gcf_request for GCF but flask.request otherwise)
    #local_request = gcf_request if gcf_request else request

    # reset all variables (GET/POST)
    #text = translated = None

    # form submission and if there is data to process (POST)
    #if local_request.method == 'POST':
        #text = local_request.form['text'].strip()
        #if text:
            #data = {
                #'contents': [text],
                #'parent': PARENT,
                #'target_language_code': TARGET[0],
            #}
            # handle older call for backwards-compatibility
            #try:
                #rsp = TRANSLATE.translate_text(request=data)
            #except TypeError:
                #rsp = TRANSLATE.translate_text(**data)


    # create context & render template

    return render_template('index.html', **context)


if __name__ == '__main__':
    app.run(debug=False, threaded=True, host="localhost", port=8080)
    #import os
    #app.run(debug=True, threaded=True, host='0.0.0.0',
            #port=int(os.environ.get('PORT', 8080)))
